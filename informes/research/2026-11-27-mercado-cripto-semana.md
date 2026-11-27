# Mercado cripto, semana 20-27 nov 2026

Fecha de elaboración: 27-nov-2026. Etiquetas: [P] primaria, [D] dato de agregador/secundaria, [S] solo un medio, [VERIFICAR], [ESPECULACIÓN]. Sin recomendaciones de compra/venta.

## 0. Límites de esta tanda (leer primero)
- Farside (btc/ y eth/) y SoSoValue devolvieron **403**; no se han evitado. Coinglass no se consultó por API (exige clave).
- **No he encontrado flujos diarios de ETF para 17-27 nov 2026** (solo el 16-nov). Los buscadores mezclan notas de nov-2025 (misma fecha, otro año) con las de 2026; he descartado las de 2025 por no coincidir con precios y contexto.
- Los precios son «CoinGecko, punto diario 00:00 UTC», no cierre de bolsa; la variación depende de ese corte.

## 1. Precios (USD) y variación
Fuente [D]: API pública CoinGecko `/coins/{id}/market_chart?days=35&interval=daily`, consultada 27-nov-2026. https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=35&interval=daily (ídem ethereum, ripple, stellar, solana).

| Activo | 27-oct | 20-nov | 27-nov (00:00 UTC) | Semanal | Mensual (desde 27-oct) |
|---|---|---|---|---|---|
| BTC | 80.029 | 61.921 | 60.510 | -2,3 % | -24,4 % |
| ETH | 2.320,7 | 1.755,6 | 1.687,9 | -3,9 % | -27,3 % |
| XRP | 1,3068 | 0,9595 | 0,9428 | -1,7 % | -27,9 % |
| XLM | 0,1692 | 0,1328 | 0,1268 | -4,5 % | -25,1 % |
| SOL | 100,75 | 73,07 | 70,97 | -2,9 % | -29,6 % |

Hechos: mínimo semanal en el punto del 21-nov (BTC 58.818; ETH 1.619,5; XRP 0,9093; XLM 0,1274; SOL 68,76); rebote parcial el 22-24 y retroceso el 25. El 27-nov a última hora de la mañana BTC ~61.490, XRP ~0,975 (dato intradía, cambia). Máximo de octubre en el punto del 29-oct: BTC 81.274.
Mapa de la semana: el movimiento semanal es pequeño frente al del mes; la caída de noviembre se concentró **antes** del 20-nov (en la semana del 9 al 15 BTC pasó de ~74.761 a ~65.312 según The Block/medios citados abajo).

## 2. Flujos de ETF spot de EE. UU.
Lo que sí consta (fuentes [S]/[D], todas citan SoSoValue o Farside):
- Semana 2-6 nov: BTC -1.280 M$ (diario: -398,6; -115,6; +74,6; -430,2; -411,9); IBIT -1.210 M$. CoinStats, 9-nov-2026: https://coinstats.app/news/59499a339fec6491ef38a0580daa5efe5d41056cf080b85ce327ea18bed0c4af_Spot-Bitcoin-ETFs-Weekly-Report-128B-in-Outflows-November-26-2026/ (el titular dice «26» pero el texto cubre 2-6 nov).
- Semana 9-13 nov: BTC -1.070 M$; ETH -398,9 M$ (séptima semana negativa seguida; patrimonio 10.850 M$); SOL -32,1 M$ (sexta negativa; 1.140 M$); XRP -19,1 M$ (segunda negativa). BTC 2026 acumulado ~-1.980 M$. The Block, 14-nov-2026: https://www.theblock.co/news/markets/2026-11-14-bitcoin-etfs-lose-1-billion-for-the-second-week-in-a-row-as-crypto-funds-except-one-440337
- 5-13 nov: siete sesiones seguidas de salida, 1.910 M$; 16-nov: +7,9 M$ (IBIT +76,5; GBTC -34,6; FBTC -11,3). Forklog, 17-nov-2026: https://www.forklog.com/en/bitcoin-etfs-break-outflow-streak-amid-market-decline/
- **Semana 20-27 nov: sin dato verificado para BTC, ETH, XRP ni SOL.** [VERIFICAR] en Farside/SoSoValue o en las páginas de Bitwise, Grayscale, Canary y 21Shares (no consultadas por falta de tiempo; acceso pendiente).

