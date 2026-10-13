# Guía G7: Derivados y apalancamiento: opciones, futuros, CFD y sus riesgos (España, 13-oct-2026)

> **Guía educativa, no es recomendación** de comprar, vender ni contratar ningún derivado, CFD, opción, futuro, ETF apalancado, bróker o entidad. Foco en España, para un inversor particular a largo plazo. Fuentes **primarias leídas hoy**: **BOE** (texto consolidado de la Ley 35/2006 del IRPF, arts. 33, 37, 45, 46, 49, 66 y 76, y del Reglamento del IRPF, art. 75, descargados de la API del BOE; **Resolución de la CNMV de 27-jun-2019** y **Resolución de la CNMV de 11-jul-2023** sobre medidas de intervención de producto; **Circular 1/2018** y **Circular 1/2022** de la CNMV, y la **Circular 1/2024**, que deroga la anterior; Reglamento (UE) 2023/1114, MiCA, en su versión del BOE/DOUE), **ESMA** (nota de prensa del 27-mar-2018 sobre sus medidas con CFD), **FRED** (VIX, serie VIXCLS, último dato 9-oct-2026), **BIS** (estadísticas de derivados OTC a jun-2025) y **FOGAIN** (fogain.com). **Matiz de lectura**: los textos del BOE de la LIRPF y del RIRPF los leí íntegros; las resoluciones y circulares de la CNMV, la nota de ESMA y la página de FOGAIN los leí con la herramienta de lectura web, que **devuelve resúmenes**, no el texto literal (por eso lo que depende de matices va como **[VERIFICAR el texto]**). **No pude abrir**: cnmv.es (error 403: listas de advertencias, notas y estadísticas), Directiva MiFID II y Reglamento PRIIPs (no abiertos), Reglamento Delegado 2017/653, consultas de la DGT, Real Decreto 1814/1991, Real Decreto 948/2001 (indemnización de inversores), AEAT (modelo 720), CME/Eurex, el boletín del BIS posterior a jun-2025. Lo no confirmado en fuente primaria va como **[VERIFICAR]**; las opiniones y previsiones, como **[ESPECULACIÓN]**. Todos los ejemplos numéricos son **hipotéticos y cálculo mío**, con método explicado. **El pasado no garantiza el futuro.**

## 0. Resumen en 12 líneas
1. Un **derivado** es un contrato cuyo valor depende de otro activo (el **subyacente**): se usa para **cubrir** un riesgo o para **especular** (§2).
2. **Apalancar** es controlar un valor grande con un depósito pequeño (**margen**). Amplifica ganancias **y pérdidas** por el mismo factor (§2).
3. **Futuro**: obligación de comprar o vender a un precio fijado, con **liquidación diaria** de ganancias y pérdidas. Ejemplo mío: nominal 50.000 € con margen de 5.000 € (10:1); el índice baja un 2 % y la pérdida es **1.000 € = 20 % del margen**; con **−10 %** se pierde el **100 %** del margen (§3).
4. **Opción**: un derecho (comprador) y una obligación (vendedor). El comprador pierde **como máximo la prima**; el vendedor de una **call descubierta** puede perder una cantidad **sin tope teórico** (§4).
5. Ejemplo mío de call: prima de 500 € por 100 acciones; con la acción en 110 € (+10 %) la opción gana **+100 %** de la prima; con la acción en 90 € o menos, **−100 %**. Un vendedor de esa call, con la acción en 200 €, pierde **9.500 €** (§4.5).
6. **CFD**: contrato con un bróker que replica el precio, sin ser dueño del activo. En la UE, para minoristas, **ESMA** y la **CNMV** fijaron: apalancamiento máximo **30:1** (divisas principales) hasta **2:1** (criptomonedas), **cierre forzoso al 50 % del margen** y **protección de saldo negativo** limitada a los fondos de la cuenta (§5).
7. El **coste oculto**: la financiación diaria. Ejemplo mío: en un CFD de 20.000 € con financiación del 5,5 % anual, mantenerlo un año cuesta **1.100 € = 110 % del margen** de 1.000 €, aunque el precio no se mueva (§5.4).
8. La **CNMV** prohíbe (Resolución de 11-jul-2023, en vigor desde el 3-ago-2023) la **publicidad** de CFD a minoristas y limita su marketing; la **Circular 1/2022** (publicidad de criptoactivos) **fue derogada el 28-dic-2024** por la Circular 1/2024, porque MiCA fija ya normas europeas (§5.7).
9. **ETF/ETN apalancados e inversos**: reajustan **cada día**. Ejemplo mío: un índice sube un 10 % y baja un 9,09 % (queda igual) y el **2x** acaba en **−1,82 %** (§7.3).
10. **MiCA no cubre derivados** que sean instrumentos financieros: esos productos dependen de **MiFID II** y de las reglas de la CNMV. Los **perpetuos** de exchanges offshore pueden quedar **fuera de las protecciones europeas** [VERIFICAR caso a caso] (§6).
11. **Fiscalidad**: ganancias y pérdidas de derivados suelen ir a la **base del ahorro** (19/21/23/27/30 % en la escala del BOE) [VERIFICAR el criterio de la DGT para CFD y forex]; el **art. 49** limita la compensación de pérdidas al **25 %** en el cruce con rendimientos del capital mobiliario (§8).
12. **FOGAIN** protege hasta **100.000 € por titular** si una entidad **quiebra y no devuelve** lo confiado; **no cubre pérdidas de mercado** ni operaciones con chiringuitos (§9). Datos del 13-oct: **VIX 14,84** (9-oct) y **846 billones de dólares** de nocional OTC a jun-2025 (BIS) (§10).

