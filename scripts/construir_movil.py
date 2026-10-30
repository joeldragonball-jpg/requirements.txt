"""Genera docs/movil/data.json: los datos de la versión móvil del Cerebro (web instalable en docs/movil/).
Sin IA y sin claves. Solo recoge datos PÚBLICOS que ya están en el repo (nada de privado/) más el petróleo (Yahoo Finance)
y el cambio USD/EUR del BCE. Si una fuente falla se conserva el valor anterior de data.json.

Uso:  python scripts/construir_movil.py
En GitHub Actions lo ejecuta el workflow «Actualizar paneles de datos» tras scripts/actualizar_paneles.py."""
import ast
import csv
import io
import json
import re
import subprocess
import sys
import tomllib
import urllib.request
from datetime import date, datetime, timedelta, timezone, tzinfo
from pathlib import Path
from zoneinfo import ZoneInfo

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


def valoracion():
    """Cuadro de valoración sectorial (explorador/valoracion.json, lo escribe scripts/valoracion_sectorial.py)."""
    try:
        v = json.loads((RAIZ / "explorador" / "valoracion.json").read_text(encoding="utf-8"))
        cols = ("sector", "ticker", "precio", "cap_mm", "per", "ev_ebitda", "fcf_yield_pct", "periodo", "notas")
        return {"generado": v.get("generado", ""), "aviso": v.get("aviso", ""), "filas": [{k: x.get(k) for k in cols} for x in v.get("filas", [])]}
    except Exception:
        return {}


def lista_md(carpeta, n):
    rutas = sorted((r for r in (RAIZ / carpeta).glob("*.md") if re.match(r"\d{4}-\d{2}-\d{2}", r.name)), reverse=True)[:n]
    try:    # informes/research/tipos.json: lo que NO es análisis de mercado (auditorías, calendarios, glosarios…) sale con la etiqueta «Informe»
        no_analisis = set(json.loads((RAIZ / carpeta / "tipos.json").read_text(encoding="utf-8")).get("informe", []))
    except Exception:
        no_analisis = set()
    return [{"titulo": titulo_md(r), "fecha": r.stem[:10], "ruta": r.relative_to(RAIZ).as_posix(), "resumen": resumen_md(r),
             "tipo": "informe" if r.name in no_analisis else "analisis"} for r in rutas]


def cubre(titulo):
    """Rutina de research que cubre este evento (eventos/vinculos.json) o None."""
    try:
        reglas = json.loads((RAIZ / "eventos" / "vinculos.json").read_text(encoding="utf-8"))["reglas"]
    except Exception:
        return None
    minus = titulo.lower()
    for r in reglas:
        if any(p in minus for p in r["palabras"]):
            return {"rutina": r["rutina"], "que": r["que"]}
    return None


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
                        "impacto": e.get("impacto", "bajo"), "aprox": bool(e.get("aproximado")), "fuente": e.get("fuente", ""), "cubre": cubre(e["titulo"])})
    return out


def noticias(n=20):
    """Foto inicial de las noticias del bot (rama datos); la app las refresca sola al abrirse. Se omiten los textos que mencionan la cartera."""
    try:
        t = subprocess.run(["git", "show", "origin/datos:noticias/noticias.json"], capture_output=True, text=True, encoding="utf-8", cwd=RAIZ).stdout
        lista = json.loads(t)["noticias"]
    except Exception:
        return None
    lista = [x for x in lista if str(x.get("puntuacion", "0")).isdigit() and int(x["puntuacion"]) >= 7]
    for x in lista:   # las noticias manuales (C18) traen fecha_envio/fecha_noticia en vez de fecha
        x["fecha"] = x.get("fecha") or x.get("fecha_envio") or x.get("fecha_noticia") or ""
    lista.sort(key=lambda x: x["fecha"], reverse=True)
    limpio = lambda s: "" if re.search(r"cartera|tesis|tu XRP|tu XLM", s, re.I) else s
    return [{"titulo": x["titulo"], "resumen": limpio(x.get("resumen", "")), "por_que": limpio(x.get("por_que", "")), "tema": x["tema"], "nota": int(x["puntuacion"]),
             "fuente": x["fuente"], "fecha": x["fecha"][:16], "url": x["url"]} for x in lista[:n]]


