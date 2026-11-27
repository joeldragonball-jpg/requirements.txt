# Pagos transfronterizos y CBDC: estado a 27-nov-2026

Método: búsquedas web (resúmenes de un buscador) y lectura directa solo de chain.link/blog/sibos-2026-recap. swift.com devolvió 403 (anotado, no evitado); docs.chain.link/ccip/directory/mainnet devolvió 404. Casi todo lo de abajo viene de resúmenes de buscador, no de la página oficial leída: por defecto es [S] hasta cotejar. Sin recomendaciones.

Etiquetas: [P] primaria oficial citada por el buscador · [D] dato de tercero · [S] secundaria · [VERIFICAR] · [ESPECULACIÓN].
Columna "Últ. 30 días" = desde 28-oct-2026.

## Resumen (producción / piloto / anuncio)

| Tema | Estado | Fecha clave | Cambio últ. 30 días |
|---|---|---|---|
| Swift ledger (Consensys/Besu) | Piloto en vivo controlado con 17 bancos (tokenised deposits) | Prensa Swift 9-jul-2026 | Nada nuevo hallado [VERIFICAR] |
| mBridge | Operativo entre China, HK, Tailandia, EAU; BIS salió en 2024; Arabia Saudí salió | FT 20-sep-2026 (salida de SAMA) | No hallado |
| BIS Agorá | Prototipo concluido; pruebas con valor real siguen | Informe final 27-may-2026 | No hallado |
| Euro digital | Legislación en trílogo; sin emisión | Pleno PE 9-jul-2026; trílogo 18-nov | Sí: trílogos 5 y 18-nov; resultado no confirmado |
| e-CNY / CIPS | CIPS en producción; e-CNY transfronterizo en fase de pruebas | Centro e-CNY Internacional, 26 instituciones, jun-2026 | No hallado |
| Nexus | Pre-producción; operador técnico nombrado | Go-live objetivo 2027 | No hallado |
| Ripple / RLUSD | Producción | >2.000 M$ de capitalización RLUSD (anuncio 25-ago-2026) | Oct: custodia RLUSD en Standard Chartered Dubai, solicitud de licencia bancaria OCC |
| Stellar / MoneyGram | Producción (rampa de efectivo); upgrade de protocolo en votación | Meridian 2026, 17-nov | Sí: integración Movantis; votación mainnet Protocolo 30 el 23-nov |
| Chainlink CCIP | CCIP 2.0 en producción; Canton añadido | 28-sep-2026 (2.0); 14-jul-2026 (Canton) | No hallado |
| DTCC / Canton | Servicio de Tokenización en producción limitada | 28-oct-2026 | Sí: lanzamiento 28-oct (borde de la ventana de 30 días) |

## 1. Swift: ledger compartido con Consensys (ISO 20022)
HECHOS:
- Anunciado en sept-2025 como prototipo conceptual de Consensys; primer caso de uso, pagos 24/7 con depósitos tokenizados. [S] (theblock.co, swift.com/insights/news/swift-add-blockchain-based-ledger)
- Marzo-2026: Swift dijo que la fase de diseño estaba cerrada y planeaba MVP con transacciones reales en 2026. [S]
- 9-jul-2026: nota de prensa de Swift «ledger listo para uso inicial»; 17 bancos pilotan transacciones reales con depósitos tokenizados. Bancos citados en la web de Swift: ANZ, BNP Paribas, BNY, Citi, DBS, First Abu Dhabi Bank, FirstRand, HSBC, Itaú Unibanco, Lloyds, Mashreq, MUFG, OCBC, Standard Chartered, UBS, UOB, Wells Fargo. [P vía buscador] https://www.swift.com/news-events/press-releases/swifts-blockchain-ledger-ready-use-17-banks-set-pioneer-tokenised-cross-border-payments-trusted-global-infrastructure
- Arquitectura: capa de orquestación sobre depósitos tokenizados de cada banco; la liquidación sigue fuera del ledger; base EVM-compatible sobre Hyperledger Besu. [P vía buscador]
- Sibos 28-sep-2026: Chainlink anuncia acceso al ledger de Swift vía CRE con modelo de autofirma; estado de producción no especificado. [S] https://chain.link/blog/sibos-2026-recap
ESTADO: piloto en vivo controlado, no producción general. Un titular de KuCoin dice «operación en vivo»; va por delante de Swift. [S]
Últ. 30 días: no hallé novedades ni volúmenes. [VERIFICAR]

