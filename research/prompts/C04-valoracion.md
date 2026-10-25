# C04 · Cuadro de valoración por sector (PER, EV/EBITDA, FCF yield)

Coste estimado: ~3 % de la cuota semanal · Cuándo: hueco del Centro; sin día fijo (lanzar solo si el semanal está por debajo del 70 %)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C04: Cuadro de valoración por sector (PER, EV/EBITDA, FCF yield).
Fuentes: SEC EDGAR XBRL (companyfacts), Yahoo, informes de las empresas.
Haz: 1) prueba qué fuente SIN navegador da múltiplos fiables y gratis (SEC EDGAR companyfacts [P] para beneficio y flujo de caja; Yahoo quoteSummary si funciona sin clave); 2) para Defensa, Energía, Ciberseguridad y Semiconductores toma 4-5 valores de `watchlist.toml` y ETF sectoriales y calcula PER, EV/EBITDA y FCF yield con fecha y fuente; 3) señala qué sesgos tiene cada múltiplo (ciclo, contabilidad) y marca [VERIFICAR] lo no contrastado; 4) propón el panel (campos, fuente, frecuencia) y el esfuerzo.
Salida: `informes/research/AAAA-MM-DD-C04-valoracion-sectorial.md`.
Al acabar actualiza el estado de este hueco en `explorador/centro.json` (falta → hecho o parcial).
```
