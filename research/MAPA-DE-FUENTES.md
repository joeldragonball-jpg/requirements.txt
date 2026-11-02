# Mapa de fuentes (actualizado 2-nov-2026, W07)

Estado: ✅ se lee con curl/urllib · 🌐 solo navegador integrado · ⛔ 403 anti-bots (no se salta; fuente secundaria [S]) · ❌ enlace roto.
Probado el 2-nov (208 URLs de voces, regulación y calendario, 12 en paralelo, sin saltar anti-bots): 161 OK, 3 EUR-Lex con 202, 34 con 403, 3 con 429 (límite de ritmo), 1 con 505, 1 sin respuesta, 1 roto (arreglado). Las URL de YouTube no se probaron. Antes (25-oct): 96 URLs, 74 OK.

| Fuente | Qué datos | Cómo se lee | Estado |
|---|---|---|---|
| Federal Register | Normas y avisos de EE. UU. | API JSON (`conditions%5Bterm%5D=`, con los corchetes codificados) | ✅ |
| SEC EDGAR (`data.sec.gov/submissions`, atom de 8-K) | Filings, 13F, 8-K, S-1 | API, User-Agent identificado | ✅ |
| sec.gov (páginas web, `/Archives`, newsroom) | Notas y órdenes | Navegador integrado | ⛔ |
| Banco Mundial | Indicadores por país | API v2 JSON | ✅ |
| Eurostat | Estadística UE | API. OJO: `prc_hicp_manr` congelada en dic-2025; usar `prc_hicp_minr` con `coicop18=TOTAL` | ✅ |
| BIS Data Portal | Tipos oficiales (WS_CBPOL) | SDMX CSV, `Accept: application/vnd.sdmx.data+csv;version=1.0.0`; ya automatizado (`leer_tipos_bis` en `actualizar_paneles.py`) | ✅ |
| BCE Data Portal (`data-api.ecb.europa.eu`) y XML de cambios | Tipos, cambios, balance | API SDMX CSV | ✅ |
| FMI DataMapper | Previsiones por país (PIB, inflación, deuda) | `www.imf.org/external/datamapper/api/v1/<indicador>/<ISO3>` da JSON (2-nov, España 2026: 2,5 %); `api.imf.org` da 404. Antes figuraba como 403 | ✅ (candidato a automatizar) |
| NY Fed, FRED (`fredgraph.csv?id=`), FiscalData (`page%5Bsize%5D`) | Tipos, series macro, deuda EE. UU. | API/CSV | ✅ |
| TreasuryDirect `TA_WS/securities/upcoming?format=json` | Subastas de EE. UU. | JSON; la página `/auctions/upcoming/` da 505 | ✅ (API) / ❌ (página) |
| CFTC Commitments of Traders | Posiciones | API Socrata `publicreporting.cftc.gov/resource/6dca-aqww.json`; los `.txt` de `cftc.gov/dea` dan 404/403 | ✅ (API) |
| Banco de Inglaterra (IADB CSV), Banco de España (`be1101.csv`), INE (`servicios.ine.es/wstempus`), BOE datos abiertos, HKMA API | Tipos, IPC y legislación | CSV/JSON | ✅ |
| Banco de Japón | Tipo y decisiones | Página HTML / PDF de `mpmdeci` | ✅ |
| OCDE SDMX | Indicadores adelantados | 403 a curl | ⛔ |
| EUR-Lex | Reglamentos UE | Navegador (202 a curl); la API REST `eurlex-ws` da 404; SPARQL de `publications.europa.eu` responde 200 (sin probar consultas) | 🌐 |
| aft.gouv.fr, bls.gov, congress.gov, senate.gov, pbc.gov.cn, rba.gov.au, fatf-gafi.org, consilium.europa.eu, europarl.europa.eu, swift.com, spglobal.com, incometaxindia.gov.in, fsca.co.za | Deuda FR, empleo EE. UU., Congreso, PBoC, RBA, FATF, euro digital, SWIFT, ratings, India, Sudáfrica | Navegador integrado o fuente que los cite [S] | ⛔ |
| bitvavo, theblock.co, tipranks, moneytalksnews, bloomberg, crowdfundinsider, puck.news | Mercado/prensa/analistas | Navegador integrado; son [S] | ⛔ |
| coindesk.com, dlapiper.com | Prensa/despacho | 429 a curl (límite de ritmo, no bloqueo); reintentar más despacio | ⚠️ |
| hkma.gov.hk/eng/key-functions/monetary-stability/ | HKMA, página antigua | 404; sustituida el 2-nov en el calendario por `/eng/news-and-media/press-releases/` | ✅ (arreglado) |
| lg.gov.cn (Longgang, APEC 18-19 nov) | Fechas del APEC | Sin respuesta a curl (¿geobloqueo?); es la fuente de fechas del calendario. Reintentar con navegador | ⚠️ [VERIFICAR] |

Regla: nunca saltar anti-bots; si no hay API ni navegador, la cifra queda [VERIFICAR].
