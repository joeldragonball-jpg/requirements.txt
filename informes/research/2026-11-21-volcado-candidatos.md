# Volcado de candidatos a la línea de tiempo (21-nov-2026)

Se volcaron a `explorador/datos.json` (lista `movimientos`, solo añadidos al final: 396 a 416) los candidatos de los informes de hoy. Cada uno se buscó antes por fecha, actor y texto; los datos [P] se leyeron en la página oficial (Chrome, pestaña propia ya cerrada) o en EDGAR. Fechas exactas y anteriores a hoy para «Ver reacción».

## Tabla

| Candidato | Resultado | Nivel |
|---|---|---|
| BoE: declaración y borrador del Código de stablecoins (22-jun) | Ya existía (22-jun, Banco de Inglaterra) | n/a |
| SEBI/RBI Demat 2.0 (10-sep) | Ya existía (nota 56/2026) | n/a |
| FCA/BoE FS26/1 (14-sep) | Añadido; leída la página: 123 respuestas, hoja de ruta conjunta «later in 2026» | P |
| RBA/Tesoro: RITS y CBDC minorista (3-sep) | Añadido; leído el comunicado 2026-24 | P |
| CVM Res. 249 (14-oct) | Añadido; leída la noticia (la Res. no); quitada la coletilla «sin inversores reales», que la noticia no dice | P |
| CVM: 11 propuestas (6-nov) | Añadido; leído (B3, ANBIMA, CSD, ABToken en Stellar; «más que el triple») | P |
| FSB Türkiye (11-nov) | Añadido; leída la nota 15/2026 | P |
| FSB Pleno 2027 (17-nov) | Añadido; reformulado a lo que dice la nota (trata stablecoins y sopesa un inventario en 2027); «programa definitivo a principios de 2027» no se leyó y se quitó | P |
| SEC: custodia (1-oct) | Ya existía (S7-2026-35) | n/a |
| CFTC: ANPRM en Federal Register (13-oct) | Descartado: el ANPRM ya está el 5-oct; la URL del candidato es una búsqueda, no el documento | n/a |
| Euro digital: trílogo sin acuerdo (18-nov) | Añadido, sin URL; solo prensa, sin comunicado oficial leído [VERIFICAR] | S |
| JPM Coin (JPMD) en Ethereum (19-oct) | Añadido; leída la nota («segunda cadena pública») | P |
| Citi Token Services en Japón y EAU (28-sep) | Añadido; leída la nota (7 mercados); quitado «red privada permisionada», no aparece en lo leído | P |
| HSBC TDS en EE. UU. (13-abr) | Añadido; leída la nota | P |
| LSEG Super Validator de Canton (28-sep) | Añadido; leída la nota; el repo intradía fue en pruebas de concepto, no producción | P |
| BCE Pontes (21-sep) | Ya existía | n/a |
| BIS Agorá (27-may) | Ya existía | n/a |
| Deutsche Bank custodia anunciada (16-sep) | Añadido como S: nota del banco sin leer, solo The Block; distinto del lanzamiento del 11-nov ya existente | S |
| Nasdaq/DTC acciones tokenizadas (18-mar) | Añadido como S: el PDF de la SEC no se pudo leer como texto [VERIFICAR] | S |
| Mastercard liquidación con stablecoins (3-jun) | Añadido; leída la nota: es un anuncio de planes («will support»), 8 redes incl. XRPL y Canton | P |
| BNY depósitos tokenizados (9-ene) | Añadido como S (The Block citando a Bloomberg; nota del banco sin leer) | S |
| BBVA en Qivalis (4-feb) | Añadido; leída la nota (11 entidades, 2S-2026) | P |
| 13F Mubadala (16-nov) | Añadido; leído en EDGAR (fecha, IBIT 14.721.917 acc., $696,9 M, cartera $20,6 mil M) | P |
| 13F ADIC (16-nov) | Añadido; leído en EDGAR: IBIT 8.218.712 acc., $389,1 M de $716,9 M. Sin dato de variación frente al 2T (no se afirma) | P |
| Goldman en ETF de XRP | Ya existía (13F del 3T, 30-sep) | n/a |
| Stellar +33,9 % distribuido en 30 días | Añadido el 20-nov (lectura del 21-nov, fecha previa a hoy para el gráfico); página pública de RWA.xyz muestra +33,86 % y $4,87 mil M | S |
| Franklin BENJI de 513 a 1.393 M$ | Añadido igual; la página pública muestra «$1.4B» pero oculta la variación (login); el 513 viene del script C355 [VERIFICAR] | S |

Resultado: 20 añadidos (13 P, 7 S), 7 ya existentes o descartados.

## Notas
- Fechas: los dos movimientos de RWA.xyz llevan 2026-11-20 aunque la lectura fue el 21-nov (lo dice el texto); es lectura de un agregador, no un hecho del día 20.
- Las etiquetas `cadenas` siguen las reglas de `etiquetar_cadenas.py` (se editaron a mano; el script no se ejecutó).
- Entidades (`ent`): nombres canónicos de los existentes (BCE, FSB, SEC, DTCC...); «Ver reacción» solo usa la fecha.
- Nivel [S] de RWA.xyz: agregador comercial sin auditar, con sesgo de promoción en parte de la prensa de Stellar. Todo son hechos de mercado o regulatorios, no recomendaciones. Interpretaciones del caso alcista o bajista están en los informes de origen.
