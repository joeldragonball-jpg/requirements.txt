# Chrome: lote de datos pasados a [P] (12-nov-2026)

Método: extensión de Chrome (pestaña nueva, sin captchas, sin descargas al repo), lectura en pantalla. Previos [S] en `2026-11-12-C203-C229-C233-lote-B3.md`. Sin volcado a JSON.

| Dato | Valor y unidad | Fecha | URL leída | Nivel |
|---|---|---|---|---|
| SMI 2026 (RD 126/2026, de 18-feb) | 40,70 €/día o 1.221 €/mes (art. 1); el BOE núm. 44 es de 19-feb-2026. Las 14 pagas / 17.094 € anuales / +3,1 % no están en el art. 1: siguen [S] | publ. 19-feb-2026 | boe.es/buscar/act.php?id=BOE-A-2026-3815&tn=1 | [P] |
| Euríbor 12 m, media octubre | 3,239 % | oct-2026 | bde.es/webbe/es/estadisticas/temas/tipos-interes.html (estadísticas del BdE, «últimos datos») | [P] (BdE; la fuente de origen es EMMI) |
| €STR (dato diario) | 2,439 % | 11-nov-2026 | misma página BdE | [P] |
| Euríbor 3 m (último diario) | 2,754 % | 11-nov-2026 | misma página BdE | [P] |
| Euríbor 12 m, último diario | No obtenido (BdE solo da el mensual; EMMI exige cuenta) | n/d | emmi-benchmarks.eu/benchmarks/euribor/rate/ | bloqueado |
| OMIE, precio medio octubre España (mercado diario) | 166,66 €/MWh = media simple de los 31 precios medios aritméticos diarios del gráfico mensual de OMIE (calculada aquí; no es media ponderada por energía). Rango diario: mín 76,28 (18-oct), máx 244,69 (30-oct); 31-oct 208,98 | oct-2026 | omie.es/es/market-results/monthly/daily-market/daily-market-price?scope=monthly&year=2026&month=10 (series del gráfico) | [P] los diarios; la media, cálculo propio |
| OMIE, último día publicado | 210,94 €/MWh (media aritmética, España = Portugal) el 11-nov; 163,19 €/MWh el 1-nov | 11-nov-2026 | omie.es/es/market-results/daily/daily-market/day-ahead-price?scope=daily&date=2026-11-11 | [P] |
| REE: generación total octubre (nacional) | 22.694.321 MWh (≈22,7 TWh). Mix: nuclear 21,7 %, ciclo combinado 21,4 %, solar fotovoltaica 21,0 %, eólica 17,5 %, hidráulica 7,1 %, cogeneración 4,8 %, resto <2 % cada uno (carbón 0,4 %, solar térmica 1,2 %) | oct-2026 (act. 11-nov) | apidatos.ree.es/es/datos/generacion/estructura-generacion (API de REData, mismo origen que ree.es/es/datos) | [P] (unidad MWh inferida de la magnitud) |
| REE: demanda octubre | 20.613.753 MWh (≈20,6 TWh) | oct-2026 | apidatos.ree.es/es/datos/demanda/evolucion | [P] (unidad MWh inferida) |
| IPC definitivo de octubre por grupos | No publicado (INE: 13-nov). Solo el adelantado: general 4,9 % anual y 0,6 % mensual; subyacente 3,1 % anual | 30-oct-2026 | ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176802&menu=ultiDatos&idp=1254735976607 | [P] solo el adelantado |
| Brent spot (EIA, USD/barril) | 4-nov 91,84 · 5-nov 97,96 · 6-nov 97,83 (también 3-nov 107,03; 9-nov 91,03; 10-nov 90,16) | nov-2026 | eia.gov/petroleum/prices/table.php (redirección de pet_pri_spt_s1_d.htm) | [P] |
| WTI spot (EIA, USD/barril) | 4-nov 91,73 · 5-nov 94,05 · 6-nov 94,37 (3-nov 99,64; 9-nov 90,40; 10-nov 89,62) | nov-2026 | misma | [P] |
| Brent y WTI, 23-oct | Brent 128,30 USD/barril; WTI 109,72 USD/barril. Semana 19-23 oct Brent: 118,82 · 115,22 · 117,37 · 125,39 · 128,30 | 23-oct-2026 | eia.gov/dnav/pet/hist/RBRTED.htm y RWTCD.htm | [P] |
| Oro 3T-2026, demanda total (WGC) | 1.369 t (−1 % interanual, incluye OTC); acumulado 3.881 t (2025: 3.884 t); valor 3T 43.000 M USD; precio LBMA PM medio 4.262 USD/oz | 3-nov-2026 | gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-q3-2026 | [P] |
| Oro, bancos centrales 3T | 321 t; acumulado 675 t (+6 % interanual). ETF: +211 t; barras y monedas 268 t (−19 %) | 3-nov-2026 | misma | [P] |

## Notas y discrepancias
- **Brent del 23-oct: la discrepancia queda cerrada, pero con un tercer valor.** EIA da 128,30 USD/barril, no 116,72 ni 111,97. Esos dos valores previos no coinciden con el spot FOB de EIA para ese día (pueden ser futuros u otro instrumento o fecha; [VERIFICAR] su origen). Aplica la nota «titulares con umbral: no es el cierre».
- El Brent spot de EIA cayó de 107,03 (3-nov) a 91,84 (4-nov) (−14 % en un día) y rebotó a 97,96 el 5-nov; el 10-nov era 90,16. Hecho, no explicado aquí.
- En la nota de WGC, el resumen dice «total supply edged down 1% to 1,369t», igual que la demanda (1.369 t): coincidencia en el texto, no se ha leído la tabla XLSX.
- La media mensual de OMIE de 166,66 €/MWh es cálculo propio; la cifra oficial ponderada puede diferir algo. Los 79,43 €/MWh de Selectra quedan descartados (muy lejos).
- Los 4,9 % de IPC y el Euríbor 3,239 % apuntan en la misma dirección que lo anotado como [S].

## Siguió bloqueado
- Euríbor 12 m diario (EMMI exige registro; no se creó cuenta).
- IPC definitivo por grupos (aún no publicado).
- RD 126/2026: 14 pagas, 17.094 €/año y +3,1 % no leídos en el texto consolidado (solo art. 1: €/día y €/mes).
- No intentado por falta de tiempo/alcance: ficha MSCI, escrow XRPL, AGSI+.

## Lecciones
1. REData y OMIE son SPA: el texto de la página no trae cifras, pero los gráficos (Highcharts en OMIE) y la API pública `apidatos.ree.es` (con `fetch` desde la pestaña de ree.es) devuelven los datos exactos; REE devuelve MWh aunque la web rotule GWh.
2. EIA: la tabla histórica va retrasada (release del 4-nov); la tabla diaria `eia.gov/petroleum/prices/table.php` trae los últimos días. Leer con JS por filas, no con `get_page_text`.
3. El BdE publica en su portada de tipos de interés el Euríbor 12 m mensual y el 3 m/€STR diarios (URL `webbe`, no `wbe`); EMMI exige cuenta.
