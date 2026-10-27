"""Noticias manuales (C18): formato, validación y lectura. Python normal: NO usa la API de Anthropic.

Cada archivo `noticias/manuales/AAAA-MM-DD-<slug>.json` es el resultado de un research hecho a mano (con la cuota de
Claude o de Gemini). El bot (noticias.py) y scripts/validar_manuales.py usan este mismo módulo.
Los archivos cuyo nombre empieza por «_» (ejemplos) se ignoran.
"""
import json
import re
import tomllib
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).parent
CARPETA = AQUI / "manuales"
NOMBRE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*\.json$")
NIVELES = {"evento", "ligera"}
ETIQUETAS = {"P", "S", "VERIFICAR"}
MAX_POR_NIVEL = {"evento": 25, "ligera": 8}
NOTA_MIN_LIGERA = 7          # en el nivel «ligera» solo entran piezas con nota >= 7
OBLIGATORIAS = ("titulo", "fuente", "url", "fecha", "resumen", "etiqueta", "tema", "nota", "fiabilidad", "bulo")


def temas_validos():
    cfg = tomllib.loads((AQUI / "config.toml").read_text(encoding="utf-8"))
    return list(cfg["temas"])


def _fecha_ok(valor):
    try:
        datetime.fromisoformat(str(valor).replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def validar(datos, nombre="", temas=None):
    """Devuelve la lista de errores (vacía = válido). Formato:
    {"evento": "FOMC 28-oct", "fecha": "2026-10-28", "nivel": "evento"|"ligera", "generado_con": "Claude|Gemini",
     "noticias": [{titulo, fuente, url, fecha, resumen, etiqueta P|S|VERIFICAR, tema, nota 1-10, fiabilidad,
                   bulo true|false, motivo_bulo (obligatorio si bulo), leccion_bulo?, fuente_nueva?}]}
    «noticias» puede ir vacía (tanda sin nada con nota >= 7): no se envía nada."""
    temas = temas or temas_validos()
    e = []
    if nombre and not nombre.startswith("_") and not NOMBRE.match(nombre):
        e.append(f"nombre de archivo «{nombre}»: debe ser AAAA-MM-DD-slug.json (minúsculas, guiones)")
    if not isinstance(datos, dict):
        return e + ["la raíz debe ser un objeto JSON"]
    if not isinstance(datos.get("evento"), str) or not datos["evento"].strip():
        e.append("falta «evento» (texto)")
    if not _fecha_ok(datos.get("fecha")):
        e.append("«fecha» no es una fecha ISO (AAAA-MM-DD)")
    nivel = datos.get("nivel")
    if nivel not in NIVELES:
        e.append(f"«nivel» debe ser uno de {sorted(NIVELES)}")
    lista = datos.get("noticias")
    if not isinstance(lista, list):
        return e + ["«noticias» debe ser una lista (puede estar vacía)"]
    if nivel in MAX_POR_NIVEL and len(lista) > MAX_POR_NIVEL[nivel]:
        e.append(f"nivel {nivel}: máximo {MAX_POR_NIVEL[nivel]} piezas (hay {len(lista)})")
    urls = set()
    for i, n in enumerate(lista, 1):
        p = f"noticia {i}"
        if not isinstance(n, dict):
            e.append(f"{p}: debe ser un objeto")
            continue
        for k in OBLIGATORIAS:
            if k not in n or n[k] in ("", None):
                e.append(f"{p}: falta «{k}»")
        if n.get("etiqueta") not in ETIQUETAS:
            e.append(f"{p}: «etiqueta» debe ser P, S o VERIFICAR")
        if n.get("tema") not in temas:
            e.append(f"{p}: «tema» no está en config.toml ({n.get('tema')!r})")
        if not isinstance(n.get("nota"), int) or isinstance(n.get("nota"), bool) or not 1 <= n["nota"] <= 10:
            e.append(f"{p}: «nota» debe ser un entero de 1 a 10")
        elif nivel == "ligera" and n["nota"] < NOTA_MIN_LIGERA:
            e.append(f"{p}: nivel ligera solo admite nota >= {NOTA_MIN_LIGERA}")
        if not isinstance(n.get("bulo"), bool):
            e.append(f"{p}: «bulo» debe ser true o false")
        elif n["bulo"] and not str(n.get("motivo_bulo", "")).strip():
            e.append(f"{p}: bulo=true exige «motivo_bulo»")
        if not str(n.get("url", "")).startswith(("http://", "https://")):
            e.append(f"{p}: «url» debe empezar por http(s)://")
        elif n["url"] in urls:
            e.append(f"{p}: url repetida dentro del archivo")
        else:
            urls.add(n["url"])
        if "fecha" in n and not _fecha_ok(n["fecha"]):
            e.append(f"{p}: «fecha» no es ISO")
        if len(str(n.get("resumen", ""))) > 600:
            e.append(f"{p}: «resumen» demasiado largo (1-2 frases, máx. 600 caracteres)")
    return e


def listar():
    """Archivos manuales a procesar (sin los que empiezan por «_»), en orden de fecha."""
    return sorted(p for p in CARPETA.glob("*.json") if not p.name.startswith("_")) if CARPETA.exists() else []


def cargar(ruta):
    """(datos, errores). Un JSON roto o inválido no debe tumbar el bot: se informa y se salta."""
    try:
        datos = json.loads(Path(ruta).read_text(encoding="utf-8"))
    except (OSError, ValueError) as ex:
        return None, [f"no se pudo leer: {ex}"]
    errores = validar(datos, Path(ruta).name)
    return (None if errores else datos), errores
