"""Precios casi en vivo para la Órbita y el móvil (C142). Sin IA y sin claves.

Qué hace: baja en una sola pasada (cada hora, lo lanza .github/workflows/precios.yml) los números que se mueven en el día
y los guarda en un archivo pequeño, `precios_vivos.json`, en la rama `datos` (la misma de las noticias; así no ensucia `main`).
La Órbita lo lee al abrirse y repinta las cifras sin esperar a la foto diaria de `explorador/paneles.json`.

Fuentes abiertas (todas [S], agregadores):
- CoinGecko: XRP, XLM, BTC y ETH en dólares, capitalización y cambio de 24 h.
- DefiLlama: precio de mercado de cada stablecoin (para ver si pierde la paridad con el dólar, p. ej. USD1).
- alternative.me: índice de miedo y codicia cripto (Fear & Greed).
- Yahoo Finance: Brent, WTI, gas, oro, VIX, S&P 500 y sus futuros, Nasdaq, SOXX, rendimiento del bono de EE. UU. a 10 años,
  más la tabla de seguimiento (watchlist.toml + cripto y ETF).

Uso:  python scripts/precios_vivos.py [carpeta_de_salida]      (por defecto: explorador/)
      python scripts/precios_vivos.py --r00 apertura|cierre    (lo lanza la sesión R00: guarda el primer o el último precio del día
                                                                en explorador/precios_r00.json, que la Órbita enseña como «desde la apertura»)
Si una fuente falla se avisa en `fallos` y se sigue con las demás; si falla todo, sale con 1 sin tocar el archivo.
"""
import json
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import actualizar_paneles as ap  # noqa: E402
import yahoo_diario  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
URL_COINGECKO = ("https://api.coingecko.com/api/v3/simple/price?ids=ripple,stellar,bitcoin,ethereum&vs_currencies=usd"
                 "&include_market_cap=true&include_24hr_change=true")
URL_MIEDO = "https://api.alternative.me/fng/?limit=2"
CRIPTO = (("ripple", "XRP", "XRP"), ("stellar", "XLM", "Stellar Lumens"), ("bitcoin", "BTC", "Bitcoin"), ("ethereum", "ETH", "Ether"))
# (símbolo de Yahoo, clave corta, nombre, unidad)
MERCADO = (("BZ=F", "brent", "Petróleo Brent (futuro)", "$/barril"), ("CL=F", "wti", "Petróleo WTI (futuro)", "$/barril"),
           ("NG=F", "gas", "Gas natural EE. UU. (futuro)", "$/MMBtu"), ("GC=F", "oro", "Oro (futuro)", "$/onza"),
           ("^VIX", "vix", "VIX (miedo en la bolsa)", "puntos"), ("^GSPC", "sp500", "S&P 500", "puntos"),
           ("ES=F", "sp500_fut", "Futuros S&P 500", "puntos"), ("^IXIC", "nasdaq", "Nasdaq Composite", "puntos"),
           ("SOXX", "soxx", "Chips (fondo SOXX)", "$"), ("^TNX", "us10y", "Bono de EE. UU. a 10 años (rendimiento)", "%"))
# cripto y ETF extra que se añaden a la tabla de seguimiento además de watchlist.toml
EXTRA = (("XRP-USD", "XRP", "XRP", "Cripto (lo que tengo)"), ("XLM-USD", "XLM", "Stellar (XLM)", "Cripto (lo que tengo)"),
         ("BTC-USD", "BTC", "Bitcoin", "Cripto (referencia)"), ("ETH-USD", "ETH", "Ether", "Cripto (referencia)"),
         ("IBIT", "IBIT", "iShares Bitcoin Trust ETF", "ETF cripto"), ("ETHA", "ETHA", "iShares Ethereum Trust ETF", "ETF cripto"),
         ("COIN", "COIN", "Coinbase", "Empresas cripto"), ("MSTR", "MSTR", "Strategy (antes MicroStrategy)", "Empresas cripto"))


def _json(url):
    return json.loads(ap.descargar(url))


def leer_cripto():
    d = _json(URL_COINGECKO)
    return [{"simbolo": s, "nombre": n, "precio": d[k]["usd"], "capitalizacion": d[k].get("usd_market_cap"),
             "cambio_24h": d[k].get("usd_24h_change")} for k, s, n in CRIPTO]


def leer_stablecoins():
    """Precio de mercado de las 25 mayores stablecoins y lista de las que han perdido la paridad con el dólar."""
    a = _json(ap.URL_LLAMA)["peggedAssets"]
    filas = []
    for x in a:
        peg = x.get("pegType", "")
        circ = ap.valor(x.get("circulating"), peg if peg in (x.get("circulating") or {}) else next(iter(x.get("circulating") or {"": 0}), ""))
        if not circ or x.get("price") is None:
            continue
        precio = float(x["price"])
        usd = circ if peg == "peggedUSD" else circ * precio
        filas.append({"simbolo": x.get("symbol"), "nombre": x.get("name"), "ligada": peg.replace("pegged", ""), "precio": round(precio, 4),
                      "usd": usd, "desvio_pct": round((precio - 1) * 100, 2) if peg == "peggedUSD" else None})
    filas.sort(key=lambda f: -f["usd"])
    top = filas[:25]
    # despegadas: más de 20 millones en circulación y más de un 2 % lejos de 1 $ (con menos, es ruido de monedas pequeñas)
    desp = [f for f in filas if f["desvio_pct"] is not None and f["usd"] >= 20e6 and abs(f["desvio_pct"]) > 2]
    return {"total": sum(f["usd"] for f in filas), "top": top, "despegadas": desp}


