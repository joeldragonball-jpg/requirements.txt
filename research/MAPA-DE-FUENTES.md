# Mapa de fuentes (actualizado 25-oct-2026, W07)

Estado: ✅ se lee con curl/urllib · 🌐 solo navegador integrado · ⛔ 403 anti-bots (no se salta; fuente secundaria [S]) · ❌ enlace roto.
Probado en la sesión del 25-oct (96 URLs: 74 OK, 19 con 403, 2 EUR-Lex con 202, 1 roto).

| Fuente | Qué datos | Cómo se lee | Estado |
|---|---|---|---|
| Federal Register | Normas y avisos de EE. UU. | API JSON, User-Agent propio | ✅ |
| SEC EDGAR (submissions, full-text) | Filings, 13F, 8-K, S-1 | API, User-Agent identificado | ✅ |
| sec.gov (páginas web) | Notas y órdenes | Navegador integrado | ⛔ |
| Banco Mundial | Indicadores por país | API | ✅ |
| Eurostat | Estadística UE | API | ✅ |
| BIS Data Portal | Tipos oficiales (WS_CBPOL: CH, CN, GB, HK, ID, IN, JP, KR, MX, RU, ZA, BR) | SDMX CSV, `Accept: application/vnd.sdmx.data+csv;version=1.0.0` | ✅ (candidato a automatizar `leer_tipos`) |
| BCE | Tipos, balance | API | ✅ |
| NY Fed | Tipos de referencia | API | ✅ |
| FiscalData | Deuda y subastas EE. UU. | API | ✅ |
| CFTC | Posiciones | Ficheros públicos | ✅ |
| FRED | Series macro | CSV | ✅ |
| Banco de Japón | Tipo y decisiones | Página HTML | ✅ |
| FMI DataMapper | Previsiones | — | ⛔ 403 |
| EUR-Lex | Reglamentos UE | Navegador (da 202 a curl) | 🌐 |
| aft.gouv.fr, bls.gov, opec.org, swift.com, congress.gov, pbc.gov.cn | Deuda FR, empleo EE. UU., OPEP, SWIFT, Congreso, PBoC | Navegador integrado o fuente que los cite [S] | ⛔ |
| bitvavo, theblock.co, tipranks, moneytalksnews | Mercado/prensa/analistas | Navegador integrado; son [S] | ⛔ |
| www.sz.gov.cn/en_szgov/news/infocus/APEC2026/ | Evento APEC 18-nov (calendario) | Sustituir por la fuente oficial de APEC [VERIFICAR URL] | ❌ |

Regla: nunca saltar anti-bots; si no hay API ni navegador, la cifra queda [VERIFICAR].
