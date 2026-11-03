# E · Fuentes de datos de Sudamérica (Brasil, Argentina, Chile, Colombia, Perú; Uruguay y México como referencia)

Leído y probado el 3-nov-2026 (curl con User-Agent identificado, Chrome y búsquedas web). Solo fuentes y datos; sin recomendaciones de compra/venta. Lo no contrastado va como [VERIFICAR].

## Resumen (8 líneas)
1. Hoy el tablero no tiene ningún país sudamericano en `paises.json` (12 países: España, Alemania, Francia, Italia, Países Bajos, Polonia, EE. UU., China, Japón, India, Reino Unido, Rusia) ni en `indicadores-manual.json` (US, GB, RU, JP, CN, IN, IT) ni en `estabilidad.json` (solo Perú aparece como mención en 25 sitios del texto, sin ficha). `elecciones.json` sí trae Brasil (2.ª vuelta 25-oct-2026, ya pasada), Argentina (24-oct-2027) y México (jun-2027).
2. Brasil es el país mejor servido: la API SGS del BCB (sin clave) devuelve JSON con tipo, IPCA, paro, cambio, reservas y deuda; IBGE SIDRA da el IPCA; Olinda da el Focus. Todo probado y funcionando.
3. Argentina: `apis.datos.gob.ar/series` (INDEC/MECON, sin clave) y `api.bcra.gob.ar/estadisticas/v4.0` (sin clave; la v3 está retirada, devuelve 410) funcionan; `api.argentinadatos.com` (tercero, sin clave) da dólar, riesgo país e inflación al día pero NO es oficial.
4. Perú: la API del BCRP (`estadisticas.bcrp.gob.pe/estadisticas/series/api/<serie>/json/<desde>/<hasta>`) funciona sin clave y es la más limpia de la región.
5. Colombia: TRM oficial vía datos.gov.co (Socrata, sin clave) funciona; BanRep (SUAMECA) y DANE son páginas dinámicas/JS sin API probada; tasa y IPC quedan manuales o por Banco Mundial.
6. Chile: el BCCh tiene API (SieteRestWS) pero exige usuario y contraseña gratuitos (solo anotado); `bcentral.cl` responde con protección Incapsula (no se salta). Como mirror usable: `mindicador.cl` (tercero; TPM, dólar, UF e Imacec al día, pero su IPC está parado en dic-2025).
7. México (Banxico SIE) exige token gratuito; Uruguay (BCU/INE) responde 200 en HTML pero sin API probada. Banco Mundial funciona para los 7 países (último dato anual 2024-2025; `lastupdated` 2026-10-08). FMI DataMapper: 403 con un User-Agent personalizado, 200 con `curl/8` (inconsistente).
8. Para automatizar primero: Brasil (SGS + SIDRA + Focus), Perú (BCRP), Argentina (datos.gob.ar + BCRA v4) y TRM de Colombia; calendario ligado a las reuniones: Copom 3-4 nov y 8-9 dic; BCCh 15 dic; INDEC IPC octubre el 12-nov.

## Tabla por país
Prueba = consulta mínima del 3-nov-2026. Prioridad: A = automatizar ya; B = automatizar después; C = manual/[VERIFICAR].

