# W11 · Política y elecciones (revisión semanal corta)

Coste estimado: ~1 % de la cuota semanal · Cuándo: una vez por semana, mejor tras cada cita electoral

## Pega esto en una sesión nueva

```
Sesión corta (máx. 15 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta ni predicción de resultados, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi «sube» (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Webs que dan 403 a curl: navegador integrado, sin saltar controles anti-bots. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Al acabar: coste real en la fila W11 de `research/COLA.md` y de `research/tareas.csv`, `python scripts/construir_movil.py`, `python scripts/construir_seguimiento.py` y `python scripts/revisar_explorador.py` (0 avisos), y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea W11: Política y elecciones.
Lee: `explorador/elecciones.json` (15 países; el campo «nivel» dice si la fecha es [P] o [S]) y las citas de los próximos 60 días de `eventos/calendario.toml`.
Haz:
1. Citas que han pasado desde la última revisión: anota el resultado oficial (comisión electoral o diario oficial) y cambia «estado» a «pasada».
2. Citas de los próximos 60 días: confirma la fecha en la fuente oficial y sube el nivel de S a P; si cambia, corrige `elecciones.json`, `calendario.toml` y el movimiento de la capa «Política y elecciones» de `explorador/datos.json` (con su campo «informe»).
3. Encuestas: solo de forma neutra y con fuente y fecha ([S]); si la fuente es un organismo público (p. ej. el CIS), di que lo es y que otras casas pueden diferir; nunca como predicción.
4. Un país de la lista con «fecha» vacía (Alemania federal, China): busca la fuente oficial y rellénalo, o deja constancia de que no aplica.
5. Efectos en regulación cripto, deuda o energía: solo como escenario marcado [ESPECULACIÓN].
Máx. 5 líneas nuevas en cualquier archivo de lecciones de `cerebro/documentos/`. Cierra con 5 líneas de resumen, 2 cosas a vigilar y 3 líneas de seguridad.
```