## 1. Glosario corto
| Término | Significado sencillo |
|---|---|
| **Derivado** | Contrato cuyo precio depende de un **subyacente** (acción, índice, divisa, materia prima, tipo de interés, cripto). |
| **Subyacente** | El activo del que depende el contrato. |
| **Cobertura (*hedging*)** | Uso del derivado para **reducir** un riesgo que ya se tiene. |
| **Especulación** | Uso del derivado para **tomar** un riesgo con la esperanza de ganar. |
| **Apalancamiento** | Nominal ÷ capital depositado. Con 10:1, una variación del 1 % del subyacente es un 10 % del capital depositado. |
| **Nominal (valor de la posición)** | Cantidad × precio × multiplicador. Es la **exposición real**, no el margen. |
| **Margen inicial** | Depósito exigido para abrir la posición (garantía, no «precio» del contrato). |
| **Margen de mantenimiento** | Nivel mínimo de fondos para mantenerla abierta. |
| **Llamada de margen (*margin call*)** | Aviso de que hay que **reponer fondos**. |
| **Liquidación forzosa (*stop out*, *close-out*)** | El bróker o el mercado **cierra** la posición si el saldo cae por debajo de un umbral. |
| **Liquidación diaria (*mark to market*)** | Cada día se abonan o cargan las ganancias y pérdidas del día en la cuenta. |
| **Futuro** | Obligación de comprar o vender a precio fijado y fecha futura. |
| **Opción *call* / *put*** | Derecho a comprar / vender el subyacente a un precio fijado (*strike*). |
| **Prima** | Precio que paga el comprador de una opción. |
| **Valor intrínseco / temporal** | Intrínseco: lo que valdría ejercerla hoy. Temporal: el resto de la prima, que se agota hacia el vencimiento. |
| **Estilo europeo / americano** | Europea: solo se ejerce al vencimiento. Americana: en cualquier momento hasta él. |
| **Griegas** | Sensibilidades del precio de la opción (delta, theta, vega…). |
| **CFD** | *Contract for difference*: contrato con un bróker sobre la diferencia de precio entre apertura y cierre. |
| **Spread** | Diferencia entre precio de compra y de venta. Es un coste. |
| **Financiación *overnight*** | Cargo o abono por mantener una posición apalancada de un día a otro. |
| **Perpetuo** | Contrato cripto **sin vencimiento**, con pagos periódicos de *funding rate* entre largos y cortos. |
| ***Funding rate*** | Pago periódico entre compradores y vendedores de un perpetuo para anclar su precio al contado. |
| **Producto complejo** | Concepto de MiFID II: exige evaluar **conveniencia** (o idoneidad si hay asesoramiento) [VERIFICAR texto de la Directiva]. |
| **KID / PRIIPs** | Documento de datos fundamentales para productos minoristas en la UE, con **indicador de riesgo (1 a 7)** [VERIFICAR el detalle del indicador; no abierto]. |
| **FOGAIN** | Fondo de Garantía de Inversiones: cubre hasta 100.000 € por titular si la entidad falla. |

## 2. Qué es un derivado y para qué se usa
### 2.1 Cobertura frente a especulación
| Uso | Ejemplo (descriptivo) | Resultado esperado |
|---|---|---|
| **Cobertura** | Una empresa que importa en dólares compra dólares a plazo para fijar su coste. Un inversor con acciones compra una *put* que le da derecho a vender a un precio fijo. | **Reduce** la incertidumbre; tiene coste (prima o renuncia a ganancia). |
| **Especulación** | Comprar una *call* sin tener la acción; abrir un CFD largo o corto sin tener el activo. | Gana si acierta la dirección **y el plazo**; puede perder más que lo que pone. |
| **Arbitraje** | Aprovechar diferencias de precio entre mercados (lo hacen profesionales). | Fuera del alcance de esta guía. |
- Los derivados existen porque trasladan riesgo de quien no lo quiere a quien lo asume. **El mismo producto** puede ser cobertura en manos de un hedger y especulación en las de otro.
- **Mercado**: los derivados de bolsa (futuros y opciones listados) los liquida una **cámara de compensación**, que reduce el riesgo de contraparte. Los **OTC** (a medida, p. ej. forex y CFD) dependen del emisor.

### 2.2 Apalancamiento, margen y liquidación
- **Apalancamiento = nominal ÷ capital depositado.** A 10:1, el activo tiene que moverse un **10 %** en contra para borrar el 100 % del depósito (si el bróker cierra a tiempo).
- **Es simétrico**: multiplica ganancias y pérdidas por el mismo factor, pero la pérdida de un depósito tiene **suelo en 100 %** (y, en futuros y opciones vendidas, puede **superarlo**, §7).
- **Llamada de margen**: el bróker pide fondos; si no se reponen, **cierra** la posición al precio de mercado, que puede ser peor que el esperado (**gap**, §7.1).
- **Stop out**: nivel fijado por el bróker o por la norma. En la UE, para CFD a minoristas, la norma fija el cierre al **50 % del margen inicial** (§5.2).

## 3. Futuros
### 3.1 Mecánica
| Elemento | Qué es |
|---|---|
| **Contrato** | Acuerdo estandarizado en un mercado organizado (CME, Eurex, MEFF…). Fija subyacente, tamaño, vencimiento y multiplicador. |
| **Multiplicador** | Euros (o dólares) por punto de índice o por unidad. Nominal = precio × multiplicador. |
| **Margen inicial** | Depósito exigido por el mercado y/o el bróker. Lo fija el mercado; puede **subir** en momentos de volatilidad. |
| **Liquidación diaria** | Cada día se abona o carga la ganancia o pérdida. Si el saldo cae por debajo del margen de mantenimiento: **llamada de margen**. |
| **Vencimiento** | Fecha de cierre. Puede ser **por diferencias** (efectivo, típico en índices) o **por entrega física** (típico en materias primas). Los futuros se suelen cerrar o **renovar** (*roll*) antes. |
| **Comprador (largo) / vendedor (corto)** | Ambos tienen **obligaciones**: el vendedor puede perder lo mismo que el comprador cuando el precio sube. |

### 3.2 Contango y backwardation (enlace con G9)
- El precio de un futuro no es una previsión del precio al contado: refleja **financiación y costes de almacenamiento** (y escasez presente, si la hay). Si el futuro lejano es **más caro** que el contado, hay **contango**; si es **más barato**, **backwardation**.
- Para un inversor que **renueva** futuros, el contango supone un coste por cada renovación (**roll yield**). **Ejemplo numérico completo: G9 §2.3** (con precio plano: −21,2 % en un año con contango del 2 % mensual, +27,4 % con backwardation). No lo repito aquí.
- **Nota**: en el futuro de **Brent** de hoy (~104,6 $) el **spot de la EIA** estaba en **125,44 $ el 6-oct** (G9 §8): **spot y futuro no son lo mismo**.

### 3.3 Ejemplo numérico: futuro sobre un índice (hipotético, cálculo mío)
**Supuestos**: índice en **5.000** puntos; multiplicador **10 €/punto** → nominal = 5.000 × 10 = **50.000 €**. Margen inicial **5.000 €** (10 %): apalancamiento **10:1**. Margen de mantenimiento ilustrativo **3.500 €** (70 % del inicial). Capital en cuenta: 5.000 €.
| Escenario | Variación del índice | Puntos | Resultado en € (puntos × 10) | Sobre los 5.000 € |
|---|---|---|---|---|
| Sube | **+2 %** | +100 | **+1.000 €** | **+20 %** |
| Baja | **−2 %** | −100 | **−1.000 €** | **−20 %** |
| Baja | **−10 %** | −500 | **−5.000 €** | **−100 %** (margen agotado) |
| Baja con salto (gap) | **−15 %** | −750 | **−7.500 €** | **−150 %**: saldo de **−2.500 €** a reponer |
- **Cuándo salta la llamada de margen**: se pierden 5.000 − 3.500 = **1.500 €** = 150 puntos = **−3 %** del índice.
- **Liquidación diaria (secuencia)**: día 1, índice **−1,5 %** (75 puntos): −750 €, saldo **4.250 €** (sobre 3.500: sin llamada). Día 2, **−2 %** sobre 4.925 (98,5 puntos): −985 €, saldo **3.265 €** (< 3.500): **llamada**. Para volver al margen inicial hay que aportar 5.000 − 3.265 = **1.735 €**. El índice acumula 173,5 puntos de baja (−3,47 %), coherente con 1.735 €.
- **Regla en España** (§5.2): la Resolución de la CNMV de 2023 aplica a futuros y opciones vendidos a minoristas un cierre de posiciones cuando los fondos caen por debajo de **la mitad del margen inicial** (en el ejemplo, **2.500 €**), y un margen inicial **no superior al menor entre el de 2019 y el del mercado** [VERIFICAR texto]. El mantenimiento de 3.500 € es solo ilustrativo.
- **Vencimiento**: el contrato se cierra o se **renueva**; con renovación se paga la diferencia entre contratos y comisiones.
- **Futuros sobre materias primas**: puede haber **entrega física** (barriles, metal) si no se cierra a tiempo; los brókers minoristas suelen cerrar antes [VERIFICAR condiciones de cada bróker].

