# C14 · Órbita: capas nuevas (energía, liquidez, riesgos) y enlace de cada elemento a su informe

Coste estimado: ~3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C14: Órbita: capas nuevas (energía, liquidez, riesgos) y enlace de cada elemento a su informe.
Lee `explorador/datos.json` (9 capas, 44 movimientos), `explorador/mapa.html` y `scripts/revisar_explorador.py`. Haz: 1) añade 3 capas nuevas con el mismo formato que las existentes: «energia» (Ormuz con barcos al día de IMF PortWatch, Brent y WTI spot de la EIA, OPEP+, STEO; informes W10 y T18), «liquidez» (M2 de EE. UU., Japón y China, M3 del euro, tipos oficiales; informe C02 y W01) y «riesgos» (los 7 escenarios de `informes/research/2026-10-25-C03-matriz-de-riesgos.md`, con probabilidad [ESPECULACIÓN]); cada elemento con su nivel [P]/[S], fuente, fecha y entidades; 2) añade un campo `informe` (ruta en `informes/`) a los elementos que ya tengan un informe detrás y haz que `mapa.html` muestre un enlace «Abrir el informe» cuando exista; 3) amplía `scripts/revisar_explorador.py` para validar el campo nuevo; 4) 0 avisos y sin recomendaciones de compra o venta.
Salida: JSON y mapa actualizados e `informes/research/AAAA-MM-DD-C14-orbita.md` corto. Edita con cuidado (JSON válido, mismo formato). No hagas commit.
Al acabar: fila C14 de `research/COLA.md` con el coste real (get_usage antes y después), `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`.
```
