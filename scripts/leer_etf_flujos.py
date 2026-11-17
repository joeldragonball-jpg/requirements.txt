"""Acumula instantáneas de ETF spot (acciones, NAV, tenencia) en explorador/etf-flujos.json y calcula el flujo
entre dos instantáneas consecutivas: flujo = (acciones_t - acciones_t-1) x NAV_t. SOLO LECTURA de datos ya leídos (sin red, sin IA).
Las webs de emisores (bitxrpetf.com, 21shares.com) son SPA: se leen en Chrome y se pasan por argumentos.
Uso: python scripts/leer_etf_flujos.py --ticker XRP --fecha 2026-11-12 --acciones 36440000 --nav 11.53 --tenencia 406770577.61 --fuente URL
"""
import argparse
import json
from datetime import date, timedelta
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "explorador" / "etf-flujos.json"


def dia_habil_siguiente(f):
    d = f + timedelta(days=1)
    while d.weekday() >= 5:
        d += timedelta(days=1)
    return d


def es_trimestral(h):
    t = f"{h.get('nivel', '')} {h.get('fuente', '')} {h.get('nota', '')}".lower()
    return "10-q" in t or "trimestral" in t


def flujo_valido(a, b):
    """Flujo diario solo entre dos instantaneas de dias habiles consecutivos y no trimestrales/derivadas; si no, (False, motivo)."""
    if es_trimestral(a) or es_trimestral(b):
        return False, "alguna instantanea es trimestral (10-Q): la diferencia no es un flujo diario"
    if "derivad" in f"{a.get('nivel', '')} {b.get('nivel', '')}".lower():
        return False, "acciones derivadas (no leidas del emisor): flujo no fiable"
    fa, fb = date.fromisoformat(a["fecha"]), date.fromisoformat(b["fecha"])
    if dia_habil_siguiente(fa) != fb:
        return False, f"las instantaneas ({a['fecha']} y {b['fecha']}) no son de dias habiles consecutivos"
    return True, None


UA = "cartera-lector/1.0 (lectura publica de EDGAR; contacto generico)"
CUSIP = {"09174F107": "XRP", "355233107": "XRPZ", "13723M100": "XRPC", "38965L106": "GXRP", "90137T103": "TOXR",
         "92864M780": "XRPI", "26923N231": "XRPR", "38963R105": "GXLM", "46438F101": "IBIT", "315948109": "FBTC"}


def _get(u):
    import urllib.request, time
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=40).read()
        except Exception:
            if i == 2:
                raise
            time.sleep(2)


