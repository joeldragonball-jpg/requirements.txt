# -*- coding: utf-8 -*-
"""Explicaciones en lenguaje llano (C248) que se anaden a explorador/espana-politica.json.
Lo llama leer_congreso.py antes de guardar; tambien se puede ejecutar solo (sin red):
    python scripts/leyendas_politica.py
Neutral: describe que es cada dato y que NO dice. Los significados de los codigos se han
deducido de los campos y ejemplos del propio fichero del Congreso (docacteco) y de la
terminologia parlamentaria; donde no hay definicion oficial leida se marca [VERIFICAR]."""
import io
import json

RES = {
    'Aprobado con modificaciones': 'El Congreso lo aprobó tras cambiar el texto. «Aprobado» aquí es un paso del Congreso: no equivale a ley publicada ni en vigor (falta el Senado y el BOE).',
    'Aprobado sin modificaciones': 'El Congreso lo aprobó tal como llegó. Igual que arriba: no equivale a ley en vigor.',
    'Caducado': 'No terminó su tramitación antes de acabar la legislatura (disolución de las Cortes); se anula sin votarse. No es un rechazo.',
    'Caducado sin calificación previa': 'Caducó (fin de legislatura) antes de que la Mesa decidiera si la admitía. No es un rechazo.',
    'Rechazado': 'El Pleno votó en contra (de la totalidad o del texto final). Es el único resultado negativo que sale de una votación.',
    'Retirado': 'Lo retiró quien lo presentó; no se votó.',
    'Decaído': 'Terminó sin votarse porque perdió su objeto (por ejemplo, no se defendió en el Pleno). No es un rechazo.',
    'Subsumido en otra iniciativa': 'Su contenido se integró en otra iniciativa parecida y se tramitó con ella.',
    'Inadmitido a trámite en términos absolutos': 'La Mesa del Congreso decidió no admitirla a debate.',
    'Inadmitido a trámite con requerimiento de aclaración': 'La Mesa no la admitió, o la paró, pidiendo antes una aclaración a quien la presentó [VERIFICAR el matiz exacto].',
    'Trasladado al próximo Congreso': 'Queda pendiente para la siguiente legislatura; no está ni aprobado ni rechazado.',
    'sin resultado': 'El fichero del Congreso no recoge resultado (puede estar aún en trámite o faltar el dato): [VERIFICAR].',
}
TIPOS = {
    'ACTIVIDAD': ('Actividad: empleo, cargo o negocio', 'Trabajo, cargo o actividad que el diputado declara (con empleador, sector público/privado, periodo y descripción). Ej. del fichero: «funcionaria, letrada-asesora».'),
    'DONACION': ('Donaciones o regalos recibidos', 'Regalos o donaciones que el diputado declara haber recibido. Muchos son del tipo «regalos de poca entidad en el ámbito familiar y social». No indica importes.'),
    'FUNDACIONES': ('Aportaciones a fundaciones u otras entidades', 'Aportaciones del diputado a una fundación o entidad (el fichero señala el destinatario, p. ej. una ONG). Definición formal no leída: [VERIFICAR].'),
    'OBSERVACIONES': ('Observaciones (texto libre)', 'Anotación libre del diputado; muchas dicen que no hay nada distinto de lo ya consignado en su declaración de bienes.'),
}
DECL = {
    'Declaración inicial': 'La que se hace al empezar el mandato.',
    'Modificación de la declaración de intereses económicos': 'Un cambio posterior a la declaración inicial.',
}
NORMAS = {
    'Leyes': 'Leyes ordinarias aprobadas por las Cortes. El fichero cuenta también las correcciones de errores como fila aparte.',
    'Leyes organicas': 'Leyes orgánicas: las que regulan derechos fundamentales, el régimen electoral o los estatutos (la Constitución exige mayoría absoluta del Congreso en la votación final).',
    'Reales decretos': 'Reales Decretos-leyes y Reales Decretos legislativos: los aprueba el Gobierno; el Congreso debe convalidar los primeros en 30 días. No son leyes votadas artículo a artículo.',
}
GRUPOS = 'Cada diputado pertenece a un grupo parlamentario (en general, su partido o coalición); «Mixto» reúne a los diputados sin grupo propio.'

