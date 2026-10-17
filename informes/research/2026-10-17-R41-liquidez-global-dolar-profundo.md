# Liquidez global y dólar: balance de la Fed, TGA, RRP, rendimientos, dólar, BCE y BoJ (2026-10-17, R41 profundo)

Plantilla: dossier-region (modo profundo). Etiquetas: **LEÍDO ENTERO** = nota/comunicado/actas descargados y leídos (curl + texto) · **LEÍDO (tabla)** = tabla o serie oficial descargada y leída, sin texto explicativo · **extracto** = parte de una página oficial · **secundaria** = prensa o agregador [VERIFICAR] · **cálculo mío** = operación aritmética sobre datos oficiales. Sin recomendaciones de compra/venta; los canales de transmisión a XRP/XLM son [ESPECULACIÓN].

**Acceso:** abrieron con curl y User-Agent identificado federalreserve.gov (H.4.1, H.10, H.15, comunicado e Implementation Note del 16-sep, actas del 15–16-sep), home.treasury.gov (curva de rendimientos diaria, XML), api.fiscaldata.treasury.gov (Daily Treasury Statement, saldo de la TGA) y ecb.europa.eu (estado financiero semanal, tras una redirección 301). **No abrió:** fred.stlouisfed.org (sin respuesta en 20 s, 3 intentos; no hay serie larga de FRED). **No leído:** cuentas del BoJ (la página de índice abre pero no localicé el fichero del 9/10-oct), serie histórica del índice del dólar (H.10 solo trae la semana), DXY de ICE (índice privado, sin fuente primaria abierta).

## Resumen (5 líneas)
1. **El balance de la Fed ya no se encoge y las compras de reservas están en pausa.** Activos totales **6.755,6 mil M$** el 14-oct (+159,2 mil M$ en un año, +2,4 %); las letras del Tesoro suben **+370,0 mil M$** y las hipotecas (MBS) bajan **−187,9 mil M$** en el año (H.4.1 del 15-oct, LEÍDO ENTERO). El FOMC del 16-sep mantiene "ample reserves", reinvierte las MBS en letras y las actas (7-oct) dicen que el Desk **pausó las compras de gestión de reservas (RMP)**.
2. **La liquidez en dólares no es abundante en el margen:** reservas bancarias medias **3.022,1 mil M$**, TGA (cuenta del Tesoro en la Fed) **885,8 mil M$** el 14-oct y **934,7 mil M$** el cierre del 15-oct (DTS), RRP de contrapartes internas prácticamente **0** (287 M$ de media) y el único saldo de "reverse repo" relevante, **332,2 mil M$**, es el de cuentas de bancos centrales y organismos extranjeros, no un colchón del mercado monetario.
3. **El precio del dinero largo es lo que más ha cambiado:** el rendimiento del Tesoro a 10 años cerró en **5,09 %** el 16-oct (máximo del periodo analizado **5,31 % el 5-oct**, mínimo **4,38 % el 26-jun**); el de 30 años **5,43 %**; el de 2 años **4,74 %**. La Fed sube a 3,75–4,00 % y la curva 2–10 años mide **+0,35 pp** (cálculo mío).
4. **Dólar fuerte pero sin serie larga abierta:** el índice amplio de la Fed fue **121,27–121,60** (5–9-oct, base ene-2006 = 100); euro **1,1193 $**, yen **158,34/$**, yuan **6,692/$** (H.10, 9-oct). No pude comparar con meses anteriores con fuente primaria: el nivel es dato, la "fortaleza" es [VERIFICAR] sin serie.
5. **Contexto de otros bancos centrales:** el Eurosistema sigue reduciendo cartera (programas de compras de política monetaria **3.316,3 mil M€**, cálculo mío, con APP y PEPP cayendo por vencimientos; BCE 13-oct) y el BoJ subió a 1,25 % (R29). Para XRP/XLM el dato relevante es el **conjunto**: tipos largos al alza, liquidez neta estable-baja y dólar alto = entorno de **riesgo**, no catalizador propio.

