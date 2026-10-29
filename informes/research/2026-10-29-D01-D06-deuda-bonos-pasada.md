# D01-D06 · Deuda y bonos: pasada del 29-oct-2026 (sin API de Anthropic)

Resultado corto: **una cifra nueva con fuente oficial (España 30 a)** y el estado real de cada acceso. Nada de esto es recomendación.

## Pruebas de acceso desde este equipo (curl, 29-oct)
| Fuente | Resultado |
|---|---|
| Bundesbank (web y API `api.statistiken.bundesbank.de`) | Conexión cortada (ECONNRESET), también desde WebFetch. No es un bloqueo anti-bot: la red no llega. Probar desde GitHub Actions u otra red. |
| Finanzagentur (Alemania) | Igual: sin conexión. |
| AFT (Francia) | 403 «Just a moment…» (Cloudflare). Sin saltarlo; solo navegador a mano. |
| Banca d'Italia (infostat, statistiche) | Abren (200), pero no hay serie diaria de rendimientos de BTP; la web no la ofrece. |
| MEF Italia (dt.mef.gov.it) | Abre (200): solo resultados de subastas (PDF). |
| ChinaBond (`yield.chinabond.com.cn`) | La página abre (200); la API da 405 a curl (ya anotado el 22-oct). Cbonds lo vende de pago. |
| BCE curva AAA zona euro (API) | Sigue funcionando: 10 a spot 3,371 % el 27-oct-2026 [P] (es la curva AAA, no Alemania). |

## Hallazgos
- **D02 Alemania:** existe la serie diaria oficial del Bundesbank de la curva Svensson de valores federales cotizados. Patrón de clave (de la página del Bundesbank, sin poder probarlo): `BBSIS.D.I.ZAR.ZI.EUR.S1311.B.A604.R{NN}XX.R.A.A._Z._Z.A` con R01XX, R02XX, R05XX, R10XX. El 30 a no lo he localizado: [VERIFICAR]. Se puede reconstruir también con los parámetros Svensson (`BBSIS.D.I.ZST.B0…`). Falta probar desde otra red.
- **D05 España 30 a:** subasta de Obligaciones al 3,95 % con vencimiento 31-oct-2056, **16-jul-2026: rendimiento al precio medio 4,286 %** (mínimo aceptado 4,290 %); adjudicado 1.591,727 M€ sobre 3.057,728 M€ solicitados [P: [BOE-A-2026-16645](https://boe.es/boe/dias/2026/07/30/pdfs/BOE-A-2026-16645.pdf), resolución del 20-jul]. Es el dato de subasta, no secundario: el secundario ya figuraba como 4,49 % [S]. Falta Italia 30 a nominal.
- **D06 Bancos:** la EBA dio por **discontinuado el ejercicio de transparencia desde junio de 2025**. El corte más reciente de exposición soberana sigue siendo el 30-jun-2025, que ya usa el panel [P: [página de la EBA](https://www.eba.europa.eu/risk-and-data-analysis/risk-analysis/eu-wide-transparency-exercise)]. Los cortes nuevos habría que sacarlos del Pillar 3 Data Hub de la EBA (`edap-public.eba.europa.eu`), no probado; el alcance de «soberano» sigue sin leer.
- **D01 Italia, D03 Francia, D04 China:** sin cambios respecto a las pasadas parciales del 26-27-oct. Las dos vías abiertas son el navegador (AFT, ChinaBond) y el Data Hub (bancos).

## Lo que queda
1. Probar la clave del Bundesbank desde GitHub Actions (script local sin IA, coste 0 de API) o desde otra red.
2. Abrir AFT y ChinaBond en el navegador a mano (sin saltar controles).
3. Pillar 3 Data Hub para D06.
4. Subastas BTP 30 a (MEF) para D01/D05.