def zona_madrid():
    """Europe/Madrid; en Windows sin el paquete tzdata, aproxima con la regla europea (UTC+1, UTC+2 del último domingo de marzo al de octubre)."""
    try:
        return ZoneInfo("Europe/Madrid")
    except Exception:
        class Madrid(tzinfo):
            def _ultimo_domingo(self, a, m):
                d = date(a, m, 31)
                return d.replace(day=31 - (d.weekday() + 1) % 7)

            def utcoffset(self, dt):
                a = dt.year
                ini = datetime.combine(self._ultimo_domingo(a, 3), datetime.min.time()) + timedelta(hours=2)
                fin = datetime.combine(self._ultimo_domingo(a, 10), datetime.min.time()) + timedelta(hours=3)
                return timedelta(hours=2 if ini <= dt.replace(tzinfo=None) < fin else 1)

            def dst(self, dt):
                return self.utcoffset(dt) - timedelta(hours=1)

            def fromutc(self, dt):
                u = dt.replace(tzinfo=None)
                return (u + timedelta(hours=1)).replace(tzinfo=self) if self.utcoffset(u + timedelta(hours=1)) == timedelta(hours=1)                     else (u + timedelta(hours=2)).replace(tzinfo=self)
        return Madrid()


def gasto_bot(dias=14):
    """Panel «Gasto del bot»: lee el registro `uso` (y `embudo`) de noticias.json en la rama datos. Solo cifras, sin secretos.
    Precios y topes salen de noticias/noticias.py y noticias/config.toml, para que cuadren con el propio bot."""
    t = subprocess.run(["git", "show", "origin/datos:noticias/noticias.json"], capture_output=True, text=True, encoding="utf-8", cwd=RAIZ).stdout
    db = json.loads(t)
    fuente = (RAIZ / "noticias" / "noticias.py").read_text(encoding="utf-8")
    precios = ast.literal_eval(re.search(r"PRECIOS_USD = (\{.*?\})", fuente, re.S).group(1))
    cfg = tomllib.loads((RAIZ / "noticias" / "config.toml").read_text(encoding="utf-8"))
    madrid = zona_madrid()

    def coste(u):
        p = next((v for k, v in precios.items() if str(u.get("modelo", "")).startswith(k)), precios["claude-sonnet-5-5"])
        return (u.get("entrada", 0) * p[0] + u.get("salida", 0) * p[1] + u.get("cache_lectura", 0) * p[2] + u.get("cache_escritura", 0) * p[3]) / 1e6

    modelo_corto = lambda m: "Haiku" if "haiku" in m else "Sonnet" if "sonnet" in m else "Opus" if "opus" in m else m
    por_dia, por_mes, por_origen, por_modelo = {}, {}, {}, {}
    hoy = datetime.now(madrid).date()
    for u in db.get("uso", []):
        f = datetime.fromisoformat(u["fecha"]).astimezone(madrid)
        c = coste(u)
        d = por_dia.setdefault(f.strftime("%Y-%m-%d"), {"total": 0.0, "llamadas": 0})
        d["total"] += c
        d["llamadas"] += 1
        por_mes[f.strftime("%Y-%m")] = por_mes.get(f.strftime("%Y-%m"), 0) + c
        if (hoy - f.date()).days < dias:
            por_origen[u.get("origen", "?")] = por_origen.get(u.get("origen", "?"), 0) + c
            por_modelo[modelo_corto(u.get("modelo", ""))] = por_modelo.get(modelo_corto(u.get("modelo", "")), 0) + c
    ultimos = sorted(por_dia)[-dias:]
    mes = hoy.strftime("%Y-%m")
    embudo = db.get("embudo", {})
    enviadas_dia = {}
    for n in db.get("noticias", []):
        k = datetime.fromisoformat(n["fecha_envio"]).astimezone(madrid).strftime("%Y-%m-%d")
        enviadas_dia[k] = enviadas_dia.get(k, 0) + 1
    r = lambda x: round(x, 3)
    return {
        "dias": [{"fecha": k, "usd": r(por_dia[k]["total"]), "llamadas": por_dia[k]["llamadas"]} for k in ultimos],
        "origen": {k: r(v) for k, v in sorted(por_origen.items(), key=lambda kv: -kv[1])},
        "modelo": {k: r(v) for k, v in sorted(por_modelo.items(), key=lambda kv: -kv[1])},
        "mes": {"clave": mes, "usd": r(por_mes.get(mes, 0)), "tope": cfg.get("tope_mensual_usd", 0)},
        "topes": {k: cfg.get(k, 0) for k in ("tope_mensual_usd", "tope_diario_usd", "max_llamadas_sonnet_dia", "max_alertas_urgentes_dia",
                                              "max_urgentes_dia", "max_noticias_dia", "max_tras_triaje", "nota_minima", "modelo_ahorro")},
        "embudo": [{"fecha": k, **embudo[k]} for k in sorted(embudo)[-7:]],
        "enviadas": [{"fecha": k, "n": enviadas_dia[k]} for k in sorted(enviadas_dia)[-7:]],
        "nota": "Solo cuenta las llamadas de este bot (noticias.json, rama datos). No incluye cerebro, revisión ni verificación mensual: la consola de Anthropic da más.",
    }


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


