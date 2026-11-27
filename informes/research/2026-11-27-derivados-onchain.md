# Derivados y datos on-chain, 20-27 nov 2026

Fecha de elaboración: 27-nov-2026, lecturas de las 12:00-12:20 UTC. Sin recomendaciones: solo datos.
Etiquetas: [P] primaria (API del propio exchange o nodo), [D] dato de agregador/medio, [S] secundaria sin contrastar, [VERIFICAR], [ESPECULACIÓN].

## 1. Precios de referencia (27-nov, ~12:16 UTC)
- BTC 61.582 USD; ETH 1.720,64 USD; XRP 0,9753 USD; XLM 0,1299 USD. [D] CoinGecko API /simple/price, 27-nov-2026. https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple,stellar&vs_currencies=usd,btc
- Ratio ETH/BTC: 0,02794 (24 h: -0,49 %). XRP/BTC 1,584e-5 (+0,90 %). XLM/BTC 2,11e-6. [D] misma fuente.
- Dominancia BTC 58,81 %; ETH 9,99 %. Capitalización total 2,104 billones USD; volumen 24 h 58,4 miles de millones USD. [D] CoinGecko /global, 27-nov-2026. https://api.coingecko.com/api/v3/global
- Trayectoria de la caída (cierres diarios UTC, CoinGecko market_chart): 12-nov 73.974; 13-nov 71.372; 14-nov 68.314; 15-nov 64.120; 18-nov 64.889; 19-nov 62.997; 20-nov 61.921; **21-nov 58.818 (mínimo diario del tramo)**; 22-nov 60.121; 25-nov 59.759; 26-nov 60.374. Caída 12→21 nov: -20,5 %. Rebote parcial posterior (~+4,7 % desde el mínimo). [D] https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=16&interval=daily
- Nota: el mínimo intradía real puede ser inferior al cierre diario. [VERIFICAR]

## 2. Open interest (OI)
### Binance USDT-M (histórico diario, fecha UTC) [P] https://fapi.binance.com/futures/data/openInterestHist
| Día | BTC OI (mill. USD) | ETH OI (mill. USD) | XRP OI (mill. USD) |
|---|---|---|---|
| 13-nov | 7.226 | 4.724 | 318 |
| 14-nov | 6.717 | 4.488 | 297 |
| 15-nov | 6.281 | 4.103 | 277 |
| 16-nov | 6.109 | 4.217 | 277 |
| 17-nov | 6.003 | 4.157 | 257 |
| 18-nov | 5.973 | 4.285 | 259 |
| 19-nov | 6.070 | 4.345 | 250 |
| 20-nov | 6.010 | 4.320 | 254 |
| 21-nov | 5.661 | 3.826 | 252 |
| 22-nov | 5.525 | 3.903 | 256 |
| 23-nov | 5.704 | 4.019 | 258 |
| 24-nov | 5.719 | 3.943 | 250 |
| 25-nov | 5.763 | 3.982 | 254 |
| 26-nov | 5.855 | 3.928 | 253 |
| 27-nov (corte 00:00) | 5.945 | 3.931 | 249 |

Lectura (hechos): del 13 al 27 nov el OI en dólares cae en BTC -17,7 %, ETH -16,8 %, XRP -21,6 % (en Binance, valorado a precio del día). En monedas, el OI de BTC apenas varía (101.152 → 98.196 BTC), es decir, gran parte de la caída en USD es precio, no cierre de posiciones. En XRP sí hay caída en unidades (305 M → 264 M XRP, -13 %). El OI de BTC en Binance sube cuatro días seguidos (22→27 nov: 91.792 → 98.196 BTC): reconstrucción de posiciones tras el mínimo. Instantáneo 27-nov: BTCUSDT 97.751 BTC; XRPUSDT 267,5 M XRP. [P]
Sesgo: Binance es un solo exchange; el agregado (Coinglass) es mayor. Coinglass exige clave para su API y no se consultó. [VERIFICAR]

### Deribit (OI de futuros, en USD para BTC/ETH; 27-nov) [P] https://www.deribit.com/api/v2/public/get_book_summary_by_currency
- BTC perpetuo: 802 M USD; futuro 25-dic-26: 316 M; 26-mar-27: 125 M; 25-jun-27: 87 M.
- ETH perpetuo: 289 M USD; futuro 25-dic-26: 78 M; 26-mar-27: 30 M.
- Base: futuro BTC dic-26 mark 61.754 frente a spot 61.585 (prima muy pequeña); jun-27 63.424 (+3,0 %). [P] Estructura casi plana: poca demanda apalancada de largo.

