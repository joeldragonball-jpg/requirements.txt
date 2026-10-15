# Plantilla: auditoría de coherencia y afirmaciones (R22, modelo Opus)

Salida: `informes/research/AAAA-MM-DD-R22-auditoria-coherencia.md` (NO en `cerebro/`). No es repetir el research: es revisar lo ya escrito con criterio.

Entradas (leer con Glob/Grep y por partes; no releer lo innecesario): `informes/research/*.md` (R02P a R12P, R21 si existe, calendarios), las líneas nuevas de 2026-10-14/15 en `cerebro/documentos/` (catalizadores, fuentes, patrones y las "Correcciones 2026-10-15"), `research/COLA.md`.

Tareas:
1. CONTRADICCIONES entre informes: misma fecha, cifra o estado con valores distintos (p. ej. fechas de SEC, Nexus, Evernorth, BCB, MAS). Tabla: tema | informe A dice | informe B dice | cuál tiene mejor fuente | acción propuesta.
2. SOBREAFIRMACIONES: frases dadas como hecho que solo tienen fuente secundaria, de parte interesada (Ripple, SDF, exchanges) o de una sola fuente. Tabla: frase | archivo:línea | fuente | cómo debería etiquetarse.
3. ETIQUETAS: cifras sin [VERIFICAR] que debieran tenerlo, y [VERIFICAR] ya resueltos por otro informe.
4. MUESTREO: elegir las 10 afirmaciones que más pesan en la tesis de Joel (sin escribir su tesis; usar solo lo público: precio, ETF, regulación, catalizadores) y re-verificarlas con fuente primaria cuando abra; anotar PRIM-LEÍDA / EXTRACTO / SECUND.
5. LECCIONES del cerebro: duplicadas, contradictorias o demasiado largas; proponer recortes SIN aplicar.
6. HUECOS por impacto: lista ordenada de documentos primarios que Joel debería descargar a `research/fuentes/` (URL y nombre de archivo sugerido).
7. Conclusión: nivel de confianza global (alto/medio/bajo) por área (macro, regulación por región, Ripple/Stellar, calendario) con una frase de por qué.

Reglas: separar HECHOS de OPINIONES; no recomendar compra/venta; NO reescribir ni borrar nada del cerebro; las correcciones se proponen y, solo con visto bueno de Joel, se aplican añadiendo líneas nuevas bajo "## Correcciones AAAA-MM-DD". No hacer commit ni push. Cierre: coste real en `research/COLA.md` (diferencia de % semanal) y lecciones máx. 5 líneas.
