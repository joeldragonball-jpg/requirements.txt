# C70 · Auditoría de diseño de la app móvil y boceto «cómo quedaría» (31-oct-2026)

Boceto: `docs/movil-prueba/index.html` (ver cómo abrirlo al final). La app real (`docs/movil/index.html`, `sw.js`) **no se ha tocado**.

## 1. HECHOS: cómo es la app hoy (medido a 375 px, datos reales del 31-oct)

Mapa (7 pestañas en la barra inferior): Hoy · Centro · Mercado · Datos · Agenda · Noticias · Cerebro (esta última tiene 4 sub-pestañas: Seguimiento, Voces, Vídeos, Informes). Pintado en `index.html`: `vHoy` l.268, `vMercado` l.287, `vAgenda` l.308, `vSeg` l.368, `vCentro` l.416, `vDatos` l.434.

| Pestaña | Alto (pantallas de 812 px) | Tarjetas/filas | Textos < 12,5 px | Elementos tocables < 40 px |
|---|---|---|---|---|
| Hoy | 2,0 | 11 | 85 | 0 |
| Centro | 3,9 | 7 | 70 | 0 |
| Mercado | **11,0** | 34 | 327 | 0 |
| Datos | 2,2 | 15 | 749 | 0 |
| Agenda | **12,5** | 71 | **1769** | 13 |
| Noticias | 5,2 | 21 | 48 | 6 |
| Cerebro > Seguimiento | 2,1 (resto plegado) | 28 | 157 | **59** |

Otros hechos del código: 7 pestañas en la barra (límite razonable en iOS: 5); cada tarjeta lleva degradado, borde y animación de entrada; casi todo usa la misma tarjeta y el mismo tamaño; la información de ayuda va en texto de 11-12 px dentro de cada bloque; la barra inferior no marca pestañas con avisos.

Limitación de las capturas: el panel de pruebas recortó el ancho de la app (la ventana del navegador integrado es más estrecha que 375 px), así que mis capturas de la app actual solo sirven para ver el arranque, no el layout completo. Las cifras de la tabla salen de medirlo por JavaScript, no de las capturas. [VERIFICAR] en un iPhone real.

## 2. Ejemplos de referencia (patrones, sin copiar marca ni textos)

Las búsquedas dieron fuentes secundarias; ninguna es la guía oficial abierta. Marco lo que no pude confirmar.

1. **Linear (móvil)** — https://linear.app/mobile y https://linear.app/now/how-we-redesigned-the-linear-ui. Patrón: bandeja con lo prioritario arriba, deslizar para descartar o posponer, más densidad con mejor contraste. Copiar: «lo urgente primero» y descartar con un gesto. Los iconos de estado concretos: [VERIFICAR] (solo lo describe un tercero).
2. **Things 3 (Hoy)** — https://thesweetsetup.com/update-review-best-gtd-app-mac-iphone-ipad-things/. Patrón: una sola lista «Hoy»; lo no hecho pasa al día siguiente, sin listas de «atrasado». Copiar: que la pantalla principal responda a «¿qué toca hoy?» y no mezcle el plan entero.
3. **Yahoo Finance (carteras y listas de seguimiento)** — https://9to5mac.com/guides/yahoo-finance/ y https://www.businesswire.com/news/home/20231107696257/en/Yahoo-Finance-Debuts-New-Design-and-Features-to-Empower-Everyday-Investors. Patrón: totales de la lista a la vista y desplegable para cambiar de lista. Si arriba hay una tarjeta resumen: [VERIFICAR] (no lo encontré). Copiar: cifra + variación alineadas a la derecha, una fila por valor, con la divisa visible.
4. **Apple Human Interface Guidelines (diseño y tamaño táctil)** — https://developer.apple.com/design/human-interface-guidelines/layout (no la abrí; las cifras vienen de resúmenes de terceros, p. ej. https://blog.openreplay.com/improving-tap-targets-mobile-ux/). Patrón: zona táctil mínima de 44×44 pt, márgenes de 16 pt, múltiplos de 8, jerarquía con peso y tamaño de letra. Copiar: 44 pt mínimo y espaciado de 8.
5. **Material Design 3 (indicadores de progreso, chips, listas)** — https://v9.material.angular.io/components/categories/buttons (documentación derivada, no m3.material.io; [VERIFICAR] ahí). Patrón: barra de progreso con valor real, chips para filtrar, lista frente a tarjeta (la tarjeta ocupa más y sirve para descubrir; la lista sirve para encontrar). Copiar: listas planas para muchos elementos y tarjetas solo para lo destacado.

