# C109 · Mapa de cobertura temática y plan de automatización de la terminal

Modelo: Sonnet · esfuerzo alto · ~6 % semanal · sesión NUEVA. Sin API de Anthropic, sin workflows lanzados. Lee `CLAUDE.md`, `graphify-out/GRAPH_REPORT.md`, `research/PLANNING.md`, `research/CATALOGO-FUENTES.md` y los §6-§7 de `informes/research/2026-11-03-C98-auditoria-opus.md`. No leas enteros `app.py` ni `cerebro/apuntes_*.md`.

## Por qué existe
Joel quiere que la terminal de inteligencia personal sea un panel de control de TODO, con la mayor automatización posible y sin tocarlo él. Las auditorías C81B/C98 miraron seguridad, cruces y medición, pero NO ampliaron los temas. Esta tarea lo hace.

## Dos niveles que Joel pidió
- **Nivel A, grandes países (superficial y automático):** los mismos 10-15 indicadores por país desde institutos de estadística y organismos (Banco Mundial, FMI, OCDE, Eurostat, BIS, oficinas nacionales): PIB, inflación, paro, deuda, tipos, balanza, población, demografía, desigualdad, gasto en defensa, energía.
- **Nivel B, España (profundo):** pagos públicos, inversión pública y contratos (PLACSP, BDNS, IGAE, Intervención), catástrofes y emergencias, accidentes de tráfico (DGT), defunciones (INE, MoMo), delitos y criminalidad (Balance de Criminalidad del Ministerio del Interior), siniestralidad laboral, incendios, sanidad, vivienda. Ya existen: DANA (informe H), inmigración (G), recaudación vs infraestructuras (I), opacidad (J), comparativa K, hipotecas y vivienda.

## Qué entregar (`informes/research/AAAA-MM-DD-C109-mapa-cobertura.md`, máx. ~6 páginas)
1. **Matriz de cobertura**: tema × nivel (A/B) × estado hoy (ya en paneles / informe suelto / nada). Marca solo lo que compruebes en `explorador/paneles.json`, `explorador/*.json` e `informes/`.
2. **Para cada tema nuevo**: fuente oficial exacta, formato (API / CSV / XLS / PDF / solo Chrome / bloqueada), cadencia real de publicación, si requiere clave o descarga con OK de Joel, y si se puede automatizar SIN IA en `actualizar_paneles.py` o un script hermano. Prueba con curl y User-Agent identificado; no saltes anti-bots.
3. **Plan de automatización**: qué ya corre solo, qué podría correr solo (con coste cero) y qué seguirá siendo manual. Un solo punto de entrada: reutilizar `paneles.yml` y el Worker, sin workflows ni capas nuevas.
4. **Lista priorizada de tareas** (valor / coste / riesgo) lista para `research/tareas.csv`, con prompt de una línea, de modo que Joel pueda dejar a Claude en modo autónomo y solo aprobar lo marcado como «manual».
5. **Qué tiene que hacer Joel a mano** (OK de descargas, claves gratuitas como el `appId` de e-Stat): lista corta y concreta.
6. **Sesgos y límites**: datos de delitos y muertes tienen definiciones distintas por país y retrasos; no los compares sin nota. Sin recomendaciones de inversión. Separa HECHO / OPINIÓN, marca [VERIFICAR] y [ESPECULACIÓN].

## Cierre
`python scripts/indice_investigacion.py`, `python scripts/construir_movil.py`, `python scripts/construir_seguimiento.py`. Comprueba que el informe sale en el índice del cerebro. Marca C109 hecha en `research/tareas.csv` con el coste real. Sin commit ni push salvo «sube». Cierra con 5 líneas y «¿Actualizo el Seguimiento y el planning?».
