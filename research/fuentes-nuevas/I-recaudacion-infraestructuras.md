# I · Recaudación récord frente a infraestructuras: qué dicen los datos (3-nov-2026)

Sin API de Anthropic. Sin recomendaciones de compra/venta. Marcas: [P] leído en el original oficial; [S] secundaria o prensa; [VERIFICAR] no contrastado; [OPINIÓN]/[ESPECULACIÓN] lo que no es dato. Los PDF se leyeron en la carpeta temporal (no se guardó nada en el repo). Reutiliza `explorador/espana.json` (Eurostat) y `informes/research/2026-10-30-C65-espana-ingresos-gasto.md`.

Pregunta: «¿recaudación récord pero infraestructuras peores?». Se parte de los datos, no de la respuesta.

## 1. Recaudación (AEAT) [P]

Base: ingresos tributarios netos, **criterio de caja**, incluida la parte que se cede a CCAA y entes locales. No es lo mismo que los «impuestos» de Eurostat (devengo) ni incluye cotizaciones.

### 1.1 Acumulado enero-septiembre 2026 (M€)
Fuente: AEAT, Informe mensual de recaudación, septiembre 2026 (Cuadro R1, págs. I-4/I-5): https://sede.agenciatributaria.gob.es/static_files/AEAT/Estudios/Estadisticas/Informes_Estadisticos/Informes_mensuales_recaudacion_tributaria/2026/IMR_26_09_es_es.pdf (leído 3-nov-2026).

| Concepto | Ene-sep 2026 | Ene-sep 2025 | Var. | Var. homogénea* |
|---|---|---|---|---|
| IRPF | 118.068 | 104.957 | +12,5 % | +11,8 % |
| Impuesto sobre Sociedades | 18.877 | 15.004 | +25,8 % | +7,0 % |
| IVA (neto) | 81.181 | 75.090 | +8,1 % | +7,4 % |
| Impuestos Especiales | 15.718 | 17.172 | −8,5 % | −8,3 % |
| **Total ingresos tributarios** | **248.326** | **225.747** | **+10,0 %** | **+8,0 %** |
Septiembre solo: 18.049 M€ (+13,5 %).
*Homogéneo = AEAT quita cambios normativos y devoluciones/ingresos extraordinarios.

- HECHO: el total acumulado de 2026 supera en 22.579 M€ al de 2025 (mismo periodo, euros corrientes). Brutos +7,6 %, devoluciones −1,9 %.
- HECHO (matiz importante): una parte del salto de Sociedades (+25,8 % frente a +7,0 % homogéneo) y del total viene de devoluciones muy altas en 2025 por sentencias (mutualistas, RDL 3/2016) que no se repiten: el propio informe cifra ese efecto en 1.122 M€ (pág. I-2).
- HECHO: los cambios normativos y de gestión **restan** 3.983 M€ hasta septiembre de 2026 (−1,8 puntos), sobre todo por las rebajas de IVA, hidrocarburos y electricidad y la suspensión del impuesto a la producción eléctrica por el conflicto de Oriente Medio (Cuadro 0, pág. I-2).
- HECHO: retenciones del trabajo +9,8 % (empleo, masa salarial y «subida del tipo efectivo»); IVA bruto +7,0 %.
- Distribución territorial: **no usar el reparto por delegaciones como mapa de recaudación por CCAA**. La AEAT avisa de que casi la mitad de los ingresos figura en la Delegación de Madrid por el domicilio fiscal de grandes empresas y retenedores (nota 8, pág. IV-7), y el País Vasco y Navarra recaudan por régimen foral (con ajustes aparte). La recaudación por CCAA en sentido económico no es un dato publicado así: [VERIFICAR] fuentes de «balanzas fiscales» y financiación autonómica (Hacienda/IGAE) antes de comparar territorios.

### 1.2 Cierres anuales (M€, AEAT, Cuadro R1 de los informes de diciembre)
Fuentes: IMR_25_12 y IMR_24_12 (misma ruta que arriba, carpetas 2025 y 2024) [P]; informe anual 2025 (23-abr-2026): https://sede.agenciatributaria.gob.es/Sede/estadisticas/recaudacion-tributaria/informe-anual/ejercicio-2025/resumen.html

