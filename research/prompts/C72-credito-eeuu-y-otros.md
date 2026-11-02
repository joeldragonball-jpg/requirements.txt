# C72 · Crédito e hipotecas fuera de la zona euro (EE. UU., Reino Unido, Japón)

Complementa el panel «Euríbor, hipotecas y crédito» (C71, BCE, ya en `explorador/paneles.html` pestaña Tipos). Vincula los datos a esa pestaña y a `scripts/actualizar_paneles.py`; NO crees pestañas ni capas nuevas.

## Qué hacer
1. EE. UU.: tipo medio de la hipoteca a 30 años (Freddie Mac PMMS, `freddiemac.com/pmms`, semanal) y crédito bancario (Fed H.8, `federalreserve.gov/releases/h8/`; hogares, empresas, inmobiliario). FRED NO responde desde los servidores de GitHub: usa las webs oficiales directas. Comprueba que cada URL abre desde `curl` ANTES de escribir código.
2. Reino Unido: tipo medio de hipotecas nuevas y aprobaciones (Banco de Inglaterra, base de datos `bankofengland.co.uk/boeapps/database`, series IUMBV34 y LPMVTVX, o las que sigan vigentes).
3. Japón: préstamos bancarios (Banco de Japón, `stat-search.boj.or.jp`) solo si abre sin control anti-bot; si no, [VERIFICAR].
4. Añade a `leer_credito()` en `scripts/actualizar_paneles.py` las series que abran (mismo formato: id, nombre, país, valor, fecha, anterior, hace_12m, serie de 13 meses). Etiqueta [P] si es el organismo oficial. Si una falla, que se conserve la anterior y avise.
5. Prueba en local (`python scripts/actualizar_paneles.py`), mira la pestaña Tipos en el navegador integrado y actualiza la tabla «De dónde sale cada panel» (objeto `PROC` de `explorador/paneles.html`) si cambia la fuente.
6. Informe corto en `informes/research/AAAA-MM-DD-C72-credito.md`: qué abre y qué no, cifras con fuente y fecha, y qué falta. Sin recomendaciones.

Fuentes que no abran: apúntalas en `research/ACCESOS-CHROME.md` como hueco (Joel descarga el archivo a `research/fuentes/`).
