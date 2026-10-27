# Temas T01-T25 del Gem «Research cripto»: estado y cola para hacerlos con Claude (22-oct-2026)

Fuente de la lista: documento «01 Prompt maestro» de la carpeta de Drive «Gemini research» (leído el 22-oct-2026). Joel pidió que los haga Claude en vez de Gemini: se hacen con las mismas reglas del prompt maestro (tres perspectivas: oficial, despachos y analistas, voces críticas; hechos separados de opiniones; [P]/[S]/[VERIFICAR]; sin recomendaciones ni predicciones de precio) y las secciones de entrega de siempre. Cada tema va a `informes/research/AAAA-MM-DD-Txx-tema.md` y lo verificado actualiza el radar (`explorador/regulacion.json`), las fichas (`explorador/datos.json`) y el calendario.

## Estado
| T | Tema | Estado |
|---|---|---|
| T01 | CLARITY Act | Hecho y verificado (`informes/gemini/2026-10-18-T01-clarity-act.md`) |
| T02 | GENIUS Act | Hecho y verificado; **la OCC publicó su norma final el 21-oct** (radar y calendario al día) |
| T03 | Regulation Crypto Assets (SEC) | Hecho y verificado (20-oct) |
| T04 | Euro digital | Hecho y verificado |
| T05, T17, T19, T20, T21, T22, T24 | MiCA, bancos centrales 27-30 oct, ETF de XRP/XLM, DTCC, custodia, XRPL y Stellar, fiscalidad internacional | Hechos (22 y 23-oct; informes en `informes/research/`) |
| T07, T11, T18 | Corea; Brasil; energía | Hechos el 24-oct (`2026-10-24-T07-corea-del-sur.md`, `…T11-brasil.md`, `…T18-energia-actualizacion.md`) |
| T23 | Ripple y Stellar por región | Hecho el 25-oct (`2026-10-25-T23-ripple-y-stellar-por-region.md`) |
| T06, T08 | Japón y Singapur | Hechos el 25-oct (W03; `informes/research/2026-10-26-W03-japon-singapur.md`) |
| T09, T10, T13, T14 | Hong Kong, India, Emiratos y China | Hechos el 27-oct (`informes/research/2026-10-27-T09-hong-kong.md`, `…T10-india.md`, `…T13-emiratos.md`, `…T14-china.md`); contrastados el RBI (5,50 %) y la HKMA (4,25 %); celdas nuevas casi todas [S] |
| T12, T15, T16, T25 | Rusia, BRICS sin cubrir, organismos y tema libre | **Pendientes**; ver el orden de abajo |

## Orden propuesto (por caducidad y valor)
1. **T17** Bancos centrales 27-30 oct (FOMC, BCE, BoJ): antes del 27-oct. Hoy ya hay curvas de bonos y tipos en los paneles; falta el research de decisiones, datos y calendario.
2. **T22** XRPL y Stellar: el arreglo fixCleanup3_4_0 se aplazó al 4-nov (31 de 35 validadores el 22-oct); falta seguridad post-cuántica, DEX/AMM y TVL.
3. **T05** MiCA (multi-emisión, registro CASP de ESMA, AMLR 2027) y **T21** custodia bancaria (OCC, BNY, State Street, JPMD).
4. **T19** ETF de XRP y XLM en EE. UU. (AUM, entradas, 13F) y **T20** DTCC y tokenización.
5. **T24** Fiscalidad internacional (CARF, DAC8, 1099-DA) y **T16** organismos internacionales (BIS, FMI, FSB, GAFI; el GAFI de julio de 2026 ya está leído en el radar).
6. **T18** Energía y geopolítica (Brent, Ormuz, EIA).
7. **Países** (verificar las celdas [S] del radar): T06 Japón, T07 Corea, T08 Singapur, T09 Hong Kong, T10 India, T11 Brasil, T12 Rusia, T13 Emiratos, T14 China, T15 BRICS sin cubrir (Indonesia pendiente del texto de la Ley 4/2026; Egipto y Etiopía descartados por ahora). En tandas de tres temas.
8. **T23** Ripple y Stellar por región; **T25** tema libre.

Ya cubierto parcialmente por trabajos anteriores: el radar regulatorio (136 celdas) y los informes de país; los temas de países se centran en lo que el radar marca como [S] o sin dato.

