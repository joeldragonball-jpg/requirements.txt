"""Lector de SEC EDGAR en SOLO LECTURA (sin IA, sin claves): filings de los últimos 30 días sobre XRP, XLM, Stellar Lumens y Ripple.

Reutiliza la consulta, los formularios y el User-Agent de scripts/vigilante_edgar.py (sin modificarlo).
Escribe explorador/edgar.json con, por filing: fecha, formulario, entidad, asunto, URL en sec.gov y nivel [P].
No envía nada a Telegram ni toca alertas/estado_edgar.json. Certificados TLS verificados (valor por defecto de urllib).
Uso: python scripts/leer_edgar.py [--dias 30]
Nota: las solicitudes SR-DTC (DTCC) NO están en EDGAR (van a sec.gov/rules) [VERIFICAR otra vía].
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vigilante_edgar as v   # solo importa constantes y enlace(); su main() no se ejecuta

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "edgar.json"


def consultar(desde, hasta):
    """Como v.buscar pero conserva el asunto (file_description/items) y pagina hasta 200 resultados."""
    todos = []
    for inicio in range(0, 200, 100):
        params = {"q": v.CONSULTA, "forms": v.FORMULARIOS, "dateRange": "custom", "startdt": desde, "enddt": hasta, "from": inicio}
        peticion = urllib.request.Request(v.API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": v.USER_AGENT})
        for intento in range(3):
            try:
                with urllib.request.urlopen(peticion, timeout=30) as r:
                    cuerpo = json.loads(r.read().decode("utf-8"))
                break
            except urllib.error.HTTPError as e:
                if e.code < 500 or intento == 2:
                    raise
                time.sleep(3)
        golpes = cuerpo.get("hits", {}).get("hits", [])
        todos += golpes
        if len(golpes) < 100:
            break
    return todos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=30)
    args = ap.parse_args()
    hoy = datetime.now(timezone.utc).date()
    desde = (hoy - timedelta(days=args.dias)).isoformat()
    filings, vistos = [], set()
    for h in consultar(desde, hoy.isoformat()):
        s = h["_source"]
        d = {"id": h["_id"], "form": s.get("form", "?"), "fecha": s.get("file_date", ""),
             "emisor": "; ".join(s.get("display_names") or ["?"])[:140],
             "cik": (s.get("ciks") or [""])[0], "adsh": s.get("adsh", "")}
        if d["id"] in vistos:
            continue
        vistos.add(d["id"])
        asunto = s.get("file_description") or ""
        items = s.get("items") or []
        if items:
            asunto = (asunto + " " if asunto else "") + "items " + ",".join(items)
        filings.append({"fecha": d["fecha"], "formulario": d["form"], "entidad": d["emisor"], "asunto": asunto or "(sin descripción en EDGAR)",
                        "url": v.enlace(d), "nivel": "[P]", "accesion": d["adsh"]})
    filings.sort(key=lambda f: (f["fecha"], f["formulario"]), reverse=True)
    SALIDA.write_text(json.dumps({"generado": datetime.now(timezone.utc).isoformat(timespec="minutes"), "ventana_dias": args.dias,
                                  "desde": desde, "hasta": hoy.isoformat(), "fuente": "efts.sec.gov (búsqueda de texto completo) [P]",
                                  "consulta": v.CONSULTA, "formularios": v.FORMULARIOS, "plazo_13f_3T": v.PLAZO_13F.isoformat(),
                                  "nota": "Las SR-DTC (DTCC) no están en EDGAR; ver sec.gov/rules [VERIFICAR]. Coincidencia de texto != relevancia: revisar cada documento.",
                                  "n": len(filings), "filings": filings}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"EDGAR: {len(filings)} filings entre {desde} y {hoy.isoformat()} -> {SALIDA}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"EDGAR: error {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