| | 2023 | 2024 | 2025 | Var. 2025 |
|---|---|---|---|---|
| IRPF | 120.280 | 129.408 | **142.466** | +10,1 % |
| Sociedades | — | 39.096 | **42.266** | +8,1 % |
| IVA (neto) | 83.909 | 90.541 | **99.532** | +9,9 % |
| Impuestos Especiales | — | 22.128 | **23.083** | +4,3 % |
| **Total** | **271.935** | **294.734** | **325.356** | **+10,4 %** |
(Columna 2023 de IMR_24_12; Sociedades y Especiales 2023 no se extrajeron.)

- HECHO: en 2025, 7.820 M€ (2,7 puntos) del aumento vienen de medidas normativas y de gestión; la base imponible creció ~7 %. La propia AEAT dice que la base consolidada de Sociedades marca máximo histórico y que el impuesto devengado supera por primera vez el máximo de 2006.
- Serie 2019-2022 (totales AEAT): 2019 = 212.808 M€ (cifra que aparece en IMR_20_12; coherente con 194.051 = −8,8 %); 2020 = 194.051; 2022 = 255.463 (IMR_22_12); 2021 ≈ 223.300 (derivado de +14,4 % en 2022; [VERIFICAR] el dato exacto). [P] salvo 2021.
- **¿Récord?** En euros corrientes, sí: 325.356 M€ es la cifra más alta de las series que he leído (todas las anteriores 2019-2024 son menores) y 2026 acumulado va +10 %. [VERIFICAR] «récord histórico» absoluto frente a 2007 con la serie de 1995 que publica la AEAT (no descargada).
- **Ajustado:** con el deflactor del PIB de `espana.json` (2019 = 104,3; 2025 = 127,8) la recaudación de 2025 equivale a ~265.600 M€ de 2019: **+25 % real** frente a 2019 (cálculo propio). Como % del PIB (cálculo propio, PIB de `espana.json`): 17,0 % (2019) → 18,4 % (2024) → **19,3 % (2025)**. Es decir, sube más que el PIB, no solo por inflación.
- Cotizaciones sociales aparte (Eurostat, `espana.json`): 160.656 M€ (2019) → 223.230 M€ (2025), estables en ~13 % del PIB.

## 2. Inversión pública y mantenimiento

### 2.1 Macro (Eurostat gov_10a_main, S13, España; actualizado 21-oct-2026) [P]
URL: https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main (consulta API 3-nov-2026). % PIB con el PIB de `espana.json`.

| Año | FBCF AAPP (M€) | % PIB | Consumo capital fijo (M€) | % PIB | Inversión − depreciación (M€) |
|---|---|---|---|---|---|
| 2010 | 50.959 | ~4,7 [VERIFICAR PIB 2010] | 26.664 | — | +24.295 |
| 2012 | 32.549 | 3,1 | 28.480 | 2,75 | +4.069 |
| 2014 | 22.079 | 2,1 | 27.795 | 2,7 | −5.716 |
| 2016 | 22.199 | 2,0 | 27.412 | 2,4 | −5.213 |
| 2018 | 25.889 | 2,1 | 28.299 | 2,3 | −2.410 |
| 2019 | 27.206 | 2,2 | 28.850 | 2,3 | −1.644 |
| 2020 | 29.694 | 2,6 | 29.191 | 2,6 | +503 |
| 2021 | 33.591 | 2,7 | 30.919 | 2,5 | +2.672 |
| 2022 | 37.350 | 2,7 | 34.076 | 2,5 | +3.274 |
| 2023 | 44.696 | 3,0 | 35.529 | 2,4 | +9.167 |
| 2024 | 43.253 | 2,7 | 37.729 | 2,4 | +5.524 |
| 2025 | 50.628 | 3,0 | 39.764 | 2,35 | +10.864 |
Otros años de la serie 2010-2025 en el mismo conjunto: 2011 40.001 / 27.936; 2013 24.651 / 28.218; 2015 28.002 / 27.552; 2017 23.118 / 27.683.

