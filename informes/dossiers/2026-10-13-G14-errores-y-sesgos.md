# Guía G14: Errores del inversor y sesgos (España, 13-oct-2026)

> **Guía educativa, no es recomendación** de comprar, vender ni contratar ningún activo, producto o estrategia, y **no es un diagnóstico personal**: describe cómo funcionan los sesgos y qué herramientas existen, sin decir qué debe hacer nadie. Foco en España, para un inversor particular a largo plazo. **Fuentes primarias leídas hoy (texto completo)**: Barber y Odean (*Journal of Finance*, 2000), Odean (*Journal of Finance*, 1998), Morningstar (informe «Mind the Gap 2025», PDF oficial del 13-ago-2025), Banco de España (Encuesta de Competencias Financieras 2021, informe de nov-2023), CNMV (estudio sobre criptomonedas, mayo-junio de 2022) y la página de la revista *Econometrica* (Kahneman y Tversky, 1979; solo el resumen). **Nota de ESMA** (27-mar-2018) leída en su web. Lo que **no** pude abrir en fuente primaria va como **[VERIFICAR]**; las opiniones y previsiones, como **[ESPECULACIÓN]**. Los cálculos son **míos con datos públicos**. **El pasado no garantiza el futuro.**

## 0. Resumen en 12 líneas
1. Un **sesgo** es una desviación sistemática y previsible al decidir. No significa «ser tonto»: lo tenemos todos, y se nota más cuando hay dinero, miedo o ruido (§1-2).
2. Hallazgo académico sólido: la **teoría prospectiva** (Kahneman y Tversky, *Econometrica*, 1979) describe que valoramos ganancias y pérdidas **respecto a un punto de referencia**, y que las pérdidas pesan más que ganancias equivalentes. Lo **discutido** es cuánto pesa, cuándo aparece y cuánto de esto explica los precios de mercado (§1).
3. **Barber y Odean (2000)**: con 66.465 hogares de un bróker de EE. UU. (1991-1996), los que más operaron ganaron **11,4 %/año** frente a **17,9 %** del mercado; el hogar medio, **16,4 %** neto (§3.2).
4. **Odean (1998)**: con 10.000 cuentas (1987-1993), se realizaron más las ganancias (**14,8 %** de las ganancias latentes) que las pérdidas (**9,8 %**): ratio **1,52** (cálculo mío sobre las cifras del artículo) (§3.3).
5. **Morningstar «Mind the Gap 2025»**: el dólar medio invertido en fondos y ETFs de EE. UU. ganó **7,0 %/año** en 10 años (hasta 31-dic-2024) frente a **8,2 %** del fondo: **1,2 puntos** menos (≈ **14,6 %** de la rentabilidad). El propio estudio advierte que **no mide el error de un inversor concreto** y que parte de la diferencia viene de hábitos razonables, como aportar cada mes (§3.1).
6. En este proyecto, la **prueba de estrés** de XRP/XLM muestra caídas de **-50 % en una semana** y **-95 %** desde el máximo (§4.1). Saber que existen **antes** de que pase es una forma de no decidir en caliente; no es una previsión.
7. **Cripto y redes**: manada, influencers, «predicciones» de precio y bulos. Comprobar una afirmación con **fuente primaria** reduce el riesgo (§5; ver [dossier de custodia §7](2026-10-09-custodia-y-seguridad.md)).
8. **Herramientas** (sin recomendar productos): reglas escritas de antemano, lista de comprobación, diario de decisiones, periodo de enfriamiento, revisión con calendario, premortem y abogado del diablo (§6).
9. Errores concretos del inversor español: comisiones, productos complejos, concentración en la empresa donde se trabaja, fiscalidad y divisa, rentabilidades pasadas, vender en pánico, apalancarse, confundir ahorro con inversión (§7).
10. **ESMA (27-mar-2018)**: en análisis de reguladores nacionales de la UE, **74-89 %** de las cuentas minoristas en CFD perdían dinero (§7.2).
11. **Banco de España (ECF 2021)**: respondieron bien a la pregunta de inflación el **65 %**, a la de interés compuesto el **41 %** y a la de diversificación el **52 %** (§3.4). No dice nada de sesgos, pero dibuja el terreno.
12. Hay un **cuestionario de 10 preguntas sí/no, sin puntuación** (§8) y una lista de lo que no verifiqué (§9).

