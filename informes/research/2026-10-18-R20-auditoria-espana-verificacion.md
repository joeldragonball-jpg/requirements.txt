# R20 · Auditoría España (BOE/AEAT): verificación de los [VERIFICAR] fiscales de cripto (2026-10-18)

**Informativo. NO es asesoramiento fiscal.** Joel tendrá asesor; esto sirve para llevarle preguntas con fuente. Única auditoría de España del ciclo (el research es global). Alcance: los [VERIFICAR] de mayor peso del [dossier de fiscalidad España](../dossiers/2026-10-09-fiscalidad-espana-xrp-xlm.md) y de [R35](2026-10-17-R35-fiscalidad-cripto-internacional-profundo.md); no se tocó ningún dossier ni el cerebro salvo las líneas permitidas.
Etiquetas: **[P]** = fuente primaria leída hoy · **[S]** = secundaria · **[VERIFICAR]**. Resultados: **CONFIRMADO / CORREGIDO / PARCIAL / SIGUE SIN VERIFICAR**.
Accesos del 18-oct-2026: BOE consolidado con `curl` (IRPF: «última actualización 07/10/2026»; LGT, orden 721) y AEAT con WebFetch (manual de Renta 2025 y FAQ del 721). Sin errores de acceso.

## Resumen (5 líneas)
1. **FIFO y permuta pasan a [P]:** el Manual práctico de Renta 2025 de la AEAT (página del 17-mar-2026) dice que se entiende transmitidas «las adquiridas en primer lugar» (criterio FIFO) y que en una permuta el valor de transmisión es el mayor entre el valor de mercado de lo recibido y de lo entregado; antes solo constaba por DGT/secundaria.
2. **Modelo 721 — umbral confirmado, pero no está en la orden:** la FAQ de la AEAT (act. 8-sep-2026) dice que no hay obligación si los saldos conjuntos a 31-dic no superan **50.000 €**, y que si se superan hay que informar de **todas** las monedas; la orden HFP/886/2023 (BOE-A-2023-17429) no contiene «50.000». Plazo: 1-ene a 31-mar. Base legal de la obligación: DA 18ª LGT, letra d) (monedas virtuales en el extranjero custodiadas por terceros).
3. **Sanciones: contradicción resuelta en parte.** Hoy mandan los arts. 198 y 199 LGT: fuera de plazo, 20 € por dato (mín. 300, máx. 20.000); incompleta o inexacta, 200 € por dato (sin magnitudes monetarias) o hasta el 2 % de las operaciones, mín. 500 € (con magnitudes monetarias). El «mínimo 10.000 €» de una asesoría no figura en esos artículos [ESPECULACIÓN: probablemente es el régimen especial anterior, ya fuera de la DA 18ª].
4. **Regla de recompra sin resolver:** el art. 33.5 e) (BOE) habla de «elementos patrimoniales» y año siguiente; f) y g) hablan de «valores o participaciones». El manual de la AEAT no menciona recompra para cripto. **No hay fuente que diga si e) alcanza a la cripto.**
5. **Sigue sin verificar:** DAC8 (no hay ley, RD ni Orden publicados que yo localice; solo proyectos), números de casilla de Renta 2025, staking/airdrops, comisiones pagadas en cripto y la firmeza del TSJ vasco.

