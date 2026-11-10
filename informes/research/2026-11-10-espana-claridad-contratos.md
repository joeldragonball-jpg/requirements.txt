# España · claridad en contratos, subvenciones y registros por día (10-nov-2026)

Tarea C251. Bloques tocados en `explorador/vistas.html` (subpestaña «Dónde va el dinero»): contratos públicos (PLACSP), subvenciones concedidas (BDNS) y «registros por día».

## Qué cambia para quien lo lee
- Arriba de cada bloque hay 3-4 frases llanas: qué es un **expediente** (un procedimiento de contratación con número propio; no es una ley), **presupuesto de licitación** (máximo previsto) frente a **adjudicado** (importe final, 0 si aún no hay adjudicación; en acuerdos marco es un techo común), qué NO dice (un contrato grande no es irregularidad; no es toda la contratación: faltan plataformas autonómicas y locales) y el alcance (solo octubre de 2026 en PLACSP; ventana de 60 días en BDNS; personas físicas enmascaradas, 31 % del importe concedido).
- Cada columna lleva su unidad: «n.º de expedientes / concesiones / convocatorias» (cantidades) frente a «M€» (millones de euros, sin IVA). Cada tabla tiene una entradilla de una frase.
- Los tipos de procedimiento llevan su explicación en la propia fila (abierto, simplificado, restringido, negociado, contrato menor, acuerdo marco…). Nivel concedente e instrumento (subvención/préstamo/garantía) también.
- Las leyendas se guardan en el JSON (`leyenda`) desde `scripts/leyendas_contratacion.py`.

## Fallo de datos encontrado y corregido [P]
La lista oficial de códigos de procedimiento de la PLACSP (SyndicationTenderingProcessCode 2.07, https://contrataciondelestado.es/codice/cl/2.07/SyndicationTenderingProcessCode-2.07.gc, leída 10-nov-2026) dice: **3 = Negociado SIN publicidad, 4 = Negociado CON publicidad, 13 = Licitación con negociación**. El script tenía 3 y 4 cambiados y no conocía 11-13. Consecuencias que había antes: el «código 13» no se entendía; los 2.256 expedientes del código 3 se llamaban «con publicidad» y el contador de «negociado sin publicidad» por órgano y el 0,3 % eran en realidad el código 4. Tras corregir `scripts/leer_contratacion.py` y releer octubre: negociado sin publicidad = 2.256 expedientes (5,64 %), con publicidad = 134, licitación con negociación = 108. Que haya un 5,6 % sin publicidad es legal en los casos tasados, pero es dato a mirar; no implica irregularidad.

## Mezcla de temas
Los tres bloques encajan en «Dónde va el dinero». El de «registros por día» solo cuenta anuncios (convocatorias, anotaciones del feed), no dinero: está bien ahí pero conviene que Joel lo vea como «ritmo de publicación».

## Pendientes
- Los «mayores contratos» incluyen adjudicaciones de años anteriores que se movieron en octubre; está avisado en el bloque.
- Verificación visual hecha a 375 px y escritorio, sin errores de consola. No se ha hecho commit ni push.
