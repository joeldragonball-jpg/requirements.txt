# W05 · Verificación por lotes de [VERIFICAR] (jueves)

Coste estimado: ~3 % de la cuota semanal · Cuándo: Jueves

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea W05: Verificación por lotes de [VERIFICAR] (jueves).
Contexto: hay ≈ 1.655 menciones de [VERIFICAR] en 155 archivos (sobre todo los dossiers G12 fiscalidad, G8 inmobiliaria, G3 avales, G4 renta fija y G11 startups). No se reescriben los informes originales: se cierran en un consolidado.
Haz: 1) con `python scripts/buscar_informes.py "VERIFICAR" -n 30` elige 15-20 de los más RELEVANTES (cripto, regulación, ETF, macro, fiscalidad cripto de España; deja inmobiliaria y startups para el final); 2) para cada uno busca la fuente primaria, lee el dato y decide: confirmado [P] / corregido / sigue sin verificar (explica por qué); 3) anótalos en `informes/research/verificaciones-consolidado.md` (tabla: ID, afirmación, archivo de origen, resultado, fuente y fecha) añadiendo siempre al final, nunca borrando; 4) si un resultado cambia un dato de `explorador/*.json` o `cerebro/documentos/`, corrígelo añadiendo, no reescribiendo (regla del cerebro: solo líneas nuevas).
Salida: el consolidado y un conteo «cerrados / quedan» para el Seguimiento.
```