## 4. Opciones
### 4.1 Conceptos
| Elemento | Qué es |
|---|---|
| **Call** | Derecho a **comprar** el subyacente al *strike*. Gana valor cuando el subyacente **sube**. |
| **Put** | Derecho a **vender** al *strike*. Gana valor cuando el subyacente **baja**. |
| **Prima** | Lo que paga el comprador al vendedor. **No se devuelve.** |
| **Strike** | Precio al que se ejerce. |
| **Vencimiento** | Fecha límite. Después, la opción **vale cero**. |
| **Valor intrínseco** | Call: máx(S − K, 0). Put: máx(K − S, 0). |
| **Valor temporal** | Prima − valor intrínseco. Se **erosiona** con el tiempo. |
| **Ejercicio** | Hacer valer el derecho. En muchos contratos de índice se liquida **por diferencias**. |
| **Estilo europeo / americano** | Europea: ejercicio solo al vencimiento. Americana: en cualquier momento. Las de acciones de EE. UU. suelen ser americanas; las de índices, europeas [VERIFICAR por contrato]. |

### 4.2 Griegas en una línea cada una
- **Delta**: cuánto cambia la prima por cada unidad que se mueve el subyacente (call entre 0 y 1; put entre −1 y 0).
- **Gamma**: cuánto cambia la delta cuando se mueve el subyacente.
- **Theta**: cuánto valor temporal pierde la opción **por día** (suele ser negativa para el comprador).
- **Vega**: cuánto cambia la prima si cambia la **volatilidad implícita**.
- **Rho**: sensibilidad al tipo de interés (menor importancia en opciones cortas).

### 4.3 Pérdida máxima y riesgo según la posición
| Posición | Ganancia máxima | Pérdida máxima |
|---|---|---|
| **Comprar call** | Ilimitada (teórica) | **La prima** |
| **Comprar put** | Strike − prima (si el subyacente llega a 0) | **La prima** |
| **Vender call descubierta** | La prima cobrada | **Sin tope teórico** (el subyacente puede subir sin límite) |
| **Vender put** | La prima | **Strike − prima** por unidad (el subyacente llega a 0): grande pero acotada |
| **Vender call cubierta** (se tiene el subyacente) | Prima + subida hasta el *strike* | Se renuncia a la subida por encima del *strike* y se sigue expuesto a la caída |
- El **vendedor** cobra la prima por **asumir riesgo**; suele exigir margen y puede sufrir llamadas de margen.

### 4.4 Valor intrínseco y temporal (ejemplo)
Acción en **103 €**, *call* con *strike* **100 €** y prima **6 €**: valor intrínseco = 103 − 100 = **3 €**; valor temporal = 6 − 3 = **3 €**. Al vencimiento, el valor temporal es **0**: si la acción sigue en 103, la opción vale **3 €** y el comprador pierde 3 € de los 6 pagados.

### 4.5 Ejemplo numérico: comprar una call (hipotético, cálculo mío)
**Supuestos**: acción en **100 €**; *call* europea con *strike* **100 €**, vencimiento a 3 meses, prima **5 €**; cada contrato cubre **100 acciones** → prima total **500 €**. **Punto de equilibrio** = *strike* + prima = **105 €**.
| Precio al vencimiento | Valor de la opción (por acción) | Resultado del comprador (× 100) | Sobre la prima (500 €) | Vendedor |
|---|---|---|---|---|
| **90 €** | 0 | **−500 €** | **−100 %** | **+500 €** |
| **100 €** | 0 | **−500 €** | **−100 %** | **+500 €** |
| **105 €** | 5 | **0 €** | 0 % | 0 € |
| **110 €** | 10 | 10 − 5 = 5 → **+500 €** | **+100 %** | **−500 €** |
| **120 €** | 20 | 20 − 5 = 15 → **+1.500 €** | **+300 %** | **−1.500 €** |
| **200 €** | 100 | 100 − 5 = 95 → **+9.500 €** | **+1.900 %** | **−9.500 €** |
- **Comparación con comprar las acciones**: 100 acciones cuestan **10.000 €**. Con la acción en **110 €** (+10 %), las acciones ganan **1.000 € (+10 %)** y la opción **+500 € (+100 % de la prima)**. Con la acción en **90 €** (−10 %), las acciones pierden **1.000 € (−10 %)** y la opción **−500 € (−100 % de la prima)**. Es **apalancamiento por prima**, con **pérdida limitada a la prima**.
- **El tiempo juega en contra del comprador**: si la acción se queda en **104 €** (+4 %) en el vencimiento, la opción vale 4 € y el comprador pierde **1 €** por acción (**−100 €**), porque la subida no superó el equilibrio.
- **Vendedor de la *call* descubierta**: cobra **500 €**; si la acción llega a **200 €** pierde **9.500 €**, y a **400 €**, **29.500 €** (cálculo: (400 − 100 − 5) × 100). **No hay límite teórico.**
- **Put comprada** (prima **4 €**, *strike* 100 €, equilibrio 96 €): con la acción en **90 €**, valor 10 − 4 = **+600 €**; con la acción en **0**, **+9.600 €** (máximo); con la acción en **100 €** o más, **−400 €**. El vendedor de esa *put* cobra **400 €** y, si la acción llega a 0, pierde **9.600 €**.
- **Uso en cobertura** (descriptivo): quien tiene 100 acciones y compra una *put* de *strike* 100 € paga la prima; si la acción cae, la *put* compensa la caída por debajo del *strike*, con el **coste de la prima** como «seguro». Un inversor cubierto no obtiene la subida completa.

### 4.6 Warrants, certificados y productos estructurados (nota breve)
- **Warrant**: opción emitida por una entidad financiera y cotizada. Es un **instrumento al portador del riesgo de crédito del emisor**.
- **Certificados** (*turbos*, *bonus*, etc.): productos estructurados que replican un subyacente con o sin apalancamiento y a veces con **barrera**; si se toca la barrera, pueden **perder todo el valor**.
- **Riesgo de emisor**: si el emisor quiebra, el inversor puede perder aunque el subyacente suba. Es la diferencia clave con una opción de mercado organizado respaldada por una cámara. [VERIFICAR características concretas en el KID de cada producto; **no he leído ningún folleto**.]
- La CNMV incluye entre los productos «especialmente complejos» los **CFD y las opciones binarias** (Circular 1/2018, §5.7).

