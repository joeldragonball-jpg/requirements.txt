# Auditoría de datos y research (C183 + C184) · hecha el 8-nov-2026

Sin recomendaciones de compra/venta. Niveles: [P] fuente primaria · [S] secundaria/agregador · [VERIFICAR] sin contrastar · [ESPECULACIÓN] opinión. Cada cifra se releyó el 8-nov-2026 con curl desde la fuente indicada (APIs públicas; no hizo falta Chrome).

## C183 · Muestreo de cifras de pantalla (fuente: `explorador/paneles.json`, leído 8-nov 21:01 UTC)

### HECHOS: 21 cifras comparadas, 0 errores de cálculo, 1 desfase por antigüedad

| # | Pantalla | Dato (en pantalla) | Fuente primaria y fecha | Diferencia | Acción |
|---|---|---|---|---|---|
| 1 | Móvil · Inflación | IPC EE. UU. sep-2026: 3,7 % (ant. 3,4 %) | FRED CPIAUCNS: 336,940 / 324,800 = 3,74 %; ago 3,40 % (8-nov) [P] | 0 | Ninguna |
| 2 | Móvil · Inflación | PCE EE. UU. sep: 3,6 % (ant. 3,4 %) | FRED PCEPI: 132,257 / 127,601 = 3,65 %; ago 3,44 % [P] | 0 (redondeo 3,65→3,6; sería 3,7 si se redondea hacia arriba) | Revisar el redondeo (ver nota 1) |
| 3 | Móvil · Inflación | IPCA zona euro oct: 4,0 % (ant. 3,8 %) | Eurostat `prc_hicp_minr`, EA, 2026-10 = 4,0; sep 3,8 [P] | 0 | Ninguna |
| 4 | Móvil · Inflación | IPCA España oct: 4,9 % (ant. 5,0 %) | Eurostat `prc_hicp_minr`, ES, 2026-10 = 4,9; sep 5,0 [P] | 0 | Ninguna |
| 5 | Móvil · Mercado | S&P 500 7.376,86 (6-nov) | Yahoo chart API, cierre 6-nov = 7.376,86 [S] | 0 | Ninguna |
| 6 | Móvil · Mercado | Nikkei 57.434,77, −5,96 % | Yahoo: 61.077,90 → 57.434,77 = −5,96 % [S] | 0 | Ninguna (caída fuerte pero real en la fuente) |
| 7 | Móvil · Mercado | Kospi 5.059,69, −6,02 % | Yahoo: 5.383,80 → 5.059,69 = −6,02 % [S] | 0 | Ninguna |
| 8 | Móvil · Mercado | Ibex 35: 19.369,5 | Yahoo, cierre 6-nov = 19.369,5 [S] | 0 | Ninguna |
| 9 | Móvil · Mercado | XRP 1,18 $ / XLM 0,1543 / BTC 75.887 / ETH 2.239,84 (leído 7-nov 01:03) | CoinGecko, 8-nov: XRP 1,13 · XLM 0,1464 · BTC 74.977 · ETH 2.171,75 [S] | XRP −4,2 %, XLM −5,1 %, BTC −1,2 %, ETH −3,0 % respecto a pantalla | Es antigüedad (~44 h), no error. Ver nota 2 |
| 10 | Móvil · Valoración | LMT: precio 567,08, PER 20,1, TTM a 27-sep | Yahoo cierre 6-nov 567,08 [S]; SEC companyfacts: resultado neto 9M-2026 5.169 M y 2025 FY 5.017 M [P] | Precio 0. El `ni` TTM de 6.513 M no se reproduce con lo que muestra el JSON de SEC (9M-2026 + resto de 2025); depende de qué trimestres de 2025 se sumen | [VERIFICAR] el cálculo TTM (ver nota 3) |
| 11 | Móvil · Valoración | RTX 189,53; NVDA 186,64 | Yahoo cierre 6-nov: RTX 189,53; NVDA 186,64 [S] | 0 | Ninguna |
| 12 | Órbita · Riesgos | HY OAS 3,48 % (5-nov); máx. 12 m = 3,48 | FRED BAMLH0A0HYM2 5-nov = 3,48 [P] | 0 | Ninguna |
| 13 | Órbita · Riesgos | IG OAS 0,93 % (5-nov) | FRED BAMLC0A0CM = 0,93 [P] | 0 | Ninguna |
| 14 | Órbita · Riesgos | NFCI −0,459 (30-oct) | FRED NFCI = −0,459 [P] | 0 | Ninguna |
| 15 | Órbita · Riesgos | STLFSI4 −0,5224 (30-oct) | FRED STLFSI4 = −0,5224 [P] | 0 | Ninguna |
| 16 | Órbita · Crédito | Euríbor 12 m oct: 3,239 % (ant. 3,247) | BCE `FM/M.U2.EUR.RT.MM.EURIBOR1YD_.HSTA`: 3,2386 (oct), 3,247 (sep) [P] | 0,0004 pp (redondeo) | Ninguna |
| 17 | Órbita · Crédito | Hipotecas ES TAE sep: 3,04 % (ant. 3,10) | BCE MIR ES: sep 3,04; ago 3,1 [P] | 0 | Ninguna |
| 18 | Órbita · Crédito | Hipotecas zona euro sep: 3,92 % | BCE MIR U2: sep 3,92; ago 3,91 [P] | 0 | Ninguna |
| 19 | Órbita · Banca | NPL España 2T-2026 todas las entidades: 2,39 % (ant. 2,48) | BCE SUP `Q.ES.W0._Z.I7000._T.ALL…`: 2026-Q2 2,39; Q1 2,48 [P] | 0 | Ninguna |
| 20 | Órbita · Crédito | Calificación España Moody's A3 / S&P A+ / Fitch A | Tesoro Público (tabla con fechas sep-2025); sin reabrir hoy | Sin contrastar con las agencias | Mantener [VERIFICAR] (ya marcado en la ficha) |
| 21 | Órbita · Estabilidad | Depeg USDT 0,99869 / USDC 0,99973 (8-nov) | DefiLlama [S]; no se contrastó con el emisor | — | Mantener [S]; la web de Tether/Circle es el contraste primario |

