# R31 · Auditoría de coherencia n.º 2 (R13 a R37, matriz, calendario, aperturas/cierres y lecciones) (2026-10-17)

Plantilla: `auditoria-coherencia`. Modelo Opus 5.5, esfuerzo medio. No repite el research: revisa lo escrito desde R22 y re-verifica en fuente primaria lo que más pesa. Dos pasadas en la misma sesión: (1) R13-R24 y cerebro; (2) R25-R37, matriz y calendario. **Nada se ha cambiado en los informes ni en el cerebro**: las correcciones son propuestas.

## Resumen (5 líneas)
1. **Error que cambia una fecha:** la mayoría de `fixCleanup3_4_0` empezó el **9-oct a las 09:34:30 UTC** (nodo xrplcluster.com, `majority` = 844853670, convertido hoy). R14 lo tenía bien; **R32, R37 y la línea R32 del cerebro dicen 10:34 UTC** (una hora tarde). La posible activación es **~23-oct 09:34 UTC**.
2. **Lo grande se sostiene:** Goldman/XRPR (110.000 acc. en 1T y 2T), 388.910.554 XRP en especie de Evernorth (suma de las 5 partidas del 8-K), Fed 3¾-4 % (16-sep), IPC sept 3,7 %, BoJ 1,25 % (7-2) y los plazos del Federal Register (19-oct, 20-oct, 7-dic, 14-dic) están confirmados hoy en primaria.
3. **Fecha nueva / [VERIFICAR] cerrado:** las dos propuestas GENIUS de la Fed se publicaron en el Federal Register el **29-sep** y cierran comentarios el **30-nov-2026**; no están en R37 y la matriz aún dice "24-sep, 60 días [VERIFICAR]". El 13F del 3T vence el **lunes 16-nov-2026** (tabla oficial de la SEC): cierra el [VERIFICAR] de R37.
4. **Correcciones que no llegaron a su informe:** R13 sigue diciendo "Goldman salió por completo en 1T" y "~473 M XRP" sin nota (R21 y la apertura del 17-oct sí la llevan). La matriz sigue con Regulation Crypto Assets en [S] cuando R23 la leyó [P].
5. **Confianza global: media-alta** en macro, calendario y datos de ledger/EDGAR; **media** en regulación por región; **media-baja** en Ripple/Stellar como empresas (casi todo autoinformado). Ningún error encontrado cambia la conclusión de fondo de los informes; el de la hora sí cambia el calendario del 23-oct.

---

## 1. Contradicciones entre informes

