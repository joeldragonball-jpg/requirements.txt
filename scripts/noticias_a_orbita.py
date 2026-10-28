"""Noticias en la Órbita con caducidad (C35). Python normal: NO usa la API de Anthropic ni la red (usa git local).

Uso:  python scripts/noticias_a_orbita.py [--simular]
Lee las noticias del bot (rama datos, ya incluye las manuales C18) y noticias/manuales/*.json, se queda con las de
nota >= 7 de las últimas 72 h, las cuelga de una capa de explorador/datos.json como movimiento con origen «noticia»
y retira las vencidas a explorador/noticias-archivo.json (nunca borra: las deja con estado «archivada»).
Los movimientos escritos a mano (sin origen «noticia») no se tocan.

Caducidad según el tema (diseño en informes/research/2026-10-28-C38-auditoria-cobertura.md, apartado 5):
  24h -> caduca a los 2 días · 7d -> 14 días · 30d -> 60 días · fija -> no caduca.
Tope: MAX_POR_CAPA noticias vigentes por capa (las demás pasan al archivo con motivo «tope»).
"""
import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "explorador" / "datos.json"
ARCHIVO = RAIZ / "explorador" / "noticias-archivo.json"
MANUALES = RAIZ / "noticias" / "manuales"

NOTA_MIN = 7
VENTANA_H = 72
MAX_POR_CAPA = 5
CADUCA_DIAS = {"24h": 2, "7d": 14, "30d": 60}
# tema del bot -> (capa de la Órbita, frecuencia de revisión). None = sin capa (se anota para C30).
TEMAS = {
    "Petróleo y Ormuz": ("energia", "24h"),
    "Economía y mercados": ("liquidez", "24h"),
    "Regulación": ("reg", "7d"),
    "Cripto y regulación": ("reg", "7d"),
    "XRP / Ripple": ("puente", "7d"),
    "Stellar / XLM": ("puente", "7d"),
    "Geopolítica y política": None,
}
PRIVADO = re.compile(r"cartera|tesis|tu XRP|tu XLM", re.I)   # el repo es público


def _fecha(s):
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def leer_bot():
    try:
        t = subprocess.run(["git", "show", "origin/datos:noticias/noticias.json"], capture_output=True, text=True,
                           encoding="utf-8", cwd=RAIZ).stdout
        return json.loads(t)["noticias"]
    except Exception:
        return []


def leer_manuales():
    salida = []
    for f in sorted(MANUALES.glob("*.json")):
        if f.name.startswith("_"):
            continue
        try:
            datos = json.loads(f.read_text(encoding="utf-8"))
        except ValueError:
            continue
        for n in datos.get("noticias", []):
            salida.append({"titulo": n.get("titulo", ""), "fuente": n.get("fuente", ""), "url": n.get("url", ""),
                           "fecha": n.get("fecha"), "tema": n.get("tema", ""), "puntuacion": n.get("nota", 0),
                           "etiqueta": n.get("etiqueta"), "bulo": n.get("bulo", False)})
    return salida


def candidatas(ahora):
    vistas, salida, sin_capa = set(), [], []
    for n in leer_bot() + leer_manuales():
        f = _fecha(n.get("fecha") or n.get("fecha_noticia") or n.get("fecha_envio"))
        nota = n.get("puntuacion", 0)
        if f is None or not str(nota).isdigit() or int(nota) < NOTA_MIN or n.get("bulo"):
            continue
        if ahora - f > timedelta(hours=VENTANA_H) or not n.get("url") or n["url"] in vistas:
            continue
        titulo = (n.get("titulo") or "").strip()
        if not titulo or PRIVADO.search(titulo):
            continue
        destino = TEMAS.get(n.get("tema"), "?")
        if destino is None or destino == "?":
            sin_capa.append((n.get("tema"), titulo[:70]))
            continue
        vistas.add(n["url"])
        capa, frec = destino
        fuente = n.get("fuente", "")
        nivel = n.get("etiqueta") if n.get("etiqueta") in ("P", "S") else "S"
        salida.append({"f": f, "nota": int(nota), "mov": {
            "fecha": f.date().isoformat(), "capa": capa, "actor": fuente[:40], "texto": titulo.rstrip(".") + ".",
            "estado": "anuncio", "nombra": "no", "fuente": f"{fuente} [{nivel}]", "ent": [fuente[:40]], "act": [],
            "url": n["url"], "nivel": nivel, "origen": "noticia", "tema": n.get("tema"), "frecuencia": frec,
            "nota_bot": int(nota)}})
    return salida, sin_capa


def con_ficha(mov, hoy):
    mov["revisado"] = hoy.isoformat()
    mov["caduca"] = (_fecha(mov["fecha"]).date() + timedelta(days=CADUCA_DIAS[mov["frecuencia"]])).isoformat() \
        if mov["frecuencia"] in CADUCA_DIAS else None
    return mov


def main():
    simular = "--simular" in sys.argv
    ahora = datetime.now(timezone.utc)
    hoy = ahora.date()
    d = json.loads(DATOS.read_text(encoding="utf-8"))
    arch = json.loads(ARCHIVO.read_text(encoding="utf-8")) if ARCHIVO.exists() else {"archivadas": []}

    previas = {m["url"]: m for m in d["movimientos"] if m.get("origen") == "noticia"}
    manuales = [m for m in d["movimientos"] if m.get("origen") != "noticia"]
    nuevas, sin_capa = candidatas(ahora)
    for c in nuevas:       # una noticia que vuelve a salir renueva `revisado` y recalcula `caduca`
        previas[c["mov"]["url"]] = con_ficha(c["mov"], hoy)

    vigentes, retiradas = [], []
    for m in previas.values():
        if m.get("caduca") and m["caduca"] < hoy.isoformat():
            retiradas.append((m, "caducada"))
        else:
            vigentes.append(m)
    por_capa = {}
    for m in sorted(vigentes, key=lambda m: (m["fecha"], m.get("nota_bot", 0)), reverse=True):
        por_capa.setdefault(m["capa"], []).append(m)
    vigentes = []
    for capa, lista in por_capa.items():
        vigentes += lista[:MAX_POR_CAPA]
        retiradas += [(m, "tope") for m in lista[MAX_POR_CAPA:]]

    urls_arch = {a["url"] for a in arch["archivadas"]}
    for m, motivo in retiradas:
        if m["url"] not in urls_arch:
            arch["archivadas"].append({**m, "estado_vida": "archivada", "archivada_el": hoy.isoformat(), "motivo": motivo})

    d["movimientos"] = manuales + sorted(vigentes, key=lambda m: m["fecha"])
    print(f"Candidatas nuevas: {len(nuevas)} · vigentes: {len(vigentes)} · archivadas ahora: {len(retiradas)} · "
          f"sin capa (para C30): {len(sin_capa)}")
    for tema, t in sin_capa[:5]:
        print(f"  sin capa [{tema}] {t}")
    if simular:
        print("(simulación: no se escribe nada)")
        return
    arch["aviso"] = "Noticias retiradas de la Órbita (caducadas o fuera del tope). No se borran. Lo escribe scripts/noticias_a_orbita.py."
    ARCHIVO.write_text(json.dumps(arch, ensure_ascii=False, indent=2), encoding="utf-8")
    DATOS.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
