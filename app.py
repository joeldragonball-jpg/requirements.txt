import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de página
st.set_page_config(page_title="Control de Porfolio Cripto", page_icon="⚡", layout="wide")

# Estilos CSS avanzados para forzar el fondo, ocultar elementos de Streamlit y limpiar la interfaz móvil
hide_streamlit_style = """
    <style>
        /* Forzar el color de fondo principal en toda la aplicación */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #0e1117 !important;
        }

        /* Ocultar elementos de desarrollo de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Ajuste de márgenes para la versión móvil */
        .stApp { margin-top: -20px; }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Inyectar el Manifest y metadatos para la instalación PWA en el móvil
pwa_header = """
    <link rel="manifest" href="https://raw.githubusercontent.com/joeldragonball-jpg/requirements.txt/main/manifest.json">
    <meta name="theme-color" content="#0e1117">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
"""
st.markdown(pwa_header, unsafe_allow_html=True)

# URLS CSV de Google Sheets
SHEET_RESUMEN_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vScLk_CfOYzrjn1IBu8kANtfGGEenlI1b4M_4KkFf1FNxw9u4f1ITCVBeuvId2-0c_0mMj45etvFVQqTrg/pub?gid=365927779&single=true&output=csv"
SHEET_XRP_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vScLk_CfOYzrjn1IBu8kANtfGGEenlI1b4M_4KkFf1FNxw9u4f1ITCVBeuvId2-0c_0mMj45etvFVQqTrg/pub?gid=10835208&single=true&output=csv"
SHEET_XLM_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vScLk_CfOYzrjn1IBu8kANtfGGEenlI1b4M_4KkFf1FNxw9u4f1ITCVBeuvId2-0c_0mMj45etvFVQqTrg/pub?gid=298064972&single=true&output=csv"

@st.cache_data(ttl=10)
def read_raw_sheet(url):
    try:
        return pd.read_csv(url, header=None, on_bad_lines='skip')
    except:
        return pd.DataFrame()

def def_clean_numeric_series(series):
    s_str = series.astype(str).str.strip()
    s_str = s_str.str.replace('€', '', regex=False).str.replace('%', '', regex=False)
    s_str = s_str.str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    return pd.to_numeric(s_str, errors='coerce').fillna(0.0)

@st.cache_data(ttl=10)
def load_resumen_data():
    df = read_raw_sheet(SHEET_RESUMEN_URL)
    if df.empty:
        return pd.DataFrame()
    
    header_idx = None
    for idx, row in df.iterrows():
        row_str = "".join(row.astype(str).values).upper()
        if "VALOR" in row_str or "ACTIVO" in row_str:
            header_idx = idx
            break
            
    if header_idx is not None:
        df.columns = df.iloc[header_idx].astype(str).str.strip()
        df = df.iloc[header_idx + 1:].reset_index(drop=True)
    
    cols_num = ['Cantidad Total TK', 'Inversión Total (€)', 'Precio Medio (€)', 'Precio Actual (€)', 'Valor Actual (€)', 'P&L No Realizado (€)', 'Rendimiento Total (%)']
    for col in cols_num:
        if col in df.columns:
            df[col] = def_clean_numeric_series(df[col])
            
    if 'Token' in df.columns:
        df['Token'] = df['Token'].astype(str).str.strip().str.upper()
        
    return df

@st.cache_data(ttl=10)
def load_tx_sheet(url, token_name):
    df = read_raw_sheet(url)
    if df.empty:
        return pd.DataFrame()
    
    header_idx = None
    for idx, row in df.iterrows():
        row_str = "".join(row.astype(str).values).upper()
        if "FECHA" in row_str and "CANTIDAD" in row_str:
            header_idx = idx
            break
            
    if header_idx is not None:
        df.columns = df.iloc[header_idx].astype(str).str.strip()
        df = df.iloc[header_idx + 1:].reset_index(drop=True)
    
    # Renombrar columnas clave por posición o coincidencia
    mapping = {}
    for c in df.columns:
        c_upper = c.upper()
        if 'FECHA' in c_upper:
            mapping[c] = 'Fecha'
        elif 'CANTIDAD' in c_upper:
            mapping[c] = 'Cantidad'
        elif 'PRECIO UNITARIO' in c_upper:
            mapping[c] = 'PrecioUnitario'
        elif 'TOTAL INVERTIDO' in c_upper or 'INVERTIDO' in c_upper:
            mapping[c] = 'Invertido'
            
    df = df.rename(columns=mapping)
    
    if 'Fecha' in df.columns and 'Cantidad' in df.columns:
        df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
        df['Cantidad'] = def_clean_numeric_series(df['Cantidad'])
        if 'PrecioUnitario' in df.columns:
            df['PrecioUnitario'] = def_clean_numeric_series(df['PrecioUnitario'])
        else:
            df['PrecioUnitario'] = 0.0
            
        if 'Invertido' in df.columns:
            df['Invertido'] = def_clean_numeric_series(df['Invertido'])
        else:
            df['Invertido'] = df['Cantidad'] * df['PrecioUnitario']
            
        df['Token'] = token_name
        df = df.dropna(subset=['Fecha']).sort_values('Fecha').reset_index(drop=True)
        return df[['Fecha', 'Token', 'Cantidad', 'PrecioUnitario', 'Invertido']]
        
    return pd.DataFrame()

# Cargar datos principales
df_resumen = load_resumen_data()
df_xrp = load_tx_sheet(SHEET_XRP_URL, "XRP")
df_xlm = load_tx_sheet(SHEET_XLM_URL, "XLM")

# Encabezado Principal de la App
st.markdown("<h1 style='text-align: center; color: #f0f2f6;'>⚡ Control de Portfolio Cripto</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #808495;'>Sincronizado en tiempo real con Google Sheets</p>", unsafe_allow_html=True)
st.markdown("---")

# Calcular KPIs globales
total_invertido_val = 0.0
valor_actual_val = 0.0

if not df_resumen.empty:
    if 'Inversión Total (€)' in df_resumen.columns:
        total_invertido_val = df_resumen['Inversión Total (€)'].sum()
    if 'Valor Actual (€)' in df_resumen.columns:
        valor_actual_val = df_resumen['Valor Actual (€)'].sum()

pnl_val = valor_actual_val - total_invertido_val
rendimiento_val = (pnl_val / total_invertido_val * 100) if total_invertido_val > 0 else 0.0

# Tarjetas KPI
col1, col2 = st.columns(2)
with col1:
    st.metric("Inversión Total", f"{total_invertido_val:,.2f} €")
    st.metric("P&L No Realizado", f"{pnl_val:,.2f} €", delta=f"{pnl_val:,.2f} €")
with col2:
    st.metric("Valor Actual", f"{valor_actual_val:,.2f} €")
    st.metric("Rendimiento Total", f"{rendimiento_val:,.2f} %")

st.markdown("---")

# -------------------------------------------------------------------------
# GRÁFICO HISTÓRICO AVANZADO ESTILO KOINLY (Con interpolación automática)
# -------------------------------------------------------------------------
st.subheader("📊 Evolución Histórica por Activo (Estilo Koinly)")

def crear_df_historico(df_tx, token_name, precio_actual_ref):
    if df_tx.empty:
        return pd.DataFrame()
    
    # Ordenar cronológicamente
    df = df_tx.sort_values('Fecha').copy()
    df['CantidadAcum'] = df['Cantidad'].cumsum()
    df['InvertidoAcum'] = df['Invertido'].cumsum()
    
    # Crear un rango de fechas diario desde la primera transacción hasta hoy
    min_date = df['Fecha'].min()
    max_date = pd.Timestamp.today()
    
    if pd.isna(min_date):
        return pd.DataFrame()
        
    date_range = pd.date_range(start=min_date, end=max_date, freq='D')
    df_full = pd.DataFrame({'Fecha': date_range})
    
    # Fusionar con las transacciones reales
    df_merged = pd.merge_asof(df_full, df, on='Fecha', direction='backward')
    df_merged['Token'] = token_name
    df_merged['CantidadAcum'] = df_merged['CantidadAcum'].fillna(0)
    df_merged['InvertidoAcum'] = df_merged['InvertidoAcum'].fillna(0)
    
    # Rellenar precios de forma interpolada lineal si hay vacíos
    if 'PrecioUnitario' in df_merged.columns:
        df_merged['PrecioUnitario'] = df_merged['PrecioUnitario'].replace(0, pd.NA).ffill().bfill()
        df_merged['PrecioUnitario'] = df_merged['PrecioUnitario'].fillna(precio_actual_ref)
    else:
        df_merged['PrecioUnitario'] = precio_actual_ref
        
    # Calcular el valor de mercado histórico diario
    df_merged['ValorMercado'] = df_merged['CantidadAcum'] * df_merged['PrecioUnitario']
    
    return df_merged[['Fecha', 'Token', 'CantidadAcum', 'InvertidoAcum', 'ValorMercado']]

# Obtener precios actuales de referencia desde el resumen si están disponibles
precio_xrp_ref = 1.24  # Valor por defecto orientativo
precio_xlm_ref = 0.16

if not df_resumen.empty:
    match_xrp = df_resumen[df_resumen['Token'] == 'XRP']
    if not match_xrp.empty and 'Precio Actual (€)' in match_xrp.columns:
        precio_xrp_ref = float(match_xrp['Precio Actual (€)'].values[0])
        
    match_xlm = df_resumen[df_resumen['Token'] == 'XLM']
    if not match_xlm.empty and 'Precio Actual (€)' in match_xlm.columns:
        precio_xlm_ref = float(match_xlm['Precio Actual (€)'].values[0])

hist_xrp = crear_df_historico(df_xrp, "XRP", precio_xrp_ref)
hist_xlm = crear_df_historico(df_xlm, "XLM", precio_xlm_ref)
df_hist_total = pd.concat([hist_xrp, hist_xlm], ignore_index=True)

if not df_hist_total.empty:
    fig_koinly = px.area(
        df_hist_total,
        x='Fecha',
        y='ValorMercado',
        color='Token',
        labels={'ValorMercado': 'Valor (€)', 'Fecha': 'Fecha', 'Token': 'Activo'},
        color_discrete_map={'XRP': '#2962ff', 'XLM': '#00e676'}
    )
    
    # Añadir líneas de coste de adquisición por debajo al estilo Koinly
    for token_name, color_line in [('XRP', '#1565c0'), ('XLM', '#00c853')]:
        df_t = df_hist_total[df_hist_total['Token'] == token_name]
        if not df_t.empty:
            fig_koinly.add_trace(
                go.Scatter(
                    x=df_t['Fecha'],
                    y=df_t['InvertidoAcum'],
                    mode='lines',
                    name=f'Coste {token_name} (€)',
                    line=dict(color=color_line, width=2, dash='dash')
                )
            )

    fig_koinly.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=10, r=10, t=30, b=10)
    )
    st.plotly_chart(fig_koinly, use_container_width=True)
else:
    st.info("Añade transacciones en tus hojas de Google Sheets para mostrar la evolución histórica.")

st.markdown("---")

# Desglose de posiciones existente
st.subheader("💼 Desglose de Posiciones por Activo")
if not df_resumen.empty:
    st.dataframe(df_resumen, use_container_width=True)
else:
    st.info("Cargando datos de posiciones...")
