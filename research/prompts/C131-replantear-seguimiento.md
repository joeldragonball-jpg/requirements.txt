# C131 · Replantear el Seguimiento (sin IA, tamaño M)

Problema (Joel, 4-nov-2026): el Seguimiento tarda en actualizarse, no se ve bien y no distingue entre «hecho», «hay que repetirlo cada mes/semana», «falló o no pude acceder (Chrome bloqueado)», «parcial» o «error». Cada vez le parece más inútil.

Qué hacer:
1. Lee `research/PLANNING.md`, `scripts/construir_seguimiento.py`, `scripts/tareas_csv.py` y el estado actual de `research/tareas.csv`. No releas informes.
2. Propón (y, si Joel aprueba, implementa) una vista de UNA pantalla con 5 grupos fijos: **Hoy** (3 cosas como máximo), **Periódicas** (semanal/mensual, con fecha de la próxima), **Bloqueadas** (motivo: pide OK, necesita Chrome, fuente cerrada), **Parciales** (qué falta exacto), **Hechas recientes** (últimos 7 días).
3. Añade a `tareas.csv` el campo de periodicidad si hace falta, sin romper el formato de 14 columnas y sin tocar tareas ya cerradas.
4. Medir tiempo: la regeneración (`construir_movil.py` + `construir_seguimiento.py`) debe tardar segundos; si no, di por qué.
5. Alternativa que Joel ha mencionado: dejar el Seguimiento casi muerto y que Claude le recuerde las tareas al abrir sesión (lee solo PLANNING.md). Valora las dos y recomienda una.
No hagas commit ni push.
