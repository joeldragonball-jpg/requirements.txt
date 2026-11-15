# C313 — Qué aporta cada red que las otras no aportan (15-nov-2026)

> Datos: `explorador/aporta-redes.json`. Información para entender cada red, no recomendación de compra o venta. No concluye qué red «gana»: cada una cubre cosas distintas y muchas cifras son instantáneas de un día. Chainlink, Ondo y Quant no son cadenas.

**Método.** Lectura de cadenas.json, comparativa-liquidacion.json, pruebas-bancos.json, empresas-redes.json, cadenas-onchain.json, cadenas-validadores.json, cadenas-incidentes.json, cadenas-gobernanza.json, profundidad-multidivisa.json y rwa-por-cadena-manual.json (15-nov-2026). Verificación nueva en fuente: blog de Algorand v5.0.0 (16-ago-2026, leído) y búsqueda sobre el registro de Plume ante la SEC (sec.gov devolvió 503: queda [VERIFICAR]). La matriz se genera celda a celda; «única» = exactamente una red con SÍ.

**Niveles.** mixto por celda: P (fuente primaria), S (secundaria o agregador), V (sin verificar), R (razonado a partir de datos del repo). Cada hecho lleva fuente, nivel y fecha. «aporta» y «para_que_sirve_mejor» son lecturas razonadas a partir de esos hechos, no hechos nuevos ni un ranking.

## 1. Capacidades únicas (exactamente una red con SÍ)

| Capacidad | Red | Parciales | Celdas sin dato |
|---|---|---|---|
| DEX con permisos activado | XRP Ledger | — | 11 |
| Comisión fijada en dólares | Hedera | canton | 0 |
| Privacidad entre participantes | Canton Network | bnb, avalanche, quant | 9 |
| Servicio de tokenización de DTC | Canton Network | stellar, solana, chainlink | 10 |
| Oráculos y mensajería como servicio a otras redes | Chainlink (capa de interoperabilidad, no cadena) | avalanche, polygon, quant | 11 |
| Registro de documentos de comercio e identidad | IOTA | xrpl, xdc | 10 |
| Cuentas resistentes a computación cuántica en el protocolo | Algorand | — | 12 |
| Emisor de un mismo producto en varias redes | Ondo (emisor y protocolo, no cadena) | plume | 12 |

*Aviso:* «única» se refiere a los datos del repo; una celda «sin dato» no es NO.

## 2. Solapes (3 o más redes con SÍ)

- **Control del emisor en el protocolo**: xrpl, stellar, algorand (parcial: ethereum, polygon, plume)
- **Staking nativo del token**: hedera, ethereum, solana, bnb, avalanche, polygon, algorand, xdc, iota, plume (parcial: canton, chainlink, quant)
- **Permisos y cumplimiento en la red**: xrpl, avalanche, canton (parcial: stellar, hedera, ethereum, bnb, polygon, algorand, quant, plume)
- **En el directorio CCIP de Chainlink**: hedera, ethereum, solana, bnb, avalanche, polygon, chainlink, xdc, plume (parcial: stellar)
- **USDC nativo por CCTP de Circle**: stellar, ethereum, solana, avalanche, polygon, xdc, plume (parcial: bnb)
- **Liquidez de stablecoins en la red**: ethereum, solana, bnb, polygon (parcial: xrpl, stellar, avalanche, algorand, xdc)
- **RWA distribuidos (transferibles en la red)**: stellar, ethereum, solana, bnb, avalanche (parcial: xrpl, polygon, plume)
- **Liquidación bancaria realizada con fuente primaria**: ethereum, solana, canton (parcial: xrpl, hedera)
- **ETF spot del token en EE. UU.**: xrpl, hedera, ethereum, solana, bnb, avalanche, chainlink

## 3. Matriz capacidad × red

| Capacidad | xrpl | stellar | hedera | ethereum | solana | bnb | avalanche | polygon | canton | chainlink | ondo | algorand | xdc | quant | iota | plume |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEX en el protocolo | SÍ | SÍ | NO | NO | NO | NO | NO | NO | · | NO | NO | NO | NO | NO | NO | NO |
| DEX con permisos activado | SÍ | NO | · | · | · | · | · | · | · | NO | NO | · | · | NO | · | · |
| Control del emisor en el protocolo | SÍ | SÍ | · | PARC | · | · | · | PARC | · | NO | NO | SÍ | · | NO | · | PARC |
| Comisión fijada en dólares | NO | NO | SÍ | NO | NO | NO | NO | NO | PARC | NO | NO | NO | NO | NO | NO | NO |
| Staking nativo del token | NO | NO | SÍ | SÍ | SÍ | SÍ | SÍ | SÍ | PARC | PARC | NO | SÍ | SÍ | PARC | SÍ | SÍ |
| Permisos y cumplimiento en la red | SÍ | PARC | PARC | PARC | · | PARC | SÍ | PARC | SÍ | NO | NO | PARC | · | PARC | · | PARC |
| Privacidad entre participantes | NO | · | · | · | · | PARC | PARC | · | SÍ | NO | NO | · | · | PARC | · | · |
| Redes propias a medida | PARC | · | · | PARC | · | · | SÍ | SÍ | PARC | NO | NO | · | PARC | NO | · | · |
| En el directorio CCIP de Chainlink | · | PARC | SÍ | SÍ | SÍ | SÍ | SÍ | SÍ | · | SÍ | NO | NO | SÍ | · | NO | SÍ |
| USDC nativo por CCTP de Circle | · | SÍ | · | SÍ | SÍ | PARC | SÍ | SÍ | · | NO | NO | NO | SÍ | NO | NO | SÍ |
| Liquidez de stablecoins en la red | PARC | PARC | NO | SÍ | SÍ | SÍ | PARC | SÍ | · | NO | NO | PARC | PARC | NO | NO | NO |
| RWA distribuidos (transferibles en la red) | PARC | SÍ | NO | SÍ | SÍ | SÍ | SÍ | PARC | NO | NO | NO | NO | NO | NO | NO | PARC |
| Servicio de tokenización de DTC | · | PARC | · | · | PARC | · | · | · | SÍ | PARC | NO | · | · | NO | · | · |
| Liquidación bancaria realizada con fuente primaria | PARC | NO | PARC | SÍ | SÍ | NO | NO | NO | SÍ | NO | NO | NO | NO | NO | NO | NO |
| ETF spot del token en EE. UU. | SÍ | NO | SÍ | SÍ | SÍ | SÍ | SÍ | · | · | SÍ | NO | · | · | NO | · | · |
| Oráculos y mensajería como servicio a otras redes | · | · | · | · | · | · | PARC | PARC | · | SÍ | NO | · | · | PARC | · | · |
| Registro de documentos de comercio e identidad | PARC | · | · | · | · | · | · | · | · | NO | NO | · | PARC | NO | SÍ | · |
| Cuentas resistentes a computación cuántica en el protocolo | · | · | · | · | · | · | · | · | · | NO | NO | SÍ | · | NO | · | · |
| Emisor de un mismo producto en varias redes | · | · | · | · | · | · | · | · | · | NO | SÍ | · | · | NO | · | PARC |

`·` = sin dato. Fuente, nivel y fecha de cada celda en el JSON.

## 4. Lectura

- HECHO: solo XRPL y Stellar tienen DEX en el protocolo; solo XRPL tiene además DEX con permisos activado.
- HECHO: más de 1.000 M$ en stablecoins solo en Ethereum, Solana, BNB Chain y Polygon; más de 1.000 M$ en RWA distribuidos en Ethereum, BNB Chain, Solana, Stellar y Avalanche; la mayor cifra «representada» está en Canton.
- HECHO: Canton es la única con el servicio de DTC en producción; Stellar y Solana tienen planes para 2027.
- HECHO: el staking nativo es la capacidad más repetida (10 redes con SÍ); no lo tienen XRPL ni Stellar.
- RAZONADO: las capacidades únicas no son excluyentes: una institución puede emitir en una red, mover dinero en otra y conectar ambas con CCIP o CCTP. [ESPECULACIÓN] si eso favorece a alguna red concreta.

## 5. Red a red

### XRP Ledger

**Aporta (razonado):** Reúne en el propio protocolo un DEX con libro de órdenes, un activo puente para pagos (XRP en ODL) y herramientas de cumplimiento ya activadas en la red principal (credenciales, dominios y DEX con permisos, congelación profunda). De las 16, es la única con DEX nativo Y DEX con permisos activados a la vez; Stellar tiene DEX nativo pero no DEX con permisos en los datos del repo.

