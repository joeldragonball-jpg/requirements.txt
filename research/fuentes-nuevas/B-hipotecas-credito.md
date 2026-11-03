# B. Fuentes de datos: hipotecas y crédito (lectura 3-nov-2026)

## Resumen (8 líneas)
1. El panel `credito` de `explorador/paneles.json` ya tiene 27 series (BCE vía API abierta, Freddie Mac, Banco de Inglaterra, Fed H.8 vía FRED, Banco de Japón): euríbor 12m, hipotecas nuevas TAE y tipo pactado (España y zona euro), crédito a hogares/empresas, BLS (criterios y demanda, zona euro y España), PMMS, H.8, BoE, BoJ.
2. `explorador/espana.json` ya recoge a mano, bloque `vivienda_hipotecas`, IPV del INE, tasación (MIVAU), compraventas, hipotecas INE (nº y tipo), TAE MIR, euríbor y morosidad BdE; la morosidad sale de prensa [S], no de la fuente oficial.
3. Huecos principales: precios de vivienda en el panel automático (INE IPV, Eurostat, Case-Shiller), morosidad oficial, volumen de nuevas hipotecas (importe), SLOOS de EE. UU., y toda Sudamérica.
4. Todo lo marcado «API/CSV sin clave» abajo respondió HTTP 200 con dato de sep-2026 u oct-2026 desde este equipo.
5. Avisos: la Fed retira «Build Your Package» del DDP la semana del 9-nov-2026 (la página sloos.htm sigue enlazando los informes SLOOS; FRED sigue sirviendo las series DRTS*). Impacto en el panel: nulo, ya que H.8 y SLOOS se leen por FRED, pero mantener FRED como ruta principal.
6. Bloqueos: Notarios (sin respuesta, también en Chrome), Idealista (403), MBA (403), SBS Perú (Incapsula, anti-bot), Superfinanciera Colombia (500), BanRep (404 en la URL probada), CMF Chile (HTML sin CSV directo).
7. Mejores altas fáciles (sin clave): Eurostat HPI, INE IPV (API ya en uso), FRED SLOOS/Case-Shiller/morosidad, BCB SGS (Brasil), BCRP (Perú), BIS precios de vivienda.
8. Cadencia: mensual, el día hábil siguiente a la publicación del BCE (MIR/BSI, aprox. día 23-25 del mes siguiente) y trimestral para BLS (tras la reunión de enero/abril/julio/octubre); semanal los jueves para Freddie Mac.

## Series que ya tiene el panel (id, país, fecha del último dato)
euribor12 (Z. euro, 2026-10) · hip_es, hip_es_tipo (España, 2026-09) · hip_ea (Z. euro, 2026-09) · hog_es, hog_ea, emp_ea (2026-09; emp_es existe en CREDITO pero no apareció en la lectura, [VERIFICAR] fallo) · hip_us30 (EE. UU., 2026-10-29) · hip_uk, aprob_uk (R. Unido, 2026-09) · cred_us_total/inmob/cons/emp (EE. UU., 2026-09) · cred_jp (Japón, 2026-08) · 12 series BLS (criterios y demanda: empresas, vivienda, consumo; Z. euro y España; 2026-T4).

## Tabla de fuentes

Todas las pruebas: curl con User-Agent identificado, 3-nov-2026. «Sin clave» = no pide registro.

