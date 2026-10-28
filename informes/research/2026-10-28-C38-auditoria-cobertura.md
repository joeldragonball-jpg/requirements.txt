# C38 · Auditoría de cobertura: qué sabemos, dónde está y qué falta en la Órbita (incluye C28)

Hecho el 28-oct-2026 sin IA de pago ni web: solo archivos del repo (`informes/`, `explorador/*.json`) y `scripts/revisar_explorador.py`. Sin recomendaciones de compra/venta. [P] = comprobado contra fuente primaria o su dato oficial guardado; [VERIFICAR] = sin confirmar.

## 1. Inventario
- **Informes:** 118 en `informes/research/` (R 50 · T 18 · C 16 · W 10 · D 4 · EV 2 · otros 18: radar v2-v5, auditorías, calendarios); 11 en `informes/gemini/` (T01-T04, D01-D05, W03 ×2, noticias del 27-oct); 7 de vídeos y 33 dossiers.
- **Órbita (`explorador/datos.json`):** 12 capas y 63 movimientos (2023-07-13 a 2026-10-25). Movimientos por capa: CBDC 7, Riesgos 7 (escenarios [ESPECULACIÓN]), Regulación 6, Puente 6, Deuda 6, Energía 6, Liquidez 6, Custodia 5, Fondos 5, Stablecoins 4, Tokenización 4, Depósitos 1.
- **Resto:** radar `regulacion.json` (8 temas × 17 jurisdicciones = 136 celdas; 94 con etapa, 29 sin dato); `voces.json` 50 voces; `valoracion.json` 18 filas; paneles (TIC, stablecoins, RWA, bonos, tipos, liquidez, Ormuz, defensa…); `calificaciones.json` 7 países; `deuda-fmi.json` 14 países; `centro.json` 5 módulos.
- **`revisar_explorador.py` (28-oct):** 0 avisos en 12 capas y 63 movimientos; radar 136 celdas, 29 sin dato.

## 2. Distribución (informe → reflejo en la Órbita → hueco)
| Tema / país | Informes | Órbita hoy | Hueco |
|---|---|---|---|
| EE. UU. regulación | R18, R23, T19, EV-OCC, Gemini T01-T03 | 26 de 63 movimientos con EE. UU.; radar completo | Norma final de la OCC (21-oct, NR 2026-92) solo en el radar, no como movimiento |
| UE / MiCA | T05, R24, Gemini T04 | 5 movimientos; radar | Bien cubierto |
| Asia (Corea, HK, India, China, Singapur) | T07, T09, T10, T14, R04P, R05P, W03 | radar con T07-T14 citados; movimientos: Corea 1, HK 1, China 1, **India 0, Singapur 0** | Investigado pero casi sin movimientos |
| BRICS, Rusia, Brasil, Emiratos | T11-T13, T15, R01P, R03P, R06P | radar; movimientos: Brasil 2, Rusia 2, **Emiratos 0** | Igual que Asia |
| Irán, Egipto, Etiopía, Sudáfrica, Indonesia | W03E, Gemini W03 ×2 | radar parcial: 23 de las 29 celdas sin dato son suyas | Falta research (ETF, custodia, tokenización, fiscal) |
| Organismos (BIS, FMI, FSB) | T16, R08P | ≥4 movimientos; radar | Bien cubierto |
| Deuda soberana | D06-D09, W02, Gemini D01-D05 | 6 movimientos + paneles de bonos, deuda y calificaciones | **D08 (subastas), D09 (calificaciones) y Gemini D01-D05 sin movimiento** |
| DTCC / tokenización | T20, R26 | 2 movimientos (dic-2025, may-2026) | T20 sin reflejo: estado del lanzamiento de oct-2026 y Collateral AppChain |
| Ripple y Stellar (empresa) | R09P, R32-R34, T22, **T23** | Puente 6 movimientos | T23 (licencias y qué nombran del token) sin reflejo |
| Flujos, 13F, derivados | R21, R21b, R42, R49, C06 | 1 movimiento (R21b) | Ninguna capa los recoge |
| Valoración | C04, C26 | panel `valoracion.json` | Bien, como panel |
| Energía y Ormuz | R46, T18, W10 | 6 movimientos | La guerra y la diplomacia van en C29 |
| Noticias (bot y manuales) | EV del 27-oct, Gemini noticias | 0 | Lo cubre C35 |
| Auditorías y sistema | C08-C20, R11P, R12P, R22, R31, R38, R39 | — | No necesitan reflejo |

Sesgo de distribución: 26 de 63 movimientos llevan EE. UU. y 11 no llevan país; los países con informe propio de octubre (T07-T16) apenas aparecen en la línea de tiempo.