- HECHO: la inversión bruta cayó de 50.959 (2010) a 22.079 M€ (2014), con 2013-2018 por debajo de la depreciación contable; supera la depreciación desde 2020, y en 2023 y 2025 por amplio margen (años de fondos europeos MRR [VERIFICAR el efecto concreto]). Suma 2019-2025 de inversión neta: ~+30.360 M€.
- HECHO (SEOPAN, patronal, prensa del 24-abr-2026): su serie de FBCF da 2,7 % del PIB en 2024 frente a 5,2 % en 2009 («en 2024 se invierte el 52 % respecto a 2009»); y que transporte, agua y residuales bajaron del 3,9 % al 1,7 % del gasto público (2008-2024). [S: emisor interesado]
- Aviso: **consumo de capital fijo ≠ mantenimiento**. Es depreciación estimada; el mantenimiento real (reparaciones, conservación) está en consumos intermedios y no se separa aquí. La FBCF incluye hospitales, colegios y cuarteles, no solo carreteras y trenes.

### 2.2 Stock de capital público (Fundación BBVA-Ivie, DT 1/2024, serie 1995-2023) [P]
https://www.fbbva.es/wp-content/uploads/2024/02/DE_2024_DT_1_2024_Stock_Ivie.pdf (leído 3-nov-2026; es un trabajo académico, no un organismo de la patronal).
- HECHO: el capital neto público empezó a caer en 2013 (−1,2 %), siguió en negativo hasta 2019 y volvió a crecer desde 2020 con los fondos europeos; el resultado fue **una reducción del 3,7 % del capital público acumulado entre 2011 y 2023**, «aunque en los tres últimos años ya vuelve a crecer».
- HECHO: la inversión pública en 2023 seguía un **45 % por debajo de la de 2009** (en términos reales según el texto) y la caída 2010-2014 la dejó en poco más de un tercio del nivel de 2009.
- HECHO: la inversión pública se usó como «variable de ajuste»; en la crisis llegó a no cubrir las amortizaciones. Las infraestructuras de titularidad pública son >70 % del capital público; el conjunto de infraestructuras (públicas+privadas) multiplicó por 1,9 desde 1995 pero está **estancado desde la Gran Recesión**.
- Pendiente: stock a 2024-2025 y euros absolutos del capital público neto (no leídos en cifras).

### 2.3 Licitación de obra (SEOPAN) [P para la cifra, sesgo marcado]
SEOPAN (patronal de grandes constructoras: ACS, Ferrovial, Acciona, OHLA, FCC, Sacyr): rueda de prensa 24-abr-2026: https://seopan.es/wp-content/uploads/2026/04/Rueda-de-Prensa-DEF-24-ABRIL-15h56.pdf
- HECHO (según SEOPAN): licitación pública de obras 2025 = **32.260 M€ (+10,2 %)**: edificación 13.646 M€ (Estado 21,7 %, CCAA 38,0 %, EELL 40,3 %); obra civil 18.615 M€ (+9,6 %; Estado 35,6 %, CCAA 24,0 %, EELL 40,3 %). Contratación (adjudicación) 21.832 M€ (+1,5 %), con el Estado a la baja (obra civil −20 %). Licitación con fondos del Plan de Recuperación: 1.571 M€ en 2025 (−31,2 %); 12.359 M€ acumulados 2019-2025, 83,2 % del Estado. (Otra nota de prensa recoge 18.418 M€ de MRR 2019-2025 con otro perímetro: Merca2, 14-jun-2026 [S]; no concilio cifras.)
- Licitación ≠ ejecución ≠ pago. Licitado en 2025 puede construirse en 2026-2028.
- **Sesgo de SEOPAN:** gana con más licitación, con la recuperación del modelo concesional y con un peaje de 0,03 €/km que propone; su cifra de necesidades (407.000 M€ en diez años; 127.000 M€ de conservación) es una estimación del emisor interesado, no un gasto medido.
- 2026 acumulado: no localizado en el original [VERIFICAR].

