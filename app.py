import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de página nativa de Streamlit
st.set_page_config(page_title="Control de Portfolio Cripto", page_icon="⚡", layout="wide")

# URLs CSV de Google Sheets
SHEET_RESUMEN_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxCL1k_cfYOIyrznI1IBxAhTl6UEhljn4mKJKFfjf1NXwh9wG4f1TCUBevW1vRIG88RJ_0UV2ohFcI/pub?gid=1415212158&single=true&output=csv"
SHEET_XRP_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxCL1k_cfYOIyrznI1IBxAhTl6UEhljn4mKJKFfjf1NXwh9wG4f1TCUBevW1vRIG88RJ_0UV2ohFcI/pub?gid=2015592342&single=true&output=csv"
SHEET_XLM_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxCL1k_cfYOIyrznI1IBxAhTl6UEhljn4mKJKFfjf1NXwh9wG4f1TCUBevW1vRIG88RJ_0UV2ohFcI/pub?gid=108352087&single=true&output=csv"

@st.cache_data(ttl=10)
def load_resumen_data():
    try:
        df = pd.read_csv(SHEET_RESUMEN_URL)
        df.columns = df.columns.str.strip()
        
        cols_num = ["Cantidad Total TK", "Inversión Total (€)", "Precio Medio (€)", "Precio Actual (€)", "Valor Actual (€)", "P&L No Realizado (€)", "P&L No Realizado (%)"]
        for col in cols_num:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace('€', '', regex=False).str.replace('%', '', regex=False).str.replace(' ', '', regex=False)
                df[col] = df[col].apply(lambda x: x.replace('.', '').replace(',', '.') if ',' in x else x)
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)

        if "Token" in df.columns:
            df = df[df["Token"].astype(str).str.upper() != "TOTAL"]
            
        return df
    except Exception:
        return pd.DataFrame()

@st.cache_data(ttl=30)
def load_history_data():
    dataframes = []
    for url, token_name in [(SHEET_XRP_URL, "XRP"), (SHEET_XLM_URL, "XLM")]:
        try:
            df_temp = pd.read_csv(url)
            df_temp.columns = [str(c).strip().upper() for c in df_temp.columns]
            
            # Identificar columnas automáticamente
            fecha_col = next((c for c in df_temp.columns if "FECHA" in c), None)
            inv_col = next((c for c in df_temp.columns if "INVERTIDO" in c or "TOTAL" in c or "EUR" in c), None)
            wallet_col = next((c for c in df_temp.columns if "HOLDING" in c or "WALLET" in c), None)
            
            if fecha_col and inv_col:
                fechas = pd.to_datetime(df_temp[fecha_col], errors='coerce', dayfirst=True)
                
                montos_str = df_temp[inv_col].astype(str).str.replace('€', '', regex=False).str.replace(' ', '', regex=False)
                montos_str = montos_str.apply(lambda x: x.replace('.', '').replace(',', '.') if ',' in x else x)
                montos = pd.to_numeric(montos_str, errors='coerce').fillna(0.0)
                
                wallets = df_temp[wallet_col].astype(str).str.strip().str.upper() if wallet_col else "OTRO"
                
                df_clean = pd.DataFrame({
                    'Fecha': fechas,
                    'Invertido': montos,
                    'Wallet': wallets,
                    'Token': token_name
                }).dropna(subset=['Fecha'])
                
                df_clean = df_clean[df_clean['Invertido'] > 0]
                if not df_clean.empty:
                    dataframes.append(df_clean)
        except Exception:
            continue

    if dataframes:
        df_all = pd.concat(dataframes, ignore_index=True)
        return df_all.sort_values('Fecha')
    return pd.DataFrame()

df = load_resumen_data()
df_hist = load_history_data()

st.title("⚡ Control de Portfolio Cripto")
st.caption("Sincronizado en tiempo real con Google Sheets")

if st.sidebar.button("🔄 Actualizar Datos"):
    st.cache_data.clear()
    st.rerun()

st.markdown("---")

