"""Datos del apartado «Seguimiento» (PC y móvil): qué se ha hecho, qué falta y qué caduca primero.
Solo lee archivos PÚBLICOS del repo (nada de privado/) y, si se pide, el estado de los workflows en la API pública de GitHub.
Sin IA, sin claves, sin coste. Escribe docs/movil/seguimiento.json.

Uso:  python scripts/construir_seguimiento.py
Desde Python:  construir_seguimiento.construir(bots_estado=False)  → dict (lo usa seguimiento.py en el ordenador)."""
import json
import os
import re
import sys
import tomllib
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "docs" / "movil" / "seguimiento.json"
REPO = "joeldragonball-jpg/requirements.txt"
WORKFLOWS = [("alertas.yml", "Alertas de precio", 2.5), ("noticias.yml", "Noticias con IA", 7.0), ("votos.yml", "Votos de noticias", 6.0),
             ("onchain.yml", "Vigilancia on-chain", 2.5), ("escrow.yml", "Escrow de Ripple", 30), ("eventos.yml", "Aviso de eventos", 30),
             ("despertador.yml", "Despertador de la app", 8), ("revision.yml", "Revisión semanal del cerebro", 24 * 8),
             ("verificar.yml", "Verificación mensual", 24 * 35), ("paneles.yml", "Paneles de datos", 72)]
# Palabras del calendario que enlazan una tarea pendiente con su próximo plazo
CLAVES = {"T06": ["Japón", "FIEA", "BoJ"], "T07": ["Corea"], "T08": ["Singapur", "MAS"], "T09": ["Hong Kong", "HKMA"], "T10": ["India", "RBI"],
          "T11": ["Brasil", "Copom"], "T12": ["Rusia"], "T13": ["Emiratos", "VARA"], "T14": ["China", "LPR"], "T15": ["BRICS"],
          "T16": ["BIS", "FMI", "FSB", "GAFI"], "T23": ["Ripple", "Stellar"], "T17": ["FOMC", "BCE", "BoJ"]}


def leer(ruta):
    try:
        return ruta.read_text(encoding="utf-8")
    except Exception:
        return ""


def limpiar(t):
    return re.sub(r"\s+", " ", re.sub(r"[*_`]+", "", re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t))).strip()


def estado(texto):
    t = texto.strip().lower()
    if t.startswith(("hecho", "hecha")):
        return "hecha"
    if "cubierto por" in t or "cubierta por" in t:
        return "cubierta"
    if t.startswith("recurrente"):
        return "recurrente"
    if t.startswith("pendiente"):
        return "pendiente"
    return "otro"


def cola_r():
    """Tareas R/G de research/COLA.md con su estado y el coste real anotado."""
    out = []
    for linea in leer(RAIZ / "research" / "COLA.md").splitlines():
        if not re.match(r"\|\s*[RGWC]\d+[A-Za-z]*\s*\|", linea):
            continue
        c = [x.strip() for x in linea.strip().strip("|").split("|")]
        if len(c) < 9:
            continue
        ruta = re.search(r"research/prompts/[^\s;)]+", " | ".join(c[8:]))
        out.append({"id": c[0], "tema": limpiar(c[1]), "estado": estado(" | ".join(c[8:])), "detalle": limpiar(" | ".join(c[8:]))[:140],
                    "tam": c[5], "modelo": c[3], "est": c[6], "real": limpiar(c[7]), "prompt": ruta.group(0) if ruta else "", "origen": "R"})
    return out


def expandir(ids):
    """«T06, T08-T10, T23» → ['T06','T08','T09','T10','T23']."""
    out = []
    for parte in re.split(r"[,\s]+", ids):
        m = re.match(r"T(\d+)-T?(\d+)$", parte)
        if m:
            out += [f"T{n:02d}" for n in range(int(m.group(1)), int(m.group(2)) + 1)]
        elif re.match(r"T\d+$", parte):
            out.append(f"T{int(parte[1:]):02d}")
    return out


