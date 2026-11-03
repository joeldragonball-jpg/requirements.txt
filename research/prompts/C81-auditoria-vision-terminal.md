# C81 · Auditoría de visión: terminal de inteligencia personal + cerebro de seguimiento

Modelo: Opus (síntesis) · esfuerzo alto · ~8-10 % semanal · sin API de Anthropic, sin workflows. Sesión nueva; leer `graphify-out/GRAPH_REPORT.md` y `research/PLANNING.md`, nunca `app.py` ni `apuntes_*.md` enteros (usa Grep y `scripts/buscar_informes.py`).

## Contexto (decidido por Joel el 3-nov-2026)
- Dos apps: **cerebro de seguimiento** (móvil, `docs/movil/`) y **terminal de inteligencia personal** (escritorio, `app.py`, pestaña Cerebro).
- Uso principal: Joel y su familia. Posible rentabilidad futura (estabilidad), sin difusión masiva. Sin decidir si saldrá como app o web.
- Preocupación principal: seguridad al abrirlo (disponibilidad, ataques, fugas). El repo hoy es PÚBLICO. La tesis de Joel es privada (`privado/`); no la escribas en el repo.
- Sin recomendaciones de compra/venta. Hecho vs opinión; fuente y fecha; [VERIFICAR] / [ESPECULACIÓN].

## Qué hay que entregar (un informe en `informes/research/AAAA-MM-DD-C81-auditoria-vision.md`, máx. ~6 páginas)
1. **Inventario real**: datos (`explorador/`, `cerebro/`, `research/`, `informes/`), paneles, bots/workflows, y qué llega a cada app. Tabla: dato → fuente → frecuencia → ¿lo ve el móvil? ¿lo ve la terminal?
2. **Huecos entre lo investigado y lo mostrado** en la terminal (ejemplo ya detectado: `research/fuentes-nuevas/` no estaba en el índice del cerebro).
3. **Cruces que faltan**: país ↔ evento ↔ activo ↔ tesis. Propón el modelo mínimo (ids comunes, no capas nuevas; ver memoria «una sola página, sin capas nuevas»).
4. **Medición**: aciertos de fuentes, predicciones y hipótesis; qué falta para puntuarlas.
5. **Calidad**: contradicciones, cifras viejas, fuentes secundarias que deberían ser primarias, [VERIFICAR] antiguos.
6. **Seguridad y salida a producción**: revisa la lista de 20 puntos de Joel (memoria `reglas-seguridad-codigo`); riesgos de repo público, secretos, bots con API de pago, Worker de Cloudflare, caídas/DoS, autenticación si se abre a terceros; comparar app vs web (PWA) con pros/contras. Si se monetiza: señalar el riesgo regulatorio de difundir información financiera como [VERIFICAR] con asesor, sin dar consejo legal.
7. **Hoja de ruta**: lista priorizada (valor / coste / riesgo) de mejoras y research profundo a lanzar, cada una como fila lista para `research/tareas.csv` con su prompt.

## Cierre
`python scripts/indice_investigacion.py`, `python scripts/construir_movil.py`, `python scripts/construir_seguimiento.py`. Comprobar que el informe sale en el índice del cerebro. Fila C81 → hecha con coste real. Sin commit ni push salvo «sube». Cierra preguntando: «¿Actualizo el Seguimiento y el planning?».