| Tema | Informe A dice | Informe B dice | Mejor fuente | Acción propuesta |
|---|---|---|---|---|
| Hora de mayoría de `fixCleanup3_4_0` | R14:24 y cerebro (catalizadores, línea R14): 9-oct **09:34:30 UTC**, activable 23-oct 09:34:30 | R32:7/19/60, R37:13 y cerebro (línea R32): 9-oct **10:34 UTC**, activación ~23-oct 10:34 | **Ledger hoy (17-oct 19:07 UTC):** `majority` 844853670 + 946684800 = 9-oct-2026 09:34:30 UTC → **R14** | Nota de corrección en R32 y R37; línea de corrección en el cerebro (con visto bueno) |
| Margen de votos de `fixCleanup3_4_0` | R32:42: ≥25 de 32, "margen de 1 voto" | R37:70: "que no pierda ni un voto de los 26" | R32 (umbral 25 según el nodo/xrpscan; el nodo de clúster hoy no devuelve `count`/`threshold`) | Corregir R37: puede perder 1 voto; si baja a 24, pierde la mayoría |
| Plazo del 13F del 3T | R19:102, R21:119/135/162, R26:61, R27:49, R33:65, matriz:17: "~14-nov" | R37:32: lun 16-nov [VERIFICAR] | **SEC, FAQ de Form 13F (tabla oficial): "3Q 2026 (September) November 16, 2026 (Monday)"** → R37 | Quitar [VERIFICAR] de R37; nota en matriz |
| Registro MiCA de ESMA | R18:8/29: **370 entidades** | R19:8 y cerebro (línea R19): **365** | R19:24 lo explica: 370 filas y 365 LEI distintos (15-oct). Hoy el CSV tiene **378 filas / 375 valores distintos** (crece) | R18: "370 filas (365 entidades distintas) a 15-oct"; citar siempre con fecha |
| Goldman en 1T | R13:60: "Goldman salió por completo en 1T" | R21b, R21:3 (nota), matriz:17: nunca a cero (XRPR 110.000 acc.) | **13f.info (índice de EDGAR), hoy:** Goldman 110.000 acc. de 26923N231 a 31-mar (1.213 k$) y a 30-jun (943 k$) → R21b | Nota de corrección en R13 |
| XRP de Evernorth | R13:67, apertura 17-oct:28/47: ~473 M XRP | R23:14: 388.910.554 en especie (8-K); 473 M es del Form 425 a 31-dic-2025 | **8-K, hoy:** partidas 211.319.096 + 126.791.458 + 50.000.000 + 600.000 + 200.000 = 388.910.554 → R23 | La apertura ya lleva nota; falta en R13 (y el 0,75 % de circulación pasa a ~0,62 % con 388,9 M sobre ~63.000 M: cálculo mío) |
| Swell 2026 | R28:53: "día exacto sin publicar" | R37:17/68, R09P, cierre 15-oct: 27-29-oct | swell.ripple.com (R37, parte interesada pero es el organizador) → R37 | Ya corregido en R37; nota en R28 |
| Propuesta GENIUS de la Fed | matriz:17: "24-sep; plazo de 60 días [VERIFICAR]"; cerebro (R08P): "comentario 60 días" | R25:28: solo títulos y fecha 29-sep | **Federal Register API, hoy:** docs 2026-19860 y 2026-19899, publicados 29-sep, **comentarios hasta 30-nov-2026** | Matriz y calendario: añadir 30-nov; el "60 días" cuenta desde la publicación (62 días) |
| Stablecoins en Stellar | R13: 461 M$ (15-oct) | R25: ~520 M$; R33: 516 M$ (17-oct); hoy 541 M$ | **No es contradicción:** la serie de DefiLlama sube 425 → 545 M$ entre 12 y 17-oct (+28 % en 5 días) | Citar siempre con día; la subida merece [VERIFICAR] de causa (¿una emisión grande?) antes de leerla como adopción |
| RLUSD | R34: 2.432 M$ | cerebro (línea R34): 2.433 M$ | Redondeo; misma fuente | Sin acción |

## 2. Sobreafirmaciones (dadas como hecho con fuente débil)

| Frase | Archivo:línea | Fuente | Cómo debería etiquetarse |
|---|---|---|---|
| "se activaría ~23-oct 10:34 UTC" | R32:7, R37:13 | cálculo propio con hora mal convertida | Hora 09:34 UTC y [ESPECULACIÓN] sobre si mantiene el apoyo |
| "Ripple posee ~38 % del XRP" | R13:93, R15:48 | dossier Ripple; Ripple declaró 37.656 M a 30-jun (R32:30) | [PARTE INTERESADA, 30-jun-2026]; incluye escrow; la cifra baja cada mes |
| "~388 M XRP se aportaron por Ripple, el patrocinador y partes relacionadas" | R13:66, R15:50 | 8-K | Precisar: Ripple aportó **126,8 M** (32,6 %); el resto, el patrocinador (211,3 M) y otras partes |
| "Ripple National Trust Bank espera aprobación final OCC" | cerebro (línea R09P) | ripple.com | [PARTE INTERESADA]; R34 tampoco localizó el estado en occ.gov [VERIFICAR] |
| "más de 85 licencias" | R34:7 | Ripple | Ya marcado como autoinformado en R34:43: correcto |
| "XRP Europa ~914 M$" | R27:7, patrones (R27) | 21Shares (emisor) con datos de Bloomberg | [PARTE INTERESADA]; R27 lo dice, la lección del cerebro no |
| "mBridge 55,49 mil M$, e-CNY >95 %" | R28:9 | Atlantic Council (tercero que cita datos del proyecto) | [SECUND] sin primaria del BIS |
| "la propuesta de custodia… sin mención de XRP/XLM" y "XRP no aparece en el texto" (notas Ripple) | R23, R34 | búsqueda de texto propia | Correcto como hecho limitado al documento leído; no generalizar a "Ripple no usa XRP" |

