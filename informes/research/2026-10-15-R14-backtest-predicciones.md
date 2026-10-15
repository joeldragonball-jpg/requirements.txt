# R14 — Backtest de `informes/predicciones.md` (15-oct-2026)

Plantilla: `generica` (backtest). Se contrastaron las **47 entradas** con lo ocurrido hasta el 15-oct-2026. No se ha modificado `predicciones.md`: al final hay una lista de cambios propuestos para que Joel decida. Sin recomendaciones; todo lo etiquetado [ESPECULACIÓN] es opinión de la fuente original.

**Criterio:** *acertó* / *falló* solo si la fecha límite ya pasó o el hecho está comprobado sin ambigüedad; *en curso* si la fecha límite no ha llegado (con la lectura de hoy); *no medible* si no hay criterio objetivo o dato público.

## 1. Resultado global
| Resultado | Nº | Entradas |
|---|---|---|
| **Acertó** | 1 | #10 |
| **Falló** | 5 | #1, #9 (propia, mal planteada), #20, #38 (probable), #45 |
| **Parcial** | 1 | #41 |
| **En curso / sin resolver** (fecha límite futura o sin fecha) | 40 | resto |

Con solo 6-7 entradas resueltas **no se puede puntuar la fiabilidad de ninguna fuente**; lo siguiente es un registro de lo medido, no un ranking.

## 2. Predicciones resueltas o con evidencia nueva hoy

| # | Quién / qué dijo | Qué ha pasado (hecho + fuente) | Veredicto |
|---|---|---|---|
| **1** | Lummis: «si el cierre de debate falla, se acabó» (CLARITY) | La votación de cierre en el Senado salió **49–50**, 11 votos corta (probablemente 15-sep; fecha y tally solo en secundaria: Bitcoin.com, American Banker; congress.gov dio 403 [VERIFICAR]). La ley **sigue en juego** para el lame-duck/2027 (Galaxy Research baja a 30 % su prob. de ser ley en 2026, secundaria). | **Falló** (el proyecto no está muerto) |
| **9** | Research propio: BatchV1_1 podría activarse a partir del 23-oct | Ledger (nodo público xrplcluster.com, 15-oct 14:33 UTC, ledger 107.674.592): `BatchV1_1` y `fixBatchV1_2` **enabled: true**. Ya estaban activas desde el 9-oct. | **Falló (error propio, ya corregido en el dossier 9)** |
| **10** | Evernorth/prensa: debut de XRPN en Nasdaq el lunes 12-oct | XRPN empezó a cotizar el 12-oct (R22: 8-K de la SEC; prensa: apertura ~16,68 $, cierre 16,91 $) | **Acertó** |
| **19** | Research propio: fixCleanup3_4_0 se activará a partir del 23-oct (~09:35 UTC) si no pierde la mayoría | Ledger hoy: `fixCleanup3_4_0 enabled: false, majority: 844853670` = **9-oct 09:34:30 UTC**. +14 días = **23-oct 09:34:30 UTC**. La mayoría sigue vigente. | **En curso, el ledger confirma el mecanismo** |
| **20** | CoinDesk (panel del XRPL): arreglo de PaymentBurn con 27/35 votos, necesitaba 29 | El ledger ya mostraba la mayoría de fixCleanup3_4_0 (que lo incluye) el 9-oct a las 09:34 UTC; hoy sigue en cuenta atrás | **Falló** (contradicho por el ledger) |
| **38** | Montero (vía democrata.es): la ley DAC8 debía aprobarse antes del 31-dic-2025 | Búsqueda hoy: no hay evidencia de publicación en el BOE; fuentes de 2026 hablan de tramitación abierta y de que DAC8 «aún no está en marcha en España» (guía actualizada jul-2026, secundaria). Real decreto en audiencia pública desde jul-2025. | **Falló (probable)** [VERIFICAR en BOE/Congreso] |
| **41** | Gracy Chen (Bitget): la pérdida del hackeo está cubierta por el fondo (>464 M$) | Bitget repuso el fondo a **>300 M$ el 30-sep** (Cointelegraph: 309 M$); retiradas restauradas por fases 28-sep → 2-oct; pérdida revisada de 351,6 a ~387,5 M$; **la cifra >464 M$ no está verificada de forma independiente**, el fondo está en BTC (varía con el precio), y no se han detallado los términos de reembolso (Finance Magnates, Bitcoinist, Cointelegraph; todo secundaria). | **Parcial** (cubrió con balance, pero sin verificar el 464 M$) |
| **45** | Web de Solana: Alpenglow en mainnet en el 3T de 2026 (fecha límite 30-sep) | **No ocurrió en el 3T.** Anza anunció el 13-oct: mainnet-beta el **miércoles 21-oct, ~14:50 UTC** (Solana Compass, The Defiant, PrimeXBT; secundaria). El rumor del 28-sep fue desmentido por los desarrolladores. | **Falló** el plazo del 3T (nueva fecha 21-oct) |

