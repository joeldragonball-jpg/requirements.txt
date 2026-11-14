"""Indicadores económicos y sociales por país (C59): cifras ya publicadas por Eurostat, Banco Mundial y FMI, sin claves.

Lo usa actualizar_paneles.leer_indicadores(); también se puede lanzar suelto: python scripts/indicadores.py
Si una fuente falla, el indicador anterior se conserva y se avisa en «fallos». No ordena países ni inventa índices.
"""
import json
import sys
import threading
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FMI = RAIZ / "explorador" / "deuda-fmi.json"
MANUAL = RAIZ / "explorador" / "indicadores-manual.json"

PAISES = [
    ("ES", "España", "ES", "ESP"), ("DE", "Alemania", "DE", "DEU"), ("FR", "Francia", "FR", "FRA"),
    ("IT", "Italia", "IT", "ITA"), ("NL", "Países Bajos", "NL", "NLD"), ("PL", "Polonia", "PL", "POL"),
    ("US", "EE. UU.", None, "USA"), ("CN", "China", None, "CHN"), ("JP", "Japón", None, "JPN"),
    ("IN", "India", None, "IND"), ("GB", "Reino Unido", None, "GBR"), ("RU", "Rusia", None, "RUS"),
    # C138-C139: BRICS ampliados y Latinoamérica (Banco Mundial; deuda y déficit del FMI solo si están en deuda-fmi.json)
    ("BR", "Brasil", None, "BRA"), ("ZA", "Sudáfrica", None, "ZAF"), ("ID", "Indonesia", None, "IDN"), ("EG", "Egipto", None, "EGY"),
    ("ET", "Etiopía", None, "ETH"), ("IR", "Irán", None, "IRN"), ("AE", "Emiratos Árabes Unidos", None, "ARE"),
    ("SV", "El Salvador", None, "SLV"), ("AR", "Argentina", None, "ARG"), ("VE", "Venezuela", None, "VEN"), ("CU", "Cuba", None, "CUB"),
]
URL_EUROSTAT = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{d}?{q}&format=JSON"
URL_BM = "https://api.worldbank.org/v2/country/{c}/indicator/{i}?format=json&mrv=6"
URL_FMI = "https://www.imf.org/external/datamapper/api/v1/{i}/{c}"


_FIN = [None]      # instante límite (time.monotonic) para todo el bloque: pasado ese punto, las peticiones fallan en seco y se conserva el dato anterior


def _get(url, t=40):
    if _FIN[0] is not None and time.monotonic() > _FIN[0]:
        raise TimeoutError("tiempo total agotado (se conserva el dato anterior)")
    r = urllib.request.Request(url, headers={"User-Agent": "cartera-joel/1.0 (uso personal)"})
    with urllib.request.urlopen(r, timeout=t) as f:
        return json.loads(f.read().decode("utf-8", "replace"))


class _Ant(threading.local):
    """Valor del periodo anterior del último indicador leído: (valor, periodo); lo recoge poner(). Uno por hilo."""
    v = None

    def __getitem__(self, i):
        return self.v

    def __setitem__(self, i, x):
        self.v = x


_ANT = _Ant()


def _eurostat(dataset, **filtros):
    """Último valor no vacío de un dataset de Eurostat con todas las dimensiones fijadas salvo el tiempo."""
    q = urllib.parse.urlencode({**filtros, "lastTimePeriod": 4}, doseq=True)
    j = _get(URL_EUROSTAT.format(d=dataset, q=q))
    tiempos = {v: k for k, v in j["dimension"]["time"]["category"]["index"].items()}
    vals = {int(k): v for k, v in j["value"].items()}
    if not vals:
        raise ValueError("sin datos")
    i = max(vals)
    ant = [k for k in sorted(vals, reverse=True) if k < i]
    _ANT[0] = (round(vals[ant[0]], 1), tiempos[ant[0]]) if ant else None
    return round(vals[i], 1), tiempos[i], j.get("updated", "")[:10]


