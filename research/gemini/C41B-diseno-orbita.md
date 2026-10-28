# C41B · Diseño de una herramienta de investigación cripto-macro: vista independiente (Gemini con búsqueda de Google, sin Deep Research)

Coste: 1 consulta ligera (~15 fuentes). Sin fecha. Se hace aparte de C41A a propósito: Gemini NO conoce el repo ni nuestras propuestas, para tener una opinión independiente que luego fusiona C41C.
Flujo manual (CLAUDE.md «Flujo Gemini»): pegas el prompt en Gemini, pegas la respuesta en Claude; Claude la guarda cruda en `informes/gemini/AAAA-MM-DD-C41B-diseno.md`, comprueba 3-5 referencias abriéndolas y anota la sesión en `research/gemini-uso.json`.

## Prompt

```
USA LA BÚSQUEDA DE GOOGLE y abre cada enlace que cites. No respondas de memoria; si no puedes abrir un enlace, di que no lo abriste y marca VERIFICAR. Responde en español. No des recomendaciones de inversión.

Soy un inversor particular en España, largo plazo. Estoy construyendo para mi ordenador (no móvil) un panel de investigación con: una línea de tiempo por capas temáticas (regulación, stablecoins, tokenización, CBDC, deuda, energía, etc.), una tabla de países × temas (estado regulatorio, fiscalidad, legalidad de uso, ETF, custodia, staking, lending, colateral) con fuente y fecha en cada celda, paneles numéricos (tipos, bonos, calificaciones, IPC) y noticias con fecha de caducidad (24 h, 7 días, 30 días, fijas). Hoy son páginas HTML con ficheros JSON. Mi problema: mucha información, difícil de leer y de encontrar, y quiero que sea fácil de actualizar y de resumir.

TAREA (consulta ligera, máx. unas 15 fuentes):
1. Encuentra 8-10 webs o productos densos y comparativos que organicen información parecida (finanzas, cripto, datos públicos, periodismo de datos o comparadores regulatorios). Para cada una: URL abierta, qué patrón de organización usa (vista por país, línea de tiempo, tabla comparativa, filtros, semáforos, fichas, buscadores), qué hace bien y qué mal, y qué copiarías.
2. Propón cómo organizar y mostrar: (a) la vista comparativa país × tema; (b) la línea de tiempo por capas sin saturarla; (c) las noticias con caducidad; (d) cómo marcar la certeza de cada dato (fuente primaria, prensa, sin verificar).
3. Propón cómo estructurar los datos (campos comunes, un índice, un esquema) para que actualizar y resumir sea rápido y barato.
4. Máx. 8 mejoras ordenadas por utilidad/esfuerzo.
FORMATO: 3 líneas de resumen, luego una tabla de referencias (nombre | URL | patrón | copiar | evitar | etiqueta P/S/VERIFICAR), luego las propuestas numeradas. Etiquetas: P = abierto y leído; S = referencia de prensa; VERIFICAR = no confirmado. No inventes URLs ni capturas.
```
