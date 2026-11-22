#!/usr/bin/env python3
"""Fondos y bolsa · lee índices bursátiles con sus rentabilidades, salidas a bolsa (OPV) y altas recientes del S&P 500.

Sin IA y sin claves: solo biblioteca estándar. Escribe explorador/bolsas.json.
Fuentes (todas nivel S, agregador o prensa; ninguna es dato oficial del mercado):
  · Yahoo Finance (gráficos diarios de 1 año) → 1 día, 1 semana, 1 mes, 3 meses, año en curso y 12 meses, en moneda local.
  · Renaissance Capital (IPO Center) → OPV recientes y próximas. La fecha de las próximas es de pago: no se copia.
  · Wikipedia (List of S&P 500 companies) → altas recientes por «fecha de alta». Las bajas NO están disponibles en una fuente abierta fiable.
Si una fuente falla se conserva el valor anterior de ese bloque y se anota en «fallos».
"""
import json, re, sys, time, urllib.request, datetime as dt
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "bolsas.json"
UA = "Mozilla/5.0 (compatible; cartera-personal/1.0; lectura diaria de datos publicos)"

# (símbolo de Yahoo, nombre, grupo, moneda)
INDICES = [
    ("^990100-USD-STRD", "MSCI World", "Mundo", "USD"),
    ("^892400-USD-STRD", "MSCI ACWI (todo el mundo)", "Mundo", "USD"),
    ("EEM", "MSCI Emerging Markets (ETF EEM)", "Mundo", "USD"),
    ("^GSPC", "S&P 500", "EE. UU.", "USD"),
    ("^NDX", "Nasdaq-100", "EE. UU.", "USD"),
    ("^IXIC", "Nasdaq Composite", "EE. UU.", "USD"),
    ("^DJI", "Dow Jones Industrial", "EE. UU.", "USD"),
    ("^RUT", "Russell 2000 (pequeñas)", "EE. UU.", "USD"),
    ("^MID", "S&P 400 (medianas)", "EE. UU.", "USD"),
    ("^SOX", "Semiconductores (PHLX)", "EE. UU.", "USD"),
    ("^STOXX", "STOXX Europe 600", "Europa", "EUR"),
    ("^STOXX50E", "Euro Stoxx 50", "Europa", "EUR"),
    ("^IBEX", "Ibex 35", "Europa", "EUR"),
    ("^GDAXI", "DAX 40", "Europa", "EUR"),
    ("^FCHI", "CAC 40", "Europa", "EUR"),
    ("^FTSE", "FTSE 100", "Europa", "GBP"),
    ("^N225", "Nikkei 225", "Asia-Pacífico", "JPY"),
    ("^KS11", "Kospi", "Asia-Pacífico", "KRW"),
    ("^HSI", "Hang Seng", "Asia-Pacífico", "HKD"),
    ("000001.SS", "Shanghái Composite", "Asia-Pacífico", "CNY"),
    ("^NSEI", "Nifty 50", "Asia-Pacífico", "INR"),
    ("^TWII", "Taiwán (TAIEX)", "Asia-Pacífico", "TWD"),
    ("^AXJO", "S&P/ASX 200", "Asia-Pacífico", "AUD"),
    ("^BVSP", "Bovespa", "Latinoamérica", "BRL"),
    ("^VIX", "VIX (volatilidad esperada del S&P 500)", "Riesgo", "USD"),
]


def get(url, intentos=2):
    for i in range(intentos):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30).read().decode("utf-8", "replace")
        except Exception as e:      # noqa: BLE001
            ultimo = e
            time.sleep(1.5)
    raise ultimo


def pct(a, b):
    return None if (a is None or b in (None, 0)) else round((a / b - 1) * 100, 2)


def leer_indice(simbolo):
    url = "https://query1.finance.yahoo.com/v8/finance/chart/" + simbolo.replace("^", "%5E") + "?range=1y&interval=1d"
    r = json.loads(get(url))["chart"]["result"][0]
    ts = r["timestamp"]
    cl = r["indicators"]["quote"][0]["close"]
    par = [(t, c) for t, c in zip(ts, cl) if c is not None]
    if len(par) < 30:
        raise ValueError("serie demasiado corta (%d puntos)" % len(par))
    par = [(t, c) for t, c in par if dt.datetime.fromtimestamp(t, dt.timezone.utc).weekday() < 5]   # MSCI repite el último cierre en domingo: se descarta
    fechas = [dt.datetime.fromtimestamp(t, dt.timezone.utc).date() for t, _ in par]
    v = [c for _, c in par]
    ult = v[-1]
    anio = fechas[-1].year
    base_ytd = next((c for f, c in reversed(list(zip(fechas, v))) if f.year < anio), None)
    return {
        "valor": round(ult, 2), "fecha": fechas[-1].isoformat(),
        "c1d": pct(ult, v[-2]), "c1s": pct(ult, v[-6]) if len(v) > 5 else None,
        "c1m": pct(ult, v[-22]) if len(v) > 21 else None, "c3m": pct(ult, v[-64]) if len(v) > 63 else None,
        "ytd": pct(ult, base_ytd), "c1a": pct(ult, v[0]) if len(v) > 240 else None,
        "min52": round(min(v), 2), "max52": round(max(v), 2),
        "pos52": round((ult - min(v)) / (max(v) - min(v)) * 100) if max(v) > min(v) else None,
        "desde_max": pct(ult, max(v)),
        "serie": [round(x, 2) for x in v[-60:]],
    }


