import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Control de Portfolio Cripto", page_icon="⚡", layout="wide")

# ESTILOS CSS CON ALTO CONTRASTE (Textos en Blanco Puro)
st.markdown("""
    <style>
    /* Fondo General */
    .stApp { background-color: #0d1117 !important; color: #ffffff !important; }
    
    /* Textos y Etiquetas de Métricas en Blanco */
    div[data-testid="stMetricLabel"] { color: #f3f4f6 !important; font-size: 15px !important; font-weight: 600 !important; }
    div[data-testid="stMetricValue"] { color: #ffffff !important; font-weight: bold !important; }
    
    /* Cajas de Métricas */
    .stMetric { background-color: #161b22 !important; padding: 18px !important; border-radius: 10px !important; border: 1px solid #30363d !important; }
    
    /* Desplegables / Expanders */
    div[data-testid="stExpander"] { background-color: #161b22 !important; border-radius: 10px !important; border: 1px solid #30363d !important; margin-bottom: 12px !important; }
    div[data-testid="stExpander"] * { color: #ffffff !important; }
    
    /* Subtítulos y Títulos */
    h1, h2, h3, p, span, label { color: #ffffff !important; }
    
    /* Campos de Entrada / Calculadora */
    .stNumberInput input, .stSelectbox div { color: #ffffff !important; background-color: #21262d !important; }
    </style>
    /* Añade esto dentro de tu bloque de estilos <style> */
div[data-baseweb="select"] * {
    color: #ffffff !important;
    background-color: #1f2937 !important;
}
ul[data-baseweb="menu"] {
    background-color: #1f2937 !important;
}
li[data-baseweb="option"] {
    color: #ffffff !important;
}
""", unsafe_allow_html=True)

# PEGA AQUÍ TU ENLACE CSV DE GOOGLE SHEETS ENTRE COMILLAS
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxCL1k_cfYOIyrznI1IBxAhTl6UEhljn4mKJKFfjf1NXwh9wG4f1TCUBevW1vRIG88RJ_0UV2ohFcI/pub?gid=1415212158&single=true&output=csv"

@st.cache_data(ttl=10)
def load_data():
    try:
        df = pd.read_csv(SHEET_CSV_URL)
        
        # Limpieza de formatos de texto a número (formato ES)
        cols_num = ["Cantidad Total TK", "Inversión Total (€)", "Precio Medio (€)", "Precio Actual (€)", "Valor Actual (€)", "PnL No Realizado (€)", "PnL No Realizado (%)"]
        
        for col in cols_num:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace('€', '', regex=False)
                df[col] = df[col].str.replace('%', '', regex=False)
                df[col] = df[col].str.replace(' ', '', regex=False)
                df[col] = df[col].apply(lambda x: x.replace('.', '').replace(',', '.') if ',' in x else x)
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)

        if "Token" in df.columns:
            df = df[df["Token"].astype(str).str.upper() != "TOTAL"]
            
        return df
    except Exception as e:
        return pd.DataFrame()

df = load_data()

st.title("⚡ Control de Portfolio Cripto")
st.caption("Sincronizado en tiempo real con Google Sheets")

if st.sidebar.button("🔄 Actualizar Datos"):
    st.cache_data.clear()
    st.rerun()

st.markdown("---")