## 3. Etiquetas

**[VERIFICAR] ya resueltos (por este informe o por otro):**
- R37:32 plazo 13F 3T → **16-nov-2026 confirmado** (SEC, FAQ Form 13F).
- Matriz:17 "Fed GENIUS 24-sep, 60 días [VERIFICAR]" → **FR 29-sep, comentarios 30-nov** (Federal Register).
- Matriz:17 "Regulation Crypto Assets, comentarios hasta 20-oct [S]" → **[P]** (R23 y FR doc 2026-17183, `comments_close_on` 2026-10-20, comprobado hoy).
- Apertura 17-oct:17/38 "Fed 3,75-4,00 %, falta federalreserve.gov" → **[P]** (R29 y comprobado hoy).
- Cierre 15-oct:16 y apertura 17-oct:32 "Swell 27-29 oct [VERIFICAR en ripple.com]" → confirmado (R37).
- R16 "DTCC, lanzamiento octubre 2026 [VERIFICAR]" sigue abierto (R26 tampoco lo confirmó).

**Cifras sin etiqueta que deberían llevarla:**
- R13:41 RLUSD "56 % Ethereum / 44 % XRPL (28-sep)" viene de KuCoin flash (C en la escala de R15): debería ir [SECUND]; R34 ya da el reparto con ledger (42 % XRPL).
- R18:8 "370 entidades [P]": la cifra es de filas, no de entidades (ver §1).
- Lección del cerebro (R27): "XRP Europa ~914 M$" sin indicar que la fuente es un emisor.

## 4. Muestreo de 12 afirmaciones de peso (re-verificadas hoy, 17-oct, con curl)

| # | Afirmación | Dónde | Fuente comprobada | Resultado | Nivel |
|---|---|---|---|---|---|
| 1 | Goldman conserva 110.000 acc. de XRPR en 1T y 2T | R21b, matriz | 13f.info JSON (CUSIP 26923N231, 2026 T1 y T2; índice de EDGAR, ya cotejado 5/5 en R21b) | **Confirmada**: 1.213 k$ y 943 k$ | SECUND-INDEXADA (EDGAR leído en R21b) |
| 2 | Evernorth: 388.910.554 XRP en especie | R23 | 8-K en EDGAR (d24481d8k.htm) | **Confirmada**: cinco partidas suman exacto | PRIM-LEÍDA |
| 3 | Ripple aportó 126.791.458 XRP | apertura 17-oct, R23 | mismo 8-K | **Confirmada** | PRIM-LEÍDA |
| 4 | Mayoría de `fixCleanup3_4_0` desde 9-oct | R14, R32, R37 | xrplcluster.com `feature` | **Confirmada la fecha; hora 09:34:30 UTC, no 10:34** | LEDGER |
| 5 | Suministro total ~99.985,59 M XRP | R32 | xrplcluster.com `ledger` validado | **Confirmada**: 99.985.589.987,67 XRP (17-oct 19:07 UTC; baja por quema de comisiones) | LEDGER |
| 6 | Fed sube a 3¾-4 % el 16-sep | R29, aperturas | federalreserve.gov monetary20260916a | **Confirmada** (texto literal "3-3/4 to 4 percent") | PRIM-LEÍDA |
| 7 | FOMC 27-28-oct y 8-9-dic | R29, R37 | federalreserve.gov fomccalendars | **Confirmada** | PRIM-LEÍDA |
| 8 | IPC sept 3,7 % (ago 3,4 %), subyacente 2,6 %, energía +20,4 % | R29 | bls.gov cpi.nr0 | **Confirmada** | PRIM-LEÍDA |
| 9 | BoJ 1,25 % por 7-2 (Asada y Sato en contra) el 18-sep | R29 | boj.or.jp k260918a.pdf | **Confirmada** | PRIM-LEÍDA |
| 10 | Plazos FR: GENIUS Treasury 19-oct; Regulation Crypto Assets 20-oct; custodia SEC 7-dic; ANPRM CFTC 14-dic | R23, R25, R37 | federalregister.gov API (2026-16796, 2026-17183, 2026-20466, 2026-20888) | **Confirmadas las cuatro** | PRIM-LEÍDA (metadatos oficiales) |
| 11 | Plazo 13F del 3T | R21, R37 | sec.gov FAQ Form 13F | **16-nov-2026 (lunes)**; "~14-nov" queda obsoleto | PRIM-LEÍDA |
| 12 | Registro MiCA de ESMA 365/370 | R18, R19 | CASPS.csv (esma.europa.eu) | Hoy 378 filas / 375 distintos: las cifras del 15-oct eran correctas para su fecha, pero ya no son actuales | PRIM-LEÍDA |

