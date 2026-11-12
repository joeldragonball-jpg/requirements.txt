# Mapa de fuentes (actualizado 7-nov-2026, W07)

Estado: ✅ se lee con curl/urllib · 🌐 solo navegador integrado · ⛔ 403 anti-bots (no se salta; fuente secundaria [S]) · ❌ enlace roto.
Probado el 2-nov (208 URLs de voces, regulación y calendario, 12 en paralelo, sin saltar anti-bots): 161 OK, 3 EUR-Lex con 202, 34 con 403, 3 con 429 (límite de ritmo), 1 con 505, 1 sin respuesta, 1 roto (arreglado). Las URL de YouTube no se probaron. Antes (25-oct): 96 URLs, 74 OK.
Reprobado el 7-nov (W07, 231 URLs de voces, regulación y calendario, 8 en paralelo, sin saltar anti-bots): 190 OK, 37 con 403 (mismos dominios: sec.gov, rba, theblock, aft, bls, congress, tipranks…), 1 con 503 (eia.gov/outlooks/steo, pasajero: respondió 200 al curl de antes), 1 con 406 (URL de fsca.co.za cortada por el paréntesis del script: falso positivo), 1 301 (parl.ca, redirige y abre 200), 1 sin respuesta (lg.gov.cn, ya anotado). **Cero enlaces rotos (404).**

