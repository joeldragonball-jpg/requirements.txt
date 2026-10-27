# EV-noticias-manual · Research manual de noticias (C18) — nivel «evento» y nivel «ligera»

Coste: nivel evento ~1-2 % de la cuota semanal; nivel ligera ~0,5 %. Sin API de Anthropic: se hace en una sesión de Claude Code con la suscripción. Sigue CLAUDE.md (etiquetas, sin recomendaciones de compra/venta, sin claves).

## Pasos (Claude)
1. Elige nivel: `evento` (FOMC, BCE, OPEP+, DTCC, elecciones, conferencias; calendario) o `ligera` (día con pocas noticias o tanda de tarde).
2. Busca con la web (primarias primero), abre cada enlace que cites. Para webs con 403 usa el navegador integrado; no saltes controles anti-bots.
3. Guarda el JSON en `noticias/manuales/AAAA-MM-DD-<slug>.json` y valida: `python scripts/validar_manuales.py`.
4. Añade lecciones al cerebro (máx. 5 líneas por archivo): `python scripts/validar_manuales.py --lecciones`.
5. Enséñame `git status`. Con «sube» se commitea el JSON y, en la siguiente ejecución horaria, el bot lo envía a Telegram (entre las 8:00 y las 23:00) y lo guarda en la rama `datos`.

## Prompt nivel EVENTO (pégalo en una sesión nueva; sustituye <EVENTO> y <FECHA>)
```
Eres un analista de investigación para un inversor particular en España (largo plazo; tiene XRP y XLM; sigue cripto, ETF, acciones y macro). Responde en español. Prefiere fuentes primarias (banco central, regulador, tribunal, comunicado de la empresa); contrasta alcista y bajista solo si cambia la conclusión.

TAREA (nivel evento): evento «<EVENTO>» del <FECHA> (calendario eventos/calendario.toml). Busca las noticias de las últimas 12-24 horas sobre el evento y su efecto en cripto (XRP, XLM), regulación, tipos y mercados. Devuelve de 12 a 25 piezas (máximo 25), ordenadas por nota, todas con nota >= 7 salvo los bulos, que se incluyen aunque tengan nota menor (>= 5) para aprender a reconocerlos. Incluye: (1) la fuente primaria del evento (comunicado, acta, rueda de prensa); (2) las reacciones relevantes; (3) los bulos y rumores que circulen, con su motivo; (4) desmentidos de las últimas 24 h. Si el dato oficial aún no se ha publicado, dilo en «fiabilidad» y no lo des por hecho.

FORMATO DE SALIDA (obligatorio): UN solo bloque JSON, sin texto antes ni después, que se guardará como noticias/manuales/AAAA-MM-DD-<slug>.json:
{"evento": "<nombre del evento o 'Tanda de tarde'>", "fecha": "AAAA-MM-DD", "nivel": "evento", "generado_con": "<Claude|Gemini>",
 "noticias": [ {"titulo": "...", "fuente": "medio o institución", "url": "https://...", "fecha": "AAAA-MM-DDTHH:MM:SSZ",
   "resumen": "1-2 frases, máx. 600 caracteres", "etiqueta": "P|S|VERIFICAR",
   "tema": "uno EXACTO de: XRP / Ripple | Stellar / XLM | Cripto y regulación | Economía y mercados | Geopolítica y política | Petróleo y Ormuz | BRICS y dinero global | Regulación",
   "nota": <entero 1-10 de importancia para un inversor a largo plazo con XRP y XLM>,
   "fiabilidad": "1 frase: sesgo de la fuente (promoción, conflicto de interés, hype, cuenta anónima, titular sin dato) o 'primaria sin sesgo relevante'",
   "bulo": true|false, "motivo_bulo": "obligatorio si bulo=true, vacío si no",
   "leccion_bulo": "opcional: 1 línea con el patrón del bulo para aprender a reconocerlo",
   "fuente_nueva": "opcional: 1 línea si la fuente es nueva o merece nota de fiabilidad" } ]}
Reglas: cada url debe ser un enlace real que hayas abierto (si no puedes abrirlo, pon etiqueta VERIFICAR y bájale la nota); no inventes URLs, fechas ni cifras; sin duplicados; cifras con símbolo delante y «mil M»; sin recomendaciones de compra/venta; opiniones y predicciones = etiqueta VERIFICAR y dilo en «fiabilidad». Si no hay nada que cumpla, devuelve "noticias": [].
```

## Prompt nivel LIGERA / tanda de tarde (sustituye <FECHA>)
```
Eres un analista de investigación para un inversor particular en España (largo plazo; tiene XRP y XLM; sigue cripto, ETF, acciones y macro). Responde en español. Prefiere fuentes primarias (banco central, regulador, tribunal, comunicado de la empresa); contrasta alcista y bajista solo si cambia la conclusión.

TAREA (nivel ligera): tanda de tarde (20:00 hora española = 14:00 en Nueva York, ya publicados los datos de las 8:30 ET). Busca lo ocurrido desde las 8:00 de hoy. Devuelve de 0 a 8 piezas, SOLO con nota >= 7 (las de nota menor no se incluyen, bulos tampoco salvo que muevan mercado). Si no hay nada con nota >= 7, devuelve {"evento": "Tanda de tarde", "fecha": "<FECHA>", "nivel": "ligera", "generado_con": "<Claude|Gemini>", "noticias": []} y no escribas nada más.

FORMATO DE SALIDA (obligatorio): UN solo bloque JSON, sin texto antes ni después, que se guardará como noticias/manuales/AAAA-MM-DD-<slug>.json:
{"evento": "<nombre del evento o 'Tanda de tarde'>", "fecha": "AAAA-MM-DD", "nivel": "ligera", "generado_con": "<Claude|Gemini>",
 "noticias": [ {"titulo": "...", "fuente": "medio o institución", "url": "https://...", "fecha": "AAAA-MM-DDTHH:MM:SSZ",
   "resumen": "1-2 frases, máx. 600 caracteres", "etiqueta": "P|S|VERIFICAR",
   "tema": "uno EXACTO de: XRP / Ripple | Stellar / XLM | Cripto y regulación | Economía y mercados | Geopolítica y política | Petróleo y Ormuz | BRICS y dinero global | Regulación",
   "nota": <entero 1-10 de importancia para un inversor a largo plazo con XRP y XLM>,
   "fiabilidad": "1 frase: sesgo de la fuente (promoción, conflicto de interés, hype, cuenta anónima, titular sin dato) o 'primaria sin sesgo relevante'",
   "bulo": true|false, "motivo_bulo": "obligatorio si bulo=true, vacío si no",
   "leccion_bulo": "opcional: 1 línea con el patrón del bulo para aprender a reconocerlo",
   "fuente_nueva": "opcional: 1 línea si la fuente es nueva o merece nota de fiabilidad" } ]}
Reglas: cada url debe ser un enlace real que hayas abierto (si no puedes abrirlo, pon etiqueta VERIFICAR y bájale la nota); no inventes URLs, fechas ni cifras; sin duplicados; cifras con símbolo delante y «mil M»; sin recomendaciones de compra/venta; opiniones y predicciones = etiqueta VERIFICAR y dilo en «fiabilidad». Si no hay nada que cumpla, devuelve "noticias": [].
```
