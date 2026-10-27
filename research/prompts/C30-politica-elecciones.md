# C30 · Política y elecciones por país

Coste estimado: ~3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa) / [VERIFICAR] / [ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes; para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Webs que dan 403 a curl: navegador integrado, sin saltar controles anti-bots. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Al terminar: fila en research/COLA.md con coste, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea C30: nuevo apartado «Política y elecciones» para controlar el calendario electoral y su peso en mercados.
1. Países: EE. UU. (mitad de mandato 3-nov-2026 y lo que viene), Alemania, Francia, Italia, España, Reino Unido, Países Bajos y el resto de la UE que mueva mercado; Japón, China, Corea del Sur, India; Brasil, México, Canadá, Argentina. Por país: próxima cita electoral (fecha oficial [P]), qué se vota, encuestas de forma neutra ([S]), y qué cambiaría en regulación cripto, deuda o energía si gana cada bloque.
2. Datos: explorador/elecciones.json (país, fecha, tipo, fuente, nivel, efecto posible) y eventos/calendario.toml (solo fechas nuevas, sin duplicar).
3. Móvil: en Agenda, desplegable «Elecciones próximas» (cerrado) ordenado por fecha; en la Órbita, capa «Política y elecciones» con sus movimientos enlazados.
4. Rutina: propón una fila W (revisión semanal corta) o añádela a W06 y a eventos/vinculos.json.
Informe en informes/research/AAAA-MM-DD-C30-politica-elecciones.md (máx. 1 página). Sin predicciones de resultado: solo calendario, hechos y escenarios marcados [ESPECULACIÓN].
```
