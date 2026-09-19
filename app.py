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

def read_sheet_with_dynamic_header(url, target_keyword):
    try:
        raw_df = pd.read_csv(url, header=None, on_bad_lines='skip')
        header_idx = None
        for idx, row in raw_df.iterrows():
            row_str = " ".join(row.fillna('').astype(str).values).upper()
            if target_keyword.upper() in row_str:
                header_idx = idx
                break
        
        if header_idx is not None:
            df = pd.read_csv(url, skiprows=header_idx, on_bad_lines='skip')
        else:
            df = pd.read_csv(url, on_bad_lines='skip')
            
        df.columns = [str(c).strip() for c in df.columns]
        return df
    except Exception:
        return pd.DataFrame()

def clean_numeric_series(series):
    s_str = series.fillna('0').astype(str)
    s_str = s_str.str.replace('€', '', regex=False).str.replace('%', '', regex=False).str.replace(' ', '', regex=False)
    s_str = s_str.str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    return pd.to_numeric(s_str, errors='coerce').fillna(0.0)

@st.cache_data(ttl=10)
def load_resumen_data():
    df = read_sheet_with_dynamic_header(SHEET_RESUMEN_URL, "Token")
    if df.empty:
        return pd.DataFrame()

    cols_num = ["Cantidad Total TK", "Inversión Total (€)", "Precio Medio (€)", "Precio Actual (€)", "Valor Actual (€)", "P&L No Realizado (€)", "P&L No Realizado (%)"]
    for col in cols_num:
        col_match = next((c for c in df.columns if col.upper() in c.upper()), None)
        if col_match:
            df[col] = clean_numeric_series(df[col_match])

    tok_col = next((c for c in df.columns if "TOKEN" in c.upper()), "Token")
    if tok_col in df.columns:
        df["Token"] = df[tok_col]
        df = df[df["Token"].astype(str).str.upper() != "TOTAL"]
        
    return df

def process_transaction_sheet(url, token_name):
    df = read_sheet_with_dynamic_header(url, "FECHA")
    if df.empty:
        return pd.DataFrame()

    df.columns = [str(c).strip().upper() for c in df.columns]

    c_fecha = next((c for c in df.columns if "FECHA" in c), None)
    c_inv = next((c for c in df.columns if "INVERTIDO" in c or "TOTAL" in c), None)
    c_cant = next((c for c in df.columns if "CANTIDAD" in c), None)
    
    # BUSCAMOS EXCLUSIVAMENTE LA COLUMNA WALLET/HOLDING
    c_holding = next((c for c in df.columns if "HOLDING" in c or "WALLET/HOLDING" in c), None)

    if not c_fecha or not c_inv:
        return pd.DataFrame()

    df['Fecha_Clean'] = pd.to_datetime(df[c_fecha], errors='coerce', dayfirst=True)
    df['Invertido_Clean'] = clean_numeric_series(df[c_inv])
    df['Cantidad_Clean'] = clean_numeric_series(df[c_cant]) if c_cant else 0.0

    if c_holding:
        df['Holding_Clean'] = df[c_holding].fillna('DESCONOCIDO').astype(str).str.strip().str.upper()
        df['Holding_Clean'] = df['Holding_Clean'].replace({'NAN': 'DESCONOCIDO', '': 'DESCONOCIDO'})
    else:
        df['Holding_Clean'] = 'DESCONOCIDO'

    df['Token_Clean'] = token_name
    
    df_res = df[['Fecha_Clean', 'Invertido_Clean', 'Cantidad_Clean', 'Holding_Clean', 'Token_Clean']].dropna(subset=['Fecha_Clean'])
    return df_res[df_res['Invertido_Clean'] > 0]

