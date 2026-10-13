# Guía G9: Commodities (materias primas): oro, plata, petróleo, cobre y más (España, 13-oct-2026)

> **Guía educativa, no es recomendación** de comprar, vender ni contratar ninguna materia prima, ETC, ETN, ETF, fondo, minera, bróker o entidad. Foco en España, para un inversor particular a largo plazo. Fuentes **primarias leídas hoy**: **BOE** (Ley 37/1992 del IVA, arts. 140 y 140 bis, texto consolidado vía API del BOE, actualizado el 7-oct-2026), **FRED** con datos de la **EIA** (Brent spot diario hasta el 6-oct-2026), **FRED** con datos del **Tesoro de EE. UU.** (tipo real a 10 años, 8-oct-2026) y **FRED/BLS** (IPC de EE. UU. hasta ago-2026). **Secundarias**: Yahoo Finance (contratos de futuros continuos de COMEX/NYMEX para oro, plata, cobre y WTI; **no son el precio oficial LBMA**). **No pude abrir**: LBMA (los datos históricos exigen licencia de ICE Benchmark Administration y su API devolvió bloqueo), World Gold Council, CME, OPEP, AIE, FMI. Lo no confirmado en fuente primaria va como **[VERIFICAR]**; las opiniones y previsiones, como **[ESPECULACIÓN]**. Los números de simulación son **cálculo mío**, con método explicado. **El pasado no garantiza el futuro.**

## 0. Resumen en 12 líneas
1. Una **commodity** es un bien físico intercambiable (oro, petróleo, cobre, trigo): su precio se fija por **oferta y demanda globales**, no por beneficios de una empresa (§1).
2. **No generan flujos**: ni cupón (G4) ni dividendo (G5). La única fuente de ganancia es que **el precio suba** (§4).
3. Cuatro formas de invertir, muy distintas: **físico**, **ETC/ETN de réplica física**, **productos de futuros** y **acciones de mineras o petroleras** (que **no son** la materia prima) (§2).
4. **Físico**: lingotes y monedas cuestan más de comprar que de vender (**prima y horquilla**) y exigen **custodia y seguro**. Con una prima de compra del 5 % y un precio de venta del 3 % bajo el de referencia, el oro tiene que **subir un 8,2 %** solo para empatar (ejemplo hipotético, §2.1).
5. **IVA**: el **oro de inversión está exento** (BOE, art. 140 bis). La **plata no** entra en esa exención y lleva IVA general (21 % según G12 [VERIFICAR]) (§5.1).
6. **Contango**: un producto de futuros puede perder dinero aunque el precio al contado no se mueva. Ejemplo mío: con un 2 % de contango mensual, **−21,2 % en un año con el precio plano**; con backwardation del 2 %, **+27,4 %** (§2.3).
7. **Rentabilidad pasada** (cierres a 30-sep-2026, 10 años): oro **12,3 %/año**, plata **12,1 %**, cobre **11,5 %**, Brent spot **9,2 %**; a 20 años bastante menos en cobre (**3,3 %**) y Brent (**3,4 %**). Caídas máximas: oro **−42 %**, plata **−72 %**, cobre **−65 %**, Brent **−89 %** (cierres mensuales) (§3).
8. **Inflación**: el oro tocó un máximo en enero de 1980 (850 $ [VERIFICAR, secundaria]) y, **descontando el IPC de EE. UU.**, no volvió a superarlo hasta **~sep-2025** (cálculo mío): **más de 45 años** (§4.3).
9. **Divisa**: cotizan en **USD**; el euro fuerte resta (G5 §5.4) (§6).
10. **Datos actuales** (13-oct-2026): oro **~4.209 $/oz**, plata **~60,5 $/oz** (ratio oro/plata **~69,6**), Brent futuros **~104,6 $**, **Brent spot 125,44 $ (6-oct, EIA)** y tipo real a 10 años en EE. UU. **2,87 %** (8-oct, Tesoro) (§8).
11. **Ormuz**: según el dossier 11, sigue **casi cerrado**; el Brent spot promedió **114,2 $ en septiembre** y llegó a **138,21 $ el 7-abr**. **El spot y los futuros no son lo mismo** (§8).
12. Los productos apalancados (futuros, CFD) se tratan en la **G7** (derivados y apalancamiento): aquí solo el aviso de riesgo (§2.4).

