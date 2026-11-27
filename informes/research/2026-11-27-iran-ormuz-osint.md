# Irán / Ormuz: verificación OSINT a 26-27 nov 2026

Fecha de la verificación: 27-nov-2026. Método: búsqueda web + lectura de las páginas citadas (arsenal en `research/OSINT-ARSENAL.md`). No es una recomendación de operar.
Niveles: **A** = fuente oficial/primaria citada por 2+ medios; **B** = medio fiable, una sola fuente o cifra no auditable; **C** = afirmación de parte (Irán, EE. UU., IRGC) o medio con sesgo/secundaria; **[VERIFICAR]** = sin triangular.
Límite honesto: no pude abrir directamente UKMTO, JMIC, CENTCOM, Reuters ni AP (todo vía prensa que los cita). Alarabiya devolvió 403 (solo leído el titular del buscador).

## 1. HECHOS

### 1.1 Tráfico en Ormuz
| # | Hecho | Fuente, fecha | URL | Nivel |
|---|---|---|---|---|
| 1 | El aviso del JMIC del 26-nov dice que se sigue cruzando, pero con tráfico muy por debajo de lo normal y amenaza «severa» (2.º nivel de 5); más ataques a petroleros «muy probables». | Khaleej Times, 27-nov (cita JMIC 26-nov) | https://www.khaleejtimes.com/world/mena/is-strait-of-hormuz-open-today-ships-still-crossing-as-tanker-attacks-disrupt-traffic | B (JMIC no leído directo) |
| 2 | 17 petroleros alcanzados desde el 1-nov; ~218 buques comerciales parados en fondeaderos al este del estrecho (~171 en Fujairah/Khor Fakkan el 26-nov, ~167 el 22-nov). Esos fondeados no son necesariamente buques que esperan cruzar. | ídem | ídem | B |
| 3 | Media de ~138 buques/día en 2025 (JMIC). Datos navales de EE. UU.: 128 cruces «asistidos» por EE. UU. del 22 al 25-nov (~32/día, frente a ~38/día del 19 al 21). S&P AIS: solo 3 cruces comerciales no asistidos (22-25 nov), todos petroleros entrando al Golfo. Sin cifra oficial para el 26-nov. | ídem | ídem | B |
| 4 | Un monitor AIS externo da 25 cruces en las 24 h hasta las 14:01 UTC del 26-nov (9 entrada, 16 salida), ~0,71 M barriles/día saliendo. Otro tracker, 2 cruces en el día parcial y media 7 días de 7,1/día. Las cifras no cuadran entre sí (distinta metodología). | agregadores citados por búsqueda | https://hormuz.data-tracking.net/ , https://hormuz.now/traffic | C (agregadores AIS, no auditados) |
| 5 | Referencia previa a la guerra: 84,8 tránsitos/día (IMF PortWatch, 28-feb-2025 a 27-feb-2026). Nota: no coincide con los 138/día del JMIC; son definiciones distintas de «buque». | PortWatch vía búsqueda | https://portwatch.imf.org | B [VERIFICAR consulta directa a la API] |

