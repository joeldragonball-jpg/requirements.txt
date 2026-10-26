# C12 · Cerebro del escritorio al día: índice autogenerado de la investigación

Coste estimado: ~1 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C12: Cerebro del escritorio al día: índice autogenerado de la investigación.
Haz: 1) escribe `scripts/indice_investigacion.py` (sin IA, solo biblioteca estándar) que recorra `informes/`, `informes/research/`, `informes/dossiers/` e `informes/videos/` y genere `cerebro/documentos/indice-investigacion.md` con el formato del cerebro: por tema (macro y tipos, deuda, energía y Ormuz, regulación por país, cripto y ETF, fiscal, voces y predicciones, auditorías) los 3-5 informes más recientes con fecha, título, ruta y UNA frase sacada de su apartado «Resumen»; tope de 15 KB; 2) enlázalo con `cerebro/documentos/estado-vigente-y-correcciones.md` y `resumen-vigente-xrp.md` (añadir una línea, no reescribir); 3) comprueba que `cerebro_bot/procesar.py` y `cerebro.py` lo leen y que el tamaño total de `cerebro/` no sube más de 15 KB (dime los KB antes y después); 4) añade el paso a la rutina: al terminar cada tarea se ejecuta `python scripts/indice_investigacion.py` junto a los dos `construir_*` (actualiza `.claude/commands/research.md`).
Salida: script, índice e `informes/research/AAAA-MM-DD-C12-indice-cerebro.md` corto. No hagas commit.
Al acabar: fila C12 de `research/COLA.md` con el coste real (get_usage antes y después), `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`.
```