EXPLICA = dict(
    composicion=(
        'Qué es: cuántos diputados figuran «en alta» en el fichero oficial del Congreso, por grupo parlamentario, y cómo votaron en la última sesión del Pleno. '
        'Unidades: personas (diputados) y votos (un voto = un diputado). '
        'Ojo: con las Cortes disueltas el 6-oct-2026 solo constan 137 en alta (de 350 escaños; 213 causaron baja ese día), así que esta tabla NO es el reparto de escaños de 2023 ni una encuesta. '
        'Un Real Decreto-ley se vota para convalidarlo; el recuento de «sí» y «no» no basta para saber su efecto: consúltalo en el BOE [VERIFICAR].'),
    iniciativas=(
        'Qué es: cuántas leyes se han propuesto en la XV legislatura y en qué estado quedaron. Las filas son estados de tramitación y cada número es un número de iniciativas (no euros ni votos). '
        'Proyecto de ley = lo presenta el Gobierno; proposición de ley = la presentan grupos, diputados, el Senado o parlamentos autonómicos. '
        'Qué NO dice: «Aprobado» es un paso del Congreso y no significa ley en vigor; «Caducado», «Decaído» o «Retirado» no son rechazos (la mayoría, simplemente, no llegó a votarse antes de la disolución). '
        'Cada fila trae a la derecha su significado.'),
    intereses=(
        'Qué es: las declaraciones de intereses que los diputados presentan en el Registro de Intereses del Congreso. «Recuento» = número de registros (líneas del fichero), NO euros ni millones: aquí no hay importes. '
        'Un diputado puede tener varios registros, y los 403 diputados con algún registro son más que los 137 en alta porque el fichero incluye a quienes ya causaron baja [VERIFICAR]. '
        'Qué NO dice: tener un registro no es una irregularidad ni una acusación; declarar es una obligación de todos. Los datos son recuentos, sin nombres. '
        'Los patrimonios y rentas completos están en otro registro (PDF por diputado) que no se ha leído.'),
    financiacion=(
        'Qué es: cifras de dos informes del Tribunal de Cuentas (organismo público que revisa las cuentas de los partidos y de sus fundaciones). Cada fila lleva su unidad: «M€» son millones de euros; «euros» son euros enteros; «partidos»/«entidades»/«donantes» son recuentos de unidades, no dinero. '
        'Fecha: el ejercicio que cubre cada informe (2020 y 2021-2022); hay un desfase de varios años. '
        'Qué NO dice: una «salvedad» o una observación del Tribunal es un reparo contable, no una sentencia ni una sanción firme; no se comparan partidos entre sí.'),
    altos_cargos=(
        'Qué es: el informe que la Oficina de Conflictos de Intereses envía al Congreso cada seis meses sobre los altos cargos del Gobierno (comprueba que no incumplen las incompatibilidades legales). '
        'Aquí solo se resume qué dice el informe de primer semestre de 2026; no se reproducen nombres ni se cuentan altos cargos. '
        'Qué NO dice: no incluye los bienes ni las rentas de cada alto cargo (otro registro, no leído) ni juzga a nadie. «Ninguno» es lo que declara el propio informe sobre sanciones.'),
    pendiente=(
        'Qué es: la lista de lo que todavía no se ha leído de la política española y por qué. «Nivel V» = sin verificar; no se rellena nada sin fuente.'),
)


def con_leyendas(o):
    ini = o['iniciativas']
    ini['leyenda_resultados'] = RES
    ini['leyenda_normas'] = NORMAS
    it = o['intereses']
    it['leyenda_tipos'] = {k: dict(nombre=v[0], texto=v[1]) for k, v in TIPOS.items()}
    it['leyenda_declaracion'] = DECL
    o['composicion']['leyenda_grupos'] = GRUPOS
    o['explicacion'] = EXPLICA
    return o


if __name__ == '__main__':
    p = 'explorador/espana-politica.json'
    d = json.load(io.open(p, encoding='utf8'))
    json.dump(con_leyendas(d), io.open(p, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print('ok')