**Puntos fuertes (hechos):**
- Cierre de ledger medio medido de 3,737 s; un ledger validado es final (sin bifurcaciones) — s1.ripple.com (métodos ledger y fee), en comparativa-liquidacion.json, 2026-11-15 [P]
- Comisión mínima de 10 gotas ≈ 0,00001 USD por transacción — s1.ripple.com método fee; precio DefiLlama, en comparativa-liquidacion.json, 2026-11-15 [P]
- Activadas en la red principal: Credentials, PermissionedDomains, PermissionedDEX, MPTokensV1, DeepFreeze y TokenEscrow — Consulta «feature» a un nodo público (cadenas.json), 2026-11-14 [P]
- Stablecoins 839 M$ en 8 emisiones, con monedas no USD (EURCV, EUROP en euros; AUDD en dólar australiano); RLUSD 762,7 M$ — DefiLlama, en comparativa-liquidacion.json, 2026-11-15 [S]
- 5.210 M$ en activos «representados» (3.ª cifra tras Canton y Avalanche) y 642,8 M$ distribuidos — RWA.xyz, ficha XRP Ledger, 2026-11-14 [S]

**Puntos flacos (hechos):**
- Stablecoins 839 M$ frente a 131.392 M$ en Ethereum y 13.913 M$ en Solana — DefiLlama, en comparativa-liquidacion.json, 2026-11-15 [S]
- TVL DeFi 30,0 M$ — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- LendingProtocol y SingleAssetVault siguen sin activar aunque rippled 3.1.0 (28-ene-2026) los incluye; sin staking nativo — Consulta «feature» al nodo y xrpl.org/blog (cadenas.json), 2026-11-14 [P]
- La lista de validadores por defecto (UNL) la publica Ripple: 35 validadores — vl.ripple.com, en cadenas-validadores.json, 2026-11-15 [P]
- Dos fallos corregidos en xrpld 3.4.1 (informe del 9-oct-2026); la enmienda afectada no estaba activada en la red principal — xrpl.org, informe de vulnerabilidades, en comparativa-liquidacion.json, 2026-10-09 [P]
- El 24-sep-2026 el robo a Bitget (387 M$, clave de cartera caliente) figura con XRPL entre las redes afectadas: fallo del exchange, no del protocolo — DefiLlama hacks, en cadenas-incidentes.json, 2026-09-24 [S]

**Mejora reciente (12 meses):**
- 2026-01-28: rippled 3.1.0 incluye Single Asset Vault y Lending Protocol (pendientes de voto, sin activar a 14-nov) [P]
- 2026-02-18: Lanzamiento de EURCV (SG-FORGE) en XRPL según prensa [VERIFICAR en comunicado de SG-FORGE] [S]
- 2026-03-25: Ripple entra en BLOOM de la MAS para probar liquidación programable de comercio con RLUSD en XRPL [S]
- 2026-05-06: Reembolso transfronterizo de OUSG: pata del activo en XRPL en menos de 5 s y pago en USD por Kinexys y Mastercard MTN [P]
- 2026-09-25: rippled 3.4.1: versión de emergencia con correcciones de seguridad [P]
- 2026-09-29: CSD BR/BTG Pactual registra en XRPL espejos de fondos con permisos y KYC [S]

**Quién la usa:**
- Emisores de stablecoins: Ripple (RLUSD); SG-FORGE (EURCV, lanzamiento solo en prensa) (producción (RLUSD); EURCV [VERIFICAR]) [S]
- Gestoras: Franklin Templeton (sgBENJI, MoU con DBS); Ondo (OUSG en XRPL) (plan (MoU) / producción) [P]
- Bancos: DBS (MoU, no operativo); J.P. Morgan Kinexys (piloto de reembolso OUSG, fuente de Ondo) (plan / piloto) [P]
- Bancos centrales: MAS (BLOOM, piloto); acuerdos antiguos con Bután, Montenegro, Georgia y Colombia sobre la plataforma CBDC privada de Ripple (no el XRPL público) (piloto / exploratorio) [S]
- Infraestructuras de mercado: CSD BR / BTG Pactual (espejos de fondos) (producción según cadenas.json) [S]

**Para qué sirve mejor (razonado):**
- Liquidación y pagos multi-divisa: DEX nativo con pares XRP/RLUSD, XRP/USD, XRP/EUR, XRP/USDC y XRP/EUROP medidos en profundidad-multidivisa.json [P]; finalidad 3,7 s y comisión mínima [P]. El volumen real de ODL en XRP no lo publica Ripple [sin dato].
- Emisión con controles de cumplimiento en protocolo: Credentials, PermissionedDomains, PermissionedDEX y DeepFreeze activadas [P].
- Tokenización de fondos monetarios y deuda: sgBENJI 193 M$ y OUSG 186 M$ distribuidos en XRPL (RWA.xyz, 15-nov-2026) [S].

**Límites conocidos:**
- Contratos inteligentes EVM solo en la XRPL EVM Sidechain (mainnet 30-jun-2025), no en el libro principal; puente nativo XChainBridge sin activar [P]
- Préstamos y bóvedas nativas sin activar (dependen del voto de validadores) [P]
- Ripple no separa el volumen de ODL en XRP del total de Ripple Payments [P]
- La comisión mediana del último ledger fue 0,0048 USD: sube con la carga [P]

### Stellar

**Aporta (razonado):** Emisión muy barata de stablecoins y fondos con «anclajes» que entran y salen de dinero fiduciario, y control del emisor en el protocolo (autorizar, congelar y recuperar). Tiene el DEX nativo con más pares en monedas distintas del USD de las redes medidas (XLM/EURC, USDC/EURC) y es la primera red pública en el calendario del servicio de tokenización de DTC (1S-2027, plan).

**Puntos fuertes (hechos):**
- Comisión mediana cobrada 100 stroops ≈ 0,0000014 USD, la más baja medida en la comparativa — Horizon fee_stats; precio DefiLlama, en comparativa-liquidacion.json, 2026-11-15 [P]
- Ledger cada 5,0 s, final al cerrarse (SCP) — horizon.stellar.org, en comparativa-liquidacion.json, 2026-11-15 [P]
- 4.662,8 M$ en RWA distribuidos, 4.ª red tras Ethereum, BNB Chain y Solana (+31,6 % en 30 días) — RWA.xyz, ficha Stellar, 2026-11-14 [S]
- BENJI (Franklin Templeton), primer fondo monetario registrado en EE. UU. tokenizado, en Stellar desde 2021; más de 650 M$ del token en Stellar a abr-2026 — SDF y Franklin, comunicado conjunto (en pruebas-bancos.json), 2026-04 [P]
- USDC nativo con CCTP de Circle desde el 19-may-2026 (sin puente custodio) — Blog de la SDF (parte interesada), 2026-05-19 [P]
- 16 stablecoins, con EURC, EURCV (euro) y AUDD (dólar australiano) — DefiLlama, en comparativa-liquidacion.json, 2026-11-15 [S]

**Puntos flacos (hechos):**
- Stablecoins 398 M$, muy por debajo de Ethereum y Solana — DefiLlama, en comparativa-liquidacion.json, 2026-11-15 [S]
- La conexión con DTC es un plan para el 1S-2027, no producción — DTCC, nota de 27-may-2026, 2026-05-27 [P]
- Sin ETF spot en EE. UU. (solo el fideicomiso GXLM en OTCQX) — Dossier ETF del repo, 2026-10-09 [P]
- Blend Pools V2 sufrió una manipulación de precio de 10,97 M$ el 22-feb-2026 — DefiLlama hacks, en cadenas-incidentes.json, 2026-02-22 [S]
- Volumen del DEX -53,4 % en 30 días (44,3 M$ en 30 días) — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]

**Mejora reciente (12 meses):**
- 2026-05-19: CCTP de Circle en vivo (USDC sin puente custodio) [P]
- 2026-05-27: DTCC anuncia que conectará su servicio de tokenización con Stellar (activos previstos en el 1S-2027) [P]
- 2026-09-02: USDT0 en vivo en Stellar [P]
- 2026-10-05: stellar-core v29.0.0 (y v30.0.0 el 16-oct-2026) [P]
- 2026-10-14: Chainlink en vivo en Stellar [P]

