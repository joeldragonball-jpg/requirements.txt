# C08 · Consolidar el archivo principal del cerebro (opción B)

Coste estimado: ~4 % de la cuota semanal · Modelo: Opus · Cuándo: sesión NUEVA tras el reinicio del martes 27-oct (03:00), no antes

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C08: Consolidar el archivo principal del cerebro en un resumen vigente (opción B autorizada por Joel el 25-oct-2026, UNA sola vez).
Contexto: `cerebro/apuntes_xrp_macro_fiscalidad_2026.md` (~80 KB) acumula afirmaciones antiguas junto a sus correcciones y repite datos (el litigio SEC-Ripple en 5 sitios, CLARITY, Fed, adquisiciones de Ripple, MEI, ITP). Ya existen `cerebro/documentos/estado-vigente-y-correcciones.md` (lo vigente) e `informes/research/2026-10-25-revision-cerebro-contradicciones.md` (hallazgos y veredictos). La revisión automática está en `informes/2026-10-25-revision.md`.
Excepción a la regla 5 de CLAUDE.md, solo para esta tarea: NO borres ni reescribas ningún archivo. Haz lo siguiente:
1) NO leas el archivo entero de una vez: lista sus secciones con Grep (`^## `) y trabaja sección a sección con `python scripts/buscar_informes.py` y lecturas por rango de líneas.
2) Crea `cerebro/documentos/resumen-vigente-xrp.md` con el formato fijo del cerebro (tema, etiquetas, actualizado y las 9 secciones) con SOLO lo vigente: cada dato una vez, con fuente, fecha y nivel [P]/[S]/[VERIFICAR]/[ESPECULACIÓN]; donde haya contradicción, aplica el veredicto del informe de revisión y el archivo de estado vigente; hechos separados de opiniones; caso alcista y bajista donde proceda.
3) Añade al FINAL del archivo antiguo UNA sola línea (añadir está permitido): «HISTÓRICO desde 2026-10-25: el estado vigente está en cerebro/documentos/resumen-vigente-xrp.md». No toques nada más de ese archivo.
4) Lista en el propio resumen vigente lo que NO se pudo resolver (ITP de Cataluña, SEC-CFTC y XRP/XLM, sección 404, fuente de cada adquisición de Ripple, base del −1,05 % de XRPN) como [VERIFICAR] con la tarea que lo cerrará (lote W05).
5) Avisa a Joel del coste de la app: procesar.py lee todos los .md de `cerebro/`; el nuevo archivo suma tamaño, así que dime los KB de antes y después.
Salida: `cerebro/documentos/resumen-vigente-xrp.md` y `informes/research/AAAA-MM-DD-C08-consolidacion.md` (qué se fusionó, qué se descartó y por qué).
Al acabar actualiza la fila C08 de `research/COLA.md` y `explorador/centro.json` si procede.
```
