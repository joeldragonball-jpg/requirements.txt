# BORRADOR: mantener el registro de predicciones y puntuar fuentes (2026-10-18)

> **Borrador, no aplicado.** No he modificado `informes/predicciones.md` ni el cerebro. No sube a GitHub hasta que Joel lo diga. Informativo; las predicciones son opiniones [ESPECULACIÓN], no hechos; sin recomendaciones de compra/venta. Base: `informes/predicciones.md` (47 filas), G17 §3 (errores documentados), `cerebro/documentos/fuentes-fiables-y-dudosas.md` y la escala A/B/C/D de R15. Los recuentos son **míos** (hechos con script sobre el archivo).

## 1. Estado del registro hoy (recuento 18-oct-2026)
- **47 predicciones**: 41 «sin resolver», 6 con algún resultado o matiz.
- Con resultado o matiz: #1 «parece que falló» (Lummis, CLARITY; inferencia); #7 casi seguro acertó (aprobación antes del 3-nov; sin confirmar en el registro); #9 mal planteada (ya resuelta por otra vía); #10 pendiente de anotar; #20 contradicha por el ledger; #45 «parece que falló» (Alpenglow, inferencia mía).
- **Con tan pocas resueltas, no se puede puntuar a nadie con porcentajes.** Si se hiciera (p. ej. «Despeja La X acierta el 0 %»), sería una cifra sin sentido estadístico. Mínimo razonable para hablar de una tasa: ≥5-10 resueltas por fuente [ESPECULACIÓN, criterio mío].

## 2. Actualizaciones que ya se pueden anotar (propuesta; hay que revisarlas)
| # | Propuesta de anotación | Motivo / fuente | Estado |
|---|---|---|---|
| 10 | **ACERTÓ**: XRPN cotiza desde el lunes 12-oct | 8-K de la SEC (catalizadores 15-oct); la prensa llegó a decir 14-oct, el 8-K manda | Hecho. Matiz: el «−1,05 %» del debut no es de apertura a cierre [VERIFICAR] |
| 7 | Mantener «sin resolver» hasta el 3-nov | Casi seguro, pero la fecha límite no ha llegado | Esperar |
| 20 | Mantener «contradicho por el ledger» | CoinDesk citó un panel con otras cifras; el ledger (9-oct) mostraba la mayoría de `fixCleanup3_4_0` | Hecho (R32/R31) |
| 19 | Vence el **23-oct** | Activación si mantiene mayoría 14 días (margen de 1 voto) | Comprobar el 23-oct |
| 44 | Vence el **31-oct** | DTCC dijo que lanzaría su servicio en octubre (Canton) | Comprobar en dtcc.com |
| 31 | Vence el **1-nov** | OPEP+: reunión del 1-nov | Comprobar el comunicado |
| 23 | Vence el **1-nov** | Escrow de Ripple: 1.000 M XRP | Ledger |
| 25 | Vence el **3-nov** | Trump: «no atacaremos Irán antes de las elecciones» | Prensa y Pentágono |

## 3. Candidatas a añadir como predicciones nuevas (de R40 a R46)
Solo se anotan cosas **dichas por alguien con fecha** (no mi opinión). Formato igual que el registro. Marcar [VERIFICAR] antes de añadir.
| Quién | Predicción (resumen) | Fecha límite | Cómo se comprueba | Informe |
|---|---|---|---|---|
| Ripple (nota 20-abr-2026) | Plan post-cuántico en 4 fases, «full readiness» no más tarde de 2028 | 2028-12-31 | Enmiendas XRPL con criptografía post-cuántica (hoy 0 de 107) | R45 |
| Stellar (SDF, plan cuántico) | ML-DSA en Soroban en 2026; CAP de Stellar en 2027 | 2026-12-31 / 2027-12-31 | Protocolo y SDF | R45 |
| NIST (borrador IR 8547) | ECDSA/EdDSA/RSA «deprecated tras 2030» y «disallowed tras 2035» (borrador, sin versión final) | 2035-12-31 | NIST: ¿versión final? | R45 |
| JPMorgan (prensa) | JPMD en Canton «en fases durante 2026», sin fechas | 2026-12-31 | Comunicado de JPMorgan | R44 |
| BNY–Galaxy | Staking «subject to regulatory review», sin fecha | 2027-06-30 | Comunicados | R44 |
| Banco de Inglaterra y Tesoro | Decisión sobre la libra digital «later this year» | 2026-12-31 | bankofengland.co.uk | R40 |
| EIA (STEO 6-oct) | Brent 105 $ en 4T26 (**escenario**, no dato). Ya está como #17 | 2026-12-31 | EIA spot | R46 (ya anotada) |
| Rusia (Banco Central) | Rublo digital obligatorio para ciertos bancos desde 1-sep-2026 (fase 2: 1-sep-2027) | 2027-09-01 | cbr.ru | R40 |

