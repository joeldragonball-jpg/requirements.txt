#!/usr/bin/env python3
"""Frescura de explorador/*.json por la fecha del DATO (no la del archivo). Sin IA, solo lectura.
Semaforo: verde <=7 d, amarillo <=30 d, rojo >30 d. Uso: python scripts/frescura_explorador.py"""
import json, re, sys, datetime as dt
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
META = {"leido", "actualizado", "as_of", "generado", "fecha_dato", "fecha_lectura", "updated", "ultima_actualizacion"}
EVENTO = {"d", "fecha", "date"}
RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
HOY = dt.date.today()


def recorre(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str) and (k in META or k in EVENTO):
                m = RE.match(v)
                if m:
                    try:
                        f = dt.date.fromisoformat(m.group(1))
                    except ValueError:
                        continue
                    if f <= HOY:  # ignora fechas futuras (calendarios, vencimientos)
                        acc["meta" if k in META else "ev"].append(f)
            else:
                recorre(v, acc)
    elif isinstance(o, list):
        for v in o:
            recorre(v, acc)


def semaforo(dias):
    if dias is None:
        return "gris"
    return "verde" if dias <= 7 else "amarillo" if dias <= 30 else "rojo"


def main():
    filas = []
    for p in sorted((RAIZ / "explorador").glob("*.json")):
        if p.name == "frescura.json":   # es la salida de este script
            continue
        acc = {"meta": [], "ev": []}
        try:
            recorre(json.loads(p.read_text(encoding="utf-8")), acc)
        except Exception as e:
            filas.append((p.name, None, "error", None)); continue
        fechas = acc["meta"] or acc["ev"]
        f = max(fechas) if fechas else None
        dias = (HOY - f).days if f else None
        fa = dt.date.fromtimestamp(p.stat().st_mtime)
        filas.append((p.name, f, semaforo(dias), dias, "meta" if acc["meta"] else "evento" if acc["ev"] else "-", fa))
    return filas


def escribir_json(filas=None):
    """Escribe explorador/frescura.json (lo lee construir_seguimiento.py). Solo fechas de dato y semáforo; sin IA."""
    filas = filas if filas is not None else main()
    items = []
    for f in sorted(filas, key=lambda x: x[0]):
        if len(f) < 6:
            items.append({"archivo": f[0], "fecha_dato": None, "dias": None, "semaforo": "error", "origen": None})
        else:
            items.append({"archivo": f[0], "fecha_dato": f[1].isoformat() if f[1] else None, "dias": f[3], "semaforo": f[2], "origen": f[4]})
    cuenta = {k: sum(1 for i in items if i["semaforo"] == k) for k in ("verde", "amarillo", "rojo", "gris", "error")}
    out = {"nivel": "P", "generado": HOY.isoformat(), "fuente": "scripts/frescura_explorador.py (fecha del dato de cada explorador/*.json; sin IA)",
           "umbrales_dias": {"verde": 7, "amarillo": 30}, "resumen": cuenta, "items": items}
    (RAIZ / "explorador" / "frescura.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + chr(10), encoding="utf-8")
    return out


SESION = [  # prefijo -> sesion que lo refresca
    ("precios", "R00 / actualizar_precios (diaria)"),
    ("paneles", "W-paneles: actualizar_paneles.py"),
    ("indicadores", "actualizar indicadores (FMI/BM) + manual"),
    ("espana", "bloque España: construir_espana*.py + rutina España a fondo"),
    ("cadenas", "sesión Cadenas (C264+)"),
    ("rwa", "sesión Cadenas / RWA"),
    ("cbdc", "sesión Cadenas / CBDC"),
    ("estabilidad", "sesión estabilidad financiera (BIS/BCE)"),
    ("bonos", "sesión renta fija / bonos"),
    ("calificaciones", "sesión crédito / calificaciones"),
    ("deuda", "sesión deuda soberana (FMI)"),
    ("reservas", "sesión reservas / oro"),
    ("regulacion", "sesión regulación por país"),
]


def propuesta(n):
    for pre, s in SESION:
        if n.startswith(pre):
            return s
    return "sesión de research del tema (asignar)"


if __name__ == "__main__":
    filas = main()
    escribir_json(filas)
    cuenta = {}
    for f in filas:
        cuenta[f[2]] = cuenta.get(f[2], 0) + 1
    L = [f"# C287 · Frescura de explorador/ ({HOY.isoformat()})", "",
         "Fecha del DATO (campos leido/actualizado/generado/as_of/fecha_dato; si no hay, la máxima d/fecha no futura), no la del archivo. "
         "Verde ≤7 d, amarillo ≤30 d, rojo >30 d, gris = sin fecha de dato legible.", "",
         "Resumen: " + ", ".join(f"{k} {v}" for k, v in sorted(cuenta.items())), "",
         "| Archivo | Fecha dato | Días | Semáforo | Origen | Modif. archivo |", "|---|---|---|---|---|---|"]
    orden = {"rojo": 0, "gris": 1, "amarillo": 2, "verde": 3, "error": 4}
    for f in sorted(filas, key=lambda x: (orden[x[2]], -(x[3] or 0))):
        if len(f) < 6:
            L.append(f"| {f[0]} | error al leer | | error | | |"); continue
        L.append(f"| {f[0]} | {f[1] or '-'} | {f[3] if f[3] is not None else '-'} | {f[2]} | {f[4]} | {f[5]} |")
    L += ["", "## Archivos rojos y grises: propuesta de sesión que los refresca", ""]
    for f in filas:
        if f[2] in ("rojo", "gris"):
            L.append(f"- {f[0]} ({f[2]}{', '+str(f[3])+' d' if f[3] is not None else ''}): {propuesta(f[0])}")
    L += ["", "Nota: un JSON «manual» o de referencia puede ser estable a propósito; el rojo indica revisar, no error. "
          "Los grises no traen fecha de dato: conviene añadir un campo `actualizado` (propuesta, no aplicada)."]
    out = RAIZ / "informes" / "research" / "2026-11-14-C287-frescura.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(out, cuenta)
