# Auditoría A (coherencia) + B (huecos) — Explorador, voces, radar y calendario

Hecha el 23-oct-2026 (noche). Solo lectura: no se ha modificado ningún archivo existente ni se ha hecho commit/push. Las correcciones están listadas para que Joel las apruebe. Sin recomendaciones de compra/venta; las cifras de precio futuro son [ESPECULACIÓN]. [P] = fuente primaria; [S] = prensa o agregador; «no verificado» = no se pudo comprobar. Línea base: `python scripts/revisar_explorador.py` → **0 avisos**, 9 capas, 44 movimientos, radar de 136 celdas (54 sin dato real; ver nota en §5).

## 1. Resumen (8 líneas)
1. El comprobador pasa limpio, pero **no ve** los fallos de fondo: contradicciones de cifras entre archivos, niveles de evidencia inflados y plazos sin entrada en el calendario.
2. Las 2 correcciones más graves son datos que se contradicen: **Evernorth 473 M XRP** (voz v032, «confirmada») frente a **388,9 M** (8-K, en `datos.json`), y **ETF de XRP «$2.178 M»** en 4 sitios de `datos.json` cuando T19 (23-oct) no encontró su origen y el AUM de 22-oct es ≈ $1.430 M [S].
3. El informe de vídeos del 22-oct sigue con **[VERIFICAR] ya resueltos** (OCC, 8 MB del BIS, cartas SEC, Swift 11.500, BoJ): hasta dice que «no hay norma final de la OCC» el día antes de que se publicara y lo contradice el propio v016 [P].
4. Faltan en el calendario 6 plazos que prometen voces (DTCC–Stellar 1S-2027, Swift Ledger y JPMD en Canton 2026-12, fin del Congreso 3-ene-2027, Sibos 2027, Collateral AppChain como evento propio) y hay 2 entradas caducadas (Evernorth 12-oct, Moody's Francia «hoy»).
5. Ni `regulacion.json` ni `datos.json` tienen **ningún enlace**: el usuario no puede ir a la fuente primaria desde el radar ni desde las capas (solo `voces.json`, calendario y paneles los tienen).
6. Diversidad de opinión: **29 de 44 voces vienen de un único canal** (Despeja La X, único canal en `canales`); no hay ningún escéptico académico, banco central crítico, analista de ETF ni agencia de rating; la capa **Deuda** tiene solo 2 voces y **Depósitos tokenizados** 0 fuentes P.
7. Huecos del radar: 54 celdas sin dato (40 %), concentradas en Irán, Egipto, Etiopía, Sudáfrica, Indonesia y en los temas política monetaria, ETF y custodia.
8. Cola: lo más urgente por caducidad es **Brasil (30-oct)** y **Corea (11-nov)**; lo más barato y útil, **D08 (subastas) y T18 (energía)**. Propongo un «R00 v2» con un script sin IA que calcule voces nuevas y plazos que vencen.

## 2. Hallazgos de coherencia

| # | Sev. | Dónde | Qué pasa | Corrección propuesta |
|---|---|---|---|---|
| C1 | **Alta** | `voces.json:908` (v032, P/confirmada) frente a `datos.json:1369, 1405, 2288` | La voz dice «unos 473 M de XRP»; `datos.json` dice que el **8-K confirma 388,9 M** (473 M = pro forma del Form 425 a 31-dic-2025). También el informe de vídeo del 23-oct (`videos/2026-10-23-…:49 y 63`) pone «Evernorth ≈473 M [P]» sin matiz. Ya lo anotaban R39 (#10) y la revisión del 18-oct (#5). | Reescribir v032: «473 M pro forma (Form 425, a 31-dic-2025); el 8-K confirma 388,9 M aportados en especie». Añadir la nota en los informes de vídeo. |
| C2 | **Alta** | `datos.json:1257, 1335, 1391, 2202` (capa fondos); `research/GUIA-ESTILO-CIFRAS.md:8, 23`; `research/COLA-TEMAS-GEMINI.md:46` | «ETF de XRP ≈ $2.178 M»: T19 (`2026-10-23-T19…:20`) dice que **no localizó su origen** y que «no usar como cifra». Cifras de T19: ≈ $1.430 M (22-oct, The Block [S], suma propia) y ≈ $1.570 M (9-oct, SoSoValue [S]). La guía de estilo usa $2.178 M como ejemplo y puede confundirse con un dato. | Sustituir por «≈ $1.430 M a 22-oct [S]» y quitar «entradas de 2026 ≈ $864 M» (no verificado). Cambiar el ejemplo de la guía por una cifra inventada claramente (p. ej. `$2.000 M`). |
| C3 | **Alta** | `informes/videos/2026-10-22-despeja-la-x-seis-videos-15-22-oct.md:41, 74` frente a `:100` y `voces.json` v016 | La fila 41 y la línea 74 dicen «no hay norma final de la OCC… prevista para nov-2026»; la fila 100 y v016 [P] dicen que la OCC la **publicó el 21-oct** (NR 2026-92). Un informe público se contradice a sí mismo. | Cerrar la fila 41 con «resuelto: norma final 21-oct [P]» y corregir la línea 74. |
| C4 | Media | Mismo informe, filas `:27, 42, 47, 40, 115, 148` | [VERIFICAR] ya resueltos por `2026-10-23-verificaciones-pendientes.md`: «8 MB» sí consta (BIS WP 1374, pág. 28) → `:27` y `:115` dicen «no encontrado»; Swift «11.500» confirmado (`:47`, `:148` dicen «no la encuentro»); cartas SEC S7-2026-27 con coalición y Coinbase en el listado [P] (`:42`); BoJ decide el 30-oct (`:40`, T17 y calendario). | Añadir al final del informe una tabla «Resuelto el 23-oct» (no reescribir). |
| C5 | Media | `datos.json:1435, 1585` (EE. UU. 10 años 5,13 % «21-oct») frente a `informes/2026-10-22-cierre.md:16` y `2026-10-23-cierre.md:55` | Cierre del 22-oct: 4,96 % (−17 pb); 23-oct ≈ 5,00 %. El texto y la cifra dicen que «se actualiza solo», pero el texto `t` y el movimiento `:2340` quedan fijos en 21-oct. Coincidencia con el TEC 10 francés (5,13 % el 22-oct) comprobada en `bonos-manual.json`: son datos distintos. | Confirmar que `actualizar_paneles.py` reescribe `t` y `v`; si solo reescribe `v`, hacer el texto genérico («cierre del último día publicado»). |
| C6 | Media | `eventos/calendario.toml:179-185` | «Evernorth (XRPN): debut previsto en Nasdaq 12-oct»; ya debutó (v032, `datos.json:2288`, vídeo 07-oct §rastreo). | Marcarlo `cumplido` o moverlo a hecho con la nota «cotiza desde el 12-oct». |
| C7 | Media | `calendario.toml:522-525` | «Moody's Francia: revisión de hoy (Aa3, negativa)»: el cierre del 23-oct la deja pendiente (sin noticia a las 20:06 UTC). `calificaciones.json` (Francia) tiene la misma fecha. | Cambiar a «pendiente de publicación» y actualizar el 24-oct (R00 de apertura). |
| C8 | Media | `voces.json` plazos de v001 (2027-06), v003 (2026-12), v012 (2027-09), v014 (2026-12), v018 (2027-01), v041 (2026-12); calendario | Ninguno tiene evento propio. Solo existe DTCC «octubre» (`:538`, que menciona Collateral AppChain en el texto) y euro digital 2027-07-01. v026 (2027-06) está cubierto por el 1-jul-2027. | Añadir 6 eventos: DTCC–Stellar (jun-2027), Collateral AppChain (4T-2026), Swift Ledger (dic-2026), JPMD en Canton (dic-2026), fin del 119.º Congreso (3-ene-2027), Sibos 2027 (20-23 sep, Singapur) con `aproximado = true`. |
| C9 | Media | `voces.json` v003 (P/compatible) | Nivel **P** con fuente DTCC 12-may, pero T20 (`informes/research/2026-10-23-T20-dtcc-tokenizacion.md`, §3 y fuentes) dice «[P, titular; plazo 4T vía buscador]»: el plazo 4T-2026 no se leyó en la primaria. Además el vídeo dijo «1T-2027» sin fuente. | Bajar a D (nota de DTCC: colaboración leída; plazo [S]) o releer la nota entera. |
| C10 | Media | `voces.json` v019 (D/compatible) | Nivel **D** («cita localizada con fecha y lugar») pero la nota admite: clip de 56 s en X de una cuenta menor, cita no transcrita, fecha aproximada. | Bajar a S, o a C si se prefiere. |
| C11 | Media | `voces.json` v027 (S, «según la prensa previa») frente a `datos.json:40` (k=P) y `:202` | La voz dice S y la capa dice «Pontes en marcha desde el 21-sep» como P (el origen es el dossier del 9-oct, anterior al 21-sep en parte). Mismo hecho, dos niveles. | Igualar: S hasta leer la nota del BCE del 21-sep. |
| C12 | Media | `calendario.toml:488-495` y `regulacion.json` (ue·ley_marco `proxima` 2027-07-10) | Dicen «el texto en EUR-Lex no se ha leído» / «[S] EUR-Lex no cargó»; `verificaciones-pendientes` lo leyó: **art. 90, aplicable desde 10-jul-2027** [P]. | Pasar a [P] en ambos y citar art. 79(1) y 90. |
| C13 | Media | `regulacion.json` (136 celdas), `datos.json` | Cero enlaces: el campo `fuente` solo vale `P`/`S`/`VERIFICAR`. No hay forma de pulsar y llegar a la fuente. (voces.json: 54 URL, todas https.) | Añadir `url` por celda y por ítem de capa (empezar por las 82 celdas con etapa). |
| C14 | Baja | `voces.json:265, 288, 293` (v008) | «100 $», «10.000 $» (símbolo detrás): rompe la guía de cifras. | `$100`, `$10.000`. |
| C15 | Baja | `datos.json:2427` | «55.000 M$» y «1,1 billones de dólares» (≈ `$1,1 billones`/`$1.100 mil M`; el 5 % → `$55 mil M`). Pasó el comprobador. | Reescribir con símbolo delante y `mil M`. |
| C16 | Baja | `paneles.json:6` | `"unidad": "miles de millones de dólares (MM$)"` (`MM$` está prohibido). | `mil M de $`. |
| C17 | Baja | `calendario.toml` cabecera línea 2 y 10 entradas con `impacto = "bajo"` | La cabecera documenta solo `alto | medio`. | Documentar `bajo` en la cabecera. |
| C18 | Baja | `calendario.toml:127-133` | Detalle del XRPL (26/35, 29 necesarios, [S]) frente a lectura [P] del 23-oct (xrplcluster: mayoría desde 21-oct 14:46:22 UTC; activación más temprana 4-nov 14:46 UTC). Los denominadores 35 y 32 vienen de fuentes distintas. | Añadir «[P] 23-oct» y aclarar «80 % de los validadores activos». |
| C19 | Baja | `datos.json` ítems de la capa deuda (`n`) | `n` guarda el nivel («P ledger», «P empresa») en las capas normales y **texto de la fuente** en deuda. | Dejar `n` solo para el nivel y mover la fuente a `f`. |
| C20 | Baja | `research/COLA-TEMAS-GEMINI.md` tabla «Estado» | Dice «T05-T25 pendientes», pero hechos: T05, T17, T19, T20, T21, T22, T24. | Actualizar la tabla. |
| C21 | Baja | `voces.json` v044 (P/confirmada) | Fuente: web «Who we are» (403 a curl; no abierta aquí); el texto cita el informe anual 2024 «vía buscador». `verificaciones-pendientes` dice que el PDF no se abrió. | Cambiar `fuente.n` a «Swift, Who we are (web)» o abrir el informe. |
| C22 | Baja | `voces.json` URL | Con curl: 58 devuelven 200, 2 devuelven 202 (EUR-Lex), 25 devuelven 403 (anti-bots: SEC, Swift, AFT, BLS, medios) y **1 devuelve 404: v039 `nippon.com/en/news/yjj2026080300142/`**. | Reabrir v039 en el navegador integrado: si es 404 real, sustituir la fuente (Reuters/Jiji/Tesoro). |

Coherencias **verificadas sin fallo**: plazos de radar frente a calendario (FOMC 27-28, BCE 28-29, BoJ 29-30, Copom 3-4 nov, RBI 2-4 dic, LPR 20-nov, Corea 11-nov y 26-nov, DAC8, Brasil 30-oct/30-nov, Rusia 2027); OCC/GENIUS 18-ene-2027 (calendario, radar y v016); XRPL 4-nov; 5,13 % de Francia; niveles `P/D/S/C/R/E` válidos en las 44 voces; ninguna URL con `http://`; `privado/voces-tesis.json` solo referencia ids que existen (v001-v044) y 20 voces (v004, v009, v015, v017, v021, v023-v026, v030, v031, v033, v034, v037-v041, v043, v044) no se usan en ninguna prueba (no copio su contenido).

### Reglas que el comprobador debería tener (propuestas, no implementadas)
1. Símbolo de moneda detrás de la cifra (`\d \$`), `M\$`, `MM\$`, `billones de dólares` y `(MM$)` en `unidad`.
2. `nivel P` ⇒ `fuente.url` en dominio de la lista primaria (sec.gov, dtcc.com, bis.org, fsb.org, occ.gov, cftc.gov, europa.eu, swift.com, federalreserve.gov…); si no, aviso.
3. `conf = confirmada` ⇒ `nivel ∈ {P, D, S}` con `fuente`; `nivel = P` con `nota` que contenga «vía buscador», «titular» o «no transcrita» ⇒ aviso.
4. Cada `plazo.prometido` (voces) debe tener un evento del calendario con fecha ± 31 días; avisar de los que no.
5. Evento del calendario con `fecha` < hoy y `titulo` que contenga «previsto» o «debut» ⇒ aviso de caducado.
6. Misma cifra con 2 valores: lista de claves (`473 M`, `388,9 M`, `2.178 M`, `5,13 %`) buscada en `explorador/*.json`, `eventos/*.toml` e `informes/2026-10-2*` con aviso si difieren.
7. Celdas del radar y capas sin `url`.
8. Voces con 2 `nivel` distintos para el mismo hecho (se detecta por entidad + fecha).
9. Texto de la capa que empiece en minúscula salvo palabra de una lista de nombres propios (`mBridge`, `iPhone`…): hoy lo marcaría como falso positivo; ya conviene prever la excepción.

## 3. Huecos medidos

### 3.1 Por capa (voces.json + datos.json)
| Capa | Voces | De ellas P | Vía Despeja La X | Sin confirmar | Ítems de capa (prod/piloto/plan) | Movimientos |
|---|---|---|---|---|---|---|
| Bancos centrales y CBDC | 7 | 1 | 5 | v026 (contradicha) | 3/3/1 | 7 |
| Stablecoins | 5 | 3 | 2 | — | 3/0/1 | 4 |
| **Depósitos tokenizados** | 4 | 1 | 3 | v041 | 1/1/1 (**0 ítems P**) | **1** |
| Redes y activo puente | 6 | 2 | 5 | v006, v008, v035 | 2/0/1 | 6 |
| Tokenización (RWA) | 9 | 4 | 6 | — | 2/1/2 | 4 |
| Liquidación y custodia | 10 | 5 | 6 | v036 | 2/1/1 | 5 |
| Regulación y política | 13 | 4 | 8 | v018 | 1/0/1 | 6 |
| Fondos, ETF y tesorerías | 5 | 1 | 4 | v036 | 3/0/1 | 5 |
| **Deuda soberana y bonos** | **2** | 1 | 2 | — | 8/0/0 | 6 |

Conclusiones: Deuda tiene los mejores datos P (8 ítems) pero solo 2 voces; Depósitos tokenizados no tiene ninguna fuente primaria en la capa y solo 1 movimiento; Fondos tiene 1 sola voz P (Evernorth). 29 de 44 voces dependen de un vídeo; 15 no. Redes citadas en voces: XRPL 11, Stellar 5, Canton 3, Besu 3 (el reparto multi-red existe, pero con muestra pequeña).

### 3.2 Radar (136 celdas)
- 68 celdas tienen `etapa = null`; 14 de ellas son de política monetaria y usan `dir` (sube/mantiene/baja), así que **sin dato real hay 54** y con dato 82 (68 con etapa 0-5 y 14 con dirección). Los recuentos por país y tema de abajo cuentan las 68 con `etapa = null`.
- Sin dato por país (etapa nula): Irán 8/8, Egipto 7/8, Etiopía 6/8, Sudáfrica 6/8, Indonesia 6/8, Emiratos 5/8, Japón 4, India 4, Rusia 4, BRICS/BIS 4, Singapur 3, China 3, resto ≤ 2.
- Sin dato por tema (etapa nula): política 17 (14 con `dir`), ETF 11, custodia 10, fiscal 9, tokenización 9, CBDC 7, stablecoins 4, ley marco 1.
- `huecos[]` del propio archivo: Egipto, Etiopía, Irán (parcial), Arabia Saudí, Reino Unido y Suiza (fuera de la matriz), Canadá y Australia, custodia fuera de EE. UU. y la UE, política monetaria de MAS/HKMA/BOK/BCB/CBUAE.
- Calidad de dato: 82 celdas con dato, 0 con etapa y sin `fuente`; 33 sin fecha de revisión; todas con `P`/`S` pero sin enlace (C13). Hay `S` en: Corea (ETF, custodia), Japón (ETF), Singapur (CBDC), China (ETF, CBDC, ley marco), Brasil (tokenización, CBDC, fiscal), India (stablecoins, ley marco), Emiratos (fiscal), Sudáfrica/Indonesia/Egipto/Etiopía (todo).

### 3.3 Diversidad de opiniones por capa (qué hay y qué falta)
| Capa | Hay hoy | Falta (candidatos; comprobar antes de citar) | Dónde buscarlo |
|---|---|---|---|
| CBDC | BCE, FSB, Parlamento Europeo, Lagarde 2018, un vídeo | Críticos del euro digital: bancos alemanes y españoles (asociaciones), Bundesbank, ponentes del PE; defensores del dinero en efectivo; informes comparados | Páginas del Consejo/PE/BCE; ESBG, EBF; Atlantic Council CBDC Tracker; informe anual del BIS |
| Stablecoins | FSB, OCC, ABA, U.S. Bank | Banco de Inglaterra, BCE (Lane/Cipollone), FMI GFSR, Fed (gobernadores), Circle/Tether/Coinbase como parte interesada, ICBA, calificadoras | Discursos en bankofengland.co.uk, ecb.europa.eu, imf.org; comentarios de la OCC (docket) |
| Depósitos tokenizados | JPM, U.S. Bank, HKMA | Críticos de los depósitos tokenizados (Digital Asset/Canton, Malekan), bancos europeos, BIS «Unified Ledger», supervisores | Informes del BIS (Agorá), EBA, comentarios a la OCC |
| Redes y puente | Garlinghouse, Claver, Swift, BIS WP 1374, vídeo | **Escépticos de XRP como puente** (académicos, bancos que usan Swift), Visa/Mastercard, Wise, estudios del FMI/BIS sobre liquidez on-demand, comunidad Ethereum/Solana/Hedera como competencia | Working papers del BIS/FMI; Finextra; discursos de Swift |
| Tokenización | DTCC, Stellar DF, Chainlink/Cardano/Aptos/Ava/Hedera (carta SEC), Fink | Detractores de acciones tokenizadas: bolsas (WFE), SIFMA, comisionados de la SEC en discrepancia, ESMA, IOSCO, académicos | Cartas al expediente S7-2026-27, informes de IOSCO/ESMA |
| Custodia | DTCC, J.P. Morgan, CSD BR, Ripple | Basilea (tratamiento prudencial), BNY/State Street, ICBA (recurso), supervisores europeos | Comité de Basilea (bis.org/bcbs), comunicados de la OCC |
| Regulación | CFTC, SEC, McHenry, senadores demócratas, Witt, Ripple, Bitvavo | **Críticos de izquierda y de la industria**: AFR, Better Markets, Public Citizen; republicanos favorables (Hill); ESMA; reguladores asiáticos | congress.gov (audiencias); comentarios públicos de la SEC |
| Fondos / ETF | Evernorth, Fink | **Analistas de ETF** (Bloomberg Intelligence, Morningstar), emisores (Bitwise, Franklin, Canary), críticos de las tesorerías cotizadas (prima/descuento sobre NAV), gestores bajistas | 424B3/10-Q en EDGAR; SoSoValue/Farside como [S] |
| Deuda | BlackRock BII, Bessent | FMI (Fiscal Monitor), BIS, OCDE, Tesoro (TBAC), agencias de rating, economistas bajistas y alcistas, BCE (estabilidad financiera) | imf.org/fm, bis.org, treasury.gov/TBAC, comunicados de las agencias |

Hecho: en todo `voces.json` solo hay **un canal** (`canales[0]`, con conflicto de interés declarado: tenedor de XRP/XLM y promoción de un exchange). Falta, al menos, un segundo canal de otra orientación (macro, regulatorio o escéptico) y un registro de «voces a favor/en contra» por capa (campo `postura`: favor/neutral/crítica/ interés propio).

### 3.4 [VERIFICAR] abiertos consolidados (con salida real o no)
| Punto | Origen | ¿Salida real? | Cómo / coste |
|---|---|---|---|
| Ripple en el expediente SEC S7-2026-27 (carta) | verificaciones; v023 (S) | **Sí** | Buscar «Ripple» en el listado de comentarios con Chrome (la paginación repetía resultados) |
| Voto de la Cámara H.R. 3633: 294-124 o 294-134 | vídeos 22-oct `:103` | **Sí** | congress.gov / clerk.house.gov (recuerdo 294-134, **no verificado**) |
| Precios XRP/XLM en la fecha de grabación (1,34; 1,30; ≈0,18) | vídeos 22-oct `:53, 55, 186` | **Sí (aprox.)** | Histórico CoinGecko/CoinMarketCap [S]; no son fuente P |
| Fecha del BoJ (30-oct) | vídeos 22-oct `:40` | **Ya resuelto** (T17: decide el 30) | Cerrar |
| OCC, 8 MB BIS, cartas SEC, Swift 11.500 | vídeos 22-oct | **Ya resueltos** | Cerrar (C3, C4) |
| JPMD operativo en Canton (v041) | verificaciones; T21 | **Parcial** | Nota de JPMorgan/Canton y X de Canton; T21 dice que JPMD está en Ethereum desde el 19-oct («vía buscador»). Sin acceso a la nota original: no verificado |
| 4.000 bancos corresponsales de JPM | verificaciones | **No** (cifra del vídeo; búsqueda negativa) | Dejar como «no encontrado» |
| Entrevista de La Salla («aceite») | verificaciones; v004 | **Improbable** | Vídeo del panel de Georgetown 23-sep si es público; coste alto |
| Entidades UE con MiCA que custodian XRP | verificaciones; T05 | **Parcial** | Lista de activos de BitGo Europe, Zodia, Bitstamp en sus webs |
| Declaración original «no queremos una sola empresa privada»; identidad de la responsable del BIS; qué «otras dos redes» | vídeo 23-oct `:22, 26, 65` | **No** (de momento) | Pedir al canal la fuente; sin ello se queda en C |
| v006 Garlinghouse «14 %» (sin transcripción) | voces | **Parcial** | Vídeo del XRP APEX 2025 en el canal oficial; sin subtítulos no se transcribe |
| v008 Claver (sin subtítulos) | voces | **No** (salvo transcripción) | — |
| v018 McHenry (desenlace) | voces | **Solo con el tiempo** (3-ene-2027) | Calendario |
| v035 / v036 | voces | **No** (E y R; no comprobables) | Mantener |
| v026 | voces | **Resuelta** (contradicha; euro digital 2S-2027) | — |
| 13 semanas de entradas ETF (titular del bot) | T19 | **Parcial** | Farside/SoSoValue como [S] |
| Cifra oficial de acciones y de XRP en custodia de los ETF | T19 | **Sí** | 10-Q/424B3 en EDGAR (Chrome) |
| Lanzamiento DTCC, lista de 25 valores y de redes | T20; calendario `:538` | **Sí (en 1-2 semanas)** | dtcc.com/press-releases |
| Marco de evaluación L1/L2 de DTCC | T20 | **Sí** | PDF en dtcc.com |
| Registro de compromisos del Global Forum; primer informe DAC8 (31-ene o ≈30-sep-2027) | T24 | **Parcial** | OCDE y leyes nacionales |
| Hitos 1S-2026 de Ripple/Stellar; auditoría de 300.000 cuentas | T22 | **Parcial** | GitHub del XRPL; CoinDesk (tercero) |
| Tabla del Tesoro español con fechas de sep-2025 | D09; `calificaciones.json` (España) | **Sí** | Comunicados de las agencias |
| Convocatoria a comercios del piloto del euro digital (27-oct) | radar ue·cbdc | **Sí (tras el 27-oct)** | Nota del BCE |
| Hong Kong: tipo base (4,25 % o 5,0 %) | COLA-TEMAS T09 | **Sí** | HKMA |

## 4. Priorización de huecos (valor, coste, siguiente paso)
Costes en % de cuota semanal: estimación propia (no medida). Los ≈1 % de D01-D05 y D08 vienen de `COLA-DEUDA-BONOS.md`.

| Prioridad | Tarea | Valor | Coste est. | Siguiente paso |
|---|---|---|---|---|
| 1 | Correcciones C1-C13 (sin IA, edición de JSON/TOML) | Alto (quita contradicciones públicas) | ≈ 0,5-1 % | Aplicar tras el OK de Joel |
| 2 | **T11 Brasil** (vence el 30-oct y el 30-nov) | Alto, **caduca** | ≈ 1,5 % | Tandas de 3 países con T12 y T13 (≈ 3-4 % la tanda) |
| 3 | **T07 Corea** (comentarios hasta el 11-nov; 4-feb-2027) | Alto, caduca | ≈ 1,5 % | Tanda con T06 (Japón) y T08 (Singapur) |
| 4 | **D08** subastas de deuda (calendario) | Medio-alto, barato | ≈ 1 % | Eventos nuevos en el calendario |
| 5 | **T18** energía y geopolítica (Brent 110-116, Ormuz) | Alto (macro) | ≈ 1,5 % | Con fuentes EIA/OPEP |
| 6 | **T16** organismos (BIS, FMI, FSB, GAFI) | Alto para voces (reguladores críticos) | ≈ 1,5 % | Prioridad si se quiere diversidad de opinión |
| 7 | **T23** Ripple y Stellar por región | Medio-alto (nombran o no el token) | ≈ 2 % | Tras T16 |
| 8 | T09 Hong Kong, T10 India, T14 China, T15 BRICS sin cubrir | Medio | ≈ 1,5-2 % cada uno | Tanda de 3 (≈ 4-5 %) |
| 9 | D01 Italia, D02 Alemania, D03 Francia (OAT), D05 (30 años) | Medio (paneles) | ≈ 1 % cada una | Con navegador; D02 falla desde este equipo |
| 10 | D04 China bonos | Medio-bajo (webs en chino) | ≈ 1,5-2 % | Última |
| 11 | T25 tema libre | n/d | ≈ 1-2 % | Joel decide el tema |

Orden global sugerido con ≈ 43 % de cuota disponible hasta el reinicio del 27-oct: corrección sin IA → T11 → T07 → D08 → T18 → T16; el resto para la semana nueva.

## 5. Propuesta «R00 v2» (informes diarios más profundos)
Estructura (máx. 2 páginas; seguridad en 1 línea):
1. **Plazos que vencen** (script sin IA, ≈ 0 %): cruza `voces.json[].plazo` y `calendario.toml` para los próximos 7 días y los vencidos sin resolver (hoy: v002 octubre; v027 cumplido; Moody's Francia; Evernorth). Salida: lista de 5 filas.
2. **Voces nuevas del día** (≈ 0,5 %): 3-5 declaraciones nuevas con fuente P/D/S de reguladores, bancos y escépticos, no solo del canal; propuesta de id `v045+` y nivel.
3. **Flujos de ETF**: AUM y flujo del día de los 5 ETF de XRP y de XLM (The Block/SoSoValue [S]); no inferir dirección de precio.
4. **Ledger**: enmiendas del XRPL (xrplcluster `feature`), protocolo de Stellar, TVL del AMM XRP/RLUSD; solo hechos.
5. **Macro en 5 líneas** (Fed, BCE, bonos a 10 años, Brent) con fuente y hora UTC.
6. **Bulos y fuentes** (máx. 2 líneas; lo que ya exige CLAUDE.md).
7. **Tesis (solo en local)**: el informe público solo dice «ver privado/ para la lectura»; el cruce con la tesis se escribe en `privado/` y nunca en `informes/`.
Coste por sesión (estimación): **apertura v2 ≈ 2 % | cierre v2-lite ≈ 1 %**; unos 3 % por día frente a un R00 actual no medido; con 5 días laborables ≈ 15 % semanal. Si la cuota aprieta, hacer v2 solo en la apertura y el cierre como lista de 10 líneas.

## 6. Plan ordenado (10 pasos)
1. Joel aprueba C1-C3 (alta) y se aplican con Edit sin IA; `python scripts/revisar_explorador.py` después.
2. Aprobar C4-C13 y anexar «Resuelto el 23-oct» al informe de vídeos del 22-oct.
3. Añadir al calendario los 6 plazos (C8) y cerrar Evernorth/Moody's (C6, C7).
4. Reescribir niveles de v003, v019, v027 y la fuente de v044 (C9-C11, C21).
5. Añadir las reglas 1-9 de §2 a `scripts/revisar_explorador.py` (código ≈ 40 líneas, sin IA).
6. Reabrir v039 (404) con el navegador integrado y sustituir la fuente.
7. Hacer T11, T07 y D08 (caducan antes del 11-nov).
8. Hacer T16 y buscar 8-10 voces críticas/escépticas; añadir `postura` y un segundo canal; ampliar capa Deuda y Depósitos tokenizados.
9. Añadir `url` por celda del radar (empezar por 82 con dato) y por ítem de capa.
10. Poner en marcha el R00 v2 y medir su coste real en la primera semana.

## 7. Lo que NO pude comprobar
- Las 25 URL con 403 (SEC, Swift, AFT, BLS, ABA, Bitvavo, medios): bloquean a curl; solo sé que existen, no su contenido ni su fecha. Solo comprobé el estado HTTP de las URL de `voces.json` y del calendario; no abrí `datos.json`/`paneles.json` enlaces (no tienen).
- Que `actualizar_paneles.py` reescriba el texto `t` de las cifras (C5): no abrí el script.
- 294-124 frente a 294-134 en la Cámara: sin congress.gov abierto: **no verificado**.
- Si JPMD está vivo en Canton y si JPMD llegó a Ethereum el 19-oct (T21): fuente solo «vía buscador».
- Los 14 `dir` de política monetaria del radar y su vigencia (solo vi el resumen).
- `privado/voces-tesis.json`: leí solo su estructura y referencias a ids; no valoré ni copié su contenido (privado/ no se sube). No leí `cerebro/`, `app.py` ni los informes G1-G17 completos; tampoco informes anteriores al 22-oct salvo búsquedas puntuales.
- Estimaciones de coste (% de cuota): no medidas; contrastar con el panel de uso de Claude.
