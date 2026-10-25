# C02 · Liquidez global (M2) y agregados monetarios

Coste estimado: ~1,5 % de la cuota semanal · Cuándo: hueco del Centro; sin día fijo (lanzar solo si el semanal está por debajo del 70 %)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C02: Liquidez global (M2) y agregados monetarios.
Fuentes: FRED (M2SL), BCE (M3), Banco de Japón, Banco Mundial.
Haz: 1) lee con curl y User-Agent propio el M2 de EE. UU. (FRED CSV), el M3 de la zona euro (BCE Data Portal) y, si hay fuente abierta, Japón y China; 2) calcula la variación interanual y la tendencia de los últimos 12 meses; 3) explica qué se dice de la relación liquidez-activos de riesgo SIN afirmar causalidad (caso a favor y en contra) y marca [ESPECULACIÓN] lo que lo sea; 4) di qué series se pueden automatizar en el panel (sin IA).
Salida: `informes/research/AAAA-MM-DD-C02-liquidez-m2.md`.
Al acabar actualiza el estado de este hueco en `explorador/centro.json` (falta → hecho o parcial).
```
