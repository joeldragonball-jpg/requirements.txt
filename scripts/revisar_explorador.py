"""Revisión de calidad de explorador/datos.json (sin IA, sin red).
Uso: python scripts/revisar_explorador.py   -> lista los avisos; código de salida 1 si hay alguno."""
import json
import re
import sys
from datetime import date
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "explorador" / "datos.json"
RAIZ_PRIV = RUTA.parent.parent          # raíz del repo (para las comprobaciones de privado/ del final)
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
        if v.get("tipo", "declaracion") not in vz.get("tipos", {"declaracion": 0}):
            aviso(dv, f"tipo desconocido: {v.get('tipo')}")
        if v.get("tipo") == "vigilar" and not (v.get("vigilar") and v.get("revisar_en")):
            aviso(dv, "una voz «a vigilar» necesita vigilar{confirma, refuta} y revisar_en")
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
        if url and not url.startswith(("https://", "http://")):
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
        if vid and vid.get("url") and not vid["url"].startswith(("https://", "http://")):
            aviso(dv, "enlace de vídeo no https")
    # misma persona o institución con la misma cifra en dos declaraciones distintas: aviso de posible duplicado
    por_texto = {}
    for v in vz["voces"]:
        if v.get("tipo", "declaracion") != "declaracion":
            continue  # tesis, datos y vigilar de un mismo vídeo comparten quien y fecha a propósito
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

# ---- Esquema común (C43): campos opcionales nuevos; solo se comprueba su forma si existen
ISO2 = re.compile(r"^[A-Z]{2,3}$")


def comprobar_comun(donde, x):
    pid = x.get("pais_id")
    if pid is not None:
        for p in ([pid] if isinstance(pid, str) else pid if isinstance(pid, list) else [None]):
            if not isinstance(p, str) or not ISO2.match(p):
                aviso(donde, f"«pais_id» no es un código de país en mayúsculas: {p!r}")
    if "nivel" in x and x["nivel"] not in ("P", "S", "V"):
        aviso(donde, f"«nivel» debe ser P, S o V: {x['nivel']!r}")
    for k in ("fecha", "caduca"):
        if k in x and x[k] is not None and not fecha_ok(x[k]):
            aviso(donde, f"«{k}» no es una fecha válida: {x[k]!r}")
    if "revisar" in x and not isinstance(x["revisar"], bool):
        aviso(donde, "«revisar» debe ser verdadero o falso")
    if "url" in x and x["url"] is not None and not str(x["url"]).startswith(("https://", "http://")):
        aviso(donde, f"«url» debe empezar por http:// o https://: {x['url']!r}")
    for k in ("sesgo", "perspectivas"):
        if k in x and not isinstance(x[k], (str, list)):
            aviso(donde, f"«{k}» debe ser texto o lista")


for m in d["movimientos"]:
    comprobar_comun(f"movimiento {m.get('fecha')} {m.get('actor')}", m)
for c in d["capas"]:
    for k, v in c.items():
        if isinstance(v, list):
            for e in v:
                if isinstance(e, dict):
                    comprobar_comun(f"{c['id']}.{k}", e)
if RUTA_REG.exists():
    for j in r.get("jurisdicciones", []):
        comprobar_comun(f"regulacion jurisdicción {j['id']}", j)
    for cel in r.get("celdas", []):
        comprobar_comun(f"regulacion {cel.get('jur')}.{cel.get('tema')}", cel)

