# W08 · Auditoría mensual de coherencia y huecos (25-nov-2026)

Alcance: muestreo con scripts sobre `explorador/regulacion.json`, `explorador/voces.json`, `eventos/calendario.toml` y las tareas vigiladas de `research/tareas.csv`. Ejecución desatendida (rutina W03→W08 por ser el último miércoles del mes). No es una revisión línea a línea. `python scripts/revisar_explorador.py`: **0 avisos** en 13 capas y 440 movimientos.

## Resumen
Sin contradicciones nuevas de cifras en lo muestreado. Los hallazgos del 2-nov que seguían abiertos se han reducido: A1 está resuelto. Quedan abiertos el nivel de evidencia de HK ETF, 8 celdas sin `url`, la falta de diversidad de canales de opinión y los huecos del radar (63 de 192 celdas sin etapa).

## Estado de los hallazgos del 2-nov
| Id | Estado hoy | Detalle |
|---|---|---|
| A1 | **Cerrado** | v002 (DTCC) ya figura `cumplido` (nota del 28-oct [P]); v062 (Binance) `cumplido` en parte, con fuente [S]. |
| A2 | Abierto | HK ETF: nivel P, sin `url`; el texto dice 11 ETF al contado con US$451 M (jun-2026). |
| A3 | Parcial | De 192 celdas con etapa, **8 sin `url`** (antes 9): UE ETF (S), HK ETF (P), KR fiscal (S), ID stablecoins/ley marco/tokenización (S), EG CBDC (S), ES CBDC (V). |
| A4 | Abierto | v036 sigue sin url (nivel R). Hay además v171 y v220 sin url. |
| A5 | **Abierto, peor** | De 244 voces, 188 vienen del mismo canal («Despeja La X»), 53 no son vídeo y 3 son research. Sin segunda fuente de vídeo. |
| A7 | Abierto | 63 de 192 celdas sin etapa. Por jurisdicción: China 7, Egipto 7, Etiopía 7, India 4, Irán 4, BRICS 3, Canadá 3, Argentina 3, El Salvador 3, EE. UU. 2, Singapur 2, Corea 2. |
| A8 | Cerrado en la práctica | v062 ya resuelto. Los plazos de 2030/2031 son [ESPECULACIÓN] y no necesitan evento. |

## Hallazgos nuevos
| Id | Gravedad | Hallazgo | Acción propuesta |
|---|---|---|---|
| B1 | Media | **Dos enlaces 404 nuevos** (`comprobar_enlaces.py`, 25-nov): (a) Al Jazeera, voz v200 (Thune, 11-nov) en `voces.json`; (b) `argentina.gob.ar/normativa/recurso/219405/...` en la celda AR custodia (nivel P) de `regulacion.json`. La celda AR es P, así que la fuente primaria debe localizarse de nuevo. | Buscar la URL vigente (InfoLEG / CNV); si no se lee, bajar a [VERIFICAR]. No se ha tocado: ambos archivos los editan otras rutinas. |
| B2 | Media | **HK ETF [P]**: una búsqueda de hoy en sfc.hk no devolvió la lista oficial de ETF al contado. El informe anual 2025-26 de la SFC (`sfc.hk/-/media/EN/files/COM/Annual-Report/2025-26/06_Year-in-Review_EN.pdf`) habla de 11 ETF al contado y una capitalización de «$4.3 billion» (moneda sin comprobar, probablemente HK$). La cifra de la celda (US$451 M) no se ha podido contrastar con esa fuente. | Leer el PDF en el navegador, fijar moneda y fecha, y añadir `url`; si no cuadra, bajar a S. [VERIFICAR] |
| B3 | Baja | 73 eventos del calendario con fecha pasada y sin campo de estado (el esquema no lo tiene): no son un error, pero el calendario no distingue «cumplido» de «sin revisar». | Decidir si se añade campo `estado`; hoy lo cubre `informes/predicciones.md`. |
| B4 | Baja | Celda EG CBDC (S): el «E-Pound» podría referirse a Marruecos (única fuente L'Economiste), ya marcado [VERIFICAR] en el propio JSON. | Mantener [VERIFICAR] o vaciar la celda. |

## Plazos de `voces.json`
15 plazos `pendiente`, 5 `cumplido`, 1 `retrasado`. Ninguno pendiente ha vencido a 25-nov. Próximos: v003 (DTCC–Chainlink, 2026-12), v014 (Swift, 2026-12), v041 (JPMorgan Kinexys, 2026-12), todos «sin comprobar» desde el 23-oct: conviene revisarlos en W05 de diciembre.

## Tareas vigiladas (regla del 21-nov)
Revisadas C61, C230, C245, C267, C275 y C331 (huecos sin fuente oficial). No se ha buscado una fuente nueva en esta pasada corta; **ninguna se ha rellenado ni cerrado** (nunca con nivel S). Nueva fecha de revisión: **2026-12-25** (+30 días) en `research/tareas.csv`. C261 y C340 tienen fecha 26-nov y las revisa W05.

## Correcciones aplicadas (solo seguras)
1. `research/tareas.csv`: fecha de revisión de 6 filas vigiladas → 2026-12-25.
2. `research/auditorias-estado.json`: entrada de esta auditoría.
No se tocaron `voces.json`, `regulacion.json` ni `cerebro/`.

## Dos cosas a vigilar
1. B1: la celda AR custodia es P con enlace roto.
2. A5: 188 de 244 voces dependen de un solo canal; riesgo de sesgo de selección.

## Confianza por área (estimación)
Macro: media (no revisado hoy). Regulación por región: media-alta, con las excepciones B1/B2. Ripple/Stellar: media. Calendario: media-alta.
