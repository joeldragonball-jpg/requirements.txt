"""C234 (9-nov-2026): cruza los hechos extraídos de los informes (informes/hechos/lote-NN.jsonl) con la Línea de tiempo de la Órbita
(explorador/datos.json). Local, sin IA y sin red. Escribe research/CRUCE-HECHOS.md.

Por cada hecho busca un movimiento de la Órbita con fecha a ±5 días y palabras en común (cifras y nombres propios pesan más).
  · «cubierto»: hay movimiento parecido.   · «falta»: no lo hay (candidato a volcar, siempre revisando antes).
  · «repetido»: el mismo hecho sale en 2+ informes (texto casi igual).
  · «cifras distintas»: mismo tema y fecha con números que no coinciden (candidato a contradicción; lo decide una persona).
Uso: python scripts/cruzar_hechos.py
"""
import collections
import datetime
import json
import pathlib
import re
import sys

R = pathlib.Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding="utf-8")
PARADAS = set("de la el los las en y a que del un una por con para se su al lo es o como más sus pero sobre entre ha han son este esta fue ser dos tras desde sin ya no si le the of and to in for".split())


def tokens(t):
    return {w for w in re.findall(r"[a-záéíóúñü0-9][a-záéíóúñü0-9.,%$-]*", t.lower()) if w not in PARADAS and len(w) > 2}


def cifras(t):
    return {c.replace(",", ".").rstrip(".") for c in re.findall(r"\d+(?:[.,]\d+)?", t) if len(c) >= 2 and not re.fullmatch(r"20\d\d", c)}


def fecha(s):
    try:
        return datetime.date.fromisoformat((s or "")[:10])
    except Exception:
        return None


def main():
    hechos = []
    for p in sorted((R / "informes" / "hechos").glob("lote-*.jsonl")):
        for n, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if l.strip():
                try:
                    h = json.loads(l)
                    h["_lote"] = p.stem
                    hechos.append(h)
                except Exception as e:
                    print(f"AVISO {p.name}:{n} JSON roto: {e}")
    mov = json.loads((R / "explorador" / "datos.json").read_text(encoding="utf-8"))["movimientos"]
    movt = [(fecha(m.get("fecha")), tokens(m.get("texto", "") + " " + m.get("actor", "")), cifras(m.get("texto", "")), m) for m in mov]
    estado = collections.Counter()
    faltan, dudas = [], []
    for h in hechos:
        f, tk, cf = fecha(h.get("fecha")), tokens(h["hecho"]), cifras(h["hecho"])
        mejor, mejor_m = 0.0, None
        for fm, tm, cm, m in movt:
            if f and fm and abs((f - fm).days) > 5:
                continue
            comun = tk & tm
            peso = len(comun) + 2 * len(cf & cm)
            pun = peso / max(6, min(len(tk), 14))
            if pun > mejor:
                mejor, mejor_m = pun, m
        if mejor >= 0.45:
            h["_est"] = "cubierto"
            if cf and mejor_m and cifras(mejor_m.get("texto", "")) and not (cf & cifras(mejor_m.get("texto", ""))) and mejor < 0.8:
                dudas.append((h, mejor_m))
        else:
            h["_est"] = "falta"
            faltan.append(h)
        estado[(h.get("nivel"), h["_est"])] += 1
    # repetidos entre informes distintos
    vistos, rep = [], []
    for h in hechos:
        tk = tokens(h["hecho"])
        for o, tko in vistos:
            if o["informe"] != h["informe"] and len(tk & tko) / max(1, len(tk | tko)) >= 0.6:
                rep.append((o, h))
                break
        vistos.append((h, tk))
    L = [f"# Cruce de hechos de los informes con la Órbita ({datetime.date.today()})", "",
         "Generado por `scripts/cruzar_hechos.py` (local, sin IA). Es una **lista de candidatos**: el solapamiento por palabras se equivoca; "
         "nada se vuelca a la Órbita sin revisarlo. Origen de los hechos: `informes/hechos/lote-NN.jsonl` (C234).", "",
         f"- Hechos leídos: **{len(hechos)}** en {len({h['_lote'] for h in hechos})} lotes · informes distintos: {len({h['informe'] for h in hechos})}",
         f"- Movimientos en la Línea de tiempo: {len(mov)}", "", "| Nivel | Cubiertos | Faltan |", "|---|---|---|"]
    for nv in ("P", "S", "V"):
        L.append(f"| {nv} | {estado[(nv, 'cubierto')]} | {estado[(nv, 'falta')]} |")
    por_ambito = collections.Counter(h.get("ambito") for h in faltan if h.get("nivel") == "P")
    L += ["", "## Hechos P que faltan, por ámbito", "", ", ".join(f"{a} {c}" for a, c in por_ambito.most_common()) or "ninguno", "",
          "## Hechos P que parecen faltar en la Órbita (más recientes primero, máx. 120)", "", "| Fecha | Ámbito | Hecho | Fuente | Informe |", "|---|---|---|---|---|"]
    for h in sorted((x for x in faltan if x.get("nivel") == "P"), key=lambda x: x.get("fecha") or "", reverse=True)[:120]:
        L.append(f"| {h.get('fecha')} | {h.get('ambito')} | {h['hecho'].replace('|', '/')} | {(h.get('fuente') or '—')[:60].replace('|', '/')} | {pathlib.Path(h['informe']).name} |")
    L += ["", f"## Mismo hecho en 2 o más informes ({len(rep)} pares; los 40 primeros)", ""]
    for a, b in rep[:40]:
        L.append(f"- {a.get('fecha')} · «{a['hecho'][:110]}» ↔ {pathlib.Path(a['informe']).name} / {pathlib.Path(b['informe']).name}")
    L += ["", f"## Cifras que no coinciden con la Órbita en el mismo tema y fecha ({len(dudas)}; revisar a mano)", ""]
    for h, m in dudas[:40]:
        L.append(f"- {h.get('fecha')} · informe dice «{h['hecho'][:120]}» ({pathlib.Path(h['informe']).name}) · Órbita dice «{m.get('texto', '')[:120]}»")
    (R / "research" / "CRUCE-HECHOS.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{len(hechos)} hechos · cubiertos {sum(v for (n, e), v in estado.items() if e == 'cubierto')} · faltan {len(faltan)} "
          f"(P: {sum(1 for x in faltan if x.get('nivel') == 'P')}) · repetidos {len(rep)} · cifras distintas {len(dudas)} → research/CRUCE-HECHOS.md")


if __name__ == "__main__":
    main()