@st.cache_data(ttl=30)
def load_history_data():
    df_xrp = process_transaction_sheet(SHEET_XRP_URL, "XRP")
    df_xlm = process_transaction_sheet(SHEET_XLM_URL, "XLM")
    
    frames = [f for f in [df_xrp, df_xlm] if not f.empty]
    if frames:
        df_all = pd.concat(frames, ignore_index=True)
        return df_all.sort_values('Fecha_Clean')
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
    # 1. MÉTRICAS GENERALES (KPIs)
    inv_total = float(df["Inversión Total (€)"].sum()) if "Inversión Total (€)" in df.columns else 0.0
    val_actual = float(df["Valor Actual (€)"].sum()) if "Valor Actual (€)" in df.columns else 0.0
    
    pnl_col = next((c for c in df.columns if "P&L" in c.upper() or "PNL" in c.upper()), None)
    if pnl_col and "P&L No Realizado (€)" in df.columns:
        pnl_eur = float(df["P&L No Realizado (€)"].sum())
    else:
        pnl_eur = val_actual - inv_total

    pnl_pct = (pnl_eur / inv_total * 100) if inv_total > 0 else 0.0

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Inversión Total", f"{inv_total:,.2f} €")
    with c2: st.metric("Valor Actual", f"{val_actual:,.2f} €")
    with c3: st.metric("P&L No Realizado", f"{pnl_eur:,.2f} €", delta=f"{pnl_eur:,.2f} €")
    with c4: st.metric("Rendimiento Total", f"{pnl_pct:.2f} %", delta=f"{pnl_pct:.2f} %")

    st.markdown("---")

    # ==============================================================================
    # BLOQUE 1: DESGLOSE CON CUSTODIA DETALLADA (EXCLUSIVAMENTE WALLET/HOLDING)
    # ==============================================================================
    st.subheader("💼 Desglose de Posiciones por Activo")

    for index, row in df.iterrows():
        token = str(row.get("Token", "N/A"))
        cant = float(row.get("Cantidad Total TK", 0.0))
        p_medio = float(row.get("Precio Medio (€)", 0.0))
        p_act = float(row.get("Precio Actual (€)", 0.0))
        inv_indiv = float(row.get("Inversión Total (€)", 0.0))
        val_indiv = float(row.get("Valor Actual (€)", 0.0))
        
        pnl_val = row.get("P&L No Realizado (€)", val_indiv - inv_indiv)
        pnl_pct_val = row.get("P&L No Realizado (%)", (pnl_val / inv_indiv * 100) if inv_indiv > 0 else 0.0)
        
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

            # Desglose de custodia únicamente tomando WALLET/HOLDING
            if not df_hist.empty:
                df_tok_custody = df_hist[df_hist['Token_Clean'] == token]
                if not df_tok_custody.empty:
                    st.markdown("<div style='margin-top: 10px; font-weight: bold; font-size: 13px;'>🔒 Custodia Actual (Wallet / Holding):</div>", unsafe_allow_html=True)
                    cust_summary = df_tok_custody.groupby('Holding_Clean').agg(
                        {'Invertido_Clean': 'sum', 'Cantidad_Clean': 'sum'}
                    ).reset_index()
                    
                    total_inv_tok = cust_summary['Invertido_Clean'].sum()
                    
                    for _, c_row in cust_summary.iterrows():
                        w_name = c_row['Holding_Clean']
                        w_inv = c_row['Invertido_Clean']
                        w_cant = c_row['Cantidad_Clean']
                        w_pct = (w_inv / total_inv_tok * 100) if total_inv_tok > 0 else 0.0
                        
                        st.markdown(f"""
                        <div style="display: flex; justify-content: space-between; background-color: #1a202c; padding: 6px 10px; border-radius: 6px; margin-top: 4px; font-size: 12px;">
                            <div><b>{w_name}</b></div>
                            <div>{w_cant:,.2f} {token} ({w_inv:,.2f} €)</div>
                            <div style="color: #3b82f6;"><b>{w_pct:.1f}%</b></div>
                        </div>
                        """, unsafe_allow_html=True)

    st.markdown("---")

    # ==============================================================================
    # BLOQUE 2: GRÁFICOS (DISTRIBUCIÓN DEL CAPITAL + HISTÓRICO SEPARADO POR TOKEN)
    # ==============================================================================
    g1, g2 = st.columns(2)
    with g1:
        st.subheader("📊 Distribución del Capital")
        fig_pie = px.pie(df, values="Valor Actual (€)", names="Token", hole=0.55,
                         color="Token", color_discrete_map={'XRP': '#2563eb', 'XLM': '#10b981'})
        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#ffffff"),
            margin=dict(l=10, r=10, t=10, b=10)
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with g2:
        st.subheader("📈 Evolución Histórica por Activo (Estilo Koinly)")
        if not df_hist.empty:
            fig_koinly = go.Figure()

            colors = {'XRP': '#2563eb', 'XLM': '#10b981'}
            for token_name in df_hist['Token_Clean'].unique():
                df_t = df_hist[df_hist['Token_Clean'] == token_name].groupby('Fecha_Clean')['Invertido_Clean'].sum().reset_index()
                df_t['Coste Acumulado (€)'] = df_t['Invertido_Clean'].cumsum()

                fig_koinly.add_trace(go.Scatter(
                    x=df_t['Fecha_Clean'],
                    y=df_t['Coste Acumulado (€)'],
                    mode='lines+markers',
                    name=f'Coste {token_name} (€)',
                    line=dict(color=colors.get(token_name, '#f59e0b'), width=3)
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
            st.info("Cargando datos de evolución temporal...")

    st.markdown("---")

    # CALCULADORA
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
