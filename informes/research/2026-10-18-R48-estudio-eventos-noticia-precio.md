# R48 · Estudio de eventos noticia → precio (XRP, XLM, BTC)

> **Nota de revisión (18-oct, sesión de revisión):** el recuento «11 efecto directo probable» es más fuerte que la tabla. Tres de esos casos tienen confusores anotados en su propia fila (E17: cascada de liquidaciones y desajuste de la bolsa; E19: otras noticias de Stellar esa semana; E06: caída de −10 % en las 24 h previas) y cinco tienen hora no verificada (tipo B: E15, E17, E18, E19 y, en parte, E16), que la regla del §2 trata con más cautela. Léase como **«salen de lo normal»**, no como «causa demostrada». Además, las columnas de 1 h de los eventos tipo B se muestran pero no se usan para clasificar.

Fecha: 2026-10-18 · Sesión R48 (Sonnet 5.5, esfuerzo alto) · Sin recomendaciones de compra/venta.
Script: `scripts/estudio_eventos.py eventos` (sin IA, sin claves; reproducible). Etiquetas: [VERIFICAR] / [ESPECULACIÓN].

## 1. Resumen (6 líneas)
1. Se midieron **19 eventos** (14 con hora de calendario oficial = tipo A; 5 con hora aproximada o desconocida = tipo B) sobre **32 pares evento-activo** (XRP 18, XLM 14).
2. Resultado de la regla (fijada antes de mirar): **11 «efecto directo probable», 6 «dudoso», 15 «sin efecto detectable»**.
3. Lo que más movió el precio *relativo a BTC*: **sentencia Torres (2023)**, **DTCC–Stellar (XLM, 2026)**, el **arancel del 100 % a China (10-oct-2025)** y el **fracaso del cloture de CLARITY (15-sep-2026)**. Entre los datos macro, solo Jackson Hole 2025 y la subida de la Fed de sept-2026 salen de lo normal; **IPC, PPI, empleo y minutas, no**, y de los 5 FOMC solo 1 sale de lo normal (2 dudosos, 2 sin efecto).
4. **ETF y tesorería (XRPC, XRPN) y activaciones técnicas del XRPL: sin efecto detectable el día de la noticia** (consistente con «noticia descontada», [ESPECULACIÓN]).
5. **Muestra pequeña y sesgada** (eventos conocidos, elegidos a posteriori): sirve para ordenar hipótesis, no para predecir. Con 32 pruebas al 5 % se esperan 2-3 falsos positivos solo por azar.
6. «Salir de lo normal» no prueba causa: coincidencia en el tiempo ≠ causa (ver §6).

## 2. Método (lo que se hizo)
- **Precios:** velas de **1 minuto** de Binance spot (XRPUSDT, XLMUSDT, BTCUSDT) en los instantes t0−24 h, t0, t0+1 h, t0+24 h y t0+7 d (precio en t = cierre de la vela que termina en t). Fuente: API pública de mercado de Binance (`data-api.binance.vision`), **C (agregador/bolsa)**, no CoinGecko, porque CoinGecko gratuito solo da datos horarios de los últimos 90 días y aquí hay eventos desde 2023. **Cruce con CoinGecko** (90 días, 2.161 puntos horarios de XRP): diferencia mediana 0,06 %, máxima 0,59 %; en E09 y E06 la variación a 24 h difiere 0,07 y 0,18 puntos. USDT no es USD: otra base de error posible [VERIFICAR].
- **Efecto relativo:** exceso = rendimiento logarítmico del activo − β × rendimiento de BTC, con β horaria de toda la muestra (**XRP 1,08; XLM 1,05**; 2023-01-01 → 2026-10-17, 33.262 horas). La prueba de estrés usaba ≈1,25 en 12 meses: aquí la β de 3,8 años es menor; la conclusión no cambia con 1,25 salvo en los casos límite (E01, E04, E08).
- **Tasa base** (¿cómo de raro es?): proporción de ventanas solapadas de la serie horaria completa con |exceso| ≥ al del evento (la «cola»). Volatilidad anualizada en la muestra: XRP 79 %, XLM 85 %, BTC 46 %. |Exceso| típico: **1 h: mediana 0,24 % / p95 1,16 % / p99 2,41 % (XRP); 24 h: 1,20 % / 5,81 % / 11,85 %; 7 d: 3,57 % / 15,4 % / 42,3 %**. XLM, algo mayor (24 h: p95 6,17 %).
- **Regla de clasificación (fijada antes):** *directo probable* = cola ≤ 5 % en 1 h (solo si la hora es tipo A y sin otro hecho de calendario en ±3,5 h) o cola ≤ 5 % en 24 h sin confusores en 24 h; *dudoso* = cola ≤ 5 % con confusor, o cola entre 5 y 15 %; *sin efecto detectable* = resto. En eventos tipo B **no se usa la ventana de 1 h**.
- **Confusores automáticos:** fin de semana, día de decisión del FOMC en ±24 h (calendario FOMC 2023-2026 de la Fed; las fechas de 2023-2025 y 2026 distintas de sept/oct están escritas de memoria, [VERIFICAR] en federalreserve.gov), día 1 (escrow). Los demás, a mano en la tabla.

