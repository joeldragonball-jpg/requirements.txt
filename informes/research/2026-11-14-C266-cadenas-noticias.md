# C266 · Cadenas ↔ noticias: relaciones entre redes, emisores y noticias (14-nov-2026)

Informativo. No es recomendación de compra ni de venta y no compara redes para elegir una «ganadora».

## Qué se hizo
1. **Campo «cadenas» en los movimientos** (`explorador/datos.json`). Lo calcula `scripts/etiquetar_cadenas.py` solo con reglas, sin IA: busca las palabras del campo «busca» de `explorador/cadenas.json` como palabra entera en el actor, las entidades y los activos; en las noticias del bot, además, en el titular y el tema. «Swift» no etiqueta a Chainlink y «Binance» no etiqueta a BNB Chain, porque nombran a un tercero. Resultado: 52 de 225 movimientos etiquetados (XRP Ledger 32, Stellar 13, Canton 8, Solana 3, Chainlink 2, Ethereum 1). `scripts/noticias_a_orbita.py` aplica la misma regla a las noticias nuevas y `scripts/revisar_explorador.py` avisa si lo escrito no coincide con la regla.
2. **Pestaña Cadenas** (`explorador/vistas.html`): cada ficha muestra las 5 últimas noticias y hechos de esa red con su nivel P/S/V y botones a las relaciones en las que participa. Hay un bloque nuevo «Relaciones entre redes».
3. **Bloque «relaciones»** en `explorador/cadenas.json`: 5 relaciones con 21 hechos (14 [P], 3 [S] y 4 [RAZONADO]).
4. **Regla W05 de titulares con umbral**: las noticias cuyo titular dice que algo «supera», «cae por debajo de», «toca», «sube a» o «alcanza» una cifra llevan el campo `umbral: true` y una marca en la ficha que recuerda que puede ser un movimiento intradía. Hoy ninguna de las 16 noticias vigentes del bot cumple el patrón.

## Hechos leídos en el navegador (14-nov-2026)
| Hecho | Fuente | Nivel |
|---|---|---|
| El servicio de tokenización de DTC está en producción desde el 28-oct-2026, integrado con Canton y con la red privada Besu de DTCC; más redes en 2027; 20 participantes firmados | [DTCC](https://www.dtcc.com/press-releases/2026/dtcc-tokenization-service-goes-live) | P |
| DTCC y la SDF planean activos de DTC en Stellar en el 1S-2027 (27-may-2026) | [DTCC](https://www.dtcc.com/press-releases/2026/tokenization-service-to-connect-with-stellar-public-blockchain-as-dtc-advances-multi-chain-strategy) | P |
| **Nuevo:** DTCC anuncia planes para Solana, integración prevista en el 2S-2027 (12-nov-2026) | [DTCC](https://www.dtcc.com/press-releases/2026/dtcc-tokenization-service-to-connect-with-solana) | P |
| La Collateral AppChain de DTCC usará CRE y el estándar de datos de Chainlink; puesta en marcha esperada en el 4T-2026 | [DTCC](https://www.dtcc.com/news/2026/may/12/dtcc-collaborates-with-chainlink-to-advance-24-7-collateral-management) | P |
| Chainlink dice que trabaja para conectar entidades al libro mayor de Swift con CRE (28-sep-2026) | [Chainlink](https://chain.link/press-releases/chainlink-is-enabling-financial-institutions-to-connect-to-swifts-blockchain-ledger) | P, parte interesada |
| El MVP del libro mayor de Swift usa EVM sobre Hyperledger Besu; la página no nombra a Chainlink | [Swift](https://www.swift.com/insights/news/swifts-blockchain-based-shared-ledger-progresses-mvp-implementation) | P |
| Directorio CCIP: 78 redes; LINK en 65 y USDC en 22 | [Chainlink](https://docs.chain.link/ccip/directory/mainnet) | P |
| Ondo: OUSG en 4 redes y USDY en 12 | [Ondo](https://docs.ondo.finance/addresses) | P, parte interesada |
| Benji (Franklin Templeton): contratos en 9 redes; el XRP Ledger no figura | [Franklin Templeton](https://digitalassets.franklintempleton.com/benji/) | P, parte interesada |
| Ripple describe su producto de pagos con liquidación «en RLUSD y otras stablecoins, o fiat»; XRP no aparece en el texto descriptivo | [Ripple](https://ripple.com/products/cross-border-payments/) | P, parte interesada |
| RLUSD se integra «en el XRPL, Ethereum y otras redes» | [Ripple](https://ripple.com/products/stablecoin/) | P, parte interesada |
| Alpenglow activo en Solana desde la época 1064 (21-oct-2026); Rotor sin fecha | [Solana](https://solana.com/upgrades/alpenglow) | P, parte interesada |
| Glamsterdam: Sepolia el 6-oct-2026; Hoodi aplazada | [Forkcast](https://forkcast.org/upgrade/glamsterdam/) | S |
| XRPL: dos fallos corregidos en xrpld 3.4.1 (informe del 9-oct-2026) | [xrpl.org](https://xrpl.org/blog/2026/vulnerabilitydisclosurereport-bug-20261009) | P |
| XRPL: versión en que entró cada enmienda | [xrpl.org](https://xrpl.org/resources/known-amendments) | P |

## Matices y límites
- Las frases «la nota no menciona…» salen de buscar las palabras en el texto de la página, no de una lectura palabra por palabra: en `cadenas.json` se redactan como «en lo leído no se encontró».
- **Discrepancia abierta [VERIFICAR]:** RWA.xyz atribuye a Franklin Templeton Benji un activo de 192,7 M$ en el XRP Ledger, pero la web de Benji no lista esa red. Las cifras de RWA.xyz no se releyeron en esta sesión.
- DTCC en Stellar y en Solana son planes con fecha, no producción.
- El anuncio de Chainlink sobre Swift es propio; no hay confirmación de Swift en lo leído.

## Sin dato
- Importe tokenizado por red en el servicio de DTCC.
- Cuáles de las 16 redes de la página están en CCIP (la lista completa de 78 no se pudo desplegar).
- Reparto de BENJI y USDY por red según el emisor.
- Volumen de ODL en XRP y reparto del volumen de Ripple Payments por activo de liquidación.
- Incidentes o paradas de Solana y Ethereum en 2026 (no se leyó ninguna página de estado) y fecha de Glamsterdam en la red principal.
- El artículo de CoinDesk del 2-nov sobre el fallo del XRPL no se leyó: sigue como titular del bot [S].

## Lección
Una regla de etiquetado por palabras debe excluir los nombres de terceros (Swift, Binance): si no, una noticia del tercero aparece en la ficha de una red que la fuente no nombra.
