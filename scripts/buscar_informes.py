"""Buscador local de informes, dossiers, vídeos y apuntes (sin IA, sin red, solo librería estándar).

Para qué: encontrar los 5-8 fragmentos relevantes en vez de releer documentos enteros (ahorra tokens).
Uso:
    python scripts/buscar_informes.py "posición del Consejo euro digital"
    python scripts/buscar_informes.py "CLARITY cierre de debate" -n 8 --ancho 500
    python scripts/buscar_informes.py "RLUSD XRPL" --carpeta informes/research
Cada resultado: archivo:línea · sección · puntuación, con el fragmento. Lee el archivo solo desde esa línea si hace falta más.
Por defecto NO indexa privado/ (usa --privado solo en local y para ti)."""
import argparse
import math
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CARPETAS = ["informes", "cerebro", "research", "G"]          # las que no existan se ignoran
EXCLUIR = ("graphify-out", "node_modules", ".git", "__pycache__", "pdf")
PARADAS = set("""de la el en y a los las un una unos unas que se del por con para al lo es son su sus no si como mas pero o u e ni
ha han fue ser sido este esta estos estas ese esa eso entre sobre sin muy ya tambien segun desde hasta cuando donde cual quien
the of and to in is for on with by at from as an or""".split())
MAX_CHARS = 900          # tamaño máximo de un fragmento
VENTANA = 6              # líneas que se muestran alrededor de la mejor coincidencia


def plano(texto):
    t = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def tokens(texto):
    return [w for w in re.findall(r"[a-z0-9][a-z0-9\-\.]*[a-z0-9]|[a-z0-9]", plano(texto)) if w not in PARADAS and len(w) > 1]


def archivos(carpetas, privado):
    lista = list(carpetas) + (["privado"] if privado else [])
    for c in lista:
        base = Path(c) if Path(c).is_absolute() else RAIZ / c
        if base.is_file() and base.suffix == ".md":
            yield base
        elif base.is_dir():
            for p in sorted(base.rglob("*.md")):
                if not any(x in p.parts for x in EXCLUIR):
                    yield p


def trocear(ruta):
    """Divide el archivo en fragmentos por secciones (títulos #) y, si son largas, por bloques de líneas."""
    try:
        lineas = ruta.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []
    out, titulo, ini, buf, n = [], ruta.stem, 1, [], 0
    for i, ln in enumerate(lineas, 1):
        if ln.startswith("#"):
            if buf:
                out.append((ini, titulo, buf))
            titulo, ini, buf, n = ln.lstrip("# ").strip()[:90], i, [], 0
        buf.append(ln)
        n += len(ln)
        if n > MAX_CHARS * 1.5:
            out.append((ini, titulo, buf))
            ini, buf, n = i + 1, [], 0
    if buf:
        out.append((ini, titulo, buf))
    return [(ruta, ini, tit, b) for ini, tit, b in out if any(x.strip() for x in b)]


class Indice:
    def __init__(self, rutas):
        self.docs = []        # (ruta, línea, título, líneas)
        self.tf = []
        self.df = Counter()
        for r in rutas:
            for d in trocear(r):
                self.docs.append(d)
                c = Counter(tokens(" ".join(d[3])))
                c.update({t: 3 for t in tokens(d[2])})       # el título pesa más
                c.update({t: 2 for t in tokens(d[0].stem)})  # y el nombre del archivo
                self.tf.append(c)
                self.df.update(c.keys())
        self.largo = [sum(c.values()) for c in self.tf]
        self.medio = (sum(self.largo) / len(self.largo)) if self.largo else 1

    def buscar(self, consulta, n):
        q = tokens(consulta)
        if not q:
            return []
        N = len(self.docs)
        k1, b = 1.5, 0.75
        frase = plano(consulta).strip()
        res = []
        for i, c in enumerate(self.tf):
            s = 0.0
            for t in set(q):
                f = c.get(t, 0)
                if not f:
                    continue
                idf = math.log(1 + (N - self.df[t] + 0.5) / (self.df[t] + 0.5))
                s += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * self.largo[i] / self.medio))
            if s and len(q) > 1 and frase in plano(" ".join(self.docs[i][3])):
                s *= 1.5                                    # la frase exacta suma
            if s:
                res.append((s, i))
        res.sort(reverse=True)
        return res[:n]

    def fragmento(self, i, q, ancho):
        ruta, ini, titulo, lineas = self.docs[i]
        qs = set(tokens(q))
        punt = [sum(1 for t in tokens(ln) if t in qs) for ln in lineas]
        mejor = max(range(len(lineas)), key=lambda j: punt[j]) if lineas else 0
        a = max(0, mejor - VENTANA // 3)
        txt = " ".join(x.strip() for x in lineas[a:a + VENTANA] if x.strip())
        if len(txt) > ancho:
            txt = txt[:ancho].rsplit(" ", 1)[0] + "…"
        return ruta, ini + a, titulo, txt


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("consulta")
    ap.add_argument("-n", type=int, default=6, help="número de resultados (6 por defecto)")
    ap.add_argument("--ancho", type=int, default=420, help="caracteres máximos por fragmento")
    ap.add_argument("--carpeta", action="append", help="carpeta o archivo a indexar (se puede repetir); por defecto informes, cerebro y research")
    ap.add_argument("--privado", action="store_true", help="incluye privado/ (solo en tu PC)")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    idx = Indice(archivos(a.carpeta or CARPETAS, a.privado))
    if not idx.docs:
        print("No hay documentos que indexar.")
        return 1
    res = idx.buscar(a.consulta, a.n)
    if not res:
        print("Sin resultados. Prueba con menos palabras o con sinónimos.")
        return 0
    print(f"{len(res)} resultado(s) de {len(idx.docs)} fragmentos indexados:\n")
    for s, i in res:
        ruta, linea, titulo, txt = idx.fragmento(i, a.consulta, a.ancho)
        try:
            rel = ruta.relative_to(RAIZ)
        except ValueError:
            rel = ruta
        print(f"{str(rel).replace(chr(92), '/')}:{linea} · {titulo} · {s:.1f}\n  {txt}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
