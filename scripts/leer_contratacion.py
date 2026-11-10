#!/usr/bin/env python3
"""Lee los ZIP mensuales de la Plataforma de Contratación del Sector Público
(PLACSP) y agrega por órgano, procedimiento y adjudicatario. Sin IA, sin claves.

Uso:
  python scripts/leer_contratacion.py --mes 202610 [--zip-lic RUTA] [--zip-men RUTA] [--tmp DIR]
Si no se dan rutas, descarga a un directorio temporal (fuera del repo) y lo borra.
Salida: explorador/espana-contratacion.json

LÍMITES HONESTOS (también van dentro del JSON):
- PLACSP solo recoge entidades con perfil en la plataforma estatal; las CCAA/EELL
  con plataforma propia pueden no estar o estar a medias [VERIFICAR cobertura].
- Es el FEED mensual: cada expediente aparece varias veces (una por modificación);
  se conserva la última versión del mes. Un expediente adjudicado antes sin cambios
  en el mes NO aparece; el mes no es "todo lo adjudicado en el mes".
- Importes = valor de licitación/adjudicación sin IVA, no ejecución ni pago.
- Emergencia, encargos a medios propios (Tragsa...) y menores no publicados pueden
  quedar fuera o parcialmente visibles [VERIFICAR].
- Adjudicatario repetido o concentración NO implican irregularidad.
- Personas físicas (NIF de persona) se agregan en un cajón y no se listan.
"""
import argparse, collections, json, shutil, sys, tempfile, urllib.request, zipfile
import datetime as dt
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "espana-contratacion.json"
URL_LIC = "https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_{mes}.zip"
URL_MEN = "https://contrataciondelestado.es/sindicacion/sindicacion_1143/contratosMenoresPerfilesContratantes_{mes}.zip"
UA = {"User-Agent": "cartera-github/leer_contratacion (investigacion personal; sin IA)"}

PROC = {"1": "Abierto", "2": "Restringido", "3": "Negociado con publicidad", "4": "Negociado sin publicidad",
        "5": "Diálogo competitivo", "6": "Contrato menor", "7": "Derivado de acuerdo marco",
        "8": "Concurso de proyectos", "9": "Abierto simplificado", "10": "Asociación para la innovación",
        "100": "Normas internas", "999": "Otros"}
URG = {"1": "Ordinaria", "2": "Urgente", "3": "Emergencia"}
import re
RE_FISICA = re.compile(r"^(\d{8}[A-Z]|[XYZ]\d{7}[A-Z]|[KLM]\d{7}[A-Z0-9])$")  # DNI/NIE/K-L-M: persona física


def tx(e, path):
    x = e.find(path)
    return x.text.strip() if x is not None and x.text else None


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def bajar(url, destino):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=600) as r, open(destino, "wb") as f:
        shutil.copyfileobj(r, f)


def leer_zip(ruta):
    """Devuelve {clave: registro} con la última versión de cada expediente."""
    datos = {}
    with zipfile.ZipFile(ruta) as z:
        for nombre in z.namelist():
            if not nombre.endswith(".atom"):
                continue
            with z.open(nombre) as fh:
                for _, el in ET.iterparse(fh, events=("end",)):
                    if not el.tag.endswith("}entry"):
                        continue
                    reg = parse_entry(el)
                    el.clear()
                    if not reg:
                        continue
                    k = (reg["exp"], reg["organo"])
                    if k not in datos or reg["upd"] >= datos[k]["upd"]:
                        datos[k] = reg
    return datos


