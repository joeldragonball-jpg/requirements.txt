# C127 · Auditoría visual, fase 1 (solo mirar, sin tocar código)

Fecha: 4-nov-2026. Cómo: app en `localhost:8793` → Cerebro, recorridas las 10 pestañas con la extensión de Chrome (pantalla de 1568 px). Medidas de España tomadas del propio DOM. Las propuestas son sugerencias mías, no decisiones.

## Resumen en una línea por pestaña
| Pestaña | Veredicto |
|---|---|
| Resumen | **Lo más flojo.** Muro de números. |
| Capas | Denso, mucho texto continuo. |
| Línea de tiempo | Buena idea visual; poco legible por abajo. |
| Calendario | Bien, pero 12+ fichas sin jerarquía. |
| Matriz país × tema | **De lo mejor**: color y leyenda claros. |
| Noticias | Bien, pero con muchísimo texto por tarjeta. |
| Voces | Bien, tarjetas largas. |
| Países | Va bien; secciones de tabla enormes. |
| España | **Lo más largo**: 18.470 px, 264 tablas, 75 desplegables. |
| Paneles de datos | Bien (tabla de bonos con mini-curvas). |

## 1. Resumen (Cifras clave)
1. 19 tarjetas del mismo tamaño y estilo: lo importante y lo secundario pesan igual. Mezclan cripto, bonos, energía, comida, miedo, chips y España sin bloques.
2. La etiqueta que dice qué es cada cifra está debajo, en gris pequeño y a menudo en dos o tres líneas («XRP · capitalización $80,9 mil millones»). La cifra grande sola no se entiende.
3. Unidades mezcladas («$297,1 mil millones», «$955 millones», «$9332 mil millones», «246 €/MWh», «37 por millón») y cifras de relleno (capitalización de cada cripto, Brent como futuro) con el mismo peso. «$9332 mil millones» es una deuda; «$297,1 mil millones», stablecoins: nada lo distingue a golpe de vista.
- Propuesta: 5 bloques con título (Cripto, Tipos y deuda, Energía y materias primas, Miedo y chips, España); 1 cifra grande por bloque y las demás pequeñas; etiqueta corta arriba; mini-curva donde haya serie; capitalización y futuros plegados.

## 2. España (la que más ordenar)
1. Una sola columna de 18.470 px (unas 25 pantallas), con 264 tablas y 43.800 caracteres de texto.
2. No hay índice ni pestañas internas: economía, deuda autonómica, presupuesto por ministerio (más de 20 bloques), pagos, mortalidad, carretera, delitos, hipotecas, todo seguido.
3. 75 desplegables, 12 abiertos por defecto: lo que se abre no es siempre lo importante. El gráfico de exceso de mortalidad (nuevo) se ve, pero es muy pequeño (unos 420 px) y queda enterrado en un bloque cerrado, debajo de más de 60 filas.
- Propuesta: 4 pestañas internas (Economía y deuda · Presupuesto y gasto · Servicios y sociedad · Seguridad y salud), 3-5 cifras con flecha al principio de cada una y el detalle plegado.

## 3. Países
1. Cada sección es una tabla de 6 columnas por 10-13 filas; cada celda lleva 3 líneas (valor, año, «antes»): informativo pero apretado.
2. Las secciones nuevas se pierden entre las ~12 que ya hay (Seguridad (Eurostat) cerrada por defecto, debajo de Indicadores económicos).
3. Solo hay datos de Seguridad para 4 de 6 países (NL y PL salen «—»). Homicidios de Alemania (8,3 por millón) [VERIFICAR]: los datos policiales alemanes pueden incluir tentativas; no comparar directamente con España hasta confirmarlo en la definición de Eurostat.

## 4. Capas
1. Párrafos largos de contexto antes de las cifras.
2. Tablas con celdas de varias líneas (comparación de CBDC, stablecoins y depósitos) difíciles de recorrer.
3. Etiquetas de certeza (P/S/V) y de nivel (1-5) compiten con el contenido.

## 5. Línea de tiempo
1. 13 casillas de capas más rango, buscador y filtro de «reacción de precios» antes del gráfico: la barra de controles ocupa casi un tercio de la pantalla.
2. Puntos y rombos agrupados a la derecha (lo reciente) tapándose entre sí.
3. El panel derecho de «Lo más reciente» tiene mucho texto y botones «Ver reacción» repetidos.

## 6. Calendario
1. 12+ fichas del mismo tamaño; el «ALTO impacto» solo se distingue por una pequeña etiqueta y un borde.
2. Cada ficha repite fuente y tema en letra muy pequeña.
3. No hay vista de semana o cuenta atrás (idea ya anotada en `ideas-pendientes-mejoras`).

## 7. Matriz país × tema
1. Pocos fallos: color y leyenda claros.
2. Insignias P/S y el punto amarillo en cada celda aportan poco a primera vista.
3. Algunas filas llevan «—» en toda la fila (Egipto, Etiopía): quizá agrupar «sin datos».

## 8. Noticias
1. Tarjetas con texto largo de verificación (el de Ormuz ocupa 5-6 líneas antes del titular).
2. 11 + 10 + 30 noticias en tres columnas: mucho para leer, sin resumen de «lo que importa hoy».
3. Bien: los colores de «Confirmado / Dudoso / Sin contrastar» funcionan.

## 9. Voces
1. 64 tarjetas con 3-4 etiquetas cada una (nivel, confirmación, capa, plazo).
2. Texto en 8-9 px en las líneas de fuente.
3. Sin ordenar por «lo que cambia tu decisión».

## 10. Paneles de datos
1. Bien en general (tabla de bonos con curvas).
2. La tabla es ancha: 10 plazos, muchas celdas con «—».
3. Los bloques siguientes se ven poco desde arriba (no hay índice).

## Qué NO tocaría (Joel lo ve bien)
Noticias, Voces, Paneles de datos y Países: solo los detalles de arriba.

## Orden de trabajo que propongo (fase 2, necesita tu OK)
1. Resumen: Cifras clave en bloques (la queja principal).
2. España: pestañas internas + resumen visual.
3. Detalles de las demás (tamaño de letra, controles de la línea de tiempo).
