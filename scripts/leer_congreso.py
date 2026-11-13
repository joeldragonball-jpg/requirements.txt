"""C242: lee datos abiertos del Congreso (sin IA, sin claves) y escribe explorador/espana-politica.json.
Solo agregados oficiales y neutrales: nada de nombres en rankings ni calificaciones."""
import urllib.request as U, json, re, html, collections, datetime, io
H = {'User-Agent': 'Mozilla/5.0'}
RAIZ = 'https://www.congreso.es'


def get(url):
    return U.urlopen(U.Request(url, headers=H), timeout=60).read()


def enlaces(pag):
    b = get(RAIZ + '/es/opendata/' + pag).decode('utf8', 'ignore')
    return sorted(set(re.findall(r'href="(/webpublica/opendata/[^"]+\.json)"', b)))


def js(pag, prefijo):
    for l in enlaces(pag):
        if l.split('/')[-1].startswith(prefijo):
            return json.loads(get(RAIZ + l).decode('utf8')), RAIZ + '/es/opendata/' + pag
    raise SystemExit('no hay ' + prefijo)


def res(x):
    return (x or '').split('\n')[0].strip()


def anio(f):
    return f[-4:]


def cuenta(l, f):
    return dict(collections.Counter(f(x) for x in l))


act, u1 = js('diputados', 'DiputadosActivos__')
baj, _ = js('diputados', 'DiputadosDeBaja__')
dec, u2 = js('diputados', 'docacteco__')
pro, u3 = js('iniciativas', 'ProyectosDeLey__')
prop, _ = js('iniciativas', 'ProposicionesDeLey__')
apr, _ = js('iniciativas', 'IniciativasLegislativasAprobadas__')
hoy = datetime.date.today()


def grp(s):
    return s.replace('Grupo Parlamentario ', '').replace(' en el Congreso', '')


comp = collections.Counter(grp(x['GRUPOPARLAMENTARIO']) for x in act)
bd = collections.Counter(x['FECHABAJA'] for x in baj).most_common(1)[0]

# votaciones: ultima sesion que muestra la pagina
b = get(RAIZ + '/es/opendata/votaciones').decode('utf8', 'ignore')
i = b.find('cuerpo-votaciones')
t = b[i:]
t = t[:t.find('Leyenda')]
t = re.sub(r'<[^>]+>', '|', t)
t = html.unescape(re.sub(r'\s+', ' ', t))
t = re.sub(r'(\| ?)+', '| ', t)
ses = re.search(r'Sesión Plenaria número (\d+) \| Fecha : (\S+)', t)
vots = [dict(texto=m[0].strip(), expediente=m[1], si=int(m[2]), no=int(m[3]), abst=int(m[4]))
        for m in re.findall(r'\| ([^|]+?)(?: \(Pública[^)]*\))? \| \(Núm\. expte\. ([\d/]+)\) \| Si: (\d+)\| No: (\d+)\| Abstenciones: (\d+)', t)]


# ---- C242 (12-nov-2026): altos cargos en el BOE (Ley 3/2015). Solo agregados, nunca nombres. ----
BOE_XML = 'https://www.boe.es/diario_boe/xml.php?id='
BOE_SEMESTRES = ['BOE-A-2026-3366', 'BOE-A-2026-16747']   # art. 22.2: informe semestral (2.º sem. 2025 y 1.º sem. 2026)
BOE_BIENES = 'BOE-A-2026-7339'                           # art. 21.5: declaraciones de bienes de quienes tomaron posesión o cesaron en 2025


def boe_lineas(ident):
    t = get(BOE_XML + ident).decode('utf8')
    t = html.unescape(re.sub(r'(?s)<[^>]+>', '\n', t))
    return [l.strip() for l in t.split('\n') if l.strip()]


def num_es(x):
    x = x.strip()
    return float(x.replace('.', '').replace(',', '.')) if re.fullmatch(r'[\d\.]+(,\d+)?', x) else None


def mediana(v):
    v = sorted(v)
    n = len(v)
    return None if not n else (v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2)


