# W01 · Tipos de interés (lunes)

Coste estimado: ~2 % de la cuota semanal · Cuándo: Lunes

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea W01: Tipos de interés (lunes).
Lee: `explorador/regulacion.json` (celdas con `tema = politica`), `explorador/paneles.json` (`tipos_vivos`: Fed, BCE, BoE, Brasil, Canadá, leídos solos), `eventos/calendario.toml` y el último R00.
Haz: 1) lista las reuniones de bancos centrales de los próximos 10 días con su fecha oficial; 2) compara `tipos_vivos` con el radar (el panel marca ⚠ si no coincide) y corrige el radar; 3) para los países SIN lectura automática (Corea, Japón, China/LPR, India, Rusia, Hong Kong, Emiratos, Sudáfrica, Indonesia, Singapur) mira si hubo reunión desde el `revisado` de su celda y, si la hubo, lee la nota oficial y actualiza valor, dirección (▲▬▼), fecha y próxima reunión [P]; 4) 3 líneas de lectura: qué dijo cada banco (sesgo), qué cambia en la liquidez. Sin predecir precios.
Fuentes primarias: federalreserve.gov, ecb.europa.eu, boj.or.jp, bok.or.kr, pbc.gov.cn (LPR), rbi.org.in, cbr.ru, hkma.gov.hk, mas.gov.sg, bcb.gov.br (API SGS 432), resbank.co.za, bi.go.id.
Salida: `informes/research/AAAA-MM-DD-W01-tipos.md` (1 página) y celdas `politica` de `explorador/regulacion.json` + eventos nuevos en `eventos/calendario.toml`. Corre `python scripts/revisar_explorador.py` (0 avisos).
```
