# Stellar a fondo (2026-10-17, R33 profundo)

Etiquetas: **LEDGER** = leído hoy en Horizon (horizon.stellar.org) · **PRIM-SDF** = Stellar Development Foundation (parte interesada: promueve la red) · **PRIM-LEÍDA** = código/documentación oficial leída · **TERCERO** = DefiLlama, RWA.xyz, Nansen, Dune · Sin recomendaciones de compra/venta.

## Resumen (5 líneas)
1. Hecho (LEDGER): la red está en **protocolo 29** desde el 1-oct-2026 17:00 UTC (ledger 64.717.645); el 28 entró el 16-sep 17:00 UTC (ledger 64.458.446). El P29 es "un lanzamiento centrado en seguridad que corrige vulnerabilidades en Stellar Core, sin CAPs nuevos" (developers.stellar.org); no he encontrado el detalle de las vulnerabilidades [VERIFICAR].
2. Hecho: `stellar-core` v30.0.0 se publicó el 16-oct (CAP-84 direcciones de contrato multiplexadas, CAP-87 funciones de verificación ML-DSA = firmas poscuánticas, CAP-88 cierre de ledger en milisegundos). La fecha de voto del P30 **no consta** en ninguna fuente que abra [VERIFICAR].
3. Cifras de suministro (SDF, parte interesada): suministro total 50.001.786.837 XLM, circulante 35.201.682.319, "mandato SDF" 14.530.351.090 (SDF mantiene ~29 % del total), quemados 55.442.115.250 (el ledger sigue contando 105.443.902.087 XLM en `total_coins` porque lo quemado se envió a una cuenta sin clave).
4. RWA y stablecoins: cada fuente da un tamaño distinto (SDF/Dune 4.000 M$ en sep; RWA.xyz 3.550 M$ "distribuido" hoy; Nansen "más de 3.000 M$" en el 2T). Stablecoins: 516 M$ + 22,6 M€ en DefiLlama (puesto 21 de 209 cadenas) frente a 556,7 M$ en RWA.xyz. Son métricas distintas, no una contradicción probada.
5. Lo no cuadrado: SDF dice "una gran actualización por trimestre" y el ledger muestra 4 protocolos en 5 meses (P26 6-may, P27 8-jul, P28 16-sep, P29 1-oct). Hay además un dato interno de SDF que no cuadra (ver "Discrepancias").

