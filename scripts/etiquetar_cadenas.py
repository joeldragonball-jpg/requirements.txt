"""Cadenas ↔ noticias (C266). Python normal: NO usa IA, ni la API de Anthropic, ni la red.

Uso:  python scripts/etiquetar_cadenas.py [--simular]
Pone en cada movimiento de explorador/datos.json dos campos opcionales, calculados solo por reglas:

  «cadenas»: ids de explorador/cadenas.json cuyas palabras («busca») aparecen como palabra entera, respetando
             mayúsculas, en el actor, las entidades («ent») o los activos («act»). En las noticias del bot
             (origen «noticia»), cuyo actor y entidad son el nombre del medio, se mira además el titular y el tema.
             Si ninguna coincide, el campo no se escribe.
  «umbral»:  true en las noticias cuyo titular dice que algo «supera», «cae por debajo de», «toca», «sube a» o
             «alcanza» una cifra. Regla W05 (research/prompts/W05-verificacion.md): puede ser un movimiento
             intradía y no un cierre, así que antes de darlo por cierto o por desmentido hay que comparar el
             mismo día, mirar máximo y mínimo y distinguir el instrumento. Es un aviso de lectura, no un veredicto.

Lo importan scripts/noticias_a_orbita.py (para las noticias nuevas) y scripts/revisar_explorador.py (que avisa
si lo escrito no coincide con las reglas).
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "explorador" / "datos.json"
CADENAS = RAIZ / "explorador" / "cadenas.json"

# Palabras de «busca» que NO etiquetan, porque nombran a un tercero y no a la red:
# una noticia de Swift no es de Chainlink, y una de la bolsa Binance no es de BNB Chain.
NO_ETIQUETA = {"chainlink": {"Swift"}, "bnb": {"Binance"}}
# Palabras que sí etiquetan aunque no estén en «busca» (nombres de la red o de su mejora).
EXTRA = {
    "bnb": ["BNB Chain", "BSC"],
    "ethereum": ["Glamsterdam", "Ether"],
    "solana": ["Alpenglow"],
    "chainlink": ["CCIP", "LINK"],
    "canton": ["Canton Coin", "Digital Asset"],
    "stellar": ["Stellar Development Foundation", "SDF"],
    "xrpl": ["XRP Ledger"],
    "polygon": ["POL"],
    "avalanche": ["Ava Labs"],
    "hedera": ["Hashgraph"],
}

_VERBO = (r"supera(?:n|ba|r|ron)?|super[óo]|rebasa(?:n)?|rebas[óo]|cae(?:n)? (?:por )?(?:debajo|bajo) de|cay[óo] (?:por )?debajo de|"
          r"baja(?:n)? de|pierde(?:n)? los|toca(?:n)?|toc[óo]|alcanza(?:n)?|alcanz[óo]|sube(?:n)? (?:a|hasta)|subi[óo] (?:a|hasta)|"
          r"rompe(?:n)?|cruza(?:n)?|roza(?:n)?|por encima de|por debajo de|(?:máximo|mínimo)s? de")
_CIFRA = (r"(?:[$€]\s?\d[\d.,]*|\d[\d.,]*\s?(?:%|\$|€|k\b|dólares|euros|puntos|pb\b|"
          r"(?:mil(?:es)? de )?(?:millones|billones)|mil\b|M\$|M€))")
UMBRAL = re.compile(r"(?:^|\W)(?:" + _VERBO + r")\b[^.;:]{0,40}?" + _CIFRA, re.I)


def reglas(cad):
    """[(id, [regex…])] a partir de cadenas.json (campo «busca») más EXTRA y menos NO_ETIQUETA."""
    salida = []
    for c in cad.get("cadenas", []):
        cid = c.get("id")
        palabras = [b for b in (c.get("busca") or []) if b not in NO_ETIQUETA.get(cid, ())] + EXTRA.get(cid, [])
        salida.append((cid, [re.compile(r"(?<!\w)" + re.escape(p) + r"(?!\w)") for p in palabras]))
    return salida


def cadenas_de(mov, regs):
    """Ids de las redes que nombra un movimiento, en el orden de cadenas.json."""
    partes = [mov.get("actor") or ""] + list(mov.get("ent") or []) + list(mov.get("act") or [])
    if mov.get("origen") == "noticia":
        partes += [mov.get("texto") or "", mov.get("tema") or ""]
    texto = " · ".join(str(p) for p in partes)
    return [cid for cid, rx in regs if any(r.search(texto) for r in rx)]


def es_umbral(mov):
    return mov.get("origen") == "noticia" and bool(UMBRAL.search(mov.get("texto") or ""))


def etiquetar(mov, regs):
    """Escribe o quita «cadenas» y «umbral» en el movimiento. Devuelve True si cambió algo."""
    antes = (mov.get("cadenas"), mov.get("umbral"))
    ids = cadenas_de(mov, regs)
    if ids:
        mov["cadenas"] = ids
    else:
        mov.pop("cadenas", None)
    if es_umbral(mov):
        mov["umbral"] = True
    else:
        mov.pop("umbral", None)
    return antes != (mov.get("cadenas"), mov.get("umbral"))


def cargar_reglas():
    return reglas(json.loads(CADENAS.read_text(encoding="utf-8"))) if CADENAS.exists() else []


def main():
    simular = "--simular" in sys.argv
    d = json.loads(DATOS.read_text(encoding="utf-8"))
    regs = cargar_reglas()
    cambios = sum(etiquetar(m, regs) for m in d["movimientos"])
    por = {}
    for m in d["movimientos"]:
        for c in m.get("cadenas", []):
            por[c] = por.get(c, 0) + 1
    con = sum(1 for m in d["movimientos"] if m.get("cadenas"))
    print(f"Movimientos: {len(d['movimientos'])} · con «cadenas»: {con} · titulares con umbral: "
          f"{sum(1 for m in d['movimientos'] if m.get('umbral'))} · cambiados: {cambios}")
    print("  " + " · ".join(f"{k} {v}" for k, v in sorted(por.items(), key=lambda x: -x[1])))
    if simular:
        print("(simulación: no se escribe nada)")
        return
    if cambios:
        DATOS.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
