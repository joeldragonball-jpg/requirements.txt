# A. Tipos de interés de los bancos centrales: fuentes y calendario de actualización

Fecha de lectura de todas las fuentes: **3-nov-2026** (curl con User-Agent identificado salvo donde se indica Chrome o búsqueda web). Nivel: [P] = web o API oficial leída hoy; [S] = fuente secundaria o búsqueda web, marcada [VERIFICAR]. No contiene recomendaciones de compra ni venta.

## Resumen (8 líneas)
1. La tabla `tipos_vivos` cubre 5 bancos con fuente primaria directa (Fed, BCE, BoE, BCB Brasil, Banco de Canadá) y `tipos_bis` otros 10 vía BIS (RU, ZA, MX, ID, IN, HK, CN, KR, JP, CH); lectura del 2-nov-2026 23:49 UTC, todo al día.
2. Faltan de tu lista: RBA, RBNZ, Riksbank, Norges Bank, Colombia, Chile, Perú y Argentina. Los 8 salen ya del mismo endpoint del BIS (`WS_CBPOL`) cambiando una lista de países (probado hoy), salvo Argentina, que no tiene tipo de política desde 10-jul-2025.
3. El BIS va días por detrás: hoy da Canadá 2,25 % (26-oct), cuando el Banco de Canadá subió a 2,50 % el 28-oct (efectivo 29-oct). Por eso conviene API propia del banco donde exista: Riksbank, Norges, SNB, BCRP y BCB responden abiertas y sin clave (probadas).
4. Sin API abierta desde curl: RBA (403 Akamai; la web HTML se lee bien con Chrome), RBNZ (bloquea también Chrome), Banxico (token gratuito), BCCh (usuario/clave gratuitos), BanRep (reto anti-bots en curl).
5. Calendarios oficiales leídos hoy: Fed, BCE, BoE, BoJ, RBA, Riksbank (hasta jun-2027), SNB y Norges (por búsqueda, [VERIFICAR] en web propia). El resto: [VERIFICAR] (ver tabla).
6. Hallazgos en el repo (no tocados): `eventos/calendario.toml` usa el día 1 de reuniones de dos días (BCE 16-dic-2026 es el día 1; decisión el 17-dic; Fed 8-dic, decisión el 9-dic; BoJ 29-oct y 17-dic, decisión el 30-oct y 18-dic). Y la ficha de Canadá (línea ~717) aún dice 2,25 %; el tipo es 2,50 %.
7. Cadencia propuesta: lanzar `actualizar_paneles` el día de la decisión (tras la hora de anuncio) y el día siguiente (los tipos «efectivos» cambian en la serie 0-1 días después); tabla fecha → qué actualizar más abajo.
8. Las reuniones de 2027 ya están publicadas para Fed, BCE, BoE, BoJ, RBA, SNB, Copom, BoC, RBNZ (hasta oct) y Norges; faltan Riksbank (2.º semestre), Banxico, BanRep, BCCh (sep-dic) y BCRP.

## 1. Diagnóstico del estado actual (`explorador/paneles.json`)
| Clave | Bancos | Fuente | Dato más reciente |
|---|---|---|---|
| `tipos_vivos` | Fed 3,75–4,00 % (cambio 17-sep, +25 pb); BCE depósito 2,50 % (16-sep, +25); BoE 3,75 % (18-dic-2025, -25); Brasil Selic 13,75 % (17-sep, -25); Canadá 2,50 % (29-oct, +25) | NY Fed, BCE data-api, BoE IADB, BCB SGS 432, Valet BoC: todas primarias | 30-oct a 2-nov-2026 |
| `tipos_bis` | Rusia 14,00; Sudáfrica 7,25; México 6,50; Indonesia 5,75; India 5,50; Hong Kong 4,25; China 3,00; Corea 3,00; Japón 1,25; Suiza 0,00 | BIS WS_CBPOL (primaria vía BIS) | 8-oct a 27-oct-2026 |

Notas: (a) «último cambio» es la fecha en la serie, no la de la reunión (Fed: reunión 15-16 sep, serie 17-sep; Canadá: anuncio 28-oct, serie 29-oct). (b) Para Japón, Suiza, México, Rusia y Sudáfrica el BIS da fecha de observación 26-27 oct; el banco puede haber decidido después (BoJ decidió el 30-oct, ver abajo: hay que comprobar contra su web, el BIS puede estar atrasado) [VERIFICAR]. (c) El Banco de Canadá ya se corrigió en `tipos_vivos`, pero el panel BIS no lo muestra: no mezclar fuentes sin indicar fecha.

