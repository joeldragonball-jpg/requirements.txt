"""Huellas de privado/ (C205): trozos de texto que SOLO existen en la tesis privada de Joel.

Sirven para comprobar que ninguna página pública (docs/, la Órbita) la incluye por error.
- No imprime ni guarda las huellas: solo dice si aparecen y dónde.
- En GitHub Actions privado/ no existe: entonces no hay huellas y la comprobación pasa (allí no hay nada que filtrar).
Uso: python scripts/huellas_privado.py   -> revisa docs/ y sale con código 1 si encuentra alguna."""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PRIVADO = RAIZ / "privado"
MIN = 60                                   # longitud de cada huella: larga para no dar falsos positivos
# Marca que lleva escrita la vista privada de la tesis (construir_tesis_privada.py): si aparece, se ha copiado la página.
# (Los NOMBRES de archivo de privado/ sí pueden salir en público, p. ej. en las tareas: no revelan la tesis.)
RUTAS = ("marca-tesis-privada-c205",)


def _norm(t):
    return re.sub(r"\s+", " ", str(t or "")).strip().lower()


def _cargar(nombre):
    try:
        return json.loads((PRIVADO / nombre).read_text(encoding="utf-8"))
    except Exception:
        return {}


def huellas():
    """Trozos de las conclusiones privadas (no de la evidencia pública, que sí puede salir en el Explorador)."""
    textos = []
    c = _cargar("contraste-tesis.json")
    puntos = list(c.get("generales", [])) + [p for v in (c.get("capas") or {}).values() for p in v]
    for p in puntos:
        textos.append(p.get("razonamiento"))      # «abierto» no: son preguntas genéricas que también salen en público
    textos.append(c.get("aviso"))
    v = _cargar("voces-tesis.json")
    textos.append(v.get("aviso"))
    textos += [h.get("desc") for h in v.get("hipotesis", [])]
    textos += [x.get("texto") for x in v.get("lecturas", [])]
    textos += [x.get("nota") for x in v.get("pruebas", [])]
    # Marco ISO 20022 y tokenización (14-nov-2026): solo las conclusiones razonadas, no los hechos públicos que cita
    mk = _cargar("marco-iso20022.json")
    textos.append(mk.get("aviso"))
    textos += [(c.get("captura") or {}).get("razon") for c in mk.get("cadenas", [])]
    textos += [x.get("razon") for x in mk.get("complementariedad", [])]
    textos += [a.get("detalle") for a in mk.get("afirmaciones", [])]
    out = set()
    for t in textos:
        t = _norm(t)
        if len(t) >= MIN:
            out.add(t[:MIN])
    return sorted(out)


def buscar(texto, hs=None):
    """Devuelve cuántas huellas (y rutas privadas) aparecen en el texto. 0 = limpio."""
    hs = huellas() if hs is None else hs
    t = _norm(texto)
    return sum(1 for h in hs if h in t) + sum(1 for r in RUTAS if r in t)


def revisar_docs():
    """Lista [(archivo, n)] de páginas publicadas en docs/ que contienen huellas privadas."""
    hs = huellas()
    malos = []
    for f in sorted((RAIZ / "docs").rglob("*")):
        if f.suffix.lower() not in (".html", ".json", ".md", ".js", ".txt") or not f.is_file():
            continue
        try:
            n = buscar(f.read_text(encoding="utf-8", errors="ignore"), hs)
        except Exception:
            continue
        if n:
            malos.append((f.relative_to(RAIZ).as_posix(), n))
    return malos


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    hs = huellas()
    malos = revisar_docs()
    print(f"Huellas privadas cargadas: {len(hs)} (no se muestran).")
    for f, n in malos:
        print(f"  ⚠ {f}: {n} huella(s) de privado/")
    print("docs/ limpio." if not malos else "Hay contenido privado en docs/: NO subir.")
    sys.exit(1 if malos else 0)