def cola_t():
    """Temas T01-T25 (nombre de la lista y estado de la tabla «Estado»)."""
    texto = leer(RAIZ / "research" / "COLA-TEMAS-GEMINI.md")
    nombres = {f"T{int(m.group(1)):02d}": limpiar(m.group(2)) for m in re.finditer(r"^- \*\*T(\d+)\s*([^*:]*?):?\*\*", texto, re.M)}
    estados = {}
    for linea in texto.splitlines():
        if not re.match(r"\|\s*T\d", linea):
            continue
        c = [x.strip() for x in linea.strip().strip("|").split("|")]
        if len(c) < 3:
            continue
        hecho = "hecho" in c[-1].lower() and "pendiente" not in c[-1].lower()
        for i in expandir(c[0]):
            estados[i] = "hecha" if hecho else "pendiente"
    return [{"id": i, "tema": nombres.get(i, i), "estado": estados.get(i, "pendiente"), "origen": "T"} for i in sorted(set(nombres) | set(estados))]


def cola_d():
    out = []
    for linea in leer(RAIZ / "research" / "COLA-DEUDA-BONOS.md").splitlines():
        if not re.match(r"\|\s*D\d+\s*\|", linea):
            continue
        c = [x.strip() for x in linea.strip().strip("|").split("|")]
        if len(c) < 2:
            continue
        hecho = c[1].upper().startswith("HECHO")
        tema = re.sub(r"^HECHO el [^.(]*(\([^)]*\))?\.?\s*", "", c[1], flags=re.I) if hecho else c[1]
        parcial = not hecho and "HECHO" in c[1].upper()
        if parcial:
            tema = "(parcial) " + re.sub(r"\(a\)\s*HECHO el [^:]*:\s*", "", c[1], flags=re.I)
        out.append({"id": c[0], "tema": limpiar(tema)[:110], "estado": "hecha" if hecho else "pendiente", "origen": "D"})
    return out


def eventos_futuros():
    try:
        with open(RAIZ / "eventos" / "calendario.toml", "rb") as f:
            evs = tomllib.load(f)["eventos"]
    except Exception:
        return []
    hoy = date.today()
    out = []
    for e in evs:
        try:
            d = date.fromisoformat(e["fecha"])
        except Exception:
            continue
        if d >= hoy:
            out.append({"fecha": e["fecha"], "titulo": e["titulo"], "impacto": e.get("impacto", "bajo"), "aprox": bool(e.get("aproximado")), "dias": (d - hoy).days})
    return sorted(out, key=lambda e: e["fecha"])


def r00():
    """¿Están hoy los R00 de apertura y cierre? Racha de días seguidos con al menos un R00."""
    carpeta = RAIZ / "informes"
    fechas = {"apertura": set(), "cierre": set()}
    for f in carpeta.glob("2*-*.md"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})-(apertura|cierre)", f.name)
        if m:
            fechas[m.group(2)].add(m.group(1))
    hoy = date.today()
    todos = fechas["apertura"] | fechas["cierre"]
    racha, d = 0, hoy if hoy.isoformat() in todos else hoy - timedelta(days=1)
    while d.isoformat() in todos:
        racha += 1
        d -= timedelta(days=1)
    ult = lambda s: max(s) if s else None
    return {"fecha": hoy.isoformat(), "apertura": hoy.isoformat() in fechas["apertura"], "cierre": hoy.isoformat() in fechas["cierre"],
            "racha": racha, "ultima_apertura": ult(fechas["apertura"]), "ultimo_cierre": ult(fechas["cierre"]), "total": len(todos)}


def predicciones():
    abiertas, resueltas = [], []
    hoy = date.today()
    for linea in leer(RAIZ / "informes" / "predicciones.md").splitlines():
        if not re.match(r"\|\s*\d+\s*\|", linea):
            continue
        c = [limpiar(x) for x in linea.strip().strip("|").split("|")]
        if len(c) < 7:
            continue
        limite = c[4] if re.match(r"\d{4}-\d{2}-\d{2}$", c[4]) else None
        res = c[6]
        item = {"n": c[0], "fecha": c[1][:10], "quien": c[2], "que": c[3][:160], "limite": limite, "como": c[5][:110], "resultado": res[:120],
                "dias": (date.fromisoformat(limite) - hoy).days if limite else None}
        (abiertas if res.lower().startswith("sin resolver") or not res else resueltas).append(item)
    abiertas.sort(key=lambda x: (x["dias"] is None, x["dias"] if x["dias"] is not None else 0))
    return {"abiertas": abiertas, "resueltas": resueltas}