### 1.2 Incidentes y minas
| # | Hecho | Fuente, fecha | URL | Nivel |
|---|---|---|---|---|
| 6 | UKMTO: tres buques alcanzados por proyectiles no identificados navegando al este por el estrecho, todos siguieron y la tripulación está a salvo (reportado 23-24 nov; Khaleej lo fecha los hechos el 22-nov). Discrepancia de un día entre fuentes. | Iran International 25-nov; Khaleej Times 27-nov | https://www.iranintl.com/en/202611254651 | B |
| 7 | 25-nov: un petrolero de salida alcanzado a ~18 mn al este de Khasab (Omán). | Khaleej Times (JMIC 26-nov) | enlace 1.1 | B |
| 8 | 20-nov: petrolero incendiado por proyectil a ~8 mn al norte de Khasab; 22-nov (informe): impactos a ~11 mn al norte y ~17 mn al este de Khasab; sin heridos. | US News 20-nov; gCaptain/Logistics ME vía búsqueda | https://www.usnews.com/news/world/articles/2026-11-20/tanker-catches-fire-after-projectile-strike-near-strait-of-hormuz-ukmto-says | B |
| 9 | 22-nov (domingo): UKMTO informa de un petrolero «involucrado en un incidente con fuerzas militares» en el Golfo de Omán, cerca de Chabahar, junto a la línea del bloqueo. Euronews señala que la redacción podría apuntar a acción de EE. UU., pero es inferencia; UKMTO no lo confirma ni hay comunicado de CENTCOM en el texto. | Euronews 22-nov | https://www.euronews.com/2026/11/22/tanker-incident-involving-military-forces-reported-in-strait-of-hormuz | B (hecho UKMTO); atribución [VERIFICAR] |
| 10 | Minas: el IRGC/Armada iraní afirman que 2-3 petroleros chocaron con minas (22-24 nov). El JMIC dice que esas afirmaciones no están confirmadas por autoridades oficiales o nacionales y que no establece que las minas causaran los impactos; recomienda vigilar posible minado en los carriles. UKMTO habla de «proyectiles no identificados». | Iran International 25-nov; Khaleej (JMIC 26-nov) | enlaces 1.1 y 1.2 | Minas como causa: C / [VERIFICAR]. Alerta del JMIC: B |
| 11 | Quién dispara: ninguna fuente consultada lo establece. Atribución contestada. | varias | , | [VERIFICAR] |

### 1.3 Bloqueo naval de EE. UU.
| # | Hecho | Fuente, fecha | URL | Nivel |
|---|---|---|---|---|
| 12 | Cronología: bloqueo impuesto el 13-abr; levantado en junio tras un entendimiento; restablecido el 14-jul al romperse el acuerdo. Las exportaciones visibles de crudo iraní, cerca de cero. (Reuters citado el 23-nov.) | Al Jazeera 20-nov; US News 23-nov | https://www.aljazeera.com/news/2026/11/20/us-targets-irans-ship-to-ship-transfers-can-tehran-break-the-blockade , https://www.usnews.com/news/world/articles/2026-11-23/iran-says-it-will-use-all-available-tools-to-confront-us-naval-blockade | B (el texto de US News no pudo abrirse; solo resumen del buscador) |
| 13 | CENTCOM, 11-nov: casi 150 buques redirigidos y 5 inutilizados desde el inicio de la fase actual (la fecha de inicio varía: junio/julio según medio). 7-nov: aviación de EE. UU. inutilizó el M/V Huda (St. Kitts) en el Golfo de Omán. | Middle East Eye; Israel National News vía búsqueda | https://www.middleeasteye.net/live-blog/live-blog-update/centcom-says-144-vessels-redirected-under-ironclad-iran-blockade | B (CENTCOM no leído directo); cifras no reconciliadas (130, 144, ~150 en fechas distintas) |
| 14 | CENTCOM amplió el criterio (aviso del 18-nov): buques que reciben carga de naves cargadas en puertos/costa iraníes pueden considerarse «evadiendo el bloqueo» y ser parados, abordados, desviados o capturados. | Al Jazeera 20-nov | enlace 12 | B |
| 15 | Kpler (24-nov): sin nuevas exportaciones de crudo ni condensado iraníes; no hay mes completo de exportación desde septiembre. Las refinerías «teapot» chinas dejaron de importar por mar crudo iraní en septiembre (según reporte del 24-nov). | Iran International 24-nov | https://www.iranintl.com/en/202611247460 | B (Kpler es de pago; citado en medio de la oposición iraní) |
| 16 | Reuters/TankerTrackers (19-20 nov): un buque cargando crudo iraní por transbordo; sería la primera exportación lograda desde julio si llega. Irán no lo confirma. | Al Jazeera 20-nov | enlace 12 | B/C (TankerTrackers: privada, no auditable) |
| 17 | Convoy: Fars (IRGC) propuso un convoy a China con amenazas a infraestructura del Golfo, «especialmente UAE»; circularon bulos de un petrolero «Line Breaker» y de 14 petroleros cruzando. Tasnim (22-nov) y Exteriores (23-nov) los niegan; TankerTrackers dijo que «Line Breaker» no existía. The National: informe no verificado de que el Consejo de Seguridad Nacional frenó 14 petroleros. | Iran International 25-nov; The National 24/26-nov | https://thenationalnews.com/news/gulf/2026/11/24/is-iran-weighing-tanker-convoy-to-break-us-blockade | Convoy realizado: **no hay evidencia**. Debate interno: B |
| 18 | Efecto interno en Irán: inflación 88,7 % interanual en octubre, recortes eléctricos, cola de ~1.200 camiones en 42 km en antiguas repúblicas soviéticas; rial ~2,82 M/USD en el mercado libre el 24-nov. | The National 24-nov; Iran International 25-nov | enlaces 17 y 1.3 | B/C (cifras iraníes no oficiales) |
| 19 | Sanciones del Tesoro: 22 entidades y 8 personas el 23-nov («Operation Economic Outcast»). | Iran International 25-nov | https://www.iranintl.com/en/202611254651 | B [VERIFICAR en comunicado OFAC] |

