"""Alertas por umbral y por evento de los DATOS del tablero (C206), por Telegram. Sin IA, sin APIs de pago, sin claves en el repo.

Lee archivos que ya están en el repo (los actualizan otros bots) y avisa solo de lo NUEVO desde la última ejecución:
  1. Datos en rojo: elementos de «frescura» que pasan a «alerta» (docs/movil/seguimiento.json).
  2. Tipos oficiales: decisión nueva de un banco central (cambia «ultimo_cambio») o cruce de un umbral tuyo
     (explorador/paneles.json → tipos_vivos, y explorador/tipos-manual.json).
  3. Noticias de nivel P: movimientos nuevos con fuente primaria [P] en explorador/datos.json.
Configuración: sección [datos] de alertas/config.toml. Memoria: alertas/estado-datos.json (caché de GitHub, no se sube).
La primera ejecución solo memoriza lo que hay y no envía nada (para no inundar el chat).
Lo lanza .github/workflows/eventos.yml una vez al día. Sin TELEGRAM_TOKEN imprime el mensaje (modo prueba).
Uso local: python alertas/datos.py"""
import hashlib
import html
import json
import os
import sys
import tomllib
from datetime import date, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
ESTADO_PATH = AQUI / "estado-datos.json"
# Mismo config.toml y mismos secrets (TELEGRAM_TOKEN / TELEGRAM_CHAT_ID) que alertas.py y eventos/avisos.py
CFG = tomllib.loads((AQUI / "config.toml").read_text(encoding="utf-8")).get("datos", {})
MAX_LINEAS = int(CFG.get("max_lineas", 8))
REPO_URL = (f"{os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/{os.environ['GITHUB_REPOSITORY']}/blob/main/"
            if os.environ.get("GITHUB_REPOSITORY") else "")


def leer(rel):
    try:
        return json.loads((RAIZ / rel).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"No se pudo leer {rel}: {type(e).__name__}", file=sys.stderr)
        return {}


def e(t):
    return html.escape(str(t if t is not None else ""))


def enlace(url, texto):
    url = str(url or "")
    if url.startswith(("https://", "http://")):
        return f'<a href="{e(url)}">{e(texto)}</a>'
    if REPO_URL and url.startswith(("informes/", "research/", "cerebro/")) and ".." not in url:
        return f'<a href="{e(REPO_URL + url)}">{e(texto)}</a>'
    return e(texto)


# ------------------------------------------------------------------ 1. datos en rojo
def rojos(estado):
    items = (leer("docs/movil/seguimiento.json").get("frescura") or {}).get("items", [])
    ahora = {f"{x['area']}|{x['titulo']}": x for x in items if x.get("nivel") == "alerta"}
    antes = set(estado.get("rojos", []))
    estado["rojos"] = sorted(ahora)
    return [f"🔴 <b>{e(x['area'])}</b>: {e(x['titulo'])} ({e(x.get('n'))})" + (f" · {e(str(x.get('detalle'))[:90])}" if x.get("detalle") else "")
            + f" → {e(x.get('rutina'))}" for k, x in ahora.items() if k not in antes]


# ------------------------------------------------------------------ 2. tipos oficiales
def tipos(estado):
    filas = {x["jur"]: x for x in leer("explorador/tipos-manual.json").get("tipos", []) if x.get("jur")}
    vivos = leer("explorador/paneles.json").get("tipos_vivos") or {}
    filas.update({x["jur"]: {"nivel": vivos.get("nivel"), **x} for x in vivos.get("paises", []) if x.get("jur")})
    umbrales = CFG.get("umbrales_tipos", {})
    margen = float(CFG.get("margen_tipos_pb", 0)) / 100          # en puntos porcentuales
    prev = estado.get("tipos", {})
    nuevo, out = {}, []
    for jur, x in filas.items():
        num, ult = x.get("num"), x.get("ultimo_cambio")
        p = prev.get(jur, {})
        lados = dict(p.get("lados", {}))
        nombre = f"{x.get('pais', jur.upper())} · {x.get('banco', '')}"
        fuente = enlace(x.get("url"), "fuente") + (f" [{e(x['nivel'])}]" if x.get("nivel") else "")
        if p and ult and p.get("ultimo_cambio") and ult != p.get("ultimo_cambio"):
            pb = x.get("cambio_pb")
            out.append(f"🏦 <b>{e(nombre)}</b>: decisión del {e(ult)} → {e(x.get('valor'))}"
                       + (f" ({'+' if pb and pb > 0 else ''}{e(pb)} pb)" if pb is not None else "") + f" · {fuente}")
        if isinstance(num, (int, float)):
            for nivel in umbrales.get(jur, []):
                clave = str(nivel)
                if num > nivel + margen:
                    lado = "arriba"
                elif num < nivel - margen:
                    lado = "abajo"
                else:
                    lado = lados.get(clave)
                if p and lado and lados.get(clave) and lado != lados[clave]:
                    out.append(f"📏 <b>{e(nombre)}</b>: el tipo ({e(x.get('valor'))}) pasa {'por encima' if lado == 'arriba' else 'por debajo'} "
                               f"de tu umbral del {str(nivel).replace('.', ',')} % · {fuente}")
                if lado:
                    lados[clave] = lado
        nuevo[jur] = {"ultimo_cambio": ult or p.get("ultimo_cambio"), "lados": lados}
    estado["tipos"] = nuevo
    return out


