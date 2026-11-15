"""Acumula instantáneas de ETF spot (acciones, NAV, tenencia) en explorador/etf-flujos.json y calcula el flujo
entre dos instantáneas consecutivas: flujo = (acciones_t - acciones_t-1) x NAV_t. SOLO LECTURA de datos ya leídos (sin red, sin IA).
Las webs de emisores (bitxrpetf.com, 21shares.com) son SPA: se leen en Chrome y se pasan por argumentos.
Uso: python scripts/leer_etf_flujos.py --ticker XRP --fecha 2026-11-12 --acciones 36440000 --nav 11.53 --tenencia 406770577.61 --fuente URL
"""
import argparse
import json
from datetime import date, timedelta
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "explorador" / "etf-flujos.json"


def dia_habil_siguiente(f):
    d = f + timedelta(days=1)
    while d.weekday() >= 5:
        d += timedelta(days=1)
    return d


def es_trimestral(h):
    t = f"{h.get('nivel', '')} {h.get('fuente', '')} {h.get('nota', '')}".lower()
    return "10-q" in t or "trimestral" in t


def flujo_valido(a, b):
    """Flujo diario solo entre dos instantaneas de dias habiles consecutivos y no trimestrales/derivadas; si no, (False, motivo)."""
    if es_trimestral(a) or es_trimestral(b):
        return False, "alguna instantanea es trimestral (10-Q): la diferencia no es un flujo diario"
    if "derivad" in f"{a.get('nivel', '')} {b.get('nivel', '')}".lower():
        return False, "acciones derivadas (no leidas del emisor): flujo no fiable"
    fa, fb = date.fromisoformat(a["fecha"]), date.fromisoformat(b["fecha"])
    if dia_habil_siguiente(fa) != fb:
        return False, f"las instantaneas ({a['fecha']} y {b['fecha']}) no son de dias habiles consecutivos"
    return True, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--fecha", required=True)
    ap.add_argument("--acciones", type=float, required=True)
    ap.add_argument("--nav", type=float, required=True)
    ap.add_argument("--tenencia", type=float)
    ap.add_argument("--fuente", required=True)
    # C280 (15-nov): datos leidos a mano en la web del emisor con Chrome; opcionales para fondos nuevos o derivados
    ap.add_argument("--aum", type=float)
    ap.add_argument("--nota")
    ap.add_argument("--nivel", default="P (emisor, parte interesada)")
    ap.add_argument("--nombre")
    ap.add_argument("--activo")
    ap.add_argument("--emisor")
    ap.add_argument("--web")
    a = ap.parse_args()
    d = json.loads(RUTA.read_text(encoding="utf-8"))
    etf = next((e for e in d["etfs"] if e["ticker"] == a.ticker), None)
    if etf is None:  # fondo nuevo (p. ej. BTC): se crea con los datos opcionales
        etf = {"ticker": a.ticker, "nombre": a.nombre, "activo": a.activo, "emisor": a.emisor, "web": a.web, "historial": [], "flujo_usd": None}
        d["etfs"].append(etf)
    hist = etf.setdefault("historial", [])
    hist[:] = [h for h in hist if h["fecha"] != a.fecha]
    reg = {"fecha": a.fecha, "acciones": a.acciones, "nav": a.nav, "tenencia_monedas": a.tenencia, "fuente": a.fuente, "nivel": a.nivel}
    if a.aum is not None:
        reg["aum_usd"] = a.aum
    if a.nota:
        reg["nota"] = a.nota
    hist.append(reg)
    hist.sort(key=lambda h: h["fecha"])
    for i in range(len(hist)):
        hist[i].pop("flujo_usd", None)
        hist[i].pop("flujo_motivo", None)
    for i in range(1, len(hist)):
        ok, motivo = flujo_valido(hist[i - 1], hist[i])
        if ok:
            hist[i]["flujo_usd"] = round((hist[i]["acciones"] - hist[i - 1]["acciones"]) * hist[i]["nav"])
        else:
            hist[i]["flujo_usd"] = None
            hist[i]["flujo_motivo"] = motivo
    RUTA.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print("ok", a.ticker, len(hist), "instantáneas")


if __name__ == "__main__":
    main()