def parse_entry(en):
    cfs = en.find("{*}ContractFolderStatus")
    if cfs is None:
        return None
    exp = tx(cfs, "{*}ContractFolderID")
    lcp = cfs.find("{*}LocatedContractingParty")
    organo = tx(lcp, "{*}Party/{*}PartyName/{*}Name") if lcp is not None else None
    cadena = []
    p = lcp.find("{*}ParentLocatedParty") if lcp is not None else None
    while p is not None:
        cadena.append(tx(p, "{*}PartyName/{*}Name") or "")
        p = p.find("{*}ParentLocatedParty")
    link = en.find("{*}link")
    proj = cfs.find("{*}ProcurementProject")
    tp = cfs.find("{*}TenderingProcess")
    adj = []
    for tr in cfs.findall("{*}TenderResult"):
        wp = tr.find("{*}WinningParty")
        nif = nombre = None
        if wp is not None:
            for pid in wp.findall("{*}PartyIdentification/{*}ID"):
                if pid.get("schemeName") in ("NIF", "EU", "OTROS") and pid.text:
                    nif = pid.text.strip()
                    break
            nombre = tx(wp, "{*}PartyName/{*}Name")
        imp = num(tx(tr, "{*}AwardedTenderedProject/{*}LegalMonetaryTotal/{*}TaxExclusiveAmount"))
        if imp is None:
            imp = num(tx(tr, "{*}AwardedTenderedProject/{*}LegalMonetaryTotal/{*}PayableAmount"))
        adj.append({"nif": nif, "nombre": nombre, "importe": imp, "res": tx(tr, "{*}ResultCode"),
                    "fecha": tx(tr, "{*}AwardDate"), "ofertas": tx(tr, "{*}ReceivedTenderQuantity")})
    return {
        "exp": exp, "organo": organo or "?", "cadena": cadena,
        "estado": tx(cfs, "{*}ContractFolderStatusCode"),
        "upd": tx(en, "{*}updated") or "",
        "link": link.get("href") if link is not None else None,
        "objeto": (tx(proj, "{*}Name") or "")[:140] if proj is not None else "",
        "tipo": tx(proj, "{*}TypeCode") if proj is not None else None,
        "presupuesto": num(tx(proj, "{*}BudgetAmount/{*}TaxExclusiveAmount")) if proj is not None else None,
        "proc": tx(tp, "{*}ProcedureCode") if tp is not None else None,
        "urg": tx(tp, "{*}UrgencyCode") if tp is not None else None,
        "adj": adj,
    }


def raiz(cadena):
    """Nivel administrativo: el penúltimo de la cadena (sobre 'Sector Público')."""
    c = [x for x in cadena if x]
    return c[-2] if len(c) >= 2 else (c[-1] if c else "?")


