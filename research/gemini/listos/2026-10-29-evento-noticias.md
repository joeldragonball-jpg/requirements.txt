# Gemini · Noticias del evento del 29-oct-2026 (listo para pegar)

Tipo: consulta ligera con búsqueda de Google (≈15 fuentes). Pégalo en Gemini, copia el JSON de respuesta y me lo das: lo guardo crudo en `informes/gemini/`, verifico 3-5 datos y solo lo verificado pasa a `noticias/manuales/`. Anotar en `research/gemini-uso.json`.

```
USA LA BÚSQUEDA DE GOOGLE para esta tarea (que se vean las fuentes de la respuesta). Cada noticia debe llevar un enlace que hayas abierto en esta misma respuesta; si no puedes buscar o abrir un enlace, dilo al principio y marca esa pieza VERIFICAR con la nota bajada. No respondas de memoria.

Eres un analista de investigación para un inversor particular en España (largo plazo; tiene XRP y XLM; sigue cripto, ETF, acciones y macro). Responde en español. Prefiere fuentes primarias (banco central, regulador, tribunal, comunicado de la empresa) y abre cada enlace que cites. No des recomendaciones de compra/venta.

TAREA (Evento: cierre del jueves 29-oct (BCE, PIB/PCE de EE. UU., caída de cripto)) del 2026-10-29: evento «Jueves 29-oct-2026»: (1) decisión del BCE de hoy (mantiene los tres tipos; depósito 2,50 %) y rueda de prensa de Lagarde (anuncia que deja la presidencia tras la reunión de febrero de 2027); (2) PIB de EE. UU. del 3T (avance) y PCE de septiembre; (3) la caída de hoy de cripto (BTC, ETH, XRP, XLM) y del Nasdaq: qué se dijo y qué causas están documentadas con fuente (si no hay causa documentada, dilo); (4) Banco de Japón (decisión el 30-oct) y Banco de Canadá (subió a 2,50 % el 28-oct). Para cada punto: qué se dijo o decidió, con la fuente primaria (comunicado, nota oficial, rueda de prensa) y hora; cifras frente a lo esperado; reacciones relevantes; bulos y desmentidos de las últimas 24 h; efecto en XRP, XLM, tipos y mercados solo si cambia la conclusión. Si el dato oficial aún no se ha publicado, dilo en «fiabilidad» y no lo des por hecho
Devuelve de 0 a 12 piezas, SOLO con nota >= 7 (los bulos, desde nota 5). Todas deben estar publicadas en el periodo que pide la tarea (por defecto, las últimas 24 h): una pieza más vieja NO entra aunque sea importante; antes de incluir cada una, comprueba su fecha de publicación. Si no hay nada que cumpla, devuelve "noticias": []. Consulta ligera: como máximo unas 15 fuentes y no repitas la búsqueda. Antes del JSON escribe 3 líneas: qué hay de nuevo, caso alcista / caso bajista y qué falta por verificar.
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

Etiquetas: [P] = leído en la fuente primaria; [S] = prensa o agregador; VERIFICAR = no pude confirmarlo. "evento" = "Evento: cierre del jueves 29-oct (BCE, PIB/PCE de EE. UU., caída de cripto)".
```