## 5. CFD y forex apalancado
### 5.1 Qué son
- **CFD**: contrato con un bróker que paga (o cobra) la diferencia entre el precio de apertura y de cierre. **No se posee el activo.** Permite **posiciones cortas** y apalancamiento.
- **Forex apalancado**: operar pares de divisas con apalancamiento (la CNMV incluye en «CFD» los contratos de divisas al contado, *rolling spot forex*, según la nota de la Resolución de 2023 [VERIFICAR texto]).
- **Dónde se ejecuta**: casi siempre **OTC con el propio bróker** (puede ser la contraparte). La CNMV describe un modelo en que las ganancias del cliente son pérdidas del bróker y se genera un **conflicto de interés** (comentario del Comité Consultivo de la CNMV, 2023 [secundaria, borrador]).

### 5.2 Límites de la UE y de España para clientes minoristas
**Origen**: ESMA adoptó medidas **temporales** (acordadas el 23-mar-2018 y anunciadas el 27-mar-2018; ESMA solo puede imponerlas por periodos de **3 meses** renovables). Después, la **CNMV** adoptó medidas **permanentes** nacionales con la **Resolución de 27-jun-2019** (BOE nº 155, 29-jun-2019), vigente desde el **1-ago-2019** (CFD) y el **2-jul-2019** (opciones binarias, **prohibidas a minoristas**). Seguimiento en la **Resolución de 11-jul-2023** (BOE-A-2023-16394).
| Subyacente | Apalancamiento máximo | Margen inicial (% del nominal) |
|---|---|---|
| Pares principales de divisas | **30:1** | 3,33 % |
| Otros pares de divisas, oro, índices bursátiles principales (FTSE 100, S&P 500, DAX…) | **20:1** | 5 % |
| Materias primas distintas del oro, índices no principales | **10:1** | 10 % |
| Acciones y otros subyacentes | **5:1** | 20 % |
| **Criptomonedas** | **2:1** | **50 %** |
- **Cierre forzoso (*close-out*)**: el proveedor debe cerrar una o más posiciones cuando los fondos más las ganancias latentes caen a **la mitad del margen inicial total** (50 %).
- **Protección de saldo negativo**: la pérdida total del cliente minorista en CFD queda **limitada a los fondos de esa cuenta**. Ojo: no limita la pérdida al margen de una posición, sino a **todo lo depositado en la cuenta**.
- **Prohibición de incentivos**: no pueden ofrecerse **beneficios monetarios ni no monetarios** ligados a la comercialización del CFD (salvo información y herramientas de análisis).
- **Aviso de riesgo**: en toda comunicación comercial, con la **proporción de cuentas minoristas que pierden** dinero con ese proveedor (actualizada trimestralmente, según el resumen de la Resolución de 2019 [VERIFICAR texto]). La nota de ESMA de 2018 citó que **entre un 74 % y un 89 %** de las cuentas minoristas de CFD solían perder dinero, según el análisis de las autoridades.
- **Quién queda fuera**: los **clientes profesionales** (por solicitud y requisitos) pueden operar con mayor apalancamiento [VERIFICAR requisitos MiFID II, no abiertos].
- **Ámbito**: las medidas de la CNMV se aplican a clientes **minoristas residentes en España**, con independencia del país del proveedor (los CFD de proveedores con sede en otro país de la UE incluidos).

### 5.3 Resolución de 2023: publicidad y otros productos apalancados
La **Resolución de 11-jul-2023** (BOE 14-jul-2023, en vigor **3-ago-2023**; revisable anualmente) establece, según la lectura:
| Parte | Contenido |
|---|---|
| **CFD (Parte primera)** | **Prohíbe la publicidad** dirigida a minoristas o al público general (incluida la que lleva a una web que ofrezca estos productos); prohíbe **patrocinios y publicidad de marca** (con excepción si la actividad es muy reducida respecto al total de la entidad); prohíbe **formación gratuita o a precio simbólico y cuentas demo** dirigidas al público; restringe **remuneraciones** (comisiones por captar clientes, pagos ligados a depósitos o pérdidas, *call centers*); **prohíbe el ingreso con tarjeta de crédito**. |
| **Otros productos apalancados (Parte segunda)** | Se aplica a los instrumentos cuyo **riesgo máximo se desconoce** al contratar o cuyo **potencial de pérdida supera el desembolso inicial** (futuros y opciones, entre ellos): **margen inicial** y **cierre de posiciones** al caer los fondos por debajo de la **mitad** del margen inicial. **No** incluye las prohibiciones de publicidad y remuneración. |
- [VERIFICAR el texto íntegro de cada punto; la lectura fue un resumen.]

### 5.4 Costes: spread y financiación overnight (ejemplo)
**Supuestos (hipotéticos, cálculo mío)**: CFD sobre un índice principal con nominal **20.000 €** y margen del **5 % = 1.000 €** (20:1). Spread del **0,05 %** del nominal. Financiación: referencia **3 %** + recargo del bróker **2,5 %** = **5,5 %** anual, base 360 días.
- **Spread**: 20.000 × 0,05 % = **10 €** (1 % del margen) solo por entrar y salir.
- **Financiación diaria**: 20.000 × 5,5 % ÷ 360 = **3,06 €/día**.
- **En un año con el precio plano**: 3,06 × 360 = **1.100 €**, es decir, **110 % del margen** de 1.000 €. Un CFD mantenido largo tiempo **paga un coste** equivalente a un préstamo caro; por eso el CFD está diseñado para posiciones **cortas en el tiempo**.
- En **posiciones cortas** la financiación puede ser de signo contrario, según el bróker y el activo [VERIFICAR en cada bróker].
- **Dividendos**: el CFD sobre una acción abona o carga un ajuste equivalente al dividendo [VERIFICAR mecánica de cada bróker].

### 5.5 Ejemplo numérico: cierre forzoso (hipotético, cálculo mío)
**Mismos supuestos**: nominal **20.000 €**, margen **1.000 €**, cuenta con **1.000 €**.
| Variación del índice | Resultado | Fondos | Qué ocurre |
|---|---|---|---|
| **−1 %** | −200 € | 800 € | Sigue abierta |
| **−2,5 %** | −500 € | 500 € | **Cierre forzoso al 50 %** del margen: se pierden **500 € (−50 %)** |
| **−5 %** | −1.000 € | 0 | Habría agotado el capital si no cerrara antes |
| **Salto de −7 %** (noche, fin de semana) | −1.400 € nominales | 0 | El cierre llega **después** del salto. Con **protección de saldo negativo**, la pérdida del cliente queda en los **1.000 €** de la cuenta; los 400 € restantes los absorbe el bróker. |
- Si el cliente tiene **más dinero en la cuenta** que el margen, **todo ese saldo** queda expuesto a la pérdida.
- La protección **no existe** para clientes **profesionales**, ni en brókers **fuera de la UE** sin esa norma [VERIFICAR].

