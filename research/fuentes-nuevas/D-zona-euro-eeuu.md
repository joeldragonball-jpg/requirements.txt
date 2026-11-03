# D. Fuentes de datos: zona euro (DE, FR, IT, agregado) y EE. UU.

Lectura y pruebas: 3-nov-2026 (curl con User-Agent identificado, una pestaña propia de Chrome para dos webs, WebFetch para el calendario del BCE). No se guardó ningún archivo en el repo ni se descargó nada a disco. Niveles: [P] oficial primaria, [S] secundaria. Nada de esto es una recomendación de compra o venta.

## Resumen (8 líneas)
1. Casi todo lo importante tiene API oficial abierta y sin clave: BCE (SDMX CSV), Eurostat (JSON-stat), Bundesbank (CSV), INSEE (SDMX XML), FRED (`fredgraph.csv`), FiscalData, TreasuryDirect, CFTC (Socrata) y la API pública de BLS v2 (sin clave, límite diario bajo).
2. Con clave gratuita (no creada, anotado): BEA API (`UserID`), EIA API v2 (`api_key`), Census API (`key`), y FRED API JSON (el CSV de gráfico NO la necesita). Alternativa sin clave a BEA y Census: FRED (PCEPILFE, GDPC1, HOUST).
3. BLS: curl con User-Agent identificado SÍ entra en `bls.gov/schedule/...` (200) y en `api.bls.gov` (200); el mapa decía ⛔ para `bls.gov`. Conviene actualizar el MAPA (solo las páginas de calendario; las demás sin probar).
4. AFT (Francia): `aft.gouv.fr` da 403 a curl pero la portada carga con Chrome (deuda negociable 2,921 billones EUR a 31-oct; resultados de subastas del 15-oct). La URL `/en/calendar-auctions` que probé no existe (404); falta localizar la URL real del calendario.
5. SLOOS: el aviso de la Fed (semana del 9-nov) habla de quitar la función «Build Your Package» del Data Download Program (DDP) «por la futura retirada del DDP», NO de borrar el SLOOS; la Fed remite a FRED. En FRED siguen las series (p. ej. DRTSCILM con dato 2026-10). Leer SLOOS desde FRED, no desde el DDP.
6. Trampa de datos: `ICP.M.U2.N.000000.4.ANR` del BCE y `prc_hicp_manr` de Eurostat están congeladas en dic-2025; usar `prc_hicp_minr` (coicop18=TOTAL), como ya hace el repo. Eurostat usa ya `EA21` (o `EA`) para el agregado; `EA20` devuelve vacío en paro.
7. En el repo ya está lo grueso: IPC/IPCA, paro, PIB, deuda y déficit de DE/FR/IT/ES/US, M2/M3, crédito (BCE, H.8 vía FRED, BLS del BCE), TIC, UST y curva BCE, subastas TreasuryDirect, EIA spot. Faltan: empleo y JOLTS de EE. UU., PCE core/PIB de EE. UU. con calendario, balance del Eurosistema y de la Fed, RRP, producción industrial/comercio, subastas europeas, spreads DE/FR/IT diarios, TARGET2, SLOOS de EE. UU.
8. Cadencia propuesta: diaria (tipos y curvas), semanal (balances, CFTC, EIA), mensual (inflación, empleo, M3/crédito), trimestral (PIB, SLOOS, BLS del BCE), anual (deuda/déficit, TIC se publica mensual).

## Tabla de indicadores

Leyenda «¿Ya está?»: Sí = en `scripts/actualizar_paneles.py` o `scripts/indicadores.py`; Mapa = en MAPA-DE-FUENTES pero sin automatizar; No = falta.

