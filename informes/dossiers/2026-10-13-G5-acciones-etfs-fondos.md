# Guía G5: Acciones, ETFs y fondos indexados (España, 13-oct-2026)

> **Guía educativa, no es recomendación** de comprar, vender ni contratar ninguna acción, fondo, ETF, bróker o entidad. Foco en España, para un inversor particular a largo plazo. Fuentes **primarias leídas hoy**: **BOE** (texto consolidado de la Ley 35/2006 del IRPF, arts. 80 y 94, descargado de la API del BOE), **MSCI** (ficha oficial del MSCI World a 30-sep-2026) y **STOXX** (página del Euro STOXX 50). **Secundarias**: Yahoo Finance (precios de índices y ETFs; no son datos oficiales del proveedor del índice), normas del IBEX 35 vía prensa y avisos de BME, justETF y ETFStream (sobre ETFs de EE. UU.). Lo no confirmado en fuente primaria va como **[VERIFICAR]**; las opiniones y previsiones, como **[ESPECULACIÓN]**. Los números de simulación son **cálculo mío con datos públicos** (método explicado en cada caso). **El pasado no garantiza el futuro.**

## 0. Resumen en 12 líneas
1. Una **acción** es una parte de una empresa; un **índice** es una cesta teórica que mide cómo se mueve un grupo de acciones. **No se puede comprar un índice**: se compra un fondo o ETF que lo copia (§2).
2. La mayoría de índices **ponderan por capitalización ajustada por *free float***: las empresas grandes pesan más. Eso concentra el riesgo en pocos valores (§2).
3. Formas de invertir: **acciones directas, fondos (activos o indexados), ETFs, ETCs/ETNs y planes** (§3). Un **ETF cotiza en bolsa** y se compra como una acción; un **fondo** se suscribe y reembolsa a su valor liquidativo.
4. **Coste**: el **TER** es lo que cobra el producto cada año; la **tracking difference** es lo que realmente se queda atrás del índice; a 30 años una diferencia de 1,3 puntos de comisión come **~31 %** del capital final en el ejemplo de §5.3.
5. **Datos oficiales**: MSCI World (rentabilidad bruta en USD) a 30-sep-2026: **+15,68 % en 1 año, 12,39 %/año en 5 años, 13,37 %/año en 10 años, 9,02 %/año desde 1987**; **caída máxima −57,46 %** (oct-2007 a mar-2009) (§11).
6. **Riesgo real**: una cartera de bolsa puede caer **la mitad**. El S&P 500 tardó **5 años y 5 meses** en recuperar su máximo de oct-2007 (cierres mensuales); el IBEX 35 (índice de precio) tardó **~18 años** en superar su máximo de sep-2007 (§5, §8).
7. **Divisa**: un ETF en dólares o con activos en dólares expone a EUR/USD. Con 1.000 USD a 1,1193, un dólar un 10 % más débil resta ~81 € (§5.4).
8. **Fiscalidad (resumen)**: ganancias y dividendos van a la **base del ahorro (19-30 %)**. Solo los **fondos de inversión** permiten **traspasar sin tributar**; el **BOE (art. 94 LIRPF) excluye expresamente a los ETFs cotizados** de ese diferimiento (§7).
9. **ETFs de EE. UU.**: suelen **no estar disponibles** para minoristas de la UE (falta del KID/PRIIPs) y además complican la fiscalidad y las obligaciones informativas (§4.3, §7.5).
10. **Aportaciones periódicas frente a entrada única**: en una simulación con el S&P 500 (2000-2026, precio), la entrada única **ganó en el 83 %** de las ventanas de 10 años, pero **perdió menos** la aportación periódica en las peores (§8.1). No hay estrategia que elimine el riesgo.
11. Errores típicos: perseguir lo que más subió, comisiones altas, concentración, vender en la caída, confundir ETF con fondo y olvidar la divisa (§10).
12. Los datos de §11 son una foto del 13-oct-2026; nada aquí es consejo.

