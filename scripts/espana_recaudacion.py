"""España › Recaudación (C265): cuánto entra por impuestos, por año y por figura. Sin red, sin claves, sin IA.

Escribe explorador/espana-recaudacion.json con:
  · cifras de la AEAT (caja, M€) leídas el 14-nov-2026 de las TABLAS de sus «Informes mensuales de recaudación
    tributaria» (cuadros 1.1, 1.2, 2.1 y 0): diciembre de 2020 a 2025 y septiembre de 2026;
  · cifras de Eurostat (devengo, cuentas nacionales) copiadas de explorador/espana.json (por eso se ejecuta DESPUÉS de
    scripts/espana_fiscal.py).
Los números de la AEAT están escritos aquí a propósito (el PDF no tiene API): al leer un informe nuevo se cambian a mano
y se vuelve a ejecutar. El script comprueba que las figuras suman el total.
Uso: python scripts/espana_recaudacion.py
"""
import json
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "espana-recaudacion.json"
ESPANA = RAIZ / "explorador" / "espana.json"
HOY = "2026-11-14"
IMR = "https://sede.agenciatributaria.gob.es/static_files/AEAT/Estudios/Estadisticas/Informes_Estadisticos/Informes_mensuales_recaudacion_tributaria/"
URL = {a: f"{IMR}20{a}/IMR_{a}_12_es_es.pdf" for a in ("20", "21", "22", "23", "24", "25")}
URL["26"] = IMR + "2026/IMR_26_09_es_es.pdf"
ANUAL_WEB = "https://sede.agenciatributaria.gob.es/Sede/eu_es/estadisticas/recaudacion-tributaria/informe-anual/ejercicio-2025/resumen.html"

FIGURAS = ("irpf", "is", "iva", "iiee", "resto")
NOMBRE = {"irpf": "IRPF (renta de las personas físicas)", "is": "Impuesto sobre Sociedades", "iva": "IVA",
          "iiee": "Impuestos Especiales", "resto": "Resto (no residentes, tasas, otros)"}

# Ingresos tributarios NETOS (después de devoluciones), M€, acumulado de enero a diciembre. Cuadro 1.2 de cada informe de diciembre.
# año: (IRPF, IS, IVA, IIEE, Resto, TOTAL, informe del que sale)
NETOS = {
    2019: (86892, 23733, 71538, 21380, 9265, 212808, "20"),
    2020: (87972, 15858, 63337, 18790, 8095, 194051, "21"),
    2021: (94546, 26627, 72498, 19729, 9985, 223385, "21"),
    2022: (109485, 32176, 82595, 20224, 10983, 255463, "23"),
    2023: (120280, 35060, 83909, 20757, 11929, 271935, "24"),
    2024: (129408, 39096, 90541, 22128, 13560, 294734, "25"),
    2025: (142466, 42266, 99532, 23083, 18009, 325356, "25"),
}
# Devoluciones, M€, enero-diciembre (Cuadro 2.1): (IRPF, IS, IVA, IIEE, Resto, TOTAL)
DEVOL = {
    2019: (13245, 9879, 28103, 584, 1832, 53644),
    2020: (12527, 12209, 26948, 619, 1576, 53878),
    2021: (12105, 9211, 28568, 683, 1631, 52198),
    2022: (11897, 11424, 39045, 818, 1778, 64962),
    2023: (13657, 13805, 37568, 803, 1928, 67762),
    2024: (15880, 14973, 37262, 863, 1782, 70760),
    2025: (18178, 16651, 39209, 1034, 1782, 76856),
}
# Enero-septiembre: 2026 y 2025 (Cuadros 1.2 y 2.1 del informe de septiembre de 2026)
ACUM = {"2026": (118068, 18877, 81181, 15718, 14483, 248326), "2025": (104957, 15004, 75090, 17172, 13525, 225747)}
DEVOL_ACUM = {"2026": (14056, 10263, 29641, 701, 1616, 56276), "2025": (14688, 12291, 28478, 649, 1239, 57346)}
# Homogéneos (Cuadro 3.1 «ingresos homogéneos»: quitan medidas y efectos de calendario), ene-sep
HOMOG = {"2026": (118634, 25035, 81337, 16093, 14358, 255458), "2025": (106144, 23400, 75767, 17547, 13630, 236487)}
# Impacto de las medidas normativas y de gestión sobre la recaudación (Cuadro 0): IRPF, IS, IVA, IIEE, otros, total
MEDIDAS = {"2025 (año)": (-1155, 3641, 2223, 831, 2280, 7820), "2026 (ene-sep)": (578, -1982, -468, -1637, -474, -3983)}

