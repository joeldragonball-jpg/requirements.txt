# R21b · 13F, segunda pasada: quién declara los ETF de XRP y qué pasó con Goldman, XRPR/XRPI y Stellar (2026-10-15)

Plantilla: `13f` · Modelo: Sonnet, esfuerzo alto · Sin recomendaciones de compra/venta. Completa [R21](2026-10-15-R21-13f-xrp-xlm.md) (sección 8 "Huecos").

**Cómo leer este informe.** Un 13F solo muestra la posición a **cierre de trimestre** (31-dic-2025 = 4T, 31-mar-2026 = 1T, 30-jun-2026 = 2T). No dice cuándo ni a qué precio se compró o vendió, ni si la posición es del gestor, de un cliente, de cobertura o de creación de mercado. Niveles: **PRIM-LEÍDA** = fila leída por mí en el XML oficial de EDGAR; **SECUND-INDEXADA** = fila tomada de 13f.info (agregador) y no contrastada con EDGAR; **SECUND** = prensa. Valores en dólares; "k" = miles.

---

## 1. Resumen (6 líneas)

1. **Corrección a R21 (importante).** Goldman **no salió a cero en 1T**: salió de los 5 ETF spot de XRP, pero conservó **110.000 acciones de XRPR** (REX-Osprey XRP ETF, CUSIP 26923N231) en las tres fechas: 1,65 M$ (4T), 1,21 M$ (1T), 0,94 M$ (2T). PRIM-LEÍDA en los XML de 1T y 2T. R21 buscaba solo 5 CUSIP. Con XRPR, Goldman suma ~153,8 M$ en 4T y ~87,4 M$ en 2T: **cuadra con los 154 M$ y 86,5–87,5 M$ de la prensa** (discrepancia (a) de R21 cerrada; la (b) "+83 M$ vs 1T" sigue abierta).
2. **Quién lo declara en Goldman:** todas las filas de XRP (5 spot + XRPR) vienen marcadas como declaradas por **Goldman Sachs & Co. LLC** (el bróker-dealer, `otherManager` = 1 en el XML), no por la gestora de activos ni por la de patrimonios. Goldman Sachs & Co. LLC y Goldman Sachs Wealth Services **no presentan 13F propio**: presentan 13F-NT y sus posiciones van dentro del 13F-HR del grupo (CIK 886982).
3. **Concentración:** en Bitwise, los 2 mayores (Goldman y Jane Street) son el 56 % del valor declarado en 2T y los 10 mayores el 92 %; en Franklin XRPZ, Goldman solo es el 72 % y los 10 mayores el 90 % (SECUND-INDEXADA, sumas mías). La cola larga son asesores patrimoniales pequeños (RIA).
4. **Base de declarantes:** los gestores distintos con algún ETF spot de XRP pasan de **72 (4T) a 122 (1T) y 129 (2T)**; 60 de los 72 de 4T siguen en 2T (SECUND-INDEXADA, recuentos míos).
5. **Identificaciones:** CUSIP 92864M780 = **XRPI (Volatility Shares Trust, "XRP ETF")** (confirmado por el índice; antes era inferencia). XRPR = 26923N231. **XRPL (CoinShares) no aparece** en el índice.
6. **Stellar:** el *Grayscale Stellar Lumens Trust (XLM)* (CIK 1761325) **sigue cotizando en OTCQX como GXLM, no como ETF**, según su 10-Q del 4-ago-2026 (PRIM-LEÍDA, extracto). No hay filas de 13F para su CUSIP (38963R105). Sigue sin haber señal 13F institucional sobre XLM.

---

## 2. Lista de valores (ampliada respecto a R21)

