# Auditoría del Explorador: datos.json y regulacion.json (2026-10-20)

Alcance:
- `explorador/datos.json`: 8 capas (fichas, cifras y hechos) y 37 movimientos.
- `explorador/regulacion.json`: 96 celdas.

Correcciones solo con datos que ya estaban en informes del repo o en las auditorías de hoy (R39 y Gemini). Lo dudoso queda [VERIFICAR]. Sin recomendaciones de compra/venta.

## Resumen (5 líneas)
1. **21 hallazgos; 16 corregidos en los JSON y 5 anotados** sin cambio.
2. Los avisos del script de calidad bajan de **8 a 1**. Queda a propósito el hecho de custodia de XRP, que sigue [VERIFICAR] porque ningún registro dice qué activos custodia cada firma.
3. Los 5 movimientos sin nombre de fuente ya tienen fuente concreta. El del Drex pasa de una fecha aproximada (15-nov) al **10-nov-2025** que da R03P.
4. En el radar se corrigen las etiquetas del euro digital ([S] para la posición del Consejo y [S, VERIFICAR] para el techo de tenencia), 4 fechas de «último cambio» que eran anteriores a un cambio normativo ya registrado y el orden de los hitos.
5. Sin cambios de etapa: ninguna se encontró mal puesta con los datos del repo.

## Hallazgos y qué se hizo
| # | Archivo | Hallazgo | Acción |
|---|---|---|---|
| 1 | datos.json · movimiento 18-jul-2025 | GENIUS sin nombre de fuente | **Corregido:** «Ley Pública 119-27, citada en la propuesta del Tesoro (Federal Register 2026-16796) [P] · R25» |
| 2 | datos.json · movimiento Drex | Sin fuente y con fecha aproximada (15-nov-2025, «mes aproximado») | **Corregido:** 10-nov-2025 (anuncio del 4-nov); fuente: prensa brasileña [S] · R03P, R40 |
| 3 | datos.json · movimiento 11-dic-2025 | No-acción a DTC sin nombre de fuente | **Corregido:** carta de la SEC (sec.gov, dtc-nal-121125.pdf) [P] · R26 |
| 4 | datos.json · movimiento 24-jun-2026 | JFSA y RLUSD sin nombre de fuente | **Corregido:** The Paypers, 24/7 Wall St y Stablecoininsider [S] · R09P |
| 5 | datos.json · movimiento 17-sep-2026 | Exención de la SEC sin nombre de fuente | **Corregido:** orden de exención (Federal Register 2026-19388) [P] · R26 |
| 6 | datos.json · deposit.plan | Hecho sin etiqueta [P]/[S] | **Corregido:** [S] con nota «R44»; el texto nombra JPMD |
| 7 | datos.json · fondos.plan | Hecho sin etiqueta | **Corregido:** [P] (plazo de 45 días de la SEC, R31), con [VERIFICAR] sobre la regla del día hábil |
| 8 | datos.json · custodia.xrp | «La custodia de XRP la ofrecen firmas cripto» [VERIFICAR] | **Reformulado** con lo que sí consta (BitGo Europe, Zodia y Coinbase Luxembourg con custodia en el registro de ESMA, R44); sigue [VERIFICAR] porque ningún registro lista los activos |
| 9 | datos.json · cifra de ETF de XRP (≈ 2.178 M$) | Choca con 1.560 M$ (8-oct) del dossier ETF; posible métrica distinta (cruce de fichas) | **Anotado en la fuente de la cifra** [VERIFICAR] |
| 10 | regulacion.json · UE · CBDC | Celda en [P], pero la posición del Consejo es [S] (403) | **Corregido:** [S] en la frase del Consejo |
| 11 | regulacion.json · UE · CBDC | «Techo de tenencia» como hecho; T04 lo deja [VERIFICAR] | **Corregido:** [S, VERIFICAR] |
| 12 | regulacion.json · UE · CBDC | Faltaba la fuente primaria de los 36 proveedores | **Añadido** el hito del 14-jul-2026 (nota de prensa del BCE, auditoría de Gemini) |
| 13 | regulacion.json · EE. UU. · stablecoins | Hito del 2-mar sin número de documento | **Corregido:** Federal Register 2026-04089, 91 FR 10202 (auditoría de Gemini) |
| 14 | regulacion.json · Japón · ley marco | Fecha 15-jul, pero la promulgación (23-jul) es posterior | **Corregido:** 2026-07-23 [S] |
| 15 | regulacion.json · EE. UU. · CBDC | Fecha 23-ene-2025, pero la Cámara aprobó la ley Anti-CBDC en jul-2025 | **Corregido:** 2025-07 |
| 16 | regulacion.json · UE · ley marco | Fecha 1-jul-2026, pero el veto a propietarios rusos de CASP rige desde el 25-ago-2026 | **Corregido:** 2026-08-25 [S] |
| 17 | regulacion.json · Hong Kong · stablecoins | Fecha 10-abr, pero la circular de la SFC (may-2026) es posterior | **Corregido:** 2026-05 |
| 18 | regulacion.json · EE. UU. · ley marco | Hitos desordenados (23-sep después de 5-oct) | **Corregido:** todos los hitos ordenados por fecha |
| 19 | regulacion.json · 6 celdas | La fecha de «último cambio» es anterior a un hito posterior (EE. UU. stablecoins y fiscal; Brasil ley marco y tokenización; Rusia ley marco y CBDC). Esos hitos son declaraciones, datos o anuncios de empresas, no cambios normativos | **Sin cambio:** criterio. La fecha es la del último cambio normativo; los hitos posteriores pueden ser datos |
| 20 | datos.json · movimiento del Drex | Estado «piloto» para un apagado de plataforma | **Anotado:** no hay un estado «retirado» en la lista; propuesta para la próxima versión del esquema |
| 21 | datos.json · fichas (stable, reg) | Las fechas de «qué vigilar» del 19-oct (comentarios del Tesoro) y del 20-oct (Regulation Crypto Assets) ya han pasado o pasan hoy | **Anotado:** actualizarlas cuando haya resultado; no se inventa el resultado |

## Comprobaciones hechas sin hallazgos
- Cifras de las 8 capas: todas tienen fuente y fecha o nivel.
- Etapas del radar frente a los estados descritos: coherentes con la escala 0-5. Sin celdas con etapa y fuente «VERIFICAR» a la vez.
- Próximas fechas del radar: ninguna anterior a hoy.
- Finales de línea: LF en los dos JSON.

## Estado del script de calidad
`python scripts/revisar_explorador.py`: **1 aviso** (custodia.xrp, pendiente de verificar a propósito); radar con 96 celdas y 29 sin dato.
