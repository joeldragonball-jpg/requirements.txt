# C60 · Una página por país en el móvil y la Órbita (30-oct-2026)

**Hecho**
- Móvil (pestaña Agenda, debajo de «Elecciones próximas»): tarjeta desplegable «Comparar países» (cerrada). Selector UE / Potencias; tabla País · IPC · Paro · Deuda · Pobreza que cabe en 375 px sin scroll horizontal; al tocar una cifra sale fecha, fuente, nivel y definición. Bajo la tabla, una ficha desplegable por país con política (C58), indicadores (C59), estabilidad por dimensión (C61) con año y fuente de cada cifra, lectura [OPINIÓN] y los tres informes. Sin puntuaciones ni ranking. Datos en `data.json` clave «paises» (lo construye `construir_movil.py`); caché del móvil v39.
- Órbita: pestaña nueva «Países» (explorador/vistas.html + mapa.html + explorador.py) con tabla comparable por dimensión (política, indicadores, 7 dimensiones de estabilidad), selector UE / Potencias, año/fuente/nivel al pasar el ratón y fichas por país.
- Frescura: `construir_seguimiento.py` avisa de fichas con datos de más de 90 días o sin fecha (hoy: Países Bajos, Polonia, China, India → W11).

**Probado** en el navegador integrado: tarjeta, selector, ficha y cifra desplegables, sin errores nuevos (4 × 404 de iconos ya existentes); Órbita con 6+6 países y 42 filas.

**No hecho:** pestaña «Países» dentro del tablero de datos (explorador/paneles.html); capa «Política y elecciones» de la Órbita con un movimiento por país (datos.json); hitos por país (siguen vacíos); enlaces clicables a los informes (solo nombres de archivo).

**Avisos:** el IPC de los países de la UE sale del último dato de Eurostat disponible (en España, dic-2025: la fecha va en la celda al tocarla); los de potencias son medias anuales del Banco Mundial, no comparables con el IPCA.
