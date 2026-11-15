"""C279: registro provisional MiCA de ESMA, sin IA ni claves. Descarga los CSV oficiales (CASPS, ARTZZ, EMTWP, OTHER, NCASP)
de esma.europa.eu, cuenta por país de origen y servicio y guarda explorador/mica-registro.json [nivel P: se lee la fuente].
Certificados verificados. Uso: python scripts/leer_esma_mica.py [--seco]"""
import csv
import io
import json
import re
import sys
import urllib.request
from collections import Counter
from datetime import date, datetime
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "explorador" / "mica-registro.json"
PAGINA = "https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica"
BASE = "https://www.esma.europa.eu"
ARCH = {"casp": "CASPS", "art": "ARTZZ", "emt": "EMTWP", "otros": "OTHER", "no_conformes": "NCASP"}


def bajar(url):
    r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60)
    return r.read().decode("utf-8-sig", "replace")


def filas(txt):
    return [f for f in csv.DictReader(io.StringIO(txt)) if any((v or "").strip() for v in f.values())]


def fecha(s):
    try:
        return datetime.strptime((s or "").strip(), "%d/%m/%Y").date().isoformat()
    except ValueError:
        return ""


CLAVES = [("a", "custody"), ("b", "trading platform"), ("c", "for funds"), ("d", "other crypto"), ("e", "execution of orders"),
          ("f", "placing"), ("g", "reception and transmission"), ("h", "advice"), ("i", "portfolio"), ("j", "transfer")]


def servicios(s):
    """Normaliza el texto libre a letras a-j (art. 3 MiCA); lo no reconocido queda sin contar."""
    out = set()
    for x in re.split(r"[|/\n]", s or ""):
        x = x.strip().lower()
        m = re.match(r"^\(?([a-j])\)?[.\s]", x + " ")
        if m:
            out.add(m.group(1))
            continue
        for l, c in CLAVES:
            if c in x:
                out.add(l)
    return sorted(out)


def main():
    seco = "--seco" in sys.argv
    html = bajar(PAGINA)
    enl = {}
    for u in set(re.findall(r'href="(/sites/default/files/[^"]+\.csv)"', html)):
        nom = u.rsplit("/", 1)[1][:-4]
        enl[nom] = BASE + u
    out = {"fuente": "ESMA, Interim MiCA Register", "url": PAGINA, "fecha_lectura": date.today().isoformat(), "nivel": "P",
           "archivos": {}, "fallos": []}
    datos = {}
    for k, nom in ARCH.items():
        if nom not in enl:
            out["fallos"].append(f"{nom}: sin enlace en la página")
            continue
        try:
            datos[k] = filas(bajar(enl[nom]))
            out["archivos"][k] = enl[nom]
        except Exception as e:
            out["fallos"].append(f"{nom}: {type(e).__name__}")
    ents = []
    por_serv = Counter()
    for f in datos.get("casp", []):
        sv = servicios(f.get("ac_serviceCode"))
        por_serv.update(sv)
        ents.append({"nombre": f.get("ae_lei_name", "").strip(), "comercial": f.get("ae_commercial_name", "").strip(),
                     "pais": f.get("ae_homeMemberState", "").strip(), "autoridad": f.get("ae_competentAuthority", "").strip(),
                     "servicios": sv, "autorizacion": fecha(f.get("ac_authorisationNotificationDate")),
                     "fin": fecha(f.get("ac_authorisationEndDate")), "web": f.get("ae_website", "").strip()})
    def pais(k):
        return dict(sorted(Counter(f.get("ae_homeMemberState", "").strip() for f in datos.get(k, [])).items(), key=lambda x: (-x[1], x[0])))
    out["conteo"] = {"casp": len(ents), "art": len(datos.get("art", [])), "emt": len({f.get("ae_lei", "") for f in datos.get("emt", [])}),
                     "emt_filas": len(datos.get("emt", [])), "otros_filas": len(datos.get("otros", [])),
                     "no_conformes": len(datos.get("no_conformes", []))}
    out["casp_por_pais"] = pais("casp")
    out["casp_por_servicio_letra"] = dict(sorted(por_serv.items()))
    out["emt_por_pais"] = pais("emt")
    out["otros_por_pais"] = pais("otros")
    out["no_conformes_por_pais"] = pais("no_conformes")
    out["casp_entidades"] = ents
    out["emt_emisores"] = sorted({(f.get("ae_lei_name", "").strip(), f.get("ae_homeMemberState", "").strip()) for f in datos.get("emt", [])})
    out["emt_emisores"] = [{"nombre": a, "pais": b} for a, b in out["emt_emisores"]]
    out["no_conformes_entidades"] = [{"nombre": f.get("ae_lei_name", "").strip(), "pais": f.get("ae_homeMemberState", "").strip(),
                                      "fecha": fecha(f.get("ae_decision_date")), "motivo": f.get("ae_reason", "").strip()[:200]}
                                     for f in datos.get("no_conformes", [])]
    out["nota"] = ("Registro provisional de ESMA (reúne lo que notifican las autoridades nacionales; no es un registro definitivo). "
                   "Las filas de OTHER y EMTWP pueden repetirse por libro blanco; por eso se cuentan emisores únicos por LEI.")
    print({k: out[k] for k in ("conteo", "fallos")})
    print(list(out["casp_por_pais"].items())[:8])
    if not seco and out["conteo"]["casp"]:
        RUTA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        print("escrito", RUTA)


if __name__ == "__main__":
    main()
