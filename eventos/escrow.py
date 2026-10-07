"""Vigilancia del escrow de Ripple en el XRP Ledger. Sin IA y sin dependencias: solo consulta nodos públicos del XRPL.
Qué mide: cuánto XRP hay bloqueado en escrow en las cuentas de eventos/escrow_cuentas.toml, cuándo es el próximo desbloqueo
programado y cuánto XRP ya es desbloqueable. Avisa por Telegram cuando el total cambia (se ha ejecutado un desbloqueo o Ripple
ha vuelto a bloquear XRP) y el día 1 de cada mes (estado). La memoria entre ejecuciones es eventos/estado-escrow.json.
Es información pública del ledger, no una recomendación."""
import json
import os
import sys
import tomllib
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).parent
ESTADO = AQUI / "estado-escrow.json"
NODOS = ["https://xrplcluster.com/", "https://s1.ripple.com:51234/", "https://s2.ripple.com:51234/"]
EPOCH_RIPPLE = 946684800          # los tiempos del XRPL cuentan segundos desde el 1-ene-2000
UMBRAL_M = 1.0                    # cambios menores de 1 millón de XRP se consideran ruido


def rpc(metodo, params):
    ultimo = None
    for nodo in NODOS:
        try:
            req = urllib.request.Request(nodo, data=json.dumps({"method": metodo, "params": [params]}).encode(),
                                         headers={"Content-Type": "application/json", "User-Agent": "cartera-bot"})
            r = json.load(urllib.request.urlopen(req, timeout=25))["result"]
            if r.get("status") == "success":
                return r
            ultimo = r.get("error_message") or r.get("error")
        except Exception as e:
            ultimo = str(e)
    raise RuntimeError(f"XRPL sin respuesta: {ultimo}")


def consultar(cuentas, ahora=None):
    """Devuelve {total, desbloqueable, proximo_fecha, proximo_cantidad, cuentas, escrows} en millones de XRP."""
    ahora = ahora or datetime.now(timezone.utc)
    t_ahora = int(ahora.timestamp()) - EPOCH_RIPPLE
    esc = []
    for c in cuentas:
        marcador = None
        while True:
            p = {"account": c["direccion"], "type": "escrow", "limit": 400, "ledger_index": "validated"}
            if marcador:
                p["marker"] = marcador
            r = rpc("account_objects", p)
            for o in r.get("account_objects", []):
                if o.get("LedgerEntryType") == "Escrow" and o.get("Amount") and not isinstance(o["Amount"], dict):
                    esc.append((int(o["Amount"]) / 1e6, o.get("FinishAfter")))
            marcador = r.get("marker")
            if not marcador:
                break
    total = sum(a for a, _ in esc)
    vencidos = sum(a for a, f in esc if f and f <= t_ahora)
    futuros = sorted((f, a) for a, f in esc if f and f > t_ahora)
    prox_f = futuros[0][0] if futuros else None
    prox_a = sum(a for f, a in futuros if f == prox_f) if prox_f else 0.0
    return {"total": total / 1e6, "desbloqueable": vencidos / 1e6, "n_escrows": len(esc), "n_cuentas": len(cuentas),
            "proximo_fecha": datetime.fromtimestamp(prox_f + EPOCH_RIPPLE, timezone.utc).strftime("%Y-%m-%d") if prox_f else None,
            "proximo_cantidad": prox_a / 1e6}


def m(x):
    return f"{x:,.0f}".replace(",", ".") if abs(x) >= 100 else f"{x:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")


def mensaje(act, prev, dia1):
    lineas = []
    if prev is not None and abs(act["total"] - prev["total"]) >= UMBRAL_M:
        d = act["total"] - prev["total"]
        if d < 0:
            lineas.append(f"🔓 El escrow de Ripple <b>bajó {m(-d)} M XRP</b>: se ejecutó un desbloqueo y ese XRP ya no está bloqueado "
                          "(Ripple suele volver a bloquear una parte unas semanas después).")
        else:
            lineas.append(f"🔒 El escrow de Ripple <b>subió {m(d)} M XRP</b>: Ripple ha vuelto a bloquear XRP.")
    if prev is None or lineas or dia1:
        estado = (f"{m(act['total'])} M XRP bloqueados en {act['n_escrows']} escrows ({act['n_cuentas']} cuentas)."
                  + (f" Antes: {m(prev['total'])} M." if prev else ""))
        prox = (f"Próximo desbloqueo programado: <b>{act['proximo_fecha']}</b> ({m(act['proximo_cantidad'])} M XRP)."
                if act["proximo_fecha"] else "Sin desbloqueos futuros programados.")
        pend = f"Ya desbloqueable y sin ejecutar: {m(act['desbloqueable'])} M XRP." if act["desbloqueable"] >= UMBRAL_M else ""
        lineas += [estado, prox] + ([pend] if pend else [])
        lineas.append("<i>Datos del XRP Ledger de las cuentas de Ripple etiquetadas en XRPScan. Información, no una recomendación.</i>")
    return "\n".join(lineas) if lineas else ""


def telegram(texto):
    token, chat = os.environ.get("TELEGRAM_TOKEN", "").strip(), os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print(texto)
        return
    datos = urllib.parse.urlencode({"chat_id": chat, "text": texto, "parse_mode": "HTML", "disable_web_page_preview": "true"}).encode()
    urllib.request.urlopen(urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=datos), timeout=20)


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    with open(AQUI / "escrow_cuentas.toml", "rb") as f:
        cuentas = tomllib.load(f)["cuentas"]
    act = consultar(cuentas)
    prev = json.loads(ESTADO.read_text(encoding="utf-8")) if ESTADO.exists() else None
    ahora = datetime.now(timezone.utc)
    forzar = os.environ.get("PRUEBA") == "true"
    texto = mensaje(act, prev, dia1=(ahora.day == 1) or forzar)
    print(json.dumps(act, ensure_ascii=False))
    if texto:
        telegram(texto)
    ESTADO.write_text(json.dumps({**act, "fecha": ahora.isoformat()}, ensure_ascii=False, indent=1), encoding="utf-8")