## 1. Glosario corto
| Término | Significado sencillo |
|---|---|
| **Acción** | Título que representa una parte del capital de una sociedad. Da derecho a dividendos (si los hay) y a votar en junta. |
| **Índice** | Número que resume la evolución de un grupo de valores. No se compra directamente. |
| **Capitalización** | Precio × número de acciones. Valor de mercado de la empresa. |
| **Free float (capital flotante)** | Parte de las acciones que realmente cotiza libremente (sin contar participaciones estables). |
| **Índice de precio / de rentabilidad total (*total return*) / neto** | Precio: solo la variación de cotización. Total: reinvierte los dividendos. Neto: reinvierte dividendos descontando la retención de origen. |
| **Valor liquidativo (VL)** | Precio de una participación de un fondo, calculado una vez al día. |
| **ETF** | Fondo cotizado: se compra y vende en bolsa durante la sesión, como una acción. |
| **ETC / ETN** | Productos cotizados que siguen una materia prima o un índice; **no son fondos**: un ETN es deuda del emisor y asume su riesgo de crédito. |
| **UCITS** | Marco europeo de fondos armonizados (armonizados para venta a minoristas en la UE). |
| **Réplica física / sintética** | Física: el ETF compra las acciones del índice (o una muestra). Sintética: usa un derivado (*swap*) con una contraparte. |
| **TER (ratio de gastos totales)** | Coste anual del producto (gestión, administración…) en % del patrimonio. No incluye comisiones del bróker ni la horquilla. |
| **Tracking difference** | Rentabilidad del fondo menos la del índice en un periodo. Es lo que el inversor realmente "pierde" respecto al índice. |
| **Tracking error** | Volatilidad de esas diferencias; mide la irregularidad de la copia, no su coste. |
| **Horquilla (*spread*)** | Diferencia entre el precio de compra (ask) y de venta (bid). |
| **Liquidez** | Facilidad de comprar o vender sin mover el precio. |
| **Acumulación / distribución** | Acumulación: el fondo reinvierte los dividendos. Distribución: los paga al inversor. |
| **KID / DFI (PRIIPs)** | Documento de datos fundamentales (máx. 3 páginas) que el productor debe entregar a minoristas de la UE antes de la compra. |
| **Retención en origen** | Impuesto que el país de la empresa descuenta del dividendo antes de pagarlo. |
| **Base del ahorro** | Parte del IRPF donde tributan dividendos y ganancias de venta (19-30 %; G12). |
| **FIFO** | "Primero en entrar, primero en salir": al vender, se entienden vendidas las unidades más antiguas. |
| **Rebalanceo** | Volver a los pesos objetivo de la cartera tras subir o bajar unos activos más que otros. |
| **Caída máxima (*drawdown*)** | Mayor caída desde un máximo hasta el mínimo siguiente. |

## 2. Qué es una acción y qué es un índice
### 2.1 La acción
**Hechos**
- Comprar una acción te hace **propietario de una parte pequeña** de la empresa. Ganas por **subida del precio** y por **dividendos**; puedes perder **todo lo invertido** (no más, si compras al contado).
- Las acciones cobran **después** de los acreedores si la empresa quiebra (mismo orden que en G4: deuda antes que acciones).
- Una acción **no tiene vencimiento** ni rentabilidad garantizada.

### 2.2 Los índices más citados y qué miden
| Índice | Qué contiene | Cómo pondera | Fuente / estado |
|---|---|---|---|
| **IBEX 35** | 35 valores españoles líquidos, elegidos por un comité de BME | Capitalización × coeficiente de *free float*; **límite del 20 % por valor** y **40 % agregado** para bancos, energía y construcción (según avisos de BME) | Secundaria + avisos de BME [VERIFICAR en las normas técnicas de BME] |
| **S&P 500** | 500 grandes empresas de EE. UU. (no son "las 500 mayores" por regla mecánica: las elige un comité con criterios de tamaño, liquidez y rentabilidad) | Capitalización ajustada por *free float* | Descripción general [VERIFICAR en S&P DJI; su web devolvió 403 hoy] |
| **MSCI World** | **1.249** valores de gran y mediana capitalización de **23 países desarrollados** (sin emergentes); cubre ~85 % de la capitalización flotante de cada país | Capitalización ajustada por *free float* | **Primaria**: ficha MSCI a 30-sep-2026 |
| **Euro STOXX 50** | 50 grandes empresas de la zona euro | **Capitalización flotante, con tope del 10 % por valor** | **Primaria**: página STOXX (hoy) |

**Qué miden y qué no**
- **Miden** el comportamiento medio de un grupo de empresas, ponderado por tamaño.
- **No miden** "la economía del país" (el IBEX 35 incluye empresas con gran parte de su negocio fuera de España; el S&P 500 también); **no son una cartera diversificada por sí solos**; no incluyen costes de comprarlos.
- **Concentración**: en el Euro STOXX 50, los 10 mayores valores hoy incluyen ASML, Siemens, SAP, Banco Santander, TotalEnergies, Allianz, Schneider, Iberdrola, BBVA y Siemens Energy (fuente STOXX, hoy); pocos valores y sectores pesan mucho.
- **Índice de precio vs. total**: el **IBEX 35 habitual** y el **S&P 500 "de precio"** que muestra la prensa **no incluyen dividendos**. Ejemplo mío: el MSCI World bruto (con dividendos) da **13,37 %/año a 10 años**, y la serie de precio del ETF que lo copia en dólares (Yahoo, URTH) da **11,0 %/año**; la diferencia (~2 puntos) son dividendos, más costes y detalles de cada serie. **Compara siempre el mismo tipo de índice.**