## 2. Tabla por banco
Columnas: fuente primaria y URL · cómo se lee · prueba (3-nov-2026) · frecuencia · cadencia recomendada · reuniones/decisiones 2026-27 (fecha = día del anuncio; «d1-d2» = reunión de dos días, anuncio el último).

| Banco (zona) | Fuente oficial y URL | Cómo se lee | Prueba | Frecuencia | Cadencia | Reuniones 2026-27 |
|---|---|---|---|---|---|---|
| **Fed** (EE. UU.) | NY Fed `https://markets.newyorkfed.org/api/rates/unsecured/effr/last/1.json` (en uso) + FRED `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFEDTARU,DFEDTARL` (sin clave) | JSON / CSV | OK 200: EFFR 3,88 %, rango 3,75–4,00 (30-oct); FRED 4,00/3,75 hasta 2-nov | Diaria | Día de decisión + día siguiente | Dic: 8-9 · 2027: 26-27 ene, 16-17 mar*, 27-28 abr, 8-9 jun*, 27-28 jul, 14-15 sep*, 26-27 oct, 7-8 dic* (*con proyecciones). Fuente [P]: `federalreserve.gov/monetarypolicy/fomccalendars.htm` (actualizada 28-oct-2026) |
| **BCE** (zona euro) | `https://data-api.ecb.europa.eu/service/data/FM/B.U2.EUR.4F.KR.DFR.LEV?format=csvdata` (en uso; MRO: `...KR.MRR_FR.LEV`) | SDMX CSV | OK: DFR 2,50 % desde 16-sep-2026 (2,25 desde 17-jun) | Diaria (cambia tras decisión) | Día de decisión + siguiente | Consejo (decisión día 2): 17-dic-2026 · 2027: 4-feb, 18-mar, 29-abr, 10-jun, 22-jul, 9-sep, 28-oct, 16-dic. [P] `ecb.europa.eu/press/calendars/mgcgc/html/index.en.html` (el .ics oficial dio 404) |
| **BoE** (Reino Unido) | `https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=..&Dateto=now&SeriesCodes=IUDBEDR&CSVF=TN&UsingCodes=Y` (en uso) | CSV | OK: 3,75 % hasta 22-oct y siguientes | Diaria | Día de decisión + siguiente | 2026: 5-nov, 17-dic · 2027: 4-feb, 18-mar, 29-abr, 17-jun, 29-jul, 16-sep, 4-nov, 16-dic. [P] `bankofengland.co.uk/monetary-policy/upcoming-mpc-dates` |
| **BoJ** (Japón) | Tipo: BIS (en uso). Calendario: `https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm`. Series: `stat-search.boj.or.jp` | Tipo: CSV BIS. Calendario: HTML | Calendario OK. Web de series responde 200 (API no explorada) | BIS diaria con retraso | Día de decisión + 2 días (BIS) | 2026: 30-oct (hecho; el BIS dio 1,25 % con fecha 27-oct, comprobar si cambió), 18-dic · 2027 (reunión d1-d2, anuncio d2): 21-22 ene, 17-18 mar, 27-28 abr, 10-11 jun, 21-22 jul, 21-22 sep, 28-29 oct, 16-17 dic [P] |
| **SNB** (Suiza) | API `https://data.snb.ch/api/cube/snbgwdzid/data/csv/en` (serie «LZ» = tipo SNB); calendario: `snb.ch/en/services-events/digital-services/event-schedule` | CSV `;` (1 MB: usar `fromDate`) | OK: LZ = 0 % (30-oct-2026; 0 desde 20-jun-2025) | Diaria | Día de decisión + siguiente | 10-dic-2026 · 2027: 18-mar, 24-jun, 23-sep, 16-dic. Calendario por búsqueda web de la página oficial [VERIFICAR en la página] |
| **BoC** (Canadá) | Valet `https://www.bankofcanada.ca/valet/observations/V39079/json?recent=3` (en uso) | JSON | OK: 2,25 hasta 28-oct, 2,50 desde 29-oct | Diaria | Día de decisión + siguiente | 2026: 9-dic [VERIFICAR] (publicación oficial del BoC de 27-jul-2026, vista por búsqueda) · 2027: 27-ene, 3-mar, 28-abr, 2-jun, 21-jul, 8-sep, 27-oct, 8-dic [VERIFICAR] (`bankofcanada.ca/2026/07/bank-canada-publishes-2027-schedule-...`) |
| **RBA** (Australia) | Tipo: `https://www.rba.gov.au/statistics/cash-rate/` (tabla HTML). Calendario: `https://www.rba.gov.au/schedules-events/board-meeting-schedules.html` | HTML; curl 403 (Akamai) | **Chrome OK**: 4,60 % desde 30-sep-2026 (+25). BIS: 4,60 (22-oct) | Cada reunión | Día de reunión + siguiente (cambio efectivo al día siguiente) | 2026: **2-3 nov** (anuncio 3-nov 14:30 Sídney), 7-8 dic · 2027: 8-9 feb, 22-23 mar, 3-4 may, 21-22 jun, 9-10 ago, 27-28 sep, 1-2 nov, 13-14 dic [P] |
| **RBNZ** (N. Zelanda) | Calendario: `rbnz.govt.nz/news-and-events/how-we-release-information/ocr-decision-dates-and-financial-stability-report-dates-to-feb-2028`. Tipo: BIS | BIS CSV | **Bloqueado** (curl 403; Chrome: «browser issue») | 7-8 al año | BIS día siguiente | 2026: 9-dic · 2027: 10-feb, 17-mar, 5-may, 16-jun, 4-ago, 15-sep, 27-oct (dic-2027 sin confirmar). Vía búsqueda, [VERIFICAR]. Tipo 2,75 % (BIS 23-oct; búsqueda: mantenido el 28-oct) |
| **Riksbank** (Suecia) | API `https://api.riksbank.se/swea/v1/Observations/SECBREPOEFF/{fecha}` (sin clave) + calendario `riksbank.se/en-gb/press-and-published/calendar/` | JSON | OK: 1,75 % (2-nov-2026) | Diaria | Día de decisión + siguiente | 2026: 4-nov (publicación, 09:00), 16-dic · 2027: 2-feb, 23-mar, 4-may, 21-jun (calendario oficial `.../calendar-2027/`; jul-dic sin publicar). Aplica desde el jueves/viernes posterior |
| **Norges Bank** (Noruega) | API `https://data.norges-bank.no/api/data/IR/B.KPRA.SD.?format=csv&lastNObservations=3&locale=en` (sin clave) | CSV | OK: 4,50 % (29-oct-2026) | Diaria | Día de decisión + siguiente | 2026: 5-nov, 17-dic · 2027: 21-ene, 18-mar, 5-may, 17-jun, 19-ago, 23-sep, 4-nov, 16-dic (búsqueda sobre calendario oficial `norges-bank.no/en/news-events/calendar/policy-rate-decisions/`; la web es JS) [VERIFICAR] |
| **BCB** (Brasil) | SGS 432 `https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/2?formato=json` (en uso) | JSON (trae fechas futuras: ignorar) | OK: 13,75 % | Diaria | Día de decisión + siguiente | Copom: **3-4 nov**, 8-9 dic · 2027: 26-27 ene, 16-17 mar, 27-28 abr, 15-16 jun, 3-4 ago, 21-22 sep, 26-27 oct, 7-8 dic [VERIFICAR: calendario oficial citado por CNN Brasil / Canal Rural; la web bcb.gov.br/.../copomcalendar es JS (con Chrome sí se lee, según ACCESOS-CHROME)] |
| **BanRep** (Colombia) | Tipo: BIS (12,25 % el 23-oct). Calendario: `https://www.banrep.gov.co/es/calendario-junta-directiva` | BIS CSV | curl: reto anti-bots (redirige a validate.perfdrive.com). Chrome carga la web, el calendario es dinámico y no devolvió texto | Mensual | Día de decisión + siguiente | 2026 (Portafolio [S]): 30-oct (hecho, 12,25 % sin cambio), 18-dic · 2027: sin publicar en lo encontrado [VERIFICAR] |
| **BCCh** (Chile) | Tipo: BIS 4,50 % (27-oct) o `https://mindicador.cl/api/tpm` (agregador [S], 4,5 % el 2-nov). Calendario: `bcentral.cl/en/content/-/detalle/calendario-de-politica-monetaria-2026` | JSON / BIS | mindicador OK. API oficial `si3.bcentral.cl/SieteRestWS` pide usuario y clave (gratis con registro): no probada | 8 al año | Día de RPM + siguiente | 2026: 15-dic · 2027: 25-26 ene, 30 mar, 26-27 abr, 15 jun, 26-27 jul (resto sin publicar) [VERIFICAR] |
| **BCRP** (Perú) | API `https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04722MM/json/2026-8/2026-11/ing` (tasa de referencia, sin clave) | JSON mensual | OK: 4,25 % (ago-oct 2026) | Mensual (programa monetario) | Segundo jueves aprox. + siguiente [VERIFICAR] | Calendario `bcrp.gob.pe/politica-monetaria/programa-monetario.html` devuelve «Pardon Our Interruption» (anti-bots): no leído. Fechas: [VERIFICAR] |
| **BCRA** (Argentina) | API v4.0 `https://api.bcra.gob.ar/estadisticas/v4.0/monetarias` (v3.0 devuelve 410, deprecada) | JSON | OK. Sin tipo de política desde 10-jul-2025 (último 29 %). Alternativas: TAMAR privados 26,89 %, BADLAR 22,75 %, pases entre terceros 1 día 21,86 % (30-oct-2026) | Diaria | Semanal (no hay reuniones de tipos) | No hay calendario de tipo; referencia: mercado, no decisión |
| **Banxico** (México) | Tipo: BIS 6,50 % (27-oct). API SIE `banxico.org.mx/SieAPIRest/service/v1/series/SF61745/datos/oportuno` pide **token gratuito** (registro) | JSON | Respuesta «token inválido» (como se esperaba) | 8 al año | Día de anuncio + siguiente | 2026 (política, sin reunión intermedia): 5-feb, 26-mar, 7-may, 25-jun, 6-ago, 24-sep (hechos), **5-nov, 17-dic** [VERIFICAR: solo blog; el PDF oficial `banxico.org.mx/politica-monetaria/d/{3B4BDA5B-...}.pdf` sale en búsqueda pero no lo abrí] · 2027: sin publicar en lo encontrado |