## 1. Qué son y qué mueve su precio
### 1.1 Glosario corto
| Término | Significado sencillo |
|---|---|
| **Commodity (materia prima)** | Bien físico estandarizado e intercambiable. Da igual quién lo produjo: un barril de Brent vale lo mismo en cualquier lote de la misma calidad. |
| **Precio al contado (*spot*)** | Precio para entrega inmediata (o casi). El oro LBMA y el Brent «físico» de la EIA son precios spot. |
| **Futuro** | Contrato para comprar o vender una cantidad a un precio fijado hoy y entrega en una fecha futura. |
| **Contrato continuo** | Serie que pega un contrato tras otro (el más cercano al vencimiento). Los saltos entre contratos pueden distorsionar la serie. |
| **Contango** | El futuro **más lejano cuesta más** que el contado. Típico si hay costes de almacenamiento y financiación. |
| **Backwardation** | El futuro **más lejano cuesta menos** que el contado. Típico si escasea el bien ahora. |
| **Roll (renovación)** | Los productos de futuros venden el contrato que vence y compran el siguiente. |
| **Roll yield** | Ganancia o pérdida **solo por renovar**: negativa en contango, positiva en backwardation. |
| **ETC** | *Exchange Traded Commodity*: producto cotizado sobre una materia prima. Si es de **réplica física**, el emisor guarda el metal. |
| **ETN** | *Exchange Traded Note*: **deuda** del emisor que paga lo que marque un índice. **Riesgo de crédito del emisor.** |
| **Prima / horquilla** | Prima: sobreprecio sobre el precio de referencia al comprar físico. Horquilla: diferencia entre precio de compra y de venta. |
| **Tipo real** | Tipo de interés **descontando la inflación esperada**. El rendimiento del bono ligado a inflación (TIPS) a 10 años es la referencia habitual en EE. UU. (G1). |
| **Tasa oro/plata** | Cuántas onzas de plata cuesta una onza de oro. |
| **Onza troy (oz)** | 31,1035 gramos. Unidad de los metales preciosos. |
| **Caída máxima (*drawdown*)** | Mayor caída desde un máximo hasta el mínimo posterior. |
| **Volatilidad** | Desviación típica anualizada de las rentabilidades mensuales. |
| **KID / PRIIPs** | Documento de datos fundamentales obligatorio para productos minoristas en la UE (G5). |

### 1.2 Tipos de commodities
| Grupo | Ejemplos | Particularidad |
|---|---|---|
| **Metales preciosos** | Oro, plata, platino, paladio | Se guardan fácilmente y duran siglos. El oro tiene además una demanda de **reserva de valor** (joyería, inversión, bancos centrales). La plata mezcla inversión con **uso industrial** (electrónica, solar). |
| **Energía** | Petróleo (Brent, WTI), gas natural, carbón | Se consumen: **no se acumulan sin límite**. Almacenarlos cuesta, y su precio depende de la geopolítica y del ciclo económico. |
| **Metales industriales** | Cobre, aluminio, níquel, litio | Muy ligados al **ciclo industrial** (China, construcción, vehículos eléctricos). |
| **Agrícolas** | Trigo, maíz, soja, café, azúcar | Dependen del clima, plagas y política comercial; precios muy estacionales. |

**Brent y WTI**: son dos referencias de crudo. **Brent** (Mar del Norte) se usa de referencia para gran parte del crudo mundial; **WTI** (Texas) se negocia en EE. UU. [VERIFICAR el peso exacto de cada una en fuente oficial].

### 1.3 Qué mueve el precio (hechos generales y relaciones habituales)
| Factor | Cómo suele actuar | Límite |
|---|---|---|
| **Oferta** | Menos producción o cierres de rutas (Ormuz) → precio al alza | Los productores pueden reaccionar con retraso (años en minería y petróleo) |
| **Demanda** | Crecimiento mundial, industria, joyería, compras de bancos centrales (oro) | Una recesión hunde la demanda de petróleo y metales industriales |
| **Dólar** | Los precios se fijan en USD: **dólar fuerte** suele presionar a la baja el precio en dólares; **débil**, al alza | Relación **habitual, no ley**; en crisis el dólar a veces sube a la vez que el oro |
| **Tipos reales** | **Tipos reales altos** suelen perjudicar al oro (no paga renta, y el dinero rinde más) | **No siempre se cumple**: hoy el tipo real a 10 años es **2,87 %** (§8) y el oro cotiza cerca de máximos |
| **Inflación** | Se espera que protejan frente a ella; el oro lo ha hecho a largo plazo pero con décadas de excepciones (§4) | La inflación **por energía** (hoy) beneficia al petróleo, no necesariamente al oro |
| **Geopolítica** | Conflictos elevan el petróleo y el oro | Los **picos** suelen revertirse (Brent −82 % en 2018-2020, §3) |
| **Almacenamiento y financiación** | Explican contango o backwardation | En los futuros, importan más que el precio al contado (§2.3) |
| **Inventarios y reservas estratégicas** | El G7 acordó liberar hasta 100 M de barriles (dossier 11, 2-oct) | Cifra de prensa y comunicado resumido [VERIFICAR] |

## 2. Formas de invertir y diferencias
### 2.1 Físico: lingotes y monedas
| Aspecto | Qué hay que saber |
|---|---|
| **Coste de compra** | Precio de referencia **+ prima** (acuñación, fabricación, margen del distribuidor). La prima es mayor en **monedas y lingotes pequeños** [VERIFICAR con tarifas públicas; no he consultado ninguna] |
| **Horquilla** | El distribuidor compra **por debajo** de la referencia. La diferencia entre compra y venta es el coste de entrar y salir |
| **Custodia y seguro** | En casa (riesgo de robo; seguro del hogar con límites habituales para objetos de valor [VERIFICAR]) o en **caja de seguridad / custodia profesional** (coste anual) |
| **Liquidez** | Se vende a un distribuidor, a veces con **verificación de pureza**. No es instantáneo ni sin coste |
| **Prueba de coste** | Para calcular la ganancia fiscal hay que **justificar** lo pagado (facturas, G12 §3.5) |
| **IVA** | **Oro de inversión: exento**; plata y otros metales: IVA general (§5.1) |

**Ejemplo numérico (hipotético, cálculo mío)**: oro de referencia **4.209 $/oz**. Compras con prima del **5 %** (4.419 $); un distribuidor te lo compraría al **97 %** de la referencia (4.082 $). Para recuperar lo pagado, la referencia debe subir **105/97 − 1 = 8,2 %**. Los porcentajes son **supuestos**, no tarifas reales.

