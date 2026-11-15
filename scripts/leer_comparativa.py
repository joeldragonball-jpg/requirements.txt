"""C318 - Comparativa neutral de liquidación entre redes (medidas públicas puntuales), sin clave y sin IA.
Uso: python scripts/leer_comparativa.py
Lee nodos/APIs públicos (XRPL, Stellar, Ethereum, Solana, Hedera, Algorand) y precios de DefiLlama;
escribe explorador/comparativa-liquidacion.json. Si una red falla, conserva el bloque bueno anterior.
Solo lectura de cadenas-onchain.json y profundidad-multidivisa.json. Verificación SSL siempre activa."""
import json
import ssl
import statistics as st
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "comparativa-liquidacion.json"
CTX = ssl.create_default_context()
UA = {"User-Agent": "cartera-lectura-publica/1.0", "Content-Type": "application/json"}
N = 20  # bloques/ledgers de la muestra


def ahora():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def http(url, cuerpo=None, intentos=3):
    ult = None
    for i in range(intentos):
        try:
            data = json.dumps(cuerpo).encode() if cuerpo is not None else None
            req = urllib.request.Request(url, data=data, headers=UA)
            with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            ult = e
            if e.code in (400, 404):
                break
            time.sleep(2 * (i + 1))
        except Exception as e:
            ult = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {ult}")


def rpc(url, metodo, params=None):
    r = http(url, {"jsonrpc": "2.0", "id": 1, "method": metodo, "params": params or []})
    if "error" in r:
        raise RuntimeError(f"{metodo}: {r['error']}")
    return r["result"]


def precios():
    ids = {"xrp": "ripple", "xlm": "stellar", "eth": "ethereum", "sol": "solana", "hbar": "hedera-hashgraph", "algo": "algorand"}
    q = ",".join("coingecko:" + v for v in ids.values())
    d = http("https://coins.llama.fi/prices/current/" + q)["coins"]
    return {k: d["coingecko:" + v]["price"] for k, v in ids.items() if "coingecko:" + v in d}


def mediana(x):
    return st.median(x) if x else None


def estadisticas(tiempos, ntx):
    """tiempos ascendentes (s); ntx = tx de los bloques posteriores al primero."""
    ints = [b - a for a, b in zip(tiempos, tiempos[1:]) if b > a]
    dur = tiempos[-1] - tiempos[0]
    return {
        "tiempo_bloque_medio_s": round(dur / (len(tiempos) - 1), 3) if dur > 0 else None,
        "tiempo_bloque_mediano_s": mediana(ints),  # en XRPL close_time se redondea a 10 s o más (y rippled suma 1 s si colisiona): la mediana no es dato, usar la media
        "muestra_bloques": len(tiempos),
        "ventana_s": round(dur, 1),
        "tps_medio": round(sum(ntx) / dur, 2) if dur > 0 else None,
    }


def xrpl(p):
    u = "https://s1.ripple.com:51234"
    r = rpc(u, "ledger", [{"ledger_index": "validated", "transactions": False}])
    idx = int(r["ledger_index"])
    ts, ntx = [], []
    for i in range(idx - N + 1, idx + 1):
        L = rpc(u, "ledger", [{"ledger_index": i, "transactions": True, "expand": False}])["ledger"]
        ts.append(int(L["close_time"]) + 946684800)
        ntx.append(len(L.get("transactions", [])))
    f = rpc(u, "fee")
    # Comisión que se paga hoy = open_ledger_fee (nivel de referencia de 10 gotas, mismo que base_fee) con la red sin congestión.
    # median_fee (5000 gotas) es el nivel por defecto de la cola (500 x referencia), NO la comisión pagada; se guarda aparte.
    # Comprobado contra el método `fee` de s1.ripple.com el 15-nov-2026: open_ledger_fee=10, base_fee=10, median_fee=5000.
    drops = float(f["drops"].get("open_ledger_fee", f["drops"]["base_fee"]))
    med = float(f["drops"]["median_fee"])
    xrp = drops / 1e6
    e = estadisticas(ts, ntx[1:])
    e.update({
        "finalidad_medida_s": e["tiempo_bloque_medio_s"],
        "finalidad_nota": "un ledger validado es final (consenso sin bifurcaciones); el tiempo medido es el intervalo de cierre",
        "comision_nativa": f"{xrp:.8f} XRP ({drops:g} gotas: comisión de ledger abierto, igual a la base; la «mediana» de la cola, {med:g} gotas, es solo el nivel por defecto con congestión)",
        "comision_mediana_cola_usd": round(med / 1e6 * p["xrp"], 8) if "xrp" in p else None,
        "comision_minima_usd": round(float(f["drops"]["minimum_fee"]) / 1e6 * p["xrp"], 8) if "xrp" in p else None,
        "comision_usd": round(xrp * p["xrp"], 8) if "xrp" in p else None,
        "ledger": idx,
        "fuente": "s1.ripple.com:51234 (rippled; métodos ledger y fee)",
    })
    return e


