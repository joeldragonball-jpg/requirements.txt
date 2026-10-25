"""Vigilante del Federal Register (sin IA): avisa por Telegram de documentos nuevos sobre cripto, stablecoins y tokenización.

Fuente: API abierta del Federal Register (primaria, [P]). La memoria de lo ya avisado va en alertas/estado_federal_register.json.
Sin TELEGRAM_TOKEN y TELEGRAM_CHAT_ID solo imprime (modo prueba). La primera vez solo apunta lo existente, sin avisar,
salvo con --inicial N (avisa de los de los últimos N días).
"""
import argparse
import html
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ESTADO = Path(__file__).resolve().parent.parent / "alertas" / "estado_federal_register.json"
API = "https://www.federalregister.gov/api/v1/documents.json"
TERMINOS = '"digital asset" OR stablecoin OR "crypto asset" OR tokenization OR cryptocurrency OR "virtual currency" OR "payment stablecoin"'
CAMPOS = ("title", "document_number", "html_url", "publication_date", "type", "agency_names", "abstract")
TIPOS = {"Rule": "Norma final", "Proposed Rule": "Propuesta de norma", "Notice": "Aviso", "Presidential Document": "Documento presidencial"}
USER_AGENT = "cartera-joel/1.0 (uso personal; vigilante Federal Register)"


def buscar(desde):
    params = [("conditions[term]", TERMINOS), ("conditions[publication_date][gte]", desde), ("order", "newest"), ("per_page", "50")]
    params += [("fields[]", c) for c in CAMPOS]
    peticion = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(peticion, timeout=30) as r:
        return json.loads(r.read().decode("utf-8")).get("results", [])


def mensaje(d):
    agencias = ", ".join(d.get("agency_names") or []) or "sin agencia"
    resumen = (d.get("abstract") or "").strip()
    if len(resumen) > 300:
        resumen = resumen[:297].rsplit(" ", 1)[0] + "…"
    partes = [f"🏛️ <b>Federal Register</b> · {html.escape(TIPOS.get(d['type'], d['type']))} · {d['publication_date']}",
              f"<b>{html.escape(d['title'])}</b>", html.escape(agencias)]
    if resumen:
        partes.append(html.escape(resumen))
    partes.append(f'<a href="{html.escape(d["html_url"])}">Leer en federalregister.gov</a> [P]')
    return "\n".join(partes)


def enviar(texto):
    token, chat = os.environ.get("TELEGRAM_TOKEN", "").strip(), os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print("[prueba, sin Telegram]\n" + texto + "\n")
        return
    datos = json.dumps({"chat_id": chat, "text": texto, "parse_mode": "HTML", "disable_web_page_preview": True}).encode("utf-8")
    peticion = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=datos, headers={"Content-Type": "application/json"})
    urllib.request.urlopen(peticion, timeout=20).read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inicial", type=int, default=0, help="primera vez: avisar de los documentos de los últimos N días")
    ap.add_argument("--dias", type=int, default=14, help="ventana de búsqueda en días")
    args = ap.parse_args()
    primera = not ESTADO.exists()
    vistos = set(json.loads(ESTADO.read_text(encoding="utf-8")).get("vistos", [])) if not primera else set()
    hoy = datetime.now(timezone.utc).date()
    docs = buscar((hoy - timedelta(days=max(args.dias, args.inicial))).isoformat())
    nuevos = [d for d in docs if d["document_number"] not in vistos]
    if primera and not args.inicial:
        nuevos_a_avisar = []
    elif primera:
        corte = (hoy - timedelta(days=args.inicial)).isoformat()
        nuevos_a_avisar = [d for d in nuevos if d["publication_date"] >= corte]
    else:
        nuevos_a_avisar = nuevos
    for d in reversed(nuevos_a_avisar):     # del más antiguo al más nuevo
        enviar(mensaje(d))
    vistos |= {d["document_number"] for d in docs}
    ESTADO.write_text(json.dumps({"vistos": sorted(vistos)[-500:], "ultima": datetime.now(timezone.utc).isoformat(timespec="minutes")}, indent=1), encoding="utf-8")
    print(f"Federal Register: {len(docs)} documentos en la ventana, {len(nuevos_a_avisar)} avisos{' (primera vez: solo se apuntó lo existente)' if primera and not args.inicial else ''}.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:      # un fallo no debe tumbar el flujo
        print(f"Federal Register: error {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
