# DEX y AMM en XRPL y Stellar: liquidez, volúmenes y uso real de XRP y XLM (2026-10-17, R43 profundo)

Plantilla: dossier-region (modo profundo). Etiquetas: **LEÍDO EN EL LEDGER** = consulta directa al nodo público xrplcluster.com (JSON-RPC) o a Horizon (horizon.stellar.org), es decir, el estado de la cadena en el momento de la consulta · **AGREGADOR** = DefiLlama (tercero, metodología propia) · **EXPLORADOR** = Stellar Expert (tercero) [VERIFICAR] · **cálculo mío**. Sin recomendaciones de compra/venta. Todas las consultas son del 17-oct-2026 (≈ 21:45 UTC) con curl y User-Agent identificado, salvo lo indicado.

**Acceso:** abrieron xrplcluster.com (`server_info`, `amm_info`, `gateway_balances`, `book_offers`, `ledger`), horizon.stellar.org (`trade_aggregations`, `trades`, `assets`, `fee_stats`), api.llama.fi (volúmenes DEX por cadena, TVL histórico) y api.stellar.expert (pools por valor). **No funcionó:** Horizon `order_book` para XLM/USDC (error 400 por mi parámetro, no repetido), RWA.xyz (no abierto en esta tarea). **Sin leer:** ficheros de volúmenes de SDEX nativo de Stellar por fuente primaria distinta de Horizon, métricas propias de Ripple/SDF.

## Resumen (5 líneas)
1. **La liquidez en cadena de ambas redes es pequeña frente a lo que dice la prensa.** TVL de DefiLlama: **XRPL ≈ 39,1 M$** (máximo 119,9 M$ el 18-jul-2025, −51 % en un año) y **Stellar ≈ 230,3 M$** (máximo 272,8 M$ el 1-oct-2026, +76 % en un año). Volumen DEX diario: **XRPL 6,2 M$** (24 h) y **Stellar 1,7 M$** (24 h); en 30 días **203,3 M$** y **93,2 M$** (DefiLlama).
2. **El pool de AMM de XRP/RLUSD, leído en el ledger, tiene 1.858.917 XRP y 2.392.362,5 RLUSD (TVL ≈ 4,8 M$, comisión 0,205 %).** Es ≈ 12 % del TVL de XRPL según DefiLlama (cálculo mío) y apenas un 0,23 % de los 1.029,4 M RLUSD emitidos en XRPL (ledger). El libro de órdenes XRP/RLUSD (100 ofertas por lado) cubre ±2 % con ≈ 125.000 $ de ventas y ≈ 103.000 $ de compras: poco fondo para órdenes grandes (la ruta real del DEX combina libro y AMM; el resultado combinado no lo calculé).
3. **Cómo se usa cada activo:** en XRPL una muestra de 368 transacciones de 5 ledgers (sep–oct) es **43 % pagos, 35 % OfferCreate (órdenes del DEX), 9 % Batch, 4 % OfferCancel**; reserva base 1 XRP, reserva por objeto 0,2 XRP, comisión base 10 drops (0,00001 XRP). En Stellar el XLM es la comisión (base 100 stroops = 0,00001 XLM) y el par de referencia (XLM/USDC y pares exóticos); **el 79 % de las últimas 200 operaciones fueron contra pools de liquidez** y el ledger iba al **98 % de capacidad** (señal de bots de arbitraje, no necesariamente de usuarios).
4. **Qué dice la prensa vs. el dato:** "XRPL como infraestructura de liquidez institucional" y "Stellar mueve cientos de millones" mezclan stablecoins/RWA emitidas con volumen negociado y con liquidez de DEX. Lo verificable en cadena: RLUSD emitido en XRPL **1.029,4 M** (R34), USDC en Stellar **≈ 489,5 M** (369,2 + 117,7 + 2,6 + 0,03; Horizon) y volúmenes de DEX mensuales de **13–20 %** de esos saldos (5–8 veces menores; ver cálculos).
5. **Para XRP/XLM:** el uso de DEX/AMM es dato de utilidad real pero modesto (millones de dólares al día); no hay en estas fuentes un precio causal. Cualquier cifra de "volumen" debe citarse con serie (DefiLlama, Horizon, ledger), ventana y fecha.