def altos_cargos_boe():
    sem = []
    for ident in BOE_SEMESTRES:
        L = boe_lineas(ident)
        k = next(i for i, l in enumerate(L) if l.startswith('Periodo comprendido'))
        T = L[k:k + 60]

        def tras(pref, desde=0):
            for i in range(desde, len(T) - 1):
                if T[i].startswith(pref):
                    return T[i + 1]
            return ''
        inc = next(i for i, l in enumerate(T) if l.startswith('Procedimientos sancionadores incoados'))
        res_ = next(i for i, l in enumerate(T) if l.startswith('Procedimientos sancionadores resueltos'))
        sem.append(dict(
            periodo=T[0].replace('Periodo comprendido ', ''), boe=ident, fuente=BOE_XML + ident,
            altos_cargos_en_activo=int(tras('Altos cargos en activo')),
            declaraciones_bienes_toma=int(tras('Declaraciones de bienes a la toma')),
            declaraciones_bienes_cese=int(tras('Declaraciones de bienes al cese')),
            declaraciones_actividades_toma=int(tras('Declaraciones de actividades a la toma')),
            declaraciones_actividades_cese=int(tras('Declaraciones de actividades al cese')),
            comunicaciones_cambio_actividad=int(tras('Comunicaciones de cambio')),
            declaraciones_anuales=int(tras('Declaraciones anuales')),
            sancionadores_incoados_ley_3_2015=tras('En virtud de la Ley 3/2015', inc).rstrip('.'),
            sancionadores_incoados_ley_19_2013=tras('En virtud de la Ley 19/2013', inc).rstrip('.'),
            sancionadores_resueltos_ley_3_2015=tras('En virtud de la Ley 3/2015', res_).rstrip('.'),
            sancionadores_resueltos_ley_19_2013=tras('En virtud de la Ley 19/2013', res_).rstrip('.')))
    L = boe_lineas(BOE_BIENES)
    CAT = [('Bienes inmuebles', 'Bienes inmuebles'), ('Depósitos', 'Depósitos y cuentas'),
           ('Accs. y participaciones en el capital social o en el fondo', 'Acciones cotizadas, deuda pública y bonos'),
           ('Accs. y participaciones en capital social o en fondos propios', 'Participaciones no cotizadas'),
           ('Seguros de vida', 'Seguros de vida y planes de pensiones'), ('Demás bienes', 'Otros bienes y derechos'), ('Pasivo', 'Pasivo (deudas)')]
    regs, cur, sec = [], None, None
    for i, l in enumerate(L):
        if l.upper().startswith('ALTOS CARGOS CESADOS'):
            sec = 'cese'
        elif l.upper().startswith('ALTOS CARGOS NOMBRADOS'):
            sec = 'toma'
        if l.startswith('Apellidos y nombre'):
            cur = dict(sec=sec, v={n: 0.0 for _, n in CAT})
            regs.append(cur)
        elif cur is not None and i + 1 < len(L):
            for pref, n in CAT:
                if l.startswith(pref):
                    x = num_es(L[i + 1])
                    if x is not None:
                        cur['v'][n] = x
    filas = []
    for _, n in CAT:
        v = [r['v'][n] for r in regs]
        filas.append(dict(concepto=n, suma_meur=round(sum(v) / 1e6, 2), mediana_eur=round(mediana(v)),
                          con_importe=sum(1 for x in v if x > 0)))
    act = [sum(x for n, x in r['v'].items() if n != 'Pasivo (deudas)') for r in regs]
    neto = [a - r['v']['Pasivo (deudas)'] for a, r in zip(act, regs)]

    def q(v, f):
        return sorted(v)[int(len(v) * f)]
    return dict(
        semestres=sem,
        bienes=dict(
            boe=BOE_BIENES, fuente=BOE_XML + BOE_BIENES, fecha_boe='2026-03-31', ejercicio='tomas de posesión y ceses de 2025',
            declaraciones=len(regs), por_cese=sum(1 for r in regs if r['sec'] == 'cese'), por_toma_posesion=sum(1 for r in regs if r['sec'] == 'toma'),
            filas=filas,
            activo=dict(suma_meur=round(sum(act) / 1e6, 2), mediana_eur=round(mediana(act)), cuartil_1_eur=round(q(act, .25)), cuartil_3_eur=round(q(act, .75))),
            neto=dict(suma_meur=round(sum(neto) / 1e6, 2), mediana_eur=round(mediana(neto)), cuartil_1_eur=round(q(neto, .25)), cuartil_3_eur=round(q(neto, .75)),
                      con_neto_negativo=sum(1 for x in neto if x < 0)),
            nota='Agregado propio de las declaraciones publicadas en el BOE (art. 21.5 de la Ley 3/2015): una por persona que tomó posesión o cesó en 2025, de ahí que no cubra a todos los altos cargos en activo. Importes tal como los declara cada persona y los publica el BOE; el criterio de valoración de los inmuebles no se indica en la resolución [VERIFICAR]. «Neto» = suma de los seis conceptos de activo menos el pasivo (cálculo nuestro). No se publican aquí nombres ni cargos concretos.'))


