# Ripple, XRP Ledger y Stellar: novedades a 27-nov-2026

Etiquetas: [P] primaria, [D] dato de tercero, [S] secundaria/agregador, [VERIFICAR], [ESPECULACIÓN]. Sin recomendaciones. Investigación del 27-nov-2026; los resúmenes de página los hizo un lector automático (cotejar antes de citar).

## 1. Ripple (Swell 2026, 27-29-oct, Nueva York)
HECHOS
- Recap oficial de Ripple fechado 16-nov-2026 [P] https://ripple.com/insights/ripple-swell-2026-recap/ : la OCC concedió aprobación final a Ripple National Trust Bank, anunciada "justo antes del evento" (sin fecha exacta); Ripple prevé cerrar 2026 cerca de 900 M USD de run rate anualizado de producto (~3x vs un año antes; es una proyección); más de 1.700 clientes; más de 1.500 asistentes.
- Socios citados en el recap [P], sin fecha: Cross River Bank integra RLUSD en su banca; C2FO Instant Pay liquida en RLUSD sobre XRPL; DBS y Franklin Templeton con un fondo monetario tokenizado que usa RLUSD; BNY da soporte a XRP en custodia; Aviva Investors lanzó clase tokenizada de su Sterling Liquidity Fund en XRPL; Ripple Treasury (plataforma 24/7, "24/7 Returns"); Water.org (6 M USD en 3 años y 1,25 M USD en RLUSD; >3 M USD movidos en Latinoamérica con Ripple Payments, fees hasta -66 %).
- Coinbase añade RLUSD en Prime, Exchange y app minorista, conversión 1:1, sobre XRPL, Ethereum y Base, 28-oct-2026 [D] https://theblock.co/news/business/2026-10-28-coinbase-adds-ripple-rlusd-stablecoin-432009 (nota de prensa de Ripple: https://ripple.com/ripple-press/ripple-and-coinbase-partner-to-expand-access-to-rlusd/). El recap oficial NO menciona Coinbase.
- Robinhood amplía alianza: RLUSD ya en Robinhood Chain y Bitstamp; app minorista prevista "más adelante en 2026"; liquidación institucional en XRPL; 27-oct-2026 [D] https://cointelegraph.com/news/ripple-robinhood-expand-partnership-rlusd-retail-institutional-markets . No implica que Robinhood compre XRP.
- Ripple Insights recientes: 5-oct (Türkiye), 14-oct (stablecoins en LatAm), 21-oct (custodia), 16-nov (recap) [P] https://ripple.com/insights/
OPINIÓN/DUDOSO
- Calificación Moody's A2/P-1 para RLUSD: solo en un agregador (Digg) [S] https://digg.com/world-business/p4aatxib [VERIFICAR].
- Capitalización RLUSD "más de 2.500 M USD" según agregadores [S] [VERIFICAR] (en mayo-2026 se citaban 1.600 M, 247wallst 26-may-2026).
- Adquisiciones: no hallé ninguna anunciada en nov-2026. En 2026 se citan Solvexia y BC Payments (1.er trimestre) [S]; Garlinghouse dijo que se frenarían [S] https://dlnews.com/articles/markets/ripple-acquisitions-to-slow-in-2026-ceo-says/ [VERIFICAR].
- Valoración: el recap no la menciona. La cifra de 40.000 M USD (ronda de 500 M) es de Swell/2025 [S] [VERIFICAR] si hay dato 2026.
- Tesorería XRP de Ripple: sin dato nuevo hallado. [VERIFICAR] (escrows mensuales, informes XRP Markets).
- Lending Protocol y Single Asset Vault "sujetos a aprobación de validadores" según recap [P].

