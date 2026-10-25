# C09 · Lote de verificación de dudas del cerebro (revisión del 25-oct)

Coste estimado: ~3 % de la cuota semanal · Cuándo: jueves tras el reinicio del martes (junto a W05) o semana de ahorro solo si el semanal está por debajo del 70 %

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C09: Lote de verificación de las dudas que dejó la revisión del cerebro del 25-oct-2026.
Lee `informes/research/2026-10-25-revision-cerebro-contradicciones.md` y `cerebro/documentos/estado-vigente-y-correcciones.md`. Webs que dan 403 (sec.gov): navegador integrado, sin saltar anti-bots.
Haz, por este orden, y anota el resultado con enlace y nivel [P]/[S]/[VERIFICAR]:
1) ITP joven en Cataluña: edad (32 o 35) y tramos del 10-13 %, en la Agència Tributària de Catalunya (atc.gencat.cat) o el DOGC.
2) Interpretación conjunta SEC-CFTC del 17-mar-2026: leer el texto oficial y decir si nombra a XRP y XLM y cuántos activos lista (¿16 o 18?).
3) «Sección 404» del proyecto CLARITY sobre intereses en stablecoins: localizar el borrador y citarlo, o decir que no existe.
4) Adquisiciones de Ripple (Hidden Road, GTreasury, Rail, Metaco, Standard Custody, Palisade, Solvexia, BC Payments): precio y fuente de cada una; suma con precio conocido.
5) Debut de XRPN (12-oct): precio de referencia, apertura 16,68 $ y cierre 16,91 $; de dónde sale el −1,05 %.
Salida: `informes/research/AAAA-MM-DD-C09-verificaciones-cerebro.md` con una fila por duda (resuelta / sigue abierta) y las líneas listas para añadir a `cerebro/documentos/estado-vigente-y-correcciones.md` (añadir, no reescribir). No toques el resto del cerebro.
Al acabar actualiza la fila C09 de `research/COLA.md`.
```
