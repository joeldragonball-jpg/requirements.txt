# C150 · Auditoría de valoración: contenido y estética (7-nov-2026)

Sesión de solo lectura. Contexto previo leído: `graphify-out/GRAPH_REPORT.md` (cabecera, 4-nov), C134 y C127 (solo pendientes). No se repiten sus hallazgos cerrados (tabla de bonos ancha, 64 voces con 3-4 etiquetas, texto de 8-9 px en el tablero, noticias en 3 columnas, matriz país×tema con «—»).

## Resumen (5 líneas)
1. La app móvil está bien en lo visual: sin desbordes a 375 px, sin texto < 11,5 px y contraste ≥ 4,5:1 en oscuro (comprobado por script en las etiquetas pequeñas). No hay problemas graves de estética nuevos.
2. El mayor riesgo es de **contenido**: datos congelados o desfasados que se muestran sin alarma clara (Ormuz parado en 25-oct; Brent futuro 97,8 $ frente a spot EIA 120,2 $).
3. Hay un movimiento de mercado gordo (Nikkei −5,96 %, Kospi −6,02 % el 6-nov) que la app resalta como «lo que más se mueve» pero **no explica** (11 de 20 noticias sin «por qué importa»).
4. Cobertura frente a la visión: XRP/XLM solo tienen precio; faltan pantallas de actividad de red/ETF y de la tesis; las voces están concentradas en DTCC.
5. Hay 6 arreglos pequeños (<30 min) y 4 tareas nuevas propuestas (C150+).

## 1. Hallazgos de contenido

| # | Hallazgo | Dónde | Etiqueta |
|---|---|---|---|
| a | **Ormuz congelado**: último dato 2026-10-25 (2 barcos, 1 petrolero) frente a media de febrero de 78/día. El aviso ámbar dice «hace N días» pero el texto dice que la fuente «dejó de responder el 4-nov»: dos fechas distintas (25-oct vs 4-nov) en la misma tarjeta. Está dentro de un `<details>` cerrado («Más datos»). | `docs/movil/index.html:360`; `data.json → ormuz.ultimo` | HECHO (fecha del JSON) |
| b | **Dos Brent que se contradicen**: futuro Yahoo 97,76 $ [S] (6-nov) y spot EIA 120,15 $ [P] (30-oct) — 22 $ de diferencia. La nota del spot está escondida en el detalle de la fila; en la pantalla principal solo se ve 97,8 $. Puede ser contango/backwardation o ruido de contrato, no se explica. | `data.json → mercado grupo Energía`; tarjeta «Brent» de Hoy | [VERIFICAR] causa |
| c | **Nikkei −5,96 % y Kospi −6,02 % en un día, VIX −9 %** (a la vez, señales opuestas: caída asiática fuerte y VIX bajando). Sin explicación en la app; «Centro de control» solo lo menciona. Puede ser dato de cierre desfasado por zona horaria (Yahoo). | `data.json → mercado Bolsas` | [VERIFICAR] antes de leerlo como pánico |
| d | **Etiqueta «cotiza en ?»** en Euro Stoxx 50 (moneda vacía); chocante en un panel que presume rigor. | `scripts/construir_movil.py:445` (`x.get('moneda') or '?'`) | Bug |
| e | **11 de 20 noticias sin «por_que»** (campo vacío). Titular sin dato ni relevancia; hay mezcla de hecho y opinión: «Daly (Fed): más subidas de tipos probables» es una opinión de una persona, no una decisión. Además contradice el ruido de «tipos 3,75–4,00 %, último cambio 17-sep» sin contexto. | `data.json → noticias`; pantalla Hoy/Noticias | Opinión vs hecho |
| f | **Fed: valor 4,0 con rango 3,75–4,00 %**: la tarjeta muestra el rango, pero la fila usa 4,0 (EFFR) como valor. Dos números distintos para «el tipo». | `data.json → Divisas y tipos`, «Tipo oficial · Reserva Federal» | Aclarar |
| g | **Ratios de valoración con periodos mezclados** (TTM a 27-sep vs 30-sep, etc.) y PER sin contexto de sector; ya avisa «periodos mezclados» pero la tabla vive plegada y sin fecha por fila. Riesgo: lectura como señal de compra/venta. | `index.html:364`; `data.json → valoracion.filas[].periodo` | Sesgo de lectura |
| h | **M2 China [S]** es de prensa (Xinhua/China Daily), no del PBoC; viene marcado [S], bien, pero se dibuja con la misma barra que M2 Japón [P]. Sin diferencia visual de nivel. | `data.json → liquidez.manual.cn` | Etiqueta correcta, visual igual |
| i | **Voces concentradas**: las 5 primeras de 20 son DTCC / Frank La Salla (CEO) con conflicto de interés evidente (promoción de su servicio de tokenización) y relacionadas con XLM. Se marcan «confirmada» (que lo dijeron) pero no hay contrapeso crítico ni de reguladores. | `data.json → voces`; `explorador/voces.json` | Sesgo de fuente |
| j | **Inconsistencia de leyenda**: `niveles` en data.json define P/D/S (3 niveles), pero los pies de pantalla solo explican «[P] oficial · [S] agregador»; la «D» no aparece en CLAUDE.md. | `index.html:552, 596`; `data.json → niveles` | Consistencia |
| k | **Frescura heterogénea sin semáforo común**: `calificaciones` (22-oct), `reservas` (22-oct), `deuda-fmi` (21-oct), `cbdc` (29-oct), `rwa-por-cadena-manual` (29-oct), `paises/estabilidad/espana-presupuesto` (30-oct) llevan 8-17 días sin releer; solo hay aviso ámbar en 1 caso (calificaciones). `indicadores-manual.json` y `liquidez-manual.json` **no tienen ninguna fecha**. | `explorador/*.json` | Sin fecha |
| l | **Fallos silenciosos en indicadores**: `indicadores-historia.json → fallos` incluye «US/pobreza: sin datos», «JP/pobreza», «BR/pobreza», «IR/pobreza», «AE/pobreza», «CU/ipc»…; el tablero lo muestra como hueco sin explicar. | `explorador/indicadores-historia.json` | Hueco |
| m | **Fechas futuras lejanas en datos** (2027-2031) en `seguimiento.json`/`voces.json`/`regulacion.json`: son plazos prometidos (p. ej. DTC en Stellar, 1.er semestre 2027); correcto, pero conviene que el UI los marque siempre como [ESPECULACIÓN]/intención, no hecho. | `seguimiento.json`, `voces.json → plazo` | Intención |

