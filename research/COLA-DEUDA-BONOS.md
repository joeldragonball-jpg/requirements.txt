# Cola de research: deuda soberana, bonos y bancos (22-oct-2026)

Para completar la capa «Deuda soberana y bonos» del mapa de órbitas y los paneles «Bonos y curvas» y «Deuda pública». Prioridad de países (pedido de Joel): **España, Francia, Italia, Japón y Estados Unidos**, luego **China** y la **Unión Europea**; el resto, poco.

Reglas: fuente oficial y abierta primero ([P]); lo que solo salga de un agregador o de prensa va [S]; si no se puede verificar, [VERIFICAR]. Sin recomendaciones. Todo dato lleva fecha y fuente. Nada de la tesis de Joel.

## Qué hay ya (22-oct)
| País | 3 m–1 a | 2–5 a | 10 a | 15–30 a | Fuente |
|---|---|---|---|---|---|
| España | sí (letras 3 m y 1 a) | 3 y 5 a | sí | 15 a | Banco de España, API `app.bde.es/bierest` (series D_DTES00B7, D_DTES00U7, D_G0B1F0ZN/ZO/ZP/ZQ) |
| Francia | no | no | TEC 10 (manual) | no | AFT, web (bloquea curl; hay que abrirla con navegador) |
| EE. UU. | 1 m, 3 m, 6 m, 1 a | 2 y 5 a | sí | 30 a | Tesoro de EE. UU., CSV diario |
| Japón | 1 a | 2, 3, 5 a | sí | 20 y 30 a | Ministerio de Finanzas, CSV |
| Zona euro (AAA) | 3 m, 1 a | 2 y 5 a | sí | 30 a | BCE, API de la curva de rendimientos |
| Reino Unido | no | 5 a | sí | 20 a | Banco de Inglaterra, series IUDSNPY, IUDMNPY, IUDLNPY |
| Alemania, Francia, Italia, España (mensual) | — | — | media mensual | — | BCE, serie IRS (con ~1 mes de retraso) |

## Cola

