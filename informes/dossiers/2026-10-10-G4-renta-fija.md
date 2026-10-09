# Guía G4: Renta fija (España, 10-oct-2026)

> **Guía educativa, no es recomendación** de comprar, vender ni contratar ningún producto, bono, fondo, bróker o entidad. Foco en España, para un inversor particular a largo plazo. Fuentes **primarias leídas hoy**: **BOE** (resolución del Banco de España del 2-oct-2026 con el tipo de rendimiento del mercado secundario de deuda a 2-6 años; resolución de la Dirección General del Tesoro del 25-sep-2026 con las emisiones de octubre), **Banco de España** (ficha de la subasta de bonos y obligaciones del 1-oct y comunicación 38/26: condiciones de las subastas, mínimos, pagos y tarifas de la Cuenta Directa). **No pude abrir** tesoro.es ni elijo.tesoro.es (error de certificado/bloqueo en esta sesión): el resultado de las **Letras del 6-oct** viene de **prensa (secundaria)** y va con [VERIFICAR]. Fiscalidad, FOGAIN, ratings actuales y definiciones de productos proceden de **memoria o búsquedas secundarias**: van con [VERIFICAR] (AEAT/BOE/CNMV). Predicciones: [ESPECULACIÓN]. Los ejemplos numéricos son **ilustrativos y cálculo mío**. Complementa a [G1](2026-10-10-G1-tipos-e-inflacion.md), [G2](2026-10-10-G2-como-funciona-un-banco.md) y [G3](2026-10-10-G3-avales-garantias-hipotecas.md).

## 0. Resumen en 10 líneas
1. **Renta fija** = prestas dinero a un emisor (Estado, empresa, banco…) que se compromete a devolverte el nominal en una fecha y, normalmente, a pagarte intereses. "Fija" no significa "sin riesgo" ni "rentabilidad garantizada" si vendes antes.
2. **Precio y rentabilidad se mueven en sentido contrario**: si suben los tipos, baja el precio de los bonos ya emitidos (ejemplo en §3: un bono al 3 % a 5 años cae ~4,5 % si el mercado pasa a exigir 4 %).
3. **Duración** = sensibilidad al tipo. Regla práctica: un bono con duración 5 pierde ~5 % si los tipos suben 1 punto (§4).
4. Riesgos: **crédito, tipo de interés, inflación, liquidez, reinversión, divisa** (§5). El Estado español paga en euros y tiene riesgo de crédito bajo, no nulo.
5. **Datos de hoy**: Letras a 12 meses **3,026 %** (subasta 6-oct, máx. desde jul-2024, prensa); Obligación a 10 años (3,40 %, 2036) **3,964 %** el 17-sep y **~4,18 %** el 1-oct (marginal; el 17-sep es del Banco de España, el 1-oct viene de buscador [VERIFICAR]); tipo de rendimiento del mercado secundario a 2-6 años: **2,983 %** en septiembre (BOE/BdE) (§8).
6. **Corrección a G1**: G1 daba bono español ~3,7 % y bund ~3,3 %, y letra a 12 m 2,679 %. Las cifras primarias de hoy indican que **eran bajas** (§8.4).
7. En España se compra en **subasta del Tesoro** (mín. 1.000 €, petición no competitiva a precio medio), en **mercado secundario** (vía entidad/bróker) o con **fondos** (§6).
8. Fiscalidad: intereses y rendimiento implícito van a la **base del ahorro** (19-30 %); **las letras suelen no llevar retención**, los cupones de bonos sí [VERIFICAR]; un **fondo permite traspasar sin tributar**, comprar bonos directos no (§7).
9. Vigilar: **BCE 28-29 oct**, subastas de **letras 3 y 9 meses (13-oct)**, ratings (Morningstar DBRS 30-oct), IPC (§9).
10. Los datos son una foto del 10-oct-2026; nada aquí es consejo.

