"""Aplana los 5 JSON de España del 17-nov (macro, energía, vivienda, pensiones, investigaciones) a una forma común para la Órbita
y el móvil: secciones con grupos de filas {nombre, valor, unidad, fecha, nivel, fuente, nota}. Solo lee; no escribe ningún JSON de datos.
Uso: import espana_cifras; espana_cifras.construir(carpeta_explorador) -> dict (o None si falta todo)."""
import json
from pathlib import Path

ARCHIVOS = {"macro": "espana-macro", "energia": "espana-energia", "vivienda": "espana-vivienda",
            "pensiones": "espana-pensiones", "investigaciones": "espana-investigaciones"}


def _fila(n, ctx=None, nombre=None):
    ctx = ctx or {}
    nom = nombre or n.get("nombre") or n.get("ccaa") or "—"
    fecha = n.get("periodo") or n.get("anio") or ctx.get("periodo") or ""
    fuente = n.get("fuente") or ctx.get("fuente")
    if not fuente and n.get("serie_ine"):
        fuente = "INE serie " + str(n["serie_ine"])
    if fuente and not str(fuente).startswith("http") and ctx.get("url"):
        fuente = ctx["url"]
    nota = n.get("nota") or ""
    ant = n.get("anterior") or n.get("anterior_sep") or n.get("hace_un_anio")
    if isinstance(ant, dict):
        ant = f"{ant.get('valor')} ({ant.get('periodo', '')})"
    if ant is not None and not isinstance(ant, dict):
        nota = (nota + " " if nota else "") + f"Anterior: {ant}."
    if n.get("ue") is not None:
        nota = (nota + " " if nota else "") + f"UE-27: {n['ue']}."
    return {"nombre": nom, "valor": n.get("valor"), "unidad": n.get("unidad") or ctx.get("unidad") or "", "fecha": str(fecha),
            "nivel": n.get("nivel") or ctx.get("nivel") or "?", "fuente": fuente if (fuente and str(fuente).startswith("http")) else (fuente or ""),
            "nota": nota.strip()}


def _lista(items, ctx=None, titulo_ccaa=False):
    return [_fila(x, ctx) for x in items or [] if isinstance(x, dict)]


def _bloque(b, ctx=None):
    """Un bloque con 'valores' [..] y periodo/publicado/fuente/nivel heredables."""
    c = dict(ctx or {})
    c.update({k: b[k] for k in ("periodo", "nivel") if b.get(k)})
    if b.get("fuente"):
        c["fuente"] = b["fuente"]
    return _lista(b.get("valores"), c)


def _macro(d):
    g = []
    ipc = d.get("ipc", {})
    g.append(("Inflación (IPC)", _lista(ipc.get("general")) + _lista(ipc.get("impuestos_constantes"), {"periodo": ipc.get("periodo")})))
    g.append(("Inflación por grupos (IPC)", _lista(ipc.get("grupos"), {"periodo": ipc.get("periodo"), "nivel": ipc.get("nivel")})))
    epa = d.get("epa", {})
    g.append(("Paro y empleo (EPA)", _lista(epa.get("nacional"), {"periodo": epa.get("periodo")})))
    g.append(("Tasa de paro por comunidad (EPA)", _lista(epa.get("tasa_paro_por_ccaa"), {"periodo": epa.get("periodo"), "nivel": "P"})))
    af = d.get("afiliacion")
    if af:
        g.append(("Afiliación a la Seguridad Social", _bloque(af)))
    s = d.get("salarios_smi", {})
    sa = dict(s.get("salario_medio_aeat") or {})
    sa.setdefault("nombre", "Salario medio (AEAT) / mediano (EAES)")
    g.append(("Salarios y SMI", _lista(s.get("smi")) + _lista(s.get("coste_laboral_etcl")) + _lista([sa])))
    t = d.get("tipos", {})
    th = dict(t.get("tipo_medio_hipotecas") or {})
    th.setdefault("nombre", "Tipo medio de las hipotecas")
    g.append(("Tipos de interés", _lista([t.get("euribor_12m") or {}, th])))
    if d.get("pib"):
        g.append(("PIB (INE, contabilidad trimestral)", _bloque(d["pib"])))
    return g


def _energia(d):
    nom = (("electricidad", "Electricidad"), ("mix_generacion", "Mix de generación"), ("combustibles", "Combustibles"),
           ("dependencia_energetica", "Dependencia energética"), ("embalses", "Embalses"), ("gas", "Gas"))
    return [(t, _lista(d.get(k))) for k, t in nom if d.get(k)]


