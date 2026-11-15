"""C308 - Profundidad de mercado multi-divisa (instantánea), sin clave y sin IA.
Uso: python scripts/leer_profundidad.py
Escribe explorador/profundidad-multidivisa.json y añade una línea al día a explorador/profundidad-historial.jsonl.
Si una fuente falla se conserva el dato bueno anterior de ese bloque."""
import json
import ssl
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "profundidad-multidivisa.json"
HIST = RAIZ / "explorador" / "profundidad-historial.jsonl"
CTX = ssl.create_default_context()  # verificación de certificados SIEMPRE activa
UA = {"User-Agent": "cartera-lectura-publica/1.0", "Content-Type": "application/json"}
XRPL_NODOS = ["https://s1.ripple.com:51234", "https://xrplcluster.com"]
HORIZON = "https://horizon.stellar.org"


def ahora():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


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
        except Exception as e:  # red, JSON, timeout
            ult = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url[:80]}: {ult}")


def rpc(metodo, params):
    ult = None
    for nodo in XRPL_NODOS:
        try:
            r = http(nodo, {"method": metodo, "params": [params]})["result"]
            if r.get("status") == "error":
                raise RuntimeError(r.get("error"))
            return r, nodo
        except Exception as e:
            ult = e
    raise RuntimeError(f"XRPL {metodo}: {ult}")


def hexmoneda(c):
    return c if len(c) == 3 else c.encode().hex().upper().ljust(40, "0")


def metricas(bids, asks, unidad):
    """bids/asks: [(precio, cantidad_base)] del mejor al peor. Precio = contradivisa por base."""
    if not bids or not asks:
        return {"estado": "libro vacio en un lado", "ofertas_compra": len(bids), "ofertas_venta": len(asks)}
    mb, ma = bids[0][0], asks[0][0]
    mid = (mb + ma) / 2

    def prof(lado, signo, pct):
        lim = mid * (1 + signo * pct / 100)
        return sum(q * p for p, q in lado if (p >= lim if signo < 0 else p <= lim))

    return {
        "mejor_compra": mb, "mejor_venta": ma, "precio_medio": mid,
        "spread_pct": round((ma - mb) / mid * 100, 4),
        "cruzado": mb >= ma,
        "ofertas_compra": len(bids), "ofertas_venta": len(asks),
        "profundidad_1pct_compra": round(prof(bids, -1, 1), 2), "profundidad_1pct_venta": round(prof(asks, 1, 1), 2),
        "profundidad_2pct_compra": round(prof(bids, -1, 2), 2), "profundidad_2pct_venta": round(prof(asks, 1, 2), 2),
        "unidad_profundidad": unidad,
        "lectura": ("spread >3 %: libro inactivo, ofertas lejos del precio de mercado; la profundidad ±1 %/±2 % sale ~0 porque el precio medio cae en un hueco" if (ma - mb) / mid > 0.03 else "libro con ofertas cerca del precio medio"),
        "aviso_cobertura": "solo libro de ordenes (CLOB); excluye AMM/pools. Se leen hasta 200-300 ofertas por lado: si la ventana ±2 % las agota, la cifra es un minimo",
    }


# ---------- XRPL ----------
EMISORES_XRPL = [
    ("XRP/RLUSD", "RLUSD", "rMxCKbEDwqr76QuheSUMdEGf4B9xJ8m5De", "USD"),
    ("XRP/USD (Bitstamp)", "USD", "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B", "USD"),
    ("XRP/USD (GateHub)", "USD", "rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq", "USD"),
    ("XRP/EUR (GateHub)", "EUR", "rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq", "EUR"),
    ("XRP/USDC (Circle)", "USDC", "rGm7WCVp9gb4jZHWTEtGUr4dd74z2XuWhE", "USD"),
    ("XRP/EUROP (Schuman)", "EUROP", "rMkEuRii9w9uBMQDnWV5AA43gvYZR9JxVK", "EUR"),
    ("XRP/SOLO", "SOLO", "rsoLo2S1kiGeCcn6hCUXVrCpGMWLrRrLZz", "SOLO"),
    ("XRP/BTC (Bitstamp)", "BTC", "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B", "BTC"),
]


