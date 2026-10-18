# Mejoras del Explorador y de Actualidad (análisis del 18-oct-2026)

Estado: solo plan. Nada de esto está hecho. Sin IA salvo donde se indica.

## Hallazgos (medidos en explorador/datos.json: 8 capas, 37 movimientos)
1. **Bloques de texto pegado.** `produccion`, `piloto` y `plan` de cada capa son UNA cadena con varios hechos separados por «;» y etiquetas [P]/[S] dentro del texto. No se pueden desplegar ni filtrar.
2. **Cifras con etiqueta en minúscula** (`e: "países exploran una CBDC; ..."`): fuera de su caja parecen cortadas y no dicen el sujeto (qué moneda, empresa o fondo).
3. **Movimientos sin país, activo ni entidad.** Solo `actor` (texto libre) y `capa`. Imposible filtrar por XRP, Ripple, DTCC, país, etc.
4. **Capas con poca profundidad:** Depósitos tokenizados (5 claves, 2 cifras) y Regulación (12 claves pero casi todo de EE. UU.).
5. **Hueco negro arriba:** el mapa va en un iframe de altura fija (`components.html(height=860)` en explorador.py) más el relleno superior de Streamlit; la altura real la ajusta `ajustarAlto()` en mapa.html, que no cuenta la cabecera.

## Plan A: una sola pantalla (maquetación)
- Quitar el hueco superior: relleno superior 0 y cabecera de Streamlit oculta o transparente en el Explorador; altura del iframe = alto de ventana menos lo que quede.
- Subir a la franja superior del mapa, en una sola fila compacta: leyenda de colores (Regulación, CBDC…), calendario y línea de tiempo.
- Resultado: mapa arriba a pantalla completa; menús y secciones debajo.

## Plan B: datos con estructura (la base de todo lo demás)
- Hechos en lista: `{texto, estado[P/S/ESP/VERIFICAR], fecha, actor, pais, activos[], entidades[], fuente, informe}` en vez de cadenas con «;».
- Cifras: `{valor, unidad, sujeto, frase completa con mayúscula, fecha, fuente}`.
- Cada hecho: «Ver más» desplegable con contexto (qué pasó, quién, por qué importa, qué falta verificar), igual que el calendario.
- Script de calidad sin IA (`scripts/revisar_explorador.py`): avisa de textos sin mayúscula inicial, sin fuente, sin fecha, sin etiquetas o con [VERIFICAR] sin resolver.
- Chips pulsables (activo, entidad, país) que filtren mapa y listas.

## Plan C: Actualidad como mapamundi + lista debajo
- Misma pantalla única. Puntos por país; color = tema; tamaño = relevancia.
- Fuentes: noticias clasificadas por el bot (rama `datos`), eventos de `eventos/calendario.toml`, informes de research (ya por país). Las que envía Joel van marcadas «tuya».
- País por diccionario de palabras clave (sin IA). Campo `pais` en el clasificador del bot solo con permiso (gasta API).
- Entrada automática solo si hay fuente oficial o dato concreto; el resto, en la lista pero sin punto.
- Fiabilidad visible: oficial / medio / anónima (usar `noticias/senales-de-bulo.md`).

## Orden propuesto
1. A (maquetación): rápido, sin tokens de investigación.
2. B (estructura de datos) junto con el glosario del lunes.
3. C (mapamundi) después, v1 sin IA.
Probar siempre en local (puerto 8791) antes de subir; la app pública solo muestra Cartera.
