# C-espana: fuentes de datos de España para el tablero Cerebro (leído el 3-nov-2026)

## Resumen (8 líneas)
1. Probadas el 3-nov-2026 con curl/Python y User-Agent identificado: la API del INE (`servicios.ine.es/wstempus`), Eurostat, BCE, CSV del BdE, OMIE, BOE (con `Accept: application/json`) y la web de AIReF, SEPE, Seguridad Social, CNMC e IGAE responden sin clave.
2. Último dato INE: IPC general oct-2026 4,9 % anual (serie `IPC290750`, avance; sept. también 4,9 %), PIB 2T-2026 (corriente, desest.) 448.442 M€ (`CNTR6597`), población activa 3T-2026 25.443,8 miles (`EPA387794`). Eurostat: paro ES sept-2026 10,3 %; HICP ES sept 5,0 % frente a EA 3,8 %.
3. Deuda/déficit (Eurostat `gov_10dd_edpt1`, act. 21-oct-2026): deuda 2025 ES 100,5 % del PIB frente a 87,7 % EA20; saldo ES 2025 -2,4 % del PIB.
4. Calendarios oficiales localizados y leídos: INE 2026 (HTML y PDF; el de 2027 aún no está, sale en el 4T), BdE 2026-27 (iCal descargado a carpeta temporal y filtrado) y Tesoro (subastas 2026 + enero 2027).
5. Ya en el repo: Eurostat gobierno (S13), IGAE ejecución del Estado, vivienda/hipotecas manual, SEPE manual, BdE `be1101` (tipos). Faltan como serie viva: IPC/IPCA del INE, PIB, EPA, salarios, afiliación y paro registrado mensuales, deuda PDE del BdE, subastas del Tesoro, balanza de pagos, morosidad en serie, precio de la luz.
6. Las series del INE cambiaron de base en 2026 (`IPC251856` y `IPC206446` quedaron congeladas en dic-2025/2021; `IPC290750` es la viva). Antes de automatizar hay que volver a localizar cada código vivo [VERIFICAR].
7. Bloqueos: CNMV (403 a curl, Chrome sin texto en la 1.ª prueba), Seguridad Social PX-Web (500), ESIOS (token personal, no se crea cuenta), REE `apidatos` precios tiempo real (400). No se descargó ningún archivo del navegador.
8. Cadencia: diaria (OMIE luz, subastas el día de cada una), mensual (paro/afiliación 2.º día hábil, IPC ~13-15, hipotecas/compraventas INE, deuda PDE BdE, balanza de pagos), trimestral (PIB, EPA, ETCL, IPV, ERI Registradores) y anual (EES, IGAE cierre, Padrón).

## Tabla de indicadores
Repo: SI = ya está; PARC = parcial o manual; NO = falta. Prioridad: A alta, M media, B baja. [S] = secundaria (prensa/agregador). «Prueba» = lectura del 3-nov-2026.

