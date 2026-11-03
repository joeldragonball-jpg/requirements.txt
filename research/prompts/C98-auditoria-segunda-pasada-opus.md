# C98 · Segunda pasada de la auditoría de visión (Opus, esfuerzo alto)

Modelo: Opus · esfuerzo alto · ~8-10 % semanal · sesión NUEVA. Sin API de Anthropic, sin workflows. Lee `CLAUDE.md`, `graphify-out/GRAPH_REPORT.md` y `research/PLANNING.md`. No leas enteros `app.py` ni `cerebro/apuntes_*.md` (Grep y `python scripts/buscar_informes.py "consulta" -n 6`).

## Punto de partida
La primera pasada (Sonnet, medio) está en `informes/research/2026-11-03-C81-auditoria-vision.md`. Léela entera y NO la repitas: critícala, verifica sus afirmaciones y profundiza. Nombres fijos: **cerebro de seguimiento** (móvil, `docs/movil/`) y **terminal de inteligencia personal** (escritorio, `app.py`). Visión de Joel: uso familiar, posible rentabilidad futura, mucha preocupación por la seguridad, duda app vs web; repo hoy PÚBLICO; la tesis es privada (`privado/`), no la escribas en el repo.

## Qué hacer (entrega: `informes/research/AAAA-MM-DD-C98-auditoria-opus.md`, máx. ~8 páginas)
1. **Verificar la primera pasada**: comprueba 10 afirmaciones suyas con evidencia (archivo:línea o comando). Marca cada una confirmada / corregida / no verificable.
2. **Seguridad a fondo (prioridad)**: `app.py` (`candado()`, `?k=`, `MOSTRAR_CEREBRO`), `docs/movil/index.html` (XSS por texto externo inyectado como HTML), Worker de Cloudflare (`scripts/cloudflare-lanzador-bots.js`), workflows y secretos, historial de git (secretos en commits), datos privados que ya estén en el repo público. Cada hallazgo: gravedad, evidencia, arreglo concreto. No expongas ni copies ningún secreto.
3. **Arquitectura de salida (app vs web)**: compara PWA en hosting estático con acceso protegido, repo privado + espejo público mínimo, y app Streamlit desplegada con auth. Coste, riesgo, esfuerzo, cómo se tumba cada una (DoS, abuso de la API de pago, fuga de datos).
4. **Modelo de cruces** `país ↔ evento ↔ activo ↔ voz ↔ predicción`: esquema mínimo (ids comunes, `enlaces.json`, la tesis solo vía referencia a `privado/`), con un ejemplo real hecho a mano de 3 casos (p. ej. Brasil, petróleo/Ormuz, CLARITY).
5. **Medición**: qué falta para puntuar fuentes y predicciones sin inventar porcentajes (n mínimo, fechas límite, criterios de acierto).
6. **Research profundo a lanzar**: lista priorizada (valor/coste/riesgo) de 8-12 tareas nuevas con prompt de una línea; no dupliques C86-C97 (ya en `research/tareas.csv`): reordénalas y di cuáles sobran o faltan.
7. **Visión a gran escala**: qué haría falta para que sea de verdad una terminal de inteligencia (y qué NO merece la pena construir). Separa HECHO / OPINIÓN, marca [VERIFICAR] y [ESPECULACIÓN]. Si se monetiza, riesgo regulatorio como [VERIFICAR] con asesor; sin consejo legal ni de inversión.

## Cierre
`python scripts/indice_investigacion.py`, `python scripts/construir_movil.py`, `python scripts/construir_seguimiento.py`. Comprueba que el informe sale en `cerebro/documentos/indice-investigacion.md`. Marca C98 hecha en `research/tareas.csv` con el coste real (get_usage). Sin commit ni push salvo «sube». Cierra con 5 líneas y «¿Actualizo el Seguimiento y el planning?».