### Huecos de cobertura frente a la visión
- **XRP/XLM**: solo precio, capitalización y variación (`mercado`); existe `onchain.py`, pero la app móvil solo lo menciona 2 veces. Falta: actividad de red, ETF/flujos, estado regulatorio específico resumido, y la tesis (privada, no al repo) → hoy el usuario no ve «qué ha cambiado para mis dos activos».
- **Macro/países**: bien cubiertos (IPC, tipos, bonos, calificaciones, elecciones). Falta un resumen único «qué cambia hoy» (C127/C134 ya lo señalaron para Resumen; sigue sin hacerse).
- **España a fondo**: muy cubierta (presupuesto, deuda, pagos, mortalidad, judicial). Falta vincular el IPC España (4,9 % en oct, bajando de 5,0 %) con vivienda, salarios y Euríbor 12 m (3,24 %) en una sola lectura. La luz (OMIE 232,6 €/MWh; PVPC 205,6) está, pero sin histórico en la pantalla principal.
- **Precios cotidianos / chips-IA**: existen (Alimentos, Chips), pero escondidos en «Paneles de datos» sin índice (hallazgo C134 aún abierto).

## 2. Hallazgos de estética y usabilidad

Probado en `docs/movil/` con servidor local, 375×812 claro y oscuro, y escritorio (la app, no el tablero Órbita; el tablero no se auditó con captura por tiempo).

Bueno:
- Hoy: jerarquía clara (cuadrícula de 9 mini-tarjetas → «Lo más importante ahora» con cuenta atrás → racha/plan/verificaciones → rutinas). Cifras grandes y legibles; rojo/verde solo donde sube/baja tiene sentido.
- Sin desbordes horizontales (0 elementos con overflow) ni texto menor de 11,5 px en la vista Mercado.
- Modo oscuro: 0 pares texto/fondo bajo 4,5:1 en etiquetas pequeñas. El borde ámbar de «De un vistazo» destaca bien.

