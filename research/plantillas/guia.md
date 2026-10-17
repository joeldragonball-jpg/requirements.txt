# Plantilla: guía práctica (G17 y siguientes)

Salida: `informes/dossiers/AAAA-MM-DD-G<n>-<tema-en-minusculas>.md` (documento NUEVO; no reescribir nada de `cerebro/`) y una fila en `informes/dossiers/MAPA.md` (solo añadir).

Estilo de la serie G: explicación clara, tablas cortas, ejemplos con cifras propias marcadas "cálculo mío", etiquetas [VERIFICAR] / [ESPECULACIÓN] / [VERIFICADO fecha], separación de HECHOS y OPINIONES, sin recomendaciones de compra/venta. Pensada para imprimir (4-6 páginas, A4).

Para G17 (cómo verificar noticias cripto):
1. Leer con Grep, por partes, las líneas de lección de 2026-10-14 en adelante de `cerebro/documentos/patrones-de-bulos.md`, `fuentes-fiables-y-dudosas.md` y `catalizadores-xrp-xlm.md`, y las secciones de errores de `informes/research/*R21b*`, `*R22*`, `*R31*`, `*R38*`.
2. Agrupar por tipo de error (fecha, cifra, fuente, serie, intervalo, atribución, resumen más fuerte que la tabla, eco entre medios, titular reciclado) y por qué fuentes abren y cuáles no.
3. Estructura: Resumen (5 líneas) · Las 10 preguntas antes de creer una cifra · Tabla de fuentes (abre/no abre, tipo A-D) · Errores reales que cometimos (Goldman/XRPR, 473 M, 10:34 vs 09:34 UTC, series de Brent, 36 h vs 24 h) y cómo se detectaron · Plantilla de comprobación de una cifra (paso a paso con Python y curl) · Dudas y datos a verificar.
4. No inventar ejemplos: usar solo los errores ya documentados, con enlace al informe de origen.
5. Cierre: coste real en `research/COLA.md`; lecciones máx. 5 líneas; sin commit ni push.