| Indicador | Fuente oficial | URL / endpoint | Cómo se lee | Prueba (3-nov-2026) y último dato | Frecuencia y próxima publicación | Cadencia recomendada | ¿En repo? | Prior. |
|---|---|---|---|---|---|---|---|---|
| IPC general (var. anual, nacional) | INE | `https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC290750?nult=2` | API JSON, sin clave | 200. oct-2026 4,9 %; sept-2026 4,9 % (oct = avance del 30-oct) | Mensual. Definitivo oct: 13-nov; avance nov: 27-nov; definitivo nov: 15-dic; avance dic: 30-dic | Mensual: ~13-15 y último día hábil (avance) | PARC (BdE/Eurostat, no INE vivo) | A |
| IPCA (armonizado) | INE; Eurostat | Eurostat `prc_hicp_minr?geo=ES&geo=EA&coicop18=TOTAL&unit=RCH_A` (usar `minr`; `manr` congelada). INE: serie viva no localizada [VERIFICAR] | API Eurostat JSON | 200. ES sept-2026 5,0 %, EA 3,8 % (act. 16-oct-2026) | Mensual, mismas fechas que el IPC | Mensual (con IPC) | SI (Eurostat) | A |
| PIB trimestral (contabilidad) | INE CNTR | `.../DATOS_SERIE/CNTR6597?nult=2` (PIB pm, corriente, desest.) | API JSON | 200. 1T-26 440.992; 2T-26 448.442 M€. Variación t/t y a/a: calcular o localizar su serie [VERIFICAR] | Trimestral. 3T-2026: 23-dic-2026 (calendario INE) | Trimestral, el día de publicación | NO (solo contexto Eurostat) | A |
| EPA / paro (encuesta) | INE | Activos: `.../DATOS_SERIE/EPA387794?nult=2`. Tasa de paro total: código vivo no localizado [VERIFICAR] (`EPA86913` y la tabla 4247 están congeladas en 2023) | API JSON | 200. Activos 2T-26 25.274,3; 3T-26 25.443,8 miles. Tasa de paro 3T-26 ~10,18 % según prensa [S] (INE publicó el 27-oct) | Trimestral. 4T-2026: finales de ene-2027 [VERIFICAR, calendario 2027 sin publicar] | Trimestral | NO | A |
| Paro mensual armonizado | Eurostat `une_rt_m` | `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/une_rt_m?geo=ES&s_adj=SA&age=TOTAL&sex=T&unit=PC_ACT&lastTimePeriod=1` | JSON, sin clave | 200. ES sept-2026 10,3 % (act. 30-oct-2026). Con `EA20` no devolvió la zona euro [VERIFICAR código `EA`] | Mensual, ~1 mes de retraso | Mensual | NO | M |
| Paro registrado | SEPE (Mº Trabajo) | `https://www.sepe.es/HomeSepe/que-es-el-sepe/estadisticas/datos-avance.html` | HTML / Excel [VERIFICAR enlace a datos abiertos] | 200. Sept-2026: 2.379.505 (+23.587) según prensa [S]. Octubre oficial: no localizado aún | Mensual, 2.º día hábil (en nov: 3-nov) [VERIFICAR] | Mensual, 2.º-3.er día hábil | PARC (`paro_sepe` manual) | A |
| Afiliación a la Seguridad Social | Mº Inclusión y Seguridad Social | `https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/EST8` (200); PX-Web `w6.seg-social.es/PXWeb` dio 500 | HTML + XLS | Sept-2026: +92.327, 22,4 M afiliados [S]; 15-oct: 22.644.485 (nota oficial vía prensa) | Mensual, 2.º día hábil; avance a mitad de mes | Mensual (con paro registrado) | NO | A |
| Salarios y coste laboral | INE ETCL (trim.), EES (anual) | `.../DATOS_SERIE/ETCL...` (códigos nacionales por localizar; `ETCL196` es de educación) | API JSON | 200 (API). Último trimestre disponible 2T-2026. Serie nacional total no localizada [VERIFICAR] | ETCL 3T-2026: 17-dic-2026. EES: sin fecha en nov-dic [VERIFICAR] | Trimestral / anual | NO | M |
| Cifras de población | INE ECP | INEbase «Estadística Continua de Población» | API INE | Dato no leído | 12-nov-2026 (ref. 1-oct-2026); Padrón: «depende del BOE» | Trimestral | PARC (`poblacion_referencia`) | M |
| Deuda AAPP (PDE) | Banco de España | CSV `https://www.bde.es/webbe/es/estadisticas/compartido/datos/csv/be1101.csv` (200, 17 KB) y calendario iCal | CSV BdE (códigos `DTNPDE2010_...`, `DTNSEC2010_...`) | CSV 200; valor de deuda no extraído (hacerlo al automatizar) | Mensual. Información temprana 17-nov y 18-dic; PDE AAPP 15-dic; Estado 30-nov y 30-dic | Mensual, ~15-18 | PARC (Eurostat anual) | A |
| Deuda y déficit anual comparados | Eurostat `gov_10dd_edpt1` | `.../data/gov_10dd_edpt1?geo=ES&geo=EA20&sector=S13&na_item=GD&unit=PC_GDP&lastTimePeriod=1` (y `na_item=B9`) | JSON | 200. Deuda 2025 ES 100,5 %, EA20 87,7 %; saldo ES 2025 -2,4 % del PIB (act. 21-oct-2026) | Semestral (abril y octubre) | Semestral | SI | A |
| Ejecución presupuestaria del Estado | IGAE | `https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Paginas/EjecucionPresupuestaria.aspx` | PDF mensual (`MENSUAL 12-25.pdf`) | 200 la página. Repo: dic-2025 y ago-2026 | Mensual, final del mes siguiente [VERIFICAR] | Mensual | SI (C65-C69) | M |
| Subastas del Tesoro | Tesoro Público | `https://www.tesoro.es/en/deuda-publica/subastas/calendario`; PDF `https://www.tesoro.es/documents/d/tesoro/calendario-tesoro-publico-2026-ingles-12`; resultados `.../subastas/resultado-ultimas-subastas/letras-del-tesoro` | HTML (fechas en formato MM.DD.AAAA) | 200. Nov-2026: Letras 6 y 12 m el 3-nov; 3 y 9 m el 10-nov; Bonos/Obl. 5 y 19-nov. Dic: Letras 1 y 9-dic; Bonos/Obl. 10 y 17-dic. Ene-2027: Letras 12 y 19; Bonos 7 y 21 | Calendario anual fijo | Los días de subasta; resto, semanal | NO | A |
| Rendimiento del bono 10 a / prima de riesgo | BCE / BdE / Tesoro | BCE `data-api.ecb.europa.eu/service/data/...` [VERIFICAR flujo y clave del 10 años de España] | SDMX CSV | API del BCE 200 (probado con el tipo MRR). Serie de España no probada | Diaria (mercado), mensual (BCE) | Semanal | PARC (`bonos-manual.json`) | A |
| Balanza de pagos | Banco de España | iCal del BdE | CSV / PDF | Avance de agosto-2026 publicado el 30-oct: capacidad de financiación 3,7 % del PIB [S: web/nota BdE vía búsqueda] | Mensual: 30-nov (sept), 29 y 30-dic (oct), 29-ene-2027; trimestral + posición de inversión 23-dic | Mensual, final de mes | NO (`exterior` es AOD) | M |
| Precios de vivienda (IPV) | INE | `.../DATOS_SERIE/IPV...` (serie viva por localizar; `IPV948` y `IPV769` llegan a 3T-2025) | API JSON | Repo: IPV 2T-2026 | Trimestral. 3T-2026: 4-dic-2026 | Trimestral | SI (manual) | A |
| Compraventas e hipotecas | INE ETDP e Hipotecas | INEbase; CSV de tabla `https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/<id>.csv` (probado con la 50902: 200) | API / CSV | Repo: ago-2026 | ETDP sept 17-nov, oct 16-dic; Hipotecas sept 25-nov, oct 18-dic | Mensual | SI (manual) | A |
| Registradores (ERI) | Colegio de Registradores | `https://www.registradores.org/documents/d/guest/eri_2t_2026` (PDF 9,3 MB, 200; no descargado) | PDF trimestral + notas mensuales | 2T-2026: 167.934 compraventas de vivienda (-5,7 % t/t), 129.240 hipotecas (-3,3 %), precio +2,4 % t/t [S: prensa/web]. Ago-2026: 48.674 operaciones (+1,3 % a/a) | Trimestral (3T ~nov, sin fecha confirmada [VERIFICAR]) y mensual | Trimestral + mensual | NO | M |
| Notarios | Consejo General del Notariado | `notariado.org/portal/...` (3 URLs probadas, todas 404) | Por localizar | 404 [VERIFICAR] | Mensual | Mensual | NO | B |
| Crédito, morosidad y banca | Banco de España | Estadísticas supervisoras de entidades de crédito | CSV / PDF | Repo: morosidad may-2026. Próximas: mensual 24-nov y 28-dic; trimestral 28-dic; 8-ene-2027 | Mensual | Mensual | PARC (manual, desfasado) | A |
| Tipos bancarios y Euríbor | Banco de España | `be1101.csv` y otras tablas | CSV | Euríbor 12 m oct-2026 en el repo | Euríbor/€STR 3-nov y 1-dic; tipos IFM 2-dic; tipos legales hipotecarios 18-nov, 17-dic, 19-ene | Mensual (principio de mes) | SI | A |
| Pensiones | Seguridad Social | Nota de prensa mensual + eSTADISS (revista.seg-social.es) | HTML / XLS | Oct-2026: 10.565.782 pensiones (+1,6 %), nómina 14.539,9 M€ (+6,3 %), media 1.376,14 €/mes (+4,6 %), jubilación media 1.577,6 € [S: nota del 27-oct vía prensa] | Mensual (~27) | Mensual | PARC (`beneficiarios`) | M |
| Previsiones fiscales | AIReF | `https://www.airef.es/es/` (200) | HTML / PDF | 17-sept-2026: déficit 2026 previsto 2,7 % del PIB, deuda en torno al 100 % [S: prensa]; en julio 99,3 % | Informes puntuales | Con cada informe | NO | M |
| Hechos relevantes, ETF y fondos | CNMV | `https://www.cnmv.es/portal/HR/HechosRelevantes.aspx` | HTML dinámico | curl 403; Chrome cargó la página pero sin texto (1 intento) | Continua | Consulta puntual, no automatizar | NO | B |
| Energía y precio de la luz | OMIE / REE / CNMC | OMIE `https://www.omie.es/es/file-download?parents=marginalpdbc&filename=marginalpdbc_AAAAMMDD.1`; REE `apidatos.ree.es/es/datos/demanda/evolucion?start_date=...&end_date=...&time_trunc=day`; CNMC (web 200) | OMIE: CSV con `;`, sin clave. REE: JSON sin clave | OMIE 2-nov-2026: horas 1-8 entre 230 y 251 (unidad €/MWh a verificar). REE demanda 200 (last-update 8-oct). REE precios tiempo real: 400 | Diaria (OMIE ~13:00 para el día siguiente) | Diaria (media diaria) | NO | M |
| BOE (normas) | AEBOE | `https://www.boe.es/datosabiertos/api/boe/sumario/AAAAMMDD` con `Accept: application/json` | API JSON | 20261102 OK; 20261103 aún 404; sin cabecera da 400 | Diaria | Diaria si hay temas vigilados | SI | B |

