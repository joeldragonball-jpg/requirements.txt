"""C288: calendario oficial automatico sin IA ni claves. BLS (.ics), BEA (HTML), Eurostat (iCal), INE (HTML), Fed (FOMC) y BCE
(reuniones del Consejo de Gobierno) -> explorador/calendario-oficial.json con fecha, hora, organismo, evento, url y nivel P
para los proximos 90 dias, y comparacion con docs/movil/data.json (solo lectura): faltantes y fechas distintas.
BLS da 403 a scripts: se usa la copia leida con Chrome (explorador/calendario-oficial-bls.ics) y se anota. Certificados verificados.
Uso: python scripts/leer_calendario_oficial.py [--seco] [--dias 90] [--bls ruta.ics]"""
import html
import json
import re
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "calendario-oficial.json"
BLS_COPIA = RAIZ / "explorador" / "calendario-oficial-bls.ics"
DATA = RAIZ / "docs" / "movil" / "data.json"
MESES = {m: i + 1 for i, m in enumerate("january february march april may june july august september october november december".split())}
MESES_ES = {m: i + 1 for i, m in enumerate("enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split())}
URLS = {
    "BLS": ("https://www.bls.gov/schedule/news_release/bls.ics", "https://www.bls.gov/schedule/news_release/"),
    "BEA": ("https://www.bea.gov/news/schedule", "https://www.bea.gov/news/schedule"),
    "Eurostat": ("https://ec.europa.eu/eurostat/o/calendars/eventsIcal", "https://ec.europa.eu/eurostat/web/main/news/release-calendar"),
    "INE": ("https://www.ine.es/dynt3/Calendario/calenHTML.htm", "https://www.ine.es/dynt3/Calendario/calenHTML.htm"),
    "Fed": ("https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"),
    "BCE": ("https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html", "https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html"),
}
# Eventos clave (para la comparacion); el resto se guarda igual pero sin marca «clave».
CLAVE = {
    "BLS": r"Consumer Price Index|Employment Situation|Producer Price|Job Openings|Employment Cost|Real Earnings",
    "BEA": r"Gross Domestic Product|Personal Income|PCE|Trade|Current Account",
    "Eurostat": r"flash estimate|HICP|inflation|unemployment|GDP|Euro indicators",
    "INE": r"Contabilidad Nacional|Encuesta de Poblaci|Precios de Consumo|IPC|Paro|Producci.n Industrial",
    "Fed": r".", "BCE": r".",
}


def bajar(url, cab=None):
    for n in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.4.0", **(cab or {})}), timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                raise
            if n == 2:
                raise
            time.sleep(3)
        except Exception:
            if n == 2:
                raise
            time.sleep(3)


def ev(org, d, hora, zona, titulo, url, **extra):
    return {"fecha": d.isoformat(), "hora": hora, "zona_horaria": zona, "organismo": org, "evento": re.sub(r"\s+", " ", titulo).strip(),
            "url": url, "nivel": "P", "aproximado": False, **extra}


def ics_eventos(txt):
    for b in txt.split("BEGIN:VEVENT")[1:]:
        g = lambda k: (re.search(r"^" + k + r"[^:\n]*:(.*)$", b, re.M) or [None, ""])[1].strip()
        yield g("DTSTART"), g("SUMMARY"), g("X-CATEGORY"), g("CATEGORIES")


def leer_bls(ruta=None):
    via = "descarga directa"
    try:
        if ruta:
            raise PermissionError
        txt = bajar(URLS["BLS"][0])
    except Exception:
        ruta = ruta or BLS_COPIA
        txt = Path(ruta).read_text(encoding="utf-8")
        via = f"copia leida con Chrome ({Path(ruta).name}): curl recibe 403"
    out = []
    for ini, resumen, _, _ in ics_eventos(txt):
        d = datetime.strptime(ini[:8], "%Y%m%d").date()
        h = f"{ini[9:11]}:{ini[11:13]}" if "T" in ini else None
        out.append(ev("BLS (EE. UU.)", d, h, "America/New_York", resumen, URLS["BLS"][1]))
    return out, via


def leer_bea():
    h = bajar(URLS["BEA"][0])
    hoy = date.today()
    out = []
    for fila in re.findall(r"<tr class=\"scheduled-releases-type-(\w+)\">(.*?)</tr>", h, re.S):
        tipo, cuerpo = fila
        m = re.search(r'release-date">([A-Za-z]+) (\d+)<', cuerpo)
        t = re.search(r"<small[^>]*>\s*(\d+):(\d+) (AM|PM)", cuerpo)
        ti = re.search(r'release-title[^>]*>(.*?)</td>', cuerpo, re.S)
        if not (m and ti):
            continue
        mes = MESES[m.group(1).lower()]
        d = date(hoy.year + (1 if mes < hoy.month - 1 else 0), mes, int(m.group(2)))
        hora = None
        if t:
            hh = int(t.group(1)) % 12 + (12 if t.group(3) == "PM" else 0)
            hora = f"{hh:02d}:{t.group(2)}"
        out.append(ev("BEA (EE. UU.)", d, hora, "America/New_York", html.unescape(re.sub(r"<[^>]+>", "", ti.group(1))), URLS["BEA"][1], tipo_bea=tipo))
    return out, "descarga directa"


def leer_eurostat():
    out = []
    for ini, resumen, cat, _ in ics_eventos(bajar(URLS["Eurostat"][0])):
        if "Euro indicators" not in cat:
            continue
        out.append(ev("Eurostat (UE)", datetime.strptime(ini[:8], "%Y%m%d").date(), None, "Europe/Luxembourg", html.unescape(resumen), URLS["Eurostat"][1]))
    return out, "descarga directa (iCal oficial; solo «Euro indicators»; el iCal no trae hora)"


def leer_ine():
    h = bajar(URLS["INE"][0])
    m = re.search(r"Calendario (\d{4})", h)
    anio = int(m.group(1)) if m else date.today().year
    out = []
    for boton, cuerpo in re.findall(r'class="toggle-button nocircle tit">([^<]*)</button>(.*?)(?=class="toggle-button nocircle tit"|$)', h, re.S):
        for dia, mes, per in re.findall(r'headers="col1_p\d+">(\d+)</td>\s*<td headers="col2_p\d+">(\w+)</td>\s*<td headers="col3_p\d+">([^<]*)</td>', cuerpo):
            mm = MESES_ES.get(mes.lower())
            if mm:
                out.append(ev("INE (España)", date(anio, mm, int(dia)), None, "Europe/Madrid", f"{html.unescape(boton.strip())} ({html.unescape(per.strip())})", URLS["INE"][1]))
    return out, f"descarga directa (calendario {anio}; la web del INE aun no publica 2027)"


def leer_fed():
    h = bajar(URLS["Fed"][0])
    out = []
    marcas = [(m.start(), int(m.group(1))) for m in re.finditer(r'<a id="\d+">(\d{4})', h)]
    for mm in re.finditer(r'fomc-meeting__month[^>]*>(.*?)</div>\s*<div[^>]*fomc-meeting__date[^>]*>(.*?)</div>', h, re.S):
        previos = [a for p, a in marcas if p < mm.start()]
        anio = previos[-1] if previos else None
        mes = re.sub(r"<[^>]+>", "", mm.group(1)).strip()
        dias = re.sub(r"<[^>]+>", "", mm.group(2)).strip()
        r = re.match(r"^([A-Za-z]+) (\d+)-(\d+)\*?$", f"{mes} {dias}")
        if not (r and anio and r.group(1).lower() in MESES):
            continue  # reuniones a caballo de dos meses y votos por escrito: se ignoran (no caen en el periodo)
        m = MESES[r.group(1).lower()]
        proy = "*" in dias
        d2 = date(anio, m, int(r.group(3)))
        e = ev("Fed (EE. UU.)", d2, "14:00", "America/New_York",
               f"Reunion FOMC ({r.group(2)}-{r.group(3)} {r.group(1)}): decision de tipos" + (" y proyecciones (SEP)" if proy else ""), URLS["Fed"][1])
        e["desde"] = date(anio, m, int(r.group(2))).isoformat()
        e["aproximado"] = anio > date.today().year  # calendario del año siguiente: la Fed lo marca provisional (tentative)
        out.append(e)
    return out, "descarga directa (2026 y 2027; la hora 14:00 ET es la habitual de la decision, no viene en la tabla)"


def leer_bce():
    h = bajar(URLS["BCE"][0])
    out = []
    for f, desc in re.findall(r"<dt>\s*(\d\d/\d\d/\d{4})\s*</dt>\s*<dd>(.*?)</dd>", h, re.S):
        t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", desc)).strip()
        if "monetary policy meeting" in t.lower() and "non-monetary" not in t.lower():
            d, m, a = map(int, f.split("/"))
            out.append(ev("BCE (zona euro)", date(a, m, d), None, "Europe/Berlin", html.unescape(t), URLS["BCE"][1]))
    return out, "descarga directa (hora de la rueda de prensa no figura en la tabla)"


def comparar(eventos, ini, fin):
    """Compara con eventos ya cargados en docs/movil/data.json (solo lectura): temas clave oficiales sin evento cargado (faltantes)
    y eventos cargados cuyo tema coincide pero con fecha distinta (±12 dias)."""
    try:
        cargados = json.loads(DATA.read_text(encoding="utf-8")).get("eventos", [])
    except Exception as e:
        return {"error": str(e)}
    claves = {
        "IPC EE. UU.": (r"Consumer Price Index$", r"IPC|inflaci.n (de )?EE|CPI"),
        "Empleo EE. UU. (Employment Situation)": (r"Employment Situation", r"empleo|n.minas|nonfarm|NFP"),
        "FOMC": (r"Reunion FOMC", r"FOMC|Fed\b"),
        "BCE tipos": (r"monetary policy meeting \(Day 2\)", r"BCE|ECB"),
        "PIB EE. UU.": (r"Gross Domestic Product", r"PIB.*EE|GDP"),
        "IPCA zona euro (flash)": (r"HICP|inflation", r"IPCA|HICP|inflaci.n.*zona euro"),
        "INE IPC": (r"Precios de Consumo|IPC", r"IPC.*Espa|INE"),
        "INE PIB trimestral": (r"Contabilidad Nacional", r"PIB.*Espa|Contabilidad Nacional"),
    }
    falt, dist, ok = [], [], 0
    for tema, (pat_of, pat_cargado) in claves.items():
        oficiales = [e for e in eventos if re.search(pat_of, e["evento"], re.I) and e.get("fecha_fin", e["fecha"]) and ini <= e["fecha"] <= fin]
        if tema == "BCE tipos":
            oficiales = [e for e in oficiales if "Day 2" in e["evento"]]
        mios = [c for c in cargados if re.search(pat_cargado, c.get("titulo", ""), re.I)]
        for e in oficiales:
            d = date.fromisoformat(e["fecha"])
            exacto = [c for c in mios if c.get("fecha") and (c["fecha"] == e["fecha"] or (c.get("hasta") and c["fecha"] <= e["fecha"] <= c["hasta"]))]
            if exacto:
                ok += 1
                continue
            cerca = [c for c in mios if c.get("fecha") and abs((date.fromisoformat(c["fecha"]) - d).days) <= 12]
            fila = {"tema": tema, "organismo": e["organismo"], "fecha_oficial": e["fecha"], "evento_oficial": e["evento"]}
            if cerca:
                dist.append({**fila, "cargado": [{"fecha": c["fecha"], "titulo": c["titulo"]} for c in cerca]})
            else:
                falt.append(fila)
    return {"eventos_en_data_json": len(cargados), "coinciden": ok, "faltantes": falt, "fechas_distintas": dist,
            "nota": "Heuristica por tema/palabras (±12 dias); revisar a mano antes de tocar eventos/calendario.toml"}


def main():
    seco = "--seco" in sys.argv
    dias = int(sys.argv[sys.argv.index("--dias") + 1]) if "--dias" in sys.argv else 90
    bls = sys.argv[sys.argv.index("--bls") + 1] if "--bls" in sys.argv else None
    hoy = date.today()
    ini, fin = hoy.isoformat(), (hoy + timedelta(days=dias)).isoformat()
    lectores = [("BLS", lambda: leer_bls(bls)), ("BEA", leer_bea), ("Eurostat", leer_eurostat), ("INE", leer_ine), ("Fed", leer_fed), ("BCE", leer_bce)]
    todos, estado = [], {}
    for nombre, fn in lectores:
        try:
            lista, via = fn()
            dentro = [e for e in lista if ini <= e["fecha"] <= fin]
            for e in dentro:
                e["clave"] = bool(re.search(CLAVE[nombre], e["evento"], re.I))
            todos += dentro
            estado[nombre] = {"ok": True, "via": via, "en_periodo": len(dentro), "leidos": len(lista)}
        except Exception as e:
            estado[nombre] = {"ok": False, "error": f"{type(e).__name__}: {str(e)[:120]}"}
    todos.sort(key=lambda e: (e["fecha"], e.get("hora") or "99:99", e["organismo"]))
    res = {"generado": datetime.now(timezone.utc).isoformat(timespec="seconds"), "periodo": {"desde": ini, "hasta": fin},
           "aviso": "Fechas y horas de calendarios oficiales de cada organismo (nivel P). Horas en la zona indicada; null = el calendario no la da. Sin IA.",
           "fuentes": estado, "eventos": todos, "comparacion": comparar(todos, ini, fin)}
    if seco:
        print(json.dumps({k: v for k, v in res.items() if k != "eventos"}, ensure_ascii=False, indent=1)[:3500])
        print(len(todos), "eventos")
        return
    SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(todos)} eventos -> {SALIDA.name}; fuentes: " + ", ".join(f"{k}={'ok' if v['ok'] else 'FALLO'}" for k, v in estado.items()))
    c = res["comparacion"]
    print("faltantes:", len(c.get("faltantes", [])), "| fechas distintas:", len(c.get("fechas_distintas", [])), "| coinciden:", c.get("coinciden"))


if __name__ == "__main__":
    main()
