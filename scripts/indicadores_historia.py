"""Series históricas cortas de los indicadores de Países (C133): Eurostat (UE) y Banco Mundial (resto), sin claves ni IA.

Guarda explorador/indicadores-historia.json con una serie por país e indicador desde 2010 (mensual, trimestral o anual).
La vista de Países calcula con ella: hace 2 y 5 años, máximo y mínimo de la serie (con su rango de años) y el cambio
durante el mandato (fechas en explorador/mandatos.json). Deuda y déficit fuera de la UE salen del FMI: el FMI da 403
a los scripts, así que se leen en el navegador y se guardan en explorador/indicadores-historia-fmi.json (si no existe,
esas series quedan «sin serie»). Uso: python scripts/indicadores_historia.py
"""
import json
import sys
import urllib.parse
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from indicadores import PAISES, URL_EUROSTAT, _get  # mismas fuentes y países que el panel de indicadores

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "indicadores-historia.json"
FMI_MANUAL = RAIZ / "explorador" / "indicadores-historia-fmi.json"
DESDE = 2010
SERIES_DESDE = {"ES": 2000}   # España llega hasta Aznar (C136); el resto, desde 2010
UE = "https://ec.europa.eu/eurostat/databrowser/view/"
BM = "https://data.worldbank.org/indicator/"
URL_BM = "https://api.worldbank.org/v2/country/{c}/indicator/{i}?format=json&date={a}:{b}&per_page=100"

# clave: (dataset, filtros, unidad) para la UE
EUROSTAT = {
    "ipc": ("prc_hicp_minr", {"coicop18": "TOTAL", "unit": "RCH_A"}, "% interanual"),
    "paro": ("une_rt_m", {"s_adj": "SA", "age": "TOTAL", "sex": "T", "unit": "PC_ACT"}, "% población activa"),
    "paro_juvenil": ("une_rt_m", {"s_adj": "SA", "age": "Y_LT25", "sex": "T", "unit": "PC_ACT"}, "% población activa"),
    "pib": ("namq_10_gdp", {"s_adj": "SCA", "na_item": "B1GQ", "unit": "CLV_PCH_SM"}, "% interanual (volumen)"),
    "deuda": ("gov_10dd_edpt1", {"na_item": "GD", "sector": "S13", "unit": "PC_GDP"}, "% del PIB"),
    "deficit": ("gov_10dd_edpt1", {"na_item": "B9", "sector": "S13", "unit": "PC_GDP"}, "% del PIB"),
    "pobreza": ("ilc_peps01n", {"age": "TOTAL", "sex": "T", "unit": "PC"}, "% de la población (AROPE)"),
    "pobreza_infantil": ("ilc_peps01n", {"age": "Y_LT18", "sex": "T", "unit": "PC"}, "% de menores de 18 (AROPE)"),
    "gini": ("ilc_di12", {"age": "TOTAL"}, "puntos (0-100)"),
}
# el IPC armonizado cambió de dataset (ECOICOP 2) en 2026; la serie larga anterior sigue en prc_hicp_manr
IPC_ANTIGUO = ("prc_hicp_manr", {"coicop": "CP00", "unit": "RCH_A"})
BANCO_MUNDIAL = {
    "ipc": ("FP.CPI.TOTL.ZG", "% interanual (media anual)"),
    "paro": ("SL.UEM.TOTL.ZS", "% población activa (modelo OIT)"),
    "paro_juvenil": ("SL.UEM.1524.ZS", "% población activa 15-24 (modelo OIT)"),
    "pib": ("NY.GDP.MKTP.KD.ZG", "% anual (volumen)"),
    "pobreza": ("SI.POV.NAHC", "% bajo la línea nacional"),
    "gini": ("SI.POV.GINI", "puntos (0-100)"),
}
# estadísticas oficiales con fiabilidad discutida: se marcan [S] y se avisa en pantalla
DUDOSAS = {"CN": "Las cifras oficiales de China (PIB, paro) se revisan poco y varios estudios las consideran suavizadas; se muestran como [S].",
           "RU": "Desde 2022 Rusia publica menos datos y algunos con retraso o sin desglose; se muestran como [S]."}


def _eurostat_serie(dataset, geo, filtros, desde=DESDE):
    q = urllib.parse.urlencode({**filtros, "geo": geo, "sinceTimePeriod": str(desde) if dataset.startswith(("gov_", "ilc_")) else f"{desde}-01" if dataset != "namq_10_gdp" else f"{desde}-Q1"}, doseq=True)
    j = _get(URL_EUROSTAT.format(d=dataset, q=q), 60)
    tiempos = {v: k for k, v in j["dimension"]["time"]["category"]["index"].items()}
    return {tiempos[int(k)]: round(v, 1) for k, v in j["value"].items()}, j.get("updated", "")[:10]