**Quién la usa:**
- Gestoras: Franklin Templeton (BENJI); Spiko, Ondo (USDY), WisdomTree, Realiz (producción) [S]
- Emisores de stablecoins y remesadoras: Circle (USDC, EURC); MoneyGram (MGUSD) (producción) [S]
- Infraestructuras de mercado: DTCC (depositaria DTC) (plan (1S-2027)) [P]
- Bancos: SG-FORGE (EURCV, integración anunciada 20-feb-2025, estado [VERIFICAR]); VersaBank (piloto de recibos de depósito) (anunciado / piloto) [S]
- Redes de pago: Visa (red incluida en su piloto de liquidación con stablecoins) (piloto) [P]

**Para qué sirve mejor (razonado):**
- Pagos con stablecoins de bajo importe y entrada/salida a fiat: Comisión ≈ 0,0000014 USD [P]; 23.710 M$ transferidos en stablecoins en 30 días con 445 M$ de oferta (RWA.xyz) [S]; MoneyGram MGUSD [S].
- Tokenización de fondos monetarios y deuda: Deuda 2.246,7 M$ en 23 activos y fondos 1.800 M$ (RWA.xyz) [S]; BENJI desde 2021 [P].
- Liquidación multi-divisa: DEX nativo con XLM/USDC, XLM/EURC y USDC/EURC medidos en profundidad-multidivisa.json [P]; EURCV y AUDD emitidos [S].

**Límites conocidos:**
- Sin staking ni inflación desde el voto del 28-oct-2019: el token no da rendimiento nativo [P]
- Capacidad observada 107 tx/s en la muestra (no es el máximo del protocolo); uso del ledger 0,62 [P]
- Volumen de pagos liquidado en XLM (no en stablecoins) y conectores ISO 20022 de los anclajes: sin dato [P]

### Hedera

**Aporta (razonado):** Es la única de las 16 con comisión por operación fijada en dólares (pagada en HBAR) y un servicio de consenso (HCS) para sellar mensajes y eventos con coste previsible. La gobierna un consejo de empresas que operan los nodos (permisionados); el staking de HBAR no tiene bloqueo ni penalización.

**Puntos fuertes (hechos):**
- Comisión fijada en USD: transferencia 0,0001 $, transferencia de token HTS 0,001 $, mensaje HCS 0,0008 $, crear token 1 $ — docs.hedera.com, tabla de comisiones, 2026-11-14 [P]
- Registros cada 2,169 s en el mirror node; finalidad aBFT de segundos según la documentación [VERIFICAR medida directa] — mirror node público, en comparativa-liquidacion.json, 2026-11-15 [S]
- 30 nodos; coeficiente de Nakamoto (1/3) = 10 — mirror node, en cadenas-validadores.json, 2026-11-15 [P]
- Staking nativo de HBAR sin bloqueo ni «slashing» — docs.hedera.com, Stake HBAR (parte interesada), 2026-11-14 [P]
- Participó en el desafío DLT del Banco de Inglaterra y el BIS Innovation Hub de Londres (sin resultados publicados) — Hedera, blog (en pruebas-bancos.json), 2025-10-28 [P]

**Puntos flacos (hechos):**
- Stablecoins 25,6 M$ (casi todo USDC) — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- 88,3 M$ en RWA distribuidos y 70,3 M$ representados — RWA.xyz, 2026-11-14 [S]
- Nodos de consenso operados por miembros del Consejo; los nodos comunitarios y sin permisos están anunciados sin fecha — hedera.com (resumen de buscador), 2026-11-14 [S]
- El comunicado del RBA sobre Acacia no nombra Hedera (la atribución viene de un blog de LF Decentralized Trust) — RBA, nota 2026-13 (en pruebas-bancos.json), 2026-05-18 [P]
- Bonzo Lend sufrió una manipulación de precio de 9,05 M$ el 11-jul-2026 — DefiLlama hacks, en cadenas-incidentes.json, 2026-07-11 [S]
- Comisiones cobradas -45,6 % y volumen DEX -55,9 % en 30 días — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]

**Mejora reciente (12 meses):**
- 2026-05-18: RBA y DFCRC publican los resultados de Acacia (20 casos mayoristas; el comunicado no nombra redes) [P]
- 2026-06-11: Archax anuncia pagos de intereses en tiempo real (en USDC) para valores tokenizados en Hedera [S]
- 2026-08-05: Taurus abre la pila de Hedera (tokens, contratos, nodos y staking) a 40+ instituciones, entre ellas CACEIS y State Street [S]
- 2026-09-24: Hedera cede CLPR (protocolo entre libros mayores sin puentes) a LF Decentralized Trust; testnet [S]
- 2026-11-11: Apex Group entra en el Consejo de Hedera (tokenización basada en ERC-3643; «explorará» Hedera) [S]

**Quién la usa:**
- Empresas del Consejo (gobierno y nodos): Apex Group (desde 11-nov-2026); resto sin cifra primaria leída (gobierno de la red) [P]
- Custodios: Taurus (custodia y staking de HBAR para bancos, según prensa); BitGo (producción según prensa) [S]
- Emisores de valores tokenizados: Archax (anunciado) [S]
- Bancos centrales (pruebas): Banco de Inglaterra/BIS (desafío); RBA Acacia (cadena atribuida por terceros) (prueba / piloto cerrado) [S]

**Para qué sirve mejor (razonado):**
- Registro y sellado de eventos con coste previsible: Mensaje HCS a 0,0008 $ fijado en USD [P].
- Tokenización con comisiones estables para empresas: Crear token 1 $ y transferir 0,001 $ fijados en USD [P]; volumen actual pequeño (88 M$) [S].
- Rendimiento y colateral: Staking sin bloqueo ni penalización [P]; tasa vigente no leída [sin dato].

**Límites conocidos:**
- La comisión de 0,0001 $ es la tarifa documentada, no una medida [S]
- Número exacto de miembros del Consejo y fecha de nodos sin permisos: sin cifra primaria [P]
- Integración real con Swift o ISO 20022: sin dato [P]

### Ethereum (y sus L2)

**Aporta (razonado):** La mayor liquidez de stablecoins (131.392 M$) y de RWA distribuidos (15.153,5 M$) de las 16, el mayor mercado DeFi de colateral y préstamos (TVL 37.971 M$) y el estándar técnico (EVM, ERC-3643) que reutilizan Polygon, Avalanche, Plume y las redes privadas Besu de Swift y DTCC.

**Puntos fuertes (hechos):**
- Stablecoins 131.392 M$ en 230 emisiones (USDT 66.783 M$, USDC 41.686 M$, RLUSD 2.020 M$) — DefiLlama, en comparativa-liquidacion.json, 2026-11-15 [S]
- 15.153,5 M$ en RWA distribuidos (1.ª red), con 2.876 acciones tokenizadas y 87 activos de deuda pública — RWA.xyz, 2026-11-14 [S]
- TVL DeFi 37.971 M$ y volumen DEX de 52.375 M$ en 30 días — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- 44,19 M de ETH en staking (35 % del suministro), APR del 2,5 % (página sin fecha) — ethereum.org/staking, 2026-11-12 [P]
- El BEI emitió en 2021 un bono digital de 100 M€ en la Ethereum pública, con el pago representado en CBDC del Banque de France — BEI, comunicado 2021-141, 2021-04-27 [P]
- Estándar ERC-3643: identidad y reglas de cumplimiento comprobadas en cadena antes de cada transferencia — EIP-3643, 2026-11-14 [P]

**Puntos flacos (hechos):**
- Finalidad «finalized» a ~1.056 s (~18 min) del último bloque en la capa 1 — ethereum-rpc.publicnode.com, en comparativa-liquidacion.json, 2026-11-15 [P]
- Transferencia simple ≈ 0,0109 USD en la capa 1, la comisión más alta de la comparativa en ese momento — eth_feeHistory; precio DefiLlama, 2026-11-15 [P]
- Capacidad observada 21 tx/s en la capa 1 (las capas 2 no se miden) — ethereum-rpc.publicnode.com, en comparativa-liquidacion.json, 2026-11-15 [P]
- 105 incidentes en 12 meses en DefiLlama (incluye el de Binance de 6.360 M$ atribuido a varias redes; no sumar entre redes) — DefiLlama hacks, en cadenas-incidentes.json, 2026-11-15 [S]
- Glamsterdam sin fecha en mainnet (aplazada en Hoodi el 22-oct-2026) — Everstake (secundaria), 2026-10-22 [S]

**Mejora reciente (12 meses):**
- 2025-12-03: Bifurcación Fusaka en la red principal [S]
- 2026-04-29: Ethereum sigue en el piloto de liquidación con stablecoins de Visa (9 redes, 7.000 M$ anualizados en conjunto) [P]
- 2026-05-11: JPM Coin (depósito tokenizado de J.P. Morgan) emitido en Base, capa 2 de Ethereum [P]
- 2026-10-06: Glamsterdam activa en la red de pruebas Sepolia [S]
- 2026-10-23: go-ethereum v1.17.10 [P]

