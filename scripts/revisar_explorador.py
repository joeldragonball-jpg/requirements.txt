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


RAIZ = RUTA.parent.parent


def comprobar_informe(donde, x):
    """El campo opcional «informe» debe ser una ruta dentro de informes/ de un .md que exista."""
    if "informe" not in x:
        return
    r = x["informe"]
    if not isinstance(r, str) or not r.startswith("informes/") or not r.endswith(".md") or ".." in r:
        aviso(donde, f"«informe» no es una ruta válida dentro de informes/: {r!r}")
    elif not (RAIZ / r).is_file():
        aviso(donde, f"«informe» apunta a un archivo que no existe: {r}")


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
    fi = c.get("ficha")
    if not fi:
        aviso(c["id"], "sin ficha del analista")
    else:
        for k in ("hace", "controla", "falta", "madurez", "favor", "contra", "vigilar", "informes"):
            if not fi.get(k):
                aviso(f"{c['id']}.ficha", f"falta «{k}»")
        if fi.get("madurez", {}).get("n") not in (1, 2, 3, 4, 5):
            aviso(f"{c['id']}.ficha", "madurez fuera de la escala 1-5")
        for k in ("falta", "favor", "contra", "vigilar"):
            for t in fi.get(k, []):
                if not empieza_bien(t):
                    aviso(f"{c['id']}.ficha.{k}", f"no empieza con mayúscula: «{t[:40]}»")
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
    comprobar_informe(dn, m)

for c in d["capas"]:
    for k in ("produccion", "piloto", "plan", "xrp"):
        if isinstance(c.get(k), list):
            for hecho in c[k]:
                comprobar_informe(f"{c['id']}.{k}", hecho)


# --- Radar regulatorio (explorador/regulacion.json) ---
RUTA_REG = RUTA.parent / "regulacion.json"
FECHA_REG = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")


def fecha_ok(f):
    """Acepta AAAA, AAAA-MM o AAAA-MM-DD (precisión según la fuente)."""
    if not isinstance(f, str) or not FECHA_REG.match(f):
        return False
    partes = [int(x) for x in f.split("-")] + [1, 1]
    try:
        date(partes[0], partes[1], partes[2])
    except ValueError:
        return False
    return True