## 1. Glosario corto
| Término | Significado sencillo |
|---|---|
| **Nominal (valor facial)** | Lo que el emisor devuelve al vencimiento (p. ej. 1.000 €). |
| **Cupón** | Interés periódico, en % del nominal. Bono al 3,40 % = 34 € al año por cada 1.000 €. |
| **Precio** | Lo que pagas hoy, en % del nominal (100 = a la par; <100 = bajo la par; >100 = sobre la par). |
| **Cupón corrido** | Parte del cupón ya "devengada" desde el último pago; el comprador la paga al vendedor. |
| **TIR (rentabilidad al vencimiento)** | Rentabilidad anual total si compras hoy y mantienes hasta vencimiento, con cupones reinvertidos a la misma tasa. |
| **Tipo marginal / medio (subasta)** | Marginal = el del último precio aceptado (el menos atractivo adjudicado). Medio = promedio ponderado de lo adjudicado. |
| **Vencimiento / amortización** | Fecha en que se devuelve el nominal. |
| **Duración** | Plazo medio ponderado de cobro; mide sensibilidad al tipo (§4). |
| **Letra / bono / obligación** | Deuda del Estado: letras hasta 18 meses (sin cupón); bonos hasta 5 años; obligaciones más de 5 (con cupón). |
| **Bono indexado** | Su nominal y cupón se ajustan a la inflación (aquí, IPCA zona euro ex-tabaco). |
| **Rating** | Nota de solvencia de una agencia (S&P, Moody's, Fitch). |
| **Prima de riesgo** | Diferencia de rentabilidad con el bono alemán a 10 años (G1). |
| **Subordinada / perpetua** | Cobra después de otros acreedores / sin vencimiento. |
| **Base del ahorro** | Parte del IRPF donde tributan intereses y ganancias (G1, G12). |

## 2. Qué es la renta fija y quién emite
**Hechos**
- Un bono es un **préstamo troceado**: muchos inversores prestan al mismo emisor y reciben un título negociable.
- Emisores:
  | Emisor | Ejemplos | Riesgo de crédito (orientativo) |
  |---|---|---|
  | **Estado** | Letras, bonos, obligaciones del Tesoro | Bajo en España (ver §5); no existe "riesgo cero" |
  | **Comunidades autónomas y ayuntamientos** | Deuda autonómica | Medio; dependen del Estado (FLA) pero no son el Estado [VERIFICAR] |
  | **Empresas** | Bonos corporativos, pagarés | Desde bajo a muy alto según la empresa |
  | **Bancos** | Cédulas hipotecarias, deuda senior, subordinada, preferentes | Muy variable según el producto (§2.1) |
  | **Organismos supranacionales** | UE, BEI | Bajo |
- Orden de cobro si el emisor quiebra (simplificado): **garantías/cédulas → deuda senior → subordinada → preferentes/AT1 → acciones**. Es el mismo orden que usa la resolución bancaria (G2).

### 2.1 Productos y sus riesgos
| Producto | Qué es | Riesgos principales | ¿Cubre el FGD? |
|---|---|---|---|
| **Letras del Tesoro** | Deuda del Estado a 3, 6, 9, 12 meses (y hasta 18). **Sin cupón**: compras con descuento y cobras el nominal | Riesgo de tipo (menor, por ser corta); inflación | No (no es un depósito) |
| **Bonos y obligaciones del Estado** | Cupón anual; bonos a 3 y 5 años, obligaciones a 10, 15, 30 y 50 | Precio si vendes antes; inflación | No |
| **Bonos ligados a la inflación** | Obligaciones del Estado indexadas al **IPCA zona euro ex-tabaco**. Hay una emisión a 10 años **al 1,15 %, vto. 30-nov-2036**, que sigue ampliándose (BOE 28-sep-2026) | El cupón real es bajo; se ajusta con el índice de la UE, no con el IPC español; si hay deflación el ajuste del nominal tiene mecánica específica [VERIFICAR] | No |
| **Bonos corporativos** | Deuda de empresas; con rating o sin él | **Crédito (impago)**, liquidez, cláusulas de amortización anticipada | No |
| **Bonos verdes** | Fondos destinados a proyectos ambientales. España emitió su primer bono verde soberano en 2021 [VERIFICAR] | *Greenwashing*; suelen rendir algo menos ("greenium") [VERIFICAR]; el estándar europeo de bono verde es voluntario [VERIFICAR] | No |
| **Pagarés** | Deuda corta (hasta 18 meses) de empresas | **Impago**; poca liquidez; sin cobertura; algunos se negocian en MARF [VERIFICAR] | No |
| **Depósitos estructurados** | Depósito + derivado: parte o todo de la rentabilidad depende de un índice o cesta | Rentabilidad variable o nula; **penalización por cancelar**; complejidad; la garantía del capital depende del banco emisor | Sí, como depósito hasta 100.000 € **si el capital es depósito** [VERIFICAR] |
| **Participaciones preferentes / AT1 / CoCos** | Perpetuas, **subordinadas**, cupón **discrecional**, pueden **convertirse en acciones** o amortizarse con pérdidas | **Pérdida de capital**; sin vencimiento; riesgo de no cobrar cupón; mercado poco líquido | **No** |
- Las preferentes se comercializaron a minoristas en 2009-2012 y causaron graves pérdidas (hecho histórico; ver G2 para la resolución bancaria). Hoy se consideran **productos complejos** y la CNMV exige test de conveniencia y advertencias [VERIFICAR en CNMV].

## 3. Cómo funciona un bono
**Elementos**: nominal, cupón, precio, vencimiento, amortización (al vencimiento o escalonada), TIR.

**Ejemplo numérico (cálculo mío).** Bono de nominal **1.000 €**, cupón **3 %** anual, vence en **5 años**, comprado **a la par (1.000 €)**.
- Cobras **30 €** cada año durante 5 años y **1.000 €** al final. TIR = **3 %**.
- **Si los tipos de mercado suben al 4 %** (un bono nuevo similar paga 4 %): ¿cuánto vale el tuyo? Suma de flujos descontados al 4 %:
  - 30 × 4,4518 (factor de anualidad a 4 %, 5 años) = 133,6 €
  - 1.000 / 1,04⁵ = 821,9 €
  - **Precio ≈ 955,5 €** (−4,45 %).
- **Si los tipos bajan al 2 %**: 30 × 4,7135 = 141,4 € + 1.000 / 1,02⁵ = 905,7 € = **≈ 1.047,1 €** (+4,7 %).
- **Por qué se mueven al revés**: tu bono paga un 3 % fijo; si el mercado ofrece 4 %, nadie te lo compra por 1.000 €; el precio baja hasta que su rentabilidad (TIR) iguala el 4 %.
- **Si lo mantienes hasta el vencimiento** (y el emisor paga), cobras los 30 €/año y los 1.000 € pase lo que pase con el precio en medio. La pérdida solo se "materializa" si vendes antes o si el emisor falla.
- **Letras (sin cupón).** Ejemplo con el tipo de la subasta del 6-oct (3,026 % a 12 meses): precio ≈ 1.000 / 1,03026 ≈ **970,6 €** por cada 1.000 € de nominal. Si lo mantienes hasta vencimiento, cobras 1.000 €: ganancia bruta **29,4 €** (≈ **294 €** por cada 10.000 € de nominal) [cálculo aproximado; el Tesoro usa fórmulas exactas con días reales].
- Dos TIR distintas: la del **momento de compra** y la que tendrías si vendes antes. Un mismo bono puede dar ganancias o pérdidas según cuándo salgas.

## 4. Duración y sensibilidad a los tipos
- **Duración (de Macaulay)** = plazo medio, ponderado por el valor actual de los flujos, en que recuperas lo invertido. En el bono del §3, **≈ 4,7 años** (cálculo mío) para un vencimiento de 5.
- **Duración modificada** ≈ 4,6. Regla práctica: **variación aproximada del precio ≈ −duración modificada × variación del tipo**. Si los tipos suben 1 punto, el bono pierde ≈ 4,6 % (exacto en el ejemplo: −4,45 %, la diferencia se debe a la *convexidad*).
- Ejemplos de órdenes de magnitud (relación general, no cifras de un producto concreto): letra a 12 m ≈ 1; bono a 3 años ≈ 2,8; obligación a 10 años con cupón ~3-4 % ≈ 8; a 30 años ≈ 16-18 [cálculo/estimación mía; VERIFICAR con la ficha de cada producto].
- Un cupón más alto **reduce** la duración; un plazo más largo la **aumenta**.
- **Cuánta pérdida aguantar es una decisión personal.** Los bonos largos pueden perder mucho si los tipos suben fuerte (lo que ocurrió en 2022); ver el ciclo del BCE en G1 §8.

## 5. Riesgos
| Riesgo | Qué es | Cómo se ve | Matiz |
|---|---|---|---|
| **Crédito** | El emisor no paga o rebaja su nota | Rating, prima de riesgo, *spread* | Mayor rendimiento suele compensar mayor riesgo; no siempre compensa |
| **Tipo de interés** | Los tipos suben y el precio baja | Duración (§4) | Solo afecta si vendes antes (o a los fondos, que valoran a mercado cada día) |
| **Inflación** | El cupón fijo compra menos | Rentabilidad real (G1 §6) | Los bonos indexados lo mitigan, con matices |
| **Liquidez** | No encuentras comprador a buen precio | Horquilla compra-venta amplia | Deuda del Estado: mercado líquido; pequeña empresa o preferentes: poco |
| **Reinversión** | Al cobrar cupones o vencimiento, los tipos son más bajos | Rentabilidad futura menor que la TIR inicial | Es el reverso del riesgo de precio |
| **Divisa** | Bono en dólares u otra moneda | Tipo de cambio | Se elimina con bonos en euros o cobertura (que cuesta) |
| **Subordinación / complejidad** | Pierdes antes que otros acreedores | Estructura del título | Preferentes, AT1 |

**Escala de ratings** (S&P y Fitch / Moody's), de más a menos solvencia:
| Grado | S&P y Fitch | Moody's |
|---|---|---|
| Máximo | AAA | Aaa |
| Alto | AA+, AA, AA- | Aa1, Aa2, Aa3 |
| Medio-alto | A+, A, A- | A1, A2, A3 |
| Medio (último "grado de inversión") | BBB+, BBB, BBB- | Baa1, Baa2, Baa3 |
| Especulativo ("bono basura") | BB+ y menos | Ba1 y menos |
| Impago | D (S&P) / C (Fitch) | C |
- **España (referencia a principios de 2026, prensa)**: S&P **A+/estable**, Fitch **A/estable**, Moody's **A3/estable**, Scope **A/positiva** [VERIFICAR: hubo revisiones el 11-sep-2026 y no leí su resultado].
- Los ratings son **opiniones de agencias privadas**, con conflicto de interés potencial (las paga el emisor) y retrasos históricos (2008) [opinión extendida; VERIFICAR].

## 6. Cómo se compra en España
### 6.1 Subastas del Tesoro (mercado primario)
**Hechos (Banco de España, comunicación 38/26 y ficha de la subasta del 1-oct-2026)**
- Pueden participar personas físicas y jurídicas **residentes en España**. Mínimo **1.000 €** (múltiplos de 1.000 €).
- Dos tipos de petición:
  - **Competitiva**: tú fijas el precio (ex-cupón); si es inferior al corte, no se adjudica.
  - **No competitiva**: no fijas precio; te adjudican **al precio medio ponderado**. Se adjudican en su totalidad siempre que haya alguna competitiva aceptada. Máximo 5.000.000 € nominales por postor.
- Entrega a cuenta del **2 % del nominal** (o depósito previo); el resto se paga en la fecha de liquidación.
- Vías: **Cuenta Directa del Banco de España** (online con certificado/Cl@ve o presencial con cita previa; el justificante de IBAN debe coincidir con el titular) o una **entidad financiera** miembro del mercado primario.
- **Costes de la Cuenta Directa (BdE)**: comisión del **1,5 por mil** sobre las transferencias de efectivo que se originan **al amortizarse los bonos y al pagar cupones**, con **mínimo 0,90 € y máximo 200 €** (texto de la ficha; ver si existen exenciones para letras [VERIFICAR]). Otras tarifas por traslado de valores o custodia: consultar el cuadro vigente [VERIFICAR].
- **Calendario**: Letras a **6 y 12 meses** (martes, mensualmente; última: 6-oct); **3 y 9 meses**: **13-oct** (inscripción online hasta el 8-oct a las 14:00 [VERIFICAR]); bonos y obligaciones, en jueves según el calendario anual del BOE. El calendario se publica por resolución de enero (14-ene-2026).

**Tipos de subasta recientes**
| Fecha | Instrumento | Tipo marginal | Fuente |
|---|---|---|---|
| 1-sep-2026 | Letra 12 m | 2,846 % | Prensa [VERIFICAR] |
| 1-sep-2026 | Letra 6 m | 2,641 % | Prensa [VERIFICAR] |
| **6-oct-2026** | **Letra 12 m** | **3,026 %** (4.173,52 M€ adjudicados; demanda 5.693,91 M€) | Prensa [VERIFICAR en Tesoro] |
| **6-oct-2026** | **Letra 6 m** | **2,798 %** (2.297,11 M€; demanda 3.323,05 M€) | Prensa [VERIFICAR] |
| 17-sep-2026 | Oblig. 10 a. al 3,40 % (vto. 31-oct-2036) | **3,964 %** | Ficha BdE |
| 1-oct-2026 | Oblig. 10 a. al 3,40 % | **~4,176 %** | Buscador [VERIFICAR] |

### 6.2 Mercado secundario
- Compras/ventas de bonos ya emitidos, a través de tu entidad o bróker, en **AIAF** (renta fija) o centros de negociación europeos [VERIFICAR según producto]. El precio fluctúa cada día.
- Ventaja: eliges plazo y cupón; inconveniente: **comisiones de compraventa y custodia** de la entidad, horquilla compra-venta, y para importes pequeños los mínimos de negociación.

### 6.3 Bróker y fondos de renta fija
| Vía | Cómo funciona | Costes típicos (a comprobar, no recomendación) | Notas |
|---|---|---|---|
| **Cuenta Directa BdE / subasta** | Compras sin intermediarios | Comisión del 1,5 ‰ en cobros (arriba) | Solo deuda del Estado; no se pueden comprar bonos corporativos |
| **Entidad / bróker** | Compras en subasta o secundario | Comisión de compraventa + custodia; tarifas muy variables [VERIFICAR] | Mercado más amplio: corporativos, extranjeros |
| **Fondo de renta fija** | Participas en una cartera gestionada de muchos bonos | Comisión de gestión y gastos corrientes (TER), de pocas décimas a más de 1 % anual [VERIFICAR en el DFI/KID de cada fondo] | Sin vencimiento fijo; **el valor liquidativo sube y baja con los tipos**; diversificación y reembolso diario |
- **Diferencia clave**: un bono tiene **vencimiento** y devuelve el nominal si el emisor paga. Un fondo **no tiene vencimiento**: su duración se mantiene más o menos constante porque los bonos se renuevan, de modo que el riesgo de tipo no desaparece "con el tiempo" como en un bono individual. Existen fondos con **vencimiento objetivo** [VERIFICAR].
- **Protección**: los valores están a tu nombre en cuenta de la entidad, **segregados**; si la entidad quiebra, existe el **Fondo de Garantía de Inversiones (FOGAIN)** para reclamaciones por valores no restituidos (límite 100.000 € [VERIFICAR]). **No cubre pérdidas por mercado.** El Fondo de Garantía de Depósitos (G2) cubre depósitos, no bonos ni fondos.

## 7. Fiscalidad en España (resumen; ver G12 para la completa)
> Todo en [VERIFICAR] con la AEAT y la Ley 35/2006 (LIRPF) antes de usarlo en una declaración. Aquí va el esquema general.

**1) Tipos (base del ahorro)**: los de G1 §6 (19 %, 21 %, 23 %, 27 %, 30 % por tramos, a verificar).

**2) Letras del Tesoro** (rendimiento implícito)
- Ganancia = **nominal cobrado − precio pagado**. Es **rendimiento del capital mobiliario** y se declara en el año del **vencimiento o de la venta**, no mientras la tienes.
- **Normalmente sin retención** en letras del Tesoro [VERIFICAR el artículo del Reglamento del IRPF]. Aun así **hay que declararla**.
- Ejemplo (cálculo mío, 10.000 € de nominal al 3,026 %): ganancia bruta ≈ 294 €; al 19 % → 55,9 € de impuesto; **neto ≈ 238 €** (≈ 2,45 % sobre lo pagado). Con IPC del 4,9 % (G1) la **rentabilidad real neta ronda −2,4 %**.