Extra (no cuenta en las 12): propuestas GENIUS de la Fed en el Federal Register (29-sep, cierre 30-nov), PRIM-LEÍDA (metadatos); stablecoins en Stellar/XRPL en DefiLlama (541 M$ / 1.121 M$ hoy), agregador.

## 5. Lecciones del cerebro: duplicadas, contradictorias o largas (propuesta, NO aplicada)
- **Contradictorias:** en `catalizadores-xrp-xlm.md` la línea R14 (09:34:30 UTC) y la línea R32 (10:34 UTC) se contradicen. Proponer línea de corrección (abajo).
- **Duplicadas:** el estado de Evernorth aparece en las líneas de la apertura del 17-oct, la corrección R23 y otras anteriores; con la corrección R23 basta. Las fechas FOMC/BCE/BoJ aparecen en R22 y en R29: dejar R29 como referencia.
- **Demasiado largas:** varias líneas de `fuentes-fiables-y-dudosas.md` (R25, R26, R30, R32, R33, R34) superan las 2-3 frases; son útiles pero rozan la regla de "cortas". Proponer recorte a 1 línea cada una en una revisión mensual (sin borrar ahora).
- **Obsoleta:** `fuentes-fiables-y-dudosas.md` (línea R12P/R11P) "sec.gov no abrió" ya está matizada por las líneas R22 y R23: correcto, sin acción.

## 6. Huecos por impacto (documentos que Joel debería descargar a `research/fuentes/`)
Los de la SEC, el Federal Register, la Fed, el BLS, el BoJ, MAS y ESMA ya los leo yo con curl: no hace falta descargarlos. Siguen cerrados desde aquí:

| # | Documento | URL de partida | Nombre sugerido |
|---|---|---|---|
| 1 | Reforma FIEA de Japón y lista de criptoactivos (¿XRP?) | fsa.go.jp | `japon-fiea-reforma-2026.pdf` |
| 2 | Resoluciones BCB 519/520/521 (plazo ≈30-oct de Brasil) | normativos.bcb.gov.br | `bcb-res-519-520-521.pdf` |
| 3 | Estado del OCC sobre Ripple National Trust Bank | occ.gov (decisiones de licencias) | `occ-ripple-trust-bank.pdf` |
| 4 | Informe del prototipo Agorá (BIS) | bis.org/publ | `bis-agora-prototipo-2026.pdf` |
| 5 | Comunicado DTCC sobre el lanzamiento del servicio de tokenización (oct-2026) | dtcc.com/news | `dtcc-tokenizacion-lanzamiento-2026.pdf` |
| 6 | Declaración de Nueva Delhi (BRICS) | pib.gov.in | `brics-declaracion-nueva-delhi-2026.pdf` |
| 7 | Ley rusa 282-ФЗ | publication.pravo.gov.ru | `rusia-ley-282-fz-2026.pdf` |

