"""Genera cerebro/documentos/indice-investigacion.md: por tema, los informes más recientes con una frase de su resumen.

Sin IA, solo biblioteca estándar. Uso: python scripts/indice_investigacion.py
Tope de tamaño: 15 KB (el cerebro se lee entero en cada llamada de los bots con IA).
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CARPETAS = ["informes", "informes/research", "informes/dossiers", "informes/videos"]
SALIDA = RAIZ / "cerebro" / "documentos" / "indice-investigacion.md"
TOPE_BYTES = 15 * 1024
POR_TEMA = 3
FRASE_MAX = 150

# (tema, palabras clave en el nombre o título); el primero que coincida gana
TEMAS = [
    ("Auditorías y verificaciones", ["auditoria", "verificacion", "cruce", "contradicciones", "coherencia", "c09", "c10", "w05", "w08"]),
    ("Voces y predicciones", ["voces", "w06", "prediccion", "fuentes", "w07"]),
    ("Fiscal", ["fiscal", "renta", "irpf", "dac8", "t24", "r20"]),
    ("Energía y Ormuz", ["energia", "ormuz", "petroleo", "opep", "w10", "t18", "r46"]),
    ("Deuda y bonos", ["deuda", "bono", "subasta", "calificacion", "d0", "w02", "bancos-y-deuda"]),
    ("Macro y tipos", ["tipos", "interes", "w01", "liquidez", "m2", "t17", "macro", "defensa", "matriz-de-riesgos", "r41"]),
    ("Cripto y ETF", ["etf", "xrp", "xlm", "stellar", "ripple", "dtcc", "derivados", "dex", "custodia", "cuantico", "w04", "t19", "t20", "t21", "t22", "t23"]),
    ("Regulación por país", ["mica", "japon", "corea", "brasil", "singapur", "cbdc", "regulacion", "radar", "w03", "t0", "t1"]),
    ("Sesiones diarias (apertura y cierre)", ["apertura", "cierre", "intradia", "inicial", "revision", "resumen"]),
]
OTROS = "Otros"


def leer(p):
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def titulo(txt, nombre):
    for l in txt.splitlines():
        if l.startswith("# "):
            return l[2:].strip()[:110]
    return nombre


def frase(txt):
    """Primera frase útil del apartado «Resumen»; si no hay, del primer párrafo tras el título."""
    lineas = txt.splitlines()
    inicio = 0
    for i, l in enumerate(lineas):
        if re.match(r"^#{1,3}\s*(\d+\.\s*)?resumen", l.strip(), re.I):
            inicio = i + 1
            break
    else:
        inicio = next((i + 1 for i, l in enumerate(lineas) if l.startswith("# ")), 0)
    for l in lineas[inicio:inicio + 40]:
        t = re.sub(r"[`*_>|#-]+", " ", l).strip()
        t = re.sub(r"\s+", " ", t)
        t = re.sub(r"^\d+\.\s*", "", t)
        if len(t) > 40 and not t.lower().startswith(("coste", "sesión", "sesion", "fuente", "fecha", "base", "informativo", "hecho el", "niveles", "etiquetas", "nota")):
            return (t[:FRASE_MAX].rsplit(" ", 1)[0] + "…") if len(t) > FRASE_MAX else t
    return "(sin resumen)"


def tema(nombre, tit):
    for texto in (nombre.lower(), tit.lower()):   # primero el nombre del archivo, luego el título
        for t, claves in TEMAS:
            if any(c in texto for c in claves):
                return t
    return OTROS


def fecha(nombre):
    m = re.match(r"(\d{4}-\d{2}-\d{2})", nombre)
    return m.group(1) if m else "0000-00-00"


# (país_id, palabras clave en nombre o título) para el índice completo por país
PAISES = [
    ("US", ["eeuu", "ee-uu", "ee. uu", "genius", "clarity", "tesoro", "occ"]),
    ("EU", ["mica", "bce", "esma", "euro-digital", "euro digital", "europa"]),
    ("JP", ["japon", "japón", "boj"]), ("KR", ["corea"]), ("SG", ["singapur"]),
    ("HK", ["hong-kong", "hong kong"]), ("CN", ["china", "pboc", "yuan"]),
    ("IN", ["india"]), ("BR", ["brasil"]), ("RU", ["rusia"]), ("IR", ["iran", "irán", "ormuz"]),
    ("ES", ["españa", "espana", "irpf", "cnmv"]), ("FR", ["francia"]),
    ("GB", ["reino unido"]), ("AE", ["emiratos"]), ("INT", ["brics", "bis-", "fmi", "imf"]),
]


def paises(nombre, tit):
    texto = (nombre + " " + tit).lower()
    return [pid for pid, claves in PAISES if any(c in texto for c in claves)]


def fichas_todas():
    """Todos los informes (sin tope) con tema, países, fecha y una frase. Para explorador/indice/informes.json."""
    out = []
    for c in CARPETAS:
        d = RAIZ / c
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            txt = leer(p)
            tit = titulo(txt, p.stem)
            out.append({"ruta": p.relative_to(RAIZ).as_posix(), "fecha": fecha(p.name), "titulo": tit,
                        "tema": tema(p.stem, tit), "pais_id": paises(p.stem, tit), "frase": frase(txt)})
    return sorted(out, key=lambda x: (x["fecha"], x["ruta"]), reverse=True)


def main():
    fichas = {}
    for c in CARPETAS:
        d = RAIZ / c
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            txt = leer(p)
            tit = titulo(txt, p.stem)
            t = tema(p.stem, tit)
            fichas.setdefault(t, []).append((fecha(p.name), tit, p.relative_to(RAIZ).as_posix(), frase(txt)))
    hoy = max((f[0] for v in fichas.values() for f in v), default="")
    orden = [t for t, _ in TEMAS] + [OTROS]
    out = [
        "---", "tema: Índice de la investigación (autogenerado)",
        "etiquetas: [indice, informes, research]", f"actualizado: {hoy}", "---",
        "# Índice de la investigación", "",
        "## Resumen",
        "Mapa de los informes más recientes por tema. Lo genera `scripts/indice_investigacion.py` (sin IA); no editar a mano. "
        "Los informes completos están en `informes/`; aquí solo la ruta y una frase. Para el estado vigente mira "
        "`estado-vigente-y-correcciones.md` y `resumen-vigente-xrp.md`.", "",
        "## Explicación",
        f"Por tema, los {POR_TEMA} informes más recientes (fecha · título · ruta · una frase de su resumen).", "",
    ]
    for t in orden:
        v = sorted(fichas.get(t, []), reverse=True)[:POR_TEMA]
        if not v:
            continue
        out.append(f"## {t}")
        for f, tit, ruta, fr in v:
            out.append(f"- {f} · {tit} (`{ruta}`): {fr}")
        out.append("")
    out += ["## Dudas y datos a verificar", "Las frases son extractos sin comprobar: lo dudoso está marcado [VERIFICAR] en el informe original.", ""]
    txt = "\n".join(out)
    # recorta por el final si pasa del tope, quitando líneas de informes más antiguos
    while len(txt.encode("utf-8")) > TOPE_BYTES:
        lineas = txt.split("\n")
        idx = max(i for i, l in enumerate(lineas) if l.startswith("- 20"))
        del lineas[idx]
        txt = "\n".join(lineas)
    SALIDA.write_text(txt, encoding="utf-8")
    print(f"{SALIDA.relative_to(RAIZ)}: {len(txt.encode('utf-8'))} bytes, "
          f"{sum(min(len(v), POR_TEMA) for v in fichas.values())} informes en {len(fichas)} temas")


if __name__ == "__main__":
    main()
