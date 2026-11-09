# C240 · Formato de cifras: unidad explícita en todas las tablas (España primero)
Problema (Joel, 9-nov): en tablas con millones no se distingue si «1.234» son miles, millones o «mil millones», ni si el separador es coma o punto. Regla nueva y única para móvil, Órbita y PC:
1. Toda cifra monetaria lleva unidad y escala visibles: «M€» = millones de euros, «mil M€» = miles de millones, «€» sin escala; en dólares «M$». Nunca solo «1.234».
2. Formato español: punto de miles y coma decimal (1.234,5 M€); en JSON siempre número puro + campos `unidad` y `escala` (sin separadores).
3. Cabecera de cada tabla dice la unidad («Importes en M€»); si hay unidades mezcladas, una columna «Unidad».
4. Auditoría: recorre `explorador/espana*.json`, presupuesto, deuda, sueldos y tipos con un script local `scripts/auditar_unidades.py` (cifras sin unidad, escala mezclada, separadores ambiguos) y corrige los casos en el JSON y en `docs/movil/index.html` y `construir_orbita.py`. Empieza por España, luego el resto.
5. Entrega: informe `informes/research/AAAA-MM-DD-C240-unidades.md` con antes/después de 10 ejemplos, y regenera móvil y Seguimiento.
Reglas: no cambiar valores, solo presentación y metadatos; nada de API de Anthropic.