## Qué es hecho verificado
| Dato | Fuente | Fecha | Etiqueta |
|---|---|---|---|
| Horizon 29.0.0 con stellar-core 30.0.0; protocolo actual 29 (soportado 29); último ledger 64.993.811 cerrado el 17-oct 16:33:57 UTC | horizon.stellar.org | 17-oct-2026 | LEDGER |
| Comisión base 100 stroops (0,00001 XLM); reserva base 5.000.000 stroops (0,5 XLM); uso de capacidad del ledger 0,7; ledger de ejemplo: 197 transacciones OK, 61 fallidas, 371 operaciones | horizon.stellar.org `ledgers`, `fee_stats` | 17-oct-2026 | LEDGER (un solo ledger: no es media) |
| Primer ledger en P29: 64.717.645 (1-oct 17:00:07 UTC); en P28: 64.458.446 (16-sep 17:00:06 UTC) (búsqueda por bisección de `protocol_version`) | horizon.stellar.org `ledgers/<n>` | 17-oct-2026 | LEDGER |
| Tabla oficial: P29 mainnet 1-oct (testnet 29-sep), "Security-focused release… introduces no new CAPs"; P28 "Adapter" 16-sep (CAP-83, 85, 86); P27 "Zipper" 8-jul (CAP-71); P26 "Yardstick" 6-may (CAP-73, 77, 78, 79, 80, 82) | developers.stellar.org/docs/networks/software-versions | leído hoy | PRIM-LEÍDA |
| `stellar-core` v29.0.0 (5-oct; versión "-internal" ya el 1-oct, el día de la activación); cambios: precisión del cruce de ofertas del DEX, descartar mensajes sobredimensionados antes, tamaño máximo de mensaje menor, cola de salida | github.com/stellar/stellar-core/releases | leído hoy | PRIM-LEÍDA (notas escuetas) |
| `stellar-core` v30.0.0 (16-oct): protocolo 30 con CAP-84, CAP-87 (ML-DSA), CAP-88 (cierre en ms) | github.com/stellar/stellar-core/releases | 16-oct-2026 | PRIM-LEÍDA |
| P28 "Adapter": guía de actualización con voto testnet 27-ago y mainnet 16-sep 17:00 UTC (inconsistencia interna: otra frase dice 9-sep) | stellar.org/blog/developers/adapter-protocol-28-upgrade-guide | leído hoy | PRIM-SDF; la fecha real la confirma el ledger: 16-sep |
| CAP-77 "Quorum Freeze" (P26): permite congelar entradas del ledger por consenso en emergencias; según Nicolas Barry (SDF), los validadores ya lo hicieron dos veces: tras un bug de protocolo (oct-2025) y un exploit DeFi (feb-2026); "no es una respuesta completa" | stellar.org/blog (ensayo de Barry, 5-may-2026) | 5-may-2026 | PRIM-SDF, parte interesada; el texto no da fecha |
| Panel de lumens (SDF): suministro original 100.000 M; inflación 5.443.902.087; quemados 55.442.115.250; suministro total 50.001.786.837; reserva de actualización 258.885.848; fee pool 10.867.581; mandato SDF 14.530.351.090; circulante 35.201.682.319 | dashboard.stellar.org/api/v2/lumens | 17-oct-2026 16:34 UTC | PRIM-SDF (cálculo del propio SDF; no auditado por mí) |
| `total_coins` del ledger 105.443.902.087,35 XLM; fee_pool 10.867.580,66 (coincide con el panel de SDF) | horizon.stellar.org | 17-oct-2026 | LEDGER |
| Cuenta nula GAAAA…WHF con saldo de 98.911,78 XLM (no es el total quemado, que SDF contabiliza en 55.442 M; la mecánica exacta de la quema **no la he verificado**) | horizon.stellar.org `accounts` | 17-oct-2026 | LEDGER; [VERIFICAR] mecánica |
| Stablecoins en Stellar: 516.108.138 $ (pegged USD) + 22.589.410 € (pegged EUR); puesto 21 de 209 cadenas por circulante en USD (Ethereum 143.946 M, Tron 94.436 M, Solana 15.564 M) | stablecoins.llama.fi/stablecoinchains | 17-oct-2026 | TERCERO |
| TVL DeFi de Stellar 235.915.845 $ (`/v2/chains`); Blend Pools V2 135,4 M$ (préstamos); la "TVL de Binance en Stellar" 348 M$ es saldo de custodia en un CEX, no uso DeFi | api.llama.fi | 17-oct-2026 | TERCERO |
| RWA.xyz: valor distribuido 3,55 mil M$ (+7,88 % en 30 d), valor "representado" 78,09 M$, 23.906 titulares, 83 RWA; stablecoins 556,74 M$ (+49,71 % en 30 d), 738.580 titulares; top: Spiko 1,9 mil M$, Ondo 537,6 M$, Franklin Templeton (Benji) 501,3 M$, Realiz 500 M$, Circle 498,7 M$ | app.rwa.xyz/networks/stellar | 17-oct-2026 | TERCERO (RWA.xyz no define "distribuido/representado" en la página) |
| SDF: "4.000 M$ en activos reales tokenizados, +360 % este año" (enlaza un panel Dune sin autor ni metodología; la entrada no tiene fecha visible) | stellar.org/blog/developers (14-sep-2026) | 14-sep-2026 | PRIM-SDF citando Dune; interesada |
| SDF Q1-2026 (7-may): 22.500 M operaciones acumuladas; 10,6 M direcciones únicas; RWA > 2.000 M$ (frente a 785 M$ a fin de 2025); volumen de pagos con stablecoins 5.500 M$ en el 1T (+72 % interanual); comisión media ~0,01 céntimo; uptime 99,99 % | stellar.org/blog/foundation-news (Mel Higgins) | 7-may-2026 | PRIM-SDF, sin auditar |
| SDF Q2-2026 (3-ago): RWA 3.000 M$ en jun (1.000 M en ene, 2.000 M en abr); volumen de transferencias de stablecoins 11.400 M$ (récord, +72 % trimestral); velocidad ~33x; 10,7 M cuentas; 2.968 desarrolladores activos al 30-jun (Electric Capital, tercero); Community Fund rondas 42-43: 5,5 M$ a 55 empresas; 0 incidentes de seguridad del protocolo en el trimestre | stellar.org/blog/foundation-news | 3-ago-2026 | PRIM-SDF, sin auditar |
| Nansen (tercero) 2T-2026: ~63.000 direcciones activas diarias de media (rango 44.000-113.000), ~4,9 M transacciones diarias (2,6-7,1 M); RWA "más de 3.000 M$"; Circle CCTP en Stellar desde el 19-may; no declara conflictos y se apoya en material de SDF; sin metodología de las cifras | nansen.ai/post/stellar-q2-2026-report | 5-ago-2026 (la ficha dice 1-oct) | TERCERO, con conflicto potencial |
| Otras entradas del blog SDF: Circle CCTP en vivo (19-may), USDT0 en Stellar (2-sep), "Stellar Private Payments" vista previa para desarrolladores (24-ago), "Confidential Tokens" vista previa (29-jun), Plan de Preparación Cuántica (9-jun) | stellar.org/blog (listados) | 2026 | PRIM-SDF (solo títulos y fechas; no leídas) |

