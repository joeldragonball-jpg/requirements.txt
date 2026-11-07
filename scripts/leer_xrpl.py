"""C149 · Lector del ledger XRPL (JSON-RPC público). Sin IA, sin claves, sin dependencias (solo biblioteca estándar).

Comprueba con POST JSON-RPC, en dos nodos independientes, las predicciones #19 (enmienda fixCleanup3_4_0) y #23 (escrow
mensual de Ripple del 1-nov-2026). Solo marca [P] lo que lee del ledger validado; el resto queda [VERIFICAR].
Uso:  python scripts/leer_xrpl.py [--informe]   (con --informe escribe informes/research/2026-11-07-C149-xrpl.md)
La verificación de certificados queda activa (valores por defecto de urllib)."""
import json
import sys
import tomllib
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NODOS = ["https://s1.ripple.com:51234/", "https://xrplcluster.com/"]
EPOCH = 946684800  # el XRPL cuenta segundos desde el 1-ene-2000
ENMIENDA = "fixCleanup3_4_0"
ESCROW_1NOV = datetime(2026, 11, 1, tzinfo=timezone.utc)


def rpc(nodo, metodo, params=None):
    cuerpo = json.dumps({"method": metodo, "params": [params or {}]}).encode()
    req = urllib.request.Request(nodo, data=cuerpo, headers={"Content-Type": "application/json", "User-Agent": "cartera-bot"})
    r = json.load(urllib.request.urlopen(req, timeout=30))["result"]
    if r.get("status") != "success":
        raise RuntimeError(r.get("error_message") or r.get("error") or "sin éxito")
    return r


def fecha(t):
    return datetime.fromtimestamp(t + EPOCH, timezone.utc)


def leer_nodo(nodo, cuentas):
    out = {"nodo": nodo}
    try:
        led = rpc(nodo, "ledger", {"ledger_index": "validated"})["ledger"]
        out["ledger"] = {"indice": int(led["ledger_index"]), "hash": led["ledger_hash"],
                         "cierre": fecha(int(led["close_time"])).strftime("%Y-%m-%d %H:%M:%S UTC")}
    except Exception as e:
        out["error"] = f"ledger: {e}"
        return out
    try:
        # el método devuelve un dict {hash_enmienda: {...}}; localizamos por nombre
        feats = rpc(nodo, "feature")["features"]
        f = next((v for v in feats.values() if v.get("name") == ENMIENDA), None)
        if f is None:  # algunos nodos solo la devuelven si se pide por nombre
            feats = rpc(nodo, "feature", {"feature": ENMIENDA})["features"]
            f = next((v for v in feats.values() if v.get("name") == ENMIENDA), None) or next(iter(feats.values()), None)
        if f is None:
            out["enmienda"] = {"error": "no aparece en el método feature"}
        else:
            e = {"enabled": f.get("enabled"), "vetoed": f.get("vetoed"), "supported": f.get("supported"),
                 "count": f.get("count"), "threshold": f.get("threshold"), "validations": f.get("validations")}
            if "majority" in f:
                e["majority"] = fecha(int(f["majority"])).strftime("%Y-%m-%d %H:%M:%S UTC")
            out["enmienda"] = e
    except Exception as ex:
        out["enmienda"] = {"error": str(ex)}
    try:
        t_ref = (ESCROW_1NOV.timestamp()) - EPOCH
        total = 0.0
        por_mes = defaultdict(float)
        vencidos_1nov = 0.0
        n = 0
        for c in cuentas:
            marcador = None
            while True:
                p = {"account": c["direccion"], "type": "escrow", "limit": 400, "ledger_index": led["ledger_index"]}
                if marcador:
                    p["marker"] = marcador
                r = rpc(nodo, "account_objects", p)
                for o in r.get("account_objects", []):
                    a = o.get("Amount")
                    if o.get("LedgerEntryType") != "Escrow" or not a or isinstance(a, dict):
                        continue
                    xrp = int(a) / 1e6
                    n += 1
                    total += xrp
                    fa = o.get("FinishAfter")
                    if fa:
                        por_mes[fecha(fa).strftime("%Y-%m")] += xrp
                        if fa <= t_ref:
                            vencidos_1nov += xrp
                marcador = r.get("marker")
                if not marcador:
                    break
        out["escrow"] = {"n_cuentas": len(cuentas), "n_escrows": n, "total_M": round(total / 1e6, 1),
                         "con_FinishAfter_hasta_1nov_aun_en_ledger_M": round(vencidos_1nov / 1e6, 1),
                         "por_mes_M": {k: round(v / 1e6, 1) for k, v in sorted(por_mes.items())}}
    except Exception as ex:
        out["escrow"] = {"error": str(ex)}
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    with open(RAIZ / "eventos" / "escrow_cuentas.toml", "rb") as f:
        cuentas = tomllib.load(f)["cuentas"]
    res = [leer_nodo(n, cuentas) for n in NODOS]
    print(json.dumps(res, ensure_ascii=False, indent=1))
    if "--informe" in sys.argv:
        escribir_informe(res)
    return res


