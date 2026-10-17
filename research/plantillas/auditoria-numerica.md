# Plantilla: auditoría numérica (R38)

Salida: `informes/research/AAAA-MM-DD-R38-auditoria-numerica.md` (NO en `cerebro/`). No busca fuentes nuevas: recalcula lo que ya está escrito.

Método:
1. Recorrer `informes/research/*.md` (R13 en adelante), `informes/research/*matriz*`, `informes/2026-10-1*-{apertura,cierre}*.md` y las líneas nuevas de 2026-10-15 en adelante de `cerebro/documentos/` (Grep por números, %, M$, "×", "≈", "veces").
2. Para cada cifra derivada (porcentaje, suma, cociente, conversión a dólares, "N veces", plazos de N días, fechas de fin de semana), recalcularla con Python en el momento (script en el directorio temporal, no en el repo) usando solo los datos que el propio informe cita.
3. Tabla: archivo:línea | cifra tal como aparece | recálculo | ¿cuadra? | acción propuesta. Marcar "no recalculable" si faltan los datos de entrada.
4. Revisar en especial: porcentajes de circulación (XRP, XLM), cociente de 13F (acciones×precio), sumas de XRP en especie (Evernorth), conversiones a dólares con precio de una fecha concreta, plazos de 45, 60, 270 y 120 días, y días de la semana de cada fecha (comprobar con Python).
5. Reglas: HECHOS separados de OPINIONES; no reescribir ni borrar nada del cerebro; las correcciones se proponen y, con el visto bueno de Joel, se aplican solo como líneas nuevas bajo "## Correcciones AAAA-MM-DD"; sin recomendaciones de compra/venta; sin commit ni push.
6. Cierre: coste real en `research/COLA.md`; lecciones máx. 5 líneas en los tres archivos permitidos.