def auditorias():
    """Hallazgos de la última auditoría de coherencia y su estado (research/auditorias-estado.json, anotado a mano)."""
    archivos = sorted((RAIZ / "informes" / "research").glob("*auditoria-coherencia*.md"), reverse=True)
    if not archivos:
        return None
    ruta = archivos[0]
    estado_json = {}
    try:
        estado_json = json.loads((RAIZ / "research" / "auditorias-estado.json").read_text(encoding="utf-8"))
    except Exception:
        pass
    cerrados = set(estado_json.get(ruta.name, {}).get("cerrados", []))
    hallazgos = []
    for linea in leer(ruta).splitlines():
        m = re.match(r"\|\s*(C\d+)\s*\|\s*(Alta|\*\*Alta\*\*|Media|Baja)\s*\|\s*([^|]*)\|\s*([^|]*)\|", linea)
        if m:
            hallazgos.append({"id": m.group(1), "sev": m.group(2).strip("*"), "donde": limpiar(m.group(3))[:90], "que": limpiar(m.group(4))[:170],
                              "estado": "cerrado" if m.group(1) in cerrados else "abierto"})
    return {"archivo": ruta.name, "hallazgos": hallazgos, "abiertos": sum(1 for h in hallazgos if h["estado"] == "abierto"),
            "cerrados": sum(1 for h in hallazgos if h["estado"] == "cerrado")}


def bots():
    ahora = datetime.now(timezone.utc)
    cab = {"User-Agent": "seguimiento", "Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        cab["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    out = []
    for archivo, nombre, tol in WORKFLOWS:
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request(
                f"https://api.github.com/repos/{REPO}/actions/workflows/{archivo}/runs?per_page=1", headers=cab), timeout=20))["workflow_runs"][0]
            horas = (ahora - datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))).total_seconds() / 3600
            ok = r["conclusion"] == "success" and horas <= tol
            out.append({"nombre": nombre, "ok": ok, "conclusion": r["conclusion"] or r["status"], "horas": round(horas, 1), "tolerancia": tol})
        except Exception:
            out.append({"nombre": nombre, "ok": None, "conclusion": "sin dato", "horas": None, "tolerancia": tol})
    return out


PLAN = {"W01": ("Tipos de interés", "2 %"), "W02": ("Deuda y subastas", "2 %"), "W03": ("Países (huecos del radar)", "4 %"), "W04": ("ETF y flujos", "3 %"),
        "W05": ("Verificación por lotes", "3 %"), "W06": ("Voces y predicciones", "3 %"), "W07": ("Research de fuentes", "3 %"), "W08": ("Auditoría mensual", "4 %"),
        "W09": ("Resumen semanal", "1,5 %"), "W10": ("Energía y geopolítica", "2 %")}
DIAS = {0: ["W01"], 1: ["W02"], 2: ["W03"], 3: ["W05"], 4: ["W06", "W09"], 5: ["W10"], 6: []}   # lunes = 0


TIPOS = {"W01": "actualizar", "W02": "actualizar", "W04": "actualizar", "W10": "actualizar", "W03": "nuevo", "W05": "verificar", "W06": "verificar",
         "W07": "fuentes", "W08": "revisar", "W09": "revisar"}
CADA = {"W01": (7, "cada lunes"), "W02": (7, "cada martes"), "W03": (7, "cada miércoles"), "W04": (14, "cada 2 jueves"), "W05": (7, "cada jueves"),
        "W06": (7, "cada viernes"), "W07": (31, "1.ª semana del mes"), "W08": (31, "última semana del mes"), "W09": (7, "cada viernes"), "W10": (7, "fin de semana")}


EQUIV = {"W01": ["*-T17-*.md"], "W02": ["*-D0*.md"], "W03": ["*-T0[6-9]-*.md", "*-T1[0-6]-*.md"], "W04": ["*-T19-*.md"], "W05": ["*verificaciones-pendientes*.md"],
         "W08": ["*auditoria-coherencia*.md"], "W10": ["*-T18-*.md"]}


def ultimo_w(ident):
    """Fecha del último informe de la rutina (archivos informes/research/AAAA-MM-DD-Wxx-*.md)."""
    patrones = [f"*-{ident}-*.md"] + EQUIV.get(ident, [])        # también cuenta lo hecho antes de que existiera la rutina
    fechas = [f.name[:10] for pat in patrones for f in (RAIZ / "informes" / "research").glob(pat) if re.match(r"\d{4}-\d{2}-\d{2}", f.name)]
    return max(fechas) if fechas else None


