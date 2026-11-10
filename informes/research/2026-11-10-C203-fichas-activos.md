# C203 · Fichas por activo (XRP, XLM, BTC, oro, ETF mundial) — 10-nov-2026

Sin recomendaciones ni predicciones. [P] = fuente primaria leída (en informes previos); [S] = agregador o prensa; [VERIFICAR] = sin contrastar; [ESPECULACIÓN] = opinión o previsión. Información general: no se mide cada activo contra ninguna tesis personal.

## Qué se ha hecho
- `explorador/fichas-activos.json` (nuevo): 5 fichas con tabla de hechos (dato, valor, unidad, fecha, nivel, fuente), caso alcista, caso bajista, sesgos de las fuentes, [VERIFICAR], [ESPECULACIÓN] y fuentes.
- Pestaña «Fichas por activo» en `explorador/vistas.html` (Órbita) y carga en `explorador.py`.
- **No se han leído fuentes oficiales nuevas** hoy: todo sale de `paneles.json` (CoinGecko, Yahoo [S]), `precios_historico.json` (Yahoo [S]), `regulacion.json`, y los informes T19, W04, C237 y G5 (con sus niveles). Por eso la tarea queda «en parte».

## HECHOS (con su nivel)
- Precios del 9/10-nov (CoinGecko, Yahoo) [S]: XRP 1,10 USD, XLM 0,1487 USD, BTC 74.558 USD, oro (futuro) 4.129,3 USD/onza; IWDA 128,52 EUR, VWCE 167,42 EUR.
- Variación desde el 6-oct-2025 (primer dato de la serie, cálculo propio) [S]: XRP -63 %, XLM -64 %, BTC -40 %, oro +4 %; oro -22 % desde su máximo de futuros de ene-2026.
- ETF de XRP en EE. UU.: ≈ 1.510 M USD de activos y ≈ 1.800 M USD de entradas acumuladas a 28-oct [S].
- Oro: compras de bancos centrales 57 t (1T revisado), 289 t (2T), 321 t (3T) [P, WGC].
- MSCI World: 1.249 valores, 23 países; 13,37 %/año a 10 años; PER 22,69; caída máxima -57,46 % [P, MSCI, 30-sep-2026].

## OPINIONES y límites
- Los casos alcista/bajista son análisis, no consejo. Las previsiones (precio, flujos, tokenización → demanda de XLM) van como [ESPECULACIÓN].
- Sin verificar: AUM actual de los ETF de BTC (cifra del 5-oct), peso de EE. UU. del MSCI World/FTSE, TER, ETF de XLM en EE. UU. (EDGAR), cifra de 2.178 M USD de R27, comunicado DTCC-SDF.

## Lecciones (≤ 5)
1. Los máximos dependen del agregador: el futuro de Yahoo (5.318) y WGC (5.405) difieren para el oro.
2. La serie de Yahoo arranca el 6-oct-2025: el «-X % desde» es desde ese día, no desde el máximo histórico.
3. Los agregadores discrepan en un mismo fondo (GXRP 87,3 frente a 28,3 M USD): citar fuente y fecha.
4. Las rentabilidades de MSCI son brutas y en USD; no son las del ETF en EUR.
5. Para cerrar la tarea: leer 10-Q en EDGAR y fichas MSCI/FTSE/KID.
