import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests
from datetime import datetime

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

        df_filtered = df[(df['Invertido_Clean'] > 0) & (df['Cantidad_Clean'] > 0)].copy()

        return df_filtered[['Fecha_Clean', 'Cantidad_Clean', 'Invertido_Clean', 'Token_Clean']].dropna(subset=['Fecha_Clean'])
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

@st.cache_data(ttl=3600)
def get_historical_prices_coingecko(asset_id, days=730):
    try:
        url = f"https://api.coingecko.com/api/v2/coins/{asset_id}/market_chart?vs_currency=eur&days={days}&interval=daily"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            prices = data.get('prices', [])
            df_p = pd.DataFrame(prices, columns=['timestamp', 'price'])
            df_p['Fecha_Clean'] = pd.to_datetime(df_p['timestamp'], unit='ms').dt.normalize()
            return df_p[['Fecha_Clean', 'price']].drop_duplicates(subset=['Fecha_Clean'])
    except Exception:
        pass
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

    df_p_xrp = get_historical_prices_coingecko('ripple')
    df_p_xlm = get_historical_prices_coingecko('stellar')

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

    df_global_daily = pd.DataFrame()

    with g2:
        st.subheader("📈 Evolución Histórica Global (Estilo Koinly)")
        if not df_hist.empty:
            min_date = df_hist['Fecha_Clean'].min()
            max_date = pd.Timestamp.today().normalize()
            date_range = pd.date_range(start=min_date, end=max_date, freq='D')
            df_timeline = pd.DataFrame({'Fecha_Clean': date_range})

            frames_processed = []
            cg_price_map = {'XRP': df_p_xrp, 'XLM': df_p_xlm}

            for token_name in df_hist['Token_Clean'].unique():
                df_t = df_hist[df_hist['Token_Clean'] == token_name].sort_values('Fecha_Clean').copy()
                df_t['Q_Acum'] = df_t['Cantidad_Clean'].cumsum()
                df_t['Inv_Acum'] = df_t['Invertido_Clean'].cumsum()
                
                df_t_daily = pd.merge_asof(df_timeline, df_t, on='Fecha_Clean', direction='backward')
                df_t_daily['Q_Acum'] = df_t_daily['Q_Acum'].fillna(0)
                df_t_daily['Inv_Acum'] = df_t_daily['Inv_Acum'].fillna(0)

                df_api_p = cg_price_map.get(token_name, pd.DataFrame())
                if not df_api_p.empty:
                    df_t_daily = pd.merge_asof(df_t_daily, df_api_p, on='Fecha_Clean', direction='backward')
                    df_t_daily['price'] = df_t_daily['price'].fillna(method='bfill').fillna(0)
                else:
                    row_t = df[df['Token'] == token_name]
                    p_ref = float(row_t['Precio Actual (€)'].values[0]) if not row_t.empty and 'Precio Actual (€)' in df.columns else 1.0
                    df_t_daily['price'] = p_ref

                df_t_daily['Valor_Mercado'] = df_t_daily['Q_Acum'] * df_t_daily['price']
                df_t_daily['Token_Clean'] = token_name
                frames_processed.append(df_t_daily)

            if frames_processed:
                df_full = pd.concat(frames_processed, ignore_index=True)
                df_global_daily = df_full.groupby('Fecha_Clean')[['Valor_Mercado', 'Inv_Acum']].sum().reset_index()

                if not df_global_daily.empty:
                    df_global_daily.iloc[-1, df_global_daily.columns.get_loc('Valor_Mercado')] = val_actual

                fig_koinly = go.Figure()

                fig_koinly.add_trace(go.Scatter(
                    x=df_global_daily['Fecha_Clean'],
                    y=df_global_daily['Valor_Mercado'],
                    mode='lines',
                    name='Worth (€)',
                    fill='tozeroy',
                    fillcolor='rgba(59, 130, 246, 0.15)',
                    line=dict(color='#3b82f6', width=2)
                ))

                fig_koinly.add_trace(go.Scatter(
                    x=df_global_daily['Fecha_Clean'],
                    y=df_global_daily['Inv_Acum'],
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

        comision_aprox = euros_inv * 0.015 
        euros_netos = euros_inv - comision_aprox
        tokens_adquiridos = euros_netos / precio_act if precio_act > 0 else 0.0
        
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

        color_delta = "normal" if diferencia_pm <= 0 else "inverse"
        st.metric(
            "Nuevo Precio Medio Estimado", 
            f"{nuevo_precio_medio:,.4f} €", 
            delta=f"{diferencia_pm:+,.4f} € vs actual", 
            delta_color=color_delta
        )

    # =========================================================================
    # 🌟 SECCIÓN 1: TABLAS DE RENTABILIDADES
    # =========================================================================
    st.markdown("---")
    st.subheader("📅 Registro Temporal y Rentabilidad (Mensual / Semanal)")

    df_rent_m = pd.DataFrame()

    if not df_hist.empty:
        meses_es = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
            7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

        min_d = df_hist['Fecha_Clean'].min()
        max_d = pd.Timestamp.today().normalize()
        range_daily = pd.date_range(start=min_d, end=max_d, freq='D')
        df_base = pd.DataFrame({'Fecha_Clean': range_daily})

        col_p1, col_p2 = st.columns([2, 1])
        with col_p1:
            tab_mensual, tab_semanal = st.tabs(["🗓️ Rentabilidad Mensual", "📅 Rentabilidad Semanal"])

            # --- 1. RENTABILIDAD MENSUAL ---
            with tab_mensual:
                month_ends = pd.date_range(start=min_d, end=max_d, freq='ME')
                if max_d not in month_ends:
                    month_ends = month_ends.append(pd.DatetimeIndex([max_d]))

                monthly_records = []
                prev_val_m = 0.0

                month_ends = sorted(list(set(month_ends)))

                for m_date in month_ends:
                    inv_m = 0.0
                    val_m = 0.0
                    for tok_name, df_api_p in [('XRP', df_p_xrp), ('XLM', df_p_xlm)]:
                        df_t = df_hist[df_hist['Token_Clean'] == tok_name].sort_values('Fecha_Clean').copy()
                        if not df_t.empty:
                            df_t['Q_Acum'] = df_t['Cantidad_Clean'].cumsum()
                            df_t['Inv_Acum'] = df_t['Invertido_Clean'].cumsum()
                            df_merged = pd.merge_asof(df_base[df_base['Fecha_Clean'] <= m_date], df_t, on='Fecha_Clean', direction='backward')
                            
                            q_at = df_merged['Q_Acum'].iloc[-1] if not df_merged.empty and not pd.isna(df_merged['Q_Acum'].iloc[-1]) else 0.0
                            inv_at = df_merged['Inv_Acum'].iloc[-1] if not df_merged.empty and not pd.isna(df_merged['Inv_Acum'].iloc[-1]) else 0.0

                            p_at = 1.0
                            if not df_api_p.empty:
                                p_row = df_api_p[df_api_p['Fecha_Clean'] <= m_date]
                                if not p_row.empty:
                                    p_at = float(p_row['price'].iloc[-1])
                            else:
                                r_ref = df[df['Token'] == tok_name]
                                p_at = float(r_ref['Precio Actual (€)'].values[0]) if not r_ref.empty else 1.0

                            inv_m += inv_at
                            val_m += (q_at * p_at)

                    pnl_m = val_m - inv_m
                    rent_acum = (pnl_m / inv_m * 100) if inv_m > 0 else 0.0
                    rent_mensual = ((val_m - prev_val_m) / prev_val_m * 100) if prev_val_m > 0 else rent_acum
                    prev_val_m = val_m

                    monthly_records.append({
                        '_date': m_date,
                        'Año': str(m_date.year),
                        'Mes_Num': m_date.month,
                        'Período': f"{m_date.year} — {meses_es[m_date.month]}",
                        'Rentabilidad Mensual (%)': f"{rent_mensual:+.2f} %",
                        'Rentabilidad Acumulada (%)': f"{rent_acum:+.2f} %",
                        'Beneficio / Pérdida (€)': f"{pnl_m:+,.2f} €",
                        '_raw_rent_m': rent_mensual
                    })

                df_rent_m = pd.DataFrame(monthly_records)
                df_rent_m_disp = df_rent_m.sort_values('_date', ascending=False)
                st.dataframe(df_rent_m_disp[['Período', 'Rentabilidad Mensual (%)', 'Rentabilidad Acumulada (%)', 'Beneficio / Pérdida (€)']], use_container_width=True, hide_index=True)

            # --- 2. RENTABILIDAD SEMANAL ---
            with tab_semanal:
                week_ends = pd.date_range(start=min_d, end=max_d, freq='W-SUN')
                if max_d not in week_ends:
                    week_ends = week_ends.append(pd.DatetimeIndex([max_d]))

                week_ends = sorted(list(set(week_ends)))

                weekly_records = []
                prev_val_w = 0.0

                for w_date in week_ends:
                    inv_w = 0.0
                    val_w = 0.0
                    for tok_name, df_api_p in [('XRP', df_p_xrp), ('XLM', df_p_xlm)]:
                        df_t = df_hist[df_hist['Token_Clean'] == tok_name].sort_values('Fecha_Clean').copy()
                        if not df_t.empty:
                            df_t['Q_Acum'] = df_t['Cantidad_Clean'].cumsum()
                            df_t['Inv_Acum'] = df_t['Invertido_Clean'].cumsum()
                            df_merged = pd.merge_asof(df_base[df_base['Fecha_Clean'] <= w_date], df_t, on='Fecha_Clean', direction='backward')
                            
                            q_at = df_merged['Q_Acum'].iloc[-1] if not df_merged.empty and not pd.isna(df_merged['Q_Acum'].iloc[-1]) else 0.0
                            inv_at = df_merged['Inv_Acum'].iloc[-1] if not df_merged.empty and not pd.isna(df_merged['Inv_Acum'].iloc[-1]) else 0.0

                            p_at = 1.0
                            if not df_api_p.empty:
                                p_row = df_api_p[df_api_p['Fecha_Clean'] <= w_date]
                                if not p_row.empty:
                                    p_at = float(p_row['price'].iloc[-1])
                            else:
                                r_ref = df[df['Token'] == tok_name]
                                p_at = float(r_ref['Precio Actual (€)'].values[0]) if not r_ref.empty else 1.0

                            inv_w += inv_at
                            val_w += (q_at * p_at)

                    pnl_w = val_w - inv_w
                    rent_acum_w = (pnl_w / inv_w * 100) if inv_w > 0 else 0.0
                    rent_semanal = ((val_w - prev_val_w) / prev_val_w * 100) if prev_val_w > 0 else rent_acum_w
                    prev_val_w = val_w

                    w_start = w_date - pd.Timedelta(days=6)
                    iso_year, iso_week, _ = w_date.isocalendar()
                    
                    str_semana = f"{iso_year} — Sem. {iso_week:02d} ({w_start.strftime('%d/%m')} al {w_date.strftime('%d/%m')})"

                    weekly_records.append({
                        '_date': w_date,
                        'Semana': str_semana,
                        'Rentabilidad Semanal (%)': f"{rent_semanal:+.2f} %",
                        'Rentabilidad Acumulada (%)': f"{rent_acum_w:+.2f} %",
                        'Beneficio / Pérdida (€)': f"{pnl_w:+,.2f} €"
                    })

                df_rent_w = pd.DataFrame(weekly_records)
                df_rent_w = df_rent_w.sort_values('_date', ascending=False)
                
                st.dataframe(df_rent_w[['Semana', 'Rentabilidad Semanal (%)', 'Rentabilidad Acumulada (%)', 'Beneficio / Pérdida (€)']], use_container_width=True, hide_index=True)

            # Botón de descarga CSV
            csv_data = df_rent_m[['Período', 'Rentabilidad Mensual (%)', 'Rentabilidad Acumulada (%)', 'Beneficio / Pérdida (€)']].to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descargar Informe de Rentabilidades (CSV)",
                data=csv_data,
                file_name=f"informe_rentabilidades_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )

        with col_p2:
            st.markdown("##### 📊 Módulo General de Rendimiento")
            st.markdown(f"""
            - **Inicio de Registro:** {df_hist['Fecha_Clean'].min().strftime('%d/%m/%Y')}
            - **Operaciones Registradas:** {len(df_hist)} movimientos
            - **Inversión Histórica Acumulada:** {inv_total:,.2f} €
            - **Valoración Actual de Cartera:** {val_actual:,.2f} €
            """)

    # =========================================================================
    # 🌟 SECCIÓN 2: MAPA DE CALOR
    # =========================================================================
    if not df_rent_m.empty:
        st.markdown("---")
        st.subheader("🔥 Mapa de Calor de Rentabilidades Mensuales (Estilo CoinGlass)")
        
        years = sorted([str(y) for y in df_rent_m['Año'].unique()])
        months_abbr = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        
        z_matrix = []
        text_matrix = []

        for yr in years:
            row_z = []
            row_text = []
            for m_idx in range(1, 13):
                match = df_rent_m[(df_rent_m['Año'] == yr) & (df_rent_m['Mes_Num'] == m_idx)]
                if not match.empty:
                    val_pct = match['_raw_rent_m'].values[0]
                    row_z.append(val_pct)
                    row_text.append(f"{val_pct:+.1f}%")
                else:
                    row_z.append(np.nan)
                    row_text.append("—")
            z_matrix.append(row_z)
            text_matrix.append(row_text)

        colorscale_custom = [
            [0.0, "#dc2626"],   # Caídas fuertes (Rojo)
            [0.15, "#ef4444"],  # Caídas leves (Rojo claro)
            [0.20, "#1f2937"],  # 0% Neutro
            [0.35, "#065f46"],  # Subida pequeña (Verde oscuro)
            [0.60, "#10b981"],  # Subida media (Verde estándar)
            [1.0, "#00ff88"]    # Subida grande >50% (Verde brillante)
        ]

        fig_heatmap = go.Figure(data=go.Heatmap(
            z=z_matrix,
            x=months_abbr,
            y=years,
            text=text_matrix,
            texttemplate="%{text}",
            textfont={"size": 13, "color": "#ffffff"},
            colorscale=colorscale_custom,
            zmin=-50,
            zmax=150,
            showscale=False,
            xgap=4,
            ygap=4
        ))

        fig_heatmap.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#ffffff"),
            margin=dict(l=10, r=10, t=20, b=20),
            yaxis=dict(type='category', autorange="reversed")
        )

        st.plotly_chart(fig_heatmap, use_container_width=True)

    # =========================================================================
    # 🌟 SECCIÓN 3: MÉTRICAS AVANZADAS DE RIESGO Y MAX DRAWDOWN HISTÓRICO
    # =========================================================================
    if not df_global_daily.empty:
        st.markdown("---")
        st.subheader("🛡️ Métricas Avanzadas de Riesgo y Máximo Histórico (ATH)")
        
        df_risk = df_global_daily.copy()
        
        # 1. EVALUACIÓN DE DRAWDOWN DE PRECIO Y VALORACIÓN
        df_risk['Peak_Acum'] = df_risk['Valor_Mercado'].cummax()
        df_risk['DD_Portfolio'] = np.where(
            df_risk['Peak_Acum'] > 0,
            ((df_risk['Valor_Mercado'] - df_risk['Peak_Acum']) / df_risk['Peak_Acum']) * 100,
            0.0
        )
        
        # Evalúa también la rentabilidad no realizada acumulada histórica (P&L %)
        df_risk['PnL_Pct_Hist'] = np.where(
            df_risk['Inv_Acum'] > 0,
            ((df_risk['Valor_Mercado'] - df_risk['Inv_Acum']) / df_risk['Inv_Acum']) * 100,
            0.0
        )
        
        # Max Drawdown real: el mínimo absoluto entre el pico de cartera y la rentabilidad histórica más baja
        min_dd_portfolio = float(df_risk['DD_Portfolio'].min())
        min_pnl_hist = float(df_risk['PnL_Pct_Hist'].min())
        max_dd_pct = min(min_dd_portfolio, min_pnl_hist)

        # 2. CÁLCULO DEL ATH GLOBAL Y DIFERENCIA ACTUAL
        ath_valor = float(df_risk['Peak_Acum'].max())
        row_ath = df_risk[df_risk['Valor_Mercado'] == ath_valor].iloc[0] if not df_risk[df_risk['Valor_Mercado'] == ath_valor].empty else df_risk.iloc[-1]
        fecha_ath = row_ath['Fecha_Clean'].strftime('%d/%m/%Y')
        
        diferencia_ath_eur = val_actual - ath_valor
        subida_necesaria_portfolio = ((ath_valor - val_actual) / val_actual * 100) if val_actual > 0 and ath_valor > val_actual else 0.0

        rk1, rk2, rk3, rk4 = st.columns(4)
        with rk1:
            # Forzado de color rojo con delta_color="inverse"
            st.metric(
                "Max Drawdown Histórico", 
                f"{max_dd_pct:.2f} %", 
                delta=f"{max_dd_pct:.2f} %", 
                delta_color="inverse"
            )
        with rk2:
            st.metric("Pico Máximo (ATH Portfolio)", f"{ath_valor:,.2f} €")
        with rk3:
            st.metric("Fecha Pico ATH", fecha_ath)
        with rk4:
            if subida_necesaria_portfolio > 0:
                st.metric(
                    "Subida p/ Recuperar ATH", 
                    f"+{subida_necesaria_portfolio:.2f} %", 
                    delta=f"{diferencia_ath_eur:,.2f} € vs ATH", 
                    delta_color="inverse"
                )
            else:
                st.metric("Subida p/ Recuperar ATH", "0.00 % (¡En Máximos!)")

    # =========================================================================
    # 🌟 SECCIÓN 4: EVOLUCIÓN DCA
    # =========================================================================
    if not df_hist.empty:
        st.markdown("---")
        st.subheader("📉 Optimización del Precio Medio de Compra (Estrategia DCA)")
        
        dca_col1, dca_col2 = st.columns([1, 3])
        with dca_col1:
            token_dca = st.selectbox("Selecciona activo para analizar DCA:", df["Token"].tolist(), key="dca_token")
            
            df_tok_h = df_hist[(df_hist['Token_Clean'] == token_dca) & (df_hist['Invertido_Clean'] > 0)].sort_values('Fecha_Clean').copy()
            
            r_tok_ref = df[df['Token'] == token_dca]
            if not r_tok_ref.empty and "Precio Medio (€)" in r_tok_ref.columns:
                pm_actual = float(r_tok_ref["Precio Medio (€)"].values[0])
            else:
                pm_actual = 0.0

            p_mkt_actual = float(r_tok_ref['Precio Actual (€)'].values[0]) if not r_tok_ref.empty and 'Precio Actual (€)' in r_tok_ref.columns else pm_actual

            if not df_tok_h.empty:
                df_tok_h['Q_Acum'] = df_tok_h['Cantidad_Clean'].cumsum()
                df_tok_h['Inv_Acum'] = df_tok_h['Invertido_Clean'].cumsum()
                df_tok_h['Precio_Medio_Hist'] = df_tok_h['Inv_Acum'] / df_tok_h['Q_Acum']
                
                df_tok_h.iloc[-1, df_tok_h.columns.get_loc('Precio_Medio_Hist')] = pm_actual
                pm_inicial = float(df_tok_h['Precio_Medio_Hist'].iloc[0])
            else:
                pm_inicial = pm_actual

            mejora_pm_pct = ((pm_actual - pm_inicial) / pm_inicial) * 100 if pm_inicial > 0 else 0.0
            margen_seguridad = ((p_mkt_actual - pm_actual) / pm_actual) * 100 if pm_actual > 0 else 0.0

            st.metric("Precio Medio Inicial", f"{pm_inicial:,.4f} €")
            st.metric("Precio Medio Actual Optimizado", f"{pm_actual:,.4f} €", delta=f"{mejora_pm_pct:+.2f} %", delta_color="normal" if mejora_pm_pct <= 0 else "inverse")
            st.metric("Margen sobre Mercado", f"{margen_seguridad:+.2f} %", delta=f"{margen_seguridad:+.2f} %")

        with dca_col2:
            if not df_tok_h.empty:
                cg_id_map = {'XRP': 'ripple', 'XLM': 'stellar'}
                df_cg_p = get_historical_prices_coingecko(cg_id_map.get(token_dca, 'ripple'))
                
                fig_dca = go.Figure()

                fig_dca.add_trace(go.Scatter(
                    x=df_tok_h['Fecha_Clean'],
                    y=df_tok_h['Precio_Medio_Hist'],
                    mode='lines+markers',
                    name='Precio Medio (€)',
                    line=dict(color='#3b82f6', width=3)
                ))

                if not df_cg_p.empty:
                    df_cg_crop = df_cg_p[df_cg_p['Fecha_Clean'] >= df_tok_h['Fecha_Clean'].min()]
                    fig_dca.add_trace(go.Scatter(
                        x=df_cg_crop['Fecha_Clean'],
                        y=df_cg_crop['price'],
                        mode='lines',
                        name='Precio de Mercado (€)',
                        line=dict(color='#10b981', width=1.5, dash='dot')
                    ))

                fig_dca.update_layout(
                    title=f"Evolución del Precio Medio de Compra — {token_dca}",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color="#ffffff"),
                    margin=dict(l=10, r=10, t=30, b=10),
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#262c3a', title="Precio (€)"),
                    hovermode="x unified"
                )
                st.plotly_chart(fig_dca, use_container_width=True)

    # =========================================================================
    # 🌟 SECCIÓN 5: CALCULADORA INVERSA / SIMULADOR DE OBJETIVOS
    # =========================================================================
    st.markdown("---")
    st.subheader("🎯 Calculadora Inversa / Simulador de Objetivos de Precio")
    
    inv_c1, inv_c2 = st.columns([1, 2])
    with inv_c1:
        token_objetivo = st.selectbox("Token para simular objetivo:", df["Token"].tolist(), key="obj_token")
        
        row_obj = df[df["Token"] == token_objetivo].iloc[0]
        p_actual_obj = float(row_obj["Precio Actual (€)"]) if "Precio Actual (€)" in row_obj else 1.0
        bal_obj = float(row_obj["Cantidad Total TK"]) if "Cantidad Total TK" in row_obj else 0.0
        inv_obj = float(row_obj["Inversión Total (€)"]) if "Inversión Total (€)" in row_obj else 0.0
        
        modo_calculo = st.radio("Modo de simulación:", ["Porcentaje de Rentabilidad (%)", "Precio Objetivo (€)"])
        
        if modo_calculo == "Porcentaje de Rentabilidad (%)":
            rentabilidad_deseada = st.number_input("Rentabilidad deseada (%):", value=100.0, step=10.0)
            precio_calculado = p_actual_obj * (1 + rentabilidad_deseada / 100.0)
        else:
            precio_calculado = st.number_input("Precio objetivo (€):", min_value=0.0001, value=p_actual_obj * 2, step=0.01)
            rentabilidad_deseada = ((precio_calculado - p_actual_obj) / p_actual_obj) * 100 if p_actual_obj > 0 else 0.0

    with inv_c2:
        valor_futuro_token = bal_obj * precio_calculado
        ganancia_neta_futura = valor_futuro_token - inv_obj
        
        st.info(f"💡 Simulando proyección para **{token_objetivo}** (Balance actual: {bal_obj:,.2f} tokens)")
        
        rc1, rc2, rc3 = st.columns(3)
        with rc1:
            st.metric("Precio Objetivo Token", f"{precio_calculado:,.4f} €")
        with rc2:
            st.metric("Rentabilidad Implícita", f"{rentabilidad_deseada:+,.2f} %")
        with rc3:
            st.metric("Valor Total Cartera en este Token", f"{valor_futuro_token:,.2f} €")
            
        st.success(f"📈 Si {token_objetivo} alcanza este precio, tu beneficio neto estimado en esta posición sería de **+{ganancia_neta_futura:,.2f} €**.")
