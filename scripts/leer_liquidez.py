"""C285: liquidez global sin IA ni claves. Lee FRED (CSV público: WALCL, RRPONTSYD, WTREGEN) y el BCE (SDMX, ILM) [P]
y los vuelca en explorador/liquidez-manual.json (claves nuevas «fed» y «eurosistema»; «jp» y «cn» se conservan con su fecha).
Si una serie no se puede leer se conserva el bloque anterior con su fecha vieja y se anota en «fallos». Certificados verificados.
Uso: python scripts/leer_liquidez.py [--seco]"""
import csv
import io
import json
import sys
import time
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "explorador" / "liquidez-manual.json"
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={i}&cosd={d}"
BCE = "https://data-api.ecb.europa.eu/service/data/ILM/W.U2.C.T000000.Z5.Z01?lastNObservations=60&format=csvdata"


def bajar(url, cab=None):
    for n in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.4.0", **(cab or {})}), timeout=30) as r:
                return r.read().decode("utf-8")
        except Exception:
            if n == 2:
                raise
            time.sleep(3)


def fred(sid, desde):
    filas = list(csv.reader(io.StringIO(bajar(FRED.format(i=sid, d=desde)))))[1:]
    return [(f[0], float(f[1])) for f in filas if len(f) == 2 and f[1] not in ("", ".")]


def bloque_fed():
    desde = f"{date.today().year - 1}-{date.today().month:02d}-01"
    wal, rrp, tga = fred("WALCL", desde), fred("RRPONTSYD", desde), fred("WTREGEN", desde)
    if not (wal and rrp and tga):
        raise ValueError("serie vacía")
    f = wal[-1][0]                                   # miércoles de WALCL; RRP y TGA se toman en esa fecha o la anterior más cercana
    dtga, drrp = dict(tga), dict(rrp)
    if f not in dtga:
        raise ValueError(f"TGA sin dato para {f}")
    fr = max(x for x in drrp if x <= f)
    neta = wal[-1][1] / 1000 - drrp[fr] - dtga[f] / 1000

    def neta_en(fecha):
        a = max((x for x in drrp if x <= fecha), default=None)
        return round(dict(wal)[fecha] / 1000 - drrp[a] - dtga[fecha] / 1000, 1) if a and fecha in dtga else None
    prev = wal[-5][0] if len(wal) >= 5 else None
    return {"serie": "Liquidez neta Fed = balance (WALCL) − repo inverso (RRPONTSYD) − TGA (WTREGEN)", "fecha": f, "unidad": "mil M$",
            "balance": round(wal[-1][1] / 1000, 1), "repo_inverso": round(drrp[fr], 3), "repo_inverso_fecha": fr, "tga": round(dtga[f] / 1000, 1),
            "liquidez_neta": round(neta, 1), "liquidez_neta_hace_4_sem": neta_en(prev) if prev else None, "fecha_hace_4_sem": prev,
            "fuente": "FRED (Reserva Federal H.4.1 y Tesoro de EE. UU.): fredgraph.csv?id=WALCL, RRPONTSYD, WTREGEN; WALCL y WTREGEN en M$ y RRP en mil M$, convertidos",
            "nivel": "P"}


def bloque_bce():
    v = [(x["TIME_PERIOD"], float(x["OBS_VALUE"])) for x in csv.DictReader(io.StringIO(bajar(BCE, {"Accept": "text/csv"}))) if x.get("OBS_VALUE")]
    if len(v) < 5:
        raise ValueError("pocas observaciones")
    sem = v[-1][0]
    lunes = datetime.strptime(sem + "-1", "%G-W%V-%u").date()
    return {"serie": "Activo total del Eurosistema (balance consolidado, ILM)", "fecha": sem, "semana_empieza": lunes.isoformat(), "unidad": "mil M€",
            "valor": round(v[-1][1] / 1000, 1), "hace_4_sem": round(v[-5][1] / 1000, 1), "fecha_hace_4_sem": v[-5][0],
            "fuente": "BCE Data Portal, ILM/W.U2.C.T000000.Z5.Z01 (millones de euros, convertidos)", "nivel": "P"}


def main():
    manual = json.loads(RUTA.read_text(encoding="utf-8"))
    fallos = []
    for clave, fn in (("fed", bloque_fed), ("eurosistema", bloque_bce)):
        try:
            manual[clave] = fn()
        except Exception as e:
            fallos.append(f"{clave}: {type(e).__name__}: {e}")
            if clave in manual:
                manual[clave]["conservado_sin_actualizar"] = True   # se mantiene su fecha vieja
    manual["fallos"] = fallos
    if len(fallos) < 2:
        manual["_actualizado"] = date.today().isoformat()
    manual["aviso"] = "jp y cn siguen a mano (sin API abierta fiable; cada uno con su fecha). fed y eurosistema los lee scripts/leer_liquidez.py (FRED y BCE) [P]."
    print(json.dumps({k: manual.get(k) for k in ("fed", "eurosistema", "fallos")}, ensure_ascii=False, indent=1))
    if "--seco" not in sys.argv:
        RUTA.write_text(json.dumps(manual, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