def leer_13f(ciks, periodo="2026-09-30"):
    """Última 13F-HR del periodo por CIK; suma por CUSIP de interés. Certificados TLS verificados."""
    import re
    import xml.etree.ElementTree as ET
    from datetime import date
    d = json.loads(RUTA.read_text(encoding="utf-8"))
    bloque = d.setdefault("13f_3T", {}).setdefault("lecturas_edgar", {})
    for cik in ciks:
        cik = cik.zfill(10)
        j = json.loads(_get("https://data.sec.gov/submissions/CIK%s.json" % cik))
        r = j["filings"]["recent"]
        cand = [i for i, f in enumerate(r["form"]) if f.startswith("13F-HR") and r["reportDate"][i] == periodo]
        if not cand:
            print(cik, "sin 13F-HR del", periodo); bloque[cik] = {"nombre": j.get("name"), "estado": "no presentado/indexado a " + date.today().isoformat()}; continue
        i = max(cand, key=lambda k: r["filingDate"][k])
        acc = r["accessionNumber"][i]
        base = "https://www.sec.gov/Archives/edgar/data/%d/%s/" % (int(cik), acc.replace("-", ""))
        idx = _get(base + "index.json").decode("utf-8")
        xmls = [x["name"] for x in json.loads(idx)["directory"]["item"] if x["name"].lower().endswith(".xml") and x["name"] != "primary_doc.xml"]
        filas = {}
        for nombre in xmls:
            txt = _get(base + nombre).decode("utf-8")
            txt = re.sub(r'\sxmlns(:\w+)?="[^"]+"', "", txt)
            txt = re.sub(r"<(/?)\w+:", r"<\g<1>", txt)       # quita prefijos de etiqueta (ns1:infoTable)
            txt = re.sub(r"\s\w+:(\w+=)", r" \g<1>", txt)    # y de atributo (xsi:schemaLocation)
            for t in ET.fromstring(txt).iter("infoTable"):
                c = (t.findtext("cusip") or "").strip()
                if c in CUSIP:
                    acc_n = int(t.findtext("shrsOrPrnAmt/sshPrnamt") or 0)
                    val = int(t.findtext("value") or 0)
                    f = filas.setdefault(CUSIP[c], {"acciones": 0, "valor_usd": 0, "filas": 0})
                    f["acciones"] += acc_n; f["valor_usd"] += val; f["filas"] += 1
        bloque[cik] = {"nombre": j.get("name"), "acceso": acc, "presentado": r["filingDate"][i], "url": base,
                       "posiciones": filas, "nivel": "P (EDGAR, infotable XML; posicion a %s, no indica motivo ni fecha de compra)" % periodo,
                       "leido": date.today().isoformat()}
        print(cik, j.get("name"), acc, {k: v["acciones"] for k, v in filas.items()})
    RUTA.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--13f", dest="f13", nargs="+", metavar="CIK", help="lee el 13F-HR del 3T de estos CIK en EDGAR (infotable XML) y lo añade a 13f_3T.lecturas_edgar")
    ap.add_argument("--ticker")
    ap.add_argument("--fecha")
    ap.add_argument("--acciones", type=float)
    ap.add_argument("--nav", type=float)
    ap.add_argument("--tenencia", type=float)
    ap.add_argument("--fuente")
    # C280 (15-nov): datos leidos a mano en la web del emisor con Chrome; opcionales para fondos nuevos o derivados
    ap.add_argument("--aum", type=float)
    ap.add_argument("--nota")
    ap.add_argument("--nivel", default="P (emisor, parte interesada)")
    ap.add_argument("--nombre")
    ap.add_argument("--activo")
    ap.add_argument("--emisor")
    ap.add_argument("--web")
    a = ap.parse_args()
    if a.f13:
        return leer_13f(a.f13)
    if not (a.ticker and a.fecha and a.acciones is not None and a.nav is not None and a.fuente):
        ap.error("faltan --ticker --fecha --acciones --nav --fuente")
    d = json.loads(RUTA.read_text(encoding="utf-8"))
    etf = next((e for e in d["etfs"] if e["ticker"] == a.ticker), None)
    if etf is None:  # fondo nuevo (p. ej. BTC): se crea con los datos opcionales
        etf = {"ticker": a.ticker, "nombre": a.nombre, "activo": a.activo, "emisor": a.emisor, "web": a.web, "historial": [], "flujo_usd": None}
        d["etfs"].append(etf)
    hist = etf.setdefault("historial", [])
    hist[:] = [h for h in hist if h["fecha"] != a.fecha]
    reg = {"fecha": a.fecha, "acciones": a.acciones, "nav": a.nav, "tenencia_monedas": a.tenencia, "fuente": a.fuente, "nivel": a.nivel}
    if a.aum is not None:
        reg["aum_usd"] = a.aum
    if a.nota:
        reg["nota"] = a.nota
    hist.append(reg)
    hist.sort(key=lambda h: h["fecha"])
    for i in range(len(hist)):
        hist[i].pop("flujo_usd", None)
        hist[i].pop("flujo_motivo", None)
    for i in range(1, len(hist)):
        ok, motivo = flujo_valido(hist[i - 1], hist[i])
        if ok:
            hist[i]["flujo_usd"] = round((hist[i]["acciones"] - hist[i - 1]["acciones"]) * hist[i]["nav"])
        else:
            hist[i]["flujo_usd"] = None
            hist[i]["flujo_motivo"] = motivo
    RUTA.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print("ok", a.ticker, len(hist), "instantáneas")


if __name__ == "__main__":
    main()
