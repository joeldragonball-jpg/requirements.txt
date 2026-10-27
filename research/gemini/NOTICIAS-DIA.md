# NOTICIAS-DIA · Prompt único de noticias para Gemini (sustituye a G01-G06, EV-noticias-ligera, EV-noticias-evento y EV-post-evento)

Un solo prompt con el **tema del día**. Flujo manual (CLAUDE.md «Flujo Gemini»): el Seguimiento del móvil te da el prompt con el tema de hoy ya puesto (puedes cambiar de tema con las etiquetas) → lo copias y lo pegas en la app de Gemini → pegas la respuesta (o la subes a Drive) → Claude la guarda cruda en `informes/gemini/AAAA-MM-DD-NOTICIAS-DIA-<tema>.md`, verifica 3-5 datos con la fuente primaria y solo lo verificado pasa a `noticias/manuales/` (formato C18). Consulta ligera (unas 15 fuentes). Se anota en `research/gemini-uso.json` (sesión con prompt «NOTICIAS-DIA · <id del tema>»).

## Temas (los lee `scripts/construir_seguimiento.py`; formato: `id` | nombre | tarea | máx. piezas | extra)
Rotación diaria: lunes y domingo xrp-xlm, martes macro-tipos, miércoles cripto-regulacion, jueves etf-flujos, viernes bulos, sábado energia-geopolitica. Si hay un evento de impacto alto en ±1 día, manda `evento`. `tarde` es la tanda de las 20:00 hora española.

- `xrp-xlm` | Noticias XRP / XLM de las últimas 24 h | busca Ripple, XRP, XRPL, Stellar, XLM, SDF: anuncios, alianzas, litigios, ETF y movimientos on-chain relevantes; incluye lo que dicen las fuentes oficiales (ripple.com, stellar.org) frente a lo que cuentan cuentas de X o canales de YouTube. | 8 |
- `macro-tipos` | Macro y tipos | busca tipos de interés y datos macro: Fed, BCE, Banco de Japón, Banco de Inglaterra; inflación, empleo, PIB, rendimientos de bonos del Tesoro y del Bund de las últimas 24 h; calendario de las próximas 48 h. | 8 |
- `cripto-regulacion` | Cripto y regulación | busca regulación cripto en EE. UU. (SEC, CFTC, Congreso, OCC), UE (MiCA, ESMA, AMLR), Reino Unido, Asia y organismos (BIS, FSB, FMI, GAFI) de los últimos 1-2 días; textos oficiales, no solo prensa. | 8 |
- `etf-flujos` | ETF y flujos | busca ETF cripto al contado (XRP, SOL, BTC, ETH, XLM si existen): solicitudes, aprobaciones, flujos diarios de entrada y salida, activos bajo gestión; cifras de la gestora o de datos de mercado con fecha. | 8 |
- `bulos` | Bulos y desmentidos de la semana | busca bulos, rumores y desmentidos de los últimos 7 días sobre XRP, XLM, cripto y regulación: qué circuló, quién lo difundió (cuenta anónima, promoción, hype), qué dice la fuente primaria y si se corrigió. En este tema `bulo: true` es lo habitual y se incluyen aunque la nota sea 5-6. | 8 | (los bulos, desde nota 5)
- `energia-geopolitica` | Energía y geopolítica | busca petróleo (Brent, WTI), Ormuz, OPEP+, sanciones, BRICS y dinero global, conflictos con efecto en mercados de las últimas 24 h; datos de EIA, OPEP, AIE o gobiernos con fecha. | 8 |
- `tarde` | Tanda de tarde | tanda de tarde (20:00 hora española = 14:00 en Nueva York, ya publicados los datos de las 8:30 ET): busca lo ocurrido desde las 8:00 de hoy en cripto, XRP, XLM, regulación, tipos y mercados. | 8 |
- `evento` | Evento: <EVENTO> | evento «<EVENTO>»: qué se dijo, decidió o anunció, con la fuente primaria (comunicado, acta, nota oficial, rueda de prensa) y hora; cifras frente a lo esperado; reacciones relevantes; bulos y desmentidos de las últimas 24 h; efecto en XRP, XLM, tipos y mercados solo si cambia la conclusión. Si el dato oficial aún no se ha publicado, dilo en «fiabilidad» y no lo des por hecho. | 12 | (los bulos, desde nota 5)

## Prompt (el script sustituye <NOMBRE>, <FECHA>, <TAREA>, <MAX> y <EXTRA>)

```
USA LA BÚSQUEDA DE GOOGLE para esta tarea (que se vean las fuentes de la respuesta). Cada noticia debe llevar un enlace que hayas abierto en esta misma respuesta; si no puedes buscar o abrir un enlace, dilo al principio y marca esa pieza VERIFICAR con la nota bajada. No respondas de memoria.

Eres un analista de investigación para un inversor particular en España (largo plazo; tiene XRP y XLM; sigue cripto, ETF, acciones y macro). Responde en español. Prefiere fuentes primarias (banco central, regulador, tribunal, comunicado de la empresa) y abre cada enlace que cites. No des recomendaciones de compra/venta.

TAREA (<NOMBRE>) del <FECHA>: <TAREA>
Devuelve de 0 a <MAX> piezas, SOLO con nota >= 7<EXTRA>. Todas deben estar publicadas en el periodo que pide la tarea (por defecto, las últimas 24 h): una pieza más vieja NO entra aunque sea importante; antes de incluir cada una, comprueba su fecha de publicación. Si no hay nada que cumpla, devuelve "noticias": []. Consulta ligera: como máximo unas 15 fuentes y no repitas la búsqueda. Antes del JSON escribe 3 líneas: qué hay de nuevo, caso alcista / caso bajista y qué falta por verificar.
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

Etiquetas: [P] = leído en la fuente primaria; [S] = prensa o agregador; VERIFICAR = no pude confirmarlo. "evento" = "<NOMBRE>".
```
