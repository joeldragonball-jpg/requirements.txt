"""Paneles nuevos de actualizar_paneles.py (C110 electricidad, C112 alimentos, C113 chips). Sin IA y sin claves.

Cada función recibe el bloque anterior de paneles.json (o None): si una fuente falla se conserva su dato previo
y se anota en «fallos». Cada serie lleva el campo «desde» (primer dato de la serie) para no confundir cobertura con historia.
"""
import csv
import io
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

import yahoo_diario

UA = {"User-Agent": "Mozilla/5.0 (cartera-joel/1.0 uso personal)"}
URL_YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/{s}?range=1mo&interval=1d"
URL_EUROSTAT = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{t}?format=JSON&lang=EN&{q}"


def _get(url, t=40, reintentos=2):
    for i in range(reintentos + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=t) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:
            if i == reintentos:
                raise
            time.sleep(2 * (i + 1))


def _fred(sid, desde="2024-01-01"):
    texto = _get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd={desde}", t=20, reintentos=1)
    return [(f, float(v)) for f, v in list(csv.reader(io.StringIO(texto)))[1:] if v not in (".", "")]


def _yahoo(simbolo):
    d = json.loads(_get(URL_YAHOO.format(s=urllib.parse.quote(simbolo))))["chart"]["result"][0]
    pares = yahoo_diario.cierres(d)   # fecha de la sesión en hora de la bolsa (C132)
    if len(pares) < 3:
        raise ValueError("menos de 3 cierres")
    (f0, c0), (f1, c1) = pares[-2], pares[-1]
    return {"simbolo": simbolo, "valor": round(c1, 3), "fecha": f1, "cambio_1d": round((c1 / c0 - 1) * 100, 2),
            "cambio_1m": round((c1 / pares[0][1] - 1) * 100, 1), "desde": pares[0][0]}


def _serie_fred(sid, nombre, unidad, desde="2024-01-01"):
    s = _fred(sid, desde)
    if len(s) < 3:
        raise ValueError("menos de 3 datos")
    (f0, v0), (f1, v1) = s[-2], s[-1]
    ref = next((v for f, v in s if f[:4] == str(int(f1[:4]) - 1) and f[5:7] == f1[5:7]), None)
    return {"id": sid, "nombre": nombre, "unidad": unidad, "valor": round(v1, 3), "fecha": f1[:7], "mes_anterior": round(v0, 3),
            "cambio_mensual": round((v1 / v0 - 1) * 100, 2), "interanual": round((v1 / ref - 1) * 100, 1) if ref else None,
            "desde": s[0][0][:7], "url": f"https://fred.stlouisfed.org/series/{sid}"}


# ---------- C110: electricidad ----------

def _omie_dia(fecha):
    """Precio marginal del mercado diario (€/MWh, zona España) de un día: media, mín y máx de sus periodos."""
    url = f"https://www.omie.es/es/file-download?parents%5B0%5D=marginalpdbc&filename=marginalpdbc_{fecha:%Y%m%d}.1"
    valores = []
    for linea in _get(url).splitlines():
        p = linea.strip().rstrip(";").split(";")
        if len(p) >= 6 and p[0].isdigit():
            try:
                valores.append(float(p[5].replace(",", ".")))      # columna 5 = España (6 = Portugal)
            except ValueError:
                pass
    if not valores:
        raise ValueError(f"OMIE {fecha:%Y-%m-%d}: archivo sin datos")
    return {"fecha": f"{fecha:%Y-%m-%d}", "media": round(sum(valores) / len(valores), 2), "min": min(valores), "max": max(valores), "periodos": len(valores)}


def _ree_pvpc():
    hoy = datetime.now(timezone.utc)
    ini, fin = (hoy - timedelta(days=7)).strftime("%Y-%m-%dT00:00"), (hoy + timedelta(days=1)).strftime("%Y-%m-%dT23:59")
    d = json.loads(_get(f"https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date={ini}&end_date={fin}&time_trunc=hour"))
    por_dia = {}
    for serie in d["included"]:
        if serie["attributes"]["title"] != "PVPC":
            continue
        for v in serie["attributes"]["values"]:
            por_dia.setdefault(v["datetime"][:10], []).append(v["value"])
    if not por_dia:
        raise ValueError("REE: sin serie PVPC")
    return [{"fecha": f, "media": round(sum(v) / len(v), 2), "min": min(v), "max": max(v), "horas": len(v)} for f, v in sorted(por_dia.items())]


EUROSTAT_PAISES = (("ES", "España"), ("DE", "Alemania"), ("FR", "Francia"), ("IT", "Italia"), ("PT", "Portugal"))
EUROSTAT_TABLAS = (("nrg_pc_204", "hogares", "nrg_cons=KWH2500-4999", "Hogares (2 500-4 999 kWh/año), impuestos incluidos"),
                   ("nrg_pc_205", "empresas", "nrg_cons=MWH500-1999", "No domésticos (500-1 999 MWh/año), impuestos incluidos"))


