"""Maqueta en PDF (A4, formato compacto) los dossiers, las guías, el cerebro y los informes de vídeos. SIN IA, 0 tokens.

Uso (desde la carpeta del repo; uv instala `markdown` de forma temporal, no toca tu Python):
    uv run --with markdown python scripts/maquetar_pdf.py              # regenera TODOS los PDFs
    uv run --with markdown python scripts/maquetar_pdf.py tomo6        # solo uno (tomo1..tomo8)
Salida: informes/pdf/*.pdf. Necesita Microsoft Edge o Google Chrome instalado (se usa en modo sin ventana).
Cuando cambien dossiers, guías, apuntes del cerebro o informes de vídeos, se vuelve a ejecutar para actualizar los PDFs.
"""
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent.parent
DOS = RAIZ / "informes" / "dossiers"
SAL = RAIZ / "informes" / "pdf"

CSS = """
@page{size:A4;margin:10mm 11mm 10mm 11mm}
body{font-family:Arial,Helvetica,sans-serif;font-size:9.5pt;line-height:1.28;color:#111}
p,li{margin:3px 0}ul,ol{margin:3px 0;padding-left:20px}
h1{font-size:15pt;border-bottom:2px solid #123;padding-bottom:4px;margin-top:0}
h2{font-size:12pt;color:#123;margin:12px 0 4px;border-bottom:1px solid #aaa;page-break-after:avoid}
h3{font-size:10.5pt;color:#234;margin:8px 0 3px;page-break-after:avoid}
table{border-collapse:collapse;width:100%;font-size:8.5pt;margin:5px 0}
tr{page-break-inside:avoid}th,td{border:1px solid #999;padding:2px 4px;vertical-align:top}th{background:#e8edf2}
blockquote{border-left:4px solid #789;background:#f3f5f7;margin:5px 0;padding:4px 8px;font-size:9pt}
code{font-family:Consolas,monospace;font-size:9pt;background:#f0f0f0;padding:0 2px}
.ver{color:#0a6b2a;font-weight:bold}.esp{color:#8a4b00;font-weight:bold}
.ok{color:#fff;background:#0a6b2a;padding:0 3px;border-radius:2px;font-weight:bold}
.portada{text-align:center;padding-top:90mm;page-break-after:always}.portada h1{border:0;font-size:20pt}
.doc{page-break-before:always}.toc{font-size:10pt}.toc li{margin:2px 0}
"""


def etiquetas(h):
    h = re.sub(r"\[VERIFICAR[^\]]*\]", lambda m: f'<span class="ver">{m.group(0)}</span>', h)
    h = re.sub(r"\[ESPECULACI[ÓO]N[^\]]*\]", lambda m: f'<span class="esp">{m.group(0)}</span>', h)
    h = re.sub(r"\[(VERIFICADO|CONFIRMADO|ACTUALIZADO)[^\]]*\]", lambda m: f'<span class="ok">{m.group(0)}</span>', h)
    return h


def md_a_html(ruta):
    t = ruta.read_text(encoding="utf-8")
    t = re.sub(r"^---\n.*?\n---\n", "", t, count=1, flags=re.S)       # quita la cabecera YAML de los apuntes
    t = re.sub(r"\[\[([^\]]+)\]\]", r"\1", t)                          # [[enlaces internos]] como texto
    t = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]*\.md[^)]*\)", r"\1", t)  # enlaces a otros .md como texto
    return etiquetas(markdown.markdown(t, extensions=["tables", "fenced_code", "sane_lists"]))


def titulo(ruta):
    for l in ruta.read_text(encoding="utf-8").splitlines():
        if l.startswith("# "):
            return re.sub(r"[*`]", "", l[2:]).strip()
    return ruta.stem


def lista(patron, carpeta=DOS):
    return sorted(carpeta.glob(patron))


