# C61 · Servicios públicos y estabilidad (INICIO, 10-nov-2026) — cobertura muy baja

Sesión cortada por cuota (~5 min). WebSearch no devuelve tablas por país; hacen falta las APIs/PDF directos (Banco Mundial WDI/WGI, OCDE, Eurostat, UNODC), vía script o navegador. No se ha creado `explorador/estabilidad.json` (no hay suficientes cifras verificadas para no inventar).

## Cifras halladas (todas [S], sin abrir la primaria)
- Sanidad, OCDE *Health at a Glance 2025* (nov-2025): gasto sanitario medio OCDE 9,3 % del PIB en 2024; esperanza de vida media OCDE 81,1 años en 2023; Reino Unido 81 años (0,1 menos que la media). Fuente: oecd.org nota de prensa 11-2025 y country notes (hay nota por país en oecd.org/en/publications/health-at-a-glance-2025_15a55280-en/). Por país: sin dato aún.
- Vivienda, Eurostat vía Euronews (31-oct-2026), sobrecarga del coste de vivienda (>40 % de la renta disponible), 2025: media UE 7,7 %; Alemania 11,2 %; España 7,2 %. Países Bajos y Polonia: sin dato (dataset tespm140). [S]/[VERIFICAR] hasta abrir Eurostat.
- Educación, OCDE PISA 2022 (matemáticas): media OCDE 472; Japón en el grupo superior. Puntuaciones por país: sin dato verificado (tabla I.B1.2.1).
- Gobernanza: el Banco Mundial publicó WGI 2025 con metodología revisada y escala 0-100 (datos en govindicators.org / data.worldbank.org GOV_WGI_*); valores por país sin extraer. Nota de comparabilidad: la revisión recalcula la serie desde 1996, no mezclar con ediciones antiguas.
- Homicidios: UNODC (dataportal) / Banco Mundial VC.IHR.PSRC.P5, serie hasta 2023; valores por país sin extraer.

## Huecos (todo lo demás)
Sistema sanitario, camas/médicos, alquiler/precio vs. ingresos, FBCF pública, LPI, banda ancha, subsidio de desempleo (OCDE), pensiones, salario mínimo, abandono escolar, CPI de Transparencia, demografía/migración, hitos y «lecturas» por país: sin empezar. Los 12 países pendientes.

## Siguiente paso recomendado
Script (sin IA) que baje de la API del Banco Mundial (WDI+WGI), Eurostat y OCDE los indicadores por los 12 códigos de país y genere `explorador/estabilidad.json`; las «lecturas» y los hitos, después, a mano con fuente.

---

# 2.ª pasada (10-nov-2026) — tablas con fuente primaria (12 países)

Método: API del Banco Mundial (WDI, actualización 8-oct-2026; WGI 2025, actualización 25-sep-2026; los datos de salud vienen de OMS/GHED, UNESCO, UNODC, ONU), Eurostat (dissemination 1.0, act. 21-oct a 6-nov-2026). Todos **[P]** (leídos en origen el 10-nov). Cada celda lleva su año; **no son del mismo año entre países** y no se ordenan. Sin recomendaciones. Esta pasada rellena los «sin dato» del bloque anterior (no se ha tocado `explorador/estabilidad.json`: el volcado queda para C39).

Códigos: US EE. UU. · CN China · JP Japón · IN India · RU Rusia · UK R. Unido · DE · FR · IT · ES · NL · PL.

