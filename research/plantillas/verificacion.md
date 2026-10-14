# Plantilla: verificación en bloque

Salida: `informes/research/AAAA-MM-DD-<ID>-verificacion.md`.

Pasos:
1. Reunir los [VERIFICAR] pendientes con Grep en `informes/dossiers/`, `informes/` y `cerebro/documentos/` (no leer archivos grandes enteros; `cerebro/apuntes_*.md` solo con Grep). Listar archivo, línea y afirmación.
2. Agrupar por tema y priorizar las que afectan a cifras, fechas o cifras fiscales.
3. Para cada una: buscar la fuente primaria en su idioma original y resolverla con una de tres salidas: CONFIRMADO (fuente, fecha), CORREGIDO (dato correcto) o SIGUE SIN VERIFICAR (qué se intentó).
4. Antes de cambiar un archivo existente: no reescribir cerebro/; en dossiers/guías, cambiar solo la etiqueta o la cifra afectada y avisarme del diff. No borrar contenido.
5. Informe: tabla `archivo:línea | afirmación | resultado | fuente | fecha`.
6. Anotar coste real en `research/COLA.md`.
