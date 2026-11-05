# C134 · Auditoría visual del tablero, 2.ª pasada (5-nov-2026)

Modelo: Opus. Solo presentación en `explorador/vistas.html`; no se han tocado datos ni fuentes. Sin subir (falta «sube»).

## Cómo se ha medido

- Copia local de la Órbita generada con `explorador._html()` (los mismos datos que la app) y abierta en el navegador integrado a **1600 × 1000 px**, letra al 100 %.
- Versión «antes» = `HEAD` (219418b), «después» = archivo actual; las dos medidas, en el mismo navegador y con la misma regla.
- **Celda de 3+ líneas** = el contenido de la celda (no la fila) mide más de 3 alturas de línea. Solo cuenta lo visible (`checkVisibility()`): lo que está dentro de un desplegable cerrado no se ve y no cuenta. Por eso no sale igual que en C129, que contaba filas.
- **Letra mínima** = `getComputedStyle().fontSize` del texto visible más pequeño.
- `node --check` del JS extraído tras cada bloque de cambios: correcto. Sin errores de consola al recorrer las 10 pestañas.

## Antes y después

| Pestaña (vista) | Celdas visibles | Celdas de 3+ líneas | Letra mínima | Textos < 13 px | Alto |
|---|---|---|---|---|---|
| Paneles (por defecto) | 851 → 755 | 5 → 5 | 13 → 13 px | 0 → 0 | 6.607 → 6.526 px |
| Paneles (todo abierto) | 1.507 → 1.507 | 12 → 11 | 13 → 13 px | 0 → 0 | 11.749 → 12.281 px (*) |
| Capas (por defecto) | 272 → 172 | 12 → 0 | 13 → 13 px | 0 → 0 | 6.157 → 5.931 px |
| Capas (todo abierto) | 293 → 193 | 24 → 1 | 13 → 13 px | 0 → 0 | 7.855 → 7.561 px |
| Países (todo abierto) | 413 → 413 | 9 → 9 | **10,4 → 13 px** | **205 → 0** | igual |
| España · Presupuesto (por defecto) | 763 → 459 | 30 → 0 | **12,5 → 13 px** | **144 → 0** | **11.996 → 7.213 px** |
| España · Presupuesto (todo abierto) | 1.973 → 1.954 | 37 → 25 | 12,5 → 13 px | 515 → 0 | 67.382 → 68.763 px |

(*) Con todo abierto, Paneles crece porque la curva de bonos se suma a la tabla (que antes era lo único que había). Con la vista normal, la tabla queda plegada.

## Qué se ha cambiado

**Paneles**
- Bonos (8 países × 10 plazos): ahora es una **curva de rendimientos** (una línea por país, nombre al final de cada línea, leyenda con fecha y nivel). Cada punto dice al pasar el ratón país, plazo, % y cambio del día en pb. La tabla completa queda en un desplegable debajo. También en la capa «Tipos, liquidez y deuda» de Capas (6 países).
- `tabla()` general: en las tablas de **más de 6 columnas**, la columna «Nota» pasa al tooltip de la fila (marca ⓘ), y los textos de más de 120 caracteres se recortan con el texto entero al pasar el ratón (ejemplo: CBDC dentro de blockchains, Programas concretos).

**Capas**
- «Próximas fechas» y «Hechos recientes» dejan de ser tablas de 4-5 columnas: ahora son **tarjetas `.ev`** con la fecha grande a la izquierda, 1-2 líneas de texto y debajo la capa y el estado o la fuente. Color = tema (fechas) o estado (hechos); impacto alto, con el borde grueso. Lo que no cabe va al tooltip.
- «En qué se basa» queda plegado (solo se ve el título).

**Países**
- Coma decimal: los valores ya salían con coma. Quedaban 4 tooltips de homicidios con «49.36 M hab.»: ahora usan `num()` («49,36»).
- La flecha ▲/▼ de cada celda pasa de 10,4 px a 13 px como mínimo (eran los 205 textos pequeños).
- Las 4 cifras grandes de la ficha del país, con un ancho máximo de 1.100 px en total (no se estiran en pantallas anchas).
- En «Comparar todos los países», la **primera columna queda fija** al desplazar la tabla en horizontal.

**España · Presupuesto**
- Nombres de la IGAE en MAYÚSCULAS → **tipo frase** al mostrarlos, con siglas respetadas («Inclusión, S.S. y migraciones», «Relaciones financieras con la U. E.») y los órganos con mayúscula en cada palabra, como en el BOE («Tribunal de Cuentas», «Casa de Su Majestad el Rey»). Al pasar el ratón, el nombre original.
- Cada ministerio abierto muestra arriba **3 cifras**: gasto total, % de personal (con los M€) y el mayor programa (con su % del ministerio). Las 5-6 tablas (ejecución, capítulos, programas, centros, a quién transfiere) quedan en un desplegable.
- «Programas concretos» (5.400 px abierto) **plegado por defecto**.
- Letra de las filas de ministerio (importe en M€, % del Estado, € por habitante) y de las barras %: mínimo 13 px (antes, 12,5 px).

## Para la siguiente pasada (2-3 por pestaña)

- **Paneles**: (1) CBDC dentro de blockchains: pasar a tarjetas por proyecto (hoy 7 columnas recortadas); (2) cabeceras de bloque como tarjetas `.cc-b`; (3) Stablecoins y Tipos oficiales: 6 columnas con cifras pequeñas en dos líneas; probar a quitar «Cadenas» y «Dato de» al tooltip.
- **Capas**: (1) el orden de «Hechos recientes» viene del archivo (mezcla 2026 y 2025): ordenarlo por fecha si Joel lo quiere; (2) la «Ficha del analista» plegada es muy larga: dividirla por capa.
- **Países**: (1) mini-serie (2-5 años) bajo cada cifra grande cuando C133 traiga la historia; (2) los 9 textos de 3+ líneas son los nombres largos de indicadores en la 1.ª columna: acortar el nombre y llevar la definición al tooltip.
- **España · Presupuesto**: (1) abreviaturas de la IGAE («Financ.», «Territ.», «Demogr.»): diccionario para escribirlas enteras; (2) con todo abierto siguen 25 celdas largas en «Programas concretos» (nombres de programa): recortar a 1 línea con tooltip.
- **Resumen / Noticias / Calendario**: siguen pendientes de C129 (novedades a 10 filas con «ver más», archivo de noticias por mes).

## A vigilar

- La curva espacia los plazos por igual (3 meses, 6 meses, 1 año… 30 años), no en proporción al tiempo: así se leen bien los plazos cortos, pero la pendiente no es la «real». Lo dice una nota bajo la curva.
- El recorte de textos largos solo se aplica a tablas de más de 6 columnas; el texto entero sigue al pasar el ratón, pero en el móvil (sin ratón) no se ve. El tablero es para PC (memoria «Órbita = ordenador»).
