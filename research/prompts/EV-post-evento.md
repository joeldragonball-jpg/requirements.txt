# EV · Research posterior a un evento del calendario

Coste estimado: ~1-2 % de la cuota semanal · Cuándo: cuando el PLANNING marque un evento pasado «SIN research»

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea EV: research posterior a un evento del calendario (usa el evento que te indique Joel: fecha y título; búscalo en `eventos/calendario.toml`).
Haz: 1) qué se dijo, decidió o anunció, con la fuente primaria en su idioma (comunicado, acta, nota oficial, blog del proyecto) y hora; lo que solo sea titular, [S] o [VERIFICAR]; 2) cifras con fecha y comparación con lo esperado (si el calendario traía una expectativa); 3) para eventos de proyectos o conferencias (Swell, Meridian, etc.): anuncios técnicos o de producto, y si se habló de incidentes, vulnerabilidades o auditorías, citando la fuente; los anuncios no son hechos hasta que se confirmen; 4) efecto en tipos, deuda, liquidez o cripto solo si cambia la conclusión, con caso alcista y bajista y sesgo de las fuentes; 5) qué fechas o tareas nuevas genera (añádelas al calendario y a `research/COLA.md` con prompt).
Salida: `informes/research/AAAA-MM-DD-EV-<slug-del-evento>.md` (máx. 1 página). Al acabar: marca el evento en `eventos/revisados.json` (clave `AAAA-MM-DD|primeras palabras del título`, estado hecho, informe), regenera con `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y anota el coste real.
```
