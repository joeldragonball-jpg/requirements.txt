# Dossier: Pagos transfronterizos (Ripple, Stellar, Swift, Pontes del BCE y SEPA) (9-oct-2026)

> Informativo. No es recomendación de compra ni venta. Fuentes **primarias** leídas: web del BCE (Pontes), nota de prensa del BCE (21-sep-2026), nota de prensa de Swift (9-jul-2026, vía resultados del buscador: su web bloquea la extensión de Chrome), nota de MoneyGram, balance del Q2-2026 de Stellar, nota de Ripple del 3-mar-2026 y el propio XRP Ledger. El resto es secundario. Lo no confirmado va como [VERIFICAR]; las predicciones, como [ESPECULACIÓN].

## 1. Resumen ejecutivo
1. **Las "autopistas" nuevas de pagos son de bancos y bancos centrales, no de cripto:** el BCE puso en marcha **Pontes** (21-sep-2026) para liquidar activos tokenizados en dinero de banco central; **Swift** activó su **libro mayor compartido** (9-jul-2026) con 17 bancos y **depósitos tokenizados**; la UE obliga a las **transferencias inmediatas SEPA** por ley.
2. **Ripple:** la cifra de "16 billones de dólares al año" (Garlinghouse, CNBC, jun-2026, según prensa) viene de **adquisiciones tradicionales** (Hidden Road/Ripple Prime y GTreasury/Ripple Treasury), y solo un **~0,1 %** se liquida con activos on-chain. **No es volumen de XRP.** La cifra propia de Ripple Payments es de **>100.000 M$ acumulados** (nota oficial, 3-mar-2026).
3. **RLUSD** (stablecoin de Ripple) tiene **1.140 M$ en el XRP Ledger** (leído en el ledger, 9-oct) y ~2.456 M$ en total (CoinGecko vía prensa, oct-2026): **XRPL ≈ 44 %** y Ethereum el resto (secundaria).
4. **Stellar** crece por **stablecoins**: 11.400 M$ de volumen de transferencias de stablecoins en el Q2-2026 (+72 % trimestral, cifra de la propia Stellar, tono promocional) y **MGUSD de MoneyGram** (2-jun-2026, emitido por Bridge). El papel de **XLM** como activo **no** se explica en esas fuentes.
5. **Qué implica para XRP/XLM:** el uso real (pagos) se desplaza hacia **stablecoins y depósitos tokenizados**; la demanda de XRP o XLM como activo puente **no está demostrada con datos oficiales**. Efecto directo en el precio: **no demostrado**.