### 2.4 Mantenimiento ferroviario (Adif) y carreteras
- Adif/Adif AV, convenios con el Estado para mantenimiento (SEOPAN, a partir de datos del Ministerio, mismo PDF): conjunto Adif + Adif AV **753 M€ (2019) → 1.101 M€ (2025)** (+46 %), y acuerdo del Ministerio con sindicatos del 9-feb-2026 para llegar a **1.808 M€ en 2030** (+64 % sobre 2025; +1.085 M€ extra 2026-2030) [S; fuente original del Ministerio y convenios sin leer: [VERIFICAR]]. El «861 M€» de mantenimiento de Adif en 2026 que citaba C77 coincide con la fila «Nuevo» del convenio de Adif (SEOPAN) [S].
- Adif y Adif AV: programa de inversión 2022-2026 de **24.100 M€** (Adif 12.108 M€; AV 12.000 M€), con ~la mitad ejecutada a cierre de 2024 y fondos MRR de >4.000 M€ y 1.375 M€ (The Objective, 19-ene-2026, citando el Programa de Actividad de Adif 2022-2026 [S]). No separa inversión y mantenimiento. Transportes ha dicho tener 7.603 M€ de MRR asignados y 7.677 M€ adjudicados (notas recogidas en prensa, ene-2025 [S]; no se ha leído el original).
- Contrato-Programa Estado-Adif 2021-2025/2026 y cuentas anuales 2025: **no localizados** [VERIFICAR]. Ejecución del capítulo 6 (inversiones reales) del Ministerio de Transportes (IGAE): **no localizada** [VERIFICAR]: lo correcto es leer la ejecución mensual de la IGAE y la liquidación del Presupuesto prorrogado 2023.
- Carreteras: AEC (Asociación Española de la Carretera, entidades y empresas del sector viario, que pide fondo propio y peajes), nota de prensa del 3-jul-2025: https://asefma.es/wp-content/uploads/2025/07/NP-Auditoria-estado-carreteras-AEC-2025_DEF_con-QR_03-07-25.pdf [P]. «Déficit de conservación» de **13.491 M€** (9.453 M€ en 2022 + 4.038 M€ nuevos: 20 % por IPC, 23 % por deterioro): Estado 4.721 M€ (26.000 km) y CCAA/forales 8.770 M€ (75.300 km). Su objetivo declarado de financiación: fondo propio y eliminar la exención del impuesto de hidrocarburos de otros modos.
- SEOPAN usa ese informe: 58.369 M€ en diez años para conservación y «puesta a cero» de las redes viarias (43.700 M€ de conservación para alcanzar umbrales de calidad, +56 % sobre el gasto actual de ~4.370 M€/año como referencia), y **7.651 M€ de déficit de conservación 2010-2024** (El Independiente, 27-abr-2026 [S]). Las dos cifras (AEC 13.491 y SEOPAN 7.651) **no son comparables**: distinto perímetro y método; ambas de emisores con interés. En diciembre de 2026 vencen 10 concesiones de autovía (993 km) que el Estado pasa a conservar directamente (SEOPAN; coste ~80.000 €/km [S]).
- Gasto de conservación real del Ministerio de Transportes (euros por año): no hallado en fuente oficial [VERIFICAR]. Una cifra de prensa (56.000 €/km en autovías frente a 80.000 €/km necesarios, El Debate 26-feb-2026) viene de la AEC [S].

## 3. Resultados (no inputs) — con la distinción percibido / medido

| Indicador | Dato | Tipo | Fuente |
|---|---|---|---|
| Carreteras, estado del firme | 52 % de la red interurbana (54.373 de 101.700 km) con deterioros graves o muy graves; 33.966 km «reconstrucción urgente», frente a 13.000 km en 2022 | Medido (muestra de 4.000 km con imágenes e IA, trabajo de campo verano 2024), pero encargado e interpretado por la AEC [sesgo] | AEC, 3-jul-2025 [P] |
| Calidad de carreteras (WEF, GCI 2019) | 5,7 sobre 7 (ferrocarril 5,4 sobre 7) | **Percibido** (encuesta a directivos), último año disponible, 2019 | theglobaleconomy.com (secundaria): https://www.theglobaleconomy.com/Spain/railroad_quality/ [S; el rango exacto 2019 no confirmado; el GCI dejó de publicarse tras 2019 [VERIFICAR]] |
| Cercanías/Rodalies, puntualidad (ene-sep 2025) | 94,9 % puntuales en destino (margen hasta 5 min), pero 47,7 % cumplen el horario en todas las paradas; regularidad Rodalies Catalunya 74,5 % | Medido por Renfe (portal de transparencia), citado por ARA, 13-oct-2025 | https://es.ara.cat/sociedad/movilidad/mitad-trenes-cercanias-incumple-horario-propia-renfe_1_5526892.html [S] |
| Rodalies, causas | Renfe atribuye el 82,9 % de incidencias a causas externas (Moncloa, oct-2026) | Prensa [S]; «externo» no equivale a «Adif» (lectura del medio) [VERIFICAR] |
| Accidente de Adamuz, ene-2026 | Hipótesis de rotura de carril (informe a la jueza 28-abr-2026); CIAF sin informe final localizado; causa no concluida | Hecho abierto [VERIFICAR]; ver C77 §10.7 |

