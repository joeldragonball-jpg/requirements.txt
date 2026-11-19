---
tema: Cotejo literal en Chrome — notas DTCC (27-may, 28-oct, 12-nov), ficha At-a-Glance, informe Bitwise sobre Solana 2031 y fuente primaria de Jupiter
fecha: 2026-11-19
etiquetas: [dtcc, stellar, solana, bitwise, jupiter, cotejo]
---
# Cotejo en Chrome (19-nov-2026)

Informativo; no es recomendación. Método: texto de la propia página (DOM) leído en Chrome, y los PDF descargados y extraídos entero (primaria, sin lector que resume). Niveles: P = primaria leída literal; S = solo medios; R = razonado. Las citas están en inglés tal como figuran.

## 1. DTCC (parte interesada: habla de sí misma)
| Documento | Cita literal | Nivel |
|---|---|---|
| Nota 27-may-2026 (DTCC y Stellar Development Foundation) | Subtítulo: «Firms anticipate DTC-tokenized assets available on the Stellar network during the 1H27». Cuerpo: «DTCC and SDF expect DTC-tokenized assets to be available on the Stellar network in the first half of 2027.» Sin mención de XRP/Ripple | P |
| Nota 28-oct-2026 (lanzamiento) | «The service is currently integrated with the Canton Network and DTCC’s private Besu network, with additional blockchain networks to be added in 2027.» «To date, 20 DTC Participants (clients) have signed agreements to access DTS including Alpaca, Apex Clearing Corporation, Barclays, Bank of America, BNP Paribas, ...». Sin XRP/Ripple/Stellar/Arc en el cuerpo (Solana solo como enlace lateral a la nota de 12-nov) | P |
| Nota 12-nov-2026 (Solana) | «DTC-tokenized assets expected to be available on Solana in the second half of 2027.» «...enable the tokenization of eligible The Depository Trust Company (DTC)-custodied assets on Solana»; «planned for the second half of 2027». Sin XRP/Ripple/Stellar | P |
| Ficha «Scope at Launch and What’s Next» (PDF) | «25 securities available to tokenize at launch»; en 2027 «Stellar (SEP-41)» y «Arc (Circle) (ERC-20)»; «The roadmap is indicative and subject to change.» Metadatos del PDF: creado 16-oct-2026 (InDesign); cabecera del servidor: Last-Modified 18-nov-2026 | P |
| Página de producto dtcc.com/products-and-services/digital-assets/tokenization | Contador «34 securities available to tokenize at launch» | P |

**25 frente a 34, resuelto a medias.** Ambas cifras están literalmente en DTCC. La ficha se creó el 16-oct (antes del lanzamiento del 28-oct) y la página de producto es la versión viva: lo más compatible es que 34 sea posterior [R]; DTCC no lo explica ni fecha. Barclays figura entre los 20 firmantes (cotejado).

XRPL/XRP/Ripple: sin ninguna mención en 27-may, 28-oct y 12-nov (búsqueda por texto en la página). Las notas de 17-dic, 4-may y 15-jul siguen leídas solo con lector que resume.

## 2. Bitwise: informe sobre Solana (PDF leído entero, 25 páginas)
«Tokenization, 24/7 Trading, and the Economics of Solana», Bitwise Asset Management, nov-2026; PDF creado 13-nov-2026. URL: https://s3.us-east-1.amazonaws.com/static.bitwiseinvestments.com/Research/bitwise-tokenization-247-trading-and-the-economics-of-solana-2026.pdf (enlazado desde la página bitwiseinvestments.com/crypto-market-insights/tokenization-247-trading-and-the-economics-of-solana) [P].

| | Bajista | Base | Alcista |
|---|---|---|---|
| Precio 2031 | 80 $ | 385 $ | 1.100 $ |
| Valor de red 2031 | 56 mil M$ | 270 mil M$ | 770 mil M$ |
| REV 2031 («real economic value») | 2,80 mil M$ | 6,75 mil M$ | 12,83 mil M$ |
| Valor presente (descuento 20 % anual, 5 años) | 32 $ | 155 $ | 442 $ |
| Acciones globales tokenizadas (por volumen) | 3 % | 4 % | 5 % |
| Cuota de Solana en acciones tokenizadas | 30 % | 50 % | 65 % |
| Rotación tokenizadas vs. tradicionales | 2x | 2,5x | 3x |
| Crecimiento anual de trading cripto y otros | 20 % | 30 % | 50 % |
| Pagos 2031 vs. hoy | 5x | 10x | 15x |
| Comisiones de trading 2031 vs. hoy | 1,00x | 0,975x | 0,945x |
| Múltiplo sobre REV | 20x | 40x | 60x |
| Suministro SOL 2031 | 700 M | 700 M | 700 M |
| Transacciones totales 2031 | 307,6 mil M | 673,7 mil M | 1.318 mil M |

