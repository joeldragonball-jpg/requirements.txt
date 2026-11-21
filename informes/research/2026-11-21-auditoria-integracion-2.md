# Auditoría de integración 2 (21-nov-2026)

Comprobado en el navegador (Órbita a 1280x800 y 1000x620; móvil a 500x800): sin errores de consola y sin desbordamiento horizontal. Regenerados `construir_orbita.py` y `construir_movil.py`; `revisar_explorador.py`: 0 avisos.

## Visible
- `tokenizado.json`, `cadenas-pistas.json`, `tokenizacion-instituciones.json` y `brecha_rwa.lectura_actual`: Órbita > Cadenas (cajas con chip de caducidad «caduca en N d»; la lógica pasa a «caducada» si la fecha vence) y móvil > Datos (tarjetas con índice).
- `etf-13f.json`: Órbita > Paneles de datos («Quién tiene los ETF») y Capas; móvil > Datos.
- 50 movimientos nuevos de `datos.json` (416 en total): entran en la Línea de tiempo (según el rango elegido; 167 con el filtro por defecto) y en Capas.
- `eventos/calendario.toml` (eventos del 23-nov al 10-dic, p. ej. subastas del Tesoro, Abu Dabi, CFTC, EIA, MEXC): salen en Órbita > Calendario y en móvil > Agenda.
- `espana-leyes.json` (RDL 40 y 41, RD 1003 y 1032, convalidaciones del 18-nov): Órbita > España > «Política y leyes».
- `regulacion.json` (122 campos cambiados, `revisado` 2026-11-21): Matriz país × tema. Resumen > «Novedades» (227 entradas, con el volcado de hoy arriba): funciona.

## Corregido
- Resumen > «Últimos movimientos» ordenaba también las fechas futuras (elecciones de Francia 2027, España 29-nov) y dejaba fuera los hechos de hoy. Ahora solo muestra fechas hasta hoy (`vistas.html`, línea ~1003). Verificado tras regenerar.

## Pendiente
- `eventos/verificados.json`: las 29 filas del 21-nov se aplican como etiqueta a las noticias que casan por fecha y texto; hoy casan 12 de 29. Las otras 17 son titulares que ya no están en la lista de noticias vigentes; no es un fallo de visualización. No se ha tocado.
- Duplicado parcial en Cadenas: la caja antigua «Valor tokenizado por cadena (leído 14-nov)» convive con la nueva «Valor tokenizado por red (21-nov)». Conviene fusionarlas o plegar la antigua (no hecho por prisa).
- `indicadores-manual.json` y `espana-macro.json` (solo cambió la fecha `leido`): no se comprobó fila por fila; las pestañas que los usan cargan sin errores.
- Con el panel del navegador oculto, `innerText` devuelve falsos negativos; los elementos se confirmaron por DOM.
