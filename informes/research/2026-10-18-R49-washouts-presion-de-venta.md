# R49 · Washouts y presión de venta recurrente (XRP, XLM)

> **Nota de revisión (18-oct, sesión de revisión):** (1) se corrigió «más de la mitad» por «entre el 47 % y el 61 %» (XLM es 50/106 = 47 %). (2) La concentración de 15:00-19:59 UTC se compara con un reparto uniforme de horas; esas horas son también las de más volatilidad, así que prueba **cuándo** ocurren las caídas bruscas, no que haya «presión de venta» (ver §4, [ESPECULACIÓN]).

Fecha: 2026-10-18 · Sesión R49 (Sonnet 5.5, esfuerzo alto) · Sin recomendaciones de compra/venta.
Script: `scripts/estudio_eventos.py washouts` (el mismo de R48; sin IA, sin claves). Etiquetas: [VERIFICAR] / [ESPECULACIÓN].

## 1. Resumen (6 líneas)
1. **Criterio fijado antes de buscar:** *washout* = caída ≥ **7 %** (máximo→mínimo con high/low horarios) en ≤ **6 h**, seguida de recuperación ≥ **50 %** de la caída en ≤ **12 h** tras el mínimo. Episodios con mínimos a < 12 h se fusionan.
2. Aplicado a toda la serie horaria de Binance (**2023-01-01 → 2026-10-17, 1.386 días**): **XRP 148 caídas ≥ 7 %, de ellas 109 washouts (≈ 28,7/año)**; **XLM 157 y 106 (≈ 27,9/año)**. Sensibilidad: con 5 % hay 251/228 washouts; con 10 %, 48/45. Es decir, **la cifra depende mucho del umbral: un «washout» de 7 % es algo que ocurre más de dos veces al mes**, no un suceso raro.
3. **Lo que sí sale del azar: la hora.** Entre las **15:00 y las 19:59 UTC** (apertura y primera mitad de la sesión de EE. UU.) caen **41 de 109 (XRP, esperados 22,7; z ≈ 4,3)** y **40 de 106 (XLM, esperados 22,1; z ≈ 4,3)**.
4. **Lo que no sale:** fin de mes, fin de trimestre, escrow del día 1 (00:00 UTC), vencimientos (último viernes del mes, viernes en general), 13F y días de decisión del FOMC **no están sobrerrepresentados de forma convincente** (p > 0,1 sin corregir por múltiples pruebas). Los fines de semana tienen **menos** washouts de los esperados en XRP (18 vs 31 esperados).
5. **Entre el 47 % y el 61 % coincide con caída del mercado:** BTC cae ≥ 3 % en el mismo tramo de 6 h en 67 de 109 (XRP, 61 %) y 50 de 106 (XLM, 47 %). El resto son más propios del activo.
6. **No hay serie pública de liquidaciones** (ver §5): la causa «cascada de liquidaciones» no se puede medir aquí; solo es coherente con la forma (caída brusca + rebote).

## 2. Método
- Datos: velas horarias Binance spot (XRPUSDT, XLMUSDT, BTCUSDT); funding de los perpetuos USDT-M de Binance (`fapi.binance.com/fapi/v1/fundingRate`). Fuente tipo **C** (bolsa). Cruce con CoinGecko en R48 §2 (diferencia mediana 0,06 %).
- Fecha y hora siempre en UTC; el «mínimo» es la hora de la vela con el low más bajo de cada episodio.
- Calendario cruzado: sábado/domingo; día 1 (escrow de Ripple, 1.000 M XRP liberables a 00:00 UTC, R32); último día de mes y de trimestre; último viernes del mes (aprox. del vencimiento mensual de futuros de CME) y cualquier viernes (vencimiento semanal de opciones, p. ej. Bybit, no verificado) [VERIFICAR]; plazos de 13F (≈ 14-feb, 15-may, 14-ago, 14-nov); decisión del FOMC (calendario de R48).
- Prueba: P(≥ observados) binomial, con la proporción de horas de la categoría como probabilidad de azar. **No corregida por múltiples pruebas** (≈ 9 categorías × 2 activos + hora).