### 1.4 Negociaciones EE. UU.-Irán
| # | Hecho | Fuente, fecha | URL | Nivel |
|---|---|---|---|---|
| 20 | Sin acuerdo firmado ni ronda formal. Araghchi (26-nov): mediadores de Catar y Pakistán siguen pasando mensajes; Irán no ha abandonado las negociaciones; hay un mecanismo bajo el Consejo Supremo de Seguridad Nacional; ideas sobre la mesa en revisión; Irán exige condiciones antes de reabrir Ormuz. | Al Arabiya 26-nov, Anadolu (anews) 26-nov (solo titular/resumen de buscador; página 403) | https://english.alarabiya.net/News/middle-east/2026/11/26/mediators-continue-transmitting-messages-between-iran-and-us-iran-s-foreign-minister-says | B (no leído íntegro) |
| 21 | 21-nov: mediadores cataríes viajaron a Teherán; el viceministro Gharibabadi dijo que aún no son negociaciones formales. | Al Jazeera 21-nov | https://www.aljazeera.com/news/2026/11/21/iran-says-held-talks-with-qatari-mediators-urges-us-to-accept-conditions | B (solo titular/resumen) |
| 22 | Condiciones públicas de Irán (resumen): cese de hostilidades, levantar el bloqueo, exención de sanciones. Reportadas también: materiales nucleares dentro de Irán. | US News 23-nov; buscador | enlace 12 | C (posición de parte) |
| 23 | Trump (22-nov): inclinado a reanudar operaciones militares tras Año Nuevo si no hay acuerdo; sobre buques iraníes que desafíen el bloqueo: «I hope they do, they will all be at the bottom of the sea». | Euronews 22-nov | enlace 9 | A como cita; contenido = posición de parte |
| 24 | Contexto: Conversaciones de Islamabad (11-12-abr, sin acuerdo); memorando de Islamabad (17-jun) que luego colapsó; ronda mediada en la ONU (sept.). | Wikipedia y Al Jazeera 23-sep vía búsqueda | https://en.wikipedia.org/wiki/Islamabad_Talks | C (Wikipedia, secundaria) |

### 1.5 China y Rusia
| # | Hecho | Fuente, fecha | URL | Nivel |
|---|---|---|---|---|
| 25 | Cumbre Trump-Xi-Putin en Shenzhen (19-nov, margen de APEC): la declaración conjunta de cuatro puntos no menciona Irán ni Ormuz. | Iran International 24-nov | https://www.iranintl.com/en/202611247460 | B (coincide con el seguimiento previo de Cumbres del repo) |
| 26 | Bessent (21-nov): Xi y Putin «acordaron que nunca puede tener un arma nuclear». Es afirmación de EE. UU.; sin comunicado que la respalde. | ídem | ídem | C |
| 27 | Irán (Baghaei, 23-nov): contacto con Moscú y Pekín antes y después de la cumbre; «las decisiones sobre Irán no se toman fuera de Teherán». | ídem | ídem | B (cita directa; posición de parte) |
| 28 | Embajador chino en Irán, Cong Peiwu (25-nov): desescalada y vuelta a las conversaciones como prioridad inmediata. Única posición china oficial localizada de noviembre. | Iran International 25-nov | https://www.iranintl.com/en/202611254651 | B |
| 29 | Posiciones anteriores (abr.-jul.): China calificó el bloqueo de «peligroso e irresponsable» (14-abr, CNBC); Rusia y China vetaron una resolución de la ONU sobre Ormuz (7-abr, Al Jazeera); Lavrov: Irán no bloqueó Ormuz y no quiere peajes (mayo-sept.). No hay declaración rusa del Kremlin sobre el bloqueo fechada en noviembre. | CNBC, Al Jazeera, TASS | https://www.cnbc.com/2026/04/14/china-us-strait-of-hormuz-war-donald-trump-oil-energy-crisis-conflict-middle-east-iran.html , https://aljazeera.com/news/2026/4/7/russia-and-china-block-un-resolution-on-strait-of-hormuz | B (histórico, no de noviembre) |
| 30 | Sin despliegue naval chino/ruso confirmado para escoltar convoyes iraníes. | análisis citados por búsqueda | , | [VERIFICAR] (ausencia de evidencia, no evidencia de ausencia) |