## 2. mBridge
HECHOS:
- Volumen acumulado ~55.500 M$, con e-CNY ~95 % (Atlantic Council vía The Block/Reuters, 17-ene-2026). [S] https://www.theblock.co/news/ecosystems/2026-01-17-china-led-cross-border-cbdc-platform-mbridge-surges-past-55-billion-in-transaction-volume-reuters-386057 Dato de enero: probablemente desfasado.
- El BIS dejó el proyecto (2024) y figura como «concluido». [P vía buscador] https://www.bis.org/project/mbridge (no leído)
- FT, 20-sep-2026: Arabia Saudí (SAMA) se retiró, al parecer en mayo-2025, tras la prueba de concepto. [S] https://www.businesstoday.in/world/story/saudi-arabia-exits-china-backed-mbridge-platform-amid-governance-and-compliance-concerns-556677-2026-09-20
- Miembros restantes: China, Hong Kong, Tailandia, EAU. [S] Un agregador dice que Macao se unió en 2026: sin confirmar [VERIFICAR].
Últ. 30 días: nada hallado.

## 3. BIS Proyecto Agorá
HECHOS:
- Informe final 27-may-2026: liquidación atómica transfronteriza mayorista con reservas de banco central tokenizadas y depósitos tokenizados; finalidad jurídica viable en las 7 jurisdicciones; pruebas con valor real usando ISO 20022 (pacs.008, pacs.009, camt.053). [P vía buscador] https://www.bis.org/press/p260527.htm · https://www.bis.org/publ/othp110.pdf (PDF no abierto)
- Siguiente paso: más pruebas, incluyendo transacciones con valor real en ciertas monedas y participantes. Participan BoE, NY Fed, BoJ, SNB, >40 empresas; se unió el Banco de Canadá. [P vía buscador]
ESTADO: prototipo/piloto concluido; no producción. Últ. 30 días: nada hallado.

## 4. Euro digital (calendario BCE y UE)
HECHOS:
- Consejo adoptó su mandato el 19-dic-2025. [S] eunews.it
- Comisión ECON del PE aprobó su posición el 23-jun-2026 (43-14-1); pleno el 9-jul-2026 (416-169-22); trílogos desde el 13-jul. [S/P vía buscador] https://www.eunews.it/en/2026/07/09/digital-euro-parliament-says-yes-inter-institutional-negotiations-to-start-on-13-july/
- 10-nov-2026: Cipollone (BCE) pidió ante ECON adoptar el reglamento antes de fin de año; sin reglamento el BCE no fija fecha de emisión. [S] lovguiden.dk
- Ronda del 5-nov sin acuerdo anunciado; trílogo del 18-nov descrito como decisivo; puntos abiertos: topes de comisiones a comerciantes y límites de tenencia offline. [S] https://borncity.com/news/digitaler-euro-trilog-am-18-november-koennte-entscheidend-werden/
- Calendario BCE si se aprueba en 2026: piloto de 12 meses desde 2.ª mitad de 2027, emisión plena 2029. [S]
- Aprobar el reglamento no obliga a emitir: el BCE decidirá después. [S]
ESTADO: anuncio/legislación; nada en producción. Resultado del 18-nov NO confirmado: [VERIFICAR] en consilium.europa.eu, europarl.europa.eu y ecb.europa.eu/euro/digital_euro.