## Calendarios oficiales (resumen utilizable)
- INE 2026: `https://www.ine.es/dynt3/Calendario/calenHTML.htm` y PDF `https://www.ine.es/daco/daco41/calendario-coyunturales-2026-A1.pdf`. Próximas: IPC 13-nov, 27-nov, 15-dic, 30-dic; ETDP 17-nov y 16-dic; Hipotecas 25-nov y 18-dic; ECP 12-nov; IPV 3T 4-dic; ETCL 3T 17-dic; PIB 3T 23-dic. El calendario 2027 no estaba publicado (sale en el último trimestre del año).
- Banco de España: iCal `https://www.bde.es/webbe/en/estadisticas/compartido/calendario/ics/calendario-bde.ics` (2026-27, 734 eventos, leído y filtrado). PDF 2027 `.../pdf/calendario-bde-2027e.pdf`. Próximas: deuda PDE información temprana 17-nov, 18-dic, 19-ene, 17-feb; PDE AAPP 15-dic y 31-mar; balanza 30-nov, 23-dic (trimestral), 29 y 30-dic, 29-ene, 26-feb; supervisoras 24-nov, 28-dic, 22-ene, 23-feb; tipos hipotecarios 18-nov, 17-dic, 19-ene, 17-feb; FASE 11-ene; EFF 2024 microdatos 29-ene-2027.
- Tesoro: calendario 2026 en la web; Letras los martes (6 y 12 m la primera semana, 3 y 9 m la segunda), Bonos y Obligaciones los jueves.
- SEPE y Seguridad Social: sin calendario publicado en las páginas leídas; regla observada: 2.º día hábil del mes [VERIFICAR].

