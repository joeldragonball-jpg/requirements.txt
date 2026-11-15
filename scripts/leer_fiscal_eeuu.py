"""C281: EE. UU. fiscal y posicionamiento, sin IA ni claves. Lee [P] Treasury Fiscal Data (deuda total diaria, tipo medio de la deuda,
déficit mensual MTS) y CFTC Commitments of Traders (BTC y ETH de CME, oro, T-Note 10 años, EUR, JPY) y escribe
explorador/eeuu-fiscal.json con series cortas (12 puntos). El COT mide posiciones de grupos de operadores en futuros; NO predice precio.
Uso: python scripts/leer_fiscal_eeuu.py [--seco]"""
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "explorador" / "eeuu-fiscal.json"
FD = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"
CFTC = "https://publicreporting.cftc.gov/resource/{d}.json?"
MESES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
COT = [  # id, nombre, dataset, código CFTC, informe
    ("btc", "Bitcoin (CME)", "gpe5-46if", "133741", "TFF"),
    ("eth", "Ether (CME)", "gpe5-46if", "146021", "TFF"),
    ("oro", "Oro (COMEX)", "6dca-aqww", "088691", "Legacy"),
    ("ust10", "T-Note EE. UU. 10 años (CBOT)", "gpe5-46if", "043602", "TFF"),
    ("eur", "Euro FX (CME)", "gpe5-46if", "099741", "TFF"),
    ("jpy", "Yen japonés (CME)", "gpe5-46if", "097741", "TFF"),
]


def bajar(url):
    for n in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.4.0"}), timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            if n == 2:
                raise
            time.sleep(3)


def fd(ruta, **q):
    return bajar(FD + ruta + "?" + urllib.parse.urlencode(q, safe=":,[]"))["data"]


def deuda():
    f = fd("v2/accounting/od/debt_to_penny", sort="-record_date", **{"page[size]": 12})[::-1]
    return {"fuente": FD + "v2/accounting/od/debt_to_penny", "unidad": "billones de USD (deuda total pendiente, diaria)",
            "serie": [[x["record_date"], round(float(x["tot_pub_debt_out_amt"]) / 1e12, 3)] for x in f],
            "en_manos_publico_ult_bn": round(float(f[-1]["debt_held_public_amt"]) / 1e12, 3)}


def tipos():
    f = fd("v2/accounting/od/avg_interest_rates", sort="-record_date", filter="security_desc:eq:Total Marketable", **{"page[size]": 12})[::-1]
    if not f:
        raise ValueError("sin tipos")
    return {"fuente": FD + "v2/accounting/od/avg_interest_rates", "unidad": "% (tipo medio de la deuda negociable, mensual)",
            "serie": [[x["record_date"], float(x["avg_interest_rate_amt"])] for x in f]}


def mts():
    d = fd("v1/accounting/mts/mts_table_1", sort="-record_date,src_line_nbr", **{"page[size]": 400, "filter": "record_date:gte:" + f"{date.today().year - 2}-01-01"})
    por = {}
    for x in d:
        fch = x["record_date"]
        if x["classification_desc"] == MESES[int(fch[5:7]) - 1] and x["current_month_dfct_sur_amt"] != "null":
            if fch not in por or int(x["src_line_nbr"]) > por[fch][0]:
                por[fch] = (int(x["src_line_nbr"]), x)
    fs = sorted(por)[-12:]
    return {"fuente": FD + "v1/accounting/mts/mts_table_1", "unidad": "miles de millones de USD (ingresos y gastos brutos del mes; déficit = gastos - ingresos)",
            "serie": [[f, round(float(por[f][1]["current_month_gross_rcpt_amt"]) / 1e9, 1), round(float(por[f][1]["current_month_gross_outly_amt"]) / 1e9, 1)] for f in fs],
            "columnas": ["fecha del informe (mes)", "ingresos brutos mes", "gastos brutos mes"]}


def cot(ds, cod, inf):
    q = {"$limit": 12, "$order": "report_date_as_yyyy_mm_dd DESC", "$where": f"cftc_contract_market_code='{cod}'"}
    f = bajar(CFTC.format(d=ds) + urllib.parse.urlencode(q))[::-1]
    if len(f) < 2:
        raise ValueError("sin datos COT")
    i = lambda x, k: int(float(x[k]))
    if inf == "TFF":
        ser = [[x["report_date_as_yyyy_mm_dd"][:10], i(x, "lev_money_positions_long") - i(x, "lev_money_positions_short"),
                i(x, "asset_mgr_positions_long") - i(x, "asset_mgr_positions_short"), i(x, "open_interest_all")] for x in f]
        cols = ["fecha (martes)", "neto fondos apalancados (largos-cortos)", "neto gestores de activos", "interés abierto"]
    else:
        ser = [[x["report_date_as_yyyy_mm_dd"][:10], i(x, "noncomm_positions_long_all") - i(x, "noncomm_positions_short_all"),
                i(x, "comm_positions_long_all") - i(x, "comm_positions_short_all"), i(x, "open_interest_all")] for x in f]
        cols = ["fecha (martes)", "neto no comerciales (largos-cortos)", "neto comerciales", "interés abierto"]
    return {"contrato": f[-1]["market_and_exchange_names"], "informe": inf, "unidad": "contratos", "columnas": cols, "serie": ser,
            "fuente": f"https://publicreporting.cftc.gov/resource/{ds}.json"}


def main():
    sal = {"nivel": "P", "generado": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "fallos": [],
           "aviso": "El COT muestra posiciones por tipo de operador a fecha de martes, publicadas el viernes. La posición neta NO es una previsión de precio. Datos fiscales: cifras oficiales sin ajuste."}
    previo = {}
    if RUTA.exists():
        try:
            previo = json.loads(RUTA.read_text(encoding="utf-8"))
        except Exception:
            previo = {}

    def conservar(k, nuevo, anterior):
        """Si la lectura falla, conserva el bloque bueno anterior y lo marca."""
        if isinstance(anterior, dict):
            anterior = dict(anterior)
            anterior["conservado_sin_actualizar"] = previo.get("generado")
            sal[k] = anterior
        return nuevo

    for k, fn in (("deuda", deuda), ("tipo_medio_deuda", tipos), ("mts_mensual", mts)):
        try:
            sal[k] = fn()
        except Exception as e:
            sal["fallos"].append(f"{k}: {type(e).__name__}")
            conservar(k, None, previo.get(k))
    sal["cot"] = {}
    for k, n, ds, cod, inf in COT:
        try:
            sal["cot"][k] = {"nombre": n, **cot(ds, cod, inf)}
        except Exception as e:
            sal["fallos"].append(f"cot {k}: {type(e).__name__}")
            conservar(None, None, None)
            if isinstance((previo.get("cot") or {}).get(k), dict):
                sal["cot"][k] = dict(previo["cot"][k], conservado_sin_actualizar=previo.get("generado"))
    if not any(sal.get(k) for k in ("deuda", "tipo_medio_deuda", "mts_mensual")) and not sal["cot"]:
        print("ERROR: todas las lecturas fallaron; no se sobrescribe", RUTA.name, sal["fallos"])
        return
    txt = json.dumps(sal, ensure_ascii=False, indent=1)
    if "--seco" in sys.argv:
        print(txt[:1500])
    else:
        RUTA.write_text(txt, encoding="utf-8")
        print("OK", RUTA.name, "fallos:", sal["fallos"])


if __name__ == "__main__":
    main()