## 4. Cómo puntuar una fuente (método propuesto)
Dos cosas distintas, que **no deben mezclarse**:
1. **Calidad de la fuente** (tipo A/B/C/D): se decide **antes** de leer el contenido, por quién es y qué gana (escala R15). Es lo que ya usa G17.
2. **Historial de predicciones** (esta sección): se calcula **después**, con predicciones resueltas.

### 4.1 Reglas para puntuar una predicción
- Solo cuenta una predicción **comprobable y con fecha límite** (si no tiene fecha, no se puntúa).
- Resultado: **1** = acertó · **0** = falló · **0,5** = parcial · **— (no cuenta)** = mal planteada, ambigua o sin dato.
- Si la fuente da una probabilidad (Polymarket «15-23 %»), puntuar con la **regla de Brier**: (probabilidad − resultado)². Cuanto menor, mejor. Se necesita un buen número de casos antes de sacar conclusiones.
- Predicciones de **cálculo propio** («podría activarse a partir del 23-oct») no puntúan a una fuente externa; son mías (#9, #19, #23, #40).
- Anotar siempre **quién lo dijo y en qué calidad** (CEO de una empresa con interés ≠ analista independiente).

### 4.2 Ficha de fuente (plantilla)
| Campo | Qué anotar |
|---|---|
| Fuente | Nombre y tipo (A primaria / B secundaria buena / C parte interesada o agregador / D no usar) |
| Interés propio | ¿Gana algo con lo que dice? (tenedor, emisor, afiliados) |
| Veces que la he usado | N |
| Errores documentados | Casos con enlace al informe (no impresiones) |
| Predicciones resueltas | n; aciertos / parciales / fallos |
| Tasa de acierto | **Solo si n ≥ 5**; si no, «sin datos suficientes» |
| Qué hacer con ella | Usar como pista y verificar / usar solo con segunda fuente / ignorar |
| Última revisión | Fecha |

### 4.3 Primeras fichas (con lo que consta; sin inventar cifras)
| Fuente | Tipo (R15) | Casos documentados (G17 §3 y cerebro) | Predicciones resueltas | Lectura |
|---|---|---|---|---|
| **Despeja La X** (YouTube, ES) | C | Útil por citas originales, pero «titulares prometen más que el contenido»; la fecha y la conclusión sobre XRP las pone el presentador; 4 vídeos = 1 sola fuente (15-oct); sesgo de tenedor y enlaces afiliados [VERIFICAR] | 0 de 4 anotadas resueltas (#4, #5, #8, y varias citas #2, #3) | Sin datos suficientes. Usar para encontrar la cita original, no como conclusión |
| **Ripple / Stellar (SDF)** (webs y notas) | C (parte interesada) | Primarias de lo que dice la empresa, no de cifras de impacto; en ripple.com/press-releases la fecha de la lista va desfasada una entrada (R34); «NIST 2029+» de la SDF no está en el borrador leído (R45) | Planes #14-#36 sin resolver | Útiles para saber qué anuncian; exigir segunda fuente para cifras |
| **CoinDesk** (panel XRPL) | B | #20: el panel citado daba 27/35 votos; el ledger contradijo la lectura (9-oct) | 1 contradicha | 1 caso: pista de que hay que mirar el ledger, no extrapolar |
| **Agregadores de precios** | C | «XRP -4,5 % a 1,29 $» frente al mínimo horario de 1,31 $ (apertura 17-oct) | — | Citar CoinGecko horario con ventana |
| **Prensa SEO / «XRP news today»** | D | Titulares reciclados de otros años; Crypto Briefing, KuCoin y mexc repetían a Bloomberg (eco) | — | No usar como fuente primaria |
| **21Shares** | C (emisor) | Solo ETP físicos; columnas mezcladas al extraer | — | Cifras de su producto, con matiz |
| **Primarias A (SEC, Fed, BLS, BoJ, BCE, EIA, ledgers, MAS)** | A | Errores del research venían del resumen, no de ellas | — | Prioridad; ojo con la fecha y el filtro de consulta |

## 5. Mantenimiento propuesto (sin IA, 10 minutos por semana)
1. **Domingos:** abrir `predicciones.md`, filtrar las que vencen en los próximos 14 días y comprobarlas (fuente en la columna «Cómo se comprueba»).
2. Anotar resultado y fecha; si es «mal planteada» o ambigua, decirlo (no borrar).
3. **Una vez al mes:** actualizar las fichas de §4.3 y mover al cerebro **solo** lecciones nuevas (máx. 5 líneas por archivo y sesión).
4. **Cada trimestre:** calcular la tasa solo para fuentes con n ≥ 5; no antes.
5. Registro de cada decisión que dependa de una predicción en el diario (privado/diario-de-decisiones.md).

## 6. Qué no sé
- Si #7 se confirmó formalmente (hace falta mirar el Congreso).
- La fecha exacta del dicho de Lummis (#1) y de otras filas marcadas [VERIFICAR].
- Cuántas predicciones resueltas necesito para una conclusión útil (mi umbral ≥5 es un criterio práctico, no una norma).
- Si las predicciones de mercados de predicción (Polymarket/Kalshi) pueden compararse con las de personas.