## 3. Tabla de eventos
Variación simple del precio; exceso = sobre BTC×β. «Cola» = fracción de ventanas normales con un movimiento igual o mayor (menor = más raro). Tipo A = hora de calendario oficial; B = hora aproximada.

| ID | Evento | UTC | Fuente primaria | Tipo | XRP 1h / 24h / 7d | XLM 1h / 24h / 7d | BTC 1h / 24h / 7d | Exceso XRP 1h / 24h (cola) | Exceso XLM 1h / 24h (cola) | Confusores | Clasificación XRP / XLM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E01 | FOMC mantiene tipos | 2025-03-19 18:00 | federalreserve.gov (calendario FOMC) | A | +0,9 / −2,6 / −4,1 % | +0,9 / −2,9 / −0,8 % | +1,6 / −0,2 / +2,8 % | −0,8 / −2,4 (0,09 / 0,23) | −0,8 / −2,7 (0,11 / 0,23) | Salto previo de +11,7 % en 24 h (ese día, la noticia del abandono del recurso de la SEC, sin hora verificada) [VERIFICAR] | dudoso / dudoso |
| E02 | Powell, Jackson Hole | 2025-08-22 14:00 | federalreserve.gov (discurso) | A | +5,8 / +6,2 / +0,3 % | +5,7 / +5,5 / −7,6 % | +3,0 / +2,1 / −3,0 % | +2,5 / +3,8 (0,009 / 0,12) | +2,5 / +3,2 (0,012 / 0,19) | ninguno | **directo / directo** |
| E03 | FOMC baja 25 pb | 2025-09-17 18:00 | federalreserve.gov (comunicado) | A | −0,7 / +2,9 / −2,5 % | −0,2 / +4,8 / −1,4 % | −0,2 / +1,8 / −1,5 % | −0,5 / +0,9 (0,24 / 0,59) | 0,0 / +2,9 (0,96 / 0,22) | ninguno | sin efecto / sin efecto |
| E04 | FOMC baja 25 pb y fin del QT | 2025-10-29 18:00 | federalreserve.gov (comunicado) | A | −1,9 / −7,8 / −14,0 % | −1,3 / −8,5 / −13,4 % | −1,0 / −3,9 / −7,1 % | −0,9 / −3,7 (0,09 / 0,12) | −0,3 / −4,5 (0,49 / 0,09) | Caída continuada tras el máximo de oct-2025 | dudoso / dudoso |
| E05 | FOMC | 2025-12-10 19:00 | federalreserve.gov (calendario FOMC) | A | 0,0 / −2,9 / −10,1 % | +0,8 / −4,4 / −16,8 % | +0,5 / −1,9 / −7,2 % | −0,5 / −0,8 (0,20 / 0,62) | +0,2 / −2,4 (0,57 / 0,27) | ninguno | sin efecto / sin efecto |
| E06 | FOMC **sube** 25 pb (3,75-4,00 %) | 2026-09-16 18:00 | federalreserve.gov (comunicado) | A | +1,3 / +3,1 / +19,1 % | +2,2 / +6,9 / +17,0 % | −0,2 / +1,2 / +11,3 % | +1,5 / +1,8 (0,03 / 0,35) | +2,4 / +5,6 (0,013 / 0,07) | Caída de −10 % en las 24 h previas | **directo / directo** |
| E07 | Empleo EE. UU. +29.000 (esp. ~89.000) | 2026-10-02 12:30 | bls.gov | A | −0,1 / −3,5 / −9,4 % | +0,4 / −4,3 / −13,4 % | 0,0 / −2,0 / −4,0 % | −0,1 / −1,3 (0,81 / 0,46) | +0,5 / −2,2 (0,30 / 0,30) | ninguno | sin efecto / sin efecto |
| E08 | Minutas FOMC del 16-sep | 2026-10-07 18:00 | federalreserve.gov | A | +0,5 / −6,5 / −6,3 % | +0,3 / −6,4 / −7,6 % | +0,3 / −2,9 / −1,9 % | +0,1 / −3,5 (0,70 / 0,13) | −0,1 / −3,4 (0,84 / 0,16) | Brent/Ormuz al alza ese día | dudoso / sin efecto |
| E09 | IPC sept 3,7 % a/a (subyacente 0,3 % m/m) | 2026-10-14 12:30 | bls.gov | A | −1,8 / −5,1 / n/d | −2,2 / −5,4 / n/d | −1,4 / −3,3 / n/d | −0,3 / −1,6 (0,47 / 0,39) | −0,7 / −2,0 (0,16 / 0,35) | ninguno | sin efecto / sin efecto |
| E10 | PPI sept +1,3 % m/m | 2026-10-15 12:30 | bls.gov | A | −1,2 / +2,4 / n/d | −1,1 / +2,1 / n/d | −1,0 / +1,6 / n/d | −0,1 / +0,7 (0,81 / 0,70) | 0,0 / +0,4 (0,96 / 0,84) | Día siguiente al IPC | sin efecto / sin efecto |
| E11 | Senado: cloture CLARITY fracasa 49-50 (votación 18:18 UTC; resultado 19:00 UTC) | 2026-09-15 18:18 | Senate floor log (vía prensa) | A | −5,1 / −7,8 / +13,8 % | −4,3 / −6,1 / +13,4 % | −0,4 / −0,9 / +13,2 % | −4,7 / −6,9 (0,002 / 0,03) | −3,9 / −5,3 (0,004 / 0,07) | FOMC al día siguiente (dentro de las 24 h, no en la 1.ª hora) | **directo / directo** (1 h) |
| E12 | XRPN (Evernorth) empieza a cotizar | 2026-10-12 13:30 | SEC EDGAR 8-K; Nasdaq | A | +0,1 / −1,4 / n/d | — | +0,5 / +1,1 / n/d | −0,4 / −2,5 (0,28 / 0,23) | — | ninguno | sin efecto / — |
| E13 | Debut del primer ETF spot de XRP (Canary XRPC, Nasdaq) | 2025-11-13 14:30 | Canary / SEC 8-A (vía prensa) | A | −0,1 / −8,1 / −13,4 % | — | −0,2 / −6,9 / −10,7 % | +0,1 / −0,7 (0,69 / 0,68) | — | Caída general de mercado | sin efecto / — |
| E14 | XRPL: mayoría de validadores para fixCleanup3_4_0 | 2026-10-09 09:34 | ledger XRPL (R32) | A | −0,2 / +0,7 / −4,1 % | — | 0,0 / +0,3 / −0,6 % | −0,1 / +0,3 (0,70 / 0,87) | — | ninguno | sin efecto / — |
| E15 | Sentencia Torres (XRP no es valor en ventas programáticas) | 2023-07-13 ~14:00 (±2 h) | CourtListener SEC v. Ripple (hora sin verificar) | B | 0,0 / **+64,4** / +70,5 % | — | −0,3 / +1,9 / −1,4 % | +0,3 / **+61,0** (0,40 / 0,000) | — | ninguno (la hora exacta no consta) | **directo** / — |
| E16 | Trump cita XRP, SOL, ADA en la reserva | 2025-03-02 ~15:00 (hora del post sin verificar; salto en la vela de 16:00) | Truth Social (vía Fortune/Bloomberg) | B | +16,7 / +15,1 / −0,7 % | +7,8 / +2,7 / −13,7 % | +3,2 / −1,1 / −9,5 % | +13,4 / +9,3 (0,000 / 0,02) | +4,8 / −2,3 (0,003 / 0,29) | Domingo; 2.º post del día | dudoso / sin efecto |
| E17 | Trump anuncia arancel adicional del 100 % a China | 2025-10-10 ~20:50 (otra cronología: primer aviso 10:57 ET) | Truth Social (vía prensa) | B | −13,6 / −12,5 / −14,1 % | −19,3 / −13,4 / −14,5 % | −3,2 / −5,6 / −8,3 % | −10,4 / −6,9 (0,000 / 0,03) | −16,4 / −7,9 (0,000 / 0,03) | Cascada de liquidaciones (≈19.000 M$ según prensa) y desajuste de precio en la bolsa | **directo / directo** |
| E18 | SEC y Ripple desisten de los recursos | 2025-08-07 (hora desconocida; se usa 12:00) | CourtListener 2.º Circuito (vía Bloomberg Law) | B | −0,1 / +8,3 / +4,5 % | — | −0,1 / +0,3 / +3,8 % | +0,1 / +8,0 (0,87 / 0,03) | — | ninguno | **directo** / — |
| E19 | DTCC anuncia tokenizar activos de DTC en Stellar | 2026-05-27 (hora desconocida; se usa 14:00) | dtcc.com (no leída; vía prensa) | B | — | +5,8 / **+30,6** / +50,8 % | −0,1 / −2,7 / −10,9 % | — | +5,9 / **+34,4** (0,002 / 0,002) | Otras noticias de Stellar de esa semana [VERIFICAR] | — / **directo** |

