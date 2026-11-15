"""C329 · Liquidez de los tokens de las 16 redes de Cadenas (sin IA, sin clave).
Lee CoinGecko /coins/markets (agregador [S]) y escribe explorador/cadenas-token.json:
capitalización, volumen 24 h, rotación (volumen/capitalización), oferta circulante y total.
No inventa nada: si una moneda no responde, queda null. Uso: python scripts/leer_liquidez_tokens.py"""
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "cadenas-token.json"
# id de la red en cadenas.json -> id de CoinGecko
IDS = {"xrpl": "ripple", "stellar": "stellar", "hedera": "hedera-hashgraph", "ethereum": "ethereum",
       "solana": "solana", "bnb": "binancecoin", "avalanche": "avalanche-2", "polygon": "polygon-ecosystem-token",
       "canton": "canton-network", "chainlink": "chainlink", "ondo": "ondo-finance", "algorand": "algorand",
       "xdc": "xdce-crowd-sale", "quant": "quant-network", "iota": "iota", "plume": "plume"}
# id de la red -> nombre de la cadena en DefiLlama (comisiones pagadas por los usuarios; solo las redes que son cadena)
LLAMA = {"xrpl": "XRPL", "stellar": "Stellar", "hedera": "Hedera", "ethereum": "Ethereum", "solana": "Solana", "bnb": "BSC",
         "avalanche": "Avalanche", "polygon": "Polygon", "algorand": "Algorand", "xdc": "XDC", "iota": "IOTA", "plume": "Plume%20Mainnet"}
URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=250&ids=" + ",".join(IDS.values())


def comisiones(nombre):
    """Comisiones pagadas por los usuarios en la cadena (M$, últimos 30 días y 24 h), DefiLlama [S]; None si no responde."""
    try:
        q = urllib.request.Request("https://api.llama.fi/overview/fees/" + nombre + "?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true",
                                   headers={"User-Agent": "cartera-cliente/1.0"})
        with urllib.request.urlopen(q, timeout=30) as r:
            j = json.load(r)
        if j.get("total30d") is None:
            return None
        return {"fees30_musd": round(j["total30d"] / 1e6, 2), "fees24_musd": round((j.get("total24h") or 0) / 1e6, 3)}
    except Exception:
        return None


def dex30(nombre):
    """Volumen de intercambios descentralizados en la cadena, últimos 30 días (M$), DefiLlama [S]; None si no responde."""
    try:
        q = urllib.request.Request("https://api.llama.fi/overview/dexs/" + nombre + "?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true",
                                   headers={"User-Agent": "cartera-cliente/1.0"})
        with urllib.request.urlopen(q, timeout=30) as r:
            j = json.load(r)
        return round(j["total30d"] / 1e6, 1) if j.get("total30d") is not None else None
    except Exception:
        return None


def main():
    req = urllib.request.Request(URL, headers={"User-Agent": "cartera-cliente/1.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        filas = {x["id"]: x for x in json.load(r)}
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = {"_actualizado": hoy, "fuente": "CoinGecko /coins/markets (agregador, nivel S)",
           "url": "https://www.coingecko.com/", "fuente_comisiones": "DefiLlama /overview/fees (agregador, nivel S): comisiones pagadas por los usuarios en la cadena, en cualquier moneda; es una cota superior de la demanda del token por comisiones",
           "unidades": "capitalización y volumen en M$ (millones de dólares); oferta en unidades del token",
           "redes": {}}
    for red, cg in IDS.items():
        x = filas.get(cg)
        if not x or not x.get("market_cap"):
            out["redes"][red] = None
            continue
        mc, vol = x["market_cap"] / 1e6, (x.get("total_volume") or 0) / 1e6
        out["redes"][red] = {"coingecko_id": cg, "simbolo": (x.get("symbol") or "").upper(), "rank": x.get("market_cap_rank"),
                             "cap_musd": round(mc, 1), "vol24_musd": round(vol, 1), "rotacion_pct": round(vol / mc * 100, 2) if mc else None,
                             "circulante": x.get("circulating_supply"), "total": x.get("total_supply"),
                             "max": x.get("max_supply"), "d": hoy, "n": "S"}
        if red in LLAMA:
            f = comisiones(LLAMA[red])
            out["redes"][red]["dex30_musd"] = dex30(LLAMA[red])
            if f:
                out["redes"][red].update(f)
                out["redes"][red]["fees_anual_pct_cap"] = round(f["fees30_musd"] * 12 / mc * 100, 2) if mc else None
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    vacias = [k for k, v in out["redes"].items() if v is None]
    print(f"{len(out['redes']) - len(vacias)} de {len(IDS)} tokens leídos; sin dato: {', '.join(vacias) or 'ninguno'}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # sin red o API caída: no pisar el archivo anterior
        print(f"No se pudo leer CoinGecko ({type(e).__name__}); archivo sin cambios.")
        sys.exit(1)