## Qué es hecho verificado
| Dato | Fuente | Fecha | Calidad |
|---|---|---|---|
| Ledger validado XRPL **#107.725.838** (build rippled 3.4.1), base fee 10 drops, reserva base **1 XRP**, reserva por objeto **0,2 XRP**; rango completo de ledgers 32570–107725838 | xrplcluster.com `server_info` | 17-oct-2026 | LEÍDO EN EL LEDGER |
| AMM XRP/RLUSD (cuenta rhWTXC2m2gGGA9WozUaoMm6kLAVPb1tcS3): **1.858.917,012668 XRP** y **2.392.362,516672 RLUSD**; comisión de negociación **205** (= **0,205 %**); tokens de LP **1.787.122.329**; precio implícito **1,28697 RLUSD/XRP** | xrplcluster.com `amm_info` (ledger 107725843) | 17-oct-2026 | LEÍDO EN EL LEDGER; precio y TVL = cálculo mío |
| RLUSD emitido en XRPL (cuenta emisora rMxCKbEDwqr76QuheSUMdEGf4B9xJ8m5De): obligaciones **1.029.443.742,86** | xrplcluster.com `gateway_balances` | 17-oct-2026 | LEÍDO EN EL LEDGER (coincide con R34) |
| Libro de órdenes XRP/RLUSD (primeras 100 ofertas por lado): mejor venta **1,28752**, mejor compra **1,28593**, diferencial **0,123 %**; fondo hasta ±0,5 %: ventas **31.736 XRP** (≈ 40.800 $) y compras **19.561 XRP** (≈ 25.200 $); hasta ±1 %: **67.196** (≈ 86.500 $) y **36.844** (≈ 47.400 $); hasta ±2 %: **97.368** (≈ 125.300 $) y **80.325** (≈ 103.400 $), con el tope de 100 ofertas alcanzado en ≈ ±2 % | xrplcluster.com `book_offers` | 17-oct-2026 | LEÍDO EN EL LEDGER; sumas = cálculo mío; el libro más allá de 100 ofertas no se leyó |
| Muestra de transacciones de 5 ledgers (107725844, 107705844, 107575844, 107325844, 106925844; 12-sep a 17-oct): **368 tx** = Payment **157 (42,7 %)**, OfferCreate **130 (35,3 %)**, Batch **34 (9,2 %)**, OfferCancel 15 (4,1 %), NFTokenCreateOffer 14 (3,8 %), AccountSet 10 (2,7 %), TrustSet 3, NFTokenCancelOffer 2, NFTokenMint 1, AccountDelete 1. Ninguna fue de tipo AMM (AMMSwap/Deposit) en la muestra; todas las del ledger actual **tesSUCCESS** | xrplcluster.com `ledger` (expand) | 17-oct-2026 | LEÍDO EN EL LEDGER; 5 ledgers = muestra pequeña, no representativa |
| DEX de XRPL (DefiLlama): volumen **24 h 6,20 M$**, **7 d 36,22 M$**, **30 d 203,28 M$**; el protocolo "XRPL DEX" aporta 202,8 M$ de los 30 d y Sologenic 0,49 M$; máximo diario **39,83 M$ el 21-ago-2026**; media diaria de 7 días: **5,17 M$** frente a **7,92 M$** (semana del 11-oct-2025) y **3,59 M$** (semana del 13-jul-2026) | api.llama.fi `overview/dexs/XRPL` | 17-oct-2026 | AGREGADOR; medias = cálculo mío |
| DEX de Stellar (DefiLlama): **24 h 1,70 M$**, **7 d 12,68 M$**, **30 d 93,17 M$**, casi todo asignado a **Aquarius Stellar (93,16 M$)**; media diaria de 7 días 1,81 M$ frente a 4,89 M$ (semana del 10-oct-2025) y 1,45 M$ (12-jul-2026); máximo histórico diario 28,4 M$ (24-nov-2024) | api.llama.fi `overview/dexs/Stellar` | 16-oct-2026 | AGREGADOR; medias = cálculo mío |
| TVL (DefiLlama): XRPL **39,05 M$** (30 d antes 38,72; 90 d antes 32,63; 365 d antes 79,17; máximo 119,95 M$ el 18-jul-2025). Stellar **230,28 M$** (30 d antes 242,39; 90 d antes 219,09; 365 d antes 130,63; máximo 272,84 M$ el 1-oct-2026) | api.llama.fi `historicalChainTvl` | 17-oct-2026 | AGREGADOR |
| Stellar XLM/USDC (Horizon `trade_aggregations`, 29 días hasta el 16-oct, resolución diaria): volumen en USDC **66,28 M$** y **2.086.668 operaciones** (media 72.000 al día; **≈ 31,8 $ por operación**); últimos 7 días (10 a 16-oct): 0,33 / 0,87 / 0,97 / 1,32 / 1,10 / 2,30 / 0,82 M$ (media **1,10 M$/día**); cierre 16-oct **0,1811 USDC/XLM** | horizon.stellar.org | 17-oct-2026 | LEÍDO EN EL LEDGER; sumas y medias = cálculo mío |
| Últimas 200 operaciones de Stellar (≈ 5 s de ledgers): **158 pool de liquidez (79 %)** y **42 libro de órdenes (21 %)**; pares más frecuentes: T99/XLM 35, R3FL3cT/XLM 34, T2L2/XAU 24, XAU/XLM 24, XLM/YxT 24 | horizon.stellar.org `trades` | 17-oct-2026 | LEÍDO EN EL LEDGER; muestra de 5 s |
| Stellar `fee_stats`: base fee **100 stroops**; comisión cobrada mediana **100**; comisión máxima ofrecida mediana **20.001**; uso de capacidad del ledger **0,98**; ledger 64.997.537, protocolo **29** | horizon.stellar.org | 17-oct-2026 | LEÍDO EN EL LEDGER |
| USDC emitido en Stellar (Circle): cuentas **369.179.520**; contratos (Soroban) **117.694.760**; en pools de liquidez clásicos **2.643.555**; saldos reclamables 29.962; cuentas autorizadas **2.485.520** | horizon.stellar.org `assets` | 17-oct-2026 | LEÍDO EN EL LEDGER; total 489,5 M = cálculo mío |
| Pool clásico XLM/USDC más grande por valor (Stellar Expert): TVL ≈ **4,77 M$** (47.672.864.841.730 ÷ 10⁷, unidad por verificar), volumen 1 d ≈ **0,164 M$**, 7 d ≈ **3,96 M$**, comisión **0,30 %**, 1.080 operaciones en 1 d. Coherente con los 2,64 M USDC de todos los pools (el lado USDC ≈ 2,4 M$) | api.stellar.expert | 17-oct-2026 | EXPLORADOR [VERIFICAR] |

