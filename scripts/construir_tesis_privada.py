"""Vista privada de la tesis (C205): privado/tesis-vista.html, solo en tu PC (privado/ no se sube a GitHub).

- La tesis es una LENTE, no una vara de medir: cada premisa del contraste (privado/contraste-tesis.json) se reparte en
  tres columnas (a favor / en contra / sin dato) según el veredicto que ya tiene; aquí no se reclasifica nada.
- Debajo de cada capa va la evidencia PÚBLICA del Explorador (movimientos, voces y radar regulatorio) con su enlace.
  Lo publicado después de la fecha del contraste sale como «Nuevo, sin clasificar»: decides tú si suma, resta o nada.
- Sin IA, sin red, sin claves. Se niega a escribir si privado/ dejara de estar en .gitignore.
Uso: python scripts/construir_tesis_privada.py   (y abre privado/tesis-vista.html con doble clic)"""
import html
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PRIVADO = RAIZ / "privado"
SALIDA = PRIVADO / "tesis-vista.html"
EXP = RAIZ / "explorador"
MARCA = "marca-tesis-privada-c205"          # la busca huellas_privado.py: si apareciera en docs/, salta el aviso
TEMA_REG = {"stable": "stablecoins", "token": "tokenizacion", "custodia": "custodia", "cbdc": "cbdc",
            "fondos": "etf", "reg": "ley_marco", "deposit": "tokenizacion"}
VEREDICTO = {"respaldado": ("Respaldado", "ok"), "parcial": ("Parcial", "med"), "contradicho": ("Contradicho", "mal"),
             "no_comprobable": ("No comprobable", "nd"), "sin_respaldo": ("Sin respaldo", "nd")}
MAX_EVID = 8


def e(t):
    return html.escape(str(t if t is not None else ""))


def enlace(url, texto):
    url = str(url or "")
    if url.startswith(("https://", "http://")):
        return f'<a href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(texto)}</a>'
    if url.startswith(("informes/", "cerebro/", "research/")) and ".." not in url:
        return f'<a href="../{e(url)}">{e(texto)}</a>'       # ruta del repo: se abre en local desde privado/
    return e(texto)


def leer(ruta):
    return json.loads(ruta.read_text(encoding="utf-8"))


def comprobar_privado():
    if SALIDA.resolve().parent != PRIVADO.resolve():
        sys.exit("La salida no está dentro de privado/: no se escribe.")
    r = subprocess.run(["git", "check-ignore", "-q", str(SALIDA.relative_to(RAIZ).as_posix())], cwd=RAIZ, timeout=20)
    if r.returncode != 0:
        sys.exit("privado/ NO está en .gitignore: no se escribe la tesis (el repo es público).")


def tarjeta(p):
    nom, cls = VEREDICTO.get(p.get("veredicto"), (p.get("veredicto") or "?", "nd"))
    ev = p.get("evidencia") or []
    ev = ev if isinstance(ev, list) else [{"t": ev}]
    lis = "".join(f'<li><span class="niv">[{e(x.get("nivel", "?"))}]</span> {e(x.get("t"))}'
                  + (f' <span class="fu">· {e(x.get("fuente"))}</span>' if x.get("fuente") else "") + "</li>"
                  for x in ev if isinstance(x, dict))
    esp = ' <span class="esp">[ESPECULACIÓN]</span>' if p.get("especulacion") else ""
    return (f'<div class="card"><div class="cab"><span class="ver {cls}">{e(nom)}</span>{esp}</div>'
            f'<p class="punto">{e(p.get("punto"))}</p><p class="raz">{e(p.get("razonamiento"))}</p>'
            + (f'<ul>{lis}</ul>' if lis else "") + "</div>")