# C265: España › Recaudación (explorador/espana-recaudacion.json, generado por scripts/espana_recaudacion.py): sumas, huecos y coherencia con el manual
RUTA_REC = RUTA.parent / "espana-recaudacion.json"
if RUTA_REC.exists():
    rc = json.loads(RUTA_REC.read_text(encoding="utf-8"))
    if not fecha_ok(rc.get("leido")):
        aviso("recaudación", "falta la fecha «leido» o no es válida")
    figs = ("irpf", "is", "iva", "iiee", "resto")
    for f in rc.get("anual", []):
        dn = f"recaudación {f.get('anio')}"
        if any(not isinstance(f.get(k), (int, float)) for k in figs + ("total", "devoluciones", "bruto")):
            aviso(dn, "falta alguna cifra (figura, total, devoluciones o bruto)")
            continue
        if abs(sum(f[k] for k in figs) - f["total"]) > 2:
            aviso(dn, f"las figuras suman {sum(f[k] for k in figs)} y el total dice {f['total']} (M€)")
        if abs(f["total"] + f["devoluciones"] - f["bruto"]) > 1:
            aviso(dn, "bruto ≠ neto + devoluciones")
        if not str(f.get("fuente", "")).startswith("https://") or f.get("nivel") != "P":
            aviso(dn, "falta la fuente (https) o el nivel P")
    ac = rc.get("acumulado_2026", {}).get("filas", [])
    tot = [x for x in ac if x.get("figura") == "total"]
    if len(ac) != 6 or not tot:
        aviso("recaudación acumulado", "debe tener 5 figuras y el total")
    elif abs(sum(x["v2026"] for x in ac if x["figura"] != "total") - tot[0]["v2026"]) > 2:
        aviso("recaudación acumulado", "las figuras de 2026 no suman el total")
    man = RUTA.parent / "espana-manual.json"
    if man.exists():            # el total de 2025 y el acumulado a septiembre deben coincidir con lo ya volcado en el manual
        m = json.loads(man.read_text(encoding="utf-8"))
        cifras = {(x.get("nombre"), str(x.get("anio"))): x.get("valor") for x in m.get("recaudacion_aeat", []) + m.get("recaudacion", [])}
        a25 = next((f for f in rc.get("anual", []) if f.get("anio") == 2025), None)
        if a25 and cifras.get(("Ingresos tributarios totales", "2025")) not in (None, a25["total"]):
            aviso("recaudación 2025", f"el total {a25['total']} no coincide con el manual {cifras[('Ingresos tributarios totales', '2025')]}")
        if tot and cifras.get(("Ingresos tributarios netos, enero-septiembre", "ene-sep 2026")) not in (None, tot[0]["v2026"]):
            aviso("recaudación ene-sep 2026", "no coincide con el manual")
else:
    aviso("recaudación", "no existe explorador/espana-recaudacion.json (python scripts/espana_recaudacion.py)")

# ---- C264: pestaña Cadenas (explorador/cadenas.json): fuentes, fechas, niveles y sin NaN
RUTA_CAD = RUTA.parent / "cadenas.json"
TOKEN_OK = ("sí", "parcial", "mínimo", "no", "sin dato")
CAPTURA_OK = ("alta", "media", "baja", "incierta")


def celda_cadena(donde, v, niveles=("P", "S", "V")):
    """Una celda con dato necesita texto, fuente, nivel P/S/V, fecha válida (o null) y enlace http o informe existente.
    En el contexto ISO también vale «R» ([RAZONADO], deducción con sus fuentes citadas en «f»)."""
    if not isinstance(v, dict):
        aviso(donde, "la celda debe ser un objeto o null")
        return
    if not str(v.get("t") or "").strip():
        aviso(donde, "celda sin texto («t»)")
    if not str(v.get("f") or "").strip():
        aviso(donde, "celda sin fuente («f»)")
    if v.get("n") not in niveles:
        aviso(donde, f"«n» debe ser uno de {niveles}: {v.get('n')!r}")
    if v.get("d") is not None and not fecha_ok(v["d"]):
        aviso(donde, f"fecha no válida: {v['d']!r}")
    u, i = v.get("u"), v.get("i")
    if u and not str(u).startswith(("https://", "http://")):
        aviso(donde, f"«u» debe empezar por http:// o https://: {u!r}")
    if i and not (RAIZ / i).is_file():
        aviso(donde, f"«i» apunta a un archivo que no existe: {i}")
    if not u and not i and v.get("n") in ("P", "S"):
        aviso(donde, "nivel P/S sin enlace ni informe: debe ser V")