- Lo que **sí** se puede decir: el firme de una parte grande de la red está deteriorado según una auditoría visual-IA de un lobby sectorial; hay incidencias ferroviarias documentadas en Rodalies. Lo que **no**: que haya una serie oficial homogénea de «calidad de infraestructuras» 2019-2026. No he localizado indicadores oficiales (Transportes) de estado del firme (IRI) ni de incidencias de infraestructura por año.

## 4. Contraste (años 2019-2025)

Euros corrientes. Recaudación = AEAT (caja, M€); cotizaciones, ingresos y gasto = Eurostat S13; % PIB con el PIB de `espana.json`. Intereses = D41 pagados (Eurostat). Pensiones = COFOG «vejez» (solo hasta 2024).

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Recaudación AEAT (M€) | 212.808 | 194.051 | ~223.300 | 255.463 | 271.935 | 294.734 | 325.356 |
| … % PIB | 17,0 | 17,2 | 18,1 | 18,6 | 18,2 | 18,4 | 19,3 |
| Cotizaciones (M€) | 160.656 | 162.174 | 171.687 | 180.086 | 197.003 | 210.294 | 223.230 |
| Ingresos AAPP (% PIB) | 39,0 | 41,5 | 42,8 | 41,7 | 42,1 | 42,2 | 42,9 |
| Gasto total (M€) | 526.769 | 580.164 | 611.124 | 637.117 | 680.225 | 725.122 | 766.296 |
| … % PIB | 42,0 | 51,4 | 49,5 | 46,3 | 45,5 | 45,4 | 45,3 |
| Inversión bruta (M€) | 27.206 | 29.694 | 33.591 | 37.350 | 44.696 | 43.253 | 50.628 |
| … % PIB | 2,2 | 2,6 | 2,7 | 2,7 | 3,0 | 2,7 | 3,0 |
| Depreciación (M€) | 28.850 | 29.191 | 30.919 | 34.076 | 35.529 | 37.729 | 39.764 |
| Intereses (M€) | 28.231 | 25.127 | 26.170 | 31.775 | 35.551 | 38.903 | 40.432 |
| … % PIB | 2,3 | 2,2 | 2,1 | 2,3 | 2,4 | 2,4 | 2,4 |
| Pensiones vejez (M€) | 118.714 | 122.744 | 129.584 | 137.505 | 153.051 | 165.050 | n.d. |
| … % PIB | 9,5 | 10,9 | 10,5 | 10,0 | 10,2 | 10,3 | n.d. |
Variación 2019→2025 (cálculo propio): recaudación AEAT +53 %; PIB nominal +35 %; gasto total +45 %; inversión bruta +86 %; intereses +43 %; pensiones 2019→2024 +39 %.

### 4.1 Qué dice el dato
- HECHO: la recaudación sube más que el PIB (17,0 → 19,3 % del PIB AEAT; ingresos AAPP 39,0 → 42,9 %) y es máxima en euros corrientes.
- HECHO: la inversión bruta de las AAPP **también** está en máximos recientes en euros (50.628 M€) y en 3,0 % del PIB, por encima de 2019 (2,2 %) y de la depreciación (+10.864 M€ en 2025). Con el gasto total en 45,3 % del PIB, la inversión es ~6,6 % del gasto (50.628 / 766.296; cálculo propio).
- HECHO: la comparación con 2009-2010 es muy distinta: 3,0 % del PIB frente a ~5 %, y el capital público neto cayó un 3,7 % entre 2011 y 2023 (Ivie).
- HECHO: intereses (+43 %) y pensiones (+39 % hasta 2024) crecen cerca del gasto total (+45 %) y más que el PIB; la inversión crece más rápido, pero desde una base baja.

