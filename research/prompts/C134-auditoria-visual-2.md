# C134 · Auditoría visual del tablero, 2.ª pasada (para Opus)

Modelo recomendado: Opus. Estimación ~3 % semanal. Solo presentación y textos en `explorador/vistas.html`; no toques datos ni fuentes.

## Contexto
C129 (5-nov-2026) encontró que Chrome tenía la Órbita al 80 % de zoom, añadió el control «Letra» (A−/A+), puso un mínimo de 13 px en las 10 pestañas, pasó la cabecera de España a tarjetas de color y plegó las explicaciones largas con `corto()`. Lee SOLO la sección «Para la siguiente pasada» de `informes/research/2026-11-05-C129-auditoria-visual.md`.

## Qué hacer
1. Abre la Órbita con Claude in Chrome (`http://localhost:8793`; el navegador integrado no abre localhost). La vista está en el iframe titulado «Vistas de la Órbita»; cambia de pestaña con `ir('id')` desde `javascript_tool`.
2. Prioridad: Paneles (Bonos 9 × 12 → curva con tabla plegada; columna «Nota» al tooltip en tablas de más de 6 columnas), Capas («Próximas fechas» y «Hechos recientes» como tarjetas `.ev`), Países (unificar la coma decimal en `cortaUnid`), Presupuesto (3 cifras arriba en cada ministerio abierto y las tablas plegadas; «Programas concretos» plegado).
3. Mide antes y después: celdas de 3+ líneas y letra mínima (`getComputedStyle`). `node --check` del JS extraído tras cada bloque de cambios.
4. Informe: `informes/research/AAAA-MM-DD-C134-auditoria-visual-2.md` con el antes y el después y 2-3 mejoras por pestaña para la pasada siguiente.

## Reglas
Español. Sin dependencias nuevas. No toques `cerebro/`, `privado/` ni claves. No hagas commit ni push; enseña `git status`.
