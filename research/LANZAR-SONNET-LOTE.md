# Lote de Sonnet: cómo ejecutarlo (12-nov-2026)

Eres el coordinador. Responde en español y sigue CLAUDE.md. Tu trabajo es terminar los bloques A y luego B de `research/BACKLOG-CLASIFICADO.md`. Puedes abrir sesiones nuevas (`start_session`) o agentes (`Agent`) cuando convenga.

## Reglas de coordinación (importantes)
1. **Una sola sesión escribe archivos compartidos a la vez** (`research/tareas.csv`, `explorador/*.json`, `docs/*`, `research/PLANNING.md`). Para evitar choques: los subagentes **investigan y devuelven resultados en texto**; solo tú aplicas los cambios, de uno en uno.
2. Lanza como máximo **3 agentes a la vez**. Sesiones nuevas solo si una tarea es larga y de su propia carpeta (informe nuevo en `informes/research/`); no dos sesiones sobre el mismo JSON.
3. Cada tarea: lee su fila en `research/tareas.csv` (columna prompt) y el prompt indicado; no leas informes ni `app.py` enteros (usa `python scripts/buscar_informes.py "consulta" -n 6`).
4. Fuente y fecha en cada dato; HECHOS separados de OPINIONES; no verificable = [VERIFICAR]; predicción = [ESPECULACIÓN]. **Regla de umbrales** (final de `research/prompts/W05-verificacion.md`): «supera/cae por debajo de X» puede ser intradía; compara mismo día y hora, instrumento y máximo/mínimo antes de poner «desmentido».
5. No llames a la API de Anthropic, no lances workflows, no descargues archivos sin mi OK, no escribas claves, no toques lo existente de `cerebro/`. Si un sitio bloquea scripts, prueba Chrome (`research/ACCESOS-CHROME.md`); si Chrome no está conectado, deja la tarea como bloqueada y sigue.
6. Tras cada tarea: informe en `informes/research/AAAA-MM-DD-<id>-<tema>.md` (máx. 5 líneas de lecciones), fila actualizada en `research/tareas.csv`.
7. Al acabar cada bloque (no cada tarea): `python scripts/construir_movil.py`, `python scripts/construir_seguimiento.py` y `python scripts/construir_orbita.py`.
8. **Presupuesto:** consulta `get_usage` al empezar y cada 3 tareas. Para si la ventana de 5 h pasa del **80 %**, si la semanal pasa del **85 %**, o si tu contexto llega al 75 % (da el relevo con `python scripts/generar_relevo.py --resumen "..."`).
9. **Commit y push solo si digo «sube»**: antes enséñame `git status` agrupado (lo mío / lo de otras sesiones), avisa de claves o archivos sensibles, y commit y push en comandos separados por nombre de archivo. Tras cambiar `docs/movil/`, prueba el móvil en local y sube la versión de caché de `docs/movil/sw.js`.

## Orden
- **Bloque A** (≈14 tareas): C173, C176, C247, C196, C236, C240, C39, C179, C245, C162, C83, C84, C85, C31. Tres agentes en paralelo para las verificaciones de prensa (C173, C176, C247 → agrúpalas por tema: Brent/Ormuz, tipos, Irán) y tú aplicas.
- **Bloque B** (si queda cuota): C58, C59, C61, C30, C42, C68B, C108, C92, C127, C135, C138, C203, C213, C231, C233 en este orden.
- No toques el bloque E (backlog) ni C (Fable).

## Cierre
Pregúntame en una línea «¿Actualizo el Seguimiento y el planning?» y resume en 3 líneas: hecho, pendiente, y qué tareas dejas para Fable o Chrome.
