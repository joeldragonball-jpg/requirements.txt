# C132 · Centro de control para el móvil: esquema (5-nov-2026)

Fase 1 de 2: **solo diseño, sin código**. Se implementa cuando Joel dé el visto bueno (paso 4 del prompt `research/prompts/C132-centro-control-movil.md`). Sin API de Anthropic. Informativo: no es una recomendación de compra ni de venta.

## 1. Qué hay ya (inventario, leído hoy del repo)

| Bloque | Dónde está | En el móvil (`data.json`) | Nivel |
|---|---|---|---|
| Bolsas: S&P 500, futuros S&P, Nasdaq, Euro Stoxx 50, DAX, CAC, FTSE, IBEX, Nikkei, Kospi, Hang Seng, Shanghái, Nifty, Bovespa, ASX, VIX | `paneles.json → indices` | sí (`indices`) | S (Yahoo) |
| ETFs de referencia: VUSA, IWDA, QQQ, EEM, SMH, SOXX, GLD, IWM… (24 valores) | `paneles.json → watchlist` | sí (`watchlist`) | S |
| Oro, plata, cobre, gas Henry Hub, trigo, maíz, café, Brent | `paneles.json → materias` | **no** | S |
| Soja y arroz (futuros), soja mensual (FRED), índice FAO de alimentos | `paneles.json → alimentos` | **no** | S / P |
| Luz España: OMIE (mercado diario) y PVPC, Eurostat semestral | `paneles.json → energia_precios` | **no** | P |
| Brent y WTI | `construir_movil.py → petroleo()` (descarga propia) | sí (`petroleo`) | S |
| EUR/USD | BCE (`cambio_euro()`) | sí (`eur`) | P |
| Tipos oficiales (Fed, BCE, BoJ…) y bono a 10 años | `tipos_vivos`, `bonos` | sí | P |
| Euríbor 12 m, hipotecas | `paneles.json → credito` | **no** | P |
| XRP, XLM, BTC, ETH | `paneles.json → mercado` + CoinGecko en vivo desde el móvil | sí | S |

### Qué falta (hay que añadirlo al bot de paneles, sin IA)
- **Dow Jones** (`^DJI`): no está en `indices`.
- **VWCE** y **SPY**: no están en la watchlist (sí VUSA, IWDA, QQQ).
- **Fondos indexados** (p. ej. Vanguard Global Stock Index, Amundi MSCI World): su valor liquidativo no tiene una API abierta fiable. Propuesta: mostrar el ETF equivalente como *referencia* y decirlo en la etiqueta. [VERIFICAR] si Morningstar o la gestora publican un CSV legible.
- **Gas europeo TTF**: Yahoo no da cierres suficientes (probado el 4-nov, ver C111). Pendiente de otra fuente.
- **Gasolina y diésel**: Boletín petrolero semanal de la Comisión Europea (Weekly Oil Bulletin, [P]); no se lee hoy.
- **Divisas** además de EUR/USD: USD/JPY, USD/CNY, EUR/GBP e índice del dólar (DXY). El BCE publica las tres primeras frente al euro ([P]).
- Opcional: azúcar (`SB=F`) y cacao (`CC=F`), dos futuros baratos de añadir. Aceite de oliva: sin fuente diaria abierta [VERIFICAR Poolred].

### Incoherencia encontrada hoy (hay que arreglarla antes de montar el panel)
El repo tiene **dos Brent que no cuadran**:
- `materias` (bot de paneles, leído el 4-nov a las 21:30 UTC): **104,06 $**, +0,44 %, con fecha 4-nov.
- `petroleo` (`construir_movil.py`, 5-nov a las 00:13 UTC): **94,89 $**, −8,41 %, con fecha 5-nov.