### 2.2 ETCs y ETNs de réplica física
**Hechos**
- Un **ETC de réplica física** guarda metal real (en cámaras de un custodio) por cada título. Cotiza en bolsa como una acción.
- Un **ETN** no guarda metal: es **deuda del emisor**. Si el emisor quiebra, puedes perder aunque el oro suba (riesgo de contraparte).
- Se compra y vende en bolsa con la comisión del bróker y la horquilla (G5 §3.3). Cobran una **comisión anual** (TER).
- **No generan flujos**: no pagan nada mientras los mantienes.
**Qué mirar en el KID** (G5 §10): réplica (física o sintética), emisor y custodio, TER, divisa, estructura jurídica (ETC o ETN) y si el metal está **asignado y auditado** [VERIFICAR; **no he leído ningún folleto**].
**Fiscalidad**: ver §5 y G12 §3.2: ganancia patrimonial al vender; la retención y la calificación exacta están **sin confirmar** [VERIFICAR].

### 2.3 ETFs y ETCs de futuros: contango, backwardation y roll yield
**Idea**: un producto de petróleo, gas o agrícolas **no puede guardar barriles**; compra **futuros** y los renueva (*roll*) antes del vencimiento. Si el contrato siguiente es **más caro**, cada renovación **cuesta dinero**.

**Ejemplo numérico (hipotético, cálculo mío)**: el precio al contado está **plano en 100** todo el año.
| Caso | Futuro a 1 mes | Efecto de cada renovación | Resultado a 12 meses |
|---|---|---|---|
| **Contango** | 102 | Compras a 102 un contrato que converge a 100: **100/102 = −1,96 %** al mes | (100/102)¹² = **0,7885 → −21,2 %** |
| **Backwardation** | 98 | Compras a 98 y converge a 100: **100/98 = +2,04 %** al mes | (100/98)¹² = **1,2743 → +27,4 %** |
- El producto de futuros **no replica el precio al contado**: replica el **precio del futuro más la renovación**. Con el spot plano, el inversor pierde en contango y gana en backwardation.
- **2 % mensual es una cifra pedagógica**, no un dato real. El contango real varía con almacenamiento, financiación y tensión física.
- **Observación del dossier 11**: la EIA publica un **Brent spot de 125,44 $ (6-oct)** frente a **~104–105 $ de futuros** (§8): la curva puede estar en **backwardation fuerte** (tensión física). Es **observación mía**, no medida [VERIFICAR].
- **Consecuencia práctica**: en un periodo largo, el rendimiento de un fondo de futuros de petróleo puede diferir mucho del spot. Mi serie de WTI (futuros continuos de Yahoo) rinde **1,8 %/año en 20 años**, y no sé qué parte se debe al roll ni cómo lo habría capturado un producto concreto [VERIFICAR].
- **Para qué sirve el oro como ejemplo de lo contrario**: los ETC de oro de réplica física **no tienen roll**, porque tienen el metal.

### 2.4 Futuros y CFD (apalancamiento)
- **Futuros**: se opera con un **margen** (una fracción del valor del contrato). Un movimiento pequeño del precio supone una ganancia o pérdida **grande sobre el margen**.
- **CFD** (*contract for difference*): contrato con un bróker que replica el precio, a menudo con **apalancamiento**. En la UE, la ESMA limitó el apalancamiento minorista y exige avisos de pérdida [VERIFICAR el límite vigente en CNMV/ESMA].
- **Ejemplo (hipotético, cálculo mío)**: apalancamiento **10×** (margen del 10 %): un movimiento del **−10 %** en el precio borra el **100 %** del margen. Con el Brent, que tuvo caídas diarias de más del 7 % (dossier 11), esto es relevante.
- **Aviso**: son productos **para operar a corto plazo**, no para largo plazo. El detalle va en la **G7**.

### 2.5 Acciones de mineras o petroleras (no son la materia prima)
| Aspecto | Qué hay que saber |
|---|---|
| **Qué compras** | Una **empresa**, no el metal ni el crudo. Su beneficio depende del precio **menos costes**, deuda, impuestos, gestión y coberturas |
| **Apalancamiento operativo** | Con costes fijos altos, una subida del precio suele **multiplicar** el beneficio, y una bajada puede **hundirlo** |
| **Riesgos propios** | Política (nacionalización, impuestos mineros), seguridad, operaciones, dilución por ampliaciones |
| **Dividendos** | Algunas pagan; es un flujo que la materia prima no tiene. Se rigen por G5 §6 |
| **Correlación** | **Sube y baja con la bolsa** además de con el metal [VERIFICAR; **no he calculado** la correlación de ninguna cesta]. |
| **Fiscalidad** | Como cualquier acción (G12 §3.2) |
- **No confundas** tener acciones de una minera de oro con tener oro. En una caída bursátil general, ambas pueden bajar a la vez.

### 2.6 Resumen comparativo
| Forma | Exposición al precio | Costes principales | Riesgo especial | Flujos |
|---|---|---|---|---|
| **Físico** | Directa (oro/plata) | Prima, horquilla, custodia, seguro | Robo, falsificación, liquidez | No |
| **ETC físico** | Directa | TER, horquilla, comisión del bróker | Custodio, emisor | No |
| **ETN** | Indirecta (deuda) | TER, horquilla | **Quiebra del emisor** | No |
| **ETF/ETC de futuros** | Futuro + renovación | TER, **roll yield** | **Contango**, error de seguimiento | No |
| **Futuros / CFD** | Apalancada | Margen, financiación, comisiones | **Pérdida superior al margen** | No |
| **Acciones mineras/petroleras** | Indirecta (empresa) | Comisiones del bróker | Gestión, deuda, bolsa | A veces |

