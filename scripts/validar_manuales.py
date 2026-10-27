"""Valida los JSON de noticias/manuales/ (C18) y, con --lecciones, añade las lecciones de bulos y fuentes al cerebro.

Uso:
  python scripts/validar_manuales.py                 # valida todos (salvo los que empiezan por «_»)
  python scripts/validar_manuales.py ruta.json       # valida uno (también _ejemplo)
  python scripts/validar_manuales.py --lecciones     # además AÑADE líneas (máx. 5 por archivo) a
                                                     # cerebro/documentos/patrones-de-bulos.md y fuentes-fiables-y-dudosas.md
Solo añade líneas; no reescribe nada. Es idempotente (no repite una línea ya escrita). Sin API, sin red."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "noticias"))
import manuales  # noqa: E402

DOCS = RAIZ / "cerebro" / "documentos"
MAX_LINEAS = 5


def _anadir(archivo, lineas):
    ruta = DOCS / archivo
    actual = ruta.read_text(encoding="utf-8") if ruta.exists() else ""
    nuevas = [l for l in lineas if l not in actual]
    if nuevas:
        sep = "" if actual.endswith("\n") or not actual else "\n"
        ruta.write_text(actual + sep + "\n".join(nuevas) + "\n", encoding="utf-8")
    return len(nuevas)


def lecciones(datos):
    """(lineas_bulos, lineas_fuentes) de un archivo ya validado. Máx. 5 de cada."""
    dia = datos["fecha"][:10]
    bulos, fuentes, vistas = [], [], set()
    for n in datos["noticias"]:
        if n["bulo"]:
            txt = (n.get("leccion_bulo") or f"{n['titulo']} — {n['motivo_bulo']}").strip()
            bulos.append(f"- {dia} (manual · {datos['evento']}): {txt} [{n['etiqueta']}] {n['url']}")
        if n.get("fuente_nueva") and n["fuente"] not in vistas:
            vistas.add(n["fuente"])
            fuentes.append(f"- {dia} (manual · {datos['evento']}): {n['fuente']} — {n['fuente_nueva'].strip()} [{n['etiqueta']}]")
    return bulos[:MAX_LINEAS], fuentes[:MAX_LINEAS]


def main(argv):
    aplicar = "--lecciones" in argv
    rutas = [Path(a) for a in argv if not a.startswith("--")] or manuales.listar()
    if not rutas:
        print("No hay archivos en noticias/manuales/ (nada que validar).")
        return 0
    malos = 0
    for r in rutas:
        datos, errores = manuales.cargar(r)
        if errores:
            malos += 1
            print(f"✗ {r.name}")
            for e in errores:
                print(f"    - {e}")
            continue
        n = len(datos["noticias"])
        extra = ""
        if aplicar:
            b, f = lecciones(datos)
            extra = f" · lecciones nuevas: {_anadir('patrones-de-bulos.md', b)} bulos, {_anadir('fuentes-fiables-y-dudosas.md', f)} fuentes"
        print(f"✓ {r.name} · nivel {datos['nivel']} · {n} piezas" + (" (vacío: no se enviará nada)" if not n else "") + extra)
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
