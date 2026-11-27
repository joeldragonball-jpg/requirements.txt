# Liquidez global — panorama a 27-nov-2026

Hechos con fuente y fecha; sin recomendaciones. Lectura el 27-nov-2026.
Niveles: **P** = fuente primaria oficial leída directamente (o su serie oficial en FRED/API); **D** = dato de agregador o prensa que cita la cifra oficial; **S** = sin lectura directa, solo referencia indirecta. Lo no leído va marcado [VERIFICAR].

## 1. Estados Unidos

| Dato | Valor | Fecha | Fuente | URL | Nivel |
|---|---|---|---|---|---|
| Balance Fed, activos totales (H.4.1) | 6.741.452 M$ (≈6,74 B$) | miércoles 18-nov-2026 (publ. 19-nov) | Federal Reserve H.4.1 | https://www.federalreserve.gov/releases/h41/current/ | P |
| Serie WALCL (contraste) | 6.755.639 (14-oct) → 6.741.452 (18-nov); -14.187 M$ en 5 semanas | 14-oct a 18-nov-2026 | FRED WALCL | https://fred.stlouisfed.org/series/WALCL | P |
| Valores en cartera (outright) | 6.472.944 M$ | 18-nov-2026 | H.4.1 | https://www.federalreserve.gov/releases/h41/current/ | P |
| Reservas bancarias en la Fed | 3.001.790 M$ (media semanal 2.979.656) | 18-nov-2026 | H.4.1 | https://www.federalreserve.gov/releases/h41/current/ | P |
| TGA (cuenta del Tesoro) | 892.310 M$ miércoles (media 916.613) | 18-nov-2026 | H.4.1; FRED WTREGEN | https://fred.stlouisfed.org/series/WTREGEN | P |
| TGA, evolución semanal (media) | 957.175 (4-nov) → 914.370 (11-nov) → 916.613 (18-nov) M$ | 4 a 18-nov-2026 | FRED WTREGEN | https://fred.stlouisfed.org/series/WTREGEN | P |
| RRP, línea H.4.1 (incluye contrapartes oficiales extranjeras) | 317.043 M$ (media 324.423) | 18-nov-2026 | H.4.1 | https://www.federalreserve.gov/releases/h41/current/ | P |
| RRP facilidad overnight (ON RRP, subastas diarias) | 0,3 mil M$ | 25-nov-2026 | FRED RRPONTSYD | https://fred.stlouisfed.org/series/RRPONTSYD | P |
| Repos / SRF (línea «repurchase agreements» de H.4.1) | 1 M$ (media semanal 16 M$); FRED WORAL: 0 (4-nov), 5 (11-nov), 1 (18-nov) M$ | 18-nov-2026 | H.4.1; FRED WORAL | https://fred.stlouisfed.org/series/WORAL | P |
| M2 EE. UU. (desestacionalizado) | 23.532,8 mil M$ (jul 23.177,3; ago 23.300,8; sep 23.414,3) | octubre 2026 | FRED M2SL (Fed) | https://fred.stlouisfed.org/series/M2SL | P |
| Rendimiento bono 10 años EE. UU. (CMT) | 4,91 % (20-nov 4,92; 23-nov 4,92) | 24-nov-2026 | FRED DGS10 | https://fred.stlouisfed.org/series/DGS10 | P |
| 10 años EE. UU., Yahoo ^TNX (cierre) | 5,052 (19-nov); 4,912 (20-nov); 4,918 (23-nov); 4,904 (24-nov); 4,848 (25-nov) | 19 a 25-nov-2026 | Yahoo Finance | https://finance.yahoo.com/quote/%5ETNX/ | D |
| 30 años EE. UU., Yahoo ^TYX | 5,235 % (último precio) | marca de tiempo de Yahoo, ~25-nov-2026 | Yahoo Finance | https://finance.yahoo.com/quote/%5ETYX/ | D |

Nota: el 19-nov (5,052 %) solo figura en Yahoo; no pude cotejarlo con FRED (la lectura de DGS10 llegó solo hasta el 24-nov) [VERIFICAR].

### Subastas del Tesoro de EE. UU., semana del 23-nov-2026

| Subasta | Importe | Rendimiento alto | Bid-to-cover | Fecha | Fuente | URL | Nivel |
|---|---|---|---|---|---|---|---|
| Nota a 2 años | 69.000 M$ | 4,700 % | 2,65 | 23-nov-2026 | TreasuryDirect (API de subastas) | https://www.treasurydirect.gov/TA_WS/securities/auctioned?format=json&days=10&type=Note | P |
| Nota a 5 años | 70.000 M$ | 4,719 % | 2,37 | 24-nov-2026 | TreasuryDirect | idem | P |
| Nota a 7 años | 44.000 M$ | 4,708 % | 2,43 | 25-nov-2026 | TreasuryDirect | idem | P |

Notas a 2, 5 y 7 años de la semana: 183.000 M$ en total (suma de los tres importes de oferta). No leí bills, FRN ni la liquidación (issue date). Una búsqueda web mostró una cifra de 5,085 % para otra subasta de 7 años, con fecha contradictoria entre fuentes; no se usa [VERIFICAR].

