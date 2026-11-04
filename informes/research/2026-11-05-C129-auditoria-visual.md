# C129 · Auditoría visual y de explicaciones del tablero (5-nov-2026)

Modelo: Opus 5.5 · Archivo tocado: `explorador/vistas.html` (solo presentación y textos; ningún dato ni fuente cambiado).
Método: tablero abierto en Chrome desde la Órbita (`localhost:8793`), recorrido de las 10 pestañas y las 4 subpestañas de España, medición con `getComputedStyle` (letra mínima, celdas de 3+ líneas, textos de más de 220 caracteres) antes y después. Sintaxis comprobada con `node --check`.

## La causa principal de la «letra de 8-9 px»

**HECHO medido:** Chrome tiene la Órbita al **80 % de zoom** (`devicePixelRatio` = 0,8, ventana de 2.350 px CSS en una pantalla de 2.560). Por eso:

| Elemento | Tamaño CSS | Lo que se ve en pantalla al 80 % |
|---|---|---|
| Celdas de tabla | 16 px | ~12,8 px |
| Fecha y «antes» en Países | 12,5 px | **~10 px** |
| Pie de barras en Paneles | 11,5 px | **~9 px** |
| Títulos de tarjetas `.cc-b` | 12,5 px | ~10 px |

El código ya tenía mínimos de 13-15 px, pero el zoom del navegador los encogía. Solución aplicada: control **Letra A− / A+** en la barra superior. Si detecta el navegador alejado, arranca compensando (al 80 % → 125 %); lo que elijas se recuerda en ese navegador.

## Problemas por pestaña

| Pestaña | Qué se veía mal | Letra mínima antes → ahora (CSS) | Solución | Estado |
|---|---|---|---|---|
| Todas | Zoom 80 %: todo un 20 % más pequeño | — | Control «Letra» con compensación automática | ✅ hecho |
| Resumen | Títulos de tarjetas y flechas a 12,5 px | 12,5 → 13,1 | Suelo de 13 px en `.cc-b h3` y en las flechas `.cc-f` | ✅ hecho |
| Capas | Tabla «Las tres, comparadas»: 7 columnas, 21 celdas de 3-5 líneas, que repetía las tarjetas de arriba | 13,5 | Tabla plegada en un desplegable bajo las tarjetas | ✅ hecho |
| Capas | Tablas «Próximas fechas» (28 celdas largas) y «Hechos recientes» (40) | 13,5 | — | ⏳ siguiente pasada |
| Línea de tiempo | Correcta | 13 | — | sin cambios |
| Calendario | Correcto; 136 textos de 13-14 px | 13 | Lo cubre el control «Letra» | sin cambios |
| Matriz | Correcta; tooltip comprobado con zoom | 14 | Posición del tooltip corregida para el zoom | ✅ hecho |
| Noticias | Archivo de 54 filas × 4 | 13,5 | — | ⏳ siguiente pasada |
| Voces | Correcta | 13,5 | — | sin cambios |
| Países | 573 líneas de 12,5 px; celdas de 3 líneas (valor / fecha / antes) → 91 celdas largas solo en Indicadores | 12,5 → 13 | Fecha y «antes» en una sola línea; la fecha del dato anterior pasa al tooltip | ✅ hecho (0 celdas de 3+ líneas) |
| España · Economía y deuda | Notas largas encima de las tablas | 13,5 | Nota corta + «ⓘ Cómo se lee · sesgos · fuente» | ✅ hecho |
| España · **Presupuesto y gasto** | Cifras de cabecera planas, sin color (no encajaban con Cifras clave); «Cómo leer» abierto con 340 caracteres antes del dato; nota de capítulos de 420 caracteres antes de la lista; etiqueta de % de las barras desplazada | 13,5 | Tarjetas con borde y degradado de color (azul, verde, oro, violeta) y cifra grande; «Cómo leer» plegado; notas cortadas a la primera frase con el resto plegado; etiqueta de la barra centrada y con sombra | ✅ hecho |
| España · Servicios y sociedad | Notas largas | 13,5 | Mismo patrón de nota corta | ✅ hecho |
| España · Seguridad y salud | Notas de 270-370 caracteres (Defunciones, DANA, Delitos) | 13,5 | Mismo patrón | ✅ hecho |
| Paneles de datos | Pie de barras a 11,5 px; Bonos 9 × 12 con 96 celdas largas; 203 celdas de 3+ líneas en total | 11,5 → 13 | Suelo de 13 px | ⚠️ parcial: falta rehacer las tablas |

## Qué se cambió (resumen técnico)

1. `corto()`: toda explicación de bloque (`bloque()`) o nota de España (`conL()`) de más de ~210 caracteres deja a la vista la primera frase y pliega el resto en «ⓘ Cómo se lee · sesgos · fuente». Se aplica solo, sin tocar los JSON.
2. `.kpis.vivo`: cabecera de las 4 subpestañas de España con tarjetas de color, como Cifras clave.
3. Control «Letra» (`#lmenos`, `#lmas`, `localStorage` `orbita-letra`, con try/catch). `ncols()` y los dos tooltips tienen en cuenta el zoom.
4. Mínimos: nada por debajo de 13 px en las 10 pestañas (medido; antes había 11,5 y 12,5).
5. Capas: el texto de la capa Dinero digital dice ahora «El desplegable de abajo las compara» (antes, «La tabla de abajo»).

## Para la siguiente pasada (2-3 por pestaña)

- **Paneles**: (1) Bonos 9 × 12: pasar a curva (línea por país) con la tabla plegada; (2) en las tablas de más de 6 columnas, la columna «Nota» al tooltip; (3) las cabeceras de bloque como tarjetas `.cc-b`.
- **Capas**: (1) «Próximas fechas» y «Hechos recientes» como lista de tarjetas `.ev` (fecha grande + 1 línea) en vez de tabla de 4-5 columnas; (2) línea «En qué se basa» plegada.
- **Países**: (1) los «antes» usan a veces punto decimal («22.7 %», «48.85 millones») y otras coma: unificar en `cortaUnid`; (2) las 4 cifras grandes se estiran a ~550 px cada una: limitar el ancho o añadir una mini-serie; (3) en «Comparar todos los países», fijar la primera columna al hacer scroll.
- **España · Presupuesto**: (1) nombres de ministerio en MAYÚSCULAS de la IGAE: pasar a tipo frase solo al mostrar; (2) en cada ministerio abierto hay 5-6 tablas seguidas: poner arriba 3 cifras (total, % personal, mayor programa) y las tablas plegadas; (3) «Programas concretos» mide 5.400 px abierto: plegarlo por defecto.
- **España · resto**: el párrafo de vigencia de los PGE (2 líneas) puede ir como insignia + 1 línea.
- **Resumen**: «Novedades de los últimos 7 días» (26 × 4): limitar a 10 filas con «ver más».
- **Noticias**: archivo de 54 filas plegado por mes.
- **Calendario / Voces**: muchos textos de 13-14 px; comprobar con el zoom nuevo antes de tocar nada.

## A vigilar

- El arranque automático al 125 % solo ocurre si Chrome está alejado. Si Joel vuelve Chrome al 100 % (Ctrl+0), el tablero arranca al 100 %.
- El `zoom` CSS se aplica a la vista dentro del iframe de Streamlit. Comprobado sin scroll horizontal en las 10 pestañas, pero con 150 % y la ventana estrecha pueden saltar las 3 columnas a 2 (es lo previsto).
