"""España: ingresos públicos, impuestos y gasto por funciones (C65). Solo cifras publicadas por Eurostat (sin claves ni IA).

Escribe explorador/espana.json. Lo que no tiene API abierta (AEAT mensual, SEPE, ayuda exterior, préstamos, rescates) va a
explorador/espana-manual.json y se funde aquí con su nivel y fuente. No inventa índices ni ordena países.
Uso: python scripts/espana_fiscal.py
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "espana.json"
MANUAL = RAIZ / "explorador" / "espana-manual.json"
BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
VISTA = "https://ec.europa.eu/eurostat/databrowser/view/"


def _serie(dataset, n=14, **f):
    q = urllib.parse.urlencode({"geo": "ES", **f, "lastTimePeriod": n}, doseq=True)
    r = urllib.request.Request(f"{BASE}{dataset}?{q}&format=JSON", headers={"User-Agent": "cartera-joel/1.0 (uso personal)"})
    with urllib.request.urlopen(r, timeout=60) as x:
        j = json.loads(x.read().decode("utf-8", "replace"))
    t = {v: k for k, v in j["dimension"]["time"]["category"]["index"].items()}
    s = {t[int(k)]: v for k, v in j["value"].items()}
    if not s:
        raise ValueError("sin datos")
    return dict(sorted(s.items())), j.get("updated", "")[:10]


# (id, grupo, nombre, dataset, filtros)
M = "MIO_EUR"
EXP = lambda c: ("gov_10a_exp", dict(cofog99=c, sector="S13", na_item="TE", unit=M))
TAX = lambda n: ("gov_10a_taxag", dict(na_item=n, sector="S13", unit=M))
MAIN = lambda n: ("gov_10a_main", dict(na_item=n, sector="S13", unit=M))
INDIC = [
    ("ingresos", "Ingresos", "Ingresos totales de las administraciones públicas", *MAIN("TR")),
    ("gasto", "Gasto", "Gasto total de las administraciones públicas", *MAIN("TE")),
    ("imp_produccion", "Ingresos", "Impuestos sobre la producción y la importación (IVA, especiales, otros)", *TAX("D2")),
    ("imp_renta", "Ingresos", "Impuestos sobre la renta y el patrimonio (IRPF, sociedades, otros)", *TAX("D5")),
    ("cotizaciones", "Ingresos", "Cotizaciones sociales efectivas e imputadas", *TAX("D61")),
    ("f_proteccion", "Gasto por función", "Protección social (total)", *EXP("GF10")),
    ("f_vejez", "Gasto por función", "  · Pensiones de vejez", *EXP("GF1002")),
    ("f_enfermedad", "Gasto por función", "  · Enfermedad e invalidez", *EXP("GF1001")),
    ("f_paro", "Gasto por función", "  · Desempleo (prestaciones y subsidios)", *EXP("GF1005")),
    ("f_familia", "Gasto por función", "  · Familia e hijos", *EXP("GF1004")),
    ("f_exclusion", "Gasto por función", "  · Exclusión social", *EXP("GF1007")),
    ("f_vivienda_soc", "Gasto por función", "  · Ayudas a la vivienda (protección social)", *EXP("GF1006")),
    ("f_sanidad", "Gasto por función", "Sanidad", *EXP("GF07")),
    ("f_educacion", "Gasto por función", "Educación", *EXP("GF09")),
    ("f_economicos", "Gasto por función", "Asuntos económicos (transporte, energía, agricultura…)", *EXP("GF04")),
    ("f_orden", "Gasto por función", "Orden público y seguridad", *EXP("GF03")),
    ("f_defensa", "Gasto por función", "Defensa", *EXP("GF02")),
    ("f_medioambiente", "Gasto por función", "Medio ambiente", *EXP("GF05")),
    ("f_vivienda", "Gasto por función", "Vivienda y servicios comunitarios", *EXP("GF06")),
    ("f_cultura", "Gasto por función", "Cultura y ocio", *EXP("GF08")),
    ("f_servicios", "Gasto por función", "Servicios generales (administración)", *EXP("GF01")),
    ("f_intereses", "Gasto por función", "  · Intereses de la deuda", *EXP("GF0107")),
    ("f_ayuda_ext", "Gasto por función", "  · Ayuda económica exterior (función COFOG 01.2)", *EXP("GF0102")),
    ("inversion", "Gasto", "Inversión pública (formación bruta de capital)", *MAIN("P51G")),
]


# Resultados que se pueden leer de Eurostat para España y la UE-27: (id, nombre, unidad, dataset, filtros)
RESULTADOS = [
    ("espera_medica", "Necesidad médica no atendida por coste, distancia o lista de espera", "% de la población de 16 años o más", "hlth_silc_08", dict(unit="PC", quant_inc="TOTAL", reason="TXP_TFAR_WLIST", age="Y_GE16", sex="T")),
    ("espera_lista", "  · solo por lista de espera", "% de la población de 16 años o más", "hlth_silc_08", dict(unit="PC", quant_inc="TOTAL", reason="WLIST", age="Y_GE16", sex="T")),
    ("sobrecarga_vivienda", "Sobrecarga del coste de la vivienda (≥ 40 % de la renta)", "% de la población", "ilc_lvho07a", dict(age="TOTAL", sex="T", unit="PC", rskpovth="TOTAL")),
    ("pobreza_exclusion", "Riesgo de pobreza o exclusión social (AROPE)", "% de la población", "ilc_peps01n", dict(age="TOTAL", sex="T", unit="PC")),
]


def main():
    previo = {}
    if SALIDA.exists():
        try:
            previo = {i["id"]: i for i in json.loads(SALIDA.read_text(encoding="utf-8")).get("indicadores", [])}
        except Exception:
            previo = {}
    fallos, ind = [], []
    for iid, grupo, nombre, ds, fil in INDIC:
        try:
            s, upd = _serie(ds, **fil)
            ind.append({"id": iid, "grupo": grupo, "nombre": nombre, "unidad": "M€ corrientes", "serie": s, "fuente": VISTA + ds, "actualizado": upd, "nivel": "P"})
        except Exception as e:
            fallos.append(f"{iid}: {type(e).__name__}: {e}")
            if iid in previo:
                ind.append(previo[iid])
    ctx = {}
    for k, ds, fil in (("pib", "nama_10_gdp", dict(na_item="B1GQ", unit="CP_MEUR")), ("deflactor", "nama_10_gdp", dict(na_item="B1GQ", unit="PD15_EUR")),
                       ("poblacion", "demo_pjan", dict(age="TOTAL", sex="T", unit="NR"))):
        try:
            ctx[k] = _serie(ds, **fil)[0]
        except Exception as e:
            fallos.append(f"{k}: {type(e).__name__}: {e}")
    if len(ctx) < 3:
        print("AVISO: faltan PIB, deflactor o población; no se escribe", fallos)
        return 1
    ultimo = max(ctx["deflactor"])
    base = ctx["deflactor"][ultimo]
    for i in ind:
        s = i["serie"]
        i["pct_pib"] = {a: round(v / ctx["pib"][a] * 100, 2) for a, v in s.items() if a in ctx["pib"]}
        i["real_por_habitante"] = {a: round(v * 1e6 * base / ctx["deflactor"][a] / ctx["poblacion"][a]) for a, v in s.items() if a in ctx["deflactor"] and a in ctx["poblacion"]}
    res = []
    prev_res = {r["id"]: r for r in json.loads(SALIDA.read_text(encoding="utf-8")).get("resultados", [])} if SALIDA.exists() else {}
    for rid, nombre, unidad, ds, fil in RESULTADOS:
        try:
            es, upd = _serie(ds, 14, **fil)
            ue = _serie(ds, 14, **{**fil, "geo": "EU27_2020"})[0]
            res.append({"id": rid, "nombre": nombre, "unidad": unidad, "es": es, "ue27": ue, "fuente": VISTA + ds, "actualizado": upd, "nivel": "P"})
        except Exception as e:
            fallos.append(f"{rid}: {type(e).__name__}: {e}")
            if rid in prev_res:
                res.append(prev_res[rid])
    manual = json.loads(MANUAL.read_text(encoding="utf-8")) if MANUAL.exists() else {}
    salida = {
        "titulo": "España: ingresos y gasto público", "leido": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "nota": f"Eurostat (cuentas nacionales de las administraciones públicas, sector S13). «Real por habitante» = euros de {ultimo} (deflactor del PIB) por habitante. Último año disponible varía: ingresos y gasto total llegan a {max(ctx['pib'])}, las funciones COFOG a un año menos. Solo cifras publicadas; las lecturas son [OPINIÓN].",
        "contexto": ctx, "indicadores": ind, "resultados": res, "manual": manual, "fallos": fallos,
    }
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"espana.json: {len(ind)} indicadores, {len(fallos)} fallos")
    for f in fallos:
        print("AVISO:", f)
    return 0


if __name__ == "__main__":
    sys.exit(main())