**3) Bonos y obligaciones**
- **Cupón**: rendimiento del capital mobiliario; el cupón cobrado suele llevar **retención del 19 %** [VERIFICAR]. Ejemplo: cupón 34 € → 6,46 € de retención; neto 27,54 €.
- **Venta antes del vencimiento**: la **diferencia entre precio de venta y de compra** es **ganancia o pérdida patrimonial** (base del ahorro); la parte de **cupón corrido** que cobras al vender es rendimiento del capital mobiliario [VERIFICAR]. Para las **letras** (rendimiento implícito) la venta anticipada genera **rendimiento del capital mobiliario**, no ganancia patrimonial [VERIFICAR art. 25 LIRPF]. Esto matiza la idea habitual de que toda venta anticipada es "ganancia patrimonial".
- **Compensación**: las pérdidas patrimoniales y los rendimientos del capital mobiliario pueden compensarse **entre sí con un límite (25 %)** [VERIFICAR], y existe la **regla anti-aplicación de 2 meses** para pérdidas en valores homogéneos [VERIFICAR].
- **Ejemplo de venta con pérdida** (§3, cálculo mío): compras a 1.000 €, tipos al 4 %, vendes a 955,5 €: pérdida patrimonial ≈ 44,5 €, que se compensa con ganancias patrimoniales del año y, con límites, con otros rendimientos.