## 1. Sanidad (Banco Mundial; origen OMS GHED / UN IGME)
| País | Gasto sanitario total % PIB | Gasto público sanitario % PIB | Pago directo % gasto | Esperanza de vida 2024 | Médicos /1.000 | Camas /1.000 | Mort. <5 años /1.000 (2024) |
|---|---|---|---|---|---|---|---|
| US | 16,69 (2023) | 9,01 (2023) | 10,93 (2023) | 78,89 | 3,68 (2022) | 2,68 (2022) | 6,5 |
| CN | 5,94 (2023) | 3,39 (2023) | 32,17 (2023) | 78,02 | 3,11 (2022) | 5,63 (2023) | 5,7 |
| JP | 10,74 (2023) | 9,11 (2023) | 12,24 (2023) | 84,04 | 2,65 (2022) | 12,59 (2022) | 2,4 |
| IN | 3,34 (2023) | 1,30 (2023) | 43,89 (2023) | 72,23 | 0,72 (2020) | 1,59 (2021) | 26,6 |
| RU | 7,04 (2023) | 4,93 (2023) | 28,39 (2023) | 73,44 | 5,11 (2022) | 6,81 (2023) | 5,2 |
| UK | 11,13 (2024) | 8,99 (2023) | 14,56 (2024) | 81,39 | 3,30 (2023) | 2,42 (2022) | 4,7 |
| DE | 12,27 (2024) | 9,29 (2023) | 10,71 (2024) | 80,79 | 4,53 (2022) | 7,55 (2023) | 3,7 |
| FR | 11,54 (2024) | 7,89 (2024) | 9,23 (2024) | 82,98 | 3,28 (2022) | 5,65 (2022) | 4,3 |
| IT | 8,44 (2024) | 6,14 (2023) | 22,31 (2024) | 83,95 | 4,19 (2022) | 3,06 (2022) | 2,7 |
| ES | 9,22 (2023) | 6,75 (2023) | 20,86 (2023) | 83,89 | 4,29 (2022) | 2,91 (2023) | 3,2 |
| NL | 10,01 (2024) | 6,72 (2023) | 11,79 (2024) | 81,97 | 3,88 (2022) | 2,42 (2022) | 3,9 |
| PL | 8,06 (2024) | 5,50 (2023) | 16,21 (2024) | 78,41 | 4,03 (2023) | 6,04 (2022) | 4,2 |

Más sanidad (Banco Mundial/OMS): mortalidad materna por 100.000 nacidos vivos 2023 (modelada) — US 17, CN 16, JP 3, IN 80, RU 9, UK 8, DE 4, FR 7, IT 6, ES 3, NL 4, PL 2. Vacuna del sarampión a 12-23 meses 2024 (%): US 92, CN 95, JP 95, IN 97, RU 97, UK 89, DE 96, FR 95, IT 95, ES 97, NL 89, PL 92.
Contexto OCDE (*Health at a Glance 2025*): media OCDE 9,3 % del PIB en 2024 (ya citado arriba). El gasto total incluye el privado; no equivale al gasto público.

## 2. Educación, I+D e infraestructuras
| País | Gasto público educación % PIB | I+D % PIB (2023) | Banda ancha fija /100 hab. | Inversión (FBCF) % PIB | Importación neta de energía % uso (2024) | LPI logística (2022, 1-5) |
|---|---|---|---|---|---|---|
| US | 5,42 (2021) | 3,45 | 38,86 (2024) | 21,35 (2024) | −9,78 (exportador neto) | 3,8 |
| CN | 3,90 (2023) | 2,58 | 47,19 (2024) | 39,65 (2024) | 24,02 | 3,7 |
| JP | 3,34 (2021) | 3,44 | 38,63 (2023) | 27,81 (2024) | 87,28 | 3,9 |
| IN | 4,10 (2022) | 0,65 (2020) | 3,15 (2024) | 31,68 (2025) | 36,03 | 3,4 |
| RU | 4,16 (2023) | 0,94 (2024) | 27,13 (2024) | 23,09 (2025) | −70,73 (exportador neto) | 2,6 |
| UK | 5,91 (2021) | 2,68 | 42,16 (2024) | 18,88 (2025) | 47,56 | 3,7 |
| DE | 5,24 (2022) | 3,15 | 45,61 (2024) | 20,31 (2025) | 70,26 | 4,1 |
| FR | 5,32 (2022) | 2,18 | 48,93 (2024) | 22,02 (2025) | 41,75 | 3,9 |
| IT | 4,07 (2022) | 1,38 | 31,78 (2024) | 21,83 (2025) | 79,19 | 3,7 |
| ES | 4,59 (2022) | 1,49 | 39,23 (2024) | 20,61 (2025) | 78,37 | 3,9 |
| NL | 5,18 (2022) | 2,27 | 42,98 (2024) | 19,80 (2025) | 88,38 | 4,1 |
| PL | 4,31 (2022) | 1,56 | 25,36 (2024) | 17,03 (2025) | 46,78 | 3,6 |

