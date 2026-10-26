# C15 · Manual de mantenimiento y paquete de continuidad sin Claude

Coste estimado: ~2 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C15: Manual de mantenimiento y paquete de continuidad sin Claude.
Haz: 1) escribe `MANTENIMIENTO.md` en la raíz (sin claves ni secretos): qué corre solo (workflows de `.github/workflows/`, el Worker de Cloudflare `lanzador-bots` y las dos apps), qué cuesta cada cosa (cuáles llaman a la API de Anthropic y cuáles no), qué caduca y cuándo (token de GitHub del Worker: 1 año), cómo lanzar cada rutina a mano, cómo comprobar que todo va (Seguimiento, `research/PLANNING.md`, Sistema), y qué hacer si un bot falla; 2) crea `research/gemini/` con un prompt AUTOCONTENIDO por rutina (W01 tipos, W02 deuda, W03 países, W05 verificación, W06 voces, W10 energía y los EV) para pegar en Gemini Deep Research, sin rutas ni herramientas de Claude, con las reglas de fuentes ([P]/[S]/[VERIFICAR]), el formato de salida y cómo volcar el resultado al repo; 3) añade una sección «Si ya no hay Claude»: qué se sigue actualizando solo (paneles, bots sin IA, alertas) y qué queda manual.
Salida: `MANTENIMIENTO.md`, `research/gemini/*.md` e informe corto. No hagas commit.
Al acabar: fila C15 de `research/COLA.md` con el coste real (get_usage antes y después), `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`.
```
