# C127 · Auditoría visual del tablero (Órbita, `explorador/vistas.html`)

Origen: Joel, 4-nov-2026. «Las cifras clave son todo número, terriblemente para leer. Se puede sacar mucho más provecho en lo visual. España tiene demasiadas cosas y se podría ordenar mucho mejor. Noticias, voces, panel de datos y Países van bastante bien.»

## Qué se ve hoy (comprobado en Chrome el 4-nov, app en localhost:8793, pestaña Cerebro)
- **Resumen · Cifras clave:** 19 tarjetas iguales, todas con el mismo peso. Mezclan cripto, bonos, energía, comida, miedo, chips y España sin orden. Cada una lleva una línea gris pequeña que hay que leer para saber qué es (p. ej. «XRP · capitalización», «Brent (futuro)»). Capitalización y Brent son datos secundarios con el mismo peso que el resto.
- **España:** una pestaña larguísima, tabla tras tabla (economía, deuda autonómica, presupuesto, pagos, mortalidad, carretera, delitos…). Sin índice ni jerarquía.

## Qué hay que hacer (en este orden; propuestas, no decisiones)
1. **Mirar antes de tocar:** abrir cada pestaña en Chrome (`localhost:8793` → Cerebro) y anotar 3 problemas concretos por pestaña (qué estorba, qué falta, qué se repite). Entregar la lista a Joel antes de cambiar código.
2. **Cifras clave → pocas y agrupadas:** 4-6 bloques con título (Mercado cripto, Tipos y deuda, Energía y materias primas, Miedo y chips, España). Dentro de cada bloque, 1 cifra grande (la importante) y las demás pequeñas. Etiqueta corta en lenguaje llano arriba, no debajo. Mini-gráfico (sparkline) o color en vez de texto cuando se pueda. Lo secundario (capitalización, futuros) fuera de la primera pantalla o plegado.
3. **España → ordenada por temas:** índice o pestañas internas (Economía y deuda · Presupuesto y gasto · Servicios y sociedad · Seguridad y salud), con un resumen visual al principio (3-5 cifras con flecha) y el detalle plegado.
4. **Criterios:** primero lo que cambia una decisión de Joel; verde/rojo solo cuando hay juicio claro; nunca una cifra sin fecha ni nivel [P]/[S]; sin mezclar unidades (millones, millardos, €/MWh) en la misma fila sin explicar.
5. Revisar noticias, voces, panel de datos y Países solo para detectar fallos (Joel las ve bien).

## Reglas
- Sin llamar a la API de Anthropic ni lanzar workflows. Commit y push solo con «sube».
- Al terminar: fila de resultado en `research/tareas.csv` y regenerar `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`.
- Coste estimado: Sonnet M, ~3-4 % de la semanal (la fase 1 sola, ~1 %).