Entre eventos tipo A, el «inicio observado» (hora con mayor |exceso| en ±6 h, solo descriptivo) coincidió con la hora del evento en E02, E06 y E11 (18:00 o 14:00), y fue anterior o posterior en el resto.

## 4. Lectura por tipo de evento (con la salvedad de la muestra)
| Tipo | Eventos | Qué se observa |
|---|---|---|
| **Regulación / demandas** | E11, E15, E18 | Los tres movimientos más claros fuera de lo normal en 24 h (+61 % exceso Torres; +8 % dismissal; −6,9 % cloture). Dirección coherente con la noticia. La hora exacta de dos de ellos no consta. |
| **Macro con sorpresa de política monetaria** | E02, E06 | Sí salen de lo normal en 1 h (+2,5 %; +1,5/+2,4 %). Pero los otros 4 FOMC (2 dudosos, 2 sin efecto) y los datos (IPC, PPI, empleo, minutas) **no**. |
| **Datos macro de rutina** | E07-E10 | Ninguno distinguible del ruido; el IPC de oct-2026 movió a los tres a la vez (BTC −1,4 % en 1 h; el exceso es −0,3 %). |
| **ETF / tesorería cotizada** | E12, E13 | Sin efecto el día del debut: coherente con noticia ya descontada [ESPECULACIÓN]. |
| **Red / tecnología** | E14 | Sin efecto (esperable en una enmienda técnica). |
| **Anuncio político** | E16, E17 | Reacciones enormes pero distintas: el post de la reserva (E16) subió XRP +16,7 % en la hora y **lo devolvió** (24 h +15,1 %, 7 d −0,7 %; XLM +2,7 % y −13,7 % a 7 d). E17 fue un choque de todo el mercado con exceso extra por la cascada. |
| **TradFi / tokenización (XLM)** | E19 | Único evento de XLM con exceso de +34 % en 24 h y +70 % en 7 d; los 7 d incluyen más noticias de la misma semana [VERIFICAR]. |