def limpia(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).replace("&amp;", "&").replace("&apos;", "'").strip()


def filas_tabla(html, caption):
    """Devuelve las filas (lista de celdas con texto) de la tabla cuyo <caption> contiene `caption`."""
    for m in re.finditer(r"<table[^>]*>(.*?)</table>", html, re.S):
        t = m.group(1)
        c = re.search(r"<caption[^>]*>(.*?)</caption>", t, re.S)
        if c and caption.lower() in limpia(c.group(1)).lower():
            return [[limpia(x) for x in re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)] for r in re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S) if "<td" in r]
    return []


def num(s):
    m = re.search(r"-?[\d,]+\.?\d*", s or "")
    return float(m.group(0).replace(",", "")) if m else None


def leer_ipos():
    base = "https://www.renaissancecapital.com/IPO-Center/"
    out = {"fuente": base, "nivel": "S", "recientes": [], "proximas": []}
    ph = get(base + "Pricings")
    for c in filas_tabla(ph, "Recently Priced"):
        # ticker, empresa, ticker, fecha, tamaño M$, precio actual, cambio hoy, retorno desde la OPV
        if len(c) >= 8:
            f = re.match(r"(\d+)/(\d+)/(\d+)", c[3])
            fecha = "20%s-%02d-%02d" % (f.group(3), int(f.group(1)), int(f.group(2))) if f else c[3]
            out["recientes"].append({"ticker": c[0], "empresa": c[1], "fecha": fecha, "tamano_musd": num(c[4]), "precio": num(c[5]), "retorno_pct": num(c[7])})
    time.sleep(1)
    cal = get(base + "Calendar")
    for c in filas_tabla(cal, "Upcoming IPOs"):
        # ticker, empresa, ticker, (fecha de pago), acciones M, rango de precio, importe M$, banco colocador
        if len(c) >= 8:
            out["proximas"].append({"ticker": c[0], "empresa": c[1], "rango": c[5], "importe_musd": num(c[6]), "colocador": c[7]})
    return out


def leer_sp500_altas():
    t = get("https://en.wikipedia.org/w/index.php?title=List_of_S%26P_500_companies&action=raw")
    filas = []
    for r in re.split(r"\n\|-\n", t):
        m = re.search(r"\|\|\s*(\d{4}-\d{2}-\d{2})", r)
        s = re.search(r"\{\{\w+Symbol\|([\w.\-]+)\}\}", r)
        n = re.findall(r"\[\[([^\]|]+)", r)
        if m and s and n:
            filas.append({"ticker": s.group(1), "empresa": n[0], "fecha_alta": m.group(1)})
    filas.sort(key=lambda x: x["fecha_alta"], reverse=True)
    return filas[:12]


def main():
    previo = {}
    if SALIDA.is_file():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        except ValueError:
            previo = {}
    fallos = []
    ahora = dt.datetime.now(dt.timezone.utc)
    prev_idx = {i["simbolo"]: i for i in previo.get("indices", [])}
    indices = []
    for sim, nombre, grupo, mon in INDICES:
        try:
            d = leer_indice(sim)
            indices.append({"simbolo": sim, "nombre": nombre, "grupo": grupo, "moneda": mon, **d})
        except Exception as e:      # noqa: BLE001
            fallos.append("%s: %s" % (sim, e))
            if sim in prev_idx:
                indices.append(prev_idx[sim])
        time.sleep(0.3)
    try:
        ipos = leer_ipos()
    except Exception as e:      # noqa: BLE001
        fallos.append("OPV: %s" % e)
        ipos = previo.get("ipos", {})
    try:
        altas = leer_sp500_altas()
    except Exception as e:      # noqa: BLE001
        fallos.append("S&P 500 altas: %s" % e)
        altas = previo.get("sp500_altas", [])
    out = {
        "_actualizado": ahora.date().isoformat(), "leido": ahora.strftime("%Y-%m-%d %H:%M UTC"), "nivel": "S",
        "fuente": "Yahoo Finance (índices), Renaissance Capital (OPV), Wikipedia (altas del S&P 500)",
        "aviso": "Agregadores y prensa, no datos oficiales de mercado. Rentabilidades en moneda local del índice (sin dividendos, salvo en ETF). Informativo, no es recomendación.",
        "indices": indices, "ipos": ipos, "sp500_altas": altas,
        "notas": ["Las bajas del S&P 500 y los cambios del MSCI o del Nasdaq-100 no están en una fuente abierta fiable: pendiente.",
                  "MSCI Emerging Markets se sigue con el ETF EEM porque Yahoo no ofrece la serie del índice."],
        "fallos": fallos,
    }
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("bolsas.json: %d índices, %d OPV recientes, %d próximas, %d altas S&P 500, %d fallos" % (len(indices), len(ipos.get("recientes", [])), len(ipos.get("proximas", [])), len(altas), len(fallos)))
    for f in fallos:
        print("  fallo:", f)
    return 1 if len(fallos) > 6 else 0


if __name__ == "__main__":
    sys.exit(main())