# ------------------------------------------------------------------ 3. noticias de nivel P
def firma(m):
    return hashlib.sha1(f"{m.get('fecha')}|{m.get('capa')}|{m.get('actor')}|{str(m.get('texto'))[:120]}".encode("utf-8")).hexdigest()[:16]


def noticias_p(estado, hoy):
    dias = int(CFG.get("noticias_dias", 7))
    desde = (hoy - timedelta(days=dias)).isoformat()
    movs = [m for m in leer("explorador/datos.json").get("movimientos", [])
            if m.get("nivel") == "P" and desde <= str(m.get("fecha", "")) <= hoy.isoformat()]
    vistos = set(estado.get("noticias", []))
    nuevas = [m for m in movs if firma(m) not in vistos]
    estado["noticias"] = sorted(vistos | {firma(m) for m in movs})[-2000:]   # memoria acotada
    nuevas.sort(key=lambda m: m.get("fecha", ""), reverse=True)
    return [f"📰 <b>{e(m.get('actor'))}</b> ({e(m.get('fecha'))}): {e(str(m.get('texto'))[:220])} · "
            + enlace(m.get("informe"), (m.get("fuente") or "fuente")[:60]) for m in nuevas]


# ------------------------------------------------------------------ mensaje
def mensaje(bloques):
    lineas, partes = 0, []
    for titulo, filas in bloques:
        if not filas:
            continue
        cabe = max(0, MAX_LINEAS - lineas)
        if cabe == 0:
            partes.append(f"<i>… y {len(filas)} aviso(s) más de {e(titulo.lower())}.</i>")
            continue
        txt = f"<b>{titulo}</b>\n" + "\n".join(filas[:cabe])
        if len(filas) > cabe:
            txt += f"\n<i>… y {len(filas) - cabe} más (ver el Explorador).</i>"
        partes.append(txt)
        lineas += min(cabe, len(filas))
    if not partes:
        return ""
    return "\n\n".join(partes) + "\n\n<i>Datos del tablero, no una recomendación de compra o venta.</i>"


def enviar(texto):
    """Igual que eventos/avisos.py: sin token o sin chat solo imprime (modo prueba)."""
    token = os.environ.get("TELEGRAM_TOKEN", "").strip()
    chat = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print(texto)
        return
    import requests
    r = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", timeout=20,
                      data={"chat_id": chat, "text": texto, "parse_mode": "HTML", "disable_web_page_preview": "true"})
    if not r.ok:                          # sin imprimir la URL (lleva el token)
        sys.exit(f"Telegram respondió {r.status_code}.")
    print("Enviado a Telegram.")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if CFG.get("activo", True) is False:
        print("Alertas de datos desactivadas en config.toml ([datos] activo = false).")
        return
    try:
        estado = json.loads(ESTADO_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        estado = {}
    primera = not estado
    hoy = date.today()
    bloques = []
    if CFG.get("rojos", True):
        bloques.append(("Datos en rojo", rojos(estado)))
    if CFG.get("tipos", True):
        bloques.append(("Tipos oficiales", tipos(estado)))
    if CFG.get("noticias_p", True):
        bloques.append(("Noticias con fuente primaria [P]", noticias_p(estado, hoy)))
    estado["ultima"] = hoy.isoformat()
    texto = "" if primera else mensaje(bloques)
    if primera:
        print("Primera ejecución: memorizo el estado actual y no envío nada.")
    elif not texto:
        print(f"{hoy}: nada nuevo que avisar.")
    else:
        enviar(texto)
    ESTADO_PATH.write_text(json.dumps(estado, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
