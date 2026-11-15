# C308 - Profundidad multi-divisa (XRPL, Stellar) y velocidad/reposo (15-nov-2026)

Instantánea de las 10:35 UTC, **no tendencia**. Script: `scripts/leer_profundidad.py` (stdlib, 3 reintentos, SSL verificado, conserva el dato anterior si falla). Salida: `explorador/profundidad-multidivisa.json`; histórico `explorador/profundidad-historial.jsonl` (una línea por día).

## Método
Profundidad = valor (en la divisa de cotización) de las ofertas del libro dentro de ±1 % y ±2 % del precio medio (mejor compra + mejor venta)/2. Solo libro de órdenes (CLOB); excluye AMM/pools. Nivel P (nodo/Horizon directo).

## XRPL (book_offers, s1.ripple.com, hasta 300 ofertas por lado)
| Par | Spread | Prof. ±1 % compra / venta |
|---|---|---|
| XRP/RLUSD | 0,13 % | 61.377 / 82.248 RLUSD |
| XRP/USDC (Circle) | 0,21 % | 41.489 / 2.684 USDC |
| XRP/SOLO | 0,20 % | 573 / 16.989 SOLO |
| XRP/USD Bitstamp | 7,4 % | 0 / 0 (libro inactivo) |
| XRP/USD GateHub | 7,3 % | 0 / 0 |
| XRP/EUR GateHub | 11,6 % | 0 / 0 |
| XRP/EUROP | 57,6 % | 0 / 0 (2 ofertas de compra) |
| XRP/BTC Bitstamp | 8,4 % | 0 / 0 |

Lectura: la liquidez del CLOB está concentrada en RLUSD y USDC; los IOU históricos (Bitstamp/GateHub) tienen ofertas obsoletas lejos del mercado (~1,00-1,14 USD por XRP frente a ~0,96 en RLUSD). Cero profundidad en ±1 % es consecuencia del hueco, no un error.

## Stellar (Horizon /order_book, 200 ofertas por lado)
| Par | Spread | Prof. ±1 % compra / venta | ±2 % compra / venta |
|---|---|---|---|
| XLM/USDC | 0,14 % | 9.634 / 128.367 USDC | 9.810 / 129.088 |
| XLM/EURC | 0,84 % | 0 / 5.369 EURC | 1.542 / 5.369 |
| USDC/EURC | 0,23 % | 1.316 / 37.699 EURC | 166.227 / 135.664 |
XLM/USDC llega al tope de 200 ofertas por lado: las cifras son un mínimo.

## Velocidad y reposo del XRP
- Pagos/día (P, extrapolación de 11 ledgers en ~24 h): ~907.000 Payment correctos (~674.000 en XRP nativo); ~6,1 M de transacciones totales/día; ~21.000 ledgers/día. Orden de magnitud; incluye bots/spam.
- Escrow (S, xrpscan + total_coins del nodo): ~35.245 M XRP = 35,25 % del supply. Es bloqueo por calendario, no "inactividad".
- % del supply inactivo >1 año: **null**, sin API pública sin clave.

## Stablecoins por red (S, DefiLlama chainCirculating)
- XRPL: RLUSD 762,7 M USD; USDV 72,8 M; EURCV 11,0 M EUR; EUROP 0,4 M EUR.
- Stellar: USDC 344,9 M USD; MGUSD 25,3 M; YLDS 25,3 M; EURCV 16,5 M EUR; EURC 7,3 M EUR.
- Solana: USDC 7.397 M; USDT 2.004 M; USDGO 1.064 M. Ethereum: USDT 66.783 M; USDC 41.686 M; USDS 5.359 M.
- Importes en su moneda de referencia, sin convertir.

## Huecos
- Sin AMM/pools (XRPL AMM, pools de Stellar): la liquidez real total es mayor que la del CLOB.
- Profundidad de mercado de Solana y Ethereum no leída (sin API pública única sin clave).
- Par XLM/AQUA descartado (emisor no válido en Horizon); emisores XRPL tomados de memoria pública, los que no tienen ofertas válidas aparecen con libro inactivo.
- Un solo punto en el histórico: la tendencia aparecerá al acumular días.
