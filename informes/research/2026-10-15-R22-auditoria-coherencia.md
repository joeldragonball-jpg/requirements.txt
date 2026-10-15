# R22 · Auditoría de coherencia y afirmaciones de todo el research (2026-10-15)

Modelo: Opus 5.5, esfuerzo medio · Plantilla: `auditoria-coherencia` · No es research nuevo: revisa lo ya escrito.
Entradas leídas enteras: los 15 informes de `informes/research/` (R02, R10, calendario-regiones, R01P–R09P, R11P, R12P, R21), los tres archivos de lecciones del cerebro, las cuatro secciones "## Correcciones 2026-10-15" y `research/COLA.md`.
Reglas: HECHOS separados de OPINIONES; sin recomendaciones de compra/venta; **no se ha tocado nada del cerebro** (todo lo que sigue son propuestas para que Joel las apruebe).
Niveles del muestreo: **PRIM-LEÍDA** (página oficial abierta hoy) · **EXTRACTO** (oficial vía buscador, sin abrir) · **SECUND** (prensa o despacho).

## Resumen (5 líneas)
1. **Calidad general buena**: no hay ninguna contradicción grave entre informes sobre cifras clave; los fallos son de matiz, de etiquetado y de método (qué web "abre").
2. **El muestreo sube de nivel 9 de 11 afirmaciones a PRIM-LEÍDA** (Fed, BCE, BoJ, BLS, MAS, Swell, Evernorth, SEC, Tesoro). Ninguna resultó falsa; **una se había leído mal** (red A7: "91.500 M$ en ene-2026" es "a enero de 2026", no un mes).
3. **sec.gov sí abre** (con curl y User-Agent identificado, método de R21): eso contradice "sec.gov no abrió" de R11P/R12P y permite cerrar varios [VERIFICAR] de la SEC y de Evernorth hoy mismo.
4. **Sobreafirmaciones típicas**: frases del resumen o del "caso alcista/bajista" más fuertes que su propia tabla (95 % de mBridge en yuan, "valor real" en Agorá, e₹ −24 %, Meritz "firmado el 1-oct").
5. **Lecciones del cerebro**: ~10 líneas duplicadas o solapadas en `patrones-de-bulos.md` y una contradicción interna en `fuentes-fiables-y-dudosas.md` (ripple.com/stellar.org como "fiables" y a la vez "parte interesada").

---

## 1. Contradicciones entre informes

