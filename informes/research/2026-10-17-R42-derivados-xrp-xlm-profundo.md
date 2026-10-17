# Derivados de XRP y XLM: futuros y opciones regulados y offshore, interés abierto, financiación (2026-10-17, R42 profundo)

Plantilla: dossier-region (modo profundo). Etiquetas de calidad de fuente: **[REG-OFICIAL]** = informe oficial de un regulador (CFTC, Commitments of Traders), leído por API · **[BOLSA-API]** = API pública de la propia bolsa (Binance, Bybit, OKX), dato del operador, sin auditar por tercero · **[SEC.]** = agregador o prensa [VERIFICAR] · **cálculo mío** = aritmética sobre los datos anteriores. Sin recomendaciones de compra/venta.

**Acceso (todo con curl y User-Agent identificado el 17-oct-2026):** publicreporting.cftc.gov (API Socrata, datasets TFF `gpe5-46if` y Disaggregated `jun7-fc8e`), fapi.binance.com y dapi.binance.com (públicas), api.bybit.com (v5), www.okx.com (v5), www.deribit.com. **No abrieron:** cmegroup.com (403 en página de producto y de especificaciones), investor.cmegroup.com (403), liquidaciones de Binance (`allForceOrders` ya no es pública: 404). **Sin dato:** CME no publica en abierto el volumen diario por contrato; el interés abierto sale de la CFTC (semanal, martes).

## Resumen (5 líneas)
1. **En XRP el mayor interés abierto regulado está en CME: 7.613 contratos de 50.000 XRP = 380,65 M XRP (≈ 490 M$ a 1,288 $, cálculo mío) el 13-oct** [REG-OFICIAL]. Es más que el de Binance perpetuo (305,6 M XRP ≈ 395 M$) y que el de Bybit y OKX juntos (193,8 M + 65,3 M XRP ≈ 334 M$) [BOLSA-API]. El rango de CME en 14 semanas: 5.539–8.684 contratos (sin tendencia clara).
2. **XLM tiene derivados mucho más pequeños:** el único contrato regulado con datos es el "Stellar perp-style" de Coinbase Derivatives (5.000 XLM por contrato): **4.643 contratos = 23,2 M XLM ≈ 4,1 M$** (13-oct) [REG-OFICIAL]; Binance perpetuo 190,3 M XLM ≈ **33,5 M$** y OKX ≈ **9,8 M$** [BOLSA-API]. No localicé un contrato de CME para XLM.
3. **Desde el pico de septiembre el interés abierto perpetuo ha caído:** Binance XRP **−28 %** (559,5 → 402,1 M$, del 23-sep al 17-oct) y XLM **−44 %** (63,4 → 35,3 M$, del 29-sep al 17-oct), con precio del XRP casi plano; la métrica es en dólares, así que parte puede ser precio (cálculo mío con la serie diaria de Binance).
4. **La financiación (funding) es pequeña y cambia de signo:** en 30 días el promedio en Binance fue **+0,0035 % por 8 h en XRP y +0,0047 % en XLM** (≈ 3,8 % y 5,1 % anualizados, cálculo mío); en las últimas 5 liquidaciones ambos alternan positivo/negativo, y la última de cada uno fue **negativa** (−0,0061 % XRP; −0,0055 % XLM). Lectura prudente: no hay apalancamiento largo agresivo en las tasas, aunque la cuenta de "largos" de Binance sea mayoritaria (ver abajo).
5. **Opciones: casi irrelevantes fuera de CME.** Deribit **no lista** opciones de XRP ni XLM (consulta de instrumentos vacía); Bybit sí (256 series de XRP, 1,80 M de contratos de 1 XRP ≈ **2,3 M$** de nocional, cálculo mío) con ratio put/call de interés abierto **0,32**. Opciones de CME sobre futuros de XRP: existen desde oct-2025 según prensa y CME [SEC.]; **su interés abierto no es público** en las fuentes que abrí.