## 5. Hechos y opiniones
**HECHOS (medidos):** los rendimientos, las colas y la β de la tabla (Binance 1 min/1 h; cruce con CoinGecko dentro de 0,6 %). Que en 15 de 32 pares el movimiento no sale de lo normal y en 11 sí. El debut de XRPC y de XRPN no dejó un movimiento propio detectable el primer día.
**OPINIONES / ESPECULACIÓN:** que los ETF estaban «descontados»; que Jackson Hole o la subida de la Fed «causaron» la subida (en E06 el precio venía de −10 % en 24 h, un rebote técnico es igual de posible). Ninguna cifra de este informe prueba causa.

## 6. Límites y sesgos
- **Sesgo de selección:** los 19 eventos son los que ya aparecían en el cerebro o se recuerdan por su efecto; no son una muestra aleatoria. Faltan los eventos «aburridos» que no movieron nada, así que la proporción de «efecto» está inflada.
- **Pruebas múltiples:** 32 pares × 2 ventanas al 5 % → 2-3 falsos positivos esperables por azar.
- **Horas tipo B no verificadas** (E15-E19): la ventana de 1 h no se usa; E16 usa 15:00 UTC porque XRP estaba plano hasta esa hora (comprobado en la serie), lo cual es mirar el resultado para fijar la hora. E15, E18 y E19 conservan solo las ventanas de 24 h y 7 d.
- **Binance ≠ mercado entero:** en la cascada del 10-oct-2025 el mínimo de Binance XRPUSDT (−55,8 %, ver R49) fue un desajuste de la propia bolsa; el exceso de E17 mezcla noticia, liquidaciones y fallo de precio. No se separan.
- **Colas con ventanas solapadas** y volatilidad no estacionaria (2023 distinta de 2026): la cola de 7 d es poco fiable.
- **FOMC y otras fechas de memoria** (2023-2025): [VERIFICAR] en federalreserve.gov. Las horas de E11 (floor log vía prensa), E13 (apertura de sesión, no la primera operación) y E14 (hora del ledger citada en R32) no se han revisado en primaria en esta sesión.