### 2.3 Ejemplo numérico de capitalización
Tres empresas: A vale 600 M€, B 300 M€ y C 100 M€. Pesos: A 60 %, B 30 %, C 10 %. Si A sube un 10 % y las otras no se mueven: A = 660; total 1.060; peso de A = **62,3 %**. En un índice ponderado por capitalización, **lo que más ha subido pasa a pesar más**; no hace falta "rebalancear" porque el índice lo hace solo.

## 3. Formas de invertir
| Forma | Qué es | Ventajas | Inconvenientes | Fiscalidad (G12) |
|---|---|---|---|---|
| **Acciones directas** | Compras acciones de empresas concretas | Control total; sin comisión anual de gestión | **Concentración**; exige elegir y seguir | Dividendo: capital mobiliario (19 % retención en España); venta: ganancia patrimonial |
| **Fondo de inversión activo** | Un gestor elige valores para batir a un índice | Posibilidad de resultados distintos | **Comisiones altas** y muchos no baten a su índice [VERIFICAR con estudios de CNMV/ESMA] | **Traspaso sin tributar** entre fondos (art. 94 LIRPF) |
| **Fondo indexado** | Gestión pasiva que copia un índice | Bajo coste; **traspasable** | Su TER no es cero; puede quedarse algo atrás del índice | Igual que el anterior |
| **ETF** | Fondo cotizado que copia un índice | Cotiza en bolsa; TER bajo; amplia diversificación | Horquilla; comisión del bróker; **no permite traspaso sin tributar** | Se tributa al vender |
| **ETC / ETN** | Materias primas u otros índices | Acceso a oro, petróleo, etc. | **ETN: riesgo de crédito del emisor**; el ETC físico depende del custodio; calificación fiscal por confirmar | [VERIFICAR] (G12 §3.2) |
| **Planes de inversión / de pensiones** | Aportación periódica a un fondo o plan | Hábito de ahorro; algunos planes reducen la base (G12 §6.1) | Restricciones de rescate en pensiones | Ver G12 |

### 3.1 Réplica física y sintética
- **Física completa**: el ETF compra todas las acciones del índice en su proporción. **Física por muestreo**: compra una selección representativa (útil en índices muy amplios).
- **Sintética**: el ETF tiene una cesta de activos y un **swap** con un banco que le entrega la rentabilidad del índice. **Riesgo extra**: la contraparte (limitado por la normativa UCITS, [VERIFICAR el tope exacto]). Ventaja: puede copiar índices difíciles con menos error.
- Si el KID dice "réplica sintética", **léelo con calma**: aparece en la ficha del producto.

### 3.2 TER, tracking difference y tracking error (ejemplo)
- Un ETF con **TER 0,20 %** copia un índice que sube **10,00 %** en el año. El ETF ofrece **9,75 %**: su **tracking difference es −0,25 %** (TER 0,20 % + otros costes pequeños de reinversión, parcialmente compensados por ingresos como el préstamo de valores; supuesto mío).
- **Tracking error**: si cada mes la diferencia con el índice oscila ±0,03 %, el tracking error es bajo aunque el coste sea alto; **no confundas ambos conceptos**.
- Importa más la **tracking difference acumulada** que el TER nominal. Se consulta en el informe anual del fondo y en las fichas de datos del emisor.

### 3.3 Liquidez y horquilla (ejemplo)
- ETF cotizado a **100,00 (venta) / 100,05 (compra)**. Comprar y vender en el mismo momento pierde **0,05 por participación = 0,05 %**: sobre 10.000 € son **5 €**. En un ETF poco negociado, la horquilla puede ser 0,20 %: **20 €**.
- La liquidez de un ETF depende de la de **sus activos subyacentes**, no solo de su volumen; en caídas fuertes la horquilla puede ensancharse.
- Para ETFs, la bolsa cierra: **no puedes vender fuera del horario**. Un fondo se reembolsa a su VL del día (con un plazo de liquidación).

## 4. Cómo se compra en España
### 4.1 Brókers, bancos y mercados
**Hechos**
- Se compra a través de **un bróker o un banco** que sea miembro o tenga acceso a las bolsas. Las bolsas españolas las gestiona **BME**; también puedes comprar valores en **bolsas extranjeras** (NYSE, Nasdaq, Xetra, Euronext…) si tu intermediario las ofrece.
- **Comisiones típicas** (varían mucho; [VERIFICAR] en la tarifa pública de cada entidad):
  | Concepto | Qué es |
  |---|---|
  | **Compraventa** | Fija, porcentual o mixta, con mínimo; suele ser mayor en bolsas extranjeras |
  | **Custodia / administración** | Algunas entidades cobran por mantener valores; otras no |
  | **Cambio de divisa** | Margen o comisión si el activo está en otra moneda |
  | **Derechos de dividendo / otros** | Cargos por cobros o corporate actions [VERIFICAR] |
