"""Stablecoins del XRPL y Stellar con fuente primaria [P], sin IA.

- XRPL: método `gateway_balances` (obligaciones del emisor) en un servidor público.
- Stellar: Horizon `/assets` (saldos en cuentas + contratos + pools + saldos reclamables).
Direcciones de emisor sacadas de las páginas oficiales (Ripple y Circle); ver FUENTE_DIRECCION.
Guarda la clave `stablecoins_primarias` en explorador/paneles.json (solo esa clave).
Si una lectura falla, conserva el dato anterior de esa moneda y avisa.

Uso:  python scripts/stablecoins_primarias.py
"""
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "paneles.json"
RPC_XRPL = "https://xrplcluster.com"
HORIZON = "https://horizon.stellar.org/assets?asset_code={c}&asset_issuer={i}"

# Fuente de la dirección = página oficial del emisor, no agregador.
MONEDAS = [
    {"id": "RLUSD", "cadena": "XRPL", "emisor": "rMxCKbEDwqr76QuheSUMdEGf4B9xJ8m5De", "divisa": "524C555344000000000000000000000000000000",
     "fuente_direccion": "https://docs.ripple.com/products/stablecoin/overview/token-addresses"},
    {"id": "USDC", "cadena": "XRPL", "emisor": "rGm7WCVp9gb4jZHWTEtGUr4dd74z2XuWhE", "divisa": "5553444300000000000000000000000000000000",
     "fuente_direccion": "https://developers.circle.com/stablecoins/usdc-contract-addresses"},
    {"id": "USDC", "cadena": "Stellar", "emisor": "GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN",
     "fuente_direccion": "https://developers.circle.com/stablecoins/usdc-contract-addresses"},
    {"id": "EURC", "cadena": "Stellar", "emisor": "GDHU6WRG4IEQXM5NZ4BMPKOXHW76MZM4Y2IEMFDVXBSDP6SJY4ITNPP2",
     "fuente_direccion": "https://developers.circle.com/stablecoins/eurc-contract-addresses"},
]
# Contraste manual con la página de transparencia de Ripple (todas las cadenas, no solo XRPL).
CONTRASTE = {"RLUSD": {"fuente": "https://ripple.com/products/stablecoin/transparency/", "fecha": "2026-10-22",
                       "total_todas_cadenas": 2382.8e6, "reservas": 2528.0e6,
                       "nota": "Cifra del emisor para TODAS las cadenas; la del XRPL es solo una parte."}}


def get(url, cuerpo=None):
    cab = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
    p = urllib.request.Request(url, json.dumps(cuerpo).encode() if cuerpo else None, cab)
    with urllib.request.urlopen(p, timeout=40) as r:
        return json.load(r)


def leer_xrpl(m):
    r = get(RPC_XRPL, {"method": "gateway_balances", "params": [{"account": m["emisor"], "ledger_index": "validated"}]})["result"]
    if r.get("status") != "success" or m["divisa"] not in (r.get("obligations") or {}):
        raise ValueError("sin obligaciones en la respuesta")
    return {"cantidad": float(r["obligations"][m["divisa"]]), "ledger": r.get("ledger_index"),
            "metodo": "XRPL gateway_balances (obligaciones del emisor)"}


def leer_stellar(m):
    reg = get(HORIZON.format(c=m["id"], i=m["emisor"]))["_embedded"]["records"]
    if len(reg) != 1:
        raise ValueError("Horizon no devolvió el activo")
    a = reg[0]
    partes = [a["balances"]["authorized"], a.get("claimable_balances_amount", 0), a.get("liquidity_pools_amount", 0), a.get("contracts_amount", 0)]
    return {"cantidad": sum(float(x) for x in partes), "ledger": None,
            "metodo": "Stellar Horizon /assets (cuentas + reclamables + pools + contratos)"}


def main():
    datos = json.loads(SALIDA.read_text(encoding="utf-8"))
    previo = {(x["id"], x["cadena"]): x for x in (datos.get("stablecoins_primarias") or {}).get("monedas", [])}
    ahora = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    monedas, fallos = [], []
    for m in MONEDAS:
        base = {k: m[k] for k in ("id", "cadena", "emisor", "fuente_direccion")}
        try:
            v = (leer_xrpl if m["cadena"] == "XRPL" else leer_stellar)(m)
            monedas.append({**base, **v, "nivel": "P", "leido": ahora})
        except Exception as e:
            fallos.append(f"{m['id']} {m['cadena']}: {e}")
            monedas.append(previo.get((m["id"], m["cadena"]), {**base, "cantidad": None, "nivel": "P"}))
    datos["stablecoins_primarias"] = {
        "leido": ahora, "nivel": "P", "monedas": monedas, "contraste_emisor": CONTRASTE,
        "pendiente_verificar": "USDV, EURCV, YLDS y otras que DefiLlama lista en XRPL/Stellar: dirección oficial del emisor no confirmada [VERIFICAR].",
    }
    SALIDA.write_text(json.dumps(datos, ensure_ascii=False, indent=1).replace("\n", "\r\n"), encoding="utf-8", newline="")
    for x in monedas:
        print(f"{x['id']} {x['cadena']}: {x['cantidad']}")
    for f in fallos:
        print("AVISO:", f)


if __name__ == "__main__":
    main()
