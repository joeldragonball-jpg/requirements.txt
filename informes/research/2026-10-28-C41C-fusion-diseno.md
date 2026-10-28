# C41C · Fusión del diseño de la Órbita (C41A Claude + C41B Gemini) · 28-oct-2026

Sin IA de pago ni cambios en datos reales, `mapa.html`, `mundo.html` ni `paneles.html`. Solo este informe, filas nuevas en la cola y un prototipo aparte: `explorador/prueba-diseno.html`. Etiquetas: [P] visto o leído; [RAZONADO] propuesta de diseño sin fuente que la pruebe. La decisión final es de Joel.

## 1. Dónde coinciden y dónde no
**Coinciden (señal fuerte, dos propuestas independientes):**
- Matriz **país × tema** con color por estado, ficha al pasar el ratón o hacer clic, con fecha y fuente.
- **Datos separados del HTML** y esquema común (país, nivel de certeza, fecha, url) más un índice para que la IA lea 1-2 archivos y no 6.
- **Filtros compartidos** (país, tema, nivel) entre vistas.
- **Caducidad** de noticias (ya decidida en C35: 24 h / 7 d / 30 d) y **certeza visible** en cada celda o nodo.
- Panel lateral fijo en vez de tarjetas flotantes.

**Discrepan:**

| Tema | C41A (Claude) | C41B (Gemini) | Mejor argumento |
|---|---|---|---|
| Estados de la celda | Etapa 0-5 que ya existe en `regulacion.json` (136 celdas) | 3 colores: legal / restringido / prohibido | **C41A**: la escala existe y distingue «aprobada, sin vigor» de «en vigor». De Gemini se toma el aspecto de «chip» |
| Esquema | Campos nuevos **sin renombrar** los viejos | Archivos nuevos planos (`matrix.json`, `timeline.json`…) | **C41A**: no rompe generadores ni Órbita. De Gemini, la idea de plano y sin anidar para el índice |
| Certeza | Textura: liso / rayado / discontinuo | Iconos: escudo / círculo / triángulo | **Gemini** (no depende del color), combinado con la textura de C41A |
| Noticias | Cabecera tipo FRED («actualizado / próxima revisión») | Carriles por color y purga en el navegador | **Complementarias**: cabecera en fichas, purga en noticias (C35) |
| Pipeline con LLM que lee URLs | No lo propone | «Utilidad altísima» | **Posponer**: cuesta API (regla 4 de CLAUDE.md) y la verificación manual es lo que da valor |

**Referencias.** La verificación hecha en C41B (28-oct) dice: Blockchain Council coincide [P]; Atlantic Council y OWID, solo en parte; DefiLlama dio 403 a esa comprobación (C41A sí lo abrió, [P]); CoinTracking, Elliptic, Messari, PwC y Chainalysis no se abrieron. No he reabierto más para no gastar cuota: las propuestas de Gemini quedan como [RAZONADO].

## 2. Cambios fusionados (10) por utilidad/esfuerzo y orden
| Orden | Cambio | Esfuerzo | Depende de | Fila |
|---|---|---|---|---|
| 1 | **Índice generado** (`explorador/indice/` + `INDICE.md` «dato → archivo → campo») e **índice completo de informes** (88 hoy invisibles) | M | nada; va **antes de C39 y C35** | C43 |
| 2 | **Esquema común** en campos nuevos (`pais_id`, `nivel`, `fecha`, `url`, `revisar`, `caduca`, `sesgo`, `perspectivas`), sin renombrar | M | 1 | C43 |
| 3 | **Arreglos rápidos de `mapa.html`**: giro apagado, texto ≥13 px, tarjetas en columna lateral, sin «…», cabecera tipo FRED | S-M | nada | C44 |
| 4 | **Noticias con caducidad** (purga en el navegador por `caduca`) | M | 2 | C35 (ya existe) |
| 5 | **Pestaña Matriz país × tema** con iconos de certeza y selector semáforo/datos | M | 2 (mejor) | C45 |
| 6 | **Línea de tiempo con panel lateral** y carriles colapsables | M-L | 3 | C46 |
| 7 | **Filtros globales y pestañas** Órbita / Matriz / Mapa / Paneles | M | 5 y 6 | C46 |
| 8 | **`mundo.html`**: etapa por tema en vez de contar eventos | S | 5 | C47 |
| 9 | **Rendimientos y colateral** en `paneles.html` | M | research C42 antes | C42 (volcado: fila nueva después) |
| 10 | Pipeline LLM de actualización (idea de Gemini) | L | — | sin fila: pospuesto |