## 5. Yuan digital y CIPS
HECHOS:
- CIPS 2024: 175 billones de yuanes (+43 %). [S] Shanghai.gov.cn. 2025: ~180 billones de yuanes (~26 billones de $), 1.766 participantes; otra fuente 25,55 billones de $ y 8,44 M de operaciones: las cifras discrepan, sin comunicado oficial del PBoC/CIPS visto. [D/VERIFICAR]
- Récord diario 1,22 billones de yuanes (abr-2026). [S] China Daily. Media diaria ~680.000 M yuanes (2025) a ~830.000 M (jun-2026). [S]
- PIIE (2026): el volumen de CIPS fue casi plano desde mediados de 2024 y CHATS/Swift perdieron cuota en yuanes: panorama mixto. [S] https://www.piie.com/blogs/realtime-economics/2026/has-chinese-yuans-rise-global-usage-hit-wall
- Centro Internacional e-CNY (Shanghai) abrió en sept-2025; jun-2026: 26 instituciones directas y plataforma CBETS. [S] https://en.people.cn/n3/2026/0617/c90000-20468089.html
- BOFIT: el e-CNY sigue en fase piloto en lo doméstico y las aplicaciones internacionales siguen en pruebas. [S]
- No hallé volúmenes del e-CNY transfronterizo fuera de mBridge. [VERIFICAR]
Últ. 30 días: nada hallado.

## 6. Project Nexus
HECHOS: BIS lo traspasó a Nexus Global Payments (fundada mar-2025); socios fundadores India, Malasia, Filipinas, Singapur, Tailandia; Indonesia se unió como sexto banco central. Operador técnico: JV PayNet–NETS (nota 9-feb-2026). Go-live objetivo: 2027 (coberturas antiguas decían 2026). [S] https://www.businesswire.com/news/home/20260209818123/en/ · https://www.bis.org/project/nexus
ESTADO: pre-producción. Últ. 30 días: nada hallado.

## 7. Ripple / RLUSD y corredores
HECHOS:
- RLUSD >2.000 M$ de capitalización (anuncio de Ripple 25-ago-2026 según KuCoin; ~1.000 M$ en XRPL). [S] https://www.kucoin.com/blog/ph-ripple-rlusd-2-billion-xrp-ledger-liquidity Cifra actual: [VERIFICAR] en CoinGecko.
- Oct-2026: Standard Chartered Dubai ofrece custodia institucional de RLUSD en XRPL; DriveWealth integra RLUSD; Ripple solicitó licencia bancaria nacional al OCC (fecha exacta sin confirmar). [S] https://www.fxstreet.com/cryptocurrencies/news/busy-week-for-ripples-rlusd-what-changes-for-stablecoin-holders-202610160733
- Ripple dice que XRP sirve de puente en corredores de baja liquidez; en corredores líquidos RLUSD cubre la función. [P] ripple.com/insights. Ripple Payments: «>100.000 M$ en >60 mercados» (cifra de tercero, [VERIFICAR]).
OPINIÓN: hay quien argumenta que RLUSD y XRP no compiten directamente (cryptoslate/fxstreet). [ESPECULACIÓN]
ESTADO: producción (pagos, custodia); licencia OCC = solicitud, no concedida.

## 8. Stellar (MoneyGram, USDC)
HECHOS:
- Rampa MoneyGram–USDC en Stellar desde 2021 (producción). [P] https://stellar.org/blog/foundation-news/three-years-with-moneygram
- MGUSD (stablecoin de MoneyGram emitida por Bridge en Stellar) lanzada el 2-jun-2026 según un explicador: [VERIFICAR] con MoneyGram/Stellar.
- 16-nov-2026: Solflare permite retirar USDC de Solana como efectivo en MoneyGram (>170 mercados, 0 $ hasta 31-dic-2026). Es Solana, no Stellar. [S] https://bitcoinworld.co.in/solflare-moneygram-usdc-cash-withdrawals/
- 17-nov-2026 (Meridian): Movantis integra Stellar, empezando con EE. UU.–El Salvador; nota patrocinada. [S] https://chainwire.org/2026/11/17/movantis-integrates-with-the-stellar-network-to-expand-its-cross-border-payments-infrastructure/
- Protocolo 30 «Bell»: votación testnet 3-nov, mainnet 23-nov. Resultado no hallado. [VERIFICAR] [S] mitrade.com
- Bermudas on-chain y desembolso de renta básica (USDM1): anuncios de stellar.org sin fecha visible. [VERIFICAR]
Últ. 30 días: Meridian/Movantis, Solflare/MoneyGram, votación P30.