## 1. Por qué importan los sesgos: finanzas conductuales en una página
### 1.1 Qué se sabe (hallazgos académicos)
- **Kahneman y Tversky (1979)**, «Prospect Theory: An Analysis of Decision under Risk», *Econometrica*, vol. 47, n.º 2, marzo de 1979. Según el resumen de la revista (leído hoy): critican la teoría de la utilidad esperada como descripción de cómo decide la gente; proponen que se valoran **ganancias y pérdidas** (no la riqueza final); la **función de valor** es cóncava en ganancias, normalmente convexa en pérdidas y **más empinada para las pérdidas**; las probabilidades se sustituyen por **«pesos de decisión»** (se sobrepondera lo muy improbable). Consecuencia: **aversión al riesgo** ante ganancias seguras y **búsqueda de riesgo** ante pérdidas seguras. La revista indica páginas 263-292 (otras fuentes dicen 263-291; **[VERIFICAR] el rango** si se cita formalmente).
- **Thaler**: Premio Nobel de Economía 2017 «por sus contribuciones a la economía conductual», con conceptos como la **contabilidad mental** (según la web del Nobel, resultado de búsqueda; no abrí la página completa).
- **Shiller**: Nobel de 2013, **compartido con Fama y Hansen**, por el análisis empírico de los precios de los activos; trabajó la idea de que los precios pueden desviarse de los fundamentos durante periodos largos (burbujas). Fama defiende que los precios a corto plazo son difíciles de predecir. Que el **mismo premio** reconociera visiones tan distintas ilustra que el debate sigue abierto (fuente: nobelprize.org, resultados de búsqueda; no abrí las páginas completas).
- **Kahneman**: Nobel de 2002 (compartido con Vernon Smith) [VERIFICAR; de memoria].

### 1.2 Qué es discutido
- **Cuánto de la «aversión a las pérdidas» es universal**: hay críticas recientes que sostienen que se ha exagerado su alcance (por ejemplo, Gal y Rucker, 2018, *Journal of Consumer Psychology*) [VERIFICAR; de memoria, no leído]. Lo prudente es decir: **las pérdidas suelen pesar más que las ganancias, pero la magnitud depende del contexto**.
- **Si los sesgos mueven los precios del mercado o solo a los individuos**: la hipótesis de mercados eficientes sostiene que los errores individuales se compensan; las finanzas conductuales sostienen que algunos errores son **sistemáticos** y no se compensan. **No hay consenso** [ESPECULACIÓN si se presenta como cerrado].
- **Por qué existe el efecto disposición**: se ha explicado con teoría prospectiva, con creencias de reversión a la media y con otros mecanismos; no hay una única explicación aceptada [VERIFICAR la literatura posterior a Odean 1998].
- **Muchos «sesgos» son etiquetas a posteriori**: es fácil llamar «sesgo» a cualquier decisión que salió mal. Un sesgo se demuestra con **diseño experimental o datos masivos**, no con una anécdota.

## 2. Catálogo de sesgos
Formato: **definición sencilla**, **ejemplo cotidiano** (ilustrativo, inventado, no es un caso real) y **señal de alarma** (algo que se puede observar en el propio comportamiento).

