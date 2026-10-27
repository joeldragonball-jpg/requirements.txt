# C31 · Inflación (IPC) por país

Coste estimado: ~3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa) / [VERIFICAR] / [ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes; para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Webs que dan 403 a curl: navegador integrado, sin saltar controles anti-bots. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Al terminar: fila en research/COLA.md con coste, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea C31: panel de inflación con datos oficiales.
1. EE. UU. (BLS/FRED: CPIAUCSL y PCE), zona euro (Eurostat HICP), España (INE), Reino Unido (ONS), Japón (MIC), China (NBS), Brasil (IBGE) y Canadá (StatCan) si hay API abierta. Interanual y último mes, con fecha del dato y próxima publicación.
2. Añade la descarga a scripts/actualizar_paneles.py como una función más (si una fuente falla se conserva el dato anterior), salida en explorador/paneles.json (clave «inflacion»), y las fechas de publicación a eventos/calendario.toml.
3. Móvil: tarjeta en Mercado junto a tipos y petróleo, con barras como las de liquidez; detalle por país en desplegable cerrado. Ojo con periodos mezclados y revisiones.
4. Órbita: capa «Liquidez y tipos oficiales» o nueva «Inflación» con los últimos movimientos enlazados.
Informe en informes/research/AAAA-MM-DD-C31-inflacion.md (máx. 1 página); 3-5 cifras contrastadas con la nota de prensa oficial.
```
