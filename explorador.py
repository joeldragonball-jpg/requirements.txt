"""Pestaña «🌌 Explorador» del Cerebro (la Órbita): resumen, capas de los raíles financieros, línea de tiempo, calendario, matriz
país × tema, mapa mundi, noticias, voces y paneles de datos, más la documentación relacionada (research, dossiers, apuntes y glosario).
Solo lee archivos del repositorio (explorador/, informes/, cerebro/): sin IA, sin APIs, sin coste.
Seguridad: el JSON se incrusta como datos (no como código) y el HTML/JS pinta todo con textContent, nunca con innerHTML."""
import json
import re
import tomllib
import unicodedata
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlsplit

import streamlit as st
import streamlit.components.v1 as components

RAIZ = Path(__file__).parent
CARPETA = RAIZ / "explorador"
FUENTES_DOCS = [("Research", RAIZ / "informes" / "research"), ("Dossier", RAIZ / "informes" / "dossiers"),
                ("Apunte", RAIZ / "cerebro" / "documentos")]


def _plano(texto):
    """Minúsculas y sin acentos, para comparar palabras clave."""
    return "".join(c for c in unicodedata.normalize("NFD", texto.lower()) if unicodedata.category(c) != "Mn")


def _leer(ruta):
    try:
        return ruta.read_text(encoding="utf-8")
    except Exception:
        return ""


def _limpiar(md):
    md = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md)          # enlaces: solo el texto
    md = re.sub(r"[*_`>#|]+", "", md)
    return re.sub(r"\s+", " ", md).strip()


def _resumen(texto):
    """Primeras frases de la sección «Resumen» (o del arranque del documento) en texto plano."""
    m = re.search(r"^##\s+Resumen[^\n]*\n(.*?)(?=^##\s|\Z)", texto, flags=re.S | re.M)
    base = m.group(1) if m else texto.split("\n", 1)[-1]
    base = re.sub(r"\A---.*?---\s*", "", base, flags=re.S)
    return _limpiar(base)[:650]


def _titulo(texto, ruta):
    sin_meta = re.sub(r"\A---.*?---\s*", "", texto, flags=re.S)
    m = re.search(r"^#\s+(.+)$", sin_meta, flags=re.M)
    return _limpiar(m.group(1))[:140] if m else ruta.stem


def _documentos():
    """Todos los documentos con título y resumen (research, dossiers y apuntes)."""
    out = []
    for tipo, carpeta in FUENTES_DOCS:
        if not carpeta.is_dir():
            continue
        for ruta in sorted(carpeta.glob("*.md")):
            if ruta.name == "MAPA.md":
                continue
            texto = _leer(ruta)
            if not texto:
                continue
            m = re.search(r"-(R\d+[A-Za-z]*|G\d+)-", ruta.name)
            out.append({"tipo": tipo, "id": m.group(1) if m else "", "titulo": _titulo(texto, ruta), "resumen": _resumen(texto),
                        "archivo": f"{ruta.parent.relative_to(RAIZ).as_posix()}/{ruta.name}", "_plano": _plano(ruta.name + " " + texto[:3500])})
    return out


def _glosario(conceptos):
    """Términos del glosario de la app (apuntes) y de la tabla R16 del research."""
    out = [{"t": c["concepto"], "d": c["definicion"][:260]} for c in (conceptos or []) if c.get("concepto")]
    for ruta in sorted((RAIZ / "informes" / "research").glob("*R16-glosario*.md")):
        for linea in _leer(ruta).splitlines():
            m = re.match(r"^\|\s*\*\*(.+?)\*\*[^|]*\|\s*(.+?)\s*\|", linea)
            if m:
                out.append({"t": _limpiar(m.group(1)), "d": _limpiar(m.group(2))[:260]})
    vistos, unicos = set(), []
    for g in out:
        k = _plano(g["t"])
        if k not in vistos:
            vistos.add(k)
            unicos.append(g)
    return unicos


def _puntos(claves, titulo, cuerpo, definicion=False):
    t, c = _plano(titulo), cuerpo
    total = 0
    for k in claves:
        k = _plano(k)
        total += 4 * t.count(k) + min(c.count(k), 3)
    return total