| Sesgo | Definición sencilla | Ejemplo cotidiano | Señal de alarma |
|---|---|---|---|
| **Aversión a las pérdidas** | Una pérdida duele más que lo que alegra una ganancia igual. | Alguien rechaza ver su cuenta cuando está en negativo, pero la mira a diario cuando sube. | Dejar de mirar la cartera en las caídas; decisiones guiadas por evitar el dolor y no por el plan. |
| **Exceso de confianza** | Creerse mejor informado o más hábil que la media. | «Esta vez sí he visto lo que el mercado no ve», tras dos aciertos seguidos. | Más operaciones tras una racha buena; no registrar ni los fallos. |
| **Sesgo de confirmación** | Buscar y recordar lo que apoya lo que ya pensamos. | Leer solo canales que dicen que un activo subirá, después de haberlo comprado. | Que todas las fuentes que sigues opinen igual; no saber el mejor argumento contrario. |
| **Anclaje** | Quedarse pegado a un número inicial. | «Lo compré a 100, no vendo hasta recuperar 100», o juzgar un precio solo por su máximo histórico. | Frases del tipo «ya vale más/menos de lo que debería» sin otro criterio que un número pasado. |
| **Efecto manada y FOMO** | Imitar a la mayoría o temer perderse una subida. | Comprar tras ver «todo el mundo hablando» de un activo que ya ha subido mucho. | La prisa; la razón de entrar es «que no se me escape»; decidir tras ver redes sociales. |
| **Sesgo de recencia** | Dar demasiado peso a lo ocurrido hace poco. | Tras tres semanas de caídas, asumir que seguirán; tras tres meses de subida, que seguirán. | Proyectar una línea recta con los últimos datos; olvidar ciclos anteriores. |
| **Efecto disposición** | Vender las ganadoras pronto y mantener las perdedoras. | Vender la que ha subido «para asegurar» y mantener la que baja «hasta que se recupere». | Realizar ganancias pequeñas rápido y arrastrar pérdidas grandes años. |
| **Contabilidad mental** | Tratar el dinero como si estuviera en «cajones» distintos. | Gastar sin cuidado «el dinero de la ganancia» como si fuera dinero de casino. | Criterios distintos para euros idénticos según su origen (sueldo, premio, ganancia). |
| **Sesgo de disponibilidad** | Juzgar la probabilidad por lo fácil que se recuerda un ejemplo. | Tras una noticia vistosa de quiebra, creer que es más común de lo que es. | Basar el riesgo en titulares recientes y no en datos de frecuencia. |
| **Ilusión de control** | Creer que se influye en lo que es azar. | Pensar que seguir el precio a diario «reduce el riesgo» de que baje. | Más actividad (revisar, operar) sin que cambie ninguna información nueva. |
| **Sesgo de supervivencia** | Mirar solo a los que quedaron y olvidar a los que desaparecieron. | Ver rankings de fondos «ganadores» a 10 años sin los fondos cerrados o fusionados. | Rankings sin decir cuántos productos se retiraron; historias de éxito sin los casos fallidos. |
| **Efecto de dotación** | Valorar más lo que ya se tiene solo por tenerlo. | No vender algo heredado o regalado, aunque no se compraría hoy. | «No lo vendo porque es mío», sin contrastar con la pregunta: «¿lo compraría hoy a este precio?». |
| **Falacia del coste hundido** | Seguir invirtiendo porque ya se ha invertido mucho. | Meter más dinero en una pérdida para «no tirar lo ya puesto». | Justificar la decisión con lo gastado y no con lo que se espera a partir de ahora. |

## 3. Evidencia
### 3.1 Rentabilidad del fondo frente a rentabilidad del inversor: Morningstar «Mind the Gap»
**Hallazgo (fuente primaria, leída hoy: informe de Morningstar, 13-ago-2025)**
- Morningstar estima que **el dólar medio invertido en fondos y ETFs de EE. UU.** ganó **7,0 % anual en los 10 años hasta el 31-dic-2024** (la «rentabilidad del inversor»), frente a **8,2 %** de la rentabilidad total agregada de esos fondos, suponiendo una compra única al principio. La diferencia, **1,2 puntos al año**, equivale a ~**15 %** de la rentabilidad total (cálculo mío: 1,2 / 8,2 = **14,6 %**).
- Según el resumen de resultados que ofrece el propio estudio, los fondos mixtos tuvieron la menor diferencia y los **fondos sectoriales** la mayor en dólares; cuanto **más volátiles los flujos**, mayor la diferencia [VERIFICAR el detalle por categoría en las tablas del PDF; me apoyo en el resumen].
- **Cálculo ilustrativo (mío, no previsión)**: 10.000 € a 7,0 %/año durante 10 años: 10.000 × 1,07¹⁰ = **19.672 €**; a 8,2 %: 10.000 × 1,082¹⁰ = **21.993 €**. Diferencia: **2.321 €** (**-10,6 %** del capital final). Esto es un **efecto agregado** sobre un euro medio, **no** lo que perdería una persona concreta.

**Metodología (según el propio informe)**
- Compara la **rentabilidad ponderada por dinero** (calculada con una **tasa interna de retorno** sobre los activos y flujos mensuales del conjunto de fondos) con la **rentabilidad ponderada por tiempo** (la del fondo).
- Se limita a **fondos y ETFs que existían a 1-ene-2015**; incluye los fusionados o liquidados (los liquidados se asumen en efectivo).

**Limitaciones que reconoce el propio estudio** (leídas hoy)
- **No es una medida del error de un inversor**: el estudio dice que la cifra no es «un sustituto de la rentabilidad ponderada por dinero del inversor medio», que depende del momento e importe de cada compra y venta.
- **Aportar cada mes o rebalancear también abre una brecha** entre la rentabilidad del inversor y la del fondo, aunque sean buenas prácticas: **no debe leerse como «parábola del dinero tonto»**.
- No corrige el sesgo de creación (excluye fondos lanzados después de 2014).
- Es solo EE. UU. y fondos abiertos y ETFs; **no es evidencia para España**.
- Segunda fuente (búsqueda del 13-oct, no leída): una edición de 2026 (hasta dic-2025) daría 8,7 % frente a 9,9 % (misma brecha de 1,2) [VERIFICAR en el PDF de Morningstar].

