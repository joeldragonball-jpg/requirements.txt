"""FIFO de criptomonedas (criterio de la AEAT: lotes homogéneos, de forma conjunta entre todas las carteras).
Lee tu Excel de control (pestañas Transacciones*) y escribe un informe en privado/ (que NO se sube a GitHub).
No llama a ninguna API ni usa IA. Uso:  python fiscal/fifo.py "privado/Copia de Control_Cartera_Cripto.xlsx"
Compras: 'Total Invertido' ya incluye la comisión. Ventas: 'Total' (negativo) es lo cobrado, ya neto de comisión."""
import sys, csv, datetime as dt
from collections import defaultdict, deque
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lector_xlsx import leer


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def cargar(ruta):
    ops = []
    for hoja, filas in leer(ruta).items():
        if not hoja.startswith("Transacciones"):
            continue
        for n, d in filas[1:]:
            if "A" not in d or "B" not in d:
                continue
            ops.append({"fecha": dt.date(1899, 12, 30) + dt.timedelta(days=int(num(d["A"]))), "tipo": d["B"], "tok": d.get("C", ""),
                        "cant": num(d.get("D")), "precio": num(d.get("E")), "fee": num(d.get("F")), "total": num(d.get("G")),
                        "cartera": d.get("H", ""), "hoja": hoja, "fila": n})
    ops.sort(key=lambda o: (o["fecha"], 0 if o["tipo"] == "Compra" else 1, o["hoja"], o["fila"]))   # el mismo día, primero las compras
    return ops


def ajustar(ops, ruta_ajustes):
    """Aplica privado/ajustes.csv (columnas: fecha,tipo,tok,cant,total,cartera,nota): operaciones que faltan en el Excel (tipo Compra/Venta)
    y, con tipo CosteLote, el coste real de una compra que figura a 0 € (misma fecha y token)."""
    if not Path(ruta_ajustes).exists():
        return ops, []
    notas = []
    for r in csv.DictReader(open(ruta_ajustes, encoding="utf-8-sig")):
        f = dt.date.fromisoformat(r["fecha"]); t = r["tipo"]
        if t == "CosteLote":
            for o in ops:
                if o["tipo"] == "Compra" and o["tok"] == r["tok"] and o["fecha"] == f and o["total"] == 0:
                    o["total"] = num(r["total"]); notas.append(f"Coste de la compra {r['tok']} del {f} fijado en {num(r['total']):.2f} € ({r['nota']})"); break
        else:
            ops.append({"fecha": f, "tipo": t, "tok": r["tok"], "cant": num(r["cant"]) * (-1 if t == "Venta" else 1), "precio": 0.0, "fee": 0.0,
                        "total": num(r["total"]) * (-1 if t == "Venta" else 1), "cartera": r.get("cartera", ""), "hoja": "ajustes", "fila": 0})
            notas.append(f"Añadida {t} {r['tok']} {f}: {r['nota']}")
    ops.sort(key=lambda o: (o["fecha"], 0 if o["tipo"] == "Compra" else 1, o["hoja"], o["fila"]))
    return ops, notas


def fifo(ops):
    lotes = defaultdict(deque)
    ventas, avisos = [], []
    for o in ops:
        tok = o["tok"]
        if o["tipo"] == "Compra":
            lotes[tok].append([o["fecha"], o["cant"], o["total"], o["cant"]])   # fecha, restante, coste total, cantidad original
        elif o["tipo"] == "Venta":
            q, cobrado, coste = abs(o["cant"]), abs(o["total"]), 0.0
            falta = q
            while falta > 1e-9 and lotes[tok]:
                lote = lotes[tok][0]
                tomar = min(falta, lote[1])
                coste += lote[2] * tomar / lote[3]
                lote[2] -= lote[2] * tomar / lote[1] if lote[1] else 0
                lote[1] -= tomar; falta -= tomar
                lote[3] = lote[1] if lote[1] else lote[3]
                if lote[1] <= 1e-9:
                    lotes[tok].popleft()
            if falta > 1e-6:
                avisos.append(f"{o['fecha']} {tok}: vendes {q:g} y solo había compras para {q - falta:g} (faltan {falta:g}): revisa compras anteriores")
            ventas.append({**o, "cobrado": cobrado, "coste": coste, "ganancia": cobrado - coste})
        else:
            avisos.append(f"{o['fecha']} {tok}: tipo desconocido '{o['tipo']}' ({o['hoja']} fila {o['fila']})")
    return lotes, ventas, avisos


def informe(ruta):
    ops, notas = ajustar(cargar(ruta), Path(ruta).parent / "ajustes.csv")
    lotes, ventas, avisos = fifo(ops)
    L = ["# Informe FIFO (cripto)", f"_Generado {dt.date.today()} a partir de tu Excel. Es un cálculo orientativo: contrástalo con tu informe de la renta y con un asesor._", ""]
    L += ["## Plusvalías y minusvalías realizadas por año", "| Año | Token | Cobrado € | Coste € | Ganancia € |", "|---|---|---|---|---|"]
    por = defaultdict(lambda: [0.0, 0.0])
    for v in ventas:
        por[(v["fecha"].year, v["tok"])][0] += v["cobrado"]; por[(v["fecha"].year, v["tok"])][1] += v["coste"]
    tot = defaultdict(float)
    for (a, t), (c, k) in sorted(por.items()):
        L.append(f"| {a} | {t} | {c:.2f} | {k:.2f} | {c - k:+.2f} |"); tot[a] += c - k
    L += ["", "**Total por año:** " + " · ".join(f"{a}: {g:+.2f} €" for a, g in sorted(tot.items())), ""]
    L += ["## Cada venta", "| Fecha | Token | Cantidad | Cobrado € | Coste FIFO € | Ganancia € | Cartera |", "|---|---|---|---|---|---|---|"]
    for v in ventas:
        L.append(f"| {v['fecha']} | {v['tok']} | {abs(v['cant']):g} | {v['cobrado']:.2f} | {v['coste']:.2f} | {v['ganancia']:+.2f} | {v['cartera']} |")
    L += ["", "## Lo que te queda (lotes vivos, orden FIFO)", "| Token | Cantidad | Coste € | Precio medio € |", "|---|---|---|---|"]
    for tok, ls in lotes.items():
        q = sum(l[1] for l in ls); c = sum(l[2] for l in ls)
        L.append(f"| {tok} | {q:.4f} | {c:.2f} | {c / q if q else 0:.4f} |")
    L += ["", "## Ajustes aplicados (privado/ajustes.csv)"] + ([f"- {n}" for n in notas] or ["- Ninguno."])
    L += ["", "## Avisos"] + ([f"- {a}" for a in avisos] or ["- Ninguno."])
    L += ["", "## Dudas [VERIFICAR]", "- Permutas entre criptos, staking y regalos/airdrops no están en el Excel: si los hubo, tributan y no los estoy contando.",
          "- Compras con coste 0 (p. ej. la primera de XRP) se tratan como coste 0 €: confirma si fue un regalo o un traspaso.",
          "- Plusvalías de ahorro: tramos 19-30 % (ver el apunte del cerebro, marcado [VERIFICAR] vigencia 2026)."]
    return "\n".join(L), ventas, lotes


if __name__ == "__main__":
    ruta = sys.argv[1]
    texto, ventas, lotes = informe(ruta)
    salida = Path(ruta).parent / "fifo-informe.md"
    salida.write_text(texto, encoding="utf-8")
    print(texto)