| Región | Indicador | Fuente oficial | URL / endpoint | Cómo se lee | Prueba (3-nov-2026) y último dato | Publicación | Cadencia recomendada | ¿Ya está? | Prioridad |
|---|---|---|---|---|---|---|---|---|---|
| ZE | IPCA (adelantado y final) | Eurostat | `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr?geo=EA&coicop18=TOTAL&unit=RCH_A&lastTimePeriod=3` | JSON-stat, sin clave | OK. EA sept-2026: 3,8 % (ago 3,2 %); DE sept 3,3 %. Actualizado 16-oct | Adelantado 4-nov (oct); final 18-nov (oct) | Mensual, dos pasadas (adelantado y final) | Sí (ea, es, y DE/FR/IT en indicadores) | Alta |
| ZE | IPCA vía BCE | BCE (ICP) | `data-api.ecb.europa.eu/service/data/ICP/M.U2.N.000000.4.ANR` | CSV | Congelado: último 2025-12 (1,9 %). NO usar | | | No (evitar) | Aviso |
| ZE | PIB trimestral (q/q) | Eurostat | `.../data/namq_10_gdp?geo=EA20&unit=CLV_PCH_PRE&s_adj=SCA&na_item=B1GQ&lastTimePeriod=2` | JSON-stat | OK, actualizado 30-oct (últimos dos trimestres 0,6 y 0,4; DE 3T 0,2 % q/q) | Flash 3T: ya publicado 30-oct; estimación con empleo 13-nov; detalle ~7-dic [VERIFICAR] | Trimestral | Sí (pib interanual en indicadores) | Media |
| ZE | Paro | Eurostat | `.../data/une_rt_m?geo=EA21&sex=T&age=TOTAL&unit=PC_ACT&s_adj=SA&lastTimePeriod=2` | JSON-stat | OK: EA21 sept 6,5 % (ago 6,5 %). `EA20` vacío | ~1.º-2 del mes (oct: ~2-dic [VERIFICAR]) | Mensual | Sí | Media |
| ZE | Producción industrial | Eurostat | `.../data/sts_inpr_m?geo=EA20&nace_r2=B-D&s_adj=CA&unit=PCH_SM` | JSON-stat | OK (act. 31-oct; FR ago +0,4 % m/m, EA20 -1,1 % una lectura [VERIFICAR unidad]) | Sept: 16-nov | Mensual | No | Media |
| ZE | Comercio minorista | Eurostat | `.../data/sts_trtu_m?geo=EA20&nace_r2=G47&s_adj=CA&unit=PCH_SM&indic_bt=VOL_SLS` | JSON-stat | OK (act. 2-nov; ago +0,8 %) | Sept: 6-nov | Mensual | No | Baja |
| ZE | Sentimiento económico (ESI) | Comisión (ECFIN) / Eurostat | `ei_bssi_m_r2` (consulta con filtros devolvió vacío); calendario: 27-nov | | Consulta sin resolver; ajustar filtros [VERIFICAR] | 27-nov (nov) | Mensual | No | Baja |
| ZE | PMI | S&P Global/HCOB | Sin API abierta | Prensa | No probado. [S] siempre | Flash ~3.ª semana | Solo [S], mensual | No | Baja |
| ZE | M3 (var. anual) | BCE (BSI) | `.../service/data/BSI/M.U2.Y.V.M30.X.I.U2.2300.Z01.A?lastNObservations=13&format=csvdata` | CSV, `Accept: text/csv` | OK: sept 3,50 % (ago 3,49 %) | ~28.º día laborable siguiente: oct sobre 27-nov [VERIFICAR] | Mensual | Sí | Alta |
| ZE | Crédito a hogares (var. anual y saldo) | BCE (BSI) | `BSI/M.U2.N.A.A20.A.I.U2.2240.Z01.A` y `.../A20.A.1.U2.2240.Z01.E` | CSV | OK: sept 4,30 % (ago 4,33 %); saldo 5.472 mil M EUR | Con M3 | Mensual | Parcial (hog_ea en crédito) | Media |
| ZE | Encuesta de préstamos bancarios (BLS del BCE) | BCE | `BLS/Q.{area}.ALL...` | CSV | Ya en el repo | Trimestral (ene, abr, jul, oct) | Trimestral | Sí | Alta (hecha) |
| ZE | Balance del Eurosistema (activos totales) | BCE (ILM) | `.../service/data/ILM/W.U2.C.T000000.Z5.Z01?lastNObservations=2&format=csvdata` | CSV | OK: 2026-W43 = 5.934.983 M EUR (W42: 5.935.346) | Estado financiero semanal, martes [VERIFICAR] | Semanal | No | Alta |
| ZE | Tipos del BCE (DFR, MRO) y €STR | BCE | `FM/B.U2.EUR.4F.KR.DFR.LEV`, `FM/...MRR_FR.LEV`, `EST/B.EU000A2X2A25.WT` | CSV | OK: MRO 2,65 % (16-sep-2026); €STR 2,44 % (30-oct). €STR: la clave `ESTR/` no existe, vale `EST/` | Diario / por reunión | Diaria (€STR) y en cada reunión | Sí (DFR); €STR No | Media |
| ZE | Curva de tipos soberana (agregado) | BCE (YC) | `YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y` | CSV/JSON | OK: 10 años 3,365 % (30-oct) | Diaria | Diaria | Sí | Alta (hecha) |
| ZE | Rendimiento 10 años por país (DE, FR, IT) y spread | BCE (IRS, mensual) | `IRS/M.{DE\|FR\|IT}.L.L40.CI.0000.EUR.N.Z` | CSV | OK sept: Bund 3,473; OAT 4,44; BTP 4,362 → BTP-Bund 0,89 pp, OAT-Bund 0,97 pp (cálculo propio) | Mensual | Mensual (diario falta) | Sí (mensual10) | Media |
| DE | Rendimiento Bund 10 años diario | Bundesbank | `https://api.statistiken.bundesbank.de/rest/data/BBSIS/D.I.ZST.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A?lastNObservations=2&format=csv` | CSV con `;` y coma decimal, sin clave | OK: 2-nov 3,37 % (Svensson) | Diaria | Diaria | No | Media |
| DE | Subastas de deuda (Finanzagentur) | Deutsche Finanzagentur | `https://www.deutsche-finanzagentur.de/en/` (portada 200); la ruta `/en/federal-securities/auctions/auction-calendar` da 404 | HTML | URL del calendario sin localizar [VERIFICAR] | Calendario trimestral | Mensual | No | Baja |
| FR | Subastas OAT/BTF | AFT | `https://www.aft.gouv.fr/en` | HTML | curl 403; Chrome OK (1 vez): deuda negociable 2,921 billones EUR (31-oct), TEC10 4,91 % (2-nov), próxima OAT larga 5-nov, BTF cada lunes; resultados 15-oct | BTF lunes; OAT primer jueves del mes | Semanal (BTF) / mensual (OAT) | No | Media |
| FR | IPC, paro, PIB (nacional) | INSEE BDM | `https://api.insee.fr/series/BDM/V1/data/SERIES_BDM/001759970?lastNObservations=2` | SDMX XML, 200 sin clave en la prueba | Accesible; serie no interpretada [VERIFICAR] | Calendario INSEE | Mensual | No (Eurostat ya cubre) | Baja |
| IT | Subastas BTP/BOT (resultados) | Tesoro (dt.mef.gov.it) | `https://www.dt.mef.gov.it/en/debito_pubblico/dati_statistici/` | HTML, curl 200 | 13-oct: BTP 3 años rend. 3,69 %, 7 años 4,24 %, 15 años 4,84 %; BOT 12 meses 9-oct | Calendario del Tesoro | Mensual | No | Media |
| IT | Datos nacionales | ISTAT SDMX | `https://esploradati.istat.it/SDMXWS/rest/dataflow/IT1` | SDMX XML (200, 2,9 MB: no volcar) | Accesible; sin consulta mínima probada | | | No | Baja |
| ZE | Deuda y déficit públicos | Eurostat | `.../data/gov_10dd_edpt1?geo=EA20&sector=S13&na_item=GD&unit=PC_GDP` (déficit: `na_item=B9`) | JSON-stat | OK: EA deuda 2025 87,7 % PIB; IT déficit 2025 -3,1 %. Trimestral `gov_10q_ggdebt`: 2T-2026 89,3 % | Notificación PDE abril y octubre (act. 21-oct); trimestral ~fin de trimestre+3 meses | Anual (+ trimestral) | Sí (anual) | Media |
| ZE | TARGET2/TARGET balances | BCE | Dataflow `TGB` no respondió con mis claves (HTML de error) | | Sin resolver [VERIFICAR]; la página «TARGET balances» del Data Portal es la ruta | Mensual | Mensual | No | Baja |
| ZE | Deuda y calendario de subastas agregados | Comisión/ESM/Eurostat | Eurostat `gov_10q_ggdebt` | JSON-stat | OK | Trimestral | Trimestral | No | Baja |
| ZE | Balanza de pagos | Eurostat | Calendario: 19-nov (sept) | | No probado (filtro mal) | Mensual | Mensual | No | Baja |
| EE. UU. | Empleo (paro, nóminas) | BLS | `https://api.bls.gov/publicAPI/v2/timeseries/data/LNS14000000?startyear=2026&endyear=2026` y `CES0000000001?latest=true` | JSON POST/GET, sin clave (límite 25 consultas/día sin registro [VERIFICAR]) | OK: paro sept 4,2 % (ago 4,1 %); nóminas sept 159.044 (miles, preliminar) | Informe de empleo el viernes ~8:30 ET: 6-nov (oct), 4-dic, 8-ene-27 | Mensual (viernes del informe) | Parcial (paro en indicadores) | Alta |
| EE. UU. | IPC | BLS | `.../CUUR0000SA0` (NSA) y `CUSR0000SA0` (SA) | JSON | OK: SA sept 336,298; repo: 3,7 % interanual sept | 10-nov (oct), 10-dic, 13-ene-27, 11-feb-27 | Mensual | Sí | Alta (hecha) |
| EE. UU. | PPI | BLS | API v2, series PPI | JSON | Calendario leído; serie no probada | 13-nov (oct), 15-dic, 14-ene-27 | Mensual | No | Baja |
| EE. UU. | JOLTS | BLS / FRED `JTSJOL` | `https://fred.stlouisfed.org/graph/fredgraph.csv?id=JTSJOL&cosd=2026-06-01` | CSV | OK: ago 7.079 (jul 7.335) | 1-dic (oct) | Mensual | No | Media |
| EE. UU. | Coste laboral (ECI) | BLS | Calendario leído | | Publicado 30-oct (3T); siguiente 29-ene-27 | Trimestral | Trimestral | No | Baja |
| EE. UU. | PCE core | BEA vía FRED `PCEPILFE` | `fredgraph.csv?id=PCEPILFE` | CSV | OK: sept índice 130,902 (ago 130,489) | 25-nov (oct) y 23-dic (nov), 8:30 ET | Mensual | Sí (PCE headline vía FRED) | Alta |
| EE. UU. | PIB real | BEA vía FRED `GDPC1` | `fredgraph.csv?id=GDPC1` | CSV | OK: 3T 24.611 (2T 24.408), estimación adelantada ya publicada | Segunda estimación 25-nov; tercera 23-dic | Trimestral | Parcial (PIB en indicadores) | Media |
| EE. UU. | BEA API directa | BEA | `https://apps.bea.gov/api/data/` | JSON | Pide `UserID` (clave gratuita, no creada) | | | No | Opcional (FRED basta) |
| EE. UU. | Tipos, M2, balance Fed, RRP | FRED | `fredgraph.csv?id=M2SL`, `WALCL`, `RRPONTSYD` | CSV | OK: WALCL 28-oct 6.745.635 M USD (21-oct 6.753.604); RRP 2-nov 5,087 mil M USD | WALCL jueves; RRP diario | Semanal (balance), diaria (RRP) | Parcial (M2 sí) | Alta |
| EE. UU. | H.4.1 (balance Fed, original) | Fed | `https://www.federalreserve.gov/releases/h41/` (200) | HTML; hoy mejor FRED | Disponible | Jueves ~16:30 ET [VERIFICAR hora] | Semanal | No | Media |
| EE. UU. | H.8 (bancos comerciales) | Fed vía FRED (`LOANS`, `REALLN`, `CONSUMER`, `BUSLOANS`) | `fredgraph.csv?id=...` | CSV | Ya en repo | Viernes [VERIFICAR] | Semanal/mensual | Sí | Alta (hecha) |
| EE. UU. | SLOOS | Fed vía FRED `DRTSCILM` | `fredgraph.csv?id=DRTSCILM` | CSV | OK: oct-2026 1,7 (jul 0,0) endurecimiento neto empresas grandes y medianas. Aviso Fed sobre DDP leído | Trimestral (ene/feb, abr/may, ago, oct/nov) | Trimestral | No (solo el del BCE) | Alta |
| EE. UU. | Subastas de bonos | TreasuryDirect | `https://www.treasurydirect.gov/TA_WS/securities/upcoming?format=json` y `.../auctioned?format=json&type=Note&days=30` | JSON | OK | Anuncios semanales; refinanciación trimestral | Semanal | Sí (upcoming) | Alta (hecha) |
| EE. UU. | Deuda federal | FiscalData | `.../v2/accounting/od/debt_to_penny?sort=-record_date&page%5Bsize%5D=1` | JSON | OK: 29-oct deuda total 40,594 billones USD; en manos del público 32,712 | Diaria (día hábil siguiente) | Diaria/semanal | Sí | Alta (hecha) |
| EE. UU. | Déficit mensual (MTS) | FiscalData | `.../v1/accounting/mts/mts_table_1?sort=-record_date&page%5Bsize%5D=1` | JSON | OK: último registro 2026-09-30 (cierre FY2026) | ~8.º día laborable del mes | Mensual | No | Media |
| EE. UU. | Rendimientos del Tesoro | Tesoro (daily yield curve CSV) | URL en `actualizar_paneles.py` | CSV | Ya en repo: 2-nov 10 años 4,91 %, 30 años 5,28 % | Diaria | Diaria | Sí | Alta (hecha) |
| EE. UU. | TIC (tenedores extranjeros) | Tesoro | `.../tic/Documents/slt_table5.txt` | TXT tabulado | OK: último mes 2026-08 | Mensual (~18 del mes) [VERIFICAR] | Mensual | Sí | Alta (hecha) |
| EE. UU. | Vivienda (inicios) | Census vía FRED `HOUST` | `fredgraph.csv?id=HOUST` | CSV | OK: sept 1.221 (ago 1.288) miles | Calendario Census (enlace en la tabla de abajo) | Mensual | No | Media |
| EE. UU. | Census API directa | Census | `api.census.gov/data/timeseries/eits/...` | JSON | Responde «Missing Key» (clave gratuita, no creada) | | | No | Opcional |
| EE. UU. | Energía semanal (petróleo, gas) | EIA | `https://www.eia.gov/dnav/pet/hist/...`; API v2 `api.eia.gov/v2/...` | HTML; API pide `api_key` (403 sin ella) | Spot Brent y Henry Hub ya en repo (páginas HTML) | Miércoles 10:30 ET; jueves 12:00 el gas natural [VERIFICAR]; retrasos por festivo (12-nov jueves) | Semanal | Parcial | Media |
| EE. UU. | CFTC COT | CFTC | `https://publicreporting.cftc.gov/resource/6dca-aqww.json?$limit=1&$order=report_date_as_yyyy_mm_dd DESC` | JSON Socrata | OK: último informe con fecha 2026-10-27 | Viernes 15:30 ET; noviembre: 6, 16*, 20, 30* | Semanal | Mapa (no en panel) | Media |