## 7. Qué falta por buscar
1. **Hora exacta con primaria** de E15 (CourtListener, marca de la orden), E16/E17 (Truth Social, archivo), E18 (PACER/CourtListener) y E19 (nota de DTCC); repetir sus ventanas de 1 h.
2. Más eventos **sin efecto** (para quitar el sesgo): cada FOMC, IPC y empleo de 2023-2026 con una regla única (sería un barrido automático, sin IA) y tasa de «salir de lo normal» por tipo.
3. Eventos de XLM: actualizaciones de protocolo de Stellar, SDF trimestral, listados; solo hay 1 evento específico de XLM (E19).
4. Hora de cada anuncio de Ripple (Swell 27-29-oct-2026, alianzas): medir **después**, no antes.
5. CoinGecko/CoinMarketCap con los mismos eventos para ver la sensibilidad a la fuente (USDT vs USD).

## Caso alcista / bajista (añadido 27-oct-2026, C27; sin predicción, solo con datos de este informe)
Tema: si las noticias mueven el precio de XRP y XLM.
- **Alcista (la noticia sí cuenta):** 11 de 32 pares salen de lo normal, y los más claros van en la dirección de la noticia: sentencia Torres (+61 % de exceso), desestimación (+8 %), fracaso del cloture de CLARITY (−6,9 %) y DTCC–Stellar (XLM, +34 % en 24 h).
- **Bajista (la noticia casi nunca cuenta):** 15 de 32 pares no muestran efecto detectable; IPC, PPI, empleo, minutas y ETF/tesorería (XRPC, XRPN) no se distinguen del ruido, y de 5 FOMC solo 1 sale de lo normal. El post de la reserva (E16) subió +16,7 % y lo devolvió.
- **Sesgo:** 19 eventos elegidos a posteriori y 2-3 falsos positivos esperables por azar; coincidencia en el tiempo no prueba causa.