if RUTA_CAD.exists():
    crudo_cad = RUTA_CAD.read_text(encoding="utf-8")
    if re.search(r"\bNaN\b|\bInfinity\b|\bundefined\b", crudo_cad):
        aviso("cadenas.json", "contiene NaN, Infinity o «undefined»")
    cad = json.loads(crudo_cad)
    if not fecha_ok(cad.get("_actualizado")):
        aviso("cadenas.json", "falta «_actualizado» con fecha válida")
    caps_c = [x["id"] for x in cad.get("capacidades", [])]
    capas_c = [x["id"] for x in cad.get("capas_red", [])]
    capas_mapa = {c["id"] for c in d["capas"]}
    for x in cad.get("capas_red", []):
        if x.get("capa_mapa") and x["capa_mapa"] not in capas_mapa:
            aviso("cadenas capas_red", f"capa del mapa inexistente: {x['capa_mapa']}")
    for x in cad.get("contexto_iso", []):
        celda_cadena("cadenas contexto_iso", x, ("P", "S", "V", "R"))
    ids_c = set()
    for c in cad.get("cadenas", []):
        cid = c.get("id")
        if cid in ids_c:
            aviso("cadenas.json", f"id repetido: {cid}")
        ids_c.add(cid)
        for k in caps_c:
            if k not in c.get("matriz", {}):
                aviso(f"cadena {cid}", f"falta la capacidad «{k}» (usa null si no hay dato)")
            elif c["matriz"][k] is not None:
                celda_cadena(f"cadena {cid}.{k}", c["matriz"][k])
        for k in capas_c:
            cp = (c.get("capas") or {}).get(k)
            if not isinstance(cp, dict):
                aviso(f"cadena {cid}", f"falta la capa «{k}»")
            elif cp.get("token") not in TOKEN_OK:
                aviso(f"cadena {cid} capa {k}", f"«token» debe ser uno de {TOKEN_OK}: {cp.get('token')!r}")
        for x in c.get("iso", []):
            celda_cadena(f"cadena {cid} iso", x)
        ta = c.get("tipos_activo")
        if ta:
            for k, x in (ta.get("tipos") or {}).items():
                celda_cadena(f"cadena {cid} tipos_activo.{k}", x)
                if not isinstance(x.get("v"), (int, float)) or not isinstance(x.get("k"), int):
                    aviso(f"cadena {cid} tipos_activo.{k}", "«v» (M$) y «k» (nº de activos) deben ser números")
            for k in ("emisores", "estandar", "liquidacion"):
                if ta.get(k) is not None:
                    celda_cadena(f"cadena {cid} tipos_activo.{k}", ta[k])
        cap = c.get("captura") or {}
        if cap.get("nivel") not in CAPTURA_OK:
            aviso(f"cadena {cid}", f"captura.nivel debe ser uno de {CAPTURA_OK}")
        if not str(cap.get("mecanismo", "")).startswith("[RAZONADO]"):
            aviso(f"cadena {cid}", "captura.mecanismo debe empezar por [RAZONADO]")
        if not cap.get("supuestos"):
            aviso(f"cadena {cid}", "captura sin supuestos")
        for h in c.get("hitos", []):
            if not fecha_ok(h.get("fecha")) or not str(h.get("u", "")).startswith("https://") or h.get("n") not in ("P", "S", "V"):
                aviso(f"cadena {cid} hito {h.get('fecha')}", "hito sin fecha válida, enlace https o nivel P/S/V")
            if h.get("tl") and not any(m.get("url") == h.get("u") for m in d["movimientos"]):
                aviso(f"cadena {cid} hito {h.get('fecha')}", "marcado en la Línea de tiempo pero no está en datos.json")
        if c.get("ficha") and c["ficha"] not in {f.get("id") for f in json.loads((RUTA.parent / "fichas-activos.json").read_text(encoding="utf-8")).get("fichas", [])}:
            aviso(f"cadena {cid}", f"ficha de activo inexistente: {c['ficha']}")
    # C266: bloque «relaciones» (hechos que unen redes) y campos «cadenas» y «umbral» de los movimientos
    ids_rel = set()
    for r in cad.get("relaciones", []):
        rid = r.get("id")
        if not rid or rid in ids_rel:
            aviso("cadenas relaciones", f"relación sin id o con id repetido: {rid!r}")
        ids_rel.add(rid)
        if not str(r.get("titulo") or "").strip() or not r.get("hechos"):
            aviso(f"relación {rid}", "falta «titulo» o no tiene hechos")
        if not r.get("cadenas") or any(x not in ids_c for x in r.get("cadenas", [])):
            aviso(f"relación {rid}", f"«cadenas» vacío o con ids que no existen: {r.get('cadenas')}")
        for h in r.get("hechos", []):
            celda_cadena(f"relación {rid}", h, ("P", "S", "V", "R"))
            if any(x not in r.get("cadenas", []) for x in h.get("cadenas", [])):
                aviso(f"relación {rid}", f"un hecho cita redes que no están en la relación: {h.get('cadenas')}")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import etiquetar_cadenas as _et
    _regs = _et.reglas(cad)
    for m in d["movimientos"]:
        dn = f"movimiento {m['fecha']} {m['actor'][:20]}"
        cs = m.get("cadenas")
        if cs is not None and (not isinstance(cs, list) or not cs or len(set(cs)) != len(cs) or any(x not in ids_c for x in cs)):
            aviso(dn, f"«cadenas» debe ser una lista sin repetidos de ids de cadenas.json: {cs!r}")
        elif (cs or []) != _et.cadenas_de(m, _regs):
            aviso(dn, f"«cadenas» no coincide con las reglas ({cs} frente a {_et.cadenas_de(m, _regs)}): ejecuta python scripts/etiquetar_cadenas.py")
        if "umbral" in m and m["umbral"] is not True:
            aviso(dn, "«umbral» solo puede ser true (o no estar)")
        elif bool(m.get("umbral")) != _et.es_umbral(m):
            aviso(dn, "«umbral» no coincide con la regla W05: ejecuta python scripts/etiquetar_cadenas.py")