**Quién la usa:**
- Emisores de stablecoins: Tether (USDT), Circle (USDC), Sky (USDS), Ripple (RLUSD) (producción) [S]
- Gestoras: BlackRock (BUIDL desde mar-2024, con Securitize y BNY); Franklin (iBENJI) [VERIFICAR]; BNP Paribas AM [VERIFICAR] (producción) [P]
- Bancos: J.P. Morgan (JPM Coin en Base); SG-FORGE (EURCV); DBS (notas estructuradas) [S]; VersaBank (piloto) [S] (producción / piloto) [P]
- Banco central y supranacional: Banque de France y BEI (bono digital de 2021, vencido en 2023) (experimento completado) [P]
- Redes de pago: Visa (piloto de liquidación con stablecoins) (piloto) [P]

**Para qué sirve mejor (razonado):**
- Colateral y préstamos: TVL 37.971 M$ y mayor mercado DeFi de préstamos [S]; staking del 35 % del suministro [P].
- Tokenización de RWA y valores con reglas de cumplimiento: 1.ª red en RWA distribuidos [S]; ERC-3643 [P]; BUIDL [P].
- Contratos inteligentes y NFT: Estándar EVM de referencia que reutilizan otras redes y Besu [P, Swift 30-mar-2026].
- Liquidación en stablecoins USD de gran volumen: 131.392 M$ en stablecoins [S]; liquidaciones bancarias realizadas con fuente primaria: 3 (pruebas-bancos.json) [P].

**Límites conocidos:**
- Comisión variable en ETH y finalidad lenta en la capa 1; la velocidad depende de capas 2 que aquí no se miden [P]
- Reparto de BUIDL por cadena y parte de las comisiones de las L2 que llega a Ethereum: sin dato del emisor [P]

### Solana

**Aporta (razonado):** El mayor rendimiento observado de las 16 (1.225 tx/s, slot de 0,215 s) con comisión ≈ 0,00036 USD, la 2.ª liquidez de stablecoins (13.913 M$) y la base minorista más amplia de RWA (1,03 M de titulares). Tiene una emisión bancaria completada con fuente primaria: el papel comercial de Galaxy tokenizado por J.P. Morgan con liquidación en USDC.

**Puntos fuertes (hechos):**
- 1.225,3 tx/s observadas en media hora y slot medio de 0,215 s — api.mainnet-beta.solana.com, en comparativa-liquidacion.json, 2026-11-15 [P]
- Stablecoins 13.913 M$ en 78 emisiones (USDC 7.397 M$, PYUSD 803 M$); comisión ≈ 0,00036 USD — DefiLlama; getRecentPrioritizationFees, 2026-11-15 [S]
- 5.144,6 M$ en RWA distribuidos (3.ª red) y 1,03 M de titulares de RWA — RWA.xyz, 2026-11-14 [S]
- J.P. Morgan creó el token y gestionó la entrega contra pago del papel comercial de Galaxy en Solana, con liquidación en USDC — J.P. Morgan, comunicado, 2025-12-11 [P]
- 661 validadores activos; coeficiente de Nakamoto (1/3) = 18 — RPC público, en cadenas-validadores.json, 2026-11-15 [P]

**Puntos flacos (hechos):**
- La finalidad real no es medible con el RPC público; no hay cifra medida — api.mainnet-beta.solana.com, en comparativa-liquidacion.json, 2026-11-15 [P]
- El recuento de tx/s no separa los votos de los validadores en esta fuente — getRecentPerformanceSamples, 2026-11-15 [P]
- La conexión con DTC es un plan para el 2S-2027, no producción — DTCC, nota de 12-nov-2026, 2026-11-12 [P]
- 20 incidentes en 12 meses con 451 M$ en DefiLlama (atribución doble posible) — DefiLlama hacks, en cadenas-incidentes.json, 2026-11-15 [S]
- 39 validadores morosos (delinquent) en la lectura — RPC público, en cadenas-validadores.json, 2026-11-15 [P]

**Mejora reciente (12 meses):**
- 2025-12-11: Papel comercial de Galaxy tokenizado por J.P. Morgan en Solana con liquidación en USDC [P]
- 2026-05: Western Union lanza USDPT (emisor Anchorage Digital Bank) en Solana para liquidación con agentes [VERIFICAR] [S]
- 2026-06-03: Mastercard anuncia liquidación de stablecoins en Solana (sin volúmenes) [S]
- 2026-10-21: Alpenglow (fase Votor) activo en la red principal, época 1064 [P]
- 2026-11-12: DTCC anuncia que conectará su servicio de tokenización con Solana (2S-2027) [P]

**Quién la usa:**
- Emisores de stablecoins: Circle (USDC), Tether, PayPal (PYUSD), World Liberty (USD1) (producción) [S]
- Bancos: J.P. Morgan (papel comercial de Galaxy); SG-FORGE (EURCV) (emisión completada / producción) [P]
- Gestoras: BlackRock (clase de BUIDL); Franklin Templeton (compradora del papel comercial) (producción) [P]
- Remesadoras y redes de pago: Western Union (USDPT) [S]; Visa (piloto) [P]; Mastercard [S] (piloto / producción inicial) [S]
- Infraestructuras de mercado: DTCC (depositaria DTC) (plan (2S-2027)) [P]

**Para qué sirve mejor (razonado):**
- Pagos con stablecoins de alto volumen y bajo coste: 1.225 tx/s y 0,00036 USD por transacción [P/S]; 13.913 M$ en stablecoins [S].
- Emisión y entrega contra pago de valores: Papel comercial de JPM liquidado en USDC [P]; 2 liquidaciones bancarias realizadas con fuente primaria (pruebas-bancos.json) [P].
- Acciones tokenizadas para minoristas: 572,9 M$ en 1.971 acciones tokenizadas y 1,03 M de titulares de RWA (RWA.xyz) [S].

**Límites conocidos:**
- Fase «Rotor» de Alpenglow sin fecha [P]
- Integración con ISO 20022 y volumen institucional por emisor: sin dato [P]

### BNB Chain

**Aporta (razonado):** La 2.ª red en RWA distribuidos (6.270 M$) y una gran liquidez minorista (12.464 M$ en stablecoins; 96 M de titulares), con un vínculo directo con el mayor exchange: BUIDL de BlackRock se acepta como colateral en Binance. Bloques de 0,45 s.

**Puntos fuertes (hechos):**
- 6.270 M$ en RWA distribuidos (2.ª red); 1.700 M$ en 2.912 acciones tokenizadas — RWA.xyz, ficha BNB Chain, 2026-11-14 [S]
- Stablecoins 12.464 M$ (USDT 9.180 M$); 96 M de titulares de stablecoins — DefiLlama y RWA.xyz, 2026-11-15 [S]
- BUIDL (BlackRock/Securitize) lanzado en BNB Chain y aceptado como colateral fuera de bolsa en Binance — BlackRock/Securitize, comunicado, 2025-11-14 [P]
- Bloques de 0,45 s y finalidad rápida ≈ 1,125 s si votan 2/3 de los validadores — docs.bnbchain.org, 2024-09-25 [P]
- Volumen DEX de 29.157 M$ en 30 días — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]

**Puntos flacos (hechos):**
- La documentación no da el número de validadores (PoSA, validadores elegidos por BNB en staking) — docs.bnbchain.org, 2026-11-14 [P]
- iBENJI de Franklin: 1.531 M$ con 4 tenedores (concentración) — RWA.xyz, ficha BNB Chain, 2026-11-14 [S]
- 61 incidentes en 12 meses con 134 M$ en DefiLlama — DefiLlama hacks, en cadenas-incidentes.json, 2026-11-15 [S]
- CCTP de Circle solo para USYC, no para USDC — Circle Docs, cadenas soportadas, 2026-11-14 [P]
- La recompensa de staking sale de las comisiones; no se publica APR — docs.bnbchain.org, staking, 2026-11-14 [P]

**Mejora reciente (12 meses):**
- 2025-11-14: BUIDL en BNB Chain y colateral en Binance (justo en el límite de la ventana de 12 meses) [P]
- 2026-02: Franklin y Binance anuncian iBENJI como colateral institucional fuera de bolsa con custodia de Ceffu [S]
- 2026-10-19: bsc v1.8.1 (y v1.8.2 el 3-nov-2026) [P]
- 2026-11-14: La documentación presenta una pila de «privacidad programable» (Intelligent Privacy Pool, ZKredit, cifrado homomórfico con Zama): hoja de ruta propia, sin usuarios contados [P]

