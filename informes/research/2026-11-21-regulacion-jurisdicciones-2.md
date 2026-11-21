# Regulación: Singapur, Japón, Canadá, Suiza y Corea (21-nov-2026)

Alcance real: pasada corta. Casi todas las celdas de estas jurisdicciones ya eran [P]; se cerraron huecos concretos. Los lectores de páginas resumen: lo marcado [P] se leyó en la página oficial; las citas literales vienen del lector (ver [VERIFICAR]).

## HECHOS leídos en fuente oficial [P]
- **Canadá (Gazette, Parte I, vol. 160 n.º 43, 24-oct-2026)**: proyecto de Stablecoin Regulations (Finanzas): 60 días de comentarios; «la intención es que entren en vigor en otoño de 2027»; reserva en la moneda de referencia con custodio canadiense cualificado; redención en 3 días hábiles, comisión máxima 1 %; prohibido el rendimiento por tenencia (recompensas por transacción permitidas); informes mensuales; sanciones hasta 1 M$ y 10 M$; afecta a ~30 proveedores de pago más. Nota: el lector leyó solo los primeros 100.000 de 188.291 caracteres.
- **Canadá (Stablecoin Act, S.C. 2026 c. 3 s. 600, Justice Canada)**: sanción real 26-mar-2026; no en vigor (art. 97, orden del Gobierno); art. 32 prohíbe pagar intereses o rendimiento; art. 37 exige reserva ≥ valor nominal.
- **Suiza (Consejo Federal, admin.ch)**: 22-oct-2025 abre consulta sobre la FinIA: licencia «payment instrument institution» (sustituye a la fintech, sin tope de CHF 100 M, puede emitir un tipo especial de stablecoin) y licencia de «crypto-institution»; plazo hasta 6-feb-2026. No se halló mensaje al Parlamento (la SIF lo situaba «como pronto» en el 2.º semestre de 2026). El PDF de la hoja informativa no se pudo leer como texto.
- **Japón (FSA, página de proyectos de la 221.ª sesión)**: reforma de la FIEA y la Ley de Servicios de Pago «presentada el 10-abr-2026, aprobada el 15-jul-2026». Celda de ley marco subida de [S] a [P] en ese punto. La página no da contenido ni número de ley; el contenido (cripto a la FIEA, información privilegiada, vigencia por orden del Gabinete en ≤ 1 año) sigue en prensa [S]. Acta de la ministra (10-abr): la reforma desarrolla «el marco legal para revisar las reglas aplicables a los criptoactivos».
- **Singapur (MAS, 1-sep-2026)**: consulta sobre enmiendas a la PS Act para stablecoins de una sola moneda (SGD o G10) emitidas en Singapur; etiqueta «MAS-regulated» solo para licenciados; el resto, DPT; prohibido interés; pruebas de estrés y planes de liquidación; reconocimiento limitado de extranjeras (mayorista); cierre 16-oct-2026. Ya constaba.

## [S] y [VERIFICAR]
- **Singapur, discurso del 19-nov (SFF 2026)**: vía lector, Chrome no devolvió el texto. Dice: Guardian Tokenised Collateral Framework publicado; guía de tokenización en actualización; BLOOM 24 miembros; GL1 con 5 instituciones; «estamos introduciendo un régimen para stablecoins»; MAS Bills tokenizadas por 100 M$ «en noviembre» (ambiguo con la emisión del 13-nov-2025: VERIFICAR año). Cotejar en la página oficial antes de [P].
- **Corea**: seminario del 5-nov (prensa): el proyecto del Gobierno de la Ley Básica de Activos Digitales «saldrá pronto»; sin norma. Sin acceso a la Asamblea.
- **Japón**: ETF, tasa fija del 20,315 % y 2027-28: sin cambio (S); decreto de ETF no localizado.
- Suiza: mensaje del Consejo Federal, Parlamento y calendario: VERIFICAR en sif.admin.ch y parlament.ch.
- DTSP de Singapur (ya en la celda de ley marco, 30-jun-2025): no reabierto.

## Lectura [ESPECULACIÓN]
- Alcista: Canadá y Singapur van a regímenes de licencia con reserva 1:1 y redención rápida, lo que da marco a emisores regulados; Suiza prepara licencia específica; Japón ya integró la cripto en la FIEA.
- Bajista: todo son proyectos, consultas o leyes sin vigencia (Canadá otoño 2027, Japón ≤ jul-2027, Suiza sin mensaje, Corea sin texto); la prohibición de rendimiento en Canadá y Singapur limita el atractivo de la stablecoin como producto de ahorro. Sesgo: la fuente de la hoja de ruta de Corea y Japón sobre fechas es prensa.

## Celdas modificadas en explorador/regulacion.json
jp/ley_marco (Dieta [P]), ch/stablecoins (consulta FinIA), ca/stablecoins (Gazette), sg/tokenizacion y sg/stablecoins (hitos 19-nov [S]), kr/stablecoins (hito 5-nov [S]). `revisar_explorador.py`: 0 avisos.

## Candidatos a movimiento de la línea de tiempo
```json
[
 {"fecha":"2026-10-24","pais":"ca","tema":"stablecoins","que":"Canadá publica en la Gazette el proyecto de Stablecoin Regulations: 60 días de comentarios, entrada en vigor prevista otoño 2027, redención en 3 días hábiles, prohibición de rendimiento.","fuente":"P","url":"https://gazette.gc.ca/rp-pr/p1/2026/2026-10-24/html/reg1-eng.html"},
 {"fecha":"2026-07-15","pais":"jp","tema":"ley_marco","que":"La Dieta aprueba la reforma de la FIEA y la Ley de Servicios de Pago (presentada 10-abr-2026).","fuente":"P","url":"https://www.fsa.go.jp/common/diet/221/index.html"},
 {"fecha":"2025-10-22","pais":"ch","tema":"stablecoins","que":"El Consejo Federal abre la consulta de la FinIA: licencias de payment instrument institution y crypto-institution; consulta cerrada el 6-feb-2026.","fuente":"P","url":"https://www.admin.ch/en/newnsb/x4TMWQ1SWofNoFx7XyHhY"},
 {"fecha":"2026-11-19","pais":"sg","tema":"tokenizacion","que":"La MAS y la industria publican el Guardian Tokenised Collateral Framework y anuncian la actualización de la guía de tokenización (discurso en el SFF).","fuente":"S","url":"https://www.mas.gov.sg/news/speeches/2026/keynote-address-by-md-at-the-singapore-fintech-festival-2026"},
 {"fecha":"2026-09-01","pais":"sg","tema":"stablecoins","que":"La MAS abre la consulta de enmiendas a la PS Act para stablecoins de una moneda (SGD/G10); cierre 16-oct-2026.","fuente":"P","url":"https://www.mas.gov.sg/news/media-releases/2026/mas-consults-on-legislative-amendments-to-implement-stablecoin-regulatory-framework"}
]
```
