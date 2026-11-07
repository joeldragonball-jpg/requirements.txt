# C159 · Auditoría de valoración de la Órbita de escritorio (7-nov-2026)

Sesión de solo lectura. Leído: `graphify-out/GRAPH_REPORT.md` (cabecera), pendientes de C127/C129/C134 y C150 (móvil). Cifras contrastadas con `explorador/*.json` y `docs/movil/data.json`, no de memoria. No se repiten hallazgos ya cerrados o con tarea (Ormuz en el móvil, Brent spot/futuro, noticias sin «por qué» en el móvil: C151-C158; tabla de bonos, textos < 13 px, España/Presupuesto: C129/C134).

## Resumen (5 líneas)
1. La Órbita está bien en lo visual: sin desbordes a 1440 ni a 1024 (salvo 1 tabla en Paneles), letra mínima 13 px (salvo «Plazo» en Voces, 12,5 px) y 0 pares texto/fondo bajo 4,5:1 medidos con composición de transparencias.
2. **No tiene modo claro**: con `prefers-color-scheme: light` sigue en fondo oscuro (`rgb(14,20,32)`). «Claro y oscuro» no es comprobable; es una decisión, no un fallo.
3. Fallo de contenido más serio: la sección **«Últimas 24 h» de Noticias mezcla hechos futuros** (presidencial francesa 18-abr-2027, elecciones españolas 29-nov-2026) con noticias de hoy; y la cabecera dice «Órbita 2026-10-27» aunque `datos.json` ya contiene hechos del 6-nov.
4. Las afirmaciones de la capa «XRP/XLM» de `datos.json` tienen la etiqueta de nivel vacía en ~9 casos; los fallos de datos (FRED sin respuesta, `divisa NoneUSD` 404, 25 huecos de indicadores) no se explican en pantalla.
5. 14 mejoras (8 pequeñas, 6 tareas) y 6 filas propuestas C160-C165.

## 1. Hallazgos de contenido