## Qué es hecho verificado
| Dato | Fuente | Fecha | Calidad |
|---|---|---|---|
| CME, "XRP" (contratos de 50.000 XRP): interés abierto **7.613**; apalancados (lev. money) **2.077 largos / 2.122 cortos**; gestores de activos **1.034 / 620**; dealers **4.292 / 4.636**; 30 operadores | CFTC, TFF Futures Only (dataset gpe5-46if), semana 41 de 2026 | 13-oct-2026 | REG-OFICIAL, EN |
| Serie CME de interés abierto (contratos): 6.676 (14-jul), 7.862 (28-jul), 5.540 (11-ago), 5.575 (18-ago), 7.778 (25-ago), 7.215 (8-sep), **8.684 (22-sep, máximo de las 14 semanas)**, 7.716 (29-sep), 7.871 (6-oct), 7.613 (13-oct). Los apalancados pasan de **618 largos y 2.539 cortos (14-jul)** a **2.077 largos y 2.122 cortos (13-oct)**: reducen la posición neta corta | CFTC, TFF | jul–oct-2026 | REG-OFICIAL, EN; lectura = cálculo mío |
| Coinbase Derivatives, "Stellar perp style" (5.000 XLM): OI **4.643** (13-oct); mínimo 3.364 (15-sep); máximo 4.643 (13-oct); apalancados **839 largos / 4.135 cortos**; "otros" **2.276 / 395**; 51 operadores | CFTC, TFF | 13-oct-2026 | REG-OFICIAL, EN |
| Coinbase Derivatives, "Nano XRP" (500 XRP): OI **59.801** (= 29,9 M XRP); "Nano XRP perp style": **38.798** (= 19,4 M XRP); "XRP" (10.000 XRP): **24.483** el 6-oct (= 244,8 M XRP), con dealers largos 22.307 y "otros" cortos 8.330 (última semana disponible; no hay fila del 13-oct) | CFTC, TFF | 13-oct / 6-oct-2026 | REG-OFICIAL, EN |
| Binance USDⓈ-M perpetuo XRPUSDT: OI **305.638.529 XRP**; marca 1,2910; última financiación **−0,001934 %** (8 h) | fapi.binance.com `openInterest`, `premiumIndex` | 17-oct-2026 | BOLSA-API |
| Binance XLMUSDT: OI **190.322.050 XLM**; marca 0,1762; última financiación **−0,016252 %** | fapi.binance.com | 17-oct-2026 | BOLSA-API |
| Binance, serie diaria (30 días, 18-sep a 17-oct) del OI en dólares: XRP máximo **559,5 M$ (23-sep)**, mínimo **396,2 M$ (16-oct)**, último **402,1 M$**; XLM máximo **63,4 M$ (29-sep)**, mínimo **34,3 M$ (16-oct)**, último **35,3 M$** | fapi.binance.com `futures/data/openInterestHist` | 17-oct-2026 | BOLSA-API |
| Binance financiación de 90 liquidaciones (30 días): XRP media **+0,00351 %** (66 positivas, 24 negativas; mín −0,01674 %, máx +0,01000 %); XLM media **+0,00469 %** (68 / 22; mín −0,01671 %, máx +0,01000 %) | fapi.binance.com `fundingRate` | 18-sep a 17-oct-2026 | BOLSA-API; promedios = cálculo mío |
| Binance: proporción de **cuentas** con posición larga frente a corta en XRPUSDT: 70,9 % / 29,1 % (11-oct) … **74,8 % / 25,2 % (17-oct)**, razón 2,97 | fapi.binance.com `globalLongShortAccountRatio` | 11 a 17-oct-2026 | BOLSA-API; mide número de cuentas, no dinero |
| Bybit lineal XRPUSDT: OI **193.770.534 XRP** (249,9 M$ a marca 1,2898); financiación **+0,003263 %**; volumen 24 h 111,5 M XRP | api.bybit.com v5 `tickers` | 17-oct-2026 | BOLSA-API |
| OKX XRP-USDT-SWAP: OI **65.250.898 XRP** (84,4 M$); financiación vigente **+0,0029 %** (la última liquidada fue **−0,0034 %**). OKX XLM-USDT-SWAP: OI **55,4 M XLM** (≈ 9,75 M$) | www.okx.com v5 `public/open-interest`, `funding-rate` | 17-oct-2026 | BOLSA-API |
| Binance COIN-M XRPUSD_PERP: OI **5.628.407 contratos** (tamaño del contrato en USD [VERIFICAR]; no convertido a dólares) | dapi.binance.com | 17-oct-2026 | BOLSA-API |
| Opciones de XRP en Bybit: 256 series; OI total **1.804.030** contratos (unidad mínima 10 → contrato = 1 XRP); calls **1.363.820** / puts **440.210** (put/call **0,32**); vencimiento **30-oct-2026 con 941.790 (52 %)**, 18-oct 386.400, 23-oct 373.510, 27-nov 67.900; volumen 24 h 344.510 | api.bybit.com v5 `tickers`, `instruments-info` (category=option) | 17-oct-2026 | BOLSA-API; sumas y razón = cálculo mío |
| Deribit: `get_instruments` para XRP y XLM (kind=option) devuelve **lista vacía**; XRP y XLM aparecen como divisas, sin opciones | www.deribit.com API v2 | 17-oct-2026 | BOLSA-API |
| OKX opciones (uly XRP-USD): lista vacía | www.okx.com v5 | 17-oct-2026 | BOLSA-API |

### Cálculos míos
| Cálculo | Resultado |
|---|---|
| OI CME en XRP: 7.613 × 50.000 | **380,65 M XRP** (≈ **490,2 M$** con el precio de Binance de 1,2879 $ del 17-oct; la fecha del OI es 13-oct, el precio es posterior: orden de magnitud) |
| OI Coinbase Derivatives "Stellar perp style": 4.643 × 5.000 XLM | **23,2 M XLM** (≈ **4,09 M$** a 0,17621 $) |
| Binance XRP: 305.638.529 × 1,2910 | **394,6 M$** (la serie diaria, valorada por Binance al cierre diario, da 402,1 M$) |
| Binance XLM: 190.322.050 × 0,1762 | **33,5 M$** |
| Variación del OI en dólares: Binance XRP 402,12 / 559,51 − 1; XLM 35,29 / 63,41 − 1 | **−28,1 %**; **−44,3 %** |
| Financiación media anualizada (media × 3 × 365) | XRP **3,84 %**; XLM **5,13 %** (simple, sin capitalizar) |
| Nocional de opciones de Bybit: 1,804 M × 1,297 | **≈ 2,3 M$** |