| Región | Indicador | Fuente oficial | URL | Cómo se lee | Prueba (3-nov-2026) | Publicación | Cadencia recomendada | Prioridad |
|---|---|---|---|---|---|---|---|---|
| España | Hipotecas nuevas TAE y tipo pactado (ya en panel) | BCE/BdE, MIR | `data-api.ecb.europa.eu/service/data/MIR/M.ES.B.A2C.A.C.A.2250.EUR.N` (tipo: `...A.R.A...`) | API CSV, sin clave | OK, 2026-09 = 3,04 % / 2,99 % | Mensual, ~5 semanas tras el mes (BCE publica MIR hacia el día 1-5 del 2.º mes siguiente) [VERIFICAR] | Mensual, día de publicación MIR | Ya hecha |
| España | Importe de nuevas hipotecas (volumen) | BCE, MIR volúmenes | `MIR/M.ES.B.A2C.A.B.A.2250.EUR.N` (nuevo negocio, volumen) [VERIFICAR clave] | API CSV | Clave no probada | Mensual, con MIR | Mensual | 2 |
| España | Stock hipotecas vivienda (saldo) | BCE BSI | `BSI/M.ES.N.A.A22.A.1.U2.2250.Z01.E` | API CSV | OK, 2026-09 = 530.589 M€ | Mensual (~día 28 del mes siguiente) | Mensual | 2 |
| España | Hipotecas sobre viviendas: nº, importe, tipo | INE, HPT | `servicios.ine.es/wstempus/js/ES/DATOS_TABLA/13896?nult=1` (tipo: tabla 24457) | API JSON, sin clave | OK (60 KB) | Mensual, ~2 meses de retraso; calendario INE | Mensual, día de publicación INE | 1 (ya está en espana.json a mano; automatizar) |
| España | Índice de Precios de Vivienda | INE, IPV | `.../DATOS_TABLA/25171?nult=1` (la 79563 que usa espana.json también) | API JSON | OK (53 KB) | Trimestral, ~mediados de cada trimestre+1 | Trimestral, día INE | 1 |
| España | Compraventas de vivienda | INE, ETDP | `.../DATOS_SERIE/ETDP1826` | API JSON | Referenciada en espana.json (no repetida) | Mensual | Mensual | 3 |
| España | Series BdE (tipos, deuda) | Banco de España | `bde.es/webbe/es/estadisticas/compartido/datos/csv/be0601.csv` y `be1101.csv` | CSV directo, sin clave, codificación latin-1 | OK (49 KB y 17 KB) | Mensual/trimestral; contenido de be0601 por inspeccionar, [VERIFICAR] qué series hipotecarias trae | Mensual | 3 |
| España | Euríbor oficial | EMMI | `emmi-benchmarks.eu/benchmarks/euribor/rate/` | HTML (200, 53 KB); valor diario | OK; el panel usa el euríbor 12m mensual vía BCE (equivalente) | Diario hábil | Mensual (media) suficiente; opcional diario | Ya hecha |
| España | Morosidad de la banca | BdE, estadísticas supervisoras (`bde.es`, Boletín Estadístico cap. 4) / BCE SUP | BCE SUP: clave probada `Q.ES.W0...I4001...` dio 400/404 | API BCE probada sin éxito; falta localizar clave exacta | Fallo: clave incorrecta | Trimestral (BCE SUP), mensual (BdE) | Mensual/trimestral | 1 (ahora solo prensa [S]) |
| España | Registradores (compraventas e hipotecas registrales) | Colegio de Registradores | `registradores.org/actualidad/portal-estadistico-registral` | HTML/PDF, sin API | HTTP 200 (99 KB), datos en PDF/Power BI [VERIFICAR] | Mensual/trimestral | Trimestral, lectura manual | 3 |
| España | Notarios (compraventas, hipotecas, préstamo medio) | Consejo General del Notariado | `consejo-notariado.org/portal-estadistico/` | HTML/Power BI | BLOQUEADA: curl sin respuesta y Chrome error de página | Mensual, ~2 meses | — | Bloqueada |
| España | Tasaciones | MIVAU/OVS (valor tasado) y Tinsa | `tinsa.es/precio-vivienda/` (HTML 200) | HTML, sin API | OK, página cargó | Trimestral/mensual | Trimestral; Tinsa = [S] (privada) | 3 |
| España | Idealista / Fotocasa | Privadas, [S] | `idealista.com/sala-de-prensa/...` 403; `fotocasa.es/indice/` 200 | HTML | Idealista bloqueada; Fotocasa carga (532 KB) | Mensual | Solo contraste, no panel | 4 |
| Zona euro | MIR / BSI | BCE | `data-api.ecb.europa.eu/service/data/{MIR,BSI}` | API CSV | OK | Mensual | Mensual, tras publicación | Ya hecha |
| Zona euro | BLS | BCE | `.../BLS/Q.ES.ALL.Z.H.H.B3.ST.S.FNET` | API CSV | OK, 2026-Q4 | Trimestral (enero, abril, julio, octubre) | Trimestral | Ya hecha |
| Zona euro | Precios de vivienda | Eurostat `prc_hpi_q` | `ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hpi_q?format=JSON&geo=ES&geo=EA&purchase=TOTAL&unit=I15_Q&lastTimePeriod=2` | API JSON (JSON-stat), sin clave | OK, actualizado 1-oct-2026 | Trimestral, ~3 meses después | Trimestral | 1 |
| EE. UU. | Freddie Mac PMMS (ya en panel) | Freddie Mac | `freddiemac.com/pmms/docs/PMMS_history.csv` | CSV, sin clave | OK, 7,24 % (29-oct-2026) | Semanal, jueves | Semanal, jueves | Ya hecha |
| EE. UU. | SLOOS: criterios de crédito a empresas (C&I grandes) | Fed vía FRED | `fred.stlouisfed.org/graph/fredgraph.csv?id=DRTSCILM` | CSV, sin clave | OK, 2026-10-01 = 1,7 | Trimestral, tras la reunión del FOMC (febr., mayo, ag., nov.) | Trimestral; encuesta de octubre ya publicada | 2 |
| EE. UU. | SLOOS: tarjetas (`DRTSCLCC`), subprime? hipotecas (`DRTSSP`=Spanish? ver nota) | FRED | `...?id=DRTSCLCC` (4,0, 2026-10-01); `DRTSSP` (20,0) | CSV | OK; `DRTSPM` solo hasta 2014 (sin uso) | Trimestral | Trimestral | 2 [VERIFICAR] nombre exacto de DRTSSP en FRED |
| EE. UU. | Hipotecas: morosidad de bancos | FRED `DRSFRMACBS` (tasa de morosidad hipotecas residenciales, bancos) | `...?id=DRSFRMACBS` | CSV | OK, 2026-04-01 = 1,86 % (dato tardío) | Trimestral | Trimestral | 1 |
| EE. UU. | Case-Shiller nacional | S&P/FHFA vía FRED | `...?id=CSUSHPINSA` | CSV | OK, 2026-08 = 336,74 | Mensual, último martes (retraso 2 meses) | Mensual, último martes | 1 |
| EE. UU. | FHFA HPI | FHFA vía FRED | `...?id=USSTHPI` | CSV | OK, 2026-04 = 719,87 (trimestral) | Trimestral | Trimestral | 3 |
| EE. UU. | Fed H.8 (ya en panel) | Fed vía FRED | `federalreserve.gov/releases/h8/` | CSV FRED | Ya en panel | Semanal (viernes) | Semanal/mensual | Ya hecha |
| EE. UU. | MBA solicitudes de hipotecas | MBA | `mba.org/...weekly-applications-survey` | HTML | BLOQUEADA (403) | Semanal, miércoles | — | Bloqueada |
| EE. UU. | NY Fed deuda de los hogares | NY Fed | `newyorkfed.org/microeconomics/hhdc` | HTML 200 (104 KB), PDF/Excel [VERIFICAR] | OK | Trimestral | Trimestral | 3 |
| EE. UU. | Census, construcción residencial | Census | `api.census.gov/data/timeseries/eits/resconst` | API; pide clave (página «Missing Key») | Requiere registro de clave, no creada | Mensual | — | Requiere registro |
| Brasil | Selic meta (SGS 432) | BCB | `api.bcb.gov.br/dados/serie/bcb.sgs.432/dados/ultimos/2?formato=json` | API JSON, sin clave | OK, 13,75 % (3-nov-2026) | Cada reunión del Copom (8 al año) | El día de cada reunión | 2 |
| Brasil | Tipo medio financiación inmobiliaria, personas físicas, recursos direccionados | BCB SGS 25497 (mercado), 25498 (regulado), 25499 (total), todas % al mes; 20772 (mercado), 20773 (regulado), 20774 (total), % al año | `api.bcb.gov.br/dados/serie/bcb.sgs.20774/dados/ultimos/13?formato=json` | API JSON, sin clave | OK, 20772 = 14,20 % y 20773 = 10,94 % (sep-2026); `dadosabertos.bcb.gov.br` confirma nombres | Mensual, ~fin del mes siguiente | Mensual | 1 |
| Brasil | Saldo de crédito inmobiliario | BCB SGS | códigos no confirmados | API | — [VERIFICAR] | Mensual | Mensual | 3 |
| Chile | TPM, tasas hipotecarias | BCCh (SiETE) y CMF | `si3.bcentral.cl/SieteRestWS/...` | API REST, pide usuario/contraseña registrados | Respondió HTML de aviso; requiere registro | Diaria/mensual | — | Requiere registro |
| Chile | Tasas y créditos hipotecarios | CMF | `cmfchile.cl/portal/estadisticas/617/w3-channel.html` | HTML 200 (123 KB), enlaces a Excel [VERIFICAR] | OK la página; descarga requiere OK | Mensual | Mensual manual | 3 |
| Colombia | Tasas de colocación vivienda | Superfinanciera / BanRep | `superfinanciera.gov.co/...` → 500; `banrep.gov.co/es/estadisticas/tasas-colocacion` → 404 | HTML | Superfinanciera con error 500; BanRep URL cambió | Semanal/mensual | — | Pendiente (reintentar con la URL vigente) |
| Argentina | Tasas y crédito hipotecario | BCRA | `api.bcra.gob.ar/estadisticas/v3.0/monetarias` → 410 (v3 retirada) | API nueva versión (v4) [VERIFICAR] | v3 deprecada | Diaria | — | 3 (probar v4) |
| Perú | Tasas activas (MN) | BCRP | `estadisticas.bcrp.gob.pe/estadisticas/series/api/PN07807NM/json/2025-1/2026-9` | API JSON, sin clave | OK (respuesta con config y series) | Mensual | Mensual | 2 |
| Perú | Crédito y morosidad por entidad | SBS | `sbs.gob.pe/app/pp/EstadisticaSBS/...` | HTML | BLOQUEADA (Incapsula anti-bot); no insistido | Mensual | — | Bloqueada |
| Global | Precios de vivienda residenciales por país | BIS | `bis.org/statistics/pp.htm` | CSV/Excel (descarga) | Página OK (245 KB); datos como archivo: requiere OK de descarga | Trimestral | Trimestral | 3 |

