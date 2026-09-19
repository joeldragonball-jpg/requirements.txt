import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="Portfolio Cripto Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo visual oscuro profesional
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #374151; }
    </style>
""", unsafe_allow_html=True)

# 1. Carga y preparación de datos desde tu Google Sheets (o CSV exportado)
@st.cache_data
def load_data():
    # Estructura basada en tu pestaña 'Resumen Portfolio'
    data = {
        "Token": ["XRP", "XLM"],
        "Cantidad Total TK": [2736.7027, 4276.9220],
        "Inversión Total (€)": [3255.15, 670.77],
        "Precio Medio (€)": [1.189, 0.157],
        "Precio Actual (€)": [1.16076, 0.163447],
        "Valor Actual (€)": [3176.66, 699.05],
        "PnL No Realizado (€)": [-78.48, 28.28],
        "PnL No Realizado (%)": [-2.41, 4.22]
    }
    df = pd.DataFrame(data)
    return df

df = load_data()

# Header
st.title("⚡ Control de Portfolio Cripto")
st.caption("Panel de control en tiempo real y proyecciones de rendimiento")
st.markdown("---")

# 2. Métricas Clave (KPIs)
inv_total = df["Inversión Total (€)"].sum()
val_actual = df["Valor Actual (€)"].sum()
pnl_eur = df["PnL No Realizado (€)"].sum()
pnl_pct = (pnl_eur / inv_total) * 100 if inv_total > 0 else 0.0

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Inversión Total", f"{inv_total:,.2f} €")
with col2:
    st.metric("Valor Actual Portfolio", f"{val_actual:,.2f} €")
with col3:
    st.metric(
        "PnL No Realizado (€)", 
        f"{pnl_eur:,.2f} €", 
        delta=f"{pnl_eur:,.2f} €", 
        delta_color="normal"
    )
with col4:
    st.metric(
        "Rendimiento Global (%)", 
        f"{pnl_pct:.2f} %", 
        delta=f"{pnl_pct:.2f} %", 
        delta_color="normal"
    )

st.markdown("---")

# 3. Gráficos Visuales
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Distribución del Capital (Valor Actual)")
    fig_donut = px.pie(
        df, 
        values="Valor Actual (€)", 
        names="Token", 
        hole=0.5,
        color_discrete_sequence=["#2563eb", "#059669"],
        template="plotly_dark"
    )
    fig_donut.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_donut, use_container_width=True)

with col_right:
    st.subheader("⚖️ Comparativa: Invertido vs Valor Actual")
    fig_bar = go.Figure(data=[
        go.Bar(name='Invertido (€)', x=df['Token'], y=df['Inversión Total (€)'], marker_color='#6b7280'),
        go.Bar(name='Valor Actual (€)', x=df['Token'], y=df['Valor Actual (€)'], marker_color='#3b82f6')
    ])
    fig_bar.update_layout(barmode='group', template="plotly_dark")
    st.plotly_chart(fig_bar, use_container_width=True)

# 4. Tabla Detallada
st.subheader("📋 Resumen por Asset")
st.dataframe(
    df.style.format({
        "Cantidad Total TK": "{:,.4f}",
        "Inversión Total (€)": "{:,.2f} €",
        "Precio Medio (€)": "{:,.4f} €",
        "Precio Actual (€)": "{:,.4f} €",
        "Valor Actual (€)": "{:,.2f} €",
        "PnL No Realizado (€)": "{:,.2f} €",
        "PnL No Realizado (%)": "{:.2f} %"
    }),
    use_container_width=True
)

st.markdown("---")

# 5. Simulador / Proyecciones Futuras
st.subheader("🔮 Simulador de Rendimiento y Escenarios")
st.write("Ajusta el porcentaje de revalorización estimado para ver cómo se proyecta tu portfolio:")

sim_col1, sim_col2 = st.columns([1, 2])

with sim_col1:
    reval_pct = st.slider("Crecimiento/Revalorización esperada (%)", min_value=-50, max_value=500, value=25, step=5)
    valor_proyectado = val_actual * (1 + reval_pct / 100.0)
    beneficio_proyectado = valor_proyectado - inv_total

    st.metric("Valor Proyectado", f"{valor_proyectado:,.2f} €", delta=f"{reval_pct}% estimado")
    st.metric("Beneficio Total Estimado", f"{beneficio_proyectado:,.2f} €")

with sim_col2:
    # Gráfico de proyección
    df_sim = df.copy()
    df_sim["Valor Proyectado (€)"] = df_sim["Valor Actual (€)"] * (1 + reval_pct / 100.0)
    
    fig_sim = px.bar(
        df_sim, 
        x="Token", 
        y=["Valor Actual (€)", "Valor Proyectado (€)"],
        barmode="group",
        title=f"Proyección por Token con Revalorización del {reval_pct}%",
        template="plotly_dark",
        color_discrete_sequence=["#3b82f6", "#10b981"]
    )
    st.plotly_chart(fig_sim, use_container_width=True)