## 2. OPINIONES / AFIRMACIONES SIN CONFIRMAR (no son hechos)
- «China advirtió a Trump de no tocar los petroleros iraníes» (Larry Johnson, vía agregadores): fuente única, anónima, sin confirmación. [ESPECULACIÓN]
- Teorías de «acuerdo secreto» en Shenzhen que dejarían a Irán de lado: figuras iraníes las defienden; analistas iraníes dicen que no hay pruebas. [ESPECULACIÓN]
- Hassanzadeh, Mohebbi (IRGC): el bloqueo se abandonará por agotamiento; capacidades «en aumento». Bessent: Irán es «un barco que se hunde». Retórica de parte. [OPINIÓN]
- Krieg (King's College): Irán puede esquivar parcialmente el bloqueo, pero no romperlo de forma sostenible; los petroleros que lo desafían buscan quizá la confrontación. Pinfold: Washington eligió el bloqueo frente a nuevos ataques masivos. [OPINIÓN de analistas]
- Previsión del JMIC de más ataques «muy probables»: valoración de riesgo, no hecho consumado. [OPINIÓN experta]

## 3. Sesgos de las fuentes
- Iran International (oposición, con sede en el exterior), Fars/Tasnim/Sabereen (IRGC) y los comunicados de EE. UU. son partes interesadas: se usan solo como cita atribuida.
- TankerTrackers/trackers AIS: empresa privada o agregadores; el AIS se apaga en la flota en la sombra. Cifras de tránsito divergen entre fuentes (media 7/día, 25-32/día, referencia previa 84,8 y 138/día según fuente y definición).
- Wikipedia: solo para cronología general.

## 4. Pendiente de triangular [VERIFICAR]
1. Lectura directa del aviso JMIC 26-nov y de UKMTO (ukmto.org) con fechas exactas de los tres impactos (22 vs 23-nov).
2. Quién atacó los petroleros y si hubo minas reales (sin confirmación oficial).
3. Qué fue el incidente «con fuerzas militares» del 22-nov cerca de Chabahar (comunicado CENTCOM).
4. Texto íntegro de Araghchi del 26-nov (Al Arabiya devolvió 403) y estado real de la mediación catarí/paquistaní.
5. Consulta a la API de IMF PortWatch (ArcGIS) para tránsitos de 24-27 nov con definición homogénea.
6. Comunicado OFAC del 23-nov y cifras vigentes de CENTCOM (redirigidos/inutilizados).
7. Posición actual del Kremlin y del MAE chino (solo se localizó al embajador en Teherán).
8. Si alguna carga de crudo iraní (transbordo 17-20 nov) llegó a destino.

## 5. Lectura (solo para análisis)
Caso «contención»: tráfico reducido pero no cortado, bloqueo firme y mediación abierta. Caso «escalada»: amenaza severa, convoy anunciado en medios de IRGC y Trump hablando de retomar ataques tras Año Nuevo. Datos de tráfico y atribución de ataques son los más débiles; el resto de la foto (bloqueo vigente, sin acuerdo, China sin gestos públicos de ruptura) está respaldado por varias fuentes.
