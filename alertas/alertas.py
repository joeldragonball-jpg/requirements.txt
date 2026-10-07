"""Alertas de precio por Telegram para la cartera cripto.

Lo ejecuta GitHub Actions cada 30 minutos (.github/workflows/alertas.yml).
La configuración está en alertas/config.toml y la memoria entre ejecuciones en alertas/estado.json.
"""
import csv
import html
import io
import json
import os
import sys
import time
import tomllib
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

AQUI = Path(__file__).parent
CONFIG = tomllib.loads((AQUI / "config.toml").read_text(encoding="utf-8"))
ESTADO_PATH = AQUI / "estado.json"
MADRID = ZoneInfo("Europe/Madrid")

TG_TOKEN = os.environ.get("TELEGRAM_TOKEN", "").strip()
TG_CHAT = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
PRUEBA = os.environ.get("PRUEBA", "").lower() == "true"


# ---------------------------------------------------------------- formato
def fmt(x, dec=2, sign=False):
    s = f"{x:{'+' if sign else ''},.{dec}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def eur(x, dec=2, sign=False):
    return fmt(x, dec, sign) + " €"


def dec_precio(p):
    return 4 if p < 10 else 2


def parse_num(x):
    s = str(x or "").replace("€", "").replace("%", "").replace("\xa0", "").replace(" ", "").strip()
    if not s:
        return None
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None


# ---------------------------------------------------------------- Telegram
def telegram(metodo, **datos):
    r = requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/{metodo}", json=datos, timeout=15)
    if not r.ok:
        print(f"Telegram {metodo} falló: {r.status_code} {r.text}")
    return r.json() if r.ok else {}


def enviar(texto):
    telegram("sendMessage", chat_id=TG_CHAT, text=texto, parse_mode="HTML", disable_web_page_preview=True)


def descubrir_chat_id():
    """Sin TELEGRAM_CHAT_ID: muestra en el registro de GitHub el chat_id de quien escribió al bot."""
    chats = {}
    for u in telegram("getUpdates").get("result", []):
        chat = (u.get("message") or {}).get("chat")
        if chat:
            chats[chat["id"]] = chat.get("first_name") or chat.get("title") or ""
    if not chats:
        print("No encuentro mensajes. Abre tu bot en Telegram, pulsa INICIAR o escríbele 'hola' y vuelve a ejecutar.")
    for cid, nombre in chats.items():
        print(f">>> Tu TELEGRAM_CHAT_ID es: {cid}  ({nombre}). Guárdalo como secreto en GitHub.")


# ---------------------------------------------------------------- datos de mercado
def precios_actuales(pares):
    res = requests.get("https://api.kraken.com/0/public/Ticker",
                       params={"pair": ",".join(pares.values())}, timeout=15).json()["result"]
    out = {}
    for tok in pares:
        clave = next((k for k in res if tok in k), None)
        if clave:
            out[tok] = float(res[clave]["c"][0])
    return out


def cambio_24h(par, actual):
    js = requests.get("https://api.kraken.com/0/public/OHLC",
                      params={"pair": par, "interval": 60}, timeout=15).json()
    velas = next(v for k, v in js["result"].items() if k != "last")
    objetivo = time.time() - 24 * 3600
    antes = [v for v in velas if v[0] <= objetivo]
    if not antes:
        return None
    return (actual / float(antes[-1][4]) - 1) * 100