## Qué es hecho verificado
| Dato | Fuente primaria | Fecha | Nivel / idioma |
|---|---|---|---|
| Fed sube el rango de fed funds 1/4 pp a **3¾–4 %**; voto **12–0**; "continuing its policy of maintaining ample reserves"; "Inflation remains elevated" | federalreserve.gov, comunicado FOMC | 16-sep-2026 | LEÍDO ENTERO, EN |
| Interés sobre reservas (IORB) **3,90 %** desde el 17-sep; repo permanente **4,0 %**; reverse repo permanente **3,75 %** con tope de **160 mil M$** por contraparte y día; tasa de descuento (primary credit) **4,0 %** | federalreserve.gov, Implementation Note | 16-sep-2026 | LEÍDO ENTERO, EN |
| Directiva al Desk: "increase the SOMA holdings of securities through purchases of Treasury bills and, if needed, other Treasury securities with remaining maturities of 3 years or less to maintain an ample level of reserves"; reinvertir todo el principal del Tesoro en subastas y las MBS **en letras** | federalreserve.gov, Implementation Note | 16-sep-2026 | LEÍDO ENTERO, EN |
| Actas: el Desk "had paused reserve management purchases (RMPs)"; el ritmo de RMP "was not on a preset course"; reservas "within a range consistent with an ample supply"; fuerte aumento de emisión de letras desde julio absorbido "with limited effect on money market rates"; algunos participantes piden planificar tensión de mercado y limitar "the Federal Reserve's footprint in the Treasury market"; **otra subida "would likely be appropriate by year end"** (según la formulación de los participantes) | federalreserve.gov, actas del FOMC 15–16-sep (publicadas 7-oct) | 7-oct-2026 | LEÍDO ENTERO (secciones de mercados y balance), EN |
| Activos totales de la Fed (miércoles 14-oct): **6.755.639 M$**, +8.079 M$ en la semana y +159.185 M$ en el año; valores mantenidos en propiedad (media semanal): **6.470.368 M$** (Tesoro **4.569.911**; letras **565.492**, +369.999 en el año; bonos nominales 3.617.961; MBS **1.898.110**, −187.885 en el año) | federalreserve.gov, H.4.1 tablas 1 y 5 | 15-oct-2026 | LEÍDO (tabla), EN |
| Reservas de bancos en la Fed: media semanal **3.022.140 M$**; miércoles **3.030.854**. Circulación de efectivo **2.488.264 M$** (media) | H.4.1 tabla 1 | 15-oct-2026 | LEÍDO (tabla), EN |
| TGA (cuenta general del Tesoro) en la Fed: media semanal **883.373 M$** (+73.780 M$ en el año); miércoles **885.823**. En el DTS: apertura 15-oct **885.823**, cierre **934.690 M$** (depósitos 449.175; retiros 400.307 M$) | H.4.1 tabla 1; fiscaldata.treasury.gov (DTS, Operating Cash Balance) | 15-oct-2026 | LEÍDO (tabla), EN |
| Reverse repo: total **332.191 M$** (media semanal), de los cuales **cuentas de oficiales extranjeros y organismos internacionales 331.904** y **"Others" (contrapartes del mercado) 287 M$** (−943 M$ semanal; −3.998 M$ anual) | H.4.1 tabla 1 | 15-oct-2026 | LEÍDO (tabla), EN |
| Curva de rendimientos del Tesoro (cierre 16-oct): 3 meses **4,26 %**, 2 años **4,74 %**, 5 años **4,89 %**, 10 años **5,09 %**, 20 años **5,47 %**, 30 años **5,43 %** | home.treasury.gov, Daily Treasury Par Yield Curve Rates | 16-oct-2026 | LEÍDO (tabla), EN |
| Serie del 10 años (96 observaciones diarias, 1-jun a 16-oct): 1-jun **4,47 %**; 30-jun 4,44; 31-jul 4,75; 31-ago 4,75; 15-sep 5,00; 16-sep 5,01; 17-sep 4,94; **30-sep 5,29**; **máximo 5,31 (5-oct)**; 14-oct 5,19; 15-oct 5,10; 16-oct 5,09; mínimo 4,38 (26-jun). 2 años: 4,05 (1-jun) → 4,88 (30-sep) → 4,74 (16-oct) | home.treasury.gov, curvas mensuales jun–oct (XML) | 2026 | LEÍDO (tabla), EN; máximos y mínimos = cálculo mío |
| H.10 (semana 5–9-oct): índice amplio del dólar **121,2708 / 120,8976 / 121,2558 / 121,4469 / 121,6023** (AFE 115,24; EME 129,77 el 9-oct); euro 1,1193 $; yen 158,34/$; yuan 6,6920; rupia 96,73; real 4,9790; libra 1,3229 $ | federalreserve.gov, H.10 (publicación 13-oct) | 13-oct-2026 | LEÍDO (tabla), EN |
| Eurosistema (9-oct): posición neta en divisa **349,6 mil M€**; dinero base **3.919,7 mil M€** (−2,7); programas de política monetaria: CBPP3 **185,6**, ABSPP 1,7, PSPP **1.646,2** (−8,6 sem.), CSPP **213,1**, PEPP **1.269,7** (−5,7 sem.) mil M€ | ecb.europa.eu, estado financiero semanal consolidado | 13-oct-2026 | LEÍDO ENTERO (texto y tabla 1), EN |

