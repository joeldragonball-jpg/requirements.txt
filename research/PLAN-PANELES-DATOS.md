# Plan de paneles de datos para el Explorador y el cerebro (21-oct-2026)

Objetivo (Joel): que la información sea más completa y más visible, con tablas como la del radar regulatorio, aprovechando lo ya verificado y completando solo lo que falte. Informativo, sin recomendaciones. Cada panel: tabla por país o activo, fecha y fuente de cada dato, etiqueta [P]/[S]/[VERIFICAR], y enlace al glosario.

## Comprobado hoy: qué datos abiertos se pueden bajar sin IA y gratis (curl, 21-oct-2026)
| Fuente | Resultado | Uso |
|---|---|---|
| DefiLlama `stablecoins.llama.fi/stablecoins` (JSON) | 200, en vivo: USDT 182,9 MM$, USDC 72,2 MM$, USDS 6,8, DAI 4,7 | Panel de stablecoins (cuota, cadena, emisor) [S: agregador] |
| Tesoro EE. UU. TIC, Tabla 5 `ticdata.treasury.gov/.../slt_table5.txt` | 200, datos hasta **ago-2026** (publicación con ~6-7 semanas de retraso): Japón 1.068,3 MM$ (1.239,3 en feb), Reino Unido 1.009,5, China continental 590,7 (695,3 en ene) | Panel de quién tiene deuda de EE. UU. [P] |
| Banco Mundial API `api.worldbank.org` | 200, pero la serie de deuda de ejemplo salió casi vacía (775 bytes) | Posible para deuda/PIB; hay que elegir otro indicador |
| FMI DataMapper API | 403 con curl | Probar Chrome o la descarga del WEO en CSV |
| FRED (CSV público) | sin conexión con curl | Alternativa: ECB, bancos centrales, Tesoro (curvas oficiales) |
| Bancos centrales (tipos oficiales) | cada uno en su web; ya hay 14 celdas de «política monetaria» en el radar (`dir` y `valor`) | Panel de tipos |

## Lo que ya tenemos verificado y se puede reutilizar
- **Stablecoins:** dossier del 9-oct (cuotas DefiLlama, RLUSD 2.466 M$, 1.140 M$ en el XRPL), radar (columna stablecoins por país), R25.
- **CBDC y redes de pago:** R40 (por país), R08P (Agorá, mBridge), radar (columna CBDC), informe Hangang.
- **Tipos de interés:** R29 (Fed, BCE, BoJ, PBoC, Rusia, RBI), R41 (Fed: IORB 3,90 %, balance, TGA, 10 años), radar (columna política monetaria con dirección y valor).
- **Deuda y liquidez:** R41 (balance de la Fed 6.755,6 MM$, reservas 3.022,1 MM$, TGA 885,8 MM$, 10 años 5,09 % el 16-oct).
- **Glosario:** R16 (ampliado el 19-oct, con CBDC, mBridge, Agorá, MiCA, GENIUS, 13F, etc.).

## Huecos (no hay nada verificado todavía)
- Deuda pública por país (deuda/PIB, déficit) y rendimientos a 10 años comparados.
- Quién compra y vende deuda de otros países: solo EE. UU. tiene serie abierta mensual (TIC). Para Japón, China y la zona euro hay que buscar fuentes (MoF de Japón, SAFE y PBoC, BCE/Eurostat, COFER del FMI).
- Reservas de los bancos centrales (oro, dólares): FMI COFER, World Gold Council. Sin leer.
- Tabla de las stablecoins «top» con red, regulador, reservas y última atestación.

## Paneles propuestos (orden sugerido)
| # | Panel | Contenido | Datos | Esfuerzo | Riesgo / límite |
|---|---|---|---|---|---|
| 1 | **Deuda de EE. UU.: quién la tiene** | Top 15 tenedores extranjeros, variación 12 meses, gráfico de línea Japón/Reino Unido/China | TIC Tabla 5 (oficial, gratis, `scripts/` sin IA) | Bajo | Mide **custodia**, no propietario final (Bélgica, Luxemburgo, Caimán); incluye cambios de valoración; retraso de ~7 semanas; no son flujos de compra/venta |
| 2 | **Stablecoins: top y cuota** | Top 10 por emisor, cadena, cuota, variación, regulador y estado en el radar | DefiLlama (agregador) + reservas de las páginas del emisor | Bajo-medio | Agregador [S]; reservas y atestaciones requieren leer cada emisor |
| 3 | **Tipos de interés por país** | Tipo oficial, dirección, próxima reunión, fecha del último cambio | Radar (14 celdas) + calendario ya en el repo; datos de cada banco central | Bajo (ya está en parte) | Mantenerlo al día en cada reunión; solo 14 países |
| 4 | **Deuda pública por país** | Deuda/PIB, déficit, rendimiento a 10 años, calificación | FMI WEO (CSV), BCE/Eurostat, Tesoro; hace falta research | Medio | FMI da 403 a curl: usar Chrome o CSV descargado a mano; los rendimientos «de agregador» son [S] |
| 5 | **Quién compra y vende deuda (resto del mundo)** | Japón, China, UE: tenencias de bonos de otros países y reservas | MoF Japón, SAFE/PBoC, BCE, COFER | Alto (research) | Datos escasos y con retraso; muchas cifras serán [S] |
| 6 | **CBDC y redes de pago por país** | Etapa, red (mBridge, Agorá, UPI, SPFS), participantes | R40, R08P + radar | Medio | Parte [S] (mBridge) |
| 7 | **Glosario visible** | Cada término con definición corta, capa del Explorador y enlace a la celda o panel | R16 + palabras clave de `datos.json` | Bajo | Mantenerlo al ampliar paneles |

## Cómo mostrarlo
- Un nuevo botón «Datos» junto al radar en el Explorador (`explorador/mapa.html`), con las tablas en el mismo estilo que el radar (cuadrícula país × columna, ficha al pulsar, etiqueta [P]/[S], fecha de cada dato).
- Los datos viven en archivos JSON propios (`explorador/datos-tenedores.json`, `datos-stablecoins.json`, `datos-tipos.json`, `datos-deuda.json`), generados por un script sin IA (`scripts/actualizar_paneles.py`) y revisados por `scripts/revisar_explorador.py`.
- Actualización: manual al principio (un comando, sin API de Anthropic). Más adelante, un workflow como los de `eventos.yml`, sin coste de IA.

## Reglas de calidad
- Cada dato lleva fuente, fecha del dato y fecha de lectura. Lo que viene de un agregador va [S].
- Separar HECHOS (tabla oficial) de LECTURAS (por qué cambia). Sin recomendaciones.
- No presentar custodia como propiedad ni tenencias como flujos de compra o venta.
- Repo público: nada de la tesis de Joel; solo datos públicos.
