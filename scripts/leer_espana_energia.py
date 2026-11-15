"""C283: energía (REE REData) y vivienda (INE Tempus) de España, sin IA y sin claves.
Salida: explorador/espana-energia-vivienda.json. Si una fuente falla se conserva el bloque previo del JSON.

REE REData (apidatos.ree.es): precio PVPC y spot peninsular (€/MWh, media diaria de los datos horarios/cuartohorarios),
demanda peninsular mensual (MWh) y estructura de generación nacional mensual (MWh, % del total).
INE Tempus: IPV (Índice de Precios de Vivienda, base 2015=100, trimestral; operación 15) por CCAA y total nacional, con la variación anual
calculada aquí (trimestre contra el mismo de un año antes); IPVA (Índice de Precios de Vivienda en Alquiler, operación 432, anual).

Uso:  python scripts/leer_espana_energia.py
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "espana-energia-vivienda.json"
UA = {"User-Agent": "cartera-joel/1.0 (uso personal)"}
REE = "https://apidatos.ree.es/es/datos/"
TEMPUS = "https://servicios.ine.es/wstempus/js/ES/"

IPV_CCAA = {"IPV769": "Nacional", "IPV766": "Andalucía", "IPV763": "Aragón", "IPV760": "Asturias", "IPV757": "Illes Balears",
            "IPV754": "Canarias", "IPV751": "Cantabria", "IPV748": "Castilla y León", "IPV745": "Castilla-La Mancha",
            "IPV742": "Cataluña", "IPV739": "Comunitat Valenciana", "IPV736": "Extremadura", "IPV733": "Galicia",
            "IPV730": "Comunidad de Madrid", "IPV727": "Región de Murcia", "IPV724": "Navarra", "IPV721": "País Vasco",
            "IPV718": "La Rioja", "IPV715": "Ceuta", "IPV712": "Melilla"}
# IPVA anual (total viviendas, índice, total): códigos hallados en SERIES_OPERACION/432
IPVA = {"IPVA5": "Nacional", "IPVA119": "Andalucía", "IPVA71": "Cataluña", "IPVA65": "Comunitat Valenciana",
        "IPVA47": "Comunidad de Madrid", "IPVA101": "Illes Balears"}


def get(url, intentos=3, timeout=60):
    err = None
    for i in range(intentos):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url[:90]}: {err}")


def ree(ruta, ini, fin, trunc, extra=""):
    q = f"{REE}{ruta}?start_date={ini}T00:00&end_date={fin}T23:59&time_trunc={trunc}{extra}"
    return get(q)


def precios():
    hoy = datetime.now(timezone.utc).date()
    ini, fin = hoy - timedelta(days=14), hoy - timedelta(days=1)
    d = ree("mercados/precios-mercados-tiempo-real", ini, fin, "hour")
    out, ult = {}, d["data"]["attributes"].get("last-update")
    for inc in d["included"]:
        t = inc["attributes"]["title"]
        por_dia = {}
        for v in inc["attributes"]["values"]:
            por_dia.setdefault(v["datetime"][:10], []).append(v["value"])
        minimo = 24 if t == "PVPC" else 92  # PVPC horario; spot en tramos de 15 min
        out[t] = [{"fecha": f, "media_eur_mwh": round(sum(x) / len(x), 2), "min_eur_mwh": round(min(x), 2), "max_eur_mwh": round(max(x), 2)}
                  for f, x in sorted(por_dia.items()) if len(x) >= minimo]
    return {"serie": out, "actualizado_ree": ult, "unidad": "€/MWh (media/mín/máx del día, mercado peninsular)"}


def demanda():
    hoy = datetime.now(timezone.utc).date()
    ini = hoy.replace(day=1) - timedelta(days=400)
    d = ree("demanda/evolucion", ini.replace(day=1), hoy, "month", "&geo_trunc=electric_system&geo_limit=peninsular&geo_ids=8741")
    vals = d["included"][0]["attributes"]["values"]
    return {"serie": [{"mes": v["datetime"][:7], "demanda_gwh": round(v["value"] / 1000, 1),
                       "parcial": v["datetime"][:7] == hoy.strftime("%Y-%m")} for v in vals],
            "actualizado_ree": d["data"]["attributes"].get("last-update"), "unidad": "GWh (demanda eléctrica peninsular, mensual)"}


def generacion():
    hoy = datetime.now(timezone.utc).date()
    ini = hoy.replace(day=1) - timedelta(days=380)
    d = ree("generacion/estructura-generacion", ini.replace(day=1), hoy, "month")
    meses = {}
    for inc in d["included"]:
        a = inc["attributes"]
        for v in a["values"]:
            m = meses.setdefault(v["datetime"][:7], {})
            m[a["title"]] = {"gwh": round(v["value"] / 1000, 1), "tipo": a.get("type")}
    filas = []
    for m, tec in sorted(meses.items()):
        tot = sum(x["gwh"] for k, x in tec.items() if k != "Generación total")
        ren = sum(x["gwh"] for x in tec.values() if x["tipo"] == "Renovable")
        filas.append({"mes": m, "parcial": m == hoy.strftime("%Y-%m"), "total_gwh": round(tot, 1), "renovable_gwh": round(ren, 1),
                      "renovable_pct": round(100 * ren / tot, 1) if tot else None,
                      "tecnologias_gwh": {k: x["gwh"] for k, x in tec.items()}})
    return {"serie": filas, "actualizado_ree": d["data"]["attributes"].get("last-update"),
            "unidad": "GWh (generación nacional por tecnología) y % renovable sobre el total; el último mes puede estar incompleto"}


def tempus(cod, n):
    d = get(f"{TEMPUS}DATOS_SERIE/{cod}?nult={n}&det=2")
    return d["Data"], d.get("Nombre", "").strip()


def ipv():
    out = []
    for cod, nombre in IPV_CCAA.items():
        data, _ = tempus(cod, 9)
        pts = [(f"{x['Anyo']}T{x['Periodo']['Valor']}", x["Valor"]) for x in data if x.get("Valor") is not None]
        if len(pts) < 5:
            continue
        ult, prev = pts[-1], pts[-5]
        out.append({"codigo": cod, "territorio": nombre, "ultimo_periodo": ult[0], "indice_base_2015": ult[1],
                    "mismo_trimestre_anio_anterior": prev[0], "indice_anio_anterior": prev[1],
                    "variacion_anual_pct": round(100 * (ult[1] / prev[1] - 1), 1)})
    return {"serie": out, "unidad": "índice (base 2015=100) y % de variación anual calculada sobre el índice; IPV nacional/CCAA general, trimestral"}


def ipva():
    out = []
    for cod, nombre in IPVA.items():
        data, _ = tempus(cod, 4)
        pts = [(x["Anyo"], x["Valor"]) for x in data if x.get("Valor") is not None]
        if len(pts) >= 2:
            out.append({"codigo": cod, "territorio": nombre, "anio": pts[-1][0], "indice": pts[-1][1], "anio_previo": pts[-2][0],
                        "indice_previo": pts[-2][1], "variacion_pct": round(100 * (pts[-1][1] / pts[-2][1] - 1), 1)})
    return {"serie": out, "unidad": "índice (base 2015=100), anual, total viviendas"}


def main():
    previo = {}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            previo = {}
    res = {"titulo": "España: energía eléctrica y vivienda", "nivel": "P",
           "leido": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
           "fuentes": {"ree": "https://apidatos.ree.es (REData, Red Eléctrica)", "ine": "https://servicios.ine.es/wstempus (INE Tempus)"}}
    errores = []
    for clave, fn in (("precios_electricidad", precios), ("demanda_electrica", demanda), ("generacion_electrica", generacion),
                      ("ipv_precios_vivienda", ipv), ("ipva_alquiler", ipva)):
        try:
            res[clave] = fn()
        except Exception as e:  # noqa: BLE001
            errores.append(f"{clave}: {e}")
            if clave in previo:
                res[clave] = previo[clave]
    if errores:
        res["errores"] = errores
    SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK {SALIDA.name}; errores: {len(errores)}")
    for e in errores:
        print("  ", e)
    return 0


if __name__ == "__main__":
    sys.exit(main())