def _bm_serie(iso, ind, anio_fin):
    try:
        j = _get(URL_BM.format(c=iso, i=ind, a=DESDE, b=anio_fin), 60)
    except TimeoutError:
        j = _get(URL_BM.format(c=iso, i=ind, a=DESDE, b=anio_fin), 90)
    if len(j) < 2 or not j[1]:
        return {}, ""
    return {x["date"]: round(x["value"], 1) for x in j[1] if x.get("value") is not None}, j[0].get("lastupdated", "")


def _frec(periodos):
    p = next(iter(periodos))
    return "M" if "-" in p and "Q" not in p else "T" if "Q" in p else "A"


def _compacta(d):
    """{periodo: valor} → {"frec", "desde", "hasta", "p": [...], "v": [...]} ordenado (periodos explícitos: hay huecos en las anuales)."""
    ks = sorted(d)
    return {"frec": _frec(ks), "desde": ks[0], "hasta": ks[-1], "p": ks, "v": [d[k] for k in ks]}


def main():
    hoy = date.today()
    fmi = json.loads(FMI_MANUAL.read_text(encoding="utf-8")) if FMI_MANUAL.exists() else {}
    salida, fallos = {}, []
    for pid, _nombre, geo, iso in PAISES:
        series = {}
        if geo:
            for clave, (ds, fil, unidad) in EUROSTAT.items():
                try:
                    d, act = _eurostat_serie(ds, geo, fil, SERIES_DESDE.get(pid, DESDE))
                    fuente = UE + ds
                    if clave == "ipc":   # se une la serie antigua (hasta 2025) con la nueva ECOICOP 2
                        try:
                            viejo, _ = _eurostat_serie(IPC_ANTIGUO[0], geo, IPC_ANTIGUO[1], SERIES_DESDE.get(pid, DESDE))
                            d = {**viejo, **d}
                            fuente += " (y prc_hicp_manr hasta su cierre)"
                        except Exception as e:
                            fallos.append(f"{pid}/ipc antiguo: {type(e).__name__}: {e}")
                    if not d:
                        raise ValueError("sin datos")
                    series[clave] = {**_compacta(d), "unidad": unidad, "fuente": fuente, "nivel": "P", "actualizado": act}
                except Exception as e:
                    fallos.append(f"{pid}/{clave}: {type(e).__name__}: {e}")
        else:
            for clave, (ind, unidad) in BANCO_MUNDIAL.items():
                try:
                    d, act = _bm_serie(iso, ind, hoy.year)
                    if not d:
                        raise ValueError("sin datos")
                    series[clave] = {**_compacta(d), "unidad": unidad, "fuente": BM + ind, "nivel": "S" if pid in DUDOSAS else "P", "actualizado": act}
                except Exception as e:
                    fallos.append(f"{pid}/{clave}: {type(e).__name__}: {e}")
            for clave in ("deuda", "deficit"):
                d = (fmi.get(iso) or {}).get(clave)
                if d:   # solo años ya cerrados: el WEO trae previsiones hasta 2031 y aquí no se mezclan
                    d = {k: v for k, v in d.items() if int(k) >= DESDE and int(k) < hoy.year and v is not None}
                    if d:
                        series[clave] = {**_compacta(d), "unidad": "% del PIB", "fuente": "https://www.imf.org/external/datamapper/" + ("GGXWDG_NGDP" if clave == "deuda" else "GGXCNL_NGDP"),
                                         "nivel": "S" if iso in ("CHN", "RUS") else "P", "actualizado": fmi.get("_leido", ""), "nota": "FMI, WEO " + fmi.get("_edicion", "") + "; el último año puede ser estimación."}
        salida[pid] = series
    out = {"generado": hoy.isoformat(), "desde": DESDE,
           "nota": "Series desde " + str(DESDE) + ". UE: Eurostat; resto: Banco Mundial (anual) y FMI (deuda y déficit). Solo cifras publicadas; sin serie = no se muestra.",
           "dudosas": DUDOSAS, "paises": salida, "fallos": fallos}
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{SALIDA.name}: {sum(len(s) for s in salida.values())} series, {len(fallos)} fallos")
    for f in fallos:
        print("  ·", f)


if __name__ == "__main__":
    main()