def rutinas():
    hoy = date.today()
    out = []
    for i, (nombre, coste) in PLAN.items():
        u = ultimo_w(i)
        dias = (hoy - date.fromisoformat(u)).days if u else None
        limite, cada = CADA[i]
        out.append({"id": i, "nombre": nombre, "coste": coste, "tipo": TIPOS[i], "cada": cada, "ultimo": u, "dias": dias,
                    "atrasada": dias is None or dias > limite + 1})
    return out


def toca(hoy):
    ids = list(DIAS[hoy.weekday()])
    if hoy.weekday() == 3 and hoy.isocalendar()[1] % 2 == 0:
        ids.append("W04")                                   # ETF: cada dos semanas
    if hoy.weekday() == 5 and hoy.day <= 7:
        ids.append("W07")                                   # fuentes: primer sábado del mes
    if hoy.weekday() == 2 and hoy.day >= 22:
        ids = ["W08"] + [i for i in ids if i != "W03"]      # auditoría: último miércoles del mes
    return [{"id": i, "nombre": PLAN[i][0], "coste": PLAN[i][1], "prompt": f"research/prompts/{i}-*.md"} for i in ids]


def semana():
    hoy = date.today()
    lunes = hoy - timedelta(days=hoy.weekday())
    nombres = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]
    return {"hoy": toca(hoy), "dias": [{"dia": nombres[i], "fecha": (lunes + timedelta(days=i)).isoformat(), "tareas": [t["id"] for t in toca(lunes + timedelta(days=i))],
                                      "es_hoy": (lunes + timedelta(days=i)) == hoy} for i in range(7)]}


def porcentaje(texto):
    m = re.search(r"(<|~|≈)?\s*(\d+(?:[.,]\d+)?)\s*%", texto or "")
    if not m:
        return None
    v = float(m.group(2).replace(",", "."))
    return 0.5 if m.group(1) == "<" and v <= 1 else v


def informes_recientes(n=12):
    out = []
    for carpeta, tipo in (("informes/research", "research"), ("informes/videos", "vídeo")):
        for f in (RAIZ / carpeta).glob("*.md"):
            m = re.match(r"(\d{4}-\d{2}-\d{2})-", f.name)
            if m:
                primera = next((l[2:].strip() for l in leer(f).splitlines() if l.startswith("# ")), f.stem)
                out.append({"fecha": m.group(1), "tipo": tipo, "titulo": primera[:110], "ruta": f.relative_to(RAIZ).as_posix()})
    return sorted(out, key=lambda x: (x["fecha"], x["ruta"]), reverse=True)[:n]