A mejorar:
1. **Cuadrícula de 9 tarjetas en Hoy**: todas pesan lo mismo (XRP, IPC EE. UU., Fed…). Nada separa «mis activos» (XRP/XLM) de contexto macro. Tiempo hasta lo importante: bueno, pero XRP/XLM merecen un bloque propio.
2. **Subtítulos con tres fuentes mezcladas** («a 05/11», «antes 5,0 · oct», «24 h»): cada tarjeta usa una convención distinta de fecha/variación; el pie explica la clave en un párrafo de 3 líneas que casi nadie lee.
3. **IPC EE. UU. 3,7 % con «sep»** mientras el evento «lo más importante» es la publicación de octubre en 3 días: bien, pero no se enlaza el evento con la tarjeta (tocar la cuenta atrás no lleva a ella).
4. **Mercado**: lista larguísima y uniforme (cada fila = 1 tarjeta de ancho completo; 17 bolsas + 5 ETFs + energía + alimentos + metales + divisas); `body.scrollHeight` real mucho mayor que la pantalla, sin índice ni anclas por grupo. Cada fila repite «sesión 6-nov · 1 día · [S] Yahoo Finance»: ruido repetido ×40.
5. **Ormuz, liquidez, inflación y valoración** viven en un `<details>` «Más datos…» cerrado por defecto: lo más contextual (Ormuz, con su alarma ámbar de dato congelado) queda oculto.
6. **Etiquetas de nivel**: [S] en gris pequeño no se distingue de [P] a simple vista; la distinción fiable/no fiable es un objetivo central y se pierde (sugerencia: punto de color o borde).
7. **Tarjetas de «Calificaciones»** usan cuadrícula de 4 columnas fija (`grid-template-columns:1.3fr 1fr 1fr 1fr`, `index.html:513`): a 375 px los códigos tipo «Baa1/AA−» pueden apretarse; no comprobado con capturas.

## 3. Mejoras priorizadas (impacto/coste)

Leyenda: **P** = arreglo pequeño (<30 min), **N** = tarea nueva.

| # | Mejora | Archivo / sección | Tipo |
|---|---|---|---|
| 1 | Poner el aviso de dato congelado de Ormuz fuera del `<details>` (banner en Hoy) y unificar fecha (25-oct vs 4-nov) | `index.html:360`; `actualizar_paneles.py:635` | P |
| 2 | Corregir «cotiza en ?» (Euro Stoxx: moneda EUR fija si falta) | `scripts/construir_movil.py:445` | P |
| 3 | Explicar o marcar [VERIFICAR] el −6 % de Nikkei/Kospi con VIX −9 % (¿cierre desfasado?); mostrarlo junto a «Lo que más se mueve» | `data.json → mercado`; Centro de control | P |
| 4 | Mostrar en la fila del Brent futuro la nota «spot EIA 120,15 $ [P] (30-oct)» visible, no oculta, con aviso de diferencia | `construir_movil.py` (grupo Energía) | P |
| 5 | Rellenar «por_que» en las 11 noticias vacías o ocultar las que no lo tengan; separar «opinión» (Daly) de «hecho» con etiqueta | `data.json → noticias`; `noticias_a_orbita.py` | P/N |
| 6 | Añadir fecha a `indicadores-manual.json` y `liquidez-manual.json` y semáforo de frescura común (verde ≤7 d, ámbar ≤14, rojo >14) para todos los JSON de explorador | `explorador/*.json`; UI | N |
| 7 | Bloque propio «Mis activos» (XRP/XLM) en Hoy, con actividad de red/ETF/regulación [P/S] y qué cambió desde ayer | `index.html` (Hoy); `onchain.py` | N |
| 8 | Índice/anclas por grupo en Mercado y «Paneles de datos» (Bolsas, Energía, Alimentos…); fila compacta con fuente una sola vez por grupo | `index.html:367`; `construir_movil.py` | N |
| 9 | Diversificar voces: límite de 3 por entidad en la vista móvil y añadir contrapeso (reguladores, críticos) con etiqueta de conflicto de interés | `explorador/voces.json`; `data.json → voces` | N |
| 10 | Unificar leyenda P/D/S en todos los pies y distinguirla visualmente (punto/borde) | `index.html:552, 596`; `data.json → niveles` | P |
| 11 | Aclarar Fed: mostrar «objetivo 3,75–4,00 % · efectivo 4,0 %» en lugar de valor único | `construir_movil.py` (Divisas y tipos) | P |
| 12 | Enlazar la cuenta atrás «Inflación EE. UU.» con la tarjeta IPC y con el último valor/previsto | `index.html` (Hoy) | P |
| 13 | Explicar los huecos de `indicadores-historia.fallos` (pobreza, IPC Cuba) en el tablero como «sin dato en la fuente», no vacío | `indicadores-historia.json`; tablero | P |
| 14 | Marcar siempre [ESPECULACIÓN]/«plazo prometido» las fechas 2027-2031 (DTCC-Stellar, etc.) | `voces.json → plazo`; UI | P |
| 15 | Resumen «qué cambia hoy» (5 líneas) arriba de Hoy, apoyado en datos, sin recomendar | `index.html`; nuevo bloque | N |