## 2. Zona euro

| Dato | Valor | Fecha | Fuente | URL | Nivel |
|---|---|---|---|---|---|
| Balance del Eurosistema, activos totales | 5.923.063 M€ (+16.804 M€ en la semana) | 20-nov-2026 (publ. 24-nov) | BCE, estado financiero semanal | https://www.ecb.europa.eu/press/pr/wfs/2026/html/ecb.fst261124.en.html | P |
| Valores de política monetaria | 3.269.994 M€ (-3.241 M€ en la semana) | 20-nov-2026 | BCE, idem | idem | P |
| Crédito de política monetaria a bancos | 42.233 M€ (MRO 20.660; LTRO 21.524; facilidad marginal 49) | 20-nov-2026 | BCE, idem | idem | P |
| Serie semanal activos (contraste) | 5.913.173 (6-nov); 5.906.258 (13-nov); 5.923.063 (20-nov) M€ | nov-2026 | FRED ECBASSETSW | https://fred.stlouisfed.org/series/ECBASSETSW | P |
| M3 zona euro | 17.764.067 M€; crecimiento anual 3,6 % | octubre 2026 (publ. 26-nov) | Trading Economics citando al BCE | https://tradingeconomics.com/euro-area/money-supply-m3 | D |
| M3, mes anterior | 3,5 % anual (M1 2,7 %; M3-M2 7,1 %) | septiembre 2026 (publ. 27-oct) | BCE vía Banco de Francia | https://www.banque-france.fr/en/press-release/monetary-developments-euro-area-september-2026 | D |
| Comunicado oficial «Monetary developments: October 2026» | existe (listado), no pude abrir el texto | 26-nov-2026 | BCE | https://www.ecb.europa.eu/press/pr/stats/md/html/index.en.html | S [VERIFICAR] |
| Curva AAA de la zona euro, 10 años (spot) | 3,26 % (23-nov 3,32; 24-nov 3,31) | 25-nov-2026 | BCE Data Portal (YC) | https://data.ecb.europa.eu/ | P |
| Bund alemán 10 años | 3,29 % (+0,03 pp en el día; -0,09 pp en el mes; +0,60 pp en 12 meses) | 27-nov-2026 | Trading Economics | https://tradingeconomics.com/germany/government-bond-yield | D |
| Bono español 10 años | 3,87 % (-0,01 pp) | 27-nov-2026 | Trading Economics | https://tradingeconomics.com/spain/government-bond-yield | D |
| Alemania 10 años, media mensual (OCDE) | 3,42 % oct; 3,47 % sep; 3,19 % ago | octubre 2026 | FRED IRLTLT01DEM156N | https://fred.stlouisfed.org/series/IRLTLT01DEM156N | P |
| España 10 años, media mensual (criterio de convergencia BCE) | 4,066 % oct; 3,927 % sep | octubre 2026 | BCE API (IRS) | https://data.ecb.europa.eu/ | P |
| España 10 años, media mensual (OCDE) | 4,07 % oct; 3,93 % sep; 3,64 % ago | octubre 2026 | FRED IRLTLT01ESM156N | https://fred.stlouisfed.org/series/IRLTLT01ESM156N | P |

Observación de coherencia: la media mensual de octubre para España (4,07 %) y el dato diario del 27-nov (3,87 %, agregador) implican un descenso; la comparación mezcla fuentes y metodología, [VERIFICAR] antes de citarla. Diferencial España-Alemania el 27-nov con las cifras de Trading Economics: 0,58 pp (cálculo mío, nivel D).

## 3. Japón

| Dato | Valor | Fecha | Fuente | URL | Nivel |
|---|---|---|---|---|---|
| Balance del BoJ, activos totales | 627,11 billones de yenes (cifra literal: 627.112.965.321 miles de yenes) | 20-nov-2026 (publ. 25-nov) | Banco de Japón, cuentas | https://www.boj.or.jp/en/statistics/boj/other/acmai/release/2026/ac261120.htm | P |
| Bonos del Estado japoneses (JGB) en balance | 506,21 billones de yenes | 20-nov-2026 | BoJ, idem | idem | P |
| Saldos en cuenta corriente en el BoJ | 410,10 billones de yenes | 20-nov-2026 | BoJ, idem | idem | P |
| Préstamos del BoJ (sin DIC) | 68,42 billones de yenes | 20-nov-2026 | BoJ, idem | idem | P |
| Serie mensual activos BoJ (FRED, otra definición) | 6.446.620 (ago); 6.250.253 (sep); 6.261.882 (oct) en la unidad de la serie | octubre 2026 | FRED JPNASSETS | https://fred.stlouisfed.org/series/JPNASSETS | P (unidad [VERIFICAR]) |
| M2 Japón, variación anual | 1,7 % (media sep-2026, revisada) | septiembre 2026 | BoJ, Money Stock | https://www.boj.or.jp/en/statistics/money/ms/ms2610.pdf | P |
| M2 Japón octubre 2026 (preliminar, publ. 11-nov) | no pude leer la cifra: el PDF salió con columnas desordenadas | octubre 2026 | BoJ, ms2610.pdf | idem | S [VERIFICAR] |
| M3 Japón sep-2026 | 0,9 % anual (misma tabla, lectura con posible desalineación) | septiembre 2026 | BoJ | idem | P [VERIFICAR] |
| Base monetaria Japón | -13,6 % anual (15.º mes seguido de caída; sep -15,2 %) | octubre 2026 | Trading Economics citando BoJ | https://tradingeconomics.com/japan/monetary-base-yoy/news/597814 | D |
| Bono japonés 10 años | 2,65 % (+0,02 pp) | 27-nov-2026 | Trading Economics | https://tradingeconomics.com/japan/government-bond-yield | D |
| JGB 10 años, media mensual (OCDE) | 2,755 % oct; 3,05 % sep; 2,94 % ago | octubre 2026 | FRED IRLTLT01JPM156N | https://fred.stlouisfed.org/series/IRLTLT01JPM156N | P |
| Titular | «Japan 10Y Yield Rises on Hawkish BOJ Signals»: el mercado espera una subida de tipos del BoJ el mes próximo | 26-nov-2026 | Trading Economics | https://tradingeconomics.com/japan/government-bond-yield | D (opinión de mercado, no hecho) |

