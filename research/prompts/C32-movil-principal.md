# C32 · Móvil: pantalla principal de precios, tipos, petróleo e inflación + auditoría de los paneles

Coste estimado: ~3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa) / [VERIFICAR] / [ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes; para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Webs que dan 403 a curl: navegador integrado, sin saltar controles anti-bots. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Al terminar: fila en research/COLA.md con coste, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea C32: que el móvil sea el índice y la visualización primaria.
1. «Hoy»/«Mercado»: arriba, una fila compacta con lo que más importa (precios de tus valores, tipos oficiales, Brent, inflación; con flecha y fecha), y debajo todo en desplegables cerrados que desglosan (valoración, deuda, liquidez, defensa, elecciones, hitos de petróleo).
2. Auditoría de los paneles actuales: cifras que no cuadran con su informe, fechas viejas, textos largos que se cortan a 375 px, paneles que nadie usa. Lista corta de mejoras (máx. 6) ordenada por utilidad y aplica las claras.
3. Prueba a 375 px con el navegador integrado (sin scroll horizontal) y sube la versión de caché de docs/movil/sw.js.
Informe en informes/research/AAAA-MM-DD-C32-movil-principal.md (máx. 1 página).
```
