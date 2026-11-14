"""Cadenas ↔ noticias (C266). Python normal: NO usa IA, ni la API de Anthropic, ni la red.

Uso:  python scripts/etiquetar_cadenas.py [--simular]
Pone en cada movimiento de explorador/datos.json dos campos opcionales, calculados solo por reglas:

  «cadenas»: ids de explorador/cadenas.json cuyas palabras («busca» más las de EXTRA) aparecen como palabra entera,
             respetando mayúsculas, en el actor, las entidades («ent») o los activos («act»); en los hechos a mano también
             en el texto, pero solo con nombres propios (TEXTO_FUERTE). Las palabras de terceros (Swift, Binance) no
             etiquetan; «DTCC» etiqueta Canton solo si el movimiento no nombra otra red. En las noticias del bot
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
# Palabras que sí etiquetan aunque no estén en «busca» (nombres de la red, de su mejora o de su token).
EXTRA = {
    "bnb": ["BNB Chain", "BNB Smart Chain", "opBNB", "BSC"],
    "ethereum": ["Glamsterdam", "Ether"],
    "solana": ["Alpenglow"],
    "chainlink": ["CCIP", "LINK"],
    "canton": ["Canton Coin", "Digital Asset"],
    "stellar": ["Stellar Development Foundation", "SDF"],
    "xrpl": ["XRP Ledger"],
    "polygon": ["POL", "MATIC", "Polygon PoS"],
    "avalanche": ["Ava Labs"],
    "hedera": ["Hashgraph", "Hedera Council"],
    "ondo": ["Ondo Finance"],
    "algorand": ["ALGO"],
    "xdc": ["XinFin", "XDC Network"],
    "quant": ["QNT"],
}
# Palabras de un tercero que solo valen si el movimiento no nombra con claridad otra red: una nota de DTCC sin red
# sigue en Canton (su primera plataforma), pero la de «DTCC y Stellar» es solo de Stellar.
DEBIL = {"canton": {"DTCC"}}
# En los hechos escritos a mano también se mira el texto, pero solo con nombres propios de la red (no con
# símbolos sueltos como ETH, SOL o LINK, que salen en notas de otros temas).
TEXTO_FUERTE = {
    "xrpl": ["XRPL", "XRP Ledger"], "stellar": ["Stellar"], "hedera": ["Hedera"], "ethereum": ["Ethereum", "Glamsterdam"],
    "solana": ["Solana", "Alpenglow"], "bnb": ["BNB Chain", "BNB Smart Chain", "opBNB"], "avalanche": ["Avalanche"],
    "polygon": ["Polygon"], "canton": ["Canton"], "chainlink": ["Chainlink"], "ondo": ["Ondo"],
    "algorand": ["Algorand"], "xdc": ["XinFin", "XDC Network"], "quant": ["Overledger"], "iota": ["IOTA"],
    "plume": ["Plume"],
}

_VERBO = (r"supera(?:n|ba|r|ron)?|super[óo]|rebasa(?:n)?|rebas[óo]|cae(?:n)? (?:por )?(?:debajo|bajo) de|cay[óo] (?:por )?debajo de|"
          r"baja(?:n)? de|pierde(?:n)? los|toca(?:n)?|toc[óo]|alcanza(?:n)?|alcanz[óo]|sube(?:n)? (?:a|hasta)|subi[óo] (?:a|hasta)|"
          r"rompe(?:n)?|cruza(?:n)?|roza(?:n)?|por encima de|por debajo de|(?:máximo|mínimo)s? de")
_CIFRA = (r"(?:[$€]\s?\d[\d.,]*|\d[\d.,]*\s?(?:%|\$|€|k\b|dólares|euros|puntos|pb\b|"
          r"(?:mil(?:es)? de )?(?:millones|billones)|mil\b|M\$|M€))")
UMBRAL = re.compile(r"(?:^|\W)(?:" + _VERBO + r")\b[^.;:]{0,40}?" + _CIFRA, re.I)


def _rx(p):
    return re.compile(r"(?<!\w)" + re.escape(p) + r"(?!\w)")


def reglas(cad):
    """[(id, [regex…], [regex débiles…], [regex de texto…])] a partir de cadenas.json («busca») más EXTRA, menos NO_ETIQUETA."""
    salida = []
    for c in cad.get("cadenas", []):
        cid = c.get("id")
        deb = DEBIL.get(cid, set())
        palabras = [b for b in (c.get("busca") or []) if b not in NO_ETIQUETA.get(cid, ()) and b not in deb] + EXTRA.get(cid, [])
        salida.append((cid, [_rx(p) for p in palabras], [_rx(p) for p in sorted(deb)], [_rx(p) for p in TEXTO_FUERTE.get(cid, [])]))
    return salida


def cadenas_de(mov, regs):
    """Ids de las redes que nombra un movimiento, en el orden de cadenas.json."""
    base = " · ".join(str(p) for p in [mov.get("actor") or ""] + list(mov.get("ent") or []) + list(mov.get("act") or []))
    texto = str(mov.get("texto") or "")
    noticia = mov.get("origen") == "noticia"
    if noticia:  # actor y entidad son el nombre del medio: se mira el titular y el tema con todas las palabras
        base += " · " + texto + " · " + str(mov.get("tema") or "")
    fuertes, debiles = [], []
    for cid, rx, deb, tx in regs:
        if any(r.search(base) for r in rx) or (not noticia and any(r.search(texto) for r in tx)):
            fuertes.append(cid)
        elif any(r.search(base) or r.search(texto) for r in deb):
            debiles.append(cid)
    if not fuertes:
        orden = [r[0] for r in regs]
        return [c for c in orden if c in debiles]
    return fuertes


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
