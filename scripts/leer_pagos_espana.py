"""C114: conteos diarios de subvenciones (BDNS) y de licitaciones (PLACSP) de España en explorador/espana-pagos.json. Sin IA y sin claves.

- BDNS (infosubvenciones.es): convocatorias registradas por día y nivel (Estado, autonómico, local, otros). Oficial [P].
- PLACSP (contrataciondelsectorpublico.gob.es): se cuentan las entradas del feed Atom de licitaciones por día de actualización; el feed
  (~13 MB) se lee por trozos y NO se guarda. Cuenta entradas del feed, no contratos únicos ni importes.

Uso:  python scripts/leer_pagos_espana.py
Cada día nuevo se suma al histórico del archivo (campo «desde» = primer día guardado). Si una fuente falla se conserva lo anterior.
"""
import collections
import json
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "espana-pagos.json"
URL_BDNS = "https://www.infosubvenciones.es/bdnstrans/api/convocatorias/busqueda?pageSize=2000&page=0&fechaDesde={d}&fechaHasta={d}&vpd=GE"
URL_PLACSP = "https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom"
DIAS_BDNS = 14
UA = {"User-Agent": "cartera-joel/1.0 (uso personal)"}


def bdns_dia(dia):
    with urllib.request.urlopen(urllib.request.Request(URL_BDNS.format(d=dia.strftime("%d%%2F%m%%2F%Y")), headers=UA), timeout=60) as r:
        j = json.loads(r.read().decode("utf-8", "replace"))
    niveles = collections.Counter(x.get("nivel1") or "SIN_NIVEL" for x in j["content"])
    if j["totalElements"] != len(j["content"]):
        raise ValueError(f"{dia:%Y-%m-%d}: la página trae {len(j['content'])} de {j['totalElements']}")
    return {"fecha": f"{dia:%Y-%m-%d}", "total": j["totalElements"], "por_nivel": dict(sorted(niveles.items()))}


def placsp_conteo():
    """Cuenta <entry> por día de su <updated>, leyendo el feed por trozos sin guardarlo."""
    por_dia, pendiente, actualizado, entradas = collections.Counter(), "", None, 0
    with urllib.request.urlopen(urllib.request.Request(URL_PLACSP, headers=UA), timeout=120) as r:
        while True:
            trozo = r.read(1 << 20)
            if not trozo:
                break
            pendiente += trozo.decode("utf-8", "replace")
            while True:
                i, j = pendiente.find("<entry"), pendiente.find("</entry>")
                if i < 0 or j < 0:
                    pendiente = pendiente[i:] if i >= 0 else pendiente[-10:]
                    break
                entrada, pendiente = pendiente[i:j], pendiente[j + 8:]
                m = re.search(r"<updated>(\d{4}-\d{2}-\d{2})", entrada)
                if m:
                    por_dia[m.group(1)] += 1
                entradas += 1
    if not entradas:
        raise ValueError("PLACSP: feed sin entradas")
    return {"entradas_feed": entradas, "por_dia": dict(sorted(por_dia.items())), "feed": URL_PLACSP}


def main():
    previo = {}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        except Exception:
            previo = {}
    fallos = []
    hoy = datetime.now(timezone.utc)
    historico = {d["fecha"]: d for d in previo.get("bdns", {}).get("dias", [])}
    for k in range(1, DIAS_BDNS + 1):
        dia = hoy - timedelta(days=k)
        try:
            d = bdns_dia(dia)
            historico[d["fecha"]] = d
        except Exception as e:
            fallos.append(f"BDNS {dia:%Y-%m-%d}: {type(e).__name__}: {e}")
    dias = [historico[f] for f in sorted(historico)]
    try:
        placsp = placsp_conteo()
        hist_p = previo.get("placsp", {}).get("por_dia", {})
        hist_p.update(placsp["por_dia"])
        placsp["por_dia"] = dict(sorted(hist_p.items()))
        placsp["desde"] = next(iter(placsp["por_dia"]))
    except Exception as e:
        fallos.append(f"PLACSP: {type(e).__name__}: {e}")
        placsp = previo.get("placsp")
    salida = {"titulo": "España: subvenciones y contratación, conteos diarios", "leido": hoy.strftime("%Y-%m-%d %H:%M UTC"), "nivel": "P",
              "nota": "Conteos de registros, no importes ni pagos. BDNS: convocatorias del Sistema Nacional de Publicidad de Subvenciones, por fecha de recepción. "
                      "PLACSP: entradas del feed de licitaciones por fecha de actualización (una licitación puede aparecer varias veces); el día en curso puede estar incompleto. "
                      "El feed solo cubre el último día o dos, así que el histórico crece con cada ejecución. Reutilización sujeta a las condiciones legales de cada fuente.",
              "bdns": {"fuente": "https://www.infosubvenciones.es/bdnstrans/", "desde": dias[0]["fecha"] if dias else None, "dias": dias},
              "placsp": placsp, "fallos": fallos}
    if not dias and not placsp:
        print("AVISO: ninguna fuente disponible; no se escribe")
        return 1
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if dias:
        print("BDNS: " + ", ".join(f"{d['fecha'][5:]} {d['total']}" for d in dias[-5:]))
    if placsp:
        print(f"PLACSP: {placsp['entradas_feed']} entradas en el feed, {len(placsp['por_dia'])} días")
    for f in fallos:
        print("AVISO (se conserva lo anterior si existía):", f)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
