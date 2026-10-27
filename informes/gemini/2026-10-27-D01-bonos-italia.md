# Gemini · D-bonos-ligera · D01 Italia (BTP 2/5/10/30 a) · 2026-10-27 (crudo + verificación)
Prueba: chat normal con búsqueda de Google, sin Deep Research. Prompt: research/gemini/D-bonos-ligera.md.

## Respuesta cruda de Gemini (resumen fiel)
- Secundario (Investing.com, [S]): 2 a 3,51% (27-oct), 5 a 3,98% (26-oct), 10 a 4,51% (27-oct), 30 a 5,11% (27-oct).
- Subasta MEF [P]: BTP 5 a 4,08% (29-sep, cobertura 1,54); BTP 10 a 4,10% (28-ago).
- 2 años subasta: «no encontrado». 30 años subasta: 2,10% «BTPei» (Teleborsa, [S]).
- Descarga: Banca d'Italia INFOSTAT (CSV/SDMX/XLS/API) infostat.bancaditalia.it; series citadas QMTS0200 (rendimientos mensuales a la emisión) y MFN_BMK.M.020.922.0.EUR.205 [VERIFICAR: códigos sin comprobar]. Retraso: Banca d'Italia hasta un mes; MEF el mismo día.
- Caso alcista/bajista: cobertura 1,54 en el 5 a «robusta»; 30 a sobre 5,1% = prima estructural.

## Verificación (27-oct, 4 datos, abriendo las fuentes)
- ✓ 5 años, 29-sep-2026: rendimiento lordo 4,08%, cobertura 1,54, asignado 3.500 M€, cupón 3,95%, vto. 1-feb-2032 [P] (PDF del MEF, leído con pdftotext).
- ✓ 10 años, 28-ago-2026: rendimiento lordo 4,10%, cobertura 1,62, asignado 4.000 M€, cupón 4,00%, vto. 1-oct-2036 [P] (PDF del MEF).
- ✓ 10 años secundario: Investing.com muestra 4,509% (+0,005), cierre 18:27; la página no dice la fecha (noticias de 26-oct): Gemini la dató 27-oct, [VERIFICAR] fecha.
- ✗ **2 años: Gemini dijo «no encontrado», pero su propia fuente (Teleborsa, 27-oct-2026) trae la subasta del BTP 3% vto. 30-10-2028: 2.000 M€, cobertura 1,72, rendimiento bruto 3,55% (−9 pb vs. 24-sep)** [S].
- ✗ **30 años «2,10%» es un error de comparación:** es el BTPei 2,35% vto. 15-09-2035 (indexado a inflación, rendimiento REAL, subasta 27-oct, cobertura 1,81), no un BTP nominal a 30 años y no comparable con el 5,11% secundario. Con 9 años de vida restante, «30 años» es la duración original. También salió un BTPei a 15 años (1,69%).
- No contrastados: 2 a 3,51%, 5 a 3,98% y 30 a 5,11% de Investing.com (agregador, [S]); códigos de series de Banca d'Italia.

## Lectura de la prueba (Google Search en vez de Deep Research)
- Funciona para LOCALIZAR fuentes y fechas de subasta: dos cifras oficiales exactas, con URL abierta y válida.
- Falla en lo que pedía el prompt: dio por no encontrada la subasta del 2 años que estaba en su propia fuente, y mezcló rendimiento real e indexado con nominal. Con cifras diarias exactas, Gemini sirve de mapa; el dato final lo da la fuente oficial.
- Fuentes: no consta nº de búsquedas (Joel no lo vio). Sin aviso de límite en esta respuesta.
- Sesgo: tabla casi toda de agregador (Investing.com); solo 2 de 8 filas son [P].
- Caso alcista/bajista de Gemini: una cobertura de 1,54 es flojita para llamarla «robusta»; en el 10 a fue 1,62 y en el 2 a 1,72 [opinión, sin referencia histórica en este informe].
- Pendiente: serie diaria abierta para 2/5/10/30 a (¿INFOSTAT? códigos sin comprobar) y 30 a nominal (D05).
