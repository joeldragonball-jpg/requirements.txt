# C28 · Auditoría de la Órbita (Cerebro visual) con los informes nuevos

Coste estimado: ~3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P]/[S]/[VERIFICAR]/[ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, y no hagas commit ni push sin mi OK (enséñame `git status` antes). No leas enteros `app.py` ni apuntes; para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`.

Tarea C28: auditar la Órbita (explorador/mapa.html + explorador/datos.json: 12 capas, 63 movimientos) frente a los informes de informes/research/ hechos desde el 22-oct (T07, T09-T16, T20, T23, T24, D06-D09, W03, W03E, W10, C02, C04, C26 y los nuevos) y mejorarla.
1. Ejecuta `python scripts/revisar_explorador.py` (hoy: 0 avisos) y anota el resultado.
2. Fallos: movimientos con fecha vieja o sin fuente, cifras que no coinciden con su informe (comprueba 5-8 al azar), enlaces «Abrir el informe» rotos, capas con pocos movimientos, texto que se corta en móvil. Los 7 movimientos sin campo «informe» (6 de deuda y 1 de BIS/BlackRock): ¿se les puede enlazar un informe o dejarlos como dato directo?
3. Información que falta: qué hechos importantes de los informes nuevos NO están en la Órbita (países T07-T16, DTCC/T20, deuda D06-D09, valoración C04/C26) y propón, sin añadir aún, una lista de movimientos nuevos con su informe y su nivel [P]/[S].
4. Mejoras de uso: si falta un filtro, una leyenda o una vista; máx. 5 propuestas ordenadas por utilidad.
5. Solo añade o corrige lo claro (nunca borres entradas sin avisarme). Informe en informes/research/AAAA-MM-DD-C28-auditoria-orbita.md (máx. 1 página, apartados: Fallos, Huecos, Mejoras, Hecho). Al terminar: fila en research/COLA.md con coste, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».
```
