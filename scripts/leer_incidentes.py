"""C296 · Lector de incidentes de seguridad por red (DefiLlama api.llama.fi/hacks), últimos 12 meses.
Sin IA, sin claves, solo biblioteca estándar. Nivel S (agregador de tercero; cifras de daño aproximadas).
Separa incidentes de puentes (bridgeHack) y de capa base/protocolos. No sobrescribe el JSON si la descarga falla.
Uso: python scripts/leer_incidentes.py"""
import json
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "cadenas-incidentes.json"
URL = "https://api.llama.fi/hacks"
# id de cadenas.json -> nombres con que DefiLlama etiqueta la red (incluye duplicados: «Ripple»/«XRPL», «BSC»/«Binance»…)
ALIAS = {
    "xrpl": ["XRPL", "Ripple", "XRP", "XRP Ledger"], "stellar": ["Stellar"], "hedera": ["Hedera"],
    "ethereum": ["Ethereum"], "solana": ["Solana"], "bnb": ["BSC", "Binance", "BNB", "BNB Chain", "Binance Smart Chain"],
    "avalanche": ["Avalanche"], "polygon": ["Polygon"], "algorand": ["Algorand"], "xdc": ["XDC", "XinFin", "XDC Network"],
    "iota": ["IOTA", "Iota"], "plume": ["Plume"], "canton": ["Canton"],
}
INVERSO = {a.lower(): k for k, v in ALIAS.items() for a in v}


def descargar():
    ult = None
    for i in range(3):
        try:
            req = urllib.request.Request(URL, headers={"User-Agent": "cartera-bot"})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:
            ult = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{type(ult).__name__}: {ult}")


def main():
    ahora = datetime.now(timezone.utc)
    try:
        datos = descargar()
        assert isinstance(datos, list) and datos
    except Exception as e:
        print(f"Fallo de descarga, no se sobrescribe: {e}", file=sys.stderr)
        return 1
    corte = (ahora - timedelta(days=365)).timestamp()
    redes = {k: {"base": [], "puentes": []} for k in ALIAS}
    sin_mapear = 0
    for h in datos:
        if not h.get("date") or h["date"] < corte:
            continue
        cadenas = h.get("chain") or []
        if isinstance(cadenas, str):
            cadenas = [cadenas]
        ids = sorted({INVERSO[c.lower()] for c in cadenas if isinstance(c, str) and c.lower() in INVERSO})
        if not ids:
            sin_mapear += 1
            continue
        item = {"fecha": datetime.fromtimestamp(h["date"], timezone.utc).strftime("%Y-%m-%d"), "nombre": h.get("name"),
                "importe_usd": h.get("amount"), "tecnica": h.get("technique") or h.get("classification"),
                "recuperado_usd": h.get("returnedFunds"), "otras_redes": [c for c in cadenas if c.lower() not in INVERSO] + [i for i in ids[1:]] if len(ids) > 1 else []}
        for i in ids:  # un incidente multi-red cuenta en cada red afectada: no sumar entre redes
            redes[i]["puentes" if h.get("bridgeHack") else "base"].append(item)
    res = {}
    for k, v in redes.items():
        r = {}
        for tipo in ("base", "puentes"):
            L = sorted(v[tipo], key=lambda x: x["fecha"], reverse=True)
            r[tipo] = {"n": len(L), "importe_usd": sum(x["importe_usd"] or 0 for x in L), "ultimo": L[0]["fecha"] if L else None,
                       "casos": L[:10]}
        res[k] = r
    out = {"generado_utc": ahora.strftime("%Y-%m-%d %H:%M UTC"), "nivel": "S",
           "ventana": f"{(ahora - timedelta(days=365)).strftime('%Y-%m-%d')} a {ahora.strftime('%Y-%m-%d')}",
           "fuente": URL, "total_incidentes_en_fuente": len(datos), "incidentes_sin_red_mapeada": sin_mapear,
           "metodo": "Descarga única del listado de DefiLlama, filtro por fecha (365 días), agrupación por red con diccionario de alias y separación por el campo bridgeHack.",
           "avisos": ["Atribución doble: un hack de puente suele figurar en las dos redes que conecta; no sumar importes entre redes.",
                      "Los nombres de red se duplican en la fuente (XRPL/Ripple, BSC/Binance/BNB); aquí se unifican por diccionario, [VERIFICAR] omisiones.",
                      "Importes y fechas son los que declara DefiLlama (agregador); 0 incidentes no prueba seguridad, solo que no constan.",
                      "Muchos incidentes son de aplicaciones sobre la red (DeFi), no fallos de la capa base."],
           "redes": res}
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OK:", {k: (v["base"]["n"], v["puentes"]["n"]) for k, v in res.items()})
    return 0


if __name__ == "__main__":
    sys.exit(main())