### Dato de prensa (no contrastado)
- Santiment, 18-nov: OI de BTC agregado ~17,99 miles de millones USD, tras caer ~20 % en dos semanas, el más bajo desde oct-2024. [S] Resumen vía buscador, URL original no abierta; ver https://cointelegraph.com/news/bitcoin-open-interest-hits-lows-not-seen-since-2024-is-tradfi-abandoning-btc (la fecha del artículo no se comprobó). [VERIFICAR]

## 3. Funding
- BTC Binance (8 h): 25-nov 16:00 0,0061 %; 26-nov 00:00 0,0080 %; 08:00 0,0085 %; 16:00 0,0045 %; 27-nov 00:00 0,0099 %; 08:00 0,0050 %. Equivale a ~5,5-10 % anualizado (referencia 0,01 % = nivel base). [P] https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT
- ETH Binance (último): 0,0039 %. [P] premiumIndex, 27-nov 12:17 UTC.
- XRP Binance (último): 0,0052 %. XRP OKX: 0,0030 % (liquidado 0,0060 %). [P]
- Deribit BTC perpetuo: funding 8 h 0,0000029; ETH perpetuo -0,00002. [P]
- Lectura: funding cercano al nivel base y levemente positivo en los tres: no hay señal de apalancamiento extremo ni largo ni corto ahora. Hecho; interpretación = [ESPECULACIÓN]. Santiment (18-nov) lo describía cerca de cero o negativo en plena caída. [S]

## 4. Liquidaciones de la semana de la caída (13-21 nov)
- 14-nov: ~1.540 M USD liquidados, 94 % largos (Santiment, vía resumen de búsqueda). [S] [VERIFICAR]
- Binance: más de 520 M USD de liquidaciones en noviembre antes de la 2.ª quincena; OI BTC en Binance 10.600→8.800 M en menos de un mes (artículo edgeX, fecha sin comprobar). [S] https://pro.edgex.exchange/en-US/news/article/bitcoin-open-interest-falls-17-binance-liquidations
- No se pudo obtener la serie diaria de Coinglass (requiere clave/web con JS). No hay cifra verificada para el 21-nov (mínimo). El buscador devolvió informes de otros años y junio-2026 que NO se usan. [VERIFICAR]
- Coherencia con datos primarios: el OI en dólares de BTC en Binance baja 7.226 → 5.525 M entre el 13 y 22-nov, y el de ETH 4.724 → 3.826 M (21-nov, mínimo, -19 %). Compatible con liquidaciones y cierres forzosos, pero no las mide.

## 5. Opciones (Deribit, 27-nov 12:00 UTC) [P] https://www.deribit.com/api/v2/public/get_book_summary_by_currency?kind=option
Cálculo propio (OI por strike; máx. dolor = strike que minimiza el valor intrínseco total pagado). Es una estimación, no cifra oficial.
- OI total opciones: BTC 339.122 BTC (~20.900 M USD a 61.585); ETH 1.616.797 ETH (~2.780 M USD).
- Vencimiento mensual 27-nov: ya liquidado a las 08:00 UTC de hoy; no aparece en el libro. Próximo diario 28-nov (BTC: C 1.866 / P 1.665, ratio P/C 0,89, máx. dolor 60.500; ETH: ratio P/C 1,64, máx. dolor 1.680).
- Vencimiento 4-dic (semanal): BTC P/C 1,38, máx. dolor 63.000; ETH P/C 1,30, máx. dolor 1.800.
- **Vencimiento 25-dic-26 (trimestral, el mayor)**: BTC calls 98.036 / puts 68.011 BTC (~6.000 M + 4.200 M USD nocional; 55 % del OI total de BTC aprox.), P/C 0,69, máx. dolor 70.000 (+13,7 % sobre spot). ETH calls 504.420 / puts 211.474, P/C 0,42, máx. dolor 2.200.
- Otros: 26-mar-27 BTC máx. dolor 70.000; 29-ene-27 BTC P/C 1,08 máx. dolor 67.000.
- Lectura: el grueso del OI de opciones está en calls de diciembre con strikes muy por encima del precio actual; el máx. dolor está lejos del spot, y la teoría de «máximo dolor» tiene un historial mixto como predictor. [ESPECULACIÓN] sobre su efecto. Las puts dominan en semanales cercanos (cobertura corta).
- Volatilidad implícita y skew: no consultados. [VERIFICAR]