def tomos():
    cer = RAIZ / "cerebro" / "documentos"
    return {
        "tomo1": ("Tomo1-Dossiers-de-actualidad", "Tomo 1 · Dossiers de actualidad (XRP, XLM, cripto y macro)", "Elaborados el 9-oct-2026, auditados el 13-oct-2026",
                  [p for p in lista("2026-10-09-*.md") if "estres" not in p.name] + lista("2026-10-09-prueba-de-estres.md")),
        "tomo2": ("Tomo2-Guias-G1-G5", "Tomo 2 · Guías G1-G5", "Tipos e inflación, bancos, avales e hipotecas, renta fija, acciones y fondos",
                  sum((lista(f"2026-10-*-G{n}-*.md") for n in range(1, 6)), [])),
        "tomo3": ("Tomo3-Guias-G6-G9", "Tomo 3 · Guías G6-G9", "Pensiones y seguros, derivados, inmobiliaria, commodities",
                  sum((lista(f"2026-10-*-G{n}-*.md") for n in range(6, 10)), [])),
        "tomo4": ("Tomo4-Guias-G10-G12", "Tomo 4 · Guías G10-G12", "Pymes y autónomos, startups, fiscalidad completa",
                  sum((lista(f"2026-10-*-G{n}-*.md") for n in range(10, 13)), [])),
        "tomo5": ("Tomo5-Guias-G13-G15", "Tomo 5 · Guías G13-G15", "Gestión patrimonial, errores y sesgos, elegir asesor y entidad",
                  sum((lista(f"2026-10-*-G{n}-*.md") for n in range(13, 16)), [])),
        "tomo6": ("Tomo6-Cerebro-apuntes", "Tomo 6 · Cerebro: apuntes y lecciones", "Apuntes del cerebro (incluye los de vídeos) y lecciones de las sesiones de research",
                  lista("*.md", cer)),
        "tomo7": ("Tomo7-Informes-de-videos", "Tomo 7 · Informes de vídeos", "Informes de research sobre vídeos (informes/videos)",
                  lista("*.md", RAIZ / "informes" / "videos")),
        "tomo8": ("Tomo8-Research-global", "Tomo 8 · Research global (jurisdicciones, BRICS, BIS, Ripple/Stellar, 13F, auditorías)",
                  "Matriz por jurisdicción primero; después los informes de informes/research por orden de fecha",
                  [p for p in lista("*matriz-jurisdicciones*.md", RAIZ / "informes" / "research")]
                  + [p for p in lista("*.md", RAIZ / "informes" / "research") if "matriz-jurisdicciones" not in p.name]),
    }


def navegador():
    for ruta in (r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
                 r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
        if Path(ruta).exists():
            return ruta
    return shutil.which("msedge") or shutil.which("google-chrome") or shutil.which("chromium")


def hacer(nombre, tit, sub, archivos, nav):
    archivos = [a for a in archivos if a.exists()]
    if not archivos:
        print(f"- {nombre}: sin archivos, se omite")
        return
    toc, cuerpo = "", ""
    for i, a in enumerate(archivos):
        toc += f'<li><a href="#d{i}">{titulo(a)}</a></li>'
        cuerpo += f'<section class="doc" id="d{i}">{md_a_html(a)}</section>'
    html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><title>{tit}</title><style>{CSS}</style><body>'
            f'<div class="portada"><h1>{tit}</h1><p>{sub}</p><p><b>Generado el {datetime.now():%d-%m-%Y %H:%M}</b></p><p><b>No es recomendación de inversión ni asesoramiento fiscal.</b><br>'
            '<span class="ver">[VERIFICAR]</span> dato sin confirmar en fuente primaria · <span class="esp">[ESPECULACIÓN]</span> opinión o previsión · '
            '<span class="ok">[VERIFICADO fecha]</span> confirmado en esa fecha</p></div>'
            f'<h2>Contenido de este tomo</h2><ol class="toc">{toc}</ol>{cuerpo}</body></html>')
    SAL.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        h = Path(tmp) / "t.html"
        h.write_text(html, encoding="utf-8")
        salida = SAL / f"{nombre}.pdf"
        if salida.exists():
            salida.unlink()  # si el navegador falla, que se note (antes quedaba el PDF viejo y se daba por bueno)
        # perfil temporal propio: así funciona aunque Edge/Chrome ya estén abiertos en el ordenador
        perfil = Path(tmp) / "perfil"
        subprocess.run([nav, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--user-data-dir={perfil}",
                        f"--print-to-pdf={salida}", h.as_uri()], capture_output=True, timeout=240)
        # el navegador termina antes de acabar de escribir el PDF: esperar a que aparezca y deje de crecer
        ultimo, estable = -1, 0
        for _ in range(240):
            tam = salida.stat().st_size if salida.exists() else 0
            estable = estable + 1 if (tam > 0 and tam == ultimo) else 0
            if estable >= 3:
                break
            ultimo = tam
            time.sleep(0.5)
    print(f"- {nombre}.pdf: {len(archivos)} documentos, {salida.stat().st_size // 1024} KB" if salida.exists() else f"- {nombre}: FALLÓ")


def main():
    nav = navegador()
    if not nav:
        sys.exit("No encuentro Edge ni Chrome.")
    cfg = tomos()
    pedidos = [a.lower() for a in sys.argv[1:]] or list(cfg)
    for k in pedidos:
        if k in cfg:
            hacer(*cfg[k], nav)
        else:
            print(f"- '{k}' no existe. Opciones: {', '.join(cfg)}")


if __name__ == "__main__":
    main()
