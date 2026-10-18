"""Prepara los paquetes de fuentes para NotebookLM (sin IA, sin red, solo librería estándar).

Une los informes, dossiers, guías, vídeos, apuntes del cerebro y los datos del Explorador en unos 20 archivos
por tema, listos para subir a mano a NotebookLM. NUNCA incluye privado/ (ahí se guardan tu tesis y el contraste).
Salida: privado/notebooklm-fuentes/ (carpeta que git ignora; aquí no hay secretos, solo está ahí para no subirla al repo).
Uso:
    python scripts/preparar_notebooklm.py            # genera los paquetes y el manifiesto
    python scripts/preparar_notebooklm.py --listar   # solo muestra qué iría en cada paquete
Cada vez que se vuelve a ejecutar, el resumen dice qué paquetes cambiaron desde la última vez: sube solo esos."""
import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "privado" / "notebooklm-fuentes"
EXCLUIR = ("privado", "graphify-out", "node_modules", ".git", "__pycache__", "pdf", "fuentes")
PALABRAS_MAX = 450_000          # NotebookLM admite unas 500.000 palabras por fuente

# Research por id de informe (R25, R21b…) o por nombre de archivo
GRUPOS_RESEARCH = [
    ("01-research-cbdc-y-pagos-transfronterizos", {"R01P", "R08P", "R40", "R28"}, ()),
    ("02-research-stablecoins", {"R24", "R25"}, ()),
    ("03-research-tokenizacion-custodia-y-bancos", {"R26", "R44", "R19"}, ()),
    ("04-research-xrpl-stellar-y-ripple", {"R32", "R33", "R34", "R43", "R45", "R09P"}, ()),
    ("05-research-fondos-etf-y-derivados", {"R21", "R21b", "R23", "R27", "R42"}, ()),
    ("06-research-jurisdicciones-y-brics", {"R02", "R02P", "R03P", "R04P", "R05P", "R06P", "R07P", "R30"}, ("matriz-jurisdicciones", "calendario-regiones")),
    ("07-research-regulacion-y-fiscalidad", {"R18", "R35", "R20"}, ()),
    ("08-research-macro-y-geopolitica", {"R29", "R41", "R46"}, ()),
    ("09-research-eventos-y-washouts", {"R48", "R49", "R14", "R13", "R15"}, ()),
    ("10-research-auditorias-y-verificacion", {"R11P", "R12P", "R22", "R31", "R38", "R39", "R16", "R10", "R37", "R17", "R36"}, ()),
    ("11-research-radar-y-cruces", set(), ("radar", "cruce-fichas", "glosario")),
]


def palabras(texto):
    return len(re.findall(r"\S+", texto))


def md_de(carpeta, patron="*.md"):
    base = RAIZ / carpeta
    if not base.exists():
        return []
    return [p for p in sorted(base.rglob(patron)) if not any(x in p.parts for x in EXCLUIR)]


def id_informe(p):
    m = re.search(r"-(R\d+[Pb]?)-", p.name) or re.search(r"-(R\d+[Pb]?)\.md$", p.name)
    return m.group(1) if m else None


def explorador_a_markdown():
    """Convierte datos.json y regulacion.json del Explorador en texto legible."""
    out = []
    p = RAIZ / "explorador" / "datos.json"
    if p.exists():
        d = json.loads(p.read_text(encoding="utf-8"))
        out.append("# Explorador de raíles: capas, hechos y fichas\n")
        out.append(d.get("aviso", "") + "\n")
        for c in d["capas"]:
            out.append(f"\n## Capa: {c['nombre']}\n{c['resumen']}\n")
            for k, tit in (("produccion", "En producción"), ("piloto", "Piloto o prueba"), ("plan", "Plan o propuesta"), ("xrp", "¿Nombra XRP o XLM?")):
                v = c.get(k)
                if isinstance(v, str):
                    out.append(f"- {tit}: {v}")
                else:
                    for h in v or []:
                        out.append(f"- {tit}: {h['t']} [{h.get('n') or h.get('k') or 'sin etiqueta'}]")
            for x in c.get("cifras", []):
                out.append(f"- Cifra: {x['v']} {x['e']} ({x['f']})")
            fi = c.get("ficha")
            if fi:
                out.append(f"\n### Ficha del analista ({c['nombre']})\n- Qué hace: {fi['hace']}\n- Quién la controla: {fi['controla']}\n- Madurez {fi['madurez']['n']}/5 (valoración propia): {fi['madurez']['t']}")
                for k, tit in (("falta", "Qué falta"), ("favor", "A favor"), ("contra", "En contra"), ("vigilar", "Qué vigilar")):
                    for t in fi.get(k, []):
                        out.append(f"- {tit}: {t}")
        out.append("\n## Hechos fechados\n")
        for m in sorted(d["movimientos"], key=lambda x: x["fecha"]):
            out.append(f"- {m['fecha']} · {m['actor']} ({m['capa']}): {m['texto']} [{m['estado']}; fuente: {m['fuente']}]")
    p = RAIZ / "explorador" / "regulacion.json"
    if p.exists():
        r = json.loads(p.read_text(encoding="utf-8"))
        nj = {j["id"]: j["nombre"] for j in r["jurisdicciones"]}
        nt = {t["id"]: t["nombre"] for t in r["temas"]}
        out.append("\n\n# Radar regulatorio por jurisdicción y tema\n" + r.get("aviso", "") + "\n")
        for c in r["celdas"]:
            est = f"etapa {c['etapa']}" if c["etapa"] is not None else (f"dirección {c.get('dir')} {c.get('valor') or ''}".strip() if c.get("dir") else "sin dato")
            out.append(f"\n## {nj[c['jur']]} · {nt[c['tema']]} ({est}, fuente {c['fuente']}, último cambio {c.get('fecha')})\n{c['estado']}")
            if c.get("proxima"):
                out.append(f"- Próxima fecha: {c['proxima']['fecha']} · {c['proxima']['que']}")
            if c.get("falta"):
                out.append(f"- Qué falta: {c['falta']}")
            for h in c.get("hitos", []):
                out.append(f"- Hito {h['fecha']}: {h['que']}")
            if c.get("informes"):
                out.append("- Informes: " + ", ".join(c["informes"]))
        for h in r.get("huecos", []):
            out.append(f"- Hueco: {h['zona']}: {h['nota']}")
    return "\n".join(out) if out else None


