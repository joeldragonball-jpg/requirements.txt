# Móvil pasada 4 (prioridad 5 y parte móvil de la 4) — 18-nov-2026

Nivel: [P] para lo comprobado con script y navegador; sin IA ni workflows.

## (a) Móvil: tarjetas nuevas en la pestaña Datos
`scripts/construir_movil.py` ahora lee los JSON del explorador con la función nueva `tarjetas_extra()` (se añade a `datos` en `datos_panel()`) y `docs/movil/index.html` (`vDatos`) las pinta. Cada fila lleva unidad y escala en el texto; lo no leído sale como «sin dato» o [VERIFICAR], nunca «null» (comprobado: 0 apariciones).

| Tarjeta | Fuente | Unidad/escala mostrada |
|---|---|---|
| Cadenas: resumen | cadenas.json (16 redes + RWA.xyz por cadena) | M$ (RWA, stablecoins), holders en unidades; nivel S del tercero |
| ETF cripto: flujos y patrimonio | etf-flujos.json (solo lectura) + serie Farside | AUM y flujos en M$ (el origen mezcla USD y miles de USD; se convierte); flujo no calculable = [VERIFICAR] |
| Fertilizantes y agua | fertilizantes-agua.json | USD/t y €/m³ |
| España: contratación pública | espana-contratacion.json | mil M€ y M€ (origen en euros, escala 1) |
| España: subvenciones (BDNS) | espana-subvenciones.json | mil M€ y M€; concesiones, no pagos |
| España: votaciones del Congreso | espana-votaciones.json | unidades y % |
| España: política y Congreso | espana-politica.json | personas / unidades |

Avisos heredados que se muestran tal cual: dos totales «adjudicado» distintos en contratación [VERIFICAR]; el fichero de diputados activos (137) no es el reparto de escaños [VERIFICAR].

Comprobación en el navegador integrado (http://localhost:8794, pestaña propia): `vDatos()` genera las 29 tarjetas, incluidas las 7 nuevas; consola sin errores; red: index, data.json y seguimiento.json 200 OK, sin 404; sin «NaN», «undefined» ni «null» en el texto.

## (b) Unidad y escala declaradas (valores sin tocar)
- `explorador/ocde-bis.json`: campo `unidad` de fichero y `unidad` en los 47 indicadores que no la tenían (tipo_oficial «% anual (fin de mes)», brecha_credito «puntos de PIB», vivienda_real «índice (base según país)»).
- `explorador/conflictos-gdelt.json`: `unidad` de fichero (% de artículos monitorizados; ratio sin unidad; días).
- `explorador/espana-empleados.json`: `unidad` de fichero (personas, escala 1; importes en EUR o M€ según campo).

## Pendiente / aviso
- Los generadores `scripts/leer_ocde_bis.py` y `scripts/leer_gdelt.py` reescriben esos JSON y borrarían la `unidad` en la próxima ejecución. No se tocaron (fuera de los ficheros autorizados); hay que añadir el campo en ellos (propuesta: copiar el texto de `unidad` y las tres unidades de BIS). Ver también `leer_ocde_bis.py`: la tabla `UNIDADES_BIS`.
- No tocados: vistas.html, etf-flujos.json, frescura.
- No se subió nada (sin commit ni push). `docs/movil/data.json` regenerado.
