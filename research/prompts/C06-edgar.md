# C06 · Vigilante de SEC EDGAR (ETF, DTCC, 13F)

Coste estimado: ~(código, sin IA) de la cuota semanal · Cuándo: hueco del Centro; sin día fijo (lanzar solo si el semanal está por debajo del 70 %)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C06: Vigilante de SEC EDGAR (ETF, DTCC, 13F).
Fuentes: API abierta de EDGAR (submissions) con User-Agent identificado.
Haz: 1) escribe `scripts/vigilante_edgar.py` calcado de `scripts/vigilante_federal_register.py` (misma memoria en `alertas/`, mismo aviso por Telegram, modo prueba sin token); 2) vigila filings nuevos (8-K, S-1, 424B, 19b-4) de los emisores de ETF de XRP y XLM y de DTCC, y avisa del plazo de los 13F (14-nov); 3) workflow `.github/workflows/edgar.yml` calcado del del Federal Register, con `permissions: contents: read`, SIN activarlo hasta que Joel diga «sube»; 4) prueba en modo prueba y enséñame el resultado.
Salida: script, workflow e `informes/research/AAAA-MM-DD-C06-edgar.md` corto con lo que vigila.
Al acabar actualiza el estado de este hueco en `explorador/centro.json` (falta → hecho o parcial).
```