## Calendario oficial de publicación (leído el 3-nov-2026)

- **BLS** (`bls.gov/schedule/news_release/*.htm`, 200 con User-Agent identificado): empleo (empsit) 6-nov, 4-dic, 8-ene-27, 5-feb, 5-mar, 2-abr, 7-may, 4-jun, 2-jul, 6-ago, 3-sep, 8-oct, 5-nov, 3-dic-27. IPC 10-nov, 10-dic, 13-ene-27, 11-feb, 10-mar, 13-abr, 12-may, 10-jun, 14-jul, 11-ago, 14-sep, 14-oct, 10-nov, 10-dic-27 (8:30 ET). PPI 13-nov, 15-dic, 14-ene-27, 12-feb, 12-mar. JOLTS oct 1-dic. ECI 29-ene, 30-abr, 30-jul, 29-oct-27.
- **BEA** (`bea.gov/news/schedule`, actualizado 2-nov): balanza comercial 4-nov y 8-dic; PIB 2.ª estimación + beneficios 25-nov; Renta y gasto personales (PCE) oct 25-nov y nov 23-dic; transacciones internacionales 3T 18-dic; PIB 3.ª estimación 23-dic. El calendario 2027 aún no figura en la página [VERIFICAR más adelante].
- **Eurostat** (`ec.europa.eu/eurostat/news/release-calendar`, renderizado en Chrome; curl solo trae la carcasa JS): IPCA adelantado oct 4-nov; precios productor 5-nov; comercio minorista sept 6-nov; servicios 9-nov; tipos y bono 10 años (BCE) 12-nov; PIB y empleo adelantado 3T 13-nov; comercio exterior 13-nov; producción industrial sept 16-nov; IPCA final oct 18-nov; balanza de pagos 19-nov; construcción 19-nov; ESI 27-nov. Diciembre sin leer.
- **BCE** (WebFetch a `ecb.europa.eu/press/calendars/mgcgc/html/index.en.html`): reuniones de política monetaria 17-dic-2026 y 2027: 4-feb, 18-mar, 29-abr, 10-jun, 22-jul, 9-sep, 28-oct, 16-dic. La página solo lista las fechas posteriores al 25-nov-2026. Calendario estadístico del BCE (`.../statscal/`): 200 pero JS, sin leer.
- **Fed** (`fomccalendars.htm`, act. 28-oct): FOMC 2026 restante 8-9 dic; 2027: 26-27 ene, 16-17 mar, 27-28 abr, 8-9 jun, 27-28 jul, 14-15 sep, 26-27 oct, 7-8 dic. H.4.1/H.8: páginas de fechas existen (200).
- **EIA** (WPSR): ajuste por festivos; jueves 12-nov a las 12:00 (Veterans Day). **CFTC** noviembre: 6, 16*, 20, 30* (retrasos por festivo); diciembre 4, 11, 18, 28*.
- **Census** (`census.gov/economic-indicators/calendar-listview.html`, 200): cubre hasta ene-2027: balanza comercial 7-ene-27, venta minorista avance 15-ene-27, nuevas ventas de viviendas 27-ene-27. Fechas de nov-dic 2026 no extraídas [VERIFICAR].
- **Tesoro**: documentos de refinanciación trimestral en `home.treasury.gov/.../quarterly-refunding/...` (200); próxima anunciada a comienzos de febrero [VERIFICAR].