## Propuesta de cadencia
- Diaria: OMIE (media diaria de luz); subastas del Tesoro solo los días de subasta.
- Semanal (lunes): rendimientos soberanos (BCE/Eurostat) y repaso del calendario de la semana.
- Mensual: días 2-3 (paro registrado, afiliación, Euríbor BdE), ~13-15 (IPC/IPCA), ~17-25 (compraventas e hipotecas INE; deuda PDE BdE), ~24 (supervisoras), 27-30 (avance IPC, balanza de pagos, pensiones).
- Trimestral: PIB, EPA (27-oct hecha; próxima finales de ene-2027), ETCL, IPV (4-dic), ERI Registradores.
- Anual: EES, Padrón, cierre IGAE, deuda/déficit anual de Eurostat (abril y octubre).

## Huecos (lo que falta en el repo)
1. Serie viva del IPC/IPCA del INE (el repo usa Eurostat y BdE); localizar códigos de la base 2025.
2. PIB: variación t/t y a/a; tasa de paro EPA (código vivo).
3. Afiliación y paro registrado mensuales como serie (hoy manual y puntual).
4. Deuda PDE mensual y balanza de pagos del BdE; morosidad desfasada (may-2026).
5. Subastas del Tesoro (calendario y resultados) y prima de riesgo.
6. Salarios (ETCL nacional, EES) y precio de la luz.
7. Registradores y Notarios como contraste del INE en vivienda.

