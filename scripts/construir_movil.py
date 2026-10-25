"""Genera docs/movil/data.json: los datos de la versión móvil del Cerebro (web instalable en docs/movil/).
Sin IA y sin claves. Solo recoge datos PÚBLICOS que ya están en el repo (nada de privado/) más el petróleo (Yahoo Finance)
y el cambio USD/EUR del BCE. Si una fuente falla se conserva el valor anterior de data.json.

Uso:  python scripts/construir_movil.py
En GitHub Actions lo ejecuta el workflow «Actualizar paneles de datos» tras scripts/actualizar_paneles.py."""
import csv
import io
import json
import re
import subprocess
import sys
import tomllib
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "docs" / "movil" / "data.json"
URL_YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/{s}?range=5d&interval=1d"
URL_BCE = "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?lastNObservations=1&format=csvdata"
PETROLEO = (("brent", "BZ=F", "Brent"), ("wti", "CL=F", "WTI (crudo de EE. UU.)"))


def descargar(url):
    peticion = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(peticion, timeout=40) as r:
        return r.read().decode("utf-8", errors="replace")


def cargar(ruta):
    return json.loads((RAIZ / ruta).read_text(encoding="utf-8"))


def limpiar(t):
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    return re.sub(r"\s+", " ", re.sub(r"[*_`>#]+", "", t)).strip()


def titulo_md(ruta):
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if linea.startswith("# "):
            return linea[2:].strip()
    return ruta.stem


def resumen_md(ruta, maximo=380):
    """Primeras líneas del apartado «Resumen» (o del primer párrafo con texto) del informe."""
    lineas = ruta.read_text(encoding="utf-8").splitlines()
    inicio = next((i + 1 for i, l in enumerate(lineas) if re.match(r"^##\s+Resumen", l)), None)
    if inicio is None:
        inicio = next((i + 1 for i, l in enumerate(lineas) if l.startswith("# ")), 0)
    partes = []
    for l in lineas[inicio:]:
        if l.startswith("## ") and partes:
            break
        t = limpiar(l)
        if not t or t.startswith(("---", "|", "Modo:", "Marca de lectura")) or re.match(r"^(tema|etiquetas|actualizado):", t):
            continue
        partes.append(t)
        if sum(len(x) for x in partes) > maximo:
            break
    texto = " ".join(partes)
    return texto[:maximo].rsplit(" ", 1)[0] + "…" if len(texto) > maximo else texto


def lista_md(carpeta, n):
    rutas = sorted((r for r in (RAIZ / carpeta).glob("*.md") if re.match(r"\d{4}-\d{2}-\d{2}", r.name)), reverse=True)[:n]
    return [{"titulo": titulo_md(r), "fecha": r.stem[:10], "ruta": r.relative_to(RAIZ).as_posix(), "resumen": resumen_md(r)} for r in rutas]


def eventos(dias=150):
    with open(RAIZ / "eventos" / "calendario.toml", "rb") as f:
        evs = tomllib.load(f)["eventos"]
    hoy = date.today()
    out = []
    for e in sorted(evs, key=lambda e: e["fecha"]):
        try:
            d = date.fromisoformat(e["fecha"])
        except ValueError:
            continue
        fin = date.fromisoformat(e["hasta"]) if e.get("hasta") else d
        if fin >= hoy and (d - hoy).days <= dias:
            out.append({"fecha": e["fecha"], "hasta": e.get("hasta"), "titulo": e["titulo"], "detalle": e.get("detalle", ""),
                        "impacto": e.get("impacto", "bajo"), "aprox": bool(e.get("aproximado")), "fuente": e.get("fuente", "")})
    return out


def noticias(n=20):
    """Foto inicial de las noticias del bot (rama datos); la app las refresca sola al abrirse. Se omiten los textos que mencionan la cartera."""
    try:
        t = subprocess.run(["git", "show", "origin/datos:noticias/noticias.json"], capture_output=True, text=True, encoding="utf-8", cwd=RAIZ).stdout
        lista = json.loads(t)["noticias"]
    except Exception:
        return None
    lista = [x for x in lista if str(x.get("puntuacion", "0")).isdigit() and int(x["puntuacion"]) >= 7]
    lista.sort(key=lambda x: x["fecha"], reverse=True)
    limpio = lambda s: "" if re.search(r"cartera|tesis|tu XRP|tu XLM", s, re.I) else s
    return [{"titulo": x["titulo"], "resumen": limpio(x.get("resumen", "")), "por_que": limpio(x.get("por_que", "")), "tema": x["tema"], "nota": int(x["puntuacion"]),
             "fuente": x["fuente"], "fecha": x["fecha"][:16], "url": x["url"]} for x in lista[:n]]


