# C16 · Revisión del coste de los bots que usan la API de Anthropic

Coste estimado: ~1 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C16: Revisión del coste de los bots que usan la API de Anthropic.
Haz: 1) lista los workflows y scripts que llaman a la API de Anthropic (`noticias`, `votos`, `cerebro`, `revision`, `verificar`, `cerebro_bot`) con modelo, frecuencia y tamaño de entrada (lee el código y los workflows; NO llames a la API ni toques secretos); 2) estima el coste mensual de cada uno con el precio actual del modelo que usan (comprueba el precio en la documentación oficial de Anthropic) y marca [VERIFICAR] lo no medible; 3) propón: qué pausar o espaciar, qué límite de gasto poner en la consola de Anthropic, y qué modelo más barato sirve; 4) di qué pasaría con cada bot el día que termine la suscripción de Claude (la API tiene facturación aparte).
Salida: `informes/research/AAAA-MM-DD-C16-costes-api.md`. No hagas commit.
Al acabar: fila C16 de `research/COLA.md` con el coste real (get_usage antes y después), `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`.
```