def libro_xrpl(cod, emisor):
    cur = {"currency": hexmoneda(cod), "issuer": emisor}
    xrp = {"currency": "XRP"}

    def ofertas(gets, pays, lado):
        r, nodo = rpc("book_offers", {"taker_gets": gets, "taker_pays": pays, "limit": 300})
        out = []
        for o in r.get("offers", []):
            g = o.get("taker_gets_funded", o["TakerGets"])
            p = o.get("taker_pays_funded", o["TakerPays"])
            xg = float(g) / 1e6 if isinstance(g, str) else float(g["value"])
            xp = float(p) / 1e6 if isinstance(p, str) else float(p["value"])
            if lado == "venta":   # vende XRP (gets=XRP) y pide divisa (pays)
                q, pr = xg, (xp / xg if xg else 0)
            else:                 # compra XRP: gets=divisa, pays=XRP
                q, pr = xp, (xg / xp if xp else 0)
            if q > 0 and pr > 0:
                out.append((pr, q))
        return out, nodo, r.get("ledger_index")

    asks, nodo, li = ofertas(xrp, cur, "venta")
    bids, _, _ = ofertas(cur, xrp, "compra")
    asks.sort(key=lambda x: x[0])
    bids.sort(key=lambda x: -x[0])
    return bids, asks, nodo, li


def bloque_xrpl_dex():
    res, fallos = {}, []
    for nombre, cod, emisor, unidad in EMISORES_XRPL:
        try:
            bids, asks, nodo, li = libro_xrpl(cod, emisor)
            m = metricas(bids, asks, f"{unidad} por XRP (valor en {unidad})")
            m.update({"emisor": emisor, "ledger": li, "fuente": nodo, "nivel": "P",
                      "metodo": "book_offers (hasta 300 ofertas por lado, saldo financiado); profundidad = suma(precio x cantidad XRP) en %s dentro de ±1 %% y ±2 %% del precio medio" % unidad,
                      "leido_utc": ahora()})
            res[nombre] = m
        except Exception as e:
            fallos.append(f"{nombre}: {e}")
    return res, fallos


def pagos_y_reposo():
    out = {"leido_utc": ahora()}
    fallos = []
    total_coins = None
    try:
        r, nodo = rpc("ledger", {"ledger_index": "validated"})
        idx = int(r["ledger"]["ledger_index"])
        t_now = int(r["ledger"]["close_time"])
        total_coins = int(r["ledger"]["total_coins"])
        r0, _ = rpc("ledger", {"ledger_index": idx - 24000})
        seg = t_now - int(r0["ledger"]["close_time"])
        ledgers_dia = 24000 * 86400 / seg if seg > 0 else 24686
        muestras = list(range(idx - 22000, idx, 2000))  # 11 ledgers repartidos en ~24 h
        tx_tot = pag_ok = pag_xrp = n = 0
        for li in muestras:
            try:
                rl, _ = rpc("ledger", {"ledger_index": li, "transactions": True, "expand": True})
            except Exception:
                continue
            n += 1
            for t in rl["ledger"]["transactions"]:
                tx_tot += 1
                if t.get("TransactionType") == "Payment":
                    meta = t.get("metaData") or t.get("meta") or {}
                    if meta.get("TransactionResult") == "tesSUCCESS":
                        pag_ok += 1
                        if isinstance(t.get("Amount"), str):
                            pag_xrp += 1
        if n >= 6:
            out["pagos_por_dia_estimados"] = {
                "valor": round(pag_ok / n * ledgers_dia),
                "tx_totales_por_dia_estimadas": round(tx_tot / n * ledgers_dia),
                "pagos_en_xrp_nativo_por_dia": round(pag_xrp / n * ledgers_dia),
                "ledgers_muestreados": n, "ledgers_por_dia": round(ledgers_dia),
                "nivel": "P", "fuente": nodo,
                "metodo": "extrapolacion: se cuentan Payment con tesSUCCESS en %d ledgers separados 2000 (~2 h) en las ultimas ~24 h y se multiplica por ledgers/dia. Muestra pequena: orden de magnitud, no cifra exacta; incluye bots, spam y pagos de IOU" % n,
                "leido_utc": ahora()}
        else:
            out["pagos_por_dia_estimados"] = {"valor": None, "motivo": "menos de 6 ledgers legibles"}
            fallos.append("pagos: muestras insuficientes")
    except Exception as e:
        out["pagos_por_dia_estimados"] = {"valor": None, "motivo": str(e)[:150]}
        fallos.append(f"pagos: {e}")
    try:
        b = http("https://api.xrpscan.com/api/v1/balances")
        esc = sum(int(x.get("escrow") or 0) for x in b)
        out["saldo_en_escrow"] = {
            "xrp": round(esc / 1e6),
            "pct_del_supply": round(esc / total_coins * 100, 2) if total_coins else None,
            "nivel": "S", "fuente": "api.xrpscan.com/api/v1/balances (cuentas mas grandes) y total_coins del nodo",
            "metodo": "suma del campo escrow de las cuentas listadas; el escrow no es 'saldo inactivo' en sentido estricto: es XRP bloqueado por calendario (principalmente Ripple)",
            "leido_utc": ahora()}
    except Exception as e:
        out["saldo_en_escrow"] = {"xrp": None, "motivo": str(e)[:150]}
        fallos.append(f"escrow: {e}")
    out["pct_supply_inactivo_mas_1_ano"] = {
        "valor": None,
        "motivo": "no hay API publica sin clave con el % del supply en cuentas sin movimiento >1 ano; exigiria recorrer el historial de todas las cuentas (servicios como Bithomp/xrpscan lo dan con clave o de pago)"}
    return out, fallos


