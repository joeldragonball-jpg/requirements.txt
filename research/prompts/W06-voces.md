# W06 · Voces y predicciones (viernes)

Coste estimado: ~3 % de la cuota semanal · Cuándo: Viernes

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea W06: Voces y predicciones (viernes).
Lee: `informes/predicciones.md` (47 filas), `explorador/voces.json` (44 voces; 6 sin confirmar; 29 de 44 de un solo canal) y la sección Predicciones de `docs/movil/seguimiento.json`.
Haz: 1) predicciones cuya fecha límite cae en los próximos 14 días o ya pasó: compruébalas en la fuente y marca acertó / falló / sin resolver con enlace; 2) las 6 voces «sin confirmar»: busca la cita original y sube o baja su nivel (P/D/S/C/R/E) con su motivo; 3) añade 3-5 voces NUEVAS de fuentes distintas a las ya usadas (escépticos, analistas de ETF, bancos centrales críticos, agencias de calificación, reguladores) con cita localizada, fecha y URL; 4) anota qué predicciones nuevas dijeron los vídeos de la semana.
Salida: `informes/predicciones.md` (filas nuevas y resultados), `explorador/voces.json` y `python scripts/revisar_explorador.py` en 0 avisos.
```