## 3. Resultados
### 3.1 Cruce con el calendario (X = 7 %)
| Categoría | XRP obs. / esperados / P | XLM obs. / esperados / P |
|---|---|---|
| Fin de semana | 18 / 31,1 / 0,999 (déficit) | 24 / 30,3 / 0,93 (déficit leve) |
| Viernes | 14 / 15,6 / 0,71 | 17 / 15,1 / 0,34 |
| Día 1 (escrow 00:00 UTC) | 3 / 3,6 / 0,71 | 3 / 3,5 / 0,69 |
| Último viernes del mes | 1 / 3,5 / 0,97 | 6 / 3,4 / 0,13 |
| Último día del mes | 2 / 3,5 / 0,87 | 6 / 3,4 / 0,13 |
| Último día del trimestre | 0 / 1,2 / 1,00 | 1 / 1,1 / 0,68 |
| Plazo 13F | 3 / 1,2 / 0,12 | 1 / 1,1 / 0,68 |
| Día de decisión del FOMC | 4 / 2,4 / 0,21 | 1 / 2,3 / 0,90 |
| **15:00-19:59 UTC** | **41 / 22,7 (z ≈ 4,3)** | **40 / 22,1 (z ≈ 4,3)** |

Por día de la semana (XRP): lunes 25, martes 21, miércoles 17, jueves 14, viernes 14, domingo 10, sábado 8. **El lunes concentra 23 % (25/109) frente a 14 % esperado**; con 7 categorías el resultado puede ser azar, sin corregir [ESPECULACIÓN: huecos del fin de semana].
Por año (XRP): 2023: 24 · 2024: 48 · 2025: 30 · 2026 (hasta 17-oct): 7. XLM: 11 · 42 · 31 · 22. **La frecuencia varía mucho entre años** (la volatilidad no es estacionaria).

### 3.2 Los mayores (mínimo UTC · caída · % de recuperación en ≤ 12 h)
**XRP:** 2023-08-17 21:00 (−27,1 %, 64 %) · 2024-01-03 12:00 (−21,4 %, 66 %) · 2024-04-13 20:00 (−23,5 %, 63 %, sábado) · 2024-12-09 21:00 (−18,8 %, 60 %) · 2024-12-10 17:00 (−14,5 %, 150 %) · 2025-10-10 21:00 (**−55,8 %**, 79 %, viernes) · 2026-08-22 05:00 (−17,7 %, 84 %, sábado).
**XLM:** 2023-08-17 21:00 (−14,8 %) · 2024-04-13 20:00 (−20,1 %, 88 %) · 2024-12-09 21:00 (−25,3 %) · 2025-10-10 21:00 (**−58,5 %**, 80 %) · 2026-06-15 15:00 (−21,5 %, 138 %).
**Coinciden en las dos monedas:** 17-ago-2023, 13-abr-2024, 9-dic-2024 y 10-oct-2025: lo que mueve a las dos es del mercado o de la plataforma, no de Ripple ni de Stellar.

### 3.3 Funding
La mediana del funding de los perpetuos en el último cobro previo al mínimo es **0,0100 %** (XRP y XLM) frente a **0,0080 % (XRP) y 0,0067 % (XLM)** en toda la serie. 0,01 % cada 8 h es el valor base habitual de esa bolsa: la diferencia es pequeña y **no demuestra apalancamiento en largo previo** [VERIFICAR; ver R42]. Se necesitan OI y liquidaciones por tramo, que no están en abierto (§5).

