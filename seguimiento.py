"""Pestaña «Seguimiento»: qué se ha hecho, qué falta y qué caduca primero (research diario, colas de temas, plazos, predicciones, auditorías, bots).
Los datos los calcula scripts/construir_seguimiento.py (los mismos que usa la app móvil). Solo lee archivos del repositorio y la API pública de GitHub:
sin IA y sin coste."""
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

RAIZ = Path(__file__).parent
sys.path.insert(0, str(RAIZ / "scripts"))
import construir_seguimiento as datos_seg   # noqa: E402

INFORMES = RAIZ / "informes" / "research"
DIARIOS = RAIZ / "informes"
ORIGEN = {"R": "Research (R/G)", "T": "Temas (T)", "D": "Deuda (D)"}


@st.cache_data(ttl=300, show_spinner=False)
def _datos():
    return datos_seg.construir(bots_estado=True)


def _cuando(dias):
    if dias is None:
        return "sin fecha"
    return "hoy" if dias == 0 else "mañana" if dias == 1 else f"en {dias} días"


def mostrar():
    st.markdown("<h1 style='margin:0 0 8px;font-size:clamp(1.6rem,5vw,2.2rem);font-weight:700'>📌 Seguimiento</h1>", unsafe_allow_html=True)
    st.caption("Qué se ha hecho, qué falta y qué caduca primero. Lee archivos del repositorio: no usa IA ni cuesta nada.")
    d = _datos()

    # --- Hoy
    h = d["hoy"]
    st.markdown("##### ☀️ Hoy")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("R00 apertura", "✅ hecho" if h["apertura"] else "⏳ pendiente", help=f"Último: {h['ultima_apertura']}")
    c2.metric("R00 cierre", "✅ hecho" if h["cierre"] else "⏳ pendiente", help=f"Último: {h['ultimo_cierre']}")
    c3.metric("Racha", f"{h['racha']} días", help="Días seguidos con al menos un R00")
    r = d["resumen"]
    c4.metric("Tareas hechas", f"{r['hechas']} de {r['hechas'] + r['pendientes']}")
    st.progress(r["hechas"] / max(1, r["hechas"] + r["pendientes"]))
    toca = d.get("semana", {}).get("hoy", [])
    st.markdown("**Hoy toca:** " + (" · ".join(f"`{t['id']}` {t['nombre']} (≈ {t['coste']})" for t in toca) if toca else "solo el R00 (día ligero)")
                + " — prompts en `research/prompts/`")
    st.caption(" · ".join(f"{ORIGEN[o]}: {v['hechas']} hechas, {v['pendientes']} pendientes" for o, v in r["por_cola"].items()))

    # --- Rutinas
    st.markdown("##### 🔁 Rutina de research (actualizar, verificar, revisar)")
    st.dataframe(pd.DataFrame([{"ID": x["id"], "Tarea": x["nombre"], "Tipo": x["tipo"], "Cada": x["cada"], "Coste": x["coste"],
                                "Último": x["ultimo"] or "sin hacer", "Estado": "⚠ atrasada" if x["atrasada"] else "✓ al día"} for x in d["rutinas"]]),
                 hide_index=True, use_container_width=True)
    st.caption("Actualizar = datos que cambian (tipos, deuda, ETF, energía). Nuevo = temas sin cubrir (países, deuda por país). Verificar/revisar = cerrar [VERIFICAR], voces, auditorías, fuentes.")

    # --- Qué toca ahora
    st.markdown("##### 🎯 Research nuevo por hacer (el plazo solo se muestra si vence en menos de 45 días)")
    if d["pendientes"]:
        filas = [{"ID": t["id"], "Tema": t["tema"][:90], "Cola": ORIGEN.get(t["origen"], t["origen"]),
                  "Plazo": _cuando(t["plazo"]["dias"]) if t["plazo"] else "—", "Fecha": t["plazo"]["fecha"] if t["plazo"] else "",
                  "Evento": t["plazo"]["evento"] if t["plazo"] else ""} for t in d["pendientes"]]
        st.dataframe(pd.DataFrame(filas), hide_index=True, use_container_width=True)
    else:
        st.success("No queda nada pendiente en las colas.")

    # --- Plazos y predicciones
    st.markdown("##### 🗓️ Próximas fechas importantes")
    if d["plazos"]:
        st.dataframe(pd.DataFrame([{"": "🔴" if e["impacto"] == "alto" else "🟡", "Fecha": e["fecha"], "Cuándo": _cuando(e["dias"]), "Evento": e["titulo"]} for e in d["plazos"]]),
                     hide_index=True, use_container_width=True)
    st.markdown("##### 🔮 Predicciones registradas")
    p = d["predicciones"]
    st.caption(f"{len(p['abiertas'])} sin resolver · {len(p['resueltas'])} resueltas (se comprueban al llegar su fecha límite)")
    if p["abiertas"]:
        st.dataframe(pd.DataFrame([{"#": x["n"], "Quién": x["quien"][:40], "Predicción": x["que"], "Límite": x["limite"] or "sin fecha", "Cuándo": _cuando(x["dias"])}
                                   for x in p["abiertas"][:15]]), hide_index=True, use_container_width=True)
        with st.expander(f"Ver las {len(p['abiertas'])} sin resolver y las {len(p['resueltas'])} resueltas"):
            st.dataframe(pd.DataFrame([{"#": x["n"], "Quién": x["quien"], "Predicción": x["que"], "Límite": x["limite"] or "—", "Resultado": x["resultado"]}
                                       for x in p["abiertas"] + p["resueltas"]]), hide_index=True, use_container_width=True)

    # --- Auditorías
    a = d["auditorias"]
    st.markdown("##### 🔎 Auditoría de coherencia")
    if a:
        st.caption(f"{a['archivo']} · {a['abiertos']} abiertos · {a['cerrados']} cerrados")
        abiertos = [x for x in a["hallazgos"] if x["estado"] == "abierto"]
        if abiertos:
            st.dataframe(pd.DataFrame([{"ID": x["id"], "Gravedad": x["sev"], "Dónde": x["donde"], "Qué": x["que"]} for x in abiertos]), hide_index=True,
                         use_container_width=True)
        else:
            st.success("Todos los hallazgos están cerrados.")
    else:
        st.info("Aún no hay auditorías en informes/research/.")

    # --- Bots y cuota
    st.markdown("##### 🤖 Bots (GitHub Actions)")
    if d["bots"]:
        st.dataframe(pd.DataFrame([{"": "🟢" if b["ok"] else "🔴" if b["ok"] is False else "⚪", "Bot": b["nombre"], "Último": b["conclusion"],
                                    "Hace (h)": b["horas"], "Tolerancia (h)": b["tolerancia"]} for b in d["bots"]]), hide_index=True, use_container_width=True)
        st.caption("Los programados de GitHub se retrasan a veces unas horas: la tolerancia lo tiene en cuenta.")
    st.markdown("##### 📊 Cuota gastada por tarea (medida)")
    q = d["cuota"]
    st.caption(f"≈ {q['total']} % de cuota semanal sumada en {q['n']} tareas con coste anotado (columna «Real» de research/COLA.md; «<1 %» cuenta como 0,5).")
    if q["tareas"]:
        st.dataframe(pd.DataFrame([{"ID": x["id"], "Tema": x["tema"], "% cuota": x["pct"]} for x in q["tareas"]]), hide_index=True, use_container_width=True)

    # --- Informes recientes
    st.markdown("##### 📄 Informes recientes")
    informes = d["informes"]
    if informes:
        st.dataframe(pd.DataFrame([{"Fecha": i["fecha"], "Tipo": i["tipo"], "Título": i["titulo"]} for i in informes]), hide_index=True, use_container_width=True)
        archivos = sorted(INFORMES.glob("*.md"), reverse=True)
        filtro = st.text_input("Buscar informe (por ejemplo: 13f, corea, stablecoins)", key="seg_filtro").strip().lower()
        coinciden = [f.name for f in archivos if not filtro or filtro in f.name.lower()]
        elegido = st.selectbox("Leer un informe", coinciden, index=None, placeholder="Elige un informe para leerlo aquí", key="seg_informe")
        if elegido:
            ruta = INFORMES / elegido
            try:
                ruta.resolve().relative_to(INFORMES.resolve())      # solo archivos dentro de informes/research/
                st.markdown(ruta.read_text(encoding="utf-8"))
            except Exception:
                st.error("No se puede leer ese informe.")

    # --- Último informe diario
    st.markdown("##### 🌅 Último informe diario")
    cand = [f for f in DIARIOS.glob("2*.md") if any(k in f.name for k in ("apertura", "cierre", "intradia", "revision", "inicial"))]
    if cand:
        f = max(cand, key=lambda x: x.name)
        st.caption(f"Archivo: {f.name}")
        with st.expander("Leer", expanded=False):
            st.markdown(f.read_text(encoding="utf-8"))
    else:
        st.info("No hay informes diarios en informes/.")