if not df.empty:
    # 1. MÉTRICAS GENERALES (KPIs) — NO SE TOCA
    inv_total = float(df["Inversión Total (€)"].sum()) if "Inversión Total (€)" in df.columns else 0.0
    val_actual = float(df["Valor Actual (€)"].sum()) if "Valor Actual (€)" in df.columns else 0.0
    
    pnl_col = "P&L No Realizado (€)" if "P&L No Realizado (€)" in df.columns else "PnL No Realizado (€)"
    pnl_eur = float(df[pnl_col].sum()) if pnl_col in df.columns else (val_actual - inv_total)
    pnl_pct = (pnl_eur / inv_total * 100) if inv_total > 0 else 0.0

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Inversión Total", f"{inv_total:,.2f} €")
    with c2: st.metric("Valor Actual", f"{val_actual:,.2f} €")
    with c3: st.metric("P&L No Realizado", f"{pnl_eur:,.2f} €", delta=f"{pnl_eur:,.2f} €")
    with c4: st.metric("Rendimiento Total", f"{pnl_pct:.2f} %", delta=f"{pnl_pct:.2f} %")

    st.markdown("---")

    # ==============================================================================
    # PASO 1: DESGLOSE COMPACTO MÓVIL (BLINDADO Y CERRADO) — NO SE TOCA
    # ==============================================================================
    st.subheader("💼 Desglose de Posiciones por Activo")

    for index, row in df.iterrows():
        token = str(row.get("Token", "N/A"))
        cant = float(row.get("Cantidad Total TK", 0.0))
        p_medio = float(row.get("Precio Medio (€)", 0.0))
        p_act = float(row.get("Precio Actual (€)", 0.0))
        inv_indiv = float(row.get("Inversión Total (€)", 0.0))
        val_indiv = float(row.get("Valor Actual (€)", 0.0))
        
        pnl_val = row.get("P&L No Realizado (€)", row.get("PnL No Realizado (€)", val_indiv - inv_indiv))
        pnl_pct_val = row.get("P&L No Realizado (%)", row.get("PnL No Realizado (%)", (pnl_val / inv_indiv * 100) if inv_indiv > 0 else 0.0))
        
        pnl_indiv_eur = float(pnl_val)
        pnl_indiv_pct = float(pnl_pct_val)
        color_pnl = "#10b981" if pnl_indiv_eur >= 0 else "#ef4444"

        with st.expander(f"📌 {token} — Balance: {cant:,.2f} {token} | Valor: {val_indiv:,.2f} €", expanded=True):
            st.markdown(f"""
            <div style="background-color: #151921; padding: 12px; border-radius: 10px; border: 1px solid #262c3a; font-size: 14px; color: #ffffff;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                    <div><b>Balance:</b> {cant:,.2f} {token}</div>
                    <div><b>Precio Medio:</b> {p_medio:,.4f} €</div>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                    <div><b>Valor Estimado:</b> {val_indiv:,.2f} €</div>
                    <div><b>Precio Actual:</b> {p_act:,.4f} €</div>
                </div>
                <hr style="border: 0.5px solid #262c3a; margin: 8px 0;">
                <div style="display: flex; justify-content: space-between; font-weight: bold;">
                    <div>Invertido: {inv_indiv:,.2f} €</div>
                    <div style="color: {color_pnl};">P&L: {pnl_indiv_eur:,.2f} € ({pnl_indiv_pct:.2f}%)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # ==============================================================================
    # PASO 2: GRÁFICOS (DONUT ANIDADO + HISTÓRICO KOINLY)
    # ==============================================================================
    g1, g2 = st.columns(2)
    with g1:
        st.subheader("📊 Distribución y Custodia de Capital")
        
        # Donut de 2 Niveles: Anillo Interior (Token) + Anillo Exterior (Wallet / Exchange)
        if not df_hist.empty and "Wallet" in df_hist.columns:
            df_sun = df_hist.groupby(["Token", "Wallet"])["Invertido"].sum().reset_index()
            fig_pie = px.sunburst(
                df_sun,
                path=['Token', 'Wallet'],
                values='Invertido',
                color='Token',
                color_discrete_map={'XRP': '#3b82f6', 'XLM': '#10b981'}
            )
            fig_pie.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color="#ffffff"),
                margin=dict(l=10, r=10, t=10, b=10)
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            fig_pie = px.pie(df, values="Valor Actual (€)", names="Token", hole=0.55)
            fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#ffffff"))
            st.plotly_chart(fig_pie, use_container_width=True)

    with g2:
        st.subheader("📈 Evolución Histórica (Estilo Koinly)")
        if not df_hist.empty:
            df_grouped = df_hist.groupby('Fecha')['Invertido'].sum().reset_index()
            df_grouped['Coste Acumulado (€)'] = df_grouped['Invertido'].cumsum()

            fig_koinly = go.Figure()
            fig_koinly.add_trace(go.Scatter(
                x=df_grouped['Fecha'],
                y=df_grouped['Coste Acumulado (€)'],
                mode='lines+markers',
                name='Coste Base (€)',
                line=dict(color='#2563eb', width=3),
                fill='tozeroy',
                fillcolor='rgba(37, 99, 235, 0.15)'
            ))

            fig_koinly.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color="#ffffff"),
                margin=dict(l=10, r=10, t=10, b=10),
                xaxis=dict(showgrid=False, title=None),
                yaxis=dict(showgrid=True, gridcolor='#262c3a', title="Euros (€)"),
                hovermode="x unified"
            )
            st.plotly_chart(fig_koinly, use_container_width=True)
        else:
            st.warning("Verifica que las pestañas contengan las columnas de FECHA y TOTAL INVERTIDO (€).")

    st.markdown("---")

    # 4. CALCULADORA DE ADQUISICIÓN DE TOKENS — NO SE TOCA
    st.subheader("🧮 Calculadora de Adquisición de Tokens")
    calc_c1, calc_c2 = st.columns([1, 2])
    with calc_c1:
        token_sel = st.selectbox("Selecciona el token:", df["Token"].tolist())
        euros_inv = st.number_input("Monto a invertir (€):", min_value=1.0, value=50.0, step=10.0)
        row_token = df[df["Token"] == token_sel].iloc[0]
        precio_ref = float(row_token["Precio Actual (€)"]) if "Precio Actual (€)" in df.columns else 1.0
        tokens_adquiridos = euros_inv / precio_ref if precio_ref > 0 else 0.0

    with calc_c2:
        st.info(f"💡 Al precio actual de {precio_ref:,.4f} € por {token_sel}:")
        res_c1, res_c2 = st.columns(2)
        with res_c1:
            st.metric(f"Tokens {token_sel} a adquirir", f"+{tokens_adquiridos:,.2f} {token_sel}")
        with res_c2:
            nuevo_balance = float(row_token["Cantidad Total TK"]) + tokens_adquiridos
            st.metric("Nuevo Balance Estimado", f"{nuevo_balance:,.2f} {token_sel}")
