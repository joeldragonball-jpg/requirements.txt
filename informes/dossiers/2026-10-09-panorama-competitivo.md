# Dossier: Panorama competitivo de XRP y XLM en pagos y tokenización (9-oct-2026)

> Informativo. No es recomendación de compra ni venta, ni de ninguna criptomoneda. Fuentes **primarias** leídas hoy: XRP Ledger (nodo público `xrplcluster.com`/`s1.ripple.com`), Stellar (Horizon público), Solana (RPC público), DTCC, ECB (Appia), Stellar Docs, Kinexys (web de J.P. Morgan), Mastercard (vía The Block, ver sesgo). **Agregadores con fecha:** DefiLlama (API, 9-oct-2026 ~21:20 UTC) y rwa.xyz (9-oct-2026). El resto es secundario. Lo no confirmado va como [VERIFICAR]; las predicciones, como [ESPECULACIÓN]. Los cálculos que no vienen de la fuente están marcados "(cálculo mío)".

## 1. Resumen ejecutivo
1. **XRPL y Stellar son pequeñas frente a Ethereum, Tron y Solana en stablecoins:** de ~304.600 M$ de stablecoins (suma por cadena, DefiLlama), **XRPL tiene 1.212 M$ (≈0,4 %)** y **Stellar 941 M$ (≈0,3 %)** (cálculo mío). Ethereum 144.870 M$ (≈48 %) y Tron 93.980 M$ (≈31 %).
2. **En tokenización (RWA) Stellar sí compite:** rwa.xyz la sitúa **4.ª con 3.580 M$ "distribuidos"** (≈9 % del total de 39.070 M$, cálculo mío), por delante de Arbitrum y muy por delante de XRPL (**499 M$ distribuidos**, ≈1,3 %). XRPL luce una cifra "representada" de **4.540 M$** que **no es comparable**: son activos registrados en la cadena, no distribuidos ni negociables en ella.
3. **Los competidores más peligrosos para el relato "pagos" no son otras cripto, sino redes de bancos y empresas de pagos:** libro mayor de Swift (17 bancos, jul-2026), Kinexys (>7.000 M$ diarios, cifra propia), Pontes del BCE (sep-2026), Visa (>20.000 M$ anualizados en stablecoins, cifra propia, 8-sep) y Mastercard (liquidación con stablecoins en 8 cadenas, **incluida XRPL**, 3-jun-2026).
4. **Ni XRP ni XLM aparecen como protagonistas en ninguna de esas redes.** Las fuentes oficiales hablan de stablecoins (RLUSD, USDC) y depósitos tokenizados; el papel de XRP/XLM como activo puente **no está medido con datos oficiales en ningún caso**.
5. **Hecho técnico:** en la muestra de hoy XRPL y Stellar procesaron cifras reales parecidas (~39 y ~47 tx/s) y Solana unas ~1.900 tx/s no-votos. Las TPS "teóricas" que presumen los proyectos no se observan.

## 2. Mapa de competidores (qué es cada uno)
| Competidor | Tipo | Qué hace en pagos / tokenización | Estado |
|---|---|---|---|
| **XRPL** (Ripple) | L1 pública, validadores (UNL de 35) | DEX nativo, RLUSD, MPT, credenciales, dominios con permisos y DEX con permisos | Producción |
| **Stellar** | L1 pública, protocolo 29 | Anclajes, USDC/EURC/MGUSD, RWA (Spiko, Franklin Templeton, Ondo), contratos Soroban | Producción |
| **Solana** | L1 pública | Mayor cadena de pagos/stablecoins no-EVM: USDC 6.794 M$, USDT 2.942 M$, PYUSD 746 M$ | Producción; Alpenglow aún no activo (ver §6) |
| **Ethereum y L2 (Base, Arbitrum)** | L1 + rollups | Ethereum: USDT 72.930 M$, USDC 45.150 M$, RWA 16.880 M$ distribuidos. Base: USDC 4.390 M$; Arbitrum: USDT 820 M$ + USDC 2.360 M$ | Producción |
| **Tron** | L1 pública | USDT 92.380 M$ (≈50 % del USDT total, cálculo mío: 92,38/183,21) | Producción |
| **Hedera** | L1 con consejo de gobernanza | USDC 48 M$; stablecoins mínimas en DefiLlama | Producción, ecosistema pequeño |
| **Algorand** | L1 pública | USDC 62 M$, TVL en RWA 127 M$ (DefiLlama categoría RWA) | Producción, ecosistema pequeño |
| **Canton** (Digital Asset) | L1 con privacidad, permisos | Repo tokenizado (Broadridge DLR, cifra propia ≈350.000 M$/día, **no es de Canton**), DTCC y Visa/Mastercard como cadena soportada | Producción limitada; DTCC prevé lanzamiento en oct-2026 |
| **Tempo** (Stripe/Paradigm) y **Arc** (Circle) | L1 de stablecoins | Pagos con stablecoins; Tempo en mainnet desde 18-mar-2026 (secundaria); Arc 2026 beta [VERIFICAR] | Muy nuevas |
| **Swift ledger** | Red de bancos (Besu/EVM) | Depósitos tokenizados 24 h; liquidación final sigue en sistemas actuales | Piloto de 17 bancos (dossier 6) |
| **Pontes / Appia (BCE)** | Infraestructura del Eurosistema | Pontes: liquidación DLT en dinero de banco central (21-sep-2026). Appia: plano para 2028 | Pontes en marcha limitada |
| **Kinexys/JPM Coin (J.P. Morgan)** | Banco privado + token de depósito en Base | Pagos institucionales | Producción |
| **Visa / Mastercard** | Redes de tarjetas | Liquidación con stablecoins entre bancos emisores y adquirentes | Producción creciente |

