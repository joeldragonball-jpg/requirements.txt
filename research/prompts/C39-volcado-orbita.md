# C39 · Volcar a la Órbita lo ya investigado que no tiene movimiento (sale de C38)

Coste estimado: ~2 % de la cuota semanal · Sin research nuevo: solo leer informes existentes y añadir movimientos

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P]/[S]/[VERIFICAR]/[ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no commit ni push sin mi «sube». No leas enteros app.py ni apuntes; para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6` y lee solo desde esa línea.

Tarea C39: añadir a explorador/datos.json movimientos fechados que ya están en informes y no en la Órbita (lista de informes/research/2026-10-28-C38-auditoria-cobertura.md, apartado 2).
1. Países: 1-2 movimientos por país con hecho fechado [P] de T07 Corea, T09 Hong Kong, T10 India, T11 Brasil, T12 Rusia, T13 Emiratos, T14 China, T15 BRICS, R04P/W03 Singapur y W03E (Irán, Egipto, Etiopía). Prioridad: India, Singapur y Emiratos (hoy 0 movimientos).
2. Temas: T20 DTCC (estado del lanzamiento de oct-2026, solo si hay hecho [P]), T23 Ripple y Stellar por región, D08 subastas, D09 calificaciones, Gemini D01-D05 (solo lo contrastado, nunca lo [S] sin aviso), norma final de la OCC del 21-oct (EV-occ-genius-norma-final).
3. Cada movimiento con fecha, capa existente, actor, texto (≤ 200 caracteres), estado, fuente con nivel, país y campo «informe». Sin borrar nada. Máximo ~20 movimientos nuevos.
4. Corre `python scripts/revisar_explorador.py` (0 avisos) y comprueba 3 cifras al azar contra su informe.
Informe corto en informes/research/AAAA-MM-DD-C39-volcado-orbita.md (máx. 1 página). Al terminar: fila C39 con coste real, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`; cierra con «¿Actualizo el Seguimiento y el planning?».
```
