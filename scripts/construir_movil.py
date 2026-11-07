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

sys.path.insert(0, str(Path(__file__).resolve().parent))
import yahoo_diario  # noqa: E402

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


MONEDA_INDICE = {"^STOXX50E": "EUR", "^IBEX": "EUR", "^GDAXI": "EUR", "^N225": "JPY", "^HSI": "HKD", "000001.SS": "CNY", "^KS11": "KRW"}


def verificados():
    """C153: estado de contraste (confirmado, dudoso, desmentido) de titulares ya revisados (eventos/verificados.json) para etiquetar las noticias en la app."""
    try:
        d = json.loads((RAIZ / "eventos" / "verificados.json").read_text(encoding="utf-8"))
    except Exception:
        return []
    return [{"c": e["contiene"], "estado": e["estado"], "con": (e.get("con") or "")[:220], "url": e.get("url", "")} for e in d.get("eventos", []) if e.get("contiene") and e.get("estado")]


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
        pares = yahoo_diario.cierres(d)   # fecha de la sesión en hora de la bolsa, no la de la descarga (C132)
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
    ep, al, ch = pn.get("energia_precios") or {}, pn.get("alimentos") or {}, pn.get("chips") or {}
    if ep.get("omie_diario"):
        pv = {x["fecha"]: x["media"] for x in ep.get("pvpc_diario", [])}
        sal["luz"] = {"nivel": ep.get("nivel"), "leido": ep.get("leido"),
                      "dias": [{"f": x["fecha"], "m": x["media"], "a": x["min"], "b": x["max"], "p": pv.get(x["fecha"])} for x in ep["omie_diario"][-7:]],
                      "tarifas": [{"k": k, "n": (ep.get("eurostat") or {}).get(k, {}).get("nombre"), "p": [{"n": y["pais"], "v": y["eur_kwh"], "v0": y.get("anterior_eur_kwh"), "t": y["periodo"]} for y in (ep.get("eurostat") or {}).get(k, {}).get("paises", [])]} for k in ("hogares", "empresas") if (ep.get("eurostat") or {}).get(k)]}
    if al.get("fao") or al.get("fred") or al.get("futuros"):
        sal["comida"] = {"nivel": al.get("nivel"), "leido": al.get("leido"), "mes": (al.get("fao") or {}).get("mes"),
                         "fao": [{k: x.get(k) for k in ("nombre", "valor", "interanual")} for x in (al.get("fao") or {}).get("indices", [])],
                         "fred": [{k: x.get(k) for k in ("nombre", "valor", "unidad", "fecha", "interanual")} for x in al.get("fred", [])],
                         "fut": [{k: x.get(k) for k in ("nombre", "valor", "unidad", "cambio_1m")} for x in al.get("futuros", [])]}
    if ch.get("produccion") or ch.get("cotizaciones"):
        sal["chips"] = {"nivel": ch.get("nivel"), "leido": ch.get("leido"),
                        "prod": [{k: x.get(k) for k in ("nombre", "valor", "fecha", "interanual")} for x in ch.get("produccion", [])],
                        "cot": [{k: x.get(k) for k in ("nombre", "simbolo", "valor", "cambio_1d", "cambio_1m")} for x in ch.get("cotizaciones", [])]}
    try:
        pg, mo, se = cargar("explorador/espana-pagos.json"), cargar("explorador/espana-mortalidad.json"), cargar("explorador/seguridad-eurostat.json")
    except Exception:
        pg = mo = se = None
    if pg and pg.get("bdns"):
        sal["pagos"] = {"nivel": pg.get("nivel"), "leido": pg.get("leido"), "nota": pg.get("nota"),
                        "dias": [{"f": x["fecha"], "t": x["total"], "n": x.get("por_nivel", {})} for x in pg["bdns"].get("dias", [])[-7:]],
                        "placsp": (pg.get("placsp") or {}).get("entradas_feed")}
    if mo and mo.get("semanas"):
        sal["muertes"] = {"nivel": mo.get("nivel"), "leido": mo.get("leido"), "nota": mo.get("nota"), "res": mo.get("resumen_anio_en_curso"),
                          "sem": [{k: x.get(k) for k in ("anio", "semana", "defunciones", "exceso_vs_2015_2019", "tipo_dato")} for x in mo["semanas"][-8:]]}
    if se:
        es = next((p for p in (se.get("delitos") or {}).get("paises", []) if p.get("id") == "ES"), None)
        sal["seg"] = {"leido": se.get("leido"), "aviso": (se.get("delitos") or {}).get("aviso"),
                      "via": {"nivel": (se.get("carretera") or {}).get("nivel"), "p": [{k: x.get(k) for k in ("pais", "anio", "muertes", "por_millon_hab")} for x in (se.get("carretera") or {}).get("paises", [])]},
                      "del": [{"n": v["delito"], "a": v["anio"], "v": v["registrados"], "v0": v["serie"].get(str(int(v["anio"]) - 5))} for v in ((es or {}).get("delitos") or {}).values()],
                      "nota": (es or {}).get("nota_definicion")}
    es = espana()
    if es:
        sal["espana"] = es
    return sal