| # | Hallazgo | Dónde | Etiqueta |
|---|---|---|---|
| a | **«Últimas 24 H (8)» incluye fechas futuras**: 2027-04-18 (Francia, 1.ª vuelta) y 2026-11-29 (España) aparecen como noticias de 24 h junto a las de 2026-11-06. Lo que es calendario sale como si fuera noticia. | Pestaña Noticias; lógica de cubos de `noticias_a_orbita.py` / `_html()` | Bug, HECHO (visto en pantalla) |
| b | **Cabecera «Órbita 2026-10-27»**: es `datos.json → version`, pero el archivo tiene 103 movimientos con 6 del 6-nov. Parece que lo central lleva 11 días sin tocar, mientras «radar 2026-11-04» y «paneles 2026-11-07» sí son recientes. | Línea «Datos reales:» (todas las pestañas); `datos.json → version` | Fecha engañosa |
| c | **Frescura heterogénea**, mismos hallazgos que el móvil pero visibles aquí: `calificaciones` y `reservas` 22-oct, `deuda-fmi` 21-oct, `cbdc-blockchains`/`rwa-por-cadena` 29-oct, `estabilidad-manual` 5-oct (máx. fecha), `espana-presupuesto` 30-oct. `indicadores-manual.json` y `liquidez-manual.json` no llevan fecha propia (la liquidez la hereda del `leido` de paneles, 4-nov 04:27). Solo el pie de cada tabla dice «leído 2026-10-22»; no hay semáforo común. | `explorador/*.json`; pies de bloque en Paneles | Sin semáforo |
| d | **Fallos silenciosos**: `paneles.json` lista `FRED no responde` (PCE EE. UU., crédito Fed H.8, soja), `divisa NoneUSD: 404` en `indices.fallos` (un símbolo mal construido) y 25 huecos en indicadores (deuda/déficit sin dato FMI para ID, EG, ET, IR, AE, SV, AR, VE, CU; pobreza de BR/IR/AE/CU). La pantalla enseña el hueco o simplemente no lo enseña. | `paneles.json → indices/inflacion/alimentos/credito/indicadores .fallos` | Hueco no explicado |
| e | **Capa XRP/XLM con nivel vacío**: en `datos.json → capas[].xrp` hay ~9 afirmaciones con `k: ''` (p. ej. «Ninguna fuente oficial leída nombra XRP, XLM, Ripple ni Stellar», «No: corre sobre Base y Canton», «Sí, pero pequeño: DEX XRPL ≈ 6,2 M$/día» sí lleva S). Son hechos de «ausencia de evidencia» sin etiqueta [P]/[S]/[VERIFICAR]. | `datos.json → capas[].xrp[].k` | Sin etiqueta |
| f | **Sistemas de niveles distintos entre pestañas**: Voces usa P/D/S/C/R/E (6 niveles, `voces.json → niveles`); Regulación P/S/V (103 P, 35 S, 30 V = 18 % por verificar); Capas «k»: P/S/ESP/vacío; el móvil explica solo P/S (+D). Tres vocabularios para «cuánto me fío». | `voces.json`, `regulacion.json`, `datos.json` | Inconsistencia |
| g | **Voces**: 68 (el móvil enseña 20). Rango 2018-11-14 a 2026-11-04; 32 son anteriores a sep-2026. Solo 15 de 68 nombran XRP/XLM (`tokens`). Hay 3 voces con Garlinghouse, 3 BIS, 3 Despeja La X, 3 Schwartz y 2 DTCC: la concentración que C150 vio en el móvil es menor aquí, pero 35 de 68 son «compatible con los datos» frente a 1 «contradicha»: poca fricción crítica. | `explorador/voces.json` | Sesgo de fuente |
| h | **Plazos prometidos a 2030-2031** (`plazo.prometido`, 19 casos con plazo) mezclados con hechos en tarjetas de Voces; solo «Plazo: …» en 12,5 px los distingue. Debe leerse como intención [ESPECULACIÓN]. | Pestaña Voces | Intención vs hecho |
| i | **Mezcla hecho/opinión en noticias del bot**: «Daly (Fed): más subidas de tipos probables» y «Se espera que la Fed mantenga su subida de tipos de diciembre» salen como «◐ Sin contrastar» sin «por qué importa». Con la Fed en 3,75-4,00 % y último cambio +25 pb el 17-sep, el segundo titular habla de una «subida de diciembre» que no se explica. | Noticias → Últimas 24 h; `noticias-archivo.json` | [VERIFICAR] |
| j | **Mismos datos con hora distinta entre Órbita y móvil**: precios en vivo (XRP 1,16 $ a las 17:45 en el KPI) frente a `paneles.mercado` XRP 1,18 / XLM 0,1543 (7-nov 01:03) y `precios_vivos` XRP 1,18 / XLM 0,1554 (6-nov 22:04). Es coherente pero el KPI no indica el instante concreto de cada cifra (solo el «en vivo» global). Ormuz coincide con el móvil (25-oct, media 3,3, banner «hace 13 días, dato congelado»): aquí sí está visible, en la tarjeta de Resumen. | Resumen → KPI Cripto; `precios_vivos.json`, `paneles.json` | Aclarar |
| k | **KPIs con unidades mezcladas** persisten de C127: «$9332 mil M» (deuda en manos extranjeras, sin separador de miles; es TIC, nivel P), «$294,7 mil millones», «233 €/MWh», «136» (FAO), «5» stablecoins despegadas. Nada en la cifra grande distingue magnitud. | Resumen → Cifras clave | Abierto (C127) |
| l | **Cobertura frente a la visión**: XRP/XLM tienen precio, stablecoins en XRPL/Stellar, DEX, custodia, ETF 13F y tesis por capa. Falta: flujos/ETF spot de XRP (cifras, no solo «sin señal 13F»), actividad de red XRPL/Stellar como serie temporal, y un bloque «qué cambió desde ayer para mis activos». Países/macro/España: cubiertos (21 jurisdicciones × 8 temas, 168 celdas); Resumen sigue sin «qué cambia hoy» (C127). | `datos.json`, Resumen | Hueco |
| m | **Regulación**: 12 «huecos» declarados (Egipto, Etiopía, Irán parcial, etc.) y 30 celdas V. Está bien documentado; no se mezcla hecho/opinión (cada celda lleva `falta`, `proxima`, `caduca`). Una celda revisada (GENIUS/OCC, 21-oct) lleva `caduca` 2027-01-19, bien. | `regulacion.json` | Correcto |

## 2. Hallazgos de estética y usabilidad

Método: servidor estático local (`python -m http.server 8797`, parado al terminar), navegador integrado a 1440×900 y 1024×768. El contenido va en un iframe `srcdoc` bajo una barra de 10 pestañas. Medidas dentro del iframe: alto, desbordes, letra mínima y contraste con transparencias compuestas. **Limitación:** el panel de capturas solo mostró ~800 px de ancho útil, así que las capturas no sirven para juzgar el borde derecho; las medidas sí.

