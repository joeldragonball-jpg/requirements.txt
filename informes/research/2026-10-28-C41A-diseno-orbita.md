# C41A · Diseño de la Órbita para ordenador: cómo se ve, cómo se organiza y cómo se recoge la información

Hecho el 28-oct-2026 con Opus. Sin IA de pago ni cambios en la Órbita ni en los datos reales: solo este informe y 2 maquetas con datos de ejemplo. Las páginas se renderizaron con `explorador.py`, `mundo.py` y `paneles.py` (datos al 28-oct) y se vieron en el navegador integrado a 1920×1080, 1600×900 y 1180×820 (tablet). [P] = visto hoy; [VERIFICAR] = no abierto hoy.

## 1. Lo que hay
**`mapa.html` (Órbita).** 12 capas giran alrededor de «Dinero y liquidación». Arriba están el calendario de 120 días, la línea de tiempo, el buscador y los botones Voces, Panel y Vista general.
- **Funciona:** la estética invita a explorar; cada capa tiene «Qué hace», «Quién la controla», a favor y en contra (hechos), cifras clave con fecha y «Qué vigilar»; el panel lateral trae voces y datos al día (bonos con tabla y variación).
- **Estorba:**
  - (1) El **giro continuo**: los clics fallan si no se pausa antes.
  - (2) **Texto pequeño**: 108 textos a 11 px, 149 a 12 px y 41 a 10,5 px; las etiquetas de las capas son ilegibles en tablet.
  - (3) **Tarjetas superpuestas**: al abrir una capa, unas 20 tarjetas flotan sobre la órbita; 11 cajas cortan el texto con «…», por ejemplo las cifras clave («Ministerio de Finanzas de…») y «Qué vigilar».
  - (4) **No hay comparación**: para saber «qué países tienen X» hay que abrir capa por capa.
  - (5) **La jerarquía** no dice qué cambió hace poco ni qué está caducado.

**`mundo.html` (mapamundi).** Cuadrícula de 21 países y organismos con puntos por tema y filtros de periodo, tema y nivel (P/S/VERIFICAR). Es lo más cercano a una vista por país.
- **Problemas:** cuenta **eventos** (EE. UU. 78, Rusia 35) y no **estado**; los puntos no se leen; la lista del país sale debajo, fuera de pantalla. Egipto, Suiza e Indonesia aparecen con 0.

**`paneles.html`.** 9 pestañas (deuda de EE. UU., bonos, reservas, stablecoins, tipos, mercado y RWA, glosario…) con tablas ordenadas, barras, sparklines y fuente con fecha.
- **Valoración:** es la página **más útil y más legible**: es el patrón a extender.

