"""Cola de caducidad de los [VERIFICAR] de cerebro/ (C93). Sin IA y sin tocar ningún archivo existente: solo escribe
research/cola-verificar.md. Fecha de cada marca = fecha del nombre del archivo (AAAA-MM-DD o semana AAAA-Wnn); sin ella, la de la última edición de la línea (git blame). Prioridad: alta si lleva > 30 días, media 14-30, baja el resto; las marcas sin fecha van aparte para fecharlas.
Uso: python scripts/caducidad_verificar.py"""
import re
import subprocess
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def fecha_archivo(nombre):
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", nombre)
    if m:
        try:
            return date(int(m[1]), int(m[2]), int(m[3]))
        except ValueError:
            return None
    m = re.search(r"(\d{4})-W(\d{2})", nombre)
    if m:
        try:
            return date.fromisocalendar(int(m[1]), int(m[2]), 7)   # domingo: cierre de la semana
        except ValueError:
            return None
    return None


def fechas_blame(ruta):
    """Fecha de la última edición de cada línea (git blame); {} si git no puede (archivo sin commitear)."""
    try:
        out = subprocess.run(["git", "blame", "--line-porcelain", "--", ruta.as_posix()], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60).stdout
    except Exception:
        return {}
    res, n = {}, 0
    for l in out.splitlines():
        if re.match(r"[0-9a-f]{40} \d+ (\d+)", l):
            n = int(l.split()[2])
        elif l.startswith("author-time "):
            res[n] = date.fromtimestamp(int(l.split()[1]))
    return res


def main():
    hoy = date.today()
    filas, vistos = [], set()
    for ruta in sorted((RAIZ / "cerebro").rglob("*.md")):
        f0 = fecha_archivo(ruta.name)
        blame = None
        for n, linea in enumerate(ruta.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if "[VERIFICAR" not in linea:
                continue
            f = f0
            if not f:
                if blame is None:
                    blame = fechas_blame(ruta.relative_to(RAIZ))
                f = blame.get(n)
            texto = re.sub(r"\s+", " ", re.sub(r"[*_`#>-]+", " ", linea)).strip()
            clave = re.sub(r"\W+", "", texto.lower())[:90]
            if clave in vistos:       # misma marca repetida en varios archivos: se cuenta una vez, con el primero
                continue
            vistos.add(clave)
            filas.append((f, ruta.relative_to(RAIZ).as_posix(), n, texto[:170]))
    con = [x for x in filas if x[0]]
    sin = [x for x in filas if not x[0]]
    edad = lambda f: (hoy - f).days
    cub = Counter("alta (>30 d)" if edad(x[0]) > 30 else "media (14-30 d)" if edad(x[0]) >= 14 else "baja (<14 d)" for x in con)
    con.sort(key=lambda x: x[0])
    L = [f"# Cola de caducidad de [VERIFICAR] (autogenerado {hoy.isoformat()}, no editar a mano)", "",
         "Lo regenera `python scripts/caducidad_verificar.py`. Solo mira `cerebro/` (las marcas únicas, sin repetidas); en `informes/` hay muchas más. "
         "La fecha de las marcas sin fecha en el nombre es la de la última edición de la línea (git blame): puede ser posterior a la apertura real. No cierra ninguna marca: eso lo hace W05 o W08 con fuente primaria.", "",
         f"- Marcas únicas: **{len(filas)}** · con fecha {len(con)} · sin fecha en el nombre {len(sin)}",
         f"- Por prioridad: " + ", ".join(f"{k} {v}" for k, v in sorted(cub.items())), "",
         "## Las 40 más antiguas (revisar primero)", "", "| Fecha | Días | Dónde | Texto |", "|---|---|---|---|"]
    for f, r, n, t in con[:40]:
        L.append(f"| {f.isoformat()} | {edad(f)} | `{r}:{n}` | {t.replace('|', '/')} |")
    L += ["", f"## Sin fecha en el nombre ({len(sin)}): fechar primero", ""]
    for f, r, n, t in sin[:25]:
        L.append(f"- `{r}:{n}` · {t.replace('|', '/')}")
    (RAIZ / "research" / "cola-verificar.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"cola-verificar.md: {len(filas)} marcas únicas ({len(con)} con fecha, {len(sin)} sin) · {dict(cub)}")


if __name__ == "__main__":
    sys.exit(main())