def _bm(pais, indicador, dec=1, escala=1):
    try:
        j = _get(URL_BM.format(c=pais, i=indicador))
    except TimeoutError:                       # el Banco Mundial da timeouts sueltos: un reintento
        j = _get(URL_BM.format(c=pais, i=indicador), 30)
    if len(j) < 2 or not j[1]:
        raise ValueError("sin datos")
    con = [x for x in j[1] if x.get("value") is not None]
    if not con:
        raise ValueError("sin datos")
    f = con[0]
    _ANT[0] = (round(con[1]["value"] / escala, dec), con[1]["date"]) if len(con) > 1 else None
    return round(f["value"] / escala, dec), f["date"], j[0].get("lastupdated", "")


def _fmi(pais, campo):
    """Deuda o saldo de explorador/deuda-fmi.json (el FMI da 403 a los scripts: se pega desde el navegador tras cada WEO). Año 2025."""
    j = json.loads(FMI.read_text(encoding="utf-8"))
    i = j["anios"].index("2025")
    for p in j["paises"]:
        if p["id"] == pais:
            _ANT[0] = (round(p[campo][i - 1], 1), "2024") if i > 0 and p[campo][i - 1] is not None else None
            return round(p[campo][i], 1), "2025"
    raise ValueError("país sin dato en deuda-fmi.json")


def _ind(valor, unidad, fecha, fuente, nivel, definicion, periodicidad, nota=None):
    d = {"valor": valor, "unidad": unidad, "fecha": fecha, "fuente": fuente, "nivel": nivel, "definicion": definicion, "periodicidad": periodicidad}
    if nota:
        d["nota"] = nota
    return d


