# W07 · Research de fuentes (mensual, 1.ª semana)

Coste estimado: ~3 % de la cuota semanal · Cuándo: 1.ª semana del mes

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea W07: Research de fuentes (mensual, 1.ª semana).
Objetivo: que la información de entrada sea mejor y más automática.
Haz: 1) comprueba enlaces de `explorador/voces.json`, `eventos/calendario.toml` y `explorador/regulacion.json` (404/403/redirecciones) y repara los que se puedan con una fuente primaria equivalente; 2) lista por tema qué fuentes primarias faltan (p. ej. BIS data portal, ECB Data Portal, Eurostat, FMI DataMapper, Banco Mundial, SEC EDGAR y Federal Register APIs, EUR-Lex, CFTC, bancos centrales con API abierta) y prueba cuáles se pueden leer SIN navegador (curl/urllib) para convertirlas en datos automáticos del workflow `paneles.yml`; 3) evalúa 2-3 fuentes nuevas de opinión o datos (consulta, formato, coste, sesgo); 4) propón candidatos a bot nuevo sin IA con su esfuerzo; 5) actualiza `cerebro/documentos/fuentes-fiables-y-dudosas.md` (≤ 5 líneas) y `research/MAPA-DE-FUENTES.md` (tabla fuente → qué datos → cómo se lee → estado).
Salida: `informes/research/AAAA-MM-DD-W07-fuentes.md` con una tabla de decisiones (hacer / descartar).
```