### 3.2 Exceso de negociación: Barber y Odean (2000)
**Hallazgo académico (leído hoy: resumen y texto del artículo)**
- Artículo: **Barber, B. y Odean, T. (2000), «Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors»**, *The Journal of Finance*, vol. 55, n.º 2, abril de 2000.
- Muestra: **66.465 hogares** con cuenta en un gran bróker de descuento de EE. UU., de **enero de 1991 a diciembre de 1996**.
- Resultados del artículo: los hogares que **más operan** obtuvieron **11,4 %** anual; el mercado, **17,9 %**; el hogar medio, **16,4 %** neto, con rotación del **75 %** de la cartera al año; los que operaban poco, **18,5 %**.
- **Antes de costes** (rentabilidad bruta) el hogar medio ganó **18,7 %** (frente a 17,9 % del mercado): casi sin diferencia con el mercado. El descuento viene **después de la horquilla y las comisiones**.
- Cálculos míos: 17,9 - 11,4 = **6,5 puntos** (los más activos frente al mercado); 18,5 - 11,4 = **7,1 puntos** (poco activos frente a muy activos); 18,7 - 16,4 = **2,3 puntos** de coste para el hogar medio (1,5 puntos si se mide en agregado: 18,2 → 16,7, cifras del artículo).
- Interpretación de los autores: la **sobreconfianza** explicaría la alta rotación y el mal resultado. Es una **hipótesis** respaldada por la comparación entre quienes operan mucho y poco, no una prueba directa de la causa.

**Limitaciones**
- Un solo bróker de EE. UU., años de **mercado alcista (1991-96)**; las comisiones de entonces eran distintas de las de hoy.
- Los hogares **eligen** operar mucho: no es un experimento. Pueden diferir en riqueza, objetivo y tolerancia al riesgo.
- Es sobre **acciones sueltas**, no sobre aportaciones periódicas a fondos.
- Hoy las comisiones son más bajas, pero hay productos de alta rotación (apalancados, derivados) que tienen otros costes.

### 3.3 Efecto disposición: Odean (1998)
**Hallazgo académico (leído hoy)**
- **Odean, T. (1998), «Are Investors Reluctant to Realize Their Losses?», *The Journal of Finance*, vol. 53, n.º 5, octubre de 1998** (págs. 1775-1798 según la cita habitual). Registros de **10.000 cuentas** de un gran bróker de descuento de EE. UU., **1987-1993**.
- Resultado: los inversores muestran **«una fuerte preferencia por realizar ganadoras antes que perdedoras»**; el comportamiento **no parece motivado por rebalancear** ni por evitar costes de acciones baratas, **ni lo justifica el rendimiento posterior**; en cuentas con impuestos, **empeora el resultado tras impuestos**. La venta por motivos fiscales se nota **en diciembre**.
- Cifras del artículo (año completo): **13.883** ganancias realizadas y **79.658** latentes; **11.930** pérdidas realizadas y **110.348** latentes. **Cálculo mío**: proporción de ganancias realizadas = 13.883 / (13.883 + 79.658) = **14,8 %**; de pérdidas = 11.930 / (11.930 + 110.348) = **9,8 %**; ratio = **1,52** (el artículo dice «algo más de 1,5»).
- **Limitaciones**: un solo bróker, años 1987-1993; **no demuestra una causa** (el artículo descarta algunas explicaciones, no todas); en cuentas con **pérdidas fiscalmente útiles** (diciembre) el patrón se invierte parcialmente. No hay datos de España en este artículo.
- **Divulgación frente a hallazgo**: «los inversores venden lo que sube y mantienen lo que baja» se cita en divulgación como si fuera una regla universal. El hallazgo es **estadístico, para una muestra y un periodo**.

### 3.4 Educación financiera en España: Banco de España (ECF 2021)
- **Encuesta de Competencias Financieras 2021** (informe de noviembre de 2023; Banco de España con INE y CNMV; **7.835 entrevistas completas**, población de 18 a 79 años): acertaron la pregunta sobre **inflación** el **65 %**, **interés compuesto** el **41 %** y **diversificación del riesgo** el **52 %**.
- **Lectura prudente**: no mide sesgos, mide **conocimientos**. Pero el interés compuesto es un concepto con el que muchos errores de intuición (subestimar cuánto pesan las comisiones o el tiempo) se relacionan [ESPECULACIÓN: no está demostrado en esta encuesta].
- OCDE (alfabetización financiera): **no consultada** en esta sesión [VERIFICAR; el marco de la ECF sigue las preguntas de la OCDE, según el propio informe].