sin_dato = 0
if RUTA_REG.exists():
    r = json.loads(RUTA_REG.read_text(encoding="utf-8"))
    jur_ids = {j["id"] for j in r.get("jurisdicciones", [])}
    tema_ids = {t["id"] for t in r.get("temas", [])}
    vistas = set()
    for cel in r.get("celdas", []):
        dn = f"regulacion {cel.get('jur')}.{cel.get('tema')}"
        for k in ("jur", "tema", "etapa", "estado", "fecha", "fuente", "proxima", "falta", "hitos", "informes"):
            if k not in cel:
                aviso(dn, f"falta el campo «{k}»")
        if cel.get("jur") not in jur_ids:
            aviso(dn, "jurisdicción desconocida")
        if cel.get("tema") not in tema_ids:
            aviso(dn, "tema desconocido")
        clave = (cel.get("jur"), cel.get("tema"))
        if clave in vistas:
            aviso(dn, "celda repetida")
        vistas.add(clave)
        etapa = cel.get("etapa")
        if cel.get("tema") == "politica" and etapa is None and cel.get("dir") is not None:
            # La política monetaria no usa etapa: usa dirección (sube, mantiene, baja, n/d)
            if cel["dir"] not in r.get("escala_politica", {}):
                aviso(dn, f"dirección no válida: {cel['dir']}")
            if not fecha_ok(cel.get("fecha")):
                aviso(dn, f"fecha del último cambio no válida: {cel.get('fecha')}")
            if not cel.get("informes"):
                aviso(dn, "sin informes de origen")
            if not cel.get("valor"):
                aviso(dn, "sin valor (nivel de tipos u otro dato)")
        elif etapa is None:
            sin_dato += 1
            if cel.get("fuente") == "VERIFICAR" and cel.get("fecha") is not None:
                aviso(dn, "celda sin dato con fecha")
        else:
            if etapa not in (0, 1, 2, 3, 4, 5):
                aviso(dn, f"etapa fuera de la escala 0-5: {etapa}")
            if not fecha_ok(cel.get("fecha")):
                aviso(dn, f"fecha del último cambio no válida: {cel.get('fecha')}")
            if not cel.get("informes"):
                aviso(dn, "sin informes de origen")
        if cel.get("fecha") is not None and not fecha_ok(cel["fecha"]):
            aviso(dn, f"fecha no válida: {cel['fecha']}")
        if etapa is not None or cel.get("dir") is not None:
            # Celda con dato: debe llevar la fecha de la última comprobación (AAAA-MM-DD completa)
            rev = cel.get("revisado")
            if not isinstance(rev, str) or not re.match(r"^\d{4}-\d{2}-\d{2}$", rev) or not fecha_ok(rev):
                aviso(dn, f"campo «revisado» ausente o no válido (AAAA-MM-DD): {rev}")
            elif rev > date.today().isoformat():
                aviso(dn, f"«revisado» en el futuro: {rev}")
        if cel.get("fuente") not in ("P", "S", "VERIFICAR"):
            aviso(dn, f"fuente no válida: {cel.get('fuente')}")
        for k in ("estado", "falta"):
            t = cel.get(k) or ""
            if not t:
                aviso(dn, f"«{k}» vacío")
            elif not empieza_bien(t):
                aviso(dn, f"«{k}» no empieza con mayúscula: «{t[:40]}»")
            elif not t.endswith("."):
                aviso(dn, f"«{k}» no acaba en punto: «{t[:40]}»")
        prox = cel.get("proxima")
        if prox is not None:
            if not fecha_ok(prox.get("fecha")):
                aviso(dn, f"próxima fecha no válida: {prox.get('fecha')}")
            if not prox.get("que") or not empieza_bien(prox["que"]):
                aviso(dn, "próxima fecha sin descripción con mayúscula")
        for h in cel.get("hitos", []):
            if not fecha_ok(h.get("fecha")):
                aviso(dn, f"hito con fecha no válida: {h.get('fecha')}")
            if not h.get("que") or not empieza_bien(h["que"]) or not h["que"].endswith("."):
                aviso(dn, f"hito sin texto completo: «{(h.get('que') or '')[:40]}»")
    for j in jur_ids:
        for t in tema_ids:
            if (j, t) not in vistas:
                aviso(f"regulacion {j}.{t}", "falta la celda")
else:
    aviso("regulacion", "no existe explorador/regulacion.json")

