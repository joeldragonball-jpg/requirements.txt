# Tokenización de activos (RWA) global (2026-10-17, R26 profundo)

> **Aviso (R38, 17-oct):** BUIDL "−1,41 %" (RWA.xyz, 30 d) y "2,68 → 2,17 mil M$" (−19 %, DefiLlama, un mes) miden cosas distintas o usan ventanas distintas: no usar "se mueve poco" para BUIDL hasta aclararlo [VERIFICAR].
Plantilla: dossier-region (modo profundo). Etiquetas: **LEÍDO ENTERO** = documento primario descargado y leído en las partes relevantes; **API/página** = dato en vivo de un tercero (RWA.xyz, DefiLlama); **secundaria** = prensa/blog sin primario [VERIFICAR]. Sin recomendaciones de compra/venta.

## Resumen
1. Hay que separar dos números que se mezclan en titulares: RWA.xyz (16-oct-2026) da **39,3 mil M$ de valor "distribuido"** (tokens transferibles en cadena) y **371,2 mil M$ "representado"** (activos registrados fuera, no transferibles libremente). Las stablecoins van aparte (291,8 mil M$ según RWA.xyz; 306 mil M$ según DefiLlama el mismo día: el agregador cambia el total).
2. El grueso "distribuido" real es pequeño y concentrado: fondos monetarios del Tesoro de EE. UU. (USYC 2,4 mil M$, USDY 2,4, BUIDL 2,2, iBENJI 1,7, WTGXX 1,1...), oro (XAUT 3,0, PAXG 1,8) y crédito privado (syrupUSDC 1,1). Las acciones tokenizadas son de cientos de millones (SECZ 293 M$ como mayor).
3. Por red, RWA.xyz pone a Ethereum primero (16,9 mil M$), luego BNB Chain 6,1, Solana 4,4, **Stellar 3,5 (4.º)** y **XRP Ledger 0,497 (10.º)**. Quién informa: RWA.xyz es plataforma de análisis que vende datos a emisores ("Register Your Assets"): tercero con incentivo comercial, no auditor.
4. Primarios leídos: la carta de no-acción de la SEC a DTC (11-dic-2025) y la orden de exención de la SEC para negociar acciones tokenizadas con AMM (17-sep-2026, publicada 22-sep). Ambas son marcos temporales y condicionados, no un mercado ya abierto.
5. Lo que no he podido verificar en primario: cifras de BlackRock/Franklin/WisdomTree (las páginas de gestoras no se abrieron en esta pasada) y si el servicio de DTC ya está operativo (estaba previsto para 2S-2026).

