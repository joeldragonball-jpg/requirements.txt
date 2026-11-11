---
titulo: C42 Rendimientos y colateral (XRP/XLM y cripto)
fecha: 2026-11-11
etiquetas: [rendimientos, colateral, staking, lending, amm, xrpl, stellar, mica, etf]
---
# C42 · Rendimientos y colateral: XRP, XLM y cripto en general (11-nov-2026)

Alcance: sesión corta, WebSearch/WebFetch (sin Chrome). Nivel [P] solo donde leí la fuente primaria (xrpl.org, DefiLlama API). Resto [S]/[VERIFICAR]. No es recomendación de compra/venta ni de contratar nada.

## 1. Lo esencial (HECHOS)
- **XRP y XLM no tienen staking de protocolo** (consenso por validadores/FBA, sin bloqueo de tokens para cobrar recompensa). Todo «rendimiento» sobre XRP/XLM viene de otra cosa: prestar, dar liquidez o estrategias de terceros. [S] (no abrí un documento que lo diga expresamente; consistente con la documentación de ambas redes) [VERIFICAR con fuente primaria]
- **AMM del XRPL (XLS-30)**: enmienda activada el 22-03-2024. Los LP depositan dos activos, reciben tokens LP y cobran las comisiones de trading como mayor valor del pool; comisión fijada por votación de LPs entre 0 % y 1 %; hay una «subasta» de 24 h que reduce la comisión a 1/10 para el ganador; la propia documentación habla de «riesgo de divisa» (el equivalente a la pérdida impermanente) que las comisiones pueden o no compensar. [P] xrpl.org/docs/concepts/tokens/decentralized-exchange/automated-market-makers (leído 11-nov-2026). Sin APY oficial: depende del volumen del par.
- **Lending nativo del XRPL (XLS-66) y vaults (XLS-65)**: introducidos en rippled 3.1.0 (ene-2026). Según la tabla de enmiendas de xrpl.org, con una captura fechada 16-sep-2026, LendingProtocol estaba «en votación» con 37,14 % y SingleAssetVault con 45,71 % (se necesita 80 % durante 14 días). [P] xrpl.org/resources/known-amendments, pero la captura es de hace ~2 meses: [VERIFICAR] estado actual hoy. Dominios y DEX con permisos (PermissionedDomains 04-02-2026, PermissionedDEX 18-02-2026) sí están activados [P].
- **Evernorth** (tesorería de XRP respaldada por Ripple, cotizada en Nasdaq): declara que buscará aumentar los XRP por acción con préstamos, provisión de liquidez y DeFi en el XRPL; depende de XLS-66. Intenciones anunciadas, no resultados. [S] prensa (Blockworks, Datawallet, Yahoo, mar-2026); la fecha de debut (12-oct) y los ~473 M XRP son [VERIFICAR].
- **Stellar, DeFi**: TVL de la cadena ≈ 212,6 M USD frente a ≈ 32,9 M USD del XRPL (Ethereum ≈ 41.359 M; Solana ≈ 5.130 M). [P] DefiLlama api.llama.fi/v2/chains, 11-nov-2026. Blend Pools V2 (préstamos, cadena Stellar): TVL ≈ 117,2 M USD el 11-nov (dos auditorías; oráculos RedStone y Reflector); su TVL cuenta lo depositado, no lo prestado. [P] api.llama.fi/protocol/blend-pools-v2. Bajó ≈ 20 % en 30 días según la web de DefiLlama (8-nov) [S].
- **Incidentes en Stellar DeFi**: fuentes secundarias hablan de un exploit en el pool Comet (BLND-USDC, ≈ 0,72 M USD) y de un incidente de 10,97 M USD (22-feb-2026, «manipulación de oráculo») en DefiLlama; no pude reconciliarlos. [VERIFICAR]. La cifra de TVL de Stellar de 270 M (22-ago) frente a 98 M (27-ago) es incoherente con la serie de DefiLlama: no usar.
- **Tasas DeFi de referencia (puntuales, no XRP/XLM)**: Aave v3 USDC en Ethereum ≈ 3,84 % base (instantánea de 23-oct-2026, ≈ 2,4 B USD depositados); ETH ≈ 1,2–1,45 % base. [S] agregador DeFi Rate. Las tasas cambian cada bloque; ver DefiLlama Yields en vivo.