def datos_panel():
    """Pestaña Datos del móvil: deuda, calificaciones, reservas, stablecoins/RWA y tenedores de deuda de EE. UU. (compactado de explorador/)."""
    try:
        pn = cargar("explorador/paneles.json")
    except Exception:
        return {}
    sal = {}
    dd = pn.get("deuda") or {}
    if dd.get("paises"):
        anios = dd.get("anios", [])
        i26, i30 = (anios.index("2026") if "2026" in anios else None), (anios.index("2030") if "2030" in anios else None)
        sal["deuda"] = {"edicion": dd.get("edicion"), "nivel": "P", "fuente": "FMI, WEO",
                        "paises": [{"id": x["id"], "n": x["nombre"], "d": x["deuda"][i26], "s": x["saldo"][i26], "d30": x["deuda"][i30]} for x in dd["paises"] if i26 is not None and i30 is not None],
                        "rend": {k: {"v": v.get("valor"), "f": v.get("fecha")} for k, v in (dd.get("rendimientos") or {}).items()}}
    try:
        cal = cargar("explorador/calificaciones.json")
        sal["calif"] = {"leido": cal.get("leido"), "paises": [{k: x.get(k) for k in ("id", "nombre", "moody", "sp", "fitch", "otras", "nivel", "fuente", "nota")} for x in cal.get("paises", [])]}
    except Exception:
        pass
    try:
        res = cargar("explorador/reservas.json")
        sal["cofer"] = res.get("cofer")
    except Exception:
        pass
    st, rw, tic = pn.get("stablecoins") or {}, pn.get("rwa") or {}, pn.get("tic") or {}
    if st:
        sal["stable"] = {"total": st.get("total"), "n": st.get("n_activos"), "nivel": st.get("nivel"), "leido": st.get("leido"),
                         "top": [{k: x.get(k) for k in ("simbolo", "nombre", "usd", "cambio_7d", "cambio_30d")} for x in st.get("top", [])[:6]],
                         "xrpl": {"total": (st.get("xrpl") or {}).get("total"), "top": [{k: x.get(k) for k in ("simbolo", "usd")} for x in (st.get("xrpl") or {}).get("top", [])[:3]]}}
    if rw:
        sal["rwa"] = {"total": rw.get("total"), "n": rw.get("n"), "nivel": rw.get("nivel"), "stellar": rw.get("stellar"), "xrpl": rw.get("xrpl"),
                      "top": [{k: x.get(k) for k in ("nombre", "usd", "cambio_7d")} for x in rw.get("top", [])[:5]]}
    if tic.get("paises"):
        sal["tic"] = {"mes": tic["meses"][0], "mes0": tic["meses"][-1], "nivel": tic.get("nivel"), "total": tic["total"][0], "total0": tic["total"][-1],
                      "paises": [{"n": x["nombre"], "v": x["serie"][0], "v0": x["serie"][-1]} for x in tic["paises"][:8]]}
    return sal


def regulacion():
    """Radar regulatorio (explorador/regulacion.json) compactado para el móvil: una lista de temas por jurisdicción."""
    try:
        r = cargar("explorador/regulacion.json")
    except Exception:
        return {}

    def corta(t, n=260):
        t = (t or "").strip()
        if len(t) <= n:
            return t
        corte = t[:n].rsplit(". ", 1)[0]
        return (corte if len(corte) > 80 else t[:n].rsplit(" ", 1)[0]) + ("." if corte != t[:n].rsplit(" ", 1)[0] else "…")
    temas = {t["id"]: t["nombre"] for t in r.get("temas", [])}
    jurs = []
    for j in r.get("jurisdicciones", []):
        cel = [{"t": temas.get(c["tema"], c["tema"]), "e": c.get("etapa"), "txt": corta(c.get("estado")), "f": c.get("fecha"), "nv": c.get("nivel"), "u": c.get("url"), "px": c.get("proxima")}
               for c in r.get("celdas", []) if c["jur"] == j["id"]]
        if cel:
            jurs.append({"id": j["id"], "n": j["nombre"], "celdas": cel})
    return {"aviso": r.get("aviso"), "escala": r.get("escala"), "revisado": r.get("revisado"), "jurs": jurs}