def frescura():
    """Qué datos del Explorador, del cerebro y de los paneles manuales se están quedando viejos y qué rutina los pone al día (sin IA)."""
    hoy = date.today()
    items = []

    def anadir(area, titulo, n, detalle, rutina, nivel):
        items.append({"area": area, "titulo": titulo, "n": n, "detalle": detalle, "rutina": rutina, "nivel": nivel})
    try:
        reg = json.loads(leer(RAIZ / "explorador" / "regulacion.json"))
        celdas = reg.get("celdas", [])
        sin_dato = [c for c in celdas if c.get("etapa") is None and c.get("tema") != "politica"]
        por_jur = {}
        for c in sin_dato:
            por_jur[c["jur"]] = por_jur.get(c["jur"], 0) + 1
        top = ", ".join(f"{j.upper()} {n}" for j, n in sorted(por_jur.items(), key=lambda x: -x[1])[:5])
        anadir("Radar regulatorio", "Celdas sin dato", len(sin_dato), f"Más huecos: {top}" if top else "", "W03", "aviso" if sin_dato else "ok")
        viejas = [c for c in celdas if c.get("revisado") and (hoy - date.fromisoformat(c["revisado"][:10])).days > 30]
        anadir("Radar regulatorio", "Celdas sin revisar en más de 30 días", len(viejas), "Se revisan con la rutina de países", "W03", "alerta" if len(viejas) > 10 else "aviso" if viejas else "ok")
        pasadas = [c for c in celdas if isinstance(c.get("proxima"), dict) and c["proxima"].get("fecha", "9999")[:10] < hoy.isoformat()]
        anadir("Radar regulatorio", "Fechas previstas ya pasadas sin actualizar", len(pasadas),
               "; ".join(f"{c['jur'].upper()}/{c['tema']}" for c in pasadas[:4]), "W03", "alerta" if pasadas else "ok")
    except Exception as e:
        anadir("Radar regulatorio", f"No se pudo leer ({type(e).__name__})", 0, "", "W03", "aviso")
    try:
        vs = json.loads(leer(RAIZ / "explorador" / "voces.json")).get("voces", [])
        sin = [v for v in vs if v.get("conf") == "sin_confirmar"]
        viejas = [v for v in sin if v.get("cuando") and (hoy - date.fromisoformat((v["cuando"] + "-01")[:10] if len(v["cuando"]) == 7 else v["cuando"][:10])).days > 14]
        anadir("Voces", "Voces sin confirmar", len(sin), f"{len(viejas)} llevan más de 14 días" if viejas else "", "W06", "alerta" if len(viejas) > 3 else "aviso" if sin else "ok")
    except Exception as e:
        anadir("Voces", f"No se pudo leer ({type(e).__name__})", 0, "", "W06", "aviso")
    try:
        pr = predicciones()
        vencidas = [x for x in pr["abiertas"] if x.get("limite") and x["limite"] < hoy.isoformat()]
        anadir("Predicciones", "Vencidas sin resultado", len(vencidas), ", ".join(f"#{x['n']}" for x in vencidas[:6]) if vencidas else "", "W06", "alerta" if vencidas else "ok")
    except Exception as e:
        anadir("Predicciones", f"No se pudo leer ({type(e).__name__})", 0, "", "W06", "aviso")
    try:
        man = json.loads(leer(RAIZ / "explorador" / "liquidez-manual.json"))
        retraso = []
        for clave in ("jp", "cn"):
            f = man.get(clave, {}).get("fecha")
            if f:
                dias = (hoy - date.fromisoformat(f[:7] + "-01")).days
                if dias > 75:
                    retraso.append(f"{clave.upper()} ({f})")
        anadir("Datos a mano", "Liquidez de Japón y China", len(retraso), ", ".join(retraso) if retraso else "al día (dato del último mes publicado)", "W01", "alerta" if retraso else "ok")
    except Exception as e:
        anadir("Datos a mano", f"No se pudo leer ({type(e).__name__})", 0, "", "W01", "aviso")
    try:
        pan = json.loads(leer(RAIZ / "explorador" / "paneles.json"))
        leido = datetime.strptime(pan["leido"][:16], "%Y-%m-%d %H:%M").date() if pan.get("leido") else None
        dias = (hoy - leido).days if leido else None
        anadir("Paneles automáticos", "Última lectura de datos", dias if dias is not None else 0, f"leído el {pan.get('leido', '?')[:16]} UTC", "paneles.yml (L-V 21:30 UTC)",
               "ok" if dias is not None and dias <= 3 else "alerta")
    except Exception as e:
        anadir("Paneles automáticos", f"No se pudo leer ({type(e).__name__})", 0, "", "paneles.yml", "aviso")
    semanales = sorted((RAIZ / "cerebro" / "actualidad").glob("*.md"))
    if semanales:
        ultima = semanales[-1]
        m = re.match(r"(\d{4})-W(\d{2})", ultima.name)
        if m:
            lunes = date.fromisocalendar(int(m.group(1)), int(m.group(2)), 1)
            dias = (hoy - lunes).days
            anadir("Cerebro", "Último resumen semanal del bot", dias, f"{ultima.stem}", "cerebro.yml", "ok" if dias <= 14 else "alerta")
    revs = sorted(f for f in (RAIZ / "informes").glob("*-revision.md"))
    if revs:
        dias = (hoy - date.fromisoformat(revs[-1].name[:10])).days
        anadir("Cerebro", "Última revisión semanal del cerebro", dias, revs[-1].name, "revision.yml", "ok" if dias <= 10 else "alerta")
    orden = {"alerta": 0, "aviso": 1, "ok": 2}
    items.sort(key=lambda x: orden[x["nivel"]])
    return {"items": items, "resumen": {k: sum(1 for x in items if x["nivel"] == k) for k in ("alerta", "aviso", "ok")}}


