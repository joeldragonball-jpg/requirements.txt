# Aplicado 11-nov-2026: mandatos (Chirac, NL) y plantilla del Senado

Origen: informes 2026-11-11-Chrome-EIA-Fed-mandatos.md y 2026-11-11-Chrome-cortes-cgpj-mandatos-DE-NL-PL.md. Edición puntual; JSON validados; diff: mandatos.json 10+/10-, espana-empleados.json 8+.

## Qué cambió
- explorador/mandatos.json (FR): Chirac pasa de S a P (inicio 17-may-1995, Elíseo leído 11-nov). La nota aclara que el fin (16-may-2007) sigue [S].
- mandatos.json (NL): Balkenende (22-jul-2002 a 14-oct-2010) y Schoof (2-jul-2024 a 23-feb-2026) pasan a P; fuente cambiada a la ruta rijksoverheid kabinetten-sinds-1945.
- mandatos.json (NL): Rutte se queda en S; nota: inicio 14-oct-2010 P, fin 2-jul-2024 por coherencia con Schoof [VERIFICAR].
- explorador/espana-empleados.json: nueva sección «SENADO (Cortes Generales)», empleados 568, nivel P, fecha «actualizado 14-oct-2026, leído 11-nov-2026», fuente senado.es; nota «568 = suma propia de 4 categorías; [VERIFICAR] si los 110 adscritos cuentan».

## Qué no cambió y por qué
- Sarkozy y Hollande siguen S (solo años P, día de traspaso S; elección ≠ inicio de mandato).
- DE y PL: sin lectura de día exacto; siguen S.
- Rutte: un solo campo de nivel por entrada; el fin no está leído literalmente, así que S.
- «CORTES GENERALES» queda con null (el Congreso no tiene total); el Senado va en sección aparte para no atribuirle al conjunto una cifra parcial. total_ministerios no se toca.
- Sin tocar cerebro/ ni EIA/Fed (no eran parte de esta tarea). No hay campo para desglose por categoría; el desglose va en la nota.