## 3. En curso, con lectura de hoy (la fecha límite aún no llegó)

| # | Predicción | Lectura de hoy |
|---|---|---|
| 2, 3 | McHenry/Witt: CLARITY posible en el lame-duck | Cloture falló 49–50; Galaxy 30 %. Sigue abierto hasta 31-dic |
| 6 | Mercados de predicción: CLARITY en 2026 ~15–23 % | Más bajo que Galaxy (30 %); coherente en el rango bajo |
| 7 | CEO Solana Policy Institute: ~10 % antes del 3-nov | Hasta hoy no hay aprobación y el cierre falló: **va camino de acertar** (cierra el 3-nov) |
| 4, 5 | Despeja La X: reglas SEC/CFTC antes que la ley; custodia SEC en vigor ~90 días | Pendiente (fechas 2027) |
| 8 | Despeja La X: XRPN puede acabar en «desplome total» | Día 1: −1,05 %; sin dato de prima sobre valor de caja; sigue abierto hasta abr-2027 |
| 11, 44 | DTCC: DTC tokenizado en Stellar 1S-2027; servicio en producción en oct-2026 (Canton) | #44: operaciones **de producción** el 15-jul con >30 firmas (secundaria); el lanzamiento de octubre aún **sin confirmar** (plazo 31-oct). #11 sin novedad |
| 12 | CEO Evernorth: reinvertirá el rendimiento en "XRP por acción" | Primer 10-Q/10-K aún no publicado |
| 13 | Grayscale: GXLM pasará a NYSE Arca tras el S-1 (23-sep-2025) | **Más de 12 meses sin confirmar el uplisting**: las búsquedas solo devuelven documentos de 2025; estado actual [VERIFICAR] en EDGAR (CIK 1761325) |
| 14, 33, 34, 35 | BCE: Pontes 24/7 ~2028; euro digital 2029; piloto 2S-2027; Appia 2028 | No medible hasta esas fechas |
| 15 | OCC: norma final GENIUS hacia noviembre | Gould lo reiteró el 19-ago; los reguladores ya **incumplieron el plazo legal de julio**; plazo máximo legal 18-ene-2027; sin publicación a 15-oct. Estado: en curso con historial de retraso |
| 16 | Qivalis: stablecoin en euros en 2S-2026 | En curso |
| 17, 27 | EIA: Brent 105 $ en 4T-2026 y 84 $ en 2027… | Sin dato spot fiable hoy: el último precio verificado en la búsqueda es ~93 $ (21-ago, secundaria); mercado de predicción Kalshi daba 63 % a >99,99 $ el 16-oct [VERIFICAR]. Medir con la media oct-dic |
| 18 | FOMC: mayoría ve otra subida antes de fin de año | Decisiones 27–28-oct y 8–9-dic (R22) |
| 21, 22 | Ripple: sin OPV; OCC carta bancaria | En curso |
| 23 | Escrow 1-nov (00:00 UTC) | En curso (cálculo del ledger) |
| 24 | Araqchi: Irán reabre Ormuz en 7 días bajo condiciones | Irán «revisa la respuesta de EE. UU.» al plan de 7 días; el bloqueo naval sigue (Gulf News/1News, secundaria). Condiciones no cumplidas |
| 25 | Trump: no atacará Irán antes del 3-nov | Reiterado el 8–9-oct; **no encontré informes de ataques desde entonces** (ausencia de evidencia, no evidencia de ausencia) [VERIFICAR]. Historial citado por la prensa: acuerdo de junio colapsó en semanas; ataques «defensivos» en mayo. |
| 26 | WSJ: Trump ve probable nueva campaña | Reuters (vía búsqueda): asesores prefieren evitar escalada antes de noviembre y estudiarían ampliarla **tras** el 3-nov. Coherente con #26 y en tensión con #25 solo después de esa fecha |
| 28–32, 36, 37, 39, 40, 42, 43, 46, 47 | Fechas 2026-2027 (G7, BRICS, OPEP+ 1-nov, euro digital, MiCA, AEAT, FTX, Visa, Mastercard…) | Sin dato nuevo hoy; mantener "sin resolver" |