| País | Indicador | Fuente oficial | URL / endpoint | Cómo se lee | Prueba y último dato | Publicación | Cadencia recomendada | Prior. |
|---|---|---|---|---|---|---|---|---|
| BR | Tipo oficial (Selic meta) | BCB SGS 432 | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/3?formato=json` | JSON, sin clave | 200. 13,75 % (fechas 2-4 nov). OJO: prensa (Renova Invest, vía búsqueda) dice 14,25 % desde 17-jun-2026: **discrepancia [VERIFICAR]** antes de volcar | En cada reunión del Copom | Tras cada Copom: 3-4 nov (decisión miércoles 4-nov), 8-9 dic; 2027: 26-27 ene, 16-17 mar, 27-28 abr, 15-16 jun, 3-4 ago, 21-22 sep, 26-27 oct (+ diciembre sin confirmar) [fechas de prensa, VERIFICAR en bcb.gov.br] | A |
| BR | Calendario Copom 2026-27 | BCB `bcb.gov.br/en/monetarypolicy/copomdates` | página con JS | curl da HTML vacío; Chrome carga pero `get_page_text` no extrae (pendiente de leer con `javascript_tool`, ver ACCESOS-CHROME) | Fechas 2026 por prensa: 27-28 ene, 17-18 mar, 28-29 abr, 16-17 jun, 4-5 ago, 15-16 sep, 3-4 nov, 8-9 dic | Anual (2027 publicado 23-jun-2026 según prensa) | Anual | B |
| BR | IPCA mensual y 12 m | IBGE SIDRA tabla 1737 | `https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/63/p/last%202` (v 2265 = 12 m) | JSON, sin clave | 200. sep-2026: +0,82 % m/m; 4,58 % 12 m (ago: -0,32 %). Espejo BCB SGS 433 / 13522 coincide | Mensual (~día 10) | Mensual, el día del IPCA (calendario IBGE; `servicodados.ibge.gov.br/api/v3/calendario` dio timeout, no leído) | A |
| BR | Expectativas Focus (IPCA, Selic, PIB) | BCB Olinda | `https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=2&$filter=Indicador eq 'IPCA'&$orderby=Data desc&$format=json` (y `ExpectativasMercadoSelic`) | OData JSON, sin clave | 200. 23-oct-2026: IPCA 2026 media 5,18 % (mediana 5,19), 2027 4,38 % | Semanal (lunes) | Semanal | A |
| BR | Paro (PNAD) | IBGE vía BCB SGS 24369 | `.../bcdata.sgs.24369/dados/ultimos/2?formato=json` | JSON | 200. sep-2026: 5,2 % (ago 5,3 %) | Mensual (trimestre móvil) | Mensual | A |
| BR | Tipo de cambio | BCB SGS 1 (dólar venta) / PTAX Olinda | `.../bcdata.sgs.1/dados/ultimos/2?formato=json` | JSON | 200. 30-oct-2026: 5,4212 BRL/USD | Diaria | Diaria o semanal | A |
| BR | Reservas internacionales | BCB SGS 13621 | `.../bcdata.sgs.13621/dados/ultimos/2?formato=json` | JSON | 200. 28-oct-2026: 364.540 M USD | Diaria | Mensual | B |
| BR | Deuda pública (% PIB) | BCB SGS 4503 y 4513 | `.../bcdata.sgs.4503/...` y `.../4513/...` | JSON | 200. sep-2026: 4503 = 61,53 %; 4513 = 69,98 %. **No he confirmado qué es cada código (deuda neta vs. bruta) [VERIFICAR]** | Mensual (~final de mes) | Mensual | B |
| BR | PIB | IBGE (Contas Nacionais Trimestrais, SIDRA 5932) | `apisidra.ibge.gov.br/values/t/5932/...` | JSON | No probado [VERIFICAR] | Trimestral | Trimestral | B |
| BR | Crédito e hipotecas / morosidad | BCB SGS (morosidad total 21082; saldo crédito ~20631/20633) y Estatísticas do SFH | `.../bcdata.sgs.21082/...` | JSON | 200. sep-2026: 4,98 % (código [VERIFICAR]); los de saldo devolvieron 747.130 y 393.432 sin confirmar unidad | Mensual | Mensual | B |
| BR | Bonos soberanos (Tesouro) | Tesouro Transparente | `tesourotransparente.gov.br` (CSV) | No probado | — | Diaria | Mensual | C |
| BR | Calificaciones | S&P, Moody's, Fitch (webs) | Moody's/Fitch bloquean (ver MAPA) | Manual | — | Eventual | Cuando haya noticia | C |
| BR | Regulación cripto | BCB (Resolução BCB 519-521 y 589) y CVM | `bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolução BCB&numero=NNN` | Solo con Chrome + `javascript_tool` (ver ACCESOS-CHROME) | Ya cubierto por W01/W03; plazo 6-nov-2026 en PLANNING | Eventual | Alerta por plazo | B |
| AR | IPC mensual | INDEC (vía datos.gob.ar, serie `148.3_INIVELNAL_DICI_M_26`) | `https://apis.datos.gob.ar/series/api/series/?ids=148.3_INIVELNAL_DICI_M_26&limit=2&sort=desc&format=json` | JSON, sin clave | 200. índice ago-2026: 12.276,77 (jul 12.076,39). Serie se queda un mes atrás | Mensual (INDEC, ~día 12-15) | Calendario INDEC: IPC oct el 12-nov; IPC nov el 15-dic (calendario 2.º semestre 2026, PDF oficial) | A |
| AR | Inflación mensual ya publicada (variación) | `api.argentinadatos.com` (TERCERO, no oficial) | `https://api.argentinadatos.com/v1/finanzas/indices/inflacion` | JSON, sin clave | 200. sep-2026: 1,9 % m/m (ago 1,7; jul 2,1) | Mensual | Usar solo como contraste de INDEC | B |
| AR | Actividad (EMAE) | INDEC vía datos.gob.ar `143.3_NO_PR_2004_A_21` | misma API | JSON | 200. jul-2026: 151,55 (jun 161,70) | Mensual | EMAE sep el 24-nov; EMAE oct el 21-dic (columna de nov-dic del PDF; alineación [VERIFICAR]) | B |
| AR | PIB y paro (EPH) trimestrales | INDEC | PDF calendario: «Informe de avance del nivel de actividad. 3.er trim.» 17-dic; «Mercado de trabajo 3.er trim.» 18-dic | Búsqueda en `apis.datos.gob.ar/series/api/search/?q=desocupacion` (los ids probados dieron «Serie inexistente», hay que buscar el vigente) | Último dato no volcado [VERIFICAR] | Trimestral | Trimestral (17-18 dic) | B |
| AR | Reservas, tipos, cambio oficial y monetarias | BCRA API v4 | `https://api.bcra.gob.ar/estadisticas/v4.0/Monetarias/1?limit=2` (1 = reservas); lista `.../Monetarias`; v3 devuelve 410 | JSON, sin clave | 200. 29-oct-2026: reservas 50.164 M USD (28-oct 50.603) | Diaria | Semanal | A |
| AR | Dólar oficial y riesgo país | argentinadatos (tercero; el oficial está en BCRA) | `.../v1/cotizaciones/dolares/oficial/2026/10/30`; `.../v1/finanzas/indices/riesgo-pais/ultimo` | JSON | 200. 30-oct-2026: oficial 1.510/1.560 ARS; riesgo país 787 pb (el índice es de JP Morgan; la API lo recopila) | Diaria | Semanal, rotulado como [S] | B |
| AR | Deuda y bonos soberanos | Ministerio de Economía (Secretaría de Finanzas) / Informe de deuda | No probado | — | — | Trimestral | Manual | C |
| AR | Regulación cripto | CNV (RG PSAV) y BCRA | cnv.gov.ar / argentina.gob.ar/normativa | No probado [VERIFICAR] | — | Eventual | Alerta por noticia | C |
| CL | Tipo oficial (TPM) | BCCh | Oficial: API `si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx` (**exige usuario y clave gratuitos**; devolvió página de error sin ellas). Mirror usado: `https://mindicador.cl/api/tpm` | JSON, sin clave (tercero) | 200. 2-nov-2026: 4,50 %. Última RPM 26-27 oct | Cada RPM | RPM 2026 restantes: 15-dic (con IPoM 16-dic). Calendario 2027 publicado por el BCCh el 30-sep-2026 [no leído, VERIFICAR] | A (con mirror) |
| CL | Dólar observado y UF | BCCh vía mindicador | `https://mindicador.cl/api/dolar`, `/api/uf` | JSON | 200. 2-nov: dólar 992,66 CLP; UF 41.258,26 | Diaria | Semanal | A |
| CL | IPC | INE Chile (ine.gob.cl) | mindicador `/api/ipc` | JSON | 200 pero **parado en dic-2025 (-0,2 %)**: no sirve. Hay que usar INE / BCCh | Mensual (día 8 aprox.) | Mensual, agenda INE 2026 publicada en dic-2025 [no leída] | C |
| CL | Imacec (actividad) | BCCh vía mindicador | `/api/imacec` | JSON | 200. sep-2026: 0,2 % (ago -1,0; jul -1,5) | Mensual (~día 1-3 tras 2 meses) | Mensual | B |
| CL | Paro, PIB, deuda, calificación, CMF/cripto | INE, BCCh, DIPRES, CMF | No probados (bcentral.cl devuelve Incapsula) | — | — | — | Manual / Banco Mundial | C |
| CO | Tipo de cambio oficial (TRM) | Superfinanciera vía datos.gov.co | `https://www.datos.gov.co/resource/32sa-8pi3.json?$limit=2&$order=vigenciadesde DESC` | JSON Socrata, sin clave | 200. 31-oct a 3-nov-2026: 3.182,99 COP/USD (30-oct 3.166,91) | Diaria | Semanal | A |
| CO | Tipo de intervención | BanRep (junta) | `banrep.gov.co/es/estadisticas/tasa-intervencion-politica-monetaria` (302); SUAMECA es una SPA | Sin API probada | Por búsqueda web (no oficial en esta lectura): 12 % desde 1-jul-2026 tras +75 pb el 30-jun; 11,25 % en abril. **[VERIFICAR]**; no encontré reuniones oct-dic | 8 decisiones/año de 12 sesiones | Calendario oficial: `banrep.gov.co/es/calendario-junta-directiva` (no leído) | C |
| CO | IPC, PIB, paro | DANE | `dane.gov.co` (carga, sin API probada); sin calendario legible en la ruta probada (404) | Manual / Banco Mundial | — | IPC día ~8-10; paro final de mes | Mensual manual | C |
| CO | Crédito, deuda, regulación cripto | Superfinanciera, MinHacienda, SFC | No probados | — | — | — | Manual | C |
| PE | Tasa de referencia | BCRP serie `PD04722MM` | `https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04722MM/json/2026-6/2026-10` | JSON, sin clave (la cabecera dice text/html pero el cuerpo es JSON) | 200. oct-2026: 4,25 % (sin cambios jun-oct) | Mensual, 2.º jueves aprox. | Sesiones 2026 conocidas: 8 ene, 12 feb, 12 mar, 9 abr, 14 may, 11 jun; segundo semestre sin confirmar (probable 2.º jueves: ~12-nov y ~10-dic) [VERIFICAR en bcrp.gob.pe]. Su página de programa monetario dio «Pardon Our Interruption» a curl | A |
| PE | IPC Lima | BCRP `PN01271PM` (var. % mensual) y `PN38705PM` (índice) | `.../PN01271PM/json/2026-6/2026-10` | JSON | 200. sep-2026: +0,117 % m/m (ago +0,067). Código `PN01288PM` está discontinuado | Mensual (INEI, día 1-2) | Mensual | A |
| PE | Tipo de cambio | BCRP `PD04637PD` (interbancario compra) | `.../PD04637PD/json/2026-10-25/2026-11-02` | JSON | 200. 30-oct-2026: 3,4617 PEN/USD | Diaria | Semanal | A |
| PE | Crédito | BCRP `PN00015MM` (crédito al sector privado en ME, M US$) | `.../PN00015MM/json/...` | JSON | 200. ago-2026: 31.393 M US$ | Mensual | Mensual | B |
| PE | PIB, paro, deuda, reservas | INEI, BCRP (series propias), MEF | Series BCRP mismo patrón; códigos no localizados | — | — | — | Manual / Banco Mundial | C |
| PE | Regulación cripto | SBS y SMV | sbs.gob.pe, smv.gob.pe | No probado | — | Eventual | Alerta por noticia | C |
| UY | IPC, tipo, PIB, deuda | BCU (bcu.gub.uy) e INE (ine.gub.uy) | Webs 200 en HTML; sin API probada | Manual | — | IPC día 1-3 | Nota breve; manual | C |
| MX | Tipo objetivo, inflación, cambio | Banxico SIE-API | `https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno` | JSON; **exige token gratuito** (error «Token inválido»); no se solicita | 400 sin token | Diaria / reuniones ~8 al año | Solo anotar; usar Banco Mundial/FMI | C |
| Todos | PIB, inflación, deuda, desempleo (anual) | Banco Mundial | `https://api.worldbank.org/v2/country/BRA;ARG;CHL;COL;PER;URY;MEX/indicator/FP.CPI.TOTL.ZG?format=json&mrnev=1&per_page=20` | JSON, sin clave | 200. Inflación: ARG 2024 219,9 %; BRA 2025 5,02 %; CHL 2025 4,21 %; actualizado 2026-10-08 | Anual (retraso 1-2 años) | Trimestral, solo respaldo | B |
| Todos | Previsiones (PIB, inflación, deuda) | FMI DataMapper | `https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH/BRA` | JSON; con UA «curl/8» devuelve 200; con UA identificado devolvió «Access Denied» (3-nov) | 200 con `curl/8`: serie con histórico y previsiones | Abril y octubre (WEO) | Semestral | B |