try:
    ACB = altos_cargos_boe()
except Exception as e:  # el BOE no debe impedir generar el resto
    print('altos cargos BOE: fallo', repr(e)[:160])
    ACB = None

out = dict(
    generado=hoy.isoformat(),
    titulo='España · Congreso: composición, iniciativas y votaciones (datos abiertos del Congreso)',
    aviso='Solo datos oficiales del Congreso de los Diputados (datos abiertos), sin calificaciones ni opinión. Una iniciativa «caducada» o «rechazada» describe su estado procesal, no su valor. Cortes disueltas por el RD 806/2026 (BOE-A-2026-20742, 6-oct-2026) [P]; elecciones generales el 29-nov-2026.',
    unidad='número de diputados / iniciativas / votos (unidades)', escala='1 (sin escala)',
    composicion=dict(
        fecha_dato=hoy.isoformat(), nivel='P', fuente=u1,
        activos_total=len(act), por_grupo=dict(comp.most_common()), bajas_total=len(baj),
        baja_masiva=dict(fecha=bd[0], diputados=bd[1]),
        nota='El fichero «DiputadosActivos» del Congreso lista %d diputados el %s; hay %d bajas, %d con fecha %s, coincidiendo con la disolución de las Cortes. El fichero no explica por qué unos constan activos y otros de baja: [VERIFICAR] en el Congreso. No es el reparto de escaños de las elecciones de 2023.' % (len(act), hoy.strftime('%d/%m/%Y'), len(baj), bd[1], bd[0])),
    iniciativas=dict(
        fecha_dato=hoy.isoformat(), nivel='P', fuente=u3, legislatura='XV (2023-2026)',
        proyectos_ley_gobierno=dict(total=len(pro), por_resultado=cuenta(pro, lambda x: res(x.get('RESULTADOTRAMITACION')) or 'sin resultado')),
        proposiciones_ley=dict(total=len(prop), por_resultado=cuenta(prop, lambda x: res(x.get('RESULTADOTRAMITACION')) or 'sin resultado'),
                               por_origen=cuenta(prop, lambda x: x['TIPO'].replace('Proposición de ley ', ''))),
        presentadas_por_anio=cuenta(pro + prop, lambda x: anio(x['FECHAPRESENTACION'])),
        normas_aprobadas_por_anio=cuenta(apr, lambda x: anio(x['FECHA_LEY']) + ' · ' + x['TIPO']),
        leyes_2026=[dict(titulo=x['TITULO_LEY'][:180], fecha=x['FECHA_LEY'], pdf=x['PDF']) for x in apr
                    if x['TIPO'] in ('Leyes', 'Leyes organicas') and anio(x['FECHA_LEY']) == '2026'],
        nota='«Caducado» y «decaído» son efecto de la disolución o del vencimiento de plazos, no una votación. Solo iniciativas legislativas; las no legislativas (mociones, preguntas) no se leyeron: [VERIFICAR]. «Normas aprobadas» incluye Reales Decretos-leyes y Reales Decretos legislativos publicados por el Congreso.'),
    votaciones=dict(
        nivel='P', fuente=RAIZ + '/es/opendata/votaciones', sesion=ses.group(1) if ses else None,
        fecha=ses.group(2) if ses else None, resultados=vots,
        nota='Aquí solo la última sesión plenaria que muestra la página. El histórico de toda la legislatura (por sesión, año y grupo) está en el bloque siguiente, leído de los ZIP oficiales por scripts/leer_votaciones_congreso.py.'),
    intereses=dict(
        nivel='P', fuente=u2, fecha_dato=hoy.isoformat(),
        declaraciones=len(dec), diputados_con_registro=len({x['NOMBRE'] for x in dec}),
        por_tipo=cuenta(dec, lambda x: x['TIPO']), por_declaracion=cuenta(dec, lambda x: x['DECLARACION']),
        registradas_por_anio=cuenta(dec, lambda x: anio(x['FECHAREGISTRO'])),
        nota='Registros de actividades, donaciones y fundaciones declaradas por diputados (fichero «docacteco» del Congreso). Se cuentan registros; no se publican nombres ni se valora ninguna declaración. Bienes y rentas completos: Registro de Intereses del Congreso (PDF por diputado), no leído: [VERIFICAR].'),
    # Cifras transcritas a mano de los informes oficiales (PDF del Congreso, leídos con pdftotext el 10-nov-2026)
    financiacion=dict(
        nivel='P', fecha_dato='2026-11-10', unidad='M€ = millones de euros; euros donde se indica', escala='millones (M€) salvo «euros»',
        aviso='Cifras del Tribunal de Cuentas, no nuestras. Las «salvedades», «incumplimientos» y «posibles infracciones» son observaciones de la fiscalización de cuentas, no sentencias ni sanciones firmes. El último informe de cuentas de los propios partidos es del ejercicio 2020 (hay desfase de varios años).',
        partidos_2020=dict(
            informe='Informe n.º 1.573, cuentas anuales de los partidos políticos, ejercicio 2020; Pleno 27-jun-2024', fuente='https://www.congreso.es/docu/inf_fiscTC/LegXV/251-114.pdf',
            filas=[
                dict(nombre='Formaciones fiscalizadas (cuentas presentadas)', valor=25, unidad='partidos', nota='21 en plazo (30-jun-2021) y 4 fuera de plazo (conclusión 1)'),
                dict(nombre='Formaciones con salvedades en sus cuentas', valor=20, unidad='de 25 partidos', nota='En 3 (CUP, Izquierda Unida, Nueva Canarias) las cuentas no reflejan adecuadamente la situación (conclusión 6)'),
                dict(nombre='Financiación pública, peso sobre ingresos', valor=73, unidad='%', nota='Privada 27 % (conclusión 13)'),
                dict(nombre='Subvenciones de funcionamiento ordinario (partidos y grupos consolidados)', valor=167.74, unidad='M€', nota='Incluye 3,08 M€ de subvención estatal para gastos de seguridad (conclusión 14)'),
                dict(nombre='Aportaciones de grupos parlamentarios (Cortes y asambleas) a los partidos', valor=64.61, unidad='M€', nota='52 % de las subvenciones que esos grupos reciben (conclusión 15)'),
                dict(nombre='Aportaciones de grupos políticos locales a los partidos', valor=38.80, unidad='M€', nota='Anexo IV (conclusión 15)'),
                dict(nombre='Recursos privados contabilizados', valor=65.88, unidad='M€', nota='Cuotas de afiliados 27,49; aportaciones de cargos públicos 28,90; patrimonial y actividades 7,42; donaciones 2,07 (conclusión 16)'),
                dict(nombre='Donaciones privadas: número de donantes', valor=5754, unidad='donantes', nota='5.268 (92 %) de menos de 1.000 €; solo 12 superaron 10.000 € en el año (conclusión 16)'),
                dict(nombre='Deuda con entidades de crédito', valor=79.24, unidad='M€', nota='Hipotecaria 59,53; no hipotecaria 17,87; electoral 1,84; más 5,77 M€ con prestamistas particulares; deuda total = 20 % del balance. Mayores: PSOE 29,56, PP 22,92, IU 13,29 M€ (conclusión 11)'),
                dict(nombre='Ingresos en cajeros automáticos de Vox pendientes de justificar (observación del Tribunal)', valor=102048.30, unidad='euros', nota='Conclusión sobre financiación privada, letra d). Observación de fiscalización; no consta sanción en este informe.')]),
        fundaciones_2021_2022=dict(
            informe='Informe n.º 1.642, aportaciones a fundaciones y entidades vinculadas a partidos, ejercicios 2021 y 2022; Pleno 25-sep-2025', fuente='https://www.congreso.es/docu/inf_fiscTC/LegXV/251-181.pdf',
            filas=[
                dict(nombre='Fundaciones y entidades fiscalizadas (2021 / 2022)', valor=36, unidad='entidades en 2021 (34 en 2022)', nota='28 fundaciones, 5 asociaciones, 3 sociedades en 2021'),
                dict(nombre='Aportaciones y donaciones privadas 2021', valor=3813743.67, unidad='euros', nota='Conclusión 8'),
                dict(nombre='Aportaciones y donaciones privadas 2022', valor=4122985.46, unidad='euros', nota='Conclusión 8'),
                dict(nombre='Subvenciones públicas recibidas 2021', valor=2394338.06, unidad='euros', nota='Sobre todo de Cultura y Deporte y de Asuntos Exteriores; en la muestra, gastos justificados con carácter general (conclusión 9)'),
                dict(nombre='Subvenciones públicas recibidas 2022', valor=2539219.75, unidad='euros', nota='Conclusión 9'),
                dict(nombre='Entidades sin cuentas presentadas', valor=3, unidad='entidades (2021 y 2022)', nota='Conclusión 1-2'),
                dict(nombre='Entidades con informe de auditoría presentado', valor=16, unidad='entidades en 2022 (15 en 2021)', nota='Conclusión 4'),
                dict(nombre='Entidades inscritas en el Registro de Partidos (31-dic-2022)', valor=18, unidad='entidades (15 fundaciones + 3 vinculadas)', nota='Conclusión 5. El apartado de seguimiento del mismo informe dice 18 fundaciones y 3 entidades: cifra discrepante dentro del propio informe [VERIFICAR]')]),
        fundaciones_2023=dict(
            informe='Informe n.º 1.697, fundaciones y entidades vinculadas a partidos, ejercicio 2023; Pleno 22-sep-2026 (resumen oficial leído el 12-nov-2026)', fuente='https://www.tcu.es/export/sites/portal/repositorio2/resumen/NR_I1697.pdf',
            filas=[
                dict(nombre='Fundaciones y entidades fiscalizadas', valor=37, unidad='entidades', nota='Ámbito del informe'),
                dict(nombre='Aportaciones y donaciones privadas 2023', valor=4720920.87, unidad='euros', nota='Conclusión 7 (4,12 M€ en 2022)'),
                dict(nombre='Subvenciones públicas recibidas 2023', valor=2125330.16, unidad='euros', nota='Conclusión 8; sobre todo de Cultura y Deporte y de Asuntos Exteriores; en la muestra, gastos correctamente justificados con carácter general'),
                dict(nombre='Cuentas remitidas en plazo', valor=15, unidad='de 37 entidades', nota='18 fuera de plazo y 4 sin remitir (conclusiones 1 y 2)'),
                dict(nombre='Entidades inscritas en el Registro de Partidos', valor=22, unidad='entidades (19 fundaciones + 3 entidades)', nota='15 sin inscribir (gráfico de la conclusión 4)'),
                dict(nombre='Fundaciones y asociaciones sin actividad en 2023', valor=10, unidad='entidades', nota='Conclusión 5'),
                dict(nombre='Fundaciones con patrimonio neto negativo', valor=5, unidad='fundaciones', nota='Conclusión 6; es un dato contable, no una irregularidad'),
                dict(nombre='Entidades que no publicaron sus cuentas de 2023 en la web', valor=14, unidad='entidades', nota='Conclusión 9')]),
        resolucion_cortes=dict(texto='La Comisión Mixta con el Tribunal de Cuentas aprobó el 21-may-2026 una resolución sobre el informe de fundaciones 2021-2022 que insta al Gobierno a exigir auditoría externa anual y reequilibrio patrimonial como requisito para recibir ayudas, y al Ministerio del Interior a exigir la inscripción en el Registro de Partidos.', fuente='https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-15347', nivel='P', fecha='2026-07-14 (BOE)')),
    altos_cargos=dict(
        nivel='P', fecha_dato='2026-11-10', fuente='https://digital.gob.es/funcion-publica/incompatibilidad-y-conflicto-intereses/informe-cumplimiento-altos-cargos',
        texto='La Oficina de Conflictos de Intereses eleva cada seis meses al Congreso un informe (art. 22 Ley 3/2015). El del primer semestre de 2026 (firmado el 2-jul-2026, 64 páginas) lista nominalmente los altos cargos en activo a 30-jun-2026 y declara «NINGUNO» en procedimientos sancionadores incoados y resueltos (Ley 3/2015 y Ley 19/2013). No se cuentan aquí los altos cargos ni se reproducen nombres.',
        nota='Las declaraciones de bienes de quienes tomaron posesión o cesaron en 2025 se publicaron en el BOE del 31-mar-2026 (BOE-A-2026-7339): aquí solo el agregado, sin nombres. Sueldos: ver el bloque «Número de cargos y retribuciones oficiales».',
        boe=ACB),
    pendiente=[
        dict(tema='Cuentas de los partidos: ejercicios 2021 en adelante', estado='no publicado',
             detalle='En la lista de informes de partidos del Tribunal de Cuentas (leída el 12-nov-2026) el último informe sobre las cuentas anuales de los propios partidos sigue siendo el n.º 1.573, del ejercicio 2020 (Pleno 27-jun-2024). Sí hay informe nuevo de fundaciones: n.º 1.697, ejercicio 2023 (22-sep-2026), ya volcado.',
             fuente='https://www.tcu.es/es/partidos-politicos/Informes/', nivel='P'),
        dict(tema='Altos cargos: declaraciones de bienes de quienes siguen en el cargo', estado='no leído',
             detalle='El BOE solo publica cada año las declaraciones de quienes tomaron posesión o cesaron el año anterior (332 en 2025). El patrimonio de quienes siguen en activo sin cambio de cargo no se publica de nuevo: [VERIFICAR] en el Portal de Transparencia.',
             fuente='https://transparencia.gob.es/', nivel='V'),
        dict(tema='Congreso: sentido del voto por iniciativa', estado='parcial',
             detalle='El histórico agrega por sesión, año y grupo. No se guarda el resultado de cada votación con su título (son 2.175) ni qué mayoría exigía cada una; el ZIP oficial de cada sesión está enlazado en los datos.',
             fuente='https://www.congreso.es/es/opendata/votaciones', nivel='P'),
        dict(tema='Senado: listado oficial de sesiones incompleto', estado='parcial',
             detalle='El fichero de sesiones plenarias del catálogo solo enumera hasta la sesión 60; los ficheros de votación existen hasta la 83 (29-sep-2026) y faltan los de 7 sesiones. Motivo no explicado en la web: [VERIFICAR].',
             fuente='https://www.senado.es/web/relacionesciudadanos/datosabiertos/catalogodatos/index.html', nivel='P')],
)
from leyendas_politica import con_leyendas  # C248: explicaciones en lenguaje llano
out = con_leyendas(out)
json.dump(out, io.open('explorador/espana-politica.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('ok', len(act), len(baj), len(vots), len(dec))