- Los **fondos** pueden comprarse en la gestora, el banco o plataformas de distribución; algunos bancos solo comercializan fondos propios.
- **Seguridad**: comprueba en el **registro de la CNMV** que la entidad esté autorizada; el **Fondo General de Garantía de Inversiones** protege contra la insolvencia del intermediario (hasta 100.000 € por inversor [VERIFICAR el límite vigente]). **No cubre pérdidas de mercado**.
- **Titularidad**: los valores están a tu nombre en el registro de la entidad; los de bróker extranjero pueden tener obligaciones informativas (modelo 720; ver G12 §9).

### 4.2 ETF UCITS europeo frente a ETF estadounidense
| Aspecto | **ETF UCITS (UE)** | **ETF de EE. UU.** |
|---|---|---|
| **Disponibilidad** | Se vende a minoristas de la UE | **Muchos brókers de la UE no lo permiten** por no tener KID |
| **KID/PRIIPs** | **Sí**, obligatorio | **No lo producen**; ver §4.3 |
| **Divisa de cotización** | EUR (o USD) según la bolsa | USD |
| **Distribución** | Hay de acumulación y de distribución | Casi siempre de distribución |
| **Fiscalidad en España** | Régimen de IIC (art. 94 LIRPF) [VERIFICAR para fondos extranjeros] | Ver §7.5 |

### 4.3 Por qué no se pueden comprar ETFs de EE. UU.
- El **Reglamento PRIIPs** exige que el productor entregue un **KID** a minoristas de la UE antes de la venta (la CNMV lo resume como un documento de **hasta 3 páginas**).
- Según ETFStream y justETF (secundarias), **los emisores de EE. UU. no han producido el KID**; entre las razones se cita el choque entre la exigencia de mostrar escenarios de rentabilidad futura y la normativa estadounidense. Si ya los tienes, **puedes mantenerlos o venderlos**, pero **no comprar más** en muchos brókers [VERIFICAR con tu entidad].
- **No es una prohibición legal de poseerlos**, es un requisito de venta a minoristas. Algunos brókers lo permiten a inversores profesionales o con otros requisitos [VERIFICAR].

## 5. Rentabilidad y riesgo
### 5.1 Qué dicen los datos históricos (método: cierres mensuales de Yahoo Finance, ventanas hasta el 30-sep-2026; fuente primaria de MSCI para el MSCI World)
| Índice | Rent. 10 años (anualizada) | Volatilidad 10 años | Caída máxima en el periodo disponible |
|---|---|---|---|
| **MSCI World (bruto, USD, MSCI)** | **13,37 %** | **14,88 %** | **−57,46 %** (2007-10 a 2009-03) |
| S&P 500 (precio, USD, Yahoo) | 13,4 % | 15,3 % | −53 % (cierres mensuales, 2007-10 a 2009-02) |
| IBEX 35 (precio, EUR, Yahoo) | 7,6 % | 17,5 % | −62 % (2007-09 a 2012-04) |
| Euro STOXX 50 (precio, EUR, Yahoo) | 7,3 % | 15,9 % | −56 % (2007-04 a 2009-01; serie desde 2007) |
- **Periodo**: cierres de 30-sep-2016 a 30-sep-2026 (10 años). **Volatilidad**: desviación típica anualizada de rentabilidades mensuales.
- **Importante**: son **cifras pasadas**. 10 años excepcionales para EE. UU. no se repiten por inercia [ESPECULACIÓN si se presentan como previsión].
- **Plazo largo**: 20 años (sep-2006 a sep-2026): **S&P 500 +473 % (9,1 %/año, precio)**; **IBEX 35 +38 % (1,6 %/año, precio)**. El IBEX está en niveles de ~19.000 puntos, pero **recuperó por primera vez el máximo mensual de sep-2007 en sep-2025** (cierres mensuales): casi 18 años.
- Un índice de precio **no incluye dividendos** y subestima la rentabilidad total, sobre todo en índices con mucho dividendo como el IBEX.

### 5.2 Diversificación
- Tener **muchas empresas** reduce el riesgo de una sola, no el del mercado entero: en 2008 casi todas las bolsas cayeron a la vez.
- Un MSCI World tiene 1.249 valores pero **una parte muy grande de EE. UU.** [VERIFICAR el peso exacto en la ficha de MSCI].
- **Diversificar** también es repartir **entre clases de activos** (bolsa, renta fija, liquidez) y **divisas**; ver §9.

