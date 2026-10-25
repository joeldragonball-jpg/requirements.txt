# C07 · Control de suscripciones y software (privado)

Coste estimado: ~(Joel aporta datos) de la cuota semanal · Cuándo: hueco del Centro; sin día fijo (lanzar solo si el semanal está por debajo del 70 %)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C07: Control de suscripciones y software (privado).
Fuentes: Solo datos que Joel escriba; nada de claves ni facturas.
Haz: 1) crea la plantilla `privado/suscripciones.md` (esa carpeta NO se sube) con columnas: servicio, coste mensual, renovación, qué se usa de verdad, alternativa gratis, decisión; 2) pide a Joel los datos y calcula el coste anual y qué recortar; 3) NO escribas nada de esto en el repo público ni en `cerebro/`.
Salida: solo `privado/suscripciones.md`.
Al acabar actualiza el estado de este hueco en `explorador/centro.json` (falta → hecho o parcial).
```
