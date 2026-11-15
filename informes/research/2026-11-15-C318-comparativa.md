# C318 - Comparativa neutral de liquidación entre redes (medida 2026-11-15T12:11:25Z UTC)

Nivel P para las medidas (nodos públicos), S para agregadores y documentación. No es recomendación de compra/venta. Una sola instantánea: la comisión y los tx/s varían con la carga.

## Medidas (HECHOS)

| Red | Bloque medio (s) | Finalidad medida (s) | Comisión (USD) | tx/s | Stablecoins |
|---|---|---|---|---|---|
| XRPL | 3.737 | 3.737 | 0.0048232 | 35.7 | 839 M$ |
| Stellar | 5.0 | 5.0 | 0.0000014 | 107.16 | 398 M$ |
| Ethereum | 12.0 | 1056 | 0.0109390 | 21.08 | 131.392 M$ |
| Solana | 0.215 | no medible | 0.0003619 | 1225.3 | 13.913 M$ |
| Hedera | 2.169 | 2.169 | 0.0001000 | 3.59 | 26 M$ |
| Algorand | 2.737 | 2.737 | 0.0000799 | 10.04 | 121 M$ |

Precios de referencia (DefiLlama): XRP 0.9646 USD, XLM 0.1393 USD, ETH 1825 USD, SOL 72.39 USD, HBAR 0.05898 USD, ALGO 0.07985 USD.
Fuentes: s1.ripple.com, horizon.stellar.org, ethereum-rpc.publicnode.com, api.mainnet-beta.solana.com, mirror node de Hedera, algonode, coins.llama.fi. Hedera: la comisión es la tarifa documentada, no medida [VERIFICAR]. Ethereum: «finalidad» es el retraso hasta el bloque finalized. Solana: finalidad no medible con el RPC público.

## Liquidación T+0 frente a T+n

«T+0» aquí significa que la transferencia del token queda final en segundos o minutos, no que el dinero fiat del banco se mueva igual de rápido. La pata en dinero bancario (emisión y redención del token, horarios de bancos) depende del emisor y no la hace la red.

- **xrpl**: nativo: Ledger final en ~4 s (medido); libro de órdenes y AMM en el protocolo; pagos entre monedas por rutas; líneas de confianza para activos emitidos. No nativo: Entrega contra pago con dinero de banco central o cuenta bancaria; la redención de cada stablecoin la hace su emisor. (Fuente: Medida P (s1.ripple.com); funciones: documentación oficial del proyecto (no releída en esta ejecución) [VERIFICAR])
- **stellar**: nativo: Ledger final en ~5 s (medido); libro de órdenes (SDEX) y pagos por rutas con conversión entre activos en el protocolo. No nativo: La conversión de dinero bancario a token la hacen entidades emisoras o «anclas» externas. (Fuente: Medida P (horizon.stellar.org); funciones: documentación oficial del proyecto (no releída en esta ejecución) [VERIFICAR])
- **ethereum**: nativo: Inclusión en bloque cada 12 s; finalidad económica por Casper FFG tras ~15 min (medido). No nativo: Libro de órdenes, intercambio y entrega contra pago no son del protocolo: dependen de contratos inteligentes de terceros. Las redes de capa 2 no se miden aquí. (Fuente: Medida P (ethereum-rpc.publicnode.com); funciones: documentación oficial del proyecto (no releída en esta ejecución) [VERIFICAR])
- **solana**: nativo: Slot de ~0,2 s (medido); confirmaciones rápidas. No nativo: Libro de órdenes e intercambio son programas de terceros; finalidad real no medible con el RPC público (ver «lo que no sabemos»). (Fuente: Medida P (api.mainnet-beta.solana.com); funciones: documentación oficial del proyecto (no releída en esta ejecución) [VERIFICAR])
- **hedera**: nativo: Registros cada ~2 s (medido en mirror node); servicio de tokens en el protocolo. No nativo: Libro de órdenes: de terceros. (Fuente: Medida S (mirror node público); funciones: documentación oficial del proyecto (no releída en esta ejecución) [VERIFICAR])
- **algorand**: nativo: Bloque cada ~2,8 s (medido), final al certificarse; activos estándar en el protocolo. No nativo: Libro de órdenes: de terceros. (Fuente: Medida P (algonode); funciones: documentación oficial del proyecto (no releída en esta ejecución) [VERIFICAR])

## Hechos de liquidación y diversificación con fuente primaria

(explorador/pruebas-bancos.json no existía al ejecutar; se toma de cadenas.json (relaciones) y cbdc-blockchains.json, solo lectura.)