# ---------- Stellar ----------
def activo_stellar(cod, emisor):
    if cod == "XLM":
        return {"asset_type": "native"}
    return {"asset_type": "credit_alphanum4" if len(cod) <= 4 else "credit_alphanum12", "asset_code": cod, "asset_issuer": emisor}


USDC_S = "GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN"
EURC_S = "GDHU6WRG4IEQXM5NZ4BMPKOXHW76MZM4Y2IEMFDVXBSDP6SJY4ITNPP2"
PARES_STELLAR = [
    ("XLM/USDC", ("XLM", None), ("USDC", USDC_S), "USDC"),
    ("XLM/EURC", ("XLM", None), ("EURC", EURC_S), "EURC"),
    ("USDC/EURC", ("USDC", USDC_S), ("EURC", EURC_S), "EURC"),
]


def bloque_stellar():
    res, fallos = {}, []
    for nombre, (bc, bi), (cc, ci), unidad in PARES_STELLAR:
        a, c = activo_stellar(bc, bi), activo_stellar(cc, ci)
        q = "&".join([f"selling_{k}={v}" for k, v in a.items()] + [f"buying_{k}={v}" for k, v in c.items()] + ["limit=200"])
        try:
            r = http(f"{HORIZON}/order_book?{q}")
            bids = sorted([(float(x["price"]), float(x["amount"])) for x in r["bids"]], key=lambda x: -x[0])
            asks = sorted([(float(x["price"]), float(x["amount"])) for x in r["asks"]], key=lambda x: x[0])
            m = metricas(bids, asks, f"{unidad} por {bc} (valor en {unidad})")
            m.update({"fuente": HORIZON, "nivel": "P", "leido_utc": ahora(),
                      "metodo": "Horizon /order_book (200 ofertas por lado); profundidad = suma(precio x cantidad base) en %s dentro de ±1 %% y ±2 %% del precio medio" % unidad})
            res[nombre] = m
        except Exception as e:
            fallos.append(f"{nombre}: {e}")
    return res, fallos