## 4. Ejemplos con datos públicos de este proyecto (ilustración neutral)
### 4.1 La prueba de estrés: qué significa «caer un 50 %» (aversión a las pérdidas, vender en pánico)
Del [dossier de prueba de estrés](2026-10-09-prueba-de-estres.md) (Yahoo Finance, cierres diarios, desde 9-nov-2017 hasta 9-oct-2026; mezcla 80 % XRP / 20 % XLM rebalanceada a diario, un supuesto; sin comisiones ni impuestos; en dólares):
| Episodio histórico | Variación | Un 100 pasaría a | Subida necesaria para volver (cálculo mío) |
|---|---|---|---|
| Peor semana | -50,5 % | 49,5 | 100 / 49,5 - 1 = **+102 %** |
| Peor año (365 días) | -87,4 % | 12,6 | 100 / 12,6 - 1 = **+694 %** |
| Caída máxima | -95,4 % | 4,6 | 100 / 4,6 - 1 = **+2.074 %** |
- Son **historia**, no previsión: el dossier lo recuerda (menos de 9 años de datos, burbuja de 2017-18). XLM **no ha recuperado** su máximo y la mezcla tardó hasta **dic-2024** en volver al suyo.
- **Por qué es útil para entender sesgos**: la aversión a las pérdidas hace que en una caída del -50 % duela más de lo previsto «en frío». Mirar **antes** estos números es una manera de comprobar si las reglas de §6 resisten ese escenario. En G5 §8.4: un -50 % exige +100 % para recuperar.

### 4.2 Las simulaciones de aportación periódica de la G5 (recencia, ilusión de control)
- De [G5 §8.1](2026-10-13-G5-acciones-etfs-fondos.md): con el S&P 500 (índice de precio, 2000-2026), la entrada única superó a la aportación periódica en **71 %** de las ventanas de 12 meses, **75 %** de 5 años, **83 %** de 10 años y **91 %** de 15 años; en el peor caso a 10 años, la aportación periódica perdió **-10 %** frente a **-31 %** de la entrada única, y a 5 años perdió **más** (-41 % frente a -36 %).
- **Lectura para sesgos**: no hay una estrategia que quite el riesgo; la tentación es **quedarse con el dato que confirma lo que ya se pensaba** (confirmación) o extrapolar el último tramo (recencia). Las ventanas se **solapan** y la serie es corta: sirven para ilustrar, no para decidir.
- Una caída del S&P 500 de **-53 %** necesitó **+113 %** para volver (100 / 47 - 1) y **5 años y 5 meses** para recuperar el máximo (G5 §8.2).

### 4.3 Cómo un titular repetido alimenta la recencia y la disponibilidad
- **Mecanismo** (descripción, no medición): si un tema (petróleo, regulación) aparece cada día en titulares, es **más fácil recordar** ejemplos de él (disponibilidad) y se le da más peso a lo último que se leyó (recencia), aunque el dato de fondo haya cambiado poco.
- **Ejemplo del propio proyecto**: la [auditoría del 13-oct-2026](../auditoria-2026-10-13.md) detectó que varios dossiers afirmaban «macro y petróleo mandan» como causa de los movimientos de cripto, mientras que los análisis de correlación del propio proyecto **no demostraban causalidad** (dossier 11: correlaciones diarias entre -0,07 y -0,13, según la auditoría). Es un caso de **narrativa que suena a explicación**: una frase repetida se vuelve «hecho» sin haberse medido. La corrección propuesta fue «coincidió con días de macro y petróleo; causalidad no medida».
- **Otro ejemplo de anclaje por un número repetido**: la auditoría encontró que un dossier citaba «Brent spot ~103,9 $» cuando era el **futuro**, y el spot de la EIA estaba en **125,44 $** (6-oct). Un número que se copia entre documentos se «ancla» sin que nadie lo revise [según la auditoría].

## 5. Sesgos, cripto y redes sociales
### 5.1 Qué sabemos de España (CNMV)
- **Estudio de la CNMV sobre criptomonedas** (informe de **mayo-junio de 2022**, población general de **1.500 casos**): el **75,8 %** había oído hablar de las criptomonedas, pero el nivel de conocimiento era **bajo** (solo el **1,4 %** con conocimientos altos y el **6,9 %** medios); el **6,8 %** había invertido alguna vez (**4,2 %** invertía entonces); entre inversores en cripto, el **88 %** recordaba advertencias de riesgo, con un perfil de **hombre de unos 40 años** y **mayor uso de redes sociales y tecnología**; la mayoría invertía **menos del 5 %** de su capital.
- **Limitaciones**: encuesta de 2022 (antes de la quiebra de FTX en nov-2022), muestra pequeña de inversores (300 casos) y **conducta declarada**, no observada. **No sirve como medida de hoy** [VERIFICAR si la CNMV ha publicado una edición posterior].
- Que el 88 % recuerde las advertencias no significa que las advertencias **cambien** la conducta: el estudio mide recuerdo y percepción, no decisiones [ESPECULACIÓN si se interpreta de otra forma].

