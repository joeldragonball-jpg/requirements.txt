"""Aplana los 5 JSON de España del 17-nov (macro, energía, vivienda, pensiones, investigaciones) a una forma común para la Órbita
y el móvil: secciones con grupos de filas {nombre, valor, unidad, fecha, nivel, fuente, nota}. Solo lee; no escribe ningún JSON de datos.
Uso: import espana_cifras; espana_cifras.construir(carpeta_explorador) -> dict (o None si falta todo)."""
import json
import re
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
        ant = f"{str(ant.get('valor')).replace('.', ',')}{' ' + n['unidad'] if n.get('unidad') in ('%', 'M€') else ''} ({ant.get('periodo', '')})" if ant.get("valor") is not None else None
    if ant is not None and not isinstance(ant, dict):
        nota = (nota + " " if nota else "") + f"Anterior: {ant}."
    if n.get("ue") is not None:
        nota = (nota + " " if nota else "") + f"UE-27: {n['ue']}."
    return {"nombre": nom, "valor": n.get("valor"), "unidad": n.get("unidad") or ctx.get("unidad") or "", "fecha": str(fecha),
            "nivel": n.get("nivel") or ctx.get("nivel") or "?", "fuente": fuente if (fuente and str(fuente).startswith("http")) else (fuente or ""),
            "nota": re.sub(r"\bnull\b", "sin dato", nota.strip())}


def _lista(items, ctx=None, titulo_ccaa=False):
    return [_fila(x, ctx) for x in items or [] if isinstance(x, dict)]


def _bloque(b, ctx=None):
    """Un bloque con 'valores' [..] y periodo/publicado/fuente/nivel heredables."""
    c = dict(ctx or {})
    c.update({k: b[k] for k in ("periodo", "nivel") if b.get(k)})
    if b.get("fuente"):
        c["fuente"] = b["fuente"]
    return _lista(b.get("valores"), c)


def _tipos_diarios(t):
    """Euríbor 12 m y ¤STR día a día (serie_diaria) y los otros plazos del Euríbor (media de octubre y 17-nov). Solo lee."""
    filas = []
    for k, tit in (("euribor_12m_diario", "Euríbor 12 meses (EMMI vía euribor-rates.eu)"), ("estr_diario", "¤STR (tipo a un día del BCE)")):
        b = t.get(k) or {}
        for x in b.get("serie_diaria") or []:
            filas.append({"nombre": tit + " · " + str(x.get("fecha")), "valor": x.get("valor"), "unidad": b.get("unidad") or "%", "fecha": str(x.get("fecha")),
                          "nivel": b.get("nivel") or "?", "fuente": b.get("fuente") or "", "nota": "Dato diario, no media mensual." + (" No contrastado con EMMI [VERIFICAR]." if k.startswith("euribor") else "")})
    b = t.get("euribor_12m_diario") or {}
    for x in b.get("otros_plazos_17nov") or []:
        filas.append({"nombre": x.get("nombre"), "valor": x.get("valor"), "unidad": "%", "fecha": "2026-11-17", "nivel": b.get("nivel") or "?", "fuente": b.get("fuente") or "", "nota": "Dato del día (no media)."})
    for x in t.get("euribor_otros_plazos_oct2026") or []:
        filas.append(_fila(x))
    return filas


def _con_nota(filas, nota):
    """Añade la nota general de un bloque a su primera fila (las filas no tienen nota de grupo)."""
    if filas and nota:
        filas[0]["nota"] = (filas[0]["nota"] + " " if filas[0]["nota"] else "") + str(nota)
    return filas


