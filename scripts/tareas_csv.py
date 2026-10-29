"""Seguimiento de tareas como CSV (research/tareas.csv): la misma tabla que se publica desde una Google Sheet.
Estados fijos: pendiente, en curso, en parte, bloqueada, hecha. Solo datos PÚBLICOS (nada de privado/ ni de la tesis).

Uso:
  python scripts/tareas_csv.py migrar      # UNA vez: vuelca COLA.md, COLA-TEMAS-GEMINI.md y COLA-DEUDA-BONOS.md a research/tareas.csv
  python scripts/tareas_csv.py sincronizar # baja la Sheet publicada (URL en research/tareas-url.txt) a research/tareas.csv
Desde Python: tareas_csv.cargar() -> lista de dicts con las claves que ya usa construir_seguimiento (estado interno: hecha/pendiente/parcial/…)."""
import csv
import io
import sys
import urllib.request
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CSV = RAIZ / "research" / "tareas.csv"
URL = RAIZ / "research" / "tareas-url.txt"
COLUMNAS = ["id", "origen", "tema", "estado", "tipo", "modelo", "tam", "est", "real", "prompt", "cuando", "falta", "bloqueo", "detalle"]
ESTADOS = ("pendiente", "en curso", "en parte", "bloqueada", "hecha")
# interno (construir_seguimiento) ↔ CSV: «recurrente» y «cubierta» se guardan como estado + tipo para no ampliar los estados fijos
A_CSV = {"hecha": ("hecha", ""), "pendiente": ("pendiente", ""), "parcial": ("en parte", ""),
         "recurrente": ("en curso", "recurrente"), "cubierta": ("hecha", "cubierta"), "otro": ("pendiente", "otro")}


def a_interno(estado, tipo):
    if tipo in ("recurrente", "cubierta", "otro"):
        return tipo
    return {"en parte": "parcial", "en curso": "pendiente", "bloqueada": "pendiente"}.get(estado, estado)


def cargar(ruta=CSV):
    """Filas del CSV con el estado interno; [] si no existe (el llamador cae a las COLA*.md)."""
    if not ruta.exists():
        return []
    out = []
    with open(ruta, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if not (r.get("id") or "").strip():
                continue
            r = {k: (r.get(k) or "").strip() for k in COLUMNAS}
            if r["cuando"].isdigit():   # Sheets publica las fechas como número de serie (días desde 1899-12-30)
                r["cuando"] = (date(1899, 12, 30) + timedelta(days=int(r["cuando"]))).isoformat()
            r["bruto"] = r["estado"]
            r["estado"] = a_interno(r["estado"].lower(), r["tipo"].lower())
            out.append(r)
    return out


def escribir(filas, ruta=CSV):
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNAS, extrasaction="ignore")
        w.writeheader()
        for r in filas:
            w.writerow({k: r.get(k, "") for k in COLUMNAS})


def migrar():
    sys.path.insert(0, str(RAIZ / "scripts"))
    import construir_seguimiento as s
    filas = []
    for t in s._cola_r_md() + s._cola_t_md() + s._cola_d_md():
        est, tipo = A_CSV.get(t["estado"], ("pendiente", "otro"))
        filas.append({**t, "estado": est, "tipo": tipo})
    escribir(filas)
    print(f"{len(filas)} tareas -> {CSV.relative_to(RAIZ)}")


def sincronizar():
    if not URL.exists():
        sys.exit("Falta research/tareas-url.txt con la URL del CSV publicado de la Sheet.")
    url = URL.read_text(encoding="utf-8").strip()
    if not url.startswith("https://docs.google.com/"):
        sys.exit("La URL debe ser de docs.google.com (Archivo -> Compartir → Publicar en la web → CSV).")
    with urllib.request.urlopen(url, timeout=30) as r:
        texto = r.read().decode("utf-8")
    cab = next(csv.reader(io.StringIO(texto)), [])
    if cab[:4] != COLUMNAS[:4]:
        sys.exit(f"Cabecera inesperada: {cab[:4]}; no se sobrescribe el CSV.")
    malos = {r["estado"] for r in csv.DictReader(io.StringIO(texto)) if r["estado"].strip().lower() not in ESTADOS}
    if malos:
        sys.exit(f"Estados fuera de la lista fija: {sorted(malos)}; no se sobrescribe el CSV.")
    CSV.write_text(texto, encoding="utf-8", newline="")
    print("CSV actualizado desde la Sheet")


if __name__ == "__main__":
    {"migrar": migrar, "sincronizar": sincronizar}.get(sys.argv[1] if len(sys.argv) > 1 else "", lambda: sys.exit(__doc__))()
