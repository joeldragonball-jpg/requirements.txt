"""Vigilancia on-chain sin IA y sin dependencias (nodos públicos):
  A) Estado de las redes XRP Ledger y Stellar: avisa cuando empieza un problema (red parada o atascada) y cuando se recupera.
  C) Movimientos grandes de las cuentas de Ripple de eventos/ripple_cuentas.toml: avisa si el saldo de alguna cambia más que
     el umbral entre dos comprobaciones (XRP que sale o entra; no implica venta).
Memoria entre ejecuciones: eventos/estado-onchain.json. Información pública del ledger, no una recomendación."""
import json
import os
import sys
import tomllib
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).parent
ESTADO = AQUI / "estado-onchain.json"
NODOS_XRPL = ["https://xrplcluster.com/", "https://s1.ripple.com:51234/", "https://s2.ripple.com:51234/"]
HORIZON = "https://horizon.stellar.org"
# Umbrales de problema
XRPL_EDAD_MAX_S = 60                 # el último ledger validado no debería tener más de 1 minuto
XRPL_CARGA_MAX = 50                  # load_factor: 1 es normal; muy alto = tarifas disparadas
STELLAR_EDAD_MAX_S = 120             # Stellar cierra un ledger cada ~5 s
STELLAR_USO_MAX = 0.95               # uso de capacidad del ledger
STELLAR_TARIFA_P90_MAX = 1_000_000   # stroops (0,1 XLM): tarifa muy por encima de lo normal


def http_json(url, datos=None, timeout=25):
    req = urllib.request.Request(url, data=json.dumps(datos).encode() if datos else None,
                                 headers={"Content-Type": "application/json", "User-Agent": "cartera-bot"})
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def rpc(metodo, params):
    ultimo = None
    for nodo in NODOS_XRPL:
        try:
            r = http_json(nodo, {"method": metodo, "params": [params]})["result"]
            if r.get("status") == "success":
                return r
            ultimo = r.get("error_message") or r.get("error")
        except Exception as e:
            ultimo = str(e)
    raise RuntimeError(f"XRPL sin respuesta: {ultimo}")


def problema_xrpl(info):
    """info = server_info['info']. Devuelve el texto del problema o None."""
    if info.get("server_state") not in ("full", "proposing", "validating"):
        return f"el nodo consultado está en estado «{info.get('server_state')}»"
    edad = (info.get("validated_ledger") or {}).get("age")
    if edad is not None and edad > XRPL_EDAD_MAX_S:
        return f"el último ledger validado tiene {edad} s de antigüedad (lo normal son 3-5 s)"
    carga = info.get("load_factor") or 1
    if carga >= XRPL_CARGA_MAX:
        return f"las tarifas están disparadas (factor de carga {carga:g}, lo normal es 1)"
    return None


def problema_stellar(ledger, fees, ahora):
    cerrado = datetime.fromisoformat(ledger["closed_at"].replace("Z", "+00:00"))
    edad = (ahora - cerrado).total_seconds()
    if edad > STELLAR_EDAD_MAX_S:
        return f"el último ledger se cerró hace {edad:.0f} s (lo normal son ~5 s)"
    uso = float(fees.get("ledger_capacity_usage", 0))
    p90 = int(fees.get("fee_charged", {}).get("p90", 0))
    if uso >= STELLAR_USO_MAX and p90 >= STELLAR_TARIFA_P90_MAX:
        return f"red saturada (uso {uso:.0%}) y tarifas muy altas ({p90 / 1e7:.4f} XLM)"
    return None


def cambios_saldo(actuales, previos, umbral_m):
    """actuales/previos: {etiqueta: saldo en millones de XRP}. Devuelve las líneas de aviso."""
    out = []
    for et, s in actuales.items():
        p = previos.get(et)
        if p is not None and abs(s - p) >= umbral_m:
            d = s - p
            out.append(f"{'⬆️ entran' if d > 0 else '⬇️ salen'} <b>{abs(d):,.0f} M XRP</b> en {et} "
                       f"({p:,.0f} → {s:,.0f} M)".replace(",", "."))
    return out


def telegram(texto):
    token, chat = os.environ.get("TELEGRAM_TOKEN", "").strip(), os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print(texto)
        return
    datos = urllib.parse.urlencode({"chat_id": chat, "text": texto, "parse_mode": "HTML",
                                    "disable_web_page_preview": "true"}).encode()
    urllib.request.urlopen(urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=datos), timeout=20)


def main():
    ahora = datetime.now(timezone.utc)
    estado = json.loads(ESTADO.read_text(encoding="utf-8")) if ESTADO.exists() else {}
    inc = estado.get("incidentes", {})
    avisos = []

    # A) estado de las redes
    comprobaciones = {}
    try:
        comprobaciones["XRP Ledger"] = problema_xrpl(rpc("server_info", {})["info"])
    except Exception as e:
        comprobaciones["XRP Ledger"] = f"no responde ningún nodo público ({str(e)[:80]})"
    try:
        ledger = http_json(f"{HORIZON}/ledgers?order=desc&limit=1")["_embedded"]["records"][0]
        comprobaciones["Stellar"] = problema_stellar(ledger, http_json(f"{HORIZON}/fee_stats"), ahora)
    except Exception as e:
        comprobaciones["Stellar"] = f"Horizon no responde ({str(e)[:80]})"
    for red, prob in comprobaciones.items():
        if prob and red not in inc:
            avisos.append(f"⚠️ <b>{red}</b>: {prob}.")
            inc[red] = ahora.isoformat()
        elif not prob and red in inc:
            avisos.append(f"✅ <b>{red}</b> se ha recuperado.")
            inc.pop(red)

    # C) movimientos grandes de cuentas de Ripple
    with open(AQUI / "ripple_cuentas.toml", "rb") as f:
        cfg = tomllib.load(f)
    saldos = {}
    for c in cfg["cuentas"]:
        try:
            r = rpc("account_info", {"account": c["direccion"], "ledger_index": "validated"})
            saldos[c["etiqueta"]] = int(r["account_data"]["Balance"]) / 1e12   # gotas -> millones de XRP
        except Exception:
            pass   # si falla una cuenta, se conserva su saldo anterior y no se avisa
    previos = estado.get("saldos", {})
    mov = cambios_saldo(saldos, previos, float(cfg.get("umbral_m", 25)))
    if mov:
        avisos.append("🐋 Movimientos de cuentas de Ripple:\n" + "\n".join(mov) +
                      "\n<i>Que salga XRP de una cuenta no implica que se venda: puede ser un traspaso interno.</i>")
    previos.update(saldos)

    ESTADO.write_text(json.dumps({"incidentes": inc, "saldos": previos, "fecha": ahora.isoformat()},
                                 ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"problemas": comprobaciones, "cuentas": len(saldos), "avisos": len(avisos)}, ensure_ascii=False))
    if avisos:
        telegram("\n\n".join(avisos) + "\n\n<i>Datos públicos de los ledgers. Información, no una recomendación.</i>")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
