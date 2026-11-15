"""C295 · Lector de validadores/nodos por red (UNL XRPL, Hedera, Solana, Avalanche, IOTA, XDC, Algorand).
Sin IA, sin claves, solo biblioteca estándar. Verificación de certificados activa.
Salida: explorador/cadenas-validadores.json (no se sobrescribe si todo falla) y una línea diaria en
explorador/cadenas-validadores-historial.jsonl. Nivel P = nodo/API directo de la red; S = agregador/tercero.
Uso: python scripts/leer_validadores.py"""
import base64
import json
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "cadenas-validadores.json"
HIST = RAIZ / "explorador" / "cadenas-validadores-historial.jsonl"
UA = {"User-Agent": "cartera-bot", "Content-Type": "application/json"}


def http(url, cuerpo=None, intentos=3, ua=None):
    ult = None
    for i in range(intentos):
        try:
            data = json.dumps(cuerpo).encode() if cuerpo is not None else None
            req = urllib.request.Request(url, data=data, headers=dict(UA, **({"User-Agent": ua} if ua else {})))
            return json.load(urllib.request.urlopen(req, timeout=40))
        except Exception as e:
            ult = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{type(ult).__name__}: {ult}")


def nakamoto(stakes, frac=1 / 3):
    """Nº mínimo de nodos (de mayor a menor stake) que acumulan más de `frac` del total."""
    tot = sum(stakes)
    if tot <= 0:
        return None
    acc = 0
    for n, s in enumerate(sorted(stakes, reverse=True), 1):
        acc += s
        if acc > tot * frac:
            return n
    return len(stakes)


def xrpl():
    d = http("https://vl.ripple.com")
    blob = json.loads(base64.b64decode(d["blob"]))
    return {"red": "XRPL", "nivel": "P", "fuente": "https://vl.ripple.com", "validadores_unl": len(blob["validators"]),
            "secuencia_lista": blob.get("sequence"), "caduca": blob.get("expiration"),
            "nota": "Lista publicada por Ripple (parte interesada): es la UNL por defecto, no toda la red."}


def hedera():
    url = "https://mainnet-public.mirrornode.hedera.com/api/v1/network/nodes?limit=100"
    nodos = []
    while url and len(nodos) < 500:
        d = http(url)
        nodos += d.get("nodes", [])
        nxt = d.get("links", {}).get("next")
        url = "https://mainnet-public.mirrornode.hedera.com" + nxt if nxt else None
    st = [int(n.get("stake") or 0) for n in nodos]
    return {"red": "Hedera", "nivel": "P", "fuente": "mirror node público de Hedera", "nodos": len(nodos),
            "nakamoto_1_3": nakamoto(st), "nota": "Consejo de gobierno de nodos; el número es de nodos del libro de direcciones."}


def solana():
    d = http("https://api.mainnet-beta.solana.com", {"jsonrpc": "2.0", "id": 1, "method": "getVoteAccounts"})["result"]
    act, dec = d["current"], d["delinquent"]
    st = [int(v["activatedStake"]) for v in act]
    tot = sum(st)
    n = nakamoto(st)
    return {"red": "Solana", "nivel": "P", "fuente": "RPC público api.mainnet-beta.solana.com", "validadores_activos": len(act),
            "delinquentes": len(dec), "stake_total_sol": round(tot / 1e9), "nakamoto_1_3": n,
            "nota": "Coeficiente = nº mínimo de validadores que acumulan más de 1/3 del stake (por identidad de voto, no por operador)."}


def avalanche():
    d = http("https://api.avax.network/ext/bc/P", {"jsonrpc": "2.0", "id": 1, "method": "platform.getCurrentValidators", "params": {}})["result"]
    v = d["validators"]
    st = [int(x.get("weight") or x.get("stakeAmount") or 0) for x in v]
    return {"red": "Avalanche", "nivel": "P", "fuente": "API pública api.avax.network (P-Chain)", "validadores": len(v),
            "nakamoto_1_3": nakamoto(st), "nota": "Validadores de la red primaria; pesos = campo weight de la API [VERIFICAR si incluye delegaciones]."}


