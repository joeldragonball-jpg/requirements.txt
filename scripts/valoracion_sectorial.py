"""Cuadro de valoración sectorial (sin IA): PER, EV/EBITDA y FCF yield de ~18 valores a partir de SEC companyfacts [P] y precio de Yahoo [S].

Escribe explorador/valoracion.json. Información para decidir tú; no es una recomendación.
User-Agent: por defecto uno genérico; si la SEC lo rechaza, define SEC_USER_AGENT con un contacto tuyo (decisión tuya: iría a la SEC).
Uso: python scripts/valoracion_sectorial.py            (todos)    ·    python scripts/valoracion_sectorial.py LMT NVDA   (solo esos)
"""
import json
import os
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "valoracion.json"
UA_SEC = os.environ.get("SEC_USER_AGENT", "cartera-joel/1.0 (uso personal; valoracion sectorial)")
UA_YAHOO = "Mozilla/5.0 (cartera-joel valoracion)"

# sector, ticker, CIK (se comprueba contra entityName de la SEC)
VALORES = [
    ("Defensa", "LMT", 936468), ("Defensa", "RTX", 101829), ("Defensa", "NOC", 1133421), ("Defensa", "GD", 40533), ("Defensa", "LHX", 202058),
    ("Energía", "XOM", 34088), ("Energía", "CVX", 93410), ("Energía", "COP", 1163165), ("Energía", "EOG", 821189),
    ("Ciberseguridad", "PANW", 1327567), ("Ciberseguridad", "CRWD", 1535527), ("Ciberseguridad", "FTNT", 1262039), ("Ciberseguridad", "ZS", 1713683),
    ("Semiconductores", "NVDA", 1045810), ("Semiconductores", "AVGO", 1730168), ("Semiconductores", "AMD", 2488),
    ("Semiconductores", "TXN", 97476), ("Semiconductores", "QCOM", 804328),
]
FLUJOS = {   # conceptos us-gaap alternativos, por orden de preferencia
    "ni": ["NetIncomeLoss", "ProfitLoss"],
    "ebit": ["OperatingIncomeLoss"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization", "DepreciationAmortizationAndAccretionNet",
           "DepreciationAndAmortizationExcludingAmortizationOfDeferredPolicyAcquisitionCosts", "Depreciation"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets", "PaymentsToAcquireOilAndGasPropertyAndEquipment",
              "PaymentsToAcquireOtherPropertyPlantAndEquipment"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
    "interes": ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt", "InterestAndDebtExpense"],
}
SALDOS = {
    "caja": ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"],
    "deuda": ["LongTermDebt", "LongTermDebtNoncurrent"],
}


def get(url, ua, intentos=3):
    for i in range(intentos):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": ua}), timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            if i == intentos - 1:
                raise
            time.sleep(3)


def f(s):
    return date.fromisoformat(s)


def flujo_ttm(hechos, conceptos):
    """TTM = año fiscal + acumulado actual − acumulado del año anterior. Devuelve (valor, fin_del_periodo, tipo) o None.
    Entre los conceptos alternativos se queda con el de periodo más reciente (las empresas cambian de etiqueta entre años)."""
    mejor = None
    for c in conceptos:
        x = _un_concepto(hechos, c)
        if x and (mejor is None or x[1] > mejor[1]):
            mejor = x
    return mejor


def _un_concepto(hechos, c):
    usd = hechos.get("us-gaap", {}).get(c, {}).get("units", {}).get("USD")
    if not usd:
        return None
    ent = [e for e in usd if e.get("form") in ("10-K", "10-Q") and e.get("start")]
    anuales = [e for e in ent if 350 <= (f(e["end"]) - f(e["start"])).days <= 380 and e["form"] == "10-K"]
    if not anuales:
        return None
    a = max(anuales, key=lambda e: e["end"])
    ytd = [e for e in ent if e["end"] > a["end"] and abs((f(e["start"]) - f(a["end"])).days) <= 7 and (f(e["end"]) - f(e["start"])).days < 350]
    if not ytd:
        return a["val"], a["end"], "año fiscal"
    y = max(ytd, key=lambda e: e["end"])
    dur = (f(y["end"]) - f(y["start"])).days
    prev = [e for e in ent if abs((f(y["end"]) - f(e["end"])).days - 365) <= 8 and abs((f(e["end"]) - f(e["start"])).days - dur) <= 8]
    if not prev:
        return a["val"], a["end"], "año fiscal (sin TTM)"
    p = max(prev, key=lambda e: e["filed"])
    return a["val"] + y["val"] - p["val"], y["end"], "TTM"


def saldo(hechos, conceptos):
    for c in conceptos:
        usd = hechos.get("us-gaap", {}).get(c, {}).get("units", {}).get("USD")
        if usd:
            e = max((e for e in usd if e.get("form") in ("10-K", "10-Q")), key=lambda e: (e["end"], e["filed"]), default=None)
            if e:
                return e["val"], e["end"]
    return None


def acciones(hechos):
    sh = hechos.get("dei", {}).get("EntityCommonStockSharesOutstanding", {}).get("units", {}).get("shares", [])
    if not sh:
        return None
    ultimo = max(e["end"] for e in sh)
    vals = {e["val"] for e in sh if e["end"] == ultimo}      # clases distintas = valores distintos con la misma fecha
    return sum(vals), ultimo


def precio(t):
    d = get(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=5d&interval=1d", UA_YAHOO)["chart"]["result"][0]["meta"]
    return d["regularMarketPrice"], datetime.fromtimestamp(d["regularMarketTime"], timezone.utc).date().isoformat()


def r(x, n=1):
    return None if x is None else round(x, n)


def fila(sector, t, cik):
    cf = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", UA_SEC)
    h = cf["facts"]
    out = {"sector": sector, "ticker": t, "empresa": cf.get("entityName", "?"), "notas": []}
    px, fpx = precio(t)
    out["precio"], out["fecha_precio"] = px, fpx
    ac = acciones(h)
    fl = {k: flujo_ttm(h, v) for k, v in FLUJOS.items()}
    sd = {k: saldo(h, v) for k, v in SALDOS.items()}
    if not ac:
        out["notas"].append("acciones no localizadas")
        return out
    cap = px * ac[0]
    out["cap_mm"] = r(cap / 1e9, 1)
    deuda = sd["deuda"][0] if sd["deuda"] else 0
    caja = sd["caja"][0] if sd["caja"] else None
    if not sd["deuda"]:
        out["notas"].append("deuda no localizada (se cuenta 0) [VERIFICAR]")
    if caja is None:
        out["notas"].append("caja no localizada")
    ev = cap + deuda - (caja or 0)
    out["ev_mm"] = r(ev / 1e9, 1)
    ni, ebit, da, ocf, capex = (fl[k][0] if fl[k] else None for k in ("ni", "ebit", "da", "ocf", "capex"))
    out["per"] = r(cap / ni, 1) if ni and ni > 0 else None
    if ebit is None and fl["pretax"] and fl["interes"]:
        ebit = fl["pretax"][0] + fl["interes"][0]
        out["notas"].append("EBITDA aprox. (antes de impuestos + intereses + D&A)")
    ebitda = ebit + da if ebit is not None and da is not None else None
    out["ev_ebitda"] = r(ev / ebitda, 1) if ebitda and ebitda > 0 else None
    out["fcf_yield_pct"] = r((ocf - capex) / cap * 100, 1) if ocf is not None and capex is not None else None
    for k, etq in (("ni", "beneficio"), ("da", "D&A"), ("ocf", "flujo operativo"), ("capex", "capex")):
        if fl[k] is None:
            out["notas"].append(f"{etq} no localizado")
    base = fl["ni"] or fl["ocf"]
    out["periodo"] = f"{base[2]} a {base[1]}" if base else "?"
    out["base"] = {"acciones": ac[0], "acciones_fecha": ac[1], "ni": ni, "ebitda": ebitda, "ocf": ocf, "capex": capex, "deuda": deuda, "caja": caja}
    if ni is not None and ni <= 0:
        out["notas"].append("pérdidas: PER no significativo")
    elif out["per"] and out["per"] > 100:
        out["notas"].append("PER > 100: no significativo")
    return out


def main():
    pedidos = {a.upper() for a in sys.argv[1:]}
    filas = []
    for sector, t, cik in VALORES:
        if pedidos and t not in pedidos:
            continue
        try:
            filas.append(fila(sector, t, cik))
        except Exception as e:
            filas.append({"sector": sector, "ticker": t, "notas": [f"error {type(e).__name__}: {e}"]})
        time.sleep(0.3)      # la SEC admite hasta 10 peticiones por segundo
    if pedidos:
        for x in filas:
            print(json.dumps(x, ensure_ascii=False))
        return
    SALIDA.write_text(json.dumps({
        "generado": datetime.now(timezone.utc).isoformat(timespec="minutes"),
        "aviso": "Información para decidir tú; no es una recomendación. Precio: Yahoo [S]. Fundamentales: SEC companyfacts [P]. "
                 "Periodos mezclados (mira la columna periodo); EBITDA = resultado operativo + D&A (n/d si falta alguno).",
        "filas": filas}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"valoracion.json: {len(filas)} valores, {sum(1 for x in filas if x.get('per') is not None)} con PER")


if __name__ == "__main__":
    main()