## Cómo ejecutar cada tema (sesión de Claude)
```
Sesión corta (máx. 20 min). Lee research/COLA-TEMAS-GEMINI.md y la guía research/GUIA-ESTILO-CIFRAS.md. Haz el tema [Txx] de la lista (texto en el apartado «Lista de temas» de este archivo) con el método del prompt maestro: tres perspectivas, hechos con fuente y fecha, [ESPECULACIÓN] y [VERIFICAR], sin recomendaciones ni predicciones de precio. Fuente primaria primero (curl, navegador integrado, pdf.js dentro de la página para PDF con 403); no saltes controles anti-bots. Guarda el informe en informes/research/AAAA-MM-DD-Txx-tema.md, actualiza radar, fichas y calendario con lo verificado, añade como máximo 5 líneas a cada archivo de lecciones y da 3 líneas de seguridad. No hagas commit ni push sin mi OK.
```

## Lista de temas (copia del documento 01 de Drive; lo que hay que comprobar en especial)
- **T05 MiCA:** multi-emisión de stablecoins (Comisión, EBA, SEBC), registro de CASP de ESMA, reglamento antiblanqueo AMLR en 2027.
- **T06 Japón:** reforma de la FIEA (¿Ley n.º 64 de 2026, promulgada el 23-jul-2026?), fecha de entrada en vigor, ETF, stablecoins (JPYC y RLUSD con SBI). *(El 22-oct se leyó el Taikō fiscal: 20 % separado, condicionado a la FIEA reformada.)*
- **T07 Corea del Sur:** Ley Básica de Activos Digitales (2.ª fase), ley del won stablecoin (disputa del 51 % bancos), tokenización de valores desde el 4-feb-2027, ETF. *(El BOK mantuvo el 3,00 % el 22-oct; próxima reunión 26-nov.)*
- **T08 Singapur:** MAS, consulta P015-2026 sobre stablecoins, decisiones de política monetaria de 2026 (banda del S$NEER), Project Guardian y letras tokenizadas con CBDC mayorista.
- **T09 Hong Kong:** licencias de stablecoins (HSBC, Anchorpoint), proyecto de ley de custodia, e-HKD y Ensemble, tipo base (¿4,25 % o 5,0 %?), ETF.
- **T10 India:** marco de cripto y stablecoins (informe n.º 36 de la comisión parlamentaria), tipo del RBI, e-rupia, impuesto del 30 % y TDS. *(Numeración de la Income-tax Act 2025 ya verificada: 194S → 393(1) fila 8(vi); 115BBH → sección 194 fila 4.)*
- **T11 Brasil:** Drex, proveedores PSAV (plazo de 270 días hacia el 30-oct), Resolución 561 sobre stablecoins, Copom (13,75 %), ETF.
- **T12 Rusia:** ley 282-ФЗ, rublo digital, A7A5 y sanciones, Banco de Rusia (tipo clave 14,00 %, reunión del 23-oct).
- **T13 Emiratos Árabes:** ADGM, DIFC, VARA y CBUAE; plazo del Decreto-Ley 6/2025 vencido el 16-sep-2026; reconocimiento de RLUSD.
- **T14 China:** e-CNY (depósito remunerado desde el 1-ene-2026), estado del mercado cripto, stablecoins offshore, LPR de la PBoC, tokenización y fiscalidad.
- **T15 BRICS sin cubrir:** Sudáfrica, Indonesia, Egipto, Etiopía e Irán (regulación cripto, CBDC, pagos), BRICS Pay y mBridge.
- **T16 Organismos internacionales:** BIS, FMI, FSB y GAFI; informes recientes sobre stablecoins, tokenización, Agorá y Travel Rule.
- **T17 Bancos centrales 27-30 oct:** Fed (FOMC), BCE y BoJ; decisiones recientes, datos y calendario; efecto en la liquidez (sin predicción de precio).
- **T18 Energía y geopolítica:** Brent, ruta de Ormuz, previsión de la EIA y efecto en la política de los bancos centrales.
- **T19 ETF de XRP y XLM en EE. UU.:** AUM por emisor, entradas netas, diferencia entre cifras de 30-sep (≈ $2.178 M) y 8-oct (≈ $1.560 M), declarantes 13F.
- **T20 DTCC y tokenización:** lanzamiento real del servicio de DTC, redes aprobadas, Collateral AppChain, activos en Stellar en 1S-2027.
- **T21 Custodia bancaria:** aprobaciones de la OCC (Ripple, Coinbase, Crypto.com, Protego), BNY, State Street, JPMD en Base y Canton, recurso de la ICBA.
- **T22 XRPL y Stellar:** enmiendas (fixCleanup3_4_0, ahora hacia el 4-nov), seguridad post-cuántica, DEX y AMM, TVL.
- **T23 Ripple y Stellar por región:** licencias y alianzas (CSD Brasil, Standard Chartered, Meritz); qué nombran y qué no nombran del token.
- **T24 Fiscalidad internacional de cripto (sin foco en España):** CARF y DAC8, formulario 1099-DA en EE. UU., otros regímenes.
- **T25 Tema libre:** se describe después de «Tema libre:».
