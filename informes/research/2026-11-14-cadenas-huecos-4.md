# Cadenas: cuarta pasada de huecos (14-nov-2026)

Solo se editó `explorador/cadenas.json`. Todas las fuentes se leyeron como texto (curl con las páginas oficiales; Chrome solo para Quant).

## Resultado
- Celdas sin dato: 37 → 26 (11 cerradas). Celdas en [VERIFICAR]: 13 → 10 (3 pasan a P). `revisar_explorador.py`: 0 avisos.

## Celdas nuevas o subidas a P (todas parte interesada: documentación propia)
| Red | Celda | Hecho | Fuente |
|---|---|---|---|
| XDC | seguridad (V→P) | masternodes con KYC y 10 M XDC; no se confirmó el nº de nodos activos | docs.xdc.network/xdcchain/developers/node_operators/masternode/ |
| XDC | rendimiento | rewards a masternodes y delegadores (doc «WIP»; sin tasa) | docs.xdc.network/xdcchain/rewards/ |
| Algorand | seguridad (V→P) | PPoS con comités VRF | dev.algorand.co/concepts/protocol/staking-rewards/ |
| Algorand | rendimiento (V→P) | 50 % de comisiones al proponente + bono decreciente dotado por la Fundación | idem |
| Algorand | pagos | comisión mínima 0,001 ALGO | dev.algorand.co/concepts/transactions/fees/ |
| Avalanche | cumplimiento | cada L1 puede exigir KYC/AML, ubicación o licencia a validadores | build.avax.network/docs/avalanche-l1s |
| Avalanche | rendimiento | mín. 2.000 AVAX validar, 25 AVAX delegar, delegación mín. 2 % | .../validate/how-to-stake |
| Avalanche | interop | ICM/Warp desde mar-2024 e ICTT | build.avax.network/docs/cross-chain |
| Chainlink | seguridad | 16 operadores en el verificador por defecto de CCIP | docs.chain.link/ccip/concepts/architecture/overview |
| IOTA | pagos | gas pagado en IOTA (sin cifras) | docs.iota.org/about-iota/tokenomics/iota-token |
| Hedera | interop | docs listan CCIP, LayerZero, USDT0 (índice; nivel P, sin uso medido) | docs.hedera.com/hedera/evm/integrations/cross-chain/index |
| Polygon | interop | Agglayer con pruebas pesimistas | docs.agglayer.dev |
| Plume | cumplimiento | OFAC/AML con analítica (no es KYC de usuarios) | docs.plume.org/plume-security/compliance-at-plume |
| BNB | interop (S) | guía borrador (4-jun-2025) de puente y widget | docs.bnbchain.org/bnb-smart-chain/cross-chain-bridge/ |

## Sigue faltando
- Quant: 7 celdas; quant.network/overledger da «página no encontrada» incluso en Chrome; docs.quant.network y developer.quant.network no resuelven.
- XDC: liquidez, pagos, interop, regulación; cifra de 108 masternodes y 2 s sin confirmar; Swift solo autodeclarado.
- IOTA: liquidez, activos, interop, regulación. Ondo: liquidez, pagos, regulación. Algorand: interop, regulación. BNB: cumplimiento. Avalanche: [V] en pagos. Plume: interop. Chainlink: liquidez, activos. Hedera: staking sigue [V] (página de staking no leída).
- Algunas de estas celdas (RWA.xyz, ETF) piden fuentes que bloquean lectores; el cuello es acceso.

## Avisos
- Para C263 (tesis privada): ninguno; no se escribió en privado/. Los datos nuevos son descriptivos y no establecen ranking.
- Lección: las docs de Avalanche/Algorand/Chainlink/Plume/IOTA responden a curl con User-Agent de navegador; el texto de nav ensucia, filtrar por grep.