## 3. Rentabilidad histórica (con método y fuente)
### 3.1 Método (cálculo mío)
- **Series**: **oro, plata, cobre y WTI**: contratos de **futuros continuos** (COMEX/NYMEX) de Yahoo Finance, último dato diario de cada mes. **Brent**: **precio spot diario** de la EIA vía FRED (serie DCOILBRENTEU), último dato diario de cada mes. **No son precios LBMA**, ni rentabilidad de ningún producto (no incluyen TER, roll real del producto, impuestos ni divisa).
- **Periodos**: 30-sep-2016 a 30-sep-2026 (10 años) y 30-sep-2006 a 30-sep-2026 (20 años). Rentabilidad anualizada = (final/inicial)^(1/años) − 1. Misma fecha de corte que G5.
- **Volatilidad y caída máxima**: sobre cierres mensuales. **Limitación**: en las series de Yahoo **faltan algunos meses** (17 de 121 en la ventana de 10 años de oro, plata, cobre y WTI; ninguno en Brent), por lo que **volatilidad y caída máxima son aproximadas**; la **rentabilidad anualizada usa solo los extremos y es exacta para esos precios**.
- **Contrato continuo**: pegar contratos distintos puede incluir saltos por roll [VERIFICAR el ajuste de Yahoo]. **La rentabilidad real de quien compra el metal físico o un ETC es otra.**

### 3.2 Resultados
| Activo (serie) | Rent. 10 años (anual) | Vol. 10 años | Caída máx. en la ventana de 10 años | Rent. 20 años (anual) | Vol. 20 años | Caída máx. en la serie disponible |
|---|---|---|---|---|---|---|
| **Oro** (COMEX, USD) | **12,3 %** | 15,2 % | −17 % (2020-08 a 2022-10) | **10,2 %** | 17,8 % | **−42 %** (2011-08 a 2015-12) |
| **Plata** (COMEX, USD) | **12,1 %** | 31,4 % | −38 % (2020-08 a 2022-08) | **8,6 %** | 35,0 % | **−72 %** (2011-04 a 2015-12) |
| **Cobre** (COMEX, USD/lb) | **11,5 %** | 20,9 % | −28 % (2017-12 a 2020-04) | **3,3 %** | 27,1 % | **−65 %** (2008-04 a 2008-12) |
| **Brent spot** (EIA, USD) | **9,2 %** | 55,9 % | −82 % (2018-09 a 2020-03) | **3,4 %** | 46,9 % | **−89 %** (2008-06 a 2020-03, cierres mensuales) |
| **WTI futuros** (NYMEX, USD) | 6,5 % | 53,2 % | −75 % | 1,8 % | 45,4 % | −85 % |
- **Series disponibles**: oro, plata, cobre y WTI desde 2000; Brent spot desde 1987. En «caída máxima en la serie» uso toda la historia disponible (no solo la ventana).
- **Brent con datos diarios**: máximo **143,95 $ (3-jul-2008)** y mínimo **9,12 $ (21-abr-2020)**: **−93,7 %** (cálculo mío, EIA vía FRED). En 2020 el WTI de futuros llegó a cotizar en negativo (hecho conocido; [VERIFICAR en CME]).
- **Sensibilidad al punto final**: el Brent spot a 30-sep-2026 (**115,91 $**) está **muy elevado** por la crisis de Ormuz (dossier 11). Esto **infla** la rentabilidad a 10 años (**9,2 %**) frente a un punto de partida «normal». El WTI de futuros, cuyo final es 90,4 $, da 6,5 %.
- **Lectura**: oro, plata y cobre subieron fuerte en los últimos 10 años, pero con **volatilidad y caídas muy distintas**: el oro es el **más estable** de los cuatro; la plata y el petróleo, mucho más volátiles. **Esto no predice nada** [ESPECULACIÓN si se usa como previsión].
- **Comparación con la inflación**: IPC de EE. UU. (FRED/BLS, desde sep-2016 a ago-2026, cálculo mío): **~3,4 %/año**; a 20 años (sep-2006 a ago-2026): **~2,6 %/año**. El oro **superó** ambos en estas ventanas; el cobre y el petróleo, **en 20 años, solo por poco** (3,3 % y 3,4 % frente a 2,6 %).

## 4. Papel en una cartera según la literatura (y sus límites)
### 4.1 Argumentos habituales (hechos de la literatura general y opiniones)
> **Aviso**: **no he leído** estudios concretos del World Gold Council, del FMI, de bancos centrales ni académicos para esta guía. Lo que sigue son **argumentos que se suelen citar**, marcados como [VERIFICAR].
- **Diversificación**: las materias primas a veces se mueven **distinto** que las acciones y los bonos [VERIFICAR con estudios]. Mi caída máxima del oro (−42 % en 2011-2015) coincidió con un periodo de **subida de las bolsas** (G5 §5.1: S&P 500 al alza en esa fase [no medido por mí]), pero en crisis bursátiles fuertes (2008) el oro **no actuó siempre como refugio inmediato** [VERIFICAR: no he calculado el oro en 2008].
- **Cobertura de inflación**: se asume que protegen frente a subidas de precios. La evidencia es **desigual** según material y periodo (§4.3).
- **Cobertura de riesgo geopolítico**: oro y petróleo suelen subir con las guerras. El Brent spot pasó de **66,6 $ (media de enero 2026)** a **117,3 $ (abril)** (dossier 11, EIA), y luego cayó a **83,8 $ (julio)** antes de volver a **114,2 $ (septiembre)**. **No es una cobertura estable**: los picos retroceden.
- **Opinión** [ESPECULACIÓN]: algunas casas de análisis defienden un porcentaje pequeño de oro en cartera. **No doy porcentaje**; lo que sea adecuado depende de objetivos y plazo (G13, pendiente).

