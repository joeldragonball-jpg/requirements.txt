"""Auditoría de frescura de las cifras de países (C63): sin IA ni red. Lee paneles.json["indicadores"] y estabilidad.json.

Retraso = meses entre el final del periodo del dato y hoy. Umbral: 12 meses (anual/irregular) o 3 meses (mensual/trimestral).
Uso: python scripts/auditoria_frescura_paises.py [--todo]
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
HOY = date.today()


def fin_periodo(f):
    """'2025' -> dic-2025; '2025-12' -> dic-2025; '2026-Q3' -> sep-2026; semestre 'S1' -> jun."""
    f = str(f or "")
    m = re.match(r"^(\d{4})-Q(\d)$", f)
    if m:
        return int(m[1]), int(m[2]) * 3
    m = re.match(r"^(\d{4})-S(\d)$", f)
    if m:
        return int(m[1]), int(m[2]) * 6
    m = re.match(r"^(\d{4})-(\d{2})", f)
    if m:
        return int(m[1]), int(m[2])
    m = re.match(r"^(\d{4})$", f)
    if m:
        return int(m[1]), 12
    return None


def retraso(f):
    p = fin_periodo(f)
    return None if not p else (HOY.year - p[0]) * 12 + HOY.month - p[1]


def main():
    todo = "--todo" in sys.argv
    pan = json.loads((RAIZ / "explorador" / "paneles.json").read_text(encoding="utf-8"))
    est = json.loads((RAIZ / "explorador" / "estabilidad.json").read_text(encoding="utf-8"))
    filas = []
    for p in pan["indicadores"]["paises"]:
        for k, d in p["indicadores"].items():
            per = d.get("periodicidad", "")
            umbral = 3 if per in ("mensual", "trimestral") else 12
            filas.append((p["id"], "ind/" + k, d.get("valor"), d.get("fecha"), umbral))
    for p in est["paises"]:
        for dim, bloque in p["dimensiones"].items():
            for c in bloque.get("cifras", []):
                filas.append((p["id"], f"{dim}/{c['nombre']}", c.get("valor"), c.get("anio"), 12))
    viejos = 0
    for pid, clave, val, f, um in filas:
        r = retraso(f)
        if val is None or r is None:
            marca = "SIN DATO"
        elif r > um:
            marca = f"VIEJO {r}m"
        else:
            marca = ""
        if marca:
            viejos += 1
        if marca or todo:
            print(f"{pid} {clave} = {val} ({f}) {marca}")
    print(f"\n{viejos} de {len(filas)} cifras viejas o sin dato (hoy {HOY})")


if __name__ == "__main__":
    main()