### Cálculos míos (con las cifras de arriba; no son datos oficiales)
| Cálculo | Resultado |
|---|---|
| Crecimiento anual de los activos de la Fed: 159.185 / (6.755.639 − 159.185) | **+2,4 %** |
| Cambio en el año de letras (+369.999) frente a Tesoro total (+373.157) | las letras explican el **99 %** del aumento de títulos del Tesoro |
| "Liquidez neta" aproximada = activos totales − TGA − RRP **total** (6.755,6 − 885,8 − 326,8; miércoles 14-oct) | **≈ 5.543 mil M$** |
| Igual, restando solo el RRP de contrapartes de mercado ("Others", 0,2 mil M$) | **≈ 5.870 mil M$** |
| Curva 10 años − 2 años (16-oct) | **0,35 pp** |
| 10 años: 16-oct frente a máximo del 5-oct | **−22 pb**; frente al 1-jun: **+62 pb** |
| Programas de política monetaria del Eurosistema (suma de la tabla 1) | **3.316,3 mil M€** |

La "liquidez neta" es una **heurística de agregadores y de analistas**, no una magnitud oficial de la Fed; los dos cálculos dan 330 mil M$ de diferencia según cómo se trate el repo de cuentas extranjeras, lo que ya muestra que el indicador no es robusto. No se debe citar como "liquidez de la Fed" sin esa nota.

## Qué está sin verificar o es opinión
- **Que la liquidez "mueva" a XRP/XLM:** es una relación estadística debatida; no hay estudio primario leído en esta sesión [ESPECULACIÓN]. Lo verificable es el nivel de cada magnitud, no su efecto en precio.
- **Cuándo volverán las RMP:** las actas dicen que no hay ritmo prefijado [VERIFICAR] en el próximo FOMC del 27–28-oct.
- **Que "la Fed hará otra subida antes de fin de año":** son palabras de las actas sobre lo que *consideraron apropiado* algunos participantes; no es compromiso ni previsión de la Fed. Titulares que lo presenten como decidido = sesgo.
- **Que el yen/BoJ esté drenando liquidez global ("carry trade"):** no leí cuentas del BoJ ni posicionamiento; es narrativa de prensa [ESPECULACIÓN].
- **DXY:** el DXY de ICE no es el índice de la Fed (composición distinta); no mezclar cifras de uno y otro.
- **Series de FRED/WALCL/RRPONTSYD citadas por agregadores:** FRED no abrió; he usado la H.4.1 y fiscaldata, que son la fuente de origen de esas mismas series.