## Huecos
- Precios de vivienda (INE IPV, Eurostat, Case-Shiller) no están en el panel automático.
- Morosidad oficial (BdE/BCE SUP): falta la clave correcta. Sugerencia: listar series con `.../service/data/SUP/Q.ES.*?lastNObservations=1` desde un script, o usar el Boletín Estadístico del BdE.
- Volumen/importe de nuevas hipotecas y stock de hipotecas vivienda (BCE BSI A22 funciona).
- Sudamérica: ninguna serie hoy; Brasil es lo más fácil.
- Calendario: el panel no enlaza lecturas con fechas de reunión (BCE, Fed, Copom). Se puede reutilizar el calendario de eventos existente.

## Fuentes nuevas (no estaban en MAPA-DE-FUENTES.md)
FRED (SLOOS, Case-Shiller, morosidad), Eurostat `prc_hpi_q`, BCB SGS, BCRP series API, BIS precios de vivienda, EMMI euríbor. En el mapa solo figuraban BoE, BdE `be1101.csv`, INE y BOE.

## Prioridad de series que añadiría al panel de crédito
1. INE IPV (precio vivienda, España) y hipotecas INE (nº y tipo).
2. Morosidad de la banca (oficial, tras localizar la clave).
3. Eurostat precios de vivienda (España y zona euro).
4. Brasil: tipo hipotecario SGS 20774 (o 25499) y Selic 432.
5. Case-Shiller y morosidad hipotecaria EE. UU. (FRED).
6. SLOOS EE. UU. (DRTSCILM, DRTSCLCC) con cadencia trimestral.
7. Perú BCRP tasa activa; Argentina BCRA v4 (probar).
8. Importe de nuevas hipotecas y saldo (BCE MIR/BSI).

## Bloqueos (anotados, sin insistir)
- Notarios: sin respuesta por curl y por Chrome (una prueba, 3-nov-2026).
- Idealista (403), MBA (403), SBS Perú (Incapsula), Superfinanciera (500), BanRep (404), Census (clave), BCCh SiETE (registro), BCRA v3 (410).
- Descargas de CMF, BIS y Registradores: requiere OK de descarga.

Nota: todo lo no contrastado en detalle está marcado [VERIFICAR]. No es recomendación de compra ni de venta.