# Detalle del año 2025 y 2024 (Cuadro 1.1 de diciembre de 2025) y de ene-sep 2026/2025 (Cuadro 1.1 de septiembre de 2026): (Estado, AA.TT., Total)
# AA.TT. = comunidades autónomas y corporaciones locales (la parte cedida: IRPF, IVA e Impuestos Especiales).
REPARTO = {
    "2025": {"directos": (117846, 76085, 193931), "indirectos": (66672, 62596, 129268), "tasas": (2156, 0, 2156), "total": (186674, 138682, 325356)},
    "2024": {"directos": (102515, 71558, 174073), "indirectos": (56045, 62601, 118646), "tasas": (2015, 0, 2015), "total": (160575, 134159, 294734)},
    "ene-sep 2026": {"directos": (81041, 62953, 143994), "indirectos": (50221, 52276, 102497), "tasas": (1835, 0, 1835), "total": (133097, 115230, 248326)},
    "ene-sep 2025": {"directos": (68718, 58139, 126857), "indirectos": (50776, 46463, 97240), "tasas": (1650, 0, 1650), "total": (121145, 104602, 225747)},
}
# Impuestos Especiales por producto, M€ (total): 2025, 2024 (diciembre 2025), ene-sep 2026 y 2025 (septiembre 2026)
IIEE = [
    ("Hidrocarburos", 12366, 12305, 8137, 9380),
    ("Labores del tabaco", 7340, 6927, 5298, 5273),
    ("Electricidad", 1587, 1112, 994, 1194),
    ("Alcohol y bebidas derivadas", 793, 824, 566, 581),
    ("Envases de plástico no reutilizables", 599, 571, 447, 463),
    ("Cerveza", 336, 346, 232, 236),
    ("Líquidos de cigarrillos electrónicos", 30, 0, 34, 19),
    ("Carbón", 9, 20, -9, 8),
    ("Otros", 23, 23, 18, 18),
]
IIEE_TOTAL = (23083, 22128, 15718, 17172)


def pct(a, b):
    return None if not b else round((a / b - 1) * 100, 1)


def comprobar():
    for a, f in NETOS.items():
        assert abs(sum(f[:5]) - f[5]) <= 2, ("suma netos", a, sum(f[:5]), f[5])
    for a, f in DEVOL.items():
        assert abs(sum(f[:5]) - f[5]) <= 2, ("suma devoluciones", a, sum(f[:5]), f[5])
    for k, f in {**ACUM, **DEVOL_ACUM, **HOMOG}.items():
        assert abs(sum(f[:5]) - f[5]) <= 2, ("suma acumulado", k)
    for k, d in REPARTO.items():
        assert abs(d["directos"][2] + d["indirectos"][2] + d["tasas"][2] - d["total"][2]) <= 2, ("directos+indirectos", k)
        for g in d.values():
            assert abs(g[0] + g[1] - g[2]) <= 2, ("Estado+AATT", k, g)
    for i, tot in enumerate(IIEE_TOTAL):
        assert abs(sum(r[i + 1] for r in IIEE) - tot) <= 3, ("IIEE", i, sum(r[i + 1] for r in IIEE), tot)
    for k, m in MEDIDAS.items():
        assert sum(m[:5]) == m[5], ("medidas", k)


