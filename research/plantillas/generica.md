# Plantilla genérica (calendario, auditoria, caso-bajista, backtest, actores, glosario, resumen-semanal, sesion-diaria)

Salida: `informes/research/AAAA-MM-DD-<ID>-<tema>.md` (la sesión diaria R00 usa `informes/AAAA-MM-DD-apertura.md` o `-cierre.md`).

Instrucciones por tipo:
- **calendario**: tabla con fecha, evento, activo/tema, fuente primaria y estado (verificado / [VERIFICAR] / [ESPECULACIÓN]); solo fechas futuras (90 días); incluir Fed, BCE, BoJ, PBoC, RBI y reguladores relevantes; ordenada por fecha.
- **auditoria**: elegir 10-15 afirmaciones con cifra o fecha de `cerebro/documentos/` (con Grep), contrastar con fuente primaria, informar errores; no reescribir cerebro/.
- **caso-bajista**: para cada tesis que ya aparezca en los dossiers, argumentos contrarios con datos y fuente; sin recomendaciones.
- **backtest**: contrastar cada entrada de `informes/predicciones.md` con lo ocurrido; puntuar fuente por fuente (acierta / falla / no medible).
- **actores**: ficha por analista, canal o proyecto: quién es, qué cobra o promociona, aciertos y fallos conocidos, fiabilidad.
- **glosario**: término, definición en una frase, fuente primaria, fecha.
- **resumen-semanal**: 1 página imprimible: hechos confirmados, lo no confirmado, 2 cosas a vigilar, fechas de la semana siguiente.
- **sesion-diaria**: seguir "Plantilla de sesión" de CLAUDE.md (máx. 20 min).

Siempre: fuente primaria en su idioma original (traducida por mí), HECHOS separados de OPINIONES, sin recomendaciones de compra/venta, marcar [VERIFICAR] y [ESPECULACIÓN]. Cierre: coste real en `research/COLA.md` y lecciones máx. 5 líneas en los tres archivos de lecciones.