## Propuesta de cadencia de actualización

| Cadencia | Qué | Días |
|---|---|---|
| Diaria (tarde en Madrid, ya lo hace el workflow de paneles) | Curva UST, curva BCE, €STR, Bund diario, RRP, deuda federal | Lun-vie |
| Semanal | WALCL y balance del Eurosistema, H.8, CFTC, EIA, BTF/OAT, subastas UST | Miércoles (EIA), jueves (Fed, EIA gas), viernes (CFTC, H.8) |
| Mensual, día de publicación | IPCA adelantado y final (4-nov, 18-nov), empleo EE. UU. (6-nov), IPC EE. UU. (10-nov), PPI (13-nov), producción industrial (16-nov), PCE (25-nov), JOLTS (1-dic), M3 y crédito BCE (~27-nov), TIC, MTS | Según calendario arriba |
| Trimestral | PIB (flash, 2.ª y 3.ª estimación), SLOOS, BLS del BCE, ECI | Oct-nov, ene-feb, abr-may, jul-ago |
| Anual | Deuda y déficit PDE | Abril y octubre |

Regla: actualizar el panel el mismo día de cada publicación oficial o al siguiente por la mañana, y en el workflow guardar la «fecha de dato» y la «fecha de lectura» para que el tablero no muestre un dato viejo como nuevo.