def _eurostat_precio(tabla, consumo):
    q = "&".join(f"geo={g}" for g, _ in EUROSTAT_PAISES) + f"&freq=S&{consumo}&tax=I_TAX&currency=EUR&unit=KWH&sinceTimePeriod=2024-S1"
    d = json.loads(_get(URL_EUROSTAT.format(t=tabla, q=q)))
    geos, tiempos = d["dimension"]["geo"]["category"]["index"], d["dimension"]["time"]["category"]["index"]
    n_t = len(tiempos)
    filas = []
    for g, nombre in EUROSTAT_PAISES:
        if g not in geos:
            continue
        serie = sorted((t, d["value"].get(str(geos[g] * n_t + i))) for t, i in tiempos.items())
        serie = [(t, v) for t, v in serie if v is not None]
        if serie:
            filas.append({"id": g, "pais": nombre, "periodo": serie[-1][0], "eur_kwh": serie[-1][1],
                          "periodo_anterior": serie[-2][0] if len(serie) > 1 else None, "anterior_eur_kwh": serie[-2][1] if len(serie) > 1 else None,
                          "desde": serie[0][0]})
    if not filas:
        raise ValueError(f"Eurostat {tabla}: sin datos")
    return {"actualizado": d.get("updated", "")[:10], "paises": filas}


def leer_electricidad(previo=None):
    previo = previo or {}
    salida = {"fuente": "OMIE (mercado diario), REE (PVPC) y Eurostat nrg_pc_204/205", "nivel": "P", "unidad_mercado": "€/MWh", "unidad_eurostat": "€/kWh", "fallos": []}
    hoy = datetime.now(timezone.utc)
    dias = []
    for k in range(0, 9):                                   # OMIE publica hoy sobre las 13:00 para el día siguiente
        try:
            dias.append(_omie_dia(hoy + timedelta(days=1 - k)))
        except Exception as e:
            if k > 1:
                salida["fallos"].append(f"OMIE {(hoy + timedelta(days=1 - k)):%Y-%m-%d}: {type(e).__name__}: {e}")
        if len(dias) >= 7:
            break
    dias.sort(key=lambda x: x["fecha"])
    salida["omie_diario"] = dias or previo.get("omie_diario", [])
    if salida["omie_diario"]:
        salida["omie_desde"] = salida["omie_diario"][0]["fecha"]
    try:
        salida["pvpc_diario"] = _ree_pvpc()
        salida["pvpc_desde"] = salida["pvpc_diario"][0]["fecha"]
    except Exception as e:
        salida["fallos"].append(f"REE PVPC: {type(e).__name__}: {e}")
        salida["pvpc_diario"] = previo.get("pvpc_diario", [])
    salida["eurostat"] = {}
    for tabla, clave, consumo, nombre in EUROSTAT_TABLAS:
        try:
            salida["eurostat"][clave] = {"tabla": tabla, "nombre": nombre, **_eurostat_precio(tabla, consumo)}
        except Exception as e:
            salida["fallos"].append(f"Eurostat {tabla}: {type(e).__name__}: {e}")
            if clave in previo.get("eurostat", {}):
                salida["eurostat"][clave] = previo["eurostat"][clave]
    salida["nota"] = ("OMIE: media del precio marginal del mercado diario (zona España); desde 2025 son periodos de 15 min. PVPC: tarifa regulada, media horaria "
                      "de REE. Eurostat: semestral, con retraso de meses. Zonas FR/DE/IT/PT en el mercado mayorista: pendiente de ENTSO-E (C111).")
    if not (salida["omie_diario"] or salida["pvpc_diario"] or salida["eurostat"]):
        raise ValueError("ninguna fuente de electricidad disponible")
    return salida


# ---------- C112: alimentos ----------

FRED_ALIMENTOS = (("PSOYBUSDM", "Soja", "$ por tonelada"), ("PWHEAMTUSDM", "Trigo", "$ por tonelada"), ("PMAIZMTUSDM", "Maíz", "$ por tonelada"),
                  ("PRICENPQUSDM", "Arroz", "$ por tonelada"), ("PSUGAISAUSDM", "Azúcar", "centavos por libra"))
YAHOO_ALIMENTOS = (("ZS=F", "Soja (futuro)", "centavos por bushel"), ("ZR=F", "Arroz bruto (futuro)", "$ por quintal"), ("SB=F", "Azúcar nº11 (futuro)", "centavos por libra"),
                   ("CC=F", "Cacao (futuro, Nueva York)", "$ por tonelada"))
URL_FAO = "https://www.fao.org/worldfoodsituation/foodpricesindex/en/"