def main():
    comprobar()
    e = json.loads(ESPANA.read_text(encoding="utf-8"))
    ind = {r["id"]: r for r in e["indicadores"]}
    pib = {str(k): v for k, v in e["contexto"]["pib"].items()}

    anual = []
    for a in sorted(NETOS):
        n = NETOS[a]
        d = DEVOL[a]
        ant = NETOS.get(a - 1)
        fila = {"anio": a, "total": n[5], "bruto": n[5] + d[5], "devoluciones": d[5],
                "var_total_m": (n[5] - ant[5]) if ant else None, "var_total_pct": pct(n[5], ant[5]) if ant else None,
                "pct_pib": round(n[5] / pib[str(a)] * 100, 1) if pib.get(str(a)) else None,
                "fuente": URL[n[6]], "nivel": "P"}
        for i, f in enumerate(FIGURAS):
            fila[f] = n[i]
            fila[f + "_var_pct"] = pct(n[i], ant[i]) if ant else None
            fila[f + "_devol"] = d[i]
        anual.append(fila)

    def bloque_acum(clave_a, clave_b, nomb_a, nomb_b):
        filas = []
        for i, f in enumerate(FIGURAS + ("total",)):
            va, vb = ACUM[clave_a][i], ACUM[clave_b][i]
            filas.append({"figura": f, "nombre": NOMBRE.get(f, "TOTAL ingresos tributarios netos"), nomb_a: va, nomb_b: vb,
                          "var_m": va - vb, "var_pct": pct(va, vb),
                          "devoluciones_a": DEVOL_ACUM[clave_a][i], "devoluciones_b": DEVOL_ACUM[clave_b][i],
                          "homogeneo_a": HOMOG[clave_a][i], "homogeneo_b": HOMOG[clave_b][i],
                          "homogeneo_var_pct": pct(HOMOG[clave_a][i], HOMOG[clave_b][i])})
        return filas

    reparto = []
    for per, d in REPARTO.items():
        reparto.append({"periodo": per, **{k: {"estado": v[0], "aatt": v[1], "total": v[2]} for k, v in d.items()}})

    iiee = [{"producto": n, "2025": a, "2024": b, "var_2025_pct": pct(a, b), "ene_sep_2026": c, "ene_sep_2025": d, "var_ene_sep_pct": pct(c, d)}
            for n, a, b, c, d in IIEE]

    # Eurostat (devengo): impuestos sobre la producción y la importación, sobre la renta y el patrimonio, y cotizaciones
    euro = []
    for a in range(2019, 2026):
        s = str(a)
        d2, d5, d61 = (ind[k]["serie"].get(s) for k in ("imp_produccion", "imp_renta", "cotizaciones"))
        euro.append({"anio": a, "impuestos_produccion_importacion": d2, "impuestos_renta_patrimonio": d5, "cotizaciones": d61,
                     "impuestos_sin_cotizaciones": d2 + d5, "impuestos_con_cotizaciones": d2 + d5 + d61,
                     "presion_fiscal_pct_pib": round((d2 + d5 + d61) / pib[s] * 100, 1),
                     "impuestos_sin_cotizaciones_pct_pib": round((d2 + d5) / pib[s] * 100, 1),
                     "aeat_pct_pib": round(NETOS[a][5] / pib[s] * 100, 1), "pib": pib[s],
                     "ingresos_totales_aapp": ind["ingresos"]["serie"].get(s)})
    euro_fuente = ind["imp_produccion"]["fuente"]

    sal = {
        "titulo": "España: cuánto se recauda (impuestos por año y por figura)",
        "leido": HOY,
        "unidad": "M€ corrientes (millones de euros, sin quitar la inflación)",
        "nivel": "P",
        "nota": ("Ingresos tributarios NETOS de devoluciones, criterio de CAJA, de la Agencia Tributaria (AEAT), leídos en las tablas de sus informes "
                 "mensuales de recaudación (no en prensa). Es lo que entra por impuestos al conjunto de las administraciones (Estado, comunidades "
                 "autónomas y entes locales por la parte cedida). No incluye cotizaciones a la Seguridad Social ni los tributos propios de comunidades "
                 "y ayuntamientos (IBI, por ejemplo): por eso no coincide con Eurostat. Último dato: septiembre de 2026 (acumulado de enero a septiembre)."),
        "fuentes": {"informes_mensuales": URL, "informe_anual_2025": ANUAL_WEB,
                    "eurostat": euro_fuente, "pib": "explorador/espana.json (contexto.pib, Eurostat)"},
        "definiciones": {
            "aeat_caja": "Lo realmente ingresado en el periodo, neto de devoluciones. Se publica cada mes; el informe de septiembre sale hacia finales de octubre.",
            "eurostat_devengo": ("Cuentas nacionales (SEC 2010): se registra cuando nace el impuesto, incluye los tributos propios de comunidades y ayuntamientos "
                                 "y las cotizaciones sociales. Sale con 1-9 meses de retraso y por eso no es comparable euro a euro con la AEAT."),
            "homogeneos": "Ingresos de la AEAT sin medidas normativas ni efectos de calendario o devoluciones extraordinarias: mide el crecimiento «de fondo».",
        },
        "anual": anual,
        "acumulado_2026": {"periodo": "enero-septiembre", "ultimo_mes": "2026-09", "fuente": URL["26"],
                           "filas": bloque_acum("2026", "2025", "v2026", "v2025"),
                           "nota": ("Variación en M€ y % frente al mismo periodo de 2025. «Homogéneo» = sin medidas ni extraordinarios (AEAT, cuadro 3.1). "
                                    "Hasta septiembre de 2025 hubo devoluciones extraordinarias (mutualistas y sentencia del RDL 3/2016) que inflan ahora la tasa "
                                    "(+1.122 M€ de impacto según la AEAT), y en 2026 las medidas por el conflicto de Oriente Medio restan 3.983 M€.")},
        "medidas": {"unidad": "M€", "columnas": ["IRPF", "Sociedades", "IVA", "Especiales", "Otros", "Total"],
                    "filas": [{"periodo": k, "valores": list(v)} for k, v in MEDIDAS.items()],
                    "fuente": URL["25"] + " y " + URL["26"], "nivel": "P",
                    "nota": "Estimación de la propia AEAT del efecto de cambios normativos y de gestión (cuadro 0). Positivo = sube la recaudación. En 2025 incluye −2.978 M€ por ingresos y devoluciones extraordinarios."},
        "reparto": {"nota": "Estado frente a «AA.TT.» (comunidades autónomas y entes locales: su parte cedida del IRPF, IVA y Especiales). Directos = capítulo I, indirectos = capítulo II, tasas = capítulo III.",
                    "fuente": URL["25"] + " y " + URL["26"], "periodos": reparto},
        "impuestos_especiales": {"unidad": "M€", "fuente": URL["25"] + " y " + URL["26"], "filas": iiee},
        "devoluciones": {"unidad": "M€", "nota": "Devoluciones tributarias pagadas (restan de los ingresos brutos). Ingresos brutos = netos + devoluciones (cálculo propio con las dos cifras de la AEAT).",
                         "fuente": URL["25"], "acumulado_2026": DEVOL_ACUM["2026"][5], "acumulado_2025": DEVOL_ACUM["2025"][5]},
        "cotizaciones_sociales": {"nota": ("Bloque separado: las cotizaciones a la Seguridad Social NO son ingresos tributarios de la AEAT. Dato anual de Eurostat (devengo, "
                                           "efectivas e imputadas). Serie mensual de la Seguridad Social/IGAE: pendiente [VERIFICAR] (otra fuente y otro criterio)."),
                                  "fuente": euro_fuente, "nivel": "P",
                                  "serie": [{"anio": r["anio"], "valor": r["cotizaciones"]} for r in euro], "unidad": "M€"},
        "contexto": {"unidad": "% del PIB", "fuente": euro_fuente, "nivel": "P",
                     "nota": ("«Presión fiscal» = impuestos sobre producción e importación + sobre renta y patrimonio + cotizaciones (Eurostat), dividido por el PIB; "
                              "excluye impuestos sobre el capital (cálculo propio con tres filas oficiales). La AEAT en % del PIB es cálculo propio (recaudación ÷ PIB corriente de Eurostat). "
                              "En euros corrientes todo sube con la inflación: el % del PIB es la medida que corrige el tamaño de la economía."),
                     "serie": euro},
        "comparacion_fuentes": {
            "texto": ("AEAT (caja) y Eurostat (devengo) miden cosas distintas, así que no se restan. En 2025: AEAT = 325.356 M€; Eurostat, impuestos sobre producción e "
                      "importación + sobre renta y patrimonio = 412.211 M€ (sin cotizaciones). La diferencia incluye tributos propios de comunidades y ayuntamientos, "
                      "impuestos que no gestiona la AEAT y el criterio de devengo; su tamaño exacto por partida queda [VERIFICAR]."),
            "aeat_2025": 325356, "eurostat_impuestos_2025": ind["imp_produccion"]["serie"]["2025"] + ind["imp_renta"]["serie"]["2025"], "nivel": "P"},
        "pendiente": [
            "Grandes empresas: el informe mensual no la desglosa; hay que buscar la estadística específica de la AEAT [VERIFICAR].",
            "Comunidades autónomas frente a entes locales por separado: el informe mensual agrupa AA.TT.; el cuadro 1.3 sí los separa por mes (no volcado).",
            "Cotizaciones sociales mensuales de la Seguridad Social: fuente y criterio distintos; no volcado.",
            "Serie 2019-2023: cada año sale de su propio informe de diciembre; la AEAT puede reponer cifras con revisiones posteriores (comparar al actualizar).",
        ],
        "lecturas": [
            {"t": "HECHO", "texto": "La recaudación neta de la AEAT creció cada año de 2021 a 2025 y en 2025 fue la mayor de la serie 2019-2025 en euros corrientes (325.356 M€, +10,4 %)."},
            {"t": "HECHO", "texto": "En 2025 las medidas y cambios de gestión sumaron +7.820 M€ (2,7 puntos de la subida); sin ellos el crecimiento habría sido menor. En 2026 (ene-sep) restan 3.983 M€."},
            {"t": "HECHO", "texto": "Hasta septiembre de 2026 la AEAT ingresó 248.326 M€ (+10,0 %); en términos homogéneos +8,0 % (AEAT). Parte de la subida frente a 2025 viene de menores devoluciones extraordinarias."},
            {"t": "OPINIÓN", "texto": "Que la recaudación esté «en máximos» no dice por sí solo si sube la presión fiscal: ver el % del PIB y la nota en «Recaudación récord» de Presupuesto. Atribuir la subida a decisiones políticas concretas es opinión."},
        ],
    }
    SALIDA.write_text(json.dumps(sal, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"espana-recaudacion.json: {len(anual)} años, acumulado ene-sep 2026 {ACUM['2026'][5]} M€ (leído {HOY})")


if __name__ == "__main__":
    main()