Capturas descritas:
- **Resumen, 1440 oscuro.** Barra de pestañas arriba, filtros País/Tema/Certeza, línea «Datos reales…» y 4 tarjetas de colores (Cripto, Tipos y deuda, Energía y materias primas, Miedo y chips). Cifra grande, insignia [S]/[P] y variación en color. Se lee bien. La tarjeta Cripto es la más larga (11 filas) y desequilibra las otras. «Barcos por Ormuz 2 · hace 13 días, dato congelado» está visible en rojo.
- **Paneles de datos, 1440.** Calificaciones soberanas (tabla 5 columnas, «Otras agencias» larga) y Deuda pública sobre PIB (7 columnas con previsiones). Columna «Otras agencias» y la de 2030 quedan al borde; el gráfico de Ormuz tiene etiquetas 01-05 legibles (mi script marcó 1,2:1, falso positivo por fondo de barra).

Medidas (1440 / 1024, alto en px):

| Pestaña | 1440 | 1024 | Desborde / nota |
|---|---|---|---|
| Resumen | 3.947 | 4.687 | 0 |
| Capas | 6.382 | 8.244 | 0 |
| Línea de tiempo | 1.024 | 943 | 0 |
| Calendario | 4.374 | 5.288 | 0; 61 fechas |
| Matriz país × tema | 1.737 | 1.977 | 0 |
| Noticias | 5.667 | 7.508 | 0 |
| Voces | 4.969 | 6.146 | 54 textos de 12,5 px |
| Países | 2.216 | 2.528 | 0 |
| España | 2.632 | 2.666 | 0 |
| Paneles de datos | 6.568 | 8.123 | **1 tabla de 1.106 px a 1024** (45 elementos fuera) |

Hallazgos:
1. **Sin modo claro** (ver resumen). Si se quiere, es una tarea; el uso es de PC y el oscuro funciona.
2. **Paneles de datos a 1024**: una tabla (`TABLE`, ancho 1.106 px) rebasa el viewport. Hay scroll horizontal dentro del bloque, pero no hay sombra ni indicación de que continúa; en Calificaciones se corta «Otras agencias».
3. **Voces**: texto «Plazo: …» a 12,5 px, el único por debajo del mínimo de 13 px acordado en C129.
4. **Pestañas más largas que una pantalla**: Capas (6.382), Paneles (6.568) y Noticias (5.667) a 1440; a 1024 crecen un 20-30 %. No hay índice interno ni anclas (se repite de C127).
5. **Resumen**: cuatro tarjetas con el mismo peso; «mis activos» (XRP/XLM) no destaca sobre «Bono a 10 años» o «VIX».
6. **Navegación entre capas**: las 10 pestañas caben a 1024 en una fila (top 4 px); bien. Los filtros País/Tema/Certeza están en todas las pestañas aunque en muchas no actúan (solo la matriz): confunde.
7. **Etiquetas**: [S] amarillo y [P] verde se distinguen en color pero no en forma; sigue pendiente de C150/C157.
8. **Contraste**: 0 pares fallidos en las 10 pestañas (tras componer la transparencia). El gris `rgb(159,176,207)` sobre fondo oscuro es el más flojo y pasa.

## 3. Mejoras priorizadas (impacto/coste)

P = arreglo pequeño (<30 min), N = tarea nueva. Los números de línea no se anotan porque `docs/orbita/index.html` es generado; el origen es `explorador/` (`_html()`/`vistas.html`) y los scripts citados.

| # | Mejora | Archivo / sección | Tipo |
|---|---|---|---|
| 1 | Excluir de «Últimas 24 h/7 d/30 d» las entradas con fecha futura (mandarlas a «Próximas») | `scripts/noticias_a_orbita.py` o `explorador/vistas.html` (cubos de Noticias) | P |
| 2 | Cambiar «Órbita 2026-10-27» por la fecha del último movimiento real (`max(movimientos.fecha ≤ hoy)`) | `explorador/datos.json → version`; línea «Datos reales» | P |
| 3 | Mostrar en cada bloque de Paneles la antigüedad con semáforo (verde ≤7 d, ámbar ≤14 d, rojo >14 d), usando `leido` o fecha | `explorador/paneles.html` / `vistas.html` | N |
| 4 | Añadir fecha propia a `indicadores-manual.json` y `liquidez-manual.json` | esos dos JSON | P |
| 5 | Etiquetar con [P]/[S]/[VERIFICAR] los ~9 `k: ''` de `capas[].xrp` (ausencia de evidencia = [S] o [VERIFICAR]) | `explorador/datos.json → capas[].xrp[].k` | P |
| 6 | Explicar los fallos de `paneles.json` (FRED sin respuesta, 25 huecos de indicadores) en una línea del bloque («sin dato en la fuente») | `vistas.html`; `indicadores-historia.json → fallos` | P |
| 7 | Arreglar `divisa NoneUSD` (símbolo mal formado en `indices`) | `scripts/actualizar_paneles.py` (divisas Yahoo) | P |
| 8 | Unificar el vocabulario de niveles (P/S/D/V/ESP) en una leyenda única visible en las 10 pestañas | `vistas.html` (pie común); `voces.json → niveles` | N |
| 9 | Subir «Plazo» en Voces a 13 px y marcarlo como [ESPECULACIÓN]/intención con badge | `vistas.html` (clase de plazo) | P |
| 10 | Bloque «Mis activos» (XRP/XLM) arriba en Resumen: precio con hora, cambio 24 h, stablecoins en XRPL/Stellar, ETF/13F y qué cambió | `vistas.html` Resumen; `precios_vivos.json`, `datos.json` | N |
| 11 | KPIs: separador de miles y unidad corta («$9.332 mil M» → «9,3 billones $»); etiqueta de periodo en cada cifra | `vistas.html` KPIs; `paneles.json → tic` | P |
| 12 | Anclas/índice interno en Capas, Paneles y Noticias; a 1024 con menú flotante | `vistas.html` | N |
| 13 | Ocultar filtros País/Tema/Certeza en las pestañas donde no actúan | `vistas.html` (barra común) | P |
| 14 | Resumen «qué cambia hoy» (5 líneas, solo hechos y fechas, sin recomendar) y noticias del bot con «por qué» obligatorio o caducidad más corta si faltan | `vistas.html`; `noticias_a_orbita.py` | N |