## 3. Funding rates, interés abierto y liquidaciones
Fuente [P/D]: API pública de Binance Futures, `fapi/v1/fundingRate` y `futures/data/openInterestHist`, consulta 27-nov-2026. Funding = media de las liquidaciones de 8 h de cada día, en % por 8 h (referencia neutra de Binance: 0,01 %).

| Día | BTC | ETH | XRP | XLM | SOL |
|---|---|---|---|---|---|
| 20-nov | 0,0018 | 0,0032 | -0,0005 | -0,0059 | -0,0014 |
| 21-nov | -0,0011 | -0,0061 | 0,0005 | -0,0080 | -0,0170 |
| 22-nov | 0,0006 | 0,0010 | 0,0045 | -0,0068 | 0,0039 |
| 23-nov | 0,0033 | -0,0008 | 0,0048 | -0,0073 | -0,0001 |
| 24-nov | 0,0037 | -0,0003 | -0,0092 | -0,0084 | -0,0023 |
| 25-nov | 0,0069 | 0,0059 | 0,0024 | -0,0140 | 0,0049 |
| 26-nov | 0,0070 | 0,0031 | 0,0090 | 0,0035 | 0,0076 |
| 27-nov | 0,0074 | 0,0079 | 0,0071 | -0,0040 | 0,0056 |

