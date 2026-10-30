# C60 · Comparador de países en el móvil y capa de la Órbita

Coste estimado: ~3 % de la cuota semanal · Cuándo: después de C58 y C59, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta ni predicción de resultados, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes; para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Webs que dan 403 a curl: navegador integrado, sin saltar controles anti-bots. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Cifras con símbolo delante y «mil M» (research/GUIA-ESTILO-CIFRAS.md). Al terminar: fila en research/COLA.md con coste real, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea C60: mostrar lo de C58 (`explorador/paises.json`), C59 (`paneles.json` clave «indicadores») y C61 (`explorador/estabilidad.json`) en el móvil y en la Órbita.
1. Móvil: en Agenda o en Mercado (elige dónde cuadra mejor, dilo), tarjeta desplegable «Comparar países» (cerrada) con tabla: país, sistema, gobierno y familia, próxima elección (días que faltan), IPC, paro, deuda/PIB, pobreza; selector UE / potencias; cada celda con fecha o nivel [P]/[S] al tocarla. Una ficha desplegable por país, TODO en una sola página (Joel: no ir de un sitio a otro): política, sistemas públicos, indicadores, estabilidad por dimensión (sanidad, vivienda, infraestructuras, trabajo, educación, seguridad, demografía) con año y fuente de cada cifra, hitos con fecha, la «lectura» del país y enlaces a los informes. Sin puntuaciones propias ni ranking de «mejor/peor».
2. Que quepa en el ancho del móvil (columnas que se pliegan, sin scroll horizontal de página); colores y estilos de las tarjetas existentes (barras como las de liquidez e inflación).
3. Órbita y tablero de datos: la misma información como capa de la Órbita (mapa.html) y como pestaña «Países» del tablero de datos (explorador/paneles.html), con tabla comparable por dimensión y selector UE / potencias; capa «Política y elecciones» con un movimiento por país y por hecho relevante (campo «informe» enlazado); corre `python scripts/revisar_explorador.py`.
4. Frescura: añade a `construir_seguimiento.py` (frescura) los países con datos de más de 90 días o sin fecha.
5. Prueba en el navegador integrado (servidor local en docs/movil), comprueba que la tarjeta se despliega y que no hay errores en consola.
Informe en informes/research/AAAA-MM-DD-C60-comparador.md (máx. 1 página).
```
