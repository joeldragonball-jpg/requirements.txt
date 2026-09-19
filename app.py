import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de página y Ocultar elementos de Streamlit para móvil
st.set_page_config(page_title="Control de Portfolio Cripto", page_icon="⚡", layout="wide")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { margin-top: -20px; }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# URLs CSV de Google Sheets
SHEET_RESUMEN_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxCL1k_cfYOIyrznI1IBxAhTl6UEhljn4mKJKFfjf1NXwh9wG4f1TCUBevW1vRIG88RJ_0UV2ohFcI/pub?gid=1415212158&single=true&output=csv"
SHEET_XRP_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxCL1k_cfYOIyrznI1IBxAhTl6UEhljn4mKJKFfjf1NXwh9wG4f1TCUBevW1vRIG88RJ_0UV2ohFcI/pub?gid=2015592342&single=true&output=csv"
SHEET_XLM_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxCL1k_cfYOIyrznI1IBxAhTl6UEhljn4mKJKFfjf1NXwh9wG4f1TCUBevW1vRIG88RJ_0UV2ohFcI/pub?gid=108352087&single=true&output=csv"

def read_raw_csv(url):
    try:
        return pd.read_csv(url, header=None, on_bad_lines='skip')
    except Exception:
        return pd.DataFrame()

def clean_numeric_series(series):
    s_str = series.fillna('0').astype(str)
    s_str = s_str.str.replace('€', '', regex=False).str.replace('%', '', regex=False).str.replace(' ', '', regex=False)
    s_str = s_str.str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    return pd.to_numeric(s_str, errors='coerce').fillna(0.0)

@st.cache_data(ttl=10)
def load_resumen_data():
    raw_df = read_raw_csv(SHEET_RESUMEN_URL)
    if raw_df.empty:
        return pd.DataFrame(), {}

    header_idx = None
    for idx, row in raw_df.iterrows():
        row_str = " ".join(row.fillna('').astype(str).values).upper()
        if "TOKEN" in row_str and "CANTIDAD" in row_str:
            header_idx = idx
            break

    if header_idx is not None:
        df = pd.read_csv(SHEET_RESUMEN_URL, skiprows=header_idx, on_bad_lines='skip')
    else:
        df = pd.read_csv(SHEET_RESUMEN_URL, on_bad_lines='skip')

    df.columns = [str(c).strip() for c in df.columns]

    cols_num = ["Cantidad Total TK", "Inversión Total (€)", "Precio Medio (€)", "Precio Actual (€)", "Valor Actual (€)", "P&L No Realizado (€)", "P&L No Realizado (%)"]
    for col in cols_num:
        col_match = next((c for c in df.columns if col.upper() in c.upper()), None)
        if col_match:
            df[col] = clean_numeric_series(df[col_match])

    tok_col = next((c for c in df.columns if "TOKEN" in c.upper()), "Token")
    if tok_col in df.columns:
        df["Token"] = df[tok_col]
        df = df[df["Token"].astype(str).str.upper() != "TOTAL"]

    custody_data = {'XRP': {}, 'XLM': {}}
    try:
        for _, row in raw_df.iterrows():
            row_vals = [str(v).strip().upper() for v in row.fillna('').values]
            for w_name in ['LEDGER', 'KRAKEN']:
                if w_name in row_vals:
                    w_idx = row_vals.index(w_name)
                    if w_idx + 1 < len(row):
                        val_xrp = clean_numeric_series(pd.Series([row.iloc[w_idx + 1]])).iloc[0]
                        custody_data['XRP'][w_name] = float(val_xrp)
                    if w_idx + 2 < len(row):
                        val_xlm = clean_numeric_series(pd.Series([row.iloc[w_idx + 2]])).iloc[0]
                        custody_data['XLM'][w_name] = float(val_xlm)
    except Exception:
        pass

    return df, custody_data