if not df.empty:
    # 1. MÉTRICAS GENERALES
    inv_total = float(df["Inversión Total (€)"].sum()) if "Inversión Total (€)" in df.columns else 0.0
    val_actual = float(df["Valor Actual (€)"].sum()) if "Valor Actual (€)" in df.columns else 0.0
    
    pnl_eur = float(df["PnL No Realizado (€)"].sum()) if "PnL No Realizado (€)" in df.columns else (val_actual - inv_total)
    pnl_pct = (pnl_eur / inv_total * 100) if inv_total > 0 else 0.0

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Inversión Total", f"{inv_total:,.2f} €")
    with c2: st.metric("Valor Actual", f"{val_actual:,.2f} €")
    with c3: st.metric("PnL No Realizado", f"{pnl_eur:,.2f} €", delta=f"{pnl_eur:,.2f} €")
    with c4: st.metric("Rendimiento Total", f"{pnl_pct:.2f} %", delta=f"{pnl_pct:.2f} %")

    st.markdown("---")

    # 2. DESGLOSE DE POSICIONES (ESTRUCTURA DE TABLA LIMPIA)
    st.subheader("💼 Desglose de Posiciones por Activo")

    for index, row in df.iterrows():
        token = str(row.get("Token", "N/A"))
        cant = float(row.get("Cantidad Total TK", 0.0))
        p_medio = float(row.get("Precio Medio (€)", 0.0))
        p_act = float(row.get("Precio Actual (€)", 0.0))
        v_act = float(row.get("Valor Actual (€)", 0.0))
        inv = float(row.get("Inversión Total (€)", 0.0))
        pnl = float(row.get("PnL No Realizado (€)", 0.0))
        pnl_p = float(row.get("PnL No Realizado (%)", 0.0))

        with st.expander(f"📌 **{token}** — Balance: {cant:,.2f} {token} | Valor: {v_act:,.2f} €"):
            # Tabla estructurada de 4 columnas
            col_a, col_b, col_c, col_d = st.columns(4)
            with col_a:
                st.markdown(f"**Balance Total:**\n{cant:,.4f} {token}")
                st.markdown(f"**Valor Estimado:**\n{v_act:,.2f} €")
            with col_b:
                st.markdown(f"**Precio Medio:**\n{p_medio:,.4f} €")
                st.markdown(f"**Precio Actual:**\n{p_act:,.4f} €")
            with col_c:
                st.markdown(f"**Coste Base (Invertido):**\n{inv:,.2f} €")
            with col_d:
                color_str = "🟢" if pnl >= 0 else "🔴"
                st.markdown(f"**P&L No Realizado (€):**\n{color_str} {pnl:,.2f} €")
                st.markdown(f"**P&L No Realizado (%):**\n{pnl_p:.2f} %")

    st.markdown("---")

    # 3. GRÁFICOS: CIRCULAR + EVOLUCIÓN TEMPORAL DE LÍNEAS
    g1, g2 = st.columns(2)

    with g1:
        st.subheader("📊 Distribución del Capital")
        fig_pie = px.pie(
            df, values="Valor Actual (€)", names="Token", hole=0.55,
            color_discrete_sequence=["#2563eb", "#10b981"]
        )
        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#ffffff", size=14), showlegend=True
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)

    with g2:
        st.subheader("📈 Evolución Temporal del Capital")
        # Generación de gráfico de línea temporal comparando Inversión vs Valor Actual por token
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=df['Token'], y=df['Inversión Total (€)'], mode='lines+markers', name='Invertido (€)', line=dict(color='#9ca3af', width=3)))
        fig_line.add_trace(go.Scatter(x=df['Token'], y=df['Valor Actual (€)'], mode='lines+markers', name='Valor Actual (€)', line=dict(color='#3b82f6', width=3)))
        
        fig_line.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#ffffff"),
            xaxis=dict(showgrid=False, title="Token"),
            yaxis=dict(showgrid=True, gridcolor='#30363d', title="Euros (€)")
        )
        st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("---")

    # 4. CALCULADORA DE COMPRA DE TOKENS
    st.subheader("🧮 Calculadora de Adquisición de Tokens")
    
    calc_c1, calc_c2 = st.columns([1, 2])

    with calc_c1:
        token_sel = st.selectbox("Selecciona el token:", df["Token"].tolist())
        euros_inv = st.number_input("Monto a invertir (€):", min_value=1.0, value=50.0, step=10.0)

        row_token = df[df["Token"] == token_sel].iloc[0]
        precio_ref = float(row_token["Precio Actual (€)"]) if "Precio Actual (€)" in df.columns else 1.0
        tokens_adquiridos = euros_inv / precio_ref if precio_ref > 0 else 0.0

    with calc_c2:
        st.info(f"💡 Al precio actual de **{precio_ref:,.4f} €** por **{token_sel}**:")
        res_c1, res_c2 = st.columns(2)
        with res_c1:
            st.metric(f"Tokens {token_sel} a adquirir", f"+{tokens_adquiridos:,.2f} {token_sel}")
        with res_c2:
            nuevo_balance = float(row_token["Cantidad Total TK"]) + tokens_adquiridos
            st.metric("Nuevo Balance Estimado", f"{nuevo_balance:,.2f} {token_sel}")

    st.markdown("---")

    # 5. SIMULADOR DE ESCENARIOS
    st.subheader("🔮 Simulador de Proyecciones Futuras")
    reval_pct = st.slider("Revalorización estimada (%)", min_value=-50, max_value=500, value=25, step=5)
    
    val_proyectado = val_actual * (1 + reval_pct / 100.0)
    beneficio_est = val_proyectado - inv_total

    sim1, sim2 = st.columns(2)
    with sim1: st.metric("Valor Proyectado Total", f"{val_proyectado:,.2f} €", delta=f"{reval_pct}% estimado")
    with sim2: st.metric("Beneficio Estimado", f"{beneficio_est:,.2f} €")

else:
    st.warning("No se cargaron los datos. Revisa la URL CSV en SHEET_CSV_URL.")