### 5.6 Riesgo de contraparte y de ejecución
- **Contraparte**: si el bróker (que es la contraparte OTC) quiebra, el reclamo es contra él. El **FOGAIN** cubre solo **el no reembolso** de fondos confiados a entidades adheridas (§9).
- **Ejecución**: **deslizamiento** (*slippage*) en momentos rápidos, **requotes** y precios que el bróker fija. La CNMV ha observado **infracciones** como falta de evaluación de conveniencia, publicidad engañosa y desconocimiento de costes implícitos (Comité Consultivo, 2023 [secundaria]).
- **Información al cliente**: la **Circular 1/2018** de la CNMV (BOE-A-2018-4247, en vigor desde el 27-jun-2018; Norma cuarta modificada por la Circular 2/2025) exige una **advertencia firmada** al comprar productos «especialmente complejos», entre ellos **CFD y opciones binarias**: el cliente debe escribir de su puño y letra «Producto difícil de entender. La CNMV considera que, en general, no es conveniente para inversores minoristas» (según la lectura [VERIFICAR texto]).

### 5.7 Restricciones de publicidad de la CNMV (qué vale hoy)
| Norma | Alcance | Estado |
|---|---|---|
| **Resolución de 11-jul-2023** | **Publicidad de CFD** a minoristas, patrocinios, formación, remuneraciones, tarjetas de crédito | **Vigente** (revisable anualmente) [VERIFICAR si hubo cambios posteriores] |
| **Circular 1/2022** (BOE-A-2022-666) | Publicidad de **criptoactivos** presentados como inversión (no CFD: «no menciona los CFD») | **Derogada el 28-dic-2024** por la Circular 1/2024 (BOE 27-dic-2024) por **MiCA** (Reglamento 2023/1114) |
| **Circular 1/2018** | Advertencias en productos complejos | **Vigente**, con modificaciones |
- **Matiz importante**: la Circular 1/2022 **no era una norma de CFD**: era de **criptoactivos**. Se menciona a menudo junto a los CFD por confusión. Para publicidad de cripto hoy rige **MiCA** (marketing communications, Título II) [VERIFICAR artículos].

## 6. Cripto y apalancamiento
### 6.1 Productos
| Producto | Qué es | Dónde |
|---|---|---|
| **CFD sobre cripto** | Contrato con un bróker sobre el precio de una cripto | Brókers de CFD (UE: **máx. 2:1** a minoristas, §5.2) |
| **Futuros de cripto** | Futuros con vencimiento sobre BTC, ETH, XRP… | Mercados regulados (p. ej. CME) o exchanges offshore |
| **Perpetuos (*perps*)** | Futuros **sin vencimiento**, con *funding rate* | Principalmente exchanges **fuera de la UE** |
| **Tokens apalancados** | Tokens que replican 2x, 3x o −1x de un activo; **reajuste periódico** | Algunos exchanges |
| **Préstamos con garantía cripto** | Se toma prestado con cripto de garantía; si el valor cae, **se liquida la garantía** | Plataformas CeFi/DeFi |

### 6.2 Funding rate y liquidación en cascada
- **Funding rate**: pago periódico entre posiciones largas y cortas. Si es positivo, **pagan los largos**.
- **Ejemplo ilustrativo (hipotético, cálculo mío)**: posición larga de **10.000 USD** con margen de **1.000 USD** (10x); *funding* del **0,01 % cada 8 horas** [valor ilustrativo, **no medido**; VERIFICAR en cada exchange]: 3 pagos al día = 0,03 % → **3 USD/día**; × 365 = **1.095 USD/año = 109,5 % del margen**.
- **Liquidación**: con margen de mantenimiento ilustrativo del 0,5 % del nominal (**50 USD**), la liquidación llega cuando la pérdida alcanza 1.000 − 50 = **950 USD**: **−9,5 %** del activo, antes de comisiones y *funding*. Cada exchange fija su fórmula.
- **Cascada**: la **liquidación forzosa** equivale a ventas (o compras) a mercado; si muchas posiciones apalancadas coinciden en un nivel, las liquidaciones **empujan el precio** y activan más liquidaciones. El dossier de geopolítica recoge una cifra de prensa de **>1.000 M$ en liquidaciones en 24 h** en marzo [VERIFICAR; secundaria]. Los episodios de liquidaciones masivas (p. ej. octubre de 2025 según prensa) **no los he verificado**.
- **Riesgos extra**: liquidación **automática de «auto-desapalancamiento»** (ADL), fallos del exchange, precios de referencia distintos (*mark price*) y **riesgo de contraparte** del exchange.

### 6.3 Regulación: MiCA frente a MiFID II
- **MiCA no cubre derivados que sean instrumentos financieros**: el Reglamento (UE) 2023/1114 dice en el **art. 2.4.a)** que **no se aplica** a los criptoactivos que se consideren **instrumentos financieros**; el **considerando 97** indica que los **derivados** que se consideren instrumentos financieros (MiFID II) con subyacente cripto están sujetos al **Reglamento de abuso de mercado** (596/2014) cuando se negocian en mercado regulado, SMN o SOC.
- En la práctica, un **CFD o futuro sobre cripto** es un derivado regulado por **MiFID II**; su comercialización a minoristas en España depende de la **CNMV** (límite 2:1, §5.2).
- Los **perpetuos y tokens apalancados** ofrecidos por plataformas sin autorización en la UE pueden **no tener ninguna garantía** de esa regulación. Qué productos concretos son «instrumento financiero» [VERIFICAR; depende de ESMA/NCA].

### 6.4 XRP y XLM (solo informativo)
- XRP y XLM tienen **CFD** y, en exchanges offshore, **perpetuos**. Un CFD cripto en España tiene tope **2:1** para minoristas: ejemplo mío, nominal **2.000 €** con margen **1.000 €** (50 %); el **cierre forzoso** llega con pérdida de 500 € = **−25 %** del precio del activo.
- La **liquidez** en derivados de XRP y XLM es menor que en BTC/ETH [VERIFICAR; no medido]: el tamaño de los **saltos** (*gaps*) y las horquillas puede ser mayor.
- **Movimientos diarios de varios puntos porcentuales** son habituales en cripto (magnitud concreta de XRP y XLM: ver dossier 8 [VERIFICAR; no calculada aquí]). Con 10:1, un 5 % diario equivale a un 50 % del margen (cálculo mío). No analizo causas (**causalidad no demostrada**).
- **Para quien tiene XRP/XLM al contado**: abrir una posición corta en derivados es una forma de cobertura que **tiene los mismos riesgos de margen** y costes de financiación; no es neutra. No es una sugerencia, es descripción.
- Para ETFs de XRP, ver el **dossier de ETFs de cripto** (§14).

## 7. Riesgos
### 7.1 Resumen de riesgos
| Riesgo | Qué significa | Dónde aparece |
|---|---|---|
| **Pérdida superior al capital** | Pérdida > depósito | **Futuros** y **opciones vendidas descubiertas**; en CFD **minorista UE** queda limitada a los fondos de la cuenta (§5.2) |
| **Liquidación forzosa** | Cierre a precio de mercado, a veces desfavorable | Todos con margen |
| **Gap** | El precio salta sin pasar por niveles intermedios; el cierre llega tarde | Noches, fines de semana, noticias |
| **Coste de financiación** | Intereses diarios | CFD, perpetuos (§5.4, §6.2) |
| **Riesgo de contraparte** | Quiebra del bróker o emisor | CFD, warrants, certificados, exchanges (§5.6, §9) |
| **Complejidad** | Se entiende mal el payoff | Opciones, estructurados |
| **Erosión temporal** | La prima se pierde cada día | Opciones compradas |
| **Concentración y psicología** | Sobreoperación y «recuperar pérdidas» | Todos (G14) |