else:
    aviso("cadenas", "no existe explorador/cadenas.json")

# C287/Tarea 3: comprobaciones mínimas de los 9 JSON nuevos (JSON válido, sin NaN/Infinity, fecha, fuente y nivel presentes)
def _hay_clave(o, claves):
    if isinstance(o, dict):
        return any(k in claves and v not in (None, "", [], {}) for k, v in o.items()) or any(_hay_clave(v, claves) for v in o.values())
    if isinstance(o, list):
        return any(_hay_clave(v, claves) for v in o)
    return False


def _rechaza(c):
    raise ValueError(f"valor {c} no válido en JSON")


for _n in ("cadenas-onchain", "mica-registro", "eeuu-fiscal", "ocde-bis", "etf-flujos", "espana-energia-vivienda",
           "calendario-oficial", "conflictos-gdelt", "liquidez-manual",
           # C312: bloques C310 de Cadenas, Matriz y Calendario
           "corredores-liquidez", "pais-corredores", "ley-eeuu", "profundidad-multidivisa", "swift-liquidacion",
           # C317: empresa detrás de cada red
           "empresas-redes",
           # C300: uso y seguridad por red
           "cadenas-validadores", "cadenas-incidentes", "cadenas-gobernanza", "comparativa-liquidacion", "pruebas-bancos",
           # C314: interconexión entre cadenas
           "interconexion", "escenarios-redes",
           # C313: qué aporta cada red
           "aporta-redes"):
    _ruta = RAIZ / "explorador" / f"{_n}.json"
    if not _ruta.is_file():
        aviso(f"{_n}.json", "no existe")
        continue
    try:
        _j = json.loads(_ruta.read_text(encoding="utf-8"), parse_constant=_rechaza)
    except (ValueError, OSError) as _e:
        aviso(f"{_n}.json", f"JSON no válido o con NaN/Infinity: {_e}")
        continue
    if not isinstance(_j, dict) or not _j:
        aviso(f"{_n}.json", "la raíz debe ser un objeto no vacío")
        continue
    if not _hay_clave(_j, {"_actualizado", "actualizado", "leido", "generado", "fecha_lectura", "generado_utc", "fecha_dato", "as_of", "revisado"}):
        aviso(f"{_n}.json", "sin fecha de lectura/generación (_actualizado, leido, generado, fecha_lectura)")
    if not _hay_clave(_j, {"fuente", "fuentes", "metodo", "url"}):
        aviso(f"{_n}.json", "sin fuente (fuente, fuentes, metodo o url)")
    if _n != "pais-corredores" and not _hay_clave(_j, {"nivel", "nota_nivel"}):   # pais-corredores toma el nivel de la celda de la Matriz (regulacion.json)
        aviso(f"{_n}.json", "sin nivel de fuente (nivel o nota_nivel)")

# C205: la tesis de Joel es privada. privado/ no puede estar en git ni su contenido en las páginas públicas (docs/)
try:
    import subprocess
    en_git = subprocess.run(["git", "ls-files", "privado"], cwd=RAIZ_PRIV, capture_output=True, text=True, timeout=20).stdout.split()
    if en_git:
        aviso("privado/", f"{len(en_git)} archivo(s) de privado/ están en git (deben quedar fuera del repo público)")
    ignorado = subprocess.run(["git", "check-ignore", "-q", "privado/tesis-vista.html"], cwd=RAIZ_PRIV, timeout=20).returncode == 0
    if not ignorado:
        aviso("privado/", ".gitignore no excluye privado/")
except (OSError, subprocess.SubprocessError) as e:
    aviso("privado/", f"no se pudo comprobar con git ({type(e).__name__})")