## 3. Fallos (calidad, C28)
- **7 movimientos sin «Abrir el informe»:** 6 enlazados hoy (ver Hecho). Queda 1: el bono de EE. UU. a 10 años del 21-oct (5,13 %), que solo tiene la curva del Tesoro guardada en el panel. Está **correcto** frente a `paneles.json` (20-oct 5,12; 21-oct 5,13) [P], pero no hay informe propio.
- **BIS WP 1374 seguía en [S]** aunque el PDF se leyó entero el 23-oct (`verificaciones-pendientes.md`): pasado a [P].
- **8 cifras contrastadas:**
  - 7 coinciden: TEC 10 francés 5,13 % el 22-oct, máximo del mes; FMI 199,4 % y 126,8 % (2026); TIC $9.332 mil M, Japón $1.068 mil M y $1.184 mil M un año antes (serie TIC: 1.183,9); EBA 116 bancos y €3.914 mil M; PortWatch 3,7 barcos/día frente a 78,3; Ripple >$100 mil M (3-mar); licencia CSSF del 6-jul.
  - Dos matices:
    - (a) El movimiento de la Fed y la GENIUS Act («comentarios hasta el 30-nov») enlaza a R08P, que **no trae esa fecha**; la respalda el dossier de stablecoins del 9-oct (Federal Register, publicación del 29-sep frente a la nota de la Fed del 24-sep).
    - (b) En el bono francés, «el diferencial con Alemania se amplía» no tiene serie alemana en el panel [VERIFICAR].
- **Radar:** 23 celdas con etapa y sin `url` (HK 4, Sudáfrica 3, Indonesia 3, EE. UU. 2, Corea 2, India 2, Brasil 2, Irán 2, UE 1, Egipto 1, Etiopía 1), que coinciden con C37. Las 29 celdas sin dato se reparten así:
  - por tema: ETF 9, custodia 5, tokenización 5, fiscal 4, stablecoins 3, política 3;
  - por país: Egipto 6, Irán 6, Etiopía 5, Sudáfrica 3, Indonesia 3, India 2, BRICS 2, Brasil 1, Emiratos 1.
- **Móvil:** los textos más largos de movimientos tienen 255, 246 y 214 caracteres (el n.º 17, BIS y BlackRock). No lo he probado a 375 px: queda para C32.

## 4. Capas y temas propuestos (no creados; por utilidad)
1. **Política y elecciones** (capa nueva): hoy hay 0 movimientos y la política solo vive en el radar. Saldría de C30, más las fechas de `eventos/calendario.toml`.
2. **Inflación (IPC)**: mejor como subgrupo de «Liquidez y tipos oficiales» que como capa propia, porque el IPC explica los tipos. Saldría de C31 y del panel nuevo.
3. **Flujos y posicionamiento** (capa nueva): ETF XRP/XLM, 13F, derivados y washouts (R21, R21b, R42, R49, C06, W04). Hoy no tiene capa, y el 13F del 3T se publica hacia el 14-nov.
4. **Energía, Ormuz y guerra**: renombrar y ampliar la capa de energía con el hilo diplomático (C29), en vez de crear una capa de guerra aparte.
5. **Países en la línea de tiempo** (tema, no capa): movimientos fechados de T07-T16 y W03E, colgados de las capas existentes con su `pais`. Es trabajo de volcado, no de research (fila C39).
6. **Calificaciones y subastas** (tema dentro de Deuda): D08, D09 y Gemini D01-D05, con `calificaciones.json` como fuente estructurada.

## 5. Diseño de lo que viene
**Estructurado frente a narrativo**
- **Estructurado** (deuda, tipos, IPC, calificaciones, reservas, bonos, Ormuz): va como número en `paneles.json`, lo actualiza un script sin IA y conserva el dato anterior si falla. En la Órbita solo entra un movimiento cuando hay un **cambio de nivel**: decisión de tipos, cambio de calificación, máximo del mes, cruce de un umbral.
- **Narrativo** (política, guerra, regulación, voces): solo entra si cumple al menos una de estas condiciones:
  - cambia una conclusión de un informe o de la tesis pública;
  - mueve un precio o un tipo con fecha comprobable;
  - tiene fecha cierta (votación, plazo, entrada en vigor).

  Se descartan los titulares sin dato, las repeticiones (el bot ya lo hace con `umbral_repeticion` y `dias_repeticion`), las cuentas anónimas y las predicciones sin base.

**Ficha mínima por elemento** (campos nuevos opcionales en el movimiento): `hecho` (= `texto`), `fecha`, `fuente` con `url`, `nivel` [P]/[S], `efecto` (en la cartera, una línea), `alcista`/`bajista` (una línea cada uno), `revisar` (24h/7d/30d/fija), `revisado` (fecha) y `caduca` (fecha).