def _macro_nuevos(d):
    """Bloques del 18-nov (4.ª pasada C229): IPC por grupos especiales, EPA por sexo/edad/sector, temporalidad calculada, afiliación y paro registrado.
    Cada fila lleva unidad explícita (%, miles de personas, personas, M€), fecha, nivel y fuente. Lo no leído se omite o se marca [VERIFICAR] en la vista."""
    g = []
    ipc = d.get("ipc", {})
    ge = ipc.get("grupos_especiales")
    if ge:
        ctx = {"periodo": ge.get("periodo"), "nivel": ge.get("nivel"), "url": "https://www.ine.es/jaxiT3/Tabla.htm?t=76130", "unidad": "%"}
        filas = [_fila(x, ctx) for x in ge.get("valores", []) if isinstance(x, dict)]
        for f in filas:
            f["unidad"] = "% anual (sobre el mismo mes de 2025)" if f["unidad"] == "%" else f["unidad"]
        g.append(("Inflación subyacente y grupos especiales (IPC, INE)", _con_nota(filas, ge.get("nota"))))
    epa = d.get("epa", {})
    sec = epa.get("sectores_ocupados_pct")
    if sec:
        ctx = {"periodo": sec.get("periodo"), "nivel": sec.get("nivel"), "url": "https://www.ine.es/jaxiT3/Tabla.htm?t=" + str(sec.get("tabla_ine", "65125")), "unidad": "% de los ocupados"}
        filas = []
        for x in sec.get("valores", []):
            f = _fila({"nombre": "Ocupados en " + x["nombre"].lower() + " (peso sobre el total)", "valor": x.get("valor"), "unidad": "% de los ocupados",
                       "serie_ine": x.get("serie_ine")}, ctx)
            ant = [f"2T-2026: {str(x['anterior_2T']).replace('.', ',')} %" if x.get("anterior_2T") is not None else "",
                   f"3T-2025: {str(x['hace_un_anio']).replace('.', ',')} %" if x.get("hace_un_anio") is not None else ""]
            f["nota"] = "Anterior: " + "; ".join(a for a in ant if a) + "." if any(ant) else ""
            filas.append(f)
        g.append(("Ocupados por sector (EPA, INE)", filas))
    tm = epa.get("temporalidad")
    if tm:
        ctx = {"periodo": tm.get("periodo"), "nivel": tm.get("nivel"), "url": "https://www.ine.es/jaxiT3/Tabla.htm?t=65200"}
        at, tc = tm.get("asalariados_temporales") or {}, tm.get("tasa_temporalidad_calculada") or {}
        filas = []
        if at:
            filas.append(_fila({"nombre": "Asalariados con contrato temporal", "valor": at.get("valor"), "unidad": "miles de personas", "serie_ine": at.get("serie_ine"),
                                "nota": f"Anterior: 2T-2026 {str(at.get('anterior_2T')).replace('.', ',')}; 3T-2025 {str(at.get('hace_un_anio_3T2025')).replace('.', ',')} (miles de personas)."}, ctx))
        if tc:
            filas.append(_fila({"nombre": "Tasa de temporalidad (CÁLCULO PROPIO: temporales / asalariados)", "valor": tc.get("valor"), "unidad": "% de los asalariados", "nivel": "P",
                                "fuente": "Cálculo propio sobre INE EPA422775 y EPA417633",
                                "nota": f"Cálculo propio, no es la cifra oficial del INE [VERIFICAR]. Anterior: 2T-2026 {str(tc.get('anterior_2T')).replace('.', ',')} %; 3T-2025 {str(tc.get('hace_un_anio_3T2025')).replace('.', ',')} %. No comparable con la de afiliación (otra definición)."}, ctx))
        g.append(("Temporalidad (EPA, INE; la tasa es cálculo propio)", filas))
    pr = d.get("paro_registrado")
    if pr:
        ctx = {"periodo": pr.get("periodo"), "nivel": pr.get("nivel"), "fuente": pr.get("fuente")}
        filas = _lista(pr.get("valores"), ctx)
        for f in filas:
            if "(septiembre" in f["nombre"]:
                f["fecha"] = "sep-2026"
        for k, v in (pr.get("sectores_variacion_mensual_personas") or {}).items():
            filas.append({"nombre": "Paro registrado, variación en el mes · " + k, "valor": v, "unidad": "personas (variación mensual)", "fecha": str(pr.get("periodo")),
                          "nivel": pr.get("nivel") or "?", "fuente": pr.get("fuente") or "", "nota": ""})
        g.append(("Paro registrado (SEPE, octubre)", _con_nota(filas, pr.get("nota"))))
    return g