| Tema | Informe A dice | Informe B dice | Mejor fuente | Acción propuesta |
|---|---|---|---|---|
| ¿Abre sec.gov? | R11P/R12P y `fuentes-fiables…:33`: "sec.gov (notas 2026-100 y reglas) no abrieron" | R12P fila 14: nota 2026-100 **PRIM-LEÍDA**; R21 y hoy R22: sec.gov abre con curl + User-Agent | R21 / R22 (probado hoy: comunicado 2026-90 y 8-K de Evernorth leídos) | Añadir lección: "sec.gov: usar curl con User-Agent identificado; WebFetch puede fallar". Rehacer con ese método los [VERIFICAR] de la SEC (ver §6) |
| "Rusia vigente en septiembre" (vídeo del cerebro) | R11P (15:32): "probablemente es el rublo digital (1-sep-2026), no una ley cripto" | R06P (15:40): Ley 282-ФЗ de cripto en vigor el **1-sep-2026** (Interfax, Pravo.ru, SECUND) | R06P (prensa rusa leída entera con cita literal) | Cambiar la hipótesis de R11P: lo más probable es la ley 282-ФЗ; ambas cosas pasaron el 1-sep |
| Red A7 (volumen) | R06P resumen: "~91.500 M$ procesados **en ene-2026**" | Tesoro sb0644 (PRIM-LEÍDA hoy): "**as of January 2026** … more than 7.5 trillion rubles … ≈13 % of 2025 foreign trade"; no dice si es acumulado | Tesoro | Corregir R06P y `catalizadores`: "a enero de 2026 (cifra autoinformada, periodo no especificado)". Leído como cifra mensual sería >150 % del comercio exterior anual |
| mBridge, volumen | R01P: 55,5 mil M$ (Atlantic Council, ene-2026) y dice que el choque con la cifra china es "solo de redondeo" | R01P misma tabla: "casi 500.000 M CNY" a fin de 2025 (PBoC) ≈ 69–70 mil M$ | Ninguna primaria leída | El redondeo solo explica 470k vs 500k CNY; **55,5 vs ~70 mil M$ es un ~25 % de diferencia** (metodología o fecha distinta). Marcar [VERIFICAR] y no mezclar |
| Rublo digital, comisiones | R01P: sin comisiones hasta 31-dic-2026 [VERIFICAR] | R11P: "CONFIRMADO con matiz" pero un medio las da vigentes desde 1-sep | Ninguna primaria (cbr.ru no abrió) | Bajar R11P a "SIGUE CONTRADICTORIO"; un CONFIRMADO no puede llevar dentro una contradicción abierta |
| e₹ −24 % (fuente) | R02: el dato venía de una academia UPSC, "sin confirmar"; lección `fuentes…:24`: "academias UPSC no valen como fuente" | R02P: lo da por cerrado con Techpillow y "Drishti/otros" (Drishti **es** una academia UPSC) | Informe Anual RBI (captcha, no leído) | Dejarlo en SECUND [VERIFICAR] hasta que Joel pegue la tabla del RBI; quitarlo como hecho de `catalizadores:22` |
| Sibos 2027 | `patrones-de-bulos:23`: "11–14 oct según swift.com [VERIFICAR]" | R11P/R12P: CONFIRMADO (sibos.com, EXTRACTO) | sibos.com | El [VERIFICAR] de la lección ya está resuelto (ver §3) |
| Meritz–Ripple (fecha) | R05P: anunciado 7-oct; "ceremonia 1-oct **según otra fuente**" (The Value News) | `patrones-de-bulos:20`: "firmado 1-oct, divulgado 7-oct" como hecho | R05P (SBS Biz leído: 7-oct) | La fecha de firma es de una sola fuente: añadir [VERIFICAR] |
| Precio de XRP en 1T | R21 §4: "XRP cayó ~27-30 % en 1T (de ~2,40 $ a 1,30-1,50 $)" | Misma frase: de 2,40 a 1,40 es −42 %, no −27 %; el −27 % sí cuadra con Bitwise 20,52 → 15,03 $ (PRIM-LEÍDA) | 13F (cocientes propios) | El "~2,40 $" de partida es incoherente; quitarlo o marcar [VERIFICAR] (secundaria) |
| RWA de Stellar | `catalizadores:9`: 3.550 M$ (rwa.xyz, 7-oct) | R09P: 4.000 M$ a 1-sep (SDF) | Ninguna independiente | R12P ya lo explicó (métricas distintas). Mantener ambas con la métrica al lado; no son una serie |

No contradictorios (comprobado): FOMC 27-28-oct en R10, calendario-regiones y catalizadores; Pontes 21-sep (R08P, R11P, R12P); 49-50 del 15-sep (R10, R11P, R12P); RLUSD >1.000 M$ (dic-2025) y >1.500 M$ (mar-2026) son fechas distintas; Res. 561 (30-abr / 1-oct) igual en R03P y catalizadores.

## 2. Sobreafirmaciones (dadas como hecho con fuente débil)

