# D-bonos-ligera · Prompt de deuda y bonos para Gemini con búsqueda de Google (sin Deep Research)

Prueba del 27-oct-2026 (C20/Gemini): en vez de Deep Research (que hizo 200+ búsquedas y se salta el tope), una consulta ligera con la búsqueda de Google, como en NOTICIAS-DIA. Sustituye `<PAIS>`, `<FUENTES>`, `<PLAZOS>` y `<FECHA>`. Flujo manual (CLAUDE.md «Flujo Gemini»): lo pegas en Gemini → pegas la respuesta aquí → Claude la guarda cruda en `informes/gemini/AAAA-MM-DD-D-bonos-<pais>.md`, abre la fuente oficial para contrastar 3-5 cifras y anota la sesión en `research/gemini-uso.json`. Lo no contrastado queda [S]/[VERIFICAR].

Variantes: D01 Italia (Banca d'Italia BDS/infostat, MEF Tesoro, Borsa Italiana; 2, 5, 10, 30 a) · D02 Alemania (Bundesbank, Finanzagentur; 2, 5, 10, 30 a) · D03 Francia (AFT, Banque de France; 2, 5, 10, 30 a) · D05 España/Italia 30 años (Tesoro Público, Banco de España, MEF).

## Prompt

```
USA LA BÚSQUEDA DE GOOGLE para esta tarea y abre cada enlace que cites en esta misma respuesta. No respondas de memoria. Si no puedes abrir un enlace, di que no lo abriste y marca esa cifra VERIFICAR.

Eres un analista de investigación para un inversor particular en España (largo plazo). Responde en español. No des recomendaciones de compra/venta.

TAREA (<FECHA>): rendimientos de la deuda pública de <PAIS> a <PLAZOS> años.
Prefiere fuentes OFICIALES y abiertas: <FUENTES>. Consulta ligera: como máximo unas 15 fuentes en total y no repitas la búsqueda.
Para cada plazo da el último dato disponible: rendimiento (%), fecha exacta del dato, fuente y URL abierta. Distingue mercado secundario (diario) de subasta del Tesoro y dilo en cada fila.
Además, dime: (1) si la fuente oficial ofrece descarga abierta (CSV, SDMX, API, XLS), con la URL y el código o nombre de la serie; (2) el retraso con el que publica; (3) qué plazos NO has podido encontrar.

FORMATO DE SALIDA: primero 3 líneas (qué hay de nuevo, caso alcista / caso bajista de la deuda de <PAIS> con datos, qué falta por verificar); después UNA tabla en Markdown con las columnas:
| plazo | rendimiento % | fecha del dato | tipo (secundario/subasta) | fuente | URL | etiqueta |
Incluye SOLO bonos nominales a tipo fijo: excluye los indexados a inflación (BTPei, BTP Italia, OATi, Bundei) y los de menos de 1 año. Si en la subasta de un plazo hay dos títulos, usa el nominal. Antes de poner «no encontrado», revisa de nuevo las fuentes que ya abriste.
Etiquetas: P = leído en la fuente primaria oficial; S = prensa o agregador; VERIFICAR = no confirmado.
Reglas: no inventes cifras, fechas ni URLs; si un plazo no aparece, escribe «no encontrado» en su fila; cifras con símbolo %; opiniones y predicciones = VERIFICAR.
```
