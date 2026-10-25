# W08 · Auditoría mensual de coherencia y huecos (última semana del mes)

Coste estimado: ~4 % de la cuota semanal · Cuándo: Última semana del mes

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (BM25 local) y lee solo desde la línea que salga. Webs que dan 403 a curl (EUR-Lex, BIS, SEC, FMI): navegador integrado y `fetch` dentro de la página (PDF con pdf.js); no saltes controles anti-bots. Cifras con símbolo delante y «mil M» (guía `research/GUIA-ESTILO-CIFRAS.md`). Al acabar: coste real en la fila de `research/COLA.md`, ejecuta `python scripts/construir_seguimiento.py` (actualiza la fecha de «último» en el Seguimiento del PC y del móvil) e incluye `docs/movil/seguimiento.json` en el commit, máx. 5 líneas nuevas en cada archivo de lecciones de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas, las 2 cosas a vigilar y 3 líneas de seguridad.

Tarea W08: Auditoría mensual de coherencia y huecos (última semana del mes).
Plantilla: `research/plantillas/auditoria-coherencia.md`. Modelo recomendado: Opus (cambia el modelo en el menú antes de empezar).
Haz: 1) cifras que se contradicen entre `explorador/*.json`, `eventos/calendario.toml`, informes y `cerebro/documentos/`; 2) niveles de evidencia inflados (P sin fuente primaria leída); 3) plazos prometidos por voces o informes sin evento en el calendario; 4) enlaces rotos y celdas del radar sin `url`; 5) huecos medidos (celdas sin dato, capas con pocas voces, temas T/D pendientes) y la diversidad de opiniones; 6) aplica solo las correcciones seguras añadiendo, y deja el resto como lista.
Salida: `informes/research/AAAA-MM-DD-auditoria-coherencia-y-huecos.md` y el estado de cada hallazgo en `research/auditorias-estado.json` (lo lee el Seguimiento). Corre `python scripts/revisar_explorador.py`.
```