## Lo que sale de cruzar los datos [cálculo mío]
- XLM en poder del "mandato SDF" / suministro total = 14.530/50.002 = 29,06 %. El circulante es el 70,4 % del total (35.202/50.002). El 29 % restante en manos de SDF es **mucho** más de lo que mueve un gran emisor privado, y su calendario de uso no lo he leído (el panel no explica el criterio del "mandato").
- Volumen de stablecoins 2T = 11.400 M$ frente a 516 M$ de suministro en DefiLlama → rotación ~22x en el trimestre: coherente en orden de magnitud con el "~33x" de SDF (cuya definición de suministro no declaran), pero la rotación no es dinero fijado ni mide uso real [ESPECULACIÓN sobre qué parte es trading/arbitraje].
- RWA.xyz muestra "volumen de transferencia a 30 d" de stablecoins 11,36 mil M$; SDF cita 11,4 mil M$ para todo el 2T. Son casi el mismo número en períodos distintos (30 días frente a 3 meses): si ambos son correctos, el volumen mensual casi triplicó la media trimestral; si no, uno de los dos está medido distinto [VERIFICAR].
- SDF: 1T 5.500 M$ → 2T 11.400 M$ = +107 % trimestral, no el "+72 %" que se cita para ambos trimestres; el "+72 %" del 1T era interanual: la etiqueta del 2T ("+72 % trimestral") **no cuadra** con sus propias cifras [VERIFICAR el texto original].

## Qué está sin verificar o es opinión
- Las "vulnerabilidades" del P29: el documento oficial no da CVE ni detalle; el comunicado de SDF no aparece en el blog de desarrolladores; ninguna fuente independiente [VERIFICAR; ¿activado con una versión "internal" privada el mismo día?].
- Fecha del voto del P30 y si habrá voto completo de la red [VERIFICAR].
- "Una gran actualización por trimestre" (SDF, Q2) frente a 4 protocolos entre 6-may y 1-oct: no es contradicción si el P29 es un parche, pero la hoja de ruta pública no cubre eso.
- "99,99 % de uptime", "0 incidentes de seguridad del protocolo" en el 2T: SDF, sin metodología. Y el propio SDF habla de un exploit DeFi (feb-2026) y un bug de protocolo (oct-2025) que obligaron a usar el congelamiento por quórum.
- Comparaciones con otras cadenas ("cuatro veces más rápido que el mercado", ~50 % mercado vs Stellar) vienen de SDF; el mercado general no está definido.
- Spiko "~520 M$ → ~970 M$": SDF dice que "la mayor parte" del crecimiento fue en Stellar; RWA.xyz muestra 1,9 mil M$ en Stellar para Spiko hoy (vs ~1 mil M$ de SDF en el 2T): las fechas difieren [VERIFICAR].

