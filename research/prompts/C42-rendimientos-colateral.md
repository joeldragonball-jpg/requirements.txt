# C42 · Rendimientos y colateral: qué existe, dónde está regulado y qué riesgo tiene (sale de C41A)

Coste estimado: ~3 % de la cuota semanal · Research nuevo con fuentes primarias · Mejor DESPUÉS de C41C (que decide el formato del panel)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min; si no cabe, para tras un bloque y dame relevo). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P]/[S]/[VERIFICAR]/[ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente (las plataformas que ofrecen rendimiento son parte interesada), nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no commit ni push sin mi «sube». Para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` (R43 DEX/AMM, R44 custodia, W04 flujos).

Tarea C42: rellenar con hechos el panel propuesto en informes/maquetas/C41A-rendimientos-colateral.html (formato final según C41C).
1. Modalidades: staking nativo (y si XRP/XLM tienen o no staking de protocolo), productos «earn» de exchanges, lending CeFi, lending DeFi, AMM de XRPL y Stellar, préstamos con garantía cripto (bancos y brókers), colateral tokenizado (fondos monetarios y repos) y letras del Tesoro tokenizadas.
2. Por modalidad y jurisdicción (EE. UU., UE/MiCA, Reino Unido, Singapur, Hong Kong, Japón, Corea, Emiratos): estado legal con norma y fecha [P], quién supervisa, ejemplos de producto (solo como hecho, nunca como sugerencia), tasa o ratio con fecha si es pública, y riesgo principal.
3. Sin decir dónde operar ni qué contratar. Las tasas son datos puntuales con fecha.
4. Propón las filas en formato JSON (campos: modalidad, activo, jurisdiccion, estado, norma, fecha, fuente, url, nivel, riesgo, revisar) en el informe; NO crees el panel sin mi OK.
Informe en informes/research/AAAA-MM-DD-C42-rendimientos-colateral.md (máx. 2 páginas). Al terminar: fila C42 con coste real, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`; cierra con «¿Actualizo el Seguimiento y el planning?».
```