def construir(bots_estado=False):
    colas = cola_r() + cola_t() + cola_d()
    eventos = eventos_futuros()
    pendientes = []
    for t in colas:
        if t["estado"] != "pendiente":
            continue
        claves = CLAVES.get(t["id"], [])
        plazo = next((e for e in eventos if any(k.lower() in e["titulo"].lower() for k in claves) and not e["aprox"]), None) \
            or next((e for e in eventos if any(k.lower() in e["titulo"].lower() for k in claves)), None) if claves else None
        if plazo and plazo["dias"] > 45:
            plazo = None
        pendientes.append({**t, "tipo": "nuevo", "plazo": ({"fecha": plazo["fecha"], "dias": plazo["dias"], "evento": plazo["titulo"][:90]} if plazo else None)})
    pendientes.sort(key=lambda t: (t["plazo"] is None, t["plazo"]["dias"] if t["plazo"] else 0, t["id"]))
    cuota = []
    for t in colas:
        v = porcentaje(t.get("real", ""))
        if v is not None:
            cuota.append({"id": t["id"], "tema": t["tema"][:60], "pct": v})
    contables = [t for t in colas if t["estado"] in ("hecha", "pendiente")]
    return {
        "generado": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "hoy": r00(), "semana": semana(), "plan": {k: {"nombre": v[0], "coste": v[1]} for k, v in PLAN.items()}, "rutinas": rutinas(),
        "resumen": {"hechas": sum(1 for t in contables if t["estado"] == "hecha"), "pendientes": sum(1 for t in contables if t["estado"] == "pendiente"),
                    "por_cola": {o: {"hechas": sum(1 for t in contables if t["origen"] == o and t["estado"] == "hecha"),
                                     "pendientes": sum(1 for t in contables if t["origen"] == o and t["estado"] == "pendiente")} for o in ("R", "T", "D")}},
        "pendientes": pendientes[:30],
        "plazos": [e for e in eventos if e["impacto"] in ("alto", "medio") and not e["aprox"]][:8],
        "predicciones": predicciones(), "auditorias": auditorias(),
        "bots": bots() if bots_estado else [],
        "cuota": {"total": round(sum(c["pct"] for c in cuota), 1), "tareas": sorted(cuota, key=lambda c: -c["pct"])[:8], "n": len(cuota)},
        "informes": informes_recientes(), "frescura": frescura(), "eventos": eventos_calendario(),
    }


def eventos_calendario():
    """Eventos de los últimos 10 días que importan (alto impacto o con rutina asociada) y de los próximos 14, con qué rutina los cubre y si ya está cubierto."""
    try:
        with open(RAIZ / "eventos" / "calendario.toml", "rb") as f:
            evs = tomllib.load(f)["eventos"]
        reglas = json.loads(leer(RAIZ / "eventos" / "vinculos.json"))["reglas"]
        revisados = json.loads(leer(RAIZ / "eventos" / "revisados.json")).get("revisados", {})
    except Exception:
        return {"pasados": [], "proximos": []}
    hoy = date.today()

    def regla(titulo):
        minus = titulo.lower()
        return next((r for r in reglas if any(w in minus for w in r["palabras"])), None)
    pasados, proximos = [], []
    for e in sorted(evs, key=lambda e: e["fecha"]):
        try:
            ini = date.fromisoformat(e["fecha"])
            fin = date.fromisoformat(e["hasta"]) if e.get("hasta") else ini
        except Exception:
            continue
        imp = e.get("impacto", "bajo")
        r = regla(e["titulo"])
        base = {"fecha": e["fecha"], "hasta": e.get("hasta"), "titulo": e["titulo"], "impacto": imp, "rutina": r["rutina"] if r else None, "que": r["que"] if r else None}
        if hoy - timedelta(days=10) <= fin < hoy and (imp == "alto" or (imp == "medio" and r)):
            clave = f"{e['fecha']}|{e['titulo'][:30]}"
            if clave in revisados:
                estado, detalle = "revisado", revisados[clave].get("estado", "hecho")
            elif r and (ultimo_w(r["rutina"]) or "") >= fin.isoformat():
                estado, detalle = "cubierto", f"{r['rutina']} del {ultimo_w(r['rutina'])}"
            else:
                estado, detalle = "por_revisar", ""
            pasados.append({**base, "estado": estado, "detalle": detalle})
        elif fin >= hoy and ini <= hoy + timedelta(days=14) and (imp in ("alto", "medio")):
            proximos.append({**base, "en_curso": ini < hoy})
    return {"pasados": pasados, "proximos": proximos}