## Qué es hecho verificado
| Dato | Fuente | Fecha | Nivel / idioma |
|---|---|---|---|
| Valor distribuido: **39,29 mil M$** (+1,35 % en 30 d); representado: **371,19 mil M$** (+0,40 %); titulares de activos: 5.277.416 (+16,6 %); stablecoins: 291,79 mil M$ (+0,03 %) | RWA.xyz, portada (app.rwa.xyz) | "as of 10/16/2026" | página (tercero), inglés; descargada con curl |
| Fondos del Tesoro tokenizados (valor): USYC 2,4 mil M$; USDY 2,4; BUIDL 2,2 (−1,41 %); iBENJI 1,7; **WTGXX 1,1 (−13,56 %)**; JLTXX 738 M; BENJI 680 M (−3,98 %); USTB 613 M; CUMIU 554 M; JTRSY 345 M | RWA.xyz | 16-oct-2026 | página; los % son variación de 30 d |
| Deuda pública no estadounidense: EUTBL 640 M$; NRW1 112 M$; CAMMF 92 M$; UKTBL 15,5 M$ | RWA.xyz | 16-oct-2026 | página |
| Crédito: syrupUSDC 1,1 mil M$; BMN2 946 M$; PRIME 593 M$; JAAA 586 M$ | RWA.xyz | 16-oct-2026 | página |
| Acciones: SECZ 293,5 M$ (−17,95 %); CRCLB 163 M$; SPCXB 138 M$; STRCx 137 M$; MSTRB 103 M$; QQQB 91 M$ | RWA.xyz | 16-oct-2026 | página |
| Materias primas: XAUT 3,0 mil M$; PAXG 1,8 mil M$ | RWA.xyz | 16-oct-2026 | página |
| Ranking por red (valor distribuido): Ethereum 16,9 mil M$ (3.042 activos); BNB Chain 6,1; Solana 4,4; **Stellar 3,5 (60 activos)**; Avalanche 1,7; Liquid 1,6; Arbitrum 957,7 M; ZKsync Era 948,7 M; Polygon 508,8 M; **XRP Ledger 496,6 M$ (24 activos)** | RWA.xyz (detalle bloqueado: "Login to Unlock") | 16-oct-2026 | página |
| BUIDL: 2,17 mil M$ (mes anterior 2,68 mil M$) | DefiLlama `stablecoins.llama.fi` | 17-oct-2026 | API |
| Categoría "RWA" de DefiLlama: 184 protocolos, TVL conjunto ≈ 4,05 mil M$ (top: Ethena USDtb 476 M$, Re 441 M$, Huma 407 M$, Anemoy 333 M$, OnRe 293 M$). **No incluye** BUIDL ni Franklin: otra definición | DefiLlama `api.llama.fi/protocols` | 17-oct-2026 | API |
| Stablecoins totales: RWA.xyz 291,8 mil M$ frente a DefiLlama ~306 mil M$ (ver R25) | ambas | 16/17-oct-2026 | diferencia de metodología |
| SEC–DTC: el 11-dic-2025 el personal (staff) de la división Trading and Markets de la SEC concede no-acción para el *piloto* ("Preliminary Base Version") de DTCC Tokenization Services: derechos tokenizados en DLT, con "Registered Wallets" en blockchains aprobadas y reconversión (de-tokenización) | sec.gov (PDF `dtc-nal-121125.pdf`, 1.952 líneas con pdftotext) | 11-dic-2025 | **LEÍDO** (cuerpo y condiciones); inglés |
| Activos elegibles del piloto: (i) valores del Russell 1000; (ii) bonos/bills/notes del Tesoro de EE. UU.; (iii) ETF que repliquen índices principales (S&P 500, Nasdaq-100) | idem | 11-dic-2025 | LEÍDO |
| La carta "se retira sin más acción a los **tres años** del lanzamiento" del piloto; DTC debe avisar por escrito del lanzamiento | idem | 11-dic-2025 | LEÍDO |
| SEC (17-sep-2026; FR 22-sep, 2026-19388): exención temporal y condicionada para "Tokenized Securities Venues" (negociación con AMM/pools de liquidez *con permisos*) respecto de la definición de "exchange", y para ciertos proveedores de liquidez respecto de "dealer"; **caduca a los 5 años** de su publicación; incluye solicitud de comentarios | Federal Register / sec.gov | 22-sep-2026 | **LEÍDO** (143 KB, partes introductoria, duración y condiciones); inglés |
| Definición SEC de "Tokenized NMS Stock": o bien tokenizada por/en nombre del emisor, o por un tercero no afiliado; **excluye** las cripto-activos que den exposición sintética (swaps, "linked securities") | idem | 22-sep-2026 | LEÍDO |
| SEC (28-ene-2026), Declaración conjunta de las divisiones de Corp Fin, IM y T&M: distingue tokenización *patrocinada por el emisor* y *por un tercero*; el formato (en cadena o no) no cambia la aplicación de las leyes de valores; un token de tercero puede no dar los derechos del valor subyacente | sec.gov | 28-ene-2026 | LEÍDO (extractos clave de la página) |

## Qué está sin verificar o es opinión
- **Titulares de crecimiento**: "mercado RWA de 30/40/370 mil M$" mezcla distribuido y representado y a veces incluye stablecoins. Una guía secundaria dice que los T-bills tokenizados superaron 7 mil M$ en 1T-2026 y otra cita 2,3 mil M$ "a mediados de 2026" citando RWA.xyz: las dos no cuadran con la tabla de hoy (suma de las diez primeras ≈ 13 mil M$) → ignorar [secundaria, VERIFICAR].
- **Contradicciones de ranking**: una fuente dice que BUIDL superó a BENJI y a USYC; otra que BENJI es mayor; la tabla de RWA.xyz de hoy pone USYC > USDY > BUIDL > iBENJI. Quedarse con la fecha de la tabla, no con la narrativa.
- **WisdomTree WTGXX −13,56 % en 30 d** y **SECZ −17,95 %**: no he encontrado causa ni dato de flujos (reembolsos, venta, cambio de contabilización) [VERIFICAR]; no inferir pánico.
- **BlackRock**: "dos fondos tokenizados nuevos" y "BUIDL 2,3 mil M$" aparecen solo en un medio (DEXTools) → [VERIFICAR] en sec.gov/EDGAR.
- **Franklin Templeton BENJI ≈ 828 M$ (1T-2026, 8 cadenas)**: un blog; la tabla actual da BENJI 680 M$ + iBENJI 1,7 mil M$, que son clases/representaciones distintas [VERIFICAR].
- **DTC**: la prensa (The Block, Yahoo/CoinDesk) dice que el servicio empieza en 2S-2026; no he leído un aviso de DTC de lanzamiento efectivo [VERIFICAR]. La no-acción es de personal, no una aprobación de la Comisión ni un cambio de ley.
- **Quién informa (parte interesada frente a tercero)**:
  - RWA.xyz: tercero comercial (vende API empresarial y registro de emisores); tabla agregada, sin auditoría; el detalle por red/gestor está de pago.
  - DefiLlama: tercero abierto; metodología distinta (TVL de protocolo).
  - Gestoras (BlackRock/Securitize, Franklin, WisdomTree, Ondo, Circle): partes interesadas; no leí sus páginas en esta pasada.
  - SEC/DTC: primario regulatorio, pero describe qué *se permite*, no cuánto se usa.
