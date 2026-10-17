"""Pestaña «🌌 Explorador» del Cerebro: mapa interactivo de los raíles financieros (capas que orbitan, clic para acercarse,
deslizador de tiempo, buscador, filtros y documentación relacionada: research, dossiers, apuntes y glosario).
Solo lee archivos del repositorio (explorador/, informes/, cerebro/): sin IA, sin APIs, sin coste.
Seguridad: el JSON se incrusta como datos (no como código) y el HTML/JS pinta todo con textContent, nunca con innerHTML."""
import json
import re
import unicodedata
from pathlib import Path

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


def _firma():
    """Cambia cuando cambia algún documento, para refrescar la caché."""
    n, ultimo = 0, 0.0
    for _, carpeta in FUENTES_DOCS:
        if carpeta.is_dir():
            for p in carpeta.glob("*.md"):
                n += 1
                ultimo = max(ultimo, p.stat().st_mtime)
    return f"{n}-{ultimo}"


def _html(conceptos):
    plantilla = (CARPETA / "mapa.html").read_text(encoding="utf-8")
    datos = json.loads((CARPETA / "datos.json").read_text(encoding="utf-8"))
    rel = _relacionados(json.dumps(conceptos or [], ensure_ascii=False, sort_keys=True), _firma())
    for capa in datos["capas"]:
        capa["docs"] = rel.get(capa["id"], {"inv": [], "glo": []})
    datos["biblioteca"] = rel.get("_totales", {})
    # Dentro de <script type="application/json"> hay que evitar que el texto cierre la etiqueta
    texto = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\!--")
    return plantilla.replace("__DATOS__", texto)


def mostrar(conceptos=None):
    # El mapa ocupa todo el ancho de la página (sin los márgenes de Streamlit)
    st.markdown("<style>.block-container{max-width:100% !important;padding-left:1.2rem !important;padding-right:1.2rem !important;"
                "padding-top:1rem !important}</style>", unsafe_allow_html=True)
    try:
        html = _html(conceptos)
    except Exception as e:
        st.error(f"No se pudo cargar el explorador ({type(e).__name__}).")
        return
    components.html(html, height=860, scrolling=False)
