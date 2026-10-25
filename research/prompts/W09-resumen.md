# W09 · Resumen semanal y siguiente semana (viernes tarde o domingo)

Coste estimado: ~1,5 % de la cuota semanal · Cuándo: Viernes tarde / domingo

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea W09: Resumen semanal y siguiente semana (viernes tarde o domingo).
Lee: los R00 de la semana (`informes/AAAA-MM-DD-apertura.md` y `-cierre.md`), los informes `W0x` de la semana, `research/COLA.md` y `docs/movil/seguimiento.json`.
Haz: 1) una página: qué cambió de verdad (tipos, deuda, regulación, ETF, XRP/XLM), qué se verificó, qué falló o quedó en [VERIFICAR]; 2) qué fechas de la semana siguiente importan (calendario) y qué prompts W0x toca lanzar; 3) coste real de la semana por tarea (columna «Real» de `research/COLA.md`) y % semanal restante; 4) lecciones (≤ 5 líneas por archivo) sin repetir; 5) propón el plan de la semana siguiente (modo normal o modo ahorro).
Salida: `informes/research/AAAA-MM-DD-W09-resumen-semanal.md`.
```