def leer_cartera(tokens):
    """Cantidad e inversión por token desde la hoja de resumen."""
    # El identificador de la hoja ya no está en el código (el repo es público): viene del secreto HOJA_ID
    hoja_id = os.environ.get("HOJA_ID", "").strip()
    if not hoja_id:
        raise RuntimeError("falta el secreto HOJA_ID en GitHub (Settings → Secrets and variables → Actions)")
    url = f"https://docs.google.com/spreadsheets/d/e/{hoja_id}/pub?gid={CONFIG['hoja_resumen_gid']}&single=true&output=csv"
    texto = requests.get(url, timeout=20).content.decode("utf-8")
    filas = list(csv.reader(io.StringIO(texto)))
    for i, fila in enumerate(filas):
        cab = [c.strip().upper() for c in fila]
        if any("TOKEN" in c for c in cab) and any("CANTIDAD" in c for c in cab):
            c_tok = next(j for j, c in enumerate(cab) if "TOKEN" in c)
            c_cant = next(j for j, c in enumerate(cab) if "CANTIDAD" in c)
            c_inv = next((j for j, c in enumerate(cab) if "INVERSI" in c), None)
            cartera = {}
            for f in filas[i + 1:]:
                tok = f[c_tok].strip().upper() if len(f) > c_tok else ""
                if tok in tokens:
                    cartera[tok] = {"cantidad": parse_num(f[c_cant]) or 0.0,
                                    "invertido": parse_num(f[c_inv]) or 0.0 if c_inv is not None else 0.0}
            return cartera
    return {}


