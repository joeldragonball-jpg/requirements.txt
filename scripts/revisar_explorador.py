"""Revisión de calidad de explorador/datos.json (sin IA, sin red).
Uso: python scripts/revisar_explorador.py   -> lista los avisos; código de salida 1 si hay alguno."""
import json
import re
import sys
from datetime import date
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "explorador" / "datos.json"
d = json.loads(RUTA.read_text(encoding="utf-8"))
avisos = []


def aviso(donde, msg):
    avisos.append(f"{donde}: {msg}")


def empieza_bien(t):
    primero = next((c for c in t if c.isalpha() or c.isdigit()), "")
    return not primero.isalpha() or primero.isupper() or bool(re.match(r"[a-z][A-Z]", t.lstrip("≈ ")))


ids = {c["id"] for c in d["capas"]}
for c in d["capas"]:
    for k in ("produccion", "piloto", "plan", "xrp"):
        v = c.get(k)
        if isinstance(v, str):
            aviso(f"{c['id']}.{k}", "sigue siendo un bloque de texto (debería ser una lista de hechos)")
            continue
        for h in v:
            dn = f"{c['id']}.{k}"
            if not empieza_bien(h["t"]):
                aviso(dn, f"no empieza con mayúscula: «{h['t'][:50]}»")
            if not h["t"].endswith("."):
                aviso(dn, f"no acaba en punto: «{h['t'][:50]}»")
            if h.get("k") == "VER":
                aviso(dn, f"pendiente de verificar: «{h['t'][:60]}»")
            if k != "xrp" and not h.get("k"):
                aviso(dn, f"sin etiqueta de fuente [P]/[S]: «{h['t'][:50]}»")
    if len(c["claves"]) < 8:
        aviso(c["id"], f"pocas palabras clave ({len(c['claves'])}); mejora el enlace con documentos y glosario")
    for x in c["cifras"]:
        if not empieza_bien(x["e"]):
            aviso(f"{c['id']}.cifras", f"descripción sin mayúscula: «{x['e'][:40]}»")
        if not x.get("f"):
            aviso(f"{c['id']}.cifras", f"cifra sin fuente: «{x['v']}»")
for m in d["movimientos"]:
    dn = f"movimiento {m['fecha']} {m['actor'][:20]}"
    try:
        date.fromisoformat(m["fecha"])
    except ValueError:
        aviso(dn, "fecha no válida")
    if m["capa"] not in ids:
        aviso(dn, f"capa desconocida: {m['capa']}")
    if m["estado"] not in d["estados"]:
        aviso(dn, f"estado desconocido: {m['estado']}")
    if not m.get("fuente") or m["fuente"].startswith("["):
        aviso(dn, "sin nombre de fuente (solo la etiqueta [P]/[S])")
    if not (m.get("ent") or m.get("act") or m.get("pais")):
        aviso(dn, "sin etiquetas de entidad, activo ni país")
    if not empieza_bien(m["texto"]):
        aviso(dn, "el texto no empieza con mayúscula")

print("\n".join(avisos) if avisos else "Sin avisos.")
print(f"\n{len(avisos)} aviso(s) en {len(d['capas'])} capas y {len(d['movimientos'])} movimientos.")
sys.exit(1 if avisos else 0)