| Fuente | Qué datos | Cómo se lee | Estado |
|---|---|---|---|
| Federal Register | Normas y avisos de EE. UU. | API JSON (`conditions%5Bterm%5D=`, con los corchetes codificados) | ✅ |
| SEC EDGAR (`data.sec.gov/submissions`, atom de 8-K) | Filings, 13F, 8-K, S-1 | API, User-Agent identificado | ✅ |
| sec.gov (páginas web, `/Archives`, newsroom) | Notas y órdenes | Navegador integrado | ⛔ |
| Banco Mundial | Indicadores por país | API v2 JSON | ✅ |
| Eurostat | Estadística UE | API. OJO: `prc_hicp_manr` congelada en dic-2025; usar `prc_hicp_minr` con `coicop18=TOTAL` | ✅ |
| BIS Data Portal | Tipos oficiales (WS_CBPOL) | SDMX CSV, `Accept: application/vnd.sdmx.data+csv;version=1.0.0`; ya automatizado (`leer_tipos_bis` en `actualizar_paneles.py`) | ✅ |
| BCE Data Portal (`data-api.ecb.europa.eu`) y XML de cambios | Tipos, cambios, balance | API SDMX CSV | ✅ |
| FMI DataMapper | Previsiones por país (PIB, inflación, deuda) | `www.imf.org/external/datamapper/api/v1/<indicador>/<ISO3>` da JSON (2-nov, España 2026: 2,5 %); `api.imf.org` daba 404 el 2-nov y el 7-nov responde 200 (SDMX 2.1, `IMF.STA`; sin probar series). Antes figuraba como 403 | ✅ (candidato a automatizar) |
| NY Fed, FRED (`fredgraph.csv?id=`), FiscalData (`page%5Bsize%5D`) | Tipos, series macro, deuda EE. UU. | API/CSV | ✅ |
| TreasuryDirect `TA_WS/securities/upcoming?format=json` | Subastas de EE. UU. | JSON; la página `/auctions/upcoming/` da 505 | ✅ (API) / ❌ (página) |
| CFTC Commitments of Traders | Posiciones | API Socrata `publicreporting.cftc.gov/resource/6dca-aqww.json`; los `.txt` de `cftc.gov/dea` dan 404/403 | ✅ (API) |
| Banco de Inglaterra (IADB CSV), Banco de España (`be1101.csv`), INE (`servicios.ine.es/wstempus`), BOE datos abiertos, HKMA API | Tipos, IPC y legislación | CSV/JSON | ✅ |
| Banco de Japón | Tipo y decisiones | Página HTML / PDF de `mpmdeci` | ✅ |
| OCDE SDMX (`sdmx.oecd.org/public/rest/data/...&format=csvfilewithlabels`) | IPC y otros indicadores por país | Responde 200 desde el 7-nov (antes ⛔), PERO el IPC de España llega solo hasta **2025-12**: serie congelada igual que `prc_hicp_manr` de Eurostat; no usar para el dato del mes | ⚠️ |
| EUR-Lex | Reglamentos UE | Navegador (202 a curl); la API REST `eurlex-ws` da 404; SPARQL de `publications.europa.eu` responde 200 (sin probar consultas) | 🌐 |
| aft.gouv.fr, bls.gov, congress.gov, senate.gov, pbc.gov.cn, rba.gov.au, fatf-gafi.org, consilium.europa.eu, europarl.europa.eu, swift.com, spglobal.com, incometaxindia.gov.in, fsca.co.za | Deuda FR, empleo EE. UU., Congreso, PBoC, RBA, FATF, euro digital, SWIFT, ratings, India, Sudáfrica | Navegador integrado o fuente que los cite [S] | ⛔ |
| bitvavo, theblock.co, tipranks, moneytalksnews, bloomberg, crowdfundinsider, puck.news | Mercado/prensa/analistas | Navegador integrado; son [S] | ⛔ |
| coindesk.com, dlapiper.com | Prensa/despacho | 429 a curl (límite de ritmo, no bloqueo); reintentar más despacio | ⚠️ |
| hkma.gov.hk/eng/key-functions/monetary-stability/ | HKMA, página antigua | 404; sustituida el 2-nov en el calendario por `/eng/news-and-media/press-releases/` | ✅ (arreglado) |
| lg.gov.cn (Longgang, APEC 18-19 nov) | Fechas del APEC | Sin respuesta a curl (¿geobloqueo?); es la fuente de fechas del calendario. Reintentar con navegador | ⚠️ [VERIFICAR] |
| `eia.gov/dnav/pet/hist/RBRTED.htm` y `RWTCD.htm` | Brent y WTI al contado (EIA) | HTML con tabla semanal; ya automatizado (`_spot_eia` en `actualizar_paneles.py`: Brent y Henry Hub; falta WTI); publica con ~3 días de retraso (el 7-nov el último dato era del 3-nov). Son spot físico, no futuro | ✅ |
| `home.treasury.gov/.../pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value_month=AAAAMM` | Curva del Tesoro de EE. UU. diaria [P] | XML; 7-nov: 6-nov 2 años 4,51 %, 10 años 4,86 %, 30 años 5,26 % | ✅ |
| Banco de Canadá Valet (`bankofcanada.ca/valet/observations/V39079/json?recent=1`) | Tipo objetivo a un día | JSON | ✅ |
| Banco de Inglaterra IADB (serie `IUDBEDR`) | Bank Rate diario [P] | CSV; 7-nov: 3,75 % hasta el 4-nov y **4,00 % el 5-nov** (confirma la decisión del 5-nov) | ✅ |
| `api.bcb.gov.br` (SELIC, SGS 432) | Tipo de Brasil | 502 el 7-nov (¿caída temporal?); reintentar | ⚠️ |
| `eservices.mas.gov.sg` | MAS (Singapur) | Devuelve página de mantenimiento el 7-nov; reintentar | ⚠️ |
| `eppo.europa.eu/media/news/...` (Fiscalía Europea) | Comunicados de investigaciones con fondos UE [P] | HTML; abre por URL directa y en buscador; 12-nov: sin novedades tras el 6-nov | ✅ |
| `transportes.gob.es/organos-colegiados/ciaf/investigaciones-en-curso/<suceso>` (CIAF) | Expediente y lista de documentos de cada accidente [P] | 403 al script; **abre en el navegador integrado** (12-nov); los PDF dan 403 al script y se leen en el navegador (texto extraído en la propia página, sin guardar archivo) | 🌐 |
| `poderjudicial.es` (notas del CGPJ y de los TSJ) | Órgano instructor, medidas y cifras oficiales de víctimas [P] | HTML; abre en el navegador integrado; se localiza con buscador limitado al dominio | 🌐 |
| `anti-fraud.ec.europa.eu` (OLAF) | Notas de prensa [P] | HTML; 12-nov: nada sobre Adif (no anuncia investigaciones en curso) | ✅ |
| XRP Ledger JSON-RPC (`xrplcluster.com`, método `gateway_balances` del emisor) | RLUSD en circulación en el XRPL [P] | JSON; 12-nov: 885,2 M (ledger 108.281.104) | ✅ |
| Horizon de Stellar (`horizon.stellar.org/assets?asset_code=USDC&asset_issuer=…`) | USDC y EURC emitidos en Stellar [P] | JSON; 12-nov: USDC 344,0 M | ✅ |
| `stablecoins.llama.fi/stablecoincharts/<cadena>` (DefiLlama) | Serie histórica de stablecoins por cadena [S] | JSON; sirve para comprobar una cifra antigua antes de compararla | ✅ |
| `eia.gov/outlooks/steo/` | STEO vigente [P] | HTML legible con script; solo guarda la edición actual (archivar el texto el día que sale) | ✅ |

Regla: nunca saltar anti-bots; si no hay API ni navegador, la cifra queda [VERIFICAR].