| Valor | CUSIP | Ticker | Cómo se identificó | Nivel |
|---|---|---|---|---|
| Bitwise XRP ETF | 09174F107 | XRP | Nombre en XML de EDGAR | PRIM-LEÍDA |
| Franklin XRP Trust | 355233107 | XRPZ | XML de EDGAR | PRIM-LEÍDA |
| Canary XRP ETF | 13723M100 | XRPC | XML de EDGAR | PRIM-LEÍDA |
| Grayscale XRP Trust ETF | 38965L106 | GXRP | XML de EDGAR | PRIM-LEÍDA |
| 21Shares XRP ETF | 90137T103 | TOXR | XML de EDGAR | PRIM-LEÍDA |
| **XRPI – Volatility Shs Tr ("XRP ETF")** | 92864M780 | XRPI | Etiqueta del índice 13f.info; en 13F de Goldman 0 filas | SECUND-INDEXADA (antes inferencia) |
| **XRPR – ETF Opportunities Trust (REX-Osprey XRP)** | 26923N231 | XRPR | Fila en XML de Goldman (nombre del emisor "ETF OPPORTUNITIES TRUST") + etiqueta del índice | PRIM-LEÍDA (fila Goldman) |
| Grayscale Stellar Lumens Trust | 38963R105 | GXLM (OTCQX) | 10-Q del trust | PRIM-LEÍDA (extracto); 0 filas en 13F |

No encontrado: **XRPL** (CoinShares) y Teucrium no devuelven resultado en el autocompletado del índice. No significa que no existan, solo que no los localicé.

---

## 3. Declarantes de Bitwise XRP ETF (CUSIP 09174F107), 2T 2026

