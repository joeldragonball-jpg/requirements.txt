# C74 · Materias primas y crédito bancario: qué se publica y qué automatizar (2-nov-2026)

Etiquetas: [P] organismo oficial, abierto hoy desde `curl` · [S] agregador/no oficial · [VERIFICAR] no comprobado · [ESPECULACIÓN] opinión. Sin recomendaciones de compra/venta. Parte de C71 (BCE: euríbor, TAE, crédito) y C72 (Freddie Mac, Banco de Inglaterra, `informes/research/2026-11-02-C72-credito.md`). Pruebas del 2-nov-2026 con `curl` y cabecera de navegador normal; ninguna fuente bloqueó por ser un script, salvo el FMI (403).

## 1. Crédito bancario: fuentes

### 1.1 BCE · Bank Lending Survey (BLS) [P]
- **Mide:** % neto de bancos del euro que endurecen (+) o relajan (−) criterios de concesión, condiciones y demanda de crédito (empresas, hogares vivienda, consumo), pasado (B3) y esperado (F3).
- **Periodicidad:** trimestral (enero, abril, julio, octubre). Última ronda: encuesta 21-sep a 6-oct-2026, publicada el **27-oct-2026** (fecha según la nota del Banco de España).
- **Acceso:** API SDMX abierta, sin clave: `https://data-api.ecb.europa.eu/service/data/BLS/<clave>?lastNObservations=6&format=csvdata`. Probado: 200 con y sin User-Agent. Diccionario de claves: `https://data-api.ecb.europa.eu/service/datastructure/ECB/ECB_BLS1?references=children`.
- **Clave útil:** `Q.U2.ALL.O.E.Z.B3.ST.S.WFNET` (zona euro, criterios globales a empresas, últimos 3 meses, % neto ponderado). Para la expectativa, `B3` pasa a `F3`. Código `O` = "Overall", `E` = empresas, `H` = hogares (según el diccionario); la combinación exacta para hogares (`O.H.H`) no devolvió serie: [VERIFICAR] antes de rotular.
- **Último dato (HECHO, API del BCE, 2-nov-2026), criterios a empresas, % neto que endurece:** 3T-2025 −1,4 · 4T-2025 +4,2 · 1T-2026 +6,6 · 2T-2026 +10,1 · 3T-2026 +7,3 · ronda de oct-2026 (etiquetada 2026-Q4) **+8,6**, con expectativa a 3 meses +7,2. Cuatro rondas seguidas con endurecimiento neto por encima de +4.
- **Límite:** la misma clave con país `ES` no devolvió datos; el detalle de España va por otro código o por la nota del Banco de España.

### 1.2 Fed · Senior Loan Officer Opinion Survey (SLOOS) [P]
- **Mide:** lo mismo para EE. UU. (C&I, inmobiliario comercial, hipotecas, tarjetas, auto, consumo): % neto que endurece y demanda.
- **Periodicidad:** trimestral (ene/feb, abr/may, jul/ago, oct/nov). Última: **encuesta de octubre 2026** (referida al 3T-2026); la página figura actualizada el **2-nov-2026**.
- **Acceso:** `https://www.federalreserve.gov/data/sloos.htm` (200); informe por ronda `.../data/sloos/sloos-202610.htm` (200); datos completos en ZIP SDMX/XML `https://www.federalreserve.gov/datadownload/Output.aspx?rel=SLOOS&filetype=zip` (200, 245 KB, contiene `SLOOS_data.xml`). Sin clave. FRED (`fredgraph.csv`) no respondió.
- **Riesgo:** la Fed avisa de que el Data Download Program (DDP) tiene retirada eventual y que la función "Build Your Package" desaparece la semana del 9-nov-2026. El ZIP puede cambiar de URL o dejar de existir: [VERIFICAR] la alternativa antes de automatizar.
- **Lectura del último informe (HECHOS, texto oficial):** estándares de C&I a empresas grandes y medianas "básicamente sin cambios", más estrictos para pymes; endurecimiento neto en todas las categorías de inmobiliario comercial con demanda más débil; hipotecas residenciales mayormente sin cambios (relajación en jumbo, endurecimiento en subprime) y demanda más débil; consumo sin cambios salvo ajustes puntuales; demanda de C&I más débil.
- **Fed H.8** (crédito bancario semanal): `https://www.federalreserve.gov/releases/h8/current/default.htm` abre (200) y la tabla HTML trae préstamos y arrendamientos (total ≈ 14,1 billones $ en las últimas semanas mostradas; [VERIFICAR] semana y columna antes de citar). Pendiente de C72.