### Coherencia de niveles
- Recorrí `paneles.json` buscando: nivel P con fuente Yahoo/CoinGecko/DefiLlama, nivel S con fuente oficial (FRED, BCE, BLS, Eurostat) o `[S]` en el texto con nivel P. **0 incoherencias.**
- Mercado (CoinGecko) = S, Índices (Yahoo) = S, Depeg (DefiLlama) = S, Inflación = P con Japón y China en S (índice BIS) y declarado [S] en la serie. Todo coherente.
- Valoración: precio Yahoo [S] + fundamentales SEC [P] se declaran por separado en el aviso. Correcto.
- Calificaciones: el nivel P es el del Tesoro, pero las fechas son de sep-2025 → hay una nota [VERIFICAR] explícita. Coherente.

### Notas
1. **Redondeo PCE.** 3,649 se muestra como 3,6; es correcto (3,649 → 3,6). No es discrepancia.
2. **Desfase de cripto.** Mercado (CoinGecko, [S]) se leyó el 7-nov 01:03 UTC mientras que `paneles.json` global tiene fecha 8-nov 21:01. Solo ese bloque va 44 h atrasado: **en una semana con caídas del 3-5 % puede inducir a error.** Acción: que la pantalla muestre la hora de lectura de ese bloque (ya hay `leido`; confirmar que sale en el móvil) o que el bot lo actualice con cada ciclo. Se enlaza con C187.
3. **TTM de LMT.** Solo contrasté el resultado neto acumulado de SEC; no recalculé el TTM de 6.513 M (necesitaría el 9M-2025). Queda [VERIFICAR] hasta rehacer la suma con los 4 trimestres. No hay indicio de error, solo no reproducido.

## C184 · Informes de la semana (2–8 nov) que siguen en S o [VERIFICAR]

Conteo de etiquetas en los 72 informes (`grep` por archivo; incluye las líneas de leyenda, así que 1-2 son ruido). **HECHOS:** los de más [VERIFICAR] son, sobre todo, investigaciones y auditorías abiertas. **Propuestas = OPINIONES** mías para que Joel decida.

