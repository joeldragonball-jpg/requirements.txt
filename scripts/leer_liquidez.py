"""C285: liquidez global sin IA ni claves. Lee FRED (CSV público: WALCL, RRPONTSYD, WTREGEN), el BCE (SDMX, ILM), el Banco de Japón
(PDF de Money Stock, Monetary Base y HTML de Cuentas del BoJ; requiere pdftotext) y el PBoC (informe de estadísticas financieras en inglés) [P]
y los vuelca en explorador/liquidez-manual.json (claves «fed», «eurosistema», «jp» y «cn»).
Si una serie no se puede leer se conserva el bloque anterior con su fecha vieja y se anota en «fallos». Certificados verificados.
Uso: python scripts/leer_liquidez.py [--seco]"""
import csv
import io
import json
import re
import subprocess
import sys
import tempfile
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


def bajar_bytes(url):
    for n in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=40) as r:
                return r.read()
        except Exception:
            if n == 2:
                raise
            time.sleep(3)


def pdf_texto(url):
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "x.pdf"
        f.write_bytes(bajar_bytes(url))
        return subprocess.run(["pdftotext", "-raw", str(f), "-"], capture_output=True, text=True, check=True).stdout


def num(x):
    return float(x.replace(",", ""))


def fila_pdf(lineas, marca):
    """(fila interanual, fila de nivel) a ambos lados de la marca de unidades del PDF del BoJ."""
    i = next(k for k, l in enumerate(lineas) if marca in l)
    yoy = next(l for l in reversed(lineas[:i]) if re.match(r"^\d+ ", l))
    filas = []
    for l in lineas[i + 1:i + 8]:
        if l.startswith("(") and filas:
            break
        if re.match(r"^\d+ ", l):
            filas.append(l)
    niv = filas[-1]
    return yoy.replace(" r ", " ").split(), niv.replace(" r ", " ").split()


def bloque_jp():
    B = "https://www.boj.or.jp/en/statistics/"
    ms = re.findall(r"money/ms/(ms\d{4})\.pdf", bajar(B + "money/ms/index.htm"))[0]
    mb = re.findall(r"other/mb/(base\d{4})\.pdf", bajar(B + "boj/other/mb/index.htm"))[0]
    yy, mm = "20" + ms[2:4], ms[4:6]
    ty, tn = fila_pdf(pdf_texto(f"{B}money/ms/{ms}.pdf").splitlines(), "(Average amounts outstanding, trillions of yen)")
    by, bn = fila_pdf(pdf_texto(f"{B}boj/other/mb/{mb}.pdf").splitlines(), "(Average amounts outstanding, 100 million yen)")
    acc = re.findall(r"release/2026/(ac\d{6})\.htm", bajar(B + "boj/other/acmai/index.htm"))
    acc = sorted(set(acc), reverse=True)

    def cuentas(a):
        h = bajar(f"{B}boj/other/acmai/release/2026/{a}.htm")
        t = re.sub(r"<[^>]+>", " ", h).replace("&nbsp;", " ")
        f = re.search(r"Accounts \(([A-Za-z]+) (\d+), (\d{4})\)", t)
        v = sorted({num(x) for x in re.findall(r"\d{3},\d{3},\d{3},\d{3}", t)})
        return f"{f.group(3)}-{datetime.strptime(f.group(1), '%B').month:02d}-{int(f.group(2)):02d}", v[-1] / 1e9, v[-2] / 1e9
    f1, tot1, jgb1 = cuentas(acc[0])
    f0, tot0, _ = cuentas(acc[3] if len(acc) > 3 else acc[-1])
    return {"serie": "Japón: M2 (Money Stock), base monetaria y balance del BoJ",
            "fecha": f"{yy}-{mm}", "unidad": "billones de yenes (1 billón = 10^12 JPY)",
            "m2_interanual": float(ty[1]), "m2_nivel": num(tn[1]),
            "base_monetaria_interanual": float(by[1]), "base_monetaria_nivel": round(num(bn[1]) / 1e4, 1),
            "balance_boj_fecha": f1, "balance_boj": round(tot1, 1), "bonos_jgb_boj": round(jgb1, 1),
            "balance_boj_hace_4_sem": round(tot0, 1), "fecha_hace_4_sem": f0,
            "interanual": float(ty[1]),
            "fuente": "Banco de Japón: Money Stock (PDF %s, promedio mensual de saldos, preliminar), Monetary Base (PDF %s) y Cuentas del BoJ cada diez días (HTML, miles de yenes convertidos); pdftotext" % (ms, mb),
            "nivel": "P"}


def bloque_cn():
    base = "http://www.pbc.gov.cn"
    h = bajar(base + "/en/3688247/3688978/3709137/index.html")
    m = re.search(r'href="(/en/3688247/3688978/3709137/\d+/index\.html)"[^>]*>\s*(Financial Statistics Report \(([^)]+)\))', h)
    if not m:
        raise ValueError("sin informe en la lista")
    per = re.sub(r"[^ -~]", " ", m.group(3))
    t = re.sub(r"<[^>]+>", " ", bajar(base + m.group(1)))
    mm = re.search(r"M2\) stood at RMB\s*([\d.]+) trillion, (?:rising|growing|up|increasing|falling|down)[a-z ]* by ([\d.]+) percent", t)
    if not mm:
        raise ValueError("no se encuentra M2 en el informe")
    meses = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    y = re.search(r"(20\d\d)", per).group(1)
    mes = next((v for k, v in meses.items() if k in per), {"Q1": 3, "H1": 6, "Q1-Q3": 9, "2025": 12}.get(per.replace(y, "").strip()))
    if not mes:
        raise ValueError("periodo no reconocido: " + per)
    m1 = re.search(r"\(M1\), at RMB\s*([\d.]+) trillion, grew by ([\d.]+) percent", t)
    return {"serie": "China: M2 (oferta monetaria amplia) al cierre del periodo", "fecha": f"{y}-{mes:02d}", "unidad": "billones de yuanes (1 billón = 10^12 CNY)",
            "m2_nivel": float(mm.group(1)), "interanual": float(mm.group(2)),
            "m1_nivel": float(m1.group(1)) if m1 else None, "m1_interanual": float(m1.group(2)) if m1 else None,
            "balance_pboc": None, "balance_pboc_motivo": "la web en inglés del PBoC solo tiene las hojas de balance de la autoridad monetaria hasta 2025; no se estima",
            "fuente": "PBoC, Financial Statistics Report (%s), %s%s" % (per, base, m.group(1)), "nivel": "P"}


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
    for clave, fn in (("fed", bloque_fed), ("eurosistema", bloque_bce), ("jp", bloque_jp), ("cn", bloque_cn)):
        try:
            manual[clave] = fn()
        except Exception as e:
            fallos.append(f"{clave}: {type(e).__name__}: {e}")
            if clave in manual:
                manual[clave]["conservado_sin_actualizar"] = True   # se mantiene su fecha vieja
    manual["fallos"] = fallos
    if len(fallos) < 4:
        manual["_actualizado"] = date.today().isoformat()
    manual["aviso"] = "fed, eurosistema, jp y cn los lee scripts/leer_liquidez.py de fuentes oficiales (FRED, BCE, Banco de Japón, PBoC) [P]; cada bloque lleva su fecha. China: la web en inglés del PBoC va con retraso y sin balance del banco central; Japón requiere pdftotext."
    print(json.dumps({k: manual.get(k) for k in ("fed", "eurosistema", "jp", "cn", "fallos")}, ensure_ascii=False, indent=1))
    if "--seco" not in sys.argv:
        RUTA.write_text(json.dumps(manual, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