### 1.3 EBA (Autoridad Bancaria Europea) · Risk Dashboard [P]
- **Mide:** ~30 indicadores de riesgo de bancos de la UE (CET1, ratio de morosidad NPL, cobertura, fase 2 de IFRS 9, rentabilidad, liquidez LCR, financiación). Son datos de supervisión, no encuesta.
- **Periodicidad:** trimestral, con ~2,5 meses de retraso. Último publicado: **2T-2026** (PDF en `/sites/default/files/2026-09/...`). Próximo: **18-dic-2026** (3T-2026), según la propia página.
- **Acceso:** `https://www.eba.europa.eu/risk-and-data-analysis/risk-analysis/risk-monitoring/risk-dashboard` (200). Ficheros: "Data Annex InteractiveRiskDashboard Q2 2026.xlsx" y "Credit Risk parameters annex - Q2 2026.xlsx". Descarga directa del xlsx probada (Q4-2025: 200, 6,5 MB, con y sin UA). Las rutas llevan un identificador aleatorio: hay que extraer el enlace de la página, no se puede deducir.
- **Cifras:** no pude extraer el NPL ratio del PDF (la tabla sale ilegible en texto); [VERIFICAR] con el xlsx del anexo. No cito cifras de la EBA aquí.
- **Transparencia (EU-wide Transparency Exercise):** enlace `.../risk-analysis/eu-wide-transparency-exercise`; datos por banco, anual. No abrí el detalle: [VERIFICAR] fecha 2026 y formato. Valor para largo plazo: bajo-medio (microdatos de bancos concretos).

### 1.4 Banco de España · encuesta y estadísticas de crédito [P]
- **Encuesta sobre Préstamos Bancarios (EPB):** versión española del BLS. Última: nota de prensa **27-oct-2026** (`https://www.bde.es/f/webbe/GAP/Secciones/SalaPrensa/NotasInformativas/26/presbe2026-101.pdf`, 200). **HECHOS del texto oficial:** criterios de concesión estables en 3T-2026 (empresas y vivienda), endurecimiento leve en consumo; las **condiciones** de los nuevos préstamos más restrictivas por la subida de tipos, sin tocar márgenes; demanda a la baja en los tres segmentos, más en vivienda; para 4T-2026 los bancos esperan endurecer moderadamente en hogares y menor demanda; la IA, según los bancos, sin impacto significativo hasta ahora. Próxima: **2-feb-2027** (según la nota). Sin CSV propio: la serie numérica por país hay que buscarla en el BCE [VERIFICAR].
- **Estadísticas de crédito (Boletín Estadístico, tablas BE 4.x):** CSV público por tabla en `https://www.bde.es/webbe/es/estadisticas/compartido/datos/csv/beNNNN.csv` (200, sin clave, sin UA). Probado: `be0412`/`be0413` (crédito de entidades a otros sectores residentes por finalidades; último dato **jun-2026**) y `be0430` (crédito a AAPP y otros sectores residentes, total nacional; jun-2026). Codificación Latin-1, 4 filas de cabecera (código, número secuencial, alias, descripción). Unidades a confirmar (probablemente miles de euros) [VERIFICAR]. Ojo: `be1801` es comercio exterior, NO crédito. Tabla de morosidad no localizada: [VERIFICAR] (el texto "dudosos" aparece en `be0401`, `be0413` y `be0414`).
- Varias rutas antiguas `/wbe/es/estadisticas/...` devuelven 404 (la web cambió): usar los CSV directos.
- **Bloqueo:** ninguno detectado.

