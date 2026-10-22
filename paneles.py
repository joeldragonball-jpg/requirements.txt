"""Paneles de datos del Explorador (v1): deuda de EE. UU. por tenedor (TIC) y stablecoins. Sin IA ni red al mostrar.

Los datos los genera scripts/actualizar_paneles.py en explorador/paneles.json; esta página solo los lee.
"""
import json
import re
import unicodedata
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

RAIZ = Path(__file__).parent
CARPETA = RAIZ / "explorador"


def _version():
    s = 0.0
    glos = list((RAIZ / "informes" / "research").glob("*R16-glosario*.md"))
    for p in (Path(__file__), CARPETA / "paneles.html", CARPETA / "paneles.json", CARPETA / "regulacion.json", CARPETA / "datos.json", CARPETA / "bancos-eba.json", *glos):
        try:
            s = max(s, p.stat().st_mtime)
        except Exception:
            pass
    return s


def _tipos():
    """Tipos de interés por país: salen de las celdas «política monetaria» del radar (regulacion.json), ya verificadas allí."""
    try:
        r = json.loads((CARPETA / "regulacion.json").read_text(encoding="utf-8"))
    except Exception:
        return []
    nombres = {j["id"]: j["nombre"] for j in r.get("jurisdicciones", [])}
    filas = []
    for c in r.get("celdas", []):
        if c.get("tema") != "politica" or not c.get("valor") or c.get("jur") == "brics":
            continue
        p = c.get("proxima") or {}
        filas.append({"pais": nombres.get(c["jur"], c["jur"]), "valor": c["valor"], "dir": c.get("dir") or "n/d",
                      "fecha": c.get("fecha"), "nivel": c.get("fuente"), "proxima": p.get("fecha"), "que": p.get("que", ""),
                      "estado": c.get("estado", "")})
    return filas


def _plano(texto):
    return "".join(c for c in unicodedata.normalize("NFD", texto.lower()) if unicodedata.category(c) != "Mn")


def _limpiar(md):
    md = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"[*_`>#|]+", "", md)
    return re.sub(r"\s+", " ", md).strip()


def _glosario():
    """Términos de las tablas R16 (informes/research) con su capa del mapa de órbitas (por palabras clave de datos.json)."""
    try:
        capas = json.loads((CARPETA / "datos.json").read_text(encoding="utf-8"))["capas"]
    except Exception:
        return []
    filas, vistos = [], set()
    for ruta in sorted((RAIZ / "informes" / "research").glob("*R16-glosario*.md")):
        for linea in ruta.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*\*\*(.+?)\*\*[^|]*\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$", linea)
            if not m:
                continue
            term, defi, fuente, estado = (_limpiar(g) for g in m.groups())
            clave = _plano(term)
            if clave in vistos:
                continue
            vistos.add(clave)
            t, c = _plano(term), _plano(defi)
            pts = [(sum(4 * t.count(_plano(k)) + min(c.count(_plano(k)), 3) for k in capa.get("claves", [])), capa["id"]) for capa in capas]
            filas.append({"t": term, "d": defi[:700], "f": fuente[:200], "e": estado[:200],
                          "capas": [i for p, i in sorted(pts, reverse=True) if p >= 2][:3], "ver": "VERIFICAR" in estado.upper() or "VERIFICAR" in defi.upper()})
    filas.sort(key=lambda x: _plano(x["t"]))
    return filas


@st.cache_data(ttl=600, show_spinner=False)
def _html(version):
    datos = json.loads((CARPETA / "paneles.json").read_text(encoding="utf-8"))
    datos["tipos"] = _tipos()
    datos["glosario"] = _glosario()
    try:
        datos["bancos"] = json.loads((CARPETA / "bancos-eba.json").read_text(encoding="utf-8"))
    except Exception:
        datos["bancos"] = None
    try:
        datos["capas"] = [{"id": c["id"], "nombre": c["nombre"]} for c in json.loads((CARPETA / "datos.json").read_text(encoding="utf-8"))["capas"]]
    except Exception:
        datos["capas"] = []
    datos["hoy"] = __import__("datetime").date.today().isoformat()
    texto = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\!--")
    return (CARPETA / "paneles.html").read_text(encoding="utf-8").replace("__DATOS__", texto)


def mostrar():
    try:
        html = _html(_version())
    except FileNotFoundError:
        st.info("Aún no hay datos. Ejecuta `python scripts/actualizar_paneles.py` y recarga.")
        return
    except Exception as e:
        st.warning(f"No se pudieron cargar los paneles ({type(e).__name__}).")
        return
    components.html(html, height=1100, scrolling=True)
