# Predicciones · revisión del 20-nov-2026

Sin recomendaciones. Registro: `informes/predicciones.md` (única fuente editada). `docs/movil/seguimiento.json` no se toca (lo regenera `construir_seguimiento.py`).

## 1. Predicción #20 (CoinDesk, PaymentBurn 27/35 votos): FALLÓ, con reserva

Evidencia leída en el navegador (Chrome, RPC público xrplcluster.com) [P]:
- `ledger_entry` del objeto Amendments (índice 7DB0788C...CD6EF4) en el ledger 107.536.129 (9-oct 09:34:31 UTC): `fixCleanup3_4_0` (ID 98433DD0...ECA76) figura en Majorities con `CloseTime` 844853670 (= 9-oct 09:34:30 UTC). Se repite a las 16:56 UTC del 9-oct (ledger 107.543.000, tras el artículo de las 12:21 EDT = 16:21 UTC) y el 12-oct (ledger 107.600.000).
- Ledger 107.824.128 (22-oct): la mayoría figura con `CloseTime` 21-oct 14:46:22 UTC (se reinició; coincide con #19) y `enabled: false`.
- `feature`: `enabled: true` hoy (ledger validado 108.451.220, 20-nov 09:39 UTC).
- xrpl.org/known-amendments [P]: el cambio de «PaymentBurn-only delegated payments» está dentro de la ficha de `fixCleanup3_4_0`, así que el objeto de CoinDesk y el del ledger coinciden.

Decisión: «Falló» (afirmación «sin mayoría, 27 de 35» contradicha por el ledger en el momento del artículo). Reserva escrita en la fila: no se identificó el panel de CoinDesk (puede medir otra métrica o un instante anterior), se puntúa la afirmación, no la intención; la fuente CoinDesk queda con 1 contradicha, sin tasa (n < 5).

## 2. Vencimientos a 14 días

| # | Plazo | Dato primario | Resultado |
|---|---|---|---|
| 24 (Ormuz, ≥ ~85 tránsitos) | 30-nov | IMF PortWatch, servicio ArcGIS `Daily_Chokepoints_Data`, Estrecho de Ormuz, `n_total`, hasta 15-nov: 1-8 al día entre 25-oct y 15-nov (15-nov: 2; media 9-15 nov: 2,3) | Umbral no cumplido; la condición (EE. UU. levanta el bloqueo) no consta; si sigue así, se cierra «sin puntuar» (condicional) el 30-nov, no «falló». No resoluble aún |
| 76 (Clarity, nuevo voto/texto demócrata) | 27-nov | senate.gov, `vote_menu_119_2.xml`: 271 votos nominales hasta el 19-nov; último de CLARITY (H.R. 3633) = 15-sep; desde el 9-nov solo H.R. 2347, H.Con.Res. 93 y nominaciones | Sin moción de cierre; texto demócrata sin buscar en congress.gov [VERIFICAR]. Abierta |
| 80 (Rusia lista cripto el 22-nov) | 22-nov | cbr.ru/news hasta el 19-nov: ningún comunicado sobre listado de cripto ni hito del 22-nov (ausencia, no prueba) | Abierta; probablemente mal planteada (solo se cierra el 22-nov+) [VERIFICAR] |
| 68 (WLF/FFF entregan documentos) | 30-nov | No se halló página primaria del PSI en esta pasada | Abierta; la nota [S] del 20-nov se mantiene |

Ninguna se puede resolver hoy: todas tienen el plazo por delante.

## 3. Normalización (C92/C108)

- La tabla «Criterios de medición» ya daba `fuente oficial` y `límite` normalizado para las 89 filas; las que no tienen fecha (#1, 13, 50, 63, 64, 67, 71, 72, 79, 89) siguen «sin puntuar» por criterio (sin fecha no vencen), y #1 conserva el límite propuesto 2026-12-31 en la tabla de criterios.
- Corregido el formato de las filas 24, 68, 76 y 80 (celda extra «| · Comprobado…» que dejaba 8 columnas): ahora el comprobado va dentro de la celda de resultado, en la tabla principal y en la de criterios.
- Pendiente que NO se hizo: la columna `fuente_id` (v### de `voces.json`) no existe en el registro; añadirla exige tocar el esquema de `medicion_predicciones.py` y construir_seguimiento.py (fuera del alcance de esta pasada).
- Aviso: `scripts/medicion_predicciones.py` cuenta las filas de las dos tablas (178 en lugar de 89) porque el regex `| n |` también casa con la tabla de criterios; sus totales (109 abiertas, 9 acertó, 6 falló) están duplicados. Conviene limitar el análisis a la primera tabla.

## 4. Validación y seguridad
`python scripts/revisar_explorador.py`: 0 avisos en 13 capas y 346 movimientos. Solo lectura de fuentes públicas, sin claves ni API de Anthropic, sin commit ni push. Se alcanzó el límite del RPC público (slowDown) por un barrido que lancé; se redujo a consultas puntuales. Pestaña propia cerrada.