def columnas(puntos):
    favor = [p for p in puntos if p.get("veredicto") in ("respaldado", "parcial")]
    contra = [p for p in puntos if p.get("veredicto") in ("contradicho", "parcial")]
    nd = [p for p in puntos if p.get("veredicto") not in ("respaldado", "parcial", "contradicho")]
    falta = [p.get("abierto") for p in puntos if p.get("abierto")]
    col = lambda t, cls, xs, extra="": (f'<div class="col"><h4 class="{cls}">{t} ({len(xs)})</h4>'
                                        + ("".join(tarjeta(p) for p in xs) or '<p class="vacio">Nada.</p>') + extra + "</div>")
    extra = ('<div class="falta"><b>Qué falta para saberlo</b><ul>' + "".join(f"<li>{e(f)}</li>" for f in falta) + "</ul></div>") if falta else ""
    return ('<div class="cols">' + col("A favor", "ok", favor) + col("En contra", "mal", contra)
            + col("Sin dato", "nd", nd, extra) + "</div>")


def evidencia_publica(capa, desde, hoy, movs, voces, celdas):
    """Evidencia del Explorador para una capa: (nuevos desde el contraste, contexto anterior). Cada fila: (fecha, html)."""
    filas = []
    for m in movs:
        if m.get("capa") == capa and m.get("fecha", "") <= hoy:
            filas.append((m["fecha"], f'<span class="niv">[{e(m.get("nivel") or "?")}]</span> <b>{e(m.get("actor"))}</b>: '
                          f'{e(m.get("texto"))} <span class="fu">· {enlace(m.get("informe"), m.get("fuente") or "informe")}</span>'))
    for v in voces:
        if capa in (v.get("capas") or []) and v.get("conf") == "confirmada" and str(v.get("cuando", "")) <= hoy:
            f = v.get("fuente") or {}
            filas.append((str(v.get("cuando")), f'<span class="niv">[{e(v.get("nivel") or "?")}]</span> <b>Voz · {e(v.get("quien"))}</b>: '
                          f'{e(v.get("texto"))} <span class="fu">· {enlace(f.get("url"), f.get("n") or "fuente")}</span>'))
    tema = TEMA_REG.get(capa)
    for c in celdas:
        if tema and c.get("tema") == tema and c.get("fecha") and c.get("etapa") is not None and c["fecha"] <= hoy:
            filas.append((c["fecha"], f'<span class="niv">[{e(c.get("nivel") or c.get("fuente") or "?")}]</span> '
                          f'<b>Radar · {e(str(c.get("jur", "")).upper())}</b> (etapa {e(c.get("etapa"))}): {e(str(c.get("estado", ""))[:260])} '
                          f'<span class="fu">· {enlace(c.get("url"), "fuente")}</span>'))
    filas.sort(key=lambda x: x[0], reverse=True)
    nuevos = [f for f in filas if f[0] > desde]
    viejos = [f for f in filas if f[0] <= desde]
    return nuevos, viejos


def lista(filas, n):
    if not filas:
        return '<p class="vacio">Nada en el Explorador.</p>'
    mas = f'<p class="vacio">… y {len(filas) - n} más en el Explorador.</p>' if len(filas) > n else ""
    return "<ul>" + "".join(f'<li><span class="fe">{e(f)}</span> {h}</li>' for f, h in filas[:n]) + "</ul>" + mas


# ------------------------------------------------------------------ marco ISO 20022 y tokenización (privado/marco-iso20022.json)
TOKEN_CLS = {"sí": "si", "no": "no", "mínimo": "min", "parcial": "min", "opcional": "min", "sin dato": "nd"}
CAPTURA_CLS = {"alta": "si", "media": "min", "baja": "no", "incierta": "nd"}


def evid(x, voces_id):
    """Un dato del marco: texto + [nivel] + fuente enlazada + fecha. x: {t, f, u|i|v, d, n}."""
    if not isinstance(x, dict):
        return '<span class="vacio">sin dato</span>'
    v = voces_id.get(x.get("v")) if x.get("v") else None
    url = x.get("u") or x.get("i") or ((v or {}).get("fuente") or {}).get("url")
    fecha = x.get("d") or (v or {}).get("cuando") or ""
    fuente = x.get("f") or ""
    return (f'<span class="niv">[{e(x.get("n", "?"))}]</span> {e(x.get("t"))} '
            f'<span class="fu">· {enlace(url, fuente or "fuente")}{(" · " + e(fecha)) if fecha else ""}</span>')


