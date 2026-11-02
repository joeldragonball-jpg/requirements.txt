"""Baja cierres DIARIOS (~400 días) de cripto, stablecoins, energía y macro a explorador/precios_historico.json. Sin IA y sin claves.

Lo usa la «Línea de tiempo» del Explorador (botón «Ver reacción»): precio de varios activos alrededor de una noticia.

Fuente: Yahoo Finance, chart API v8 (agregador, NO oficial) -> nivel [S].
- Los futuros continuos (BZ=F, CL=F, NG=F, GC=F) cambian de contrato al vencer: el día del cambio puede haber un salto
  que no es movimiento de mercado. Se marcan como «futuro_continuo» y se listan los días con saltos grandes («saltos»).
- ^TNX es la rentabilidad del bono a 10 años de EE. UU. en % (no un precio).
- Cripto y stablecoins cotizan todos los días; bolsa, futuros e índices no tienen cierre en fines de semana ni festivos.

Uso:  python scripts/actualizar_precios_historico.py
Si un símbolo falla, se conserva la serie que ya había en el JSON y se avisa en «fallos»; el resto sigue.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "precios_historico.json"
URL_YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/{s}?range=2y&interval=1d"
DIAS = 400

# símbolo de Yahoo: (nombre, grupo, unidad, futuro continuo)
ACTIVOS = {
    "BTC-USD": ("Bitcoin", "cripto", "$", False),
    "ETH-USD": ("Ethereum", "cripto", "$", False),
    "XRP-USD": ("XRP", "cripto", "$", False),
    "XLM-USD": ("Stellar (XLM)", "cripto", "$", False),
    "USDT-USD": ("Tether (USDT)", "stable", "$", False),
    "USDC-USD": ("USD Coin (USDC)", "stable", "$", False),
    "RLUSD-USD": ("Ripple USD (RLUSD)", "stable", "$", False),     # opcional: si Yahoo no la tiene, queda en «fallos»
    "BZ=F": ("Brent (futuro)", "energia", "$/barril", True),
    "CL=F": ("WTI (futuro)", "energia", "$/barril", True),
    "NG=F": ("Gas natural Henry Hub (futuro)", "energia", "$/MMBtu", True),
    "^GSPC": ("S&P 500", "macro", "puntos", False),
    "^IXIC": ("Nasdaq Composite", "macro", "puntos", False),
    "^VIX": ("VIX (volatilidad)", "macro", "puntos", False),
    "GC=F": ("Oro (futuro)", "macro", "$/onza", True),
    "^TNX": ("Bono 10 años EE. UU.", "macro", "% rentab.", False),
    "DX-Y.NYB": ("Dólar (DXY)", "macro", "puntos", False),
}
GRUPOS = {"cripto": "Cripto", "stable": "Stablecoins", "energia": "Petróleo y energía", "macro": "Macro y mercados"}
SALTO_FUTURO = 0.07      # cambio diario > 7 % en un futuro continuo: posible cambio de contrato (o movimiento real): revisar


def descargar(url):
    peticion = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(peticion, timeout=40) as r:
        return r.read().decode("utf-8", errors="replace")


def serie(simbolo):
    """Lista [fecha, cierre] de los últimos DIAS días (fecha local del mercado)."""
    d = json.loads(descargar(URL_YAHOO.format(s=urllib.parse.quote(simbolo, safe=""))))["chart"]["result"][0]
    desfase = int(d["meta"].get("gmtoffset") or 0)
    cierres = d["indicators"]["quote"][0]["close"]
    limite = (datetime.now(timezone.utc) - timedelta(days=DIAS)).date().isoformat()
    por_fecha = {}
    for t, c in zip(d.get("timestamp") or [], cierres):
        if c is None:
            continue
        # Yahoo marca la vela diaria al inicio de la sesión (00:00 UTC en cripto, 04:00-05:00 UTC en futuros de NY, 13:30 UTC en
        # bolsa de NY): la fecha UTC es la del día de mercado. «gmtoffset» es el desfase ACTUAL (no el de la fecha, cambia con el
        # horario de verano), así que solo se suma si es positivo (mercados de Asia), donde la vela empieza el día UTC anterior.
        f = datetime.fromtimestamp(t + max(desfase, 0), timezone.utc).date().isoformat()
        if f >= limite:
            por_fecha[f] = round(float(c), 6 if c < 10 else 4 if c < 1000 else 2)    # el último del día gana (Yahoo repite el día en curso)
    if len(por_fecha) < 20:
        raise ValueError(f"solo {len(por_fecha)} cierres")
    return sorted(por_fecha.items())


def saltos(puntos):
    out = []
    for (f0, c0), (f1, c1) in zip(puntos, puntos[1:]):
        if c0 and abs(c1 / c0 - 1) > SALTO_FUTURO:
            out.append([f1, round((c1 / c0 - 1) * 100, 1)])
    return out


def main():
    try:
        previo = json.loads(SALIDA.read_text(encoding="utf-8")).get("series", {})
    except Exception:
        previo = {}
    series, fallos = {}, []
    for simbolo, (nombre, grupo, unidad, futuro) in ACTIVOS.items():
        try:
            puntos = [list(p) for p in serie(simbolo)]
            series[simbolo] = {"nombre": nombre, "grupo": grupo, "unidad": unidad, "futuro_continuo": futuro, "datos": puntos}
            if futuro:
                series[simbolo]["saltos"] = saltos(puntos)
            print(f"OK  {simbolo:10} {len(puntos)} cierres, último {puntos[-1][0]} = {puntos[-1][1]}")
        except Exception as e:                       # tolerar fallos por símbolo
            fallos.append(f"{simbolo}: {type(e).__name__}: {str(e)[:120]}")
            if simbolo in previo:
                series[simbolo] = previo[simbolo]
                series[simbolo]["conservado"] = True
            print(f"FALLO {simbolo}: {e}", file=sys.stderr)
        time.sleep(0.4)
    salida = {
        "leido": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "fuente": "https://finance.yahoo.com/ (chart API v8, cierres diarios)",
        "nivel": "S",
        "grupos": GRUPOS,
        "avisos": [
            "Yahoo Finance es un agregador, no una fuente oficial [S].",
            "Los futuros continuos (Brent, WTI, gas, oro) cambian de contrato al vencer: puede haber saltos que no son movimiento de mercado (ver «saltos»).",
            "Cripto y stablecoins tienen cierre todos los días; bolsa, índices y futuros no cotizan en fines de semana ni festivos.",
            "^TNX es rentabilidad en % (no precio); la fecha es la del mercado local de cada activo.",
        ],
        "series": series,
        "fallos": fallos,
    }
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Guardado {SALIDA} ({SALIDA.stat().st_size // 1024} KB): {len(series)} series, {len(fallos)} fallos")


if __name__ == "__main__":
    main()
