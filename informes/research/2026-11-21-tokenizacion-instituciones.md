# Tokenización de las finanzas tradicionales: qué hace cada actor (21-nov-2026)

Datos estructurados: `explorador/tokenizacion-instituciones.json` (29 actores, 78 iniciativas). Sin recomendaciones. Niveles: P = página oficial abierta hoy (el lector resume; citas literales devueltas); P(15-nov) = leída el 15-nov y recogida en `pruebas-bancos.json`; S = prensa o agregador; V = verificar.

## HECHOS (con fuente primaria)
- J.P. Morgan: JPM Coin (JPMD) llegó a Ethereum L1 el 19-oct-2026, tras Base (nov-2025); Kinexys: más de 4 billones de $ acumulados y 7.000 M$ diarios (cifras del banco). Fuente: jpmorgan.com/payments.
- Citi: Citi Token Services en 7 mercados el 28-sep-2026, "private-permissioned blockchain" (literal). Sin cifra concreta en el comunicado.
- HSBC: depósitos tokenizados en EE. UU. el 13-abr-2026; red propia, sin cadena pública nombrada.
- LSEG: Super Validator de Canton (28-sep-2026); DSD multi-cadena sin nombrar ninguna (12-feb-2026).
- BCE: Pontes en producción desde el 21-sep-2026 (Santander, Deutsche Bank, SG, BEI, KfW, Clearstream entre otros); Appia, plano en 2028.
- BIS: informe final de Agorá el 27-may-2026 (7 bancos centrales, más de 40 entidades privadas); sin cadena pública nombrada.
- DTCC: servicio de tokenización en vivo el 28-oct-2026 (Canton y Besu); Stellar 1S-2027, Solana 2S-2027 (plan).
- Clearstream, Euroclear y DTCC: libro blanco de interoperabilidad (4-mar-2026).
- Swift: libro mayor con 17 bancos (9-jul-2026); el comunicado no nombra cadena pública.
- Visa: 7.000 M$ anualizados de liquidación con stablecoins en 9 redes (29-abr-2026).

## Lo que dice cada parte (separar banco vs terceros)
- Deutsche Bank. Dicho por el banco (declaración recogida por The Block, 16-sep-2026): custodia para clientes corporativos e institucionales europeos en 2026, "pendiente de autorización regulatoria"; BTC, ETH, USDC, EURC, EURAU; claves gestionadas por el banco; proveedores "externos" sin nombrar. Dicho por terceros: Taurus (Reuters, 2023) y Bitpanda (Bloomberg, jul-2025). Ripple/XRP: no aparece en lo leído; lo de "cinco años de preparación" y cualquier comentario del banco sobre Ripple no se ha podido atribuir al banco. [VERIFICAR] en su web.
- Swift frente a Ripple/Stellar: Swift no nombra ninguna de las dos en su comunicado. Compararlas es [ESPECULACIÓN]; operan en capas distintas. Mastercard sí nombra XRPL y Canton entre las redes de su liquidación con stablecoins (3-jun-2026, S por 403).

## Caso alcista vs. bajista
- Alcista: producción real (JPM, Citi, HSBC, DTCC, Pontes), reguladores aprobando (SEC-Nasdaq, exención a WisdomTree), varias cadenas públicas ya incluidas (Ethereum, Solana, Canton, Stellar, XRPL).
- Bajista: mucho es red privada o permisionada; bastantes anuncios son planes o pilotos; los importes más citados son del propio emisor o de agregadores y discrepan (BUIDL: 2.170 M$ a 30-oct frente a 2.800 M$ a fin de ago); Nasdaq y NYSE dependen de aprobaciones o de DTC; los depósitos tokenizados bancarios no usan redes públicas.

## Sesgos de la fuente
Comunicados corporativos = promoción; The Block y agregadores = S; Ondo y WisdomTree dan sus propias cifras; ARA (alianza de Santander) fuente única; Business Wire/Mastercard/Swift/Euroclear/Goldman devolvieron 403 a la lectura.

## Qué quedó [VERIFICAR] y por qué
1. Deutsche Bank: si ya opera y cualquier mención a Ripple (solo prensa; sin comunicado leído).
2. Swift: Linea o Besu (fuentes contradictorias; 403 hoy).
3. Nasdaq: PDF de la SEC ilegible como texto; primeras operaciones tras sep-2026 sin confirmar.
4. Mastercard 3-jun, WisdomTree 29-sep, Goldman/BNY 2025, Euroclear-SG 25-jun: 403, contenido vía buscador.
5. BBVA/Qivalis: si ya lanzada; recuento de bancos (11-12 frente a 37).
6. LSEG 1-sep (acciones del Reino Unido y Payward) y JPM fondos tokenizados de 2025/2026: solo títulos.
7. mBridge: cifra de ene-2026 vía Reuters/The Block; sin dato oficial.
8. Nexus: sin transacción real confirmada.

