import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de página
st.set_page_config(page_title="Control de Portfolio Cripto", page_icon="⚡", layout="wide")

# Estilos CSS avanzados para fondo oscuro estilo Kraken Pro
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #e5e7eb; }
    .stMetric { background-color: #151921; padding: 16px; border-radius: 12px; border: 1px solid #262c3a; }
    div[data-testid="stExpander"] { background-color: #151921; border-radius: 12px; border: 1px solid #262c3a; margin-bottom: 12px; }
    </style>
""", unsafe_allow_html=True)

# PEGA TU ENLACE CSV ENTRE LAS COMILLAS (OBLIGATORIO DEJAR LAS COMILLAS)
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxCL1k_cfYOIyrznI1IBxAhTl6UEhljn4mKJKFfjf1NXwh9wG4f1TCUBevW1vRIG88RJ_0UV2ohFcI/pub?gid=1415212158&single=true&output=csv"

@st.cache_data(ttl=10)
def load_data():
    try:
        df = pd.read_csv(SHEET_CSV_URL)
        
        # Limpieza robusta de columnas numéricas (formato español / texto a número)
        cols_num = ["Cantidad Total TK", "Inversión Total (€)", "Precio Medio (€)", "Precio Actual (€)", "Valor Actual (€)", "PnL No Realizado (€)", "PnL No Realizado (%)"]
        
        for col in cols_num:
            if col in df.columns:
                # Convertir a texto, limpiar comas, puntos y símbolo de Euro
                df[col] = df[col].astype(str).str.replace('€', '', regex=False)
                df[col] = df[col].str.replace('%', '', regex=False)
                df[col] = df[col].str.replace(' ', '', regex=False)
                
                # Manejo de formato decimal en español (puntos de miles y coma decimal)
                df[col] = df[col].apply(lambda x: x.replace('.', '').replace(',', '.') if ',' in x else x)
                
                # Convertir a numérico forzado (si falla pone 0.0)
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)

        if "Token" in df.columns:
            df = df[df["Token"].astype(str).str.upper() != "TOTAL"]
            
        return df
    except Exception as e:
        return pd.DataFrame()

df = load_data()

st.title("⚡ Control de Portfolio Cripto")
st.caption("Sincronizado en tiempo real con Google Sheets")

if st.sidebar.button("🔄 Actualizar datos"):
    st.cache_data.clear()
    st.rerun()

st.markdown("---")

if not df.empty:
    # 1. MÉTRICAS GENERALES (SUMA SEGURA)
    inv_total = float(df["Inversión Total (€)"].sum()) if "Inversión Total (€)" in df.columns else 0.0
    val_actual = float(df["Valor Actual (€)"].sum()) if "Valor Actual (€)" in df.columns else 0.0
    
    if "PnL No Realizado (€)" in df.columns:
        pnl_eur = float(df["PnL No Realizado (€)"].sum())
    else:
        pnl_eur = val_actual - inv_total
        
    pnl_pct = (pnl_eur / inv_total * 100) if inv_total > 0 else 0.0

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Inversión Total", f"{inv_total:,.2f} €")
    with c2: st.metric("Valor Actual", f"{val_actual:,.2f} €")
    with c3: st.metric("PnL No Realizado", f"{pnl_eur:,.2f} €", delta=f"{pnl_eur:,.2f} €")
    with c4: st.metric("Rendimiento Total", f"{pnl_pct:.2f} %", delta=f"{pnl_pct:.2f} %")

    st.markdown("---")

    # 2. SECCIÓN KRAKEN PRO: DESGLOSE POR ACTIVO INTERACTIVO
    st.subheader("💼 Vistas de Activo (Estilo Kraken Pro)")
    st.caption("Haz clic en un token para ver el desglose detallado de balance, coste base y PnL:")

    for index, row in df.iterrows():
        token = str(row.get("Token", "N/A"))
        cant = float(row.get("Cantidad Total TK", 0.0))
        p_medio = float(row.get("Precio Medio (€)", 0.0))
        p_act = float(row.get("Precio Actual (€)", 0.0))
        v_act = float(row.get("Valor Actual (€)", 0.0))
        inv = float(row.get("Inversión Total (€)", 0.0))
        pnl = float(row.get("PnL No Realizado (€)", 0.0))
        pnl_p = float(row.get("PnL No Realizado (%)", 0.0))

        with st.expander(f"📌 **{token}** — Balance: {cant:,.2f} {token} | Valor: {v_act:,.2f} €", expanded=False):
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                st.write(f"**Balance Disponible:** {cant:,.4f} {token}")
                st.write(f"**Valor Estimado:** {v_act:,.2f} €")
            with m2:
                st.write(f"**Precio Medio:** {p_medio:,.4f} €")
                st.write(f"**Precio Actual:** {p_act:,.4f} €")
            with m3:
                st.write(f"**Coste Base:** {inv:,.2f} €")
                st.write(f"**PnL Realizado:** 0.00 €")
            with m4:
                color_pnl = "🟢" if pnl >= 0 else "🔴"
                st.write(f"**PnL No Realizado:** {color_pnl} {pnl:,.2f} €")
                st.write(f"**% PnL Sin Realizar:** {pnl_p:.2f} %")

    st.markdown("---")

    # 3. GRÁFICOS VISUALES MEJORADOS
    g1, g2 = st.columns(2)

    with g1:
        st.subheader("📊 Distribución del Portfolio")
        fig_pie = px.pie(
            df, values="Valor Actual (€)", names="Token", hole=0.6,
            color_discrete_sequence=["#3b82f6", "#10b981"]
        )
        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#ffffff", size=14), showlegend=True
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)

    with g2:
        st.subheader("⚖️ Invertido vs Valor Actual")
        fig_bar = go.Figure(data=[
            go.Bar(name='Invertido (€)', x=df['Token'], y=df['Inversión Total (€)'], marker_color='#4b5563'),
            go.Bar(name='Valor Actual (€)', x=df['Token'], y=df['Valor Actual (€)'], marker_color='#3b82f6')
        ])
        fig_bar.update_layout(
            barmode='group', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#ffffff"), yaxis=dict(gridcolor='#262c3a')
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")

    # 4. CALCULADORA DE COMPRA RÁPIDA
    st.subheader("🧮 Calculadora de Adquisición de Tokens")
    st.write("Calcula cuántos tokens recibirás al hacer una nueva inversión según el precio actual:")

    calc_col1, calc_col2 = st.columns([1, 2])

    with calc_col1:
        token_sel = st.selectbox("Selecciona el token:", df["Token"].tolist())
        euros_inv = st.number_input("Monto a invertir (€):", min_value=1.0, value=50.0, step=10.0)

        row_token = df[df["Token"] == token_sel].iloc[0]
        precio_ref = float(row_token["Precio Actual (€)"]) if "Precio Actual (€)" in df.columns else 1.0

        tokens_adquiridos = euros_inv / precio_ref if precio_ref > 0 else 0.0

    with calc_col2:
        st.info(f"💡 Al precio actual de **{precio_ref:,.4f} €** por **{token_sel}**:")
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric(f"Tokens {token_sel} a recibir", f"+{tokens_adquiridos:,.2f} {token_sel}")
        with res_col2:
            nuevo_balance = float(row_token["Cantidad Total TK"]) + tokens_adquiridos
            st.metric("Nuevo Balance Estimado", f"{nuevo_balance:,.2f} {token_sel}")

    st.markdown("---")

    # 5. SIMULADOR DE ESCENARIOS Y PROYECCIONES
    st.subheader("🔮 Simulador de Proyecciones Futuras")
    reval_pct = st.slider("Porcentaje de Revalorización Estimado (%)", min_value=-50, max_value=500, value=25, step=5)
    
    val_proyectado = val_actual * (1 + reval_pct / 100.0)
    beneficio_est = val_proyectado - inv_total

    sim1, sim2 = st.columns(2)
    with sim1: st.metric("Valor Proyectado Total", f"{val_proyectado:,.2f} €", delta=f"{reval_pct}% estimado")
    with sim2: st.metric("Beneficio Estimado", f"{beneficio_est:,.2f} €")

else:
    st.warning("No se pudieron cargar los datos. Revisa que el enlace CSV dentro de SHEET_CSV_URL sea correcto y esté entre comillas.")
