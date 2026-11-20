# Correcciones de la auditoría de integración (20-nov-2026)

Solo código (`scripts/construir_movil.py`, `explorador/vistas.html`, `docs/movil/index.html`). Ningún JSON de datos editado. Sin commit, sin API.

## Arreglado
- **#2 `[object Object]`** (Paneles, ETF): `bloques_no_hechos` ahora muestra `t`+`n` de los objetos y la clave sin guiones bajos.
- **#3 «null»/«None» en el móvil**: `construir_movil.py` pasa todas las fichas de país por un saneador («(null)» a «(sin dato)», «null» y «None» a «sin dato»). Fertilizantes: «None · mes sin dato %» ahora sale «sin mes · mes sin dato · …» sin unidad duplicada; el nivel ya no se corta a 60 caracteres (140).
- **#4 `rendimiento_redes.xrpl.historia`**: pintado en Cadenas («Por qué siguen sin activarse», más `tvl_volumen` si llega a tener texto) y en el móvil (fila de «Cadenas: préstamos y bóvedas»).
- **#8 AR/SV**: `banco_central` (mandato sin leer = [VERIFICAR] tal como consta) y `hitos_datos` en la ficha de país de la Órbita y del móvil.
- **#5**: `comparativa_2024_2025` en España (bloque «Altos cargos y personal eventual: 2024 frente a 2025»): tabla por sección (art. 10 y 11), capítulos totales, nota de Cortes, estructura de secciones y cierre 19-nov.
- **#6 (parcial)**: el texto `limites` de `espana-empleados.json` (RPT del Consejo de Estado: 137 puestos dotados, 108 ocupados; puestos, no personas) se muestra en ese mismo bloque.
- **#9**: `chips-manual.actualizacion_19nov` en la vista de chips («Qué se intentó el 19-nov»).
- Incidencia propia detectada y corregida: un `const CP` duplicado rompía todo el JS de las vistas (Órbita vacía); renombrado a `CMP`. Comprobado con `node --check`.

## Comprobación
`revisar_explorador.py`: 0 avisos. Regenerados movil, orbita y seguimiento. Chrome headless por CDP (puerto propio, procesos cerrados): 12 vistas de la Órbita (con pliegues abiertos y botones internos) y 5 pestañas + Datos/Noticias/Centro del móvil: 0 «[object», «undefined», «NaN», «(null)» ni «None» visibles. Quedan «null» como palabra en prosa: textos de tareas del Seguimiento (C68, C233, C247, C280) y la leyenda «null = sin dato» de la nota de estabilidad; no son fallos de pintado.

## Queda
- **#6 datos**: poner `empleados: 137`, `comparable: false` y nota «puestos dotados» en la sección CONSEJO DE ESTADO de `espana-empleados.json` (no toqué datos).
- Medias no hechas: #7 (subvenciones y contratación, tres tablas y columnas por verificar), #10 (`tipos_activo` en el móvil, decisión de diseño), #11 hecho; #12 (4 bloques), bajas #13-#17 (incl. `_resumen` que pierde barras bajas en `explorador.py`).
- #1 resuelto en lo regenerable; los datos de otros agentes que se escriban después exigen repetir `construir_movil.py`, `construir_orbita.py`, `construir_seguimiento.py`.