### 7.2 Complejidad: MiFID II y el test
- MiFID II exige a las entidades **evaluar la conveniencia** (si el cliente tiene conocimientos y experiencia para el producto) o la **idoneidad** (si hay asesoramiento) en productos complejos. Los CFD y opciones binarias figuran como complejos en la Circular 1/2018 (§5.6). [VERIFICAR artículos de la Directiva 2014/65/UE; no abiertos.]
- **El test no es una certificación de seguridad**: un resultado aprobado no reduce el riesgo del producto.

### 7.3 ETF/ETN apalancados e inversos: reajuste diario y decay
- Un ETF **2x** o **3x** busca replicar **2 o 3 veces el rendimiento DIARIO** del índice; uno **inverso** (−1x) busca el opuesto. **No** replican 2x el rendimiento de un periodo largo.
- Como **reajustan cada día**, el resultado de varios días depende de la **trayectoria** del índice. **Ejemplos (cálculo mío)**:
| Caso | Índice | ETF 2x | Comentario |
|---|---|---|---|
| **A**: +10 % y luego −9,0909 % | 100 → 110 → **100** (0 %) | 100 → **120** (+20 %) → 120 × (1 − 0,181818) = **98,18** (**−1,82 %**) | El índice vuelve a su punto de partida y el 2x queda en pérdida. |
| **B**: +10 % y luego −10 % | 100 → 110 → **99** (−1 %) | 100 → 120 → 120 × 0,80 = **96** (**−4 %**) | Un índice **−1 %** da un 2x **−4 %**, no −2 %. |
| **C**: +10 % y +10 % (tendencia) | 100 → 110 → **121** (+21 %) | 100 → 120 → **144** (+44 %) | En tendencias fuertes, el 2x **supera** el doble del índice (42 %). |
| **D**: mismo caso A, ETF 3x | 100 → 110 → 100 | 100 → 130 → 130 × (1 − 0,272727) = **94,55** (**−5,45 %**) | Más apalancamiento, más pérdida por el «decay». |
| **E**: inverso −1x, caso A | 100 → 110 → 100 | 100 → 90 → 90 × 1,090909 = **98,18** (**−1,82 %**) | Mismo efecto: el inverso también pierde. |
- **Estimación teórica** (aproximada, **no medida**): el arrastre anual por volatilidad de un apalancado de factor L con volatilidad anual σ es ≈ L(L−1)/2 · σ². Para un 2x con σ = 20 %: ≈ **4 %/año**; con σ = 50 %: ≈ **25 %/año**. Para 3x con σ = 20 %: ≈ **12 %/año**.
- **Producto diseñado para el corto plazo**: los folletos de estos productos suelen advertir de que **no son aptos para mantener a largo plazo** [VERIFICAR en un KID; **no he leído ninguno**].
- Los **ETN** (deuda del emisor) añaden **riesgo de crédito del emisor** (G9 §2.2).
- **En la UE**: un ETF apalancado cotizado europeo debe llevar **KID** con indicador de riesgo y se vende bajo reglas de complejidad; los ETFs de EE. UU. suelen **no estar disponibles** para minoristas de la UE (G5 §4.3).

### 7.4 KID, PRIIPs e indicador de riesgo
- El **KID** resume costes, riesgos y escenarios, con un **indicador de riesgo de 1 (menor) a 7 (mayor)** [VERIFICAR detalle y metodología; **no abierto**].
- **Matiz**: el indicador mide **volatilidad y riesgo de crédito**, no la probabilidad de perder más que lo invertido; en derivados con pérdida potencial ilimitada hay que leer también la **sección de escenarios** [VERIFICAR].
- **Los derivados de mercado** (futuros y opciones listados) **no siempre tienen KID**; los CFD, warrants y certificados para minoristas, normalmente sí [VERIFICAR].

## 8. Fiscalidad en España
> Resumen educativo, **no asesoramiento fiscal**. Coherente con **G12 §1.5 y §4** (tramos de la base del ahorro y compensación). Texto de la LIRPF leído hoy desde la API del BOE.

### 8.1 Base y tipos
- **Calificación**: las ganancias y pérdidas por derivados son **ganancias o pérdidas patrimoniales**. El **art. 37.1.m** LIRPF dice que en las operaciones de **futuros y opciones en los mercados regulados por el Real Decreto 1814/1991** se considera ganancia o pérdida patrimonial «el rendimiento obtenido», salvo que sea **cobertura de una operación principal** de una actividad económica (entonces va con la actividad). [VERIFICAR vigencia actual del Real Decreto 1814/1991; no abierto.]
- **Base del ahorro**: el **art. 46.b** incluye en la renta del ahorro las **ganancias y pérdidas patrimoniales con ocasión de transmisiones de elementos patrimoniales**. El **art. 45** dice que lo que no es renta del ahorro es **renta general**. **No encontré** en la LIRPF un artículo que diga expresamente que los CFD o el forex cierran «transmisiones»; **el criterio habitual de las entidades y de la AEAT** los trata en la **base del ahorro**, pero **[VERIFICAR consultas de la DGT]**; para **CFD, forex y perpetuos cripto** la calificación debe confirmarse con un asesor [VERIFICAR].
- **Tipos** (BOE, **art. 66** estatal + **art. 76** supletorio autonómico; versión consolidada **22-dic-2024**, vigente tras la **Ley 7/2024**): la escala estatal es **9,5 / 10,5 / 11,5 / 13,5 / 15 %**; sumada a la autonómica supletoria da **19 % hasta 6.000 €, 21 % hasta 50.000 €, 23 % hasta 200.000 €, 27 % hasta 300.000 € y 30 % por encima**. Las comunidades **pueden fijar su escala** [VERIFICAR la de tu comunidad]. **El 28 % que aparece en algunas webs no coincide con el BOE** (G12 §1.5).
- **Retenciones**: el **art. 75.1.d) del RIRPF** lista las ganancias sujetas a retención: **reembolsos de IIC**, aprovechamientos forestales y derechos de suscripción. **Los derivados no figuran** en esa lista, de modo que **no se practica retención** sobre sus ganancias: el inversor las declara. Un **bróker extranjero** no practica retención ni informa a la AEAT en la misma forma que uno español [VERIFICAR obligaciones de información].