## 2. ETF, staking y colateral
- **EE. UU.**: estándares genéricos de cotización para ETP de materias primas aprobados por la SEC el 17-sep-2025 (sin 19b-4 individual). Staking en ETF de ETH operativo desde oct-2025; una interpretación conjunta SEC-CFTC de mar-2026 habría sacado el staking de la categoría de valores. [S] (cointelegraph, natlawreview, Jito); una enmienda de jul-2026 (15 % de «commodities digitales» no elegibles) solo aparece en un blog interesado (Jito): [VERIFICAR] contra el registro de la SEC.
- **ETF de XRP al contado** (Canary, Franklin, 21Shares, Bitwise, Grayscale): no encontré que ninguno haga staking ni lending (no hay staking posible en XRP). [S]. Que un ETF sirva de colateral para préstamo depende de cada bróker/banco: no verificado. [VERIFICAR]
- **UE / MiCA**: el periodo transitorio acabó el 01-07-2026 sin prórroga; ESMA (17-abr y 23-jun-2026) exige a los CASP no autorizados cerrar de forma ordenada. [S] vía AMF, Banco de Irlanda, Elvinger Hoss (no abrí el PDF de ESMA). En su respuesta a la consulta de revisión de MiCA (sep-2026), ESMA pide reglas específicas para staking, lending y borrowing y describe los programas de préstamo como «cajas negras» para el cliente [S, citada por Mondaq/The TRADE]: es propuesta, no norma. Cifra de ≈ 210 CASP autorizados (mayo-2026): [VERIFICAR] con el registro de ESMA.
- **Otras jurisdicciones (Reino Unido, Singapur, Hong Kong, Japón, Corea, Emiratos)**: no investigadas en esta pasada por límite de sesión. Quedan como filas vacías [VERIFICAR].
- **España**: staking = rendimiento de capital mobiliario (art. 25.2 LIRPF) valorado a mercado al percibirlo (DGT V1766-22, V0376-24) [S]; la tributación de comisiones de AMM/lending DeFi no está fijada por consulta clara. Cambia la conclusión solo si se usa un servicio que reparte rendimiento periódico: se tributa al cobrarlo aunque no se venda. Detalle en informes/research/2026-11-11-C232-fiscalidad-cripto-espana.md.

## 3. Caso alcista vs. bajista (sobre usar XRP/XLM como activo productivo)
- **Alcista**: el XRPL añade piezas nativas (AMM ya activo; vaults y préstamos con auditoría Halborn de ene-2026, dominios y DEX con permisos) pensadas para crédito institucional; Stellar ya tiene ≈ 213 M de TVL y un mercado de préstamos en producción; Evernorth sería un comprador/prestamista grande de XRP. [S/ESPECULACIÓN en el efecto]
- **Bajista**: el TVL del XRPL (≈ 33 M) es ínfimo frente a Ethereum (≈ 1/1.250); LendingProtocol seguía sin 80 % de apoyo en sep-2026 [P, a re-verificar]; Stellar sufrió incidentes y una caída de TVL; los ETF de XRP no generan rendimiento; ESMA califica los programas de préstamo de opacos. [HECHOS/S]

## 4. Riesgos por modalidad
- **Earn / lending CeFi**: contraparte y custodia (los fondos se prestan, el cliente es acreedor no propietario), regulatorio (CASP no autorizado en la UE desde 01-07-2026), opacidad. Rendimientos de marketing (APY) suelen incluir recompensas en tokens y promociones.
- **Lending DeFi (Blend, Aave)**: contrato inteligente, oráculos (manipulación), liquidaciones, depeg de la stablecoin. TVL ≠ fondos prestados.
- **AMM (XRPL, Stellar)**: «riesgo de divisa»/pérdida impermanente, liquidez baja en pares poco usados, arbitraje.
- **Colateral**: ratio de liquidación con cripto volátil; si el prestamista rehipoteca, riesgo de contraparte; fiscalidad española: la liquidación forzosa es transmisión.
- **Sesgos de fuente**: exchanges, Evernorth, Jito, MEXC y similares son parte interesada; muchas webs de «noticias» son reposts. Fechas y cifras de prensa cripto, siempre [VERIFICAR] con on-chain/oficial.