Según las noticias del propio repo (4-nov, 17:13), el Brent bajó de 95 $ esa tarde, así que lo más probable es que el 104,06 sea un cierre viejo (Yahoo no había actualizado la barra del día) y que el 94,89 lleve la fecha de la barra siguiente aunque es la sesión del 4-nov. [VERIFICAR] contra el cierre oficial de ICE. **Regla del panel: una sola fuente por cifra** (el Brent sale de un único sitio) y la fecha que se enseña es la de la sesión, no la de la descarga.

## 2. Dónde va (sin pantallas nuevas)
Siguiendo la regla «una sola página, sin capas nuevas»: el Centro de control **no es una pestaña más**. Se coloca **arriba del todo de la pestaña «Mercado»** como primer bloque, con el nombre «Control». Lo que hay ahora en Mercado (tipos, bonos, Ormuz, liquidez, defensa, valoración, watchlist completa) queda debajo, plegado bajo «Análisis y más datos». El id interno será `control` (ya existe una vista `centro` para los módulos y no la piso).

## 3. Paneles (orden de arriba abajo)
Una sola columna. Cada panel es una tarjeta con su título y **filas de cifra**.

| # | Panel | Filas | Fuente |
|---|---|---|---|
| 0 | Resumen del día (una línea, calculada sin IA) | «Leído a las HH:MM · el mayor movimiento: X · N datos con más de 3 días» | `data.json` |
| 1 | Mis cripto | XRP, XLM (en €, en vivo) · BTC y ETH como referencia | CoinGecko [S] |
| 2 | Bolsas | S&P 500, Nasdaq, Dow*, Euro Stoxx 50, IBEX, DAX, Nikkei, Hang Seng, Shanghái, Kospi · VIX al final en gris | Yahoo [S] |
| 3 | ETFs y fondos indexados (referencia) | VWCE*, IWDA, VUSA, SPY*, QQQ · nota: «el fondo indexado equivalente va en paralelo al ETF» | Yahoo [S] |
| 4 | Energía | Brent, WTI, gas Henry Hub, gas TTF*, luz España (OMIE media del día y PVPC media), gasolina y diésel en España* (semanal) | Yahoo [S], OMIE/REE [P], CE [P] |
| 5 | Alimentos | Trigo, maíz, soja, arroz, café · azúcar* y cacao* · índice FAO (mensual) | Yahoo [S], FAO [P] |
| 6 | Metales | Oro, plata, cobre | Yahoo [S] |
| 7 | Divisas y tipos | EUR/USD, USD/JPY*, USD/CNY*, EUR/GBP* · Fed, BCE, BoJ · bono 10 años EE. UU. y España · Euríbor 12 m | BCE, Fed, BoJ [P] |

`*` = falta la fuente (lista del apartado 1). Mientras falte, la fila no aparece (no se pintan huecos).

## 4. Cómo se ve cada cifra
```
┌────────────────────────────────────┐
│ PETRÓLEO BRENT · $ el barril       │  ← etiqueta ARRIBA, pequeña, en mayúsculas
│ 94,89                    ▼ 8,4 %   │  ← número grande (28 px) · variación con flecha
│ sesión 4-nov · 1 día · [S] Yahoo   │  ← fecha, periodo y nivel, en gris
└────────────────────────────────────┘
```
- **Número grande** a la izquierda, variación a la derecha con flecha ▲/▼.
- **Color** (regla del prompt: solo si el sentido es claro):
  - Bolsas, ETFs y cripto: verde si sube, rojo si baja (es el valor de lo que se tiene).
  - Materias primas, energía, alimentos, divisas y tipos: **flecha sin color** (gris). Que suba el petróleo es bueno para un productor y malo para quien llena el depósito; no lo juzgo con el color.
  - VIX: gris siempre.
- **Unidades legibles**: el trigo, el maíz y la soja vienen en centavos por bushel; se enseñan en **$ por tonelada** (conversión fija: trigo y soja 36,74 bushels/t; maíz 39,37) y en la etiqueta va la unidad original para quien la busque. El café en $ por libra. La luz en €/MWh.
- **Frescura**: si el dato tiene más de 3 días hábiles, la fecha sale en ámbar con «dato del 2-nov». Si una bolsa estuvo cerrada por festivo (p. ej. Japón el 3-nov), la fecha lo cuenta y no se marca como error.
- **Nivel**: [P] fuente oficial leída, [S] agregador o prensa. Se toca la fila → se despliega la fuente con enlace, la variación a 1 mes si existe y una nota de una línea.
- Números en formato español (coma decimal, punto de miles).