def leer_miedo():
    d = _json(URL_MIEDO)["data"]
    hoy, ayer = d[0], d[1] if len(d) > 1 else None
    return {"valor": int(hoy["value"]), "clasificacion": hoy.get("value_classification"), "anterior": int(ayer["value"]) if ayer else None,
            "fecha": datetime.fromtimestamp(int(hoy["timestamp"]), timezone.utc).strftime("%Y-%m-%d")}


def leer_mercado(fallos):
    salida = {}
    for simbolo, clave, nombre, unidad in MERCADO:
        try:
            d = _json(ap.URL_YAHOO.format(s=urllib.parse.quote(simbolo)))["chart"]["result"][0]
            pares = yahoo_diario.cierres(d)
            if len(pares) < 2:
                raise ValueError("menos de 2 cierres")
            (f0, c0), (f1, c1) = pares[-2], pares[-1]
            salida[clave] = {"simbolo": simbolo, "nombre": nombre, "unidad": unidad, "valor": round(c1, 3), "fecha": f1,
                             "cambio_1d": round((c1 / c0 - 1) * 100, 2) if clave != "us10y" else round((c1 - c0) * 100, 1)}   # el bono: puntos básicos
        except Exception as e:
            fallos.append(f"{clave}: {type(e).__name__}: {e}")
    return salida


def leer_seguimiento(fallos):
    """Tabla de seguimiento: watchlist.toml + cripto y ETF cripto. Reutiliza leer_watchlist (precio, 1 d, 1 sem., 3 m, año y dividendo)."""
    import tomllib
    with open(RAIZ / "watchlist.toml", "rb") as fh:
        lista = tomllib.load(fh).get("valores", [])
    lista = [dict(v) for v in lista] + [{"ticker": t, "yahoo": y, "nombre": n, "categoria": c} for y, t, n, c in EXTRA]
    r = ap.leer_watchlist(lista)
    fallos += r.get("fallos", [])
    return r["valores"]


def guardar_r00(salida, momento):
    """Guarda una foto corta (cripto y mercado) como apertura o cierre de HOY (hora de Madrid) en explorador/precios_r00.json; conserva 45 días."""
    try:
        from zoneinfo import ZoneInfo
        hoy = datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d")
    except Exception:
        # Windows sin base de zonas horarias (sin tzdata): CET/CEST a mano (último domingo de marzo a último de octubre, 01:00 UTC).
        from datetime import timedelta, timezone as _tz
        u = datetime.now(_tz.utc)
        def _ult_dom(m):
            d = datetime(u.year, m, 31, 1, tzinfo=_tz.utc)
            return d - timedelta(days=(d.weekday() + 1) % 7)
        verano = _ult_dom(3) <= u < _ult_dom(10)
        hoy = (u + timedelta(hours=2 if verano else 1)).strftime("%Y-%m-%d")
    ruta = RAIZ / "explorador" / "precios_r00.json"
    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except Exception:
        datos = {}
    dias = datos.setdefault("dias", {})
    dias.setdefault(hoy, {})[momento] = {
        "leido": salida["leido"],
        "cripto": {c["simbolo"]: c["precio"] for c in salida.get("cripto", [])},
        "mercado": {k: v["valor"] for k, v in salida.get("mercado", {}).items()},
        "miedo_cripto": (salida.get("miedo_cripto") or {}).get("valor")}
    for f in sorted(dias)[:-45]:
        del dias[f]
    datos["nota"] = "Primer (apertura) y último (cierre) precio del día que fija la sesión R00; fuentes [S] (CoinGecko y Yahoo). Hora de Madrid."
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"R00 {momento} {hoy}: guardado en {ruta.name}")


def main():
    args = sys.argv[1:]
    momento = None
    if "--r00" in args:
        i = args.index("--r00")
        momento = args[i + 1] if i + 1 < len(args) else ""
        if momento not in ("apertura", "cierre"):
            sys.exit("Uso: --r00 apertura|cierre")
        del args[i:i + 2]
    destino = Path(args[0]) if args else RAIZ / "explorador"
    destino.mkdir(parents=True, exist_ok=True)
    fallos = []
    salida = {"leido": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "nivel": "S"}
    for clave, f in (("cripto", leer_cripto), ("stablecoins", leer_stablecoins), ("miedo_cripto", leer_miedo)):
        try:
            salida[clave] = f()
        except Exception as e:
            fallos.append(f"{clave}: {type(e).__name__}: {e}")
    salida["mercado"] = leer_mercado(fallos)
    try:
        salida["seguimiento"] = leer_seguimiento(fallos)
    except Exception as e:
        fallos.append(f"seguimiento: {type(e).__name__}: {e}")
    salida["fallos"] = fallos
    if not (salida.get("cripto") or salida.get("mercado") or salida.get("seguimiento")):
        print("Ninguna fuente respondió: no se escribe nada.", file=sys.stderr)
        sys.exit(1)
    ruta = destino / "precios_vivos.json"
    ruta.write_text(json.dumps(salida, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    x = {c["simbolo"]: c for c in salida.get("cripto", [])}
    print(f"{ruta.name}: {ruta.stat().st_size // 1024} KB · XRP {x.get('XRP', {}).get('precio')} $ · "
          f"{len(salida.get('seguimiento', []))} valores · {len(salida['mercado'])} cifras de mercado · "
          f"{len((salida.get('stablecoins') or {}).get('despegadas', []))} stablecoins despegadas · fallos: {len(fallos)}")
    for f in fallos:
        print("  ⚠", f)
    if momento:
        guardar_r00(salida, momento)


if __name__ == "__main__":
    t0 = time.monotonic()
    main()
    print(f"{time.monotonic() - t0:.0f} s")