**4) Fondos de renta fija**
- **Traspaso entre fondos**: **no tributa** mientras el dinero pase de un fondo a otro (art. 94 LIRPF) [VERIFICAR]; tributa solo al **reembolso** (ganancia patrimonial en la base del ahorro, **método FIFO**), sin retención para residentes [VERIFICAR].
- **Bonos directos no tienen esta ventaja**: vender un bono y comprar otro tributa en el momento de la venta.
- Los intereses que genera el fondo **no tributan año a año** para el partícipe (el fondo tributa al 1 % [VERIFICAR]); el impuesto llega al reembolso. Es un diferimiento, no una exención.

**5) Otros productos**
- **Pagarés, bonos corporativos y depósitos estructurados**: rendimientos del capital mobiliario, con retención del 19 % habitualmente [VERIFICAR].
- **Patrimonio**: la deuda pública y los fondos computan en el Impuesto sobre el Patrimonio (según comunidad); G12.

**Hecho vs. opinión**: que los traspasos de fondos no tributen es un hecho normativo; que ello convenga a un inversor concreto depende de plazos, comisiones e impuestos, y es una decisión personal.

## 8. Datos actuales
### 8.1 Tabla (10-oct-2026)
| Dato | Valor | Fecha | Fuente |
|---|---|---|---|
| **Letra 12 m, tipo marginal** | **3,026 %** | 6-oct | Prensa sobre Tesoro [VERIFICAR] (máx. desde jul-2024) |
| Letra 6 m, tipo marginal | 2,798 % | 6-oct | Prensa [VERIFICAR] |
| **Oblig. 10 a. 3,40 % vto. 2036, tipo marginal** | **3,964 %** (17-sep); **~4,176 %** (1-oct) | sept-oct | **BdE** (17-sep); buscador (1-oct) [VERIFICAR] |
| **Rend. mercado secundario deuda 2-6 años** (tipo oficial) | **2,983 %** | media sept-2026 | **BOE / BdE** (resolución 2-oct, BOE-A-2026-20586) |
| Mismo índice, meses previos | ene 2,403; mar 2,488; jun 2,823; jul 2,848; ago 2,888 | 2026 | BOE (listado de buscador) [VERIFICAR] |
| Bono alemán 10 a. | **3,48 %** (9-oct) según un agregador; otras fuentes dan ~3,3 % | 9-oct | Agregadores [VERIFICAR en Bundesbank] |
| Prima de riesgo | **45 pb** (agregador); 49 pb el 25-sep (G1) | oct-2026 | Secundaria [VERIFICAR] |
| BCE, tipo de depósito | 2,50 % | desde 16-sep | BCE (G1) |
| IPC España (adelantado, sept.) | 4,9 % | 29-sep | INE (G1) |