## 2. Materias primas: qué se publica frente a lo que ya usan los paneles

**Ya en los paneles (C71, `leer_materias()`):** futuros continuos de Yahoo Finance [S], no oficial: oro, plata, cobre, gas natural Henry Hub, trigo, maíz, café; cambio de 1 día y ~1 mes. Brent/WTI salen en los cierres diarios por esa vía. Yahoo respondió hoy (oro 3.950,5 $, 200). Limitaciones: no oficial, sin garantía de continuidad y el cambio de contrato del futuro continuo mete ruido en el cambio de un día.

**Alternativas oficiales abiertas, sin clave (probadas hoy):**

| Fuente | Qué da | Periodicidad / último dato | Acceso |
|---|---|---|---|
| EIA, Brent spot | Dated Brent diario [P] | Semana 26-30 oct: 128,12 y 123,10 $/barril (lun-mar); publicado 28-oct, próximo 4-nov | `https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls` (200); HTML `.../pet/hist/RBRTED.htm` |
| EIA, gas Henry Hub spot | diario [P] | Semana 26-30 oct: 2,52 y 2,76 $/MMBtu | `https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls` (200) |
| Banco Mundial, Pink Sheet | precios mensuales de ~70 materias (Brent, oro, plata, cobre LME, gas, trigo, maíz, café) [P] | mensual; hasta **sep-2026** (2026M09) | `https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Historical-Data-Monthly.xlsx` (200). El hash cambia cada año: extraerlo de `https://www.worldbank.org/en/research/commodity-markets` |
| CFTC, Commitments of Traders | posicionamiento en futuros [P] | semanal; último fichero con fecha **27-oct-2026** | `https://www.cftc.gov/dea/newcot/f_disagg.txt` (200, CSV sin cabecera, ~460 KB) |
| USDA WASDE | oferta/demanda agrícola [P] | mensual | `https://www.usda.gov/oce/commodity/wasde/` (200; formato sin probar) |
| FMI, precios de materias | serie mensual [P] | — | `imf.org/en/Research/commodity-prices` devuelve **403** (bloquea bots) |
| LBMA | fijaciones oro/plata | diario | la página abre (200); la licencia de uso de datos [VERIFICAR] |

**Hecho que obliga a prudencia:** el Brent al contado de la EIA (123–128 $ el 26-27 oct) y el Brent de futuros de los cierres del repo (111–112 $ el 29-30 oct) difieren en unos 10–15 $. Puede deberse a contrato, fecha o prima de entrega inmediata; no es un error probado [VERIFICAR contrato y fecha antes de compararlos]. Rotular siempre "spot" o "futuro" y no restar series distintas.

## 3. Ciclo de crédito: lectura alcista frente a bajista

**HECHOS (arriba):** criterios de crédito a empresas de la eurozona endurecidos en las últimas cuatro rondas del BCE y +8,6 % neto en la última; España: condiciones más duras por tipos y demanda a la baja, sobre todo vivienda; EE. UU.: pymes y comercial inmobiliario más duros, hipoteca a 30 años en 7,24 % (C72); Reino Unido: aprobaciones −19 % en un año (C72).

