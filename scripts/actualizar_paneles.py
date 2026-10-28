"""Baja los datos de los paneles del Explorador a explorador/paneles.json. Sin IA y sin claves.

Fuentes abiertas:
- Tesoro de EE. UU. (TIC), Tabla 5: mayores tenedores extranjeros de bonos del Tesoro. Fuente primaria [P].
- DefiLlama (stablecoins.llama.fi): circulación de stablecoins por emisor y por cadena. Agregador [S].

Uso:  python scripts/actualizar_paneles.py
Si una fuente falla, se conserva lo que ya había de esa fuente en paneles.json y se avisa.
"""
import csv
import gzip
import io
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "paneles.json"
URL_TIC = "https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.txt"
URL_LLAMA = "https://stablecoins.llama.fi/stablecoins?includePrices=true"
URL_UST = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv"
URL_JGB = "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv"
URL_BCE = "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y?lastNObservations=3&format=jsondata"
URL_BOE = "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom={d1}&Dateto={d2}&SeriesCodes=IUDMNZC&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N"
URL_BCE_YC = "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_{p}?lastNObservations={n}&format=jsondata"
URL_BCE_IRS = "https://data-api.ecb.europa.eu/service/data/IRS/M.{c}.L.L40.CI.0000.EUR.N.Z?lastNObservations=3&format=jsondata"
URL_BDE = "https://app.bde.es/bierest/resources/srdatosapp/listaSeries?idioma=es&series={s}&rango=3M"
BDE_SERIES = {"D_DTES00B7": "3M", "D_DTES00U7": "1A", "D_G0B1F0ZN": "3A", "D_G0B1F0ZO": "5A", "D_G0B1F0ZP": "10A", "D_G0B1F0ZQ": "15A"}
BOE_PAR = {"IUDSNPY": "5A", "IUDMNPY": "10A", "IUDLNPY": "20A"}
BONOS_MANUAL = Path(__file__).resolve().parent.parent / "explorador" / "bonos-manual.json"
FMI = Path(__file__).resolve().parent.parent / "explorador" / "deuda-fmi.json"
NOMBRES_TIC = {
    "Japan": "Japón", "United Kingdom": "Reino Unido", "China, Mainland": "China continental", "Belgium": "Bélgica",
    "Canada": "Canadá", "Cayman Islands": "Islas Caimán", "Luxembourg": "Luxemburgo", "France": "Francia",
    "Ireland": "Irlanda", "Taiwan": "Taiwán", "Switzerland": "Suiza", "Singapore": "Singapur", "Hong Kong": "Hong Kong",
    "India": "India", "Norway": "Noruega", "Brazil": "Brasil", "Saudi Arabia": "Arabia Saudí",
    "Korea, South": "Corea del Sur", "United Arab Emirates": "Emiratos Árabes Unidos", "Bermuda": "Bermudas",
    "Germany": "Alemania", "Italy": "Italia", "Netherlands": "Países Bajos", "Mexico": "México", "Israel": "Israel",
    "Spain": "España", "Australia": "Australia", "Thailand": "Tailandia", "Turkey": "Turquía", "Russia": "Rusia",
}


def descargar(url):
    peticion = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(peticion, timeout=40) as r:
        datos = r.read()
    if datos[:2] == b"\x1f\x8b":            # el Banco de España responde comprimido aunque no se le pida
        datos = gzip.decompress(datos)
    return datos.decode("utf-8", errors="replace")


def leer_tic():
    texto = descargar(URL_TIC).replace("\r", "")
    filas = [f.split("\t") for f in texto.split("\n")]
    cab = next(f for f in filas if f and f[0].strip() == "Country")
    meses = [m.strip() for m in cab[1:] if m.strip()]          # del más reciente al más antiguo
    paises, resumen = [], {}
    for f in filas[filas.index(cab) + 1:]:
        nombre = f[0].strip()
        if not nombre or nombre.startswith("Notes"):
            if nombre.startswith("Notes"):
                break
            continue
        try:
            serie = [float(x) for x in f[1:1 + len(meses)]]
        except ValueError:
            continue
        if nombre in ("Grand Total", "All Other") or nombre.startswith("Of Which"):
            resumen[nombre] = serie
        else:
            paises.append({"clave": nombre, "nombre": NOMBRES_TIC.get(nombre, nombre), "serie": serie})
    if len(meses) < 13 or len(paises) < 10 or "Grand Total" not in resumen:
        raise ValueError("la tabla TIC no tiene el formato esperado")
    return {
        "fuente": URL_TIC, "nivel": "P", "unidad": "mil M de $", "meses": meses,
        "paises": paises, "otros": resumen["All Other"], "total": resumen["Grand Total"],
        "oficial": resumen.get("Of Which: Foreign Official"),
        "nota": ("Los datos se recogen sobre todo de custodios y brókeres de EE. UU. Si los valores están en cuentas de custodia en el "
                 "extranjero, pueden no atribuirse a su propietario real (Tesoro, TIC FAQ n.º 7); por eso Bélgica, Luxemburgo o las "
                 "Islas Caimán suben tanto. Las tenencias incluyen cambios de valor de mercado: una bajada no es necesariamente una venta."),
    }


def valor(d, clave):
    v = (d or {}).get(clave)
    return float(v) if v is not None else None