@st.cache_data(ttl=300, show_spinner=False)
def _relacionados(conceptos_clave, firma):
    """Por capa: los documentos y términos del glosario más relacionados (por palabras clave)."""
    conceptos = json.loads(conceptos_clave)
    datos = json.loads((CARPETA / "datos.json").read_text(encoding="utf-8"))
    docs, glos = _documentos(), _glosario(conceptos)
    resultado = {}
    for capa in datos["capas"]:
        claves = capa.get("claves", [])
        puntuados = sorted(((_puntos(claves, d["titulo"], d["_plano"]), d) for d in docs), key=lambda x: -x[0])
        inv = []
        cupo = {"Research": 5, "Dossier": 3, "Apunte": 2}
        for p, d in puntuados:
            if p < 4 or cupo[d["tipo"]] == 0:
                continue
            cupo[d["tipo"]] -= 1
            inv.append({k: v for k, v in d.items() if k != "_plano"})
        gl = sorted(((_puntos(claves, g["t"], _plano(g["d"])), g) for g in glos), key=lambda x: -x[0])
        resultado[capa["id"]] = {"inv": inv, "glo": [g for p, g in gl if p >= 2][:8]}
    resultado["_totales"] = {"docs": len(docs), "glosario": len(glos)}
    return resultado


def _version():
    """Cambia al editar este archivo (para que la caché no sirva resultados de una versión antigua del código)."""
    try:
        return str(Path(__file__).stat().st_mtime)
    except Exception:
        return ""


def _firma():
    """Cambia cuando cambia algún documento, para refrescar la caché."""
    n, ultimo = 0, 0.0
    for _, carpeta in FUENTES_DOCS:
        if carpeta.is_dir():
            for p in carpeta.glob("*.md"):
                n += 1
                ultimo = max(ultimo, p.stat().st_mtime)
    for p in CARPETA.glob("*.json"):      # los paneles y datos de explorador/ también cambian la firma (si no, la app sirve la caché vieja)
        ultimo = max(ultimo, p.stat().st_mtime)
    for p in CARPETA.glob("*.html"):
        ultimo = max(ultimo, p.stat().st_mtime)
    return f"{n}-{ultimo}-{_version()}"



# ---------------------------------------------------------------- calendario (eventos/calendario.toml)
TEMAS = {"reg": {"nombre": "Regulación", "color": "#ff7a59"},
         "tok": {"nombre": "Tokenización y digital assets", "color": "#2ee6a6"},
         "cbdc": {"nombre": "CBDC y bancos centrales digitales", "color": "#6cb4ff"},
         "fondos": {"nombre": "Fondos y ETF", "color": "#ffd166"},
         "macro": {"nombre": "Macro y política monetaria", "color": "#b8a1ff"},
         "fiscal": {"nombre": "Fiscalidad y reporte", "color": "#aab4c8"}}
# Orden de prioridad al clasificar: lo más específico primero
PALABRAS_TEMA = [("cbdc", ["euro digital", "cbdc", "mas bill", "rublo", "pontes", "nexus", "agora", "bis "]),
                 ("tok", ["tokeniz", "dtcc", "stellar", "xrpl", "escrow", "enmienda", "swell", "meridian", "protocolo", "rwa", "ripple"]),
                 ("fondos", ["13f", "etf", "xrpn", "evernorth", "21shares", "opciones de etf"]),
                 ("reg", ["comentarios", "sec:", "sec ", "cftc", "genius", "clarity", "mica", "esma", "regulaci", "licencia", "senado",
                          "stablecoin", "norma", "fsc", "corea", "brasil", "autorizaci"]),
                 ("fiscal", ["dac8", "modelo 721", "campana de la renta", "ejercicio fiscal", "renta 2026"]),
                 ("macro", ["fomc", "fed", "bce", "banco de japon", "ipc", "empleo", "pce", "pib", "brent", "opep", "eia", "aie", "petroleo",
                            "elecciones", "tesoro", "g20", "apec", "rbi", "lpr", "inflacion"])]
CAPA_DE_TEMA = {"reg": "reg", "cbdc": "cbdc", "fondos": "fondos", "macro": "reg", "fiscal": "custodia"}


