"""Aviso diario por Telegram de los eventos del calendario (eventos/calendario.toml). Sin IA, sin APIs de pago.
- Avisa el día antes y el mismo día de cada evento; los lunes añade un resumen de los próximos 7 días.
- Si no hay nada que avisar, no envía nada. Sin TELEGRAM_TOKEN imprime el mensaje (modo prueba)."""
import os
import sys
import tomllib
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

AQUI = Path(__file__).parent
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]


def cargar():
    with open(AQUI / "calendario.toml", "rb") as f:
        evs = tomllib.load(f).get("eventos", [])
    out = []
    for e in evs:
        if e.get("aproximado"):      # fecha sin confirmar: se muestra en la app pero no se avisa por Telegram
            continue
        ini = date.fromisoformat(e["fecha"])
        fin = date.fromisoformat(e.get("hasta", e["fecha"]))
        out.append({**e, "ini": ini, "fin": fin})
    return sorted(out, key=lambda e: e["ini"])


def cuando(d):
    return f"{DIAS[d.weekday()]} {d.day} {MESES[d.month]}"


def linea(e, hoy):
    marca = "🔴" if e.get("impacto") == "alto" else "🟡"
    rango = cuando(e["ini"]) + (f" al {cuando(e['fin'])}" if e["fin"] != e["ini"] else "")
    return f"{marca} <b>{e['titulo']}</b>\n    {rango}. {e.get('detalle', '')}"


def mensaje(hoy, evs, forzar_semana=False):
    hoy_evs = [e for e in evs if e["ini"] <= hoy <= e["fin"]]
    manana = hoy + timedelta(days=1)
    man_evs = [e for e in evs if e["ini"] == manana]
    semana = [e for e in evs if hoy < e["ini"] <= hoy + timedelta(days=7) and e not in man_evs]
    partes = []
    if hoy_evs:
        partes.append("📅 <b>Hoy</b>\n" + "\n".join(linea(e, hoy) for e in hoy_evs))
    if man_evs:
        partes.append("⏭️ <b>Mañana</b>\n" + "\n".join(linea(e, hoy) for e in man_evs))
    if semana and (hoy.weekday() == 0 or forzar_semana):
        partes.append("🗓️ <b>Próximos 7 días</b>\n" + "\n".join(linea(e, hoy) for e in semana))
    if not partes:
        return ""
    return "\n\n".join(partes) + "\n\n<i>Información del calendario oficial, no una recomendación de compra o venta.</i>"


def enviar(texto):
    token = os.environ.get("TELEGRAM_TOKEN", "").strip()
    chat = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print(texto)
        return
    import requests
    r = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", timeout=20,
                      data={"chat_id": chat, "text": texto, "parse_mode": "HTML", "disable_web_page_preview": "true"})
    r.raise_for_status()


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if len(sys.argv) > 1:
        hoy = date.fromisoformat(sys.argv[1])          # prueba: python eventos/avisos.py 2026-10-26
    else:
        try:
            hoy = datetime.now(ZoneInfo("Europe/Madrid")).date()
        except Exception:                               # sin base de zonas horarias (solo ocurre en un PC sin tzdata)
            hoy = date.today()
    texto = mensaje(hoy, cargar(), forzar_semana=os.environ.get("PRUEBA") == "true")
    if texto:
        enviar(texto)
    else:
        print(f"{hoy}: nada que avisar.")
