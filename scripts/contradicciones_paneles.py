"""Contradicciones entre la terminal y el móvil (C94). Sin IA, sin red. Compara las mismas cifras en
explorador/paneles.json (terminal) y docs/movil/data.json (móvil, generado de aquel) y avisa si difieren, o si hay tres cosas más:
Brent en dos fuentes del mismo día, y fechas de lectura muy distintas entre paneles. Escribe research/contradicciones-paneles.md.
Una diferencia casi siempre significa que el móvil no se ha regenerado (python scripts/construir_movil.py). Uso: python scripts/contradicciones_paneles.py"""
import json
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def cargar(ruta):
    return json.loads((RAIZ / ruta).read_text(encoding="utf-8"))


def indexar(lista, clave):
    return {x[clave]: x for x in lista if isinstance(x, dict) and clave in x}


def main():
    P = cargar("explorador/paneles.json")
    M = cargar("docs/movil/data.json")
    # (nombre, lista terminal, lista móvil, clave de unión, campo numérico)
    pares = [
        ("Cripto (precio)", P["mercado"]["activos"], M["mercado"], "simbolo", "precio"),
        ("Índices (valor)", P["indices"]["indices"], M["indices"], "simbolo", "valor"),
        ("Tipos de interés (num)", P["tipos_vivos"]["paises"], M["tipos"], "jur", "num"),
        ("Tipos BIS (num)", P["tipos_bis"]["paises"], M["tipos_bis"], "id", "num"),
        ("Inflación (interanual)", P["inflacion"]["paises"], M["inflacion"], "id", "interanual"),
        ("Bonos 10 a. (valor)", [dict(id=x["id"], valor=x.get("ultimo", x.get("valor"))) for x in P["bonos"]["paises"]], M["bonos"], "id", "valor"),
        ("Defensa (% PIB)", P["defensa"]["paises"], M["defensa"], "id", "valor"),
    ]
    filas, comparadas, avisos = [], 0, []
    for nombre, a, b, clave, campo in pares:
        ia, ib = indexar(a, clave), indexar(b, clave)
        for k in sorted(set(ia) & set(ib)):
            va, vb = ia[k].get(campo), ib[k].get(campo)
            if not isinstance(va, (int, float)) or not isinstance(vb, (int, float)):
                continue
            comparadas += 1
            if abs(va - vb) > 1e-6 * max(1, abs(va)):
                filas.append((nombre, k, va, vb))
        solo = (set(ia) ^ set(ib))
        if solo and ia and ib:
            avisos.append(f"{nombre}: sin pareja en el otro lado → {', '.join(sorted(map(str, solo)))[:90]}")
    # Brent: futuro de materias (terminal) frente al de petróleo del móvil, si son del mismo día
    try:
        br_t = next(m for m in P["materias"]["materias"] if "Brent" in m["nombre"])
        br_m = M["petroleo"]["brent"]
        if br_t["fecha"] == br_m["fecha"]:
            if abs(br_t["valor"] - br_m["valor"]) > 0.5:
                filas.append(("Brent futuro (mismo día)", br_t["fecha"], br_t["valor"], br_m["valor"]))
            comparadas += 1
        else:
            avisos.append(f"Brent: terminal {br_t['valor']} ({br_t['fecha']}) y móvil {br_m['valor']} ({br_m['fecha']}) son de días distintos: no comparables")
        spot = next(s for s in P["materias"]["spot_eia"]["series"] if s["id"] == "brent")
        avisos.append(f"Brent spot EIA {spot['valor']} ({spot['fecha']}) frente al futuro {br_t['valor']} ({br_t['fecha']}): son medidas distintas (spot fechado vs futuro), con fechas lejanas")
    except Exception as e:
        avisos.append(f"Brent: no se pudo comparar ({type(e).__name__})")
    hoy = date.today().isoformat()
    L = [f"# Contradicciones entre paneles (autogenerado {hoy}, no editar a mano)", "",
         "Lo regenera `python scripts/contradicciones_paneles.py`. Compara la terminal (`explorador/paneles.json`) con el móvil (`docs/movil/data.json`). "
         "Una diferencia = el móvil está desfasado: `python scripts/construir_movil.py`.", "",
         f"- Cifras comparadas: **{comparadas}** · diferencias: **{len(filas)}**", ""]
    if filas:
        L += ["| Panel | Clave | Terminal | Móvil |", "|---|---|---|---|"] + [f"| {n} | {k} | {a} | {b} |" for n, k, a, b in filas] + [""]
    L += ["## Avisos (no son errores)", ""] + [f"- {x}" for x in avisos]
    (RAIZ / "research" / "contradicciones-paneles.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"contradicciones-paneles.md: {comparadas} cifras comparadas, {len(filas)} diferencias, {len(avisos)} avisos")
    return 1 if filas else 0


if __name__ == "__main__":
    sys.exit(main())