### 4.2 Límites
1. **No generan flujos**: un bono paga cupón y una acción puede pagar dividendo; el oro **no paga nada** (§1). Tu ganancia depende **por completo** del precio de venta.
2. **Costes de mantener**: custodia y seguro en físico; TER en ETC; **roll** en futuros.
3. **Volatilidad alta** en energía y metales industriales (50 % y 21-27 %, §3).
4. **Ciclos largos**: pueden pasar décadas sin batir a la inflación (§4.3).
5. **Divisa**: cotizan en USD (§6).
6. **Sin valoración fundamental sencilla**: no hay PER ni cupón para saber si «está caro».

### 4.3 ¿Cuánto tarda el oro en batir a la inflación? (cálculo mío)
- **Hecho (secundaria, [VERIFICAR])**: el oro marcó un máximo de **~850 $/oz en enero de 1980** (no pude abrir LBMA).
- **IPC de EE. UU.** (CPIAUCSL, FRED/BLS): **78,0** (ene-1980) y **334,1** (ago-2026): factor **×4,28**. Los 850 $ de 1980 equivalen a **~3.641 $ de ago-2026**.
- **Mi serie** (futuros de oro de Yahoo, desde 2000, último dato mensual con IPC disponible): el oro superó ese nivel real **por primera vez en sep-2025 (3.873 $ frente a 3.533 $ de umbral)**. En términos **reales**, tardó **unos 45 años** en volver a su máximo de 1980.
- **En términos nominales**, el oro **no superó 850 $ hasta 2008** (cifra de la memoria histórica; no la he comprobado: [VERIFICAR]).
- **Otro ejemplo (mi serie)**: entre ago-2011 (1.829 $) y dic-2015 (1.060 $), el oro cayó **42 %** nominal. Sin ajustar por inflación.
- **Y en el sentido contrario**: del IPC y precios de sep-2006 a ago-2026, el oro en términos reales multiplicó por **~4,5** (cálculo mío). **Los dos hechos conviven**: protege a veces, pero **no cuando uno lo necesita**.
- **Petróleo**: el Brent spot en dólares nominales rindió **~4,7 %/año desde 1987** (serie EIA, cálculo mío); **no lo comparé con el IPC** [no calculado]. Además, **un inversor no obtiene el spot**: obtiene futuros con roll (§2.3).

## 5. Fiscalidad en España (resumen; ver G12 y dossier 13)
### 5.1 IVA
- **Oro de inversión: exento** (BOE, Ley 37/1992, **art. 140 bis, apartado uno, 1.º**, leído hoy): «las entregas, adquisiciones intracomunitarias e importaciones de oro de inversión».
- **Concepto** (art. 140, leído hoy): **lingotes o láminas de oro de ley ≥ 995 milésimas** (con peso ajustado al anexo) y **monedas de oro** que cumplan: **ley ≥ 900 milésimas**, **acuñadas después de 1800**, que **sean o hayan sido moneda de curso legal** y que se comercialicen habitualmente por un precio **no superior en un 80 % al valor del oro contenido**. Una lista anual publicada en el *Diario Oficial de la UE* sirve de presunción.
- **No hay una exención equivalente para la plata ni para el platino** en esos artículos: **la plata tributa por IVA general** (21 % según G12 §3.5 [VERIFICAR el tipo vigente en el art. 90: la versión que obtuve hoy de la API mostraba el texto histórico de 15 % y no pude confirmar el 21 %]). **Joyería y monedas que no cumplan los requisitos** también quedan fuera [VERIFICAR].
- **Efecto práctico**: con la plata, parte del precio de compra es **IVA que no recuperas** al vender como particular. Ejemplo (hipotético, cálculo mío): 1.000 € de plata sin IVA + 21 % = **1.210 €**; para recuperar lo pagado, el precio debería subir **21 %**, antes de primas y horquilla.
- **ETCs y ETNs**: son valores, no entregas de metal: **no llevan IVA** (G12 §3.5 [VERIFICAR]).

### 5.2 IRPF: ganancia patrimonial
- La venta de oro físico o de un ETC/ETN genera **ganancia o pérdida patrimonial** en la **base del ahorro** (G12 §3.1 y §3.5). Escala del ahorro: **19 %** hasta 6.000 €, **21 %** hasta 50.000 €, **23 %** hasta 200.000 €, etc. (G12 §1.5).
- **FIFO** si hay compras en varias fechas (G12 §3.1).
- **Ejemplo (hipotético, cálculo mío)**: una onza comprada hace años por **1.500 €** (con factura) y vendida a **4.000 €**: ganancia **2.500 €** → 19 % = **475 €**, sin otras rentas del ahorro, sin primas ni gastos.
- **Justificación del coste**: sin **factura o prueba** de lo pagado, el cálculo de la ganancia es discutible [VERIFICAR en AEAT/DGT cómo se acredita el coste de adquisición de oro sin justificante].
- **Retención**: el físico no lleva retención; un **ETC o ETN puede llevarla al reembolso**, un ETF no [G12 §3.2; DGT V0267-25 citada en G12; VERIFICAR].
- **Compensación de pérdidas** y **regla de los 2 meses** (G12 §4): igual que con acciones.

