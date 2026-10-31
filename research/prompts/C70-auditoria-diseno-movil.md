# C70 · Auditoría de diseño de la app móvil (Seguimiento) y boceto «cómo quedaría»

Mismo trabajo que se hizo con el Explorador del ordenador (30-oct: jerarquía visual, colores, barras, tablas fusionadas, lo importante arriba), ahora con la app móvil `docs/movil/` (`index.html` ~100 KB, `data.json`, `seguimiento.json`). Joel se queja de pantallas con todo del mismo tamaño y color.

## Qué hacer
1. **Mapa de la app (sin leer index.html entero):** `Grep` por `<section`, `id="` y las funciones de pintado; lista las pantallas (Seguimiento, Agenda, Comparar países, Todo el plan, etc.) y qué datos muestra cada una. Mira antes `graphify-out/GRAPH_REPORT.md` si existe.
2. **Capturas de la app actual:** `preview_start` (si hay config en `.claude/launch.json`; si no, abre `docs/movil/index.html` en el navegador integrado) a 375×812; una captura por pantalla; apunta lo que falla: jerarquía, densidad, tamaño de tap, contraste, scroll infinito, lo importante escondido.
3. **Ejemplos de referencia (4-6):** busca con el navegador integrado cómo resuelven lo mismo apps de seguimiento o de inversión en móvil (por ejemplo, listas de tareas con estado tipo Linear o Things, paneles de cartera tipo Yahoo Finance o Trading 212, agendas de calendario económico). Por cada ejemplo: URL, qué patrón copiarías (tarjeta de resumen arriba, chips de estado, barra de progreso, agrupación plegable, semáforo) y por qué. Sin copiar marca, textos ni imágenes: solo patrones.
4. **Propuesta:** por pantalla, 3-5 cambios concretos ordenados por impacto, y qué información extra cabría sin recargar (p. ej. racha, próximas 3 fechas, % del plan hecho, cuota usada). Separa HECHOS de la app actual de OPINIONES de diseño.
5. **Boceto «cómo quedaría»:** UN archivo HTML autocontenido `docs/movil-prueba/index.html` (o `informes/research/C70-boceto-movil.html`) con la pantalla principal y 1-2 pantallas más, leyendo los datos reales de `data.json` y `seguimiento.json`; misma información que hoy y, si cabe, un poco más. Comprobar a 375 px de ancho y en oscuro. NO modificar `docs/movil/index.html` ni `sw.js` hasta que Joel diga que sí.
6. Informe `informes/research/AAAA-MM-DD-C70-diseno-movil.md` con: tabla «problema → cambio propuesto», ejemplos con URL, capturas citadas, y qué falta.

## Reglas
- iOS: no tocar el arreglo de la banda inferior (`viewport-fit=cover`, memoria `ios-pantalla-completa-pwa`).
- Sin claves, sin workflows, sin API de Anthropic. Sin commit hasta que Joel diga «sube».
- Hasta aprobación, todo va en archivos nuevos; no reescribir lo existente.
- Parar al 70 % de contexto y dar relevo.