| Informe | [VERIFICAR] / [S] / [P] | Qué queda | Propuesta |
|---|---|---|---|
| 2026-11-02-C42-rendimientos-colateral | 20 / 11 / 1 | Solo 7 búsquedas web; Reino Unido, Corea, Emiratos y buena parte de Singapur/Japón sin leer; casi todo [S] | **Subir**: es el que más debe a normas primarias. Segunda pasada por jurisdicción (staking/lending). Mientras tanto, no citar cifras como [P] |
| 2026-11-03-C98-auditoria-opus | 16 / 0 / 0 | Es una auditoría con lista de chequeo; los [VERIFICAR] son pendientes técnicos (tope del chat sin token, coste de repo privado) | **Archivar** como histórico; convertir S4 (tope de 40 preguntas) en tarea si no existe |
| 2026-11-03-C81-auditoria-vision | 14 / 1 / 0 | Auditoría de visión; ya superada por C98 | **Archivar** |
| 2026-11-02-C74-materias-primas-credito-bancario | 13 / 3 / 12 | Riesgo: el Data Download Program de la Fed cambia la semana del 9-nov | **Subir** tras el 9-nov (comprobar que sigue el ZIP/URL); lo demás ya es [P] |
| 2026-11-08-creditos-y-riesgos | 12 / 4 / 9 | Plan de paneles; las cifras de FRED y BCE que revisé hoy coinciden (HY, IG, NPL ES) | **Mantener**: ya hay paneles de spreads y NPL; falta zona euro agregada (clave no hallada) |
| 2026-11-03-C77-espana-gasto-inmigracion-dana | 7 / 2 / 0 | Cifras sin fuente primaria | **Subir** (INE/Hacienda/IGAE) cuando se aborde C77 |
| 2026-11-02-C30-elecciones-eeuu-brasil | 9 / 16 / 3 | Resultados de noviembre ya conocidos | **Archivar** la parte previa al 3-nov y dejar la verificación de resultados en `EV-elecciones-eeuu` |
| 2026-11-06-C69-espana-2024-2025 · 2026-11-04-C69-parte2 | 9 y 6 / 2 / 8 y 5 | Mezcla de [P] y huecos | **Subir** los [VERIFICAR] con IGAE/INE (ya hay presupuesto en `espana-presupuesto.json`) |
| 2026-11-02-C73-vivienda · 2026-11-02-auditoria-coherencia-tras-W08 | 8 y 10 | Mixtos | **Mantener**; revisar en la próxima pasada de coherencia |
| 2026-11-08-verificacion-prensa · 2026-11-08-edgar-w04 · 2026-11-07-C150-auditoria-valoracion | 6 / 5 / 5 | Verificaciones recientes, abiertas por el acceso a fuentes | **Mantener**; reintentar con Chrome senate.gov/congress.gov no sirve (bloqueado, ver `ACCESOS-CHROME.md`) |
| Resto (≈58 informes) | ≤ 5 cada uno | Cierre normal | **Sin acción** |

### Qué NO se hizo (límites)
- No se verificó con la fuente de emisor (Tether, Circle) ni con las agencias (Moody's, S&P, Fitch); no se usó Chrome porque todas las fuentes elegidas respondieron por API.
- No leí informes enteros; el conteo es por etiqueta y no distingue [VERIFICAR] de leyenda.
- Valoración: solo 3 de las filas; un PER no se contrastó con una segunda fuente independiente.

## Resumen (3 líneas)
1. 21 cifras de Mercado, Inflación, Valoración, Riesgos y Crédito coinciden con su fuente; la única diferencia es la antigüedad del bloque cripto (~44 h).
2. Los niveles S/P son coherentes en todo `paneles.json`; queda pendiente recalcular el TTM de LMT y contrastar las calificaciones con las agencias.
3. Proponer: archivar C81/C98 y la parte previa de C30; subir C42, C74 (tras el 9-nov), C77 y C69 con fuentes primarias.