def seccion_marco(m, voces_id, celdas):
    caps, capas = m.get("capacidades", []), m.get("capas", [])
    cad = m.get("cadenas", [])
    h = [f'<section id="marco"><h2>Marco ISO 20022 y tokenización</h2>'
         f'<div class="lente">{e(m.get("leyenda"))} Versión {e(m.get("version"))}. Qué aporta cada cadena y si la institución '
         f'necesita el token; no hay ranking ni ganador.</div>']
    h.append("<h3>Qué es hecho sobre ISO 20022</h3><ul>" + "".join(f"<li>{evid(x, voces_id)}</li>" for x in m.get("hechos_iso", [])) + "</ul>")
    # afirmaciones de Joel
    h.append("<h3>Dos afirmaciones comprobadas [J]</h3>")
    for a in m.get("afirmaciones", []):
        h.append(f'<div class="card"><p class="punto">{e(a["j"])}</p><p><span class="ver med">{e(a["veredicto"])}</span></p>'
                 f'<p class="raz">{e(a["detalle"])}</p><ul>' + "".join(f"<li>{evid(x, voces_id)}</li>" for x in a.get("e", [])) + "</ul></div>")
    # métrica RWA
    r = m.get("metrica_rwa", {})
    num = lambda v: "—" if v is None else f"{v:,.1f}".replace(",", " ").replace(".", ",")
    filas = "".join(f'<tr><td>{e(x["cadena"])}</td><td class="num">{num(x.get("dist"))}</td><td class="num">{num(x.get("rep"))}</td>'
                    f'<td class="num">{num(x.get("stable"))}</td></tr>' for x in r.get("filas", []))
    h.append(f'<h3>Valor tokenizado por cadena (M$)</h3><p class="fu">{e(r.get("nota"))} {enlace(r.get("u"), r.get("f", ""))} · {e(r.get("d"))} [{e(r.get("n"))}]. {e(r.get("totales", ""))}</p>'
             f'<div class="tabla"><table><tr><th>Cadena</th><th>Distribuido</th><th>Representado</th><th>Stablecoins</th></tr>{filas}</table></div>')
    # matriz de capacidades
    cab = "".join(f"<th>{e(c['n'])}</th>" for c in caps)
    filas = "".join(f'<tr><th class="fila">{e(c["nombre"])}<br><span class="fu">{e(c["token"])}</span></th>'
                    + "".join(f'<td>{evid((c.get("matriz") or {}).get(k["id"]), voces_id)}</td>' for k in caps) + "</tr>" for c in cad)
    h.append(f'<h3>Matriz de capacidades</h3><p class="fu">Por capacidad, no por ranking. «sin dato» = no encontrado con fuente; nunca relleno.</p>'
             f'<div class="tabla"><table class="matriz"><tr><th>Cadena</th>{cab}</tr>{filas}</table></div>')
    # capas: ¿la usa la institución y necesita el token?
    cab = "".join(f"<th>{e(c['n'])}</th>" for c in capas)
    filas = ""
    for c in cad:
        celdas_c = ""
        for k in capas:
            x = (c.get("capas") or {}).get(k["id"]) or {}
            tok = str(x.get("token") or "sin dato")
            cls = next((v for kk, v in TOKEN_CLS.items() if tok.startswith(kk)), "nd")
            celdas_c += (f'<td><span class="tok {cls}">token: {e(tok)}</span>'
                         + (f'<br><b class="fu">{e(x["quien"])}</b>' if x.get("quien") else "")
                         + (f'<br><span class="fu">{e(x.get("ev"))}</span>' if x.get("ev") else "") + "</td>")
        cap = c.get("captura") or {}
        filas += (f'<tr><th class="fila">{e(c["nombre"])}<br><span class="fu">{e(c["token"])} · {e(c.get("tipo"))}</span></th>{celdas_c}'
                  f'<td><span class="tok {CAPTURA_CLS.get(cap.get("nivel"), "nd")}">{e(cap.get("nivel", "—"))}</span></td></tr>')
    h.append(f'<h3>Capas: ¿la usa la institución y NECESITA el token?</h3><p class="fu">«token: sí» = el uso consume o exige el token '
             f'(comisiones, quema, staking, colateral); «mínimo» = solo comisiones o reservas pequeñas; «no» = prescindible. '
             f'La última columna es la captura de valor [RAZONADO].</p>'
             f'<div class="tabla"><table class="matriz"><tr><th>Cadena</th>{cab}<th>Captura del token</th></tr>{filas}</table></div>')
    # fichas
    h.append("<h3>Fichas por cadena</h3>")
    for c in cad:
        cap = c.get("captura") or {}
        lst = lambda xs: ("<ul>" + "".join(f"<li>{e(x)}</li>" for x in xs) + "</ul>") if xs else '<p class="vacio">Sin dato.</p>'
        h.append(f'<details class="ficha"><summary><b>{e(c["nombre"])}</b> · {e(c["token"])} · captura '
                 f'<span class="tok {CAPTURA_CLS.get(cap.get("nivel"), "nd")}">{e(cap.get("nivel", "—"))}</span></summary>'
                 f'<p><b>Qué aporta:</b> {e(c.get("aporta"))}</p><p><b>Relación con ISO 20022 (lo que existe de verdad):</b></p>'
                 f'<ul>' + "".join(f"<li>{evid(x, voces_id)}</li>" for x in c.get("iso", [])) + "</ul>"
                 f'<div class="cols"><div class="col"><h4 class="ok">A favor</h4>{lst(c.get("favor"))}</div>'
                 f'<div class="col"><h4 class="mal">En contra</h4>{lst(c.get("contra"))}</div>'
                 f'<div class="col"><h4 class="nd">Sin dato</h4>{lst(c.get("sin_dato"))}<b>Qué lo refutaría</b>{lst(c.get("refutaria"))}</div></div>'
                 f'<p class="raz"><b>Captura de valor:</b> {e(cap.get("razon"))}</p>'
                 + (f'<p class="fu">Supuestos: {e("; ".join(cap.get("supuestos") or []))}</p>' if cap.get("supuestos") else "")
                 + f'<p class="fu"><b>Sesgos de las fuentes:</b> {e(c.get("sesgos"))}</p></details>')
    # complementariedad y riesgos
    h.append("<h3>Complementariedad [RAZONADO]</h3><ul>" + "".join(
        f'<li><b>{e(x["combo"])}</b> → {e(x["cubre"])}. <span class="raz">{e(x["razon"])}</span></li>' for x in m.get("complementariedad", [])) + "</ul>")
    h.append('<h3>Riesgos de concentración y de contraparte por capacidad</h3><div class="tabla"><table><tr><th>Capacidad</th><th>Concentración</th><th>Contraparte</th></tr>'
             + "".join(f'<tr><td>{e(x["cap"])}</td><td>{e(x["concentracion"])}</td><td>{e(x["contraparte"])}</td></tr>' for x in m.get("riesgos_capacidad", []))
             + "</table></div>")
    # regulación por país desde el Radar
    rp = m.get("regulacion_paises") or {}
    idx = {(c.get("jur"), c.get("tema")): c for c in celdas}
    cab = "".join(f"<th>{e(t)}</th>" for t in rp.get("temas", []))
    filas = ""
    for j in rp.get("jur", []):
        fila = ""
        for t in rp.get("temas", []):
            c = idx.get((j, t)) or {}
            fila += (f'<td>{enlace(c.get("url"), str(c["etapa"]))} <span class="fu">{e(c.get("fecha") or "")} [{e(c.get("nivel") or c.get("fuente") or "?")}]</span></td>'
                     if c.get("etapa") is not None else '<td class="vacio">sin dato</td>')
        filas += f"<tr><th class='fila'>{e(j.upper())}</th>{fila}</tr>"
    h.append(f'<h3>Madurez regulatoria por país</h3><p class="fu">{e(rp.get("nota"))} Fuente: {e(rp.get("f"))}.</p>'
             f'<div class="tabla"><table><tr><th>Jurisdicción</th>{cab}</tr>{filas}</table></div>')
    hc = m.get("huecos_c263") or {}
    if hc:
        li = ""
        for x in hc.get("resultados", []):
            fu = " · ".join(enlace(s.get("u"), s.get("f") or "fuente") + f' <span class="fu">{e(s.get("d") or "")} [{e(s.get("n") or "?")}]</span>' for s in x.get("e", []))
            li += f"<li><b>{e(x.get('hueco'))}</b> — <i>{e(x.get('estado'))}</i>. {e(x.get('detalle'))} {fu}</li>"
        h.append(f'<h3>Cierre de huecos (C263, {e(hc.get("fecha"))})</h3><p class="fu">{e(hc.get("nota"))}</p><ol>{li}</ol>')
    h.append('<h3>Huecos [VERIFICAR] pendientes</h3><ol>' + "".join(f"<li>{e(x)}</li>" for x in m.get("huecos", [])) + "</ol></section>")
    return "".join(h)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    comprobar_privado()
    try:
        con = leer(PRIVADO / "contraste-tesis.json")
    except FileNotFoundError:
        sys.exit("No existe privado/contraste-tesis.json (la tesis solo vive en tu PC).")
    datos = leer(EXP / "datos.json")
    voces = leer(EXP / "voces.json").get("voces", [])
    celdas = leer(EXP / "regulacion.json").get("celdas", [])
    nombres = {c["id"]: c.get("nombre", c["id"]) for c in datos.get("capas", [])}
    desde = str(con.get("version", "2000-01-01"))[:10]
    hoy = date.today().isoformat()
    tesis = sorted(PRIVADO.glob("*tesis-viva*.md"))
    tesis_link = f'<a href="{e(tesis[-1].name)}">{e(tesis[-1].name)}</a>' if tesis else "—"

    total_nuevos = 0
    secciones = [f'<section><h2>Premisas generales</h2>{columnas(con.get("generales", []))}</section>']
    for capa, puntos in (con.get("capas") or {}).items():
        nuevos, viejos = evidencia_publica(capa, desde, hoy, datos.get("movimientos", []), voces, celdas)
        total_nuevos += len(nuevos)
        secciones.append(
            f'<section id="{e(capa)}"><h2>{e(nombres.get(capa, capa))}</h2>{columnas(puntos)}'
            f'<details open><summary>Nuevo, sin clasificar ({len(nuevos)} desde el {e(desde)})</summary>{lista(nuevos, MAX_EVID)}</details>'
            f'<details><summary>Evidencia pública anterior al contraste ({len(viejos)})</summary>{lista(viejos, MAX_EVID)}</details></section>')
    try:                                  # marco ISO 20022 y tokenización (tesis multi-cadena, 14-nov-2026)
        marco = leer(PRIVADO / "marco-iso20022.json")
    except FileNotFoundError:
        marco = None
    if marco:
        voces_id = {v.get("id"): v for v in voces}
        secciones.append(seccion_marco(marco, voces_id, celdas))
    indice = ('<a href="#marco">Marco ISO 20022 y tokenización</a> · ' if marco else "") + " · ".join(
        f'<a href="#{e(c)}">{e(nombres.get(c, c))}</a>' for c in (con.get("capas") or {}))
    pagina = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>Tesis privada · vista</title><!-- {MARCA} -->
