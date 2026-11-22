#!/usr/bin/env python3
"""Frescura de explorador/*.json por la fecha del DATO (no la del archivo). Sin IA, solo lectura.
Semaforo: verde <=7 d, amarillo <=30 d, rojo >30 d. Uso: python scripts/frescura_explorador.py"""
import json, re, sys, datetime as dt
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
# fecha de LECTURA/actualizacion del archivo (no prueba que el dato sea reciente)
META = {"leido", "actualizado", "_actualizado", "as_of", "generado", "fecha_lectura", "updated", "ultima_actualizacion",
        "generado_utc", "_leido", "revisado"}   # 21-nov (C362): claves de lectura que ya traían 3 archivos grises
# No son datos sino índices, listas de enlaces o exportaciones de prueba: no se juzgan por frescura (C362, 21-nov)
EXCLUIR = {"frescura.json", "centro.json", "enlaces.json", "prueba-datos.json"}
# Cierres periódicos: un rojo puede significar «aún no hay edición nueva» y no un fallo de lectura. Se marca para que
# W05/W08 comprueben en la fuente si ya salió la siguiente edición (no se da por buena sin mirar).
PERIODICOS = {
    "bancos-eba.json": "EBA: ejercicio de transparencia anual; comprobar si hay edición posterior a jun-2025",
    "seguridad-eurostat.json": "Eurostat: cierre anual; comprobar si hay edición nueva",
    "deuda-fmi.json": "FMI WEO: abril y octubre; comprobar la edición vigente",
    "espana-contratacion.json": "PLACSP: trimestral o anual; comprobar si hay periodo nuevo",
}
MESES = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
         "septiembre": 9, "setiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}
# fecha/periodo del DATO: se usa la mas reciente no futura; si el archivo no trae ninguna, se cae a la de lectura
DATO = {"fecha_dato", "fecha", "d", "date", "ultimo_periodo", "periodo", "hasta", "mes", "anio", "ultimo_dato", "dato_de"}
EVENTO = DATO
RE = re.compile(r"^(\d{4})(?:-(\d{2})(?:-(\d{2}))?|-?[QqTt](\d)|T(\d))?")
HOY = dt.date.today()


def parsea(v):
    """AAAA-MM-DD, AAAA-MM (fin de mes), AAAA-Qn / AAAAT n (fin de trimestre) o AAAA (31-dic) -> date; None si no es fecha."""
    if isinstance(v, int) and 1990 <= v <= 2100:
        v = str(v)
    if not isinstance(v, str):
        return None
    s = v.strip().lower()
    mq = re.match(r"^(?:([1-4])\s*[tq]|[tq]\s*([1-4]))\s*(?:de\s+)?(\d{4})\b", s)   # «2T 2026», «T2 2026», «3Q 2026»
    if mq:
        return parsea(f"{mq.group(3)}-Q{mq.group(1) or mq.group(2)}")
    ma = re.match(r"^([a-záéíóú]{3,10})\.?[\s-]+(?:de\s+)?(\d{4})\b", s)   # «oct-2026», «oct 2026», «octubre de 2026»
    if ma:
        for nombre, n in MESES.items():
            if nombre == ma.group(1) or (len(ma.group(1)) == 3 and nombre.startswith(ma.group(1))):
                return parsea(f"{ma.group(2)}-{n:02d}")
    mm = re.match(r"^([a-záéíóú]+) (\d{4})", v.strip().lower())   # «enero 2026 (revisión agosto 2026)» -> fin de mes
    if mm and mm.group(1) in MESES:
        a, mes = int(mm.group(2)), MESES[mm.group(1)]
        return dt.date(a + (mes == 12), mes % 12 + 1, 1) - dt.timedelta(days=1)
    m = re.match(r"^(\d{4})(?:-(\d{2})(?:-(\d{2}))?|-?[QqTt](\d))?$", v.strip()[:10]) or re.match(r"^(\d{4})-(\d{2})-(\d{2})", v.strip())
    if not m:
        return None
    a, mes, dia, q = m.group(1), m.group(2), m.group(3), (m.group(4) if m.re.groups >= 4 else None)
    try:
        a = int(a)
        if dia:
            return dt.date(a, int(mes), int(dia))
        if mes:
            mes = int(mes)
        elif q:
            mes = 3 * int(q)
        else:
            mes = 12
        if not 1 <= mes <= 12:
            return None
        fin = dt.date(a + (mes == 12), mes % 12 + 1, 1) - dt.timedelta(days=1)
        return fin
    except ValueError:
        return None


