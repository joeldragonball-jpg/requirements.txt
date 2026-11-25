# Lectura directa de EDGAR con Chrome (25-nov-2026)

Método: extensión de Chrome sobre www.sec.gov (carga de /Archives/ y data.sec.gov/submissions; sin captchas). Datos leídos del XML de la tabla de información de cada 13F-HR y del 10-Q. Sin recomendaciones. Nivel P = documento oficial leído.

## 1. 13F-HR del 3T-2026 (periodo 30-sep-2026), presentados el 16-nov-2026

| Dato | Valor leído | Fuente (EDGAR) | Nivel | Diferencia con el repo | Campo a corregir |
|---|---|---|---|---|---|
| Goldman Sachs Group: fecha de presentación | 13F-HR, 2026-11-16, acc. 0000886982-26-000647 | https://www.sec.gov/Archives/edgar/data/886982/000088698226000647/ | P | El repo no da la fecha de presentación | gestoras-13f.json, goldman.hechos[d=2026-09-30]: añadir «presentado 16-nov-2026» |
| Goldman: Bitwise XRP | 2.307.591 acc.; 38.375.238 USD | misma, Submit_this.xml (CUSIP 09174F107) | P | Coincide (38,4 M$) | ninguno |
| Goldman: Franklin XRP | 2.953.228 acc.; 47.783.229 USD | idem (CUSIP 355233107) | P | Coincide (47,8) | ninguno |
| Goldman: Canary XRP | 2.108.998 acc.; 33.258.898 USD | idem (13723M100) | P | Coincide (33,3) | ninguno |
| Goldman: Grayscale XRP | 503.523 acc.; 14.501.462 USD | idem (38965L106) | P | Coincide (14,5) | ninguno |
| Goldman: 21Shares XRP | 695.767 acc.; 10.081.664 USD | idem (90137T103) | P | Coincide (10,1) | ninguno |
| Goldman: REX-Osprey (1,3 M$ en el repo) | No localizada por nombre con XRP/OSPREY ni por CUSIP 74347/76/90 en el XML | idem | [VERIFICAR] | El repo la da como P (1,3 M$) | goldman.hechos (3T): marcar REX-Osprey 1,3 M$ como [VERIFICAR] hasta localizar la línea; las 5 posiciones leídas suman 143,99 M$ (el repo dice ≈145 M$ con 6 fondos) |
| Susquehanna (SIG): fecha | 13F-HR, 2026-11-16, acc. 0001446194-26-000009 | https://www.sec.gov/Archives/edgar/data/1446194/000144619426000009/ | P | El repo no da fecha | gestoras-13f.json, sig.hechos: añadir «presentado 16-nov-2026» |
| SIG: acciones en 5 ETF (sin opciones) | Bitwise 878.786 (14,61 M$); Franklin 421.700 (6,82); Canary 300.821 (4,74); Grayscale 199.374 (5,74); 21Shares 12.572 (0,18). Total 1.813.253 acc.; 32.105.403 USD | idem (file.XML / .txt) | P | Coincide con 32,1 M$ y ≈879.000 de Bitwise | ninguno |
| SIG: opciones sobre los mismos ETF | Bitwise: put 204.200/208.400 acc. nocionales (3,47 M$) y call 204.200 (3,40 M$); Canary call 176.300 (2,78); Franklin call 55.800 (0,90); Grayscale call 7.000 (0,20) | idem | P | El repo no menciona opciones de SIG (sí las de Jane Street) | sig.papel_etf: añadir que también declara opciones (≈10,7 M$ nocionales); no suman a los 32,1 M$ |
| Schonfeld: fecha | 13F-HR, 2026-11-16, acc. 0001665241-26-000003 | https://www.sec.gov/Archives/edgar/data/1665241/000166524126000003/ | P | Sin fecha en el repo | schonfeld.hechos: añadir «presentado 16-nov-2026» |
| Schonfeld: Bitwise XRP | 600.000 acc.; 9.978.000 USD (16,63 $/acc.) | idem, Submit_this/info table | P | Coincide (600.000; ≈10,0 M$) | ninguno |

Nota: la URL de la ficha en el JSON apunta a la lista de presentaciones (browse-edgar); la URL directa del documento es la de la tabla anterior.

## 2. Bitwise XRP ETF (CIK 0002039525) y Evernorth (CIK 0002092592), noviembre 2026

| Dato | Valor | Fuente | Nivel | Diferencia con el repo | Campo a corregir |
|---|---|---|---|---|---|
| Bitwise XRP: único documento de nov-2026 en su ficha | 10-Q presentado el 6-nov-2026, periodo 30-sep-2026 (sin 8-K/424B/N-PORT en nov) | https://www.sec.gov/Archives/edgar/data/2039525/000119312526451776/xrp-20260930.htm | P | Coherente | ninguno |
| Bitwise: acciones a 30-sep | 36.990.000 (31-dic-2025: 11.800.000) | idem | P | Coincide con etf-flujos.json | ninguno |
| Bitwise: activos netos / NAV por acción | 614.850 miles USD; 16,62 USD | idem | P | Coincide | ninguno |
| Bitwise: XRP en custodia a 30-sep | 413.140.980,47 XRP; valor razonable 615,0 M$ (coste 634,9 M$) | idem (calendario de inversiones) | P | El repo da el dato diario de la web de Bitwise (otras fechas); a 30-sep no hay cifra de XRP registrada en el JSON que revisé | etf-flujos.json, nota Bitwise XRP: añadir 413.140.980 XRP a 30-sep-2026 como anclaje P del dato trimestral |
| Evernorth (XRPN): presentaciones nov | 10-Q 13-nov (periodo 30-sep); 8-K/A 17-nov (evento 9-oct); varias 424B3 el 13 y 17-nov | https://www.sec.gov/Archives/edgar/data/2092592/000162828026073871/xrpn-20260930.htm ; .../000162828026074319/xrpn-20261009.htm | P | W04-etf (4. Evernorth) los daba solo como [S] por prensa | W04-etf.md sección 4: subir a P la existencia del cierre y listado (símbolos XRPN y XRPNW en Nasdaq, 8-K del 9-oct) |
| Evernorth: XRP en poder a 30-sep-2026 | «aproximadamente 346 millones de XRP» (10-Q, 13-nov) | idem 10-Q | P | El repo dice ≈473 M XRP (nota de prensa del 9-oct, [S]); 346 M es el saldo a 30-sep, anterior o distinto al del cierre. Posible diferencia temporal, no contradicción probada | W04-etf.md sección 4: mostrar ambos con fecha («346 M a 30-sep, 10-Q [P]; 473 M, prensa 9-oct [S]») y [VERIFICAR] qué explica la diferencia |
| Evernorth: acciones en circulación | El 10-Q muestra 1 acción ponderada (la sociedad contable del periodo previo al cierre); no hay cifra útil de acciones post-fusión en lo leído | idem | [VERIFICAR] | Sin cifra en el repo | Leer portada del 424B3 del 17-nov (no abierta) |

## Límites
- No se abrió el 424B3 de Evernorth ni las N-PORT (el ETF de Bitwise es un trust de materias primas y no presenta N-PORT).
- REX-Osprey de Goldman no localizada; Goldman presenta otras posiciones que no son XRP y el filtro por nombre pudo no cubrirla.
- Un lector de página del navegador bloqueó una consulta por texto con URL; se repitió con salida acotada.
