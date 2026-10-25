# C05 · Archivo de precedentes históricos (formato fijo)

Coste estimado: ~3 % de la cuota semanal · Cuándo: hueco del Centro; sin día fijo (lanzar solo si el semanal está por debajo del 70 %)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C05: Archivo de precedentes históricos (formato fijo).
Fuentes: FRED, Yahoo, bancos centrales, prensa fechada.
Haz: 1) crea `cerebro/documentos/archivo-de-precedentes.md` con el formato del cerebro y una tabla fija por precedente: evento, fecha, qué pasó con tipos, bolsas, petróleo, dólar y cripto (si existía), cuánto tardó en recuperarse, fuente [P]/[S]; 2) rellena 8-10 precedentes (p. ej. 2008, 2011 rebaja de EE. UU., 2013 taper tantrum, 2020 COVID, 2022 invasión de Ucrania, 2022 Terra y FTX, 2023 SVB, aranceles de 2025) con series de FRED/Yahoo [P]; 3) para cada uno, la lección y en qué se parece o NO se parece a hoy (caso alcista y bajista); 4) enlázalo desde la matriz C03.
Salida: el archivo del cerebro más `informes/research/AAAA-MM-DD-C05-precedentes.md`. No reescribas archivos existentes del cerebro.
Al acabar actualiza el estado de este hueco en `explorador/centro.json` (falta → hecho o parcial).
```