def _vivienda(d):
    b = d.get("bloques", {})
    f = lambda nombre, valor, unidad, fecha, bl, nota="": {"nombre": nombre, "valor": valor, "unidad": unidad, "fecha": str(fecha), "nivel": bl.get("nivel") or "?",
                                                           "fuente": bl.get("fuente") or "", "nota": nota or bl.get("nota") or ""}
    g = []
    dc = b.get("deuda_ccaa") or {}
    if dc:
        g.append(("Deuda de las comunidades (BdE, PDE)", [f("Deuda total de las CCAA", dc.get("total_meur"), "M€", dc.get("periodo"), dc),
                                                          f("Variación interanual", dc.get("total_var_pct"), "%", dc.get("periodo"), dc, "Frente a jun-2025 (" + str(dc.get("total_jun25_meur")) + " M€). Próxima publicación: " + str(dc.get("proxima_publicacion")))]))
    p = b.get("precio_vivienda_ine_ipv") or {}
    r = b.get("precio_m2_registradores") or {}
    ir = (b.get("alquiler") or {}).get("irav") or {}
    ip = (b.get("alquiler") or {}).get("ipva_2024") or {}
    pre = [f("Precio de la vivienda, variación anual (IPV, INE)", p.get("nacional_var_anual_pct"), "%", p.get("periodo"), p)]
    if r:
        pre += [f("Precio escriturado medio (Registradores)", r.get("espana_eur_m2"), "€/m²", r.get("periodo"), r),
                f("  · vivienda nueva", r.get("nueva_eur_m2"), "€/m²", r.get("periodo"), r, "Precio declarado en escritura."),
                f("  · vivienda usada", r.get("usada_eur_m2"), "€/m²", r.get("periodo"), r, "Precio declarado en escritura."),
                f("  · variación interanual", r.get("var_interanual_12m_pct"), "%", r.get("periodo"), r, "Precio declarado en escritura; no es el IPV.")]
    g.append(("Precios de compra", pre))
    al = []
    if ir:
        for k, et in (("oct_2026_pct", "oct-2026"), ("sep_2026_pct", "sep-2026"), ("ago_2026_pct", "ago-2026")):
            if ir.get(k) is not None:
                al.append(f("IRAV, variación anual · " + et, ir[k], "%", et, ir, "Índice de Referencia de Arrendamientos (serie INE " + str(ir.get("serie_ine")) + "); no es el precio de contratos nuevos."))
    if ip:
        al.append(f("Alquiler (IPVA), variación anual nacional", ip.get("nacional_pct"), "%", ip.get("ultimo_ano_publicado"), ip))
    g.append(("Alquiler", al))
    h = b.get("hipotecas") or {}
    if h:
        g.append(("Hipotecas (INE)", [f("Hipotecas sobre fincas, ago-2026", h.get("n_hipotecas_total_fincas_ago26"), "n.º", "ago-2026", h),
                                      f("Hipotecas sobre fincas, jul-2026", h.get("n_total_fincas_jul26"), "n.º", "jul-2026", h),
                                      f("Tipo de interés medio (viviendas)", h.get("tipo_interes_medio_viviendas_ago26_pct"), "%", "ago-2026", h),
                                      f("  · tipo fijo", h.get("tipo_fijo_viviendas_pct"), "%", "ago-2026", h),
                                      f("  · tipo variable", h.get("tipo_variable_viviendas_pct"), "%", "ago-2026", h)]))
    e = b.get("ejecuciones_hipotecarias") or {}
    if e:
        g.append(("Ejecuciones hipotecarias (INE)", [f("Fincas con inscripción de ejecución", e.get("total_fincas"), "n.º", e.get("anio"), e, "2024: " + str(e.get("total_fincas_2024"))),
                                                      f("  · de ellas, viviendas", e.get("viviendas"), "n.º", e.get("anio"), e, "2024: " + str(e.get("viviendas_2024")))]))
    es = b.get("esfuerzo_alquiler_bde_2024") or {}
    if es:
        rows = []
        for k, et in (("esfuerzo_medio_renta_neta_pct", "Esfuerzo medio (alquiler/hipoteca, % renta neta)"),
                      ("hogares_en_sobresfuerzo_mas_30pct_renta_neta_pct", "Hogares con esfuerzo > 30 % de la renta neta"),
                      ("esfuerzo_medio_grandes_ciudades_pct", "Esfuerzo medio en grandes ciudades")):
            for kk, v in (es.get(k) or {}).items():
                if isinstance(v, (int, float)):
                    rows.append(f(et + " · " + kk.replace("_", " "), v, "%", "2024", es))
        ev = es.get("eurostat_2025_sobresfuerzo_renta_bruta_pct") or {}
        for kk, v in ev.items():
            rows.append(f("Sobresfuerzo (Eurostat, renta bruta) · " + kk, v, "%", "2025", es))
        g.append(("Esfuerzo de los hogares (BdE, Eurostat)", rows))
    return g