**Quién la usa:**
- Exchange: Binance (colateral con BUIDL e iBENJI) (producción) [P]
- Gestoras: BlackRock (BUIDL); Franklin (iBENJI); Circle (USYC); Ondo (USDY) (producción) [S]
- Emisores de stablecoins: Tether (USDT), World Liberty (USD1), United Stables (U) (producción) [S]
- Bancos centrales: Banco Nacional de Kazajistán (pruebas del tenge digital en 2022) (sin evidencia de producción) [S]

**Para qué sirve mejor (razonado):**
- Colateral tokenizado en exchange: BUIDL e iBENJI como colateral en Binance [P/S].
- Acciones tokenizadas y stablecoins minoristas: 1.700 M$ en acciones tokenizadas [S]; 96 M de titulares de stablecoins [S].

**Límites conocidos:**
- Información primaria escasa por emisor; integración institucional fuera de Binance sin dato [P]
- La guía leída no da una comisión típica [P]

### Avalanche

**Aporta (razonado):** Permite lanzar redes L1 propias que fijan requisitos a sus validadores (ubicación, KYC/AML, licencia) y guardan datos privados, conectadas entre sí por mensajería nativa (ICM sobre Avalanche Warp Messaging). Tiene la 2.ª mayor cifra de valor «representado» (11.403,5 M$) tras Canton y el mayor coeficiente de Nakamoto de las redes medidas (24).

**Puntos fuertes (hechos):**
- Cada L1 puede exigir requisitos a sus validadores (ubicación, KYC/AML o licencia) y mantener datos privados — build.avax.network, L1 (parte interesada), 2026-11-14 [P]
- Mensajería entre L1 (ICM sobre Warp Messaging, desde Durango, mar-2024) y transferencia de tokens (ICTT) — build.avax.network, cross-chain, 2026-11-14 [P]
- 604 validadores en la red primaria; coeficiente de Nakamoto (1/3) = 24, el más alto de las redes medidas — API pública P-Chain, en cadenas-validadores.json, 2026-11-15 [P]
- 1.413,9 M$ distribuidos y 11.403,5 M$ representados; crédito tokenizado 690,6 M$ — RWA.xyz, 2026-11-14 [S]
- Clase de BUIDL en Avalanche con BNY como administrador y custodio — BlackRock, comunicado, 2024-11-13 [P]

**Puntos flacos (hechos):**
- Stablecoins 773 M$ — DefiLlama, en comparativa-liquidacion.json, 2026-11-15 [S]
- Modelo de comisiones de las L1 institucionales y emisores del valor representado: sin dato — cadenas.json (sin_dato), 2026-11-14 [P]
- Las pruebas con Citi y J.P. Morgan (Onyx) no tienen fecha ni fuente primaria leída — pruebas-bancos.json, 2026-11-15 [S]
- Volumen DEX -40,7 % en 30 días (2.473 M$) — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]

**Mejora reciente (12 meses):**
- 2026-03-11: Grayscale lanza un ETF de AVAX con staking (GAVA) [S]
- 2026-04-29: Avalanche sigue en el piloto de liquidación con stablecoins de Visa [P]
- 2026-07-28: Helicon en vigor en la red de pruebas Fuji [S]
- 2026-09-22: Activación programada de Helicon en mainnet: ejecución asíncrona en la C-Chain, staking con renovación automática y duración mínima de 48 h (la release no confirma la activación efectiva) [P]
- 2026-11-05: avalanchego v1.15.3 [P]

**Quién la usa:**
- Gestoras: BlackRock (BUIDL); Franklin (BENJI) [VERIFICAR] (producción) [P]
- Bancos (pruebas): Citi (cambio de divisas simulado en subredes Evergreen, Guardian); J.P. Morgan Onyx (carteras multicadena) (prueba) [S]
- Redes de pago: Visa (piloto) [P]
- Emisores de stablecoins: Tether, Circle, Ethena (producción) [S]

**Para qué sirve mejor (razonado):**
- Redes institucionales a medida con requisitos de cumplimiento: L1 con requisitos a validadores y datos privados [P]; ICM [P].
- Crédito tokenizado: 690,6 M$ en 40 activos de crédito (RWA.xyz) [S].
- Rendimiento: Staking con mínimo 2.000 AVAX para validar y 25 para delegar [P].

**Límites conocidos:**
- Las L1 propias no hacen stake de AVAX pero pagan una tarifa continua (mínimo ≈ 1,33 AVAX al mes por validador) [P]
- El peso de los validadores de la API puede incluir delegaciones [VERIFICAR] [P]

### Polygon

**Aporta (razonado):** Red EVM barata (0,002 $ por transacción, autodeclarado) con kit para lanzar cadenas propias (CDK) unidas por Agglayer, cuyas «pruebas pesimistas» limitan el daño de una cadena comprometida a sus propios depósitos. Sobre esa base se anunció T-REX Ledger, una cadena de cumplimiento para valores ERC-3643.

**Puntos fuertes (hechos):**
- Stablecoins 2.798 M$ (USDC 1.610 M$; pUSD de Polymarket 499 M$) — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- Finalidad determinista en 2-5 s por milestones — docs.polygon.technology (parte interesada), 2026-11-14 [P]
- Agglayer: interoperabilidad con «pruebas pesimistas» — docs.agglayer.dev, 2026-11-14 [P]
- T-REX Ledger (Polygon CDK + Agglayer) para valores ERC-3643; Apex se compromete a 100 mil M$ tokenizados hasta jun-2027 (compromiso, no volumen) — polygon.technology/blog, 2026-03-18 [P]
- USDC nativo por CCTP (dominio 7); clase de BUIDL en Polygon PoS — Circle Docs; BlackRock, 2026-11-14 [P]

**Puntos flacos (hechos):**
- 447,6 M$ en RWA distribuidos — RWA.xyz, 2026-11-14 [S]
- Máximo de 105 validadores activos; el número real no lo da la documentación — docs.polygon.technology, 2026-11-14 [P]
- 18 incidentes en 12 meses con 54 M$ en DefiLlama (Polymarket International 2,7 M$ por ataque a la cadena de suministro) — DefiLlama hacks, en cadenas-incidentes.json, 2026-11-15 [S]
- Emisión de POL del 2 % anual desde jul-2025; si propuestas posteriores la cambian sigue [VERIFICAR] — docs.polygon.technology, rewards, 2026-11-15 [P]

**Mejora reciente (12 meses):**
- 2026-03-18: Anuncio de T-REX Ledger con Tokeny/Apex [P]
- 2026-04-29: Visa añade Polygon a su piloto de liquidación con stablecoins [P]
- 2026-11-05: bor v2.11.0 (y v2.11.1 el 13-nov-2026) [P]

**Quién la usa:**
- Gestoras y emisores: BlackRock (BUIDL); Ondo (OUSG en Polygon) (producción) [P]
- Redes de pago: Visa (piloto (alta anunciada)) [P]
- Mercados de predicción: Polymarket (pUSD 499 M$) (producción) [S]
- Tokenización regulada: Apex Group / Tokeny (T-REX Ledger) (compromiso) [P]
- Bancos (pilotos antiguos): DBS, J.P. Morgan (Onyx) y SBI Digital Asset en el Proyecto Guardian de MAS (2022; cadena según The Block) (piloto) [S]

**Para qué sirve mejor (razonado):**
- Pagos baratos compatibles con EVM: 0,002 $ autodeclarado [P]; Visa [P]; 2.798 M$ en stablecoins [S].
- Cadenas propias de cumplimiento conectadas: CDK + Agglayer [P]; T-REX Ledger [P].
- Inmuebles tokenizados: 79,5 M$ en 58 inmuebles (RWA.xyz) [S].

**Límites conocidos:**
- Rentabilidad de staking en vivo no publicada (solo calendario de emisión) [P]
- Sin estatus regulatorio de la red en su documentación; el producto de pagos Open Money Stack tiene KYC/AML pero sin licencia citada [P]

### Canton Network

**Aporta (razonado):** Privacidad entre participantes con permisos sobre un sincronizador global: cada parte solo ve sus operaciones. Es la única de las 16 donde el servicio de tokenización de DTC está en producción (desde el 28-oct-2026) y donde DTCC y más de 30 participantes hicieron operaciones de producción de colateral, repo y préstamo de valores.