### 8.2 Compensación de pérdidas (art. 49) y regla de los 2 meses
- **Art. 49.1 (leído hoy)**: se compensan ganancias y pérdidas del ahorro del año; si queda saldo negativo, se compensa con el saldo positivo de **rendimientos del capital mobiliario** del mismo año con el **límite del 25 %**, y lo no compensado se arrastra **4 años**.
- **Ejemplo mío**: en el año, ganancias en acciones de **2.000 €** y pérdidas por CFD de **7.000 €** → saldo **−5.000 €**. Rendimientos del capital mobiliario (intereses) **2.000 €**: se compensan hasta 25 % × 2.000 = **500 €**. Base del ahorro del año = 2.000 − 500 = 1.500 € → 19 % = **285 €**. Quedan **4.500 €** para los 4 años siguientes.
- **Otro ejemplo**: ganancias de futuros **8.000 €** y pérdidas de CFD **3.000 €** → saldo **+5.000 €** → 19 % (primer tramo, hasta 6.000 €) = **950 €**.
- **Regla de los 2 meses** (**art. 33.5.f**): no se computa la pérdida por transmisión de **«valores o participaciones»** admitidos a negociación si se adquieren **valores homogéneos** en los 2 meses anteriores o posteriores. El texto habla de **valores o participaciones**: **si aplica a futuros, opciones, CFD o forex** (que no son «valores») no lo he podido confirmar: **[VERIFICAR DGT]**. La del **año** del **art. 33.5.e** (elementos patrimoniales readquiridos en el año siguiente) se menciona en G12 §4.2.
- **Pérdidas por no justificar** (art. 33.5.a): **no se computan** si no se justifican; la prueba habitual son los **extractos del bróker**.

### 8.3 Obligaciones informativas
- **Modelo 720**: bienes en el **extranjero** (cuentas, valores, inmuebles, seguros): plazo **1-ene a 31-mar**, umbral **50.000 € por categoría** (G12 §9). Un **bróker no español** con **saldo en una cuenta** y/o **valores** puede entrar en categorías [VERIFICAR; no he leído la Orden HAP/72/2013 ni la AEAT]. **Si un CFD o futuro** en un bróker extranjero computa como «valor» o solo el saldo de la cuenta, **no lo he comprobado**.
- **Modelo 721** (criptoactivos en custodia en el extranjero): G12 §9 y dossier 13. Un perpetuo en un exchange extranjero [VERIFICAR si procede].
- **Modelo D-6**: es una declaración de inversiones exteriores (participaciones relevantes) que, por su naturaleza, **no parece aplicar a CFD ni futuros de cartera** [VERIFICAR; no abierto].
- **Brókers sin retención ni informativa a la AEAT**: la ganancia sigue sujeta a IRPF; la **declaración la hace el contribuyente** (G12 §9).

## 9. Protecciones y chiringuitos
### 9.1 Qué hay
| Protección | Qué hace | Qué no hace |
|---|---|---|
| **FOGAIN** (Fondo de Garantía de Inversiones) | Paga hasta **100.000 € por titular** si una **entidad adherida** (sociedades y agencias de valores, gestoras de carteras…) cae en concurso o la CNMV declara que no puede cumplir, sobre **efectivo e instrumentos confiados** a ella | **No cubre pérdidas de mercado** (la página no lo detalla; es el principio del sistema [VERIFICAR RD 948/2001]); no cubre activos en paraísos fiscales ni de determinados inversores ni de vinculados a la entidad; **no cubre a entidades no autorizadas** |
| **Brókers de otro país de la UE** | Dependen de su **propio sistema** de indemnización nacional [VERIFICAR el importe y el sistema del país del bróker] | |
| **Supervisión CNMV/ESMA** | Autorización, vigilancia, medidas de intervención (§5) | No evita pérdidas |
| **Protección de saldo negativo (CFD)** | Limita la pérdida a los fondos de la cuenta (§5.2) | No cubre la pérdida de **todo el saldo** de la cuenta |

### 9.2 Chiringuitos y «trading» con CFD y cripto
- La CNMV publica **advertencias** sobre entidades **no autorizadas** («chiringuitos financieros») y recoge también las de otros supervisores europeos. **No pude abrir cnmv.es** (error 403) ni su listado.
- Notas de prensa citan lotes de **más de 20 a casi 80 entidades** por aviso (p. ej. **marzo de 2025: 22**; **7-ene-2026: casi 80**) [secundaria, **VERIFICAR**; no es un recuento oficial].
- Hay que distinguir: una **entidad autorizada** puede ofrecer CFD (con las reglas de §5); un **chiringuito** no está autorizado y su cliente **queda fuera del FOGAIN**.

### 9.3 Señales de fraude (descripción de patrones)
- Rentabilidades **garantizadas** o muy altas con «cero riesgo».
- Contacto por **WhatsApp, Telegram o llamada en frío**; «asesor» o «gestor de cuenta» que **presiona** para ingresar más.
- Uso de **famosos** en anuncios falsos (la CNMV ha avisado de campañas así).
- Plataformas **sin autorización** consultable en el registro de la CNMV [VERIFICAR el registro] o con sede en un país sin supervisor.
- Peticiones de **más ingresos para retirar** (comisiones, impuestos «previos»).
- **Pagos por criptomonedas** o a cuentas de terceros; **formación gratuita** o **cuenta demo** que lleva a depositar (la CNMV las prohíbe a CFD, §5.3).
- Plataformas con **gráficos «demo»** que muestran ganancias que luego no se pueden retirar.
- Esto **describe señales**; no sustituye comprobar la autorización de la entidad y las advertencias de la CNMV.

## 10. Datos actuales (13-oct-2026)
| Dato | Valor | Fecha | Fuente | Nota |
|---|---|---|---|---|
| **VIX** (volatilidad implícita S&P 500) | **14,84** | **9-oct-2026** (último dato disponible) | **FRED, serie VIXCLS (primaria, leída hoy)** | 15,41 el 8-oct; máximo de 2026: **31,05 (27-mar)**; mínimo de 2026: **14,21 (22-sep)** |
| **VIX: referencia histórica** | Mediana **17,09** (desde ene-2006, 5.258 observaciones); máximo **82,69 (16-mar-2020)** | | FRED (cálculo mío) | El máximo de la serie bajada incluye 2006-2026 |
| **OTC derivados: nocional vivo** | **846 billones de $** | **jun-2025** | **BIS (publicado 8-dic-2025; primaria, leída hoy)** | +16 % interanual; **tipos de interés = 79 %**; el BIS señala diferencias de cobertura entre encuestas |
| **OTC derivados: valor bruto de mercado** | **21,8 billones de $** | jun-2025 | BIS | +29 % interanual. **21,8 ÷ 846 = 2,6 %** del nocional (cálculo mío) |
| **OTC divisas** | **155 billones de $** | jun-2025 | BIS | |
| **OTC: dato de dic-2025** | No obtenido en primaria | | | Una nota de ISDA cita un valor bruto de mercado de 22,8 billones a fin de 2025 [secundaria, **VERIFICAR**] |
| **EUR/USD** | 1,1193 | 13-oct | G5 (Yahoo, secundaria) | |
- **Cómo leer el nocional**: el **nocional** (846 billones) **no es** lo que puede perderse: es el **valor de referencia** de los contratos. El **valor bruto de mercado** (21,8 billones) es una medida más cercana a la **exposición**; aun así incluye posiciones **compensables** entre sí (el BIS lo señala; [VERIFICAR el comentario]).
- **Un VIX de 14,84** está **por debajo de la mediana desde 2006** (17,09): la volatilidad implícita del S&P 500 está en niveles **moderados** frente a esa serie. **No predice nada** [ESPECULACIÓN si se usa como señal]. El VIX no mide la volatilidad de XRP ni XLM.
- **Contexto**: tipos y macro, en G1 y dossier 8; petróleo y Ormuz, en dossier 11 y G9.