def agregar(datos, etiqueta):
    n = len(datos)
    por_proc = collections.defaultdict(lambda: [0, 0.0, 0.0])  # n, presupuesto, adjudicado
    por_urg = collections.Counter()
    por_estado = collections.Counter()
    por_nivel = collections.defaultdict(lambda: [0, 0.0])
    por_org = collections.defaultdict(lambda: {"n": 0, "pres": 0.0, "adj": 0.0, "emerg": 0, "menores": 0, "negsinpub": 0,
                                               "nivel": ""})
    por_adj = collections.defaultdict(lambda: {"nombre": "", "n": 0, "importe": 0.0, "n_marco": 0, "organos": collections.Counter()})
    fis = [0, 0.0]
    tot_adj = [0, 0.0]
    grandes = []
    sin_importe = 0
    marcos = [0]
    for r in datos.values():
        pn = PROC.get(r["proc"], f"código {r['proc']}") if r["proc"] else "sin dato"
        # Acuerdo marco con varios adjudicatarios: cada uno consta con el mismo techo.
        # Se cuenta el importe UNA vez por grupo de >=3 adjudicatarios con importe idéntico.
        gr = collections.Counter(a["importe"] for a in r["adj"] if a["importe"] is not None)
        marco = {i for i, c in gr.items() if c >= 3}
        for a in r["adj"]:
            a["marco"] = a["importe"] in marco
        vistos = set()
        sumadj = 0.0
        for a in r["adj"]:
            if a["importe"] is None:
                continue
            if a["marco"]:
                if a["importe"] in vistos:
                    continue
                vistos.add(a["importe"])
            sumadj += a["importe"]
        n_marco_exp = 1 if marco else 0
        marcos[0] += n_marco_exp
        pres = r["presupuesto"] or 0.0
        pp = por_proc[pn]
        pp[0] += 1
        pp[1] += pres
        pp[2] += sumadj
        urg = URG.get(r["urg"], "sin dato")
        por_urg[urg] += 1
        por_estado[r["estado"] or "?"] += 1
        nv = raiz(r["cadena"])
        por_nivel[nv][0] += 1
        por_nivel[nv][1] += sumadj
        o = por_org[r["organo"]]
        o["nivel"] = nv
        o["n"] += 1
        o["pres"] += pres
        o["adj"] += sumadj
        if r["urg"] == "3":
            o["emerg"] += 1
        if r["proc"] == "6":
            o["menores"] += 1
        if r["proc"] == "4":
            o["negsinpub"] += 1
        if not r["adj"]:
            sin_importe += 1
        for a in r["adj"]:
            imp = a["importe"]
            if imp is None:
                continue
            nif = a["nif"] or ""
            tot_adj[0] += 1
            if not a["marco"]:
                tot_adj[1] += imp
            if not nif or RE_FISICA.match(nif):
                fis[0] += 1
                fis[1] += imp
                continue
            x = por_adj[nif]
            x["nombre"] = a["nombre"] or x["nombre"]
            x["n"] += 1
            if not a["marco"]:
                x["importe"] += imp
            else:
                x["n_marco"] = x.get("n_marco", 0) + 1
            x["organos"][r["organo"]] += 1
            grandes.append({"expediente": r["exp"], "organo": r["organo"], "adjudicatario": a["nombre"], "nif": nif,
                            "importe": imp, "acuerdo_marco_multiple": a["marco"], "fecha_adjudicacion": a["fecha"], "procedimiento": pn,
                            "urgencia": urg, "ofertas": a["ofertas"], "objeto": r["objeto"], "enlace": r["link"]})
    grandes.sort(key=lambda g: -g["importe"])
    vistos_m, gg = set(), []
    for g in grandes:  # un solo representante por acuerdo marco multiadjudicatario
        if g["acuerdo_marco_multiple"]:
            k = (g["expediente"], g["importe"])
            if k in vistos_m:
                continue
            vistos_m.add(k)
            g["adjudicatario"] = (g["adjudicatario"] or "") + " (+ otros adjudicatarios del mismo acuerdo marco)"
        gg.append(g)
    grandes = gg
    top_adj = sorted(por_adj.items(), key=lambda kv: -kv[1]["importe"])[:25]
    suma_jur = sum(v["importe"] for v in por_adj.values())
    top10 = sum(v["importe"] for _, v in top_adj[:10])
    orgs = sorted(por_org.items(), key=lambda kv: -kv[1]["adj"])
    n_emerg = por_urg.get("Emergencia", 0)
    n_menor = por_proc.get("Contrato menor", [0])[0]
    n_nsp = por_proc.get("Negociado sin publicidad", [0])[0]
    return {
        "etiqueta": etiqueta,
        "expedientes_unicos": n,
        "adjudicaciones_con_importe": {"n": tot_adj[0], "importe": round(tot_adj[1], 2)},
        "expedientes_sin_resultado_en_feed": sin_importe,
        "expedientes_con_acuerdo_marco_multiple": marcos[0],
        "nota_acuerdo_marco": "Si >=3 adjudicatarios de un expediente comparten importe idéntico (acuerdos marco), el importe se cuenta una sola vez en totales y por órgano, y no se suma a cada adjudicatario (es un techo común, no dinero repartido).",
        "por_estado": dict(por_estado.most_common()),
        "por_procedimiento": [{"procedimiento": k, "n": v[0], "pct_expedientes": round(100 * v[0] / n, 1) if n else 0,
                               "presupuesto": round(v[1], 2), "adjudicado": round(v[2], 2)}
                              for k, v in sorted(por_proc.items(), key=lambda kv: -kv[1][0])],
        "por_urgencia": {k: {"n": v, "pct": round(100 * v / n, 2) if n else 0} for k, v in por_urg.most_common()},
        "pct_emergencia": round(100 * n_emerg / n, 2) if n else 0,
        "pct_menores": round(100 * n_menor / n, 2) if n else 0,
        "pct_negociado_sin_publicidad": round(100 * n_nsp / n, 2) if n else 0,
        "por_nivel_administrativo": [{"nivel": k, "n": v[0], "adjudicado": round(v[1], 2)}
                                     for k, v in sorted(por_nivel.items(), key=lambda kv: -kv[1][1])[:12]],
        "por_organo_top": [{"organo": k, "nivel": v["nivel"], "n": v["n"], "presupuesto": round(v["pres"], 2),
                            "adjudicado": round(v["adj"], 2), "n_emergencia": v["emerg"], "n_menores": v["menores"],
                            "n_negociado_sin_publicidad": v["negsinpub"]} for k, v in orgs[:20]],
        "adjudicatarios_top": [{"nif": k, "adjudicatario": v["nombre"], "n_adjudicaciones": v["n"],
                                "importe": round(v["importe"], 2), "n_adjudicaciones_en_acuerdo_marco_sin_importe_propio": v["n_marco"], "n_organos_distintos": len(v["organos"]),
                                "organo_principal": v["organos"].most_common(1)[0][0]} for k, v in top_adj],
        "concentracion": {"top10_adjudicatarios_pct_importe_juridicas": round(100 * top10 / suma_jur, 1) if suma_jur else 0,
                          "adjudicatarios_juridicos_distintos": len(por_adj),
                          "personas_fisicas": {"n": fis[0], "importe": round(fis[1], 2)},
                          "nota": "Concentración y repetición NO implican irregularidad: UTE, grandes concesionarias y encargos marco son habituales."},
        "mayores_adjudicaciones": grandes[:25],
        "_orgs_completo": {k: v for k, v in orgs},  # se recorta fuera
    }