**Puntos fuertes (hechos):**
- Servicio de tokenización de DTC en producción desde el 28-oct-2026, integrado con Canton y con una red privada Besu; 20 participantes de DTC (Barclays, BofA, BNP Paribas, Citi, J.P. Morgan, State Street, UBS…) han firmado acceso — DTCC, nota de prensa, 2026-10-28 [P]
- Jul-2026: DTCC y más de 30 participantes completan operaciones de producción con Tesoro, acciones y ETF tokenizados (colateral, margen, repo y préstamo de valores) — Canton, blog de 8-sep-2026, 2026-07-15 [P]
- BNP Paribas prestó valores intradía con Tesoro tokenizado por DTCC desde un nodo propio en Canton — Canton, blog, 2026-07 [P]
- 374.118 M$ en valor «representado», la mayor cifra de RWA.xyz — RWA.xyz, 2026-11-14 [S]
- Sin incidentes registrados en DefiLlama en 12 meses — DefiLlama hacks, en cadenas-incidentes.json, 2026-11-15 [S]

**Puntos flacos (hechos):**
- 0 $ en RWA distribuidos: todo es «representado» (registro de activos que existen fuera de la cadena) — RWA.xyz, 2026-11-14 [S]
- Sin cifra de stablecoins en DefiLlama; TVL 11,3 M$ — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- La media diaria de repos de Broadridge (351.000 M$) viene de una web entusiasta y no aclara qué parte va por Canton — Genfinity (secundaria), 2026-09-11 [S]
- El tráfico por encima de la franja gratuita se paga en Canton Coin (60 $/MB en la configuración de ejemplo); los Super Validators no pagan — docs.canton.network, Synchronizer Traffic, 2026-11-14 [P]

**Mejora reciente (12 meses):**
- 2025-12-11: Carta de no acción de la SEC a DTC para un servicio de tokenización de 3 años [S]
- 2026-04-29: Visa añade Canton a su piloto de liquidación con stablecoins [P]
- 2026-05-11: J.P. Morgan dice que JPM Coin se extenderá a Canton (plan) [P]
- 2026-07-15: Operaciones de producción de DTCC con más de 30 participantes [P]
- 2026-09-09: Broadridge DLX se conecta a DTCC vía Canton [S]
- 2026-10-28: DTCC Tokenization Service en producción con Canton [P]

**Quién la usa:**
- Infraestructuras de mercado: DTCC (DTC); Broadridge (DLX) [S] (producción) [P]
- Bancos y custodios: BNP Paribas (nodo propio); 20 participantes de DTC con acuerdo de acceso; J.P. Morgan (plan JPM Coin) (producción / acuerdo / plan) [P]
- Redes de pago: Visa (piloto (alta anunciada)) [P]

**Para qué sirve mejor (razonado):**
- Colateral, margen, repo y préstamo de valores entre instituciones: Operaciones de producción con DTCC [P]; 2 liquidaciones bancarias realizadas con fuente primaria (pruebas-bancos.json) [P].
- Registro de valores existentes con privacidad: 374.118 M$ representados [S]; privacidad entre participantes [P, docs.canton.network].

**Límites conocidos:**
- No es una red abierta: los participantes necesitan permisos [P]
- Volumen de transacciones de DTC en Canton y si los dominios privados pagan tráfico en CC: sin dato [P]
- Digital Asset, su desarrollador, es parte interesada [P]

### Chainlink (capa de interoperabilidad, no cadena)

**Aporta (razonado):** No es una cadena. Aporta lo que ninguna de las otras ofrece a terceros a esa escala: oráculos (precios, prueba de reservas, NAV) y mensajería entre cadenas (CCIP en 78 redes), más un motor de orquestación (CRE) que conecta sistemas bancarios (Swift, DTCC, Kinexys) con varias cadenas a la vez. Quant dice ofrecer algo parecido con su propio software.

**Puntos fuertes (hechos):**
- Directorio CCIP en mainnet: 78 redes y 281 tokens — docs.chain.link, CCIP Directory (parte interesada), 2026-11-14 [P]
- CCIP: 16 operadores independientes por ruta — docs.chain.link, 2026-11-14 [P]
- La Collateral AppChain de DTCC (colateral 24/7) usará Chainlink; producción prevista en el 4T-2026 — DTCC, nota de 12-may-2026, 2026-05-12 [P]
- Prueba de entrega contra pago multicadena con pago en Kinexys (J.P. Morgan) y OUSG en la testnet de Ondo Chain — Chainlink, blog CRE-DvP, 2025-06-12 [P]
- 30,76 mil M$ de «valor total asegurado» (exposición de protocolos que usan sus oráculos; no es liquidez) — DefiLlama, página Chainlink, 2026-11-14 [S]

**Puntos flacos (hechos):**
- Muchos feeds SmartData dependen de una única fuente (emisor, administrador, custodio o auditor) — docs.chain.link, SmartData, 2026-11-14 [P]
- La conexión con el libro mayor de Swift es un anuncio de Chainlink, sin cita de Swift — Chainlink, nota de 28-sep-2026, 2026-09-28 [P]
- Algorand, IOTA y Ondo no figuran en el directorio CCIP; uso real de los carriles (volumen) sin dato — docs.chain.link, CCIP Directory (leído en Chrome), 2026-11-15 [P]

**Mejora reciente (12 meses):**
- 2026-05-12: DTCC anuncia que su Collateral AppChain usará Chainlink [P]
- 2026-09-28: Chainlink anuncia trabajo para conectar instituciones al libro mayor de Swift [P]
- 2026-09-30: Fulcrum: flujo de repo y colateral entre cadenas (CRE + CCIP + Data Streams); demostración con DTCC en Sibos 2026 [P]
- 2026-10-14: Chainlink en vivo en Stellar [P]

**Quién la usa:**
- Infraestructuras de mercado: DTCC (Collateral AppChain) (plan (4T-2026)) [P]
- Bancos: J.P. Morgan Kinexys (prueba DvP); Swift/UBS (piloto, según cadenas.json) (prueba / piloto) [P]
- Redes que integran CCIP: Ethereum, Solana, BNB Chain, Avalanche, Polygon, Hedera, XDC, Plume, entre 78 (producción (sin volumen por carril)) [P]

**Para qué sirve mejor (razonado):**
- Interoperabilidad y mensajería entre cadenas: 78 redes en CCIP [P].
- Datos de precio, reservas y NAV para RWA: SmartData [P], con dependencia de fuente única [P].
- Orquestación de colateral y entrega contra pago entre sistemas: DTCC AppChain [P]; Fulcrum [P]; DvP con Kinexys [P].

**Límites conocidos:**
- Si CRE y CCIP pasan a producción con bancos fuera de pilotos: sin dato [P]
- El slashing del staking de LINK solo afecta a operadores de nodo y a los servicios asegurados por staking [P]

### Ondo (emisor y protocolo, no cadena)

**Aporta (razonado):** No es una cadena sino un emisor: aporta deuda pública tokenizada (USDY 1.970 M$ en circulación; OUSG 312,85 M$) desplegada a la vez en varias redes (OUSG en 4, USDY en 12), lo que la convierte en un caso que conecta redes distintas. Su red propia (Ondo Network) está anunciada.

**Puntos fuertes (hechos):**
- USDY: 1.970 M$ en circulación con colateralización del 156,90 % (11-nov-2026); OUSG 312,85 M$ (13-nov-2026) — ondo.finance/usdy y /ousg (parte interesada), 2026-11-13 [P]
- Contratos oficiales: OUSG en Ethereum, Polygon, Solana y XRP Ledger; USDY en 12 redes (incluye Stellar, BNB Chain y Plume) — docs.ondo.finance/addresses, 2026-11-15 [P]
- Suscripción y reembolso instantáneos de OUSG en Ethereum (mínimo 5.000 $; tope global 50 M$ cada 24 h) — docs.ondo.finance, límites, 2026-11-14 [P]
- Reembolso transfronterizo de OUSG con Kinexys, Mastercard y Ripple (activo en XRPL, pago en USD) — Ondo, blog, 2026-05-06 [P]

**Puntos flacos (hechos):**
- Acceso restringido: OUSG solo para compradores cualificados; USDY prohíbe personas de EE. UU., Canadá y otras jurisdicciones — docs.ondo.finance, elegibilidad, 2026-11-14 [P]
- Los productos principales se controlan con multifirmas del equipo — Aragon OTF (resumen de buscador), 2026-11-14 [S]
- Ondo Chain/Network no figura en el directorio CCIP ni en la tabla CCTP — Chainlink y Circle (leídos en Chrome), 2026-11-15 [P]
- Reembolso instantáneo solo en Ethereum; por encima de los topes hay que pedirlo al emisor — docs.ondo.finance, 2026-11-14 [P]

