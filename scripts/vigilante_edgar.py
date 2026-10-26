"""Vigilante de SEC EDGAR (sin IA): avisa por Telegram de filings nuevos sobre XRP, XLM/Stellar y Ripple (ETF, fideicomisos, tesorerías).

Fuente: búsqueda de texto completo de EDGAR (efts.sec.gov, primaria, [P]) con User-Agent identificado, como pide la SEC.
La memoria de lo ya avisado va en alertas/estado_edgar.json. Sin TELEGRAM_TOKEN y TELEGRAM_CHAT_ID solo imprime (modo prueba).
La primera vez solo apunta lo existente, sin avisar, salvo con --inicial N (avisa de los de los últimos N días).
También avisa una vez, desde 7 días antes, del plazo de los 13F del 3T (45 días tras el cierre del trimestre).
DTCC: sus solicitudes SR-DTC no están en EDGAR (van a sec.gov/rules); este vigilante no las cubre [VERIFICAR otra vía].
"""
import argparse
import html
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ESTADO = Path(__file__).resolve().parent.parent / "alertas" / "estado_edgar.json"
API = "https://efts.sec.gov/LATEST/search-index"
CONSULTA = '"XRP" OR "XLM" OR "Stellar Lumens" OR "Ripple"'
FORMULARIOS = "S-1,19b-4,8-A12B,424B2,424B3,424B4,8-K"   # S-1 ya incluye las enmiendas S-1/A (con «/A» la API devuelve de menos)
USER_AGENT = os.environ.get("EDGAR_USER_AGENT", "cartera-joel/1.0 (uso personal; vigilante EDGAR)")
PLAZO_13F = date(2026, 11, 16)   # 45 días tras el 30-sep es el 14-nov (sábado): pasa al lunes 16 [VERIFICAR en sec.gov]


def buscar(desde, hasta):
    params = {"q": CONSULTA, "forms": FORMULARIOS, "dateRange": "custom", "startdt": desde, "enddt": hasta}
    peticion = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": USER_AGENT})
    for intento in range(3):    # la API de EDGAR da algún 500 suelto
        try:
            with urllib.request.urlopen(peticion, timeout=30) as r:
                golpes = json.loads(r.read().decode("utf-8")).get("hits", {}).get("hits", [])
            break
        except urllib.error.HTTPError as e:
            if e.code < 500 or intento == 2:
                raise
            time.sleep(3)
    return [{"id": h["_id"], "form": h["_source"].get("form", "?"), "fecha": h["_source"].get("file_date", ""),
             "emisor": "; ".join(h["_source"].get("display_names") or ["?"])[:140],
             "cik": (h["_source"].get("ciks") or [""])[0], "adsh": h["_source"].get("adsh", "")} for h in golpes]


def enlace(d):
    acc, _, archivo = d["id"].partition(":")
    cik = str(int(d["cik"])) if d["cik"] else ""
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{archivo}" if cik and archivo else "https://www.sec.gov/edgar/search/"


def mensaje(d):
    return "\n".join([f"📑 <b>SEC EDGAR</b> · {html.escape(d['form'])} · {d['fecha']}", f"<b>{html.escape(d['emisor'])}</b>",
                      f'<a href="{html.escape(enlace(d))}">Leer el documento en sec.gov</a> [P]'])


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
    ap.add_argument("--inicial", type=int, default=0, help="primera vez: avisar de los filings de los últimos N días")
    ap.add_argument("--dias", type=int, default=7, help="ventana de búsqueda en días")
    args = ap.parse_args()
    primera = not ESTADO.exists()
    memoria = json.loads(ESTADO.read_text(encoding="utf-8")) if not primera else {}
    vistos = set(memoria.get("vistos", []))
    hoy = datetime.now(timezone.utc).date()
    docs = buscar((hoy - timedelta(days=max(args.dias, args.inicial))).isoformat(), hoy.isoformat())
    nuevos = [d for d in docs if d["id"] not in vistos]
    if primera and not args.inicial:
        a_avisar = []
    elif primera:
        corte = (hoy - timedelta(days=args.inicial)).isoformat()
        a_avisar = [d for d in nuevos if d["fecha"] >= corte]
    else:
        a_avisar = nuevos
    for d in sorted(a_avisar, key=lambda x: x["fecha"]):
        enviar(mensaje(d))
    aviso_13f = memoria.get("aviso_13f", "")
    if not aviso_13f and timedelta(0) <= PLAZO_13F - hoy <= timedelta(days=7):
        enviar(f"📑 <b>SEC EDGAR</b> · Plazo de los 13F del 3T: {PLAZO_13F.isoformat()} (fecha por confirmar en sec.gov). "
               "Muestran qué fondos tenían ETF/tesorerías de XRP y XLM a 30-sep.")
        aviso_13f = hoy.isoformat()
    vistos |= {d["id"] for d in docs}
    ESTADO.write_text(json.dumps({"vistos": sorted(vistos)[-500:], "aviso_13f": aviso_13f,
                                  "ultima": datetime.now(timezone.utc).isoformat(timespec="minutes")}, indent=1), encoding="utf-8")
    print(f"EDGAR: {len(docs)} filings en la ventana, {len(a_avisar)} avisos{' (primera vez: solo se apuntó lo existente)' if primera and not args.inicial else ''}.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:      # un fallo no debe tumbar el flujo
        print(f"EDGAR: error {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
