# C322 - Interconexión de cadenas con redes institucionales (a 27-nov-2026)

Alcance: XRPL, Stellar, Hedera, Canton, Solana y Ethereum frente a Chainlink CCIP, Circle CCTP, Swift (ledger compartido), DTCC, Partior, Fnality, Agorá (BIS), mBridge y Nexus. Solo hechos con fuente y fecha; sin recomendaciones ni tesis.

Niveles: P = fuente primaria leída directamente en esta sesión; S = secundaria (prensa, agregadores, resúmenes de búsqueda) [VERIFICAR]. Estados: producción / piloto / anunciado / concepto / sin evidencia.

Limitaciones: la página de redes de CCIP y el directorio de CCIP devolvieron 404, y swift.com (notas de prensa) devolvió 403 al lector. Por eso la lista oficial de redes CCIP no se pudo contrastar: la ausencia de XRPL/Stellar en CCIP es «no encontrado», no «confirmado que no existe».

## Tabla de enlaces

| # | Enlace | Estado | Fecha | Fuente / URL | Nivel |
|---|---|---|---|---|---|
| 1 | Chainlink CCIP - Canton (interoperar con Ethereum; más rutas previstas) | producción (según changelog) | 14-jul-2026 | Chainlink dev changelog: https://dev.chain.link/changelog/ccip-on-canton | P |
| 2 | Chainlink CCIP - Hedera | producción («live on mainnet») | 8-abr-2025 | Hedera blog: https://hedera.com/blog/hedera-adopts-chainlink-standard-for-cross-chain-interoperability-to-accelerate-ecosystem-adoption (cifra de cadenas accesibles inconsistente en la misma página: 46+ y 41+) | P |
| 3 | Chainlink CCIP - Stellar | anunciado (la página habla de «once completed», sin fecha ni lanzamiento) | fecha no visible | Stellar Foundation: https://stellar.org/blog/foundation-news/stellar-to-join-chainlink-scale-and-adopt-data-feeds-data-streams-and-ccip-to-power-next-gen-defi-applications | P (estado de producción: sin evidencia) [VERIFICAR] |
| 4 | Chainlink CCIP - XRPL (mainnet o sidechain EVM) | sin evidencia | - | Búsqueda sin resultados; la interoperabilidad de XRPL aparece con Axelar y Wormhole (Ripple, jun-2025: https://ripple.com/insights/ripple-expands-multichain-interoperability-infrastructure-with-wormhole/) | S [VERIFICAR] |
| 5 | Chainlink CCIP - Ethereum y Solana | [VERIFICAR] no se pudo leer la lista oficial (404). Ethereum aparece como contraparte de Canton en el enlace 1 | - | https://docs.chain.link/ccip/supported-networks (404) | - |
| 6 | Circle CCTP V2 - Ethereum (dominio 0) | producción (Standard + Fast + Forwarding) | página vigente nov-2026 | https://developers.circle.com/cctp/concepts/supported-chains-and-domains | P |
| 7 | Circle CCTP V2 - Solana (dominio 5) | producción (Standard + Fast + Forwarding) | ídem | misma URL | P |
| 8 | Circle CCTP V2 - Stellar (dominio 27) | producción (solo Standard Transfer; sin Fast, sin comisión previa, sin Forwarding Service; precisión y direcciones distintas) | ídem; fecha de alta no verificada | misma URL | P (fecha de alta [VERIFICAR]) |
| 9 | Circle CCTP - Hedera, XRPL, Canton | no listados en la página de dominios | nov-2026 | misma URL | P (ausencia en la lista) |
| 10 | Swift ledger compartido (tokenised deposits, +30 instituciones) - anuncio | anunciado | 29-sep-2025 (Sibos) | Swift: https://www.swift.com/news-events/news/swift-add-blockchain-based-ledger (no leído directamente; 403 en otras páginas de Swift) | S |
| 11 | Swift ledger - estado | piloto: 17 bancos «preparando» transacciones reales con depósitos tokenizados; actúa como capa de orquestación, no sustituye sistemas de liquidación | 9-jul-2026 (The Block); diseño completado 30-mar-2026 | https://www.theblock.co/news/ecosystems/2026-07-09-swift-launches-blockchain-ledger-for-tokenized-deposit-pilot-with-17-banks-407687 ; Swift press release (403, no leído) | S |
| 12 | Swift ledger - cadena subyacente | [VERIFICAR] fuentes discrepan: Linea (Consensys) vs Besu; Swift no la nombra en lo contrastado | 2026 | BeInCrypto / KuCoin (secundarias) | S |
| 13 | Swift - XRPL, Hedera, Stellar (ISO 20022, pruebas) | pruebas/pilotos antiguos y afirmaciones de prensa cripto; sin comunicado Swift contrastado de integración con ninguna | - | https://thepaypers.com/crypto-web3-and-cbdc/news/swift-tests-xrp-ledger-and-hederas-hashgraph-for-cross-border-payments | S [VERIFICAR] |
| 14 | DTCC Tokenization Service - lanzamiento (Canton y red privada Besu de DTCC) | producción (voluntario, 3 años, bajo carta de no acción SEC) | 28-oct-2026 | DTCC Tokenization Hub: https://www.dtcc.com/products-and-services/digital-assets/tokenization/hub ; carta SEC 11-dic-2025: https://www.sec.gov/files/tm/no-action/dtc-nal-121125.pdf | P (hub y carta); redes concretas Canton/Besu: S (The Block/Decrypt) |
| 15 | DTCC - Solana | anunciado: conexión prevista 2.º semestre 2027 | 12-nov-2026 | https://www.dtcc.com/press-releases/2026/dtcc-tokenization-service-to-connect-with-solana | P |
| 16 | DTCC - Stellar y Arc (Circle) | anunciado para 2027 según ficha de DTCC citada por Decrypt | nov-2026 | https://decrypt.co/383132/dtcc-to-bring-tokenized-stocks-and-treasuries-to-solana-in-2027 | S [VERIFICAR] (no figura en el comunicado leído) |
| 17 | DTCC - Canton (Treasuries con Digital Asset) | piloto/controlado, luego integrado en el servicio (enlace 14) | 2025-2026 | Winston & Strawn / prensa | S |
| 18 | DTCC - Hedera, XRPL, Ethereum | sin evidencia en comunicado ni hub leídos | - | - | [VERIFICAR] |
| 19 | Partior - red en vivo (USD, SGD, EUR según materiales de Partior) | producción; Emirates NBD pagos USD en tiempo real | 14-jul-2026 (comunicado en la web de Partior; otra fuente dice jun-2026) | https://partior.com/news-and-insights | S (índice leído solo vía búsqueda) [VERIFICAR] |
| 20 | Partior - OpenAssets (DvP atómico con depósitos tokenizados) | prueba de concepto | 30-jul-2026 | partior.com/news-and-insights | S |
| 21 | Partior - SOOHO.IO (Corea) | MOU | 26-ago-2026 | https://technode.global/2026/08/26/sooho-partior-korean-digital-finance-global-settlement-rails/ | S |
| 22 | Partior - cadenas públicas (XRPL, Stellar, Hedera, Solana, Ethereum) | sin evidencia; Partior se describe como ledger de consorcio bancario | - | https://frame.xyz/insights/partior-explained/ | S |
| 23 | Fnality - sistema en libras (£FnPS) | producción | dic-2023 | Blockworks (secundaria) | S |
| 24 | Fnality - sistemas USD y EUR | en desarrollo; sin fecha de lanzamiento confirmada | 10-sep-2026 | https://thecurrencyanalytics.com/regulations/fnality-adds-3-former-central-bankers-as-dollar-and-euro-systems-near-launch-292315 | S [VERIFICAR] |
| 25 | Fnality - cadenas públicas del universo | sin evidencia | - | - | [VERIFICAR] |
| 26 | BIS Agorá (tokenización de reservas y depósitos; 7 bancos centrales, +40 entidades; Banco de Canadá se ha unido después) | prototipo/informe exploratorio publicado; siguiente paso pruebas con valor real | 27-may-2026 | https://www.bis.org/press/p260527.htm | P |
| 27 | Agorá - pruebas con valor real | piloto: 28 entidades, ~800.000 CHF, jul-2026 | jul-2026 | resumen de búsqueda de prensa; no confirmado en BIS | S [VERIFICAR] |
| 28 | Agorá - cadenas públicas (XRPL, Stellar, Hedera, Solana, Ethereum) | sin evidencia; arquitectura de plataforma compartida de bancos centrales | - | BIS (enlace 26) | P (ausencia en el comunicado) |
| 29 | mBridge (China, HK, Tailandia, EAU, Arabia Saudí; BIS salió en 2024) | piloto avanzado; FT informó (14-jun-2026) de preparación para despliegue comercial | 14-jun-2026 | Financial Times vía prensa (secundaria) | S [VERIFICAR] |
| 30 | mBridge - Agorá / cadenas públicas | sin interoperabilidad encontrada («dos rieles paralelos», comentario) | 2026 | comentario secundario | S |
| 31 | BIS Nexus (pagos minoristas instantáneos entre sistemas rápidos nacionales) | anunciado; operador técnico PayNet-NETS elegido feb-2026; puesta en marcha apuntada a 2027 (antes se decía 2026) | 9-feb-2026 | https://www.bis.org/about/bisih/topics/fmis/nexus.htm (no leído directamente); https://ffnews.com/news/nexus-global-payments-appoints-technical-operator | S [VERIFICAR] |
| 32 | Nexus - cadenas públicas | no aplica por diseño: conecta sistemas nacionales de pagos, no blockchains | - | BIS Nexus | S |

## Lectura por cadena (solo hechos)

- Ethereum: CCTP V2 en producción (P); interoperable con Canton vía CCIP (P, 14-jul-2026). En la lista de DTCC leída no consta.
- Solana: CCTP V2 en producción (P); DTCC lo anuncia para 2.º semestre 2027 (P). CCIP no contrastado.
- Stellar: CCTP V2 solo Standard (P); CCIP anunciado sin estado de producción (P); DTCC 2027 (S).
- Hedera: CCIP en producción desde abr-2025 (P); no figura en CCTP ni en DTCC en lo leído.
- Canton: CCIP desde 14-jul-2026 (P); DTCC lanzado 28-oct-2026 (hub P; red concreta S). No figura en CCTP.
- XRPL: sin enlace contrastado con CCIP, CCTP, DTCC, Agorá, Partior, Fnality, mBridge ni Nexus. Sus puentes documentados son Axelar y Wormhole (S/P Ripple 2025; vigencia en nov-2026 [VERIFICAR]).

## Sesgos y cautelas

- Los comunicados de cada proyecto (Hedera, Stellar, Chainlink) son autopromoción; «live on mainnet» no indica volumen ni uso.
- La prensa cripto sobre Swift con XRPL/Hedera/Linea es la fuente menos fiable del conjunto.
- Anunciado no es producción: DTCC-Solana (2027), CCIP-Stellar, Nexus (2027), Fnality USD/EUR.
- Los resúmenes de búsqueda no son lectura directa; las filas S requieren cotejo en navegador (Chrome) antes de pasar al cerebro. Pendiente cotejar: lista oficial de redes CCIP (docs.chain.link, 404 en el lector), notas de prensa de Swift (403), novedades de Partior/Fnality, Agorá RVT.