Tipos BIS también disponibles para: AU 4,60; CA 2,25 (desfase); CL 4,50; CO 12,25; GB 3,75; NO 4,50; NZ 2,75; PE 4,25; SE 1,75; US 3,875 (punto medio); XM 2,50; AR 29 (2025-07-10); BR 13,75 (BIS WS_CBPOL, `lastNObservations=1`, leído hoy).

## 3. Calendario de actualización propuesto (desde 3-nov-2026)
Regla: ejecutar `leer_tipos`/`leer_tipos_bis` (y las lecturas nuevas) el día del anuncio tras la hora de publicación y de nuevo el día siguiente; fuera de esos días, una pasada semanal de control (el panel ya se actualiza con el flujo habitual). Las fechas son el día de anuncio; «efectivo» puede ser el día siguiente.

| Fecha | Banco / evento | Qué actualizar |
|---|---|---|
| 3-nov (mar) | RBA (anuncio 14:30 Sídney) | Chrome/BIS: tipo RBA el 4-nov; pendiente añadir RBA |
| 3-4 nov | Copom (decisión el 4) | `tipos_vivos` Brasil el 5-nov |
| 4-nov | Riksbank | Riksbank API el 4 y 5-nov |
| 5-nov | BoE, Norges, Banxico [VERIFICAR] | `tipos_vivos` BoE; Norges por API; Banxico por BIS |
| 9-dic | Fed (8-9), BoC, RBNZ [VERIFICAR] | `tipos_vivos` EE. UU. y Canadá el 9 y 10-dic; RBNZ vía BIS |
| 9-dic | Copom (8-9) | Brasil 10-dic |
| 10-dic | SNB | SNB API |
| 15-dic | BCCh (RPM) | BIS Chile / mindicador |
| 16-dic | Riksbank | Riksbank API |
| 17-dic | BCE, BoE, Norges | BCE data-api, BoE, Norges |
| 17-dic | Banxico [VERIFICAR] | BIS México |
| 18-dic | BoJ, Banco de Rusia (toml), BanRep [S] | BIS Japón/Rusia/Colombia a los 2 días |
| 2027: 21-ene Norges · 22-ene BoJ · 26-27-ene Fed y Copom · 27-ene BoC · 28-ene Riksbank [VERIFICAR] | primera ronda del año | Fed, BoC, BoJ, Norges, Brasil |
| 2027: 2-feb Riksbank · 4-feb BCE y BoE · 8-9-feb RBA · 10-feb RBNZ | febrero | cada banco |
| 2027: 16-17-mar Fed y Copom · 17-mar RBNZ · 18-mar BCE, BoE, SNB, Norges, BoJ · 22-23-mar RBA · 23-mar Riksbank | marzo (mes denso) | todos los de la tabla |
| 2027: abr: 27-28 Fed, Copom, RBA (3-4 may) · 28 BoC · 29 BCE y BoE | abril-mayo | cada banco |
| 2027: jun: 8-9 Fed · 10 BCE · 11 BoJ · 15-16 Copom · 17 BoE, Norges · 21 Riksbank · 21-22 RBA · 24 SNB | junio | ídem |
| 2027: jul-dic | ver columna de la tabla; los que faltan (Riksbank, Banxico, BanRep, BCCh, BCRP) se leen cuando publiquen | |

