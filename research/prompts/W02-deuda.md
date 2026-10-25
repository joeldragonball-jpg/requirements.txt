# W02 · Deuda, subastas y calificaciones (martes)

Coste estimado: ~2 % de la cuota semanal · Cuándo: Martes

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea W02: Deuda, subastas y calificaciones (martes).
Lee: `explorador/paneles.json` (bonos y curvas, deuda), `explorador/calificaciones.json`, `research/COLA-DEUDA-BONOS.md` (D01-D06 pendientes) y `informes/research/2026-10-24-D08-subastas-deuda.md`.
Haz: 1) subastas de la semana siguiente (EE. UU. TreasuryDirect API, España tesoro.es, Francia aft.gouv.fr imagen del calendario, Japón mof.go.jp; Italia MEF aún sin localizar) y añade los eventos nuevos al calendario con su fuente; 2) acciones de agencias de calificación: mira el calendario oficial de calificaciones soberanas de la UE y las tablas de la AFT/Tesoro; si alguna decidió (S&P, Moody's, Fitch, DBRS), actualiza `calificaciones.json` con fecha y fuente [P]; 3) rendimientos a 10 años y diferenciales (Francia-Alemania, Italia-Alemania) de los paneles: qué cambió en la semana y por qué solo si hay fuente; 4) UNA tarea de la cola de deuda por semana, en este orden: D03 (curva OAT de Francia), D01 (BTP de Italia), D02 (Bund), D04 (China), D05 (30 años de España e Italia), D06 (bancos).
Salida: `informes/research/AAAA-MM-DD-W02-deuda.md` y actualizar la fila D0x de `research/COLA-DEUDA-BONOS.md`.
```