def leer_stablecoins():
    datos = json.loads(descargar(URL_LLAMA))
    lista = []
    for a in datos["peggedAssets"]:
        peg = a.get("pegType", "")
        circ_clave = peg if peg in a.get("circulating", {}) else next(iter(a.get("circulating", {}) or {"": 0}), "")
        circ = valor(a.get("circulating"), circ_clave)
        if not circ:
            continue
        precio = a.get("price") or 1.0
        factor = 1.0 if peg == "peggedUSD" else float(precio)    # monedas ligadas al euro u otras: pasar a dólares con el precio de la propia moneda
        previo_mes = valor(a.get("circulatingPrevMonth"), circ_clave)
        previo_sem = valor(a.get("circulatingPrevWeek"), circ_clave)
        cadenas = a.get("chains") or []
        por_cadena = {}
        for nombre, c in (a.get("chainCirculating") or {}).items():
            v = valor(c.get("current"), circ_clave)
            if v:
                por_cadena[nombre] = v * factor
        lista.append({
            "simbolo": a.get("symbol"), "nombre": a.get("name"), "ligada": peg.replace("pegged", ""),
            "mecanismo": a.get("pegMechanism", ""), "usd": circ * factor,
            "cambio_7d": None if not previo_sem else (circ / previo_sem - 1) * 100,
            "cambio_30d": None if not previo_mes else (circ / previo_mes - 1) * 100,
            "n_cadenas": len(cadenas), "cadenas": cadenas[:6], "por_cadena": por_cadena,
        })
    lista.sort(key=lambda x: -x["usd"])
    total_usd = sum(x["usd"] for x in lista if x["ligada"] == "USD")
    total = sum(x["usd"] for x in lista)

    def top_cadena(nombre, n=6):
        filas = [{"simbolo": x["simbolo"], "nombre": x["nombre"], "usd": x["por_cadena"][nombre], "mecanismo": x["mecanismo"]}
                 for x in lista if nombre in x["por_cadena"]]
        filas.sort(key=lambda f: -f["usd"])
        return {"total": sum(f["usd"] for f in filas), "n": len(filas), "top": filas[:n]}

    return {
        "fuente": URL_LLAMA, "nivel": "S", "unidad": "dólares (USD)", "n_activos": len(lista), "total": total,
        "total_ligadas_usd": total_usd,
        "top": [{k: v for k, v in x.items() if k != "por_cadena"} for x in lista[:15]],
        "xrpl": top_cadena("XRPL"), "stellar": top_cadena("Stellar"),
        "nota": ("DefiLlama es un agregador: sus cifras de circulación son estimaciones y pueden diferir de las atestaciones de cada emisor. "
                 "Las monedas ligadas al euro se pasan a dólares con su propio precio. La lista de DefiLlama incluye también fondos tokenizados de letras (p. ej. BUIDL) y monedas sintéticas (p. ej. USDe): no todo lo que aparece es una stablecoin de pago, y el «respaldo» es la clasificación de DefiLlama."),
    }


URL_PROTOCOLOS = "https://api.llama.fi/protocols"
URL_PRECIOS = "https://api.coingecko.com/api/v3/simple/price?ids=ripple,stellar,bitcoin,ethereum&vs_currencies=usd&include_market_cap=true&include_24hr_change=true"
URL_YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/{s}?range=5d&interval=1d"
INDICES = (("^GSPC", "S&P 500", "EE. UU."), ("ES=F", "Futuros S&P 500", "EE. UU. (futuros)"), ("^IXIC", "Nasdaq Composite", "EE. UU."),
           ("^STOXX50E", "Euro Stoxx 50", "Zona euro"), ("^IBEX", "Ibex 35", "España"), ("^N225", "Nikkei 225", "Japón"),
           ("^KS11", "Kospi", "Corea del Sur"), ("000001.SS", "Shanghái Composite", "China"), ("^HSI", "Hang Seng", "Hong Kong"))
URL_NYFED = "https://markets.newyorkfed.org/api/rates/unsecured/effr/search.json?startDate={d1}&endDate={d2}"
URL_BCE_TIPO = "https://data-api.ecb.europa.eu/service/data/FM/B.U2.EUR.4F.KR.DFR.LEV?startPeriod={d1}&format=csvdata"
URL_BOE_TIPO = "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom={d1}&Dateto={d2}&SeriesCodes=IUDBEDR&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N"
URL_BCB_TIPO = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial={d1}&dataFinal={d2}"
URL_BOC_TIPO = "https://www.bankofcanada.ca/valet/observations/V39079/json?start_date={d1}"


def rwa_por_cadena(rwa, n=10):
    """TVL RWA de DefiLlama sumado por cadena (sin las claves «-borrowed», «-staking», «-pool2», que repiten valor).
    Devuelve las n mayores y, siempre, XRPL y Stellar con su puesto, aunque no entren en el top."""
    tot = {}
    for p in rwa:
        for k, v in (p.get("chainTvls") or {}).items():
            if "-" in k or k.lower() in ("staking", "borrowed", "pool2", "vesting", "offers"):
                continue
            tot[k] = tot.get(k, 0) + (v or 0)
    orden = sorted(tot.items(), key=lambda kv: -kv[1])
    total = sum(tot.values()) or 1
    fila = lambda i, k, v: {"cadena": k, "usd": v, "pct": v / total * 100, "puesto": i + 1,
                            "n_protocolos": sum(1 for p in rwa if (p.get("chainTvls") or {}).get(k))}
    filas = [fila(i, k, v) for i, (k, v) in enumerate(orden[:n])]
    for nombre in ("XRPL", "Stellar"):
        if nombre not in [f["cadena"] for f in filas]:
            for i, (k, v) in enumerate(orden):
                if k == nombre:
                    filas.append(fila(i, k, v))
    return {"n_cadenas": len(orden), "top": filas}


