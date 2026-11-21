# Repaso de la semana 14–21 nov 2026

Informativo; sin recomendaciones. Cifras del repo a 21-nov (script y planning propios).

## 1. Qué se hizo (107 commits, ~217 informes en informes/research)
- **Rutinas:** R00 apertura/cierre cada día (racha 14), W01–W10 hechas en el periodo, W12 diaria (5–10 hechos volcados al día).
- **Cadenas:** escenarios sin stablecoin (CBDC, depósitos tokenizados, nostro/vostro, BRICS/BIS), capa Mercado en 16 redes, mapa de leyes (MiCA, GENIUS, CLARITY), DTCC leído literal, préstamos XRPL, rendimientos (nueva hoja `rendimientos.json`).
- **España a fondo:** pensiones, vivienda (compraventas INE), presupuesto IPC real, SEPE, energía (OMIE corregido: la cifra anterior era la columna de Portugal), leyes BOE, empleados públicos.
- **Países:** mandatos, elecciones, indicadores, bloques; regulación (VARA, Hong Kong fiscal a P).
- **Voces y predicciones:** 31+ voces de vídeos, 72 criterios, #20 «falló» con reserva, #19 confirmada; 178 filas en la medición (109 abiertas, 9 acertó, 6 falló).
- **Estado del tablero:** 366 movimientos, 13 capas, 0 avisos del revisor, 308 ids sin fallos. Bot de paneles arreglado el 19-nov (fallaba desde el 16).

## 2. Qué pasó en el mercado (hechos, fuente: R00 propios)
Caída escalonada: S&P −2,0 % el 19-nov y −3,7 % el 20-nov, SOXX −10,5 %, VIX 38,8, BTC −5,9 %. La causa sigue sin verificar [VERIFICAR]. El tablero ya recoge los precios; la explicación no.

## 3. Qué falla o queda a medias
1. **Medición de predicciones**: `medicion_predicciones.py` duplica filas (los totales no son fiables).
2. **Radar regulatorio**: 9 celdas sin dato por bloqueos de red (CNMV, OJK, SCA, DFSA).
3. **Mandatos**: casi todos siguen [S]; solo Putin pasó a [P].
4. **~1.080 menciones [VERIFICAR]** en explorador; el consolidado W05 cierra ~15 por semana.
5. **Auditoría de integración**: hallazgos 7, 10 y 12–17 sin hacer.
6. **`leer_liquidez.py`**: URL fija del informe de septiembre del PBoC; puede pisar el dato corregido de China.
7. **Informes antiguos** que citan el OMIE de Portugal sin nota de corrección.
8. **Rendimiento**: muchas capas y pestañas; C223 (carga por pestaña) sin hacer.
9. **Despertador**: GitHub se salta ejecuciones programadas (no es fallo del código).

## 4. Qué perfeccionar (propuesta, ordenada)
A. Arreglos baratos y seguros (≈2–3 %): medicion_predicciones, leer_liquidez dinámica, nota OMIE en informes viejos, nivel RBI/Basilea alineado.
B. Explicar la caída del 19–20-nov con fuentes primarias (calendario, datos, bonos) separando hechos de hipótesis.
C. Cerrar hallazgos 7, 10, 12–17 y repasar el tablero en móvil (Joel lo revisa y dicta cambios).
D. Cuatro huecos de contenido con más valor: mandatos S→P (con Chrome), 9 celdas de regulación (consulta manual), flujos ETF XRP/SOL/XLM, indicadores sociales C59 (cuando FMI/Banco Mundial vuelvan).

## 5. Research a agendar (ya en el calendario de W09)
- 23-nov: W01 y voto Stellar P30. 24-nov: W02. 25-nov: W08. 26-nov: W04 y W05. 27-nov: W06/W09. 30-nov: cierres de #24, #68, #9, #15, #19, #23. 9-dic: FOMC.
- Gemini del día: Energía y geopolítica (prompt `research/gemini/NOTICIAS-DIA.md`), lo pega Joel.
- Nuevo propuesto: tarea «Causa del desplome 19–20-nov» (B) y «Mandatos S→P con Chrome» (D).