## Caso alcista / caso bajista (sobre la red, no sobre el precio)
**Alcista:** ritmo de ingeniería muy alto (P26-P30 en 6 meses); RWA y stablecoins creciendo en tres fuentes distintas aunque con cifras diferentes (SDF, RWA.xyz, Nansen); socios de peso (Circle CCTP en vivo, Franklin Templeton Benji, Ondo, WisdomTree, USDT0, MoneyGram); herramientas de respuesta a incidentes por consenso (CAP-77); ya se prepara la criptografía poscuántica (CAP-87).
**Bajista:** la métrica de RWA depende de pocos emisores (Spiko, Ondo, Franklin, Realiz, Circle suman ~4,0 mil M$ de los 3,55 mil M$ "distribuidos" según la tabla de RWA.xyz: la tabla no aclara si usa la vista "distribuido" o "representado", así que no se puede sumar) [VERIFICAR]; SDF controla ~29 % del suministro total y 4 protocolos en 5 meses aumentan riesgo operativo (un parche "de seguridad" activado el mismo día en que salió la versión interna); TVL DeFi pequeña (236 M$) y 516 M$ en stablecoins frente a 144.000 M$ en Ethereum; el cuadro de uso (63.000 direcciones activas/día) es de un tercero sin metodología; el 61/258 de transacciones fallidas en el ledger de muestra es un solo dato, pero conviene vigilar la tasa de fallos [VERIFICAR con una serie].

## Qué cambia para los digital assets (XRP, XLM, stablecoins, CBDC, tokenización)
- XLM: la oferta circulante la fija SDF vía el "mandato"; no hay quema nueva en lo medido hoy (el fee_pool de 10,87 M XLM va a reciclarse en el ledger). Sin dato de precio aquí.
- Stablecoins: no comparo con XRPL en este informe (no medí su serie de stablecoins aquí; ver R25).
- Tokenización: SDF y RWA.xyz muestran más de 3.000 M$ en RWA en Stellar; el ranking por emisor (RWA.xyz) concentra el valor en 5 emisores.
- Privacidad: "Confidential Tokens" y "Private Payments" están en vista previa para desarrolladores (junio y agosto): no son producción.

## Fechas próximas (catalizadores) con fuente
| Fecha | Evento | Estado |
|---|---|---|
| sin fecha publicada | Voto de mainnet del protocolo 30 (CAP-84, 87, 88) tras v30.0.0 del 16-oct | [VERIFICAR]; fuente: GitHub stellar-core |
| 4T-2026 | Siguiente "gran actualización" (según SDF: una por trimestre) | [ESPECULACIÓN]; el panel de versiones no lista P30 |
| ~nov-2026 | Q3-2026 de SDF (los Q1 y Q2 salieron el 7-may y el 3-ago) | [ESPECULACIÓN] por patrón |
| 14-nov-2026 | 13F del 3T (ya en cola: no incluye XLM spot) | ver R21b |

## Discrepancias detectadas
- RWA: 2.000 M$ (SDF, abr) → 3.000 M$ (SDF, jun) → 4.000 M$ (SDF/Dune, sep) frente a 3.550 M$ distribuido (RWA.xyz, 17-oct). Con la métrica de Dune desconocida, no son comparables.
- SDF 2T: "+72 % trimestral" frente a 5.500 → 11.400 M$ (+107 %).
- Guía del P28: 16-sep (clave) frente a "9-sep" (en otra frase). El ledger dice 16-sep.
- Ficha de Nansen: publicada 5-ago, ficha "1-oct".
- "SDF mantiene ~29 %" sale del panel de SDF (cálculo mío); el panel llama a ese concepto "sdfMandate" sin explicar qué incluye [VERIFICAR].

## Qué falta por buscar
- Detalle técnico de las vulnerabilidades del P29 (lista stellar-dev / stellar-validators; sin acceso: Google Groups no cargó con WebFetch).
- Número y nombres de validadores Tier 1 y quién los controla (no hallado; SDF no da recuento).
- Informes financieros de SDF (tesorería, ventas de XLM, gasto): el blog muestra solo operaciones y métricas.
- Metodología del panel Dune de RWA y de la tabla de RWA.xyz; hoja de ruta de P30.
- La mecánica exacta de la quema de 55.442 M XLM (cuenta sin clave, comprobación en el ledger).