def paises():
    """Una sola ficha por país (C60): política (C58), indicadores (C59) y estabilidad (C61), compactada para el móvil."""
    try:
        fich = cargar("explorador/paises.json")
        ind = {x["id"]: x["indicadores"] for x in cargar("explorador/paneles.json").get("indicadores", {}).get("paises", [])}
        est = {x["id"]: x for x in cargar("explorador/estabilidad.json").get("paises", [])}
    except Exception:
        return {}

    def fuente(url):
        return "Eurostat" if "eurostat" in (url or "") else "Banco Mundial" if "worldbank" in (url or "") else "FMI" if "imf.org" in (url or "") else (url or "")[:40]
    salida = []
    for f in fich.get("paises", []):
        i = f["id"]
        e = est.get(i, {})
        dims = {d: [{"n": c["nombre"], "v": c["valor"], "u": c["unidad"], "a": c["anio"], "f": fuente(c.get("fuente")), "nv": c.get("nivel"), "nota": c.get("nota", ""), "ant": c.get("anterior"), "anf": c.get("anterior_anio")} for c in v.get("cifras", [])] for d, v in e.get("dimensiones", {}).items()}
        hitos = [h for v in e.get("dimensiones", {}).values() for h in v.get("hitos", [])]
        salida.append({"id": i, "pais": f["pais"], "bloque": f["bloque"], "pol": {k: f.get(k) for k in ("sistema", "reparto_poder", "jefe_estado", "jefe_gobierno", "gobierno", "familia", "apoyo", "oposicion", "proxima_eleccion", "ultima_eleccion", "temas_clave", "sistemas_publicos", "lectura", "fuente", "nivel", "fecha_dato")},
                       "ind": {k: {"v": x.get("valor"), "u": x.get("unidad"), "f": x.get("fecha"), "nv": x.get("nivel"), "def": x.get("definicion"), "fu": fuente(x.get("fuente")), "per": x.get("periodicidad"), "ant": x.get("anterior"), "antf": x.get("anterior_fecha")} for k, x in ind.get(i, {}).items()},
                       "est": dims, "hitos": hitos, "lectura_est": e.get("lectura")})
    return {"nota": fich.get("nota"), "nota_est": cargar("explorador/estabilidad.json").get("nota"), "paises": salida,
            "informes": ["informes/research/2026-10-30-C58-fichas-politicas.md", "informes/research/2026-10-30-C59-indicadores.md", "informes/research/2026-10-30-C61-estabilidad.md"]}


def centro():
    """Plano del Centro (explorador/centro.json) con el informe más reciente de cada módulo y el recuento por estado."""
    plano = cargar("explorador/centro.json")
    sys.path.insert(0, str(RAIZ / "scripts"))
    from construir_seguimiento import cola_r
    colas = {t["id"]: t for t in cola_r()}
    salida = []
    for m in plano["modulos"]:
        archivos = sorted({a for patron in m.get("patron", []) for a in RAIZ.glob(patron)}, key=lambda a: a.name[:10])
        ultimo = None
        for a in reversed(archivos):
            if re.match(r"\d{4}-\d{2}-\d{2}", a.name):
                ultimo = {"fecha": a.name[:10], "titulo": titulo_md(a).split(" — lanzada")[0]}
                break
        estados = [e["estado"] for e in m["elementos"]]
        for e in m["elementos"]:   # estado vivo de la tarea de la cola (research/COLA.md) para no depender de lo escrito a mano aquí
            t = colas.get(e.get("tarea", ""))
            if t:
                e["tarea_estado"], e["tarea_detalle"] = t["estado"], t["detalle"][:160]
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
        "defensa": p.get("defensa", {}).get("paises", []), "liquidez": p.get("liquidez", {}), "inflacion": p.get("inflacion", {}).get("paises", []), "ormuz": p.get("ormuz", {}), "hitos_petroleo": cargar("explorador/hitos_petroleo.json"), "elecciones": cargar("explorador/elecciones.json"), "paises": paises(), "regulacion": regulacion(), "datos": datos_panel(),
        "valoracion": valoracion(),
        "bonos": [{"id": k, "valor": bonos[k]["plazos"].get("10A"), "fecha": bonos[k]["fecha"]} for k in ("USA", "JPN", "EUR", "ESP", "FRA", "GBR") if k in bonos],
        "eventos": eventos(), "voces": voces(), "niveles": cargar("explorador/voces.json").get("niveles", {}),
        "informes": lista_md("informes", 6), "investigacion": lista_md("informes/research", 8), "videos": lista_md("informes/videos", 6), "centro": centro(),
    }
    fallos = []
    for clave, funcion in (("eur", cambio_euro), ("petroleo", petroleo), ("noticias", noticias), ("gasto", gasto_bot)):
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