## 5. Filas propuestas (JSON; NO crear panel sin OK)
```json
[
{"modalidad":"AMM nativo","activo":"XRP","jurisdiccion":"Global (XRPL)","estado":"Activo desde 22-03-2024","norma":"Enmienda AMM (XLS-30)","fecha":"2026-11-11","fuente":"xrpl.org docs AMM","url":"https://xrpl.org/docs/concepts/tokens/decentralized-exchange/automated-market-makers","nivel":"P","riesgo":"Riesgo de divisa; sin APY oficial","revisar":"trimestral"},
{"modalidad":"Lending nativo + vaults","activo":"XRP","jurisdiccion":"Global (XRPL)","estado":"En votación (37,14 % / 45,71 % a 16-sep-2026)","norma":"XLS-66 / XLS-65 (rippled 3.1.0)","fecha":"2026-09-16","fuente":"xrpl.org known-amendments","url":"https://xrpl.org/resources/known-amendments","nivel":"P","riesgo":"Aún no activo; contrato/contraparte; re-verificar","revisar":"mensual"},
{"modalidad":"Lending DeFi","activo":"XLM/USDC","jurisdiccion":"Global (Stellar)","estado":"Activo; TVL 117,2 M USD","norma":"n/d","fecha":"2026-11-11","fuente":"DefiLlama Blend Pools V2","url":"https://api.llama.fi/protocol/blend-pools-v2","nivel":"P","riesgo":"Oráculo/exploits [VERIFICAR]","revisar":"mensual"},
{"modalidad":"Staking nativo","activo":"XRP/XLM","jurisdiccion":"Global","estado":"No existe","norma":"n/d","fecha":"2026-11-11","fuente":"docs de las redes","url":"","nivel":"S","riesgo":"Cualquier 'staking' de XRP/XLM es producto de tercero","revisar":"semestral"},
{"modalidad":"Staking/lending custodial","activo":"Cripto","jurisdiccion":"UE (MiCA)","estado":"Solo CASP autorizado desde 01-07-2026; reglas específicas solo propuestas","norma":"Reglamento (UE) 2023/1114; declaraciones ESMA 17-abr y 23-jun-2026","fecha":"2026-07-01","fuente":"AMF/Banco de Irlanda sobre ESMA","url":"https://www.amf-france.org/en/news-publications/news/end-mica-transitional-period-esma-sets-out-its-expectations-professionals-and-warns-retail-investors","nivel":"S","riesgo":"Contraparte y opacidad","revisar":"trimestral"},
{"modalidad":"ETF spot con staking","activo":"ETH/otros","jurisdiccion":"EE. UU.","estado":"Estándares genéricos desde 17-sep-2025; staking en ETF ETH desde oct-2025","norma":"Orden SEC de estándares genéricos","fecha":"2025-09-17","fuente":"cointelegraph / natlawreview","url":"https://cointelegraph.com/news/sec-approves-generic-etf-listing-standards-clearing-path-for-digital-asset-listings-without-individual-approval","nivel":"S","riesgo":"Cambio de criterio; el ETF de XRP no stakea","revisar":"trimestral"}
]
```

## 6. Pendientes
Reino Unido, Singapur, Hong Kong, Japón, Corea y Emiratos; préstamos con garantía cripto de bancos/brókers; fondos monetarios y letras tokenizadas; leer PDF de ESMA y orden de la SEC; comprobar el estado actual de XLS-66 (xrpl.org/xrpscan); tasa de pools AMM del XRPL con datos DefiLlama/XRPScan.

Resumen: (1) XRP/XLM no tienen staking de protocolo; el rendimiento viene de AMM (XRPL activo desde 2024), préstamos (Blend en Stellar ≈ 117 M USD; XLS-66 del XRPL aún en votación a sep-2026) o terceros.
(2) TVL: Stellar ≈ 213 M vs XRPL ≈ 33 M (DefiLlama, 11-nov); riesgos principales contraparte, oráculo/contrato, pérdida por divisa, MiCA (CASP desde 01-07-2026).
(3) Faltan seis jurisdicciones y verificar fuente primaria de varios datos (SEC, ESMA, estado XLS-66); filas JSON propuestas, sin panel.