Total 2T (sin opciones): **71,7 M$ · 6,15 M acciones · 73 declaraciones** (69 filas sin opciones). Fuente: índice [13f.info](https://13f.info/cusip/09174F107/2026/2) (SECUND-INDEXADA); los 5 marcados ✓ los contrasté fila a fila con el XML de EDGAR (PRIM-LEÍDA).

| # | Gestor | CIK | Valor 2T (k$) | Acc. 4T | Acc. 1T | Acc. 2T | Cambio 1T→2T | % acumulado | EDGAR |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Goldman Sachs Group ✓ | 886982 | 25.756 | 1.940.433 | 0 | 2.208.949 | nuevo vs 1T (+13,8 % vs 4T) | 36 % | [13F-HR 14-ago](https://www.sec.gov/Archives/edgar/data/886982/000088698226000519/0000886982-26-000519-index.htm) |
| 2 | Jane Street Group ✓ (R21) | 1595888 | 14.051 | 84.582 | 20.658 | 1.205.067 | ×58 | 56 % | [13F-HR](https://www.sec.gov/Archives/edgar/data/1595888/000159588826000108/0001595888-26-000108-index.htm) |
| 3 | IronBridge Private Wealth ✓ | 1850996 | 6.097 | 0 | 109.526 | 522.961 | +377 % | 64 % | [13F](https://www.sec.gov/Archives/edgar/data/1850996/000117266126003351/) |
| 4 | Millennium Management ✓ (R21) | 1273087 | 5.781 | 468.894 | 495.856 | 495.856 | 0 % | 72 % | [13F-HR](https://www.sec.gov/Archives/edgar/data/1273087/000127308726000007/0001273087-26-000007-index.htm) |
| 5 | Marex Group ✓ | 1997464 | 4.378 | 0 | 286.021 | 375.517 | +31 % | 78 % | [13F](https://www.sec.gov/Archives/edgar/data/1997464/000199746426000070/) |
| 6 | Kaleidoscope Capital ✓ | 1702912 | 2.462 | 0 | 211.158 | 211.158 | 0 % | 82 % | [13F](https://www.sec.gov/Archives/edgar/data/1702912/000106299326004164/) |
| 7 | Wolverine Asset Management ✓ | 1279891 | 2.330 | 1.500 | 77.004 | 199.912 | +160 % | 85 % | [13F](https://www.sec.gov/Archives/edgar/data/1279891/000127989126000010/) |
| 8 | Envestnet Asset Management ✓ (restatement) | 1407543 | 2.172 | 0 | 0 | 186.346 | nuevo | 88 % | [13F](https://www.sec.gov/Archives/edgar/data/1407543/000121465926011925/) |
| 9 | Refined Wealth Management | 1724729 | 1.792 | 0 | 148.603 | 153.726 | +3 % | 90 % | índice |
| 10 | Sloy Dahl & Holst | 1690295 | 1.006 | 86.291 | 86.291 | 86.291 | 0 % | 92 % | índice |
| 11 | Susquehanna Intl Group | 1446194 | 619 | 0 | 51.870 | 53.116 | +2 % | 93 % | índice |
| 12 | Sovran Advisors | 2051471 | 559 | 0 | 33.969 | 47.295 | +39 % | 93 % | índice |
| 13 | Militia Capital Management | 2130487 | 411 | 0 | 95.460 | 35.320 | −63 % | 94 % | índice |
| 14 | Beacon Pointe Advisors | 1744317 | 404 | 33.435 | 35.558 | 34.692 | −2 % | 95 % | índice |
| 15 | Stifel Financial | 720672 | 372 | 0 | 12.455 | 31.967 | +157 % | 95 % | índice |
| 16–25 | IMC-Chicago, HighTower, Graetz, Keel Point, FSA, RFG, Kovack, Penserra, Commonwealth Equity, Cetera | — | 146–329 cada uno | — | — | 12.550–28.237 | — | 96–98 % | índice |

Notas (HECHOS): (a) las cifras de acciones y valor de los 5 ✓ coinciden exactamente con el XML (IronBridge suma 68.920 + 454.041 = 522.961 acciones en dos filas del mismo 13F; Marex 375.517; Kaleidoscope 211.158; Wolverine 199.912; Envestnet 186.346). (b) **3T 2026 parcial:** solo 8 declarantes a 15-oct, 284 k acciones, 4,7 M$; Refined Wealth (160.705) y Sloy Dahl (86.291) ya presentaron; **Goldman, Jane Street y Millennium no**. No sacar conclusiones del 3T.

## 4. Declarantes de Franklin XRPZ (CUSIP 355233107), 2T 2026

Total 2T (sin opciones): **35,1 M$ · 3,09 M acciones · 52 filas (46 sin opciones)**. SECUND-INDEXADA salvo lo marcado.

| # | Gestor | Valor 2T (k$) | Acc. 4T | Acc. 1T | Acc. 2T | % acum. |
|---|---|---|---|---|---|---|
| 1 | Goldman Sachs Group ✓ | 25.405 | 1.932.684 | 0 | 2.238.407 | 72 % |
| 2 | Kaleidoscope Capital ✓ | 1.119 | 0 | 98.666 | 98.666 | 75 % |
| 3 | Millennium Management ✓ | 1.006 | 0 | 88.661 | 88.661 | 78 % |
| 4 | Inscription Capital | 916 | 31.811 | 66.857 | 80.770 | 81 % |
| 5 | RPO LLC | 897 | 0 | 0 | 79.050 | 83 % |
| 6 | Larson Financial Group | 858 | 37.275 | 74.077 | 75.613 | 86 % |
| 7 | Jane Street Group ✓ | 456 | 0 | 0 | 40.185 | 87 % |
| 8–9 | Blueprint Financial Advisors / Blueprint Investment Partners (misma cifra: 39.393 acc., probable duplicado de grupo) | 447 + 447 | 0 | 15.061 | 39.393 | 89–90 % |
| 10 | Arax Advisory Partners | 400 | 201 | 0 | 35.278 | 91 % |
| 11–25 | Sanctuary Advisors, Flow Traders U.S., Susquehanna, Centric Wealth, Legacy Wealth, Leisure Capital, Captrust, SRH, Synergy, Gerber, MAI, Cetera, Vista Finance, AdvisorNet, Huntington National Bank | 122–257 | — | — | 10.783–22.698 | 92–98 % |

**Franklin Templeton:** la matriz **Franklin Resources (CIK 38777)** figura con 70.000 acciones en 4T (1,39 M$) y 1T (1,02 M$) y **ya no aparece en 2T** (PRIM-LEÍDA en R21; confirmado por el índice). Citadel Advisors pasó en 2T a **solo opciones** en XRPZ (Call 54.500 / Put 13.700).

## 5. XRPR e XRPI (los dos que faltaban)

| Valor | 4T | 1T | 2T | Mayores declarantes 2T |
|---|---|---|---|---|
| **XRPR** (26923N231) | 18,1 M$ · 1,21 M acc. · 33 filas | 7,6 M$ · 0,68 M acc. · 28 filas | **5,1 M$ · 0,59 M acc. · 26 filas** | Citadel 1,85 M$ (215.639 acc.), **Goldman 0,94 M$ (110.000 acc.)**, Mustico Financial 0,58 M$, Inscription, Realta, Jane Street |
| **XRPI** (92864M780) | 18,6 M$ · 1,76 M acc. · 55 filas | 14,7 M$ · 1,94 M acc. · 45 filas | **11,3 M$ · 1,97 M acc. · 40 filas** | IronBridge 3,97 M$, Farringdon Capital 2,81 M$, Tactive 1,24 M$, UBS Group 1,13 M$ (197.369 acc., igual en 1T y 2T), Citadel (puts y acciones), Bank of America 76 k$ |

SECUND-INDEXADA salvo la fila de Goldman en XRPR (PRIM-LEÍDA, XML de 1T y 2T: 110.000 acciones, 1.213.300 $ y 943.800 $). XRPI y XRPR **no tienen la escala** de los cinco spot (11 y 5 M$ frente a ~179 M$ del conjunto spot en 2T). Que Goldman tenga 0 en XRPI se comprobó en los XML de 1T y 2T (0 coincidencias del CUSIP).

## 6. Vista agregada de los cinco ETF spot (sumas mías, SECUND-INDEXADA; clasificación por nombre = **[ESPECULACIÓN]**)

| | 4T 2025 | 1T 2026 | 2T 2026 |
|---|---|---|---|
| Valor declarado (sin opciones) | 207,8 M$ | 92,4 M$ | 179,3 M$ |
| De ello, Goldman | 152,2 M$ (73 %) | 0 (0 %) | 86,5 M$ (48 %) |
| De ello, otros brókeres/creadores de mercado/fondos multiestrategia/bancos (por nombre: Jane Street, Millennium, Marex, Wolverine, Susquehanna, IMC, Flow Traders, Citadel, Stifel…) | 29,3 M$ (14 %) | 50,7 M$ (55 %) | 49,9 M$ (28 %) |
| Resto (asesores patrimoniales, bancos privados, otros) | 26,3 M$ (13 %) | 41,7 M$ (45 %) | 43,0 M$ (24 %) |
| Gestores distintos | 72 | 122 | 129 |

Lectura de HECHOS: el "resto" pasa de 26,3 a 43,0 M$ aunque el precio por acción cayó ~43 % entre 4T y 2T (R21): ello implica, en orden de magnitud, que el número de acciones de ese grupo se multiplicó por ~2,9 (aritmética mía, mezcla ETF con precios distintos). Entre 4T y 2T, 25 gestores son nuevos frente a 1T y 18 salieron; de los 72 de 4T, 12 ya no tienen acciones (entre ellos Franklin Resources, Royal Bank of Canada, Comerica; Citadel no "salió": pasó a declarar solo opciones).

## 7. Goldman: lo que cambia y lo que sigue abierto

| Pregunta | Resultado |
|---|---|
| ¿Hay otro filer Goldman con posición XRP en 1T? | **No.** Goldman Sachs & Co. LLC (CIK 769993) y Goldman Sachs Wealth Services (CIK 1055957) presentan **13F-NT** (aviso: declaran dentro del grupo) todos los trimestres 2025-2026 (listado EDGAR, PRIM-LEÍDA). No hay 13F-HR/A de 1T posterior al 15-may-2026 en la lista de EDGAR |
| ¿Qué filial tiene los ETF de XRP? | En el 13F de 2T todas las filas de los 5 ETF spot llevan `otherManager` = 1 = **Goldman Sachs & Co. LLC** (nº 028-00687). La gestora (Goldman Sachs Asset Management, nº 2) y Wealth Services (nº 6) no figuran en esas filas. Dato de **qué entidad**, no de **para qué** (inventario, creación/rescate, cobertura de swaps o clientes siguen sin poder distinguirse) |
| ¿"Salió por completo en 1T"? | **Corrección:** salió de los 5 ETF spot; **mantuvo 110.000 acciones de XRPR** (1,21 M$) |
| Discrepancia (a): prensa 154 M$ en 4T vs. 152,17 M$ | **Cerrada:** 152,165 M$ (5 spot) + 1,647 M$ (XRPR) = 153,8 M$ |
| 2T: prensa 86,5–87,5 M$ | Coincide: 86,503 M$ (5 spot) + 0,944 M$ (XRPR) = 87,4 M$ |
| Discrepancia (b): prensa "+83,15 M$ vs trimestre anterior" | **Abierta [VERIFICAR].** Si el 1T fuera 1,21 M$ (XRPR) el aumento sería ~86 M$, no 83 M$; puede ser otra base o otro producto. No tengo fuente primaria para la cifra de prensa |

## 8. Stellar / XLM: estatus (PRIM-LEÍDA, extracto del 10-Q)

- **Grayscale Stellar Lumens Trust (XLM)**, CIK 1761325. 10-Q de 30-jun-2026 presentado el 4-ago-2026 ([índice EDGAR](https://www.sec.gov/Archives/edgar/data/1761325/000176132526000008/0001761325-26-000008-index.htm)): "The Trust's Shares have traded on OTC Markets since October 19, 2021. The Trust's trading symbol on OTCQX is 'GXLM' and the CUSIP number for its Shares is 38963R105" (Las acciones cotizan en OTC Markets desde el 19-oct-2021; símbolo GXLM en OTCQX).
- Sigue siendo **fideicomiso, no ETF**: "To date, the Trust has not met its investment objective… the Shares… have traded at both premiums and discounts to such value, which at times have been substantial" (hasta hoy no ha cumplido su objetivo; ha cotizado con primas y descuentos, a veces sustanciales). "At this time, the Trust is not accepting redemption requests" (no acepta reembolsos).
- Comisión: 2,5 % anual del valor liquidativo, pagada en XLM. Cada acción representa ~**82,76 XLM** a 30-jun-2026 (83,80 a 31-dic-2025). Comisiones devengadas: 129.519 $ en el trimestre y 259.822 $ en el semestre (indica unos 20-21 M$ de activos si se aplica el 2,5 % anual; cálculo mío, aproximado). Coste de la inversión en XLM: 23,2 M$.
- Historial EDGAR: **S-1 de 24-sep-2025** (conversión a ETF en NYSE Arca) y cambio de ejercicio fiscal (10-KT de 12-mar-2026). **No hay 424B ni formulario de admisión a cotización** en la lista de EDGAR hasta 15-oct-2026 (lista leída, sin los Form 144). La conversión a ETF **no se ha materializado** según esa lista.
- **13F:** el índice devuelve **0 filas** para 38963R105 en los cuatro trimestres. Consistente con que un fideicomiso OTC no sea un valor declarable en 13F (inferencia mía [VERIFICAR] con la lista oficial de la SEC). Otros productos de XLM (STLR de futuros, WisdomTree XLMW en Europa) siguen sin 13F relevante.
- Los resultados de "Stellar" en 13F (Stellar Bancorp, Stellar V Capital) **no tienen que ver con la red Stellar**.

## 9. Qué NO se puede concluir (obligatorio)

- **Cuándo ni a qué precio:** solo cierres de trimestre; lo ocurrido dentro del trimestre es invisible.
- **Para quién y por qué:** Goldman declara a nivel de grupo y la fila viene del bróker-dealer; ese rol incluye inventario, creación/rescate y cobertura. No es una "apuesta" demostrada. Lo mismo para Jane Street, Marex, Wolverine, IMC, Susquehanna y Citadel (calls y puts a la vez).
- **Intención de los asesores patrimoniales** (la cola larga): son carteras de clientes; que el número de gestores suba no implica convicción del gestor.
- **Exposición total:** los 13F no incluyen XRP/XLM spot, fondos fuera de EE. UU., Ripple (no cotiza) ni gestores con menos de 100 M$. La escala real de los fondos es mayor que lo declarado.
- **Predicción de precio:** ningún cambio entre cierres demuestra anticipación al precio.
- **3T 2026:** no existe todavía (plazo ~14-nov).
- **Clasificación por tipo de gestor:** la hice por nombre (regex) y es aproximada; no sustituye a una clasificación oficial.

## 10. Caso alcista / bajista (hechos, no recomendación) y sesgos

- **Lectura alcista [ESPECULACIÓN]:** casi se duplicó la base de gestores distintos (72 → 129); los asesores patrimoniales ("resto") mantienen o aumentan la posición mientras el precio cae ~43 %; Goldman volvió a los ETF spot con más acciones en Bitwise y Franklin que en diciembre.
- **Lectura bajista [ESPECULACIÓN]:** el valor total declarado en 2T (179 M$) sigue por debajo de 4T (208 M$); la mitad es Goldman, cuyo rol es probablemente de intermediario; los dos productos "alternativos" (XRPR y XRPI) bajan en valor trimestre a trimestre (XRPR 18,1 → 5,1 M$; XRPI 18,6 → 11,3 M$); Millennium y Kaleidoscope mantienen acciones idénticas dos trimestres seguidos (posiciones estáticas o de cobertura); el único vehículo de XLM sigue en OTC con primas/descuentos "sustanciales" y comisión del 2,5 %.
- **Sesgos:** (1) ETF recién lanzados (comparar 4T con 2T es comparar un mercado casi vacío con otro ya poblado); (2) el índice 13f.info es un agregador (SECUND) con anuncios, sin responsabilidad editorial: lo usé como directorio y verifiqué en EDGAR los cinco nuevos mayores; (3) emisores y Grayscale/DCG son parte interesada; (4) la prensa cripto titula "Goldman lidera" sin explicar que el 13F es de grupo.

## 11. Huecos pendientes

1. 3T 2026: repetir tras ~14-nov (comparar Goldman, Jane Street, Millennium, Marex, IronBridge).
2. Verificar en EDGAR el resto de declarantes 6–25 (solo contrasté 5 de los nuevos mayores; el índice coincidió en 5 de 5).
3. Discrepancia (b) de Goldman 1T ("+83 M$"): no hay primaria; descartar o localizar la fuente de Bloomberg.
4. Carácter de XRPI y XRPR (qué tienen en cartera: futuros, filial en Islas Caimán, etc.): no lo he leído en sus prospectos.
5. CoinShares XRPL y Teucrium: ¿existen como valores con CUSIP en 13F?
6. Confirmar con la lista oficial de valores 13(f) de la SEC que GXLM/OTC no es declarable.
7. Cómo se reparte el rol del bróker (inventario, AP, swaps) en Goldman: no deducible de un 13F.

## 12. Método

- Índice: `https://13f.info/data/cusip/<CUSIP>/<año>/<trimestre>` (JSON con todos los declarantes por trimestre; curl con User-Agent identificado) para 8 CUSIP × 4 trimestres.
- Verificación: XML de EDGAR (13F infotable) de IronBridge, Marex, Kaleidoscope, Wolverine, Envestnet y de Goldman (1T y 2T); `primary_doc.xml` de Goldman (lista de filiales y números de archivo); listados `browse-edgar` de los CIK 769993, 1055957, 886982 y 1761325; 10-Q del trust de Stellar (extracto del texto).
- Ficheros temporales solo en el área temporal; no se descargó nada al proyecto. Totales por ETF y trimestre coinciden con los de R21 (Bitwise 66,3 / 29,7 / 71,7 M$).