# Organismos pedidos por el plan: coincidencia por texto en nombre o cadena del órgano
VIGILADOS = {"Adif": ["adif"], "Ministerio de Transportes": ["transportes"], "Defensa": ["defensa"],
             "Sanidad": ["sanidad", "salud", "insalud", "ingesa"], "Interior": ["interior", "guardia civil", "policía"]}


def vigilados(datos):
    out = {}
    for etq, claves in VIGILADOS.items():
        n = pres = adj = em = men = nsp = 0
        ejemplo = None
        for r in datos.values():
            txt = (r["organo"] + " " + " ".join(r["cadena"])).lower()
            if not any(c in txt for c in claves):
                continue
            n += 1
            pres += r["presupuesto"] or 0
            s = sum(a["importe"] or 0 for a in r["adj"])
            adj += s
            em += r["urg"] == "3"
            men += r["proc"] == "6"
            nsp += r["proc"] == "4"
        out[etq] = {"n_expedientes": n, "presupuesto": round(pres, 2), "adjudicado": round(adj, 2),
                    "n_emergencia": em, "n_menores": men, "n_negociado_sin_publicidad": nsp,
                    "criterio": "coincidencia por texto en nombre/cadena del órgano: " + ", ".join(claves)
                                + ". Puede incluir otros órganos con ese texto (p. ej. 'salud' autonómica) [VERIFICAR]."}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mes", default=(dt.date.today().replace(day=1) - dt.timedelta(days=1)).strftime("%Y%m"))
    ap.add_argument("--zip-lic")
    ap.add_argument("--zip-men")
    ap.add_argument("--tmp")
    a = ap.parse_args()
    tmp = Path(a.tmp) if a.tmp else Path(tempfile.mkdtemp(prefix="placsp_"))
    tmp.mkdir(parents=True, exist_ok=True)
    zl = Path(a.zip_lic) if a.zip_lic else tmp / "lic.zip"
    zm = Path(a.zip_men) if a.zip_men else tmp / "men.zip"
    if not a.zip_lic:
        print("descargando licitaciones…", file=sys.stderr)
        bajar(URL_LIC.format(mes=a.mes), zl)
    if not a.zip_men:
        print("descargando menores…", file=sys.stderr)
        bajar(URL_MEN.format(mes=a.mes), zm)
    print("leyendo licitaciones…", file=sys.stderr)
    lic = leer_zip(zl)
    print(f"  {len(lic):,} expedientes; leyendo menores…", file=sys.stderr)
    men = leer_zip(zm)
    print(f"  {len(men):,} menores", file=sys.stderr)
    A = agregar(lic, "Licitaciones (excluye menores)")
    B = agregar(men, "Contratos menores")
    A["organismos_vigilados"] = vigilados(lic)
    B["organismos_vigilados"] = vigilados(men)
    for X in (A, B):
        X.pop("_orgs_completo", None)
    out = {
        "id": "espana-contratacion",
        "generado": dt.date.today().isoformat(),
        "mes": a.mes,
        "fuente": {"nombre": "Plataforma de Contratación del Sector Público (Hacienda), datos abiertos",
                   "url": "https://contrataciondelestado.es/wps/portal/DatosAbiertos",
                   "licitaciones_zip": URL_LIC.format(mes=a.mes), "menores_zip": URL_MEN.format(mes=a.mes),
                   "nivel": "P (ficheros oficiales leídos)"},
        "unidad": "EUR", "escala": 1,
        "nota_unidad": "importe = euros sin IVA (escala 1). M€ = importe/1e6; mil M€ = importe/1e9.",
        "licitaciones": A, "menores": B,
        "limites": [
            "Solo entidades con perfil en la plataforma estatal; CCAA/EELL con plataforma propia pueden estar incompletas [VERIFICAR].",
            "Feed mensual: se conserva la última versión de cada expediente movida en el mes; no es 'todo lo adjudicado en el mes'.",
            "Importes de licitación/adjudicación sin IVA; no son ejecución ni pago.",
            "Emergencia, encargos a medios propios y menores no publicados pueden faltar [VERIFICAR].",
            "Adjudicatario repetido o concentrado NO implica irregularidad.",
            "Personas físicas (DNI/NIE) agregadas en un cajón y no listadas. Los identificadores no españoles sí se listan.",
            "Algunos órganos publican una 'relación trimestral' de menores como una sola entrada: infravalora el número de contratos.",
        ],
    }
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK {SALIDA}", file=sys.stderr)
    if not a.tmp and not a.zip_lic:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