## 9. Chainlink CCIP
HECHOS:
- CCIP 2.0 «oficialmente en vivo» el 28-sep-2026 (Sibos). [P/S] https://chain.link/blog/sibos-2026-recap
- Canton añadido a CCIP el 14-jul-2026 (interop con Ethereum). [P vía buscador] https://dev.chain.link/changelog/ccip-on-canton
- Fulcrum (repo/colateral multi-cadena) demostrado con DTCC; no confirmado en vivo. DTCC Collateral AppChain: planificado. [S]
- Lista de redes soportadas: NO obtenida (docs.chain.link/ccip/directory/mainnet dio 404). Una guía de terceros dice «>50 cadenas»; sin verificar. [VERIFICAR] en https://docs.chain.link/ccip/directory
Últ. 30 días: nada hallado.

## 10. Canton / DTCC
HECHOS:
- DTCC y Digital Asset anunciaron el 17-dic-2025 tokenizar Treasuries custodiados en DTC sobre Canton. [P] https://www.dtcc.com/news/2025/december/17/dtcc-and-digital-asset-partner-to-tokenize-dtc-custodied-us-treasury-securities
- 15-jul-2026: piloto con >30 firmas (colateral, préstamo de valores, repo DvP). [P vía buscador] https://www.dtcc.com/news/2026/july/15/dtcc-turns-tokenization-into-reality
- 28-oct-2026: lanzamiento del DTCC Tokenization Service con ~20 firmas y 34 valores (acciones Russell 1000, ETF, Treasuries), en Canton y la red Besu privada de DTCC; más redes en 2027. [S] https://cryptobriefing.com/dtcc-launches-tokenization-service-150-firms/ La cifra «~30 billones de $ elegibles» es de un solo medio y sin confirmar.
ESTADO: producción limitada (controlada). Últ. 30 días: lanzamiento del 28-oct.

## Qué cambió en los últimos 30 días (28-oct a 27-nov)
- DTCC Tokenization Service en producción (28-oct). [S]
- Euro digital: trílogos del 5 y 18-nov; sin acuerdo confirmado en lo hallado. Cipollone, 10-nov: urge adoptar antes de fin de año. [S]
- Stellar: Meridian y Movantis (17-nov); Solflare/MoneyGram (16-nov, Solana); votación mainnet P30 (23-nov). [S]
- Ripple: noticias de oct (custodia StanChart Dubai, DriveWealth, solicitud OCC); nada de noviembre hallado.
- Swift, mBridge, Agorá, Nexus, CCIP, CIPS: nada nuevo localizado (ausencia de hallazgo, no prueba de ausencia).

## Sesgos y lectura
- Gran parte del material es de promotores (Chainlink, Canton, Ripple, Movantis); los titulares de «en vivo» a menudo adelantan a la fuente oficial (caso Swift/KuCoin).
- Sin recomendaciones. Cómo esto cambie la tesis es decisión de Joel (se mantiene en privado/).

## Lista de [VERIFICAR]
1. Resultado del trílogo del euro digital del 18-nov (Consejo/PE/BCE) y si hay fecha de voto final.
2. Swift: leer la nota oficial del 9-jul (swift.com dio 403 al fetch; probar con Chrome según ACCESOS-CHROME) y buscar novedades de oct-nov: volúmenes, bancos nuevos, fecha de producción general.
3. Lista y número de redes de CCIP en docs.chain.link/ccip/directory (la URL probada dio 404; buscar la ruta vigente con Chrome).
4. Fecha y texto de la solicitud de licencia OCC de Ripple, y capitalización actual de RLUSD (CoinGecko/Ripple).
5. Volumen de CIPS 2025 y 2026: comunicado oficial de CIPS/PBoC (hay cifras divergentes).
6. mBridge: miembros actuales (Macao), volumen 2026 más reciente; confirmar salida saudí en bis.org o FT.
7. MGUSD (2-jun-2026), Bermudas y UBI en Stellar: fecha y fuente oficial; resultado de la votación P30 del 23-nov.
8. Cifra «~30 billones de $» y número de firmas del DTCC Tokenization Service en dtcc.com.
9. Agorá: leer el PDF othp110 para el calendario de pruebas con valor real.
10. Nexus: confirmar go-live 2027 y miembros en nexusglobalpayments.org.
