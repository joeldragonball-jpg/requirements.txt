# V01 · Analizar vídeos que sube Joel y ampliar voces y predicciones

Coste estimado: ~2 % por vídeo · Cuándo: cuando Joel pase la URL de uno o dos vídeos

## Pega esto en una sesión nueva (y añade debajo las URL)

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] / [S] / [RAZONADO] / [ESPECULACIÓN] / [VERIFICAR], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin que yo diga «sube» (enséñame `git status` antes). Antes de leer informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`.

Tarea V01: analiza los vídeos cuyas URL te paso debajo.
1) Transcripción (subtítulos automáticos; navegador integrado si hace falta) y corrige los nombres mal transcritos. Cuidado: los vídeos mezclan hechos, opinión y publicidad.
2) Informe en `informes/videos/AAAA-MM-DD-<canal>-<slug>.md` con el mismo formato que `informes/videos/2026-10-23-despeja-la-x-prediccion-precio-xrp-2027-2030.md`: datos del vídeo (URL, canal, fecha, duración), resumen, tabla de afirmaciones con minuto, etiqueta, fuente y fecha, y contraste alcista/bajista y sesgos (conflicto de interés, patrocinio, hype, titulares sin dato).
3) Cada afirmación de hecho se busca en su fuente original y se marca [P]/[S]/[VERIFICAR]; las citas atribuidas a terceros (CEO, banco central, regulador) se localizan con fecha y URL, o quedan como [VERIFICAR]. Predicciones de precio = [ESPECULACIÓN].
4) Voces: añade en `explorador/voces.json` las voces NUEVAS que salgan (quien, cuando, texto corto, nivel, confianza, fuente con URL, canal y fecha del vídeo); si una voz ya existe, no la dupliques: actualiza su nivel o conf. Predicciones nuevas: filas en `informes/predicciones.md` con fecha límite si la hay. Fuentes originales que salgan por primera vez: añadirlas a `research/fuentes-de-los-videos.md`.
5) Cierre: `python scripts/revisar_explorador.py` en 0 avisos, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, máx. 5 líneas de lecciones por archivo de `cerebro/documentos/` (patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm), resumen de 5 líneas y las 2 cosas a vigilar. Pregúntame: «¿Actualizo el Seguimiento y el planning?».

URL de los vídeos:
- 
```
