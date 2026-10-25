# C01 · Gasto en defensa (% del PIB)

Coste estimado: ~1,5 % de la cuota semanal · Cuándo: hueco del Centro; sin día fijo (lanzar solo si el semanal está por debajo del 70 %)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C01: Gasto en defensa (% del PIB).
Fuentes: Banco Mundial (MS.MIL.XPND.GD.ZS, API abierta) y, para contraste, SIPRI y la OTAN.
Haz: 1) con la API del Banco Mundial (curl con User-Agent propio) obtén el último dato disponible y la serie de 10 años de EE. UU., China, Rusia, India, Alemania, Francia, Reino Unido, España, Polonia, Japón, Corea del Sur, Israel, Arabia Saudí, Turquía y Ucrania; 2) contrasta 3-4 países con SIPRI o la OTAN [P] y anota diferencias de definición; 3) caso alcista y bajista para los sectores de defensa sin recomendar nada; 4) propón cómo automatizarlo en `scripts/actualizar_paneles.py` (sin IA).
Salida: `informes/research/AAAA-MM-DD-C01-defensa.md` con tabla (país, % PIB, año del dato, fuente, nivel [P]/[S]).
Al acabar actualiza el estado de este hueco en `explorador/centro.json` (falta → hecho o parcial).
```