## 5. Datos y seguridad (C90)
- `construir_movil.py` añade a `data.json` una clave nueva `control`, compactada de `paneles.json` (materias, alimentos.futuros, último día de OMIE y PVPC, Euríbor) más lo que ya hay (índices, watchlist, petróleo, eur, tipos, bonos). Formato de cada fila: `{grupo, etq, valor, unidad, cambio, periodo, fecha, nivel, fuente, color: "precio"|"neutro"}`. Tamaño estimado: +4 KB.
- El móvil no hace descargas nuevas (solo la de CoinGecko, que ya existe).
- La vista nueva se construye con `createElement` y **`textContent`**, no con `innerHTML`: ningún texto de fuera se interpreta como HTML. Así no aumenta la superficie que revisa C90 (el resto de la app sigue usando `esc()` dentro de plantillas).

## 6. Qué haría en la fase 2 (con tu OK)
1. Arreglar el Brent duplicado (una sola fuente; fecha de sesión).
2. Añadir al bot de paneles, sin IA: `^DJI`, `VWCE`, `SPY`, `SB=F`, `CC=F` y divisas del BCE (JPY, CNY, GBP).
3. `construir_movil.py`: clave `control`.
4. `docs/movil/index.html`: bloque «Control» arriba de Mercado, con `textContent`.
5. Probarlo en el navegador a ancho de móvil (375 px) y en modo oscuro.
Quedan fuera de esta tarea (necesitan fuente nueva): TTF (C111), gasolina y diésel (Weekly Oil Bulletin), fondos indexados por valor liquidativo.

Coste estimado de la fase 2: ~3-4 % semanal (Opus o Sonnet; el diseño ya está hecho, Sonnet basta).

## Lecciones
- Antes de montar un panel nuevo, comprobar que una misma cifra no sale de dos scripts distintos (hoy el Brent: 104,06 frente a 94,89).

## Fase 2 hecha (5-nov-2026, con el OK de Joel)
- **Brent arreglado en la raíz**: `scripts/yahoo_diario.py` fecha cada cierre con la hora de la bolsa y usa el último precio de mercado. Se aplica a índices, materias primas, futuros de alimentos, petróleo del móvil y watchlist. Antes y después: Brent 104,06 $ «4-nov» / 94,89 $ «5-nov» → 94,67 $ con fecha 4-nov y −8,6 % en las dos fuentes. El mismo fallo afectaba a la watchlist: VWCE, IWDA y VUSA daban el precio de hoy con la variación del día anterior (−0,78 % «3-nov» → +1,07 % el 4-nov).
- **Datos nuevos en el bot de paneles (sin IA)**: Dow Jones (`^DJI`), VWCE y SPY (en `watchlist.toml`), cacao (`CC=F`), divisas del BCE (USD, GBP, CHF, JPY, CNY) y DXY (`leer_divisas`, clave `divisas`). Aparecerán en el móvil cuando el bot de paneles corra con este código.
- **`construir_movil.py`**: nueva clave `control` (7 grupos, ~14 KB).
- **`docs/movil/index.html`**: bloque «Control» arriba de Mercado, hecho con `createElement` y `textContent`; lo de antes queda plegado en «Análisis y más datos». Caché del móvil `cerebro-movil-56`.
- **Probado** a 375 px en modo oscuro y claro: 7 tarjetas y 49 cifras con los datos nuevos, sin desplazamiento lateral, sin errores nuevos en la consola.
- Pendiente fuera de C132: gas TTF (C111), gasolina y diésel (Weekly Oil Bulletin) y valor liquidativo de fondos indexados.