## Tabla de verificación
| # | Afirmación (origen) | Resultado | Fuente [P] | Fecha |
|---|---|---|---|---|
| 1 | Las ventas parciales siguen FIFO (dossier §1.5, antes DGT/secundaria) | **CONFIRMADO [P]**: «las que se transmiten son las adquiridas en primer lugar» | [AEAT, Manual Renta 2025, compra-venta de monedas virtuales](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c11-ganancias-perdidas-patrimoniales/monedas-virtuales/compra-venta-monedas-virtuales-tributacion-inversor.html) | pág. 17-mar-2026 |
| 2 | Permuta cripto-cripto = ganancia/pérdida; valor = el mayor de los dos (dossier §4.1) | **CONFIRMADO [P]**: valor de transmisión = mayor entre valor de mercado de lo recibido y de lo entregado; lo recibido se adquiere por ese valor | AEAT (misma página) | 17-mar-2026 |
| 3 | Gastos y comisiones de la operación (dossier, «sin consulta específica») | **PARCIAL**: en ventas por euros la AEAT dice que se consideran «los gastos y tributos» de la operación; no detalla permutas ni comisiones pagadas **en cripto** | AEAT (misma página) | 17-mar-2026 |
| 4 | Pérdidas se compensan en el año; saldo negativo, 25 % contra capital mobiliario y 4 años | **CONFIRMADO [P]** (art. 49.1 a y b; también entre ganancias y pérdidas patrimoniales) | [BOE, Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764), art. 49 (redacción en vigor desde 1-ene-2015) | texto a 7-oct-2026 |
| 5 | Recompra: art. 33.5 e) (año) y f) (2 meses) frente a cripto (dossier §1.4, «sin consulta DGT») | **TEXTO CONFIRMADO; aplicación a cripto SIGUE SIN VERIFICAR.** e) «elementos patrimoniales… vuelva a adquirirlos dentro del año siguiente»; f) valores admitidos a negociación y valores homogéneos en 2 meses; g) valores no admitidos, año anterior o posterior. La AEAT no menciona recompra para cripto | BOE, art. 33.5; AEAT (sin mención) | 7-oct y 17-mar-2026 |
| 6 | Modelo 721: umbral 50.000 € (R35, secundaria) | **CONFIRMADO [P]** en la FAQ de la AEAT; **no figura en la orden** (0 coincidencias de «50.000») | [AEAT FAQ 721](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721/respecto-que-monedas-virtuales-no-informacion.html); [Orden HFP/886/2023](https://www.boe.es/buscar/doc.php?id=BOE-A-2023-17429) | 8-sep-2026; BOE 29-jul-2023 |
| 7 | Plazo del 721 | **CONFIRMADO [P]**: 1-ene a 31-mar del año siguiente | Orden HFP/886/2023 (art. 4) | 29-jul-2023 |
| 8 | Base legal de informar monedas virtuales en el extranjero | **CONFIRMADO [P]**: DA 18ª LGT, letra d) (custodiadas por quienes salvaguardan claves privadas); «última actualización 10/03/2022» | [BOE, Ley 58/2003 (LGT)](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | texto consolidado |
| 9 | Sanciones por declaraciones informativas: «20 €/dato, mín. 300, máx. 20.000» frente a «mínimo 10.000» (dossier §DAC8, contradicción de secundarias) | **CORREGIDO parcialmente**: art. 198.1 (fuera de plazo) = 20 €/dato, mín. 300, máx. 20.000 [P]; art. 199.4 = 200 €/dato (sin magnitudes monetarias); art. 199.5 = hasta el 2 % de lo no declarado o mal declarado, mín. 500 € [P]. El «mínimo 10.000» no aparece; el texto leído de la DA 18ª no contiene régimen sancionador | BOE, LGT arts. 198 y 199 | texto consolidado |
| 10 | Orden HAC/1504/2024 modifica anexos de HFP/886 y 887 | **NUEVO HECHO [P]**: existe y modifica los anexos de las órdenes de los modelos 721 y 172; **no leí el texto consolidado** [VERIFICAR antes de usar los anexos] | [BOE-A-2024-27528](https://www.boe.es/buscar/doc.php?id=BOE-A-2024-27528) | 31-dic-2024 |
| 11 | DAC8: ley, RD y Orden (modelos 172, 175, 721, 042) | **SIGUE SIN VERIFICAR**: solo localizo **proyectos** (RD de 28-jul-2025 y Orden de 9-mar-2026) en hacienda.gob.es; ninguna publicación en el BOE | hacienda.gob.es (proyectos) | búsqueda 18-oct-2026 |
| 12 | Casillas «1800–1814» frente a «1626/0033» | **SIGUE SIN VERIFICAR**: el manual de 2025 confirma el apartado F2 «transmisión o permuta de monedas virtuales», pero no obtuve los números de casilla de 2025; 1800–1814 vienen del Modelo 100 de 2022 | AEAT, apartado F2 | 2025 |
| 13 | Staking, airdrops y recompensas | **SIGUE SIN VERIFICAR [P]**: la página de la AEAT no los menciona; queda la doctrina DGT [S] | AEAT (silencio) | 17-mar-2026 |
| 14 | Firmeza del TSJ País Vasco (9-ene-2025, rec. 75/2024) | **NO INTENTADO**: afecta al IRPF foral, no al régimen común | — | — |
| 15 | ITSGF, ETP/ETN (V0267-25), dividendos, inmuebles (G12) | **NO INTENTADO** (fuera del alcance de una tarea de 1 %) | — | — |

## Qué cambia en lo que ya escribimos (propuesta; NO aplicada, espero OK de Joel)
- Dossier 13 (fiscalidad España) §1.5 y §4: subir FIFO y permuta de «DGT, secundaria» a **«AEAT, Manual Renta 2025 [P]»** (cambio de etiqueta).
- Dossier 13 y R35: el umbral del 721 de «secundaria» a **[P] (FAQ AEAT, 8-sep-2026)**, aclarando que **no está en la orden**.
- Dossier 13 (DAC8, sanciones): sustituir la contradicción por los importes de los arts. 198 y 199 LGT.
- Los números de casilla 1800–1814 deben salir como **no verificados para Renta 2025**.

## Hechos y opiniones
- **Hecho:** los textos del BOE y de la AEAT citados arriba (leídos hoy).
- **Opinión mía [ESPECULACIÓN]:** que e) pueda alcanzar a la cripto por su redacción amplia («elementos patrimoniales») es una lectura literal, no una doctrina; no hay consulta ni sentencia leída. Es la pregunta más importante para el asesor sobre las ventas con pérdida.

## Para el asesor (resumen)
1. ¿Se aplica el art. 33.5 e) (recompra en el año siguiente) a cripto? ¿Afecta a una venta con pérdida si luego se recompra?
2. ¿Los saldos en exchanges extranjeros cuentan para el 721? ¿Se suman conjuntamente a 31-dic y a precio de mercado?
3. ¿Cómo declaro una comisión pagada en la propia cripto?

## Qué falta por buscar
- Números de casilla del Modelo 100 de Renta 2025 (apartado F2).
- Texto consolidado de la Orden HFP/886/2023 con los anexos tras la Orden HAC/1504/2024.
- Publicación en el BOE de la ley, RD y Orden de DAC8 (vigilar boe.es y hacienda.gob.es).
- Doctrina DGT sobre recompra y sobre comisiones pagadas en cripto (la base de la DGT, petete, no se consultó).
