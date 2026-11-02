# C71 (2-nov-2026): euríbor, hipotecas y crédito (BCE), materias primas, más bolsas y ficha «De dónde sale»

Informe reconstruido a posteriori (la tarea no dejó informe propio). Base: fila C71 de `research/tareas.csv` y `git show 32b4139 --stat`. Etiquetas: [P] fuente primaria · [S] prensa/agregador · [VERIFICAR] no re-verificado al escribir esto. Sin recomendaciones.

## Qué se hizo (hecho, según el commit 32b4139)
- `scripts/actualizar_paneles.py`: nueva `leer_credito` (8 series de la API abierta del BCE: euríbor 12 m, tipos de hipotecas y saldos de crédito a hogares y empresas, zona euro y España) [P].
- Nueva `leer_materias` (7 futuros de Yahoo: oro, plata, cobre, gas natural Henry Hub, trigo, maíz, café) [S]: Yahoo es agregador, no fuente oficial.
- 7 índices más en Mercado (DAX, CAC 40, FTSE 100, Nifty 50, Bovespa, ASX 200, VIX) [S].
- `explorador/paneles.html`: pestaña Tipos con crédito y pestaña «De dónde sale» (diccionario PROC con fuente, cadencia y qué mide cada panel). `explorador/paneles.json` regenerado. Sin capas nuevas en datos.json.
- Se añadieron a la cola C72 (crédito EE. UU. y otros) y C73 (vivienda e hipotecas de España).

## Lectura y avisos
- Las series del BCE son mensuales y de última fecha distinta por serie; no mezclar fechas al compararlas.
- Las materias primas son futuros (precio de contrato, no al contado) y cotizan en dólares; Yahoo puede fallar o retrasarse [S].
- Auditoría posterior (2-nov, tras W08) detectó: la fuente global de Crédito decía solo «BCE» tras añadir Freddie Mac y Banco de Inglaterra (C72), y un hueco en jun-2026 en crédito a hogares de España que sí está en la API del BCE (causa sin explicar, [VERIFICAR]).

## No re-verificado en este informe
- Cifras concretas de las series y sus fechas: no se re-leyeron aquí; las vigentes están en `explorador/paneles.json` (regenerado hoy).
- Que Yahoo devuelva los 7 contratos con el mismo símbolo en cada ejecución [VERIFICAR].