## 4. Observaciones por tipo de fuente (solo lo medido, n pequeña)
| Tipo | Resueltas | Detalle |
|---|---|---|
| **Políticos** | 2 falladas | Lummis (#1) y Montero (#38, probable): ambas dieron **plazos** que no se cumplieron. Los plazos de la política legislativa se han incumplido de forma sistemática (también el de julio de los reguladores GENIUS, #15) |
| **Prensa cripto citando a terceros** | 1 fallada | CoinDesk/panel XRPL (#20): resumen desfasado frente al ledger |
| **Empresas con calendario propio** | 1 acertó, 1 falló, 1 parcial | Evernorth (#10) acertó la nueva fecha tras un aplazamiento; Solana (#45) falló el trimestre; Bitget (#41) no verificable su cifra clave |
| **Research propio (cálculos)** | 1 fallada, 2 en curso | #9 mal planteada (se mezcló BatchV1_1 con fixCleanup3_4_0); #19 y #23 se apoyan en datos del ledger y de momento resisten |
| **Instituciones oficiales (BCE, FOMC, EIA, OPEP, AEAT)** | 0 | Todas con fecha futura |

## 5. Lecciones del backtest
1. **Las fechas anunciadas por una empresa o un legislador se deslizan con frecuencia**: de las 7 con veredicto (6 + 1 parcial), las que incluían un plazo de otro (Lummis, Montero, Solana) fallaron; la que se acertó (XRPN) era una fecha ya re-fijada a 4 días vista.
2. Los resúmenes de prensa sobre paneles on-chain pueden ir desfasados: contrastar con el ledger (nodo público) antes de calcular fechas.
3. Un cálculo propio de activación (#9, #19) debe indicar **qué enmienda concreta** y citar el campo del ledger (`majority`); no inferir por el nombre de la versión.
4. «Ya cubierto por el fondo/la caja» (#41, Bitget) exige que la cifra del fondo sea verificable por un tercero; si solo sale del CEO, queda [VERIFICAR].
5. Ausencia de ataques o noticias no es verificación: en #25 marcar "sin evidencia en contra" hasta el 3-nov.

## 6. Cambios propuestos para `informes/predicciones.md` (NO aplicados)
- #1 → «Falló (el proyecto no está muerto: cloture 49–50 el ~15-sep; sigue en lame-duck/2027)».
- #9 → mantener «Resuelta / mal planteada» y añadir «verificado en el ledger 15-oct».
- #10 → «Acertó (XRPN cotizó el 12-oct; 8-K, R22)».
- #19 → añadir «Ledger 15-oct: majority = 9-oct 09:34:30 UTC; activa a partir del 23-oct 09:34:30 UTC si la mantiene».
- #20 → «Falló (contradicho por el ledger)».
- #38 → «Falló (probable): sin ley publicada [VERIFICAR BOE]».
- #41 → «Parcial: fondo repuesto a >300 M$ (30-sep); el >464 M$ no verificado».
- #45 → «Falló el 3T; Anza fija mainnet-beta el 21-oct ~14:50 UTC».
- Nuevas filas sugeridas: «Anza: Alpenglow en mainnet el 21-oct (comprobable en una semana)» y «DTCC: servicio de tokenización en producción en octubre (31-oct)» (ya está como #44).

## 7. Huecos
1. congress.gov (403): voto exacto y fecha de CLARITY.
2. BOE/Congreso: estado de la ley DAC8 (verificar en la fuente primaria).
3. Brent spot de hoy (sin fuente fiable en la búsqueda).
4. EDGAR CIK 1761325: estado de GXLM (no leído).
5. Eventos de la semana que viene que resuelven predicciones: Alpenglow 21-oct, fixCleanup3_4_0 23-oct, escrow 1-nov, OPEP+ 1-nov, FOMC 27–28-oct.

## 8. Fuentes
- Ledger XRPL (nodo público xrplcluster.com, método `feature`, 15-oct-2026 14:33 UTC).
- Alpenglow: https://solanacompass.com/news/anza-sets-alpenglow-mainnet-date-solanas-consensus-switch-is-scheduled-for-october-21-at-about-1450-utc · https://thedefiant.io/news/blockchains/anza-sets-oct-21-for-solana-s-alpenglow-mainnet-upgrade (secundaria; página de Anza no leída).
- CLARITY: https://news.bitcoin.com/clarity-act-isnt-dead-but-washington-is-running-out-of-calendar/ · https://www.americanbanker.com/news/as-divisions-linger-senate-punts-clarity-act-to-september
- OCC/GENIUS: https://theblock.co/news/regulation/2026-08-19-occ-races-to-finalize-genius-act-stablecoin-rules-by-november-412240 · https://www.pymnts.com/legal/2026/occ-promises-final-rule-for-genius-act-by-november/ · https://infobytes.orrick.com/2026-08-28/comptroller-gould-highlights-digital-asset-efforts-says-occ-will-finalize-genius-act-rule-by-november/
- Bitget: https://cointelegraph.com/news/bitget-operations-protection-fund-security-breach · https://bitcoinist.com/bitget-protection-fund-restored-300m/amp/ · https://www.financemagnates.com/cryptocurrency/exchange/bitgets-388-million-hack-could-consume-84-of-its-protection-fund/
- Irán/Trump: https://www.courthousenews.com/trump-says-us-will-not-resume-military-strikes-on-iran-before-the-nov-3-midterm-elections · https://www.1news.co.nz/2026/10/09/trump-rules-out-new-strikes-on-iran-before-us-midterm-elections/
- DTCC: https://www.canton.network/dtcc-tokenization-service-on-canton · https://www.theasianbanker.com/press-releases/dtcc-completes-production-trades-using-tokenised-dtc-held-securities
- GXLM S-1: https://www.sec.gov/Archives/edgar/data/1761325/000119312525213783/gxlm-20250924.htm
- DAC8 España: https://www.legaltoday.com/actualidad-juridica/noticias-de-derecho/transposicion-de-la-directiva-dac8-para-el-control-sobre-proveedores-de-criptomonedas-2025-06-04/ · https://finreg360.com/alerta/el-ministerio-de-hacienda-pone-en-audiencia-publica-el-proyecto-de-real-decreto-que-completa-la-transposicion-de-la-dac-8/
- XRPN debut: https://www.kucoin.com/news/flash/ripple-backed-evernorth-lists-on-nasdaq-as-xrpn-with-473m-xrp-treasury
