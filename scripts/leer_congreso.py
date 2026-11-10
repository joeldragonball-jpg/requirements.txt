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
        nota='Solo la última sesión plenaria que muestra la página. El histórico por sesión y el voto por grupo («Detalle» y ZIP) no se leyeron: el selector de fecha no admite consulta directa. [VERIFICAR] / pendiente.'),
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
        resolucion_cortes=dict(texto='La Comisión Mixta con el Tribunal de Cuentas aprobó el 21-may-2026 una resolución sobre el informe de fundaciones 2021-2022 que insta al Gobierno a exigir auditoría externa anual y reequilibrio patrimonial como requisito para recibir ayudas, y al Ministerio del Interior a exigir la inscripción en el Registro de Partidos.', fuente='https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-15347', nivel='P', fecha='2026-07-14 (BOE)')),
    altos_cargos=dict(
        nivel='P', fecha_dato='2026-11-10', fuente='https://digital.gob.es/funcion-publica/incompatibilidad-y-conflicto-intereses/informe-cumplimiento-altos-cargos',
        texto='La Oficina de Conflictos de Intereses eleva cada seis meses al Congreso un informe (art. 22 Ley 3/2015). El del primer semestre de 2026 (firmado el 2-jul-2026, 64 páginas) lista nominalmente los altos cargos en activo a 30-jun-2026 y declara «NINGUNO» en procedimientos sancionadores incoados y resueltos (Ley 3/2015 y Ley 19/2013). No se cuentan aquí los altos cargos ni se reproducen nombres.',
        nota='El contenido de las declaraciones de bienes y derechos de cada alto cargo no se leyó (Portal de Transparencia / Registro de Bienes y Derechos Patrimoniales): [VERIFICAR]. Sueldos: ver el bloque «Número de cargos y retribuciones oficiales».'),
    pendiente=[
        dict(tema='Cuentas de los partidos: ejercicios 2021 en adelante', estado='no publicado/no leído',
             detalle='El último informe del Tribunal de Cuentas sobre las cuentas de los propios partidos que se leyó es el del ejercicio 2020 (Pleno 27-jun-2024). Si existe uno posterior: [VERIFICAR] en tcu.es. El endpoint BDNS «partidospoliticos» (6.638 concesiones) devuelve entidades de todo tipo (probado: una asociación de Castilla-La Mancha), por lo que no se usa como financiación de partidos.',
             fuente='https://www.tcu.es/', nivel='V'),
        dict(tema='Altos cargos: contenido de las declaraciones de bienes', estado='no leído',
             detalle='Registro de Bienes y Derechos Patrimoniales (Oficina de Conflictos de Intereses) y Portal de Transparencia: qué se publica de cada declaración no se comprobó. [VERIFICAR].',
             fuente='https://transparencia.gob.es/', nivel='V'),
        dict(tema='Senado', estado='no leído', detalle='Iniciativas y votaciones del Senado no consultadas: [VERIFICAR] en senado.es.',
             fuente='https://www.senado.es/', nivel='V')],
)
from leyendas_politica import con_leyendas  # C248: explicaciones en lenguaje llano
out = con_leyendas(out)
json.dump(out, io.open('explorador/espana-politica.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('ok', len(act), len(baj), len(vots), len(dec))