### 5.3 Efecto de las comisiones (ejemplo numérico; cálculo mío)
Supuestos **hipotéticos, no previsión**: rentabilidad bruta **6 %/año** constante, antes de impuestos y sin inflación.
| Caso | TER 0,2 % | TER 1,5 % | Diferencia |
|---|---|---|---|
| **10.000 € a 20 años** | 30.883 € | 24.117 € | 6.765 € (**−21,9 %**) |
| **10.000 € a 30 años** | 54.271 € | 37.453 € | 16.818 € (**−31,0 %**) |
| **200 €/mes durante 20 años** (48.000 € aportados) | 88.684 € | 76.832 € | 11.852 € (−13,4 %) |
| **200 €/mes durante 30 años** (72.000 € aportados) | 188.012 € | 149.413 € | 38.599 € (−20,5 %) |
- Fórmula: capital = capital inicial × (1 + 6 % − TER)^años; en aportaciones, interés mensual equivalente y suma de cuotas.
- La comisión se cobra **aunque el mercado caiga**.

### 5.4 Riesgo de divisa (ejemplo)
- EUR/USD a **1,1193** (Yahoo, 13-oct-2026). **1.000 USD = 893,42 €**.
- Si el dólar pierde un 10 % frente al euro (EUR/USD a 1,2312), esos 1.000 USD = **812,20 €**: **−81 €** por el cambio, aunque el activo no se mueva en dólares.
- Un ETF de acciones de EE. UU. en euros **sigue expuesto al dólar** salvo que la clase esté **cubierta** (con un coste y un error de cobertura) [VERIFICAR en el KID].
- El riesgo de divisa puede restar o sumar; no es "gratis" eliminarlo.

## 6. Dividendos: reparto o acumulación, y retención en origen
### 6.1 Reparto o acumulación
- **Distribución**: cobras el dividendo y decides qué hacer. **Tributa cada año**, aunque lo reinviertas.
- **Acumulación**: el fondo/ETF lo reinvierte. En España, **un fondo de acumulación no tributa hasta que vendes** (la ganancia incluye lo acumulado), lo que **retrasa el impuesto** pero no lo elimina [VERIFICAR para ETFs extranjeros de acumulación en la práctica de la AEAT/DGT].
- **Compara**: a igualdad de índice y costes, la diferencia es **fiscal y de comodidad**, no de rentabilidad bruta.

### 6.2 Retención en origen y doble imposición
- Un dividendo de una empresa **extranjera** suele llevar **retención en el país de origen** (en el caso de EE. UU., **15 % con convenio y formulario W-8BEN**, 30 % sin él [VERIFICAR en la AEAT/IRS]).
- En España tributa **también** (19-30 %, base del ahorro). Para evitar pagar dos veces existe la **deducción por doble imposición internacional (art. 80 LIRPF, texto del BOE leído hoy)**: se deduce **la menor** de (a) lo efectivamente pagado fuera y (b) el tipo medio efectivo aplicado a esa renta en España.
- **Ejemplo (cálculo mío)**: dividendo bruto de EE. UU. 1.000 €; 15 % retenido (150 €). España 19 % = 190 €; deducción = menor de 150 € y 190 € = 150 €. **Pagas 40 € en España**; en total 190 €.
- **En ETFs UCITS con acciones de EE. UU.**: la retención de EE. UU. se aplica **a nivel del fondo** (según el domicilio del ETF y el convenio, [VERIFICAR]); como inversor **no puedes deducirla** porque no la pagaste tú. Es **un coste oculto** que se refleja en la rentabilidad del ETF.
- **Dividendo de empresa española**: retención de **19 %** (1.000 € brutos → 190 € retenidos, 810 € netos); es un **anticipo**, no el impuesto final (G12).
- **Brókers extranjeros**: pueden no retener; entonces **tú declaras** el dividendo en la renta y, si hay doble imposición, usas el art. 80 y la documentación de lo retenido.

## 7. Fiscalidad en España (resumen; ver G12 y dossier 13)
### 7.1 Acciones y ETFs cotizados
- **Venta**: ganancia o pérdida patrimonial = precio de venta − precio de compra − gastos. Va a la **base del ahorro**, con tarifa de **19 % a 30 %** (G12 §1).
- **FIFO**: si has comprado en varias fechas, se entiende vendido lo **más antiguo** (G12 §3.1, art. 37.2 leído en G12).
- **Ejemplo (cálculo mío)**: compras 10 unidades a 100 € y 10 a 120 €. Vendes 10 a 150 €. Se vende lo primero: ganancia = 10 × (150 − 100) = **500 €**. A 19 % = **95 €**.
- **Dividendos**: capital mobiliario, **retención 19 %** en España; **ETF de distribución** de un bróker español: [VERIFICAR retención] (G12 §2.1).
- **ETF**: no tiene retención al vender (el bróker no retiene; el inversor declara) [VERIFICAR; G12 §3.2].