### 8.2 Letras 12 m frente a depósitos e IPC
- **Letra 12 m (3,03 %) vs. IPC (4,9 %)**: rentabilidad real bruta ≈ **−1,8 %** (G1 §6). Los agregadores señalan que el 3 % queda por debajo de algunos depósitos del mercado (hecho de prensa) [VERIFICAR]; compararlo exige mirar impuestos, retenciones y garantías (G2).
- **Obligación a 10 años (~4,0-4,2 %)**: rentabilidad real bruta ≈ −0,7 % a −0,9 % con el IPC actual; con IPC a la baja, positiva. Esto es matemática, no predicción.

### 8.3 Prima de riesgo (cómo leerla)
- Con España ~4,18 % y una prima de 45-49 pb, el bund implícito sería ~3,7 %. Esto **no cuadra** con el 3,48 % del agregador, y el mismo agregador daba 3,71 % para España (que con ese bund implicaría ~23 pb, no 45). Las fuentes secundarias **no coinciden entre sí**; hay que consultar el **Banco de España** (tipo del bono a 10 años en el mercado secundario) y la **Bundesbank** [VERIFICAR].

### 8.4 Contraste con G1 (corrección)
| Cifra en G1 | Dato de hoy | Qué hacer |
|---|---|---|
| Letra 12 m **2,679 %** ("agosto") | Subasta 1-sep: **2,846 %**; **6-oct: 3,026 %** | G1 estaba **desfasada** (no contradice, pero ya no es la actual). Corregida. |
| Bono español 10 a. **~3,7 %** | **3,964 %** (17-sep, BdE) y ~4,18 % (1-oct) en subasta | La cifra de G1 parece **baja**: el rendimiento primario de subasta es más alto; el secundario puede diferir unos pb pero no 40-50 pb [VERIFICAR]. Corregida. |
| Bund 10 a. **~3,3 %** | 3,48 % (9-oct, agregador) | G1 parece **bajo**. [VERIFICAR] |
| Prima ~34 pb (otra: 49 pb) | 45-49 pb | La horquilla de 34 es la dudosa; usar 45-49 [VERIFICAR]. |
- Los tramos del IRPF de G1 no se han re-verificado aquí (siguen [VERIFICAR]).