## Huecos (qué falta en el repo)
1. Empleo EE. UU. (nóminas), JOLTS, PCE core con serie y calendario propios.
2. Balance del Eurosistema y de la Fed, RRP (liquidez semanal).
3. Spreads diarios BTP-Bund y OAT-Bund (hoy solo mensual por el BCE).
4. Subastas europeas (AFT, Finanzagentur, Tesoro italiano) y TARGET2.
5. SLOOS de EE. UU. (FRED `DRTSCILM`, `DRTSCIS`, `DRTSCLCC`...) para completar la pareja con el BLS del BCE.
6. Producción industrial y comercio minorista de la zona euro, vivienda de EE. UU., déficit mensual (MTS).
7. Fecha de dato y calendario por serie, para disparar actualizaciones.

## Fuentes nuevas (no estaban en MAPA-DE-FUENTES)
- Bundesbank Statistik API `https://api.statistiken.bundesbank.de/rest/data/...` (CSV, sin clave): 200, Bund 10 años 2-nov 3,37 %.
- INSEE BDM `https://api.insee.fr/series/BDM/V1/data/SERIES_BDM/<id>` (SDMX XML, 200 sin clave en la prueba).
- Tesoro italiano (`dt.mef.gov.it`), página con resultados de subastas (HTML, 200).
- ISTAT SDMX `esploradati.istat.it/SDMXWS/rest/` (200).
- BLS API pública v2 (ya usada en el repo para el IPC; ampliar a empleo/JOLTS).
- BLS `schedule/news_release/*.htm` y BEA `news/schedule` como fuente de calendarios (200 con User-Agent identificado).
- Eurostat release calendar (solo con navegador).
- Census indicators calendar `census.gov/economic-indicators/calendar-listview.html` (200).
- EIA schedule del WPSR `eia.gov/petroleum/supply/weekly/schedule.php` (200) y CFTC release schedule (200).
- FRED `fredgraph.csv` para JTSJOL, PCEPILFE, GDPC1, WALCL, RRPONTSYD, HOUST, DRTSCILM (todas 200).
- Fed SLOOS/H.4.1/H.8 y FOMC calendar (200).

