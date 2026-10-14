---
description: Ejecuta varias tareas de research seguidas (ej. /research-lote grandes, /research-lote regiones, /research-lote R01P R08P). Para si se acerca al tope de cuota.
argument-hint: "[grandes | regiones | lista de IDs]"
---

Argumento recibido: $ARGUMENTS

Responde siempre en español y sigue las reglas de CLAUDE.md. Trabaja en serie, sin subagentes en paralelo.

1. Lee `research/COLA.md` (sección "Lotes predefinidos" y la fila de cada tarea). Si el argumento es `grandes` o `regiones`, usa la lista de ese lote; si son IDs, úsalos en ese orden. Sin argumento: muestra los lotes y pregunta cuál.
2. Antes de empezar, llama a `get_usage` (mcp__ccd_session_mgmt__get_usage; cárgala con ToolSearch si hace falta). Anota el % semanal y el de 5 horas. Muestra el plan: lista de tareas y estimación, y espera mi confirmación solo si el lote entero estima pasar del 85 % semanal.
3. Para cada ID, en orden:
   a. Ejecuta la tarea como lo haría `/research <ID>` (plantilla de la fila; si el ID acaba en P, usa el "Modo PROFUNDO" de `research/plantillas/dossier-region.md`). Si el ID es R12P/R11P u otro sin plantilla propia, usa `verificacion.md` o `generica.md` según la cola.
   b. Guarda el informe en `informes/research/` (nunca en `cerebro/`), con el nombre de la plantilla.
   c. Llama a `get_usage` y anota en la columna "Real" de `research/COLA.md` el coste de esa tarea (diferencia de % semanal; si el medidor no se mueve, "<1 %") y pon el estado "hecho AAAA-MM-DD".
   d. Lecciones: como máximo 5 líneas nuevas por archivo en los tres archivos de lecciones, sin repetir.
   e. Antes de pasar a la siguiente, **para el lote** si: el semanal ≥ 90 %, o la ventana de 5 horas ≥ 85 %, o una fuente pide algo fuera de la carpeta o de `privado/`. En ese caso, di qué quedó pendiente y cuándo se reinicia la ventana.
4. No uses `git commit` ni `git push`. No lances workflows de GitHub ni nada que llame a la API de Anthropic. No toques `privado/`. No intentes saltar captchas ni accesos bloqueados: anota el intento y sigue.
5. Para no inflar el contexto, no releas informes ya escritos; apóyate en la cola y en los archivos.
6. Al terminar: resumen de 5 líneas (tareas hechas, coste total medido, % semanal restante), las 2 cosas a vigilar y los huecos que requieren PDFs que debe descargar Joel (ponlos en una lista con la URL y el nombre de archivo sugerido para `research/fuentes/`).