- **Representado 371 mil M$**: son activos registrados (p. ej. deuda, crédito privado, fondos) cuyo token no circula libremente; no equivale a "dinero en cadena".

## Caso alcista / caso bajista (sin pronóstico)
- **Alcista**: marcos reales y primarios (DTC con Russell 1000, Tesoro y ETF; exención SEC con AMM; declaración SEC de enero); 5,3 M de titulares (+16,6 % en 30 d); productos de crédito y acciones tokenizadas lanzándose a diario (lista de altas del 14-15-oct en RWA.xyz); Stellar y XRPL entre las 10 primeras redes.
- **Bajista**: el valor *distribuido* es ~10 % del "representado" y una fracción del de stablecoins; los fondos monetarios más grandes se mueven poco en 30 d (BUIDL −1,4 %, WTGXX −13,6 %, BENJI −4 %); el ranking por red depende de unos pocos activos; las exenciones son temporales (3 y 5 años) y condicionadas; detalles por red/gestor ocultos tras registro; cifras de la propia industria.

## Qué cambia para los digital assets (XRP, XLM, stablecoins, CBDC, tokenización)
- **Stellar** aparece 4.º por valor RWA (3,5 mil M$, 60 activos) y **XRPL** 10.º (0,497 mil M$, 24 activos) en RWA.xyz. Hecho: son posiciones en un ranking de un tercero. No sé qué activos las componen (detalle bloqueado) [VERIFICAR]; es una cifra de actividad en la red, no un efecto medido en el precio de XLM o XRP.
- La relación con la lista anterior (R25): el total "distribuido" tiene mucha mezcla con dólares digitales en forma de fondos monetarios; los emisores de stablecoin (Circle, Ripple) y de fondos compiten por el mismo colateral (T-bills).
- **DTC/SEC**: si el piloto de DTC se lanza, la liquidez de valores estadounidenses tokenizados dependería de blockchains *aprobadas por DTC*; la carta no nombra cadenas concretas en lo que he leído → XRPL/Stellar solo si DTC las aprueba [ESPECULACIÓN].
- **Tokenización de acciones por terceros** (xStocks, bStocks, Robinhood tokens) está definida por la SEC como tokenización de tercero: puede no dar derechos de accionista (declaración del 28-ene).

## Fechas próximas (catalizadores) con fuente
| Fecha | Evento | Fuente |
|---|---|---|
| 2S-2026 (previsto) | Lanzamiento del piloto de DTCC Tokenization Services; desde el lanzamiento corre el plazo de 3 años | carta SEC–DTC (11-dic-2025) + prensa [VERIFICAR el lanzamiento] |
| Abierto | Comentarios a la exención SEC para TSV (se publicó 22-sep-2026; el plazo concreto no lo localicé: la API del Federal Register da `comments_close_on` nulo) | FR 2026-19388 |
| ~14-nov-2026 | 13F de 3T (para ETF y empresas ligadas a tokenización) | calendario SEC (R21) |
| 19-oct-2026 | Cierre de comentarios GENIUS (stablecoins que mueven la liquidez del colateral) | R25 |
| Continuo | Altas diarias de activos en RWA.xyz; seguimiento de WTGXX, BUIDL, USYC | RWA.xyz |

## Qué falta por buscar
1. Páginas oficiales de BlackRock (BUIDL), Franklin (BENJI), WisdomTree (WTGXX) y Securitize: cifras y fechas de primario. Las páginas de gestoras no se abrieron en esta pasada.
2. Qué compone los 3,5 mil M$ de Stellar y los 497 M$ de XRPL (RWA.xyz detalle de pago): alternativa, `stellar.expert`/`xrpscan` o DefiLlama chain breakdown.
3. Aviso de lanzamiento de DTC y lista de blockchains aprobadas.
4. Causa del −13,6 % de WTGXX y del −18 % de SECZ.
5. Plazo de comentarios de la orden SEC de TSV (página sec.gov/comments/4-927).
6. Fuera de EE. UU.: Project Guardian (MAS), HKMA Ensemble, SIX Digital Exchange, Banco de Francia: cifras primarias (parcialmente en R04P, R07P).
