# Plantilla: research con Gemini (Deep Research) para verificar después con Claude

Reparto: **Gemini** hace la búsqueda amplia en la web y la primera redacción; **Claude** verifica las fuentes, cruza con lo que ya hay en el repo e integra los datos buenos (Explorador, radar, fichas). Todo lo que traiga Gemini entra como **[S]** (secundaria) hasta que Claude compruebe sus fuentes.

## 1. Cómo usarla (Joel)
1. En Gemini, activa **Deep Research** y pega el prompt de la sección 2, cambiando solo la línea «TEMA».
2. Cuando termine, **exporta a Google Docs** y guarda el documento en la carpeta de Drive «Gemini research», con el nombre `AAAA-MM-DD tema`.
3. En una sesión de Claude escribe: «Lee en mi Drive el documento `AAAA-MM-DD tema` y verifícalo con la plantilla de Gemini.» Claude lo lee con el conector de Google Drive; no hace falta copiar y pegar.
4. Claude guarda el resultado verificado en `informes/gemini/AAAA-MM-DD-tema.md` y actualiza los datos del Explorador si procede.
Lo que pegues en Gemini lo procesa Google: no pegues datos personales ni tu tesis.

## 2. Prompt para Gemini (copiar y pegar)
```
Eres un analista de investigación. Responde en español, claro y práctico. NO des recomendaciones de compra, venta ni mantenimiento, ni predicciones de precio.

TEMA: [escribe aquí el tema y el periodo; por ejemplo «estado de la CLARITY Act en el Senado de EE. UU. y calendario previsto, a fecha de hoy»]

Marco: investigación sobre activos digitales (XRP, XLM, stablecoins, CBDC, tokenización) con enfoque global. Contrasta TRES perspectivas: (a) fuentes oficiales (reguladores, bancos centrales, textos legales, la propia empresa); (b) despachos de abogados y analistas; (c) voces críticas (BIS, FMI, FSB, académicos). Prefiere la fuente primaria y la más reciente. Hipótesis de trabajo neutra para enmarcar: «la infraestructura financiera migra a rieles blockchain»; busca evidencia a favor y evidencia en contra.

Entrega EXACTAMENTE estas secciones:
1. Resumen (máximo 6 líneas).
2. Hechos verificables: tabla con columnas Dato | Fecha del dato | Fuente (nombre y enlace completo) | Tipo de fuente (oficial / despacho / prensa / agregador).
3. Opiniones y especulaciones, separadas de los hechos y marcadas [ESPECULACIÓN].
4. Contradicciones entre fuentes: qué dice cada una y en qué difieren.
5. Qué NO he podido comprobar (páginas que no abrieron, datos sin fuente primaria) [VERIFICAR].
6. Sesgos de las fuentes: promoción, conflicto de interés, hype, cuentas anónimas, titulares sin dato.
7. Lista de fuentes consultadas con enlace y fecha de acceso.

Reglas: cita fuente y fecha de CADA dato; no inventes enlaces ni cifras; si no lo encuentras, escribe «no consta» en vez de suponer; si dos fuentes se contradicen, di cuál prevalece y por qué.
```

## 3. Lista de verificación para Claude (no gastar más de lo necesario)
1. **Abre las fuentes de los 5 datos más importantes** y comprueba que el enlace existe y dice lo que Gemini afirma (WebFetch). Si no abre (403, captcha, caído), el dato queda [VERIFICAR]; no lo des por bueno.
2. **Cruza con el repo** con `python scripts/buscar_informes.py "tema"`: ¿coincide con lo que ya consta? Las contradicciones se anotan, no se resuelven a favor de Gemini por defecto.
3. **Etiqueta cada dato:** [P] solo si la fuente primaria se abrió y se leyó; [S] si es prensa, despacho o agregador; [VERIFICAR] si no se pudo comprobar.
4. **Marca lo que parece inventado:** enlaces que no existen, cifras sin fuente, citas literales que no aparecen en la página.
5. **Integra** solo lo verificado: datos del Explorador o del radar (`explorador/regulacion.json`) con fuente, fecha y nivel. Revisa con `python scripts/revisar_explorador.py`.
6. Guarda el informe en `informes/gemini/AAAA-MM-DD-tema.md` con una cabecera: «Fuente: Gemini Deep Research (AAAA-MM-DD). Verificado por Claude el AAAA-MM-DD: N datos comprobados, M sin comprobar.»
7. Nada de la tesis personal de Joel en estos archivos (repo público).

## 4. Qué le conviene a cada uno
- **Gemini:** búsqueda web amplia, comparar muchas fuentes, resumir PDFs largos, preguntas sobre las 21 fuentes de la libreta de NotebookLM, audio y tarjetas de estudio.
- **Claude:** código, datos estructurados (JSON), verificar y cruzar, aplicar las etiquetas, revisión de seguridad.

## 5. Atajo ya montado en Drive (19-oct-2026)
En el Drive de Joel hay una carpeta «Gemini research» con: «00 LEEME», «01 Prompt maestro» (para pegar una vez en un Gem de Gemini; incluye la lista de temas T01 a T25) y la subcarpeta «Resultados». Joel solo escribe «Tema T04» en el Gem y mueve el resultado a «Resultados». Claude lo lee con el conector de Google Drive, verifica con la lista de la sección 3 y guarda el informe en `informes/gemini/`. Si cambian los temas, hay que actualizar el documento 01 en Drive y esta plantilla.

## 6. Qué modelo de Gemini usar (plan Google AI Plus; referencia del 19-oct-2026, los límites cambian)
- Primera pasada de casi todo (calendarios, resúmenes, tablas, actualizar datos): **3.6 Flash**, razonamiento medio.
- Textos legales o fuentes que se contradicen (T01 a T07, T16, T20, T21): **3.1 Pro**, razonamiento alto (sigue en versión preliminar).
- Consulta suelta sobre un dato: 3.6 Flash, razonamiento bajo. Temas muy grandes (T01, T04, T14, T15): Deep Research.
- Regla: empezar con Flash medio y repetir con Pro alto si hay contradicciones o datos sin fuente. Ningún modelo está libre de citas inventadas: Claude verifica siempre.
