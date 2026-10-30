"""Servicios públicos y estabilidad social por país (C61): solo cifras ya publicadas por Banco Mundial y Eurostat, sin claves.

Escribe explorador/estabilidad.json. Las «lecturas» y los «hitos» se escriben a mano en explorador/estabilidad-manual.json
y se funden aquí. No inventa índices ni ordena países. Si una cifra falla, se conserva la anterior.
Uso: python scripts/estabilidad.py
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "estabilidad.json"
MANUAL = RAIZ / "explorador" / "estabilidad-manual.json"
PAISES = [("ES", "España", "ES", "ESP"), ("DE", "Alemania", "DE", "DEU"), ("FR", "Francia", "FR", "FRA"), ("IT", "Italia", "IT", "ITA"),
          ("NL", "Países Bajos", "NL", "NLD"), ("PL", "Polonia", "PL", "POL"), ("US", "EE. UU.", None, "USA"), ("CN", "China", None, "CHN"),
          ("JP", "Japón", None, "JPN"), ("IN", "India", None, "IND"), ("GB", "Reino Unido", None, "GBR"), ("RU", "Rusia", None, "RUS")]

# (dimensión, nombre, id Banco Mundial, unidad, nota de comparabilidad)
BM = [
    ("sanidad", "Gasto sanitario total", "SH.XPD.CHEX.GD.ZS", "% del PIB", "OMS GHED vía Banco Mundial; público + privado"),
    ("sanidad", "Gasto sanitario por habitante", "SH.XPD.CHEX.PC.CD", "$ corrientes", "Sin ajustar por poder adquisitivo"),
    ("sanidad", "Esperanza de vida al nacer", "SP.DYN.LE00.IN", "años", ""),
    ("sanidad", "Mortalidad infantil", "SP.DYN.IMRT.IN", "por 1.000 nacidos vivos", ""),
    ("sanidad", "Médicos", "SH.MED.PHYS.ZS", "por 1.000 hab.", "Año distinto según país; definiciones nacionales"),
    ("sanidad", "Camas hospitalarias", "SH.MED.BEDS.ZS", "por 1.000 hab.", "Año distinto según país"),
    ("infraestructuras", "Banda ancha fija", "IT.NET.BBND.P2", "suscripciones por 100 hab.", ""),
    ("infraestructuras", "Importaciones netas de energía", "EG.IMP.CONS.ZS", "% del uso de energía", "Negativo = exportador neto"),
    ("trabajo", "Empleo vulnerable (cuenta propia y familiar sin sueldo)", "SL.EMP.VULN.ZS", "% del empleo", "Aproximación al empleo informal; no es lo mismo"),
    ("educacion", "Gasto público en educación", "SE.XPD.TOTL.GD.ZS", "% del PIB", ""),
    ("seguridad", "Homicidios intencionados", "VC.IHR.PSRC.P5", "por 100.000 hab.", "UNODC vía Banco Mundial; el registro varía por país"),
    ("seguridad", "Estabilidad política y ausencia de violencia (WGI)", "GOV_WGI_PV.EST", "estimación (−2,5 a +2,5)", "Indicador de percepción de expertos y encuestas"),
    ("seguridad", "Imperio de la ley (WGI)", "GOV_WGI_RL.EST", "estimación (−2,5 a +2,5)", "Percepción"),
    ("seguridad", "Control de la corrupción (WGI)", "GOV_WGI_CC.EST", "estimación (−2,5 a +2,5)", "Percepción"),
    ("demografia", "Tasa de natalidad", "SP.DYN.CBRT.IN", "por 1.000 hab.", ""),
    ("demografia", "Hijos por mujer", "SP.DYN.TFRT.IN", "hijos", ""),
    ("demografia", "Población de 65 años o más", "SP.POP.65UP.TO.ZS", "% de la población", ""),
    ("demografia", "Ratio de dependencia", "SP.POP.DPND", "por 100 en edad de trabajar", "Menores de 15 y mayores de 64"),
    ("demografia", "Migración neta", "SM.POP.NETM", "personas (5 años)", "Estimación ONU; sumada a cinco años"),
]
# Eurostat: solo UE (dimensión, nombre, dataset, filtros, unidad, nota)
EUROSTAT = [
    ("vivienda", "Sobrecarga del coste de la vivienda", "ilc_lvho07a", {"age": "TOTAL", "sex": "T", "unit": "PC", "rskpovth": "TOTAL"}, "% de la población", "Gastos de vivienda ≥ 40 % de la renta disponible"),
    ("trabajo", "Gasto en pensiones de vejez", "spr_exp_sum", {"spdep": "OLD_AGE" if False else "TOTAL"}, "", ""),
]
EUROSTAT = EUROSTAT[:1]


def _get(url, t=60):
    r = urllib.request.Request(url, headers={"User-Agent": "cartera-joel/1.0 (uso personal)", "Accept": "application/json"})
    with urllib.request.urlopen(r, timeout=t) as f:
        return json.loads(f.read().decode("utf-8", "replace"))


def _bm(iso, ind):
    j = _get(f"https://api.worldbank.org/v2/country/{iso}/indicator/{ind}?format=json&mrnev=1")
    if len(j) < 2 or not j[1] or j[1][0]["value"] is None:
        raise ValueError("sin datos")
    f = j[1][0]
    v = f["value"]
    return (round(v, 2) if abs(v) < 10 else round(v, 1) if abs(v) < 1000 else round(v)), f["date"], "https://data.worldbank.org/indicator/" + ind


def _eurostat(dataset, geo, **filtros):
    q = urllib.parse.urlencode({"geo": geo, **filtros, "lastTimePeriod": 4}, doseq=True)
    j = _get(f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{dataset}?{q}&format=JSON")
    tiempos = {v: k for k, v in j["dimension"]["time"]["category"]["index"].items()}
    vals = {int(k): v for k, v in j["value"].items()}
    if not vals:
        raise ValueError("sin datos")
    i = max(vals)
    return round(vals[i], 1), tiempos[i], "https://ec.europa.eu/eurostat/databrowser/view/" + dataset


def main():
    previo = {}
    if SALIDA.exists():
        try:
            previo = {p["id"]: p for p in json.loads(SALIDA.read_text(encoding="utf-8")).get("paises", [])}
        except Exception:
            previo = {}
    manual = json.loads(MANUAL.read_text(encoding="utf-8")) if MANUAL.exists() else {}
    fallos, paises = [], []
    for pid, nombre, geo, iso in PAISES:
        dims = {}
        antiguo = {(c["nombre"]): c for d in previo.get(pid, {}).get("dimensiones", {}).values() for c in d.get("cifras", [])}

        def anadir(dim, nombre_c, fn, unidad, nota):
            ya = antiguo.get(nombre_c)
            if ya and ya.get("valor") is not None and "--refrescar" not in sys.argv:
                dims.setdefault(dim, {"cifras": [], "hitos": []})["cifras"].append(ya)
                return
            try:
                v, anio, fuente = fn()
                cifra = {"nombre": nombre_c, "valor": v, "unidad": unidad, "anio": anio, "fuente": fuente, "nivel": "P", "nota": nota}
            except Exception as e:
                fallos.append(f"{pid}/{nombre_c}: {type(e).__name__}: {e}")
                cifra = antiguo.get(nombre_c) or {"nombre": nombre_c, "valor": None, "unidad": unidad, "anio": None, "fuente": "", "nivel": "VERIFICAR", "nota": "sin dato"}
            dims.setdefault(dim, {"cifras": [], "hitos": []})["cifras"].append(cifra)

        for dim, n, ind, u, nota in BM:
            anadir(dim, n, lambda ind=ind: _bm(iso, ind), u, nota)
        if geo:
            for dim, n, ds, fil, u, nota in EUROSTAT:
                anadir(dim, n, lambda ds=ds, fil=fil: _eurostat(ds, geo, **fil), u, nota)
        m = manual.get(pid, {})
        for dim, extra in (m.get("dimensiones") or {}).items():
            d = dims.setdefault(dim, {"cifras": [], "hitos": []})
            d["cifras"] += extra.get("cifras", [])
            d["hitos"] += extra.get("hitos", [])
        paises.append({"id": pid, "pais": nombre, "dimensiones": dims, "lectura": m.get("lectura")})
    salida = {"titulo": "Servicios públicos y estabilidad social", "leido": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
              "nota": "Solo cifras publicadas por organismos (Banco Mundial/OMS/UNODC, Eurostat) con su año y definición; ningún índice propio ni ranking. «null»/sin dato = no publicado o no leído. Los indicadores de gobernanza (WGI) son percepciones. Lecturas = [OPINIÓN]/[ESPECULACIÓN].",
              "paises": paises, "fallos": fallos}
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sin = sum(1 for p in paises for d in p["dimensiones"].values() for c in d["cifras"] if c["valor"] is None)
    print(f"estabilidad.json: {len(paises)} países, {sum(len(d['cifras']) for p in paises for d in p['dimensiones'].values())} cifras, {sin} sin dato")
    for f in fallos:
        print("AVISO:", f)
    return 0


if __name__ == "__main__":
    sys.exit(main())