### Filas propuestas para `research/COLA.md` (no se ha editado la COLA)
- **C150** — Banner y fecha única de Ormuz fuera de «Más datos» + aviso Brent futuro vs spot EIA visible. *Prompt: «Saca el aviso de dato congelado de Ormuz al banner de Hoy, unifica 25-oct/4-nov y muestra la nota del spot EIA junto al Brent futuro en la fila de Energía».*
- **C151** — Corregir «cotiza en ?» y explicar el −6 % Nikkei/Kospi. *Prompt: «Arregla moneda vacía en Euro Stoxx (construir_movil.py:445) y verifica con 2 fuentes el cierre de Nikkei y Kospi del 6-nov; añade [VERIFICAR] si no cuadra».*
- **C152** — Noticias sin «por_que»: rellenar u ocultar. *Prompt: «Rellena el campo por_que de las 11 noticias vacías o ocúltalas, y etiqueta opinión vs hecho».*
- **C153** — Semáforo de frescura común y fechas en JSON manuales. *Prompt: «Añade fecha a indicadores-manual.json y liquidez-manual.json y un semáforo verde/ámbar/rojo para todos los JSON del explorador».*
- **C154** — Bloque «Mis activos» XRP/XLM en Hoy. *Prompt: «Diseña un bloque XRP/XLM con precio, actividad de red (onchain.py), ETF y regulación con etiquetas P/S, sin recomendar».*
- **C155** — Índice y anclas en Mercado/Paneles, fuente una vez por grupo. *Prompt: «Añade anclas por grupo y compacta las filas repetidas en la vista Mercado móvil y Paneles de datos».*
- **C156** — Equilibrar voces (máx. 3 por entidad, contrapeso, conflicto de interés). *Prompt: «Limita DTCC a 3 voces en móvil y añade 3-5 voces críticas o de reguladores sobre tokenización con etiqueta de conflicto de interés».*
- **C157** — Leyenda P/D/S unificada y visual. *Prompt: «Unifica los pies y la leyenda P/D/S en index.html con un indicador visual distinto para [S]».*

## 4. Las 2 cosas más urgentes
1. **Ormuz congelado + contradicción Brent futuro/spot (C150)**: son dos datos de energía/geopolítica que pueden llevar a una lectura equivocada y ahora están escondidos o sin contexto.
2. **Explicar o marcar [VERIFICAR] el movimiento de Nikkei/Kospi (C151) y arreglar «cotiza en ?»**: es lo primero que ve el usuario en «Lo que más se mueve» y no se puede leer sin contexto.

## Limitaciones
- Capturas: solo se vieron Hoy/Mercado a 375 px (claro y oscuro) y no se auditó la Órbita de PC con captura; las observaciones sobre Calificaciones y desktop son de código/estructura, no visuales.
- No se verificaron externamente cifras (fuentes no consultadas en esta sesión de solo lectura).

## Resumen final (5 líneas)
1. App móvil visualmente sólida (sin desbordes, contraste correcto en oscuro, cifras legibles).
2. Riesgo principal: datos congelados o contradictorios (Ormuz 25-oct; Brent 97,8 $ vs 120,2 $).
3. Movimiento Nikkei/Kospi ≈ −6 % sin explicar; 11/20 noticias sin «por qué importa».
4. Huecos: XRP/XLM solo con precio, voces concentradas en DTCC, resumen «qué cambia hoy».
5. 15 mejoras (10 pequeñas, 5 tareas nuevas) y 8 filas COLA propuestas (C150-C157).

## Nota del revisor (sesión principal, 7-nov) — dos matices tras comprobar con los datos

- **Hallazgo b (Brent futuro 97,8 $ frente a spot 120,15 $):** la diferencia de 22 $ **no es una contradicción real**: compara el spot del 30-oct con el futuro del 6-nov. Con las mismas fechas, el spot EIA [P] del 3-nov es 107,03 $ y el futuro del 3-nov 103,6 $ (diferencia de 3 a 4 $; 6,7 $ el 30-oct). La prima física es real (la AIE vio el Dated en 134 $ el 14-oct) pero la tarjeta debe comparar **misma fecha**. Ver `2026-11-07-W10-energia.md` y la tarea C147.
- **Hallazgo c (Nikkei −5,96 % y Kospi −6,02 % el 6-nov):** **sí está documentado**: R00 de apertura del 6-nov (`informes/2026-11-06-apertura.md`) lo recoge como segunda sesión seguida de ventas (Kospi −11,0 % y Nikkei −7,6 % desde el 4-nov) tras el −4,4 % de Wall Street del 5-nov [S, Yahoo]; la causa sigue sin verificar. El VIX −9 % es de la sesión de EE. UU. del 6-nov (otra sesión), no es una señal opuesta en el mismo momento. Falta mostrar esa explicación en la app (C152).
- Las filas propuestas C150-C157 se registran como **C151-C158** (C150 es este informe).
