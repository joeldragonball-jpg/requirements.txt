"""Sección «🔒 Privado»: lector de tus apuntes privados (carpeta privado/, que NO se sube a GitHub).
Solo se muestra en tu ordenador: la app desplegada no tiene esa carpeta, así que aquí no hay nada que enseñar.
Lee únicamente archivos .md; no envía nada a ninguna parte, no usa IA y no cuesta nada."""
from pathlib import Path

import streamlit as st

CARPETA = Path(__file__).parent / "privado"


def disponible():
    """True solo si existe privado/ (es decir, solo en tu PC)."""
    return CARPETA.is_dir()


def _archivos():
    """Apuntes .md de privado/ (y sus subcarpetas), los más recientes primero por nombre de archivo."""
    try:
        return sorted((p for p in CARPETA.rglob("*.md") if p.is_file()), key=lambda p: p.name, reverse=True)
    except Exception:
        return []


def _nombre(p):
    return str(p.relative_to(CARPETA)).replace("\\", "/")


def mostrar():
    st.markdown("<h1 style='margin:0 0 8px;font-size:clamp(1.6rem,5vw,2.2rem);font-weight:700'>🔒 Privado</h1>",
                unsafe_allow_html=True)
    if not disponible():
        st.info("Esta sección solo existe en tu ordenador (necesita la carpeta privado/).")
        return
    st.caption("Tus apuntes privados (tesis, diario, mapa de riesgos, disparadores, preguntas al asesor). "
               "No se suben a GitHub ni se envían a ninguna IA.")
    archivos = _archivos()
    if not archivos:
        st.info("No hay archivos .md en privado/ todavía.")
        return
    nombres = [_nombre(p) for p in archivos]
    elegido = st.selectbox("Documento", nombres, key="privado_doc")
    ruta = CARPETA / elegido
    try:
        ruta.resolve().relative_to(CARPETA.resolve())      # por seguridad: solo archivos dentro de privado/
        texto = ruta.read_text(encoding="utf-8")
    except Exception:
        st.error("No se puede leer ese archivo.")
        return
    st.markdown(texto)
