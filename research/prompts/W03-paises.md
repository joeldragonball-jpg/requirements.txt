# W03 · Regulación por países: rellenar huecos del radar (miércoles)

Coste estimado: ~4 % de la cuota semanal · Cuándo: Miércoles

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea W03: Regulación por países: rellenar huecos del radar (miércoles).
Rotación de 4 semanas (2 países por sesión): sem. 1 Japón (T06) + Singapur (T08); sem. 2 Hong Kong (T09) + India (T10); sem. 3 China (T14) + Rusia (T12); sem. 4 Emiratos (T13) + BRICS/organismos (T15/T16). Después: Irán, Egipto, Etiopía, Sudáfrica, Indonesia (opcional).
Lee: la ficha del país en `explorador/regulacion.json` (celdas sin `etapa` = hueco; celdas solo [S] = subir a [P]), `research/COLA-TEMAS-GEMINI.md` (apartado del tema Txx) y su informe anterior (R0xP, matriz de jurisdicciones).
Haz: 1) para cada celda sin dato o solo [S] (prioridad ETF, custodia, tokenización, fiscal, CBDC) busca la fuente primaria en su idioma original (regulador, boletín oficial, banco central) y rellena etapa, estado, fecha, próxima fecha y `url` [P]; 2) plazos nuevos al calendario; 3) caso a favor / en contra y qué cambia para XRP/XLM y otros digital assets, sin recomendar nada; 4) deja [VERIFICAR] lo que no puedas leer en la fuente.
Gemini puede hacer una primera pasada gratis (prompt completo, no el código «Txx»); Claude solo verifica fuentes.
Salida: `informes/research/AAAA-MM-DD-Txx-pais.md`, `explorador/regulacion.json` (campo `revisado` = hoy) y `research/COLA-TEMAS-GEMINI.md` (estado de Txx).
```