| Hecho | Fuente | Fecha | Nivel |
|---|---|---|---|
| Pontes (BCE) enlaza plataformas DLT de mercado con TARGET/T2; producción inicial desde el 21-sep-2026; volúmenes no publicados. | Página del BCE sobre Pontes, leída 29-oct-2026 (cbdc-blockchains.json) | 2026-09-21 | P |
| El DTCC Tokenization Service se lanzó el 28-oct-2026; hoy está integrado con Canton Network y con la red privada Besu de DTCC. No incluye Ethereum público, XRPL, Stellar ni Solana en producción. | DTCC, nota de prensa (dtcc.com/press-releases/2026/dtcc-tokenization-service-goes-live) | 2026-10-28 | P |
| DTCC y la Stellar Development Foundation anunciaron planes para tokenizar activos custodiados en DTC en Stellar, esperados para el primer semestre de 2027. Es plan, no producción. | DTCC, nota de prensa 27-may-2026 | 2026-05-27 | P |
| DTCC anunció planes para Solana con integración prevista en el segundo semestre de 2027. Es plan, no producción. | DTCC, nota de prensa 12-nov-2026 | 2026-11-12 | P |
| El MVP del libro mayor de Swift usa una arquitectura compatible con EVM basada en Hyperledger Besu; la página no menciona otras redes públicas. | Swift, noticia del 30-mar-2026 | 2026-03-30 | P |
| Ripple describe liquidar «en RLUSD y otras stablecoins, o en moneda fiat»; no publica qué parte del volumen se liquida con XRP, RLUSD o fiat. | Ripple, página de pagos transfronterizos (leída 14-nov-2026); parte interesada | 2026-11-14 | P |
| RLUSD figura en XRPL (~764 M$) y Ethereum (~1.900 M$) según un agregador; la propia página de RLUSD dice que se integra en XRPL, Ethereum y otras redes. | RWA.xyz (agregador, 14-nov-2026) y Ripple (página de RLUSD) | 2026-11-14 | S |
| Un mismo fondo tokenizado vive en varias redes: OUSG de Ondo en 4 (Ethereum, Polygon, Solana, XRPL); USDY en 12 (incluye Ethereum, Solana y Stellar). | Ondo, documentación de direcciones (14-nov-2026); parte interesada | 2026-11-14 | P |
| Benji (Franklin Templeton) lista contratos en 9 redes: Stellar (minorista e institucional) y, solo institucional, Ethereum, Solana y otras; el XRPL no figura en esa lista. | Franklin Templeton, web de Benji (14-nov-2026); parte interesada | 2026-11-14 | P |
| Solana: Alpenglow activo en la red principal desde el 21-oct-2026; el tiempo de slot bajó de 400 a 200 ms. | Solana Foundation, página de Alpenglow | 2026-10-21 | P |
| mBridge (consorcio de bancos centrales): ~55.500 M$ acumulados y >4.000 operaciones, ~95 % e-CNY. Cadena permisionada propia, no una red pública. | Atlantic Council vía prensa, ene-2026 (cbdc-blockchains.json) | 2026-01 | S |
| Hong Kong (Ensemble): piloto de valor real desde el 13-nov-2025; Singapur: liquidación en vivo de un préstamo interbancario con wCBDC en nov-2025; Suiza (Helvetia): piloto en producción ampliado hasta mediados de 2027. | HKMA 13-nov-2025; MAS; SNB (cbdc-blockchains.json) | 2025-11 | P |
| Ucrania: piloto de e-hryvnia sobre Stellar (dic-2021, informe ene-2023); Palau: token respaldado 1:1 en dólares sobre XRPL en 2023. Pilotos antiguos; estado actual sin verificar. | Stellar.org y NBU; Business Wire/Forkast jul-2023 (cbdc-blockchains.json) | 2023 | S |

## Puntos fuertes y flacos por red (hechos con fuente)

### XRPL
**Fuertes**
- Cierre de ledger medio de 3.737 s con ledger validado final. (s1.ripple.com, 2026-11-15T12:11:25Z; P)
- Comisión mínima ≈ 0.000010 USD por transacción (10 gotas). (s1.ripple.com método fee; precio DefiLlama; P)
- Stablecoins en la red: 839 M$ (8 stablecoins, incluye RLUSD, EURCV y AUDD). (DefiLlama y profundidad-multidivisa.json, 15-nov-2026; S)
**Flacos**
- Stablecoins 839 M$ frente a 131.392 M$ en Ethereum y 13.913 M$ en Solana. (DefiLlama, 15-nov-2026; S)
- En la muestra la comisión mediana fue 10 gotas el mínimo y 0.0048 USD la mediana del último ledger: sube con la carga o con transacciones con comisión alta. (s1.ripple.com método fee, 2026-11-15T12:11:25Z; P)
- Dos fallos corregidos en xrpld 3.4.1 (informe del 9-oct-2026); la enmienda afectada no estaba activada en la red principal. (xrpl.org, informe de vulnerabilidades 9-oct-2026; P)

