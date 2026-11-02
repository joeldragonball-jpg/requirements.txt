# Gemini · Elecciones de mitad de mandato de EE. UU. (3-nov-2026) · listo para pegar

Tipo: consulta ligera con búsqueda de Google (≈15 fuentes), tema `evento` de `research/gemini/NOTICIAS-DIA.md`. NO lanzado. Pégalo en Gemini cuando quieras (antes del cierre de urnas del 3-nov vale como previa; después de los resultados, vuelve a pegarlo cambiando la fecha). Luego sigue la rutina diaria de `informes/research/2026-11-02-C36-rutina-noticias.md`.

```
USA LA BÚSQUEDA DE GOOGLE para esta tarea (que se vean las fuentes de la respuesta). Cada noticia debe llevar un enlace que hayas abierto en esta misma respuesta; si no puedes buscar o abrir un enlace, dilo al principio y marca esa pieza VERIFICAR con la nota bajada. No respondas de memoria.

Eres un analista de investigación para un inversor particular en España (largo plazo; tiene XRP y XLM; sigue cripto, ETF, acciones y macro). Responde en español. Prefiere fuentes primarias (banco central, regulador, tribunal, comunicado de la empresa) y abre cada enlace que cites. No des recomendaciones de compra/venta.

TAREA (Evento: EE. UU.: elecciones de mitad de mandato) del 2026-11-03: evento «EE. UU.: elecciones de mitad de mandato» (martes 3-nov-2026): qué se dijo, decidió o anunció, con la fuente primaria (comunicado, acta, nota oficial, rueda de prensa) y hora; cifras frente a lo esperado; reacciones relevantes; bulos y desmentidos de las últimas 24 h; efecto en XRP, XLM, tipos y mercados solo si cambia la conclusión. Si el dato oficial aún no se ha publicado, dilo en «fiabilidad» y no lo des por hecho. Si lanzas la consulta antes del cierre de urnas, cubre lo previo: encuestas y su margen de error, horas de cierre por estado, qué escaños/gobernaciones deciden el control de la Cámara y el Senado, calendario del recuento y de las fechas de certificación, y qué dicen los textos oficiales (Congreso, estados) sobre la CLARITY Act y el presupuesto en la sesión posterior (lame-duck). Separa encuesta/proyección (opinión) de resultado oficial (hecho). Incluye lo que digan las fuentes oficiales de cada estado frente a lo que cuentan medios o cuentas de X.
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

Etiquetas: [P] = leído en la fuente primaria; [S] = prensa o agregador; VERIFICAR = no pude confirmarlo. "evento" = "Evento: EE. UU.: elecciones de mitad de mandato".
```
