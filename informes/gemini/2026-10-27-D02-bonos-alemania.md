# Gemini · D-bonos-ligera · D02 Alemania (Bund 2/5/10/30 a) · 2026-10-27 (crudo + verificación)
Segunda prueba de Google Search sin Deep Research; el prompt ya excluía indexados y pedía revisar antes de «no encontrado». Plantilla: research/gemini/D-bonos-ligera.md.

## Respuesta cruda de Gemini (resumen fiel)
- Secundario [S]: 2 a 3,08% (Investing.com), 5 a 3,16%, 10 a 3,36%, 30 a 3,69% (Trading Economics), todos datados 27-oct.
- Subastas Bundesbank [P] (PDF «tenderergebnis»): 2 a 3,08% (27-oct), 5 a 3,22% (13-oct), 30 a 3,80% (14-oct). 10 a subasta: «no encontrado» (cita anuncio del 22-oct).
- Descarga: Bundesbank CSV/SDMX/API; serie «BBSIS-10Y» [VERIFICAR]. Retraso: nulo.
- Texto: «alta demanda en subastas a 5, 20 y 30 años»; curva con pendiente positiva (2 a 3,08% → 30 a 3,69%).

## Verificación (27-oct)
- ✓ 10 a secundario 3,36% (3,359), 27-oct-2026: Trading Economics [S].
- ✓ 30 a subasta 14-oct: reapertura de los Bunds 2047 y 2056 con rendimiento medio 3,80% en ambos: confirmado en el índice del PDF que cita Gemini y en el resultado de búsqueda [S]; el PDF no se pudo abrir directamente (ver abajo).
- ✗ **2 a subasta 27-oct 3,08% [P]: NO confirmado, probablemente copiado del secundario.** El PDF «2026-10-27-tenderergebnis» no se abrió (error de conexión repetido con el servidor de la Bundesbank) y la búsqueda no encuentra ningún resultado de subasta del 27-oct; los PDF indexados llegan hasta el 19-oct. El último Schatz que sí aparece es el del 6-oct (3% dic-2028): rendimiento medio 3,10%, adjudicado 4.526 M€ de 6.000 M€, cobertura 1,1 [S, vía resumen de búsqueda]. 3,08% coincide exactamente con su cifra de Investing.com, un indicio de que repitió la cifra. Etiqueta correcta: VERIFICAR, no P.
- ? 5 a subasta 13-oct 3,22%: no verificado (PDF no abierto).
- ✗ Serie «BBSIS-10Y»: no tiene el formato de los códigos reales de la Bundesbank (del tipo BBSIS.D.I.ZST.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A, de memoria): [VERIFICAR] en el portal antes de usarlo en un script.
- ✗ «Alta demanda» en las subastas: el 2 a del 6-oct se adjudicó solo 4.526 M€ de 6.000 M€ (cobertura 1,1). Es el dato contrario; Gemini no lo comparó. 

## Lectura de la prueba (D01 + D02)
- Mismo patrón que Italia: sirve para localizar el portal de las subastas y las URL de los PDF oficiales; los secundarios de agregadores coinciden entre sí.
- La etiqueta [P] no es fiable: Gemini puede marcar P una cifra que no leyó. Hay que abrir cada PDF. Aquí un PDF concreto no se pudo abrir y la cifra era sospechosa.
- No hubo omisión del 2 a esta vez (la corrección del prompt pudo ayudar) ni mezcla con indexados; sí cifra dudosa y una interpretación («alta demanda») no respaldada.
- Consumo: Joel no vio avisos de límite ni gasto notable.
- Pendiente: abrir los PDF del 13-oct y del 27-oct (si se publica) desde un navegador (la Bundesbank cortó la conexión desde este equipo, igual que la API el 22-oct); serie diaria abierta de la Bundesbank; 10 a subasta.
