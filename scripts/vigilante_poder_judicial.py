"""Vigilante de notas del Poder Judicial (C143, sin IA): avisa por Telegram cuando una nota oficial nueva menciona un caso de explorador/espana-judicial.json.

Fuentes (primarias, [P]): archivo de notas de prensa del Tribunal Supremo, noticias de la Audiencia Nacional y noticias judiciales generales de poderjudicial.es.
Solo mira el TITULAR de cada nota y lo compara con las palabras clave de cada caso (sin tildes). No interpreta: el aviso es un titular, no una conclusión,
y recuerda la presunción de inocencia. La memoria de lo ya avisado va en alertas/estado_poder_judicial.json.
Sin TELEGRAM_TOKEN y TELEGRAM_CHAT_ID solo imprime (modo prueba). La primera vez solo apunta lo existente, salvo con --inicial (avisa de lo que haya ahora).
"""
import argparse
import html
import json
import os
import re
import sys
import unicodedata
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESTADO = RAIZ / "alertas" / "estado_poder_judicial.json"
CASOS = RAIZ / "explorador" / "espana-judicial.json"
BASE = "https://www.poderjudicial.es"
FUENTES = [
    ("Tribunal Supremo", BASE + "/cgpj/es/Poder-Judicial/Tribunal-Supremo/Oficina-de-Comunicacion/Archivo-de-notas-de-prensa"),
    ("Audiencia Nacional", BASE + "/cgpj/es/Poder-Judicial/Audiencia-Nacional/Noticias-Judiciales"),
    ("Poder Judicial", BASE + "/cgpj/es/Poder-Judicial/Noticias-Judiciales"),
]
USER_AGENT = "Mozilla/5.0 (cartera-joel; vigilante personal de notas del Poder Judicial)"


def plano(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def leer_notas(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        h = r.read().decode("utf-8", "replace")
    notas = {}
    for href, txt in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", txt)).strip()
        if len(t) > 45 and ("Noticias-Judiciales/" in href or "Archivo-de-notas-de-prensa/" in href):
            notas[href if href.startswith("http") else BASE + href] = t
    return notas


def casos():
    d = json.loads(CASOS.read_text(encoding="utf-8"))
    return [(c["nombre"], [plano(k) for k in c.get("palabras_clave", [])]) for c in d["casos"]]


def coincidencias(titular, lista):
    t = plano(titular)
    return [n for n, ks in lista if any(re.search(r"\b" + re.escape(k) + r"\b", t) for k in ks)]


def mensaje(fuente, titular, url, nombres):
    return "\n".join([f"⚖️ <b>Poder Judicial</b> · {html.escape(fuente)}", f"<b>{html.escape(titular)}</b>",
                      "Caso(s): " + html.escape("; ".join(nombres)),
                      f'<a href="{html.escape(url)}">Leer la nota oficial</a> [P]',
                      "Titular de una nota oficial; no es una condena. Presunción de inocencia hasta sentencia firme."])


def enviar(texto):
    token, chat = os.environ.get("TELEGRAM_TOKEN", "").strip(), os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print("[prueba, sin Telegram]\n" + texto + "\n")
        return
    datos = json.dumps({"chat_id": chat, "text": texto, "parse_mode": "HTML", "disable_web_page_preview": True}).encode("utf-8")
    req = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=datos, headers={"Content-Type": "application/json"})
    urllib.request.urlopen(req, timeout=20).read()


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--inicial", action="store_true", help="primera vez: avisar de las notas que ya haya con coincidencia")
    args = ap.parse_args()
    primera = not ESTADO.exists()
    vistos = set(json.loads(ESTADO.read_text(encoding="utf-8")).get("vistos", [])) if not primera else set()
    lista = casos()
    todas, errores = {}, 0
    for nombre, url in FUENTES:
        try:
            for u, t in leer_notas(url).items():
                todas.setdefault(plano(t), (nombre, t, u))     # la misma nota sale en varias portadas: se distingue por el titular
        except Exception as e:
            errores += 1
            print(f"{nombre}: error {type(e).__name__}: {e}", file=sys.stderr)
    nuevas = [(u, f, t) for k, (f, t, u) in todas.items() if k not in vistos]
    avisar = [] if (primera and not args.inicial) else nuevas
    n = 0
    for u, f, t in reversed(avisar):
        nombres = coincidencias(t, lista)
        if nombres:
            enviar(mensaje(f, t, u, nombres))
            n += 1
    if todas:      # si todas las fuentes fallan no se pisa la memoria
        vistos |= set(todas)
        ESTADO.parent.mkdir(exist_ok=True)
        ESTADO.write_text(json.dumps({"vistos": sorted(vistos)[-800:], "ultima": datetime.now(timezone.utc).isoformat(timespec="minutes")}, indent=1), encoding="utf-8")
    print(f"Poder Judicial: {len(todas)} notas leídas, {len(nuevas)} nuevas, {n} avisos{' (primera vez: solo se apuntó lo existente)' if primera and not args.inicial else ''}")
    if errores == len(FUENTES):
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Poder Judicial: error {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