**Mejora reciente (12 meses):**
- 2026-05-06: Reembolso transfronterizo de OUSG con Kinexys, Mastercard y Ripple [P]
- 2026-07-27: Ondo presenta Ondo Network como evolución de Ondo Chain [S]

**Quién la usa:**
- Inversores cualificados e institucionales: Compradores de OUSG (criterio de patrimonio > 5 M$ personas o > 25 M$ entidades) (producción) [P]
- Bancos y redes de pago (piloto): J.P. Morgan Kinexys; Mastercard (MTN) (piloto) [P]
- Comercio: Liquidaciones a comercios de Shopify convertidas a USDY (descripción comercial, sin volumen) (anunciado) [P]

**Para qué sirve mejor (razonado):**
- Tesorería y colateral en deuda pública tokenizada en varias redes: USDY en 12 redes y OUSG en 4 [P]; OUSG invierte en BUIDL, BENJI y otros fondos [P].

**Límites conocidos:**
- Si Ondo Chain/Network está en producción y qué papel tendría ONDO: sin dato [P]
- Los rendimientos (OUSG 3,70 % y USDY 3,75 % APY) son anunciados por el emisor; no es recomendación [P]

### Algorand

**Aporta (razonado):** Prueba de participación pura con finalidad por bloque (~2,7 s medida) y control del emisor en cada activo (congelar, recuperar y congelado por defecto para KYC). Es la única de las 16 con cuentas resistentes a la computación cuántica (Falcon) integradas en el protocolo desde la v5.0.0 (aprobada el 15-ago-2026), y aloja dinero electrónico europeo (Quantoz EURQ/USDQ, licencia EMI de DNB según el emisor).

**Puntos fuertes (hechos):**
- Bloque cada 2,737 s, final al certificarse; tarifa mínima 0,001 ALGO ≈ 0,00008 USD — algonode, en comparativa-liquidacion.json, 2026-11-15 [P]
- Activos ASA con cuenta de congelación (incluido congelado por defecto) y de recuperación (clawback) — dev.algorand.co, assets, 2026-11-14 [P]
- v5.0.0 aprobada (90 % de apoyo el 15-ago-2026): cuentas Falcon-1024 resistentes a computación cuántica en el protocolo y comisiones según uso de recursos (los pagos simples no cambian) — Algorand, blog del 16-ago-2026 (leído 15-nov-2026; parte interesada), 2026-08-16 [P]
- State Proofs: pruebas firmadas por el consenso para clientes ligeros entre cadenas — Repositorio algorandfoundation/devportal, 2026-11-15 [P]
- Un solo incidente en 12 meses (HermesVault, 30.000 $, 26.000 $ recuperados) — DefiLlama hacks, en cadenas-incidentes.json, 2026-05-19 [S]

**Puntos flacos (hechos):**
- Stablecoins 121 M$ (casi todo USDC); USDQ de Quantoz figura con 1 $ en DefiLlama — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- 39,4 M$ en RWA distribuidos (1 activo) en RWA.xyz; otras fuentes dan cifras distintas — RWA.xyz y cadenas.json (sesgos), 2026-11-14 [S]
- No figura en el directorio CCIP ni en la tabla CCTP, ni en las listas de DTCC, Ondo y BENJI leídas — Chainlink, Circle y comparativa-liquidacion.json, 2026-11-15 [P]
- El bono al proponente lo dota la Fundación y su documentación lo llama «insostenible» solo con comisiones — dev.algorand.co, staking rewards, 2026-11-14 [P]
- Único hecho bancario: piloto de VersaBank (fuente secundaria) — pruebas-bancos.json, 2025-08-26 [S]

**Mejora reciente (12 meses):**
- 2026-01: La Algorand Foundation pasa su sede a Delaware (EE. UU.); antes Singapur [S]
- 2026-06: La Fundación presenta una hoja de ruta para ser resistente a la computación cuántica a finales de 2027 [S]
- 2026-08-15: v5.0.0 aprobada por el 90 % (activa tras ~7 días de enfriamiento; día exacto en mainnet no leído) [P]
- 2026-10-28: go-algorand 5.0.5 [P]

**Quién la usa:**
- Emisores de dinero electrónico: Quantoz (EURQ, USDQ, EURD; licencia EMI de DNB según el emisor) (producción según el emisor) [P]
- Custodios: Hex Trust (custodia regulada y staking institucional) (producción) [P]
- Bancos: VersaBank (piloto de recibos de depósito) (piloto) [S]
- Inmuebles tokenizados: Lofty (250 propiedades, 100,6 M$ según el panel de la Fundación) (producción según la Fundación) [S]

**Para qué sirve mejor (razonado):**
- Activos con control del emisor y pagos baratos con finalidad inmediata: ASA con congelación/recuperación [P]; 2,7 s y 0,00008 USD [P].
- Identidad y seguridad de cuentas a largo plazo: Cuentas Falcon-1024 en el protocolo [P].

**Límites conocidos:**
- No hay API pública simple del número de proponentes/validadores [S]
- Pilotos con bancos o con ISO 20022: sin dato [P]

### XDC Network

**Aporta (razonado):** Red EVM orientada a la financiación del comercio: XDC Ventures anunció la compra de Contour (cartas de crédito digitales de un consorcio bancario) y ofrece subredes conectadas con XDC Zero. Comisión documentada de unos 0,00004 $ por transferencia y presencia en CCIP y CCTP.

**Puntos fuertes (hechos):**
- Transferencia simple ≈ 0,00004 US$ según la documentación (no medida) — docs.xdc.network, Gas & Fees, 2026-11-14 [P]
- 108 masternodes activos, 257 en espera y 4 penalizados — RPC público, en cadenas-validadores.json, 2026-11-15 [P]
- En el directorio CCIP (2 carriles salientes) y en CCTP de Circle (dominio 18) — Chainlink y Circle (leídos en Chrome), 2026-11-15 [P]
- Stablecoins 103,2 M$ (USDC 52,8 M$, USDf 49,8 M$) — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]

**Puntos flacos (hechos):**
- No aparece entre las 37 redes con valor en RWA.xyz — RWA.xyz, 2026-11-14 [S]
- No se halló banco ni banco central con fuente primaria (la vinculación de Standard Chartered no está confirmada) — pruebas-bancos.json, 2026-11-15 [P]
- TVL DeFi 1,9 M$ — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- Última versión oficial del cliente v2.7.1 (4-jun-2026); la v3.0.0 sigue en testnet — GitHub XinFinOrg/XDPoSChain, en cadenas-gobernanza.json, 2026-06-04 [P]
- La compra de Contour es un anuncio de parte interesada sin precio ni cierre confirmado — EZ Newswire (XDC Ventures), 2025-10-22 [P]

**Mejora reciente (12 meses):**
- 2026-06-04: XDPoSChain v2.7.1 [P]
- 2026-11-15: Confirmada su presencia en CCIP y en CCTP de mainnet (fecha de lectura; fecha de alta sin dato) [P]

**Quién la usa:**
- Financiación del comercio: Contour (cartas de crédito digitales; propiedad anunciada de XDC Ventures) (anunciado) [P]
- Emisores de stablecoins: Circle (USDC); Falcon (USDf) (producción) [S]
- Custodios: Utila (MPC); BitGo (producción) [P]

**Para qué sirve mejor (razonado):**
- Financiación del comercio y documentos comerciales: Contour [P, anuncio propio]; sin bancos con fuente primaria [P].

**Límites conocidos:**
- Swift e ISO 20022 solo autodeclarados; finalidad de 6 s en un artículo y 2 s o 2-4 s en otras páginas [P]
- Material casi todo de la propia XDC y de webs promocionales [P]

### Quant (Overledger; capa de interoperabilidad, no cadena)

**Aporta (razonado):** No es una cadena: software para conectar sistemas bancarios con varias cadenas (Overledger, Fusion). Según Quant, The Clearing House la eligió para una red de depósitos tokenizados conectada a RTP y CHIPS, disponible en el 1S-2027; sería la única de las 16 ligada a los sistemas de pago interbancario privados de EE. UU.

**Puntos fuertes (hechos):**
- The Clearing House elige a Quant para su On-Chain Money Initiative (red de depósitos tokenizados conectada a RTP y CHIPS; 1S-2027) — Quant, nota (sin confirmación de TCH leída), 2026-09-24 [P]
- Fusion Rollup en mainnet; dice conectar 74 redes — Quant, nota, 2026-06-02 [P]
- Miembro fundador de INATBA y asociado de UK Finance (no es estatus regulatorio) — quant.network/associations, 2026-11-14 [P]

