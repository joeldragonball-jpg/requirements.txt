# ETF al contado, Protocolo 30 de Stellar y escrow de XRP (27-nov-2026)

Alcance: hechos con fuente y fecha. Sin recomendaciones. [S] = no verificado en fuente primaria; [VERIFICAR] = contradicción o duda; [ESPECULACIÓN] = predicción.
Límite: no se pudo abrir ninguna fuente primaria de flujos (ver sección 1). Todos los flujos vienen de agregadores secundarios.

## 1. Flujos netos diarios de los ETF al contado de EE. UU. (13 al 26-nov-2026)

Accesos:
- Farside (farside.co.uk/btc/): HTTP 403 el 27-nov-2026. No se evitó; queda sin consultar.
- SoSoValue (sosovalue.com/assets/etf/us-btc-spot): HTTP 403 el 27-nov-2026.
- Se usaron agregadores que dicen citar Farside y SoSoValue: TFTC (datos actualizados 25-nov, revisados 27-nov), cryptodataapi.com y prensa. Todo [S].
- Los datos llegan hasta el 25-nov. El 26-nov en EE. UU. fue festivo (Acción de Gracias) [S: supuesto por calendario, no verificado]; el 27-nov aún no está incluido.

### 1.1 BTC (US$ millones; negativo = salida)

| Fecha | TFTC | cryptodataapi |
|---|---|---|
| 13-nov | -185,5 | -185,4 |
| 16-nov | +8,0 | +7,9 |
| 17-nov | -239,9 | -239,9 |
| 18-nov | -306,4 | -306,5 |
| 19-nov | -582,2 | -582,3 |
| 20-nov | -669,2 | -669,2 |
| 23-nov | -569,7 | -569,7 |
| 24-nov | -231,6 | -231,4 |
| 25-nov | -453,1 | -453,0 |
| 26-nov | sin dato | sin dato |

- Suma 13 al 25-nov (TFTC): aprox. -3.229 M$ (cálculo propio). Acumulado noviembre (2 al 25): -5.391 M$ en ambas fuentes.
- Otras cifras: ChainCatcher habla de unos -5.390 M$ y la nota de que supera el récord mensual previo; Pouyam, citando Farside/SoSoValue, daba unos -4.710 M$ a 23-nov; The Block (20-nov) daba unos -3.470 M$ hasta esa fecha. Las diferencias son de fecha de corte [S].
- Racha: salidas 7 sesiones seguidas del 17 al 25-nov (SoSoValue vía TokenPost, -453,12 M$ el 25-nov).
- Hecho: 16 de 18 sesiones de noviembre con salida neta.

### 1.2 ETH (cryptodataapi.com, dice usar Farside/SoSoValue; US$ M)

13-nov +2,3 · 16-nov -8,4 · 17-nov -29,1 · 18-nov -39,8 · 19-nov -131,2 · 20-nov -97,3 · 23-nov -84,9 · 24-nov -64,1 · 25-nov -68,5 · 26-nov sin dato.
- Acumulado noviembre (2 al 25): -1.287,4 M$. Solo 2 sesiones positivas (4-nov y 13-nov). [S]
- No contrastado con una segunda fuente.

### 1.3 XRP

- No se obtuvo tabla diaria completa. Datos sueltos (SoSoValue citado por prensa):
  - Del 1 al ~21-nov: -30,76 M$ netos, sin ningún día positivo (36Crypto, Hokanews, bitcoinworld, c. 21-nov).
  - 25-nov: +4,07 M$, todo de XRPZ de Franklin Templeton; único ETF cripto en positivo ese día (Digital Today, Crypto Economy, CoinAlert, 26-nov).
  - Activos netos totales aprox. 1.040 M$; entradas acumuladas desde el lanzamiento aprox. 1.780 M$ (otras fuentes 1.790 M$) [S].
  - 30 días hasta el 25-nov: -21,25 M$ netos.
- Aritmética: -30,76 + 4,07 = aprox. -26,7 M$ en noviembre hasta el 25 (cálculo propio, solo si no hubo otros días con entrada entre el 21 y el 24-nov) [VERIFICAR].
- Desglose por fecha del 13 al 24-nov: no disponible.

### 1.4 SOL (cryptodataapi.com; US$ M)

13-nov -3,1 · 16-nov +11,7 · 17-nov 0,0 · 18-nov 0,0 · 19-nov -1,1 · 20-nov -5,9 · 23-nov -3,8 · 24-nov +0,7 · 25-nov 0,0 · 26-nov sin dato.
- Acumulado noviembre (2 al 25): -55,4 M$. [S]
- Entrada de +11,684 M$ el 16-nov (hora ET), BSOL de Bitwise +10,784 M$ (SoSoValue vía KuCoin, Invezz). Cryptobriefing la fecha el 17-nov y habla de racha de 24 días sin entradas cortada; otros rastreadores dicen 0 el 17-nov. [VERIFICAR fecha por diferencia de liquidación.]
- 24-nov: +0,7496 M$, todo del Morgan Stanley Solana Trust (MSOL) (SoSoValue vía KuCoin). Activos netos aprox. 982 M$ y entradas acumuladas aprox. 1.412 M$ [S].