## Falta respecto a lo ya en el repo
`pruebas-bancos.json` ya cubre redes públicas por banco. Faltaba: depósitos tokenizados en redes privadas (Citi, HSBC, BNY), bolsas (Nasdaq, NYSE, LSEG), depositarias europeas, Pontes con sus participantes, Agorá y Mastercard/BVNK.

## Candidatos a movimiento de la línea de tiempo
```json
[
  {"fecha": "2026-10-19", "capa": "tokenizacion", "actor": "J.P. Morgan", "texto": "Lleva JPM Coin (JPMD) a Ethereum L1, además de Base, para clientes institucionales", "fuente": "J.P. Morgan Payments, comunicado", "nivel": "P", "url": "https://www.jpmorgan.com/payments/newsroom/jpm-coin-live-on-ethereum"},
  {"fecha": "2026-09-28", "capa": "tokenizacion", "actor": "Citi", "texto": "Citi Token Services llega a Japón y EAU: 7 mercados, red privada permisionada", "fuente": "Citigroup, comunicado", "nivel": "P", "url": "https://www.citigroup.com/global/news/press-release/2026/citi-token-services-expands-global-footprint-japan-united-arab-emirates"},
  {"fecha": "2026-04-13", "capa": "tokenizacion", "actor": "HSBC", "texto": "Lanza su servicio de depósitos tokenizados en EE. UU.", "fuente": "HSBC EE. UU., nota de prensa", "nivel": "P", "url": "https://www.about.us.hsbc.com/newsroom/press-releases/hsbc-expands-tokenized-deposit-service-to-the-united-states"},
  {"fecha": "2026-09-28", "capa": "tokenizacion", "actor": "LSEG", "texto": "Nombrada Super Validator de Canton; DiSH ya liquidó repos intradía en efectivo sobre Canton", "fuente": "LSEG, comunicado", "nivel": "P", "url": "https://www.lseg.com/en/media-centre/press-releases/2026/lseg-appointed-as-a-super-validator-on-canton-network"},
  {"fecha": "2026-09-21", "capa": "bancos_centrales", "actor": "BCE / Eurosistema", "texto": "Pontes en producción: liquidación de activos tokenizados en dinero de banco central (Santander, Deutsche Bank, SG, Clearstream y otros)", "fuente": "BCE, nota de prensa", "nivel": "P", "url": "https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260921~e754847a7b.en.html"},
  {"fecha": "2026-05-27", "capa": "bancos_centrales", "actor": "BIS / IIF", "texto": "Proyecto Agorá: informe final; liquidación atómica con reservas y depósitos tokenizados; pasa a pruebas con valor real", "fuente": "BIS, nota de prensa", "nivel": "P", "url": "https://www.bis.org/press/p260527.htm"},
  {"fecha": "2026-09-16", "capa": "tokenizacion", "actor": "Deutsche Bank", "texto": "Anuncia custodia de BTC, ETH, USDC, EURC y EURAU para clientes europeos en 2026, pendiente de autorización; no nombra a sus proveedores tecnológicos", "fuente": "The Block citando al banco", "nivel": "S", "url": "https://theblock.co/news/business/2026-09-16-deutsche-bank-plans-bitcoin-ether-custody-for-institutional-clients-in-europe-415251"},
  {"fecha": "2026-03-18", "capa": "tokenizacion", "actor": "Nasdaq", "texto": "La SEC aprueba negociar acciones y ETF tokenizados en Nasdaq vía el programa de DTC", "fuente": "The Block / Reuters", "nivel": "S", "url": "https://www.sec.gov/files/rules/sro/nasdaq/2026/34-104693.pdf"},
  {"fecha": "2026-06-03", "capa": "pagos", "actor": "Mastercard", "texto": "Liquidación on-chain con stablecoins regulados (USDC, PYUSD, RLUSD...) en 8 redes, incluidas XRPL y Canton", "fuente": "Mastercard (nota; 403, vía buscador)", "nivel": "S", "url": "https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html"},
  {"fecha": "2026-01-09", "capa": "tokenizacion", "actor": "BNY", "texto": "Activa depósitos tokenizados para colateral y margen de clientes institucionales", "fuente": "The Block", "nivel": "S", "url": "https://www.theblock.co/news/business/2026-01-09-bny-activates-tokenized-deposit-service-payments-collateral-384930"},
  {"fecha": "2026-02-04", "capa": "tokenizacion", "actor": "BBVA", "texto": "Se une al consorcio Qivalis para una stablecoin en euros; lanzamiento previsto 2S-2026 si hay autorización", "fuente": "BBVA, nota (localizada) / The Block", "nivel": "S", "url": "https://www.bbva.com/en/innovation/bbva-joins-banking-consortium-to-issue-european-stablecoin/"}
]
```
