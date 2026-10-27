# G03-macro-tipos · Rutina G: Macro y tipos — prompt para Gemini (C20)

Flujo manual (CLAUDE.md «Flujo Gemini»): Claude te da este prompt (con <FECHA> rellena) → lo pegas en la app de Gemini → pegas la respuesta o la subes a Drive → Claude la guarda cruda en `informes/gemini/AAAA-MM-DD-G03.md`, contrasta las 3-5 afirmaciones de mayor impacto con la fuente primaria y solo lo verificado pasa a `noticias/manuales/` (formato de C18). Máx. 1 por día. Si Gemini avisa de límite (o llegas al 80 %), para y anótalo en `research/gemini-uso.json`.

```
USA LA BÚSQUEDA DE GOOGLE para esta tarea (que se vean las fuentes de la respuesta). Cada noticia debe llevar un enlace que hayas abierto en esta misma respuesta; si no puedes buscar o abrir un enlace, dilo al principio y marca esa pieza VERIFICAR con la nota bajada. No respondas de memoria.

Eres un analista de investigación para un inversor particular en España (largo plazo; tiene XRP y XLM; sigue cripto, ETF, acciones y macro). Responde en español. Prefiere fuentes primarias (banco central, regulador, tribunal, comunicado de la empresa) y abre cada enlace que cites. No des recomendaciones de compra/venta.

TAREA (rutina G · Macro y tipos) del <FECHA>: busca tipos de interés y datos macro: Fed, BCE, Banco de Japón, Banco de Inglaterra; inflación, empleo, PIB, rendimientos de bonos del Tesoro y del Bund de las últimas 24 h; calendario de las próximas 48 h.
Devuelve de 0 a 8 piezas, SOLO con nota >= 7. Si no hay nada que cumpla, devuelve "noticias": []. Consulta ligera: como máximo unas 15 fuentes y no repitas la búsqueda. Antes del JSON escribe 3 líneas: qué hay de nuevo, caso alcista / caso bajista y qué falta por verificar.
FORMATO DE SALIDA (obligatorio): UN solo bloque JSON, sin texto antes ni después, que se guardará como noticias/manuales/AAAA-MM-DD-<slug>.json:
{"evento": "<nombre del evento o 'Tanda de tarde'>", "fecha": "AAAA-MM-DD", "nivel": "ligera", "generado_con": "Gemini",
 "noticias": [ {"titulo": "...", "fuente": "medio o institución", "url": "https://...", "fecha": "AAAA-MM-DDTHH:MM:SSZ",
   "resumen": "1-2 frases, máx. 600 caracteres", "etiqueta": "P|S|VERIFICAR",
   "tema": "uno EXACTO de: XRP / Ripple | Stellar / XLM | Cripto y regulación | Economía y mercados | Geopolítica y política | Petróleo y Ormuz | BRICS y dinero global | Regulación",
   "nota": <entero 1-10 de importancia para un inversor a largo plazo con XRP y XLM>,
   "fiabilidad": "1 frase: sesgo de la fuente (promoción, conflicto de interés, hype, cuenta anónima, titular sin dato) o 'primaria sin sesgo relevante'",
   "bulo": true|false, "motivo_bulo": "obligatorio si bulo=true, vacío si no",
   "leccion_bulo": "opcional: 1 línea con el patrón del bulo para aprender a reconocerlo",
   "fuente_nueva": "opcional: 1 línea si la fuente es nueva o merece nota de fiabilidad" } ]}
Reglas: cada url debe ser un enlace real que hayas abierto (si no puedes abrirlo, pon etiqueta VERIFICAR y bájale la nota); no inventes URLs, fechas ni cifras; sin duplicados; cifras con símbolo delante y «mil M»; sin recomendaciones de compra/venta; opiniones y predicciones = etiqueta VERIFICAR y dilo en «fiabilidad». Si no hay nada que cumpla, devuelve "noticias": [].

Etiquetas: [P] = leído en la fuente primaria; [S] = prensa o agregador; VERIFICAR = no pude confirmarlo. "evento" = "Rutina G · Macro y tipos".
```