### Stellar
**Fuertes**
- Ledger cada 5.0 s, final al cerrarse. (horizon.stellar.org, 2026-11-15T12:11:25Z; P)
- Comisión mediana cobrada: 0.0000100 XLM (mediana cobrada, 100 stroops) ≈ 0.0000014 USD. (Horizon fee_stats; precio DefiLlama; P)
- USDC en Stellar ≈ 345 M$ y 16 stablecoins; Benji (Franklin Templeton) lo lista con acceso minorista e institucional. (profundidad-multidivisa.json 15-nov-2026; web de Benji 14-nov-2026; S)
**Flacos**
- Stablecoins 398 M$, por debajo de Ethereum y Solana. (DefiLlama, 15-nov-2026; S)
- La integración de DTCC con Stellar es un plan para 1S-2027, no producción. (DTCC, nota de prensa 27-may-2026; P)
- Capacidad observada 107.16 tx/s en la muestra (no es el máximo del protocolo). (horizon.stellar.org, 2026-11-15T12:11:25Z; P)

### Ethereum
**Fuertes**
- Mayor volumen de stablecoins de la tabla: 131.392 M$ y 230 stablecoins. (DefiLlama y profundidad-multidivisa.json, 15-nov-2026; S)
- Presente en la lista de redes de OUSG, USDY y Benji, y en la de RLUSD. (Ondo, Franklin Templeton, Ripple (14-nov-2026); partes interesadas; P)
- Bloque cada 12 s con estado «finalized» verificable por RPC. (ethereum-rpc.publicnode.com, 2026-11-15T12:11:25Z; P)
**Flacos**
- Finalidad «finalized» a ~1056 s (~18 min) del último bloque. (ethereum-rpc.publicnode.com, 2026-11-15T12:11:25Z; P)
- Comisión de una transferencia simple ≈ 0.0109 USD en la capa 1, la más alta de la tabla en ese momento. (eth_feeHistory; precio DefiLlama; P)
- Capacidad observada 21.08 tx/s en la capa 1 (las capas 2 no se cuentan). (ethereum-rpc.publicnode.com, 2026-11-15T12:11:25Z; P)

### Solana
**Fuertes**
- Slot medio de 0.215 s. (getRecentPerformanceSamples, 2026-11-15T12:11:25Z; P)
- 1225.3 tx/s observadas en la última media hora, la cifra más alta de la tabla. (api.mainnet-beta.solana.com, 2026-11-15T12:11:25Z; P)
- Stablecoins 13.913 M$ (78 stablecoins) y comisión ≈ 0.00036 USD. (DefiLlama; getRecentPrioritizationFees; S)
**Flacos**
- La integración de DTCC con Solana es un plan para 2S-2027, no producción. (DTCC, nota de prensa 12-nov-2026; P)
- El RPC público no permite medir la finalidad real; no hay cifra medida aquí. (api.mainnet-beta.solana.com, 2026-11-15T12:11:25Z; P)
- El recuento de tx/s no separa los votos de los validadores en esta fuente. (getRecentPerformanceSamples; P)

### Hedera
**Fuertes**
- Registros cada 2.169 s (mirror node). (mirror node público, 2026-11-15T12:11:25Z; S)
**Flacos**
- La comisión (0,0001 USD) es la tarifa documentada, no una medida; stablecoins solo en cadenas-onchain.json (26 M$). (documentación de Hedera [VERIFICAR]; DefiLlama; S)

### Algorand
**Fuertes**
- Bloque cada 2.737 s, tarifa mínima ≈ 0.00008 USD. (algonode, 2026-11-15T12:11:25Z; P)
**Flacos**
- Stablecoins 121 M$; no aparece en la lista de redes de DTCC, Ondo ni Benji leídas. (DefiLlama; notas de DTCC, Ondo y Benji (14-nov-2026); S)

## Lo que NO sabemos

- Finalidad real de Solana con el RPC público: la cifra no es medible aquí y la que da el proyecto no se ha contrastado [VERIFICAR].
- Si las medidas de una sola instantánea (20 bloques, 30 min en Solana) son representativas: la comisión y los tx/s cambian con la carga.
- Qué parte de los tx/s son pagos de liquidación y cuál es actividad especulativa, de bots o de votos.
- Volumen real de liquidación de stablecoins por red (se conoce la emitida, no la movida) ni cuánto se usa para pagos entre bancos.
- Capas 2 de Ethereum y otras redes secundarias: no se han medido; la comparación es solo capa 1.
- Qué parte del volumen de Ripple Payments se liquida con XRP, RLUSD o fiat: Ripple no lo publica.
- Volúmenes de Pontes (BCE) y de los pilotos de bancos centrales: no publicados o sin verificar.
- Si los pilotos antiguos (Palau, Ucrania) siguen activos en 2026.
- Coste y riesgo de redención fiat de cada stablecoin, y horarios bancarios de la pata en dinero.
- Los tx/s de Hedera y Algorand vienen de nodos de terceros (mirror node y algonode); el nodo público puede estar limitado.

## Lectura

- HECHOS: cada red optimiza una cosa distinta (velocidad de slot, comisión, profundidad de stablecoins, funciones nativas); ninguna lidera en todas las columnas.
- OPINIÓN [ESPECULACIÓN]: no se extrae ninguna conclusión de inversión; la diversificación de emisores entre redes (Ondo, Benji, RLUSD) es un hecho de los emisores, no una predicción.

Regenerar: `python scripts/leer_comparativa.py` (conserva los bloques manuales del JSON).
