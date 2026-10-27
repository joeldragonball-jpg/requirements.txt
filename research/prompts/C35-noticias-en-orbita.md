# C35 · Noticias en la Órbita

Coste estimado: ~2-3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P]/[S]/[VERIFICAR]/[ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes; usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Al terminar: fila en research/COLA.md con coste, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea C35: meter las noticias en la Órbita (explorador/mapa.html + explorador/datos.json).
1. Fuente: las noticias del bot (noticias/ y rama «datos») y las manuales de noticias/manuales/*.json con nota ≥ 7, de las últimas 72 h. Cada una con fecha, fuente, nivel [P]/[S] y enlace.
2. Cada noticia se asigna a una capa existente (Energía y Ormuz, Bancos centrales, Regulación, Liquidez y tipos…) como movimiento con campo «informe» o «noticia». Si el tema no tiene capa (política, elecciones), anótalo para C30.
3. Un script sin IA (scripts/noticias_a_orbita.py) que lo regenere, para engancharlo luego a paneles.yml. Corre `python scripts/revisar_explorador.py`.
4. Prueba a 1920×1080 que no se corta nada y que el Panel no se satura (tope razonable de noticias por capa).
Informe en informes/research/AAAA-MM-DD-C35-noticias-orbita.md (máx. 1 página).
```