def recorre(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in META or k in DATO:
                f = parsea(v)
                if f is not None:
                    acc["meta" if k in META else "ev"].append(min(f, HOY) if k in DATO and f > HOY and f.month == HOY.month and f.year == HOY.year else f)
                    continue
            if isinstance(v, (dict, list)):
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
        if p.name in EXCLUIR:   # salida de este script, índices y pruebas
            continue
        acc = {"meta": [], "ev": []}
        try:
            recorre(json.loads(p.read_text(encoding="utf-8")), acc)
        except Exception as e:
            filas.append((p.name, None, "error", None)); continue
        meta = [x for x in acc["meta"] if x <= HOY]
        ev = [x for x in acc["ev"] if x <= HOY]   # ignora fechas futuras (calendarios, vencimientos)
        fechas = ev or meta                       # primero la fecha del DATO; la de lectura solo si no hay otra
        f = max(fechas) if fechas else None
        dias = (HOY - f).days if f else None
        origen = "dato" if ev else "lectura" if meta else "-"
        lec = max(meta) if meta else None
        # Periodo cerrado + lectura reciente: un dato anual (fin de año) o trimestral (fin de trimestre) NO envejece por el calendario
        # mientras sea el último cierre publicable (anual: hasta 400 d; trimestral: hasta 130 d) y el archivo se haya leído hace <=30 d.
        # Se juzga entonces por la fecha de lectura. Un dato fuera de esos plazos, o sin fecha de lectura, sigue en rojo.
        if ev and f and lec and dias is not None and dias > 30 and (HOY - lec).days <= 30:
            fin_anio = (f.month, f.day) == (12, 31) and dias <= 400
            fin_trim = (f.month, f.day) in ((3, 31), (6, 30), (9, 30), (12, 31)) and dias <= 130
            if fin_anio or fin_trim:
                dias, origen = (HOY - lec).days, "periodo cerrado + lectura"
        fa = dt.date.fromtimestamp(p.stat().st_mtime)
        filas.append((p.name, f, semaforo(dias), dias, origen, fa, lec))
    return filas


def escribir_json(filas=None):
    """Escribe explorador/frescura.json (lo lee construir_seguimiento.py). Solo fechas de dato y semáforo; sin IA."""
    filas = filas if filas is not None else main()
    items = []
    for f in sorted(filas, key=lambda x: x[0]):
        if len(f) < 6:
            items.append({"archivo": f[0], "fecha_dato": None, "dias": None, "semaforo": "error", "origen": None})
        else:
            items.append({"archivo": f[0], "fecha_dato": f[1].isoformat() if f[1] else None, "dias": f[3], "semaforo": f[2], "origen": f[4], "fecha_lectura": f[6].isoformat() if f[6] else None,
                          **({"periodico": PERIODICOS[f[0]]} if f[0] in PERIODICOS and f[2] in ("rojo", "amarillo") else {})})
    cuenta = {k: sum(1 for i in items if i["semaforo"] == k) for k in ("verde", "amarillo", "rojo", "gris", "error")}
    out = {"nivel": "P", "generado": HOY.isoformat(), "fuente": "scripts/frescura_explorador.py (fecha del DATO de cada explorador/*.json: periodo/fecha más reciente no futura; si no hay, la de lectura; un cierre anual/trimestral reciente se juzga por la lectura; sin IA)",
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
         "Fecha del DATO (la más reciente no futura entre fecha/ultimo_periodo/periodo/hasta/mes/d...); solo si el archivo no trae ninguna se usa la de lectura (leido/_actualizado/generado). "
         "Verde ≤7 d, amarillo ≤30 d, rojo >30 d, gris = sin fecha de dato legible.", "",
         "Resumen: " + ", ".join(f"{k} {v}" for k, v in sorted(cuenta.items())), "",
         "| Archivo | Fecha dato | Días | Semáforo | Origen | Modif. archivo | Lectura |", "|---|---|---|---|---|---|---|"]
    orden = {"rojo": 0, "gris": 1, "amarillo": 2, "verde": 3, "error": 4}
    for f in sorted(filas, key=lambda x: (orden[x[2]], -(x[3] or 0))):
        if len(f) < 6:
            L.append(f"| {f[0]} | error al leer | | error | | |"); continue
        L.append(f"| {f[0]} | {f[1] or '-'} | {f[3] if f[3] is not None else '-'} | {f[2]} | {f[4]} | {f[5]} | {f[6] or '-'} |")
    L += ["", "## Archivos rojos y grises: propuesta de sesión que los refresca", ""]
    for f in filas:
        if f[2] in ("rojo", "gris"):
            L.append(f"- {f[0]} ({f[2]}{', '+str(f[3])+' d' if f[3] is not None else ''}): {propuesta(f[0])}"
                     + (f" · PERIÓDICO: {PERIODICOS[f[0]]}" if f[0] in PERIODICOS else ""))
    L += ["", "Nota: un JSON «manual» o de referencia puede ser estable a propósito; el rojo indica revisar, no error. "
          "Los grises no traen fecha de dato: conviene añadir un campo `actualizado` (propuesta, no aplicada)."]
    out = RAIZ / "informes" / "research" / "2026-11-14-C287-frescura.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(out, cuenta)
