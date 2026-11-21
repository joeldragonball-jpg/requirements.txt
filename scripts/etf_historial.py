#!/usr/bin/env python3
"""Serie histórica de ETF cripto (C361b). Sin IA, solo stdlib.

Añade UNA línea por (fecha, ticker) a explorador/etf-historial.jsonl a partir de
explorador/etf-flujos.json. Idempotente: no duplica fecha+ticker.
Uso: PYTHONUTF8=1 python scripts/etf_historial.py [--todos] [--activos XRP,XLM,SOL]
  por defecto: solo el ULTIMO punto de cada fondo; --todos vuelca todo el historial (siembra).
"""
import argparse, json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FLUJOS = RAIZ / "explorador" / "etf-flujos.json"
SALIDA = RAIZ / "explorador" / "etf-historial.jsonl"
CAMPOS = ("fecha", "ticker", "acciones", "nav", "tenencia_monedas", "aum_usd", "fuente", "nivel")


# Puntos trimestrales leídos en SEC EDGAR (data.sec.gov XBRL companyfacts, consultado 21-nov-2026).
# (ticker, fecha, acciones, nav, tenencia_monedas, aum_usd, accn del 10-Q/10-K)
SEC = [
 ("XRP","2025-12-31",11800000,20.46,None,241369000,"0001193125-26-451776"),
 ("XRP","2026-03-31",17420000,15.03,None,261855000,"0001193125-26-346245"),
 ("XRP","2026-06-30",25660000,11.66,None,299146000,"0001193125-26-346245"),
 ("XRPZ","2025-11-23",100000,24.40,None,2440079,"0001140361-26-026732"),
 ("XRPZ","2025-12-31",10900000,19.85,None,216376202,"0001140361-26-005816"),
 ("XRPZ","2026-03-31",14700000,14.63,159659740.0158,215061670,"0001140361-26-043720"),
 ("XRPZ","2026-06-30",20750000,11.39,225368820.7314,236440941,"0001140361-26-043720"),
 ("XRPZ","2026-09-30",27000000,16.28,293112265.4002,439606153,"0001140361-26-043720"),
 ("XRPC","2025-12-31",16490000,19.58,175625441,322819725,"0001999371-26-025352"),
 ("XRPC","2026-03-31",18540000,14.28,197214584,264767022,"0001999371-26-017438"),
 ("XRPC","2026-06-30",21770000,11.08,231279303,241173971,"0001999371-26-025352"),
 ("XRPC","2026-09-30",23350000,15.79,247755213,368656616,"0001999371-26-025352"),
 ("TOXR","2025-12-31",13890000,17.83,None,247658271,"0001213900-26-118028"),
 ("TOXR","2026-03-31",10850000,13.10,None,142148631,"0001213900-26-087823"),
 ("TOXR","2026-06-30",11110000,10.16,None,112916689,"0001213900-26-118028"),
 ("GXRP","2025-12-31",6300100,35.45,None,223364000,"0002037427-26-000009"),
 ("GXRP","2026-03-31",2360100,26.06,None,61516000,"0002037427-26-000007"),
 ("GXRP","2026-06-30",2840100,20.22,None,57413000,"0002037427-26-000009"),
 ("GXLM","2025-12-31",1389200,16.69,None,23191000,"0001761325-26-000010"),
 ("GXLM","2026-03-31",1398200,14.01,None,19596000,"0001761325-26-000008"),
 ("GXLM","2026-06-30",1414200,15.38,None,21753000,"0001761325-26-000010"),
]


def leer_existente():
    claves = set()
    if SALIDA.exists():
        for lin in SALIDA.read_text(encoding="utf-8").splitlines():
            if lin.strip():
                r = json.loads(lin)
                claves.add((r["fecha"], r["ticker"]))
    return claves


def fila(ticker, h):
    r = {"fecha": h.get("fecha"), "ticker": ticker}
    for c in CAMPOS[2:]:
        r[c] = h.get(c)
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--todos", action="store_true")
    ap.add_argument("--sec", action="store_true", help="vuelca también los puntos trimestrales SEC de la tabla SEC")
    ap.add_argument("--activos", default="XRP,XLM,SOL")
    a = ap.parse_args()
    activos = {x.strip().upper() for x in a.activos.split(",")}
    datos = json.loads(FLUJOS.read_text(encoding="utf-8"))
    claves = leer_existente()
    nuevas = []
    for e in datos.get("etfs", []):
        if e.get("activo") not in activos:
            continue
        hist = [h for h in e.get("historial", []) if h.get("fecha")]
        if not hist:
            continue
        hist.sort(key=lambda h: h["fecha"])
        for h in (hist if a.todos else hist[-1:]):
            k = (h["fecha"], e["ticker"])
            if k in claves:
                continue
            claves.add(k)
            nuevas.append(fila(e["ticker"], h))
    if a.sec:
        for t, f, ac, nav, ten, aum, accn in SEC:
            if (f, t) in claves:
                continue
            claves.add((f, t))
            nuevas.append({"fecha": f, "ticker": t, "acciones": ac, "nav": nav, "tenencia_monedas": ten, "aum_usd": aum,
                           "fuente": f"https://data.sec.gov/api/xbrl/companyfacts/ (accn {accn})",
                           "nivel": "P (SEC, XBRL del 10-Q/10-K; emisor = parte interesada, no auditado)"})
    if nuevas:
        with SALIDA.open("a", encoding="utf-8", newline="\n") as f:
            for r in nuevas:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(nuevas)} líneas nuevas en {SALIDA.name}")


if __name__ == "__main__":
    main()