# ---------- Stablecoins por red ----------
def bloque_stablecoins():
    redes = ["XRPL", "Stellar", "Solana", "Ethereum"]
    try:
        d = http("https://stablecoins.llama.fi/stablecoins?includePrices=false")["peggedAssets"]
    except Exception as e:
        return None, [f"stablecoins: {e}"]
    out = {}
    for red in redes:
        filas = []
        for a in d:
            cc = a.get("chainCirculating", {}).get(red)
            if cc and cc.get("current"):
                moneda, v = list(cc["current"].items())[0]
                if v:
                    filas.append({"simbolo": a["symbol"], "emitido": round(v), "unidad": moneda.replace("pegged", ""), "mecanismo": a.get("pegMechanism")})
        filas.sort(key=lambda x: -x["emitido"])
        out[red] = {"top": filas[:6], "n_stablecoins": len(filas),
                    "nota": "importes en la moneda de referencia indicada en 'unidad' (USD, EUR, JPY...), sin convertir"}
    return {"datos": out, "nivel": "S", "fuente": "https://stablecoins.llama.fi/stablecoins (DefiLlama, agregador)",
            "metodo": "campo chainCirculating.current por red, top 6 por importe. Profundidad de mercado en Solana y Ethereum no leida: exige APIs de DEX/pools concretas (no hay una sola API publica sin clave comparable al libro del XRPL o de Stellar)",
            "leido_utc": ahora()}, []


def main():
    previo = json.loads(SALIDA.read_text(encoding="utf-8")) if SALIDA.exists() else {}
    fallos = []
    dex, f = bloque_xrpl_dex(); fallos += f
    vel, f = pagos_y_reposo(); fallos += f
    stl, f = bloque_stellar(); fallos += f
    sc, f = bloque_stablecoins(); fallos += f

    def elegir(nuevo, clave):
        if nuevo:
            return nuevo
        viejo = previo.get(clave)
        if viejo:
            fallos.append(f"{clave}: se conserva el dato anterior")
        return viejo
    salida = {
        "_actualizado": ahora(),
        "nivel": "P (libros y nodos directos) con partes S (agregadores)",
        "aviso": "INSTANTANEA, NO TENDENCIA: la profundidad cambia cada segundo y un libro delgado no implica nada por si solo. Solo CLOB (sin AMM/pools). Pares sin ofertas o con emisor no valido quedan fuera y figuran en 'fallos'. Sin recomendaciones.",
        "metodo": "XRPL: book_offers a nodos publicos (s1.ripple.com, xrplcluster). Stellar: Horizon /order_book. Profundidad = valor en la divisa de cotizacion de las ofertas dentro de ±1 % y ±2 % del precio medio ((mejor compra + mejor venta)/2). Velocidad: muestreo de ledgers. Stablecoins: DefiLlama. Historico diario resumido en explorador/profundidad-historial.jsonl.",
        "fallos": fallos,
        "xrpl_dex": elegir(dex, "xrpl_dex"),
        "xrpl_velocidad_reposo": elegir(vel, "xrpl_velocidad_reposo"),
        "stellar_dex": elegir(stl, "stellar_dex"),
        "stablecoins_por_red": elegir(sc, "stablecoins_por_red"),
    }
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    hoy = ahora()[:10]
    resumen = {"fecha": hoy, "hora_utc": ahora()[11:]}
    for k in ("xrpl_dex", "stellar_dex"):
        resumen[k] = {n: {"spread_pct": m.get("spread_pct"), "prof_1pct_c": m.get("profundidad_1pct_compra"), "prof_1pct_v": m.get("profundidad_1pct_venta")}
                      for n, m in (salida[k] or {}).items() if m.get("spread_pct") is not None}
    pp = (salida["xrpl_velocidad_reposo"] or {}).get("pagos_por_dia_estimados") or {}
    resumen["xrpl_pagos_dia"] = pp.get("valor")
    lineas = HIST.read_text(encoding="utf-8").splitlines() if HIST.exists() else []
    lineas = [x for x in lineas if x.strip() and json.loads(x).get("fecha") != hoy]
    lineas.append(json.dumps(resumen, ensure_ascii=False))
    HIST.write_text("\n".join(lineas) + "\n", encoding="utf-8", newline="\n")
    print("OK", len(salida["xrpl_dex"] or {}), "pares XRPL;", len(salida["stellar_dex"] or {}), "pares Stellar; fallos:", fallos)


if __name__ == "__main__":
    main()