### 5.2 Patrones que alimentan los sesgos
- **Manada y FOMO**: «todos hablan de X», «última oportunidad», cuentas atrás, capturas de ganancias ajenas. La señal de alarma es la **prisa** ([custodia §7](2026-10-09-custodia-y-seguridad.md): «prisa, rentabilidad garantizada, pedir enviar primero, canal privado, presión para no consultar a nadie»).
- **Influencers y «finfluencers»**: el incentivo del emisor (cobrar por promoción, vender cursos, tener posición propia) no siempre se declara. La CNMV anunció en su plan de 2025 vigilar a los finfluencers [según resultado de búsqueda del 13-oct; no leído el plan; VERIFICAR].
- **«Predicciones» de precio**: números redondos virales (XRP 6 $, 500 $…) son **[ESPECULACIÓN]** o promoción; en el [archivo de patrones de bulos](../../cerebro/documentos/patrones-de-bulos.md) del proyecto están catalogados como «no señal».
- **Bulos y patrones concretos** (de ese archivo, leído, no modificado): cuentas anónimas o de **marca azul** sin respaldo; promesas de **«alianza» o «adopción»** sin documento (un piloto interno no equivale a adopción: ejemplo U.S. Bank en el archivo); cifras redondas enormes en «flash news» sin fuente; **noticias antiguas recicladas como actuales** (CFTC/SEC de marzo de 2026, discursos de Lagarde o del FMI); **falsos anuncios y deepfakes** de directivos; «sorteos» y «doble o nada».

### 5.3 Cómo comprobar una afirmación (fuente primaria)
1. **¿Quién lo dice y qué gana?** Cuenta anónima, conflicto de interés, enlace de afiliación.
2. **¿Hay documento?** Comunicado en el dominio oficial de la empresa, ficha de un registro público (SEC/EDGAR, BOE, CNMV, ESMA, Banco de España, banco central), o contrato.
3. **¿Cuál es la fecha?** Muchos «noticias de hoy» son de otro año; fíjate en fecha y hora.
4. **¿Se puede ver on-chain?** Para movimientos en XRP Ledger o Stellar, un explorador de bloques muestra transacciones reales (según el archivo de patrones de bulos: «traspaso ≠ venta»).
5. **¿Es la entidad que dice ser?** Comprobar en el registro de la CNMV (ver [custodia §4](2026-10-09-custodia-y-seguridad.md)) y desconfiar de mensajes directos.
6. **¿Hay dos fuentes independientes?** Si todas citan a la misma, es **una** fuente.
7. **Si no se puede verificar**, anotar «[VERIFICAR]» y **no actuar** sobre ello como si fuera hecho.

## 6. Estrategias de mitigación (descritas como herramientas)
Son **herramientas descritas**, no recomendaciones. Su eficacia concreta para cada persona **no está demostrada aquí**; la literatura sobre «nudges» y reglas previas es amplia, pero **no la he revisado en esta guía** [VERIFICAR].

| Herramienta | Qué es | Qué sesgo ataca | Límite |
|---|---|---|---|
| **Reglas escritas de antemano (política de inversión)** | Documento propio con objetivos, plazos, reglas de entrada/salida, límites; ver [G13](MAPA.md) (en preparación; no depende de su contenido). | Decidir en caliente; recencia, manada | Una regla que nunca se revisa puede quedar obsoleta; hay que poder cambiarla **en frío**. |
| **Lista de comprobación antes de operar** | Preguntas fijas (ver ejemplo abajo) que se contestan por escrito. | Impulsividad, confirmación | Se puede contestar en automático si no hay disciplina. |
| **Diario de decisiones** | Anotar fecha, motivo, qué se esperaba y qué podría salir mal. | Sesgo retrospectivo, exceso de confianza | Exige honestidad al registrar los fallos. |
| **Periodo de enfriamiento** | Esperar un plazo fijado (horas, días) antes de operar fuera de plan. | FOMO, pánico | Un plazo largo puede hacer perder una oportunidad real; es un coste conocido. |
| **Revisar con calendario, no con noticias** | Fechas fijas de revisión (p. ej. trimestral) en lugar de reaccionar a cada titular. | Recencia, disponibilidad | Si la situación personal cambia, hay que revisar antes. |
| **Diversificar fuentes** | Leer fuentes con opiniones distintas y primarias. | Confirmación | Más fuentes no es mejor si todas son de baja calidad. |
| **Premortem** | Imaginar que la decisión salió mal dentro de un año y escribir por qué. | Exceso de confianza | Puede alimentar el miedo si se usa sin límite. |
| **Abogado del diablo** | Defender la postura contraria o pedir a otra persona que lo haga. | Confirmación, manada | Hay que escoger a alguien sin interés en la operación. |

