"""C284: metricas on-chain sin IA para las 16 redes de explorador/cadenas.json.
Fuentes: DefiLlama (agregador, nivel S), Horizon (Stellar), rippled publico (XRPL).
Lo que no se puede leer queda en null. Salida: explorador/cadenas-onchain.json."""
import json, sys, urllib.request, datetime, pathlib
RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "cadenas-onchain.json"
UA = {"User-Agent": "cartera-lector/1.0", "Content-Type": "application/json"}
# id de cadenas.json -> nombre en DefiLlama (None = no es cadena: sin dato)
MAPA = {"xrpl": "XRPL", "stellar": "Stellar", "hedera": "Hedera", "ethereum": "Ethereum",
        "solana": "Solana", "bnb": "BSC", "avalanche": "Avalanche", "polygon": "Polygon",
        "canton": "Canton", "chainlink": None, "ondo": None, "algorand": "Algorand",
        "xdc": "XDC", "quant": None, "iota": "IOTA", "plume": "Plume"}
ALIAS_STABLE = {"BSC": ["BSC", "Binance"], "XRPL": ["XRPL", "Ripple"]}

def get(url, cuerpo=None):
    rq = urllib.request.Request(url, data=cuerpo, headers=UA)
    with urllib.request.urlopen(rq, timeout=25) as r:
        return json.load(r)

def seguro(f, *a):
    try:
        return f(*a)
    except Exception as e:
        print("aviso:", type(e).__name__, str(e)[:80], file=sys.stderr)
        return None

def rpc(metodo, params):
    r = get("https://s1.ripple.com:51234/", json.dumps({"method": metodo, "params": [params]}).encode())
    return r.get("result")

def xrpl():
    info = rpc("server_info", {})["info"]
    v = info["validated_ledger"]
    out = {"ledger": v["seq"], "comision_base_xrp": v["base_fee_xrp"],
           "reserva_base_xrp": v["reserve_base_xrp"], "reserva_incr_xrp": v["reserve_inc_xrp"],
           "hora_servidor": info.get("time"), "fuente": "s1.ripple.com (rippled/Clio publico)"}
    l = seguro(rpc, "ledger", {"ledger_index": "validated", "transactions": True})
    if l and "ledger" in l:
        out["tx_en_ultimo_ledger"] = len(l["ledger"].get("transactions", []))
        out["cierre_ledger"] = l["ledger"].get("close_time_human")
    return out

def stellar():
    f = get("https://horizon.stellar.org/fee_stats")
    l = get("https://horizon.stellar.org/ledgers?order=desc&limit=1")["_embedded"]["records"][0]
    return {"ledger": l["sequence"], "cierre_ledger": l["closed_at"],
            "tx_correctas_ultimo_ledger": l.get("successful_transaction_count"),
            "operaciones_ultimo_ledger": l.get("operation_count"),
            "uso_capacidad_ledger": f.get("ledger_capacity_usage"),
            "comision_stroops_mediana": f["fee_charged"].get("p50"),
            "comision_stroops_p95": f["fee_charged"].get("p95"),
            "fuente": "horizon.stellar.org"}

def main():
    cad = json.load(open(RAIZ / "explorador" / "cadenas.json", encoding="utf-8"))["cadenas"]
    ids = [c["id"] for c in cad]
    chains = seguro(get, "https://api.llama.fi/v2/chains") or []
    tvl = {c["name"]: c.get("tvl") for c in chains}
    st = seguro(get, "https://stablecoins.llama.fi/stablecoinchains") or []
    stab = {c["name"]: (c.get("totalCirculatingUSD") or {}).get("peggedUSD") for c in st}
    nativo = {"xrpl": seguro(xrpl), "stellar": seguro(stellar)}
    res = {}
    for i in ids:
        n = MAPA.get(i)
        s = None
        if n:
            for a in ALIAS_STABLE.get(n, [n]):
                if stab.get(a) is not None:
                    s = stab[a]; break
        res[i] = {"nombre_defillama": n, "tvl_usd": tvl.get(n) if n else None,
                  "stablecoins_usd": s, "nativo": nativo.get(i)}
    out = {"_actualizado": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
           "nivel": "S",
           "aviso": "TVL y stablecoins vienen de DefiLlama, un agregador (nivel S): cambia de metodologia, "
                    "TVL no es uso real y Ethereum no incluye sus L2. Las metricas nativas de XRPL y Stellar "
                    "vienen de nodos publicos. null = no leido o no aplica (Chainlink, Ondo y Quant no son cadenas).",
           "fuentes": ["https://api.llama.fi/v2/chains", "https://stablecoins.llama.fi/stablecoinchains",
                       "https://horizon.stellar.org", "https://s1.ripple.com:51234"],
           "redes": res}
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("OK", SALIDA, sum(1 for v in res.values() if v["tvl_usd"] is not None), "con TVL")

if __name__ == "__main__":
    main()
