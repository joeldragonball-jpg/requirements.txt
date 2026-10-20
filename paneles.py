"""Paneles de datos del Explorador (v1): deuda de EE. UU. por tenedor (TIC) y stablecoins. Sin IA ni red al mostrar.

Los datos los genera scripts/actualizar_paneles.py en explorador/paneles.json; esta página solo los lee.
"""
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

CARPETA = Path(__file__).parent / "explorador"


def _version():
    s = 0.0
    for p in (Path(__file__), CARPETA / "paneles.html", CARPETA / "paneles.json", CARPETA / "regulacion.json"):
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


@st.cache_data(ttl=600, show_spinner=False)
def _html(version):
    datos = json.loads((CARPETA / "paneles.json").read_text(encoding="utf-8"))
    datos["tipos"] = _tipos()
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