**Puntos flacos (hechos):**
- Sin clientes en producción con fuente primaria — cadenas.json (sin_dato), 2026-11-14 [P]
- Sin documento primario del modelo de token: quant.network/overledger da «no encontrada» y docs.quant.network no resuelve — Lectura en Chrome (cadenas.json), 2026-11-14 [P]
- No consta licencia ni registro regulatorio en su web — quant.network/associations, 2026-11-14 [P]

**Mejora reciente (12 meses):**
- 2026-06-02: Fusion Rollup en mainnet [P]
- 2026-09-24: Anuncio con The Clearing House [P]

**Quién la usa:**
- Bancos (infraestructura interbancaria): The Clearing House (según Quant) (plan (1S-2027)) [P]
- Operadores de nodo: Operadores de confianza con stake de QNT (producción según Blockworks) [S]

**Para qué sirve mejor (razonado):**
- Conectar sistemas bancarios y depósitos tokenizados con varias cadenas: TCH (según Quant) [P]; Fusion [P]; descripción comercial sin volumen.

**Límites conocidos:**
- Afirmaciones propias sin auditoría ni cliente nombrado en Fusion [P]

### IOTA

**Aporta (razonado):** Registro de documentos de comercio e identidad digital en programas públicos: ADAPT, con la Secretaría del AfCFTA, el Tony Blair Institute y el WEF (Kenia, Nigeria y Marruecos), según el blog de IOTA. Es la única de las 16 centrada en comercio e identidad en África; no tiene integración bancaria verificada.

**Puntos fuertes (hechos):**
- Consenso Starfish en la red principal desde el 23-abr-2026 — Blog de IOTA (parte interesada), 2026-04-23 [P]
- Kenia, Marruecos y Nigeria primeros países de ADAPT (identidad digital, datos de comercio y pagos) — Blog de IOTA; socios no leídos en sus webs, 2026-05-19 [S]
- 60 validadores activos; coeficiente de Nakamoto (1/3) = 7 — RPC público, en cadenas-validadores.json, 2026-11-15 [P]
- Versiones de mainnet frecuentes (v1.34.1 el 21-oct y v1.35.2 el 4-nov-2026) — GitHub iotaledger/iota, en cadenas-gobernanza.json, 2026-11-04 [P]

**Puntos flacos (hechos):**
- Stablecoins 0,42 M$ y TVL 1,1 M$ (solo IOTA EVM) — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- No aparece en RWA.xyz — RWA.xyz, 2026-11-14 [S]
- No figura en CCIP ni en CCTP — Chainlink y Circle (leídos en Chrome), 2026-11-15 [P]
- No se halló banco ni banco central — pruebas-bancos.json, 2026-11-15 [P]
- Virtue: 894.500 $ por configuración errónea de oráculo (28-ago-2026) — DefiLlama hacks, en cadenas-incidentes.json, 2026-08-28 [S]

**Mejora reciente (12 meses):**
- 2026-04-23: Consenso Starfish en mainnet [P]
- 2026-05-19: Primeras implementaciones de ADAPT (Kenia, Marruecos, Nigeria) [P]
- 2026-11-04: IOTA mainnet v1.35.2 [P]

**Quién la usa:**
- Organismos públicos y de comercio: Secretaría del AfCFTA, Tony Blair Institute, WEF (según IOTA) (implementación en marcha) [S]
- Exportadores: TWIN (flores de Kenia, según agregadores) (sin verificar) [V]

**Para qué sirve mejor (razonado):**
- Identidad digital y trazabilidad de documentos de comercio: ADAPT [S]; TWIN [V].

**Límites conocidos:**
- Integración con ISO 20022, con bancos o con EBSI de la UE: sin resultado [P]
- Objetivos como «1.500 M de personas en 2035» son promocionales [P]

### Plume

**Aporta (razonado):** Red EVM dedicada solo a activos reales, con monitorización de sanciones y AML en la red y distribución de RWA a otras cadenas (SkyLink). Una empresa de su grupo (Kimber Transfer Agency) figura como agente de transferencia registrado ante la SEC según la prensa; sería la única de las 16 con esa figura propia [VERIFICAR en sec.gov].

**Puntos fuertes (hechos):**
- 114,1 M$ en crédito tokenizado en 29 activos — RWA.xyz, 2026-11-14 [S]
- Monitoriza sanciones (OFAC) y AML con Forta, Predicate, TRM, Chainalysis y Elliptic; admite valores bajo Reg. D 506(b)/(c) — docs.plume.org, Compliance (parte interesada), 2026-11-14 [P]
- Kimber Transfer Agency (100 % de Plume Network Inc.) con registro de agente de transferencia efectivo el 26-sep-2025, según prensa que cita un documento de la SEC — Cointelegraph y otros (vía buscador, 15-nov-2026); sec.gov no accesible (503), 2025-10-06 [S]
- USDY de Ondo desplegado en Plume; Plume en CCIP (7 carriles) y CCTP (dominio 22) — docs.ondo.finance/addresses; cadenas.json (capas), 2026-11-14 [P]
- Sin incidentes registrados en DefiLlama en 12 meses — DefiLlama hacks, en cadenas-incidentes.json, 2026-11-15 [S]

**Puntos flacos (hechos):**
- Stablecoins 10,8 M$ y TVL 1,1 M$ — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- Las cifras de activos varían mucho según el agregador (177 M$ o 577 M$) — CoinPaprika (resumen de buscador), 2026-08 [V]
- Volumen DEX -94 % en 30 días — DefiLlama, en cadenas-onchain.json, 2026-11-15 [S]
- Instituciones que la usan solo con fuente secundaria (UBS AM vía DigiFT, WisdomTree vía OpenTrade) — pruebas-bancos.json, 2026-11-15 [S]

**Mejora reciente (12 meses):**
- 2026-11-15: Sin hito con fuente primaria en los últimos 12 meses en el repo; el registro de agente de transferencia (26-sep-2025) y SkyLink (27-ene-2025) quedan fuera de la ventana [P]

**Quién la usa:**
- Gestoras (vía intermediarios): UBS Asset Management (uMINT vía DigiFT); WisdomTree (vía OpenTrade) (producción [VERIFICAR]) [S]
- Emisores: Ondo (USDY); emisores de crédito tokenizado (producción) [P]

**Para qué sirve mejor (razonado):**
- Crédito y RWA en DeFi con filtros de sanciones: 114,1 M$ de crédito [S]; compliance documentado [P].

**Límites conocidos:**
- El estándar ERC-3643 está anunciado (nov-2024), sin constancia de que esté operativo [S]
- Integración con ISO 20022 e instituciones con fuente primaria: sin dato [P]

## 6. Lo que no sabemos

- Volumen real de liquidación por red (se conoce lo emitido, no lo movido), y cuánto es pago entre bancos.
- Volumen de ODL en XRP: Ripple no lo separa del total de Ripple Payments.
- Volumen de las operaciones de DTC en Canton y uso real de los carriles CCIP y CCTP.
- Finalidad real de Solana (no medible con el RPC público) y de Hedera (medida indirecta).
- Capas 2 de Ethereum: no medidas; la comparación es de capa 1.
- Registro de agente de transferencia de Plume/Kimber en sec.gov (servidor no accesible el 15-nov-2026) [VERIFICAR].
- Día exacto de activación en mainnet de Algorand v5.0.0 y de Helicon en Avalanche.
- Número de miembros del Consejo de Hedera, validadores reales de Polygon y BNB Chain, y proponentes de Algorand.
- Si los pilotos antiguos (Palau, Ucrania, Kazajistán, bancos centrales con Ripple) siguen activos.
- Clientes en producción de Quant y estado de Ondo Network.
- Celdas «sin dato» de la matriz: Solana, Hedera y otras pueden tener capacidades (p. ej. control del emisor por extensiones de token) que el repo aún no recoge con fuente.

## Fuentes externas leídas en esta tarea
- Algorand, «Algorand v5.0.0 is here» (16-ago-2026): https://algorand.co/blog/algorand-v5.0.0-is-here.-heres-what-it-means-for-you
- Búsqueda sobre Plume/Kimber como agente de transferencia (prensa: Cointelegraph https://cointelegraph.com/news/plume-network-sec-transfer-agent); sec.gov devolvió 503 → [VERIFICAR].