## 2. XRP Ledger
HECHOS [P] https://xrpl.org/blog (consultado 27-nov)
- 16-sep-2026: versión 3.4.0. 25-sep-2026: 3.4.1 (emergencia, parches de seguridad); 9-oct-2026: informe de vulnerabilidades de xrpld 3.4.1 (validación de envoltorio de transacción interna de Batch y desbordamiento de XRP en motor de pagos). 21-sep-2026: informe sobre XLS-68 Sponsored Fees and Reserves (bug reportado 7-ago).
- 9-nov-2026: aviso de reinicio de Testnet y Devnet el 25-nov-2026. 24-nov-2026: caso de estudio Heurist/t54 (pagos de inferencia IA en XRPL).
- Notas de 3.4.1: añade fixBatchV1_2 (voto por defecto "Sí"), supermayoría ya lograda, activación prevista 9-oct-2026; actualizar urgente. [P] https://xrpl.org/blog/2026/xrpld-3.4.1 . Incoherencia: la tabla de amendments habla de BatchV1_1 prevista 29-sep. [VERIFICAR] cuál se activó.
- Activadas en 2026 (tabla known-amendments, instantánea 16-sep) [P] https://xrpl.org/resources/known-amendments : lote del 27-ene; PermissionedDomains 4-feb; TokenEscrow 12-feb; PermissionedDEX 18-feb; fixCleanup3_1_3 27-may; fixCleanup3_2_0 29-jul; fixCleanup3_3_0 11-sep.
- Abiertas a voto el 16-sep: PermissionDelegationV1_1 62,86 %; SingleAssetVault 45,71 %; LendingProtocol 37,14 %; ConfidentialTransfer 31,43 %; DynamicMPT 31,43 %; Sponsor 17,14 %; XChainBridge 14,29 %; LendingProtocolV1_1 0 %. Regla: activación tras 2 semanas con supermayoría (80 %).
- Sin entradas de amendments ni XLS nuevos en el blog de sep-nov. No hallé activaciones en nov-2026. [VERIFICAR] estado actual en el tracker (xrpscan/xrpl.org) porque mi dato de apoyo es de 16-sep.
- Nota: rippled pasó a llamarse xrpld [P].
- Aviso: una fuente secundaria alerta de que 3.4.1 deja de contar votos de un validador tras rotar clave [S] [VERIFICAR].

## 3. Stellar / SDF
HECHOS [P] https://stellar.org/blog
- Protocol 25 "X-Ray": voto 22-ene-2026. Protocol 26 "Yardstick": voto 6-may-2026 (CAP-0077, lista de claves de ledger congeladas por consenso).
- Protocol 30 "Bell" (guía 20-oct-2026): CAP-84 direcciones de contrato multiplexadas; CAP-87 verificación de firmas poscuánticas ML-DSA en contratos (firmas de red siguen Ed25519); CAP-88 tiempos de ledger en milisegundos. Core v30.0.0 estable 16-oct; voto testnet 3-nov 17:00 UTC; voto mainnet 23-nov-2026 17:00 UTC (fechas "sujetas a cambio"). Resultado del voto de mainnet: NO confirmado en mis fuentes [VERIFICAR] (stellar-validators y stellar.org/protocol-upgrades). Hay una fuente que habla de 4 y 24 nov [S].
- Posts: 14-oct Chainlink en vivo en Stellar (ecosistema RWA >4.000 M USD); 28-oct Project Thruput (computación); 29-oct Freighter pasa a llamarse Varial; 23-nov Soroban Rust SDK v30; 16-nov "Q3 2026: The rail, put to work".
- Cifras de ese informe de SDF [P, autoinformadas] https://stellar.org/blog/foundation-news/q3-2026-the-rail-put-to-work : RWA 4.100 M USD a fin de sep, >5.000 M a primeros de nov, cuota 12,7 % de RWA tokenizados (4,9 % un año antes); volumen mensual de pagos 18.500 M USD en octubre (89 % más que sep); stablecoins Q3 25.100 M USD; 50.000 transacciones BENJI costaron 1,13 USD a Franklin Templeton frente a ~75.000 USD con agente de transferencias tradicional; socios: U.S. Bank (USBDC, 9-sep), DTCC, State Street/Galaxy, BVNK, MoneyGram, Spiko/Amundi, UNDP, MetaMask. Sesgo: datos de promoción propia; "volumen de pagos" no equivale a uso económico neto.

## Caso alcista / bajista (resumen)
- Alcista: licencia fiduciaria, RLUSD en Coinbase/Robinhood, custodia BNY, tokenización en XRPL y Stellar con cifras al alza.
- Bajista/matices: RLUSD no se traduce necesariamente en demanda de XRP; varias cifras son autoinformadas o proyecciones; 3.4.1 requirió parches de seguridad de emergencia; amendments clave (Lending, Vault) lejos del 80 %; no hay confirmación de Bell.

[VERIFICAR] resultado del voto de Bell (23-nov); estado actual de Lending/Vault/Sponsor en el tracker; Moody's A2 y OCC (fecha exacta); BatchV1_1 vs fixBatchV1_2; cifra de RLUSD; valoración de Ripple 2026; tesorería XRP.
