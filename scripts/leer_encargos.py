#!/usr/bin/env python3
"""Encargos a medios propios (PLACSP, sindicacion_1383) -> bloque en
explorador/espana-contratacion.json["encargos_medios_propios"]. Sin IA, sin claves.
Uso: python scripts/leer_encargos.py [--zip ruta.zip]   (si no, descarga EMP_SectorPublico_<año>.zip)
Dedupe por id de entrada (gana la ultima <updated>); se descartan ANULADAS (at:deleted-entry).
Un encargo NO es contrato licitado: es una orden a un medio propio (Tragsa, Ineco...);
que un medio propio concentre encargos NO implica irregularidad.
"""
import argparse, collections, datetime as dt, json, re, sys, tempfile, urllib.request, zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
SAL = RAIZ / "explorador" / "espana-contratacion.json"
NS = {"a": "http://www.w3.org/2005/Atom",
      "cbc": "urn:dgpe:names:draft:codice:schema:xsd:CommonBasicComponents-2",
      "cac": "urn:dgpe:names:draft:codice:schema:xsd:CommonAggregateComponents-2",
      "ext": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonAggregateComponents-2",
      "cbe": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonBasicComponents-2",
      "at": "http://purl.org/atompub/tombstones/1.0"}
def tx(e, p):
    r = e.find(p, NS); return r.text.strip() if r is not None and r.text else None
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--zip"); ap.add_argument("--anio", default=str(dt.date.today().year)); a = ap.parse_args()
    zp = a.zip
    if not zp:
        zp = str(Path(tempfile.gettempdir()) / f"EMP_{a.anio}.zip")
        urllib.request.urlretrieve(f"https://contrataciondelestado.es/sindicacion/sindicacion_1383/EMP_SectorPublico_{a.anio}.zip", zp)
    ents, borr = {}, set()
    with zipfile.ZipFile(zp) as z:
        for n in z.namelist():
            root = ET.fromstring(z.read(n))
            for d in root.findall("at:deleted-entry", NS): borr.add(d.get("ref").rsplit("/", 1)[-1])
            for e in root.findall("a:entry", NS):
                i = tx(e, "a:id").rsplit("/", 1)[-1]; u = tx(e, "a:updated")
                if i not in ents or u > ents[i][0]: ents[i] = (u, e)
    filas = []
    for i, (u, e) in ents.items():
        if i in borr: continue
        c = e.find("ext:ContractFolderStatus", NS)
        imp = tx(c, "cac:ProcurementProject/cac:BudgetAmount/cbc:TotalAmount")
        org = tx(c, "ext:LocatedContractingParty/cac:Party/cac:PartyName/cbc:Name")
        ccaa = None
        padres = [x.text for x in c.iterfind(".//ext:ParentLocatedParty/cac:PartyName/cbc:Name", NS)]
        medio = tx(c, "cac:TenderResult/cac:WinningParty/cac:PartyName/cbc:Name")
        fecha = tx(c, "cac:TenderResult/cbc:AwardDate")
        filas.append(dict(id=i, estado=tx(c, "cbe:ContractFolderStatusCode"), organo=org, padres=padres, medio=medio,
                          importe=float(imp) if imp else None, fecha=fecha))
    def agg(k):
        d = collections.defaultdict(lambda: [0, 0.0])
        for f in filas:
            if f["importe"] is None: continue
            x = d[k(f)]; x[0] += 1; x[1] += f["importe"]
        return sorted(([k, n, round(s, 2)] for k, (n, s) in d.items()), key=lambda r: -r[2])
    medio = lambda f: re.sub(r"\s+", " ", f["medio"] or "[sin adjudicatario]")
    nivel = lambda f: (f["padres"][-2] if len(f["padres"]) >= 2 else "[VERIFICAR]")
    top = lambda L, n=15: [dict(nombre=r[0], encargos=r[1], importe=r[2]) for r in L[:n]]
    tot = sum(f["importe"] or 0 for f in filas)
    bloque = dict(fuente="PLACSP sindicacion_1383 EMP_SectorPublico_%s.zip (Hacienda), leido %s" % (a.anio, dt.date.today().isoformat()),
        unidad="EUR", escala=1, nota_unidad="importe = euros del campo TotalAmount del encargo (escala 1). M€ = importe/1e6.",
        n_entradas_unicas=len(ents), n_anuladas=len(borr & set(ents)), n_encargos=len(filas), importe_total=round(tot, 2),
        por_anio_adjudicacion=[dict(anio=k, encargos=n, importe=v) for k, n, v in sorted(agg(lambda f: (f["fecha"] or "sin fecha")[:4]), key=lambda r: r[0])],
        por_estado=[dict(estado=k, encargos=n, importe=s) for k, n, s in agg(lambda f: f["estado"])],
        por_medio_propio=top(agg(medio)), por_administracion=top(agg(nivel)), por_organo=top(agg(lambda f: f["organo"] or "?")),
        mayores_encargos=[dict(id=f["id"], organo=f["organo"], medio=f["medio"], importe=f["importe"], fecha=f["fecha"], estado=f["estado"])
                          for f in sorted(filas, key=lambda f: -(f["importe"] or 0))[:10]],
        limites=["El ZIP anual reune entradas cuya ULTIMA actualizacion cae en el año; la fecha de adjudicacion puede ser de años anteriores (ver por_anio_adjudicacion): no es el gasto de un solo año.",
                 "Hay pares de entradas con mismo importe y fecha (p. ej. dos de 215,8 M€ de Tragsa, dos de 98,05 M€ en Canarias): pueden ser duplicados de publicacion o encargos distintos [VERIFICAR].",
                 "Un encargo a medio propio no es una licitacion: no hay concurrencia por diseño legal (art. 32 LCSP).",
                 "El ZIP anual puede no incluir encargos sin publicar; cobertura real [VERIFICAR].",
                 "Un medio propio con muchos encargos NO implica irregularidad.",
                 "Importe = presupuesto del encargo, no pago efectivo."])
    d = json.loads(SAL.read_text(encoding="utf-8")); d["encargos_medios_propios"] = bloque
    SAL.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(filas), round(tot / 1e6, 1), "M EUR"); print(json.dumps(bloque["por_estado"], ensure_ascii=False)); print(json.dumps(bloque["por_medio_propio"][:8], ensure_ascii=False))
main()