## 2. Referencias (consultadas el 28-oct-2026)
| Web | Patrón | Qué copiar | Qué no | Para qué uso de Joel |
|---|---|---|---|---|
| [Atlantic Council, Crypto Regulation Tracker](https://www.atlanticcouncil.org/programs/geoeconomics-center/cryptoregulationtracker/) [P] | 75 países; estado legal en 3 niveles (legal, prohibición parcial, prohibición general) y categorías regulatorias | Pocas etapas y bien definidas por país; texto de método arriba | Portada de vídeo a pantalla completa y desplazamiento lento | Vista país × tema |
| [FRED, DGS10](https://fred.stlouisfed.org/series/DGS10) [P] | Ficha de serie: unidades, frecuencia, «actualizado» y **próxima publicación** en la cabecera | La cabecera de metadatos en cada ficha (actualizado / próxima revisión / fuente) | — | Noticias con caducidad y paneles |
| [DefiLlama](https://defillama.com/) [P] | Menú lateral por tipo de dato, cifras clave arriba y tablas ordenables debajo; barra de cadenas como filtro | Filtro rápido por red o activo; tablas largas con columnas de variación | Saturación de anuncios y menús | Rendimientos y colateral (TVL, yields) |
| [Our World in Data, grapher](https://ourworldindata.org/grapher/life-expectancy?tab=table) [P: abre, gráfico no cargó] | Misma serie en pestañas Mapa / Tabla / Gráfico; fuente y nota al pie | Las pestañas Mapa / Tabla / Línea de tiempo sobre los mismos datos | — | Cambiar entre Órbita, mapamundi y matriz |
| [Finviz, mapa de mercado](https://finviz.com/map.ashx) [P: carga; sin captura] | Mapa de calor denso por sector | Color = estado y tamaño = peso, sin texto superfluo | Densidad extrema | Semáforo de la matriz |
| Koyfin [VERIFICAR] | Paneles configurables y tablas con columnas elegidas | Guardar vistas («mis 10 países») | Requiere cuenta | Seguimiento a largo plazo |
| TradingView [VERIFICAR] | Línea de tiempo con marcas de eventos sobre el precio | Marcar los movimientos de la Órbita sobre el precio de XRP o del Brent (ya pedido en C29) | Ruido de ideas de usuarios | Noticia ↔ precio |
| Messari / Glassnode [VERIFICAR] | Perfil de activo con secciones fijas (gobernanza, emisión, riesgos) | La ficha con secciones fijas por país | Muro de pago | Ficha de país |
| Reuters Graphics / FT [VERIFICAR] | Cronologías verticales con fecha a la izquierda y texto corto | La línea de tiempo vertical como alternativa a las tarjetas flotantes | — | Guerra y Ormuz, política (C29, C30) |
| Bloomberg (terminal, tabla WIRP/ECO) [VERIFICAR] | Tablas monoespaciadas, densas, con fecha y próxima cita | Columnas «último», «anterior», «próxima» | Estética de terminal | Tipos, IPC, elecciones |

## 3. Vista por país (maqueta 1)
Matriz de **países (filas) × temas (columnas)**:
- **Temas:** los 8 del radar más **Legal de uso**, **Rendimientos** y **Colateral**, que son nuevos.
- **Celda:** color = etapa 0-5 (la escala que ya usa `regulacion.json`); textura = certeza (liso [P], rayado [S], borde discontinuo [VERIFICAR]); punto = cambio en 30 días; «sin research» con borde gris.
- **Filtros:** cambios en 30 días, solo [P] y revisión vencida.
- **Ficha al hacer clic:** hecho, fecha, fuente con url, qué falta, efecto en cartera, alcista y bajista, informes y «Ver en la Órbita». La Órbita queda como segunda vista (historia y relaciones).
- **Datos:** casi todo existe ya en `regulacion.json` (136 celdas con `etapa`, `fecha`, `fuente`, `url`, `falta`, `proxima`, `informes`). Faltan las 3 columnas nuevas y el campo `revisar`.

**Rendimientos y colateral (maqueta 2).** Una tabla por modalidad: staking, lending CeFi, lending DeFi, AMM en XRPL, préstamo con garantía cripto, colateral tokenizado y letras tokenizadas. Columnas: activo, dónde (tipo), jurisdicción, estado legal (del radar), tasa o ratio con fecha, riesgo principal, fuente y certeza. Solo hechos: no dice dónde operar. La alimentarían W04, R43, R44 y una fila nueva de research (C42).

## 4. Estructura de los datos y facilidad de recogida
- **Archivos grandes:** `regulacion.json` 170 KB, `datos.json` 113 KB, `bancos-eba.json` 110 KB, `voces.json` 52 KB, `paneles.json` 49 KB. Ninguno debe leerse entero: hoy cada consulta empieza por descubrir el esquema con Python.
- **Campos incoherentes entre archivos:**
  - País: `pais` (lista de nombres en español, datos.json), `jur` (códigos `kr`, `eeuu`; radar y tipos), `id` (ISO3 `USA` en bonos y deuda), `clave` (inglés `Japan` en TIC).
  - Nivel: dentro del texto de `fuente` («[P]»), en `k`/`n` (capas), en `fuente: "P"` (radar) o en `nivel` (paneles, voces).
  - Fecha: `fecha`, `leido`, `dato_de`, `revisado`, `generado`, `cuando`.
  - Otros: los movimientos no tienen `url` (solo `informe`); `revisar` y `caduca` no existen en ningún archivo (solo `proxima` en el radar).
- **Índices:** `cerebro/documentos/indice-investigacion.md` cubre **30 de 118** informes (los 3 más recientes de 10 temas). `buscar_informes.py` busca texto, pero no sabe en qué JSON está un dato. **No hay índice de datos.**
- **Medición** (estimada a partir de lo que costó C38 hoy):

| Tarea | Hoy | Con índice y esquema común |
|---|---|---|
| «Resume Corea» | 6-8 lecturas: radar (jur `kr`), datos (`pais` «Corea del Sur»), paneles (`KOR`/`kr`), voces, T07, R05P y calendario; unos 20-25 mil tokens | 2 lecturas: ficha generada `indice/pais/kr.json` más 1 extracto de informe; unos 5-7 mil |
| «Qué cambió esta semana en regulación» | 4-5 lecturas (radar por `revisado`, datos por `fecha`, `ls informes`, manuales); unos 10-15 mil | 1 lectura: `indice/cambios-7d.json`; unos 3 mil |
| «Países con ETF aprobado» | 2-4 (aprender el esquema y la escala, luego filtrar); unos 6-10 mil | 1: `indice/tema/etf.json`; unos 2 mil |

## 5. Propuestas (por utilidad y esfuerzo)
| # | Tipo | Qué | Por qué | Esfuerzo | Riesgo |
|---|---|---|---|---|---|
| 1 | Datos | **Índice generado** (`scripts/indice_datos.py` → `explorador/indice/`): por país, por tema y cambios a 7 y 30 días, más `INDICE.md` «dato → archivo → campo» | Reduce cada consulta de unas 6 lecturas a 1-2 | M | Bajo (solo lectura) |
| 2 | Datos | **Esquema común** en campos nuevos (sin renombrar los viejos): `pais_id` (ISO2), `nivel` (P/S/V), `fecha`, `url`, `revisar`, `revisado`, `caduca` | Base de la matriz, la caducidad y el índice | M | Medio: tocar generadores; hacerlo por capas |
| 3 | Visual | **Vista país × tema** (maqueta 1) como pestaña nueva junto a la Órbita | Responde «qué países ya tienen X» de un vistazo | M | Bajo |
| 4 | Visual | **Giro desactivado por defecto** y botón «Girar» | Evita clics fallidos | S | Nulo |
| 5 | Visual | **Texto mínimo 13 px** y tarjetas de capa en **columna lateral** en vez de flotantes; quitar el «…» de cifras y «Qué vigilar» | Legibilidad en tablet; 11 cortes | S-M | Bajo |
| 6 | Organización | **Cabecera tipo FRED** en cada ficha: actualizado, próxima revisión, fuente y nivel | Se ve lo caducado sin abrir nada | S | Nulo |
| 7 | Organización | `mundo.html`: mostrar **etapa por tema** en vez de contar eventos, y el listado en un panel lateral | Hoy el número induce a error (más eventos ≠ más avance) | S | Bajo |
| 8 | Visual | **Rendimientos y colateral** (maqueta 2) como panel en `paneles.html` | Lo pide Joel y no existe | M (más research C42) | Bajo |
| 9 | Organización | **Pestañas Órbita / Matriz / Mapa / Paneles** con filtros compartidos (país, tema, nivel) que se mantienen al cambiar | Patrón OWID: mismos datos, distintas vistas | M | Medio |
| 10 | Datos | `indice_investigacion.py`: todos los informes por tema y país, no solo los 3 últimos | 88 informes hoy invisibles en el índice | S | Nulo |

## 6. Maquetas (datos de ejemplo, marcados así en la propia página)
- `informes/maquetas/C41A-vista-pais-tema.html`: matriz de 10 países × 10 temas con semáforo, certeza, filtros y ficha lateral.
- `informes/maquetas/C41A-rendimientos-colateral.html`: tabla por modalidad con estado legal, tasa con fecha, riesgo y certeza.

No se ha tocado `mapa.html` ni ningún dato real. Durante la prueba hubo un servidor temporal en `.claude/launch.json`, ya revertido. Lo siguiente es C41B (Gemini) y C41C (fusión), que decide qué entra.
