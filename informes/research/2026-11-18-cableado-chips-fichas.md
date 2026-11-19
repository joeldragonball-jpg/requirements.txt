# Cableado de chips, fichas por activo y Macro España · 18-nov-2026

Solo vistas y código; no se tocó ningún dato salvo 2 unidades vacías en `fichas-activos.json`. Sin IA, sin API, sin `privado/`, sin commit ni push. Sin recomendaciones.

## 1. Chips y centros de datos en la Órbita
- `explorador.py`: `chips-manual.json` se carga en `D.chips_manual`.
- Panel nuevo «Chips y centros de datos: memoria, fabricantes y electricidad (ficha manual)» en la capa de Energía, junto al de FRED/Yahoo. Tablas: precios de memoria, revisiones del 17-nov, fabricantes (Micron, SK hynix, Samsung), electricidad y centros de datos (IEA, EIA STEO de noviembre incluido), caso alcista/bajista y pendientes.
- Cada cifra lleva fecha, nivel (todo S: resúmenes secundarios), fuente con enlace y chip [VERIFICAR] cuando la nota lo pide. Unidades explícitas en la cabecera (M$, billones de wones = 10^12, TWh = mil millones de kWh). Se quita el pendiente «falta cablear» (ya resuelto).
- Aviso: Micron oficial sigue sin leer (404) y la discrepancia 4.390/4.539 de la EIA queda [VERIFICAR].

## 2. Fichas por activo
- Los hechos de XRP, XLM, BTC, oro y ETF mundial ya salían; ahora cada fila marca «nuevo» (17-18 nov) y [VERIFICAR] (por texto o valor vacío). «null» se muestra «sin dato».

## 3. Macro España, «Pendiente de leer»
- Se ocultan las líneas RESUELTO (subyacente) y las superadas por una posterior del 18-nov (Euríbor diario, salario medio AEAT): de 9 a 6, con aviso de cuántas se ocultan. El JSON no se modificó.

## 4. C240 (unidad y escala)
- Tabla España frente a zona euro y EE. UU.: cabeceras con «(% PIB)» y «(p.p.)». Fichas: unidad para «número de valores» (MSCI) y «versión de protocolo» (Stellar). Barrido de las tablas de España: sin más cifras sin unidad detectadas por heurística.

## Comprobación
`revisar_explorador.py`: 0 avisos. `construir_orbita.py` y `construir_movil.py` ejecutados. Navegador («orbita»): 0 errores de consola, sin null/undefined/NaN visibles.