def _macro(d):
    g = []
    ipc = d.get("ipc", {})
    g.append(("Inflación (IPC)", _lista(ipc.get("general")) + _lista(ipc.get("impuestos_constantes"), {"periodo": ipc.get("periodo")})))
    g.append(("Inflación por grupos (IPC)", _lista(ipc.get("grupos"), {"periodo": ipc.get("periodo"), "nivel": ipc.get("nivel")})))
    nuevos = _macro_nuevos(d)
    g += nuevos[:1]
    epa = d.get("epa", {})
    g.append(("Paro y empleo (EPA)", _lista(epa.get("nacional"), {"periodo": epa.get("periodo")})))
    g.append(("Tasa de paro por comunidad (EPA)", _lista(epa.get("tasa_paro_por_ccaa"), {"periodo": epa.get("periodo"), "nivel": "P"})))
    g += [x for x in nuevos[1:] if not x[0].startswith("Paro registrado")]
    af = d.get("afiliacion")
    if af:
        fa = _bloque(af, {"url": af.get("fuente")})
        for f in fa:
            if f["unidad"] == "ratio":
                f["unidad"] = "afiliados por pensionista"
        g.append(("Afiliación a la Seguridad Social (octubre)", _con_nota(fa, af.get("nota"))))
    g += [x for x in nuevos if x[0].startswith("Paro registrado")]
    s = d.get("salarios_smi", {})
    sa = dict(s.get("salario_medio_aeat") or {})
    sa.setdefault("nombre", "Salario medio (AEAT) / mediano (EAES)")
    g.append(("Salarios y SMI", _lista(s.get("smi")) + _lista(s.get("coste_laboral_etcl")) + _lista([sa])))
    t = d.get("tipos", {})
    th = dict(t.get("tipo_medio_hipotecas") or {})
    th.setdefault("nombre", "Tipo medio de las hipotecas")
    g.append(("Tipos de interés", _lista([t.get("euribor_12m") or {}, th])))
    g.append(("Euríbor y ¤STR: otros plazos y serie diaria", _tipos_diarios(t)))
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


def _tramos_edad(d):
    a = ((d.get("demografia") or {}).get("afiliados_por_tramos_edad")) or {}
    if not a.get("valor"):
        return None
    ia = a.get("interanual") or {}
    filas = [{"tramo": k, "valor": v, "anterior": ia.get(k), "var": (a.get("variacion_interanual_pct") or {}).get(k), "pct": (a.get("pct_del_total") or {}).get(k),
              "pct_ant": (a.get("pct_del_total_2025-10") or {}).get(k)} for k, v in a["valor"].items()]
    filas.append({"tramo": "Total", "valor": a.get("total"), "anterior": ia.get("total"), "var": (a.get("variacion_interanual_pct") or {}).get("total"), "pct": None, "pct_ant": None})
    return {"filas": filas, "fecha": a.get("fecha"), "fecha_ant": ia.get("fecha"), "unidad": a.get("unidad"), "nivel": a.get("nivel") or "?", "fuente": a.get("fuente") or "", "nota": a.get("nota") or ""}


def _envejecimiento(d):
    e = ((d.get("demografia") or {}).get("envejecimiento_ccaa")) or {}
    if not e.get("regiones"):
        return None
    return {"filas": e["regiones"], "periodo": e.get("periodo"), "unidad": e.get("unidad"), "nivel": e.get("nivel") or "?", "fuente": e.get("fuente") or "", "nota": e.get("nota") or ""}


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
             "nota": re.sub(r"\bnull\b", "sin dato", d.get("nota") or d.get("_nota") or ""), "pendiente": d.get("pendiente") or d.get("por_abrir") or []}
        if k == "investigaciones":
            s["casos"] = _investigaciones(d)
            s["remite_a"] = d.get("remite_a", [])
        else:
            s["grupos"] = [{"grupo": t, "filas": f} for t, f in fns[k](d) if f]
            if k == "vivienda":
                s["ccaa"] = _tabla_vivienda(d)
            if k == "pensiones":
                s["tramos"] = _tramos_edad(d)
                s["envejecimiento"] = _envejecimiento(d)
        salida[k] = s
    return salida or None