### Cálculos míos
| Cálculo | Resultado |
|---|---|
| TVL del pool AMM XRP/RLUSD = 2 × 2.392.362,5 RLUSD | **4,78 M$** |
| Ese TVL / TVL de XRPL de DefiLlama (39,05 M$) | **12,2 %** |
| RLUSD en el pool / RLUSD emitido en XRPL | 2,392 M / 1.029,4 M = **0,23 %** |
| Volumen DEX en 30 días / RLUSD emitido (XRPL, 203,3 M$ / 1.029,4 M) | **19,7 %** al mes (no es "rotación": mezcla todos los pares) |
| Volumen XLM/USDC en Horizon, 29 días / USDC en Stellar (66,3 M$ / 489,5 M$) | **13,5 %** |
| Volumen medio diario de 7 días XRPL: 5,17 M$ frente a 7,92 M$ hace un año | **−35 %** |
| Volumen medio diario de 7 días Stellar: 1,81 M$ frente a 4,89 M$ hace un año | **−63 %** |
| TVL XRPL: 39,05 / 79,17 − 1; Stellar: 230,28 / 130,63 − 1 | **−50,7 %**; **+76,3 %** |
| Fondo ±2 % del libro XRP/RLUSD (primeras 100 ofertas): 125.285 $ y 103.355 $ | una orden de ≈ 100.000 $ consume todo el libro de su lado hasta ±2 % |