def _tabla_vivienda(d):
    rg = ((d.get("bloques") or {}).get("deuda_ccaa") or {}).get("regiones") or []
    return [{"ccaa": r.get("ccaa"), "deuda": r.get("deuda_pde_jun26_meur"), "deuda_1a": r.get("deuda_pde_jun25_meur"), "var": r.get("var_interanual_pct"),
             "pct_pib": r.get("deuda_sobre_pib2025_pct_calculado"), "pct_bde": r.get("deuda_sobre_pib_pct_bde_nota"),
             "ipv": r.get("ipv_2t26_var_anual_pct"), "ipva": r.get("ipva_alquiler_2024_var_pct")} for r in rg]


def _pensiones(d):
    g = []
    for k, t in (("pensiones", "Pensiones (Seguridad Social)"), ("saldo_ss", "Saldo de la Seguridad Social"), ("fondo_reserva", "Fondo de Reserva"),
                 ("gasto_pensiones_pib", "Gasto en pensiones (Eurostat, % PIB)")):
        if isinstance(d.get(k), dict):
            filas = _bloque(d[k], {"url": d[k].get("fuente")})
            if k == "gasto_pensiones_pib" and d[k].get("lectura"):
                filas.append({"nombre": "Lectura", "valor": None, "unidad": "", "fecha": "", "nivel": "P", "fuente": "", "nota": str(d[k]["lectura"])})
            g.append((t, filas))
    dm = d.get("demografia") or {}
    for k, t in (("poblacion", "Población"), ("natalidad", "Natalidad"), ("migracion", "Migración"), ("proyecciones", "Proyecciones (INE 2026-2076)")):
        if dm.get(k):
            g.append((t, _lista(dm[k])))
    return g


def _investigaciones(d):
    casos = []
    for c in d.get("casos", []):
        casos.append({"nombre": c.get("nombre"), "tribunal": c.get("tribunal"), "tipo": c.get("tipo"), "fase": c.get("fase"),
                      "hechos": sorted(({"fecha": h.get("fecha"), "texto": h.get("texto"), "nivel": h.get("nivel") or "?", "fuente": h.get("fuente") or ""}
                                        for h in c.get("hechos_judiciales", [])), key=lambda h: h["fecha"] or "", reverse=True),
                      "prensa": [x if isinstance(x, str) else (x.get("texto") or "") for x in c.get("filtraciones_prensa", [])],
                      "opinion": [x if isinstance(x, str) else (x.get("texto") or "") for x in c.get("opinion", [])],
                      "pendiente": c.get("pendiente", [])})
    return casos


def construir(carpeta):
    carpeta = Path(carpeta)
    fns = {"macro": _macro, "energia": _energia, "vivienda": _vivienda, "pensiones": _pensiones}
    salida = {}
    for k, arch in ARCHIVOS.items():
        try:
            d = json.loads((carpeta / f"{arch}.json").read_text(encoding="utf-8"))
        except Exception:
            continue
        s = {"titulo": d.get("titulo") or d.get("_nota", "")[:80], "leido": d.get("leido") or d.get("actualizado"), "nivel": d.get("nivel"),
             "nota": d.get("nota") or d.get("_nota") or "", "pendiente": d.get("pendiente") or d.get("por_abrir") or []}
        if k == "investigaciones":
            s["casos"] = _investigaciones(d)
            s["remite_a"] = d.get("remite_a", [])
        else:
            s["grupos"] = [{"grupo": t, "filas": f} for t, f in fns[k](d) if f]
            if k == "vivienda":
                s["ccaa"] = _tabla_vivienda(d)
        salida[k] = s
    return salida or None