def process_transaction_sheet(url, token_name):
    try:
        raw_df = read_raw_csv(url)
        header_idx = None
        for idx, row in raw_df.iterrows():
            row_str = " ".join(row.fillna('').astype(str).values).upper()
            if "FECHA" in row_str:
                header_idx = idx
                break

        if header_idx is not None:
            df = pd.read_csv(url, skiprows=header_idx, on_bad_lines='skip')
        else:
            df = pd.read_csv(url, on_bad_lines='skip')

        df.columns = [str(c).strip().upper() for c in df.columns]

        c_fecha = next((c for c in df.columns if "FECHA" in c), None)
        c_cant = next((c for c in df.columns if "CANTIDAD" in c), None)
        c_inv = next((c for c in df.columns if "INVERTIDO" in c or "TOTAL" in c), None)

        if not c_fecha or not c_inv:
            return pd.DataFrame()

        df['Fecha_Clean'] = pd.to_datetime(df[c_fecha], errors='coerce', dayfirst=True)
        df['Cantidad_Clean'] = clean_numeric_series(df[c_cant]) if c_cant else 0.0
        df['Invertido_Clean'] = clean_numeric_series(df[c_inv])
        df['Token_Clean'] = token_name

        return df[['Fecha_Clean', 'Cantidad_Clean', 'Invertido_Clean', 'Token_Clean']].dropna(subset=['Fecha_Clean'])
    except Exception:
        return pd.DataFrame()

@st.cache_data(ttl=30)
def load_history_data():
    df_xrp = process_transaction_sheet(SHEET_XRP_URL, "XRP")
    df_xlm = process_transaction_sheet(SHEET_XLM_URL, "XLM")

    frames = [f for f in [df_xrp, df_xlm] if not f.empty]
    if frames:
        df_all = pd.concat(frames, ignore_index=True)
        return df_all.sort_values('Fecha_Clean')
    return pd.DataFrame()

df, custody_data = load_resumen_data()
df_hist = load_history_data()

st.title("⚡ Control de Portfolio Cripto")
st.caption("Sincronizado en tiempo real con Google Sheets")

if st.sidebar.button("🔄 Actualizar Datos"):
    st.cache_data.clear()
    st.rerun()

st.markdown("---")

