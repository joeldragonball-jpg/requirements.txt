---
tema: Congreso, Senado, partidos y altos cargos (C242, tercera pasada)
etiquetas: [españa, congreso, senado, votaciones, tribunal-de-cuentas, altos-cargos, boe]
actualizado: 2026-11-13
---
# C242 · Histórico de votaciones, Senado, fundaciones 2023 y bienes de altos cargos

Lecturas del 12-nov-2026. Solo datos oficiales y agregados: **sin nombres, sin clasificaciones de mejor a peor**. Datos en `explorador/espana-votaciones.json` (nuevo, `scripts/leer_votaciones_congreso.py`) y `explorador/espana-politica.json` (`scripts/leer_congreso.py`). Vista: España › Política y leyes (3 bloques nuevos).

## HECHOS

### Congreso: histórico de votaciones del Pleno, XV legislatura [P, ZIP oficial de cada sesión]
- 2.175 votaciones nominales en 149 sesiones (147 días), del 19-sep-2023 al 2-oct-2026. Con más síes que noes: 993; con más noes: 1.163; empates: 19; decididas por 5 votos o menos: 222.
- Por año: 2023, 32 votaciones; 2024, 862; 2025, 741; 2026, 540 (en 2026 ganan los síes: 288 frente a 244; en 2024 y 2025 ganaban los noes).
- Lo que más se vota: mociones tras interpelación (623), dictámenes de leyes (508), proposiciones no de ley (314), enmiendas del Senado (249), tomas en consideración (113), convalidación de reales decretos-leyes (97).
- Por grupo (toda la legislatura; % de los votos emitidos por el grupo): el detalle está en la tabla de la Órbita, en orden alfabético. La columna «coincide con la opción más votada» va del 47,6 % al 77,0 % según el grupo.

### Senado [P, ficheros XML del catálogo de datos abiertos]
- Composición por grupos (fichero de la legislatura): 264 senadores en 7 grupos; el mayor tiene 144 (120 electos y 24 designados) y el segundo 87.
- 973 votaciones en 76 sesiones con fichero (3-oct-2023 a 29-sep-2026): 495 con más síes y 478 con más noes; **ninguna** decidida por 5 votos o menos (un grupo tiene mayoría absoluta).
- 274 iniciativas legislativas tramitadas, 201 con votación.
- Límite: el listado oficial de sesiones solo llega a la n.º 60 (7-oct-2025), pero hay ficheros de votación hasta la 83; faltan los de 7 sesiones (1, 10, 20, 27, 29, 36 y 68).

### Tribunal de Cuentas [P]
- Informe n.º 1.697 (Pleno 22-sep-2026), fundaciones y entidades vinculadas a partidos, ejercicio 2023: 37 entidades; aportaciones y donaciones privadas 4.720.920,87 € (4,12 M€ en 2022); subvenciones públicas 2.125.330,16 €; 15 rinden cuentas en plazo, 18 fuera de plazo y 4 no las rinden; 22 inscritas en el Registro de Partidos y 15 no; 10 sin actividad; 5 fundaciones con patrimonio neto negativo; 14 sin publicar sus cuentas.
- En la lista de informes de partidos de tcu.es (12-nov-2026) el último sobre las **cuentas de los propios partidos** sigue siendo el n.º 1.573, ejercicio 2020: no hay uno posterior.

### Altos cargos (Ley 3/2015) [P, BOE]
- Informes semestrales (BOE-A-2026-3366 y BOE-A-2026-16747): 819 altos cargos en activo a 31-dic-2025 y 823 a 30-may-2026. Procedimientos sancionadores por la Ley 3/2015: ninguno incoado ni resuelto en los dos semestres. Por la Ley 19/2013 (transparencia): **5 incoados** en el 2.º semestre de 2025, ninguno resuelto; ninguno en el 1.er semestre de 2026.
- Declaraciones de bienes publicadas en el BOE del 31-mar-2026 (BOE-A-2026-7339): 332 declaraciones (176 nombramientos y 156 ceses de 2025). Suma de activos 201,68 M€; pasivo 33,44 M€; neto 168,23 M€. **Mediana del patrimonio neto: 320.286 €**; la mitad central está entre 130.876 € y 572.222 €; 35 declaran más deudas que bienes. Por concepto (suma): inmuebles 78,81 M€, acciones cotizadas y deuda 46,45 M€, depósitos 33,76 M€, seguros y planes 23,12 M€, participaciones no cotizadas 14,16 M€.

## OPINIÓN (mía) y límites
- «Coincide con la opción más votada» no es una nota: un grupo que apoya al Gobierno coincide más cuando el Gobierno gana, y al revés. Tampoco distingue una ley de una proposición sin efecto jurídico.
- La suma del patrimonio está dominada por pocas declaraciones muy altas; por eso se da la mediana. El BOE no indica cómo se valoran los inmuebles [VERIFICAR], así que no es comparable con precios de mercado.
- Un procedimiento «incoado» es un expediente abierto, no una sanción.

## Pendiente
Patrimonio de quienes siguen en el cargo sin cambio (no se republica); título y mayoría exigida de cada votación; motivo de los ficheros que faltan en el Senado.

## Lecciones (máx. 5)
1. La página de votaciones del Congreso admite fecha (`targetDate`) solo para los días que lista en `diasVotaciones`.
2. El listado de un catálogo puede estar incompleto aunque los ficheros existan: probar la numeración.
3. Con datos nominales públicos, agregar antes de guardar: el repo no necesita los nombres.
4. Los ficheros del Senado van en ISO-8859-1 y con etiquetas distintas («NO VOTAN»).

## Fuentes
- Congreso, votaciones: https://www.congreso.es/es/opendata/votaciones
- Senado, catálogo: https://www.senado.es/web/relacionesciudadanos/datosabiertos/catalogodatos/index.html
- Tribunal de Cuentas, informe 1.697 (resumen): https://www.tcu.es/export/sites/portal/repositorio2/resumen/NR_I1697.pdf
- BOE: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-7339 · BOE-A-2026-3366 · BOE-A-2026-16747