Lectura de hechos: funding casi plano y por debajo de 0,01 % (sin apalancamiento largo exuberante); XLM con funding negativo casi toda la semana (más posiciones cortas que largas en Binance). OKX BTC-USDT: funding actual -0,0016 % (https://www.okx.com/api/v5/public/funding-rate?instId=BTC-USDT-SWAP).
Interés abierto en Binance (miles de M$, BTC): 6,01 (20-nov) -> 5,66 (21) -> 5,95 (27); ETH 4,32 -> 3,83 -> 3,93; SOL 0,62 -> 0,53; XRP ~0,25 estable. Cayó el 21-nov (día del mínimo semanal), señal compatible con cierre de posiciones.
**Liquidaciones:** no hay cifra verificada para 20-27 nov (Coinglass sin acceso). Dato previo [D]: ~2.020 M$ liquidados entre sábado 8:00 y domingo 8:00 ET del 14-15 nov (1.680 M$ largos, 342 M$ cortos), según CoinGlass vía The Block/investinglive, 16-nov-2026: https://investinglive.com/cryptocurrency/weekend-bitcoin-fell-to-four-month-low-near-62-000-as-crypto-liquidations-top-2-billion/ . [VERIFICAR] la semana en curso.

## 4. Dominancia y stablecoins
- Dominancia BTC 58,8 % (ETH 10,0 %); capitalización total ~2,10 billones de $; -1,2 % en 24 h. [D] CoinGecko `/global`, 27-nov-2026: https://api.coingecko.com/api/v3/global . Capitalización BTC ~1.238 mil M$.
- Stablecoins, total circulante [D] DefiLlama (https://stablecoins.llama.fi/stablecoincharts/all): 299,45 mil M$ (27-oct) -> 283,43 (20-nov) -> 281,89 (27-nov): **-0,5 % en la semana y -5,9 % en el mes**; pico de la serie consultada 300,67 (24-oct). Caída casi ininterrumpida desde el 24-oct.
- Por emisor (DefiLlama /stablecoins, 27-nov): USDT 173,56 mil M$ (semana previa 175,05; mes previo 181,78); USDC 69,12 (68,80; 71,33); USDe 4,93; DAI 4,52; USDS 3,13 (hace un mes 6,66); USD1 2,85 (3,92). Es decir, la salida mensual la lidera USDT y USDS.

## 5. On-chain XRPL y Stellar
Consultas directas a nodos públicos el 27-nov-2026 (livenet.xrpl.org y stellar.expert no se leyeron: renderizan con JavaScript / 404 en la API probada) [VERIFICAR] en esos exploradores.
- XRPL [P]: ledger validado 108.605.280 (cierre 11:56 UTC 27-nov), estado `full`, comisión base 0,00001 XRP, reserva base 1 XRP, incremental 0,2 XRP (servidor xrplcluster.com, método `server_info`).
- Stellar [P]: ledger 65.698.920 (cierre 11:57:54 UTC 27-nov); ese ledger: 299 transacciones correctas, 388 operaciones (Horizon, https://horizon.stellar.org/ledgers?order=desc&limit=1). Una muestra de un solo ledger no es una cifra semanal.
- TVL DeFi [D] DefiLlama: XRPL 38,6 M$ (hace ~5 semanas) -> 29,3 M$ (~20-nov); último dato 31,2 M$ (26-nov). Stellar 227,5 -> 181,2 M$ (~20-nov); último 182,7 M$. Ambas redes bajan ~20 % en el mes, en línea con el precio. https://api.llama.fi/v2/historicalChainTvl/XRPL y /Stellar.
- Sin datos verificados de pagos diarios, cuentas activas o volumen DEX de la semana.

## 6. Lectura
**Hechos (con fuente arriba)**
1. Entre el 27-oct y el 27-nov las cinco monedas caen 24-30 %; el grueso ocurre en 1-21 nov, y la semana 20-27 es de lateralidad bajista (-2 % a -5 %).
2. Salidas de ETF: -1.280 M$ (2-6 nov) y -1.070 M$ (9-13 nov) en BTC; ETH, SOL y XRP también con salidas la semana del 9-13.
3. Liquidación de ~2.000 M$, mayoritariamente largos, el 14-15 nov, con BTC cerca de 62.000.
4. La oferta de stablecoins cae de ~300 a ~282 mil M$ desde el 24-oct (menos liquidez disponible en el sistema cripto).
5. Funding ahora neutro y OI por debajo de los niveles previos: el apalancamiento largo se ha reducido.
6. TVL de XRPL y Stellar cae en proporción parecida al precio.

**Hipótesis [ESPECULACIÓN]**
- Las salidas de ETF son causa o síntoma: el flujo y el precio se correlacionan en el día (p. ej. -5,5 % el jueves 5-nov con la mayor salida), pero la causalidad no está probada; el propio medio lo advierte.
- Changpeng Zhao atribuyó la caída a retiradas de ETF, expectativa de otra subida de tipos de la Fed, liquidez que se aparta para una OPV de Anthropic y miedo residual tras el hackeo de Binance [S: investinglive, 16-nov]; el propio artículo dice que es su opinión, no causa establecida. Conflicto de interés a considerar: Zhao es parte interesada en el sector.
- La contracción de stablecoins sugiere salida neta de capital del sector más que rotación interna [ESPECULACIÓN]; pudo influir la caída de USDS y USD1.
- El funding neutro tras la purga indica que el exceso de apalancamiento ya se limpió, pero no implica suelo [ESPECULACIÓN].
- Caso alcista: apalancamiento limpio, salidas de ETF cortadas el 16-nov, caída semanal ya pequeña. Caso bajista: stablecoins aún en descenso, sin flujos de ETF confirmados positivos, TVL en mínimos del periodo.

[VERIFICAR] Flujos diarios de ETF 17-27 nov (Farside/SoSoValue/emisores); liquidaciones de la semana (Coinglass); actividad on-chain semanal en livenet.xrpl.org y stellar.expert; si el punto 00:00 UTC de CoinGecko coincide con cierres de Yahoo; cifra del hackeo de Binance y fecha de la OPV de Anthropic citadas por Zhao.