sys.path.insert(0, str(RAIZ_PRIV / "scripts"))
import huellas_privado  # noqa: E402
for archivo, n in huellas_privado.revisar_docs():
    aviso(archivo, f"contiene {n} huella(s) de la tesis privada (privado/): no se puede publicar")

# C321: cada «ref» de escenarios-redes.json debe existir en aporta-redes.json; cada paso sin ref debe llevar razón
try:
    _esc = json.loads((RAIZ / "explorador" / "escenarios-redes.json").read_text(encoding="utf-8"))
    _apo = json.loads((RAIZ / "explorador" / "aporta-redes.json").read_text(encoding="utf-8"))["redes"]

    def _pasos(_e):
        for _r, _v in _e["redes"].items():
            for _s in ("encaja_mejor", "recompensas", "leyes", "mensajeria", "seguridad", "beneficiados"):
                for _x in _v.get(_s, []):
                    yield _r, _x
            for _f in _v.get("flujos", {}).values():
                for _x in _f["pasos"]:
                    yield _r, _x
        for _x in _e["marco"]["leyes"] + _e["marco"]["mensajeria"]:
            yield "marco", _x

    for _r, _x in _pasos(_esc):
        if "ref" in _x:
            try:
                _q = _x["ref"].split(".")
                _apo[_q[0]][_q[1]][int(_q[2])]
            except (KeyError, IndexError, ValueError):
                aviso("escenarios-redes.json", f"{_r}: ref {_x['ref']} no existe en aporta-redes.json")
        elif not (_x.get("esp") or _x.get("hecho") or _x.get("ref_archivo")):
            aviso("escenarios-redes.json", f"{_r}: paso sin ref ni razón [ESPECULACIÓN]: {str(_x.get('t') or _x.get('nombre'))[:50]}")
except (OSError, ValueError, KeyError) as _e:
    aviso("escenarios-redes.json", f"no se pudo validar ({type(_e).__name__})")

# C327: una misma URL no puede llevar niveles distintos (P/S/V/R) en los JSON de Cadenas
try:
    _niv = {}

    def _recorre_niv(_o, _f):
        if isinstance(_o, dict):
            _u = _o.get("u") or _o.get("url")
            _n = _o.get("n") if "n" in _o else _o.get("nivel")
            if isinstance(_u, str) and _u.startswith("http") and _n in ("P", "S", "V", "R"):
                _niv.setdefault(_u, {}).setdefault(_n, set()).add(_f)
            for _v in _o.values():
                _recorre_niv(_v, _f)
        elif isinstance(_o, list):
            for _v in _o:
                _recorre_niv(_v, _f)

    for _f in ("cadenas", "aporta-redes", "interconexion", "pruebas-bancos", "escenarios-redes", "regulacion", "datos"):
        _rf = RAIZ / "explorador" / f"{_f}.json"
        if _rf.exists():
            _recorre_niv(json.loads(_rf.read_text(encoding="utf-8")), f"{_f}.json")
    for _u, _ns in _niv.items():
        if len(_ns) > 1:
            aviso("Cadenas niveles", f"la URL {_u[:90]} tiene niveles distintos: " + ", ".join(f"{k} en {'/'.join(sorted(v))}" for k, v in sorted(_ns.items())))
except (OSError, ValueError) as _e:
    aviso("Cadenas niveles", f"no se pudo validar ({type(_e).__name__})")

# C327: recuento de «[VERIFICAR fecha]», fuentes sin URL y nivel R en los JSON de Cadenas (informativo: no cuenta como aviso)
_pend327 = {}


def _pend(cat, donde, msg):
    _pend327.setdefault(cat, []).append(f"{donde}: {msg}")


try:
    def _recorre_c327(_o, _f, _ruta=""):
        if isinstance(_o, dict):
            _n = _o.get("n") if "n" in _o else _o.get("nivel")
            _u = _o.get("u") if "u" in _o else _o.get("fuente")
            _tiene_f = bool(_o.get("f") or _o.get("fuente"))
            if _n == "R":
                _pend("nivel R", _f, f"{_ruta}: celda con nivel R (sin fuente verificable)")
            if _n in ("P", "S", "V") and _tiene_f and not (isinstance(_u, str) and _u.startswith("http")):
                _pend("fuente sin URL", _f, f"{_ruta}: nivel {_n} sin URL ({str(_o.get('f') or _u)[:60]})")
            for _k, _v in _o.items():
                _recorre_c327(_v, _f, f"{_ruta}/{_k}")
        elif isinstance(_o, list):
            for _i, _v in enumerate(_o):
                _recorre_c327(_v, _f, f"{_ruta}[{_i}]")
        elif isinstance(_o, str) and "[VERIFICAR fecha" in _o:
            _pend("[VERIFICAR fecha]", _f, f"{_ruta}: {_o[:70]}")

    for _f in ("cadenas", "aporta-redes", "interconexion", "pruebas-bancos", "escenarios-redes"):
        _rf = RAIZ / "explorador" / f"{_f}.json"
        if _rf.exists():
            _recorre_c327(json.loads(_rf.read_text(encoding="utf-8")), f"{_f}.json")
