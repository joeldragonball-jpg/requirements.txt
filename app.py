import numpy as np
import pandas as pd
import plotly.graph_objects as go
import requests
import streamlit as st
import base64
import hashlib
import hmac
import html as html_lib
import threading
import time
from pathlib import Path

import streamlit.components.v1 as components
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from zoneinfo import ZoneInfo

try:
    import tomllib  # Python 3.11+
except ImportError:
    tomllib = None

ASSETS = Path(__file__).parent / "assets"   # icono del escudo (sin texto) para la pestaña y la cabecera
st.set_page_config(page_title="Mi Cartera Cripto", layout="wide",
                   page_icon=str(ASSETS / "icono.png") if (ASSETS / "icono.png").exists() else "⚡")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: calc(1.2rem + env(safe-area-inset-top, 0px)); padding-bottom: 2rem;}
    html, body {background-color: #0b0f17;}
    /* iOS amplia la pantalla al enfocar un campo con letra menor de 16 px (y no vuelve sola): se fija en 16 px */
    input, textarea, select {font-size: 16px !important;}
    [data-testid="stMetricValue"] {font-size: 1.45rem;}
    /* Tarjetas de indicadores: 5 en fila en ordenador, 2 por fila en el móvil */
    .kpis {display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin: 4px 0 4px;}
    .kpi {background: #141b29; border: 1px solid #25304a; border-radius: 14px; padding: 12px 14px;}
    .kpi .lbl {color: #9aa7c2; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em;}
    .kpi .val {color: #eef2fb; font-size: 1.4rem; font-weight: 700; line-height: 1.4; white-space: nowrap;}
    .kpi .dlt {font-size: 0.85rem; font-weight: 600;}
    .kpi.hero {grid-column: 1 / -1; background: linear-gradient(135deg, #19233a 0%, #141b29 70%); border-color: #2a3a5c; padding: 16px 18px;}
    .kpi.hero .val {font-size: 2.4rem; line-height: 1.2;}
    .meta {color: #6b7a99; font-size: 0.72rem; margin: 2px 2px 14px;}
    /* Menú principal: losetas cuadradas con icono grande (4 en ordenador, 2x2 en el móvil) */
    .st-key-grupo_menu_cerebro div[role="radiogroup"] {display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 8px; width: 100%;}
    .st-key-grupo_menu_cerebro div[role="radiogroup"] > label {flex-direction: column; justify-content: center; text-align: center;
                                                       min-height: 84px; border-radius: 14px; padding: 8px;}
    .st-key-grupo_menu_cerebro div[role="radiogroup"] > label p {font-size: 0.95rem; line-height: 1.35; text-align: center;}
    .st-key-grupo_menu_cerebro div[role="radiogroup"] > label p::first-line {font-size: 1.9rem;}
    /* Móvil/tablet: sin zoom al tocar dos veces ni al pellizcar los gráficos; el dedo desliza la página */
    html, body {touch-action: manipulation;}
    .js-plotly-plot, .js-plotly-plot * {touch-action: pan-y !important;}
    /* Menús como botones grandes (más fáciles de tocar que los círculos de radio) */
    div[role="radiogroup"] {gap: 6px; flex-wrap: wrap;}
    div[role="radiogroup"] > label {background: #141b29; border: 1px solid #25304a; border-radius: 10px; padding: 6px 12px;
                                    margin: 0 !important; min-height: 40px; align-items: center;}
    div[role="radiogroup"] > label:has(input:checked) {background: #19233a; border-color: #f1d58a;}
    div[role="radiogroup"] > label > div:first-child {display: none;}
    div[role="radiogroup"] > label p {margin: 0; font-weight: 600;}
    /* Menú del cerebro: 9 losetas, todas en una fila en pantallas anchas */
    @media (min-width: 900px) {
        .st-key-grupo_menu_cerebro div[role="radiogroup"] {grid-template-columns: repeat(9, minmax(0, 1fr));}
    }
    .st-key-noticias_vista [role="radiogroup"] {display: flex; flex-wrap: wrap; gap: 8px;}
    .st-key-noticias_vista label[data-testid="stRadioOption"] {width: auto; padding: 6px 14px;}
    /* Apartados del grupo: tarjetas en vertical con título y descripción */
    [class*="st-key-sub_"] div[role="radiogroup"] {display: flex; flex-direction: column; gap: 8px; width: 100%;}
    [class*="st-key-sub_"] div[role="radiogroup"] > label {width: 100%; justify-content: flex-start; padding: 10px 14px;
                                                          min-height: 58px; border-radius: 12px;}
    [class*="st-key-sub_"] div[role="radiogroup"] > label:has(input:checked) {background: #19233a; border-color: #6ea8ff;}
    [class*="st-key-sub_"] div[role="radiogroup"] > label p {text-align: left; font-size: 0.82rem; color: #9aa7c2; line-height: 1.4; font-weight: 400;}
    [class*="st-key-sub_"] div[role="radiogroup"] > label p strong {color: #eef2fb; font-size: 1rem; font-weight: 600;}
    /* Botón de ajustes pegado a la derecha, separado del título */
    [data-testid="stPopover"] {display: flex; justify-content: flex-end;}
    /* Pestañas: reparten el ancho (sin deslizar) */
    button[role="tab"] {flex: 1 1 0; padding: 10px 4px; justify-content: center; min-height: 46px; font-size: 0.9rem;}
    @media (max-width: 640px) {
        button[role="tab"] {font-size: 0.82rem; padding: 10px 2px;}
        .kpis {grid-template-columns: repeat(2, 1fr); gap: 8px;}
        .kpi .val {font-size: 1.2rem;}
        .kpi.hero .val {font-size: 2.1rem;}
        .st-key-grupo_menu_cerebro div[role="radiogroup"] {grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px;}
        .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] {padding: 6px 2px; min-height: 76px;}
        .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] p {font-size: 0.68rem; letter-spacing: -0.01em;}
        .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] p::first-line {font-size: 1.6rem;}
    }

    /* --- Opciones de los menús (selectores reales: label[data-testid="stRadioOption"]) --- */
    label[data-testid="stRadioOption"] {background: #141b29; border: 1px solid #25304a; border-radius: 12px; padding: 8px 14px;
                                        min-height: 44px; margin: 0 !important; box-sizing: border-box; width: 100%;}
    label[data-testid="stRadioOption"][data-selected="true"] {background: #19233a; border-color: #f1d58a;}
    label[data-testid="stRadioOption"][data-selected="true"] p {color: #f1d58a;}
    label[data-testid="stRadioOption"] > div > div:first-child {display: none;}           /* el círculo del radio */
    label[data-testid="stRadioOption"] p {margin: 0; font-weight: 600;}
    /* Cartera / Cerebro en una fila, sin ocupar todo el ancho */
    .st-key-seccion [role="radiogroup"] {display: flex; gap: 8px;}
    .st-key-seccion label[data-testid="stRadioOption"] {width: auto; padding: 6px 16px;}
    /* Losetas del menú principal */
    .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] {height: 100%; min-height: 84px; justify-content: center; text-align: center; padding: 6px 4px;}
    .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] > div {width: 100%; justify-content: center;}
    .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] p {text-align: center; font-size: 0.95rem; line-height: 1.35;}
    /* Tarjetas de los apartados */
    [class*="st-key-sub_"] label[data-testid="stRadioOption"] {min-height: 60px; justify-content: flex-start;}
    [class*="st-key-sub_"] label[data-testid="stRadioOption"][data-selected="true"] {background: #19233a; border-color: #6ea8ff;}
    [class*="st-key-sub_"] label[data-testid="stRadioOption"] p {text-align: left; font-size: 0.82rem; color: #9aa7c2; font-weight: 400; line-height: 1.4;}
    [class*="st-key-sub_"] label[data-testid="stRadioOption"] p strong {color: #eef2fb; font-size: 1rem; font-weight: 600;}
    [class*="st-key-sub_"] [role="radiogroup"] > div {width: 100%;}
    [class*="st-key-sub_"] label[data-testid="stRadioOption"] > div {width: 100%;}
    .st-key-grupo_menu_cerebro [role="radiogroup"] > div {width: 100%; height: 100%;}
    .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] p::first-line {font-size: 1.9rem;}
    /* Cabecera: título a la izquierda y ajustes a la derecha en la misma fila, también en el móvil */
    .st-key-cab [data-testid="stHorizontalBlock"] {flex-wrap: nowrap !important; align-items: center;}
    .st-key-cab [data-testid="stColumn"] {min-width: 0 !important;}
    .st-key-cab [data-testid="stColumn"]:first-child {flex: 1 1 auto !important; width: auto !important;}
    .st-key-cab [data-testid="stColumn"]:last-child {flex: 0 0 auto !important; width: auto !important;}
    /* MÓVIL (al final para que gane a las reglas generales): 4 losetas por fila, texto que cabe sin partirse */
    @media (max-width: 640px) {
        /* Safari de iPhone encogía el menú a su contenido: se fuerza el ancho completo y columnas con medida propia
           (ancho de pantalla menos los márgenes de 16 px a cada lado y los 3 huecos de 6 px) */
        .st-key-grupo_menu_cerebro, .st-key-grupo_menu_cerebro [data-testid="stRadio"] {width: 100% !important; max-width: 100% !important;}
        .st-key-grupo_menu_cerebro div[role="radiogroup"] {width: 100% !important; max-width: 100% !important; box-sizing: border-box;
                                                           grid-template-columns: repeat(4, calc((100vw - 50px) / 4)) !important;
                                                           justify-content: space-between !important; gap: 6px !important;}
        .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] {padding: 6px 0 !important; min-height: 76px !important;
                                                                       width: 100% !important; box-sizing: border-box;}
        .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] p {font-size: 0.76rem !important; letter-spacing: -0.02em !important;
                                                                         word-break: keep-all; overflow-wrap: normal;}
        .st-key-grupo_menu_cerebro label[data-testid="stRadioOption"] p::first-line {font-size: 1.6rem !important;}
    }
    </style>
""", unsafe_allow_html=True)

# Aspecto de terminal financiero (sobrio y denso; mismo color base que docs/movil). Va aparte y detrás del bloque anterior.
# No toca alturas ni safe-area de la página.
st.markdown("""
    <style>
    :root {--bg:#0b0f17; --panel:#141b29; --panel2:#19233a; --linea:#25304a; --txt:#eef2fb; --sub:#9aa7c2; --acc:#6ea8ff;
           --sube:#4fe3a1; --baja:#ff6b7d; --oro:#f1d58a; --r:20px;}
    .stApp {background: linear-gradient(180deg, var(--bg) 0, var(--bg) 16px, transparent 150px),
                        radial-gradient(900px 500px at 85% 6%, #1d2a52 0, transparent 60%),
                        radial-gradient(700px 400px at -10% 35%, #2a1d4a55 0, transparent 60%), var(--bg);}
    .block-container {max-width: 1200px;}
    @keyframes entra {from {opacity: 0; transform: translateY(8px)} to {opacity: 1; transform: none}}
    @media (prefers-reduced-motion: reduce) {* {animation: none !important; transition: none !important;}}

    /* Tarjetas como en docs/movil: degradado suave, borde fino, números grandes y poco por pantalla */
    .kpis {display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin: 4px 0;}
    .kpi {background: linear-gradient(160deg, var(--panel2), var(--panel)); border: 1px solid var(--linea); border-radius: var(--r);
          padding: 14px; animation: sube-card .5s cubic-bezier(.2,.8,.2,1) both; animation-delay: calc(var(--i, 0) * 70ms);}
    @keyframes sube-card {from {opacity: 0; transform: translateY(16px) scale(.98)} to {opacity: 1; transform: none}}
    .kpi .lbl {display: flex; justify-content: space-between; align-items: center; color: var(--sub); font-size: .72rem;
               letter-spacing: .08em; font-weight: 700; text-transform: uppercase;}
    .kpi .ic {width: 26px; height: 26px; border-radius: 9px; display: grid; place-items: center; background: #ffffff12; color: var(--oro);
              font-size: .8rem; letter-spacing: 0;}
    .kpi .val {color: var(--txt); font-size: 1.4rem; font-weight: 800; letter-spacing: -.02em; line-height: 1.2; margin: 6px 0 2px;
               font-variant-numeric: tabular-nums; white-space: nowrap;}
    .kpi .dlt {display: inline-block; padding: 1px 9px; border-radius: 999px; font-size: .78rem; font-weight: 700; font-variant-numeric: tabular-nums;}
    .kpi .dlt.up {background: #4fe3a122; color: var(--sube);} .kpi .dlt.dn {background: #ff6b7d22; color: var(--baja);}
    .kpi .val.up {color: var(--sube);} .kpi .val.dn {color: var(--baja);}
    .kpi.hero {grid-column: 1 / -1; background: linear-gradient(135deg, #2a3a78, #1b2347 60%, #2d1f55); border-color: #3c4d92; padding: 12px 16px;}
    .kpi.hero .lbl {color: #bcc7ec;}
    .kpi.hero .val {font-size: 2rem; font-weight: 800; letter-spacing: -.03em; margin: 2px 0 6px;}
    .kpi.hero .sub {display: flex; flex-wrap: wrap; gap: 6px;}
    .pill {display: inline-flex; padding: 3px 11px; border-radius: 999px; font-size: .78rem; font-weight: 700; background: #ffffff14;
           font-variant-numeric: tabular-nums;}
    .pill.up {background: #4fe3a122; color: var(--sube);} .pill.dn {background: #ff6b7d22; color: var(--baja);}
    .kpi.hero svg.spark {display: block; width: 100%; height: 28px; margin-top: 6px; overflow: visible;}
    .kpis-mini {display: flex; gap: 8px; margin: 2px 0 8px;}
    .kpis-mini .kpi {flex: 1 1 0; min-width: 0; padding: 8px 12px; border-radius: 16px;}
    .kpis-mini .kpi .val {font-size: 1rem; margin: 2px 0 0; overflow: hidden; text-overflow: ellipsis;}
    .kpis-mini .kpi .lbl {font-size: .6rem;} .kpis-mini .kpi .ic {display: none;}
    .meta {color: #6b7a99; font-size: .7rem;}
    @media (min-width: 900px) {.kpis {grid-template-columns: repeat(4, 1fr);}}
    /* Posiciones: tarjeta con avatar, importes y barra de peso */
    .pcard {background: linear-gradient(160deg, var(--panel2), var(--panel)); border: 1px solid var(--linea); border-radius: var(--r);
            padding: 14px; margin-bottom: 10px; animation: sube-card .5s cubic-bezier(.2,.8,.2,1) both; animation-delay: calc(var(--i, 0) * 70ms);}
    .pcard .fila {display: grid; grid-template-columns: 44px 1fr auto; gap: 12px; align-items: center;}
    .pcard .av {width: 44px; height: 44px; border-radius: 50%; display: grid; place-items: center; font-weight: 800; font-size: .8rem; color: #10131c;}
    .pcard h4 {margin: 0; font-size: 1rem; font-weight: 700; color: var(--txt);} .pcard p {margin: 2px 0 0; font-size: .8rem; color: var(--sub);}
    .pcard .der {text-align: right; font-weight: 800; font-variant-numeric: tabular-nums; color: var(--txt);}
    .pcard .der small {display: block; font-weight: 700; font-size: .8rem;}
    .pcard .der small.up {color: var(--sube);} .pcard .der small.dn {color: var(--baja);}
    .pcard .barra {height: 8px; border-radius: 8px; background: #ffffff12; overflow: hidden; margin-top: 10px;}
    .pcard .barra i {display: block; height: 100%; border-radius: 8px;}
    [data-testid="stMetric"] {background: linear-gradient(160deg, var(--panel2), var(--panel)); border: 1px solid var(--linea);
                              border-radius: 16px; padding: 10px 14px;}
    [data-testid="stMetricValue"] {font-variant-numeric: tabular-nums; font-weight: 800;}
    [data-testid="stMetricLabel"] p {text-transform: uppercase; letter-spacing: .08em; font-size: .7rem; color: var(--sub); font-weight: 700;}
    [data-testid="stPlotlyChart"] {background: linear-gradient(160deg, var(--panel2), var(--panel)); border: 1px solid var(--linea);
                                   border-radius: var(--r); padding: 8px 6px 2px;}
    [data-testid="stDataFrame"] {border: 1px solid var(--linea); border-radius: 16px; overflow: hidden;}
    [data-testid="stVerticalBlockBorderWrapper"] {border-radius: 18px; border-color: var(--linea);}
    .stMarkdown h5 {font-size: .76rem; font-weight: 700; text-transform: uppercase; letter-spacing: .12em; color: var(--sub); margin: 18px 4px 8px;}
    .stMarkdown h5 {border: 0; padding: 0;}
    .fecha-cab {color: var(--sub); font-size: .8rem; letter-spacing: .08em; text-transform: uppercase; margin: 0 0 6px; padding-left: 2px;}

    /* Barra inferior fija (como la versión móvil de docs/movil): iconos de línea, nombre debajo y raya dorada en el activo */
    .st-key-dest_menu, .stApp:has(.modo-barra) .st-key-seccion {position: fixed !important; left: 10px; right: 10px; bottom: calc(env(safe-area-inset-bottom, 0px) * .5 + 8px);
        z-index: 999; width: auto !important; max-width: 560px; margin: 0 auto !important; padding: 4px !important;
        background: #0d1320f2; -webkit-backdrop-filter: blur(16px); backdrop-filter: blur(16px);
        border: 1px solid #2a3858; border-radius: 22px; box-shadow: 0 10px 30px #000000b0, inset 0 1px 0 #ffffff12;}
    .st-key-dest_menu [data-testid="stRadio"], .st-key-dest_menu [role="radiogroup"],
    .stApp:has(.modo-barra) .st-key-seccion [role="radiogroup"] {width: 100%; max-width: 640px; margin: 0 auto;}
    .st-key-dest_menu [role="radiogroup"], .stApp:has(.modo-barra) .st-key-seccion [role="radiogroup"] {display: grid !important;
        grid-template-columns: repeat(var(--n, 5), minmax(0, 1fr)); gap: 0;}
    .st-key-dest_menu label[data-testid="stRadioOption"], .stApp:has(.modo-barra) .st-key-seccion label[data-testid="stRadioOption"] {background: none !important; border: 0 !important; border-radius: 0; min-height: 46px; padding: 5px 0 3px !important; display: flex !important;
        width: 100% !important; flex-direction: column; justify-content: center; align-items: center; gap: 2px; text-align: center; position: relative; border-radius: 18px !important;}
    .st-key-dest_menu label[data-testid="stRadioOption"]::before, .stApp:has(.modo-barra) .st-key-seccion label[data-testid="stRadioOption"]::before {content: ""; display: block; width: 22px; height: 22px; background: currentColor;
        -webkit-mask: center / contain no-repeat; mask: center / contain no-repeat; transition: transform .25s;}
    .st-key-dest_menu label[data-testid="stRadioOption"], .stApp:has(.modo-barra) .st-key-seccion label[data-testid="stRadioOption"] {color: var(--sub);}
    .st-key-dest_menu label[data-testid="stRadioOption"] > div, .stApp:has(.modo-barra) .st-key-seccion label[data-testid="stRadioOption"] > div {width: 100%; justify-content: center;}
    .st-key-dest_menu label[data-testid="stRadioOption"] p, .stApp:has(.modo-barra) .st-key-seccion label[data-testid="stRadioOption"] p {font-size: .64rem; font-weight: 600; color: inherit; text-align: center; line-height: 1.15; letter-spacing: 0;
        word-break: keep-all; overflow-wrap: normal;}
    .st-key-dest_menu label[data-testid="stRadioOption"][data-selected="true"], .stApp:has(.modo-barra) .st-key-seccion label[data-testid="stRadioOption"][data-selected="true"] {color: var(--oro);}
    .st-key-dest_menu label[data-testid="stRadioOption"][data-selected="true"]::before, .stApp:has(.modo-barra) .st-key-seccion label[data-testid="stRadioOption"][data-selected="true"]::before {transform: scale(1.1);}
    .st-key-dest_menu label[data-testid="stRadioOption"][data-selected="true"], .stApp:has(.modo-barra) .st-key-seccion label[data-testid="stRadioOption"][data-selected="true"] {background: #f1d58a1c !important; box-shadow: inset 0 0 0 1px #f1d58a33;}
    .st-key-dest_menu [role="radiogroup"] > div:nth-child(1) label[data-testid="stRadioOption"]::before {-webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 11l9-8 9 8v9a1 1 0 01-1 1h-5v-6H9v6H4a1 1 0 01-1-1z'/%3E%3C/svg%3E"); mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 11l9-8 9 8v9a1 1 0 01-1 1h-5v-6H9v6H4a1 1 0 01-1-1z'/%3E%3C/svg%3E");}
    .st-key-dest_menu [role="radiogroup"] > div:nth-child(2) label[data-testid="stRadioOption"]::before {-webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='6' width='18' height='14' rx='3'/%3E%3Cpath d='M3 10h18M16 15h2'/%3E%3C/svg%3E"); mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='6' width='18' height='14' rx='3'/%3E%3Cpath d='M3 10h18M16 15h2'/%3E%3C/svg%3E");}
    .st-key-dest_menu [role="radiogroup"] > div:nth-child(3) label[data-testid="stRadioOption"]::before {-webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 17l5-5 4 4 8-9'/%3E%3Cpath d='M15 7h5v5'/%3E%3C/svg%3E"); mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 17l5-5 4 4 8-9'/%3E%3Cpath d='M15 7h5v5'/%3E%3C/svg%3E");}
    .st-key-dest_menu [role="radiogroup"] > div:nth-child(4) label[data-testid="stRadioOption"]::before {-webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 4h11a3 3 0 013 3v13H7a3 3 0 01-3-3V5a1 1 0 011-1z'/%3E%3Cpath d='M8 9h8M8 13h8M8 17h5'/%3E%3C/svg%3E"); mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 4h11a3 3 0 013 3v13H7a3 3 0 01-3-3V5a1 1 0 011-1z'/%3E%3Cpath d='M8 9h8M8 13h8M8 17h5'/%3E%3C/svg%3E");}
    .st-key-dest_menu [role="radiogroup"] > div:nth-child(5) label[data-testid="stRadioOption"]::before {-webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='5' cy='12' r='1.5'/%3E%3Ccircle cx='12' cy='12' r='1.5'/%3E%3Ccircle cx='19' cy='12' r='1.5'/%3E%3C/svg%3E"); mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='5' cy='12' r='1.5'/%3E%3Ccircle cx='12' cy='12' r='1.5'/%3E%3Ccircle cx='19' cy='12' r='1.5'/%3E%3C/svg%3E");}
    .stApp:has(.modo-barra) .st-key-seccion [role="radiogroup"] > div:nth-child(1) label[data-testid="stRadioOption"]::before {-webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='6' width='18' height='14' rx='3'/%3E%3Cpath d='M3 10h18M16 15h2'/%3E%3C/svg%3E"); mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='6' width='18' height='14' rx='3'/%3E%3Cpath d='M3 10h18M16 15h2'/%3E%3C/svg%3E");}
    .stApp:has(.modo-barra) .st-key-seccion [role="radiogroup"] > div:nth-child(2) label[data-testid="stRadioOption"]::before {-webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M9 4a3 3 0 00-3 3 3 3 0 00-2 5 3 3 0 002 5 3 3 0 006 0V4a3 3 0 00-3 0zM15 4a3 3 0 013 3 3 3 0 012 5 3 3 0 01-2 5 3 3 0 01-6 0'/%3E%3C/svg%3E"); mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M9 4a3 3 0 00-3 3 3 3 0 00-2 5 3 3 0 002 5 3 3 0 006 0V4a3 3 0 00-3 0zM15 4a3 3 0 013 3 3 3 0 012 5 3 3 0 01-2 5 3 3 0 01-6 0'/%3E%3C/svg%3E");}
    .stApp:has(.modo-barra) .st-key-seccion [role="radiogroup"] > div:nth-child(3) label[data-testid="stRadioOption"]::before {-webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='5' width='18' height='16' rx='3'/%3E%3Cpath d='M8 3v4M16 3v4M3 10h18'/%3E%3C/svg%3E"); mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='5' width='18' height='16' rx='3'/%3E%3Cpath d='M8 3v4M16 3v4M3 10h18'/%3E%3C/svg%3E");}
    .stApp:has(.modo-barra) .st-key-seccion [role="radiogroup"] > div:nth-child(4) label[data-testid="stRadioOption"]::before {-webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='5' y='11' width='14' height='10' rx='2'/%3E%3Cpath d='M8 11V8a4 4 0 018 0v3'/%3E%3C/svg%3E"); mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='5' y='11' width='14' height='10' rx='2'/%3E%3Cpath d='M8 11V8a4 4 0 018 0v3'/%3E%3C/svg%3E");}
    .block-container {padding-bottom: 92px;}
    @media (max-width: 640px) {
        .kpi .val {font-size: 1.3rem;} .kpi.hero .val {font-size: 1.85rem;}
        .kpis-mini .kpi .val {font-size: .92rem;}
    }
    .st-key-pill_menu [role="radiogroup"] {display: flex !important; flex-wrap: nowrap !important; overflow-x: auto; gap: 8px;
                                           padding: 2px 2px 8px; scrollbar-width: none; -webkit-overflow-scrolling: touch;}
    .st-key-pill_menu [role="radiogroup"]::-webkit-scrollbar {display: none;}
    .st-key-pill_menu label[data-testid="stRadioOption"] {flex: none; width: auto !important; min-height: 38px; padding: 7px 16px;
                                  border-radius: 999px; background: var(--panel); border-color: var(--linea); transition: all .2s;}
    .st-key-pill_menu label[data-testid="stRadioOption"] p {font-size: .86rem; font-weight: 600; color: var(--sub); white-space: nowrap;}
    .st-key-pill_menu label[data-testid="stRadioOption"][data-selected="true"] {background: var(--oro); border-color: var(--oro);}
    .st-key-pill_menu label[data-testid="stRadioOption"][data-selected="true"] p {color: #241b00;}
    .st-key-pill_menu [role="radiogroup"] > div {width: auto;}
    /* Cambio de sección (Cerebro, Seguimiento, Privado) */
    .st-key-seccion [role="radiogroup"] {display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px;}
    .st-key-seccion label[data-testid="stRadioOption"] {width: 100%; min-height: 52px; justify-content: center;}
    /* Densidad: menos aire y más ancho útil (también en el iPhone) */
    [data-testid="stVerticalBlock"] {gap: .6rem;}
    .block-container {padding-top: calc(.5rem + env(safe-area-inset-top, 0px)) !important; padding-bottom: 104px;}
    .st-key-cab {min-height: 52px;}
    .st-key-cab h1 {font-size: 1.3rem !important; line-height: 1.2 !important; margin: 0 !important; padding: 0 !important;}
    .kpi:not(.hero) {padding: 8px 12px;}
    .kpi:not(.hero) .lbl {font-size: .64rem;} .kpi:not(.hero) .ic {width: 20px; height: 20px; border-radius: 7px; font-size: .68rem;}
    .kpi:not(.hero) .val {display: inline-block; font-size: 1.15rem; margin: 2px 6px 0 0;}
    .kpi:not(.hero) .dlt {display: inline-block; padding: 0 8px; font-size: .72rem;}
    .kpi.hero {padding: 10px 14px;} .kpi.hero .val {font-size: 1.75rem; margin: 0 0 4px;} .kpi.hero svg.spark {height: 22px; margin-top: 4px;}
    .kpis {gap: 8px;}
    .pcard {padding: 10px 12px; margin-bottom: 8px;} .pcard .fila {grid-template-columns: 34px 1fr auto; gap: 10px;}
    .pcard .av {width: 34px; height: 34px; font-size: .68rem;} .pcard h4 {font-size: .95rem;} .pcard p {font-size: .74rem;}
    .pcard .barra {height: 5px; margin-top: 8px;}
    [data-testid="stVerticalBlockBorderWrapper"] {overflow-x: hidden;}
    [data-testid="stMetricLabel"], [data-testid="stMetricValue"], [data-testid="stMetricDelta"] {max-width: 100%;}
    [data-testid="stMetricValue"] div, [data-testid="stMetricLabel"] p {overflow: hidden; text-overflow: ellipsis;}
    /* Aviso de bots: punto pequeño que abre el detalle al tocarlo */
    details.bots {margin: 0 0 4px;}
    details.bots summary {list-style: none; display: inline-block; padding: 2px 10px; border-radius: 999px; background: #ffb15c1f;
                          color: #ffb15c; font-size: .78rem; font-weight: 700; cursor: pointer;}
    details.bots summary::-webkit-details-marker {display: none;}
    details.bots div {margin-top: 6px; font-size: .78rem; color: var(--sub);}
    @media (max-width: 640px) {
        .block-container {padding-left: 14px !important; padding-right: 14px !important;}
        /* Filas de indicadores (st.metric): 2 por fila en el móvil en vez de una debajo de otra */
        [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"] > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"] > [data-testid="stMetric"]) {
            flex-wrap: wrap !important; gap: 8px !important;}
        [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"] > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"] > [data-testid="stMetric"]) > [data-testid="stColumn"] {
            flex: 0 0 calc(50% - 4px) !important; min-width: 0 !important; width: calc(50% - 4px) !important;}
        [data-testid="stMetric"] {padding: 6px 10px;}
        [data-testid="stMetricValue"] {font-size: 1.1rem;}
        [data-testid="stMetricLabel"] p {font-size: .62rem;}
        [data-testid="stMetricDelta"] {font-size: .7rem;}
    }
    /* ===== Paneles grandes agrupados (listas tipo iOS): un panel por tema, sin tarjetas dentro de tarjetas ===== */
    :root {--card: #141b29; --card2: #19233a; --azul: #6ea8ff;}
    @property --cnt {syntax: '<integer>'; initial-value: 0; inherits: false;}
    @keyframes sube {from {opacity: 0; transform: translateY(18px) scale(.98)} to {opacity: 1; transform: none}}
    @keyframes cuenta {from {--cnt: 0} to {--cnt: var(--fin)}}
    @keyframes oculta {to {visibility: hidden}}
    @keyframes aparece {from {opacity: 0} to {opacity: 1}}
    @keyframes crece {from {width: 0}}
    .panel {background: linear-gradient(160deg, var(--card2), var(--card)); border: 1px solid var(--linea); border-radius: 20px;
            padding: 14px 16px; margin-bottom: 12px;}
    .panel.anim {animation: sube .5s cubic-bezier(.2,.8,.2,1) both; animation-delay: calc(var(--i, 0) * 70ms);}
    .panel .tit {color: var(--sub); font-size: .8rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase;}
    .panel .gran {color: var(--txt); font-size: 2.2rem; font-weight: 800; letter-spacing: -.03em; line-height: 1.15; margin: 2px 0 0;
                  font-variant-numeric: tabular-nums;}
    .panel svg.spark {display: block; width: 100%; height: 26px; margin-top: 6px; overflow: visible;}
    .panel .rejilla {display: grid; grid-template-columns: 1fr 1fr; margin-top: 10px;}
    .panel .m {padding: 9px 0 2px; border-top: 1px solid var(--linea);}
    .panel .m:nth-child(odd) {padding-right: 12px;}
    .panel .m:nth-child(even) {padding-left: 12px; border-left: 1px solid var(--linea);}
    .panel .m .l {color: var(--sub); font-size: .72rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase;}
    .panel .m .v {color: var(--txt); font-size: 1.2rem; font-weight: 800; letter-spacing: -.02em; font-variant-numeric: tabular-nums; white-space: nowrap;}
    .panel .m .d {font-size: .8rem; font-weight: 700; font-variant-numeric: tabular-nums;}
    .panel .up {color: var(--sube);} .panel .dn {color: var(--baja);} .panel .nu {color: var(--sub);}
    .panel .fila {display: grid; grid-template-columns: 34px 1fr auto; gap: 10px; align-items: center; padding: 10px 0 8px; border-top: 1px solid var(--linea);}
    .panel .fila:first-of-type {border-top: 0; padding-top: 2px;}
    .panel .av {width: 34px; height: 34px; border-radius: 50%; display: grid; place-items: center; font-weight: 800; font-size: .68rem; color: #10131c;}
    .panel .fila h4 {margin: 0; font-size: .95rem; font-weight: 700; color: var(--txt);} .panel .fila p {margin: 1px 0 0; font-size: .78rem; color: var(--sub);}
    .panel .der {text-align: right; font-weight: 800; font-variant-numeric: tabular-nums; color: var(--txt);}
    .panel .der small {display: block; font-weight: 700; font-size: .8rem;}
    .panel .barra {grid-column: 1 / -1; height: 5px; border-radius: 5px; background: #ffffff12; overflow: hidden;}
    .panel .barra i {display: block; height: 100%; border-radius: 5px;}
    .panel.anim .barra i {animation: crece 1s cubic-bezier(.2,.8,.2,1) both;}
    /* Número que cuenta hasta su valor (sin JavaScript): al terminar se enseña el texto final con su formato */
    .cu {display: inline-grid;} .cu > * {grid-area: 1 / 1;}
    .cu .c {counter-reset: n var(--cnt); animation: cuenta .9s cubic-bezier(.2,.8,.2,1) both, oculta 0s linear .9s forwards;}
    .cu .c::after {content: var(--pre, "") counter(n) var(--suf, "");}
    .cu .f {animation: aparece 0s linear .9s both;}
    @media (prefers-reduced-motion: reduce) {.cu .c {display: none;}}
    /* Paneles de Streamlit (contenedores con borde) con el mismo aspecto; las métricas dentro van planas, separadas por líneas */
    [data-testid="stVerticalBlockBorderWrapper"] {background: linear-gradient(160deg, var(--card2), var(--card)); border-radius: 20px;}
    [data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMetric"] {background: none; border: 0; border-radius: 0; padding: 8px 0 2px;
                                                                           border-top: 1px solid var(--linea);}
    /* Espacio: escala 4/8/12/16 */
    [data-testid="stVerticalBlock"] {gap: .75rem;}
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {margin: 0; padding: .25rem 0;}
    [data-testid="stMarkdownContainer"] p {margin-bottom: .4rem;}
    hr {margin: .75rem 0 !important;}
    .stMarkdown h5 {font-size: .8125rem; letter-spacing: .1em; margin: 16px 4px 8px;}
    .block-container {max-width: 1100px; padding-bottom: 96px;}
    @media (max-width: 640px) {.block-container {padding-left: 16px !important; padding-right: 16px !important;}}
    /* Barra inferior: fondo y borde de la paleta */
    .st-key-dest_menu, .stApp:has(.modo-barra) .st-key-seccion {background: rgba(13,19,32,.93); border-color: var(--linea);}
    /* Sin huecos fantasma arriba: los elementos de 0 px (estilos, componentes con script) no deben sumar el hueco entre bloques */
    [data-testid="stElementContainer"][height="0px"] {position: absolute; width: 1px; height: 0; overflow: hidden;}
    [data-testid="stElementContainer"]:has(style):not(:has(p, span, svg, img, table, details, ul, ol, h1, h2, h3, h4, h5, h6, .panel, .kpis, .meta, .fecha-cab, .pcard)) {display: none;}
    .meta {margin: -6px 2px 0;}
    .stMarkdown h5 {margin: 10px 4px 6px;}
    /* Indicadores de Cartera: todos del mismo alto para que las filas queden alineadas */
    [data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMetric"] {min-height: 88px;}
    /* Cartera: el panel de cada token (contenedor con clave), métricas planas y del mismo alto, custodia compacta */
    [class*="st-key-pos_"] {background: linear-gradient(160deg, var(--card2), var(--card)); border: 1px solid var(--linea) !important;
                            border-radius: 20px !important; padding: 14px 16px !important; gap: .5rem;}
    [data-testid="stMetric"] {background: none !important; border: 0 !important; border-radius: 0 !important; border-top: 1px solid var(--linea) !important;
                              padding: 10px 0 6px !important; min-height: 96px;}
    @media (max-width: 640px) {
        [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"] > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"] > [data-testid="stMetric"]) > [data-testid="stColumn"]:nth-child(even) [data-testid="stMetric"] {
            border-left: 1px solid var(--linea) !important; padding-left: 12px !important;}
        [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"] > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"] > [data-testid="stMetric"]) {gap: 0 !important;}
        [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"] > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"] > [data-testid="stMetric"]) > [data-testid="stColumn"] {
            flex: 0 0 50% !important; width: 50% !important;}
    }
    .cust {margin-top: 6px;} .cust .tit {color: var(--sub); font-size: .75rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; margin-bottom: 4px;}
    .cust .cr {display: flex; justify-content: space-between; gap: 8px; font-size: .85rem; color: var(--txt); margin-top: 8px;}
    .cust .cr span:last-child {color: var(--sub); text-align: right; font-variant-numeric: tabular-nums;}
    .cust .cb {height: 5px; border-radius: 5px; background: #ffffff12; overflow: hidden; margin-top: 4px;}
    .cust .cb i {display: block; height: 100%; border-radius: 5px; background: var(--oro);}
    </style>
""", unsafe_allow_html=True)


def candado():
    """Contraseña de la app: la misma APP_CLAVE del chat (Settings → Secrets de Streamlit). Si no existe, la app queda
    abierta como antes. Al acertarla, la dirección lleva una huella (?k=...): si guardas esa dirección en favoritos no te
    la vuelve a pedir, ni al recargar ni cuando la pestaña se reconecta. La huella no revela la contraseña (es un HMAC),
    pero quien tenga la dirección completa entra: no la compartas. Para anular todas las huellas, cambia APP_CLAVE."""
    try:
        clave = st.secrets.get("APP_CLAVE")
    except Exception:
        clave = None
    if not clave:
        return
    clave = str(clave)
    huella = hmac.new(clave.encode(), b"cartera-app-v1", hashlib.sha256).hexdigest()[:32]
    if st.session_state.get("app_ok") or hmac.compare_digest(str(st.query_params.get("k", "")).encode(), huella.encode()):
        st.session_state["app_ok"] = True
        if st.session_state.pop("app_aviso", False):
            st.toast("Guarda esta página en favoritos tal cual: la dirección ya lleva tu acceso y no te pedirá la contraseña.",
                     icon="🔖")
        return
    _, centro, _ = st.columns([1, 2, 1])
    with centro:
        grande = ASSETS / "icono-oscuro-256.png"
        if grande.exists():
            b64 = base64.b64encode(grande.read_bytes()).decode()
            st.markdown('<div style="text-align:center;margin:7vh 0 4px">'
                        f'<img src="data:image/png;base64,{b64}" style="width:clamp(140px,40vw,200px)"></div>',
                        unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;font-size:clamp(1.6rem,6vw,2.1rem);font-weight:700;line-height:1.2">'
                    'Mi Cartera Cripto</div>'
                    '<div style="text-align:center;color:#9aa7c2;margin:6px 0 18px">🔒 Acceso privado</div>',
                    unsafe_allow_html=True)
        intento = st.text_input("Contraseña", type="password", key="app_clave_input",
                                placeholder="Contraseña", label_visibility="collapsed")
        if intento:
            if hmac.compare_digest(intento.encode(), clave.encode()):
                st.session_state["app_ok"] = True
                st.session_state["app_aviso"] = True
                st.query_params["k"] = huella
                st.rerun()
            time.sleep(1)   # frena los intentos seguidos
            st.error("Contraseña incorrecta.")
    listo()   # la pantalla de contraseña ya está dibujada: la página de entrada puede retirarse
    st.stop()


def ajustes_movil():
    """Streamlit no deja tocar la cabecera de la página, así que se añaden con JavaScript (misma web, mismo origen):
    - theme-color y estilo de la barra de estado: en iPhone la franja de arriba salía blanca sobre el fondo negro.
    - icono de la pantalla de inicio (apple-touch-icon) con el escudo, para cuando guardas la app como acceso directo.
    Si algo falla, no pasa nada: la app funciona igual (solo se ve la franja blanca de siempre)."""
    icono = "https://raw.githubusercontent.com/joeldragonball-jpg/requirements.txt/main/assets/icono-180.png"
    try:
        components.html("""<script>
    (function () {
      /* Abierta desde la página de entrada (via=shell, dentro de un marco): Streamlit la envuelve en otra página que añade una
         barra "Built with Streamlit" abajo y un margen de 2 px. Esa envoltura es del mismo origen que la app, así que se
         puede retocar desde aquí: se oculta la barra y el marco ocupa la pantalla entera, sin recortar nada. */
      try {
        var via = new URL(window.parent.location.href).searchParams.get('via');
        var w = window.parent.parent.document;
        if (via === 'shell' && w && !w.getElementById('ajuste-marco')) {
          var s = w.createElement('style'); s.id = 'ajuste-marco';
          s.textContent = 'html, body { background: #0b0f17 !important; }'
            + '[class*="_stateContainer_"] { position: fixed !important; inset: 0 !important; width: 100% !important; height: 100% !important; margin: 0 !important; padding: 0 !important; }'
            + '[class*="_stateContainer_"] iframe, iframe[class*="_iframe_"] { width: 100% !important; height: 100% !important; border: 0 !important; }'
            + '[class*="_container_"]:has([class*="_hostedName_"]) { display: none !important; }';
          w.head.appendChild(s);
          /* respaldo para navegadores sin :has() — oculta el contenedor fijo que contiene el texto del pie */
          [].slice.call(w.querySelectorAll('[class*="_hostedName_"]')).forEach(function (e) {
            var p = e; while (p && p !== w.body && w.defaultView.getComputedStyle(p).position !== 'fixed') p = p.parentElement;
            if (p && p !== w.body) p.style.display = 'none';
          });
        }
      } catch (e) {}
      var docs = [];
      try { docs.push(window.parent.document); } catch (e) {}
      try { if (window.top !== window.parent) docs.push(window.top.document); } catch (e) {}
      docs.forEach(function (d) {
        try {
          function meta(n, c) { var m = d.querySelector('meta[name="' + n + '"]');
            if (!m) { m = d.createElement('meta'); m.setAttribute('name', n); d.head.appendChild(m); } m.setAttribute('content', c); }
          meta('theme-color', '#0b0f17'); meta('color-scheme', 'dark');
          meta('apple-mobile-web-app-capable', 'yes'); meta('mobile-web-app-capable', 'yes');
          meta('apple-mobile-web-app-status-bar-style', 'black-translucent'); meta('apple-mobile-web-app-title', 'Cartera');
          var l = d.querySelector('link[rel="apple-touch-icon"]');
          if (!l) { l = d.createElement('link'); l.setAttribute('rel', 'apple-touch-icon'); d.head.appendChild(l); }
          l.setAttribute('href', '""" + icono + """'); l.setAttribute('sizes', '180x180');
          var vp = d.querySelector('meta[name="viewport"]');
          if (vp && vp.content.indexOf('viewport-fit') < 0) vp.setAttribute('content', vp.content + ', viewport-fit=cover');
          d.documentElement.style.backgroundColor = '#0b0f17';
          if (d.body) d.body.style.backgroundColor = '#0b0f17';
        } catch (e) {}
      });
    })();
    </script>""", height=0)
    except Exception:   # los ajustes del móvil son un extra: si fallan, la app funciona igual
        pass


def listo():
    """Avisa a la página de entrada (docs/index.html) de que la app ya está lista, para que retire su pantalla de carga.
    Si la app se abre directamente, el aviso no tiene efecto. Incluye la huella ?k para poder guardarla en favoritos."""
    try:
        components.html("""<script>try {
          var k = new URL(window.parent.location.href).searchParams.get('k');
          window.top.postMessage({tipo: 'cartera-listo', k: k}, '*');
        } catch (e) {}</script>""", height=0)
    except Exception:
        pass


if str(st.query_params.get("via", "")) == "shell":
    # Abierta desde la página de entrada (dentro de un marco): ella ya reserva el espacio de la barra de estado del iPhone
    st.markdown("<style>.block-container{padding-top:.5rem !important}"
                # el marco ya llega al borde de la pantalla: la barra flotante baja sin depender de la zona segura (env), que ahí no es fiable
                ".st-key-dest_menu, .stApp:has(.modo-barra) .st-key-seccion {bottom: 10px !important}</style>", unsafe_allow_html=True)
ajustes_movil()
candado()

# Secciones: la app desplegada solo enseña la cartera (con sus noticias). Cerebro, Seguimiento y Privado salen en tu
# ordenador (donde existe la carpeta privado/, que no se sube) o si pones MOSTRAR_CEREBRO = true en los Secrets.
import privado_vista
_LOCAL = privado_vista.disponible()
try:
    _CEREBRO_PUBLICO = bool(st.secrets.get("MOSTRAR_CEREBRO"))
except Exception:
    _CEREBRO_PUBLICO = False
try:
    _HAY_HOJA = bool(st.secrets.get("SHEET_ID"))
except Exception:
    _HAY_HOJA = False
_SECCIONES = []
if _HAY_HOJA or not _LOCAL:          # en tu PC sin la hoja de la cartera (sin el secreto SHEET_ID) no hay cartera que mostrar
    _SECCIONES.append("📊 Cartera")
if _LOCAL or _CEREBRO_PUBLICO:
    _SECCIONES += ["🧠 Cerebro", "📌 Seguimiento"]
if _LOCAL:
    _SECCIONES += ["🔒 Privado"]
if not _SECCIONES:
    _SECCIONES = ["📊 Cartera"]
if st.session_state.get("seccion") not in _SECCIONES:
    st.session_state.pop("seccion", None)
seccion = st.session_state.get("seccion", _SECCIONES[0])


def menu_secciones():
    """Menú de secciones (Cartera, Cerebro, Seguimiento, Privado). En Cerebro, Seguimiento y Privado es la barra inferior fija;
    en la Cartera va dentro de «Más» como tarjetas (la barra de abajo es la de los destinos de la cartera)."""
    if len(_SECCIONES) > 1:
        en_barra = seccion != "📊 Cartera"
        if en_barra:
            st.markdown(f"<div class='modo-barra' style='display:none'></div><style>.st-key-seccion{{--n:{len(_SECCIONES)}}}</style>",
                        unsafe_allow_html=True)
        nueva = st.radio("Sección", _SECCIONES, horizontal=True, label_visibility="collapsed", key="seccion",
                         format_func=(lambda t: t.split(" ", 1)[1]) if en_barra else str)
        if nueva != seccion:
            st.rerun()


if seccion == "🔒 Privado":
    import importlib
    importlib.reload(privado_vista)
    privado_vista.mostrar()
    menu_secciones()
    listo()
    st.stop()
if seccion == "📌 Seguimiento":
    import importlib
    import seguimiento
    importlib.reload(seguimiento)
    seguimiento.mostrar()
    menu_secciones()
    listo()
    st.stop()
if seccion == "🧠 Cerebro":
    import importlib
    import cerebro
    importlib.reload(cerebro)  # así siempre usa la última versión de cerebro.py subida a GitHub
    cerebro.mostrar()
    menu_secciones()
    listo()
    st.stop()

# =============================================================================
# CONFIGURACIÓN — para añadir un token nuevo basta con añadir una línea a TOKENS
# =============================================================================
# El identificador de la hoja es privado (el repo es público): está en los Secrets de Streamlit como SHEET_ID
try:
    SHEET_ID = st.secrets["SHEET_ID"]
except Exception:
    st.error("Falta el secreto SHEET_ID en Streamlit (Manage app → Settings → Secrets).")
    st.stop()
SHEET_BASE = f"https://docs.google.com/spreadsheets/d/e/{SHEET_ID}/pub?single=true&output=csv&gid="
GID_RESUMEN = "1415212158"

TOKENS = {
    "XRP": {"gid": "2015592342", "kraken": "XRPEUR", "coingecko": "ripple", "color": "#6ea8ff"},
    "XLM": {"gid": "108352087", "kraken": "XLMEUR", "coingecko": "stellar", "color": "#4fe3a1"},
}
COLD_WALLETS = {"LEDGER"}  # el resto se considera custodia en exchange
# Noticias que guarda el bot (noticias/noticias.py) en la rama 'datos' del repositorio
NOTICIAS_URL = "https://raw.githubusercontent.com/joeldragonball-jpg/requirements.txt/datos/noticias/noticias.json"
# Configuración del bot de alertas (para mostrar tus niveles en la app)
ALERTAS_URL = "https://raw.githubusercontent.com/joeldragonball-jpg/requirements.txt/main/alertas/config.toml"
MADRID = ZoneInfo("Europe/Madrid")

POS, NEG, MUTED, GRID = "#4fe3a1", "#ff6b7d", "#9aa7c2", "rgba(37,48,74,.55)"
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
MESES_CORTOS = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

# Streamlit >= 1.49 sustituye use_container_width por width="stretch"
_NEW_ST = tuple(int(p) for p in st.__version__.split(".")[:2]) >= (1, 49)
WIDE = {"width": "stretch"} if _NEW_ST else {"use_container_width": True}
PLOT_CFG = {"displayModeBar": False, "scrollZoom": False, "doubleClick": False, "showTips": False}


# =============================================================================
# FORMATO (estilo español: 1.234,56 €)
# =============================================================================
def fmt(x, dec=2, sign=False):
    if x is None or pd.isna(x):
        return "—"
    s = f"{x:{'+' if sign else ''},.{dec}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def eur(x, dec=2, sign=False):
    return "—" if x is None or pd.isna(x) else fmt(x, dec, sign) + " €"


def pct(x, dec=2, sign=True):
    return "—" if x is None or pd.isna(x) else fmt(x, dec, sign) + " %"


def enlace(titulo, url):
    """Enlace Markdown seguro con texto que viene de internet: sin HTML y solo direcciones http(s)."""
    texto = html_lib.escape(str(titulo)).replace("$", r"\$").replace("[", "(").replace("]", ")")
    url = str(url or "")
    if not url.startswith(("https://", "http://")):
        return texto
    return f"[{texto}]({url.replace('(', '%28').replace(')', '%29').replace(' ', '%20')})"


def color_sign(v):
    if v is None or pd.isna(v) or v == 0:
        return ""
    return f"color: {POS}" if v > 0 else f"color: {NEG}"


def style_fig(fig, height=360):
    fig.update_layout(
        template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=height, margin=dict(l=10, r=10, t=30, b=10), hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        separators=",.",
        hoverlabel=dict(bgcolor="#19233a", bordercolor="#25304a", font=dict(color="#eef2fb")),
        font=dict(family="system-ui, -apple-system, Segoe UI, Roboto, sans-serif", color="#9aa7c2"),
    )
    fig.update_xaxes(showgrid=True, gridcolor="rgba(37,48,74,.4)", gridwidth=1, title=None, fixedrange=True, showline=True, linecolor="#25304a",
                     ticks="outside", tickcolor="#25304a", tickfont=dict(size=11), showspikes=True, spikemode="across",
                     spikethickness=1, spikecolor="#4b5a7a", spikedash="dot")   # fixedrange: sin zoom con los dedos
    fig.update_yaxes(gridcolor=GRID, gridwidth=1, title=None, fixedrange=True, zeroline=True, zerolinecolor="#25304a",
                     tickfont=dict(size=11))
    fig.update_layout(dragmode=False)
    return fig


def chart(fig):
    st.plotly_chart(fig, theme=None, config=PLOT_CFG, **WIDE)


# =============================================================================
# LECTURA DE DATOS
# =============================================================================
def parse_num(x):
    """Convierte '1.234,56 €', '12,01%', '30' o '0.5' en float."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return np.nan
    if isinstance(x, (int, float, np.number)):
        return float(x)
    s = str(x).replace("€", "").replace("%", "").replace("\xa0", "").replace(" ", "").strip()
    if s in ("", "-", "nan"):
        return np.nan
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    elif "." in s:
        # Sin coma: '1.234' es separador de miles, pero '0.5' es decimal
        entero, dec = s.lstrip("-").split(".")
        if len(dec) == 3 and entero not in ("", "0"):
            s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return np.nan


def to_num(series):
    return series.map(parse_num).astype(float)


# Las hojas de Google se releen cada 30 min (tus movimientos son pocos al día); tras anotar uno, ⚙️ → «Actualizar datos» las relee al momento.
@st.cache_data(ttl=1800, show_spinner=False)
def fetch_sheet(gid):
    return pd.read_csv(SHEET_BASE + gid, header=None, dtype=str, on_bad_lines="skip")


def table_from_raw(raw, must_have):
    """Busca la fila de cabecera (la que contiene todas las palabras clave) y devuelve la tabla."""
    for i, row in raw.iterrows():
        txt = " ".join(row.fillna("").astype(str)).upper()
        if all(k in txt for k in must_have):
            df = raw.iloc[i + 1:].copy()
            df.columns = [str(c).strip() if pd.notna(c) and str(c).strip() else f"_col{j}"
                          for j, c in enumerate(row)]
            return df.reset_index(drop=True)
    return pd.DataFrame()


def find_col(df, *keys, exclude=None):
    for c in df.columns:
        cu = c.upper()
        if all(k in cu for k in keys) and not (exclude and exclude in cu):
            return c
    return None


@st.cache_data(ttl=1800, show_spinner=False)
def load_positions():
    t = table_from_raw(fetch_sheet(GID_RESUMEN), ("TOKEN", "CANTIDAD"))
    if t.empty:
        return pd.DataFrame(), {}, []

    c_tok = find_col(t, "TOKEN")
    tokens = t[c_tok].fillna("").str.strip().str.upper()
    pos = pd.DataFrame({"token": tokens})
    spec = {"cantidad": ("CANTIDAD",), "invertido": ("INVERSI",), "precio_hoja": ("PRECIO ACTUAL",)}
    for key, keys in spec.items():
        c = find_col(t, *keys)
        pos[key] = to_num(t[c]) if c else np.nan

    ignorar = {"", "NAN", "TOTAL"}
    desconocidos = sorted(set(tokens) - set(TOKENS) - ignorar)
    pos = pos[pos["token"].isin(TOKENS.keys())].reset_index(drop=True)

    # Custodia: columna 'Wallet' + una columna por token, p.ej. 'Columna J (XRP)'
    custody = {tok: {} for tok in TOKENS}
    c_wallet = find_col(t, "WALLET")
    for tok in TOKENS:
        c = find_col(t, f"({tok})")
        if not (c_wallet and c):
            continue
        for w, v in zip(t[c_wallet], t[c]):
            w, v = str(w).strip().upper(), parse_num(v)
            if w and w != "NAN" and v > 0:
                custody[tok][w] = v
    return pos, custody, desconocidos


@st.cache_data(ttl=1800, show_spinner=False)
def load_transactions():
    frames, errores = [], []
    for tok, cfg in TOKENS.items():
        try:
            t = table_from_raw(fetch_sheet(cfg["gid"]), ("FECHA",))
        except Exception as e:
            errores.append(f"{tok}: no se pudo leer la hoja ({e})")
            continue
        c_fecha, c_cant = find_col(t, "FECHA"), find_col(t, "CANTIDAD")
        c_total = find_col(t, "INVERTIDO") or find_col(t, "TOTAL")
        if not (c_fecha and c_cant and c_total):
            errores.append(f"{tok}: faltan columnas Fecha / Cantidad / Total Invertido")
            continue
        c_tipo, c_precio = find_col(t, "TIPO"), find_col(t, "PRECIO")
        c_fee = find_col(t, "COMISI") or find_col(t, "FEE")
        c_plat, c_cust = find_col(t, "WALLET", exclude="HOLDING"), find_col(t, "HOLDING")
        c_fisc = find_col(t, "FISCAL")   # opcional: coste de adquisición para Hacienda cuando difiere del dinero puesto (regalos, recompensas)

        d = pd.DataFrame({
            "fecha": pd.to_datetime(t[c_fecha], format="%d/%m/%Y", errors="coerce"),
            "token": tok,
            "cantidad": to_num(t[c_cant]),
            "precio": to_num(t[c_precio]) if c_precio else np.nan,
            "comision": to_num(t[c_fee]) if c_fee else 0.0,
            "total": to_num(t[c_total]),
            "fiscal": to_num(t[c_fisc]) if c_fisc else np.nan,
            "plataforma": t[c_plat].fillna("—").str.strip().str.upper() if c_plat else "—",
            "custodia": t[c_cust].fillna("—").str.strip().str.upper() if c_cust else "—",
        })
        d = d.dropna(subset=["fecha", "cantidad"])
        d = d[d["cantidad"] != 0].copy()
        d["total"] = d["total"].fillna(0.0)
        d["fiscal"] = d["fiscal"].fillna(d["total"])   # sin «Coste fiscal» en la fila: el coste para Hacienda es lo que pusiste
        d["comision"] = d["comision"].fillna(0.0)
        d["tipo"] = np.where(d["cantidad"] > 0, "Compra", "Venta")
        if c_tipo:
            d["tipo"] = t.loc[d.index, c_tipo].fillna("").str.strip().str.capitalize().replace("", np.nan).fillna(d["tipo"])
        frames.append(d)

    if not frames:
        return pd.DataFrame(), errores
    tx = pd.concat(frames, ignore_index=True).sort_values("fecha", kind="mergesort").reset_index(drop=True)
    return tx, errores


@st.cache_data(ttl=3600, show_spinner=False)
def price_history(tok):
    """Cierre diario en EUR. Kraken da ~2 años gratis; CoinGecko (gratis) solo 365 días."""
    cfg = TOKENS[tok]
    try:
        r = requests.get("https://api.kraken.com/0/public/OHLC",
                         params={"pair": cfg["kraken"], "interval": 1440}, timeout=10)
        js = r.json()
        if not js.get("error"):
            key = next(k for k in js["result"] if k != "last")
            rows = js["result"][key]
            s = pd.Series([float(x[4]) for x in rows],
                          index=pd.to_datetime([int(x[0]) for x in rows], unit="s").normalize())
            return s[~s.index.duplicated(keep="last")], "Kraken"
    except Exception:
        pass
    try:
        r = requests.get(f"https://api.coingecko.com/api/v3/coins/{cfg['coingecko']}/market_chart",
                         params={"vs_currency": "eur", "days": 365}, timeout=10)
        if r.ok:
            p = r.json().get("prices", [])
            s = pd.Series([x[1] for x in p], index=pd.to_datetime([x[0] for x in p], unit="ms").normalize())
            return s.groupby(level=0).last(), "CoinGecko"
    except Exception:
        pass
    return pd.Series(dtype=float), None


@st.cache_data(ttl=300, show_spinner=False)
def load_noticias():
    try:
        r = requests.get(NOTICIAS_URL, timeout=10)
        if r.ok:
            return r.json().get("noticias", [])
    except Exception:
        pass
    return []


@st.cache_data(ttl=30, show_spinner=False)
def live_prices():
    """Precio actual y apertura del día (UTC) desde Kraken."""
    try:
        pairs = ",".join(cfg["kraken"] for cfg in TOKENS.values())
        res = requests.get("https://api.kraken.com/0/public/Ticker", params={"pair": pairs}, timeout=8).json()["result"]
        out = {}
        for tok in TOKENS:
            k = next((k for k in res if tok in k), None)
            if k:
                out[tok] = {"precio": float(res[k]["c"][0]), "apertura": float(res[k]["o"])}
        return out
    except Exception:
        return {}


# =============================================================================
# CÁLCULOS
# =============================================================================
def add_twr(df):
    """Rentabilidad diaria ponderada en el tiempo (TWR): elimina el efecto de tus aportaciones,
    así una compra grande no aparece como 'rentabilidad'."""
    base = df["valor"].shift(1, fill_value=0.0) + df["flujo"]
    df["ret"] = np.where(base > 0, df["valor"] / base.where(base > 0, 1) - 1, 0.0)
    df["indice"] = (1 + df["ret"]).cumprod() * 100
    df["drawdown"] = (df["indice"] / df["indice"].cummax() - 1) * 100
    return df


def build_daily(tx, prices, current):
    today = pd.Timestamp.now(tz=MADRID).normalize().tz_localize(None)
    tx = tx.assign(fecha=tx["fecha"].clip(upper=today))
    idx = pd.date_range(tx["fecha"].min(), today, freq="D")
    per = {}
    for tok in [t for t in TOKENS if t in set(tx["token"])]:
        t = tx[tx["token"] == tok]
        p = prices.get(tok, pd.Series(dtype=float)).reindex(idx).ffill().bfill()
        if p.isna().all():
            p = pd.Series(current.get(tok, 0.0), index=idx)
        p.iloc[-1] = current.get(tok, p.iloc[-1])
        # Entradas a 0 € (regalos, transferencias) cuentan como aportación a precio de mercado
        t = t.assign(flujo=np.where(t["total"] != 0, t["total"], t["cantidad"] * p.reindex(t["fecha"]).values))
        g = t.groupby("fecha")
        q = g["cantidad"].sum().reindex(idx, fill_value=0.0).cumsum()
        aport = g["total"].sum().reindex(idx, fill_value=0.0)
        d = pd.DataFrame({
            "cantidad": q, "invertido": aport.cumsum(), "precio": p,
            "valor": q * p, "flujo": g["flujo"].sum().reindex(idx, fill_value=0.0),
        })
        per[tok] = add_twr(d[d.index >= t["fecha"].min()].copy())  # cada token empieza en su primera compra
    tot = pd.concat([d[["valor", "invertido", "flujo"]] for d in per.values()]).groupby(level=0).sum()
    return add_twr(tot), per


def todo_de_golpe(tx, prices, current, idx):
    """Valor diario de una cartera alternativa: el mismo dinero neto de cada token invertido entero el primer día."""
    alt = pd.Series(0.0, index=idx)
    for tok, invertido in tx.groupby("token")["total"].sum().items():
        p = prices.get(tok, pd.Series(dtype=float)).reindex(idx).ffill().bfill()
        if p.isna().all() or invertido <= 0:
            continue
        p.iloc[-1] = current.get(tok, p.iloc[-1])
        alt += invertido / p.iloc[0] * p
    return alt


@st.cache_data(ttl=300, show_spinner=False)
def load_alertas():
    """Niveles de precio configurados en el bot de alertas (alertas/config.toml en GitHub)."""
    if tomllib is None:
        return {}
    try:
        r = requests.get(ALERTAS_URL, timeout=10)
        return tomllib.loads(r.text) if r.ok else {}
    except Exception:
        return {}


def period_table(df, freq):
    out = pd.DataFrame({
        "ret": ((1 + df["ret"]).resample(freq).prod() - 1) * 100,
        "valor_fin": df["valor"].resample(freq).last(),
        "flujo": df["flujo"].resample(freq).sum(),
        "invertido": df["invertido"].resample(freq).last(),
    })
    out["resultado"] = out["valor_fin"] - out["valor_fin"].shift(1, fill_value=0.0) - out["flujo"]
    out["pnl_acum"] = out["valor_fin"] - out["invertido"]
    out["pnl_acum_pct"] = np.where(out["invertido"] > 0, out["pnl_acum"] / out["invertido"] * 100, np.nan)
    return out


def xirr(dates, amounts):
    """TIR anualizada (como la función TIR.NO.PER de Sheets)."""
    if len(dates) < 2:
        return None
    t = np.array([(d - dates[0]).days / 365.25 for d in dates])
    a = np.array(amounts, dtype=float)
    npv = lambda r: np.sum(a / (1 + r) ** t)
    lo, hi = -0.99, 10.0
    f_lo = npv(lo)
    if np.sign(f_lo) == np.sign(npv(hi)):
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = npv(mid)
        if np.sign(f_mid) == np.sign(f_lo):
            lo, f_lo = mid, f_mid
        else:
            hi = mid
    return mid * 100


def fifo_realized(tx):
    """Ganancias realizadas por venta con método FIFO (el que exige Hacienda en España)."""
    rows = []
    for tok, t in tx.groupby("token", sort=False):
        lots = []  # [cantidad restante, coste unitario]
        for r in t.itertuples():
            if r.cantidad > 0:
                lots.append([r.cantidad, max(getattr(r, "fiscal", r.total), 0.0) / r.cantidad])
            else:
                pendiente, coste = -r.cantidad, 0.0
                while pendiente > 1e-12 and lots:
                    usar = min(pendiente, lots[0][0])
                    coste += usar * lots[0][1]
                    lots[0][0] -= usar
                    pendiente -= usar
                    if lots[0][0] <= 1e-12:
                        lots.pop(0)
                rows.append({"Fecha": r.fecha, "Token": tok, "Cantidad": -r.cantidad,
                             "Transmisión (€)": -r.total, "Adquisición (€)": coste,
                             "Ganancia (€)": -r.total - coste})
    return pd.DataFrame(rows)


def _metricas_yahoo(js, hoy):
    """Precio actual y rentabilidades (1 semana, 3 meses, en el año) a partir de la respuesta del gráfico de Yahoo Finance."""
    res = js["chart"]["result"][0]
    meta = res["meta"]
    cierres = [(datetime.fromtimestamp(t).date(), c) for t, c in zip(res.get("timestamp") or [], res["indicators"]["quote"][0]["close"])
               if c is not None]
    if not cierres:
        raise ValueError("sin datos")
    ultimo = float(meta.get("regularMarketPrice") or cierres[-1][1])

    def desde(limite):
        previos = [c for d, c in cierres if d <= limite]
        return (ultimo / previos[-1] - 1) * 100 if previos else np.nan
    anio_ant = [c for d, c in cierres if d.year < hoy.year]
    ytd = (ultimo / anio_ant[-1] - 1) * 100 if anio_ant else (ultimo / cierres[0][1] - 1) * 100
    return {"moneda": meta.get("currency", ""), "precio": ultimo, "1s": desde(hoy - pd.Timedelta(days=7)),
            "3m": desde(hoy - pd.Timedelta(days=91)), "ytd": ytd}


@st.cache_data(ttl=1800, show_spinner=False)
def watchlist_datos(simbolos):
    """Datos de Yahoo Finance (API no oficial, con retraso) de los valores de watchlist.toml, más los cambios a euros."""
    hoy = datetime.now().date()

    def uno(sim):
        try:
            r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sim}",
                             params={"range": "1y", "interval": "1d"}, headers={"User-Agent": "Mozilla/5.0"}, timeout=12)
            r.raise_for_status()
            return sim, _metricas_yahoo(r.json(), hoy)
        except Exception:
            return sim, None
    with ThreadPoolExecutor(max_workers=8) as ex:
        out = dict(ex.map(uno, list(simbolos) + ["EURUSD=X", "EURGBP=X"]))
    return out


# =============================================================================
# CABECERA Y CARGA
# =============================================================================
def titulo_con_logo():
    """Título con el icono del escudo. Si falta el archivo, vuelve al título de siempre."""
    p = ASSETS / "icono-oscuro-96.png"   # emblema en tonos claros y fondo transparente: se funde con el tema oscuro
    if not p.exists():
        return None
    b64 = base64.b64encode(p.read_bytes()).decode()
    return ('<div style="display:flex;align-items:center;gap:12px">'
            f'<img src="data:image/png;base64,{b64}" style="width:56px;height:56px;flex:none">'
            '<h1 style="margin:0;padding:0;font-size:clamp(1.6rem,5vw,2.4rem);font-weight:700;line-height:1.1">'
            'Mi Cartera Cripto</h1></div>')


with st.container(key="cab"):
    h1, h2 = st.columns([6, 1], vertical_alignment="center")
    _titulo = titulo_con_logo()
    if _titulo:
        h1.markdown(_titulo, unsafe_allow_html=True)
    else:
        h1.title("⚡ Mi Cartera Cripto")
    _hoy = datetime.now(MADRID)
    h1.markdown(f"<div class='fecha-cab'>{('Lunes Martes Miércoles Jueves Viernes Sábado Domingo'.split())[_hoy.weekday()]} "
                f"{_hoy.day} {MESES_CORTOS[_hoy.month - 1].lower()}</div>", unsafe_allow_html=True)
    try:
        _ajustes = h2.popover("⚙️", help="Ajustes y actualizar datos")
    except Exception:                      # versiones antiguas de Streamlit sin popover
        _ajustes = h2.expander("⚙️")
    with _ajustes:
        use_live = st.toggle("Precio en vivo", value=True,
                             help="Activado: precio actual de Kraken (cada 30 s). Desactivado: el precio de tu Google Sheet.")
        if st.button("🔄 Actualizar datos", help="Vuelve a leer ahora las hojas de Google (se releen solas cada 30 min)", **WIDE):
            st.cache_data.clear()
            st.rerun()


# --- Refresco automático y estado de los datos ---
REFRESCO_S = 300      # con la app abierta se recarga sola cada 5 min (precios 30 s, noticias 5 min)
st.session_state["_carga_t"] = time.time()


@st.fragment(run_every=REFRESCO_S)
def _autorefresco():
    # el temporizador solo salta si desde la última carga completa pasó el intervalo (una interacción tuya lo reinicia)
    if time.time() - st.session_state.get("_carga_t", time.time()) >= REFRESCO_S - 5:
        st.rerun()


_autorefresco()


def linea_estado():
    """Solo avisa si algún bot falla o va con retraso; la hora de los datos ya sale en la línea de «precios: Kraken en vivo»."""
    try:
        import sistema
        problemas, _ = sistema.resumen_bots()
        if problemas:
            from html import escape
            st.markdown(f"<details class='bots'><summary>● Bots</summary><div>Con retraso o fallo: {escape(', '.join(problemas))}. "
                        "Detalle en Más → Sistema.</div></details>", unsafe_allow_html=True)
    except Exception:
        pass


def precargar():
    """Pide A LA VEZ todo lo que viene de internet (Google Sheets, Kraken, noticias, alertas).
    Antes iba uno detrás de otro; así la app abre varios segundos antes. Lo descargado queda en caché."""
    try:
        from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx
        ctx = get_script_run_ctx()
    except Exception:
        add_script_run_ctx, ctx = None, None
    tareas = [lambda g=g: fetch_sheet(g) for g in [GID_RESUMEN] + [cfg["gid"] for cfg in TOKENS.values()]]
    tareas += [lambda t=t: price_history(t) for t in TOKENS]
    tareas += [live_prices, load_noticias, load_alertas]
    try:
        import sistema
        tareas.append(sistema.estado_workflows)
    except Exception:
        pass

    def ejecutar(tarea):
        if add_script_run_ctx and ctx:
            add_script_run_ctx(threading.current_thread(), ctx)
        try:
            tarea()
        except Exception:
            pass  # si algo falla, se vuelve a intentar (y se avisa) en la carga normal de abajo

    with ThreadPoolExecutor(max_workers=len(tareas)) as ex:
        list(ex.map(ejecutar, tareas))


with st.spinner("Cargando cartera..."):
    precargar()
    try:
        pos, custody, desconocidos = load_positions()
    except Exception as e:
        st.error(f"No se pudo leer la hoja de resumen de Google Sheets: {e}")
        listo()
        st.stop()
    tx, tx_errores = load_transactions()
    live = live_prices() if use_live else {}
    hist = {tok: price_history(tok) for tok in TOKENS}

# (el aviso de bots se retiró de las pantallas: el estado está en Más → Sistema)

if pos.empty:
    st.warning("La hoja de resumen no tiene posiciones. Revisa que tenga las columnas 'Token' y 'Cantidad'.")
    listo()
    st.stop()

# --- Posiciones con precio actual ---
pos["precio"] = pos["token"].map(lambda t: live.get(t, {}).get("precio", np.nan)).astype(float).fillna(pos["precio_hoja"])
pos["valor"] = pos["cantidad"] * pos["precio"]
pos["pnl"] = pos["valor"] - pos["invertido"]
pos["pnl_pct"] = np.where(pos["invertido"] > 0, pos["pnl"] / pos["invertido"] * 100, np.nan)
pos["precio_medio"] = np.where(pos["cantidad"] > 0, pos["invertido"] / pos["cantidad"], np.nan)
pos["hoy_pct"] = pos["token"].map(
    lambda t: (live[t]["precio"] / live[t]["apertura"] - 1) * 100 if t in live and live[t]["apertura"] else np.nan
).astype(float)
pos["hoy_eur"] = pos["valor"] - pos["valor"] / (1 + pos["hoy_pct"].fillna(0) / 100)
pos["peso"] = pos["valor"] / pos["valor"].sum() * 100
current = dict(zip(pos["token"], pos["precio"]))
P = pos.set_index("token")

inv_total, val_total = pos["invertido"].sum(), pos["valor"].sum()
pnl_total = val_total - inv_total
pnl_total_pct = pnl_total / inv_total * 100 if inv_total > 0 else 0.0
hoy_eur = pos["hoy_eur"].sum()
hoy_pct = hoy_eur / (val_total - hoy_eur) * 100 if live else np.nan

fuente = "Kraken en vivo" if live else "Google Sheets"
_pie_datos = f"Google Sheets · precios: {fuente} · {datetime.now(MADRID):%d/%m/%Y %H:%M}"

# --- Avisos de calidad de datos ---
avisos = list(tx_errores)
if desconocidos:
    avisos.append(f"Tokens en el resumen que no están configurados en la app: {', '.join(desconocidos)} (añádelos a TOKENS).")
if use_live and not live:
    avisos.append("No se pudo obtener el precio en vivo de Kraken; se usa el precio de la hoja.")
daily, per = pd.DataFrame(), {}
if not tx.empty:
    hoy = pd.Timestamp.now().normalize()
    futuras = tx[tx["fecha"] > hoy]
    for r in futuras.itertuples():
        avisos.append(f"Operación con fecha futura: {r.token} {fmt(r.cantidad, 4)} el {r.fecha:%d/%m/%Y} "
                      f"(¿error al escribir la fecha?). Se cuenta como si fuera de hoy.")
    for tok, cant_tx in tx.groupby("token")["cantidad"].sum().items():
        if tok in P.index and abs(cant_tx - P.at[tok, "cantidad"]) > 0.01:
            avisos.append(f"{tok}: la suma de operaciones ({fmt(cant_tx, 4)}) no cuadra con el resumen "
                          f"({fmt(P.at[tok, 'cantidad'], 4)}).")
    sin_hist = [tok for tok, (s, _) in hist.items() if s.empty]
    if sin_hist:
        avisos.append(f"Sin histórico de precios para {', '.join(sin_hist)}: el gráfico usa el precio actual.")
    prices = {tok: s for tok, (s, _) in hist.items()}
    daily, per = build_daily(tx, prices, current)
if avisos:
    with st.expander(f"⚠️ {len(avisos)} aviso(s) sobre tus datos", expanded=False):
        for a in avisos:
            st.markdown(f"- {a}")

# =============================================================================
# KPIs PRINCIPALES
# =============================================================================
tir = None
if not tx.empty:
    flujos = tx[tx["total"] != 0]
    tir = xirr(list(flujos["fecha"].clip(upper=pd.Timestamp.now().normalize())) + [pd.Timestamp.now().normalize()],
               list(-flujos["total"]) + [val_total])

# Menú en dos niveles: barra inferior fija con 5 destinos y, arriba, pastillas con los apartados de cada destino.
# _sec sigue siendo el índice del apartado (0-11) que usa el resto del código; solo se ejecuta el código del apartado elegido
# (la app carga más rápido y consulta menos fuentes).
_NOMBRES = ["🏠 Inicio", "💼 Posiciones", "📈 Evolución", "📅 Rentabilidad", "🧾 Operaciones", "🛡️ Riesgo", "🧮 Simuladores",
            "🏛️ Fiscalidad", "📰 Noticias", "👀 Watchlist", "🗓️ Eventos", "🩺 Sistema"]
_DESTINOS = [("🏠 Inicio", [0]),
             ("💼 Cartera", [1, 4, 7]),                # Posiciones, Operaciones, Fiscalidad
             ("📈 Análisis", [2, 3, 5, 6]),            # Evolución, Rentabilidad, Riesgo, Simuladores
             ("📰 Mercado", [8, 9, 10]),               # Noticias, Watchlist, Eventos
             ("⚙️ Más", [11])]                         # Sistema + cambio de sección (Cerebro, Seguimiento, Privado)
_dest = st.radio("Destino", range(len(_DESTINOS)), horizontal=True, label_visibility="collapsed", key="dest_menu",
                 format_func=lambda d: _DESTINOS[d][0].split(" ", 1)[1])      # el icono lo pone el CSS (SVG de línea)
_apartados = _DESTINOS[_dest][1]
if len(_apartados) > 1:
    if st.session_state.get("pill_menu") not in _apartados:      # al cambiar de destino se empieza por su primer apartado
        st.session_state["pill_menu"] = _apartados[0]
    _sec = st.radio("Apartado", _apartados, horizontal=True, label_visibility="collapsed", key="pill_menu",
                    format_func=lambda i: _NOMBRES[i].split(" ", 1)[1])
else:
    _sec = _apartados[0]


def _spark(serie, color):
    """Minigráfico SVG (línea y área) con los valores diarios; solo números calculados, ningún texto externo."""
    v = [float(x) for x in serie if pd.notna(x)]
    if len(v) < 3:
        return ""
    lo, hi = min(v), max(v)
    rng = (hi - lo) or 1.0
    pts = [(i / (len(v) - 1) * 300, 44 - (x - lo) / rng * 40) for i, x in enumerate(v)]
    linea = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f"<svg class='spark' viewBox='0 0 300 46' preserveAspectRatio='none'>"
            f"<polygon points='0,46 {linea} 300,46' fill='{color}' fill-opacity='.14'/>"
            f"<polyline points='{linea}' fill='none' stroke='{color}' stroke-width='1.6' vector-effect='non-scaling-stroke'/></svg>")


# La animación de entrada solo corre la primera vez que se pinta cada apartado: cada clic relanza el script y, si no, parpadearía.
_vistos = st.session_state.setdefault("anim_visto", set())
_anim = " anim" if _sec not in _vistos else ""
_vistos.add(_sec)


def _cuenta(x, texto):
    """Número que cuenta hasta su valor (CSS puro). x: importe en euros; texto: el importe ya formateado (es-ES), que se
    enseña al terminar. Sin animación (o sin dato) devuelve solo el texto."""
    from html import escape
    if not _anim or x is None or pd.isna(x):
        return escape(str(texto))
    pre = "-" if x < 0 else ("+" if str(texto).startswith("+") else "")
    return (f"<span class='cu' style='--fin:{int(abs(round(float(x))))};--pre:\"{pre}\";--suf:\" €\"'>"
            f"<span class='c' aria-hidden='true'></span><span class='f'>{escape(str(texto))}</span></span>")


def _flecha(v):
    return "nu" if v is None or pd.isna(v) or v == 0 else ("up" if v > 0 else "dn")


def panel_resumen():
    """UN panel: valor de la cartera grande arriba y, debajo, 4 métricas en rejilla de 2 columnas separadas por líneas."""
    from html import escape
    chispa = ""
    if not daily.empty:
        ult = daily[daily.index >= daily.index.max() - pd.Timedelta(days=30)]
        chispa = _spark(ult["valor"], POS if pnl_total >= 0 else NEG)
    def celda(titulo, valor_html, v, delta=None, ayuda=""):
        c = _flecha(v)
        sim = {"up": "▲ ", "dn": "▼ "}.get(c, "")
        d = f"<div class='d {c}'>{sim}{escape(delta)}</div>" if delta else ""
        return (f"<div class='m' title='{escape(ayuda, quote=True)}'><div class='l'>{titulo}</div>"
                f"<div class='v {c if c != 'nu' else ''}'>{valor_html}</div>{d}</div>")
    celdas = [
        celda("Invertido", _cuenta(inv_total, eur(inv_total)), None, None,
              "Dinero puesto menos dinero retirado con ventas (incluye comisiones)."),
        celda("Beneficio", _cuenta(pnl_total, eur(pnl_total, sign=True)), pnl_total, pct(pnl_total_pct),
              "Beneficio no realizado: valor actual menos invertido."),
        celda("Hoy", _cuenta(hoy_eur, eur(hoy_eur, sign=True)) if live else "—", hoy_eur if live else None,
              pct(hoy_pct) if live else None, "Variación desde la apertura del día (00:00 UTC) en Kraken."),
        celda("TIR anual", escape(pct(tir)) if tir is not None else "—", tir, None,
              "Rentabilidad anualizada teniendo en cuenta cuándo metiste cada euro. Es la cifra comparable con un depósito o un fondo."),
    ]
    return (f"<div class='panel{_anim}' style='--i:0'><div class='tit'>Valor actual</div>"
            f"<div class='gran'>{_cuenta(val_total, eur(val_total))}</div>{chispa}"
            f"<div class='rejilla'>{''.join(celdas)}</div></div>"
            f"<div class='meta'>{escape(_pie_datos)}</div>")


def kpi_card(label, value, delta=None, ayuda=None, hero=False, colorear=False, ic="", i=0, extra=""):
    """Tarjeta HTML (dos por fila en el móvil). hero: la tarjeta grande de arriba. colorear: valor en verde/rojo según su signo.
    ic: símbolo corto de la esquina. i: orden de entrada (animación). extra: HTML ya construido por el código."""
    from html import escape
    dlt = ""
    if delta and delta != "—":
        dlt = f"<div class='dlt {'dn' if delta.strip().startswith('-') else 'up'}'>{escape(str(delta))}</div>"
    titulo = f" title='{escape(str(ayuda), quote=True)}'" if ayuda else ""
    clase = ""
    if colorear and value not in ("—", None):
        clase = " dn" if str(value).strip().startswith("-") else " up"
    icono = f"<span class='ic'>{escape(ic)}</span>" if ic else ""
    return (f"<div class='kpi{' hero' if hero else ''}'{titulo} style='--i:{i}'><div class='lbl'>{escape(str(label))}{icono}</div>"
            f"<div class='val{clase}'>{escape(str(value))}</div>{dlt}{extra}</div>")


def _resumen_hero():
    """Bajo el valor total: beneficio y hoy en pastillas, más un minigráfico fino de 30 días."""
    def pastilla(txt, v, cifra):
        c = "" if v is None or pd.isna(v) or v == 0 else (" up" if v > 0 else " dn")
        return f"<span class='pill{c}'>{txt} {cifra}</span>"
    partes = [pastilla("Beneficio", pnl_total, f"{eur(pnl_total, sign=True)} ({pct(pnl_total_pct)})")]
    if live:
        partes.append(pastilla("Hoy", hoy_eur, f"{eur(hoy_eur, sign=True)} ({pct(hoy_pct)})"))
    chispa = ""
    if not daily.empty:
        ult = daily[daily.index >= daily.index.max() - pd.Timedelta(days=30)]
        chispa = _spark(ult["valor"], POS if pnl_total >= 0 else NEG)
    return "<div class='sub'>" + "".join(partes) + "</div>" + chispa


kpis = [
    ("Valor actual", eur(val_total), None, None, True, False, ""),
    ("Invertido", eur(inv_total), None, "Dinero puesto menos dinero retirado con ventas (incluye comisiones).", False, False, "€"),
    ("Beneficio", eur(pnl_total, sign=True), pct(pnl_total_pct), "Beneficio no realizado: valor actual menos invertido.", False, True, "↗"),
    ("Hoy", eur(hoy_eur, sign=True) if live else "—", pct(hoy_pct) if live else None,
     "Variación desde la apertura del día (00:00 UTC) en Kraken.", False, True, "☀"),
    ("TIR anual", pct(tir) if tir is not None else "—", None,
     "Rentabilidad anualizada teniendo en cuenta cuándo metiste cada euro. Es la cifra comparable con un depósito o un fondo.", False, False, "%"),
]
if _sec == 0:
    st.markdown(panel_resumen(), unsafe_allow_html=True)
else:      # en el resto de apartados, una tira compacta (valor, beneficio y hoy) para no quitar sitio al contenido
    st.markdown("<div class='kpis-mini'>" + "".join(kpi_card(*kpis[n][:2], delta=None, colorear=kpis[n][5], i=j)
                                                    for j, n in enumerate((0, 2, 3))) + "</div>", unsafe_allow_html=True)

# Cambio de sección (Cerebro, Seguimiento, Privado): en «Más», con tarjetas grandes
if _dest == len(_DESTINOS) - 1:
    menu_secciones()
_SEL = [_sec]
tabs = {_sec: st.container()}

# =============================================================================
# 0. INICIO — lo esencial de un vistazo
# =============================================================================
if 0 in _SEL:
    with tabs[0]:
        i1, i2 = st.columns([3, 2], gap="small")
        with i1:
            st.markdown("##### Tus posiciones")
            from html import escape as _esc
            _filas = []
            for n, r in enumerate(pos.itertuples()):
                if pd.notna(r.hoy_pct):
                    hoy_txt = f"<small class='{'up' if r.hoy_pct >= 0 else 'dn'}'>{'▲' if r.hoy_pct >= 0 else '▼'} {_esc(pct(r.hoy_pct))} hoy</small>"
                else:
                    hoy_txt = ""
                color = TOKENS[r.token]["color"]
                _filas.append(
                    f"<div class='fila'>"
                    f"<div class='av' style='background:{color}'>{_esc(r.token)}</div>"
                    f"<div><h4>{_esc(r.token)}</h4><p>{_esc(fmt(r.cantidad, 0))} uds · precio {_esc(eur(r.precio, 4))}</p></div>"
                    f"<div class='der'>{_cuenta(r.valor, eur(r.valor))}{hoy_txt}</div>"
                    f"<div class='barra'><i style='width:{max(0, min(100, float(r.peso))):.0f}%;background:{color}'></i></div></div>")
            st.markdown(f"<div class='panel{_anim}' style='--i:1'>{''.join(_filas)}</div>", unsafe_allow_html=True)

            st.markdown("##### Últimos 30 días")
            if not daily.empty:
                ult = daily[daily.index >= daily.index.max() - pd.Timedelta(days=30)]
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=ult.index, y=ult["invertido"], name="Invertido", mode="lines",
                                         line=dict(color=MUTED, width=1.5, dash="dash"), hovertemplate="%{y:,.2f} €"))
                fig.add_trace(go.Scatter(x=ult.index, y=ult["valor"], name="Valor", mode="lines", fill="tonexty",
                                         fillcolor="rgba(110,168,255,.16)", line=dict(color="#6ea8ff", width=2.5),
                                         hovertemplate="%{y:,.2f} €"))
                fig = style_fig(fig, 190)
                fig.update_yaxes(ticksuffix=" €")
                chart(fig)
                mercado_30 = ult["valor"].iloc[-1] - ult["valor"].iloc[0] - ult["flujo"].iloc[1:].sum()
                st.caption(f"En 30 días has aportado {eur(ult['flujo'].iloc[1:].sum())} y el mercado te ha dado "
                           f"**{eur(mercado_30, sign=True)}**.")
        with i2:
            st.markdown("##### Tus alertas")
            cfg_alertas = load_alertas()
            if not cfg_alertas:
                st.caption("No se pudo leer la configuración del bot de alertas.")
            for tok in P.index:
                p_act = P.at[tok, "precio"]
                niveles = sorted(float(x) for x in cfg_alertas.get("niveles", {}).get(tok, []))
                arriba = next((x for x in niveles if x > p_act), None)
                abajo = next((x for x in reversed(niveles) if x < p_act), None)
                lineas = [f"**{tok}** · {eur(p_act, 4)}"]
                if arriba:
                    lineas.append(f"🔼 Subiendo: **{eur(arriba, 4)}** ({pct((arriba / p_act - 1) * 100, 1)})")
                if abajo:
                    lineas.append(f"🔽 Bajando: **{eur(abajo, 4)}** ({pct((abajo / p_act - 1) * 100, 1)})")
                pm = P.at[tok, "precio_medio"]
                if pd.notna(pm):
                    lineas.append(f"⚖️ Precio medio: {eur(pm, 4)} ({pct((pm / p_act - 1) * 100, 1)})")
                with st.container(border=True):
                    st.markdown("  \n".join(lineas))
            if cfg_alertas:
                st.caption(f"También te avisa si un token se mueve más de un {cfg_alertas.get('movimiento_brusco_pct', 7)} % "
                           "en 24 h. Los niveles se cambian en `alertas/config.toml` en GitHub.")

            st.markdown("##### Últimas noticias")
            ultimas = sorted(load_noticias(), key=lambda n: n.get("fecha_envio", ""), reverse=True)[:3]
            if not ultimas:
                st.caption("Todavía no hay noticias.")
            for n in ultimas:
                voto = {1: " 👍", -1: " 👎"}.get(n.get("valoracion"), "")
                st.markdown(f"{enlace(n['titulo'], n['url'])}{voto}  \n"
                            f"<span style='color:{MUTED};font-size:0.8rem'>{html_lib.escape(str(n['tema']))} · "
                            f"⭐ {html_lib.escape(str(n['puntuacion']))}/10</span>",
                            unsafe_allow_html=True)

# =============================================================================
# 1. POSICIONES
# =============================================================================
if 1 in _SEL:
    with tabs[1]:
        with st.container():
            for r in pos.itertuples():
                with st.container(border=True, key=f"pos_{r.token}"):
                    st.markdown(f"#### {r.token} &nbsp; <span style='color:{MUTED};font-size:0.9rem'>"
                                f"{fmt(r.cantidad, 2)} tokens · {fmt(r.peso, 1)} % de la cartera</span>",
                                unsafe_allow_html=True)
                    # El dinero (lo que pusiste → lo que vale → la diferencia) y los precios: 6 indicadores en una sola fila
                    # (en el móvil se reparten en 3 filas de 2)
                    c1, c2, c3, c4, c5, c6 = st.columns(6)
                    c1.metric("💶 Invertido", eur(r.invertido),
                              help="Dinero que has metido en este token, menos lo que has sacado con ventas (incluye comisiones).")
                    c2.metric("💰 Valor actual", eur(r.valor), delta=pct(r.hoy_pct) + " hoy" if pd.notna(r.hoy_pct) else None)
                    c3.metric("📈 Beneficio", eur(r.pnl, sign=True), delta=pct(r.pnl_pct))
                    c4.metric("⚖️ Precio medio", eur(r.precio_medio, 4),
                              help="Tu punto de equilibrio: invertido neto / tokens. Por encima de este precio ganas.")
                    c5.metric("🏷️ Precio actual", eur(r.precio, 4),
                              delta=pct((r.precio / r.precio_medio - 1) * 100) + " vs medio" if r.precio_medio else None)
                    c6.metric("🪙 Tokens", fmt(r.cantidad, 2))
                    # Barra visual: cuánto vale hoy cada euro invertido
                    if r.invertido > 0:
                        ratio = r.valor / r.invertido
                        color = POS if ratio >= 1 else NEG
                        ancho_inv = min(100, 100 / ratio) if ratio > 1 else 100
                        ancho_val = min(100, ratio * 100)
                        st.markdown(
                            f"<div style='font-size:0.8rem;color:{MUTED};margin:2px 0 4px'>Invertido vs valor actual</div>"
                            f"<div style='background:#25304a;border-radius:6px;height:10px;margin-bottom:4px'>"
                            f"<div style='width:{ancho_inv:.1f}%;background:{MUTED};height:10px;border-radius:6px'></div></div>"
                            f"<div style='background:#25304a;border-radius:6px;height:10px'>"
                            f"<div style='width:{ancho_val:.1f}%;background:{color};height:10px;border-radius:6px'></div></div>"
                            f"<div style='font-size:0.8rem;color:{MUTED};margin-top:4px'>Cada 1 € invertido vale hoy "
                            f"<b style='color:{color}'>{fmt(ratio, 2)} €</b></div>",
                            unsafe_allow_html=True)

                    wallets = custody.get(r.token, {})
                    if wallets:
                        from html import escape as _e
                        _filas = []
                        for w, q in sorted(wallets.items(), key=lambda x: -x[1]):
                            frac = min(q / r.cantidad, 1.0) if r.cantidad > 0 else 0.0
                            icono = "🧊" if w in COLD_WALLETS else "🏦"
                            _filas.append(f"<div class='cr'><span>{icono} {_e(str(w))}</span>"
                                          f"<span>{_e(fmt(q, 2))} {_e(r.token)} · {_e(eur(q * r.precio))} · {_e(fmt(frac * 100, 1))} %</span></div>"
                                          f"<div class='cb'><i style='width:{frac * 100:.1f}%'></i></div>")
                        st.markdown("<div class='cust'><div class='tit'>Custodia</div>" + "".join(_filas) + "</div>",
                                    unsafe_allow_html=True)

        # Distribución: los dos gráficos debajo de las tarjetas, uno al lado del otro
        def donut(labels, values, centro, colores=None):
            fig = go.Figure(go.Pie(labels=labels, values=values, hole=0.62, sort=False,
                                   marker=dict(colors=colores, line=dict(color="#0b0f17", width=2)),
                                   textinfo="percent", textposition="inside", insidetextorientation="horizontal",
                                   hovertemplate="%{label}: %{value:,.2f} €<extra></extra>"))
            fig = style_fig(fig, 320)
            fig.update_layout(margin=dict(l=10, r=10, t=10, b=40), hovermode="closest",
                              legend=dict(orientation="h", yanchor="top", y=-0.02, xanchor="center", x=0.5),
                              annotations=[dict(text=centro, showarrow=False, font=dict(size=15))])
            return fig

        st.markdown("##### Distribución de la cartera")
        d1, d2 = st.columns(2, gap="large")
        with d1:
            with st.container(border=True):
                st.markdown("**Por token**")
                chart(donut(pos["token"], pos["valor"], eur(val_total, 0), [TOKENS[t]["color"] for t in pos["token"]]))

        cust_total = {}
        for tok, ws in custody.items():
            for w, q in ws.items():
                cust_total[w] = cust_total.get(w, 0.0) + q * current.get(tok, 0.0)
        with d2:
            if cust_total:
                with st.container(border=True):
                    st.markdown("**Por custodia**")
                    colores = ["#9a7bff" if w in COLD_WALLETS else "#f1d58a" for w in cust_total]
                    chart(donut(list(cust_total), list(cust_total.values()), f"{len(cust_total)} sitios", colores))
                en_exchange = sum(v for w, v in cust_total.items() if w not in COLD_WALLETS)
                frac_ex = en_exchange / sum(cust_total.values()) * 100
                (st.warning if frac_ex > 20 else st.info)(
                    f"{fmt(frac_ex, 1)} % de la cartera ({eur(en_exchange)}) está en exchange. "
                    "Lo que no vayas a mover pronto es más seguro en tu Ledger.")

# =============================================================================
# 2. EVOLUCIÓN
# =============================================================================
if 2 in _SEL:
    with tabs[2]:
        if daily.empty:
            st.info("No hay operaciones para construir el histórico.")
        else:
            vista = st.radio("Vista", ["Total", "Por token"], horizontal=True, label_visibility="collapsed")
            fig = go.Figure()
            if vista == "Total":
                fig.add_trace(go.Scatter(x=daily.index, y=daily["valor"], name="Valor", mode="lines",
                                         line=dict(color="#6ea8ff", width=2), fill="tozeroy",
                                         fillcolor="rgba(110,168,255,0.15)", customdata=daily["valor"] - daily["invertido"],
                                         hovertemplate="%{y:,.2f} € (beneficio %{customdata:+,.2f} €)"))
                fig.add_trace(go.Scatter(x=daily.index, y=daily["invertido"], name="Invertido neto", mode="lines",
                                         line=dict(color=MUTED, width=2, dash="dash"), hovertemplate="%{y:,.2f} €"))
            else:
                for tok, d in per.items():
                    fig.add_trace(go.Scatter(x=d.index, y=d["valor"], name=tok, mode="lines", stackgroup="uno",
                                             line=dict(color=TOKENS[tok]["color"], width=1), hovertemplate="%{y:,.2f} €"))
            fig = style_fig(fig, 420)
            fig.update_xaxes(rangeselector=dict(
                buttons=[dict(count=1, label="1M", step="month", stepmode="backward"),
                         dict(count=3, label="3M", step="month", stepmode="backward"),
                         dict(count=6, label="6M", step="month", stepmode="backward"),
                         dict(count=1, label="1A", step="year", stepmode="backward"),
                         dict(step="all", label="Todo")],
                bgcolor="#141b29", activecolor="#6ea8ff", font=dict(color="#eef2fb")))
            # Leyenda abajo para que los botones 1M/3M/... no la tapen
            fig.update_layout(legend=dict(orientation="h", yanchor="top", y=-0.12, xanchor="left", x=0),
                              margin=dict(l=10, r=10, t=40, b=50))
            fig.update_yaxes(ticksuffix=" €", rangemode="tozero")
            chart(fig)
            fuentes = {tok: src for tok, (_, src) in hist.items()}
            st.caption("Precios históricos: " + " · ".join(f"{t} → {s or 'sin datos'}" for t, s in fuentes.items()))

            st.subheader("📉 Tu precio medio frente al mercado (DCA)")
            tok_dca = st.radio("Token", list(per), horizontal=True, key="dca_tok")
            d = per[tok_dca]
            pm = (d["invertido"] / d["cantidad"]).where(d["cantidad"] > 0)
            t_tok = tx[(tx["token"] == tok_dca) & (tx["precio"] > 0)]
            compras, ventas = t_tok[t_tok["cantidad"] > 0], t_tok[t_tok["cantidad"] < 0]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=d.index, y=d["precio"], name="Precio de mercado", mode="lines",
                                     line=dict(color=TOKENS[tok_dca]["color"], width=1.5), hovertemplate="%{y:,.4f} €"))
            fig.add_trace(go.Scatter(x=pm.index, y=pm, name="Tu precio medio", mode="lines",
                                     line=dict(color="#f1d58a", width=2.5, shape="hv"), hovertemplate="%{y:,.4f} €"))
            if not compras.empty:
                size = 7 + 14 * np.sqrt(compras["total"].clip(lower=0) / compras["total"].max())
                fig.add_trace(go.Scatter(x=compras["fecha"], y=compras["precio"], name="Compras", mode="markers",
                                         marker=dict(symbol="triangle-up", color=POS, size=size, line=dict(width=0)),
                                         customdata=compras["total"], hovertemplate="Compra a %{y:,.4f} € (%{customdata:,.2f} €)"))
            if not ventas.empty:
                fig.add_trace(go.Scatter(x=ventas["fecha"], y=ventas["precio"], name="Ventas", mode="markers",
                                         marker=dict(symbol="triangle-down", color=NEG, size=11),
                                         customdata=-ventas["total"], hovertemplate="Venta a %{y:,.4f} € (%{customdata:,.2f} €)"))
            chart(style_fig(fig, 400))
            r = P.loc[tok_dca]
            dist = (r["precio"] / r["precio_medio"] - 1) * 100
            st.caption(f"Precio actual {eur(r['precio'], 4)} · tu precio medio {eur(r['precio_medio'], 4)} → "
                       f"estás un **{pct(dist)}** {'por encima' if dist >= 0 else 'por debajo'} de tu punto de equilibrio. "
                       f"El gráfico empieza en tu primera compra de {tok_dca}.")

# =============================================================================
# 3. RENTABILIDAD
# =============================================================================
if 3 in _SEL:
    with tabs[3]:
        if daily.empty:
            st.info("No hay operaciones para calcular rentabilidades.")
        else:
            # --- Tu estrategia (comprar poco a poco) frente a meterlo todo el primer día ---
            st.markdown("##### Tu estrategia frente al mercado")
            alt = todo_de_golpe(tx, prices, current, daily.index)
            valor_hoy = daily["valor"].iloc[-1]
            dif = valor_hoy - alt.iloc[-1]
            e1, e2, e3 = st.columns(3)
            e1.metric("Tu cartera hoy", eur(valor_hoy), help="Comprando poco a poco, como has hecho.")
            e2.metric(f"Todo de golpe el {daily.index[0]:%d/%m/%Y}", eur(alt.iloc[-1]),
                      help="El mismo dinero neto que has puesto en cada token, invertido entero el primer día.")
            e3.metric("Diferencia a tu favor" if dif >= 0 else "Diferencia en tu contra", eur(dif, sign=True))
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=daily.index, y=daily["valor"], name="Tu cartera", mode="lines",
                                     line=dict(color="#6ea8ff", width=2), hovertemplate="%{y:,.2f} €"))
            fig.add_trace(go.Scatter(x=alt.index, y=alt, name="Todo de golpe el primer día", mode="lines",
                                     line=dict(color="#f1d58a", width=1.5, dash="dot"), hovertemplate="%{y:,.2f} €"))
            fig = style_fig(fig, 280)
            fig.update_yaxes(ticksuffix=" €")
            chart(fig)
            twr_total = (daily["indice"].iloc[-1] / 100 - 1) * 100
            st.caption(
                f"Desde que empezaste, los precios de tu cartera han variado un **{pct(twr_total)}** (rentabilidad TWR, "
                f"la del mapa de abajo). Pero a ti te ha ido {'mejor' if tir is not None and tir > twr_total else 'distinto'}: "
                f"tu TIR es **{pct(tir) if tir is not None else '—'}** al año, porque cuenta cuándo compraste. "
                "Si la TIR es mejor que la TWR, tus compras escalonadas en las caídas han funcionado.")
            st.divider()

            ambito = st.radio("Ámbito", ["Cartera"] + list(per), horizontal=True, key="rent_scope")
            base_df = daily if ambito == "Cartera" else per[ambito]
            st.caption("La rentabilidad se calcula **sin el efecto de tus aportaciones** (método TWR): si en un mes "
                       "compras 500 €, eso no cuenta como ganancia. Así ves cómo se ha comportado el mercado con tu cartera.")

            m = period_table(base_df, "ME")
            anual = ((1 + base_df["ret"]).resample("YE").prod() - 1) * 100
            years = sorted(m.index.year.unique())
            z, text = [], []
            for y in years:
                fila = [m[(m.index.year == y) & (m.index.month == mes)]["ret"] for mes in range(1, 13)]
                fila = [v.iloc[0] if len(v) else np.nan for v in fila]
                fila.append(anual[anual.index.year == y].iloc[0])
                z.append(fila)
                text.append(["" if pd.isna(v) else f"{fmt(v, 1, True)}%" for v in fila])
            lim = float(min(max(10.0, np.nanmax(np.abs(np.array(z, dtype=float)))), 60.0))
            fig = go.Figure(go.Heatmap(
                z=z, x=MESES_CORTOS + ["Año"], y=[str(y) for y in years], text=text, texttemplate="%{text}",
                colorscale=[[0, "#b91c1c"], [0.5, "#25304a"], [1, "#059669"]], zmid=0, zmin=-lim, zmax=lim,
                showscale=False, xgap=3, ygap=3, hovertemplate="%{x} %{y}: %{text}<extra></extra>"))
            fig = style_fig(fig, 90 + 55 * len(years))
            fig.update_layout(hovermode="closest")
            fig.update_yaxes(type="category", autorange="reversed", showgrid=False)
            fig.update_xaxes(side="top")
            chart(fig)

            def tabla_periodos(df, etiqueta, nombre):
                tbl = pd.DataFrame({
                    nombre: etiqueta,
                    "Rentabilidad": df["ret"].values,
                    "Resultado (€)": df["resultado"].values,
                    "Aportado (€)": df["flujo"].values,
                    "Valor final (€)": df["valor_fin"].values,
                    "Beneficio acum. (€)": df["pnl_acum"].values,
                    "Beneficio acum. (%)": df["pnl_acum_pct"].values,
                }).iloc[::-1]
                sty = (tbl.style
                       .format({"Rentabilidad": pct, "Resultado (€)": lambda v: eur(v, sign=True),
                                "Aportado (€)": eur, "Valor final (€)": eur,
                                "Beneficio acum. (€)": lambda v: eur(v, sign=True), "Beneficio acum. (%)": pct}, na_rep="—")
                       .map(color_sign, subset=["Rentabilidad", "Resultado (€)", "Beneficio acum. (€)", "Beneficio acum. (%)"]))
                st.dataframe(sty, hide_index=True, **WIDE)
                return tbl

            t_m, t_w = st.tabs(["🗓️ Mensual", "📅 Semanal"])
            with t_m:
                tbl_m = tabla_periodos(m, [f"{MESES[d.month - 1]} {d.year}" for d in m.index], "Mes")
            with t_w:
                w = period_table(base_df, "W-SUN")
                etiquetas = [f"Sem {d.isocalendar()[1]:02d} · {(d - pd.Timedelta(days=6)):%d/%m} – {d:%d/%m/%Y}" for d in w.index]
                tabla_periodos(w, etiquetas, "Semana")

            st.download_button("📥 Descargar informe mensual (CSV para Excel)",
                               tbl_m.to_csv(index=False, sep=";", decimal=",").encode("utf-8-sig"),
                               file_name=f"rentabilidad_{ambito.lower()}_{datetime.now():%Y%m%d}.csv", mime="text/csv")

# =============================================================================
# 4. OPERACIONES
# =============================================================================
if 4 in _SEL:
    with tabs[4]:
        if tx.empty:
            st.info("No hay operaciones registradas.")
        else:
            f1, f2 = st.columns(2)
            sel_tok = f1.multiselect("Token", list(TOKENS), default=list(TOKENS))
            sel_tipo = f2.multiselect("Tipo", sorted(tx["tipo"].unique()), default=sorted(tx["tipo"].unique()))
            ops = tx[tx["token"].isin(sel_tok) & tx["tipo"].isin(sel_tipo)].copy()
            ops["precio_hoy"] = ops["token"].map(current)
            es_compra = ops["cantidad"] > 0
            ops["valor_hoy"] = np.where(es_compra, ops["cantidad"] * ops["precio_hoy"], np.nan)
            ops["res_lote"] = np.where(es_compra, ops["valor_hoy"] - ops["total"], np.nan)
            ops["res_lote_pct"] = np.where(es_compra & (ops["total"] > 0), ops["res_lote"] / ops["total"] * 100, np.nan)

            compras = ops[es_compra & (ops["total"] > 0)]
            n_verde = int((compras["res_lote"] > 0).sum())
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Operaciones", len(ops), help=f"{int(es_compra.sum())} compras/entradas · {int((~es_compra).sum())} ventas")
            m2.metric("Comisiones pagadas", eur(ops["comision"].sum()))
            m3.metric("Comisión media en compras",
                      pct(compras["comision"].sum() / compras["total"].sum() * 100, sign=False) if not compras.empty else "—")
            m4.metric("Compras en beneficio", f"{n_verde} de {len(compras)}",
                      help="Compras cuyo valor hoy supera lo que pagaste por ellas.")

            tabla = pd.DataFrame({
                "Fecha": ops["fecha"].dt.strftime("%d/%m/%Y"), "Token": ops["token"], "Tipo": ops["tipo"],
                "Cantidad": ops["cantidad"], "Precio": ops["precio"], "Comisión": ops["comision"], "Total": ops["total"],
                "Plataforma": ops["plataforma"], "Custodia": ops["custodia"],
                "Valor hoy": ops["valor_hoy"], "Resultado": ops["res_lote"], "Resultado %": ops["res_lote_pct"],
            }).iloc[::-1]
            sty = (tabla.style
                   .format({"Cantidad": lambda v: fmt(v, 4), "Precio": lambda v: eur(v, 4), "Comisión": eur,
                            "Total": eur, "Valor hoy": eur, "Resultado": lambda v: eur(v, sign=True), "Resultado %": pct},
                           na_rep="—")
                   .map(color_sign, subset=["Resultado", "Resultado %"]))
            st.dataframe(sty, hide_index=True, height=420, **WIDE)

            st.subheader("💸 ¿Cuánto te cuesta cada plataforma?")
            plat = (tx[(tx["cantidad"] > 0) & (tx["total"] > 0)].groupby("plataforma")
                    .agg(comision=("comision", "sum"), total=("total", "sum"), n=("total", "size")))
            plat["pct"] = plat["comision"] / plat["total"] * 100
            plat = plat.sort_values("pct")
            fig = go.Figure(go.Bar(x=plat["pct"], y=plat.index, orientation="h",
                                   marker_color=[POS if v < 1 else ("#f1d58a" if v < 3 else NEG) for v in plat["pct"]],
                                   text=[f"{fmt(v, 2)} % · {eur(c)} en {n} compras" for v, c, n in zip(plat["pct"], plat["comision"], plat["n"])],
                                   textposition="auto", hoverinfo="skip"))
            fig = style_fig(fig, 80 + 45 * len(plat))
            fig.update_layout(hovermode=False)
            fig.update_xaxes(ticksuffix=" %")
            chart(fig)
            st.caption("Comisión pagada sobre el importe de cada compra. Verde < 1 %, ámbar < 3 %, rojo ≥ 3 %.")

# =============================================================================
# 5. RIESGO
# =============================================================================
if 5 in _SEL:
    with tabs[5]:
        if daily.empty:
            st.info("No hay histórico para calcular métricas de riesgo.")
        else:
            rets = daily["ret"].iloc[1:]
            ult_anyo = rets[rets.index >= rets.index.max() - pd.Timedelta(days=365)]
            vol = ult_anyo.std() * np.sqrt(365) * 100 if len(ult_anyo) > 2 else np.nan
            mdd = daily["drawdown"].min()
            f_mdd = daily["drawdown"].idxmin()
            dd_hoy = daily["drawdown"].iloc[-1]
            ath = daily["valor"].max()
            f_ath = daily["valor"].idxmax()
            dias_verde = (daily["valor"] > daily["invertido"]).mean() * 100
            mejor, peor = rets.idxmax(), rets.idxmin()

            r1 = st.columns(4)
            r1[0].metric("Caída máxima (drawdown)", pct(mdd), help=f"Peor caída desde un máximo, el {f_mdd:%d/%m/%Y}. Sin contar aportaciones.")
            r1[1].metric("Caída actual desde máximos", pct(dd_hoy))
            r1[2].metric("Volatilidad anual", pct(vol, sign=False), help="Cuánto oscila la cartera en un año típico. Bolsa ≈ 15-20 %, cripto suele superar 60 %.")
            r1[3].metric("Días en beneficio", pct(dias_verde, 0, sign=False))
            r2 = st.columns(4)
            r2[0].metric("Valor máximo de la cartera", eur(ath),
                         help=f"Alcanzado el {f_ath:%d/%m/%Y}. Incluye el dinero que has ido aportando, "
                              "por eso puede estar en máximos aunque los precios no lo estén.")
            subida_necesaria = (100 / (100 + dd_hoy) - 1) * 100 if dd_hoy < 0 else 0.0
            r2[1].metric("Subida para recuperar", pct(subida_necesaria) if subida_necesaria > 0 else "¡En máximos!",
                         help="Cuánto tendrían que subir los precios de tu cartera para volver a su mejor rentabilidad "
                              f"(caída actual {pct(dd_hoy)}). Una caída del 50 % necesita una subida del 100 % para recuperarse.")
            r2[2].metric("Mejor día", pct(rets.max() * 100), help=f"{mejor:%d/%m/%Y}")
            r2[3].metric("Peor día", pct(rets.min() * 100), help=f"{peor:%d/%m/%Y}")

            fig = go.Figure(go.Scatter(x=daily.index, y=daily["drawdown"], mode="lines", fill="tozeroy",
                                       line=dict(color=NEG, width=1.5), fillcolor="rgba(239,68,68,0.2)",
                                       hovertemplate="%{y:.2f} %", name="Caída"))
            fig = style_fig(fig, 260)
            fig.update_layout(title=dict(text="Distancia a máximos (%)", x=0), showlegend=False)
            fig.update_yaxes(ticksuffix=" %")
            chart(fig)

            mayor = pos.loc[pos["peso"].idxmax()]
            st.info(f"**Concentración:** el {fmt(mayor['peso'], 1)} % de tu cartera está en {mayor['token']}, y XRP y XLM "
                    "suelen moverse muy juntos, así que en la práctica la diversificación es baja. "
                    "Una caída del 50 % en ambos supondría perder unos "
                    f"{eur(val_total * 0.5)}.")

# =============================================================================
# 6. SIMULADORES
# =============================================================================
if 6 in _SEL:
    with tabs[6]:
        st.subheader("🧮 Simulador de compra")
        s1, s2 = st.columns([1, 2])
        with s1:
            tok_c = st.selectbox("Token", list(P.index), key="calc_tok")
            rc = P.loc[tok_c]
            fee_def = 0.4
            if not tx.empty:
                ult = tx[(tx["token"] == tok_c) & (tx["cantidad"] > 0) & (tx["total"] > 0)].tail(10)
                if not ult.empty and ult["total"].sum() > 0:
                    fee_def = round(float(ult["comision"].sum() / ult["total"].sum() * 100), 2)
            importe = st.number_input("Importe a invertir (€)", min_value=1.0, value=50.0, step=10.0)
            precio_c = st.number_input("Precio de compra (€)", min_value=0.000001, value=float(rc["precio"]), format="%.5f")
            fee = st.number_input("Comisión (%)", min_value=0.0, max_value=10.0, value=fee_def, step=0.1,
                                  help="Por defecto, la media de tus últimas 10 compras de este token.")
        with s2:
            tokens_nuevos = importe * (1 - fee / 100) / precio_c
            nueva_cant = rc["cantidad"] + tokens_nuevos
            nuevo_pm = (rc["invertido"] + importe) / nueva_cant
            a, b, c = st.columns(3)
            a.metric("Tokens que recibes", f"+{fmt(tokens_nuevos, 2)}")
            b.metric("Comisión", eur(importe * fee / 100))
            c.metric("Nuevo balance", fmt(nueva_cant, 2))
            st.metric("Nuevo precio medio", eur(nuevo_pm, 4),
                      delta=eur(nuevo_pm - rc["precio_medio"], 4, sign=True) + " vs actual", delta_color="inverse")

            st.markdown("**¿Cuánto tendría que comprar para bajar mi precio medio a…?**")
            q1, q2 = st.columns(2)
            with q1:
                objetivo_pm = st.number_input("Precio medio objetivo (€)", min_value=0.000001,
                                              value=float(round(rc["precio_medio"] * 0.95, 5)), format="%.5f")
            p_ef = precio_c / (1 - fee / 100)
            with q2:
                if objetivo_pm >= rc["precio_medio"]:
                    st.caption("Pon un objetivo por debajo de tu precio medio actual.")
                elif objetivo_pm <= p_ef:
                    st.warning(f"Imposible comprando a {eur(precio_c, 4)}: tu precio medio nunca bajará de {eur(p_ef, 4)} (precio + comisión).")
                else:
                    necesario = (objetivo_pm * rc["cantidad"] - rc["invertido"]) / (1 - objetivo_pm / p_ef)
                    st.success(f"Necesitarías invertir **{eur(necesario)}** a {eur(precio_c, 4)} para dejar tu precio medio en {eur(objetivo_pm, 4)}.")

        st.divider()
        st.subheader("🎯 Simulador de objetivos")
        o1, o2 = st.columns([1, 2])
        with o1:
            tok_o = st.selectbox("Token", list(P.index), key="obj_tok")
            ro = P.loc[tok_o]
            modo = st.radio("Simular por", ["% de subida", "Precio objetivo", "Valor objetivo de la posición"])
            if modo == "% de subida":
                subida = st.number_input("Subida (%)", value=100.0, step=10.0)
                p_obj = ro["precio"] * (1 + subida / 100)
            elif modo == "Precio objetivo":
                p_obj = st.number_input("Precio objetivo (€)", min_value=0.000001, value=float(ro["precio"] * 2), format="%.5f")
            else:
                v_obj = st.number_input("Valor objetivo (€)", min_value=1.0, value=float(round(ro["valor"] * 2, -1)), step=100.0)
                p_obj = v_obj / ro["cantidad"] if ro["cantidad"] > 0 else ro["precio"]
        with o2:
            v_fut = ro["cantidad"] * p_obj
            g_fut = v_fut - ro["invertido"]
            a, b, c = st.columns(3)
            a.metric("Precio objetivo", eur(p_obj, 4), delta=pct((p_obj / ro["precio"] - 1) * 100) + " vs hoy")
            b.metric("Valor de la posición", eur(v_fut))
            c.metric("Beneficio", eur(g_fut, sign=True), delta=pct(g_fut / ro["invertido"] * 100) if ro["invertido"] > 0 else None)
            (st.success if g_fut >= 0 else st.error)(
                f"Si {tok_o} llega a {eur(p_obj, 4)}, tu posición valdría {eur(v_fut)} "
                f"({'ganancia' if g_fut >= 0 else 'pérdida'} de {eur(abs(g_fut))} sobre lo invertido).")

        st.markdown("**Escenarios para toda la cartera** (todos los tokens se mueven el mismo %)")
        escenarios = [-50, -25, 0, 25, 50, 100, 200, 400]
        filas = []
        for e in escenarios:
            fila = {"Escenario": "Hoy" if e == 0 else f"{e:+d} %"}
            for tok in P.index:
                fila[f"Precio {tok}"] = P.at[tok, "precio"] * (1 + e / 100)
            fila["Valor cartera"] = val_total * (1 + e / 100)
            fila["Beneficio"] = fila["Valor cartera"] - inv_total
            filas.append(fila)
        esc = pd.DataFrame(filas)
        formatos = {f"Precio {tok}": (lambda v: eur(v, 4)) for tok in P.index}
        formatos.update({"Valor cartera": eur, "Beneficio": lambda v: eur(v, sign=True)})
        st.dataframe(esc.style.format(formatos, na_rep="—").map(color_sign, subset=["Beneficio"]), hide_index=True, **WIDE)

# =============================================================================
# 7. FISCALIDAD
# =============================================================================
if 7 in _SEL:
    with tabs[7]:
        st.caption("Cálculo orientativo con método FIFO (las primeras unidades compradas son las primeras vendidas), "
                   "que es el que aplica Hacienda en España. No sustituye a un asesor fiscal: no incluye permutas "
                   "cripto-cripto, staking ni otras rentas.")
        gratis = tx[(tx["cantidad"] > 0) & (tx["fiscal"] <= 0)] if not tx.empty else tx
        if not gratis.empty:
            st.warning("Hay compras con coste fiscal 0 € en tu hoja (regalos o recompensas, sin coste de adquisición): "
                       + "; ".join(f"{r.fecha:%d/%m/%Y} {r.token} {fmt(r.cantidad, 4)}" for r in gratis.itertuples())
                       + ". No cuentan como dinero invertido (el beneficio del panel es correcto). Si Hacienda debe considerarlas "
                         "con valor de mercado, anótalo en una columna «Coste fiscal» de la hoja; consúltalo con tu asesor [VERIFICAR].")
        st.caption("Solo se calculan las monedas que tienes en tu hoja de control (XRP, XLM…). Si en algún año vendiste otras "
                   "(p. ej. LTC, ETH o ADA en un exchange), esas ventas no están aquí y también cuentan en la renta.")
        if tx.empty or (tx["cantidad"] < 0).sum() == 0:
            st.info("No hay ventas registradas, así que no hay ganancias realizadas que declarar.")
        else:
            rz = fifo_realized(tx)
            rz["Año"] = rz["Fecha"].dt.year
            resumen = rz.groupby("Año")[["Transmisión (€)", "Adquisición (€)", "Ganancia (€)"]].sum().reset_index()
            cols = st.columns(len(resumen))
            for col, r in zip(cols, resumen.itertuples()):
                col.metric(f"Ganancia/pérdida patrimonial {r.Año}", eur(r[4], sign=True),
                           help=f"Transmisión {eur(r[2])} − Adquisición {eur(r[3])}")
            rz_disp = rz.drop(columns="Año").iloc[::-1]
            rz_disp["Fecha"] = rz_disp["Fecha"].dt.strftime("%d/%m/%Y")
            st.dataframe(rz_disp.style.format({"Cantidad": lambda v: fmt(v, 4), "Transmisión (€)": eur,
                                               "Adquisición (€)": eur, "Ganancia (€)": lambda v: eur(v, sign=True)},
                                              na_rep="—")
                         .map(color_sign, subset=["Ganancia (€)"]), hide_index=True, **WIDE)
            st.download_button("📥 Descargar ventas FIFO (CSV)",
                               rz_disp.to_csv(index=False, sep=";", decimal=",").encode("utf-8-sig"),
                               file_name=f"ventas_fifo_{datetime.now():%Y%m%d}.csv", mime="text/csv")

# =============================================================================
# 8. NOTICIAS
# =============================================================================
if 8 in _SEL:
    with tabs[8]:
        noticias = load_noticias()
        if not noticias:
            st.info("Todavía no hay noticias guardadas. Te llegarán a Telegram a las horas de envío y aparecerán aquí.")
        else:
            nt = pd.DataFrame(noticias)
            nt["fecha_envio"] = pd.to_datetime(nt["fecha_envio"], utc=True).dt.tz_convert("Europe/Madrid")
            nt = nt.sort_values("fecha_envio", ascending=False)

            n1, n2, n3, n4 = st.columns(4)
            n1.metric("Noticias guardadas", len(nt))
            n2.metric("👍 Útiles", int((nt["valoracion"] == 1).sum()))
            n3.metric("👎 No interesantes", int((nt["valoracion"] == -1).sum()))
            n4.metric("Sin valorar", int((nt["valoracion"] == 0).sum()),
                      help="Valóralas en Telegram con los botones: así la IA aprende qué te interesa.")

            with st.expander("📊 Qué fuentes y temas te sirven (según tus 👍/👎)"):
                def utilidad(col):
                    g = nt.groupby(col)["valoracion"].agg(Enviadas="count", **{"👍": lambda v: int((v == 1).sum()),
                                                                              "👎": lambda v: int((v == -1).sum())}).reset_index()
                    g["Valoradas"] = g["👍"] + g["👎"]
                    g["% útiles"] = np.where(g["Valoradas"] > 0, g["👍"] / g["Valoradas"].replace(0, np.nan) * 100, np.nan)
                    g["Fiabilidad"] = np.where(g["Valoradas"] >= 5, "con datos", "pocos votos")
                    return g.sort_values(["Valoradas", "Enviadas"], ascending=False)
                st.caption("Con menos de 5 votos por fuente no hay datos fiables: vota también los 👎, que son los que más enseñan al bot "
                           "qué descartar.")
                for etiqueta, col in (("Por tema", "tema"), ("Por fuente", "fuente")):
                    st.markdown(f"**{etiqueta}**")
                    st.dataframe(utilidad(col).style.format({"% útiles": lambda v: pct(v, 0, False)}, na_rep="—"),
                                 hide_index=True, **WIDE)

            f1, f2, f3 = st.columns([2, 1, 2])
            temas_sel = f1.multiselect("Tema", sorted(nt["tema"].unique()), default=sorted(nt["tema"].unique()))
            filtro_val = f2.selectbox("Valoración", ["Todas", "👍 Útiles", "👎 No interesantes", "Sin valorar"])
            buscar = f3.text_input("Buscar", placeholder="p. ej. ETF, SEC, Fed…")

            vista = nt[nt["tema"].isin(temas_sel)]
            vista = {"👍 Útiles": vista[vista["valoracion"] == 1], "👎 No interesantes": vista[vista["valoracion"] == -1],
                     "Sin valorar": vista[vista["valoracion"] == 0]}.get(filtro_val, vista)
            if buscar:
                texto = (vista["titulo"] + " " + vista["resumen"] + " " + vista["por_que"]).str.lower()
                vista = vista[texto.str.contains(buscar.lower(), regex=False)]

            import vistas
            modo = st.radio("Ver", ["📂 Por tema", "🏷️ Por etiqueta", "🕒 Recientes"], horizontal=True,
                            key="noticias_vista", label_visibility="collapsed")
            st.caption(f"{len(vista)} noticias")
            md = lambda s: str(s).replace("$", "\\$")  # evita que Streamlit interprete '$' como fórmula

            def tarjeta_noticia(r):
                voto = {1: "👍", -1: "👎"}.get(r.valoracion, "")
                with st.container(border=True):
                    st.markdown(f"**{md(r.titulo)}** {voto}")
                    st.caption(f"{r.tema} · ⭐ {r.puntuacion}/10 · {r.fecha_envio:%d/%m/%Y %H:%M} · {md(r.fuente)}")
                    st.markdown(md(r.resumen))
                    st.markdown(f"💡 *{md(r.por_que)}*")
                    st.markdown(enlace("Leer la noticia completa →", r.url))

            def grupo_noticias(nombre, g):
                utiles = int((g["valoracion"] == 1).sum())
                titulo = f"{nombre} · {len(g)}" + (f" · 👍 {utiles}" if utiles else "")
                with st.expander(titulo, expanded=False):
                    for r in g.head(30).itertuples():
                        tarjeta_noticia(r)

            if modo == "📂 Por tema":
                for tema, g in sorted(vista.groupby("tema"), key=lambda x: -len(x[1])):
                    grupo_noticias(tema, g)
            elif modo == "🏷️ Por etiqueta":
                et = vista.assign(etiquetas=[vistas.etiquetar(r.titulo, r.resumen, r.tema) for r in vista.itertuples()])
                st.caption("Las etiquetas se detectan por palabras clave; una noticia puede estar en varias.")
                orden = sorted(vistas.ETIQUETAS, key=lambda e: -sum(e in x for x in et["etiquetas"]))
                for e in orden:
                    g = et[[e in x for x in et["etiquetas"]]]
                    if len(g):
                        grupo_noticias(e, g)
                sin = et[[not x for x in et["etiquetas"]]]
                if len(sin):
                    grupo_noticias("📄 Sin etiqueta", sin)
            else:
                for r in vista.head(100).itertuples():
                    tarjeta_noticia(r)

# =============================================================================
# 9. WATCHLIST — valores que sigues (no son posiciones)
# =============================================================================
if 9 in _SEL:
    with tabs[9]:
        st.caption("Valores que SIGUES (no son posiciones tuyas). Se editan en watchlist.toml. Datos de Yahoo Finance, "
                   "no oficiales y con retraso. Es información, no una recomendación de compra o venta.")
        wl = []
        try:
            if tomllib is not None:
                with open(Path(__file__).parent / "watchlist.toml", "rb") as fh:
                    wl = tomllib.load(fh).get("valores", [])
        except Exception:
            wl = []
        if not wl:
            st.info("No se pudo leer watchlist.toml.")
        else:
            datos = watchlist_datos(tuple(v["yahoo"] for v in wl))
            eurusd = (datos.get("EURUSD=X") or {}).get("precio")
            eurgbp = (datos.get("EURGBP=X") or {}).get("precio")

            def a_euros(d):
                if not d:
                    return np.nan
                m, p = d["moneda"], d["precio"]
                if m == "EUR":
                    return p
                if m == "USD" and eurusd:
                    return p / eurusd
                if m == "GBP" and eurgbp:
                    return p / eurgbp
                if m == "GBp" and eurgbp:
                    return p / 100 / eurgbp
                return np.nan
            filas = []
            for v in wl:
                d = datos.get(v["yahoo"])
                filas.append({"Ticker": v["ticker"], "Nombre": v["nombre"], "Categoría": v["categoria"],
                              "Moneda": d["moneda"] if d else "—", "Precio": d["precio"] if d else np.nan, "Precio (€)": a_euros(d),
                              "1 semana": d["1s"] if d else np.nan, "3 meses": d["3m"] if d else np.nan,
                              "En el año": d["ytd"] if d else np.nan})
            w = pd.DataFrame(filas)
            fallos = int(w["Precio"].isna().sum())
            if fallos:
                st.warning(f"No se pudieron leer {fallos} de {len(w)} valores (Yahoo no respondió). Prueba en unos minutos.")
            cats = ["Todas"] + sorted(w["Categoría"].unique())
            cat = st.selectbox("Categoría", cats, key="wl_cat")
            if cat != "Todas":
                w = w[w["Categoría"] == cat]
            graf = w.dropna(subset=["En el año"]).sort_values("En el año")
            if not graf.empty:
                fig = go.Figure(go.Bar(x=graf["En el año"], y=graf["Ticker"], orientation="h",
                                       marker_color=[POS if x >= 0 else NEG for x in graf["En el año"]],
                                       text=[pct(x, 1) for x in graf["En el año"]], textposition="outside",
                                       hovertemplate="%{y}: %{x:.1f} %<extra></extra>"))
                fig = style_fig(fig, height=max(260, 26 * len(graf) + 80))
                fig.update_layout(title="Rentabilidad en el año (%)", hovermode="closest")
                chart(fig)
            st.dataframe(w.style.format({"Precio": lambda v: fmt(v, 2), "Precio (€)": eur, "1 semana": pct, "3 meses": pct,
                                         "En el año": pct}, na_rep="—")
                         .map(color_sign, subset=["1 semana", "3 meses", "En el año"]), hide_index=True, **WIDE)

# =============================================================================
# 10. EVENTOS — calendario macro y cripto (eventos/calendario.toml)
# =============================================================================
if 10 in _SEL:
    with tabs[10]:
        st.caption("Próximos eventos que mueven el mercado, con la fuente oficial de cada fecha. Se editan en eventos/calendario.toml "
                   "y el bot te avisa por Telegram el día antes. Información, no una recomendación.")
        evs = []
        try:
            if tomllib is not None:
                with open(Path(__file__).parent / "eventos" / "calendario.toml", "rb") as fh:
                    evs = tomllib.load(fh).get("eventos", [])
        except Exception:
            evs = []
        hoy_d = datetime.now(ZoneInfo("Europe/Madrid")).date()
        prox = []
        for e in evs:
            ini = datetime.strptime(e["fecha"], "%Y-%m-%d").date()
            fin = datetime.strptime(e.get("hasta", e["fecha"]), "%Y-%m-%d").date()
            if fin >= hoy_d:
                prox.append((ini, fin, e))
        if not prox:
            st.info("No hay eventos próximos en el calendario.")
        for ini, fin, e in sorted(prox, key=lambda x: x[0]):
            dias = (ini - hoy_d).days
            cuando_txt = "en curso" if ini <= hoy_d else ("hoy" if dias == 0 else ("mañana" if dias == 1 else f"en {dias} días"))
            rango = ("≈ " if e.get("aproximado") else "") + f"{ini:%d/%m/%Y}" + (f" → {fin:%d/%m/%Y}" if fin != ini else "")
            marca = "🔴" if e.get("impacto") == "alto" else "🟡"
            with st.container(border=True):
                st.markdown(f"{marca} **{html_lib.escape(e['titulo'])}** · {rango} · _{cuando_txt}_")
                st.caption(f"{e.get('detalle', '')} " + (f"[Fuente]({e['fuente']})" if str(e.get("fuente", "")).startswith("https://") else ""))

# =============================================================================
# 7 (continuación). FISCALIDAD — informe para la renta (renta.py)
# =============================================================================
if 7 in _SEL:
    with tabs[7]:
        st.divider()
        st.subheader("🧾 Informe para la renta")
        if tx.empty:
            st.info("Cuando haya operaciones en tu hoja, aquí aparecerá el informe.")
        else:
            import renta
            lineas_r, abiertos_r, avisos_r = renta.lotes_fifo(tx.assign(total=np.where(tx["cantidad"] > 0, tx["fiscal"], tx["total"]))[["fecha", "token", "cantidad", "total"]].to_dict("records"))
            anios_r = sorted({l["f_venta"].year for l in lineas_r}, reverse=True)
            if not anios_r:
                st.info("No hay ventas registradas: no hay plusvalías que declarar.")
            else:
                anio_r = st.selectbox("Ejercicio", anios_r, key="renta_anio")
                res_r = renta.resumen_anual(lineas_r)[anio_r]
                m1, m2, m3 = st.columns(3)
                m1.metric("Valor de transmisión", eur(res_r["transmision"]))
                m2.metric("Valor de adquisición", eur(res_r["adquisicion"]))
                m3.metric("Ganancia / pérdida", eur(res_r["ganancia"], sign=True))
                for a in avisos_r:
                    st.warning(a)
                det = pd.DataFrame([{"Moneda": l["token"], "Adquisición": l["f_compra"].strftime("%d/%m/%Y") if l["f_compra"] else "sin compra",
                                     "Transmisión": l["f_venta"].strftime("%d/%m/%Y"), "Cantidad": l["cantidad"],
                                     "Valor adq. (€)": l["v_adquisicion"], "Valor transm. (€)": l["v_transmision"],
                                     "Ganancia (€)": l["ganancia"]} for l in lineas_r if l["f_venta"].year == anio_r])
                st.dataframe(det.style.format({"Cantidad": lambda v: fmt(v, 4), "Valor adq. (€)": eur, "Valor transm. (€)": eur,
                                               "Ganancia (€)": lambda v: eur(v, sign=True)})
                             .map(color_sign, subset=["Ganancia (€)"]), hide_index=True, **WIDE)
                d1, d2 = st.columns(2)
                d1.download_button("📄 Informe para imprimir (HTML → PDF)", renta.html_anio(lineas_r, avisos_r, anio_r).encode("utf-8"),
                                   file_name=f"plusvalias_cripto_{anio_r}.html", mime="text/html", key="renta_html")
                d2.download_button("📥 Detalle por lote (CSV)", renta.csv_anio(lineas_r, anio_r).encode("utf-8-sig"),
                                   file_name=f"plusvalias_cripto_{anio_r}.csv", mime="text/csv", key="renta_csv")
                st.caption("Abre el HTML en el navegador y usa Imprimir → Guardar como PDF. Cálculo orientativo: contrasta cada cifra con tus "
                           "extractos y con tu asesor. No incluye monedas fuera de tu hoja, permutas, staking ni recompensas.")


# =============================================================================
# 11. SISTEMA — estado de los bots, fuentes y gasto (sistema.py)
# =============================================================================
if 11 in _SEL:
    with tabs[11]:
        import sistema
        sistema.mostrar()


# Última línea: todo lo de arriba ya está dibujado, así que la página de entrada retira su pantalla de carga ahora
# (antes se retiraba al cargar los datos y se veían las pestañas y gráficos montándose: cortes y parpadeos)
listo()
