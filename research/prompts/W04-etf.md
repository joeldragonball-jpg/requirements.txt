# W04 · ETF de XRP/XLM, flujos y 13F (cada dos semanas, jueves)

Coste estimado: ~3 % de la cuota semanal · Cuándo: Jueves (quincenal)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea W04: ETF de XRP/XLM, flujos y 13F (cada dos semanas, jueves).
Lee: `informes/research/2026-10-23-T19-etf-xrp-xlm-eeuu.md`, `explorador/datos.json` (capa Fondos, ETF y tesorerías) y los plazos de `eventos/calendario.toml` (13F del 3T el 14-nov, plazo SEC 11-nov).
Haz: 1) AUM por emisor y entradas netas de los ETF de XRP y XLM en EE. UU. con la fuente de cada cifra (SoSoValue/Farside son [S]; los emisores y la SEC EDGAR son [P]) y la diferencia entre fuentes; 2) 13F recientes (EDGAR): quién declara XRP/XLM; 3) Evernorth (XRPN): 8-K, Form 425 y total de XRP (la cifra de 388,9 M aportada frente a la pro forma de 473 M); 4) custodios y avisos de la SEC/OCC relacionados; 5) qué cifras de `datos.json` quedan desactualizadas.
Salida: `informes/research/AAAA-MM-DD-W04-etf.md` y las cifras corregidas en `explorador/datos.json` (con fecha y nivel).
```