### 1.5 Sesgos y límites
- Los agregadores no son primarios; los titulares de "récord" dependen del corte de fecha.
- Sesgo de cobertura: la prensa cripto destaca el "único ETF en verde" aunque sean 4 M$ frente a cientos de millones de salidas en BTC.
- Los flujos son de EE. UU.; no incluyen ETP europeos ni de Hong Kong.

## 2. Stellar, Protocolo 30 "Bell" (votación mainnet 23-nov-2026)

Hechos (fuente primaria parcial):
- Guía oficial de la SDF (stellar.org/blog/developers/bell-protocol-30-upgrade-guide, leída 27-nov): votación mainnet 23-nov-2026 a las 17:00 UTC; marcada como completa, con la frase "Mainnet is on Protocol 30" y en el registro de cambios "Protocol 30 is live on Mainnet". El comando de armado de validadores (upgradetime=2026-11-23T17:00:00Z, protocolversion=30) se compartió el 4-nov.
- Testnet: votación el 3-nov, completada a las 17:05 UTC según estado oficial citado por prensa.
- Contenido (prensa citando CAP-84, CAP-87, CAP-88): direcciones multiplexadas para contratos, verificación de firmas poscuánticas en Soroban, tiempo de ledger en milisegundos [S en los detalles].
- Requisito: Stellar Core v30.0.0 (publicado 16-oct-2026).
- CoinGabbar (24-nov, act. 25-nov) dice que la mejora está activa, citando a Wu Blockchain; no da recuento de votos ni ledger.

No encontrado:
- Recuento de validadores, ledger exacto de activación, ni incidencias. No se consultó stellar.expert ni el hilo de stellar-validators (no abiertos). [VERIFICAR]
- Una pieza de Coinotag (24-oct) daba fechas distintas (4 y 24-nov); es un valor atípico frente a SDF y otros medios.

## 3. Liberación del escrow de XRP de Ripple, 1-dic-2026

- Estructura (Ripple, ripple.com/insights): escrows que liberan 1.000 M XRP el día 1 de cada mes; lo no usado se vuelve a bloquear en nuevos escrows.
- Hoy (27-nov) no ha ocurrido: la liberación programada es el 1-dic-2026 a las 00:00 UTC (xrp-insights.com). No hay dato del resultado. Los XRP relockeados se verán on-chain (XRPScan/Bithomp/Whale Alert) en los días siguientes.
- Último mes cerrado, nov-2026: se liberaron 1.000 M XRP el 1-nov (dos transacciones de 500 M); Ripple devolvió 700 M a escrow con vencimiento 2029, neto fuera aprox. 300 M (Coinpaper, CryptoTicker, KuCoin, 1-2 nov). Bitbase, antes, decía que el relock aún no estaba confirmado; las fuentes posteriores lo superan.
- Histórico (xrp-insights.com, ene-2025 a nov-2026, 23 liberaciones): 22 meses con relock de 700 M (70 %), jun-2025 con 670 M (67 %); total relockeado 16,07 mil M de 23 mil M (aprox. 69,9 %); neto fuera aprox. 6,93 mil M XRP. Últimos 12: 70 %. [S]
- [VERIFICAR] La serie es sospechosamente uniforme (casi siempre 700 M exactos) y no está contrastada con la cadena. Un análisis encontrado en la búsqueda sostiene que en mayo-2026 no se relockearon 800 M, lo que contradice la tabla; otras piezas citan relocks de 200 M, 400 M y 500 M en otros momentos. Además, unos medios afirman relocks de "todo el mil millones" que la cadena no respaldó. Falta comprobar mes a mes en XRPScan.
- Matiz: lo liberado no equivale a lo vendido; Ripple lo usa para operaciones y ventas programadas, y los XRP relockeados tardan horas o días [S].
- [ESPECULACIÓN] Si se repite el patrón, el 1-dic saldrían aprox. 300 M netos; es continuidad histórica, no certeza.

## Lista [VERIFICAR]
1. Farside y SoSoValue dieron 403: pedir la tabla diaria de BTC/ETH/XRP/SOL a mano (Chrome) y cotejar con TFTC y cryptodataapi.
2. Flujos del 26-nov (festivo en EE. UU.) y del 27-nov: sin dato.
3. XRP: falta la serie diaria del 13 al 24-nov y confirmar si hubo entradas entre el 21 y el 24.
4. SOL: entrada del 16 o 17-nov (diferencia de fecha).
5. Stellar: recuento de validadores y ledger de activación en stellar.expert / stellar-validators.
6. Escrow: comprobar en XRPScan los relocks reales de mayo-2026 y de los últimos 12 meses; y el resultado real del 1-dic.

Fuentes: farside.co.uk (403), sosovalue.com (403), tftc.io/bitcoin-etf-flows/november-2026, cryptodataapi.com/etf-flows/{btc,eth,sol}/2026-11, theblock.co (20-nov), tokenpost.com, chaincatcher.com, pouyam.com, 36crypto.com, hokanews.com, digitaltoday.co.kr, coinalertnews.com (26-nov), kucoin.com/news, invezz.com (18-nov), cryptobriefing.com, stellar.org (guía Bell), coingabbar.com, coinranking.com, coinpaper.com, cryptoticker.io, xrp-insights.com/xrp-radar/escrow, ripple.com/insights.