### 7.2 Fondos de inversión
- **Traspaso**: el importe del reembolso se destina a **suscribir otro fondo** sin computar ganancia; las nuevas participaciones **conservan valor y fecha de adquisición** (art. 94.1.a LIRPF, BOE leído hoy).
- **Condiciones leídas en el BOE**: el diferimiento **no aplica** si el importe se pone **a disposición del contribuyente** por cualquier medio; en **sociedades de inversión (SICAV)**, solo con más de 500 socios y sin haber superado el 5 % del capital en los 12 meses anteriores.
- **Los ETFs (fondos de inversión cotizados) quedan fuera**: el propio art. 94 dice que **el diferimiento no se aplica cuando la transmisión o adquisición tenga por objeto participaciones de fondos cotizados** (leído hoy). **Vender un ETF para comprar otro tributa.**
- **Reembolso**: ganancia sobre las participaciones más antiguas (FIFO), con **retención del 19 %** de la gestora [VERIFICAR el tipo vigente].
- **Ejemplo (cálculo mío)**: 100 participaciones a 10 € y 100 a 15 €; reembolsas 150 a 20 €. Ganancia = 100 × 10 + 50 × 5 = **1.250 €**; impuesto a 19 % = 237,50 € (G12 §3.3).
- **Por qué importa**: el traspaso permite **cambiar de fondo, rebalancear y diversificar** sin pagar hasta el reembolso final. Eso es **una ventaja fiscal** frente al ETF, aunque su TER suele ser algo mayor [VERIFICAR comparando fichas].

### 7.3 Regla de los 2 meses y compensación de pérdidas
- **2 meses (art. 33.5 f))**: si vendes con pérdida valores cotizados y **compras valores homogéneos** 2 meses antes o después, **la pérdida no computa** hasta que vendas los nuevos (G12 §4.2). Para **fondos**, hay matices; consulta [VERIFICAR].
- **Compensación (art. 49)**: pérdidas contra ganancias del mismo año; el saldo negativo, contra rendimientos del capital mobiliario con **límite del 25 %**; lo no compensado se **arrastra 4 años** (G12 §4.1).

### 7.4 Obligaciones informativas
- Si mantienes valores en **un bróker extranjero**, puede haber obligación de declarar **modelo 720** (umbral por categoría, G12 §9) [VERIFICAR el umbral y el régimen actual].
- Algunos brókers europeos **informan a la AEAT**; otros no. **La obligación de declarar es tuya** aunque no te envíen resumen.

### 7.5 ETFs de EE. UU. y por qué suelen ser problemáticos
1. **Acceso**: muchos brókers de la UE no permiten comprarlos (§4.3).
2. **Régimen fiscal**: el art. 94 se refiere a instituciones reguladas en la Ley 35/2003 (leído hoy); un ETF de EE. UU. **no registrado en la CNMV** no encaja en el régimen de IIC y tributa **por las reglas generales** (dividendos como capital mobiliario con retención de 15 % en EE. UU. y deducción art. 80; venta como ganancia patrimonial) [VERIFICAR con la AEAT/DGT].
3. **Obligaciones**: custodia fuera de España → **modelo 720** y mayor carga de documentación.
4. **Riesgo de sucesión en EE. UU.**: se comenta que activos "situados en EE. UU." de no residentes pueden estar sujetos al **impuesto de sucesiones estadounidense** por encima de cierto umbral [VERIFICAR con un asesor; no he comprobado la norma vigente ni el convenio con España].
5. **Sin diferimiento**: igual que cualquier ETF (§7.2).

## 8. Estrategia (explicada, sin recomendar)
### 8.1 Aportaciones periódicas frente a entrada única (simulación mía)
**Método**: cierres mensuales del S&P 500 (índice **de precio**, USD, Yahoo) de ene-2000 a sep-2026. Para cada ventana de N meses: **entrada única** = invertir 1 al inicio y valorar al final; **aportación periódica (DCA)** = 1/N cada mes durante N meses; ambas valoradas al cierre del mes N, rentabilidad sobre lo aportado. Ventanas que se solapan (**no son independientes**); sin dividendos ni intereses del dinero aún no invertido.
| Horizonte | Ventanas | Entrada única mejor que DCA | Mediana DCA / entrada única | Peor caso DCA / entrada única |
|---|---|---|---|---|
| 12 meses | 309 | **71 %** | +6 % / +11 % | −35 % / −45 % |
| 5 años | 261 | **75 %** | +28 % / +56 % | −41 % / −36 % |
| 10 años | 201 | **83 %** | +65 % / +105 % | **−10 % / −31 %** |
| 15 años | 141 | **91 %** | +113 % / +188 % | +54 % / +30 % |
- **Lectura**: en mercados que suben de media, **tener el dinero invertido antes** suele rendir más (el DCA mantiene parte del dinero fuera). En el **peor** caso (empezar en ene-2000), el DCA perdió menos: **−7 % frente a −23 %** a 10 años; empezar en oct-2007 (justo antes de la crisis), DCA **+77 %** frente a **+66 %** de entrada única.
- **No es un fallo del método**: el DCA reduce el riesgo de "elegir mal el día" a costa de rentabilidad esperada si el mercado sube. **Elegir el momento perfecto no es posible a priori** [ESPECULACIÓN si se asegura lo contrario].
- Los 26 años incluyen **dos grandes caídas (2000-2002 y 2008)**; otros periodos darían otros números.

