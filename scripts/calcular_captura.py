"""C329 · «Captura del token» con regla explícita y reproducible (sin IA).
Lee explorador/cadenas.json (capas[].token por red) y explorador/cadenas-token.json (scripts/leer_liquidez_tokens.py).
Dos ejes, y el nivel sale de combinarlos:
  NECESIDAD (¿el diseño de la red obliga a usar el token?), por las 5 capas:
    sin_dato     = 3 o más capas «sin dato»
    obligatorio  = token «sí» en 2 o más capas y una es liquidación o emisión
    parcial      = token «sí» en 1 capa, o «parcial» en 2 o más
    sustituible  = el resto (solo comisiones mínimas o «parcial» en 1 capa)
  CONSUMO (¿se nota en el mercado?): comisiones anualizadas pagadas por los usuarios ÷ capitalización del token
    alto ≥ 1 %, medio 0,2–1 %, bajo < 0,2 %, sin_dato si la red no es una cadena con dato de comisiones.
  NIVEL (alta/media/baja/incierta, mismos colores que antes):
    necesidad sin_dato -> incierta;  necesidad sustituible -> baja;  consumo bajo -> baja
    obligatorio + consumo medio/alto -> alta;  parcial + consumo medio/alto -> media
    obligatorio o parcial SIN dato de consumo -> incierta (no se sube sin evidencia de consumo)
Aparte se informa la LIQUIDEZ del token (rotación = volumen 24 h ÷ capitalización) y el peso (valor tokenizado ÷ capitalización).
Compara con el juicio manual (captura.nivel) y marca «discrepa» para revisión humana.
Uso: python scripts/calcular_captura.py [--escribir]   (sin --escribir solo muestra la tabla)"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RC = RAIZ / "explorador" / "cadenas.json"
RT = RAIZ / "explorador" / "cadenas-token.json"
CAPAS = ("liquidacion", "emision", "seguridad", "mensajeria", "custodia")


def nivel_regla(capas):
    cuenta = {k: sum(1 for c in CAPAS if (capas.get(c) or {}).get("token") == k) for k in ("sí", "parcial", "mínimo", "no", "sin dato")}
    si, pa, sd = cuenta["sí"], cuenta["parcial"], cuenta["sin dato"]
    if sd >= 3:
        n = "sin_dato"
    elif si >= 2 and any((capas.get(c) or {}).get("token") == "sí" for c in ("liquidacion", "emision")):
        n = "obligatorio"
    elif si >= 1 or pa >= 2:
        n = "parcial"
    else:
        n = "sustituible"
    return n, cuenta


def consumo(t):
    if not t or t.get("fees_anual_pct_cap") is None:
        return "sin_dato"
    p = t["fees_anual_pct_cap"]
    return "alto" if p >= 1 else "medio" if p >= 0.2 else "bajo"


def nivel_final(nec, cons):
    if nec == "sin_dato":
        return "incierta"
    if nec == "sustituible" or cons == "bajo":
        return "baja"
    if cons == "sin_dato":
        return "incierta"
    return "alta" if nec == "obligatorio" else "media"


def peso(valor_musd, cap_musd):
    if not valor_musd or not cap_musd:
        return "sin_dato", None
    p = valor_musd / cap_musd * 100
    return ("alto" if p >= 25 else "medio" if p >= 5 else "bajo"), round(p, 1)


def calcular():
    cad = json.loads(RC.read_text(encoding="utf-8"))
    tok = json.loads(RT.read_text(encoding="utf-8")) if RT.exists() else {"redes": {}}
    res = {}
    for c in cad["cadenas"]:
        n, cuenta = nivel_regla(c.get("capas") or {})
        tipos = ((c.get("tipos_activo") or {}).get("tipos")) or {}
        valor = sum(x.get("v", 0) for x in tipos.values()) or None
        t = (tok.get("redes") or {}).get(c["id"])
        pw, pct = peso(valor, t and t.get("cap_musd"))
        manual = (c.get("captura") or {}).get("nivel")
        cons = consumo(t)
        fin = nivel_final(n, cons)
        res[c["id"]] = {"nivel": fin, "necesidad": n, "consumo": cons, "fees_pct": t and t.get("fees_anual_pct_cap"), "rotacion_pct": t and t.get("rotacion_pct"), "capas": cuenta, "peso": pw, "peso_pct": pct, "valor_tokenizado_musd": round(valor, 1) if valor else None,
                        "discrepa": bool(manual and fin != manual), "atipico": bool(t and (t.get("fees_anual_pct_cap") or 0) > 20), "manual": manual}
    return cad, res


def main():
    cad, res = calcular()
    tok = json.loads(RT.read_text(encoding="utf-8")) if RT.exists() else {"redes": {}}
    print(f"{'red':10} {'nivel':8} {'manual':8} {'necesidad':12} {'consumo':8} {'fees%':>6} {'peso':8}  capas(si/parc/min/no/sd)")
    for k, r in res.items():
        cu = r["capas"]
        print(f"{k:10} {r['nivel']:8} {str(r['manual']):8} {r['necesidad']:12} {r['consumo']:8} {str(r['fees_pct']):>6} {r['peso']:8}  {cu['sí']}/{cu['parcial']}/{cu['mínimo']}/{cu['no']}/{cu['sin dato']}{'  <- discrepa' if r['discrepa'] else ''}")
    if "--escribir" in sys.argv:
        raw = RC.read_text(encoding="utf-8")
        nl = "\r\n" if "\r\n" in raw else "\n"
        for c in cad["cadenas"]:
            r = res[c["id"]]
            t = (tok.get("redes") or {}).get(c["id"])
            c.setdefault("captura", {})["liquidez"] = ({k: t.get(k) for k in ("cap_musd", "vol24_musd", "rotacion_pct", "fees30_musd", "fees_anual_pct_cap", "circulante", "total", "d", "n")} if t else None)
            c["captura"]["regla"] = {k: r[k] for k in ("nivel", "necesidad", "consumo", "fees_pct", "rotacion_pct", "peso", "peso_pct", "valor_tokenizado_musd", "discrepa", "atipico")}
        s = json.dumps(cad, ensure_ascii=False, indent=1)
        RC.write_text(s.replace("\n", nl) + (nl if raw.endswith("\n") else ""), encoding="utf-8", newline="")
        print("escrito en cadenas.json (captura.regla)")


if __name__ == "__main__":
    main()