## 3. Stablecoins por cadena (DefiLlama, 9-oct-2026) — agregador
| Cadena | Total stablecoins | USDT | USDC | RLUSD | % del total (cálculo mío) |
|---|---|---|---|---|---|
| Ethereum | 144.870 M$ | 72.930 M$ | 45.150 M$ | 1.300 M$ | 47,6 % |
| Tron | 93.980 M$ | 92.380 M$ | — | — | 30,9 % |
| Solana | 16.100 M$ | 2.942 M$ | 6.794 M$ | — | 5,3 % |
| BSC | 13.310 M$ | 9.180 M$ | 1.590 M$ | — | 4,4 % |
| Base | 5.190 M$ | — | 4.390 M$ | — | 1,7 % |
| Arbitrum | 3.800 M$ | 820 M$ | 2.360 M$ | — | 1,2 % |
| **XRPL** | **1.212 M$** | 0 | 3,6 M$ | **1.135 M$** | **0,4 %** |
| **Stellar** | **941 M$** | 0 | 377 M$ | — | **0,3 %** |
| Algorand / Hedera | 63 M$ / 48 M$ | 0,8 M$ / 0,1 M$ | 61,5 / 48,3 M$ | — | <0,03 % |

- **Total suma por cadena:** ≈304.600 M$ (cálculo mío); USDT 183.210 M$ y USDC 73.040 M$ circulantes.
- **RLUSD:** 2.440 M$ en total, **1.135 M$ en XRPL (≈47 %)**; el resto, en Ethereum. Coincide con el ledger de XRPL (1.140 M$ en dossier 6).
- **Lectura:** en XRPL la stablecoin dominante es RLUSD (una empresa, Ripple); en Stellar casi todo lo que hay además del USDC (377 M$) son otras emisiones que DefiLlama no detalla aquí [VERIFICAR]. USDT, la mayor, **no tiene presencia relevante en ninguna de las dos** (0 en el agregador).
- **Papel de XRP / XLM:** XRPL tiene DEX nativo y puede usar XRP como activo puente; Stellar tiene pagos por ruta (path payments) pero **su documentación oficial sobre XLM solo describe comisiones, reserva y alquiler de contratos**, no un papel de puente ([Stellar Docs](https://developers.stellar.org/docs/learn/fundamentals/lumens)). Para XRP, la página oficial de XRPL que he leído tampoco cuantifica el uso como puente. **Cuánta liquidez real pasa por XRP o XLM no figura en ninguna fuente primaria que haya podido leer.**

## 4. Tokenización de activos reales (RWA) — rwa.xyz y DefiLlama
| Cadena | RWA distribuidos (rwa.xyz, 9-oct) | RWA representados | % de distribuidos (cálculo mío) |
|---|---|---|---|
| Ethereum | 16.880 M$ | 98 M$ | 43,2 % |
| BNB Chain | 5.810 M$ | — | 14,9 % |
| Solana | 4.370 M$ | 126 M$ | 11,2 % |
| **Stellar** | **3.580 M$** | 78 M$ | **9,2 %** |
| Avalanche | 1.720 M$ | 11.400 M$ | 4,4 % |
| Liquid Network | 1.550 M$ | — | 4,0 % |
| Arbitrum | 931 M$ | 26 M$ | 2,4 % |
| **XRPL** | **499 M$** | **4.540 M$** | **1,3 %** |
| Total (39 redes) | 39.070 M$ | 351.970 M$ | |
- **Distribuido vs. representado:** "distribuido" = token que se mueve y se tiene en la cadena; "representado" = registro en la cadena de un activo que vive fuera (definición de rwa.xyz). El 90 % del valor "total" de XRPL es representado. Un artículo secundario (KuCoin/Yahoo) atribuye más de la mitad a tokens de un solo emisor (Justoken JMWH, energía) [VERIFICAR; secundaria].
- **Canton, Hedera, Algorand:** Canton no figura entre las 10 primeras de rwa.xyz; DefiLlama no la clasifica en su categoría RWA por TVL (12,7 M$ de TVL total). Que los volúmenes de Canton existan (repo) **no implica** que aparezcan como "RWA distribuidos" en este agregador; la métrica de repo de Broadridge es otra [VERIFICAR].
- **Discrepancia entre agregadores:** DefiLlama (categoría RWA, TVL en protocolos) da a Stellar solo ~7 M$ y a XRPL 0; rwa.xyz da 3.580 M$ y 499 M$. **Cada agregador mide cosas distintas; no se pueden sumar ni comparar.**
- **Concentración en Stellar:** dossier 3 (Spiko ≈ 39 %, cinco emisores ≈ 93 %, datos de agosto).

## 5. Ventajas y desventajas técnicas (solo hechos)
| Aspecto | XRPL | Stellar | Solana | Ethereum/L2 | Tron | Canton |
|---|---|---|---|---|---|---|
| **Cierre de bloque (medido hoy)** | ~3-4 s (15 ledgers: 59 s entre cierre primero y último) | **5,0 s** (40 ledgers) | 0,2 s por slot; finalidad actual ≈12,8 s (solana.com) | L1 ≈12 s; L2 más rápidos [VERIFICAR] | ~3 s [VERIFICAR] | No público |
| **Rendimiento observado hoy** | **~39 tx/s** (2.285 tx, incl. fallidas) | **~47 tx/s** (9.183 tx, 15.037 operaciones) | **4.943 tx/s totales, 1.868 no-votos** | — | — | — |
| **Comisión base** | 0,00001 XRP (leído en el ledger, `base_fee_xrp`) | 100 stroops; p90 se encarece (17.380 stroops en horas punta) | Fracciones de céntimo [VERIFICAR] | Variable | Variable (energía/ancho de banda) | No público |
| **Descentralización** | UNL de 35 validadores publicados por Ripple (vl.ripple.com) | Validadores de nivel 1 definidos por la red (SCP) | Votos on-chain hoy; gran número de validadores | Miles de validadores | 27 super-representantes [VERIFICAR] | Permisos; validadores con privacidad |
| **Cumplimiento / permisos** | **Credenciales, dominios con permisos y DEX con permisos: ACTIVOS** (comprobado en el ledger: `Credentials`, `PermissionedDomains`, `PermissionedDEX`, `TokenEscrow`, `MPTokensV1`, `BatchV1_1`, `DeepFreeze` = true) | Congelar/recuperar activos y autorizaciones por trustline; protocolo 29 | Token extensions (opcional) [VERIFICAR] | Estándares ERC-3643, etc. | Depende del emisor (USDT congela) | Privacidad por contrato y permisos |
| **Lo que NO está activo** | `LendingProtocol`, `SingleAssetVault`: **no activados** en el ledger | — | Alpenglow no activado (votos siguen en bloques) | — | — | — |

- **Cifras de muestra:** son 15 ledgers de XRPL y 40 de Stellar el 9-oct (un minuto aproximado); **no son medias anuales**. En XRPL solo **1.018 de 2.285 transacciones tuvieron éxito** (`tesSUCCESS`) y **sólo 584 fueron Pagos** (26 %); 1.078 fueron ofertas del DEX (47 %). Muchos fallos son típicos de bots de mercado que cobran la tasa de red. **No es "volumen de pagos"**.
- **En Solana, ~62 % de las transacciones son votos de validadores** (cálculo mío: (4.943−1.868)/4.943), coherente con que Alpenglow (que los elimina) **aún no está activo**.
- **TPS teórica:** no usar. Tempo (secundaria) cita 20.000 TPS en pruebas; Hedera, "2.400 TPS" en un resumen secundario; ninguno verificado en cadena por mí.
- **Protocolo y versiones leídas:** XRPL rippled 3.4.1 (ledger 107.547.113); Stellar protocolo 29, Horizon 29.0.0 (ledger 64.859.020).

## 6. Adopción real medible: lo que dicen y lo que se puede comprobar
| Proyecto | Cifra que publica | ¿Verificable en cadena? | Estado |
|---|---|---|---|
| **Ripple (XRPL)** | >100.000 M$ acumulados en Ripple Payments (3-mar-2026, primaria) | No (mezcla métodos; ver dossier 6) | No verificable |
| **Stellar** | 11.400 M$ de volumen de stablecoins en Q2-2026 (+72 %), 10,7 M de cuentas | Parcial: Horizon permite contar operaciones, **no** distingue qué es "volumen de pago real" [VERIFICAR] | Cifra propia, promocional |
| **Solana** | Alpenglow "Q3 2026", finalidad ~150 ms (solana.com) | Sí, la finalidad se puede medir; **hoy no cumple** | Retrasada [VERIFICAR] |
| **Visa** | >20.000 M$ anualizados de liquidación con stablecoins, >15× interanual, >160 programas de tarjeta (8-sep-2026; vía The Block, sin enlace al comunicado) | No (liquidación entre Visa y bancos, no pública) | Cifra propia; run rate, no acumulado. Cadenas del piloto: Ethereum, Solana, Stellar, Avalanche + Base, Polygon, Canton, Arc, Tempo (secundaria, abr-2026) [VERIFICAR] |
| **Mastercard** | Liquidación con USDC, PYUSD, USDG, USDP, RLUSD, SoFiUSD en Ethereum, Solana, Polygon, Base, Arbitrum, Canton, Tempo y XRPL (3-jun-2026); sin volúmenes publicados. Compra de BVNK cerrada el 3-ago-2026 (hasta 1.800 M$, secundaria) | No | Alcance anunciado, sin volúmenes |
| **Kinexys (J.P. Morgan)** | >3 billones de $ desde el inicio; >7.000 M$ de media diaria (web oficial, "datos propios 2025") | No (red interna/Base para JPMD) | Cifra propia y datada 2025 |
| **DTCC / Canton** | 15-jul-2026: operaciones reales de producción con activos tokenizados de DTC (Canton y Besu) con más de 30 firmas; **lanzamiento del servicio: oct-2026**; sin volúmenes | Parcial (Canton es privada) | Primaria (DTCC), sin cifras |
| **Broadridge DLR** | ≈350.000 M$/día de repo (ago-2026, cifra de Broadridge vía prensa) | No | **No es de Canton** (Broadridge es la plataforma); Genfinity es secundaria y entusiasta |
| **Swift ledger** | 17 bancos, jul-2026 | No | Piloto (dossier 6) |
| **Pontes (BCE)** | Lanzamiento 21-sep-2026, 13 entidades (secundaria) | No (T2) | Dossier 6 |
| **Tron/Tether** | USDT en Tron ≈ 92.380 M$ (DefiLlama) y 2,1 billones de $ de transferencias de stablecoins en Q2 (cifra de Tron vía prensa) | Sí en el saldo de USDT; las transferencias incluyen movimientos entre exchanges y bots | Es la red de uso real más grande de USDT |
- **Alianzas sin contrato público:** "Visa en Stellar", "Mastercard en XRPL" y "DTCC" son **anuncios de soporte técnico**; ningún comunicado leído da volumen por cadena. Para XRPL y Stellar, **no puedo cuantificar cuánto de los 20.000 M$ de Visa o del servicio de Mastercard pasa por ellas**.

## 7. Caso favorable y desfavorable por competidor (sin recomendar)
| Frente a… | Caso favorable (XRP / XLM) | Caso desfavorable |
|---|---|---|
| **Solana** | XRPL y Stellar son más sencillas y ya ofrecen DEX, anclajes y herramientas de cumplimiento; Solana depende de Alpenglow, aún sin activar | Solana mueve ~1.900 tx/s sin votos y 6.800 M$ de USDC; mucho más ecosistema y liquidez |
| **Ethereum y L2** | Comisiones y tiempo de cierre estables y bajos; XRPL tiene permisos nativos | Ethereum: 48 % de las stablecoins y 43 % de los RWA distribuidos; Base y Arbitrum ya son rails de bancos (JPMD en Base) |
| **Tron** | RLUSD y USDC regulados con auditorías; Tether sigue siendo opaco para algunos reguladores [VERIFICAR] | Tron mueve más USDT (≈50 % del total) y es el uso real de pagos en mercados emergentes |
| **Hedera / Algorand** | XRPL y Stellar tienen unas 15-20 veces más stablecoins (cálculo mío: 1.212/63 y 941/48) | Ambas tienen consejos o apoyo corporativo (Hedera: 31 miembros según secundaria) |
| **Canton** | Públicas y verificables en cadena | Privacidad, DTCC y Broadridge. Canton es el favorito de infraestructura de Wall Street |
| **Swift / Pontes / Kinexys** | Podrían ser clientes, no competidores (Swift dice que orquestará redes públicas y privadas; Mastercard ya soporta XRPL) | Los bancos usan depósitos tokenizados, no stablecoins ni XRP/XLM; liquidar en dinero de banco central (Pontes) sustituye al activo puente |
| **Visa / Mastercard** | Ambas anuncian XRPL (Mastercard) o Stellar (Visa) como cadenas | El activo que se mueve es la stablecoin, no XRP/XLM; sin volumen por cadena |
| **Stripe Tempo / Circle Arc** | Aún sin masa crítica | Respaldadas por Visa, Stripe y Circle; cadenas nuevas hechas para pagos |

## 8. Qué datos tendrían que cambiar (señales a vigilar)
| Señal | Se inclina a favor de XRPL/Stellar si… | Se inclina en contra si… | Dónde mirar |
|---|---|---|---|
| RLUSD/USDC en cada cadena | RLUSD supera 2.000 M$ en XRPL; USDC en Stellar > 1.000 M$ | Se estancan frente a Solana/Base | DefiLlama (stablecoins) |
| RWA distribuidos | Stellar mantiene > 9 % con menos concentración; XRPL sube de 499 M$ a >1.500 M$ | Spiko u otros emisores se van | rwa.xyz |
| DTCC | Activos de DTC en Stellar (1S-2027) en producción | Solo en Canton | dtcc.com, stellar.org |
| Mastercard/Visa | Publican volumen por cadena con XRPL/Stellar > 5 % | Quedan como "soporte" sin volumen | Notas de prensa |
| Actividad en cadena | Más **pagos** (no ofertas del DEX) y menos fallos en XRPL | Predominan ofertas/bots y fallos | Nodos públicos (script de este dossier) |
| Bancos | Swift/Pontes interoperan con XRPL/Stellar | Se cierran en redes con permisos | Swift, BCE |
| Solana Alpenglow | Se retrasa de forma continuada | Se activa y baja la ventaja de velocidad | solana.com/upgrades |
| Regulación | CLARITY (dossier 1) incluye a XRP/XLM como commodities digitales | Se estanca | congress.gov |

## 9. Propuesta para `eventos/calendario.toml` (NO añadida)
| Fecha | Evento | Impacto | Aproximada | Fuente |
|---|---|---|---|---|
| 2026-10-31 | DTCC: lanzamiento del servicio de tokenización en Canton (previsto "octubre de 2026") | medio | **sí** (mes, sin día) | https://www.dtcc.com/news/2026/july/15/dtcc-turns-tokenization-into-reality |
| 2026-12-31 | Solana: activación de Alpenglow (objetivo declarado: "Q3 2026"; ya incumplido, nuevo plazo sin fecha) | bajo | **sí** | https://solana.com/upgrades/alpenglow |
| 2027-06-30 | DTCC: activos de DTC en Stellar (1S-2027) | medio | **sí** | ya en predicción 11 |
(Pontes 24/7 y Appia 2028 ya están en predicciones 14 y 35.)

## 10. Escenarios [ESPECULACIÓN]
| Escenario | Qué pasaría | Señales |
|---|---|---|
| **A. Convivencia** | Bancos y empresas de pagos usan varias cadenas; XRPL/Stellar captan nichos (RLUSD, RWA, anclajes) | Mastercard/Visa publican volúmenes en XRPL/Stellar |
| **B. Ethereum + Tron + Solana absorben** | La liquidez de stablecoins se concentra | USDT/USDC > 95 % fuera de XRPL/Stellar |
| **C. Redes de bancos absorben el flujo** | Depósitos tokenizados y Pontes sustituyen a activos puente | Swift/Pontes en producción masiva |

## 11. Lo que no sé
- Qué parte de la liquidez de XRPL/Stellar pasa por XRP/XLM como puente (sin dato oficial).
- Los volúmenes de Visa y Mastercard por cadena, y el comunicado original de Visa (no pude abrirlo; solo vía The Block).
- La composición exacta de los 4.540 M$ representados de XRPL en rwa.xyz (página muy pesada; no se pudo abrir) [VERIFICAR].
- Si Alpenglow está activo o retrasado (la señal de los votos es una inferencia mía).
- Datos oficiales de Hedera, Algorand y Tron (solo agregadores y prensa); estado actual de Arc y Tempo.
- Mis medidas de rendimiento son una muestra de ~1 min; hay que repetirlas varios días.