| Frase | archivo:línea | Fuente real | Cómo debería etiquetarse |
|---|---|---|---|
| "~95 % del mBridge es yuan digital" (caso bajista) | R01P:42 (y resumen :10 "dominado por") | Reuters/Atlantic Council; la propia tabla (:25) dice que el 95 % no apareció en otra búsqueda | "[VERIFICAR] ~95 % según una fuente" |
| "tres bancos centrales G10 ya probaron atómica con valor real en preparación" | R08P:39 | BIS/BCE: prototipo; la fase de valor real es la **siguiente** (R08P:9) | "prototipo terminado; pruebas con valor real pendientes" |
| "Fed propuso reglas GENIUS el 24-sep (comentario 60 días)" | catalizadores:28; R08P:50 | Solo el título en el índice de la Fed; el "60 días" no tiene fuente citada | "[VERIFICAR] plazo de comentarios" |
| "e₹ minorista −24 % a 771,66 crore ₹" | catalizadores:22; R02P:7 | Blog (Techpillow) + academia UPSC; PDF del RBI no leído | SECUND [VERIFICAR] |
| "≈30-oct-2026 vence el plazo" de Brasil | catalizadores:23 | Cálculo propio (270 días desde 2-feb; la aritmética da 30-oct) sobre **un solo** despacho (Lefosse) | Añadir "(cálculo propio, una fuente)" como en R03P:59 |
| Innovation Exemption "≈17-sep-2026" | patrones-de-bulos:41; R11P:25 | Era SECUND con "≈" | **Resuelto hoy**: SEC, comunicado 2026-90, "Washington D.C., Sept. 17, 2026" (PRIM-LEÍDA). Quitar el "≈" |
| Licencia Ripple MPI "ampliada dic-2025" | catalizadores:24 | Solo Ripple vía Cointelegraph (R04P:29) | Ya lleva [VERIFICAR]; añadir "según Ripple" |
| "Meritz–Ripple firmado 1-oct" | patrones-de-bulos:20 | Una fuente (The Value News) | [VERIFICAR] |
| "Bermuda eligió Stellar" | R09P:29 | Afirmación de SDF, sin fuente del Gobierno | "según SDF" (ya en la tabla, no en el resumen) |
| "ETF de XRP sin flujos" (5-oct) | catalizadores:10 | Sin fuente citada en la línea | [VERIFICAR] (SoSoValue) |
| Fuentes "fiables (primarias): ripple.com, stellar.org" | fuentes-fiables-y-dudosas:6 | Son parte interesada (lo dicen las líneas 32 y 35 del mismo archivo) | "primarias **de lo que afirma la empresa**, no de cifras ni de impacto" |

Patrón: la tabla de cada informe suele estar bien etiquetada; la sobreafirmación aparece **al resumir** (resumen de 5 líneas, caso alcista/bajista y línea al cerebro).

## 3. Etiquetas

**[VERIFICAR] ya resueltos (por otro informe o por el muestreo de hoy):**
- Sibos 2027 11–14-oct (`patrones-de-bulos:23`) → R11P/R12P.
- LPR 20-oct (R10:12, `catalizadores:20`) → R11P.
- FOMC 27-28-oct y 8-9-dic con proyecciones (R10:13, :22) → **PRIM-LEÍDA hoy** (federalreserve.gov).
- BCE 28-29-oct (decisión el 29) y 16-17-dic (R10:14, :24) → **PRIM-LEÍDA hoy** (ecb.europa.eu). Resuelve también la duda "28 o 29".
- BoJ 29-30-oct y 17-18-dic (R10:15, :25; `fuentes…:23` "sin confirmar en boj.or.jp") → **PRIM-LEÍDA hoy** (boj.or.jp abre).
- IPC de octubre el 10-nov y de noviembre el 10-dic (R10:18, :23) → **PRIM-LEÍDA hoy** (BLS). El "11-dic" del tercero es erróneo.
- Elecciones EE. UU. 3-nov (R10:16) → fecha fijada por ley (primer martes tras el primer lunes de noviembre): no necesita [VERIFICAR].
- Swell 27–29-oct (calendario-regiones:12, R09P:52) → **PRIM-LEÍDA hoy** (swell.ripple.com): Nueva York, The Shed; hackathon 24–25-oct.
- Evernorth cierre 9-oct y cotización 12-oct (corrección del cerebro con "[VERIFICAR en la SEC]") → **PRIM-LEÍDA hoy** (8-K en EDGAR).
- Innovation Exemption 17-sep (R11P:26 "[VERIFICAR] en sec.gov") → **PRIM-LEÍDA hoy**.
- Umbral TDS 194S (R02:28) → resuelto en R02P (10.000 / 50.000 ₹ anuales según tipo de pagador).
- HKMA 10-abr: R07P no abrió el comunicado (la URL probada era otra) → URL correcta `hkma.gov.hk/…/press-releases/2026/04/20260410-4/` (EXTRACTO: FRS01 Anchorpoint, FRS02 HSBC; 36 solicitantes en la primera tanda).