| ID | Qué buscar | Prioridad | Modelo y esfuerzo | Cómo | Entregable |
|---|---|---|---|---|---|
| D01 | **Italia**: rendimientos diarios de BTP a 2, 5, 10 y 30 años con fuente oficial abierta (Banca d'Italia BDS/infostat, MEF Tesoro, Borsa Italiana datos oficiales) | Alta | Claude Sonnet, esfuerzo medio (sesión con Chrome) | Probar APIs con curl y navegador; ver si hay CSV o SDMX | URL o código de serie, formato, retraso, y si se puede bajar sin IA desde GitHub | | **Parcial 27-oct (prueba Gemini con búsqueda de Google):** subastas BTP 5 a (4,08 %, 29-sep) y 10 a (4,10 %, 28-ago) leídas en los PDF del MEF; 2 a de subasta 3,55 % (27-oct, Teleborsa [S]); 4,509 % a 10 a secundario [S]; faltan serie diaria abierta y 30 a nominal. Ver `informes/gemini/2026-10-27-D01-bonos-italia.md`.
| D02 | **Alemania**: rendimientos diarios de Bund (2, 5, 10, 30 a): Bundesbank (API de series temporales) o Finanzagentur | Alta | Claude Sonnet, medio | La API del Bundesbank no respondió desde este equipo el 22-oct: probar con navegador y desde otra red | Ídem | | **Parcial 27-oct (prueba Gemini con búsqueda de Google):** 10 a secundario 3,36 % y 30 a subasta 3,80 % (14-oct) confirmados [S]; el 2 a 3,08 % de subasta del 27-oct sin confirmar (último Schatz hallado: 6-oct, 3,10 %, cobertura 1,1); PDF de la Bundesbank no abren desde este equipo. Ver `informes/gemini/2026-10-27-D02-bonos-alemania.md`.
| D03 | **Francia**: curva OAT por plazos (2, 5, 10, 30 a) además del TEC 10 y descarga automática o semiautomática | Alta | Claude Sonnet, medio | AFT da 403 a curl: probar su fichero «OATs key figures» (XLS) por navegador | Ídem | **Hecho 26-oct (parcial):** puntos de subasta AFT a 4-22 años en `informes/research/2026-10-26-W02-deuda-d03-francia.md`; faltan 2 y 30 años [VERIFICAR].
| D04 | **China**: rendimientos de los bonos del Estado (1, 2, 5, 10, 30 a) de ChinaBond/ChinaMoney, PBoC o Ministerio de Finanzas | Alta | Claude Sonnet, alto (webs en chino) | `yield.chinabond.com.cn` carga pero su API da 405 a curl: inspeccionar con el navegador | Ídem, marcando [P]/[S] |
| D05 | **30 años de España e Italia** (y Francia si D03 no lo trae): bono a 30 años, secundario | Media | Claude Sonnet, bajo | El Banco de España publica hasta 15 años: ver el Tesoro Público (subastas del bono a 30 años) y el MEF | Datos de subasta como alternativa (rendimiento y fecha) |
| D06 | **Bancos y deuda**: (a) HECHO el 22-oct: exposición soberana de 116 bancos europeos (EBA, corte 30-jun-2025; `scripts/preparar_bancos_eba.py`, panel «Deuda por banco»); queda (a2) cortes más recientes del Pillar 3 Data Hub de la EBA y el alcance exacto de «soberano» en la guía de la EBA; (b) y (c) HECHOS el 22-oct (deuda emitida por cada banco desde la misma EBA; balances de Fed, Eurosistema y Banco de Japón; informe `informes/research/2026-10-22-D06-bancos-y-deuda.md`); queda el detalle de cada emisión (folletos) | Media | Gemini 3.1 Pro, Deep Research, nivel alto + verificación de Claude | Pegar el prompt D06 | Informe `informes/gemini/AAAA-MM-DD-deuda-bancos.md` |
| D07 | HECHO el 22-oct (`informes/research/2026-10-22-D07-quien-compra-y-vende-deuda.md` y pestaña «Reservas y bancos centrales»; faltan Japón TIC de agosto, China sept. y zona euro). **Quién compra y vende deuda de otros países** (panel 5): tenencias de Japón, China, zona euro; reservas (COFER del FMI, SAFE, MoF Japón, BCE) | Media | Gemini 3.1 Pro, Deep Research, alto; después Claude verifica | Pegar el prompt D07 | Informe verificado y tabla de series abiertas |
| D08 | HECHO el 24-oct (`informes/research/2026-10-24-D08-subastas-deuda.md`; EE. UU., Japón, España y Francia; falta Italia). **Calendario de subastas** de deuda de España, Francia, Italia, Japón y EE. UU. con fechas del próximo trimestre | Media | Claude Sonnet, bajo | Calendarios oficiales (Tesoro, AFT, MEF, MoF, TreasuryDirect) | Eventos nuevos en `eventos/calendario.toml` |
| D09 | HECHO el 22-oct (`informes/research/2026-10-22-D09-calificaciones-soberanas.md`; tabla en «Deuda pública»). **Calificaciones soberanas** de los 7 países (S&P, Moody's, Fitch) y su última acción | Baja | Gemini 3.6 Flash medio + Claude verifica | Prompt D09; las agencias son [P] pero de pago: lo público es el comunicado | Tabla con fecha |

Estado (22-oct noche): D06, D07 y D09 hechos por Claude en vez de Gemini (con fuentes oficiales y sin Deep Research). Pendientes D01-D05 y D08 (Claude con Chrome, ≈ 1 % semanal cada una).

## Prompts guardados

### Prompt para Claude (D01-D05; sesión nueva con la carpeta del repo)
```
Sesión corta (máx. 20 min). Lee research/COLA-DEUDA-BONOS.md y la guía research/GUIA-ESTILO-CIFRAS.md. Haz la tarea [D0X].
Objetivo: encontrar una fuente OFICIAL y ABIERTA de rendimientos diarios de bonos del Estado [país] a los plazos indicados, y comprobar que se puede descargar sin IA (curl o urllib) para añadirla a scripts/actualizar_paneles.py.
Pasos: (1) busca el portal oficial (banco central, tesoro o agencia de deuda); (2) prueba curl con User-Agent; si da 403, abre la página en el navegador integrado y localiza la URL de la API o del archivo; si hace falta, baja el PDF con fetch dentro de la página y léelo con pdf.js; (3) comprueba que el último dato coincide con la web oficial; (4) anota código de serie, formato, plazos disponibles, retraso y si hay captcha.
Reglas: no saltes controles anti-bots (Cloudflare, captcha): si aparecen, para y dilo. Marca [P] lo oficial y [S] lo demás. Sin recomendaciones de inversión. No hagas commit ni push.
Entrega: 8 líneas con la fuente, el código y el estado, y el trozo de código de lectura listo para pegar en scripts/actualizar_paneles.py (función leer_bonos).
```

### Prompt D06 para Gemini (Deep Research; pegar completo)
```
Eres un analista de investigación. Responde en español, claro y práctico. NO des recomendaciones de compra, venta ni mantenimiento, ni predicciones de precio.

TEMA: deuda de los bancos y de los Estados que figura a nombre de cada banco, a fecha de octubre de 2026. Cubre (a) la exposición de bancos europeos concretos a deuda soberana (España, Francia, Italia, Alemania, EE. UU., Japón, China) según el último ejercicio de transparencia de la EBA (Autoridad Bancaria Europea) y los informes del BCE (supervisión bancaria), con una tabla por banco: nombre, país, exposición a cada soberano en miles de millones de euros, fecha; (b) la deuda emitida por los grandes bancos de España, Francia, Italia, Japón y EE. UU. (bonos, subordinada, AT1) con importes y vencimientos principales según sus propios informes anuales o folletos; (c) el balance de los bancos centrales del BCE, la Fed y el Banco de Japón (cuánta deuda soberana tienen y su variación en los últimos 12 meses, con la fuente oficial).

Marco: panel de datos de un inversor particular en España que sigue macro, cripto y deuda. Prioridad de países: España, Francia, Italia, Japón y EE. UU.; luego China y la UE.

Entrega EXACTAMENTE estas secciones:
1. Resumen (máximo 6 líneas).
2. Hechos verificables: tabla con columnas Dato | Fecha del dato | Fuente (nombre y enlace completo) | Tipo de fuente (oficial / informe del banco / prensa / agregador).
3. Opiniones y especulaciones, separadas de los hechos y marcadas [ESPECULACIÓN].
4. Contradicciones entre fuentes.
5. Qué NO he podido comprobar [VERIFICAR] (por ejemplo, datos solo de pago).
6. Sesgos de las fuentes.
7. Lista de fuentes consultadas con enlace y fecha de acceso.

Reglas: cita fuente y fecha de CADA dato; no inventes enlaces ni cifras; si no lo encuentras, escribe «no consta»; si dos fuentes se contradicen, di cuál prevalece y por qué. Prefiere la EBA, el BCE, la Fed, el Banco de Japón y los informes anuales de cada banco.
```

### Prompt D07 para Gemini (Deep Research; pegar completo)
```
Eres un analista de investigación. Responde en español, claro y práctico. NO des recomendaciones de compra, venta ni mantenimiento, ni predicciones de precio.

TEMA: quién compra y quién vende deuda pública de otros países, a fecha de octubre de 2026: (a) tenencias de deuda de EE. UU. por país (TIC del Tesoro) comparadas con series propias de Japón (Ministerio de Finanzas), China (SAFE y Banco Popular de China) y la zona euro (BCE: balanza de pagos, inversiones de cartera); (b) composición de las reservas oficiales de divisas (COFER del FMI) y compras de oro de los bancos centrales (Consejo Mundial del Oro), con las últimas cifras trimestrales; (c) qué series abiertas y gratuitas permiten seguirlo cada mes sin pagar, con el enlace de descarga y el retraso de cada una.

Marco: panel de datos de un inversor particular en España. Prioridad de países: Japón, China, España, Francia, Italia, EE. UU. y la Unión Europea.

Entrega EXACTAMENTE estas secciones:
1. Resumen (máximo 6 líneas).
2. Hechos verificables: tabla Dato | Fecha del dato | Fuente (enlace completo) | Tipo de fuente.
3. Opiniones y especulaciones [ESPECULACIÓN].
4. Contradicciones entre fuentes.
5. Qué NO he podido comprobar [VERIFICAR].
6. Sesgos de las fuentes. Ten en cuenta que la TIC mide custodia y no propietario final.
7. Series abiertas recomendadas para automatizar: nombre, URL de descarga, formato, frecuencia, retraso.
8. Lista de fuentes con enlace y fecha de acceso.

Reglas: cita fuente y fecha de CADA dato; no inventes enlaces ni cifras; «no consta» si no lo encuentras.
```

### Prompt D09 para Gemini (modelo rápido)
```
Eres un analista de investigación. Responde en español. NO des recomendaciones de inversión.
TEMA: calificación crediticia soberana vigente (S&P, Moody's, Fitch) de España, Francia, Italia, Japón, EE. UU., China y Alemania, con perspectiva (positiva, estable, negativa), fecha de la última acción y enlace al comunicado de cada agencia o al de un tercero oficial (Ministerio de Economía, Tesoro). Octubre de 2026.
Entrega una tabla País | Agencia | Calificación | Perspectiva | Fecha | Enlace | Tipo de fuente. Marca [VERIFICAR] lo que solo salga en prensa. No inventes enlaces: «no consta» si no lo encuentras.
```

## Cómo se usa
1. Claude (D01-D05, D08): abre una sesión nueva en la carpeta, elige Sonnet, pega el prompt de Claude cambiando `[D0X]`.
2. Gemini (D06, D07, D09): en Gemini, Deep Research (Pro, nivel alto para D06 y D07; 3.6 Flash medio para D09), pega el prompt completo (no el código «Dxx»: en Deep Research no funciona), exporta a Documentos una sola vez y guárdalo en «Gemini research / Resultados». Después pide a Claude «Verifica en mi Drive el documento …».
3. Al terminar cada tarea: Claude actualiza la tabla «Qué hay ya», `scripts/actualizar_paneles.py` y las capas del mapa, y anota el coste real.
