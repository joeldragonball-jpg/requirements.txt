# Catálogo de fuentes con estado y cadencia (Fase 2, 3-nov-2026)

Complementa `MAPA-DE-FUENTES.md` (cómo se lee cada cosa) y `ACCESOS-CHROME.md` (pruebas con Chrome). Estado: **API** = abierta, se automatiza · **Chrome** = solo navegador real · **Bloqueada** = 403/Cloudflare, no se salta (fuente secundaria [S]) · **Manual** = requiere clave, descarga o decisión de Joel.
Probado con curl y User-Agent identificado el 3-nov-2026 (sin saltar controles).

| Dato | Fuente | Estado | Cadencia sugerida | Dónde se usa |
|---|---|---|---|---|
| Tipos de bancos centrales (17 países) | BIS WS_CBPOL (`stats.bis.org`) | API | diaria (paneles.yml) | tarjeta de tipos; cubre **Colombia, Nueva Zelanda, Chile, Perú, Australia, Japón…** |
| Fed, BCE, BoE, Canadá, Brasil | fuentes primarias (NY Fed, `data-api.ecb.europa.eu`, IADB, BoC, `api.bcb.gov.br`) | API | diaria | paneles |
| Bono EE. UU., series macro | FRED `fredgraph.csv` (200 el 3-nov, antes no respondía), FiscalData, TreasuryDirect JSON | API | diaria / por subasta | paneles, W02 |
| Inflación y PIB por país | Banco Mundial v2, Eurostat (`prc_hicp_minr`), FMI DataMapper | API | mensual / trimestral | C59, C31 |
| España: IPC, hipotecas, paro | INE `servicios.ine.es/wstempus`, BdE `be1101.csv` | API | mensual | paneles España |
| Brasil: SGS, Focus | `api.bcb.gov.br`, `olinda.bcb.gov.br`, IBGE SIDRA | API | semanal (Focus lunes) | paneles Brasil |
| Cripto on-chain | XRPL (`xrplcluster.com`), Horizon (Stellar), DefiLlama | API | diaria | onchain.yml |
| Filings EE. UU. | SEC EDGAR (`data.sec.gov`), Federal Register | API | diaria (vigilantes) | edgar.yml, federal-register.yml |
| Posiciones | CFTC Socrata `6dca-aqww` | API | semanal (viernes) | W04 |
| **Escaños Reino Unido** | `members-api.parliament.uk/api/Parties/StateOfTheParties/1/<fecha>` | **API (nueva, 3-nov)**: Labour 404, Conservative 118, Lib Dem 71, Reform 8, SNP 8… | tras cada by-election | C58 (cierra laguna UK) |
| **Escaños Italia** | `dati.camera.it/sparql` (200; consulta SPARQL sin probar) | API probable | tras cambios de grupo | C58 |
| **Colombia: tipo del BanRep** | BIS (arriba); `datos.gov.co` (200, serie TRM `ceyp-9c7c`) | API | diaria | cierra laguna BanRep para el tipo; la TRM sale de datos.gov.co |
| **Nueva Zelanda: RBNZ** | web `rbnz.govt.nz` (403 en la página de decisiones, 200 portada) | tipo por BIS (API); comunicados Chrome | cada decisión | cierra el tipo; el texto de la decisión queda [S] |
| **Japón e-Stat** | `api.e-stat.go.jp` responde pero exige `appId` gratuito | **Manual**: registro de Joel (no creo cuentas) | mensual | IPC y paro de Japón |
| CNMV | `cnmv.es` responde con redirecciones (301/302), sin API probada | Chrome | mensual | registros/ESMA |
| Senado de EE. UU. (roll call) | `senate.gov` 403; Chrome «Unauthorized» | **Bloqueada** (no insistir); cloture 49-50 sigue [VERIFICAR], buscar [S] | — | CLARITY |
| congress.gov | Cloudflare, bloquea Chrome | **Bloqueada** | — | CLARITY §404 |
| RBNZ página de decisiones, OCDE SDMX, sec.gov web, bls.gov, pbc.gov.cn, rba.gov.au… | ver mapa | **Bloqueada** | — | fuente secundaria [S] |
| EUR-Lex | 202 a curl | Chrome | al citar norma | regulación UE |
| BOE texto consolidado | `boe.es/buscar/act.php?id=…` | Chrome (funciona) | al citar norma | fiscalidad |
| Brasil normativos | `bcb.gov.br/exibenormativo` | Chrome (funciona) | al citar resolución | W03 |
| aft.gouv.fr | XLS de subastas | Manual (descarga con OK) | trimestral | D03/D05 |
| DANA fallecidos | fuente única (Generalitat/Justicia) | Manual/[VERIFICAR] | semestral | informe H |
| XRPL lending | `enabled=false` en config; no activar sin revisar | Manual | — | C42 |
| PDF de descarga pendientes | BdE deuda 2T-2026, Registradores ERI 2T, auto de Catarroja | **Manual: necesitan OK de Joel** | trimestral | C79, informe H |

## Lagunas de la Fase 2: resultado
- **Cerradas hoy:** escaños UK (API), tipo de Colombia y Nueva Zelanda (ya en BIS), FRED vuelve a responder.
- **Siguen abiertas:** senate.gov y congress.gov (bloqueadas), e-Stat (falta `appId` de Joel), Italia (falta probar la consulta SPARQL), CNMV (falta Chrome), DANA fallecidos, XRPL lending, 3 PDF.
- **Chrome:** no estaba conectado en esta sesión; lo marcado «Chrome» no se ha re-probado hoy.