## 9. Errores comunes y señales a vigilar
**Errores comunes**
1. **Creer que "renta fija = garantizado"**: garantizado solo si mantienes hasta vencimiento y el emisor paga (§3).
2. **Mirar solo el cupón** y no la TIR ni el precio (un bono con cupón alto puede cotizar bajo la par por riesgo de crédito).
3. **Comprar un producto complejo** (preferente, estructurado) pensando que es un depósito (§2.1).
4. **Ignorar la inflación y los impuestos**: el 3 % bruto no es el 3 % real (§7, §8.2).
5. **Confundir fondo con bono**: el fondo no tiene vencimiento (§6.3).
6. **Comprar a plazos largos por rentabilidad sin ver la duración** (§4).
7. **Perseguir el mayor rendimiento** sin ver el rating, la subordinación o la liquidez.
8. **Decidir por titulares**: usar la ficha del Tesoro/BdE y la CNMV como fuente.
9. **Suponer que las pérdidas por venta anticipada se compensan siempre sin límite** (§7).

**Señales a vigilar**
| Fecha | Evento | Qué mirar |
|---|---|---|
| **13-oct** | Subasta de **Letras a 3 y 9 meses** [VERIFICAR] | Si el tipo sigue subiendo |
| ~14-15-oct | **IPC definitivo** de septiembre (INE) [VERIFICAR] | Confirmación del 4,9 % |
| **28-29-oct** | **Reunión del BCE** | Si repite subida; efecto en la curva |
| **30-oct** | Revisión del rating de España por Morningstar DBRS [VERIFICAR, prensa] | Cambios de nota/perspectiva |
| Mediados de oct. y siguientes | Subastas de bonos y obligaciones (calendario anual del BOE) | Rendimiento marginal del 10 años |
| Principios de nov. | Subasta de Letras 6 y 12 meses | ¿Supera el 3 %? |
| Principios de nov. | Resolución del BdE con el rendimiento a 2-6 años de octubre (BOE) | Tendencia del tipo oficial |
- **Escenarios** [ESPECULACIÓN]: (A) el BCE pausa y los rendimientos se estabilizan; (B) más subidas por inflación energética y los bonos largos caen; (C) desaceleración y los rendimientos bajan. No hay forma fiable de saber cuál.