## 2. Qué es cada pieza y cómo funciona
- **Ripple (ODL / Ripple Payments):** ODL usaba XRP como activo puente para evitar tener dinero parado en cuentas en el extranjero. Ripple Payments ahora es una plataforma "de extremo a extremo" con stablecoins (RLUSD), custodia (Palisade) y cuentas virtuales (Rail). Nota oficial del 3-mar-2026: **no menciona ODL ni XRP** y cita a Corpay usando RLUSD en Asia-Pacífico ([Ripple](https://ripple.com/ripple-press/ripple-redefines-payments-with-end-to-end-stablecoin-platform-and-global-customer-momentum/)).
- **Stellar:** red de pagos con stablecoins (USDC, MGUSD, otras) y anclajes de entrada/salida a efectivo; XLM paga las comisiones. Socios citados por Stellar: MoneyGram, Circle (CCTP), DTCC, Figure y otros ([Stellar Q2-2026](https://stellar.org/blog/foundation-news/q2-2026-what-stellar-was-built-for-has-arrived)).
- **Swift:** red de mensajería entre bancos. Su **libro mayor compartido** (EVM compatible, basado en Hyperledger Besu) coordina compromisos de pago entre bancos con **depósitos tokenizados** (deuda del banco, **no** stablecoins) las 24 h; la **liquidación final** sigue en los sistemas actuales. 17 bancos piloto: ANZ, BNP Paribas, BNY, Citi, DBS, FAB, FirstRand, HSBC, Itaú, Lloyds, Mashreq, MUFG, OCBC, Standard Chartered, UBS, UOB y Wells Fargo ([Swift](https://www.swift.com/news-events/press-releases/swifts-blockchain-ledger-ready-use-17-banks-set-pioneer-tokenised-cross-border-payments-trusted-global-infrastructure), nota de prensa del 9-jul-2026, vista en el buscador).
- **Pontes (BCE):** enlaza plataformas DLT de mercado con TARGET para liquidar en **dinero de banco central**; finalidad en T2; protocolo Hash-Link para entrega contra pago. **Solo entidades con acceso a T2 y operadores autorizados** ([BCE](https://www.ecb.europa.eu/paym/target/pontes/html/index.en.html)).
- **SEPA / pagos inmediatos:** el Reglamento (UE) 2024/886 obliga a las entidades a recibir y enviar transferencias inmediatas, con **igual comisión** que las normales y **verificación del beneficiario** gratuita ([BCE](https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.en.html)).

## 3. Cifras con su fuente
| Dato | Valor | Estado |
|---|---|---|
| Lanzamiento inicial de Pontes | **21-sep-2026** | **Verificado (primaria, BCE)** |
| Participantes de Pontes al inicio | 13 entidades (Deutsche Bank, Santander, Société Générale, DZ Bank, BEI, KfW, etc.) y 4 operadores DLT (Axiology, Cashlink, Clearstream, SWIAT) | **Verificado (primaria, nota del BCE vía buscador)** |
| Horario de Pontes | 08:00–16:00 CET en días hábiles; 24/7 previsto hacia **2028** | Secundaria (cryptonomist, CoinDesk) y nota del BCE ("plena implantación hacia 2028") [VERIFICAR horario en BCE] |
| Libro mayor de Swift | Activo desde **9-jul-2026**, 17 bancos, depósitos tokenizados, liquidación final en sistemas existentes | **Verificado (primaria, nota de Swift vía buscador)** |
| RLUSD en XRPL | **1.140.114.698** (objeto de obligaciones del emisor, ledger 107541076, 9-oct) | **Verificado en el ledger** (cálculo mío: el emisor es el de dominio ripple.com) |
| RLUSD total | ~2.456 M$ (oct-2026) y 2.491 M$ el 28-sep; +86 % en 2026 | Secundaria (KuCoin/CoinGecko) [VERIFICAR] |
| Ripple Payments volumen acumulado | **>100.000 M$** (3-mar-2026) | **Primaria (Ripple)**; no dice cuánto es con XRP |
| "16 billones $/año" | Hidden Road (~3 b$) + GTreasury (~13 b$); ~0,1 % on-chain | Secundaria (CNBC citado por prensa); **no es volumen de XRP** [VERIFICAR] |
| ODL "35.000 M$ en Q1-2026, +41 %" | Sin fuente de Ripple | **Dudoso** (agregadores y webs promocionales: coingabbar, openpr, 247WallSt) |
| Stellar: volumen de stablecoins | 11.400 M$ en Q2-2026 (+72 %); 10,7 M de cuentas; RWA 3.000 M$ | Primaria (Stellar) pero **promocional**; definiciones no detalladas |
| MGUSD | Lanzado el **2-jun-2026**, emisor Bridge (Stripe), con M0 y Fireblocks; en EE. UU. al inicio | Primaria (MoneyGram vía PR Newswire, resumen del buscador) |
| Euros: plazos de pagos inmediatos | Zona euro: recibir 9-ene-2025, enviar y verificación 9-oct-2025. Fuera del euro: recibir 9-abr-2027, enviar/verificación 9-jul-2027 | **Verificado (primaria, BCE)** |

## 4. Calendario
| Fecha | Qué | Fuente |
|---|---|---|
| 21-sep-2026 (hecho) | Lanzamiento inicial de Pontes | BCE |
| 9-jul-2026 (hecho) | Libro mayor de Swift, piloto de 17 bancos | Swift |
| 2-jun-2026 (hecho) | MGUSD de MoneyGram en Stellar | MoneyGram |
| 27–29-oct-2026 | Swell (Ripple): posibles anuncios de pagos | ya en calendario |
| 9-abr-2027 | Países UE fuera del euro: recibir transferencias inmediatas | BCE (primaria) |
| 9-jul-2027 | Fuera del euro: enviar transferencias inmediatas y verificar al beneficiario | BCE (primaria) |
| 2028 | Pontes 24/7 y plena implantación (previsión del BCE) | BCE / prensa |

**Propuesta para `eventos/calendario.toml` (no añadida):** 9-jul-2027, "UE: transferencias inmediatas y verificación del beneficiario fuera de la zona euro" (impacto medio, fuente BCE). Las demás ya pasaron o no tienen fecha oficial.

## 5. Riesgos [lo que dicen las fuentes]
- **Desplazamiento:** si los depósitos tokenizados de bancos (Swift) y el dinero de banco central (Pontes) resuelven la liquidez 24/7, el papel de un activo puente como XRP o XLM podría **reducirse**. Es una hipótesis, no un hecho.
- **Piloto, no producción masiva:** Swift dice que la liquidación final sigue en sistemas existentes; Pontes tiene horario limitado y 17 participantes.
- **Cifras infladas:** 16 billones de Ripple y volúmenes de ODL mezclan o no definen qué se liquida con XRP.
- **Concentración de RLUSD:** emisión por una sola empresa; reservas y dato de circulación cambian por fuente.
- **Fuente propia de Stellar:** el balance trimestral es promocional y no habla de XLM.

## 6. Escenarios [ESPECULACIÓN]
| Escenario | Qué pasaría | Señales |
|---|---|---|
| **A. Convivencia** | Bancos usan depósitos tokenizados; redes públicas (XRPL, Stellar) captan pagos con stablecoins y nichos de efectivo | Más socios de MoneyGram/Ripple; RLUSD sigue creciendo |
| **B. Los bancos absorben el flujo** | Pontes y el libro mayor de Swift se amplían a más corredores | Más bancos en Pontes; Swift pasa del piloto a producción |
| **C. Estancamiento** | Pilotos sin escala | Sin nuevos participantes en 6 meses |

## 7. Qué implica para XRP y XLM (sin consejos)
- El volumen que Ripple presume **no es de XRP**; el producto actual se apoya sobre todo en **RLUSD**. La demanda de XRP por pagos **no tiene cifra oficial** en lo que he podido leer.
- Stellar muestra más actividad en **stablecoins** (USDC, MGUSD) que en XLM; la relación entre ese volumen y el precio de XLM **no está demostrada**.
- Pontes y Swift son **competencia o complemento** según cómo evolucionen; hoy no mencionan XRP ni XLM.
- **Efecto en precio: no demostrado.** Estos días mandan macro y petróleo.

## 8. Qué vigilar
Participantes nuevos en Pontes, el paso de Swift de piloto a producción, el volumen y los socios de MGUSD, la definición de volumen en las cifras de Ripple, la cifra de RLUSD (ledger y emisor) y Swell (27–29-oct).

## 9. Lo que no sé
- La nota de Swift la he visto solo por el buscador: no pude abrir la página (permiso de la extensión) [VERIFICAR texto completo].
- Si la cifra de 16 billones la dijo Garlinghouse en CNBC con esas partes (solo fuentes secundarias).
- Cuánto del volumen de Ripple Payments usa XRP, y el volumen real de ODL.
- El horario y calendario exacto de ampliación de Pontes más allá de 2028.
- SEPA: no he mirado el Reglamento 2025/1979 ni el esquema SCT Inst del EPC; solo los plazos del BCE.