## 6. XRP Ledger
- Libro mayor validado 108.605.596 (27-nov 12:18 UTC), rippled 3.4.1. [P] https://s1.ripple.com:51234/ (server_info)
- Ritmo actual: 25,8 tx/s, 98 tx por ledger, intervalo 3,87 s, comisión media 0,000246 XRP. [P] https://livenet.xrpl.org/api/v1/metrics (27-nov)
- Transacciones diarias, estimación propia por muestreo de 20 ledgers por día (precisión baja, ±30 %): 27-nov ~2,3 M (parcial); 26-nov ~1,7 M; 25-nov ~4,3 M; 24-nov ~3,3 M; 23-nov ~2,1 M; 22-nov (aprox.) ~3,0 M. Ritmo vivo 25,8 tx/s ≈ 2,2 M/día. [P-estimación] Prensa citaba 2,5-3 M diarios en meses previos [S]; el muestreo es compatible.
- Cuentas activas: no hay cifra fiable para 20-27 nov. Referencias de prensa: 32.604 activas el 27-oct (récord de 2026, ~68 % sobre la media de 30 días de 19.400) y 7.934 cuentas nuevas el 1-nov. [S] https://coinpaper.com/38042/xrp-ledger-hits-2026-record-with-32-604-active-accounts-but-xrp-price-falls-13 y https://cryptobriefing.com/xrp-ledger-new-wallets-november-1/. Bitquery (ago-2026): 793 cuentas generaron el 93 % del tráfico; casi la mitad de las activas envió una sola tx: el recuento de cuentas sobrestima participación real. [S] https://bitquery.io/investigations/xrp-ledger-adoption-audit [VERIFICAR]
- Volumen DEX XRPL y escrow de Ripple (saldo y desbloqueo del 1-dic): no obtenidos (xrpscan/livenet sin endpoint abierto utilizable; data.ripple.com solo llega a 2022). Pendiente: la liberación mensual de hasta 1.000 M XRP de escrow del 1-nov se anunció; el 1-dic toca la siguiente, y Ripple suele volver a bloquear la mayoría (patrón histórico). [VERIFICAR] en https://xrpscan.com/ o https://livenet.xrpl.org/

## 7. Stellar
- Ledger 65.699.162 (27-nov 12:18 UTC): 349 operaciones, 171 transacciones exitosas y 184 fallidas. [P] https://horizon.stellar.org/ledgers
- Operaciones diarias, estimación propia (muestra de 200 ledgers ≈ 17 min a las ~12:17 UTC de cada día × 17.280 ledgers/día; muy aproximado): 27-nov 5,9 M; 26-nov 6,8 M; 25-nov 8,2 M; 24-nov 7,6 M; 23-nov 8,5 M; 22-nov 6,5 M; 21-nov 8,5 M; 20-nov 9,1 M; 19-nov 7,2 M. Tendencia a la baja de 9,1 a 5,9 M en la muestra. [P-estimación]
- Alta proporción de transacciones fallidas (~52 % en el ledger actual): típico de bots de arbitraje; no equivale a uso de pagos. [ESPECULACIÓN]
- stellar.expert devuelve 402 (pago requerido) en su API; no se evadió. Cuentas activas y volumen DEX de Stellar: no obtenidos. [VERIFICAR]

## 8. Resumen para el tablero
1. Tras caer BTC un 20,5 % (12→21-nov), el OI en dólares bajó un 17-22 % y se estabiliza; en BTC (unidades) el OI casi no cambió y vuelve a subir.
2. Funding en niveles base: sin sobreapalancamiento visible.
3. Opciones: OI concentrado en 25-dic con máx. dolor de BTC en 70.000 y ETH en 2.200, lejos del spot.
4. ETH/BTC 0,0279; dominancia BTC 58,8 %.
5. XRPL ~2-3 M tx/día (estimación) y Stellar ~6-9 M ops/día (estimación); datos de cuentas, DEX y escrow quedan sin cubrir.
Sesgos: datos de Binance/Deribit son parciales del mercado; medios agregan cifras sin metodología; los muestreos propios son aproximados.

## Pendientes [VERIFICAR]
- Liquidaciones diarias 13-21 nov en Coinglass (clave/JS necesarios; no se evitó).
- OI agregado multi-exchange de BTC/ETH/XRP y funding agregado.
- Fecha y cifra exacta de Santiment/edgeX (artículos citados vía resumen de buscador).
- Cuentas activas XRPL y Stellar, volumen DEX, saldo y calendario del escrow de Ripple (1-dic).
- Volatilidad implícita y skew de Deribit; confirmación de «máx. dolor» con la web de Deribit.
- Mínimo intradía real del 21-nov.