def _fao():
    html_ = _get(URL_FAO)
    m = re.search(r'href="(https://www\.fao\.org/media/docs/[^"]*food_price_indices_data\.csv[^"]*)"', html_)
    if not m:
        raise ValueError("FAO: no aparece el enlace del CSV (¿cambió la página?)")
    texto = _get(m.group(1).replace("&amp;", "&"))
    filas = [f for f in csv.reader(io.StringIO(texto)) if f]
    cab = next(i for i, f in enumerate(filas) if f[0].strip().lower() == "date")
    nombres = [c.strip() for c in filas[cab]]
    datos = []
    for f in filas[cab + 1:]:
        if re.match(r"\d{4}-\d{2}", f[0].strip()) and len(f) > 1:
            try:
                datos.append((f[0].strip()[:7], [float(x) if x.strip() else None for x in f[1:len(nombres)]]))
            except ValueError:
                continue
    if len(datos) < 14:
        raise ValueError("FAO: CSV con menos de 14 meses")
    (m1, v1), ref = datos[-1], dict(datos).get(f"{int(datos[-1][0][:4]) - 1}{datos[-1][0][4:]}")
    indices = []
    for i, n in enumerate(nombres[1:]):
        if v1[i] is not None:
            indices.append({"nombre": n, "valor": v1[i], "mes_anterior": datos[-2][1][i], "hace_12m": ref[i] if ref else None,
                            "interanual": round((v1[i] / ref[i] - 1) * 100, 1) if ref and ref[i] else None})
    return {"fuente": URL_FAO, "nivel": "P", "mes": m1, "desde": datos[0][0], "base": "2014-2016 = 100", "indices": indices}


def leer_alimentos(previo=None):
    previo = previo or {}
    salida = {"nivel": "P/S", "fuente": "FAO (índice, [P]), FRED/Banco Mundial (precios mensuales, [P]) y Yahoo Finance (futuros, [S])", "fallos": []}
    try:
        salida["fao"] = _fao()
    except Exception as e:
        salida["fallos"].append(f"FAO: {type(e).__name__}: {e}")
        if previo.get("fao"):
            salida["fao"] = previo["fao"]
    salida["fred"] = []
    for sid, nombre, unidad in FRED_ALIMENTOS:
        try:
            salida["fred"].append(_serie_fred(sid, nombre, unidad))
        except Exception as e:
            salida["fallos"].append(f"FRED {sid}: {type(e).__name__}: {e}")
            prev = next((x for x in previo.get("fred", []) if x["id"] == sid), None)
            if prev:
                salida["fred"].append(prev)
            if "no responde" in str(e) or isinstance(e, (TimeoutError, OSError)):
                break                                         # FRED caído: no insistir con el resto
    salida["futuros"] = []
    for simbolo, nombre, unidad in YAHOO_ALIMENTOS:
        try:
            salida["futuros"].append({**_yahoo(simbolo), "nombre": nombre, "unidad": unidad, "nivel": "S"})
        except Exception as e:
            salida["fallos"].append(f"Yahoo {simbolo}: {type(e).__name__}: {e}")
            prev = next((x for x in previo.get("futuros", []) if x["simbolo"] == simbolo), None)
            if prev:
                salida["futuros"].append(prev)
    if not (salida.get("fao") or salida["fred"] or salida["futuros"]):
        raise ValueError("ninguna fuente de alimentos disponible")
    return salida


# ---------- C113: chips ----------

FRED_CHIPS = (("IPG3344S", "Producción industrial de semiconductores y componentes (EE. UU., índice 2017=100)", "índice"),
              ("PCU334413334413", "Precios de productor de semiconductores (EE. UU., índice)", "índice"))
YAHOO_CHIPS = (("SOXX", "iShares Semiconductor ETF"), ("TSM", "TSMC (ADR)"), ("ASML", "ASML (ADR)"), ("MU", "Micron"))


def leer_chips(previo=None):
    previo = previo or {}
    salida = {"nivel": "P/S", "fuente": "FRED (Reserva Federal/BLS, [P]) y Yahoo Finance (cotizaciones, [S])", "fallos": []}
    salida["produccion"] = []
    for sid, nombre, unidad in FRED_CHIPS:
        try:
            salida["produccion"].append(_serie_fred(sid, nombre, unidad))
        except Exception as e:
            salida["fallos"].append(f"FRED {sid}: {type(e).__name__}: {e}")
            prev = next((x for x in previo.get("produccion", []) if x["id"] == sid), None)
            if prev:
                salida["produccion"].append(prev)
    salida["cotizaciones"] = []
    for simbolo, nombre in YAHOO_CHIPS:
        try:
            salida["cotizaciones"].append({**_yahoo(simbolo), "nombre": nombre, "nivel": "S"})
        except Exception as e:
            salida["fallos"].append(f"Yahoo {simbolo}: {type(e).__name__}: {e}")
            prev = next((x for x in previo.get("cotizaciones", []) if x["simbolo"] == simbolo), None)
            if prev:
                salida["cotizaciones"].append(prev)
    salida["nota"] = "Cotizaciones de Yahoo = nivel S (no oficial). Solo datos; sin recomendaciones."
    if not (salida["produccion"] or salida["cotizaciones"]):
        raise ValueError("ninguna fuente de chips disponible")
    return salida