## Qué está sin verificar o es opinión
- **Cifras de CME de 2025–26 que circulan** (1.000 M$ de OI en 3 meses; 1.400 M$ en sept-2025; "3.000 M$ en futuros y opciones de XRP y SOL"): vienen de prensa y de notas de CME que no pude abrir (403) [SEC.]. Son de otro precio del XRP; no son comparables con los 490 M$ de hoy sin ajustar por precio.
- **Interés abierto de las opciones de CME sobre futuros de XRP:** no hay fuente abierta leída [VERIFICAR].
- **Datos de agregadores (Coinglass, CoinMarketCap, etc.):** no los usé (piden clave o no abren con curl). Suelen sumar bolsas con definiciones distintas (contratos, monedas o dólares) y cuentan la OI por moneda de colateral; sus totales no coinciden con las APIs de cada bolsa. Marcar siempre [SEC.].
- **"Los largos dominan, mercado sobrecomprado":** la razón larga/corta de Binance cuenta **cuentas**, no dinero; una cuenta pequeña pesa igual que una grande. No es sentimiento institucional [ESPECULACIÓN].
- **Liquidaciones:** no hay serie pública de Binance leída; las cifras de "liquidaciones de 24 h" de la prensa vienen de agregadores [SEC.].
- **Atribución del descenso del OI** (cierre de posiciones vs. bajada de precio): no separado; la serie en dólares mezcla ambos.

## Caso alcista / caso bajista (sobre lo que dicen los derivados; datos, no recomendación)
**Alcista:** el OI regulado de CME ronda 490 M$ y es mayor que el de cualquier bolsa offshore individual; los apalancados en CME han pasado de 618 largos a 2.077 largos en 14 semanas y han reducido su corto neto de 1.921 a 45 contratos (cálculo mío con la tabla del 14-jul y del 13-oct); la financiación media del último mes es positiva pero pequeña (no hay posiciones largas "caras"); no hay opciones offshore relevantes que añadan cobertura en cadena (gamma pequeña).
**Bajista:** el OI perpetuo de Binance ha caído 28 % (XRP) y 44 % (XLM) desde su máximo; las últimas financiaciones son negativas; en CME los dealers (4.636 cortos) tienen más cortos que largos (4.292) —típico de contrapartida de ETF/clientes, no necesariamente una apuesta [ESPECULACIÓN]—; el OI regulado de XLM es de ~4 M$, demasiado pequeño para que los derivados midan el interés institucional; las opciones de Bybit se concentran un 52 % en el vencimiento del 30-oct, pero todo el mercado vale ~2 M$.

## Qué cambia para los digital assets
- **XRP:** el mercado de derivados regulado (CME + Coinbase Derivatives) es grande en relación con el offshore, y se puede seguir cada martes con la CFTC (sin clave). Esto permite separar flujo regulado de especulación offshore, algo que no se puede hacer con XLM.
- **XLM:** apenas hay derivados regulados; el seguimiento depende de Binance/OKX (dato de la bolsa) y de un contrato en Coinbase Derivatives.
- **Riesgo de narrativa:** titulares de "récord de interés abierto" suelen medir dólares (sube con el precio), no contratos ni monedas; verificar siempre unidad, bolsa y fecha.

## Fechas próximas (catalizadores) con fuente
| Fecha | Evento | Fuente | Estado |
|---|---|---|---|
| 20-oct (martes de referencia) → publicación 23-oct | Nuevo informe COT/TFF (posiciones a 20-oct) | CFTC (calendario de publicación) | [VERIFICAR] fecha exacta de la CFTC; suele ser viernes 15:30 ET |
| 18-oct, 23-oct, 30-oct | Vencimientos de opciones de Bybit en XRP (30-oct = 52 % del OI) | api.bybit.com `tickers` | dato de la bolsa |
| 27–28-oct | FOMC (variable de riesgo para el apalancamiento) | federalreserve.gov (R29/R41) | oficial |

## Qué falta por buscar
1. Interés abierto y volumen de las **opciones de CME sobre futuros de XRP** (CME no abre; probar boletín de CME Group "Crypto Insights" o PDF descargado por Joel a `research/fuentes/`).
2. Contrato de XLM en CME (¿existe?) y tamaño real del contrato COIN-M de Binance.
3. Serie larga del OI regulado (CFTC desde el lanzamiento, mayo-2025) para comparar contratos y monedas con el pico de 2025; solo traje 14 semanas.
4. Liquidaciones en fuente primaria (Binance/Bybit/OKX solo las dan por API privada o WebSocket).
5. Contraste con la data del **ETF de futuros** (SEC/N-PORT) para saber si el dealer corto de CME es cobertura de ETF [ESPECULACIÓN hasta verificar].