def escribir_informe(res):
    ok = [r for r in res if "ledger" in r]
    L = ["# C149 · Lector del ledger XRPL (7-nov-2026)", "",
         "Script: `scripts/leer_xrpl.py` (POST JSON-RPC, sin IA ni claves). Etiqueta [P] = leído del ledger validado.", ""]
    for r in res:
        if "ledger" not in r:
            L.append(f"- Nodo `{r['nodo']}`: **sin respuesta** ({r.get('error')}).")
            continue
        g = r["ledger"]
        L.append(f"- Nodo `{r['nodo']}`: ledger **{g['indice']}**, cierre {g['cierre']}, hash `{g['hash']}`.")
    L += ["", "## #19 · fixCleanup3_4_0 (previsto: activación desde el 23-oct; el 28-oct se recalculó a ~4-nov 14:46 UTC)"]
    for r in ok:
        e = r.get("enmienda", {})
        if "error" in e:
            L.append(f"- {r['nodo']}: no comprobable ({e['error']}).")
        else:
            L.append(f"- {r['nodo']}: enabled={e['enabled']}, majority={e.get('majority', 'sin campo')}, "
                     f"votos {e.get('count')}/{e.get('validations')} (umbral {e.get('threshold')}) [P]")
    L += ["", "## #23 · Escrow de Ripple del 1-nov-2026 00:00 UTC (hasta 1.000 M XRP)"]
    for r in ok:
        s = r.get("escrow", {})
        if "error" in s:
            L.append(f"- {r['nodo']}: no comprobable ({s['error']}).")
        else:
            L.append(f"- {r['nodo']}: {s['total_M']} M XRP en {s['n_escrows']} escrows ({s['n_cuentas']} cuentas vigiladas); "
                     f"con FinishAfter ≤ 1-nov aún sin ejecutar: {s['con_FinishAfter_hasta_1nov_aun_en_ledger_M']} M; "
                     f"por mes de vencimiento (M): {s['por_mes_M']} [P]")
    L += ["", "## Qué falta",
          "- Fecha exacta de activación de fixCleanup3_4_0: el método `feature` solo dice enabled=true; la fecha está en la "
          "transacción pseudo-EnableAmendment (no se localizó con account_tx) [VERIFICAR]. Un nodo que responda "
          "«Feature unknown» (p. ej. s1 si va con versión anterior) no puede confirmar la enmienda.",
          "- Del ledger actual solo se ve el estado, no la historia: que el escrow del 1-nov se ejecutó y cuánto se volvió a bloquear "
          "exige comparar con la lectura previa (`eventos/estado-escrow.json`) o `account_tx` de las cuentas. Hasta entonces, "
          "esa parte de #23 es [VERIFICAR].",
          "- Cuánto líquido salió a exchanges no está en el ledger de escrows: necesita seguir las cuentas de destino [VERIFICAR].",
          "- Solo se vigilan las cuentas etiquetadas de `escrow_cuentas.toml`; ambos nodos son de lectura pública (s1 es de Ripple: "
          "conflicto de interés leve, de ahí el segundo nodo)."]
    ruta = RAIZ / "informes" / "research" / "2026-11-07-C149-xrpl.md"
    ruta.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Informe: {ruta}")


if __name__ == "__main__":
    main()