Huecos sin descarga (tarea corta posible): causa de la subida de stablecoins en Stellar (425 → 545 M$ en 5 días, DefiLlama por emisor); votos por validador de `fixCleanup3_4_0` el 22-oct.

## 7. Conclusión: confianza por área

| Área | Confianza | Por qué (una frase) |
|---|---|---|
| Macro / bancos centrales | **Alta** | Fed, BLS, BoJ y el calendario FOMC re-verificados hoy en fuente oficial sin una sola discrepancia. |
| Regulación EE. UU. (SEC, CFTC, Treasury, Fed) | **Alta** | Todos los plazos salen de los metadatos del Federal Register; solo faltaba el 30-nov de la Fed. |
| Regulación resto de regiones | **Media** | MAS, ESMA, HKMA, FSC y RBI en primaria; Brasil, Japón, Emiratos federales, BRICS y Rusia (ley) siguen en secundaria. |
| 13F / ETF | **Alta** en datos, **baja** en interpretación | Las cifras cuadran con EDGAR; el 13F sigue sin decir cuándo ni por qué compran. |
| XRPL / Stellar (redes) | **Alta** en datos de ledger, **media** en cálculos propios | El ledger es primario, pero el error de hora de R32 muestra que las conversiones de tiempo propias necesitan doble control. |
| Ripple / Stellar (empresas) | **Media-baja** | Licencias, valoración, volúmenes y socios siguen siendo en su mayoría autoinformados. |
| Calendario de catalizadores (R37) | **Media-alta** | Fechas oficiales confirmadas; corregir la hora del 23-oct y añadir el 30-nov (Fed GENIUS). |

**Hechos vs. opiniones:** §1, §3 y §4 son hechos comprobables con la fuente indicada; las valoraciones de confianza de §7 son **opinión mía** sobre la calidad de las fuentes, no sobre el precio de XRP/XLM. Nada de este informe es recomendación de compra o venta.

## Correcciones propuestas (solo con visto bueno de Joel; se añadirían como líneas nuevas, sin borrar nada)
1. `cerebro/documentos/catalizadores-xrp-xlm.md`, bajo "## Correcciones 2026-10-17": "La mayoría de fixCleanup3_4_0 empezó el 9-oct 09:34:30 UTC (ledger: majority 844853670); la línea R32 que dice 10:34 UTC está desfasada 1 hora; posible activación ~23-oct 09:34 UTC si mantiene ≥25 votos."
2. Nota al principio de R32 y R37 con la misma hora corregida; en R37:70, "puede perder 1 voto" en vez de "ni un voto".
3. Nota al principio de R13: Goldman nunca estuvo a cero (XRPR, R21b) y Evernorth = 388,9 M XRP en especie (R23).
4. Matriz, fila EE. UU.: Regulation Crypto Assets → [P]; Fed GENIUS → FR 29-sep, comentarios hasta 30-nov-2026 [P]; 13F del 3T → 16-nov-2026 [P].
5. R18: "370 filas / 365 entidades distintas (15-oct)".

## Fuentes consultadas hoy (17-oct-2026)
- xrplcluster.com (JSON-RPC `feature` y `ledger`), 19:07 UTC.
- https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm · https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- https://www.bls.gov/news.release/cpi.nr0.htm
- https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260918a.pdf
- https://www.federalregister.gov/api/v1/documents/ (2026-16796, 2026-17183, 2026-20466, 2026-20888, 2026-19860, 2026-19899)
- https://www.sec.gov/Archives/edgar/data/2092592/000119312526419146/d24481d8k.htm (8-K de Evernorth)
- https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f
- https://13f.info/data/cusip/26923N231/2026/1 y /2 (índice de EDGAR)
- https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv
- https://stablecoins.llama.fi/stablecoinchains y /stablecoincharts/Stellar (agregador)