### 5.3 Impuesto sobre el Patrimonio y obligaciones informativas
- **Patrimonio** (G12 §7.1): los **bienes y derechos de valor económico** cuentan a **31-dic**, con mínimo exento de **700.000 €** si la comunidad no fija otro y bonificaciones autonómicas. **Cómo se valora el oro físico** (a precio de mercado a 31-dic, como los valores) [VERIFICAR en Ley 19/1991; no leído para esta guía].
- **Modelo 720** (G12 §9): 1-ene a 31-mar, **50.000 € por categoría** (cuentas, valores, inmuebles, seguros). Un **ETC o ETN custodiado en un bróker extranjero** entraría como **valores** [VERIFICAR]. **Metal físico guardado en una caja de seguridad en el extranjero**: no figura como categoría en la tabla de G12 §9 [VERIFICAR con un asesor; **no lo he comprobado**].
- **Custodia en el extranjero**: sin modelo 720 [pendiente de confirmar], hay riesgo de sanciones (G12 §9, régimen general de la LGT tras la Ley 5/2022 [VERIFICAR]).
- **Herencia**: el oro físico se hereda como cualquier bien; regla autonómica (G12 §8).

## 6. Riesgos
| Riesgo | Qué significa | Dónde aparece |
|---|---|---|
| **Volatilidad** | Caídas de **−42 %** (oro), **−72 %** (plata), **−89 %** (Brent, mensual) (§3) | Todas |
| **Contango y roll** | El producto pierde aunque el spot no cambie (§2.3) | Futuros |
| **Riesgo de contraparte (ETN)** | Si el emisor quiebra, pierdes aunque el metal suba | ETN |
| **Custodia física** | Robo, pérdida, falsificación; en ETC físico, el custodio | Físico y ETC |
| **Divisa** | Todo cotiza en **USD**. Con EUR/USD a 1,1193 (13-oct, G5), **1.000 USD = 893 €**; si el dólar pierde un 10 %, son **−81 €** sin que cambie el activo (G5 §5.4). Hay ETCs **con clase cubierta al euro** [VERIFICAR; la cobertura cuesta y no es perfecta] | Todas |
| **Liquidez y costes de venta** | Primas y horquillas del físico; horquillas en ETCs poco negociados (G5 §3.3) | Físico, ETC |
| **Apalancamiento** | Pérdida superior al capital (§2.4) | Futuros y CFD |
| **Riesgo de modelo/serie** | Mis cifras usan contratos continuos de Yahoo, **no LBMA** (§3.1) | Esta guía |
| **Riesgo regulatorio y fiscal** | Cambios del IVA o del IRPF (G12) | Todas |
| **Concentración** | Poner una gran parte del patrimonio en un solo activo sin flujos | Todas |

## 7. Comparación con renta fija, bolsa y cripto
Cifras de **10 años a 30-sep-2026**. **Las series no son homogéneas** (precio, rentabilidad bruta, futuros), así que la comparación es **orientativa**. Las filas de bolsa, renta fija y cripto **reutilizan G5 §9**.
| Activo | Rentabilidad anualizada 10 años | Volatilidad 10 años | Caída máxima de referencia | Fuente / nota |
|---|---|---|---|---|
| **Renta variable global (MSCI World, bruto USD)** | 13,37 % | 14,88 % | −57,46 % | MSCI (G5, primaria) |
| **S&P 500 (precio)** | 13,4 % | 15,3 % | −53 % | Yahoo (G5) |
| **IBEX 35 (precio)** | 7,6 % | 17,5 % | −62 % | Yahoo (G5) |
| **Oro (futuros COMEX, USD)** | 12,3 % | 15,2 % | −42 % (2011-2015) | Yahoo (G5: 12,3 % / 15,3 %; **coincide**) |
| **Plata (futuros COMEX, USD)** | 12,1 % | 31,4 % | −72 % (2011-2015) | Yahoo (cálculo mío) |
| **Cobre (futuros COMEX, USD)** | 11,5 % | 20,9 % | −65 % (2008) | Yahoo (cálculo mío) |
| **Brent spot (EIA, USD)** | 9,2 % | 55,9 % | −89 % (2008-2020, mensual) | EIA/FRED (primaria; punto final inflado por la crisis) |
| **Bitcoin (USD)** | 63,6 % (muy sesgada por el origen de la serie) | 68,6 % | −76 % (2017-2019) | Yahoo (G5) |
| **Renta fija del Estado español** | **No calculada** | Menor que la bolsa, no nula | Ver G4 §5 | Letra 12 m 3,026 %; obligación 10 años 3,964 % (17-sep-2026, Banco de España, G4) |
- **Cuidado con la lectura**: el oro **12,3 %/año** en dólares **no es** «la rentabilidad del oro para un inversor en euros»: el cambio EUR/USD **cambia** la cifra (§6).
- **Rentabilidad = precio**: no hay cupón ni dividendo; **el metal no paga**, mientras que MSCI World incluye dividendos (G5 §2.2).
- **No he comparado** la rentabilidad con la renta fija ni con la inflación para el mismo periodo salvo el IPC de EE. UU. (§3.2).
- **No puedo decir qué mezcla es «adecuada»** (G13, pendiente).