## Qué está sin verificar o es opinión
- **"XRPL es la cadena de liquidez de la banca":** los datos de este informe (TVL 39 M$, volumen diario 6 M$) no lo respaldan como uso de DEX; el uso institucional (pagos, custodia, RLUSD) es otra métrica y está en R28/R34 [ESPECULACIÓN] si se mezcla.
- **Que el TVL de DefiLlama sea completo:** DefiLlama solo suma los protocolos que tiene catalogados; el AMM nativo de XRPL (que no es un contrato) y el SDEX nativo de Stellar pueden quedar fuera o dentro según la métrica. La asignación de casi todo el volumen de Stellar a un solo protocolo (Aquarius, 93,16 M$ de 93,17 M$) sugiere que el agregador no cubre todo el SDEX [VERIFICAR] (Horizon mide solo XLM/USDC en 66,3 M$ en 29 días, sin comparar con DefiLlama por pares).
- **Interpretar 72.000 operaciones diarias de XLM/USDC como "usuarios":** a ≈ 32 $ por operación y con el 79 % en pools y el ledger al 98 %, el patrón es compatible con bots de arbitraje; no puedo separar usuarios de bots con estos datos [ESPECULACIÓN].
- **Valoración de Stellar Expert (unidad ÷10⁷):** inferida, no documentada en esta sesión [VERIFICAR].
- **Que no existan swaps de AMM en XRPL:** la muestra de 368 transacciones no incluye ninguno, pero el DEX encamina órdenes de pago y de oferta por el AMM de forma interna; el uso real del AMM no se mide por tipo de transacción.
- **Titulares de "volumen récord en XRPL/Stellar":** comprobar si hablan de volumen DEX, de pagos, de valor emitido o de operaciones; el máximo diario de DefiLlama en XRPL (39,83 M$, 21-ago-2026) es un solo día.

## Caso alcista / caso bajista (sobre el uso real de los DEX/AMM; datos, no recomendación)
**Alcista:** Stellar crece en TVL (+76 % anual; máximo 272,8 M$ el 1-oct-2026) y en USDC emitido (≈ 489,5 M$ en total, con 117,7 M$ ya en contratos Soroban); el AMM de XRPL tiene diferencial bajo (0,12 %) y comisión baja (0,205 %); el máximo diario de volumen de XRPL de 39,8 M$ muestra que la capacidad puntual existe.
**Bajista:** el TVL de XRPL es la mitad del de hace un año y el 67 % menos que su máximo; el volumen DEX de 7 días es −35 % (XRPL) y −63 % (Stellar) frente a hace un año; el libro XRP/RLUSD tiene ≈ 100.000 $ de fondo a ±2 %; el pool AMM XRP/RLUSD vale 4,8 M$ frente a 1.029 M$ de RLUSD en la red; gran parte del tráfico de Stellar son bots y tokens exóticos.

## Qué cambia para los digital assets
- **XRP:** utilidad en el ledger = comisiones (mínimas), reservas (1 XRP + 0,2 por objeto) y moneda puente del DEX/AMM; su peso en la liquidez cargada es pequeño (1,86 M XRP en el pool principal).
- **XLM:** igual para comisiones y par de referencia; el XLM necesita pools para exóticos, y el XLM/USDC tiene ≈ 2,4 M$ de USDC.
- **Stablecoins:** RLUSD y USDC dominan los saldos; la actividad DEX es una fracción mensual de lo emitido (13–20 %, ver cálculos).
- **Tokenización (R26/R33):** cifras RWA y de stablecoins por cadena no son volumen de DEX; no sumarlas.

## Fechas próximas (catalizadores) con fuente
| Fecha | Evento | Fuente | Estado |
|---|---|---|---|
| ~23-oct | Posible activación de fixCleanup3_4_0 en XRPL (R32) | xrplcluster.com `feature` (R32) | [VERIFICAR] |
| 27–29-oct | Swell (Nueva York) y Meridian (Lisboa), eventos de Ripple y SDF | swell.ripple.com, meridian.stellar.org (R37) | parte interesada |
| Semanal | Re-medir TVL/volumen (DefiLlama, Horizon, ledger) para ver si la tendencia cambia | api.llama.fi; horizon.stellar.org | rutina |

## Qué falta por buscar
1. Fondo combinado (libro + AMM) de XRP/RLUSD con la ruta del DEX (`ripple_path_find`) para órdenes de 10.000, 100.000 y 1.000.000 $.
2. Lista y tamaño de otros pools de XRPL (XRP/USDC, XRP/EUROP, etc.): no hay forma pública de enumerar todos los pools con `amm_info` sin conocer los pares; Bithomp/XRPScan/DefiLlama como terceros.
3. Comparación por pares entre DefiLlama y Horizon para Stellar (¿se cuenta el SDEX nativo?).
4. Quién crea la mayor parte del tráfico de Stellar (cuentas más activas en 24 h) y si son bots de arbitraje.
5. Métricas oficiales de Ripple y de SDF sobre uso de DEX (si existen) para contraste con terceros.