### 8.2 Horizonte temporal
- **Pérdidas en ventanas de entrada única** (S&P 500 de precio, mismo método): **21 %** de las ventanas de 5 años acabaron en negativo, **6 %** de las de 10 años y **0 %** de las de 15 años (la serie solo cubre 2000-2026; **no garantiza** que no ocurra en el futuro).
- **Recuperación de caídas** (cierres mensuales del S&P 500): máximo de oct-2007 (1.549) → mínimo de feb-2009 (735, **−53 %**) → recuperado en mar-2013 (**5 años y 5 meses** desde el máximo); máximo de ago-2000 (1.518) → mínimo de sep-2002 (815, −46 %) → recuperado en may-2007.
- **Regla práctica**: el dinero que **necesitarás en pocos años** no debería estar en renta variable. Esto es planificación, no recomendación de producto.

### 8.3 Rebalanceo
- **Ejemplo (cálculo mío)**: cartera 60 % bolsa / 40 % renta fija; la bolsa sube un 20 % y la renta fija no cambia. Bolsa = 72, renta fija = 40, total 112 → **64,3 % / 35,7 %**. Rebalancear es vender 4,8 de bolsa (de 72 a 67,2) y comprar renta fija (de 40 a 44,8) para volver a 60/40.
- **Fiscalidad**: con **fondos**, el rebalanceo mediante **traspaso no tributa**; con **ETFs o acciones**, **vender tributa**. Se puede rebalancear **con nuevas aportaciones** (dirigirlas a lo infraponderado) sin vender.
- Rebalancear **reduce el riesgo de desviarse** del objetivo; no es garantía de más rentabilidad.

### 8.4 Mercado alcista y bajista
- En un **mercado alcista**, las comisiones y el riesgo se olvidan; en uno **bajista**, la tentación es vender. Los datos de §8.2 muestran que **la caída puede durar años**.
- Un **−50 % exige +100 %** para volver al punto de partida (100 → 50 → 100): la caída pesa más que el rebote.

## 9. Comparación con renta fija y con cripto
| Activo | Rentabilidad histórica de referencia (10 años a 30-sep-2026) | Volatilidad 10 años | Caída máxima | Fuente / nota |
|---|---|---|---|---|
| **Renta variable global (MSCI World, bruto USD)** | 13,37 % | 14,88 % | −57,46 % | MSCI (primaria) |
| **S&P 500 (precio)** | 13,4 % | 15,3 % | −53 % | Yahoo (secundaria) |
| **IBEX 35 (precio)** | 7,6 % | 17,5 % | −62 % | Yahoo (secundaria) |
| **Oro (USD, contrato continuo)** | 12,3 % | 15,3 % | −42 % (2011-2015) | Yahoo (secundaria) |
| **Bitcoin (USD)** | 63,6 % (muy sesgada por el origen de la serie) | 68,6 % | −76 % (2017-2019) | Yahoo (secundaria) |
| **Renta fija del Estado español** | **No calculada aquí** | Menor que la bolsa, no nula | Ver G4 §5 | Rendimientos actuales en G4: letra 12 m 3,026 %; obligación 10 años 3,964 % (17-sep-2026, Banco de España) |
- **Interpretación**: una rentabilidad alta se pagó con **caídas profundas**. BTC es un activo **mucho más volátil**: −26,7 % en el último año, +91 % en 5 años (hasta 30-sep-2026); **XRP y XLM** están en riesgo similar o mayor [ESPECULACIÓN en cuanto a su futuro].
- **Renta fija**: el precio baja si suben los tipos (G4 §3-4), y a **plazos cortos** ofrece más estabilidad; **no existe activo sin riesgo** para todos los plazos.
- **No puedo decir qué mezcla es "adecuada"**: depende de tus objetivos, plazo y capacidad de aguantar caídas (G13, pendiente).