## 8. Datos actuales (13-oct-2026)
| Dato | Valor | Fecha / hora | Fuente | Nota |
|---|---|---|---|---|
| **Oro** (futuro COMEX, continuo) | **4.208,6 $/oz** | 13-oct-2026, ~14:37 Madrid | Yahoo (**secundaria**) [VERIFICAR en LBMA/CME] | **No es el fix LBMA**. Cierre 12-oct: 4.190,6 $ |
| **Plata** (futuro COMEX) | **60,49 $/oz** | 13-oct-2026, ~14:37 | Yahoo (secundaria) [VERIFICAR] | Cierre a 30-sep: 60,10 $ |
| **Ratio oro/plata** | **~69,6** | 13-oct | Cálculo mío (4.208,6 / 60,49) | No tengo la media histórica [VERIFICAR] |
| **Cobre** (futuro COMEX) | **6,74 $/lb** | 13-oct | Yahoo (secundaria) | |
| **Brent futuros** (continuo) | **~104,6 $** | 13-oct, ~14:36 | Yahoo (secundaria) | Dossier 11: 102-105 $ la semana anterior |
| **Brent spot (EIA)** | **125,44 $** | 6-oct-2026 (último dato disponible) | **EIA vía FRED (primaria, leída hoy)** | 135,51 $ el 2-oct; 114,82 $ el 1-oct |
| **WTI spot (EIA)** | **96,24 $** | 6-oct-2026 | EIA vía FRED (primaria) | |
| **Brent spot, media de septiembre** | **114,2 $** | sep-2026 | EIA/FRED (dossier 11, cálculo mío) | Máximo del año **138,21 $ (7-abr)**; mínimo **61,08 $ (7-ene)** |
| **Previsión EIA (STEO oct.)** | **105 $ (4T-26)** y **84 $ (2027)** | oct-2026 | EIA (dossier 11, primaria) | Se refiere al spot de la EIA |
| **Tipo real a 10 años (TIPS), EE. UU.** | **2,87 %** | 8-oct-2026 | **Tesoro vía FRED (DFII10, primaria, leído hoy)** | Era 2,95 % el 5-oct |
| **Bono del Tesoro a 10 años (nominal)** | **5,22 %** | 8-oct-2026 | Tesoro (dossier 8, primaria) | Máximo 2026: 5,31 % el 5-oct |
| **Tipos de la Fed** | **3,75-4,00 %** | Comunicado 16-sep | federalreserve.gov (G5, primaria) | |
| **EUR/USD** | 1,1193 | 13-oct | Yahoo (G5) | |
| **Oro: variación 2026 (a 30-sep)** | 4.341 $ (dic-25) → 4.187 $: **−3,6 %** | | Yahoo (cálculo mío) | |
| **Plata: variación 2026 (a 30-sep)** | 70,1 $ (dic-25) → 60,1 $: **−14,3 %** | | Yahoo (cálculo mío) | Un agregador citó un **máximo histórico de 118,45 $ (fix LBMA, 29-ene-2026)** [secundaria, **VERIFICAR**] |
| **Oro: variación en 12 meses (30-sep-2025 a 30-sep-2026)** | 3.873 $ → 4.187 $: **+8,1 %** | | Yahoo (cálculo mío) | |

**Contexto (hechos del dossier 11, secundarios salvo indicación)**
- **Guerra EE. UU./Israel–Irán desde el 28-feb-2026** (prensa/Wikipedia [VERIFICAR]); el **estrecho de Ormuz sigue casi cerrado**: el 27-sep, IMF PortWatch registró **1 tránsito** frente a unos **85 diarios** antes de la crisis.
- **G7**: acuerdo de **liberar hasta 100 M de barriles** en 4 meses (2-oct).
- **Spot frente a futuros**: el spot de la EIA (crudo físico) cotiza **muy por encima** de los futuros; no se comparan como iguales (dossier 11).
- **Lectura sobre oro y tipos reales** [observación mía, **no es ley**]: un tipo real del **2,87 %** es históricamente alto y, en teoría, desfavorable para el oro, y aun así el oro cotiza cerca de **4.200 $**. La relación inversa **no explica el nivel actual por sí sola**. [ESPECULACIÓN si se busca una causa].
- **Tipos y G1**: ver G1 para el estado de la inflación y los tipos.

## 9. Errores comunes y señales a vigilar
### 9.1 Errores comunes
1. **Confundir spot con futuros**: el Brent «a 125 $» (EIA) y el «a 104 $» (futuros) **no son el mismo precio** (§8).
2. **Comprar un ETC de futuros pensando que replica el precio al contado**: puede perder por contango (§2.3).
3. **Ignorar la prima y la horquilla del físico**: comprar y vender el mismo día cuesta (§2.1).
4. **Creer que el oro siempre protege de la inflación**: puede tardar décadas (§4.3).
5. **Olvidar el IVA de la plata** (§5.1).
6. **Confundir acciones mineras con el metal** (§2.5).
7. **Olvidar la divisa**: el precio en dólares no es tu rentabilidad en euros (§6).
8. **Perseguir el último pico**: la plata cayó **−72 %** en 2011-2015 tras un máximo; el Brent, **−82 %** de 2018 a 2020 (§3).
9. **Usar apalancamiento sin entenderlo** (§2.4).
10. **No guardar facturas**: se necesitan para justificar el coste fiscal (§5.2).
11. **Fiarse de rankings de «mejores ETCs» y de compradores de oro** de comparadores con enlaces de afiliación o de **tiendas de oro** [sesgo: conflicto de interés, tono promocional].
12. **Confiar en que un ETN es como un ETC físico**: el ETN es **deuda del emisor**.