def planning_md(d):
    """Resumen corto y autogenerado de TODO lo que hay por hacer (research/PLANNING.md): lo lee /research en vez de COLA.md y los informes."""
    hoy = date.today()
    dias = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]
    L = [f"# PLANNING (autogenerado, no editar a mano) · {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}", "",
         "Lo regenera `python scripts/construir_seguimiento.py` (el mismo que alimenta el Seguimiento del móvil y del PC), así que **Seguimiento y planning no pueden diverger**. "
         "`/research` sin argumento lee SOLO este archivo; con un ID, lee la fila de `research/COLA.md` y el prompt indicado aquí. Cuota: se mide con get_usage, no está aquí.", ""]
    h = d["hoy"]
    lunes = hoy - timedelta(days=hoy.weekday())
    L += [f"## Hoy ({dias[hoy.weekday()]} {hoy.isoformat()}): solo lo casi obligatorio",
          f"- R00 apertura {'✓' if h['apertura'] else '⏳ pendiente'} · cierre {'✓' if h['cierre'] else '⏳ pendiente (desde las 15:00)'} · racha {h['racha']} días"]
    rut = {r["id"]: r for r in d["rutinas"]}
    fijas = []
    if hoy.weekday() == 0:
        fijas.append(("W01", "lunes: semana de bancos centrales"))
    if hoy.weekday() == 4:
        fijas.append(("W09", "viernes: resumen semanal"))
    if hoy.weekday() == 2 and hoy.day >= 22:
        fijas.append(("W08", "último miércoles del mes: auditoría mensual"))
    for i, motivo in fijas:
        r = rut.get(i, {})
        L.append(f"- Fija de hoy ({motivo}): **{i} {r.get('nombre', '')}** (~{r.get('coste', '?')}) · último {r.get('ultimo') or 'nunca'} · `research/prompts/{i}-*.md`")
    if not fijas:
        L.append("- Sin rutina fija hoy: elige por prioridad en las secciones de abajo.")

    L += ["", "## Rutinas W: lo que falta este periodo (sin día fijo; se hacen cuando haya hueco, de más atrasada a menos)"]

    def hecha(r):
        u = r["ultimo"]
        if not u:
            return False
        f = date.fromisoformat(u)
        limite = CADA[r["id"]][0]
        if limite <= 7:
            return f >= lunes
        if limite <= 14:
            return (hoy - f).days < 14
        return (f.year, f.month) == (hoy.year, hoy.month)
    faltan = sorted((r for r in d["rutinas"] if not hecha(r)), key=lambda r: -(r["dias"] if r["dias"] is not None else 999))
    for r in faltan:
        L.append(f"- {r['id']} · {r['nombre']} · ~{r['coste']} · {r['cada']} · último {r['ultimo'] or 'nunca'}{' · ATRASADA' if r['atrasada'] else ''} · `research/prompts/{r['id']}-*.md`")
    hechas = [r["id"] for r in d["rutinas"] if hecha(r)]
    L.append("Hechas en este periodo: " + (", ".join(hechas) if hechas else "ninguna"))

    L += ["", "## Research nuevo pendiente (por sección)"]
    pend = d["pendientes"]
    c_ = [t for t in pend if t["id"].startswith("C")]
    if c_:
        L.append("**Centro y revisión del cerebro (C)**")
        for t in c_:
            L.append(f"- {t['id']} · {t['tema'].replace('Hueco del Centro: ', '')[:80]} · {t.get('modelo', '')} {t.get('tam', '')} · ~{t.get('est', '?')} · `{t.get('prompt', '')}`")
    for pref, nombre, fichero in (("T", "Países y temas (T)", "research/COLA-TEMAS-GEMINI.md"), ("D", "Deuda y bonos (D)", "research/COLA-DEUDA-BONOS.md"),
                                  ("R", "Otros research (R)", "research/COLA.md")):
        xs = [t for t in pend if t["id"].startswith(pref)]
        if xs:
            L.append(f"**{nombre}** · detalle en `{fichero}`")
            for t in xs:
                plazo = f" · vence/ocurre {t['plazo']['fecha']} ({t['plazo']['evento'][:40]})" if t.get("plazo") else ""
                L.append(f"- {t['id']} · {t['tema'][:70]}{plazo}")
    L += ["", "## Auditorías abiertas"]
    a = d.get("auditorias") or {}
    ab = [x for x in a.get("hallazgos", []) if x["estado"] == "abierto"]
    L += [f"- {x['id']} ({x['sev']}): {x['que'][:110]}" for x in ab] or ["- ninguna"]
    L.append("- Auditoría mensual W08: última semana del mes (miércoles)")

    L += ["", "## Verificaciones abiertas ([VERIFICAR]; las cierra W05 o W08)"]
    try:
        txt = leer(RAIZ / "cerebro" / "documentos" / "resumen-vigente-xrp.md")
        bloque = txt.split("## Dudas y datos a verificar", 1)[1]
        abiertas = [x.strip()[2:].strip() for x in bloque.splitlines() if x.strip().startswith("- [VERIFICAR]")]
        L += [f"- {x[:150]}" for x in abiertas[:10]] or ["- ninguna anotada"]
        if len(abiertas) > 10:
            L.append(f"- … y {len(abiertas) - 10} más en `cerebro/documentos/resumen-vigente-xrp.md`")
    except Exception:
        L.append("- (no se pudo leer `cerebro/documentos/resumen-vigente-xrp.md`)")

    L += ["", "## Qué se está quedando viejo (frescura)"]
    fr = [f for f in (d.get("frescura") or {}).get("items", []) if f["nivel"] != "ok"]
    L += [f"- {'🔴' if f['nivel'] == 'alerta' else '🟡'} {f['area']}: {f['titulo']} ({f['n']}) → {f['rutina']}" + (f" · {f['detalle'][:80]}" if f["detalle"] else "") for f in fr] or ["- todo al día"]
    mal = [b["nombre"] for b in d.get("bots", []) if b.get("ok") is False]
    L += ["", "## Bots con problema", "- " + (", ".join(mal) if mal else "ninguno")]

    ev = d.get("eventos") or {"pasados": [], "proximos": []}
    L += ["", "## Calendario: ya pasaron (10 días) y qué falta decidir"]
    for e in ev["pasados"]:
        marca = {"cubierto": f"✓ cubierto por {e['detalle']}", "revisado": f"✓ revisado ({e['detalle']})", "por_revisar": "⏳ SIN research: decidir (EV)"}[e["estado"]]
        L.append(f"- {e['fecha']} · {e['titulo'][:70]} ({e['impacto']}) → {marca}")
    if not ev["pasados"]:
        L.append("- ninguno")
    L.append("Para los «SIN research»: pide `/research EV <fecha> <título>`; usa `research/prompts/EV-post-evento.md`. Descartar o marcar hecho: `eventos/revisados.json`.")
    L += ["", "## Calendario: próximos 14 días de impacto y qué los cubre"]
    for e in ev["proximos"][:12]:
        cub = f"cubre {e['rutina']} ({e['que']})" if e["rutina"] else "sin rutina: valorar research EV"
        L.append(f"- {e['fecha']}{('→' + e['hasta'][5:]) if e.get('hasta') else ''} · {e['titulo'][:60]} ({e['impacto']}){' · EN CURSO' if e.get('en_curso') else ''} → {cub}")
    if not ev["proximos"]:
        L.append("- ninguno")
    L += ["", "## Predicciones que vencen en 14 días"]
    pr = [x for x in d["predicciones"]["abiertas"] if x.get("limite") and x["limite"] <= (hoy + timedelta(days=14)).isoformat()]
    L += [f"- #{x.get('n', '?')} · {x['limite']} · {str(x.get('texto') or x.get('quien') or '')[:80]}" for x in pr[:8]] or ["- ninguna"]
    L += ["", "## Próximas fechas clave"] + [f"- {e['fecha']} · {e['titulo'][:90]}" for e in d["plazos"][:7]]
    return "\n".join(L) + "\n"


def main():
    datos = construir(bots_estado=True)
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(datos, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    (RAIZ / "research" / "PLANNING.md").write_text(planning_md(datos), encoding="utf-8")
    r = datos["resumen"]
    print(f"seguimiento.json: {r['hechas']} hechas, {r['pendientes']} pendientes ({r['por_cola']}), R00 hoy: apertura={datos['hoy']['apertura']} cierre={datos['hoy']['cierre']} "
          f"racha={datos['hoy']['racha']}, predicciones abiertas={len(datos['predicciones']['abiertas'])}, auditoría abiertos={(datos['auditorias'] or {}).get('abiertos')}, "
          f"bots con problema={sum(1 for b in datos['bots'] if b['ok'] is False)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