def iota():
    d = http("https://api.mainnet.iota.cafe", {"jsonrpc": "2.0", "id": 1, "method": "iotax_getLatestIotaSystemState", "params": []})["result"]
    v = d.get("activeValidators", [])
    st = [int(x.get("votingPower") or 0) for x in v]
    return {"red": "IOTA", "nivel": "P", "fuente": "RPC público api.mainnet.iota.cafe", "validadores_activos": len(v),
            "epoca": d.get("epoch"), "nakamoto_1_3": nakamoto(st), "nota": "Poder de voto por validador del estado del sistema."}


def xdc():
    d = http("https://rpc.xinfin.network", {"jsonrpc": "2.0", "id": 1, "method": "XDPoS_getMasternodesByNumber", "params": ["latest"]}, ua="Mozilla/5.0 (compatible; lector-publico)")["result"]
    return {"red": "XDC", "nivel": "P", "fuente": "RPC público rpc.xinfin.network", "masternodes": len(d.get("Masternodes", [])),
            "standbynodes": len(d.get("Standbynodes", [])), "penalizados": len(d.get("Penalty", [])),
            "nota": "Masternodes de la época actual (consenso XDPoS)."}


def algorand():
    d = http("https://mainnet-api.algonode.cloud/v2/status")
    return {"red": "Algorand", "nivel": "S", "fuente": "nodo de tercero (Nodely/Algonode)",
            "ultima_ronda": d.get("last-round"), "validadores": None,
            "nota": "No hay API pública simple del nº de proponentes; solo se confirma que la red avanza. [VERIFICAR] recuento de cuentas con voto."}


LECTORES = [xrpl, hedera, solana, avalanche, iota, xdc, algorand]


def main():
    ahora = datetime.now(timezone.utc)
    redes, fallos = [], []
    for f in LECTORES:
        try:
            r = f()
            r["leido_utc"] = ahora.strftime("%Y-%m-%d %H:%M UTC")
            redes.append(r)
        except Exception as e:
            fallos.append({"red": f.__name__, "error": str(e)[:200]})
            print(f"  FALLO {f.__name__}: {e}", file=sys.stderr)
    if not redes:
        print("Todo falló: no se sobrescribe el JSON.")
        return 1
    previo = {}
    if SALIDA.exists():  # conservar la última lectura buena de redes que fallen hoy
        try:
            previo = {r["red"]: r for r in json.loads(SALIDA.read_text(encoding="utf-8")).get("redes", [])}
        except Exception:
            pass
    nombres = {r["red"] for r in redes}
    for red in previo.values():
        if red["red"] not in nombres:
            red["obsoleto"] = True
            redes.append(red)
    out = {"generado_utc": ahora.strftime("%Y-%m-%d %H:%M UTC"),
           "metodo": "Consultas directas a nodos/APIs públicos sin clave; reintentos x3. Nivel P = nodo directo de la red; S = tercero.",
           "avisos": ["Cifras de decentralización por identidad de nodo, no por operador real: un operador puede controlar varios [VERIFICAR].",
                      "XRPL: la UNL la publica Ripple (parte interesada)."],
           "fallos": fallos, "redes": redes}
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    dia = ahora.strftime("%Y-%m-%d")
    lineas = HIST.read_text(encoding="utf-8").splitlines() if HIST.exists() else []
    lineas = [l for l in lineas if not l.startswith('{"fecha": "%s"' % dia)]
    resumen = {r["red"]: {k: v for k, v in r.items() if k in ("validadores_unl", "nodos", "validadores_activos", "delinquentes",
               "validadores", "masternodes", "nakamoto_1_3")} for r in redes if not r.get("obsoleto")}
    lineas.append(json.dumps({"fecha": dia, "redes": resumen}, ensure_ascii=False))
    HIST.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(f"OK: {len(redes)} redes, {len(fallos)} fallos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