## Prioridad
- **Automatizar primero (A):** Brasil SGS (432, 433/13522, 24369, 1) + SIDRA 1737 + Focus; BCRA v4 (reservas y tipos) y datos.gob.ar (IPC, EMAE); BCRP (tasa, IPC, tipo de cambio); TRM de Colombia (datos.gov.co); `mindicador.cl` solo para TPM, dólar, UF e Imacec con etiqueta de tercero.
- **Después (B):** Brasil PIB, crédito, deuda, reservas, Tesouro; argentinadatos como contraste; FMI y Banco Mundial como respaldo trimestral/semestral.
- **Manual (C):** tasa de Colombia, IPC de Chile (INE), PIB y paro de Colombia/Perú/Chile, Uruguay, México, regulación cripto de CNV/CMF/SFC/SBS, calificaciones soberanas.

## Cadencia coordinada con los bancos centrales
- **Diaria/semanal:** tipos de cambio y reservas (semanal basta); Focus los lunes.
- **Por reunión:** Brasil 4-nov y 9-dic (resultado a última hora del miércoles); Chile 15-dic; Perú ~2.º jueves de mes [VERIFICAR]; Colombia sin calendario confirmado [VERIFICAR].
- **Mensual:** IPCA (~día 10); IPC Argentina 12-nov y 15-dic; IPC Perú día 1-2; EMAE (24-nov, 21-dic).
- **Trimestral:** PIB y mercado de trabajo de Argentina 17-18 dic; PIB de Brasil por IBGE; Banco Mundial.