- **Lectura bajista:** crédito más caro y escaso frena inversión y vivienda; el endurecimiento es sostenido y en España se espera más en hogares; el inmobiliario comercial de EE. UU. aparece débil en todas las categorías; los bancos trasladan el coste de financiación al cliente (presión sobre el prestatario).
- **Lectura alcista:** un +8,6 % neto es moderado frente a episodios de crisis (el máximo histórico de la serie no se consultó aquí [VERIFICAR]); la SLOOS describe estándares "básicamente sin cambios" para grandes empresas e hipotecas, con relajación en jumbo; los bancos pueden estar trasladando costes sin tocar márgenes (BdE), lo que protege su rentabilidad; la demanda débil con estándares estables puede ser un ajuste de precio y no una restricción de oferta; solvencia de la banca europea según la EBA [VERIFICAR cifra].
- **Sesgos de lectura:** las encuestas miden opinión de bancos, no volumen concedido; el % neto no es intensidad; el BLS pondera por tamaño y la SLOOS no; los datos de crédito (BdE, jun-2026) llevan meses de retraso respecto a las encuestas (oct-2026).
- **[ESPECULACIÓN]:** si el ciclo termina en "tipos altos persistentes" o en "aterrizaje suave" no se deduce de estas fuentes; es una opinión que cada uno debe formular, no un dato.

## 4. Qué automatizar

| Fuente | Indicador | Método de descarga | Esfuerzo | Valor para decidir | Prioridad |
|---|---|---|---|---|---|
| BCE BLS | % neto criterios y demanda (empresas, vivienda, consumo), B3 y F3, zona euro | API SDMX `csvdata` con pocas claves (mismo cliente que C71) | Bajo | Alto: indicador adelantado trimestral, abierto y estable | **1** |
| Freddie Mac / BoE (C72) | hipoteca 30 a EE. UU., 2 a RU | ya en el panel | Hecho | Alto | — |
| Fed SLOOS | % neto C&I, CRE, hipoteca, consumo, demanda | ZIP SDMX del DDP, o tablas HTML por ronda | Medio (XML; riesgo por retirada del DDP) | Alto para EE. UU. (trimestral) | **2** (tras confirmar alternativa al DDP) |
| EIA | Brent y gas Henry Hub spot diarios | XLS `hist_xls` (hace falta lector xls) o tabla HTML | Bajo-medio | Medio-alto: serie oficial para contrastar con Yahoo | **2** |
| Banco de España BE 4.x | crédito a hogares/empresas, saldo y variación | CSV directo `beNNNN.csv` (Latin-1) | Bajo (elegir bien la tabla) | Medio-alto para España (enlaza con C73) | **2** |
| Banco Mundial Pink Sheet | precios mensuales de las 7 materias del panel | XLSX, enlace extraído de la página | Medio (sin librería xlsx aquí: zip+XML) | Medio: referencia oficial mensual | 3 |
| BdE EPB | nota trimestral | PDF; enlace manual o BLS `ES` | Bajo | Medio | 3 |
| EBA Risk Dashboard | CET1, NPL, cobertura, fase 2 | xlsx del anexo (raspar la página por el id) | Medio-alto | Medio (trimestral, retraso largo) | 3 |
| CFTC COT | posicionamiento en oro, petróleo, trigo | TXT/CSV semanal | Medio (130+ columnas) | Medio (sentimiento; interpretación = opinión) | 3 |
| EBA Transparency | datos por banco | CSV grande anual | Alto | Bajo | 4 |
| FMI precios | — | bloqueado (403) | — | — | descartada; usar Banco Mundial |

Reglas al automatizar: conservar la serie anterior si falla (como en C72); rotular [P] o [S]; no mezclar spot y futuro.

## 5. Pendiente
- Confirmar códigos BLS para hogares y país (`ES`) y qué tabla BE contiene la morosidad.
- Descargar el xlsx de la EBA (2T-2026) y leer CET1 y NPL; citarlos con fecha.
- Vigilar el anuncio de la Fed sobre la retirada del DDP (semana del 9-nov).
- Resolver la diferencia Brent spot (EIA) frente a futuro (Yahoo) antes de usar ambos en un panel.

Fuentes (consultadas el 2-nov-2026): API del BCE `data-api.ecb.europa.eu`; nota de prensa del Banco de España de 27-oct-2026; Fed (`federalreserve.gov/data/sloos`, `/releases/h8`); EBA Risk Dashboard; EIA (`eia.gov/dnav`); Banco Mundial (Commodity Markets); CFTC.