def _tema_y_capa(titulo, detalle):
    t = _plano(titulo + " " + detalle)
    for tema, claves in PALABRAS_TEMA:
        if any(_plano(k) in t for k in claves):
            if tema == "tok":
                capa = "puente" if any(k in t for k in ("xrpl", "stellar", "escrow", "enmienda", "swell", "meridian", "protocolo")) else "token"
                return tema, capa
            capa = CAPA_DE_TEMA[tema]
            if tema == "reg":                     # la regulación se reparte entre las capas que afecta
                if any(k in t for k in ("stablecoin", "genius", "mica")):
                    capa = "stable"
                elif "custodia" in t:
                    capa = "custodia"
            return tema, capa
    if any(k in t for k in ("bono ", "bonos", "deuda publica", "subasta de deuda", "letras del tesoro")):
        return "macro", "deuda"            # emisiones y deuda soberana: capa «Deuda soberana y bonos»
    return "macro", "reg"


@st.cache_data(ttl=600, show_spinner=False)
def _calendario(hoy_iso, version_codigo=""):
    """Eventos futuros del calendario, clasificados por tema y asignados a una capa del mapa."""
    try:
        with open(RAIZ / "eventos" / "calendario.toml", "rb") as fh:
            crudos = tomllib.load(fh).get("eventos", [])
    except Exception:
        return []
    hoy = date.fromisoformat(hoy_iso)
    limite = hoy + timedelta(days=270)
    out = []
    for e in crudos:
        try:
            ini = date.fromisoformat(e["fecha"])
            fin = date.fromisoformat(e.get("hasta", e["fecha"]))
        except Exception:
            continue
        if fin < hoy or ini > limite:
            continue
        tema, capa = _tema_y_capa(str(e.get("titulo", "")), str(e.get("detalle", "")))
        dominio = urlsplit(str(e.get("fuente", ""))).netloc.replace("www.", "")
        out.append({"ini": ini.isoformat(), "fin": fin.isoformat(), "titulo": str(e.get("titulo", ""))[:150],
                    "detalle": _limpiar(str(e.get("detalle", "")))[:230], "impacto": str(e.get("impacto", "bajo")),
                    "aprox": bool(e.get("aproximado")), "fuente": dominio, "tema": tema, "capa": capa})
    return sorted(out, key=lambda x: x["ini"])