**Comisiones (de red, no de ETF).** Media por transacción de acciones tokenizadas 0,0133 $; trading cripto 0,0063 $; mediana 0,00057 $ (constante hasta 2031). Hoy (3T-2026): 14,2 mil M de transacciones sin votos (56,8 mil M anualizadas), comisión media 0,0049 $, ingresos anualizados de red 278 M$, acciones tokenizadas con 33,5 mil M$ de volumen anual y 12,6 M$ de comisiones (tasa de captación 3,8 pb). El caso base exige ~21.000 tx/s de media y ~2,5 veces el límite de cómputo por bloque actual (5 veces en el alcista).

**Aviso del propio informe:** «There is no guarantee these forecasts or predictions will prove to be correct». Admite que Solana cotiza hoy a ~230x ingresos frente a su base de 40x, y que usa un descuento del 20 % por riesgo. Sección «Risks»: regulación, caídas de red, adopción, competencia (Ethereum y L2 concentran el valor tokenizado), captura de comisiones, escalado, descentralización, seguridad, riesgo de modelo.

**Sesgo.** Bitwise emite el ETF de Solana (BSOL) y gana comisión sobre el patrimonio; el informe es de la propia gestora. Los supuestos son suyos (la «cuota 65 %» y «60x» del vídeo son los del escenario alcista, no el central). Resuelve el [VERIFICAR] de C344: bull/bear, 65 %, 60x y 700 M SOL. Las comisiones de los ETF (BSOL, XRP ETF) NO están en este informe: siguen pendientes de prospecto.

## 3. Jupiter: fuente primaria
- **Localizado [P]:** cuenta oficial @JupiterExchange en X, 16-nov-2026 (https://x.com/JupiterExchange/status/2122367569495564567): «BREAKING: A NYSE-listed company is bringing its own shares directly to Jupiter Lend. Today at Breakpoint, we announced our partnership with @Bullish to launch a dedicated, permissioned $BLSH market. For the first time, Issuer Tokens can be used as collateral inside Solana’s ...» y «Note: The market will launch with $BLSH, with more Issuer Tokens to follow. Not available in all jurisdictions.» Sin fecha de apertura. @kashdhanda lo reposteó con comentario («Bullish has been a long-term supporter of Solana and Jupiter...»). La cuenta de @solana (16-nov) cita el «post-tokenization stack: Global Passport..., Liquidity Services..., stock lending market» [lectura parcial del extracto de búsqueda].
- **No localizado:** ninguna publicación escrita oficial (blog developers.jup.ag, X de Jupiter o de Dhanda, búsqueda de «460», «39.5», «3.4B», «finish line») con las cifras de 460.000 M$, 39.500 M$ y 3.400 M$ de DeFi; el panel Barclays/DTCC solo consta en Decrypt. La charla de Dhanda es un vídeo de Breakpoint (un repost del 18-nov enlaza una presentación de 8:31; no leída). Esas cifras siguen [S].
- Nota: la página de OneBullEx (secundaria) titula «Kash Dhanda raises tokenization utility estimate 25% to $5 billion», cifra distinta de las de Decrypt; no se usa y queda como [VERIFICAR] (no es primaria).
- Los blogs técnicos de Jupiter (developers.jup.ag/blog, hasta 8-jul-2026) no tratan este anuncio.

## Cambios en datos (solo notas y fuentes; sin borrar)
- `explorador/cadenas.json` → `dtcc_ruta`: nota general, cartas del marco (28-oct, ficha con fecha 2026-10-16 y 25/34), celdas Stellar (también en la tabla de calendario), Solana y XRPL con la cita literal. Los niveles ya eran P en esas celdas; se mantienen.
- `explorador/voces.json`: v212 (PDF Bitwise leído, cifras), v213 (Barclays literal), v214 (notas literales; 25/34), v216 (post oficial de Jupiter para BLSH; nivel sigue S porque las cifras del COO y el panel no se hallaron).

## Sigue sin leerse
- Charla de Dhanda en Breakpoint y panel Barclays/DTCC (vídeo): sin transcripción oficial.
- Origen de 460.000 M$, 39.500 M$ y 3.400 M$ de Jupiter.
- Notas DTCC de 17-dic-2025, 4-may y 15-jul-2026 (solo lector que resume); carta SEC HTML (404; PDF leído).
- Comisiones de los ETF BSOL y XRP de Bitwise (prospecto).
- Por qué la ficha dice 25 y la web 34; Arc por semestre.