## 4. Qué nos dice (y qué no)
- **Hechos:** los washouts de 7 % son frecuentes (≈ 2-3 al mes por moneda); se agrupan en la sesión de EE. UU. (15-19 UTC); hay años con mucha más frecuencia (2024); entre el 47 % (XLM) y el 61 % (XRP) coincide con caída de BTC; fin de mes/trimestre, vencimientos y escrow no destacan.
- **No se puede afirmar:** que haya «presión de venta recurrente» a fin de trimestre o por el escrow. Con los datos, ni se confirma ni se descarta en detalle: la muestra por categoría es de 0-6 casos.
- **[ESPECULACIÓN]:** el pico de 15-19 UTC podría reflejar la liquidez que entra con la sesión de EE. UU. (datos macro 12:30-14:00 UTC, FOMC 18:00 UTC), pero no se ha probado qué parte coincide con datos o con la apertura de Wall Street.
- **Efecto del 10-oct-2025:** el −55,8 % de XRPUSDT en Binance en una hora es un valor extremo, mayor que el movimiento de mercado (BTC −3,2 % en la hora); parte es un desajuste de la propia bolsa. Un washout «de libro» no distingue entre una cascada real y un fallo de precio de una plataforma.

## 5. Lo que NO se puede medir (y por qué)
- **Liquidaciones:** no hay serie pública gratuita de liquidaciones por activo y hora (R42). Las cifras de prensa (CoinGlass, ≈19.000 M$ el 10-oct-2025) son de un agregador.
- **Interés abierto (OI):** la API pública de Binance solo da ~30 días de histórico; CFTC publica semanalmente (informe COT) y no por horas: no sirve para fechar un washout.
- **Calendario de vencimientos:** CME (futuros de XRP) y Bybit (opciones) tienen reglas propias; aquí solo se usó «último viernes» y «viernes» como aproximación [VERIFICAR contra las especificaciones de CME y Bybit].

## 6. Hechos y opiniones
**HECHOS (medidos):** 109 y 106 washouts del criterio; concentración horaria 15-19 UTC (z ≈ 4,3); sin sobrerrepresentación convincente en fin de mes/trimestre/escrow/vencimientos/13F; 67/109 y 50/106 con BTC cayendo ≥ 3 %.
**OPINIONES:** cualquier relato sobre «manos fuertes», «market makers» o «ballenas» que provoquen los washouts. No se contrastó ninguno; sin dato de libro de órdenes.

## 7. Qué falta por buscar
1. Repetir con el **mínimo/máximo de 1 min** (más preciso que las barras de 1 h) en los 20 mayores y cruzarlos con la hora de datos macro y de noticias propias.
2. Obtener **liquidaciones por hora** de un proveedor con histórico (CoinGlass, CoinAPI, Tardis) si Joel tiene acceso a una descarga (hueco para PDF/CSV, no automatizable aquí).
3. **Vencimientos reales** (CME XRP/XLM; Bybit/Deribit-type opciones): calendarios oficiales para sustituir la aproximación.
4. **OI y funding por hora** del archivo propio: empezar a guardar una serie diaria desde hoy (script sin IA) para dentro de 3-6 meses.
5. Mismo estudio con **USD de CoinGecko/Kraken** para ver cuánto del resultado es de la base USDT.

## Caso alcista / bajista (añadido 27-oct-2026, C27; sin predicción, solo con datos de este informe)
Tema: caídas bruscas con rebote (washouts) en XRP y XLM.
- **Alcista:** el rebote es la norma en la definición usada (≥ 50 % de la caída recuperado en ≤ 12 h) y entre el 47 % (XLM) y el 61 % (XRP) coincide con caída de BTC, es decir, no es debilidad propia del activo. Fin de mes, fin de trimestre, escrow, vencimientos y FOMC no destacan.
- **Bajista:** son frecuentes (≈ 28-29 al año por moneda, más de dos al mes) y se concentran de forma significativa en la sesión de EE. UU. (15:00-19:59 UTC, z ≈ 4,3). El resto de caídas (39-53 %) es más propio del activo, y no se puede medir la causa (sin serie pública de liquidaciones).
- **Sesgo:** la cifra depende del umbral (5 %: 251/228; 10 %: 48/45) y el −55,8 % del 10-oct-2025 en Binance mezcla cascada real y fallo de precio de la bolsa.