## 4. China

| Dato | Valor | Fecha | Fuente | URL | Nivel |
|---|---|---|---|---|---|
| M2 | 359,06 billones de yuanes; +7,1 % anual (-0,1 pp vs. septiembre; esperado 7,2 %) | octubre 2026 (publ. 13-nov) | PBoC vía Newsquawk / prensa financiera | https://www.newsquawk.com/headlines/chinese-m2-money-supply-oct-yy-71-vs-exp-72-prev-72 | D |
| M1 | 116,9 billones de yuanes; +4,4 % anual (+1,2 pp vs. septiembre; efecto base débil de oct-2025) | octubre 2026 | idem / Yicai | https://www.yicaiglobal.com/news/chinas-money-supply-social-financing-accelerate-in-october-as-borrowing-costs-fall | D |
| Financiación social total (stock) | 469,16 billones de yuanes; +7,2 % anual | octubre 2026 | idem | idem | D |
| Préstamos en yuanes (stock) | 283,33 billones; +4,7 % anual; nuevos préstamos en octubre ≈ -100.000 M¥ (análisis de Diyi Caijing) | octubre 2026 | idem | https://en.people.cn/n3/2026/1114/c90000-20519006.html | D [VERIFICAR el signo y la cifra] |
| Informe oficial «Financial Statistics Report (October 2026)» | listado, publ. 13-nov-2026; no abrí las tablas | 13-nov-2026 | PBoC | https://www.pbc.gov.cn/en/3688247/3688978/3709137/index.html | S [VERIFICAR] |

Los analistas citados atribuyen el frenazo de M2 a los préstamos negativos de octubre y al aumento de depósitos fiscales por emisión de deuda pública (opinión de analistas, no dato oficial).

## 5. Lectura de hechos (sin conclusiones de inversión)

- Fed: activos 6,74 B$ el 18-nov, 14.187 M$ por debajo del 14-oct; reservas ≈3,0 B$ y TGA ≈0,89-0,92 B$; el uso de repos/SRF es residual (1 M$) y el ON RRP, prácticamente cero (0,3 mil M$ el 25-nov).
- BCE: balance 5,92 B€, 20-nov, casi plano en tres semanas (5,906-5,923 B€); los valores de política monetaria bajan unos miles de M€ por semana.
- BoJ: 627,1 billones de yenes, de ellos 506,2 en JGB.
- M2/M3 anual: EE. UU. aprox. +5,3 % si se compara 23.532,8 con el mismo mes de 2025 (no leído; [VERIFICAR] antes de citar); zona euro M3 +3,6 % (oct); China M2 +7,1 % (oct); Japón M2 +1,7 % (sep).
- Rendimientos a 10 años: EE. UU. 4,91 % (24-nov, FRED), Alemania 3,29 %, España 3,87 %, Japón 2,65 % (27-nov, agregador).
- Contraste: caso «liquidez abundante» = reservas por encima de 3 B$ y SRF sin uso. Caso «liquidez ajustada» = TGA alto, ON RRP agotado y M2 de China frenándose. Con estos datos no se puede decidir entre los dos [ESPECULACIÓN si se hace].

## 6. Pendientes [VERIFICAR]

1. Texto del comunicado del BCE de M3 de octubre 2026 (solo leído vía Trading Economics).
2. M2 de Japón octubre 2026 (PDF del BoJ ilegible por script).
3. Tablas del PBoC de octubre (solo prensa); M2 de China en FRED está desactualizada (la serie MYAGM2CNM189N llega solo a 2019).
4. Bund, JGB y bono español del 27-nov (solo Trading Economics); sustituir por Bundesbank, MOF Japón y Tesoro/Banco de España.
5. Cierre de 5,052 % del 19-nov en ^TNX frente a FRED.
6. Crecimiento anual del M2 de EE. UU. (calcular con la serie completa).
7. Resto de subastas de la semana (bills, FRN, TIPS) no leídas.