**Cifras sin [VERIFICAR] que deberían tenerlo:** las de la tabla §2 (95 % mBridge, 60 días GENIUS, e₹ −24 %, "ETF XRP sin flujos", Meritz 1-oct) y el "~2,40 $" de R21:120.

## 4. Muestreo de 11 afirmaciones de peso (solo datos públicos: precio, ETF, regulación, catalizadores)

| # | Afirmación (dónde) | Resultado | Nivel | Fuente y fecha |
|---|---|---|---|---|
| 1 | FOMC 27-28-oct; 8-9-dic con SEP (R10, catalizadores) | CONFIRMADO | PRIM-LEÍDA | [federalreserve.gov, calendario FOMC](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm), leída 15-oct-2026 |
| 2 | Fed subió el 16-sep a 3,75–4,00 % (catalizadores:11) | CONFIRMADO ("raise the target range … by 1/4 percentage point to 3-3/4 to 4 percent") | PRIM-LEÍDA | [Comunicado FOMC 16-sep-2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm) |
| 3 | BCE: decisión 29-oct y 17-dic (R10) | CONFIRMADO (día 2 con rueda de prensa) | PRIM-LEÍDA | [BCE, calendario del Consejo de Gobierno](https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html) |
| 4 | BoJ 29-30-oct y 17-18-dic (R10) | CONFIRMADO; Informe de Perspectivas el 30-oct | PRIM-LEÍDA | [boj.or.jp, calendario MPM](https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm) |
| 5 | IPC oct → 10-nov; nov → 10-dic (R10) | CONFIRMADO | PRIM-LEÍDA | [BLS, calendario CPI](https://www.bls.gov/schedule/news_release/cpi.htm) |
| 6 | Consulta MAS P015-2026 cierra 16-oct 23:59 (R04P) | CONFIRMADO ("closes at 11.59 PM on 16 October 2026") | PRIM-LEÍDA | [MAS, ficha de la consulta](https://www.mas.gov.sg/publications/consultations/2026/consultation-on-proposed-amendments-to-the-payment-services-act-for-stablecoin-regulation) |
| 7 | Swell 27–29-oct (calendario-regiones) | CONFIRMADO (Nueva York) | PRIM-LEÍDA (organizador = parte interesada, válido para la fecha) | [swell.ripple.com](https://swell.ripple.com/llms.txt) |
| 8 | Evernorth: cierre 9-oct, XRPN cotiza 12-oct (cerebro, R11P, R12P) | CONFIRMADO ("began trading on Nasdaq on October 12, 2026"; "Closing on October 9, 2026") | PRIM-LEÍDA | [8-K EDGAR, CIK 2092592](https://www.sec.gov/Archives/edgar/data/2092592/000119312526419146/d24481d8k.htm) (presentado 13-oct) |
| 9 | Innovation Exemption = acciones tokenizadas, ~17-sep, 5 años (R11P) | CONFIRMADO: 17-sep-2026; "expire five years after publication"; pide comentarios | PRIM-LEÍDA | [SEC, comunicado 2026-90](https://www.sec.gov/newsroom/press-releases/2026-90-sec-issues-innovation-exemption-facilitate-trading-tokenized-nms-stock-request-comment) |
| 10 | Red A7: 91.500 M$ "en ene-2026" (R06P) | **CORREGIDO**: "as of January 2026", autoinformada, periodo no especificado; FinCEN: comentarios 30 días tras el Federal Register | PRIM-LEÍDA | [Tesoro sb0644, 1-oct-2026](https://home.treasury.gov/news/press-releases/sb0644) |
| 11 | HKMA: dos primeras licencias de stablecoin 10-abr-2026 (R07P) | CONFIRMADO (Anchorpoint FRS01, HSBC FRS02; la HKMA dice que el número seguirá "very limited") | EXTRACTO | [HKMA, comunicado 20260410-4](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/04/20260410-4/) |
| — | CLARITY: cloture 49-50 el 15-sep | Intentado: la lista de votaciones de senate.gov no devolvió la votación con curl | SECUND (se mantiene) | — |

Resultado: **10 confirmadas, 1 corregida (lectura), 0 falsas.** El calendario macro de R10 queda ya en fuente oficial entera.

## 5. Lecciones del cerebro: duplicadas, contradictorias o largas (propuesta, NO aplicada)

`patrones-de-bulos.md` (40 líneas de lección; tiende a repetirse):
- **Duplicadas**: :18 y :20 (el "gran socio coreano" de Ripple) → fusionar en una línea. :10, :17, :21, :32 y :33 dicen lo mismo ("buscadores mezclan fechas o páginas sin fecha") → una sola línea con 2-3 ejemplos. :25 y :40 (vídeos del mismo canal / datos de vídeo contra el BCE) → fusionar. :9 y :30 (predicciones de precio) → fusionar.
- **Resuelta**: :23 "[VERIFICAR]" de Sibos 2027 → ya confirmado.
- **Demasiado largas**: :34, :41, :44 (tres ideas cada una) → partir o recortar a la regla ("leer el verbo", "exigir nombre del documento").
- Ahorro estimado: de 40 a ~30 líneas sin perder ninguna regla.

`fuentes-fiables-y-dudosas.md`:
- **Contradicción**: :6 pone ripple.com y stellar.org como "fiables (primarias)"; :32 y :35 las llaman parte interesada. Proponer: "primarias de lo que dice la empresa; no de cifras ni de impacto".
- **Desfasada**: :33 "sec.gov no abrió" → corregir con :36 (sí abre con curl + User-Agent).
- **Duplicadas**: :13 y :22 (Despeja La X) → una línea. :18 y :21 (iea.org 403) → una línea.
- **Nueva (de hoy)**: boj.or.jp y ecb.europa.eu (calendario) abren; senate.gov (lista de votaciones) no.

`catalizadores-xrp-xlm.md`:
- No hay duplicados reales, pero las líneas :22 a :33 (una por informe) son resúmenes de informe, no "qué evento movió el precio y cuánto". La propia regla del archivo pide eso. Propuesta: a partir de ahora, solo eventos con efecto medido o fecha confirmada; el resto, en los informes.
- :6 ("CLARITY Act fracasa") queda corregida por :17, pero quien lea solo :6 se lleva el error. Con la regla de no reescribir, basta con que la corrección ya esté; no hay acción.

## 6. Huecos por impacto: documentos que Joel debería descargar a `research/fuentes/`

Ordenados por cuánto pesan en las conclusiones. **Nuevo**: lo marcado (SEC) ya lo puedo leer yo con curl en otra tarea, sin descarga.

| # | Documento | URL de partida | Nombre sugerido |
|---|---|---|---|
| 1 | Informe Anual RBI 2025-26 (tabla de e₹) — captcha | rbidocs.rbi.org.in (enlace en R02:18) | `rbi-informe-anual-2025-26.pdf` |
| 2 | Declaración de Nueva Delhi (BRICS) — 403 | pib.gov.in / brics2026.gov.in | `brics-declaracion-nueva-delhi-2026.pdf` |
| 3 | Resoluciones BCB 519/520/521, 561 y 584 — web JS | normativos.bcb.gov.br (buscar por número) | `bcb-res-519-520-521.pdf`, `bcb-res-561.pdf`, `bcb-res-584.pdf` |
| 4 | Consulta MAS P015-2026 + Anexo C (cierra mañana) | ficha MAS (enlace §4, n.º 6) | `mas-p015-2026-consulta.pdf`, `mas-p015-2026-anexo-c.pdf` |
| 5 | Informe del prototipo Agorá (BIS, 97 págs.) — ECONNRESET | bis.org/publ (proyecto Agorá) | `bis-agora-prototipo-2026.pdf` |
| 6 | Propuestas GENIUS de la Fed (24-sep) | federalreserve.gov, comunicados 24-sep-2026 | `fed-genius-propuestas-2026-09-24.pdf` |
| 7 | Comunicado DTCC–Stellar (27-may) — 403 | dtcc.com/news | `dtcc-stellar-2026-05-27.pdf` |
| 8 | Ley rusa 282-ФЗ — ECONNRESET | publication.pravo.gov.ru | `rusia-ley-282-fz-2026.pdf` |
| 9 | Reglamentos UE paquetes 20.º y 21.º | eur-lex.europa.eu | `ue-paquete-20.pdf`, `ue-paquete-21.pdf` |
| 10 | Reforma FIEA de Japón y lista de criptoactivos (¿XRP?) | fsa.go.jp | `japon-fiea-reforma-2026.pdf` |
| — | (SEC, sin descarga) Regulation Crypto Assets S7-2026-27; interpretación SEC–CFTC 17-mar (Rel. 33-11412); propuesta de custodia 1-oct; Form 425/8-K de Evernorth con cifras de XRP | sec.gov con curl | tarea corta propuesta |

## 7. Conclusión: confianza por área

| Área | Confianza | Por qué (una frase) |
|---|---|---|
| Macro / calendario de bancos centrales | **Alta** | Tras el muestreo de hoy, Fed, BCE, BoJ y BLS están en fuente oficial leída. |
| Regulación por región | **Media** | Singapur, Hong Kong y el Tesoro de EE. UU. tienen primaria; Brasil, Rusia, UE, Japón, India y Corea dependen de despachos y prensa con cita (webs oficiales cerradas). |
| Ripple / Stellar | **Media-baja** | Casi todo procede de la propia empresa (ripple.com, stellar.org) o de agregadores; reguladores (OCC, CSSF, JFSA, MAS) sin leer en su web. |
| 13F / ETF | **Alta** en los datos leídos, **baja** en la interpretación | Las tablas de EDGAR son primarias; el 13F no permite inferir intención ni momento (R21 lo dice bien). |
| Calendario de catalizadores cripto | **Media-alta** | Swell, MAS y Evernorth ya confirmados; quedan el plazo de Brasil (cálculo propio) y fixCleanup3_4_0 (aprox.). |

**Hechos vs. opiniones:** todo lo de §1, §3 y §4 son hechos comprobables; las valoraciones de confianza de §7 son **opinión mía** sobre la calidad de las fuentes, no sobre XRP/XLM. Nada de este informe es recomendación de compra/venta.

## Correcciones propuestas para el cerebro (solo con visto bueno de Joel; se añadirían bajo "## Correcciones 2026-10-15")
1. `evernorth-xrpn-tesoreria-xrp.md`: las fechas 9-oct (cierre) y 12-oct (XRPN) quedan **confirmadas en el 8-K de la SEC** (PRIM-LEÍDA); quitar "[VERIFICAR en la SEC]" de la corrección de R12P.
2. `catalizadores-xrp-xlm.md`: red A7 = "más de 7,5 billones de rublos (91.500 M$) a enero de 2026, autoinformado, periodo no especificado"; e₹ −24 % = SECUND [VERIFICAR]; plazo de Brasil = cálculo propio de una sola fuente; "60 días" de la Fed = [VERIFICAR].
3. `fuentes-fiables-y-dudosas.md`: matizar la línea 6 (ripple.com/stellar.org = parte interesada) y corregir la 33 (sec.gov sí abre con curl).
4. `patrones-de-bulos.md`: Sibos 2027 confirmado; Innovation Exemption 17-sep confirmado en sec.gov; Meritz "firma 1-oct" = una sola fuente.
