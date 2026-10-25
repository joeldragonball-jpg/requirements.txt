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
        if not re.match(r"\|\s*[RGW]\d+[A-Za-z]*\s*\|", linea):
            continue
        c = [x.strip() for x in linea.strip().strip("|").split("|")]
        if len(c) < 9:
            continue
        out.append({"id": c[0], "tema": limpiar(c[1]), "estado": estado(" | ".join(c[8:])), "detalle": limpiar(" | ".join(c[8:]))[:140],
                    "tam": c[5], "modelo": c[3], "real": limpiar(c[7]), "origen": "R"})
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
        "informes": informes_recientes(),
    }


def main():
    datos = construir(bots_estado=True)
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(datos, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    r = datos["resumen"]
    print(f"seguimiento.json: {r['hechas']} hechas, {r['pendientes']} pendientes ({r['por_cola']}), R00 hoy: apertura={datos['hoy']['apertura']} cierre={datos['hoy']['cierre']} "
          f"racha={datos['hoy']['racha']}, predicciones abiertas={len(datos['predicciones']['abiertas'])}, auditoría abiertos={(datos['auditorias'] or {}).get('abiertos')}, "
          f"bots con problema={sum(1 for b in datos['bots'] if b['ok'] is False)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