def leer_rwa():
    protocolos = json.loads(descargar(URL_PROTOCOLOS))
    rwa = [p for p in protocolos if (p.get("category") or "") == "RWA" and p.get("tvl")]
    rwa.sort(key=lambda p: -p["tvl"])
    if len(rwa) < 20:
        raise ValueError("la lista de protocolos RWA es demasiado corta")
    return {
        "fuente": URL_PROTOCOLOS, "nivel": "S", "unidad": "dólares (USD)", "n": len(rwa), "total": sum(p["tvl"] for p in rwa),
        "top": [{"nombre": p["name"], "usd": p["tvl"], "cambio_7d": p.get("change_7d"), "cadenas": (p.get("chains") or [])[:3]} for p in rwa[:8]],
        "stellar": sum((p.get("chainTvls") or {}).get("Stellar", 0) for p in rwa),
        "xrpl": sum((p.get("chainTvls") or {}).get("XRPL", 0) for p in rwa),
        "por_cadena": rwa_por_cadena(rwa),
        "nota": ("Es el valor bloqueado (TVL) en protocolos DeFi que DefiLlama clasifica como RWA: NO es el valor total de activos tokenizados. "
                 "Otras metodologías (p. ej. RWA.xyz) dan cifras mucho mayores porque cuentan fondos y bonos tokenizados fuera de DeFi."),
    }


def leer_mercado():
    d = json.loads(descargar(URL_PRECIOS))
    salida = {"fuente": URL_PRECIOS, "nivel": "S", "unidad": "dólares (USD)", "activos": []}
    for clave, simbolo, nombre in (("ripple", "XRP", "XRP"), ("stellar", "XLM", "Stellar Lumens"), ("bitcoin", "BTC", "Bitcoin"), ("ethereum", "ETH", "Ether")):
        x = d[clave]
        salida["activos"].append({"simbolo": simbolo, "nombre": nombre, "precio": x["usd"], "capitalizacion": x.get("usd_market_cap"),
                                  "cambio_24h": x.get("usd_24h_change")})
    return salida