Alternativa mínima (si se quiere simplificar): una sola ejecución diaria del panel durante «semanas de decisión» (las de la lista de arriba) y semanal el resto; la lectura de calendarios (Fed/BCE/BoE/BoJ/RBA/Riksbank/SNB) cada trimestre, porque publican con un año de antelación.

## 4. Huecos
1. Sin lectura propia en el repo: RBA, RBNZ, Riksbank, Norges, SNB, Colombia, Chile, Perú, Argentina (el BIS los cubre salvo AR). Añadir al URL_BIS_TIPOS: `AU+NZ+SE+NO+CO+CL+PE+AR+US+XM+GB+CA+BR` (usado hoy: 13 países, un solo CSV).
2. Japón, Suiza, México, Rusia y Sudáfrica dependen del BIS con desfase de 1-7 días: verificar al día siguiente de cada reunión.
3. Calendarios 2027 sin fecha oficial leída: Riksbank (jul-dic), Banxico, BanRep, BCCh (sep-dic), BCRP.
4. Calendarios leídos solo por búsqueda (secundaria): BoC, Norges, SNB, RBNZ, Copom, Banxico 2026, BanRep 2026, BCCh. Marcados [VERIFICAR].
5. `calendario.toml`: usar el día de decisión (día 2) en reuniones de dos días; Canadá sigue citando 2,25 %.
6. Argentina: no existe tipo de política. Mostrar TAMAR/BADLAR con etiqueta explícita, no como «tipo oficial».
7. BCE tipo de refinanciación principal y facilidad marginal no están en la tabla (la API los da).