**Ejemplo de lista de comprobación (modelo editable, no un consejo)**: ¿qué motivo tengo, por escrito? ¿Hay una fuente primaria? ¿Cuál sería el argumento contrario más fuerte? ¿Esta operación está dentro de mi política? ¿Qué coste total tiene (comisiones, horquilla, divisa, impuestos; ver G5 y G12)? ¿Qué pasa si baja un 50 % (§4.1)? ¿Habría decidido lo mismo hace una semana?

## 7. Errores concretos del inversor particular español
### 7.1 Tabla de errores
| Error | Qué ocurre | Dónde profundizar |
|---|---|---|
| **Comisiones ocultas** | El TER no incluye comisión del bróker, horquilla ni cambio de divisa; la diferencia entre 0,2 % y 1,5 % de TER resta ~31 % del capital en 30 años (ejemplo hipotético de G5 §5.3). | [G5 §3.2, §5.3](2026-10-13-G5-acciones-etfs-fondos.md) |
| **Productos complejos** | **Preferentes, estructurados, apalancados, inversos, CFDs, ETNs**: el KID (PRIIPs) los describe; hay riesgo de **perder más de lo previsto** o de contraparte. | G5 §3, §10; §7.2 |
| **Concentrar en la empresa donde se trabaja** | Si falla la empresa se pierden **sueldo y ahorro a la vez** (correlación del riesgo). Un caso clásico (Enron) [VERIFICAR; de memoria]. | [G5 §10](2026-10-13-G5-acciones-etfs-fondos.md) (concentración) |
| **Ignorar la fiscalidad** | Vender un ETF para comprar otro tributa; el fondo permite traspaso sin tributar (art. 94 LIRPF); la compensación de pérdidas tiene límites. | [G12](2026-10-10-G12-fiscalidad-completa.md), [G5 §7](2026-10-13-G5-acciones-etfs-fondos.md) |
| **Ignorar la divisa** | Un activo en dólares expone al EUR/USD: con un dólar un 9,1 % más débil, 1.000 USD pasan de 893 € a 812 € (**-81 €**). | [G5 §5.4](2026-10-13-G5-acciones-etfs-fondos.md) |
| **Comprar por rentabilidades pasadas** | «El que más subió» tiene sesgo de supervivencia y de recencia; no se repite por inercia. | G5 §10; §2 |
| **Vender en pánico** | Convierte una caída temporal en pérdida definitiva (el S&P 500 tardó 5 años y 5 meses en recuperar el máximo de 2007). | G5 §8.2; §4.1 |
| **Apalancarse (hipoteca o préstamo para invertir)** | La deuda se debe aunque el activo caiga; **amplifica pérdidas**. | [G3 (hipotecas y garantías)](2026-10-10-G3-avales-garantias-hipotecas.md) |
| **Confundir ahorro con inversión** | Ahorro (liquidez, depósito, fondo de emergencia) **frente a** inversión (riesgo de pérdida); distintos objetivos y plazos. | [G1](2026-10-10-G1-tipos-e-inflacion.md), [G4](2026-10-10-G4-renta-fija.md), [G13](MAPA.md) |

### 7.2 Dato de contexto sobre productos apalancados (ESMA, fuente primaria)
- **ESMA, nota de prensa del 27-mar-2018**: los análisis de los supervisores nacionales sobre **CFDs** en distintas jurisdicciones de la UE mostraban que **entre el 74 % y el 89 %** de las cuentas minoristas **perdía dinero**, con pérdidas medias por cliente de **entre 1.600 y 29.000 €** (según la propia nota). Condujo a restricciones a los CFDs y a la prohibición de las opciones binarias.
- **Limitaciones**: datos de 2018, solo CFDs; ESMA atribuye las pérdidas a las **características del producto** (apalancamiento, complejidad), no solo al comportamiento del inversor. Es un ejemplo de **regulación basada en datos**, no una medida del sesgo.

