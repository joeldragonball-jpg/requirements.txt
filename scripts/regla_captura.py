#!/usr/bin/env python3
"""Regla reproducible para «Captura del token» (pestaña Cadenas). Solo lee; no escribe en cadenas.json.

Regla (v1, propuesta [RAZONADO]):
  Puntos por capa segun capas.<capa>.token: si=2, parcial=1, minimo=0.5, no=0, sin dato=excluida.
  Capas: liquidacion, emision, seguridad, mensajeria, custodia.
  1) Si hay dato en menos de 3 de las 5 capas  -> incierta.
  2) Si no, puntuacion = suma de puntos / (2 * capas con dato)  (0 a 1).
  3) alta  si puntuacion >= 0.6 y liquidacion o emision es «si»;
     media si puntuacion >= 0.35 (o hay al menos un «si»);
     baja  en otro caso.
  4) Aviso (no cambia el nivel): si sin_dato de la red cita «volumen» y el nivel propuesto es alta/media.
Uso: PYTHONIOENCODING=utf-8 python scripts/regla_captura.py [--json]
"""
import json, sys
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "explorador" / "cadenas.json"
CAPAS = ["liquidacion", "emision", "seguridad", "mensajeria", "custodia"]
PTS = {"sí": 2, "si": 2, "parcial": 1, "mínimo": 0.5, "minimo": 0.5, "no": 0}


def propuesta(red):
    capas = red.get("capas") or {}
    vals = {c: PTS.get((capas.get(c) or {}).get("token")) for c in CAPAS}
    con = {c: v for c, v in vals.items() if v is not None}
    if len(con) < 3:
        return "incierta", None, len(con)
    p = sum(con.values()) / (2 * len(con))
    si_uso = any(vals.get(c) == 2 for c in ("liquidacion", "emision"))
    if p >= 0.6 and si_uso:
        n = "alta"
    elif p >= 0.35 or any(v == 2 for v in con.values()):
        n = "media"
    else:
        n = "baja"
    return n, p, len(con)


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    filas, disc = [], 0
    for r in d["cadenas"]:
        act = (r.get("captura") or {}).get("nivel")
        n, p, k = propuesta(r)
        vol = any("volumen" in s.lower() for s in (r.get("sin_dato") or []))
        dif = act != n
        disc += dif
        filas.append({"id": r["id"], "actual": act, "regla": n, "puntuacion": None if p is None else round(p, 2),
                      "capas_con_dato": k, "discrepancia": dif, "aviso_volumen": vol and n in ("alta", "media")})
    if "--json" in sys.argv:
        print(json.dumps(filas, ensure_ascii=False, indent=1)); return
    print(f"{'red':10}{'actual':9}{'regla':9}{'punt':6}{'capas':6}discrepancia")
    for f in filas:
        print(f"{f['id']:10}{f['actual']:9}{f['regla']:9}{str(f['puntuacion']):6}{f['capas_con_dato']:<6}{'SI' if f['discrepancia'] else '-'}"
              + (" [aviso: volumen sin dato]" if f['aviso_volumen'] else ""))
    print(f"Discrepancias: {disc} de {len(filas)}")


if __name__ == "__main__":
    main()