## 5. Fuentes nuevas respecto a `research/MAPA-DE-FUENTES.md`
| Fuente | Uso | Estado (3-nov-2026) |
|---|---|---|
| Riksbank SWEA API `api.riksbank.se/swea/v1` | Tipo de política diario, sin clave | OK |
| Norges Bank `data.norges-bank.no/api/data/IR/...` | Tipo clave, SDMX, sin clave | OK |
| SNB `data.snb.ch/api/cube/snbgwdzid/...` | Tipo SNB (LZ), SARON | OK |
| BCRP `estadisticas.bcrp.gob.pe/estadisticas/series/api/` | Tasa de referencia mensual | OK sin clave |
| BCRA API v4.0 | Variables monetarias (TAMAR, BADLAR, pases) | OK; v3 muerta |
| FRED `fredgraph.csv?id=DFEDTARU,DFEDTARL` | Rango de la Fed sin clave, cotejo de NY Fed | OK |
| BIS WS_CBPOL ampliado a 13 países | Cobertura del hueco 1 | OK |
| mindicador.cl `/api/tpm` | TPM Chile [S] | OK; agregador, no oficial |
| Banxico SIE (token gratuito) | Tipo objetivo México | Requiere registro |
| BCCh SieteRestWS (usuario/clave gratuitos) | TPM Chile oficial | Requiere registro; no probado |
| RBA web «cash-rate» | Historial HTML del tipo | Solo Chrome |
| CEMLA | Calendarios latinoamericanos | No probado (sin tiempo) |
| BoJ `stat-search.boj.or.jp` | Series BoJ | Responde 200; API no explorada |

## 6. Bloqueado o pendiente
- **RBNZ** (curl 403; Chrome: «browser issue»): bloqueado, no insistir. Calendario de búsqueda web, tipo vía BIS.
- **RBA** curl 403 (Akamai, `Access Denied`): solo Chrome (HTML); la descarga del CSV F1 requeriría OK de descarga.
- **BanRep**: curl redirige a validate.perfdrive.com; Chrome carga pero el calendario no se vuelca como texto; URLs de estadísticas probadas dieron 404 (ruta equivocada).
- **BCRP** calendario: «Pardon Our Interruption» (reto anti-bots), no leído.
- **Banxico** calendario oficial: ruta de curl 404 y PDF no abierto (visor de PDF no funciona en Chrome según ACCESOS-CHROME).
- **BCE .ics**: 404.
- Tab de Chrome propia cerrada al terminar. No se descargó nada a disco del repo (los HTML de prueba están en el scratchpad).