## 8. Autoevaluación: 10 preguntas sí/no
Pensado para **detectar patrones propios**, **sin puntuación ni diagnóstico**. Si respondes «sí» a varias, puede ser útil mirar las secciones indicadas; si respondes «no», no significa que no tengas sesgos (la **autoevaluación** también está sesgada).
1. ¿He comprado algo en las últimas semanas principalmente porque «todo el mundo hablaba de ello»? (manada/FOMO, §2)
2. ¿Puedo explicar por escrito el mejor argumento **en contra** de mi última decisión importante? (confirmación)
3. ¿He operado más en los últimos meses, tras una racha de aciertos? (exceso de confianza, §3.2)
4. ¿Dejo de mirar alguna posición cuando está en negativo, o la miro mucho cuando sube? (aversión a las pérdidas)
5. ¿Tengo alguna posición que mantengo «hasta recuperar lo que pagué»? (anclaje, coste hundido)
6. ¿Suelo vender antes lo que sube y mantener lo que baja? (efecto disposición, §3.3)
7. ¿Mis decisiones cambian según el origen del dinero (sueldo frente a «ganancia»)? (contabilidad mental)
8. ¿Mis fuentes de información piensan casi todas lo mismo que yo? (confirmación, §6)
9. ¿Sé cuánto pagaría en comisiones, impuestos y divisa por la última operación? (§7)
10. ¿He decidido alguna vez algo importante tras ver un mensaje con prisa o un «último día»? (§5)

## 9. Errores y señales a vigilar
1. **Tratar esta lista como diagnóstico**: los sesgos son tendencias de todos, no etiquetas.
2. **Confundir estudio con regla**: Barber y Odean, Odean y Morningstar describen **muestras y periodos**, no leyes.
3. **Causalidad no demostrada**: la diferencia entre fondo e inversor **no prueba** que el inversor «se equivoque» (puede ser aportar cada mes).
4. **Fuentes sin primaria**: titulares, hilos de redes, rankings con afiliación.
5. **Usar la guía para justificar una decisión ya tomada** (confirmación).
6. **Señales a vigilar**: prisa, fecha ausente, cifras redondas sin fuente, «garantizado», canal privado, presión para no consultar.

## 10. Lo que no sé / no verifiqué
- **Primaria leída hoy**: Barber y Odean (2000), Odean (1998), Morningstar «Mind the Gap 2025» (PDF oficial), ECF 2021 del Banco de España, estudio de cripto de la CNMV (2022), nota de prensa de ESMA (27-mar-2018) y la página de *Econometrica* para Kahneman y Tversky (solo resumen).
- **No leí el texto completo** de Kahneman y Tversky (1979), solo el resumen de la revista. El rango de páginas varía según la fuente [VERIFICAR].
- **Nobel (Thaler 2017, Shiller 2013)**: solo resultados de búsqueda del dominio nobelprize.org; no abrí las páginas completas. **Nobel de Kahneman en 2002**: de memoria.
- **No verificado**: críticas recientes a la aversión a las pérdidas (Gal y Rucker, 2018); explicaciones alternativas del efecto disposición; edición 2026 de «Mind the Gap»; caso Enron; plan de la CNMV 2025 sobre finfluencers.
- **No consulté** estudios de ESMA ni de la CNMV sobre sesgos de minoristas (la búsqueda del 13-oct no devolvió un informe de ESMA específico sobre sesgos; el más cercano es un informe de **IOSCO de 2019** sobre «behavioural insights» que **no he leído**), **ni datos de la OCDE** sobre alfabetización financiera.
- **Evidencia española sobre exceso de negociación o efecto disposición**: no encontrada en esta sesión [VERIFICAR; puede haber estudios de la CNMV o de universidades].
- **Eficacia de las herramientas de §6**: no revisé evidencia; son descripciones.
- **Datos del proyecto** (prueba de estrés, G5): se usan tal como figuran en esos documentos; sus fuentes (Yahoo Finance) son secundarias.

## 11. Guías relacionadas
- [G1](2026-10-10-G1-tipos-e-inflacion.md) (tipos e inflación), [G4](2026-10-10-G4-renta-fija.md) (renta fija), [G5](2026-10-13-G5-acciones-etfs-fondos.md) (acciones, ETFs y fondos), [G12](2026-10-10-G12-fiscalidad-completa.md) (fiscalidad), [G9](2026-10-13-G9-commodities.md) (commodities), [dossier de custodia](2026-10-09-custodia-y-seguridad.md) y [prueba de estrés](2026-10-09-prueba-de-estres.md).
- **G13** (gestión patrimonial) y **G15** (asesores y entidades) están en preparación; ver [MAPA](MAPA.md).