# ---- Voces (explorador/voces.json) y cruce privado con la tesis (privado/voces-tesis.json, solo local)
RUTA_VOC = RUTA.parent / "voces.json"
RUTA_TES = RUTA.parent.parent / "privado" / "voces-tesis.json"
n_voces = 0
if RUTA_VOC.exists():
    vz = json.loads(RUTA_VOC.read_text(encoding="utf-8"))
    niveles, confs = set(vz["niveles"]), set(vz["confirmaciones"])
    vistos, ids_voz = set(), set()
    for v in vz["voces"]:
        n_voces += 1
        dv = f"voz {v.get('id', '?')}"
        if v.get("id") in vistos:
            aviso(dv, "id repetido")
        vistos.add(v.get("id")); ids_voz.add(v.get("id"))
        if v.get("nivel") not in niveles:
            aviso(dv, f"nivel desconocido: {v.get('nivel')}")
        if v.get("conf") not in confs:
            aviso(dv, f"confirmación desconocida: {v.get('conf')}")
        if not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(v.get("cuando", ""))):
            aviso(dv, f"fecha no válida: {v.get('cuando')}")
        for k in v.get("capas", []):
            if k not in ids:
                aviso(dv, f"capa inexistente: {k}")
        if not v.get("capas"):
            aviso(dv, "sin capa")
        if not v.get("texto") or not empieza_bien(v["texto"]) or not v["texto"].rstrip().endswith((".", "»", ")")):
            aviso(dv, f"texto sin mayúscula inicial o sin punto final: «{(v.get('texto') or '')[:40]}»")
        url = (v.get("fuente") or {}).get("url", "")
        if v.get("nivel") in ("P", "D") and not url:
            aviso(dv, "nivel P o D sin enlace a la fuente (una declaración localizada necesita saber dónde se localizó)")
        if url and not url.startswith("https://"):
            aviso(dv, f"el enlace de la fuente no es https: {url[:40]}")
        if v.get("nivel") == "P" and v.get("conf") in ("sin_confirmar", "contradicha"):
            aviso(dv, "un hecho de fuente primaria no puede estar «sin confirmar» o «contradicha»")
        if v.get("nivel") in ("E", "C") and v.get("conf") == "confirmada":
            aviso(dv, "una especulación o una afirmación del canal no puede constar como «confirmada»")
        pz = v.get("plazo")
        if pz:
            for k in ("dicho", "prometido"):
                if k in pz and not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(pz[k])):
                    aviso(dv, f"plazo con {k} no válido: {pz[k]}")
            if pz.get("estado") not in ("cumplido", "pendiente", "incumplido", "retrasado", "distinto"):
                aviso(dv, f"estado de plazo desconocido: {pz.get('estado')}")
            if pz.get("dicho") and pz.get("prometido") and str(pz["dicho"]) > str(pz["prometido"]):
                aviso(dv, "plazo: «dicho» es posterior a «prometido»")
        vid = v.get("video")
        if vid and vid.get("url") and not vid["url"].startswith("https://"):
            aviso(dv, "enlace de vídeo no https")
    # misma persona o institución con la misma cifra en dos declaraciones distintas: aviso de posible duplicado
    por_texto = {}
    for v in vz["voces"]:
        clave = (v["quien"].split(" (")[0], v["cuando"], tuple(sorted(v.get("capas", []))))
        por_texto.setdefault(clave, []).append(v["id"])
    for clave, lst in por_texto.items():
        if len(lst) > 1:
            aviso("voces", f"posible duplicado ({clave[0]}, {clave[1]}): {', '.join(lst)}")
    if RUTA_TES.exists():
        vt = json.loads(RUTA_TES.read_text(encoding="utf-8"))
        hids = {h["id"] for h in vt["hipotesis"]}
        for p in vt["pruebas"]:
            for h in hids:
                if p["celdas"].get(h) not in ("C", "I", "N"):
                    aviso(f"tesis prueba {p['id']}", f"celda de {h} sin valor C/I/N")
            for idv in p["voces"]:
                if idv not in ids_voz:
                    aviso(f"tesis prueba {p['id']}", f"voz inexistente: {idv}")
        for k, pr in vt["premisas"].items():
            for rol_ in pr["roles"]:
                if rol_["voz"] not in ids_voz:
                    aviso(f"tesis premisa {k}", f"voz inexistente: {rol_['voz']}")
                if rol_["rol"] not in ("apoya", "contradice", "matiza"):
                    aviso(f"tesis premisa {k}", f"rol desconocido: {rol_['rol']}")
else:
    aviso("voces", "no existe explorador/voces.json")

print("\n".join(avisos) if avisos else "Sin avisos.")
print(f"\n{len(avisos)} aviso(s) en {len(d['capas'])} capas y {len(d['movimientos'])} movimientos.")
if RUTA_REG.exists():
    print(f"Radar regulatorio: {len(r.get('celdas', []))} celdas, {sin_dato} sin dato (etapa null, no cuentan como aviso).")
sys.exit(1 if avisos else 0)