## Huecos
- Ningún país sudamericano está aún en `paises.json`, `indicadores-manual.json` ni `estabilidad.json`.
- Sin leer: calendario IBGE 2026-27, calendario de la junta de BanRep, sesiones BCRP del 2.º semestre, calendario BCCh 2027, calendarios DANE e INE Chile.
- Discrepancia Selic (13,75 % SGS vs 14,25 % prensa) sin resolver.
- Códigos SGS de deuda, morosidad y saldo de crédito sin confirmar.
- Deuda/bonos soberanos, calificaciones y regulación cripto de AR/CL/CO/PE sin fuente probada.

## Fuentes nuevas (no estaban en MAPA-DE-FUENTES.md)
BCB SGS y Olinda (`api.bcb.gov.br`, `olinda.bcb.gov.br`); IBGE SIDRA (`apisidra.ibge.gov.br`); `apis.datos.gob.ar/series`; BCRA API v4 (`api.bcra.gob.ar/estadisticas/v4.0`); `api.argentinadatos.com` (tercero); BCRP series API; `datos.gov.co` (TRM Socrata); `mindicador.cl` (tercero); INDEC calendario PDF `indec.gob.ar/ftp/cuadros/publicaciones/calendario_2sem2026.pdf`. Candidatas sin probar: Tesouro Transparente, SUAMECA, Banxico SIE (token), BCCh SieteRestWS (usuario).

## Bloqueos
- `bcentral.cl` (Incapsula) y `bcrp.gob.pe/politica-monetaria/...` («Pardon Our Interruption»): no se saltan. `imf.org` DataMapper: «Access Denied» con User-Agent identificado, 200 con `curl/8`.
- `bcb.gov.br/en/monetarypolicy/copomdates` en Chrome: carga, pero `get_page_text` no extrae texto (una prueba hecha; pendiente leer con `javascript_tool`). Pestaña propia cerrada.
- `servicodados.ibge.gov.br/api/v3/...`: timeout. Banxico y BCCh: exigen registro (no se hizo).
- PDF del INDEC leído en scratchpad (fuera del repo); layout en dos columnas, alineación de fechas de nov-dic [VERIFICAR] contra el PDF.