def construir():
    """Devuelve una lista de (nombre del paquete, [(origen, texto)])."""
    paquetes, usados = [], set()

    def tomar(nombre, rutas):
        rutas = [p for p in rutas if p not in usados]
        if rutas:
            usados.update(rutas)
            paquetes.append((nombre, [(str(p.relative_to(RAIZ)).replace("\\", "/"), p.read_text(encoding="utf-8", errors="replace")) for p in rutas]))

    research = md_de("informes/research")
    for nombre, ids, nombres in GRUPOS_RESEARCH:
        tomar(nombre, [p for p in research if (id_informe(p) in ids) or any(n in p.name for n in nombres)])
    tomar("12-research-otros", research)
    dossiers = md_de("informes/dossiers")
    guias = [p for p in dossiers if re.search(r"-G\d+-", p.name)]
    tomar("13-dossiers-de-actualidad", [p for p in dossiers if p not in guias])
    tomar("14-guias-G1-a-G9-finanzas-basicas", [p for p in guias if re.search(r"-G[1-9]-", p.name)])
    tomar("15-guias-G10-a-G17-patrimonio-fiscalidad-y-noticias", guias)
    tomar("16-videos-informes", md_de("informes/videos"))
    tomar("17-cerebro-documentos", md_de("cerebro/documentos"))
    tomar("18-cerebro-actualidad-semanal", md_de("cerebro/actualidad"))
    tomar("19-cerebro-apunte-principal", [p for p in md_de("cerebro") if p.name.startswith("apuntes_")])
    diarios = [p for p in sorted((RAIZ / "informes").glob("*.md"))]
    tomar("20-informes-diarios-y-auditorias", diarios)
    tomar("21-research-metodo-y-cola", [p for p in sorted((RAIZ / "research").glob("*.md")) if p.name != "notebooklm-estado.md"])
    ex = explorador_a_markdown()
    if ex:
        paquetes.append(("22-explorador-datos-fichas-y-radar", [("explorador/datos.json y explorador/regulacion.json", ex)]))
    return paquetes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--listar", action="store_true", help="solo muestra el contenido de cada paquete")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    paquetes = construir()
    previo = {}
    man = SALIDA / "manifiesto.json"
    if man.exists():
        try:
            previo = json.loads(man.read_text(encoding="utf-8"))
        except Exception:
            previo = {}
    hoy = date.today().isoformat()
    nuevo, total = {}, 0
    if not a.listar:
        SALIDA.mkdir(parents=True, exist_ok=True)
    print(f"{'paquete':<62}{'archivos':>9}{'palabras':>10}  estado")
    for nombre, fuentes in paquetes:
        cuerpo = [f"# {nombre}\n\nPaquete generado el {hoy} desde el repositorio cartera-github. Informativo: no es recomendación de compra ni venta. "
                  f"Etiquetas: [P] fuente oficial leída; [S] secundaria o agregador; [VERIFICAR] sin confirmar; [ESPECULACIÓN] inferencia.\n"]
        for origen, texto in fuentes:
            cuerpo.append(f"\n\n---\n## FUENTE: {origen}\n\n{texto}")
        texto = "".join(cuerpo)
        n = palabras(texto)
        # Si un paquete pasara del límite se avisa (hoy ninguno se acerca)
        h = hashlib.sha256(texto.encode("utf-8")).hexdigest()[:12]
        estado = "nuevo" if nombre not in previo else ("cambiado" if previo[nombre]["hash"] != h else "igual")
        nuevo[nombre] = {"hash": h, "palabras": n, "archivos": len(fuentes)}
        total += n
        aviso = "  ¡SUPERA EL LÍMITE!" if n > PALABRAS_MAX else ""
        print(f"{nombre:<62}{len(fuentes):>9}{n:>10}  {estado}{aviso}")
        if not a.listar:
            (SALIDA / f"{nombre}.md").write_text(texto, encoding="utf-8", newline="\n")
    print(f"\n{len(paquetes)} paquetes, {total:,} palabras en total.".replace(",", "."))
    if not a.listar:
        man.write_text(json.dumps(nuevo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"Escritos en {SALIDA.relative_to(RAIZ)}. Sube solo los marcados «nuevo» o «cambiado».")
    return 0


if __name__ == "__main__":
    sys.exit(main())