Educación UE (Eurostat edat_lfse_14, abandono 18-24, 2025): UE 9,1 · DE 13,1 · ES 12,8 · FR 7,2 · IT 8,2 · NL 7,4 · PL 4,0. PISA 2022 (OCDE): sigue sin extraerse de la tabla primaria → [VERIFICAR].

## 3. Gasto público por función, UE (Eurostat gov_10a_exp, COFOG, % PIB, 2024) [P]
| País | Sanidad | Orden público y seguridad | Educación | Vejez (pensiones) |
|---|---|---|---|---|
| UE-27 | 7,3 | 1,7 | 4,7 | 10,6 |
| DE | 7,6 | 1,6 | 4,5 | 9,9 |
| ES | 6,5 | 1,8 | 4,1 | 10,4 |
| FR | 8,9 | 1,8 | 5,1 | 13,4 |
| IT | 6,6 | 1,8 | 4,0 | 13,9 |
| NL | 7,3 | 1,9 | 5,1 | 6,1 |
| PL | 6,1 | 2,4 | 5,6 | 10,8 |

## 4. Seguridad y gobernanza
Gobernanza: Banco Mundial WGI 2025, edición revisada (puntuación 0-100; **no comparable con ediciones antiguas** en escala −2,5/+2,5). Son **percepciones** agregadas.
| País | Estabilidad política | Estado de derecho | Eficacia del gobierno | Control corrupción | Homicidios /100.000 | Muertes tráfico /100.000 (2019) | Suicidio /100.000 (2021) |
|---|---|---|---|---|---|---|---|
| US | 60,3 | 71,7 | 76,7 | 65,5 | 5,76 (2023) | 12,7 | 15,63 |
| CN | 66,0 | 51,6 | 65,1 | 49,5 | 0,5 (2020) | 17,4 | 8,95 |
| JP | 87,7 | 84,1 | 94,1 | 77,4 | 0,23 (2023) | 3,6 | 17,43 |
| IN | 55,0 | 56,5 | 62,6 | 42,4 | 2,82 (2022) | 15,6 | 12,56 |
| RU | 49,1 | 37,7 | 42,1 | 28,2 | 6,77 (2021) | 12,0 | 21,37 |
| UK | 70,7 | 79,5 | 77,6 | 78,9 | 1,12 (2021) | 3,2 | 9,55 |
| DE | 69,3 | 85,1 | 82,8 | 81,9 | 0,91 (2023) | 3,8 | 12,90 |
| FR | 64,0 | 74,6 | 77,1 | 73,1 | 1,34 (2023) | 5,1 | 16,58 |
| IT | 73,6 | 68,3 | 71,3 | 59,8 | 0,57 (2023) | 5,3 | 6,99 |
| ES | 68,7 | 73,0 | 75,5 | 61,2 | 0,69 (2023) | 3,9 | 8,72 |
| NL | 75,0 | 86,2 | 88,0 | 85,9 | 0,69 (2023) | 4,0 | 11,50 |
| PL | 77,8 | 68,0 | 68,6 | 65,2 | 0,80 (2023) | 9,4 | 13,67 |

Homicidios: UNODC vía Banco Mundial (definiciones nacionales distintas; Rusia y R. Unido de 2021, China de 2020: años desactualizados). Tráfico y suicidio son estimaciones OMS, no las cifras oficiales nacionales (DGT, NHTSA…).

