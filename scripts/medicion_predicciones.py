"""Medición del registro de predicciones (C92). Sin IA, sin APIs: lee informes/predicciones.md y escribe research/medicion-predicciones.md.
Cuenta por estado, vencidas sin resultado, filas sin fecha límite y filas por fuente. NO calcula porcentajes de acierto de una fuente
hasta que tenga n >= N_MIN predicciones ya resueltas (con menos, un porcentaje sería inventado). Uso: python scripts/medicion_predicciones.py"""
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
N_MIN = 5


def limpiar(t):
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", t)).strip()


def estado(res):
    r = res.lower()
    if not r or r.startswith("sin resolver"):
        return "abierta"
    if r.startswith("parece que falló") or r.startswith("falló") or "fallo" in r[:12]:
        return "falló"
    if r.startswith("acertó") or r.startswith("parece que acertó"):
        return "acertó"
    return "otro"


def fuente(quien):
    """Fuente principal sin el «citado por …»/«según prensa» (el que habla, no el que cita)."""
    q = re.split(r"\s*(?:,|\(|vía|según)\s*", limpiar(quien), maxsplit=1)[0]
    return q or "?"


def main():
    hoy = date.today()
    filas = []
    for linea in (RAIZ / "informes" / "predicciones.md").read_text(encoding="utf-8").splitlines():
        if not re.match(r"\|\s*\d+\s*\|", linea):
            continue
        c = [limpiar(x) for x in linea.strip().strip("|").split("|")]
        if len(c) < 7:
            continue
        lim = c[4] if re.match(r"\d{4}-\d{2}-\d{2}$", c[4]) else None
        filas.append({"n": int(c[0]), "quien": fuente(c[2]), "limite": lim, "est": estado(c[6])})
    tot = Counter(f["est"] for f in filas)
    vencidas = [f for f in filas if f["est"] == "abierta" and f["limite"] and f["limite"] < hoy.isoformat()]
    sin_limite = [f for f in filas if not f["limite"]]
    por = defaultdict(Counter)
    for f in filas:
        por[f["quien"]][f["est"]] += 1
    L = [f"# Medición de predicciones (autogenerado {hoy.isoformat()}, no editar a mano)", "",
         "Lo regenera `python scripts/medicion_predicciones.py` desde `informes/predicciones.md`. Son opiniones [ESPECULACIÓN], no hechos. "
         f"Un % de acierto por fuente solo aparece con n ≥ {N_MIN} predicciones resueltas; con menos sería inventado.", "",
         f"- Total: **{len(filas)}** · abiertas {tot['abierta']} · acertó {tot['acertó']} · falló {tot['falló']} · otro {tot['otro']}",
         f"- Vencidas sin resultado: **{len(vencidas)}** " + (", ".join(f"#{f['n']}" for f in vencidas) or "(ninguna)"),
         f"- Sin fecha límite parseable: **{len(sin_limite)}** (no se pueden dar por vencidas) " + ", ".join(f"#{f['n']}" for f in sin_limite[:30]), "",
         "| Fuente | n | abiertas | resueltas | acertó | falló | % acierto |", "|---|---|---|---|---|---|---|"]
    for q, k in sorted(por.items(), key=lambda x: -sum(x[1].values()))[:25]:
        n = sum(k.values()); res = k["acertó"] + k["falló"]
        pct = f"{round(100 * k['acertó'] / res)} %" if res >= N_MIN else f"— (n resueltas = {res} < {N_MIN})"
        L.append(f"| {q} | {n} | {k['abierta']} | {res} | {k['acertó']} | {k['falló']} | {pct} |")
    (RAIZ / "research" / "medicion-predicciones.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"medicion-predicciones.md: {len(filas)} predicciones, {len(vencidas)} vencidas sin resultado, {len(sin_limite)} sin fecha límite")


if __name__ == "__main__":
    sys.exit(main())