## Fuentes nuevas (no estaban en MAPA-DE-FUENTES.md)
- INE calendario HTML y PDF 2026; INE CSV por tabla (`jaxiT3/files/t/es/csv_bdsc/<id>.csv`).
- BdE iCal de calendario (2026-27).
- Tesoro Público: calendario y resultados de subastas.
- OMIE (`file-download`, CSV sin clave) y REE `apidatos.ree.es` (demanda, sin clave).
- SEPE `datos-avance`; Seguridad Social EST8 (afiliación) y `revista.seg-social.es` (nota mensual de pensiones).
- Registradores ERI (PDF y notas); AIReF (informes).
- BOE datos abiertos con `Accept: application/json` (ya figuraba, pero sin esta precisión).
- Eurostat `une_rt_m` y `gov_10dd_edpt1` (Eurostat ya figuraba; estos conjuntos concretos no).

## Bloqueos y avisos
- CNMV: curl 403 en `Consultas/HechosRelevantes.aspx`; Chrome (1 prueba, pestaña propia cerrada) no devolvió texto. No se insistió. `cnmv.es` sin www devuelve WML sin contenido útil.
- Seguridad Social PX-Web: 500. MIVAU: 403 a curl y 404 en Chrome con la URL probada (URL equivocada, no bloqueo); buscar la página correcta [VERIFICAR]. Notarios: 404. Hacienda (calendario y estadísticas): 404 en las URLs probadas.
- ESIOS (REE) pide token personal: no se crea cuenta. REE `precios-mercados-tiempo-real` dio 400.
- Descargas: el PDF de Registradores (9,3 MB) y los PDF de calendario de INE y Tesoro requieren OK de descarga si se quieren guardar. No se descargó nada al repo; el iCal del BdE (614 KB) quedó solo en la carpeta temporal.
- Los datos [S] proceden de prensa o notas reenviadas, no de la tabla oficial. Sin recomendaciones de compra o venta.