## 3. Problema → cambio propuesto (por impacto)

OPINIONES de diseño; los problemas medidos están en el apartado 1.

| # | Pantalla | Problema | Cambio propuesto |
|---|---|---|---|
| 1 | Todas | 7 pestañas y todas pesan igual | 5 pestañas: Hoy · Seguimiento · Agenda · Mercado · Más (Datos, Noticias, Voces, Informes, Centro, Buscar). Hecho en el boceto |
| 2 | Hoy | Anillo, cinta, cuadrícula, píldoras, eventos y noticia compiten | Un solo bloque grande (qué es lo siguiente y a cuántos días, con barra de color por impacto) + 3 cifras (racha, % del plan, verificaciones urgentes) + estado de R00 + 4 activos + próximas 3 fechas |
| 3 | Agenda | 12,5 pantallas, 71 filas iguales, 1769 textos pequeños | Agrupar por mes con cabecera, barra de color por impacto, filtros de 44 px; tarjetas planas. Plegar los países y el radar |
| 4 | Mercado | 11 pantallas apiladas del mismo tamaño | Tipos, bolsas y bonos como listas planas; el resto (inflación, liquidez, Ormuz, defensa) plegado bajo «Más datos» |
| 5 | Seguimiento | 59 tocables pequeños; los datos útiles (racha, % del plan) están en dos textos | Cifra grande de % con barra, semáforo de «qué se queda viejo» (punto verde/ámbar/rojo + número), verificaciones con barra de color por urgencia, plan completo plegado |
| 6 | Todas | Degradados y animación por tarjeta; todo del mismo color | Tarjetas planas, un solo acento (dorado), rojo y verde solo para estado y variación; sin animación de entrada |
| 7 | Todas | Solo modo oscuro | Claro y oscuro automáticos (más legible a plena luz), con botón ◐ |
| 8 | Todas | Texto de 11-12 px | Mínimo 13 px en lo que se lee, 12 px solo en etiquetas |

Información extra que cabe sin recargar: % del plan hecho, verificaciones urgentes, racha y próximas fechas con «en N d». Ya están en el boceto.

## 4. Boceto: qué se comprobó

- Lee los datos reales (`../movil/data.json` y `../movil/seguimiento.json`); 5 pantallas: Hoy, Seguimiento, Agenda, Mercado, Más (esta última es un hueco explicativo).
- A 375×812: sin desborde horizontal, sin NaN/undefined, sin errores de consola. Hoy 1,5 pantallas (la app actual 2,0), Agenda 5,9 (antes 12,5), Mercado 1,4 (antes 11,0), Seguimiento 2,0.
- Tocables ≥ 44 px (corregido el único fallo, los enlaces «Mercado ›/Agenda ›»; no lo medí otra vez tras el arreglo).
- Modo claro comprobado en captura; **modo oscuro con botón ◐ no capturado** (la ventana del navegador integrado arranca en claro). [VERIFICAR] con el botón.
- Precios cripto en euros al cambio BCE, igual que la app actual.

## 5. Qué falta

- Joel decide: ¿qué cambios (1-8) pasan a la app real? Hasta entonces no se toca `docs/movil/` ni `sw.js`.
- Pantallas no bocetadas: Centro, Datos, Noticias, Voces, Informes.
- Prueba en un iPhone real (la banda inferior de iOS y `viewport-fit=cover` no se han tocado; el boceto lo mantiene en la etiqueta viewport pero no tiene el parche `ios-sa` de la app).
- El boceto no tiene todavía la hoja CSV en vivo del Seguimiento ni el service worker.

## Cómo abrirlo

Con el servidor `movil-estatico` (puerto 8795): http://localhost:8795/movil-prueba/. Desde el móvil, solo cuando se publique `docs/movil-prueba/` en GitHub Pages (requiere «sube»).

## Lecciones (máx. 5 líneas)
- Los datos de la app actual se miden con JS; las capturas del navegador integrado se recortan si el panel es más estrecho que la emulación.
- Las búsquedas de patrones dieron sobre todo fuentes secundarias: marcar [VERIFICAR] lo no leído en origen.
