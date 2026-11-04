"""C115: muertes en carretera (Eurostat tran_sf_roadus) y delitos registrados por la policía (Eurostat crim_off_cat) de ES/FR/DE/IT/PT.
Sin IA y sin claves. Salida: explorador/seguridad-eurostat.json (serie anual, con nota de definición por país).

Uso:  python scripts/leer_seguridad_eurostat.py
Si una fuente falla se conserva lo anterior. Los delitos NO son comparables entre países sin leer las notas (cada policía registra distinto).
"""
import json
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "seguridad-eurostat.json"
BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{t}?format=JSON&lang=EN&{q}"
PAISES = (("ES", "España"), ("FR", "Francia"), ("DE", "Alemania"), ("IT", "Italia"), ("PT", "Portugal"))
GEO = "&".join(f"geo={g}" for g, _ in PAISES)
DESDE = "2015"
DELITOS = {"ICCS0101": "Homicidio doloso", "ICCS020111": "Agresión grave", "ICCS0301": "Violencia sexual", "ICCS0401": "Robo con violencia",
           "ICCS0501": "Robo con fuerza (allanamiento)", "ICCS05012": "Robo en vivienda", "ICCS0502": "Hurto", "ICCS05021": "Robo de vehículo o piezas",
           "ICCS0601": "Drogas", "ICCS0701": "Fraude", "ICCS0903": "Ataques a sistemas informáticos"}
NOTA_DELITOS = {
    "DE": "[VERIFICAR] Alemania: estadística policial (PKS) con recuento de casos resueltos y no resueltos; el hurto y el robo se desglosan distinto que en España.",
    "FR": "[VERIFICAR] Francia: hechos registrados por policía y gendarmería; las denuncias online y las agresiones se contabilizan con criterios propios.",
    "ES": "[VERIFICAR] España: delitos conocidos por policía y Guardia Civil (Balance de Criminalidad); el fraude informático se suma a estafas.",
    "IT": "[VERIFICAR] Italia: delitos denunciados a las fuerzas del orden; algunas series tienen revisiones retroactivas.",
    "PT": "[VERIFICAR] Portugal: participaciones registradas por las fuerzas de seguridad; posibles cambios de criterio entre años.",
}


def _eurostat(tabla, q):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(BASE.format(t=tabla, q=q), headers={"User-Agent": "cartera-joel/1.0 (uso personal)"}), timeout=60) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception:
            if i == 2:
                raise
            time.sleep(3 * (i + 1))


def _series(j, dims_fijas):
    """Devuelve {(geo, claves de la dim variable): {año: valor}}; dims_fijas son las dimensiones de tamaño 1 o ya filtradas."""
    ids, size = j["id"], j["size"]
    cats = {k: list(j["dimension"][k]["category"]["index"]) for k in ids}
    salida = {}
    for pos_str, v in j["value"].items():
        pos, idx = int(pos_str), {}
        for k, n in zip(reversed(ids), reversed(size)):
            idx[k] = cats[k][pos % n]
            pos //= n
        salida.setdefault(tuple(idx[k] for k in ids if k not in ("time", "freq")), {})[idx["time"]] = v
    return salida


def muertes():
    q = f"{GEO}&sex=T&age=TOTAL&pers_cat=TOTAL&sinceTimePeriod={DESDE}"
    j = _eurostat("tran_sf_roadus", q)
    s = _series(j, None)
    ids = [k for k in j["id"] if k not in ("time", "freq")]
    pos_unit, pos_geo = ids.index("unit"), ids.index("geo")
    filas = []
    for g, nombre in PAISES:
        nr = next((v for k, v in s.items() if k[pos_geo] == g and k[pos_unit] == "NR"), {})
        tasa = next((v for k, v in s.items() if k[pos_geo] == g and k[pos_unit] == "P_MHAB"), {})
        if nr:
            a = max(nr)
            filas.append({"id": g, "pais": nombre, "anio": a, "muertes": nr[a], "por_millon_hab": tasa.get(a), "serie": {k: nr[k] for k in sorted(nr)},
                          "serie_por_millon": {k: tasa[k] for k in sorted(tasa)}, "desde": min(nr)})
    if not filas:
        raise ValueError("tran_sf_roadus sin datos")
    return {"tabla": "tran_sf_roadus", "actualizado": j.get("updated", "")[:10], "unidad": "muertos en accidente de carretera (a 30 días) y por millón de habitantes",
            "fuente": "https://ec.europa.eu/eurostat/databrowser/view/tran_sf_roadus", "nivel": "P", "paises": filas}


def delitos():
    cods = "&".join(f"iccs={c}" for c in DELITOS)
    j = _eurostat("crim_off_cat", f"{GEO}&{cods}&unit=NR&sinceTimePeriod={DESDE}")
    s = _series(j, None)
    ids = [k for k in j["id"] if k not in ("time", "freq")]
    pos_i, pos_g = ids.index("iccs"), ids.index("geo")
    filas = []
    for g, nombre in PAISES:
        cat = {}
        for c, etiqueta in DELITOS.items():
            serie = next((v for k, v in s.items() if k[pos_g] == g and k[pos_i] == c), {})
            if serie:
                a = max(serie)
                cat[c] = {"delito": etiqueta, "anio": a, "registrados": serie[a], "serie": {k: serie[k] for k in sorted(serie)}}
        if cat:
            filas.append({"id": g, "pais": nombre, "nota_definicion": NOTA_DELITOS[g], "delitos": cat, "desde": DESDE})
    if not filas:
        raise ValueError("crim_off_cat sin datos")
    return {"tabla": "crim_off_cat", "actualizado": j.get("updated", "")[:10], "unidad": "delitos registrados por la policía (número, no tasa)",
            "fuente": "https://ec.europa.eu/eurostat/databrowser/view/crim_off_cat", "nivel": "P", "paises": filas,
            "aviso": "No comparar el nivel entre países: cada policía y cada código penal registran distinto. Es útil para ver la tendencia dentro de un mismo país."}


def main():
    previo = {}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        except Exception:
            previo = {}
    salida, fallos = {"titulo": "Seguridad vial y delitos (Eurostat)", "leido": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}, []
    for clave, f in (("carretera", muertes), ("delitos", delitos)):
        try:
            salida[clave] = f()
        except Exception as e:
            fallos.append(f"{clave}: {type(e).__name__}: {e}")
            if clave in previo:
                salida[clave] = previo[clave]
    salida["fallos"] = fallos
    if "carretera" not in salida and "delitos" not in salida:
        print("AVISO: ninguna fuente disponible; no se escribe")
        return 1
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for p in salida.get("carretera", {}).get("paises", []):
        print(f"Carretera {p['id']} {p['anio']}: {p['muertes']} muertos ({p['por_millon_hab']} por millón)")
    for p in salida.get("delitos", {}).get("paises", []):
        h = p["delitos"].get("ICCS0101")
        print(f"Delitos {p['id']}: {len(p['delitos'])} categorías" + (f"; homicidios {h['anio']}: {h['registrados']}" if h else ""))
    for f in fallos:
        print("AVISO (se conserva lo anterior si existía):", f)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