### 9.2 Señales a vigilar (calendario; fechas del dossier 8 y 11 salvo indicación)
| Fecha | Evento | Por qué importa | Fuente |
|---|---|---|---|
| **14-oct** | IPC de EE. UU. (subyacente) | Inflación, expectativas de la Fed | Dossier 8 |
| **27-28-oct** | Fed (decisión) | Tipos y dólar | Dossier 8 |
| **28-29-oct** | BCE (conferencia el 29) | Tipos del euro y EUR/USD | Dossier 8 |
| **29-oct** | PCE de septiembre y PIB 3T (avance) | Indicador de inflación que sigue la Fed | BEA (dossier 8) |
| **1-nov** | **OPEP+** | Oferta de petróleo | Dossier 11 |
| **3-nov** | Elecciones de EE. UU. y fin de facto del compromiso de no atacar Irán | Geopolítica, petróleo | Dossier 11 |
| **Mensual** | **STEO de la EIA** (previsión Brent) | Si sube o baja la previsión de 105 $ | EIA [VERIFICAR fecha de noviembre] |
| **Mensual** | **Informe de mercado de petróleo de la AIE** | Oferta, demanda e inventarios | AIE [VERIFICAR fecha] |
| **Continuo** | Tránsitos diarios por Ormuz (PortWatch) | Si se reabre la ruta | Dossier 11 |
| **Trimestral** | World Gold Council: demanda de oro (compras de bancos centrales) | Un motor de demanda | WGC [VERIFICAR fecha del 3T] |
- **Otros**: curva de futuros del Brent (¿backwardation o contango?), prima del físico, tipo real a 10 años, dólar.

## 10. Hechos frente a opiniones
| Hechos (con fuente) | Opiniones o previsiones |
|---|---|
| Oro de inversión exento de IVA (BOE, art. 140 bis) | «El oro es refugio seguro» |
| Brent spot **125,44 $ el 6-oct** (EIA vía FRED) | «El petróleo bajará a 84 $ en 2027» (**es una previsión de la EIA**, no un hecho) |
| Tipo real a 10 años **2,87 %** (8-oct) | Que el oro «debería» caer por ello |
| Caída máxima del oro **−42 %** (2011-2015, mi serie) | Que «la plata seguirá subiendo» |
| El oro tardó **~45 años** en recuperar en términos reales su máximo de 1980 (cálculo mío, con un dato de 1980 de secundaria) | Que «dará lo mismo en el futuro» |

## 11. Lo que no sé / no he podido verificar
- **Precio oficial LBMA** de oro y plata: **no accesible** (licencia de ICE Benchmark Administration; la API devolvió bloqueo). Todos los precios del oro, plata, cobre y WTI son **futuros continuos de Yahoo** [VERIFICAR en LBMA/CME/WGC]. **El precio actual del oro y de la plata quedó sin verificar en primaria.**
- **Verificado en primaria hoy**: **(1)** texto del **IVA del oro de inversión** (arts. 140 y 140 bis del BOE); **(2)** **Brent spot** hasta el 6-oct (EIA vía FRED); **(3)** **tipo real a 10 años** (Tesoro vía FRED) y **IPC de EE. UU.** (BLS vía FRED).
- **IVA de la plata y tipo general vigente**: no confirmé el **21 %** en el art. 90 (la API mostró el texto histórico de 15 %).
- **Máximo del oro de 1980 (850 $)** y que no se superó en términos nominales hasta 2008: **memoria y secundarias**; el umbral real depende de ese dato.
- **Pureza y requisitos de monedas** de oro de inversión: leído el art. 140; **la lista anual del DOUE** no la he consultado.
- **Valoración del oro físico en el Impuesto sobre el Patrimonio** y **modelo 720 para metal físico en el extranjero**: no comprobado.
- **Retención y calificación fiscal exacta de ETC/ETN**: [VERIFICAR con AEAT/DGT] (G12).
- **Estudios sobre diversificación y cobertura de inflación**: **no los he leído**; los argumentos de §4.1 son **generales**.
- **Correlación de mineras y petroleras con el metal o con la bolsa**: no calculada.
- **Roll yield real de productos concretos** y **curva de futuros actual del Brent** (contango o backwardation): no medidos.
- **Rentabilidad de la renta fija en el mismo periodo**: no calculada aquí (G4).
- **Brent y WTI frente a IPC desde 1987**: no calculado.
- **Series de Yahoo**: faltan meses (§3.1) y los contratos continuos no son rentabilidad de un producto. **Volatilidad y caída máxima son aproximadas.**
- **Precios hoy a las ~14:37 (Madrid)**: sesión en curso.
- **Comisiones, primas y TER reales**: no consultadas; no recomiendo entidades ni productos.
- **IVA e impuestos de otras comunidades o países**: no analizados; los ejemplos fiscales son simplificados.

## 12. Guías relacionadas
- **G1** (tipos e inflación: tipos reales), **G4** (renta fija), **G5** (acciones, ETFs y fondos: costes, divisa, horquilla, KID) y **G12** (fiscalidad completa; §3.5 oro y commodities físicos, §7 Patrimonio, §9 modelo 720).
- **Dossier 8** (macro) y **dossier 11** (geopolítica, petróleo y BRICS); **dossier 13** (fiscalidad de XRP y XLM y ETFs de cripto).
- **Pendientes de la serie**: **G13** (gestión patrimonial).