except (OSError, ValueError) as _e:
    aviso("Cadenas C327", f"no se pudo validar ({type(_e).__name__})")

# C329: la regla de captura guardada en cadenas.json debe coincidir con lo que calcula scripts/calcular_captura.py
try:
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("calcular_captura", RAIZ / "scripts" / "calcular_captura.py")
    _cc = _iu.module_from_spec(_sp)
    _sp.loader.exec_module(_cc)
    _cad2, _res = _cc.calcular()
    for _c in _cad2.get("cadenas", []):
        _rg = (_c.get("captura") or {}).get("regla")
        if not _rg:
            aviso(f"cadena {_c['id']}", "falta captura.regla (ejecuta python scripts/calcular_captura.py --escribir)")
        elif _rg.get("nivel") != _res[_c["id"]]["nivel"] or _rg.get("consumo") != _res[_c["id"]]["consumo"]:
            aviso(f"cadena {_c['id']}", f"captura.regla desactualizada: guardado {_rg.get('nivel')}/{_rg.get('consumo')}, calculado {_res[_c['id']]['nivel']}/{_res[_c['id']]['consumo']}")
except (OSError, ValueError, KeyError, ImportError) as _e:
    aviso("Captura", f"no se pudo validar ({type(_e).__name__})")

# C332: las tarjetas de DEX nativos llevan hechos con texto, fuente, nivel, fecha y enlace
try:
    for _t in json.loads((RAIZ / "explorador" / "cadenas.json").read_text(encoding="utf-8")).get("dex_nativos", {}).get("tarjetas", []):
        for _h in _t.get("hechos", []):
            celda_cadena(f"dex_nativos {_t.get('red')} {_t.get('nombre', '')[:30]}", _h)
except (OSError, ValueError) as _e:
    aviso("dex_nativos", f"no se pudo validar ({type(_e).__name__})")

# C331: cada paso del escenario del activo puente es hecho con fuente y nivel, o [ESPECULACIÓN] con su razón
try:
    _mk = json.loads((RAIZ / "explorador" / "escenarios-redes.json").read_text(encoding="utf-8")).get("marco", {})
    # C333: las secciones ampliadas siguen la misma regla que el escenario del puente neutral
    _pp = list(_mk.get("puente_neutral", {}).get("pasos", []))
    for _sx in _mk.get("escenarios_ampliados", []):
        _pp += _sx.get("pasos", [])
    for _i, _p in enumerate(_pp, 1):
        _hh = _p.get("hecho")
        if _hh:
            if not (_hh.get("fuente") and _hh.get("nivel") in ("P", "S", "V")):
                aviso("puente_neutral", f"paso {_i}: hecho sin fuente o nivel válido")
            if _hh.get("url") and not str(_hh["url"]).startswith("https://"):
                aviso("puente_neutral", f"paso {_i}: url debe empezar por https://")
        elif not _p.get("esp"):
            aviso("puente_neutral", f"paso {_i}: sin hecho con fuente ni razón [ESPECULACIÓN]")
except (OSError, ValueError) as _e:
    aviso("puente_neutral", f"no se pudo validar ({type(_e).__name__})")

print("\n".join(avisos) if avisos else "Sin avisos.")
if _pend327:
    print("\nPendientes de Cadenas (C327, no cuentan como aviso; detalle con --pendientes):")
    for _c, _l in sorted(_pend327.items()):
        print(f"  {_c}: {len(_l)}")
        if "--pendientes" in sys.argv:
            for _x in _l:
                print("    " + _x[:200])
print(f"\n{len(avisos)} aviso(s) en {len(d['capas'])} capas y {len(d['movimientos'])} movimientos.")
if RUTA_REG.exists():
    print(f"Radar regulatorio: {len(r.get('celdas', []))} celdas, {sin_dato} sin dato (etapa null, no cuentan como aviso).")
sys.exit(1 if avisos else 0)