def stellar(p):
    h = "https://horizon.stellar.org"
    L = http(f"{h}/ledgers?order=desc&limit={N}")["_embedded"]["records"][::-1]
    ts = [datetime.fromisoformat(x["closed_at"].replace("Z", "+00:00")).timestamp() for x in L]
    ntx = [x["successful_transaction_count"] + x["failed_transaction_count"] for x in L[1:]]
    fs = http(f"{h}/fee_stats")
    stroops = float(fs["fee_charged"]["p50"])
    xlm = stroops / 1e7
    e = estadisticas(ts, ntx)
    e.update({
        "finalidad_medida_s": e["tiempo_bloque_medio_s"],
        "finalidad_nota": "un ledger cerrado por el protocolo de consenso federado (SCP) es final; el tiempo medido es el intervalo de cierre",
        "comision_nativa": f"{xlm:.7f} XLM (mediana cobrada, {stroops:g} stroops)",
        "comision_usd": round(xlm * p["xlm"], 8) if "xlm" in p else None,
        "ledger": L[-1]["sequence"],
        "fuente": "horizon.stellar.org (ledgers y fee_stats)",
    })
    return e


def ethereum(p):
    u = "https://ethereum-rpc.publicnode.com"
    ult = rpc(u, "eth_getBlockByNumber", ["latest", False])
    n = int(ult["number"], 16)
    ts, ntx = [], []
    for i in range(n - N + 1, n + 1):
        b = ult if i == n else rpc(u, "eth_getBlockByNumber", [hex(i), False])
        ts.append(int(b["timestamp"], 16))
        ntx.append(len(b["transactions"]))
    fin = rpc(u, "eth_getBlockByNumber", ["finalized", False])
    seg = rpc(u, "eth_getBlockByNumber", ["safe", False])
    fh = rpc(u, "eth_feeHistory", [hex(10), "latest", [50]])
    base = int(fh["baseFeePerGas"][-1], 16)
    prio = mediana([int(x[0], 16) for x in fh["reward"]])
    eth = 21000 * (base + prio) / 1e18
    e = estadisticas(ts, ntx[1:])
    e.update({
        "finalidad_medida_s": int(ult["timestamp"], 16) - int(fin["timestamp"], 16),
        "finalidad_nota": "retraso medido entre el último bloque y el bloque «finalized» (Casper FFG); el bloque «safe» va %d s detrás" % (int(ult["timestamp"], 16) - int(seg["timestamp"], 16)),
        "bloques_hasta_finalizado": n - int(fin["number"], 16),
        "comision_nativa": f"{eth:.8f} ETH (transferencia simple de 21000 gas; base {base/1e9:.3f} gwei + propina mediana {prio/1e9:.3f} gwei)",
        "comision_usd": round(eth * p["eth"], 6) if "eth" in p else None,
        "ledger": n,
        "fuente": "ethereum-rpc.publicnode.com (eth_getBlockByNumber latest/safe/finalized, eth_feeHistory)",
    })
    return e


def solana(p):
    u = "https://api.mainnet-beta.solana.com"
    m = rpc(u, "getRecentPerformanceSamples", [30])
    tx = sum(x["numTransactions"] for x in m)
    nv = sum(x.get("numNonVoteTransactions", 0) for x in m)
    seg = sum(x["samplePeriodSecs"] for x in m)
    slots = sum(x["numSlots"] for x in m)
    fin = rpc(u, "getSlot", [{"commitment": "finalized"}])
    conf = rpc(u, "getSlot", [{"commitment": "confirmed"}])
    pf = rpc(u, "getRecentPrioritizationFees", [])
    prio = mediana([x["prioritizationFee"] for x in pf]) or 0  # microlamports por unidad de cómputo
    lamports = 5000 + prio * 450 / 1e6  # base 5000/firma + prioridad sobre ~450 CU de una transferencia simple
    sol = lamports / 1e9
    tslot = seg / slots if slots else None
    return {
        "tiempo_bloque_medio_s": round(tslot, 3) if tslot else None,
        "tiempo_bloque_mediano_s": None,
        "muestra_bloques": slots,
        "ventana_s": seg,
        "tps_medio": round(tx / seg, 1) if seg else None,
        "tps_sin_votos": round(nv / seg, 1) if seg and nv else None,
        "tps_nota": "numTransactions del nodo público; en Solana las transacciones de voto de los validadores suelen contarse aparte o dentro: si tps_sin_votos coincide con tps_medio, no se puede separar con esta fuente [VERIFICAR]",
        "finalidad_medida_s": None,
        "finalidad_nota": "no medible con el RPC público (getSlot confirmed/finalized difiere en %d slots, no es un retraso de finalidad real); la ficha de Solana indica slot de 200 ms tras Alpenglow (21-oct-2026) [VERIFICAR finalidad]" % (conf - fin),
        "comision_nativa": f"{lamports:.0f} lamports (base 5000 por firma + prioridad mediana {prio} µlamports/CU × ~450 CU)",
        "comision_usd": round(sol * p["sol"], 8) if "sol" in p else None,
        "ledger": fin,
        "fuente": "api.mainnet-beta.solana.com (getRecentPerformanceSamples, getSlot, getRecentPrioritizationFees)",
    }