**Sobre lo ya programado:** C30 (5-nov) y C39 pueden hacerse sin esperar, pero ganan si antes está C43 (nacerían con los campos nuevos, sin migrar). C35 necesita el campo `caduca` de C43. C42 va antes que el cambio 9.

## 3. Prototipo
**Actualización v3 (28-oct, tras la 2.ª crítica de Joel):** la v2 dejaba poco sitio a la información en «Capas» y los «Paneles» eran filas de números con etiquetas ambiguas («3M», «2A»). Ahora: capas como pastillas arriba y detalle a ancho completo (cabecera de 2 líneas; 4 cuadros paralelos de producción/piloto/plan/XRP-XLM con chips; datos al día de cada capa; cifras; ficha del analista; fechas próximas; hechos; biblioteca y glosario); pestaña Calendario; bonos con plazos escritos («3 meses», «10 años»), cambio diario en puntos básicos y minigráfico a 10 años; TIC, stablecoins, FMI, defensa y Ormuz con barras o minigráficos; cada bloque con «qué mide», unidad, fuente, nivel y fecha. Se corrigió un fallo de la v2: «Deuda de EE. UU. en manos extranjeras» leía el mes más antiguo (9.249) en vez del último (9.332, ago-2026). Datos de calendario y documentos por capa: `explorador/prueba-datos.json`, generado con `scripts/exportar_prueba_orbita.py`.

**Actualización v4 (28-oct, pantalla grande):** mismo estilo, textos y pestañas que la v3, pensado para 1920 y 2560 px (revisado también a 1366). Rejillas que se adaptan al ancho; en «Capas» los cuadros sin hechos con el filtro se colapsan a una línea (con el recuento sin filtrar), «Datos al día» va a ancho completo en columnas, cifras clave y ficha del analista en filas anchas y la biblioteca en rejilla; calendario en columnas por mes; voces en dos columnas; paneles en columnas con los bloques anchos (bonos, deuda, valoración…) a ancho completo. Donde antes había hueco ahora sale un dato real alternativo (últimos hechos de otras capas, próximas fechas, celdas por etapa y revisadas hace poco en la matriz, lo más reciente en la línea de tiempo y en noticias). Movimiento sobrio: fundido al cambiar de pestaña, tarjetas que aparecen, hover en filas y celdas, cifras que cuentan hacia arriba, barras y minigráficos que se dibujan; solo la primera vez que se ve cada pestaña y desactivado con `prefers-reduced-motion`. Sin tocar la app real ni los datos.

**Versión v2 (superada):** la primera versión solo mostraba 3 bloques y se quedaba corta frente a la Órbita. Se rehízo como v2 con 7 pestañas que cubren todo el contenido de datos: Resumen (cifras clave, últimos movimientos, próximas fechas), Capas (las 12, con producción/piloto/plan/XRP-XLM/claves/cifras/ficha y sus movimientos), Línea de tiempo (63 movimientos de 2023 a hoy, carriles apagables, búsqueda, rango, panel lateral), Matriz (136 celdas con hitos e informes en el panel), Noticias (con archivo), Voces (50, con filtros) y Paneles de datos (stablecoins, RWA, TIC, bonos, tipos, defensa, Ormuz, índices, liquidez, calificaciones, deuda FMI, reservas, valoración y bancos EBA). Lo que NO incluye: la vista animada de raíles (se conserva en `mapa.html`) y el contraste privado con la tesis (solo en tu PC). Descripción de la v1 abajo, ya superada:

`explorador/prueba-diseno.html`: independiente, lee `regulacion.json` y `datos.json` por `fetch` (solo lectura) y no está enlazado desde nada. Muestra la matriz 17 jurisdicciones × 8 temas con ficha al pasar el ratón, iconos de certeza (🛡 [P], ◐ [S], △ [VERIFICAR]), punto de cambio en 30 días, selector Semáforo / Datos y filtros; la línea de tiempo por capas (último año) con panel lateral; y noticias en 3 columnas de caducidad. Probado en el navegador integrado: 0 errores de consola, 18 filas, 56 nodos; `scripts/revisar_explorador.py` sigue en 0 avisos. Lo único «EJEMPLO» es el hueco «alcista/bajista» del panel lateral (`datos.json` no tiene ese campo). Los movimientos reales llegan al 25-oct, así que la columna de 24 h sale vacía hoy.

**Cómo abrirlo:** `fetch` no funciona con doble clic (file://), hace falta un servidor local de solo lectura (ver el mensaje final).

## 4. Qué decide Joel
Qué filas C43-C47 se hacen, cuáles se posponen y si el pipeline con LLM se descarta. Orden sugerido (no es una orden): C43 → C44 → C45 → C46/C47, y C42 cuando haya cuota.