### 4.2 Qué no dice
- No mide mantenimiento (depreciación ≠ conservación) ni la **ejecución** (licitar ≠ construir ≠ pagar), ni qué parte de la inversión va a hospitales, colegios o vivienda en lugar de carreteras y trenes.
- No hay una relación mecánica: la recaudación se reparte por impuestos cedidos (CCAA, EELL), la inversión depende de cada administración (Estado, CCAA, ayuntamientos; las EELL licitan el 40 % de la obra), y el 2025-2026 incluye fondos MRR (UE) que no vienen de la recaudación.
- No separa lo que se debe a inflación de costes de obra (SEOPAN pide revisión de precios; es parte interesada) de volumen real.
- «Calidad» no se puede inferir del input: faltan series oficiales de resultado (IRI, incidencias, retrasos por causa infraestructura).

### 4.3 Dos relatos y su sesgo
- **«Se invierte menos de lo que se recauda» / «hay déficit de conservación»** (AEC, SEOPAN, ASEFMA, oposición política): argumentos válidos — inversión al 3,0 % del PIB frente a ~5 % en 2009-2010; stock de capital público −3,7 % 2011-2023 (Ivie); deterioro del firme medido en 4.000 km. Sesgo: AEC/SEOPAN/ASEFMA representan a empresas del sector con interés en más licitación, peajes o concesiones; sus cifras de «necesidad» son proyecciones propias (13.491 / 58.369 / 127.000 M€) y no coinciden entre sí. [OPINIÓN]: la dirección (infraestructura envejecida) es plausible; la magnitud en euros no está verificada.
- **«El problema es el gasto corriente (pensiones, intereses, plantillas), no la recaudación»** (visión centrada en el gasto): argumentos válidos — pensiones ~10 % del PIB, intereses 2,4 %, y gasto total +45 % desde 2019. Sesgo: quien lo dice suele proponer recortar gasto social o bajar impuestos; el dato muestra que la inversión **sí** ha subido en 2019-2025 (+86 %), mientras intereses (+43 %) y pensiones (+39 % hasta 2024) suben algo más que el PIB nominal (+35 %; +27 % hasta 2024) y casi como el gasto total (+45 %). [OPINIÓN]: este relato es incompleto, porque en 2013-2018 la inversión cayó bajo la depreciación por un ajuste deliberado, no por pensiones.
- Hecho que ambos usan poco: la parte pública ejecutada vía **Adif, Enaire, Puertos y concesionarias** puede estar o no en la FBCF de las AAPP según clasificación contable [VERIFICAR perímetro Eurostat de Adif].

### 4.4 Lectura (graduada)
- HECHO: «récord de recaudación» se confirma (nominal y en % del PIB). HECHO: «inversión pública en mínimos» **no** se confirma para 2025 (3,0 % del PIB, la más alta desde 2012); sí se confirma frente a 2009.
- RAZONADO: el deterioro de redes que se ve hoy (firmes, vía) es compatible con 2013-2019 de inversión bajo la depreciación y con costes de conservación que el aumento reciente aún no ha compensado; el efecto de la inversión reciente tarda años en verse. Por tanto «recaudación récord y servicios peores» no es una contradicción lógica.
- [ESPECULACIÓN]: parte de la inversión 2023 y 2025 (MRR) puede haberse concentrado en obra nueva (alta velocidad, digitalización) más que en conservación.
- Sin fuente fiable: cuánto se gasta hoy exactamente en conservar carreteras y vía (no hay total oficial), ejecución real del capítulo 6 de Transportes y serie de incidencias por causa.

## 5. Pendientes ([VERIFICAR])
1. Serie AEAT 1995-2025 (fichero adjunto al informe anual 2025) para confirmar «récord histórico» en % PIB y valores 2021/2023 de Especiales y Sociedades.
2. IGAE: ejecución del capítulo 6 y transferencias a Adif; cuentas anuales 2025 de Adif y Contrato-Programa 2021-2025.
3. Informe oficial de Transportes sobre estado de carreteras (IRI) y datos de incidencias de infraestructura por causa; CIAF/informe final de Adamuz.
4. Stock de capital público neto en euros y 2024-2025 (Ivie 2025/2026 o INE/AMECO).
5. SEOPAN licitación 2026 acumulada; ejecución de MRR en infraestructuras (Plan de Recuperación, ficha oficial).
6. Si quieres actualizar el Seguimiento y el planning: lo hago bajo tu orden.