def hedera(p):
    b = http("https://mainnet-public.mirrornode.hedera.com/api/v1/blocks?limit=%d&order=desc" % N)["blocks"][::-1]
    ts = [float(x["timestamp"]["from"]) for x in b]
    ntx = [x["count"] for x in b[1:]]
    e = estadisticas(ts, ntx)
    e.update({
        "finalidad_medida_s": e["tiempo_bloque_medio_s"],
        "finalidad_nota": "el mirror node publica registros por intervalos de pocos segundos; la finalidad aBFT es del orden de segundos según la documentación [VERIFICAR medida directa]",
        "comision_nativa": "tarifa documentada en USD (transferencia cripto ≈ 0,0001 USD) [VERIFICAR, no medida]",
        "comision_usd": 0.0001,
        "comision_es_medida": False,
        "ledger": b[-1]["number"],
        "fuente": "mainnet-public.mirrornode.hedera.com (blocks); tarifa: documentación de Hedera",
    })
    return e


def algorand(p):
    u = "https://mainnet-api.algonode.cloud"
    r = http(u + "/v2/status")["last-round"]
    ts, tc = [], []
    for i in range(r - N + 1, r + 1):
        b = http(f"{u}/v2/blocks/{i}?format=json")["block"]
        ts.append(b["ts"])
        tc.append(b.get("tc", 0))
    ntx = [b - a for a, b in zip(tc, tc[1:])]
    pr = http(u + "/v2/transactions/params")
    fee = max(int(pr.get("min-fee", 1000)), 1000)
    algo = fee / 1e6
    e = estadisticas(ts, ntx)
    e.update({
        "finalidad_medida_s": e["tiempo_bloque_medio_s"],
        "finalidad_nota": "un bloque certificado es final (sin bifurcaciones); el tiempo medido es el intervalo entre bloques",
        "comision_nativa": f"{algo:.6f} ALGO (tarifa mínima, {fee} microALGO)",
        "comision_usd": round(algo * p["algo"], 8) if "algo" in p else None,
        "ledger": r,
        "fuente": "mainnet-api.algonode.cloud (nodo público; status, blocks, transactions/params)",
    })
    return e


REDES = [("xrpl", "XRPL", xrpl), ("stellar", "Stellar", stellar), ("ethereum", "Ethereum", ethereum),
         ("solana", "Solana", solana), ("hedera", "Hedera", hedera), ("algorand", "Algorand", algorand)]


def activos():
    """Solo lectura de los JSON de stablecoins/fiat tokenizada ya generados."""
    out = {}
    try:
        co = json.loads((RAIZ / "explorador" / "cadenas-onchain.json").read_text(encoding="utf-8"))
        for k, v in co["redes"].items():
            out.setdefault(k, {})["stablecoins_usd_defillama"] = v.get("stablecoins_usd")
            out[k]["fecha_dato"] = co.get("_actualizado")
    except Exception as e:
        out["_error_onchain"] = str(e)
    try:
        pm = json.loads((RAIZ / "explorador" / "profundidad-multidivisa.json").read_text(encoding="utf-8"))
        mapa = {"XRPL": "xrpl", "Stellar": "stellar", "Ethereum": "ethereum", "Solana": "solana", "Hedera": "hedera", "Algorand": "algorand"}
        for nombre, v in pm["stablecoins_por_red"]["datos"].items():
            k = mapa.get(nombre)
            if k:
                out.setdefault(k, {})["stablecoins_top"] = v.get("top", [])[:6]
                out[k]["n_stablecoins"] = v.get("n_stablecoins")
        out["_fecha_profundidad"] = pm.get("_actualizado")
    except Exception as e:
        out["_error_profundidad"] = str(e)
    return out


def main():
    previo = {}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        except Exception:
            previo = {}
    fallos = []
    try:
        p = precios()
    except Exception as e:
        p = previo.get("precios_usd", {})
        fallos.append(f"precios: {e}")
    ahora_ = ahora()
    redes = dict(previo.get("redes", {}))
    for k, nombre, f in REDES:
        try:
            b = f(p)
            b["medido_utc"] = ahora_
            b["nombre"] = nombre
            redes[k] = b
        except Exception as e:
            fallos.append(f"{nombre}: {e}")
            if k in redes:
                redes[k]["dato_antiguo"] = True
    if not redes:
        raise SystemExit("sin datos y sin copia previa: no se escribe nada\n" + "\n".join(fallos))
    out = dict(previo)  # conserva bloques manuales (T+0/T+n, fortalezas, lo que no sabemos, hechos con fuente)
    out.update({
        "_actualizado": ahora_,
        "nivel": "P",
        "aviso": "Medidas puntuales de nodos públicos (una instantánea, no un promedio histórico): la comisión y el TPS varían con la carga. No es recomendación.",
        "precios_usd": p,
        "precios_fuente": "coins.llama.fi (DefiLlama, precio de referencia en el momento de la medida)",
        "redes": redes,
        "activos_liquidacion": activos(),
        "fallos": fallos,
    })
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("OK", ahora_, "fallos:", fallos or "ninguno")


if __name__ == "__main__":
    main()
