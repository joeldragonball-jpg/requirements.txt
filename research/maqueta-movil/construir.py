"""Genera maqueta.html (maqueta de la versión móvil) con datos PÚBLICOS ya existentes del repo. Sin IA, sin red, sin claves.
No lee nada de privado/. Uso: python research/maqueta-movil/construir.py"""
import json
import re
import subprocess
import tomllib
import csv
import io
import urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
AQUI = Path(__file__).parent
HOY = date.today()


def cargar(ruta):
    return json.loads((RAIZ / ruta).read_text(encoding="utf-8"))


def titulo_md(ruta):
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if linea.startswith("# "):
            return linea[2:].strip()
    return ruta.stem


def limpiar(t):
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    return re.sub(r"\s+", " ", re.sub(r"[*_`>#]+", "", t)).strip()


def resumen_md(ruta, maximo=420):
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


def cambio_euro():
    """USD por 1 EUR: tipo de referencia del BCE (fuente oficial). Si falla, la maqueta se queda en dólares."""
    try:
        url = "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?lastNObservations=1&format=csvdata"
        t = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read().decode("utf-8")
        fila = list(csv.DictReader(io.StringIO(t)))[-1]
        return {"tipo": float(fila["OBS_VALUE"]), "fecha": fila["TIME_PERIOD"]}
    except Exception:
        return None


def eventos(n):
    with open(RAIZ / "eventos" / "calendario.toml", "rb") as f:
        evs = tomllib.load(f)["eventos"]
    futuros = [e for e in evs if e["fecha"] >= HOY.isoformat()]
    futuros.sort(key=lambda e: e["fecha"])
    return [{"fecha": e["fecha"], "hasta": e.get("hasta"), "titulo": e["titulo"], "detalle": e.get("detalle", ""), "impacto": e.get("impacto", "bajo"),
             "aprox": bool(e.get("aproximado")), "fuente": e.get("fuente", "")} for e in futuros[:n]]


def noticias(n):
    try:
        t = subprocess.run(["git", "show", "origin/datos:noticias/noticias.json"], capture_output=True, text=True, encoding="utf-8", cwd=RAIZ).stdout
        lista = json.loads(t)["noticias"]
    except Exception:
        return []
    lista = [x for x in lista if str(x.get("puntuacion", "0")).isdigit() and int(x["puntuacion"]) >= 7]
    lista.sort(key=lambda x: x["fecha"], reverse=True)
    limpio = lambda t: "" if re.search(r"cartera|tu XRP|tu XLM|tus XRP|tus XLM", t, re.I) else t   # el bot a veces menciona el peso de la cartera: no se publica
    return [{"titulo": x["titulo"], "resumen": limpio(x.get("resumen", "")), "por_que": limpio(x.get("por_que", "")), "tema": x["tema"], "nota": int(x["puntuacion"]),
             "fuente": x["fuente"], "fecha": x["fecha"][:16], "url": x["url"]} for x in lista[:n]]


def voces(n):
    v = cargar("explorador/voces.json")
    lista = v["voces"] if isinstance(v, dict) else v
    return [{"quien": x["quien"], "texto": x["texto"], "nivel": x["nivel"], "conf": x["conf"], "cuando": x.get("cuando", ""),
             "fuente": x.get("fuente"), "video": x.get("video"), "plazo": x.get("plazo"), "nota": x.get("nota", "")} for x in lista[:n]]


def main():
    p = cargar("explorador/paneles.json")
    bonos = {q["id"]: q for q in p.get("bonos", {}).get("paises", [])}
    datos = {
        "hoy": HOY.isoformat(), "leido": p.get("leido"),
        "mercado": p.get("mercado", {}).get("activos", []), "indices": p.get("indices", {}).get("indices", []),
        "tipos": p.get("tipos_vivos", {}).get("paises", []),
        "bonos": [{"id": k, "valor": bonos[k]["plazos"].get("10A"), "fecha": bonos[k]["fecha"]} for k in ("USA", "JPN", "EUR", "ESP", "FRA", "GBR") if k in bonos],
        "eventos": eventos(14), "noticias": noticias(14), "voces": voces(20), "eur": cambio_euro(),
        "niveles": cargar("explorador/voces.json").get("niveles", {}),
        "informes": lista_md("informes", 6), "investigacion": lista_md("informes/research", 8), "videos": lista_md("informes/videos", 6),
    }
    plantilla = (AQUI / "plantilla.html").read_text(encoding="utf-8")
    texto = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")
    (AQUI / "maqueta.html").write_text(plantilla.replace("__DATOS__", texto), encoding="utf-8")
    print("maqueta.html generada:", len(datos["eventos"]), "eventos,", len(datos["noticias"]), "noticias,", len(datos["voces"]), "voces")


if __name__ == "__main__":
    main()