**Capas futuras**
| Capa | Qué lleva | Se cuelga de | Fuente y rutina |
|---|---|---|---|
| Energía, Ormuz y guerra (C29) | Hitos diplomáticos y militares fechados, separando hechos y opiniones, más Brent/WTI antes y después | Energía (ya existe); `pais` Irán, EE. UU., Israel | PortWatch y EIA/FRED (panel Ormuz), prensa [S]; W10 y la rutina de noticias |
| Política y elecciones (C30) | Por país: próxima cita (fecha oficial), qué se vota, situación de partidos, efecto posible en cripto, deuda o energía | Radar (tema `politica`) más `elecciones.json` | Juntas electorales y gobiernos [P], encuestas [S]; revisión semanal (W06 o fila W nueva) |
| Inflación (C31) | IPC interanual y mensual, fecha del dato y próxima publicación | Liquidez y tipos; panel `inflacion` | BLS, Eurostat, INE, ONS, MIC, NBS, IBGE, StatCan; `actualizar_paneles.py` |
| Noticias (C35) | Noticias con nota ≥ 7, con caducidad | La capa de su tema | Bot (`noticias/`) y `noticias/manuales/*.json` |

**Apartado de noticias con caducidad**
- **Frecuencias de revisión:**
  - **24 h:** guerra, Ormuz, mercados, reuniones de bancos centrales. Caduca a las 48 h si nadie la renueva.
  - **7 días:** política, elecciones, regulación en trámite. Caduca a los 14 días.
  - **30 días:** marco legal, deuda, demografía. Caduca a los 60 días.
  - **Fija:** hecho cerrado (sentencia, ley publicada). No caduca.
- **Cómo se sabe que sigue vigente:**
  - Se renueva si una tanda nueva (Gemini del día, pasada ligera de Claude, bot) trae una pieza del mismo tema que la confirma o la actualiza: se cambia `revisado` y se recalcula `caduca`.
  - Pasa a «fija» si se cumple el hecho (votación hecha, norma publicada).
- **Retirada sin borrar:** un script sin IA (dentro de C35, `noticias_a_orbita.py`) mueve las vencidas de `datos.json` a `explorador/noticias-archivo.json` con `estado: "archivada"` y la fecha. La Órbita solo muestra las vigentes y un enlace «Ver archivo».
- **Sin duplicar el bot:** el bot ya filtra por `nota_minima = 7`, duplicados (`umbral_duplicado`), repeticiones a 4 días y enfriamiento por tema a 24 h, y `manuales.py` envía las manuales por Telegram. La caducidad **no** se aplica en el bot: se aplica solo al volcado en la Órbita. El bot sigue decidiendo qué se envía; C35 decide cuánto tiempo se ve.

## 6. Cambios a las tareas previstas
- **W01B (29-oct):** añadir como movimientos de Liquidez las decisiones de la Fed, Canadá, el BCE y el Banco de Japón (`informe` = el de W01B, `revisar: fija`), y actualizar `tipos_vivos`. Enlazar ahí también el bono de EE. UU. del 21-oct, que no tiene informe.
- **C29:** renombrar la capa a «Energía, Ormuz y guerra» y usar la ficha mínima con `revisar: 24h` para los hitos diplomáticos. Ya existen 6 movimientos y el panel Ormuz: aportar solo hitos nuevos y la marca de precio.
- **C30:** el radar ya tiene 14 de 17 celdas de política con dato, así que C30 aporta las fechas electorales y la capa nueva. Faltan las 3 celdas vacías de política (Egipto, Etiopía e Irán), que irán con `revisar: 7d`.
- **C31:** el IPC va como subgrupo de Liquidez (no como capa propia). Movimientos solo cuando el dato cambia de tendencia o sorprende frente a la anterior publicación.
- **C32:** probar a 375 px los 3 textos largos señalados y los desplegables nuevos de C29-C31.
- **C33:** usar la tabla de distribución de este informe como lista de control semanal.
- **C35:** añadir el diseño de caducidad (campos `revisar`, `revisado`, `caduca`, archivo `noticias-archivo.json`) y un tope de unas 5 noticias vigentes por capa.
- **C36:** cada pieza manual nueva lleva `revisar` según su tema, para que C35 la vuelque con caducidad.
- **Filas nuevas en la cola:**
  - **C39:** volcado a la Órbita de lo ya investigado (países T07-T16 y W03E, T20, T23, D08, D09, Gemini D01-D05, norma OCC). Sin research nuevo.
  - **C40:** research de las jurisdicciones fuera del radar (Reino Unido, Suiza, Canadá, Australia, Arabia Saudí). Son huecos anotados en `regulacion.json` que ninguna tarea cubre.

## 7. Hecho hoy
- `explorador/datos.json`: campo `informe` añadido a 6 movimientos (bono francés → W02; FMI WEO → W07-fuentes; TIC → D07; EBA → D06; BIS 1374 → verificaciones-pendientes; BlackRock → vídeos 22-oct). Fuente del BIS 1374 cambiada de [S] a [P]. Sin borrar nada. `revisar_explorador.py`: 0 avisos.
- Filas C39 y C40 en `research/COLA.md`, con su prompt en `research/prompts/`. C28 ya figuraba como «absorbida en C38».