if not df.empty:
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

            tok_custody = custody_data.get(token, {})
            if tok_custody:
                st.markdown("<div style='margin-top: 10px; font-weight: bold; font-size: 13px;'>🔒 Custodia Actual (Wallet / Holding):</div>", unsafe_allow_html=True)

                for w_name, w_cant in tok_custody.items():
                    if w_cant > 0:
                        w_val = w_cant * p_act
                        w_pct = (w_cant / cant * 100) if cant > 0 else 0.0

                        st.markdown(f"""
                        <div style="display: flex; justify-content: space-between; background-color: #1a202c; padding: 6px 10px; border-radius: 6px; margin-top: 4px; font-size: 12px;">
                            <div><b>{w_name}</b></div>
                            <div>{w_cant:,.2f} {token} ({w_val:,.2f} €)</div>
                            <div style="color: #3b82f6;"><b>{w_pct:.1f}%</b></div>
                        </div>
                        """, unsafe_allow_html=True)

    st.markdown("---")

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
        st.subheader("📈 Evolución Histórica Global (Estilo Koinly)")
        if not df_hist.empty:
            min_date = df_hist['Fecha_Clean'].min()
            max_date = pd.Timestamp.today()
            date_range = pd.date_range(start=min_date, end=max_date, freq='D')
            df_timeline = pd.DataFrame({'Fecha_Clean': date_range})

            frames_processed = []
            for token_name in df_hist['Token_Clean'].unique():
                df_t = df_hist[df_hist['Token_Clean'] == token_name].sort_values('Fecha_Clean').copy()
                df_t['Q_Acum'] = df_t['Cantidad_Clean'].cumsum()
                df_t['Inv_Acum'] = df_t['Invertido_Clean'].cumsum()
                
                row_t = df[df['Token'] == token_name]
                p_ref = float(row_t['Precio Actual (€)'].values[0]) if not row_t.empty and 'Precio Actual (€)' in df.columns else 1.0
                
                df_t_daily = pd.merge_asof(df_timeline, df_t, on='Fecha_Clean', direction='backward')
                df_t_daily['Token_Clean'] = token_name
                df_t_daily['Q_Acum'] = df_t_daily['Q_Acum'].fillna(0)
                df_t_daily['Inv_Acum'] = df_t_daily['Inv_Acum'].fillna(0)
                df_t_daily['Valor_Mercado'] = df_t_daily['Q_Acum'] * p_ref
                frames_processed.append(df_t_daily)

            if frames_processed:
                df_full = pd.concat(frames_processed, ignore_index=True)
                df_global = df_full.groupby('Fecha_Clean')[['Valor_Mercado', 'Inv_Acum']].sum().reset_index()

                fig_koinly = go.Figure()

                fig_koinly.add_trace(go.Scatter(
                    x=df_global['Fecha_Clean'],
                    y=df_global['Valor_Mercado'],
                    mode='lines',
                    name='Worth (€)',
                    fill='tozeroy',
                    fillcolor='rgba(59, 130, 246, 0.15)',
                    line=dict(color='#3b82f6', width=2)
                ))

                fig_koinly.add_trace(go.Scatter(
                    x=df_global['Fecha_Clean'],
                    y=df_global['Inv_Acum'],
                    mode='lines',
                    name='Cost Basis (€)',
                    line=dict(color='#94a3b8', width=2, dash='dash')
                ))

                fig_koinly.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color="#ffffff"),
                    margin=dict(l=10, r=10, t=10, b=10),
                    xaxis=dict(showgrid=False, title=None),
                    yaxis=dict(showgrid=True, gridcolor='#262c3a', title=None),
                    hovermode="x unified",
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                )
                st.plotly_chart(fig_koinly, use_container_width=True)
            else:
                st.info("Procesando datos históricos...")
        else:
            st.info("Cargando datos de evolución temporal...")

    st.markdown("---")

    st.subheader("🧮 Calculadora Avanzada de Adquisición")
    calc_c1, calc_c2 = st.columns([1, 2])
    with calc_c1:
        token_sel = st.selectbox("Selecciona el token:", df["Token"].tolist())
        euros_inv = st.number_input("Monto a invertir (€):", min_value=1.0, value=50.0, step=10.0)
        
        row_token = df[df["Token"] == token_sel].iloc[0]
        precio_act = float(row_token["Precio Actual (€)"]) if "Precio Actual (€)" in df.columns else 1.0
        precio_med_actual = float(row_token["Precio Medio (€)"]) if "Precio Medio (€)" in df.columns else precio_act
        cant_actual = float(row_token["Cantidad Total TK"]) if "Cantidad Total TK" in df.columns else 0.0
        inv_actual = float(row_token["Inversión Total (€)"]) if "Inversión Total (€)" in df.columns else 0.0

        # Cálculo estimado de tokens y comisión aprox (ej. ~1.5% o tarifa media de exchange)
        comision_aprox = euros_inv * 0.015 
        euros_netos = euros_inv - comision_aprox
        tokens_adquiridos = euros_netos / precio_act if precio_act > 0 else 0.0
        
        # Nuevo precio medio estimado
        nueva_inv_total = inv_actual + euros_inv
        nuevo_balance_tk = cant_actual + tokens_adquiridos
        nuevo_precio_medio = nueva_inv_total / nuevo_balance_tk if nuevo_balance_tk > 0 else precio_act
        diferencia_pm = nuevo_precio_medio - precio_med_actual

    with calc_c2:
        st.info(f"💡 Precio actual de referencia: **{precio_act:,.4f} €** por {token_sel}")
        res_c1, res_c2, res_c3 = st.columns(3)
        with res_c1:
            st.metric(f"Tokens a adquirir", f"+{tokens_adquiridos:,.2f}")
        with res_c2:
            st.metric("Comisión Aprox.", f"~{comision_aprox:,.2f} €")
        with res_c3:
            st.metric("Nuevo Balance", f"{nuevo_balance_tk:,.2f}")

        # Indicador de cómo afecta al precio medio de compra
        color_delta = "normal" if diferencia_pm <= 0 else "inverse"
        st.metric(
            "Nuevo Precio Medio Estimado", 
            f"{nuevo_precio_medio:,.4f} €", 
            delta=f"{diferencia_pm:+,.4f} € vs actual", 
            delta_color=color_delta
        )
