# XRPL y Stellar: datos on-chain, enmiendas y protocolo (27-nov-2026)

Alcance: hechos con fuente, fecha y URL. Nivel: P = primaria/oficial, D = agregador de datos o API, S = secundaria (prensa cripto). [VERIFICAR] = no contrastado con primaria. Sin recomendaciones ni tesis. Limitación: no pude abrir XRPSCAN, livenet.xrpl.org, stellar.expert ni rwa.xyz (403/404 o páginas dinámicas sin datos); varias cifras vienen de prensa que cita esas fuentes.

## 1. Enmiendas del XRPL

| Hecho | Fuente y fecha | URL | Nivel |
|---|---|---|---|
| SingleAssetVault: 29 de 35 validadores de confianza; alcanzó el umbral y empezó su cuenta atrás de 14 días; activación estimada hacia el 9-dic-2026 si el apoyo se mantiene | Crypto Economy, 26-nov (actualizado 27-nov 01:12 UTC), cita XRPL Dashboard | https://crypto-economy.com/xrpl-lending-amendments-sit-one-vote-short/ | S [VERIFICAR contra livenet.xrpl.org/amendments] |
| LendingProtocol y LendingProtocolV1_1: 28 votos cada una; faltaba 1 para los 29 que inician la cuenta atrás; sin fecha de activación | Crypto Economy, 26-nov, misma cita | idem | S [VERIFICAR] |
| Regla: más del 80 % de validadores de la UNL durante 14 días seguidos | xrpl.org, página de enmiendas conocidas | https://xrpl.org/resources/known-amendments | P |
| Foto anterior de xrpl.org (16-sep-2026): ninguna activada; SingleAssetVault 45,71 %, LendingProtocol 37,14 %, ambas introducidas en 3.1.0 | xrpl.org, snapshot 2026-09-16 | https://xrpl.org/resources/known-amendments | P (desfasada) |
| Evolución: 4-nov SingleAssetVault 21 votos, Lending 19 (el apoyo cayó por debajo del 80 % el 21-oct y reinició la cuenta atrás); 12-nov Lending 22, Vault 23; 26-nov 28/28/29 | COINTURK 4-nov; crypto.news (10-12 nov) | https://en.coin-turk.com/xrp-ledger-to-activate-security-upgrade-as-lending-protocol-vote-lags/ | S |
| fixCleanup3_4_0: 33 de 35 (94,3 %) el 4-nov, activación prevista ese día (~14:46 UTC) | COINTURK, 4-nov | idem | S [VERIFICAR si se activó] |
| Dependencia: LendingProtocolV1_1 (vaults cerrados, contabilidad de caja) es previa al despliegue de Lending según prensa | crypto.news, ~12-nov | https://crypto.news/xrpl-lending-protocol-gains-validator-support-as-vault-vote-advances/ | S [VERIFICAR] |

Lectura: el único con fecha estimada es SingleAssetVault; los de préstamos dependen de un voto más y de 14 días posteriores (como pronto, mediados/finales de diciembre; [ESPECULACIÓN]).

## 2. Stablecoins y TVL

| Hecho | Fuente y fecha | URL | Nivel |
|---|---|---|---|
| XRPL: RLUSD 732,6 M USD; USDC 4,46 M USD (suma visible ~737 M) | DefiLlama stablecoins, valores "current" (snapshot 27-nov; la página no da fecha) | https://stablecoins.llama.fi/stablecoins?includePrices=false | D |
| Stellar: USDC 335,8 M USD; PYUSD 17,9 M USD (suma visible ~353,7 M). EURC no apareció en la parte leída (solo leí 100.000 de 579.000 caracteres) | idem | idem | D [VERIFICAR EURC] |
| TVL DeFi (DefiLlama): XRPL 25-nov 29,68 M, 26-nov 30,22 M, 27-nov 31,11 M USD; Stellar 25-nov 176,64 M, 26-nov 181,10 M, 27-nov 182,48 M USD | DefiLlama historicalChainTvl, 27-nov | https://api.llama.fi/v2/historicalChainTvl/XRPL y .../Stellar | D |
| Discrepancia: prensa cita RLUSD en XRPL ~1.010 M (informe T3, 2-nov) y RLUSD cap. total 2.700 M (14-nov); DefiLlama da 732,6 M en XRPL. Diferencia probable de definición (suministro total vs. solo XRPL) | coinalertnews 2-nov y 14-nov | https://coinalertnews.com/news/2026/11/14/xrp-ledger-batch-ticket-high | S [VERIFICAR] |
| rwa.xyz: no accesible; sin cifra propia | - | - | [VERIFICAR] |