# ---------------------------------------------------------------- estado
def cargar_estado():
    try:
        return json.loads(ESTADO_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def guardar_estado(estado):
    ESTADO_PATH.write_text(json.dumps(estado, indent=2, ensure_ascii=False), encoding="utf-8")


def lado(precio, nivel, anterior, margen):
    """'arriba' / 'abajo' con un pequeño margen para no avisar 20 veces si el precio baila en el nivel."""
    if precio > nivel * (1 + margen):
        return "arriba"
    if precio < nivel * (1 - margen):
        return "abajo"
    return anterior


# ---------------------------------------------------------------- mensajes
def din(x, dec, moneda="€"):
    return f"{fmt(x, dec)} {moneda}"


def alertas_de_nivel(tok, precio, niveles, estado, margen, moneda="€"):
    """niveles: lista de (clave, valor, descripción)."""
    msgs = []
    lados = estado.setdefault("lados", {})
    d = dec_precio(precio)
    nombre = html.escape(tok)
    for clave, nivel, desc in niveles:
        k = f"{tok}:{clave}"
        nuevo = lado(precio, nivel, lados.get(k), margen)
        previo = lados.get(k)
        if previo and nuevo and nuevo != previo:
            que = f"{desc} {din(nivel, d, moneda)}" if desc else din(nivel, d, moneda)
            if nuevo == "arriba":
                msgs.append(f"🚀 <b>{nombre}</b> ha superado {que} → ahora {din(precio, d, moneda)}")
            else:
                msgs.append(f"🔻 <b>{nombre}</b> ha bajado de {que} → ahora {din(precio, d, moneda)}")
        if nuevo:
            lados[k] = nuevo
    return msgs


def alerta_brusca(tok, cambio, estado, umbral, ahora, periodo="en 24 h"):
    if cambio is None or abs(cambio) < umbral:
        return None
    sentido = "sube" if cambio > 0 else "baja"
    previo = estado.setdefault("bruscos", {}).get(tok)
    if previo and previo["sentido"] == sentido and ahora - datetime.fromisoformat(previo["hora"]) < timedelta(hours=12):
        return None
    estado["bruscos"][tok] = {"sentido": sentido, "hora": ahora.isoformat()}
    icono = "📈" if cambio > 0 else "📉"
    return f"{icono} <b>{html.escape(tok)}</b> {sentido} un <b>{fmt(cambio, 1, True)} %</b> {periodo}"


def alertas_de_watchlist(estado, ahora):
    """Avisa si un valor de watchlist.toml se mueve más de movimiento_brusco_watchlist_pct en la sesión (una vez por hora, sin IA)."""
    umbral = CONFIG.get("movimiento_brusco_watchlist_pct", 6)
    if not umbral or ahora.minute >= 30:      # la ejecución de las :07 de cada hora; la de las :37 se salta (menos peticiones a Yahoo)
        return []
    try:
        with open(AQUI.parent / "watchlist.toml", "rb") as f:
            valores = tomllib.load(f).get("valores", [])
    except Exception as e:
        print(f"watchlist.toml no disponible: {e}")
        return []
    alertas = []
    for v in valores:
        try:
            precio, previo = precio_yahoo(v["yahoo"])
        except Exception:
            continue
        cambio = (precio / float(previo) - 1) * 100 if previo else None
        nombre = f"{v['ticker']} ({v['nombre'].split(' (')[0][:28]})"
        brusca = alerta_brusca("WL:" + nombre, cambio, estado, umbral, ahora, periodo="en la sesión")
        if brusca:
            alertas.append(brusca.replace("WL:", "👀 "))
    return alertas


# ---------------------------------------------------------------- mercados y materias primas (Yahoo Finance, sin IA)
MERCADOS_VISTOS = {}   # nombre -> (precio, cambio %, moneda) de esta ejecución, para el resumen diario


def precio_yahoo(simbolo):
    """Precio actual y cierre anterior. API no oficial de Yahoo: si falla, el mercado se salta sin afectar al resto."""
    r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{simbolo}",
                     params={"interval": "1d", "range": "5d"}, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
    r.raise_for_status()
    res = r.json()["chart"]["result"][0]
    meta = res["meta"]
    cierres = [c for c in res["indicators"]["quote"][0]["close"] if c is not None]
    # OJO: meta["chartPreviousClose"] es el cierre de hace ~5 días (antes del rango pedido), no el de ayer: se usa el penúltimo cierre diario
    previo = cierres[-2] if len(cierres) >= 2 else meta.get("chartPreviousClose")
    return float(meta["regularMarketPrice"]), previo


def alertas_de_mercados(estado, margen, ahora):
    alertas = []
    umbral_def = CONFIG.get("movimiento_brusco_mercados_pct", 4)
    for nombre, m in CONFIG.get("mercados", {}).items():
        try:
            precio, previo = precio_yahoo(m["simbolo"])
        except Exception as e:
            print(f"Mercado '{nombre}' no disponible: {e}")
            continue
        moneda = m.get("moneda", "$")
        cambio = (precio / float(previo) - 1) * 100 if previo else None
        MERCADOS_VISTOS[nombre] = (precio, cambio, moneda)
        niveles = [(f"{n:g}", float(n), "") for n in m.get("niveles", [])]
        alertas += alertas_de_nivel(nombre, precio, niveles, estado, margen, moneda)
        brusca = alerta_brusca(nombre, cambio, estado, m.get("brusco_pct", umbral_def), ahora, periodo="en la sesión")
        if brusca:
            alertas.append(brusca)
    return alertas


def resumen(precios, cambios, cartera, estado, ahora_es):
    lineas = [f"📊 <b>Resumen de tu cartera</b> · {ahora_es:%d/%m/%Y %H:%M}", ""]
    total_val = total_inv = 0.0
    for tok, p in precios.items():
        ch = cambios.get(tok)
        ch_txt = f" ({fmt(ch, 1, True)} % 24h)" if ch is not None else ""
        pos = cartera.get(tok)
        if pos and pos["cantidad"] > 0:
            valor = pos["cantidad"] * p
            pnl = valor - pos["invertido"]
            pnl_pct = pnl / pos["invertido"] * 100 if pos["invertido"] > 0 else 0.0
            medio = pos["invertido"] / pos["cantidad"]
            total_val += valor
            total_inv += pos["invertido"]
            lineas.append(f"<b>{tok}</b> {eur(p, dec_precio(p))}{ch_txt}\n"
                          f"   {eur(valor)} · {eur(pnl, sign=True)} ({fmt(pnl_pct, 1, True)} %) · medio {eur(medio, dec_precio(medio))}")
        else:
            lineas.append(f"<b>{tok}</b> {eur(p, dec_precio(p))}{ch_txt}")
    if total_val:
        pnl = total_val - total_inv
        lineas += ["", f"💼 <b>Total: {eur(total_val)}</b>",
                   f"Beneficio: {eur(pnl, sign=True)} ({fmt(pnl / total_inv * 100 if total_inv else 0, 1, True)} %)"]
        anterior = estado.get("valor_ultimo_resumen")
        if anterior:
            lineas.append(f"Desde el último resumen: {eur(total_val - anterior, sign=True)}")
        estado["valor_ultimo_resumen"] = total_val
    if MERCADOS_VISTOS:
        lineas += ["", "🌍 <b>Mercados</b>"]
        for nombre, (p, ch, moneda) in MERCADOS_VISTOS.items():
            lineas.append(f"{html.escape(nombre)} {din(p, dec_precio(p), moneda)}"
                          + (f" ({fmt(ch, 1, True)} %)" if ch is not None else ""))
    return "\n".join(lineas)


# ---------------------------------------------------------------- principal
def main():
    if not TG_TOKEN:
        sys.exit("Falta el secreto TELEGRAM_TOKEN en GitHub (Settings → Secrets and variables → Actions).")
    if not TG_CHAT:
        descubrir_chat_id()
        return

    estado = cargar_estado()
    ahora = datetime.now(timezone.utc)
    ahora_es = ahora.astimezone(MADRID)
    pares = CONFIG["kraken"]
    margen = CONFIG.get("margen_pct", 0.5) / 100

    try:
        precios = precios_actuales(pares)
    except Exception as e:
        print(f"No se pudieron leer los precios de Kraken: {e}")
        return
    cambios = {}
    for tok, p in precios.items():
        try:
            cambios[tok] = cambio_24h(pares[tok], p)
        except Exception as e:
            print(f"Cambio 24h de {tok} no disponible: {e}")
    try:
        cartera = leer_cartera(pares)
    except Exception as e:
        print(f"No se pudo leer la hoja de resumen: {e}")
        cartera = {}

    alertas = []
    for tok, p in precios.items():
        niveles = [(f"{n:g}", float(n), "") for n in CONFIG.get("niveles", {}).get(tok, [])]
        pos = cartera.get(tok)
        if CONFIG.get("avisar_precio_medio", True) and pos and pos["cantidad"] > 0 and pos["invertido"] > 0:
            niveles.append(("medio", pos["invertido"] / pos["cantidad"], "tu precio medio"))
        alertas += alertas_de_nivel(tok, p, niveles, estado, margen)
        brusca = alerta_brusca(tok, cambios.get(tok), estado, CONFIG.get("movimiento_brusco_pct", 7), ahora)
        if brusca:
            alertas.append(brusca)
    alertas += alertas_de_mercados(estado, margen, ahora)   # Brent, oro, índices... (config: [mercados.*])
    alertas += alertas_de_watchlist(estado, ahora)          # valores de watchlist.toml con un movimiento brusco

    if alertas:
        enviar("🔔 <b>Alerta de precio</b>\n\n" + "\n".join(alertas))
        print("\n".join(alertas))

    hora = CONFIG.get("resumen_diario_hora", 21)
    hoy = ahora_es.date().isoformat()
    if PRUEBA:
        enviar("✅ <b>Tu bot de alertas funciona.</b>\n\n" + resumen(precios, cambios, cartera, estado, ahora_es))
    elif hora >= 0 and ahora_es.hour >= hora and estado.get("resumen_enviado") != hoy:
        enviar(resumen(precios, cambios, cartera, estado, ahora_es))
        estado["resumen_enviado"] = hoy

    estado["ultima_ejecucion"] = ahora.isoformat()
    guardar_estado(estado)
    print(f"OK · precios: {precios} · alertas enviadas: {len(alertas)}")


if __name__ == "__main__":
    main()
