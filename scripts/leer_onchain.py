"""C284: metricas on-chain sin IA para las 16 redes de explorador/cadenas.json.
Fuentes: DefiLlama (agregador, nivel S), Horizon (Stellar), rippled publico (XRPL).
Lo que no se puede leer queda en null. Salida: explorador/cadenas-onchain.json."""
import json, sys, urllib.request, datetime, pathlib
RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "cadenas-onchain.json"
UA = {"User-Agent": "cartera-lector/1.0", "Content-Type": "application/json"}
# Diccionario unico: id de cadenas.json -> {"tvl": nombre en /v2/chains, "stable": nombres en stablecoinchains (en orden de preferencia)}
# None = no es cadena (sin dato). Comprobado contra api.llama.fi el 15-nov-2026: "Plume" (TVL 0) es un nombre antiguo, la red viva es
# "Plume Mainnet"; en IOTA el TVL esta en "IOTA" y las stablecoins en "IOTA EVM"; "Binance" figura con TVL 0 (la red viva es BSC).
DL = {"xrpl": ("XRPL", ["XRPL", "Ripple"]), "stellar": ("Stellar", ["Stellar"]), "hedera": ("Hedera", ["Hedera"]),
      "ethereum": ("Ethereum", ["Ethereum"]), "solana": ("Solana", ["Solana"]), "bnb": ("BSC", ["BSC", "Binance"]),
      "avalanche": ("Avalanche", ["Avalanche"]), "polygon": ("Polygon", ["Polygon"]), "canton": ("Canton", ["Canton"]),
      "chainlink": None, "ondo": None, "algorand": ("Algorand", ["Algorand"]), "xdc": ("XDC", ["XDC"]), "quant": None,
      "iota": ("IOTA", ["IOTA", "IOTA EVM"]), "plume": ("Plume Mainnet", ["Plume Mainnet"])}

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
    previo = {}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8")).get("redes", {})
        except Exception:
            previo = {}
    fallos = []
    chains = seguro(get, "https://api.llama.fi/v2/chains") or []
    st = seguro(get, "https://stablecoins.llama.fi/stablecoinchains") or []
    if not chains:
        fallos.append("DefiLlama /v2/chains sin datos: TVL conservado del dato previo")
    if not st:
        fallos.append("DefiLlama stablecoinchains sin datos: stablecoins conservadas del dato previo")
    tvl = {c["name"]: c.get("tvl") for c in chains}
    stab = {c["name"]: (c.get("totalCirculatingUSD") or {}).get("peggedUSD") for c in st}
    nativo = {"xrpl": seguro(xrpl), "stellar": seguro(stellar)}
    for k, v in nativo.items():
        if v is None:
            fallos.append(f"nativo {k} no leido: conservado el previo")
    res = {}
    for i in ids:
        ent = DL.get(i)
        n = ent[0] if ent else None
        t = s_ = None
        if ent:
            t = tvl.get(n)
            for a in ent[1]:
                if stab.get(a) is not None:
                    s_ = stab[a]; break
        r0 = previo.get(i, {})
        res[i] = {"nombre_defillama": n, "tvl_usd": t if chains else r0.get("tvl_usd"),
                  "stablecoins_usd": s_ if st else r0.get("stablecoins_usd"),
                  "nativo": nativo.get(i) if nativo.get(i) is not None else r0.get("nativo")}
    if not chains and not st and not any(nativo.values()):
        print("ERROR: no se pudo leer nada; no se sobrescribe", SALIDA, file=sys.stderr)
        return
    out = {"_actualizado": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
           "nivel": "S",
           "aviso": "TVL y stablecoins vienen de DefiLlama, un agregador (nivel S): cambia de metodologia, "
                    "TVL no es uso real y Ethereum no incluye sus L2. Las metricas nativas de XRPL y Stellar "
                    "vienen de nodos publicos. null = no leido o no aplica (Chainlink, Ondo y Quant no son cadenas).",
           "fuentes": ["https://api.llama.fi/v2/chains", "https://stablecoins.llama.fi/stablecoinchains",
                       "https://horizon.stellar.org", "https://s1.ripple.com:51234"],
           "fallos": fallos, "redes": res}
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("OK", SALIDA, sum(1 for v in res.values() if v["tvl_usd"] is not None), "con TVL")

if __name__ == "__main__":
    main()