def espana():
    """Tarjetas de España del móvil: ministerios, programas, beneficiarios y fiscal (explorador/espana*.json)."""
    try:
        b = cargar("explorador/espana-presupuesto.json")
        e = cargar("explorador/espana.json")
    except Exception:
        return None
    m = e.get("manual", {})
    dato = lambda x: {"n": x["nombre"], "v": x.get("valor"), "u": x.get("unidad"), "a": x.get("anio"), "niv": x.get("nivel"), "nota": x.get("nota")}
    fiscal = []
    for i in e.get("indicadores", []):
        if i["id"] in ("ingresos", "gasto", "imp_renta", "imp_produccion", "cotizaciones", "f_proteccion", "f_sanidad", "f_educacion", "f_defensa", "f_intereses"):
            a = sorted(i["serie"])
            fiscal.append({"n": i["nombre"].replace("·", "").strip(), "a": a[-1], "v": i["serie"][a[-1]], "v0": i["serie"][a[-2]], "pib": i.get("pct_pib", {}).get(a[-1])})
    cm, fm, pp, cp = b.get("capitulos_por_ministerio", {}), b.get("fuera_de_ministerios", {}), b.get("personal_publico", {}), b.get("cargos_politicos", {})
    detalle = {
        "ley": cm.get("leyenda"), "nota": cm.get("nota"),
        "sec": [{"n": s["seccion"], "t": s["total"], "p": s["pct_total_estado"], "h": s["por_habitante"], "c": {k: v for k, v in s["capitulos"].items() if v}, "pr": s["programas"][:6],
                 "ce": [{"n": c["n"], "o": c["o"]} for c in s["centros"][:6]], "de": s["destino"], "tr": [{"n": x["n"][:110], "d": x["dest"], "o": x["o"]} for x in s["transf_mayores"][:3]],
                 "ac": s["altos_cargos"]["obligaciones"], "ev": s["eventuales"]["obligaciones"]} for s in cm.get("secciones", []) if s["total"]],
        "ret": [dato(x) for x in cm.get("retribuciones", [])], "num_ac": dato(cm["altos_cargos_numero"]) if cm else None,
    } if cm else None
    fuera = {"ss": [dato(x) for x in fm["seguridad_social"]["datos"]], "org": [{"n": x["nombre"], "o": x["obligaciones_2025"], "h": x["por_habitante"], "nota": x["nota"]} for x in fm["organismos"]["lista"]],
             "sin": [dato(x) for x in fm["organismos"]["sin_dato"]], "adm": fm["administraciones_2024"], "par": dato(fm["parlamentos_autonomicos"]), "iue": [dato(x) for x in fm["intereses_y_ue"]]} if fm else None
    personal = {"ef": pp["efectivos"], "epa": pp["epa"], "rem": pp["remuneracion"], "ue": pp["comparativa_ue"]} if pp else None
    cargos = {"num": [dato(x) for x in cp["numero"]], "ret": [dato(x) for x in cp["retribuciones"]], "par": [dato(x) for x in cp["partidos"]], "suma": cp["suma_publicada"]} if cp else None
    return {"detalle": detalle, "fuera": fuera, "personal": personal, "cargos": cargos, "leido": b.get("leido"), "vigencia": b["vigencia"]["texto"], "lecturas": b.get("lecturas", {}), "como": b.get("como_leerlo", []),
            "total": b.get("totales"), "no_aislable": [{"t": x["tema"], "x": x["texto"], "niv": x["nivel"]} for x in b.get("no_aislable", [])],
            "minist": [{"n": x["nombre"], "i": x["inicial_2025"], "o": x["obligaciones_2025"], "o26": x["obligaciones_2026_ago"]} for x in sorted((s for s in b["secciones"] if s["tipo"] == "ministerio"), key=lambda s: -s["obligaciones_2025"])],
            "prog": [{"g": x["grupo"], "n": x["nombre"], "i": x["inicial_2025"], "o": x["obligaciones_2025"], "nota": x.get("nota")} for x in b["programas"]],
            "pob": [dato(x) for x in m.get("poblacion_referencia", [])], "benef": [dato(x) for x in m.get("beneficiarios", [])],
            "req": [{"n": x["nombre"], "x": x["nota"]} for x in m.get("requisitos_acceso", [])], "vg": [dato(x) for x in m.get("violencia_genero", [])],
            "fiscal": fiscal, "leido_eurostat": e.get("leido")}


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