## Caso alcista / caso bajista (para el riesgo cripto; datos, no recomendación)
**Alcista:** el balance de la Fed ya crece (+2,4 % anual) y el FOMC dejó por escrito comprar letras "para mantener reservas amplias"; la ventanilla de repo permanente a 4,0 % y los 160 mil M$ de RRP permanente dan suelo a los mercados de financiación; el rendimiento del 10 años bajó 22 pb desde el 5-oct; el TGA es alto pero estable (883–935 mil M$), sin drenaje nuevo visible en la tabla.
**Bajista:** las RMP están **pausadas** (actas); el 10 años a 5,09 % y el 30 años a 5,43 % encarecen cualquier activo sin flujo de caja; el FOMC y las actas hablan de subir más; la heurística de liquidez neta ronda 5,5–5,9 billones y cae si el TGA sube con la emisión de letras (+370 mil M$ en un año las compra la Fed, pero el aumento de emisión desde julio lo absorbe el mercado); BCE y BoJ no compensan (cartera del Eurosistema en descenso; BoJ en 1,25 %).

## Qué cambia para los digital assets
- **XRP/XLM:** nada específico en estos datos; el canal es **tipo real y dólar**. La stablecoin y el colateral en bonos del Tesoro (R25/R26) sí dependen del nivel de tipos: a 4,26 % en 3 meses el rendimiento de reservas de stablecoins en letras es alto (hecho: curva del Tesoro), de lo que se benefician los emisores (R25).
- **Tokenización (R26):** fondos tokenizados de letras compiten con los tipos de depósitos; el nivel de 3 meses al 4,26 % lo explica, no un cambio regulatorio.
- **Riesgo de narrativa:** titulares de "inyección de liquidez de la Fed" suelen mezclar RMP, repo y swaps; distinguir cuál es (H.4.1: repo = 1 M$ de media, swaps con bancos centrales 205 M$, préstamos primarios 11.312 M$).

## Fechas próximas (catalizadores) con fuente
| Fecha | Evento | Fuente | Estado |
|---|---|---|---|
| 22-oct (jue) | H.4.1 semanal (miércoles 21-oct) | federalreserve.gov/releases/h41 | calendario de la Fed (publicación semanal) [VERIFICAR] fecha exacta |
| 27–28-oct | FOMC (con comunicado y posible nota de implementación) | federalreserve.gov (calendario, R29) | oficial |
| 29-oct | BCE (decisión) | ecb.europa.eu (R29) | oficial |
| 29–30-oct | BoJ con Informe de Perspectivas | boj.or.jp (R29) | oficial |
| ~28-oct | Actas del FOMC: 3 semanas después → ~18-nov | federalreserve.gov | [VERIFICAR] |
| 8–9-dic | FOMC con proyecciones | federalreserve.gov | oficial |

## Qué falta por buscar
1. Serie histórica del índice amplio del dólar (H.10 mensual/anual, o FRED DTWEXBGS) para decir si 121,3 es alto o bajo; FRED no abrió.
2. Cuentas del BoJ (activos totales, tenencias de JGB) y ritmo actual de compras.
3. Texto del comunicado del BCE del 10/16-sep y proyecciones de balance; solo leí el estado semanal.
4. Subasta de letras: calendario de emisión del Tesoro (TBAC, anuncio de refinanciación trimestral) para estimar el TGA futuro.
5. Tamaño de las RMP anteriores (cuántos mil M$ al mes compró el Desk) en nyfed.org; solo sé que están pausadas y que las letras subieron 370 mil M$ en el año.
6. Una segunda fuente independiente (BIS/FMI) sobre el canal liquidez → activos de riesgo; no lo busqué en esta pasada.
