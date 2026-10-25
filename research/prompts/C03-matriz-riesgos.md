# C03 · Matriz de riesgos y escenarios de estrés (cisnes negros)

Coste estimado: ~3 % de la cuota semanal · Cuándo: hueco del Centro; sin día fijo (lanzar solo si el semanal está por debajo del 70 %)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C03: Matriz de riesgos y escenarios de estrés (cisnes negros).
Fuentes: Informes ya hechos (T/D/R), calendario, radar.
Haz: 1) con `python scripts/buscar_informes.py` reúne lo ya investigado (Ormuz y energía, deuda de EE. UU./Japón/Francia, Taiwán, regulación cripto, fix del XRPL, bancos centrales); 2) construye 6-8 escenarios con: disparador observable, indicador que ya está en la app, probabilidad a 12 meses marcada [ESPECULACIÓN], impacto cualitativo en tipos, bolsas, petróleo y cripto, y qué lo desmentiría; 3) para cada uno, caso alcista y bajista y sesgo de las fuentes; 4) tabla resumen ordenada por impacto×probabilidad.
Salida: `informes/research/AAAA-MM-DD-C03-matriz-de-riesgos.md`. Nada de recomendaciones de compra o venta.
Al acabar actualiza el estado de este hueco en `explorador/centro.json` (falta → hecho o parcial).
```