BU_T = {"ZW=F": 36.744, "ZS=F": 36.744, "ZC=F": 39.368}   # bushels por tonelada: trigo y soja 60 lb, maíz 56 lb
LB_T = 2204.62                                           # libras por tonelada


def control(p, datos):
    """C132: «Control» del móvil (arriba de Mercado). Una fila por cifra, una sola fuente por cifra.
    Campos: e etiqueta · u unidad · v valor · d decimales · t texto (si no es número) · c variación % · pp variación en puntos ·
    per periodo de la variación · f fecha de la sesión o del dato · n nivel P/S · fu fuente · url · col precio|neutro ·
    fr diario|semanal|mensual (para avisar de datos viejos) · x notas del detalle. Las cripto las pinta el móvil desde «mercado» (en vivo)."""
    YH = ("Yahoo Finance", "https://finance.yahoo.com/")

    def fila(e, v, u, f, n, fu, url, c=None, d=2, col="neutro", fr="diario", per="1 día", **extra):
        if v is None:
            return None
        return {k: x for k, x in {"e": e, "v": v, "u": u, "d": d, "c": c, "per": per, "f": f, "n": n, "fu": fu, "url": url, "col": col, "fr": fr, **extra}.items() if x not in (None, [], "")}

    grupos = []

    def grupo(t, filas, nota=None):
        filas = [x for x in filas if x]
        if filas:
            grupos.append({"t": t, "filas": filas, **({"nota": nota} if nota else {})})

    idx = {x["simbolo"]: x for x in p.get("indices", {}).get("indices", [])}
    orden = (("^GSPC", "S&P 500 · EE. UU."), ("^IXIC", "Nasdaq · EE. UU."), ("^DJI", "Dow Jones · EE. UU."), ("^STOXX50E", "Euro Stoxx 50 · zona euro"),
             ("^IBEX", "IBEX 35 · España"), ("^GDAXI", "DAX · Alemania"), ("^N225", "Nikkei 225 · Japón"), ("^HSI", "Hang Seng · Hong Kong"),
             ("000001.SS", "Shanghái · China"), ("^KS11", "Kospi · Corea del Sur"))

    def bolsa(s, e, col="precio"):
        x = idx.get(s)
        if not x:
            return None
        nota = [f"Para un inversor en dólares: {x['cambio_1d_usd']:+.2f} % (índice + divisa)".replace(".", ",")] if x.get("moneda") != "USD" and x.get("cambio_1d_usd") is not None else []
        moneda = x.get("moneda") or MONEDA_INDICE.get(s) or "USD"
        if abs(x.get("cambio_1d") or 0) >= 4:   # C152: un salto grande no se deja sin contexto
            nota = nota + ["Movimiento de más de un 4 % en un día: la causa no está verificada; lee el R00 de apertura de esa fecha (Seguimiento) antes de interpretarlo"]
        return fila(e, x["valor"], f"puntos · cotiza en {moneda}", x["fecha"], "S", *YH, c=x.get("cambio_1d"), col=col, x=nota)
    grupo("Bolsas", [bolsa(s, e) for s, e in orden] + [bolsa("^VIX", "VIX · miedo esperado en el S&P 500", col="neutro")],
          "Índices en puntos, no en dinero. El VIX sube cuando el mercado espera más sustos; va en gris.")

    wl = {x["ticker"]: x for x in p.get("watchlist", {}).get("valores", [])}
    etf = (("VWCE", "VWCE · todo el mundo (acumula)"), ("IWDA", "IWDA · países desarrollados (acumula)"), ("VUSA", "VUSA · S&P 500 (reparte)"),
           ("SPY", "SPY · S&P 500 (EE. UU.)"), ("QQQ", "QQQ · Nasdaq 100 (EE. UU.)"))

    def fondo(t, e):
        x = wl.get(t)
        if not x:
            return None
        notas = [f"{k}: {x[c]:+.2f} %".replace(".", ",") for k, c in (("1 semana", "cambio_1s"), ("3 meses", "cambio_3m"), ("en lo que va de año", "ytd")) if x.get(c) is not None]
        return fila(e, x["precio"], {"EUR": "€", "USD": "$"}.get(x.get("moneda"), x.get("moneda") or ""), x["fecha"], "S", *YH, c=x.get("cambio_1d"), col="precio", x=[x["nombre"]] + notas)
    grupo("ETFs y fondos indexados (referencia)", [fondo(t, e) for t, e in etf],
          "Son referencias, no posiciones ni recomendaciones. Un fondo indexado que copia el mismo índice se mueve casi igual que su ETF.")

    mat = {x["simbolo"]: x for x in p.get("materias", {}).get("materias", [])}
    fut = {x["simbolo"]: x for x in p.get("alimentos", {}).get("futuros", [])}
    eia = {x["id"]: x for x in (p.get("materias", {}).get("spot_eia") or {}).get("series", [])}

    def futuro(s, e, u, factor=1.0, d=2, fuente=None):
        x = mat.get(s) or fut.get(s)
        if not x:
            return None
        notas = [f"Unidad original: {fm_es(x['valor'], 2)} {x.get('unidad', '')}"] if factor != 1.0 else []
        if x.get("cambio_1m") is not None:
            notas.append(f"Desde {x.get('desde', '')}: {x['cambio_1m']:+.1f} %".replace(".", ","))
        return fila(e, round(x["valor"] * factor, d), u, x["fecha"], "S", *(fuente or YH), c=x.get("cambio_1d"), d=d, x=notas)

    pet = datos.get("petroleo") or {}

    def crudo(k, e):
        x = pet.get(k)
        if not x:
            return None
        notas = []
        s = eia.get(k)
        unidad = "$ el barril (futuro)"
        if s:   # C151: spot oficial visible en la propia fila, con su fecha (no se resta al futuro de otro día)
            unidad += f" · spot EIA [P] {fm_es(s['valor'], 2)} $ el {s['fecha'][8:]}/{s['fecha'][5:7]}"
            notas.append(f"{s['nombre']} (EIA, [P]): {fm_es(s['valor'], 2)} $ el {s['fecha']}. Es crudo físico y la EIA publica con ~3 días de retraso: compara solo con el futuro de la MISMA fecha (suele estar 3-7 $ por encima)")
        return fila(e, x["valor"], unidad, x["fecha"], "S", *YH, c=x.get("cambio_1d"), x=notas)

    ep = p.get("energia_precios", {})

    def luz(serie, e, fu):
        s = ep.get(serie) or []
        if not s:
            return None
        a, b = (s[-2] if len(s) > 1 else None), s[-1]
        return fila(e, b["media"], "€/MWh (media del día)", b["fecha"], "P", *fu, c=round((b["media"] / a["media"] - 1) * 100, 2) if a and a["media"] else None, per="frente al día anterior",
                    x=[f"Mínimo {fm_es(b['min'], 2)} · máximo {fm_es(b['max'], 2)} €/MWh"])
    grupo("Energía", [crudo("brent", "Petróleo Brent"), crudo("wti", "Petróleo WTI (EE. UU.)"),
                      futuro("NG=F", "Gas natural Henry Hub (EE. UU.)", "$ por MMBtu", d=3),
                      luz("omie_diario", "Luz España · mercado mayorista (OMIE)", ("OMIE", "https://www.omie.es/es/market-results/daily/daily-market/daily-hourly-price")),
                      luz("pvpc_diario", "Luz España · tarifa regulada PVPC", ("REE (Red Eléctrica)", "https://www.ree.es/es/datos/mercados/componentes-precio-energia-cierre-desglose"))],
          "Flechas en gris: que la energía suba no es bueno ni malo para todos. Falta el gas europeo TTF (C111) y la gasolina y el diésel (boletín semanal de la UE).")

    fao = next((x for x in (p.get("alimentos", {}).get("fao") or {}).get("indices", []) if x.get("nombre") == "Food Price Index"), None)
    fao_meta = (p.get("alimentos", {}).get("fao") or {})
    grupo("Alimentos", [futuro("ZW=F", "Trigo", "$ por tonelada", BU_T["ZW=F"] / 100, 0), futuro("ZC=F", "Maíz", "$ por tonelada", BU_T["ZC=F"] / 100, 0),
                        futuro("ZS=F", "Soja", "$ por tonelada", BU_T["ZS=F"] / 100, 0), futuro("ZR=F", "Arroz", "$ por tonelada", LB_T / 100, 0),
                        futuro("KC=F", "Café arábica", "$ por libra", 0.01), futuro("SB=F", "Azúcar", "$ por tonelada", LB_T / 100, 0),
                        futuro("CC=F", "Cacao", "$ por tonelada", d=0),
                        fila("Índice FAO de precios de los alimentos", fao["valor"], f"índice ({fao_meta.get('base', '2014-2016 = 100')})", fao_meta.get("mes"), "P",
                             "FAO", fao_meta.get("fuente") or "https://www.fao.org/worldfoodsituation/foodpricesindex/en/", c=round((fao["valor"] / fao["mes_anterior"] - 1) * 100, 2) if fao.get("mes_anterior") else None,
                             d=1, fr="mensual", per="1 mes", x=[f"Frente a hace 12 meses: {fao['interanual']:+.1f} %".replace(".", ",")] if fao.get("interanual") is not None else []) if fao else None],
          "Futuros de Chicago y Nueva York convertidos a $ por tonelada (en el detalle, la unidad original). El índice FAO es mensual.")

    grupo("Metales", [futuro("GC=F", "Oro", "$ por onza troy"), futuro("SI=F", "Plata", "$ por onza troy"), futuro("HG=F", "Cobre", "$ por tonelada", LB_T, 0)])

    filas = []
    dv = p.get("divisas", {})
    for x in dv.get("divisas", []):
        filas.append(fila(f"1 € en {x['nombre'].lower()}", x["valor"], x["codigo"], x["fecha"], "P", "BCE (tipo de referencia)", x["url"], c=x.get("cambio_1d"), d=2 if x["valor"] > 10 else 4))
    if not dv.get("divisas") and datos.get("eur"):
        filas.append(fila("1 € en dólar estadounidense", datos["eur"]["tipo"], "USD", datos["eur"]["fecha"], "P", "BCE (tipo de referencia)", "https://data.ecb.europa.eu/data/datasets/EXR/EXR.D.USD.EUR.SP00.A", d=4))
    if dv.get("dxy"):
        x = dv["dxy"]
        filas.append(fila(x["nombre"], x["valor"], "índice frente a 6 monedas", x["fecha"], "S", *YH, c=x.get("cambio_1d")))
    tv = {t["jur"]: t for t in p.get("tipos_vivos", {}).get("paises", [])}
    tb = {t["id"]: t for t in p.get("tipos_bis", {}).get("paises", [])}
    for t, e in ((tv.get("eeuu"), "Tipo oficial · Reserva Federal"), (tv.get("ue"), "Tipo oficial · BCE (depósito)"), (tb.get("JP"), "Tipo oficial · Banco de Japón")):
        if t:
            filas.append(fila(e, t["num"], "", t.get("dato_de"), "P", t.get("fuente") or "BIS (tipos oficiales)", "https://data.bis.org/topics/CBPOL" if t is tb.get("JP") else None,
                              t=t["valor"], fr="diario", x=[f"Último cambio: {t['ultimo_cambio']}"] if t.get("ultimo_cambio") else []))
    bonos = {q["id"]: q for q in p.get("bonos", {}).get("paises", [])}
    for k, e in (("USA", "Bono a 10 años · EE. UU."), ("ESP", "Bono a 10 años · España"), ("EUR", "Bono a 10 años · zona euro AAA (curva BCE)")):
        q = bonos.get(k)
        if q and q["plazos"].get("10A") is not None:
            ant = (q.get("prev") or {}).get("10A")
            filas.append(fila(e, q["plazos"]["10A"], "% de rentabilidad", q["fecha"], q.get("nivel") or "P", q.get("fuente") or q.get("nombre") or "", q.get("url"),
                              pp=round(q["plazos"]["10A"] - ant, 2) if ant is not None else None, per="frente al dato anterior"))
    eur12 = next((s for s in p.get("credito", {}).get("series", []) if s["id"] == "euribor12"), None)
    if eur12:
        filas.append(fila("Euríbor a 12 meses (media del mes)", eur12["valor"], "%", eur12["fecha"], "P", "BCE", "https://data.ecb.europa.eu/data/datasets/FM/FM.M.U2.EUR.RT.MM.EURIBOR1YD_.HSTA",
                          d=3, pp=round(eur12["valor"] - eur12["anterior"], 3) if eur12.get("anterior") is not None else None, per="1 mes", fr="mensual",
                          x=[f"Hace 12 meses: {fm_es(eur12['hace_12m'], 3)} %"] if eur12.get("hace_12m") is not None else []))
    grupo("Divisas y tipos", filas, "Divisas: cuánto vale 1 euro. Tipos y bonos: la variación va en puntos, no en %.")
    return {"generado": datos["generado"], "leido": p.get("leido"), "grupos": grupos}


def fm_es(v, d=2):
    """Número en formato español (punto de miles, coma decimal)."""
    return f"{v:,.{d}f}".replace(",", " ").replace(".", ",").replace(" ", ".")


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
        "eventos": eventos(), "voces": voces(), "niveles": cargar("explorador/voces.json").get("niveles", {}), "verificados": verificados(),
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
    try:
        datos["control"] = control(p, datos)
    except Exception as e:
        fallos.append(f"control: {type(e).__name__}: {e}")
        if "control" in previo:
            datos["control"] = previo["control"]
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(datos, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"data.json: {len(datos['eventos'])} eventos, {len(datos.get('noticias') or [])} noticias, {len(datos['voces'])} voces, "
          f"petróleo {', '.join(f'{k} {v['valor']}' for k, v in datos.get('petroleo', {}).items())}, USD/EUR {datos.get('eur', {}).get('tipo')}")
    for f in fallos:
        print("AVISO (se conserva lo anterior si existía):", f)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