## Bloqueos y avisos
- `aft.gouv.fr`: 403 a curl, portada OK con Chrome; calendario de subastas sin localizar. Deuda negociable y resultados leídos solo con Chrome (una pestaña propia, cerrada).
- BEA API, EIA API v2 y Census API: piden clave gratuita (no creada ni introducida). FRED sin clave vale como alternativa.
- ECB `TGB` (TARGET balances): sin respuesta válida con mi clave; Data Portal en navegador queda pendiente.
- Eurostat `ei_bssi_m_r2` y `bop_c6_m`: consulta con parámetros inválidos o vacía; reintentar con la estructura del dataset.
- Calendarios del BCE estadístico y de AFT/Finanzagentur son páginas dinámicas: sin fechas leídas.
- `destatis.de` Calendar 404, `insee.fr/en/information/2861250` 404, `istat.it/en/calendar/` 500: rutas erradas o caídas, sin probar más.
- `congress.gov` y `senate.gov` siguen bloqueados (no se tocaron).
- Descargas a disco desde el navegador: ninguna; el XLSX/PDF de los calendarios «requiere OK de descarga».
- No verificado: cifras indicadas como [VERIFICAR] (horas exactas de publicación, fechas de diciembre, EA20 -1,1 % producción industrial, límite de consultas sin clave de BLS). Lo contrastado contra APIs oficiales el 3-nov-2026 es [P]; PMI y prensa son [S].
