# C29 · Petróleo, Ormuz y guerra ↔ noticias ↔ Órbita

Fecha: 2026-10-30 · Sin recomendaciones de compra/venta · Etiquetas: [P] primaria leída · [S] prensa o titular · [VERIFICAR] · [ESPECULACIÓN]

## 1. Resumen
1. Los hitos diplomáticos y militares de octubre salen de los informes diarios del repo (titulares de CoinDesk, CNBC, Al Jazeera y el bot) **[S]**: no abrí comunicados oficiales de la Casa Blanca ni de Teherán.
2. **La «caída del 5-6 % tras la noticia de Teherán» (26-oct) depende de cómo se mida.** Del máximo intradía del viernes 23-oct (114,4 $) al mínimo del lunes (109,4 $) es −4,4 %; de cierre a cierre, solo −1,2 %. La cifra 116,72 → 109,84 que circuló no se reproduce con la serie horaria (máximo 114,4 $) **[VERIFICAR]**.
3. Con el **spot de la EIA** (otra serie, no comparable) la caída del 23 al 27-oct sí es de −4,1 % (128,30 → 123,10 $) **[P]**. Spot y futuros difieren en unos 12-18 $, así que no se pueden mezclar.
4. En 4 de 6 hitos el movimiento de cierre es pequeño (≤ 1,2 %) y el pico fue intradía. Solo el 22-oct (+2,8 %) y el 16-oct (+4,0 %, causa sin documentar) destacan.

## 2. Cronología (HECHOS) y precio
Brent / WTI = futuros continuos, último valor horario del día (UTC); «antes» = día previo. Fuente de precios: Yahoo Finance (BZ=F, CL=F) **[S]**.

| Fecha | Hecho (fuente) | Brent antes → después | WTI antes → después |
|---|---|---|---|
| 9-oct | Trump: sin ataque a Irán antes del 3-nov (bot; primaria sin abrir) [S][VERIFICAR] | 103,82 → 104,72 (+0,9 %) | 91,17 → 91,85 (+0,7 %) |
| 16-oct | Salto sin causa documentada [VERIFICAR] | 105,62 → 109,86 (+4,0 %) | 96,15 → 99,02 (+3,0 %) |
| 21-oct | «Fallan las conversaciones con Irán» (bot) [S] | 109,34 → 110,04 (+0,6 %) | 98,42 → 97,99 (−0,4 %) |
| 22-oct | Ataques hutíes, dron en Shaybah (Bloomberg vía CNBC); «7 petroleros» según la Guardia Revolucionaria, desmentido por CENTCOM (Al Jazeera) [S] | 110,04 → 113,08 (+2,8 %) | 97,99 → 99,29 (+1,3 %) |
| 23-oct | Titulares «114 $» y «117 $» (bot, CoinDesk) [S] | 113,08 → 111,70 (−1,2 %); máx. 114,4 | 99,29 → 103,27 (+4,0 %) |
| 26-oct | Mediadores de Catar en Teherán; FT: enviados saudíes, paquistaníes y turcos; Trump «sin ataque el domingo» [S] | 111,70 → 110,37 (−1,2 %) | 103,27 → 101,49 (−1,7 %) |

Contexto estructural: PortWatch contaba 3,7 barcos/día por Ormuz (hasta el 18-oct) frente a 78,3 en febrero **[P]** (W10); CENTCOM dice que el 95 % de los buques pasa **[S]**; son versiones que no cuadran.

## 3. Alcista / bajista y sesgos
- **Para el precio al alza:** ataques a infraestructura saudí, minas y petroleros alcanzados, tráfico de petroleros en mínimos de dos meses (W41, Bloomberg) **[S]**.
- **A la baja:** vías diplomáticas (Catar, FT), Trump hablando de conversaciones «productivas», flujos de Oriente Medio cerca de niveles previos a la guerra (Bloomberg, W43) **[S]**.
- **Sesgos:** las dos fuentes principales de las noticias de acuerdo son filtraciones («fuentes sin nombre» del FT) y declaraciones de Trump que dejan la opción militar abierta; Irán y EE. UU. se desmienten sobre los barcos; los titulares de máximos intradía se leen como cierres.

## 4. Límites
Correlación en el tiempo no es causa: el mismo día coinciden Fed, datos macro y rumores. Seis hitos son una muestra mínima. Brent y WTI se mueven a veces en sentido contrario (contrato/calendario, **[VERIFICAR]**). Opiniones o previsiones de precio: **[ESPECULACIÓN]**, no incluidas.

## 5. Qué se tocó
- `explorador/hitos_petroleo.json` (datos del desplegable del móvil) y capa «Energía y Ormuz» de `explorador/datos.json` (6 hitos con campo «informe»).
- `research/gemini/NOTICIAS-DIA.md`: la tanda `energia-geopolitica` pregunta ahora por negociaciones, treguas y fechas.
- Móvil: Mercado → «Petróleo y guerra: últimos hitos» (desplegable, cerrado).