## 11. Errores comunes y señales a vigilar
### 11.1 Errores comunes
1. **Confundir margen con riesgo**: el margen es el depósito; la exposición es el **nominal** (§2.2).
2. **Pensar que el máximo que se pierde es el depósito**: en futuros y opciones vendidas puede ser **más** (§7.1).
3. **Mantener CFD o apalancados a largo plazo** sin contar la **financiación** y el **decay** (§5.4, §7.3).
4. **Comprar opciones sin considerar el tiempo**: la prima se erosiona y exige acertar dirección **y plazo** (§4.5).
5. **Vender opciones por la prima «fácil»**: ganancia acotada, pérdida grande (§4.3).
6. **Creer que un ETF 2x duplica el rendimiento anual**: replica el **diario** (§7.3).
7. **Operar con chiringuitos o plataformas no autorizadas** (§9).
8. **Fiarse de la «protección de saldo negativo» como seguro total**: limita a los fondos de la cuenta, no al margen (§5.2).
9. **Aumentar el apalancamiento tras una pérdida** («recuperar»).
10. **No guardar extractos** para justificar pérdidas fiscales (§8.2).
11. **Dejar fondos de sobra en la cuenta del bróker de CFD**: todo el saldo está expuesto.
12. **Pensar que cubrir con un perpetuo es «gratis»**: *funding*, margen y liquidación existen (§6.2).
13. **Confundir spot y futuro** (G9 §9.1).

### 11.2 Señales a vigilar (descripción de patrones, no órdenes)
| Señal | Qué puede indicar |
|---|---|
| Un VIX que **sube bruscamente** | Mayor probabilidad de **saltos** y **llamadas de margen** |
| *Funding rate* muy **positivo** durante varios días | Mucho apalancamiento largo; riesgo de **liquidaciones en cascada** si se invierte |
| **Spreads** que se ensanchan | Menor liquidez o volatilidad; **coste** de entrada y salida mayor |
| Subida del **margen** exigido por la cámara o el bróker | El mercado percibe más riesgo |
| Anuncios de **famosos** y promesas de rentabilidad | Patrón de **fraude** (§9.3) |
| **Aviso de riesgo** con porcentaje de cuentas que pierden | Dato oficial del propio proveedor (§5.2) |
| **Resolución de la CNMV o ESMA** nueva | Cambio de reglas para minoristas |

## 12. Hechos frente a opiniones
| Hechos (con fuente) | Opiniones o previsiones |
|---|---|
| Límites para CFD minorista: **30:1 a 2:1**; cierre al 50 %; saldo negativo limitado (Resolución CNMV 2019; ESMA 2018) | «Los CFD son una trampa» / «los CFD son una herramienta legítima» |
| Resolución CNMV de 11-jul-2023: **publicidad de CFD prohibida** a minoristas | Que la prohibición **funcione** |
| **Circular 1/2022 derogada** el 28-dic-2024 (BOE) | Que MiCA proteja **mejor o peor** |
| **MiCA art. 2.4.a)**: no se aplica a instrumentos financieros | Que los perpetuos «acabarán prohibidos» |
| **Art. 49 LIRPF**: compensación del **25 %** y arrastre de **4 años** | Que «las pérdidas siempre se compensan» |
| **VIX 14,84** el 9-oct (FRED) | Que «hay poca volatilidad, luego habrá calma» |
| **846 billones $** de nocional OTC a jun-2025 (BIS) | Que ese tamaño sea «un riesgo sistémico» |
| FOGAIN cubre **100.000 €/titular** si falla la entidad | Que cubra «la pérdida de dinero» |

## 13. Lo que no sé / no he podido verificar
- **cnmv.es** (error 403): no pude abrir la **lista de advertencias** ni las notas, ni **estadísticas de pérdidas de minoristas** actualizadas. Las cifras de chiringuitos son de prensa.
- Las **resoluciones y circulares de la CNMV**, la **nota de ESMA** y la **página de FOGAIN** las leí con una herramienta que devuelve **resúmenes**, no el texto literal: las cifras de §5 provienen de esos resúmenes (**coinciden entre ESMA y CNMV**) y conviene confirmarlas en el BOE.
- **MiFID II**, **PRIIPs** y el **Reglamento Delegado 2017/653**: no abiertos; lo dicho sobre conveniencia, idoneidad e indicador de riesgo es general [VERIFICAR].
- **Real Decreto 1814/1991** (referenciado en el art. 37.1.m LIRPF): no abierto; no sé si sigue vigente en su redacción.
- **Tratamiento fiscal exacto de CFD, forex y perpetuos cripto** (¿ahorro?, ¿homogeneidad para la regla de 2 meses?): **sin consulta de la DGT leída**.
- **Modelo 720/721** para posiciones en derivados en el extranjero: no leí la norma de la AEAT.
- **Retenciones en brókers españoles sobre derivados**: leído el art. 75 RIRPF; **no comprobé** la práctica de cada entidad.
- **Datos del BIS posteriores a jun-2025** (dic-2025) y **estadísticas de mercados organizados** (volumen de futuros, interés abierto): no obtenidos en primaria.
- **Funding rates, comisiones, spreads y recargos** de los ejemplos: **ilustrativos**, no de ningún bróker o exchange.
- **Liquidaciones masivas de octubre de 2025**: solo recuerdo de prensa; **no verificadas**.
- **Tratamiento de ETFs apalancados europeos** (existencia, KID, complejidad): sin leer ningún KID.
- **Si una plataforma concreta está autorizada**: **no he consultado ningún registro**.
- **Datos de mercado a las ~13:00 del 13-oct**: la sesión sigue en curso.

## 14. Guías relacionadas
- **G1** (tipos e inflación: tipo de financiación y de referencia), **G4** (renta fija: bonos como activos sin apalancamiento), **G5** (acciones, ETFs y fondos: KID, divisa, ETFs de EE. UU.; **§5.4** y **§10**), **G9** (commodities: contango, backwardation y **§2.3**; **§2.4** anunciaba esta G7), **G12** (fiscalidad: **§1.5** escala del ahorro, **§4** compensación, **§9** modelos 720/721), **G13** (gestión patrimonial: cómo encaja el riesgo en la cartera), **G14** (errores del inversor y sesgos: sobreoperación, aversión a la pérdida) y **G15** (elegir asesor y entidad: autorización y reclamaciones).
- **G6** (planes de pensiones, PIAS y seguros de ahorro): pendiente.
- **Dossier de ETFs de cripto** (`2026-10-09-etfs-cripto.md`), **dossier de stablecoins** (`2026-10-09-stablecoins.md`), **dossier de fiscalidad de XRP y XLM** (`2026-10-09-fiscalidad-espana-xrp-xlm.md`) y **dossier 8** (macro).
