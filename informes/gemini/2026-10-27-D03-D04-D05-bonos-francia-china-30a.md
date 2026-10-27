# Gemini · D-bonos-ligera · D03 Francia + D04 China + D05 30 años España/Italia · 2026-10-27 (crudo + verificación)
Prueba B («más de uno»): 3 bloques en un solo prompt con búsqueda de Google, tope pedido ~25 fuentes. Plantilla: research/gemini/D-bonos-ligera.md.

## Respuesta cruda de Gemini (resumen fiel)
- Tabla de 22 filas, todas de secundario [S] (Investing.com y Trading Economics, 26/27-oct) y 11 filas de subasta, TODAS «no encontrado».
- Francia: 2 a 3,73%, 5 a 4,13%, 10 a 4,72% (TE), 30 a 5,43%. China: 1 a 1,17%, 2 a 1,25%, 5 a 1,35%, 10 a 1,64%, 30 a 2,07%. España 30 a 4,49%, Italia 30 a 5,08%.
- Descarga: Banque de France webstat (CSV/SDMX), serie TEC 10 «FM.M.FR.EUR.FR2.BB.FRMOYTEC10.HSTA» [código sin verificar; lleva «M»]; ChinaBond (XLS) sin código; Banco de España/Banca d'Italia (series sin verificar, ~1 mes de retraso).
- Subastas: dice no localizar AFT (2/5/10/30), MEF China, Tesoro español ni BTP nominal a 30 a.

## Verificación (27-oct)
- ✓ España 30 a 4,49% (27-oct, +0,01 diario): Trading Economics [S].
- ✓ Italia 30 a 5,08% (27-oct): Trading Economics [S]. (D01 dio 5,11% de Investing.com: diferencia de 3 pb entre agregadores.)
- ✓ China 10 a: TE da 1,63% (1,6343) frente a 1,64% de Gemini: coincide, 1 pb [S].
- ✓ China 2 a 1,25% (1,249) [S] y China 30 a 2,07% [S]: el 2,07% sale en la sección de bonos relacionados de esa misma página; **la URL que dio para el 30 a es la del 2 a**, no la del 30 a. Valor correcto, enlace equivocado.
- ✗ **Francia 10 a: 4,72% «Trading Economics» es incorrecto: TE da 4,92% (4,922) el 27-oct. Error de 20 pb en la cifra más importante.** Coherente con la subasta del 1-oct (4,93%) y con 4,79% el 16-oct.
- ✗ **Subastas francesas «no encontrado»: sí existen.** AFT, 1-oct-2026: OAT 3,70% nov-2036 a 10 a, tipo medio ponderado 4,93%, demanda 12.564 M€ y adjudicado 6.271 M€ (cobertura ≈ 2,0); OAT 3,80% jun-2037, 4,97%; total 11.999 M€. [S, vía prensa/Boursorama, Fortuneo, dbfranceinvest; AFT no abierto]. Ya lo recoge nuestro informe W02 del 26-oct (4,93% el 1-oct). En septiembre (3-sep) la misma línea salió al 4,23%: +70 pb en un mes [S].
- ? No contrastados: Francia 2 a 3,73%, 5 a 4,13%, 30 a 5,43% (Investing.com); China 1 a 1,17% y 5 a 1,35%.
- ✗ Serie TEC 10: «FM.M.FR...»: la «M» suele indicar frecuencia mensual, pero dijo «series diarias sin retraso»: incoherente; [VERIFICAR] en webstat.banque-france.fr antes de usarla.
- Interpretación sin respaldo: en España dice que «aguanta» y que «demuestra solidez al colocar» a 30 años, pero a la vez no encontró el resultado de ninguna subasta española; el apartado alcista no se apoya en datos del propio informe. «Mínimos plurianuales» de China (TE: −0,14 pb a un año, −0,06 en el mes) [S, sin más contraste].

## Lectura de la prueba B (D01 + D02 + D03/04/05)
- **«Más de uno» funciona en coste:** 3 bloques, 22 filas, sin aviso de límite ni problema (Joel); el prompt unitario no era necesario.
- **Calidad:** los secundarios de agregador son aceptables (6 de 7 contrastados bien; 1 error de 20 pb en Francia 10 a). Las subastas son su punto débil: 0 de 11 encontradas, y en Francia sí existen.
- Mejor uso: instantánea de secundarios para localizar cifras que luego se contrastan; NO para subastas ni para series diarias.
- **Para series diarias abiertas, Gemini no hace falta:** las APIs oficiales (Banque de France webstat, Bundesbank, BCE, Banca d'Italia) las da Claude con Chrome (D01-D05 en COLA-DEUDA-BONOS). Pendiente comprobar el código real de cada serie.
- Fallo de verificación repetido: el error de Francia 10 a lo cazó la comprobación en la fuente que Gemini citaba. Etiqueta «S» no equivale a «cifra correcta».
