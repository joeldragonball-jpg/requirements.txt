# Macro de España en la Órbita y el móvil · 18-nov-2026

Solo vistas y código; no se tocó ningún dato (`espana-macro.json` queda igual). Sin IA, sin API, sin `privado/`, sin commit ni push. Sin recomendaciones.

## Qué se pinta (fuente: `explorador/espana-macro.json`, nivel P, leído 18-nov)
- **Inflación subyacente y grupos especiales (INE, tabla 76130, oct-2026)**: subyacente, subyacente a impuestos constantes, energía, carburantes, alimentos, servicios, bienes industriales (con y sin energía), aceite de oliva, hoteles. Unidad: «% anual (sobre el mismo mes de 2025)»; cada fila con su valor de septiembre.
- **EPA 3T-2026**: tasas de paro por sexo y edad (ya estaban en «Paro y empleo»; ahora sin textos «None»), **ocupados por sector** (% de los ocupados) y **temporalidad**: temporales en miles de personas y tasa de temporalidad marcada «CÁLCULO PROPIO», con aviso [VERIFICAR] (no es la oficial del INE; no comparable con la de afiliación).
- **Afiliación de octubre (Seguridad Social)**: extranjeros, afiliados ligados a la regularización (490.586, cifra de la nota oficial), Régimen General, autónomos, mujeres/hombres y afiliados por pensionista (unidad «afiliados por pensionista», antes «ratio»).
- **Paro registrado (SEPE, octubre)**: total, sexo, menores de 25, contratos, prestaciones (fecha sep-2026), inversión 2.134,8 M€ y variación mensual por sector (personas). Aviso: no es lo mismo que parados EPA.
- La atribución del repunte a la regularización queda como [VERIFICAR] (nota del bloque).

## Dónde
- Órbita: pestaña España, chip «Macro 17-nov» (grupos nuevos, mismo aplanado que el resto) y 3 cifras nuevas en el resumen de esa pestaña (subyacente, paro registrado, afiliados extranjeros).
- Móvil: Más, Datos, tarjeta nueva «España: inflación, empleo y paro (detalle)» (valor con unidad, fecha, nivel, nota y enlace a la fuente).

## Arreglos de paso
- Sin la palabra «null» ni «None» en lo que se ve: `scripts/espana_cifras.py` sustituye «null» por «sin dato» en las notas y no escribe «Anterior: None» cuando falta el dato del año anterior (16-19 y 20-24 años en 3T-2025).
- «Anterior» ahora lleva unidad cuando es % o M€.

## Comprobación
`revisar_explorador.py`: 0 avisos. `construir_orbita.py` y `construir_movil.py` ejecutados. Navegador integrado (configuraciones «orbita» y «movil»): España y la tarjeta nueva se ven, 0 errores de consola, ningún «null/None/undefined/NaN» visible.

## `scripts/indicadores.py`
No se tocó, a propósito: ese panel compara países con Eurostat, Banco Mundial y FMI, y estos bloques (IPC por grupos del INE, paro registrado del SEPE, afiliación) no tienen equivalente comparable en los otros 22 países. Ya se leen en la pestaña España. Si se quisiera, el IPC subyacente de España se podría añadir como indicador solo de ES vía `indicadores-manual.json`.

## Pendiente (no es de esta tarea)
- El bloque «Pendiente de leer (9)» de Macro sale de la lista `pendiente` del JSON, que aún puede mencionar la subyacente y las vistas ya resueltas.
- `docs/movil/index.html` es HTML escrito a mano (construir_movil.py solo genera `data.json`): ahí está el código de la tarjeta.