def voces(n=20):
    v = cargar("explorador/voces.json")
    lista = v["voces"] if isinstance(v, dict) else v
    return [{"quien": x["quien"], "texto": x["texto"], "nivel": x["nivel"], "conf": x["conf"], "cuando": x.get("cuando", ""),
             "fuente": x.get("fuente"), "video": x.get("video"), "plazo": x.get("plazo"), "nota": x.get("nota", "")} for x in lista[:n]]


def cambio_euro():
    fila = list(csv.DictReader(io.StringIO(descargar(URL_BCE))))[-1]
    return {"tipo": float(fila["OBS_VALUE"]), "fecha": fila["TIME_PERIOD"], "fuente": "BCE"}


def petroleo():
    salida = {}
    for clave, simbolo, nombre in PETROLEO:
        d = json.loads(descargar(URL_YAHOO.format(s=urllib.request.quote(simbolo))))["chart"]["result"][0]
        pares = [(datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%d"), c) for t, c in zip(d["timestamp"], d["indicators"]["quote"][0]["close"]) if c]
        (f0, c0), (f1, c1) = pares[-2], pares[-1]
        salida[clave] = {"nombre": nombre, "valor": round(c1, 2), "cambio_1d": round((c1 / c0 - 1) * 100, 2), "fecha": f1, "moneda": "USD"}
    return salida


def centro():
    """Plano del Centro (explorador/centro.json) con el informe más reciente de cada módulo y el recuento por estado."""
    plano = cargar("explorador/centro.json")
    salida = []
    for m in plano["modulos"]:
        archivos = sorted({a for patron in m.get("patron", []) for a in RAIZ.glob(patron)}, key=lambda a: a.name[:10])
        ultimo = None
        for a in reversed(archivos):
            if re.match(r"\d{4}-\d{2}-\d{2}", a.name):
                ultimo = {"fecha": a.name[:10], "titulo": titulo_md(a).split(" — lanzada")[0]}
                break
        estados = [e["estado"] for e in m["elementos"]]
        salida.append({"id": m["id"], "nombre": m["nombre"], "apodo": m["apodo"], "color": m["color"], "resumen": m["resumen"],
                       "elementos": m["elementos"], "ultimo": ultimo, "n": {k: estados.count(k) for k in ("hecho", "parcial", "falta")}})
    return salida


def main():
    previo = {}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        except Exception:
            previo = {}
    p = cargar("explorador/paneles.json")
    bonos = {q["id"]: q for q in p.get("bonos", {}).get("paises", [])}
    datos = {
        "generado": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "leido": p.get("leido"),
        "mercado": p.get("mercado", {}).get("activos", []), "indices": p.get("indices", {}).get("indices", []),
        "tipos": p.get("tipos_vivos", {}).get("paises", []), "tipos_bis": p.get("tipos_bis", {}).get("paises", []),
        "watchlist": p.get("watchlist", {}).get("valores", []),
        "defensa": p.get("defensa", {}).get("paises", []), "liquidez": p.get("liquidez", {}), "ormuz": p.get("ormuz", {}),
        "bonos": [{"id": k, "valor": bonos[k]["plazos"].get("10A"), "fecha": bonos[k]["fecha"]} for k in ("USA", "JPN", "EUR", "ESP", "FRA", "GBR") if k in bonos],
        "eventos": eventos(), "voces": voces(), "niveles": cargar("explorador/voces.json").get("niveles", {}),
        "informes": lista_md("informes", 6), "investigacion": lista_md("informes/research", 8), "videos": lista_md("informes/videos", 6), "centro": centro(),
    }
    fallos = []
    for clave, funcion in (("eur", cambio_euro), ("petroleo", petroleo), ("noticias", noticias)):
        try:
            valor = funcion()
            if valor is None:
                raise ValueError("sin datos")
            datos[clave] = valor
        except Exception as e:
            fallos.append(f"{clave}: {type(e).__name__}: {e}")
            if clave in previo:
                datos[clave] = previo[clave]
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(datos, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"data.json: {len(datos['eventos'])} eventos, {len(datos.get('noticias') or [])} noticias, {len(datos['voces'])} voces, "
          f"petróleo {', '.join(f'{k} {v['valor']}' for k, v in datos.get('petroleo', {}).items())}, USD/EUR {datos.get('eur', {}).get('tipo')}")
    for f in fallos:
        print("AVISO (se conserva lo anterior si existía):", f)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