## 3. Actividad y DEX

| Hecho | Fuente y fecha | URL | Nivel |
|---|---|---|---|
| DEX nativo XRPL: volumen 24 h 7,75 M USD; 7 d 48,35 M; variación 7 d +32,5 %, 1 m +104,7 %. Sologenic 20,3 K; Yellow Onchain 2,0 K (doble conteo) | DefiLlama overview DEX, 27-nov (sin fecha en la página) | https://api.llama.fi/overview/dexs/Ripple | D |
| XRPL: 119,7 M de transacciones en 30 días hasta el 13-nov, 33,4 % batch | prensa citando XRPSCAN, 13-nov | https://coinalertnews.com/news/2026/11/14/xrp-ledger-batch-ticket-high | S [VERIFICAR en XRPSCAN] |
| Batch: máximo de noviembre 1,962 M el 3-nov (función en mainnet desde el 9-oct); Tickets 1,553 M el 7-nov | idem (Bithomp/XRPSCAN) | idem | S |
| Cuentas nuevas: 7.734-7.934 el 1-nov (fuentes difieren) | cryptobriefing / XRPSCAN, 1-nov | https://cryptobriefing.com/xrp-ledger-new-wallets-november-1/ | S |
| Cuentas activas diarias en T2: media 16.587 (-25 % interanual) | Evernorth, citado en prensa | https://cryptobriefing.com/xrp-ledger-institutional-transactions-active-accounts/ | S |
| Stellar: transacciones y cuentas activas actuales | stellar.expert no devolvió datos (página dinámica) | - | [VERIFICAR] |

## 4. Stellar: Protocolo 30 "Bell"

| Hecho | Fuente y fecha | URL | Nivel |
|---|---|---|---|
| Votación en mainnet fijada el 23-nov-2026 a las 17:00 UTC (fechas sujetas a cambio); testnet el 3-nov (activación reportada el 4-nov) | SDF, stellar.org/protocol-upgrades; plan publicado 20-oct | https://stellar.org/protocol-upgrades | P |
| Contenido: direcciones de contrato multiplexadas, comprobaciones de firma poscuántica ML-DSA en Soroban, tiempo de ledger en milisegundos | crypto.news / bitrss, oct-nov | https://crypto.news/stellar-protocol-30-bell-upgrade-goes-live-on-testnet-ahead-of-mainnet-vote/ | S |
| Validadores deben instalar Stellar Core v30.0.0 antes de la votación | prensa, oct | https://en.coinotag.com/stellar-bell-protocol-30-operator-software-requirements-november-vote | S |
| Resultado de la votación del 23-nov: NO encontrado. La lista stellar-validators solo muestra el post del 20-oct | stellar-validators (Google Groups), consulta 27-nov | https://groups.google.com/g/stellar-validators | P | [VERIFICAR] |
| Cuórum de validadores (nº, umbral): no publicado en las páginas leídas | - | - | [VERIFICAR] |

## 5. Noticias oficiales de noviembre

- Ripple: no hallé comunicado oficial fechado en noviembre de 2026. Último bloque en octubre: 26-oct aprobación final de la OCC para Ripple National Trust Bank; 27-oct ampliación con BNY; 28-oct previsión de ~900 M USD de ingresos de producto anualizados. https://ripple.com/ripple-press/ripple-reports-banner-year-approaching-900m-product-revenue-run-rate-signs-multi-solution-partnerships/ (P, oct). El comunicado de prime brokerage "3-nov" probablemente es de 2025 [VERIFICAR].
- SDF: sin comunicado de noviembre localizado salvo el calendario de Bell. Otros (Bermuda on-chain, ERC3643, inversión en Ascend) sin fecha clara: https://stellar.org/press/stellar-to-power-bermuda-s-plan-to-become-world-s-first-fully-onchain-economy (P, fecha [VERIFICAR]).

## Huecos para próxima pasada
Resultado del voto de Bell; cuórum de validadores Stellar; EURC en Stellar/XRPL; transacciones/cuentas de Stellar; rwa.xyz; livenet.xrpl.org/amendments en directo (confirmar 29/28/28 y fecha del 9-dic); XRPSCAN en directo.