## 5. Demografía, mercado laboral y desigualdad
| País | Población 2025 (M) | 65+ % (2025) | Hijos por mujer (2024) | Migración neta 2025 (miles) | Paro juvenil 15-24 OIT 2025 % | Gini (año) |
|---|---|---|---|---|---|---|
| US | 341,8 | 18,4 | 1,63 | +1.231 | 9,3 | 41,8 (2024) |
| CN | 1.406,6 | 14,9 | 1,01 | −268 | 15,8 | 36,0 (2022) |
| JP | 123,4 | 30,0 | 1,15 | +141 | 3,9 | 32,3 (2020) |
| IN | 1.463,9 | 7,4 | 1,96 | −496 | 16,0 | 23,0 (2023, consumo) |
| RU | 143,5 | 17,8 | 1,42 | −252 | 7,6 | 33,0 (2023) |
| UK | 69,5 | 19,7 | 1,55 | +390 | 14,7 | 32,4 (2021) |
| DE | 83,5 | 23,7 | 1,36 | −334 | 6,9 | 33,7 (2022) |
| FR | 68,7 | 22,5 | 1,61 | +92 | 18,9 | 31,8 (2023) |
| IT | 58,9 | 25,1 | 1,18 | +75 | 20,6 | 34,3 (2023) |
| ES | 49,4 | 21,6 | 1,10 | +97 | 24,8 | 33,4 (2023) |
| NL | 18,1 | 20,9 | 1,43 | +105 | 8,8 | 25,7 (2021) |
| PL | 36,4 | 20,8 | 1,14 | −331 | 10,7 | 28,5 (2023) |

Nota: la migración neta del Banco Mundial es estimación de la ONU (WPP) con revisiones grandes (Alemania −334 mil en 2025 contrasta con lo que cabría esperar: [VERIFICAR] en Destatis). Paro juvenil OIT es modelado y difiere de Eurostat mensual (sep-2026: ES 22,8 %, FR 21,9 %, IT 19,9 %). Gini de India es de consumo, no de renta; los de la UE (EU-SILC 2025: UE 29,2 · DE 30,1 · ES 30,8 · FR 30,4 · IT 31,0 · NL 25,9 · PL 24,9) no son comparables con los del Banco Mundial.

## 6. Vivienda y pobreza (UE, Eurostat) [P]
- Precio de la vivienda, variación anual 2026-T2 (prc_hpi_q, act. 1-oct): UE +4,7 · DE +0,6 · ES **+12,1** · FR −0,8 · IT +4,0 · NL +4,3 · PL +6,3.
- AROPE 2025 (pobreza o exclusión): UE 20,9 · DE 21,2 · ES 25,7 · FR 20,8 · IT 22,6 · NL 15,8 · PL 15,0 (ilc_peps01n, act. 20-oct).
- Sobrecarga del coste de vivienda (>40 % de la renta, 2025): UE 7,7 · DE 11,2 · ES 7,2 — cifras de Euronews 31-oct, siguen [S] (el dataset tespm140 no respondió por API con los parámetros usados) → [VERIFICAR].
- Vivienda fuera de la UE (precio/ingresos, alquiler de UK, JP, CN, IN, RU): sin dato primario abierto → [VERIFICAR].

## 7. Cobertura y huecos tras esta pasada
Cubierto con fuente primaria: sanidad, educación (gasto), I+D, infraestructuras digitales/energía/logística, seguridad (homicidios, tráfico, suicidio), WGI, demografía, Gini, COFOG UE, vivienda UE.
Sigue sin primaria: PISA por país (OCDE), subsidio de desempleo (OCDE), pensiones fuera de la UE, CPI de Transparencia Internacional, electricidad doméstica, delincuencia no homicida, hitos y reformas por país, tespm140.

## 8. Lectura (hechos / opinión)
- HECHO: el gasto público sanitario ronda el 9 % del PIB en DE, UK, US y JP, frente a 1,3 % en IN y 3,4 % en CN; el pago directo del paciente es 43,9 % del gasto en India frente a 9-11 % en FR, DE y US.
- HECHO: el envejecimiento es desigual: 65+ en Japón 30,0 % e Italia 25,1 % frente a India 7,4 %; la fecundidad de China (1,01), España (1,10) y Polonia (1,14) está entre las más bajas.
- HECHO: España destaca por el paro juvenil (24,8 % OIT 2025; 22,8 % Eurostat sep-2026) y por el precio de la vivienda (+12,1 % i.a. en T2-2026); su gasto en sanidad (6,5 % PIB COFOG) está por debajo de la media UE (7,3 %).
- Sesgo: los WGI son percepciones y la revisión metodológica recalcula series; la puntuación de un año no permite inferir estabilidad futura [ESPECULACIÓN].
