"""C284: metricas on-chain sin IA para las 16 redes de explorador/cadenas.json.
Fuentes: DefiLlama (agregador, nivel S), Horizon (Stellar), rippled publico (XRPL).
Lo que no se puede leer queda en null. Salida: explorador/cadenas-onchain.json."""
import json, sys, urllib.request, urllib.parse, datetime, pathlib
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

RWA = RAIZ / "explorador" / "rwa-por-cadena-manual.json"
# Nombre en rwa-por-cadena-manual.json por id (solo las que tiene RWA.xyz)
RWA_NOMBRE = {"ethereum": "Ethereum", "solana": "Solana", "stellar": "Stellar", "xrpl": "XRPL", "avalanche": "Avalanche",
              "polygon": "Polygon", "bnb": "BNB Chain", "hedera": "Hedera", "algorand": "Algorand", "xdc": "XDC",
              "plume": "Plume", "iota": "IOTA", "canton": "Canton"}

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

def overview(tipo, nombres):
    """fees/dexs 24h y 30d en USD desde DefiLlama overview; prueba cada nombre de cadena hasta que uno devuelva dato."""
    for n in nombres:
        d = seguro(get, f"https://api.llama.fi/overview/{tipo}/{urllib.parse.quote(n)}?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true")
        if d and d.get("total24h") is not None:
            return {"usd_24h": d.get("total24h"), "usd_30d": d.get("total30d"), "cambio_30d_pct": d.get("change_30dover30d"), "nombre_usado": n}
    return None

def emisores(st_json, nombres, top=5):
    """Top emisores de stablecoins en la red a partir de /stablecoins (chainCirculating, USD)."""
    fil = []
    for a in st_json:
        if a.get("pegType") != "peggedUSD":
            continue
        cc = a.get("chainCirculating") or {}
        for n in nombres:
            v = ((cc.get(n) or {}).get("current") or {}).get("peggedUSD")
            if v:
                fil.append({"emisor": a.get("name"), "simbolo": a.get("symbol"), "usd": round(v)}); break
    fil.sort(key=lambda x: -x["usd"])
    return fil[:top]

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
    sts = seguro(get, "https://stablecoins.llama.fi/stablecoins") or {}
    sts = sts.get("peggedAssets") or []
    if not sts:
        fallos.append("DefiLlama /stablecoins sin datos: emisores conservados del dato previo")
    try:
        rwa = {c["cadena"]: c for c in json.loads(RWA.read_text(encoding="utf-8")).get("cadenas", [])}
        rwa_fecha = json.loads(RWA.read_text(encoding="utf-8")).get("leido")
    except Exception:
        rwa, rwa_fecha = {}, None
    tvl = {c["name"]: c.get("tvl") for c in chains}
    stab = {c["name"]: (c.get("totalCirculatingUSD") or {}).get("peggedUSD") for c in st}
    nativo = {"xrpl": seguro(xrpl), "stellar": seguro(stellar)}
    for k, v in nativo.items():
        if v is None:
            fallos.append(f"nativo {k} no leido: conservado el previo")
    hoy = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
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
        fees = dex = emi = None
        if ent:
            nombres = list(dict.fromkeys([ent[0]] + ent[1]))
            fees, dex = overview("fees", nombres), overview("dexs", nombres)
            emi = emisores(sts, ent[1]) if sts else None
        # Aviso: stablecoins DefiLlama frente a RWA.xyz (no son lo mismo: RWA.xyz mide activos reales tokenizados)
        av = None
        rr = rwa.get(RWA_NOMBRE.get(i, ""))
        if rr and s_:
            av = (f"DefiLlama: stablecoins {s_/1e6:,.0f} M USD (leido {hoy}). RWA.xyz: RWA distribuidos "
                  f"{rr['distribuido']/1e6:,.0f} M USD (leido {rwa_fecha}). Son magnitudes distintas (stablecoins vs. activos reales "
                  f"tokenizados) y de agregadores distintos (nivel S): no comparar ni sumar.")
        res[i] = {"nombre_defillama": n, "tvl_usd": t if chains else r0.get("tvl_usd"),
                  "stablecoins_usd": s_ if st else r0.get("stablecoins_usd"),
                  "nativo": nativo.get(i) if nativo.get(i) is not None else r0.get("nativo"),
                  "fees": fees if fees else r0.get("fees"),
                  "dex_volumen": dex if dex else r0.get("dex_volumen"),
                  "stablecoins_emisores_top5": emi if emi else r0.get("stablecoins_emisores_top5"),
                  "aviso_rwa": av if av else r0.get("aviso_rwa")}
        if ent and (not fees or not dex):
            fallos.append(f"{i}: fees/dex no leidos (o la red no esta en el overview): conservado el previo")
    if not chains and not st and not any(nativo.values()):
        print("ERROR: no se pudo leer nada; no se sobrescribe", SALIDA, file=sys.stderr)
        return
    out = {"_actualizado": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
           "nivel": "S",
           "aviso": "TVL y stablecoins vienen de DefiLlama, un agregador (nivel S): cambia de metodologia, "
                    "TVL no es uso real y Ethereum no incluye sus L2. Las metricas nativas de XRPL y Stellar "
                    "vienen de nodos publicos. Fees y volumen DEX (fees/dex_volumen): USD, 24 h y 30 dias moviles, DefiLlama overview (nivel S); "
                    "fees = comisiones pagadas por usuarios, no ingresos del protocolo. stablecoins_emisores_top5: USD, DefiLlama /stablecoins por chainCirculating. null = no leido o no aplica (Chainlink, Ondo y Quant no son cadenas).",
           "fuentes": ["https://api.llama.fi/v2/chains", "https://stablecoins.llama.fi/stablecoinchains", "https://stablecoins.llama.fi/stablecoins",
                       "https://api.llama.fi/overview/fees/{red}", "https://api.llama.fi/overview/dexs/{red}", "explorador/rwa-por-cadena-manual.json",
                       "https://horizon.stellar.org", "https://s1.ripple.com:51234"],
           "fallos": fallos, "redes": res}
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("OK", SALIDA, sum(1 for v in res.values() if v["tvl_usd"] is not None), "con TVL")

if __name__ == "__main__":
    main()
