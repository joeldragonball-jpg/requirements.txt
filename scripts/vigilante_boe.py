"""Vigilante del BOE (sin IA): avisa de leyes, reales decretos-ley y convalidaciones de la sección I del sumario diario.

Fuente: API de datos abiertos del BOE (primaria, [P]). Memoria en alertas/estado_boe.json.
Sin TELEGRAM_TOKEN y TELEGRAM_CHAT_ID solo imprime. La primera vez solo apunta lo existente (salvo --inicial N días).
NO está activado en workflows.
"""
import argparse, html, json, os, re, urllib.request
from datetime import date, timedelta
from pathlib import Path

ESTADO = Path(__file__).resolve().parent.parent / "alertas" / "estado_boe.json"
API = "https://www.boe.es/datosabiertos/api/boe/sumario/"
PATRON = re.compile(r"^(Ley|Real Decreto-ley|Real Decreto Legislativo|Resoluci[oó]n .*convalidaci)|Real Decreto-ley", re.I)
CLAVES = re.compile(r"cripto|activos digitales|MiCA|mercado de valores|IRPF|impuesto|vivienda|arrendamiento|pensi|Seguridad Social|salario|energ|presupuesto|CNMV|ahorro", re.I)


def sumario(d):
    r = urllib.request.Request(API + d.strftime("%Y%m%d"), headers={"Accept": "application/json", "User-Agent": "cartera-joel/1.0 (vigilante BOE)"})
    try:
        return json.loads(urllib.request.urlopen(r, timeout=30).read())
    except Exception:
        return None


def lista(x):
    return x if isinstance(x, list) else ([x] if x else [])


def items(d):
    j = sumario(d)
    if not j:
        return
    for dia in lista(j.get("data", {}).get("sumario", {}).get("diario")):
        for s in lista(dia.get("seccion")):
            if s.get("codigo") != "1":
                continue
            for dep in lista(s.get("departamento")):
                for ep in lista(dep.get("epigrafe")):
                    for it in lista(ep.get("item")):
                        yield it


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=3)
    ap.add_argument("--inicial", type=int, default=0)
    a = ap.parse_args()
    primera = not ESTADO.exists()
    vistos = set() if primera else set(json.loads(ESTADO.read_text(encoding="utf-8")).get("vistos", []))
    hoy = date.today()
    nuevos = []
    for i in range(max(a.dias, a.inicial)):
        for it in items(hoy - timedelta(days=i)):
            t = it.get("titulo", "")
            if PATRON.search(t) and it["identificador"] not in vistos:
                nuevos.append((it["identificador"], t, it.get("url_html", "")))
    if primera and not a.inicial:
        aviso = []
    else:
        aviso = nuevos
    for ident, t, url in aviso:
        marca = "⭐ " if CLAVES.search(t) else ""
        print(f"[BOE] {marca}{html.unescape(t)[:300]}\n{url} [P]\n")
        tok, chat = os.environ.get("TELEGRAM_TOKEN", "").strip(), os.environ.get("TELEGRAM_CHAT_ID", "").strip()
        if tok and chat:
            datos = json.dumps({"chat_id": chat, "text": f"🏛️ BOE {marca}{t[:300]}\n{url}", "disable_web_page_preview": True}).encode()
            urllib.request.urlopen(urllib.request.Request(f"https://api.telegram.org/bot{tok}/sendMessage", data=datos, headers={"Content-Type": "application/json"}), timeout=20).read()
    ESTADO.parent.mkdir(exist_ok=True)
    ESTADO.write_text(json.dumps({"vistos": sorted(vistos | {n[0] for n in nuevos})[-2000:]}, ensure_ascii=False), encoding="utf-8")
    print(f"{len(nuevos)} norma(s) nueva(s); avisadas {len(aviso)}.")


if __name__ == "__main__":
    main()