def leer_indices():
    """Cierre diario de 9 índices bursátiles y los futuros del S&P 500 (el contrato cambia de vencimiento: ES=F salta cada trimestre) (Yahoo Finance, no oficial [S]). Si uno falla se avisa y se sigue con los demás."""
    salida = {"fuente": "https://finance.yahoo.com/", "nivel": "S", "indices": [], "fallos": []}
    for simbolo, nombre, zona in INDICES:
        try:
            d = json.loads(descargar(URL_YAHOO.format(s=urllib.request.quote(simbolo))))["chart"]["result"][0]
            cierres = d["indicators"]["quote"][0]["close"]
            pares = [(datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%d"), c) for t, c in zip(d["timestamp"], cierres) if c]
            if len(pares) < 2:
                raise ValueError("menos de 2 cierres")
            (f0, c0), (f1, c1) = pares[-2], pares[-1]
            moneda = d["meta"].get("currency")
            fila = {"simbolo": simbolo, "nombre": nombre, "zona": zona, "valor": round(c1, 2), "fecha": f1,
                    "cambio_1d": round((c1 / c0 - 1) * 100, 2), "moneda": moneda}
            if moneda == "USD":
                fila["cambio_1d_usd"] = fila["cambio_1d"]
            else:   # el índice son puntos, no dinero: lo que sí se puede convertir es lo que habría ganado o perdido un inversor en dólares
                try:
                    fx = json.loads(descargar(URL_YAHOO.format(s=f"{moneda}USD=X")))["chart"]["result"][0]
                    cx = [c for c in fx["indicators"]["quote"][0]["close"] if c]
                    fila["cambio_1d_usd"] = round(((c1 / c0) * (cx[-1] / cx[-2]) - 1) * 100, 2)
                except Exception as e:
                    salida["fallos"].append(f"divisa {moneda}USD: {type(e).__name__}: {e}")
            salida["indices"].append(fila)
        except Exception as e:
            salida["fallos"].append(f"índice {simbolo}: {type(e).__name__}: {e}")
    if not salida["indices"]:
        raise ValueError("ningún índice disponible")
    return salida


def leer_watchlist():
    """Valores de watchlist.toml (los que SIGO, no posiciones) con precio y rentabilidades (Yahoo Finance, no oficial [S])."""
    import tomllib
    with open(SALIDA.parent.parent / "watchlist.toml", "rb") as fh:
        lista = tomllib.load(fh).get("valores", [])
    hoy = datetime.now(timezone.utc).date()
    salida = {"fuente": "https://finance.yahoo.com/", "nivel": "S", "valores": [], "fallos": []}
    for v in lista:
        try:
            d = json.loads(descargar(URL_YAHOO.format(s=urllib.request.quote(v["yahoo"])) .replace("range=5d", "range=1y") + "&events=div"))["chart"]["result"][0]
            pares = [(datetime.fromtimestamp(t, timezone.utc).date(), c) for t, c in zip(d["timestamp"], d["indicators"]["quote"][0]["close"]) if c]
            if len(pares) < 2:
                raise ValueError("menos de 2 cierres")
            ultimo = float(d["meta"].get("regularMarketPrice") or pares[-1][1])

            def desde(dias):
                previos = [c for f, c in pares if f <= hoy - timedelta(days=dias)]
                return round((ultimo / previos[-1] - 1) * 100, 2) if previos else None
            repartos = [x["amount"] for x in ((d.get("events") or {}).get("dividends") or {}).values()
                        if datetime.fromtimestamp(x["date"], timezone.utc).date() > hoy - timedelta(days=365)]
            div12 = round(sum(repartos) / ultimo * 100, 2) if repartos else None   # dividendos de los últimos 12 meses / precio actual
            anio = [c for f, c in pares if f.year < hoy.year]
            ytd = round((ultimo / (anio[-1] if anio else pares[0][1]) - 1) * 100, 2)
            salida["valores"].append({"ticker": v["ticker"], "nombre": v["nombre"], "categoria": v.get("categoria", "Otros"), "precio": round(ultimo, 2),
                                      "moneda": d["meta"].get("currency"), "fecha": pares[-1][0].isoformat(),
                                      "cambio_1d": round((pares[-1][1] / pares[-2][1] - 1) * 100, 2), "cambio_1s": desde(7), "cambio_3m": desde(91), "ytd": ytd, "div_12m": div12, "n_repartos": len(repartos)})
        except Exception as e:
            salida["fallos"].append(f"watchlist {v.get('ticker')}: {type(e).__name__}: {e}")
    if not salida["valores"]:
        raise ValueError("ningún valor de la watchlist disponible")
    return salida


URL_BIS_TIPOS = "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_CBPOL/1.0/D.CH+CN+HK+ID+IN+JP+KR+MX+RU+ZA?lastNObservations=1"
PAISES_BIS = {"CH": "Suiza", "CN": "China", "HK": "Hong Kong", "ID": "Indonesia", "IN": "India", "JP": "Japón", "KR": "Corea del Sur",
              "MX": "México", "RU": "Rusia", "ZA": "Sudáfrica"}


def leer_tipos_bis():
    """Último tipo oficial de 10 bancos centrales según el BIS (Data Portal, SDMX CSV) [P vía BIS]. El BIS puede ir días por detrás del banco central."""
    peticion = urllib.request.Request(URL_BIS_TIPOS, headers={"Accept": "application/vnd.sdmx.data+csv;version=1.0.0", "User-Agent": "cartera-joel/1.0 (uso personal)"})
    with urllib.request.urlopen(peticion, timeout=30) as r:
        texto = r.read().decode("utf-8")
    filas, fallos = [], []
    for f in csv.DictReader(io.StringIO(texto)):
        try:
            cod = f["REF_AREA"]
            valor = float(f["OBS_VALUE"])
            filas.append({"id": cod, "pais": PAISES_BIS.get(cod, cod), "banco": f.get("SOURCE_REF", ""), "num": valor,
                          "valor": f"{valor:.2f}".replace(".", ",") + " %", "dato_de": f["TIME_PERIOD"]})
        except Exception as e:
            fallos.append(f"BIS {f.get('REF_AREA')}: {type(e).__name__}: {e}")
    if not filas:
        raise ValueError("el BIS no devolvió ningún tipo")
    filas.sort(key=lambda x: -x["num"])
    return {"fuente": "https://data.bis.org/topics/CBPOL", "nivel": "P", "paises": filas, "fallos": fallos}


PAISES_DEFENSA = {"US": "EE. UU.", "CN": "China", "RU": "Rusia", "IN": "India", "DE": "Alemania", "FR": "Francia", "GB": "Reino Unido", "ES": "España",
                  "PL": "Polonia", "JP": "Japón", "KR": "Corea del Sur", "IL": "Israel", "SA": "Arabia Saudí", "TR": "Turquía", "UA": "Ucrania"}


def leer_defensa():
    """Gasto militar en % del PIB (Banco Mundial, indicador MS.MIL.XPND.GD.ZS, reutiliza datos de SIPRI) [P]. La API tarda: en paralelo, con reintento."""
    from concurrent.futures import ThreadPoolExecutor

    def uno(codigo):
        url = f"https://api.worldbank.org/v2/country/{codigo}/indicator/MS.MIL.XPND.GD.ZS?format=json&per_page=60&date=2014:2026"
        for _ in range(2):
            try:
                peticion = urllib.request.Request(url, headers={"User-Agent": "cartera-joel/1.0 (uso personal)"})
                with urllib.request.urlopen(peticion, timeout=30) as r:
                    datos = json.loads(r.read().decode("utf-8"))[1]
                return codigo, sorted(((x["date"], x["value"]) for x in datos if x["value"] is not None), reverse=True)
            except Exception:
                pass
        return codigo, None
    with ThreadPoolExecutor(max_workers=8) as ex:
        res = dict(ex.map(uno, PAISES_DEFENSA))
    filas, fallos = [], []
    for cod, nombre in PAISES_DEFENSA.items():
        serie = res.get(cod)
        if not serie:
            fallos.append(f"defensa {cod}: sin datos")
            continue
        anio, valor = serie[0]
        previo = next((v for a, v in serie if int(a) <= int(anio) - 10), None)
        filas.append({"id": cod, "pais": nombre, "valor": round(valor, 2), "anio": anio, "hace_10": None if previo is None else round(previo, 2)})
    if not filas:
        raise ValueError("el Banco Mundial no devolvió ningún país")
    filas.sort(key=lambda x: -x["valor"])
    return {"fuente": "https://data.worldbank.org/indicator/MS.MIL.XPND.GD.ZS", "nivel": "P", "paises": filas, "fallos": fallos}


URL_PORTWATCH = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query"
LIQUIDEZ_MANUAL = Path(__file__).resolve().parent.parent / "explorador" / "liquidez-manual.json"


def leer_ormuz():
    """Barcos al día por el estrecho de Ormuz (IMF PortWatch, API abierta; dato propio del FMI con retraso de días) [P]."""
    import collections
    params = urllib.parse.urlencode({"where": "portname='Strait of Hormuz' AND date >= '2026-01-01'", "outFields": "date,n_total,n_tanker",
                                     "orderByFields": "date ASC", "resultRecordCount": "500", "f": "json"})
    datos = json.loads(descargar(f"{URL_PORTWATCH}?{params}"))["features"]
    filas = [(f["attributes"]["date"][:10], f["attributes"]["n_total"] or 0, f["attributes"]["n_tanker"] or 0) for f in datos]
    if not filas:
        raise ValueError("PortWatch no devolvió datos")
    meses = collections.defaultdict(list)
    for fecha, total, petro in filas:
        meses[fecha[:7]].append((total, petro))
    mensual = [{"mes": m, "dias": len(v), "total": round(sum(x[0] for x in v) / len(v), 1), "petroleros": round(sum(x[1] for x in v) / len(v), 1)} for m, v in sorted(meses.items())]
    ultimos = filas[-7:]
    return {"fuente": "https://portwatch.imf.org/", "nivel": "P", "ultimo": {"fecha": filas[-1][0], "total": filas[-1][1], "petroleros": filas[-1][2]},
            "media_7d": round(sum(x[1] for x in ultimos) / len(ultimos), 1), "mensual": mensual}


def leer_liquidez():
    """M2 de EE. UU. (FRED, variación interanual) y M3 de la zona euro (BCE, variación anual) [P]."""
    with urllib.request.urlopen(urllib.request.Request("https://fred.stlouisfed.org/graph/fredgraph.csv?id=M2SL&cosd=2024-01-01", headers={"User-Agent": "cartera-joel/1.0 (uso personal)"}), timeout=40) as r:
        filas = list(csv.reader(io.StringIO(r.read().decode("utf-8"))))[1:]
    m2 = {f: float(v) for f, v in filas if v not in (".", "")}
    ult = max(m2)
    ant = f"{int(ult[:4]) - 1}{ult[4:]}"
    peticion = urllib.request.Request("https://data-api.ecb.europa.eu/service/data/BSI/M.U2.Y.V.M30.X.I.U2.2300.Z01.A?lastNObservations=13&format=csvdata",
                                      headers={"Accept": "text/csv", "User-Agent": "cartera-joel/1.0 (uso personal)"})
    with urllib.request.urlopen(peticion, timeout=40) as r:
        m3 = [(f["TIME_PERIOD"], float(f["OBS_VALUE"])) for f in csv.DictReader(io.StringIO(r.read().decode("utf-8")))]
    manual = json.loads(LIQUIDEZ_MANUAL.read_text(encoding="utf-8")) if LIQUIDEZ_MANUAL.exists() else {}
    return {"fuente": "FRED (M2SL) y BCE (BSI, M3)", "nivel": "P", "manual": manual,
            "us": {"serie": "M2 EE. UU.", "fecha": ult[:7], "valor_mil_m": round(m2[ult] / 1000, 2), "interanual": round((m2[ult] / m2[ant] - 1) * 100, 2) if ant in m2 else None},
            "ea": {"serie": "M3 zona euro", "fecha": m3[-1][0], "interanual": round(m3[-1][1], 2), "hace_12m": round(m3[0][1], 2)}}


def _ultimo_cambio(serie):
    """serie = [(fecha ISO, valor)] ordenada; devuelve (valor actual, fecha del último cambio, valor anterior)."""
    serie = [(f, v) for f, v in serie if v is not None]
    actual = serie[-1][1]
    for i in range(len(serie) - 1, 0, -1):
        if abs(serie[i][1] - serie[i - 1][1]) > 1e-9:
            return actual, serie[i][0], serie[i - 1][1]
    return actual, None, None


def _pct(v):
    return f"{v:.2f}".replace(".", ",") + " %"


def leer_tipos():
    """Tipos oficiales al día de 5 bancos centrales con fuente abierta [P]; el resto sigue a mano en el radar (regulacion.json)."""
    hoy = datetime.now(timezone.utc)
    hoy_iso = hoy.strftime("%Y-%m-%d")
    d1y = (hoy - timedelta(days=500)).strftime("%Y-%m-%d")
    filas, fallos = [], []

    def anadir(jur, pais, banco, valor_txt, num, fecha_cambio, previo, leido, fuente, url):
        filas.append({"jur": jur, "pais": pais, "banco": banco, "valor": valor_txt, "num": num, "ultimo_cambio": fecha_cambio,
                      "cambio_pb": None if previo is None else round((num - previo) * 100), "dato_de": leido, "fuente": fuente, "url": url})

    try:    # Reserva Federal: rango objetivo, en el archivo del Banco de la Reserva Federal de Nueva York (primaria)
        r = sorted(json.loads(descargar(URL_NYFED.format(d1=d1y, d2=hoy_iso)))["refRates"], key=lambda x: x["effectiveDate"])
        n, f, pv = _ultimo_cambio([(x["effectiveDate"], x.get("targetRateTo")) for x in r])
        ult = r[-1]
        rango = f"{ult['targetRateFrom']:.2f}".replace(".", ",") + "–" + _pct(ult["targetRateTo"])
        anadir("eeuu", "EE. UU.", "Reserva Federal (rango objetivo)", rango, n, f, pv, ult["effectiveDate"],
               "Banco de la Reserva Federal de Nueva York (EFFR y rango objetivo)", "https://www.newyorkfed.org/markets/reference-rates/effr")
    except Exception as e:
        fallos.append(f"tipo Fed: {type(e).__name__}: {e}")
    try:    # BCE: tipo de la facilidad de depósito (primaria)
        serie = sorted((x["TIME_PERIOD"], _num(x["OBS_VALUE"])) for x in csv.DictReader(io.StringIO(descargar(URL_BCE_TIPO.format(d1=d1y)))))
        n, f, pv = _ultimo_cambio(serie)
        anadir("ue", "Zona euro", "BCE (facilidad de depósito)", _pct(n), n, f, pv, serie[-1][0], "BCE, data-api.ecb.europa.eu (FM, DFR)",
               "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html")
    except Exception as e:
        fallos.append(f"tipo BCE: {type(e).__name__}: {e}")
    try:    # Banco de Inglaterra: Bank Rate (primaria)
        meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        fmt = lambda t: f"{t.day:02d}/{meses[t.month - 1]}/{t.year}"
        serie = []
        for linea in descargar(URL_BOE_TIPO.format(d1=fmt(hoy - timedelta(days=500)), d2=fmt(hoy))).splitlines():
            partes = [x.strip() for x in linea.split(",")]
            if len(partes) == 2 and _num(partes[1]) is not None:
                serie.append((datetime.strptime(partes[0], "%d %b %Y").strftime("%Y-%m-%d"), _num(partes[1])))
        serie.sort()
        n, f, pv = _ultimo_cambio(serie)
        anadir("uk", "Reino Unido", "Banco de Inglaterra (Bank Rate)", _pct(n), n, f, pv, serie[-1][0],
               "Banco de Inglaterra, base de datos estadística (IUDBEDR)", "https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp")
    except Exception as e:
        fallos.append(f"tipo BoE: {type(e).__name__}: {e}")
    try:    # Brasil: meta de la Selic del Copom (SGS 432; la serie trae fechas futuras y se ignoran)
        filas_j = json.loads(descargar(URL_BCB_TIPO.format(d1=(hoy - timedelta(days=500)).strftime("%d/%m/%Y"), d2=hoy.strftime("%d/%m/%Y"))))
        serie = sorted((datetime.strptime(x["data"], "%d/%m/%Y").strftime("%Y-%m-%d"), _num(x["valor"])) for x in filas_j)
        serie = [x for x in serie if x[0] <= hoy_iso]
        n, f, pv = _ultimo_cambio(serie)
        anadir("br", "Brasil", "Banco Central de Brasil (meta Selic)", _pct(n), n, f, pv, serie[-1][0], "Banco Central de Brasil, SGS 432",
               "https://www.bcb.gov.br/controleinflacao/historicotaxasjuros")
    except Exception as e:
        fallos.append(f"tipo Brasil: {type(e).__name__}: {e}")
    try:    # Canadá: tipo objetivo a un día (Valet API del Banco de Canadá)
        serie = sorted((x["d"], _num(x["V39079"]["v"])) for x in json.loads(descargar(URL_BOC_TIPO.format(d1=d1y)))["observations"])
        n, f, pv = _ultimo_cambio(serie)
        anadir("ca", "Canadá", "Banco de Canadá (tipo a un día)", _pct(n), n, f, pv, serie[-1][0], "Banco de Canadá, Valet API (V39079)",
               "https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/")
    except Exception as e:
        fallos.append(f"tipo Canadá: {type(e).__name__}: {e}")
    if not filas:
        raise ValueError("ningún tipo disponible: " + "; ".join(fallos))
    try:    # comparación con el radar: números del texto «valor» de la celda de política monetaria
        radar = json.loads((SALIDA.parent / "regulacion.json").read_text(encoding="utf-8"))
        valores = {c["jur"]: c.get("valor") for c in radar["celdas"] if c.get("tema") == "politica"}
    except Exception:
        valores = {}
    for fila in filas:
        v = valores.get(fila["jur"])
        fila["radar"] = v
        if v is None:
            fila["coincide_radar"] = None
            continue
        numeros = [float(x.replace(",", ".")) for x in re.findall(r"\d+,\d+|\d+", v)]
        fila["coincide_radar"] = any(abs(fila["num"] - x) < 0.006 for x in numeros)
    return {"fuente": "Bancos centrales (ver cada fila)", "nivel": "P", "paises": filas, "fallos": fallos,
            "nota": "Valores leídos de la fuente oficial de cada banco. «Último cambio» es la fecha en que cambió el valor en la serie, no la de la reunión."}


def _num(x):
    try:
        return float(x)
    except Exception:
        return None


def leer_bonos():
    """Rendimientos de bonos y letras por plazo (3M a 30A) de fuentes oficiales abiertas. Sin IA."""
    out, fallos = [], []

    def anade(pais, nombre, nivel, fuente, plazos, prev, fecha, hist10=None, url=None):
        out.append({"id": pais, "nombre": nombre, "nivel": nivel, "fuente": fuente, "fecha": fecha, "plazos": plazos,
                    "prev": prev, "hist10": hist10 or [], "url": url})

    def probar(nombre, f):
        try:
            f()
        except Exception as e:
            fallos.append(f"{nombre}: {type(e).__name__}: {e}")

    def eeuu():
        filas = sorted(csv.DictReader(io.StringIO(descargar(URL_UST))), key=lambda r: datetime.strptime(r["Date"], "%m/%d/%Y"))
        col = {"3M": "3 Mo", "6M": "6 Mo", "1A": "1 Yr", "2A": "2 Yr", "5A": "5 Yr", "10A": "10 Yr", "30A": "30 Yr"}
        f1, f0 = filas[-1], filas[-2]
        anade("USA", "EE. UU.", "P", "Tesoro de EE. UU., curva diaria de rendimientos (bonos del Tesoro a vencimiento constante)",
              {k: _num(f1[v]) for k, v in col.items()}, {k: _num(f0[v]) for k, v in col.items()},
              datetime.strptime(f1["Date"], "%m/%d/%Y").strftime("%Y-%m-%d"),
              [[datetime.strptime(r["Date"], "%m/%d/%Y").strftime("%Y-%m-%d"), _num(r["10 Yr"])] for r in filas[-22:]],
              "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve")

    def japon():
        lineas = [l for l in descargar(URL_JGB).splitlines() if l[:4].isdigit()]
        cab = ["1A", "2A", "3A", "4A", "5A", "6A", "7A", "8A", "9A", "10A", "15A", "20A", "25A", "30A", "40A"]

        def fila(l):
            c = l.split(",")
            y, m, d = c[0].split("/")
            return f"{y}-{int(m):02d}-{int(d):02d}", {k: _num(v) for k, v in zip(cab, c[1:])}

        (f1, v1), (_, v0) = fila(lineas[-1]), fila(lineas[-2])
        keep = ("1A", "2A", "3A", "5A", "10A", "20A", "30A")
        anade("JPN", "Japón", "P", "Ministerio de Finanzas de Japón, rendimientos de JGB (bonos del Estado) por plazo",
              {k: v1[k] for k in keep}, {k: v0[k] for k in keep}, f1, [[fila(l)[0], fila(l)[1]["10A"]] for l in lineas[-22:]],
              "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/index.htm")

    def zona_euro():
        pl = {"3M": "3M", "1A": "1Y", "2A": "2Y", "5A": "5Y", "10A": "10Y", "30A": "30Y"}
        v1, v0, fecha, hist = {}, {}, None, []
        for k, p in pl.items():
            j = json.loads(descargar(URL_BCE_YC.format(p=p, n=22 if k == "10A" else 2)))
            obs = list(j["dataSets"][0]["series"].values())[0]["observations"]
            fechas = [x["id"] for x in j["structure"]["dimensions"]["observation"][0]["values"]]
            idx = sorted(obs, key=int)
            v1[k] = round(obs[idx[-1]][0], 3)
            v0[k] = round(obs[idx[-2]][0], 3)
            if k == "10A":
                fecha = fechas[int(idx[-1])]
                hist = [[fechas[int(i)], round(obs[i][0], 3)] for i in idx]
        anade("EUR", "Zona euro (AAA)", "P", "BCE, curva de rendimientos de la zona euro (emisores con calificación AAA; no es la de un país)",
              v1, v0, fecha, hist, "https://data.ecb.europa.eu/data/datasets/YC")

    def espana():
        j = json.loads(descargar(URL_BDE.format(s=",".join(BDE_SERIES))))
        v1, v0, hist, fecha = {}, {}, [], None
        for ser in j:
            k = BDE_SERIES[ser["serie"]]
            v1[k], v0[k] = ser["valores"][0], ser["valores"][1]
            if k == "10A":
                fecha = ser["fechas"][0][:10]
                hist = [[f[:10], v] for f, v in zip(ser["fechas"][:22], ser["valores"][:22])][::-1]
        anade("ESP", "España", "P", "Banco de España, tipos de interés del mercado secundario de deuda del Estado (letras y bonos y obligaciones, operaciones simples al contado)",
              v1, v0, fecha, hist, "https://www.bde.es/webbe/es/estadisticas/temas/mercados-financieros.html")

    def reino_unido():
        v1, v0, fecha = {}, {}, None
        hoy = datetime.now(timezone.utc)
        for cod, k in BOE_PAR.items():
            url = ("https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=%s&Dateto=%s&SeriesCodes=%s&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N"
                   % ((hoy - timedelta(days=14)).strftime("%d/%b/%Y"), hoy.strftime("%d/%b/%Y"), cod))
            lineas = [l for l in descargar(url).splitlines()[1:] if l.strip()]
            f, v = lineas[-1].split(",")
            v1[k] = round(float(v), 3)
            v0[k] = round(float(lineas[-2].split(",")[1]), 3)
            fecha = datetime.strptime(f, "%d %b %Y").strftime("%Y-%m-%d")
        anade("GBR", "Reino Unido", "P", "Banco de Inglaterra, rendimiento nominal «par» de los gilts (series IUDSNPY, IUDMNPY, IUDLNPY)",
              v1, v0, fecha, [], "https://www.bankofengland.co.uk/statistics/yield-curves")

    def francia():
        m = json.loads(BONOS_MANUAL.read_text(encoding="utf-8"))["francia"]
        serie = m["serie10"]
        anade("FRA", m["nombre"], m["nivel"], m["fuente"], {"10A": serie[-1][1]}, {"10A": serie[-2][1]}, serie[-1][0], serie, m["url"])

    for nombre, f in (("EE. UU.", eeuu), ("Japón", japon), ("Zona euro", zona_euro), ("España", espana), ("Reino Unido", reino_unido), ("Francia", francia)):
        probar(nombre, f)
    mensual = {}
    for c, n in (("DE", "Alemania"), ("ES", "España"), ("FR", "Francia"), ("IT", "Italia")):
        try:
            j = json.loads(descargar(URL_BCE_IRS.format(c=c)))
            obs = list(j["dataSets"][0]["series"].values())[0]["observations"]
            fechas = [x["id"] for x in j["structure"]["dimensions"]["observation"][0]["values"]]
            idx = sorted(obs, key=int)
            mensual[c] = {"nombre": n, "mes": fechas[int(idx[-1])], "valor": round(obs[idx[-1]][0], 3),
                          "mes_ant": fechas[int(idx[-2])], "valor_ant": round(obs[idx[-2]][0], 3)}
        except Exception as e:
            fallos.append(f"BCE mensual {c}: {type(e).__name__}: {e}")
    paises = {p["id"]: p for p in out}
    previo = (PREVIO.get("bonos") or {}).get("paises") or []
    for p in previo:                              # si una fuente falla, se conserva el dato anterior (con su fecha)
        if p["id"] not in paises:
            out.append(p)
    return {"paises": out, "mensual10": mensual, "fallos": fallos,
            "nota_mensual": "Rendimiento medio mensual del bono a 10 años que usa el BCE para los criterios de convergencia: sirve para comparar países euro entre sí (Alemania, España, Francia, Italia), con ~1 mes de retraso."}


def leer_deuda():
    """Deuda pública por país: FMI (archivo manual, la API da 403 a curl) + rendimiento a 10 años de fuentes oficiales abiertas."""
    base = json.loads(FMI.read_text(encoding="utf-8"))
    rend = {}
    fallos = []

    def probar(pais, funcion):
        try:
            rend[pais] = funcion()
        except Exception as e:
            fallos.append(f"{pais}: {type(e).__name__}: {e}")

    def ust():
        filas = list(csv.DictReader(io.StringIO(descargar(URL_UST))))
        f = max(filas, key=lambda r: datetime.strptime(r["Date"], "%m/%d/%Y"))
        return {"valor": float(f["10 Yr"]), "fecha": datetime.strptime(f["Date"], "%m/%d/%Y").strftime("%Y-%m-%d"), "nivel": "P",
                "fuente": "Tesoro de EE. UU., curva diaria de rendimientos (bonos a 10 años)"}

    def jgb():
        lineas = [l for l in descargar(URL_JGB).splitlines() if l[:4].isdigit()]
        celdas = lineas[-1].split(",")
        y, m, d = celdas[0].split("/")
        return {"valor": float(celdas[10]), "fecha": f"{y}-{int(m):02d}-{int(d):02d}", "nivel": "P",
                "fuente": "Ministerio de Finanzas de Japón, rendimientos de JGB a 10 años"}

    def bce():
        j = json.loads(descargar(URL_BCE))
        obs = list(j["dataSets"][0]["series"].values())[0]["observations"]
        fechas = j["structure"]["dimensions"]["observation"][0]["values"]
        k = max(obs, key=int)
        return {"valor": round(obs[k][0], 2), "fecha": fechas[int(k)]["id"], "nivel": "P",
                "fuente": "BCE, curva de rendimientos de la zona euro (emisores AAA, 10 años); no es solo Alemania"}

    def boe():
        hoy = datetime.now(timezone.utc)
        f = lambda t: t.strftime("%d/%b/%Y")
        url = URL_BOE.format(d1=f(hoy - timedelta(days=14)), d2=f(hoy))
        lineas = [l for l in descargar(url).splitlines()[1:] if l.strip()]
        fecha, v = lineas[-1].split(",")
        return {"valor": round(float(v), 2), "fecha": datetime.strptime(fecha, "%d %b %Y").strftime("%Y-%m-%d"), "nivel": "P",
                "fuente": "Banco de Inglaterra, serie IUDMNZC («Yield from British Government Securities - 10 year Nominal Zero Coupon»): rendimiento cupón cero, no «par»; la versión par (IUDMNPY) da 5,37 % el 19-oct, así que no es comparable con otros bonos a 10 años"}

    probar("USA", ust)
    probar("JPN", jgb)
    probar("EUR", bce)
    probar("GBR", boe)
    base["rendimientos"] = rend
    base["fallos"] = fallos
    return base


PREVIO = {}


def main():
    global PREVIO
    previo = {}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        except Exception:
            previo = {}
    PREVIO = previo
    salida = {"leido": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}
    fallos = []
    for clave, funcion in (("tic", leer_tic), ("stablecoins", leer_stablecoins), ("rwa", leer_rwa), ("mercado", leer_mercado), ("deuda", leer_deuda), ("bonos", leer_bonos), ("indices", leer_indices), ("watchlist", leer_watchlist), ("tipos_vivos", leer_tipos), ("tipos_bis", leer_tipos_bis), ("defensa", leer_defensa), ("liquidez", leer_liquidez), ("ormuz", leer_ormuz)):
        try:
            salida[clave] = funcion()
            salida[clave]["leido"] = salida["leido"]
        except Exception as e:
            fallos.append(f"{clave}: {type(e).__name__}: {e}")
            if clave in previo:
                salida[clave] = previo[clave]
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    tic = salida.get("tic")
    if tic:
        print(f"TIC: {len(tic['paises'])} países, último mes {tic['meses'][0]}, total {tic['total'][0]:,.1f} MM$")
    st = salida.get("stablecoins")
    if st:
        print(f"Stablecoins: {st['n_activos']} activos, total {st['total'] / 1e9:,.1f} MM$; XRPL {st['xrpl']['total'] / 1e6:,.0f} M$; Stellar {st['stellar']['total'] / 1e6:,.0f} M$")
    bo = salida.get("bonos")
    if bo:
        print("Bonos: %s; mensual 10A: %s" % (", ".join(f"{p['id']} {p['plazos'].get('10A')} ({p['fecha']})" for p in bo["paises"]), ", ".join(f"{k} {v['valor']}" for k, v in bo["mensual10"].items())))
        fallos += bo.get("fallos", [])
    de = salida.get("deuda")
    if de:
        print("Deuda: %d países FMI; rendimientos a 10 años: %s" % (len(de["paises"]), ", ".join(f"{k} {v['valor']} % ({v['fecha']})" for k, v in de["rendimientos"].items())))
        fallos += de.get("fallos", [])
    ix = salida.get("indices")
    if ix:
        print("Índices: " + ", ".join(f"{i['nombre']} {i['valor']:,.0f} ({i['cambio_1d']:+.2f} %, {i['fecha']})" for i in ix["indices"]))
        fallos += ix.get("fallos", [])
    ti = salida.get("tipos_vivos")
    if ti:
        print("Tipos: " + ", ".join(f"{p['pais']} {p['valor']}" + ("" if p.get("coincide_radar") in (True, None) else " (¡no coincide con el radar: " + str(p["radar"]) + "!)") for p in ti["paises"]))
        fallos += ti.get("fallos", [])
    for f in fallos:
        print("AVISO (se conserva lo anterior si existía):", f)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
