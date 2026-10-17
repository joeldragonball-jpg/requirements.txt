"""Pestaña «Seguimiento»: avance de la cola de research, informes recientes, último informe diario y próximas fechas.
Solo lee archivos del repositorio (research/COLA.md, informes/ y eventos/calendario.toml). Sin IA, sin APIs, sin coste."""
import re
import tomllib
from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st

RAIZ = Path(__file__).parent
COLA = RAIZ / "research" / "COLA.md"
INFORMES = RAIZ / "informes" / "research"
DIARIOS = RAIZ / "informes"
CALENDARIO = RAIZ / "eventos" / "calendario.toml"


def _leer(ruta):
    try:
        return ruta.read_text(encoding="utf-8")
    except Exception:
        return ""


def _estado(texto):
    t = texto.strip().lower()
    if t.startswith("hecho"):
        return "hecha"
    if "cubierto por" in t or "cubierta por" in t:
        return "cubierta"
    if t.startswith("recurrente"):
        return "recurrente"
    if t.startswith("pendiente"):
        return "pendiente"
    return "otro"


def cargar_cola():
    """Filas de la tabla de research/COLA.md (las que empiezan por | R.. o | G..)."""
    filas = []
    for linea in _leer(COLA).splitlines():
        if not re.match(r"\|\s*[RG]\d+[A-Za-z]*\s*\|", linea):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) < 9:
            continue
        estado_txt = " | ".join(celdas[8:])
        filas.append({"ID": celdas[0], "Tema": celdas[1], "Modelo": celdas[3], "Esfuerzo": celdas[4],
                      "Tam.": celdas[5], "Estado": _estado(estado_txt), "Detalle": estado_txt})
    return filas


def cargar_informes():
    """Informes de informes/research/ (fecha y tarea sacadas del nombre; título de la primera línea)."""
    out = []
    for f in sorted(INFORMES.glob("*.md")):
        m = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", f.name)
        if not m:
            continue
        primera = _leer(f).split("\n", 1)[0].lstrip("# ").strip()
        out.append({"Fecha": m.group(1), "Archivo": f.name, "Título": primera[:110]})
    return sorted(out, key=lambda x: (x["Fecha"], x["Archivo"]), reverse=True)


def ultimo_diario():
    """Último informe diario (apertura/cierre/intradía) de informes/."""
    cand = [f for f in DIARIOS.glob("2*.md") if re.search(r"(apertura|cierre|intradia|revision|inicial)", f.name)]
    return max(cand, key=lambda f: f.name) if cand else None


def proximas_fechas(n=10):
    try:
        with open(CALENDARIO, "rb") as fh:
            evs = tomllib.load(fh).get("eventos", [])
    except Exception:
        return []
    hoy = date.today()
    out = []
    for e in evs:
        try:
            ini = date.fromisoformat(e["fecha"])
            fin = date.fromisoformat(e.get("hasta", e["fecha"]))
        except Exception:
            continue
        if fin >= hoy:
            out.append({**e, "ini": ini, "fin": fin, "dias": (ini - hoy).days})
    return sorted(out, key=lambda e: e["ini"])[:n]


def mostrar():
    st.markdown("<h1 style='margin:0 0 8px;font-size:clamp(1.6rem,5vw,2.2rem);font-weight:700'>📌 Seguimiento</h1>",
                unsafe_allow_html=True)
    st.caption("Qué se ha hecho, qué falta y qué viene. Lee los archivos del repositorio: no usa IA ni cuesta nada.")

    cola = cargar_cola()
    informes = cargar_informes()

    # --- Avance de la cola
    st.markdown("##### 🧭 Avance de la cola de research")
    if not cola:
        st.info("No encuentro research/COLA.md o su tabla.")
    else:
        hechas = sum(1 for c in cola if c["Estado"] == "hecha")
        pend = [c for c in cola if c["Estado"] == "pendiente"]
        contables = [c for c in cola if c["Estado"] in ("hecha", "pendiente")]
        c1, c2, c3 = st.columns(3)
        c1.metric("Hechas", hechas)
        c2.metric("Pendientes", len(pend))
        c3.metric("Informes guardados", len(informes))
        if contables:
            st.progress(hechas / len(contables), text=f"{hechas} de {len(contables)} tareas con trabajo propio")
        if pend:
            st.markdown("**Pendientes:**")
            st.dataframe(pd.DataFrame(pend)[["ID", "Tema", "Modelo", "Esfuerzo", "Tam."]],
                         hide_index=True, use_container_width=True)
        with st.expander("Ver toda la cola"):
            st.dataframe(pd.DataFrame(cola)[["ID", "Tema", "Modelo", "Estado"]], hide_index=True,
                         use_container_width=True)

    # --- Próximas fechas
    st.markdown("##### 🗓️ Próximas fechas")
    prox = proximas_fechas()
    if not prox:
        st.info("No hay fechas futuras en eventos/calendario.toml.")
    else:
        filas = []
        for e in prox:
            if e["dias"] < 0:
                cuando = "en curso"
            elif e["dias"] == 0:
                cuando = "hoy"
            elif e["dias"] == 1:
                cuando = "mañana"
            else:
                cuando = f"en {e['dias']} días"
            marca = {"alto": "🔴", "medio": "🟡"}.get(e.get("impacto"), "⚪")
            filas.append({"": marca, "Fecha": e["ini"].strftime("%d-%m-%Y"), "Cuándo": cuando,
                          "Evento": e["titulo"] + (" (aprox.)" if e.get("aproximado") else "")})
        st.dataframe(pd.DataFrame(filas), hide_index=True, use_container_width=True)
        st.caption("Las fechas con «aprox.» no se avisan por Telegram hasta confirmarlas.")

    # --- Informes recientes
    st.markdown("##### 📄 Informes de research recientes")
    if informes:
        st.dataframe(pd.DataFrame(informes[:15]), hide_index=True, use_container_width=True)
        with st.expander(f"Ver los {len(informes)} informes"):
            st.dataframe(pd.DataFrame(informes), hide_index=True, use_container_width=True)
        filtro = st.text_input("Buscar informe (por ejemplo: 13f, corea, stablecoins)", key="seg_filtro").strip().lower()
        coinciden = [i for i in informes if not filtro or filtro in (i["Archivo"] + " " + i["Título"]).lower()]
        elegido = st.selectbox("Leer un informe", [i["Archivo"] for i in coinciden], index=None,
                               placeholder="Elige un informe para leerlo aquí", key="seg_informe")
        if elegido:
            ruta = INFORMES / elegido
            try:
                ruta.resolve().relative_to(INFORMES.resolve())      # solo archivos dentro de informes/research/
                st.markdown(ruta.read_text(encoding="utf-8"))
            except Exception:
                st.error("No se puede leer ese informe.")
    else:
        st.info("Aún no hay informes en informes/research/.")

    # --- Último informe diario
    st.markdown("##### 🌅 Último informe diario")
    f = ultimo_diario()
    if f is None:
        st.info("No hay informes diarios en informes/.")
    else:
        texto = _leer(f)
        st.caption(f"Archivo: {f.name}")
        with st.expander("Leer", expanded=False):
            st.markdown(texto)
