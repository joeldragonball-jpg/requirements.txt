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
import sys
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
        "fuente": URL_TIC, "nivel": "P", "unidad": "miles de millones de dólares (MM$)", "meses": meses,
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
URL_PRECIOS = "https://api.coingecko.com/api/v3/simple/price?ids=ripple,stellar,bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_change=true"


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
        "nota": ("Es el valor bloqueado (TVL) en protocolos DeFi que DefiLlama clasifica como RWA: NO es el valor total de activos tokenizados. "
                 "Otras metodologías (p. ej. RWA.xyz) dan cifras mucho mayores porque cuentan fondos y bonos tokenizados fuera de DeFi."),
    }


def leer_mercado():
    d = json.loads(descargar(URL_PRECIOS))
    salida = {"fuente": URL_PRECIOS, "nivel": "S", "unidad": "dólares (USD)", "activos": []}
    for clave, simbolo, nombre in (("ripple", "XRP", "XRP"), ("stellar", "XLM", "Stellar Lumens"), ("bitcoin", "BTC", "Bitcoin")):
        x = d[clave]
        salida["activos"].append({"simbolo": simbolo, "nombre": nombre, "precio": x["usd"], "capitalizacion": x.get("usd_market_cap"),
                                  "cambio_24h": x.get("usd_24h_change")})
    return salida


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
    for clave, funcion in (("tic", leer_tic), ("stablecoins", leer_stablecoins), ("rwa", leer_rwa), ("mercado", leer_mercado), ("deuda", leer_deuda), ("bonos", leer_bonos)):
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
    for f in fallos:
        print("AVISO (se conserva lo anterior si existía):", f)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