## 10. Errores comunes y señales a vigilar
1. **Perseguir la rentabilidad pasada**: lo que más subió en 10 años (EE. UU., tecnología, BTC) **no tiene por qué repetir**.
2. **Ignorar las comisiones** (§5.3): 1,3 puntos más al año restan ~31 % del capital en 30 años.
3. **Concentración**: pocas empresas, un solo sector o un solo país (el IBEX 35 está muy concentrado en bancos, energía y construcción por sus límites del 40 % agregado, [VERIFICAR]).
4. **Vender en la caída**: convierte una pérdida temporal en definitiva; el S&P 500 tardó 5 años y 5 meses en recuperar el máximo de 2007.
5. **Confundir ETF con fondo**: el ETF cotiza y **no permite traspaso sin tributar**; el fondo sí (§7.2).
6. **Olvidar la divisa** (§5.4) y **la retención en origen** (§6.2).
7. **Comparar índices de precio con índices de rentabilidad total**.
8. **Comprar un producto que no entiendes** (réplica sintética, ETN, apalancado o inverso): lee el **KID**.
9. **Hacer *market timing***: ningún dato aquí lo hace fiable.
10. **Fiarse de rankings de "mejores ETFs"** de agregadores o comparadores con enlaces de afiliación [sesgo de fuente: conflicto de interés, tono promocional].
- **Señales a vigilar**: TER y tracking difference en el KID; horquilla; domicilio y divisa del ETF; si es de acumulación o distribución; cambios fiscales (**G12**).

## 11. Datos actuales (13-oct-2026)
| Índice | Nivel | Fecha / hora | Fuente |
|---|---|---|---|
| **S&P 500** | **7.807,24** | cierre 12-oct-2026 | Yahoo (secundaria) [VERIFICAR en S&P DJI] |
| **IBEX 35** | **19.275** | 13-oct-2026, 14:23 aprox. hora de Madrid (sesión en curso) | Yahoo [VERIFICAR en BME] |
| **Euro STOXX 50** | **6.183** | 13-oct-2026, 14:23 aprox. (sesión en curso) | Yahoo [VERIFICAR en STOXX] |
| **MSCI World (bruto, USD)** | ficha a 30-sep-2026 | 30-sep-2026 | **MSCI (primaria)** |
| **EUR/USD** | 1,1193 | 13-oct-2026 | Yahoo |
| Rentabilidad YTD (30-sep-2026; precio, Yahoo) | S&P 500 **+11,8 %**; IBEX 35 **+6,4 %**; Euro STOXX 50 **+3,8 %**; MSCI World bruto **+12,09 %** (MSCI) | | |
| Rentab. 1 año (30-sep-2025 a 30-sep-2026) | S&P 500 **+14,4 %** (precio); IBEX **+18,7 %** (precio); Euro STOXX 50 **+9,0 %** (precio); MSCI World bruto **+15,68 %** (MSCI) | | |
| Fundamentales MSCI World | Rentab. por dividendo **1,52 %**; PER **22,69**; PER esperado **17,92**; P/VC **4,10** | 30-sep-2026 | MSCI (primaria) |
- **Aviso**: una valoración alta (PER 22,7) **no predice una caída** ni su fecha [ESPECULACIÓN si se interpreta como señal]. Es un dato descriptivo.
- **Comprobación cruzada**: la rentabilidad a 10 años del MSCI World en la ficha (13,37 %, bruta) y la serie de precio de Yahoo del ETF de MSCI World en dólares (11,0 %) difieren porque una incluye dividendos y la otra no.
- **Macro actual**: tipos de la Fed en 3,75-4,00 % (confirmado en federalreserve.gov, comunicado del 16-sep), petróleo cerca de 105 $, fuerte debilidad de altcoins en cripto esta semana (informe de apertura de hoy). **Contexto**, no señal.

## 12. Lo que no sé / no he podido verificar
- **S&P 500**: la web de S&P Dow Jones Indices dio **403**; los datos son de **Yahoo** y la descripción del índice es general [VERIFICAR en la ficha oficial].
- **IBEX 35**: no he podido abrir las **normas técnicas de BME**; el 20 % por valor, el 40 % sectorial y los coeficientes de *free float* provienen de prensa y avisos [VERIFICAR].
- **Peso de EE. UU. en el MSCI World** y la composición sectorial: **no leído** [VERIFICAR en la ficha completa].
- **Retención de ETFs de distribución en bróker español**, **calificación fiscal de ETCs/ETNs** y **de ETFs extranjeros de acumulación**: [VERIFICAR con la AEAT/DGT].
- **Comisiones de brókers y bancos**: no he consultado tarifas; no recomiendo entidades.
- **Impuesto de sucesiones de EE. UU. para residentes en España**: no comprobado.
- **Tope de exposición a contraparte en UCITS** y **límite del Fondo de Garantía de Inversiones** [VERIFICAR].
- **Renta fija: rentabilidad histórica** no calculada en esta guía (ver G4).
- **Dividendos del S&P 500 e IBEX 35** (rentabilidad total): no calculados.
- Simulaciones de §8: sin dividendos ni costes; solo 26 años de datos.

## 13. Guías relacionadas
- **G1** (tipos e inflación), **G4** (renta fija), **G12** (fiscalidad completa) y **dossier 13** (fiscalidad de XRP y XLM, ETFs de cripto).
- Pendientes de la serie: G13 (gestión patrimonial), G8, G9.