## 10. Lo que no sé / no he podido verificar
- **Resultados oficiales** de las subastas del 6-oct (Letras) y 1-oct (obligaciones): tesoro.es no se pudo abrir; las cifras son de prensa y buscador.
- **Rendimiento exacto del 10 años en secundario** y del **bund** a una fecha concreta, y la prima de riesgo (45 vs. 49 vs. 34 pb).
- **Ratings vigentes de España** tras las revisiones de septiembre.
- **Retención exacta** de letras y cupones de deuda pública, **límite de compensación (25 %)**, trato de la venta anticipada de letras, art. 94 de traspasos, tipo del 1 % del fondo, tramos del IRPF 2026.
- **Tarifas** de custodia/compraventa de entidades y bróker, y TER de los fondos.
- **FOGAIN** (cuantía y alcance), **bono verde soberano** (fecha/importe) y **mecánica de indexación** en deflación.
- Calendario completo de subastas de bonos de noviembre y diciembre (BOE, enero).

## 11. Guías relacionadas
[G1](2026-10-10-G1-tipos-e-inflacion.md) (tipos e inflación), [G2](2026-10-10-G2-como-funciona-un-banco.md) (banco, FGD, resolución), [G3](2026-10-10-G3-avales-garantias-hipotecas.md) (hipotecas), G5 (acciones, ETFs y fondos indexados), G12 (fiscalidad completa). Ver [MAPA](MAPA.md).