### Filas propuestas (no editadas en tareas.csv ni COLA.md)
- **C160** — Noticias sin fechas futuras en «24 h». *Prompt: «En Noticias de la Órbita, saca de Últimas 24 h/7 d/30 d las entradas con fecha posterior a hoy y envíalas a una sección Próximas; corrige la cabecera “Órbita 2026-10-27” con la fecha real del último movimiento».*
- **C161** — Semáforo de frescura en Paneles y fechas en JSON manuales. *Prompt: «Añade semáforo verde/ámbar/rojo (≤7, ≤14, >14 días) al pie de cada bloque de Paneles y fecha propia a indicadores-manual.json y liquidez-manual.json».*
- **C162** — Niveles y fallos legibles. *Prompt: «Etiqueta los k vacíos de capas[].xrp en datos.json, explica en una línea los fallos de paneles.json y arregla la divisa NoneUSD de actualizar_paneles.py; unifica la leyenda P/S/D/V/ESP en un pie común».*
- **C163** — Bloque «Mis activos» XRP/XLM en Resumen. *Prompt: «Diseña un bloque XRP/XLM en Resumen con precio y hora, cambio 24 h, stablecoins por cadena, ETF/13F y novedades de la capa, con etiquetas P/S y sin recomendar».*
- **C164** — Pulido de legibilidad: plazos de Voces a 13 px con badge de intención, KPIs con unidades legibles y filtros que solo aparezcan donde actúan. *Prompt: «Sube Plazo a 13 px y márcalo [ESPECULACIÓN], reformatea los KPIs de Resumen (separador de miles, unidad corta, periodo) y oculta los filtros sin efecto por pestaña».*
- **C165** — Anclas internas y «qué cambia hoy». *Prompt: «Añade índice con anclas en Capas, Paneles y Noticias y un resumen de 5 líneas “qué cambia hoy” arriba de Resumen, solo hechos y fechas».*

## 4. Las 2 cosas más urgentes
1. **Noticias «Últimas 24 h» con fechas futuras (C160)**: un hecho de 2027 aparece como noticia del día; es un error de lectura fácil y barato de arreglar. Con él, corregir la cabecera «Órbita 2026-10-27».
2. **Etiquetas de nivel vacías en la capa XRP/XLM y fallos sin explicar (C162)**: es lo que más toca a los activos de Joel y hoy parte de lo dicho no lleva [P]/[S]/[VERIFICAR].

## Limitaciones
- Capturas: el panel solo enseñó ~800 px de ancho; las medidas se tomaron con JS dentro del iframe. Sin modo claro disponible, solo se vio oscuro.
- No se verificó ninguna cifra contra fuentes externas (sesión de lectura); el contraste de transparencias es una estimación.
- Sin números de línea por ser `docs/orbita/index.html` un archivo generado.

## Resumen final (5 líneas)
1. Visualmente sólida: sin desbordes graves, letra ≥13 px (salvo «Plazo» de Voces) y contraste correcto; sin modo claro.
2. Bug de contenido: fechas futuras dentro de «Últimas 24 h» y cabecera «Órbita 2026-10-27» desfasada.
3. Capa XRP/XLM con ~9 afirmaciones sin nivel; fallos de FRED/FMI y `divisa NoneUSD` sin explicar.
4. Faltan semáforo de frescura común, leyenda única de niveles, bloque «Mis activos» y «qué cambia hoy».
5. 14 mejoras (8 P, 6 N) y 6 filas propuestas C160-C165.