def _html(conceptos):
    plantilla = (CARPETA / "mapa.html").read_text(encoding="utf-8")
    datos = json.loads((CARPETA / "datos.json").read_text(encoding="utf-8"))
    rel = _relacionados(json.dumps(conceptos or [], ensure_ascii=False, sort_keys=True), _firma())
    for capa in datos["capas"]:
        capa["docs"] = rel.get(capa["id"], {"inv": [], "glo": []})
    try:
        datos["radar"] = json.loads((CARPETA / "regulacion.json").read_text(encoding="utf-8"))
    except Exception:
        datos["radar"] = None            # sin el archivo del radar, el mapa funciona igual (sin esa sección)
    try:                              # contraste privado con la tesis: solo existe en tu PC (privado/ no se sube a GitHub)
        datos["contraste"] = json.loads((RAIZ / "privado" / "contraste-tesis.json").read_text(encoding="utf-8"))
    except Exception:
        datos["contraste"] = None
    try:                              # datos al día de los paneles (scripts/actualizar_paneles.py): sin el archivo, el mapa funciona igual
        datos["paneles"] = json.loads((CARPETA / "paneles.json").read_text(encoding="utf-8"))
    except Exception:
        datos["paneles"] = None
    try:                              # voces: declaraciones de personas e instituciones (informes de vídeos y research)
        datos["voces"] = json.loads((CARPETA / "voces.json").read_text(encoding="utf-8"))
    except Exception:
        datos["voces"] = None
    try:                              # cruce privado de las voces con la tesis: solo existe en tu PC (privado/ no se sube a GitHub)
        datos["voces_tesis"] = json.loads((RAIZ / "privado" / "voces-tesis.json").read_text(encoding="utf-8"))
    except Exception:
        datos["voces_tesis"] = None
    try:                              # exposición soberana por banco (scripts/preparar_bancos_eba.py)
        datos["bancos"] = json.loads((CARPETA / "bancos-eba.json").read_text(encoding="utf-8"))
    except Exception:
        datos["bancos"] = None
    for clave, archivo in (("calificaciones", "calificaciones"), ("deuda_fmi", "deuda-fmi"), ("valoracion", "valoracion"), ("reservas", "reservas"), ("rwa_cadena_manual", "rwa-por-cadena-manual"), ("cbdc_blockchains", "cbdc-blockchains")):
        try:                          # tablas de los paneles de datos (solo lectura); sin el archivo, esa tabla no sale
            datos[clave] = json.loads((CARPETA / f"{archivo}.json").read_text(encoding="utf-8"))
        except Exception:
            datos[clave] = None
    datos["biblioteca"] = rel.get("_totales", {})
    hoy = date.today().isoformat()
    datos["calendario"] = {"hoy": hoy, "temas": TEMAS, "eventos": _calendario(hoy, _version())}
    # Dentro de <script type="application/json"> hay que evitar que el texto cierre la etiqueta
    texto = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\!--")
    vistas = json.dumps((CARPETA / "vistas.html").read_text(encoding="utf-8"), ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\!--")
    return plantilla.replace("__VISTAS__", vistas).replace("__DATOS__", texto)


def mostrar(conceptos=None):
    # El mapa ocupa todo el ancho de la página (sin los márgenes de Streamlit)
    # Fondo de toda la página igual que el del mapa (el mapa es transparente), para que se vea como una sola pantalla
    st.markdown("<style>.block-container{max-width:100% !important;padding-left:1.2rem !important;padding-right:1.2rem !important;"
                "padding-top:0 !important;padding-bottom:.5rem !important}"
                "html,body,.stApp,[data-testid='stAppViewContainer'],[data-testid='stMain']{background:"
                "radial-gradient(ellipse 55% 38% at 14% 12%,rgba(99,102,241,.22),transparent 70%),"
                "radial-gradient(ellipse 45% 34% at 92% 30%,rgba(190,70,130,.15),transparent 70%),"
                "radial-gradient(ellipse 45% 30% at 72% 4%,rgba(34,160,190,.13),transparent 70%),"
                "radial-gradient(ellipse 80% 60% at 50% 32%,#0b1230 0%,#050816 85%) fixed !important}"
                "[data-testid='stHeader']{display:none !important}"
                "html,body,.stApp,[data-testid='stAppViewContainer'],[data-testid='stMain']{overflow:hidden !important}"
                "[data-testid='stPopover']{position:fixed !important;right:14px;bottom:84px;z-index:1000;width:auto !important}"
                "[data-testid='stPopover'] button{padding:4px 10px !important;min-height:0 !important;font-size:.78rem !important;opacity:.85}"
                "[data-testid='stPopoverBody'] .st-key-grupo_menu_cerebro div[role='radiogroup']{display:flex !important;flex-direction:column !important;gap:2px !important}"
                "[data-testid='stPopoverBody'] .st-key-grupo_menu_cerebro label[data-testid='stRadioOption']{min-height:0 !important;height:auto !important;padding:4px 10px !important;flex-direction:row !important;text-align:left !important}"
                "[data-testid='stPopoverBody'] .st-key-grupo_menu_cerebro label p{font-size:.9rem !important}"
                "[data-testid='stPopoverBody'] .st-key-grupo_menu_cerebro label p::first-line{font-size:.9rem !important}"
                "*::-webkit-scrollbar{width:4px;height:4px}*::-webkit-scrollbar-track{background:rgba(148,163,184,.08)}"
                "*::-webkit-scrollbar-thumb{background:rgba(226,232,240,.45);border-radius:2px}*::-webkit-scrollbar-thumb:hover{background:rgba(241,213,138,.85)}</style>", unsafe_allow_html=True)
    try:
        html = _html(conceptos)
    except Exception as e:
        st.error(f"No se pudo cargar el explorador ({type(e).__name__}).")
        return
    components.html(html, height=860, scrolling=False)
