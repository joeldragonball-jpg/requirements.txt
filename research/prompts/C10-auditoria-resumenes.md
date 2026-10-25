# C10 · Auditoría cruzada de cifras de los resúmenes semanales del bot (W41-W43) con series primarias

Coste estimado: ~3 % de la cuota semanal · Cuándo: jueves tras el reinicio del martes (junto a W05) o semana de ahorro solo si el semanal está por debajo del 70 %

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea C10: Auditoría de cifras de `cerebro/actualidad/2026-W41.md`, `2026-W42.md` y `2026-W43.md`.
Haz: 1) extrae todas las cifras con número (precios, rendimientos, tipos, flujos, porcentajes) de cada resumen; 2) contrástalas con series primarias abiertas: Tesoro de EE. UU. (CSV daily_treasury_yield_curve), FRED, BCE, EIA, IMF PortWatch, CoinGecko y nodo del XRPL, `docs/movil/data.json`; 3) marca cada una: coincide / no coincide / sin plazo o sin fuente / no verificable; 4) detecta mezclas de series (spot y futuro, 10 y 30 años, países) y titulares tratados como hechos; 5) propón una regla automática sin IA para el bot de resúmenes (por ejemplo exigir plazo y fecha a cada cifra de rendimiento).
Contexto ya encontrado: el «Treasury al 5,34 %» de W43 es casi seguro el 30 años (5,33 % el 23-oct), y Bloomberg «flujos cerca de prebélicos» no concilia con PortWatch.
Salida: `informes/research/AAAA-MM-DD-C10-auditoria-resumenes.md` con una tabla (resumen, cifra, serie primaria, veredicto).
Al acabar actualiza la fila C10 de `research/COLA.md`.
```
