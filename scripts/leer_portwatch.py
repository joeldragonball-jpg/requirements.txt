"""Lee el tráfico diario del estrecho de Ormuz en IMF PortWatch (API ArcGIS pública) y escribe explorador/ormuz-portwatch.json.
Sin IA y sin claves. Si la fuente falla, conserva el archivo anterior y sale con 1.
Uso: python scripts/leer_portwatch.py"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "ormuz-portwatch.json"
URL = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query"
PORTAL = "https://portwatch.imf.org"


def main():
    hoy = datetime.now(timezone.utc)
    desde = (hoy - timedelta(days=365)).strftime("%Y-%m-%d")
    q = urllib.parse.urlencode({
        "where": "portname = 'Strait of Hormuz' AND date >= DATE '%s'" % desde,
        "outFields": "date,n_total,n_tanker", "orderByFields": "date ASC",
        "resultRecordCount": 2000, "returnGeometry": "false", "f": "json"})
    try:
        req = urllib.request.Request(URL + "?" + q, headers={"User-Agent": "cartera-explorador/1.0"})
        with urllib.request.urlopen(req, timeout=40) as r:
            d = json.loads(r.read().decode("utf-8"))
        filas = [f["attributes"] for f in d.get("features", [])]
        serie = [{"fecha": a["date"], "total": a["n_total"], "petroleros": a["n_tanker"]}
                 for a in filas if a.get("date") and a.get("n_total") is not None]
        if not serie:
            raise ValueError("respuesta sin datos")
    except Exception as e:
        print("AVISO: PortWatch no se pudo leer (%s); se conserva el archivo anterior." % e)
        return 1
    out = {
        "leido": hoy.strftime("%Y-%m-%d %H:%M UTC"),
        "fuente": "IMF PortWatch, Daily_Chokepoints_Data, Strait of Hormuz (" + PORTAL + ")",
        "nivel": "P",
        "aviso": "Tránsitos diarios de buques detectados por AIS (unidades: buques/día). Retraso de 2-3 días. Mide tráfico, no explica la causa; "
                 "el AIS puede estar apagado en parte de la flota. [VERIFICAR] la causa con UKMTO y agencias.",
        "serie": serie,
    }
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("ormuz-portwatch.json: %d días, último %s" % (len(serie), serie[-1]["fecha"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
