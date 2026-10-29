# C54-C57 · Noticias, verificación, Seguimiento y eventos de proyectos (pedido de Joel, 29-oct-2026)

Contexto: la pestaña «Eventos y noticias» se ha BORRADO (duplicaba Calendario y Noticias). Lo que no cuaja: [P]/[S] se lee como «verdadero/falso» y no lo es; el Seguimiento no enseña bien las verificaciones. Reglas: sigue CLAUDE.md; sin API de Anthropic ni workflows; commit y push solo con «sube» (`python scripts/subir.py`).

## C54 · Noticias: tipo de fuente ≠ verificación (sesión de código, ~2 %)
Pestaña «Noticias» (explorador/vistas.html, función de noticias; datos en explorador/datos.json y noticias/). Haz:
1. El tipo de fuente (primaria / prensa / empresa) va como etiqueta gris neutra; NO es calidad ni veracidad.
2. La verificación es otro campo aparte: ✔ Confirmado (con quién o con qué), ◐ Sin contrastar, ✖ Dudoso/desmentido. Fuente de datos: un registro `eventos/verificados.json` (fecha, contiene, estado, con, url, verificado) que rellenan las sesiones de verificación; una fuente primaria cuenta como confirmada.
3. Que «sin contrastar» no alarme en rojo por defecto: solo lo de importancia alta o media y de más de 7 días.
4. Prueba en el navegador (preview app-cartera); no dejes dos scrolls.
Hecho = captura mental de 3 noticias reales (una de prensa cierta y confirmada, una sin contrastar, una primaria).

## C55 · Seguimiento: que sirva de verdad (sesión de código, ~2 %)
Seguimiento del PC (seguimiento.py) y del móvil (docs/movil), generados por scripts/construir_seguimiento.py. Haz:
1. Sección «Verificaciones pendientes» con antigüedad (de `eventos/verificados.json` y de los [VERIFICAR] del PLANNING), ordenadas por importancia.
2. Eventos pasados «SIN research» y su estado (lo ya hecho sale como hecho, no se repite).
3. Un bloque «Qué toca hoy» corto arriba, y lo demás plegado.
4. Mismo contenido en PC y móvil (misma fuente, no divergen).

## C56 · Verificar noticias de prensa recientes (research, ~2 %)
Con `python scripts/buscar_informes.py` y fuentes primarias: confirma o descarta las noticias de los últimos 14 días que sean de importancia alta o media y vengan de prensa. Primeras: (a) OCC aprueba definitivamente el banco fiduciario nacional de Ripple (CoinDesk, 27-oct; Joel dice que lo confirmaron el CEO de Ripple y la OCC: busca el comunicado en occ.gov o ripple.com y anótalo con enlace), (b) cifras oficiales de la BEA del 29-oct (PIB 3T avance y PCE de septiembre), (c) las [VERIFICAR] del PLANNING. Todo lo contrastado va a `eventos/verificados.json`. Salida: informes/research/AAAA-MM-DD-C56-verificacion-noticias.md.

## C57 · EV Swell 2026 (Ripple) y Meridian 2026 (Stellar) (research, ~2 %)
Usa research/prompts/EV-post-evento.md: anuncios técnicos o de producto, incidentes o auditorías, con fuente primaria (blogs de Ripple y Stellar); los anuncios no son hechos hasta que se confirmen. Afectan a XRP y XLM: caso alcista y bajista y sesgos. Marca ambos en eventos/revisados.json.