def leer_indicadores(previo=None):
    """Devuelve {"paises": [...], "fallos": [...]}; previo = el bloque «indicadores» anterior para conservar lo que falle."""
    previo_p = {p["id"]: p.get("indicadores", {}) for p in (previo or {}).get("paises", [])}
    manual = json.loads(MANUAL.read_text(encoding="utf-8")) if MANUAL.exists() else {}
    fallos, salida = [], []
    def _uno(pid, nombre, geo, iso):
        fallos = []
        ind = {}

        def poner(clave, fn):
            try:
                _ANT[0] = None
                ind[clave] = fn()
                if _ANT[0]:
                    ind[clave]["anterior"], ind[clave]["anterior_fecha"] = _ANT[0]
                elif clave in previo_p.get(pid, {}) and previo_p[pid][clave].get("fecha") != ind[clave].get("fecha") and previo_p[pid][clave].get("valor") is not None:
                    ind[clave]["anterior"], ind[clave]["anterior_fecha"] = previo_p[pid][clave]["valor"], previo_p[pid][clave].get("fecha")
            except Exception as e:
                fallos.append(f"{pid}/{clave}: {type(e).__name__}: {e}")
                if clave in previo_p.get(pid, {}):
                    ind[clave] = previo_p[pid][clave]

        if geo:
            ue = "https://ec.europa.eu/eurostat/databrowser/view/"
            poner("ipc", lambda: _ind(*(lambda v: (v[0], "% interanual", v[1], ue + "prc_hicp_minr", "P", "IPCA (índice armonizado de la UE, ECOICOP 2), tasa anual del último mes", "mensual"))(_eurostat("prc_hicp_minr", geo=geo, coicop18="TOTAL", unit="RCH_A"))))
            poner("paro", lambda: _ind(*(lambda v: (v[0], "% población activa", v[1], ue + "une_rt_m", "P", "Paro total, desestacionalizado (definición OIT)", "mensual"))(_eurostat("une_rt_m", geo=geo, s_adj="SA", age="TOTAL", sex="T", unit="PC_ACT"))))
            poner("paro_juvenil", lambda: _ind(*(lambda v: (v[0], "% población activa", v[1], ue + "une_rt_m", "P", "Paro de menores de 25 años, desestacionalizado (definición OIT)", "mensual"))(_eurostat("une_rt_m", geo=geo, s_adj="SA", age="Y_LT25", sex="T", unit="PC_ACT"))))
            poner("pib", lambda: _ind(*(lambda v: (v[0], "% interanual (volumen)", v[1], ue + "namq_10_gdp", "P", "PIB trimestral en volumen frente al mismo trimestre del año anterior, corregido", "trimestral"))(_eurostat("namq_10_gdp", geo=geo, s_adj="SCA", na_item="B1GQ", unit="CLV_PCH_SM"))))
            poner("deuda", lambda: _ind(*(lambda v: (v[0], "% del PIB", v[1], ue + "gov_10dd_edpt1", "P", "Deuda bruta de las administraciones públicas (Maastricht)", "anual"))(_eurostat("gov_10dd_edpt1", geo=geo, na_item="GD", sector="S13", unit="PC_GDP"))))
            poner("deficit", lambda: _ind(*(lambda v: (v[0], "% del PIB (negativo = déficit)", v[1], ue + "gov_10dd_edpt1", "P", "Capacidad (+) o necesidad (−) de financiación de las administraciones públicas", "anual"))(_eurostat("gov_10dd_edpt1", geo=geo, na_item="B9", sector="S13", unit="PC_GDP"))))
            poner("pobreza", lambda: _ind(*(lambda v: (v[0], "% de la población", v[1], ue + "ilc_peps01n", "P", "AROPE: riesgo de pobreza o exclusión social (pobreza relativa tras transferencias, privación material grave o hogares con muy baja intensidad laboral)", "anual"))(_eurostat("ilc_peps01n", geo=geo, age="TOTAL", sex="T", unit="PC"))))
            poner("gini", lambda: _ind(*(lambda v: (v[0], "puntos (0-100)", v[1], ue + "ilc_di12", "P", "Gini de la renta disponible equivalente", "anual"))(_eurostat("ilc_di12", geo=geo, age="TOTAL"))))
            poner("salario_minimo", lambda: _ind(*(lambda v: (v[0], "€ al mes", v[1], ue + "earn_mw_cur", "P", "Salario mínimo bruto mensual legal (semestral)", "semestral"))(_eurostat("earn_mw_cur", geo=geo, currency="EUR"))))
        else:
            bm = "https://data.worldbank.org/indicator/"
            poner("ipc", lambda: _ind(*(lambda v: (v[0], "% interanual (media anual)", v[1], bm + "FP.CPI.TOTL.ZG", "P", "IPC, media anual (Banco Mundial)", "anual", "El último mes sale en el panel «inflacion» si hay API abierta."))(_bm(iso, "FP.CPI.TOTL.ZG"))))
            poner("paro", lambda: _ind(*(lambda v: (v[0], "% población activa", v[1], bm + "SL.UEM.TOTL.ZS", "P", "Paro total, estimación modelo OIT (Banco Mundial)", "anual"))(_bm(iso, "SL.UEM.TOTL.ZS"))))
            poner("paro_juvenil", lambda: _ind(*(lambda v: (v[0], "% población activa 15-24", v[1], bm + "SL.UEM.1524.ZS", "P", "Paro de 15 a 24 años, estimación modelo OIT (Banco Mundial)", "anual"))(_bm(iso, "SL.UEM.1524.ZS"))))
            poner("pib", lambda: _ind(*(lambda v: (v[0], "% anual (volumen)", v[1], bm + "NY.GDP.MKTP.KD.ZG", "P", "Crecimiento anual del PIB real (Banco Mundial)", "anual"))(_bm(iso, "NY.GDP.MKTP.KD.ZG"))))
            f = "https://www.imf.org/external/datamapper/"
            poner("deuda", lambda: _ind(*(lambda v: (v[0], "% del PIB", v[1], f + "GGXWDG_NGDP", "P", "Deuda bruta de las administraciones públicas (FMI, WEO octubre de 2026)", "anual", "Leída del navegador porque el FMI da 403 a los scripts; 2025 puede ser estimación."))(_fmi(iso, "deuda"))))
            poner("deficit", lambda: _ind(*(lambda v: (v[0], "% del PIB (negativo = déficit)", v[1], f + "GGXCNL_NGDP", "P", "Préstamo neto (+) / endeudamiento neto (−) de las administraciones públicas (FMI, WEO octubre de 2026)", "anual", "Leída del navegador porque el FMI da 403 a los scripts; 2025 puede ser estimación."))(_fmi(iso, "saldo"))))
            poner("pobreza", lambda: _ind(*(lambda v: (v[0], "% de la población", v[1], bm + "SI.POV.NAHC", "P", "Pobreza según la línea nacional de cada país (no comparable con AROPE ni entre países)", "irregular"))(_bm(iso, "SI.POV.NAHC"))))
            poner("gini", lambda: _ind(*(lambda v: (v[0], "puntos (0-100)", v[1], bm + "SI.POV.GINI", "P", "Gini (Banco Mundial; encuestas de años distintos)", "irregular"))(_bm(iso, "SI.POV.GINI"))))
        # C119: Banco Mundial v2 para los 12 países (población, electricidad per cápita, balanza corriente, gasto en defensa)
        bm = "https://data.worldbank.org/indicator/"
        poner("poblacion", lambda: _ind(*(lambda v: (v[0], "millones de habitantes", v[1], bm + "SP.POP.TOTL", "P", "Población total (Banco Mundial)", "anual"))(_bm(iso, "SP.POP.TOTL", 2, 1e6))))
        poner("electricidad_pc", lambda: _ind(*(lambda v: (v[0], "kWh por habitante", v[1], bm + "EG.USE.ELEC.KH.PC", "P", "Consumo eléctrico per cápita (Banco Mundial, datos de la AIE)", "anual"))(_bm(iso, "EG.USE.ELEC.KH.PC", 0))))
        poner("balanza_corriente", lambda: _ind(*(lambda v: (v[0], "% del PIB", v[1], bm + "BN.CAB.XOKA.GD.ZS", "P", "Balanza por cuenta corriente (Banco Mundial)", "anual"))(_bm(iso, "BN.CAB.XOKA.GD.ZS"))))
        poner("gasto_defensa", lambda: _ind(*(lambda v: (v[0], "% del PIB", v[1], bm + "MS.MIL.XPND.GD.ZS", "P", "Gasto militar (SIPRI vía Banco Mundial)", "anual", "Definición SIPRI: no coincide con la de la OTAN."))(_bm(iso, "MS.MIL.XPND.GD.ZS", 2))))
        m = manual.get(pid, {})
        for clave, dato in m.items():
            ind[clave] = dato
            fallos[:] = [x for x in fallos if not x.startswith(f"{pid}/{clave}:")]
        return {"id": pid, "pais": nombre, "indicadores": ind}, fallos

    _FIN[0] = time.monotonic() + 150       # tope de 2,5 min en total: antes, con el Banco Mundial lento, el paso entero se colgaba 15 min
    with ThreadPoolExecutor(max_workers=6) as ex:
        res = list(ex.map(lambda a: _uno(*a), PAISES))
    _FIN[0] = None
    salida = [r[0] for r in res]
    fallos = [x for r in res for x in r[1]]
    return {"paises": salida, "fallos": fallos}


if __name__ == "__main__":
    r = leer_indicadores()
    for p in r["paises"]:
        print(p["id"], {k: v["valor"] for k, v in p["indicadores"].items()})
    for x in r["fallos"]:
        print("AVISO:", x)
    sys.exit(1 if r["fallos"] else 0)