<style>
:root{{--bg:#050816;--panel:#0d1428;--borde:#1f2a48;--txt:#e6ebf5;--suave:#9aa6c2;--ok:#3ecf8e;--mal:#ff6b6b;--med:#f5b942;--nd:#8ea0c8}}
body{{background:var(--bg);color:var(--txt);font:15px/1.5 system-ui,Segoe UI,sans-serif;margin:0;padding:16px;max-width:1300px;margin:auto}}
a{{color:#7cb4ff}} h1{{font-size:22px;margin:4px 0}} h2{{font-size:18px;border-bottom:1px solid var(--borde);padding-bottom:4px;margin-top:28px}}
.aviso{{background:#2a1020;border:1px solid #6b2340;border-radius:8px;padding:10px 12px;margin:10px 0}}
.lente{{background:var(--panel);border:1px solid var(--borde);border-radius:8px;padding:10px 12px;color:var(--suave)}}
.cols{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}}
.col h4{{margin:8px 0}} h4.ok{{color:var(--ok)}} h4.mal{{color:var(--mal)}} h4.nd{{color:var(--nd)}}
.card{{background:var(--panel);border:1px solid var(--borde);border-radius:8px;padding:10px;margin-bottom:10px}}
.ver{{font-size:12px;padding:1px 8px;border-radius:10px;border:1px solid}} .ver.ok{{color:var(--ok)}} .ver.mal{{color:var(--mal)}} .ver.med{{color:var(--med)}} .ver.nd{{color:var(--nd)}}
.esp{{color:var(--med);font-size:12px}} .punto{{font-weight:600;margin:6px 0}} .raz{{color:var(--suave);margin:4px 0}}
.niv{{color:var(--med);font-size:12px}} .fu,.fe{{color:var(--suave);font-size:13px}} .fe{{font-variant-numeric:tabular-nums}}
ul{{padding-left:18px;margin:6px 0}} li{{margin:3px 0}} .vacio{{color:var(--suave);font-style:italic}}
.falta{{background:var(--panel);border:1px dashed var(--borde);border-radius:8px;padding:8px 10px;font-size:14px}}
details{{margin-top:10px}} summary{{cursor:pointer;color:#cdd6ea}}
h3{{font-size:16px;margin:22px 0 6px}} .tabla{{overflow-x:auto;max-width:100%}}
table{{border-collapse:collapse;font-size:13px;width:100%}} th,td{{border:1px solid var(--borde);padding:6px;vertical-align:top;text-align:left}}
th{{background:#111a33}} th.fila{{min-width:120px}} td.num{{text-align:right;font-variant-numeric:tabular-nums}}
table.matriz td{{min-width:170px}} .ficha{{background:var(--panel);border:1px solid var(--borde);border-radius:8px;padding:8px 12px}}
.tok{{font-size:12px;padding:1px 7px;border-radius:10px;border:1px solid;white-space:nowrap}}
.tok.si{{color:var(--ok)}} .tok.min{{color:var(--med)}} .tok.no{{color:var(--suave)}} .tok.nd{{color:var(--nd)}}
</style></head><body>
<h1>Tesis privada · evidencia a favor, en contra y sin dato</h1>
<div class="aviso">🔒 PRIVADO: este archivo vive en <code>privado/</code> y no se sube a GitHub. No lo copies a docs/ ni a la Órbita.</div>
<div class="lente">La tesis es <b>una lente</b>, no la vara de medir del Explorador. Las columnas usan el veredicto del contraste
(<b>{e(desde)}</b>); lo publicado después queda en «Nuevo, sin clasificar» ({total_nuevos} entradas) hasta que tú decidas.
Etiquetas: [P] fuente primaria · [S] secundaria · [V] verificar. Tesis: {tesis_link}. Generado el {e(hoy)}, sin IA.
No es una recomendación de compra o venta.</div>
<p>{indice}</p>
{''.join(secciones)}
</body></html>"""
    SALIDA.write_text(pagina, encoding="utf-8")
    print(f"privado/tesis-vista.html: {len(pagina) // 1024} KB · {total_nuevos} entradas públicas nuevas sin clasificar (solo en tu PC)")


if __name__ == "__main__":
    main()
