# C59 · Indicadores económicos y sociales (parcial, 10-nov-2026)

Sesión corta con WebSearch (sin leer PDF oficiales: casi todo es [S] salvo donde se indica que el buscador enlaza la nota oficial). No se ha escrito `leer_indicadores()` ni `indicadores-manual.json` (pendiente). Sin recomendaciones.

## Cifras recogidas (último dato publicado)
| País/zona | Indicador | Dato | Periodo | Fuente | Nivel |
|---|---|---|---|---|---|
| Zona euro | IPCA (estimación rápida) | 4,0 % i.a. (sept 3,8 %); energía 20,8 %; subyacente 2,5 % | oct-2026 (pub. 4-nov) | Eurostat flash vía prensa; final 18-nov | [S] |
| Alemania / Italia / Francia | IPCA flash | 2,8 % / 5,6 % / 3,8 % | oct-2026 | Eurostat vía prensa | [S] |
| España | IPC adelantado | 4,9 % i.a. (igual que sept); subyacente 3,1 %; IPCA 4,9 %; mensual 0,6 % | oct-2026 (pub. 30-oct); dato definitivo 13-nov | INE (ine.es/dyngs/Prensa/adIPC1026) | [S] (nota INE localizada, no abierta) |
| España | PIB | +0,6 % t/t Q3 (una décima menos) | Q3-2026 | INE vía prensa | [S] |
| Zona euro / UE | Paro | 6,5 % (UE 6,2 %); paro juvenil 15,4 % (UE 15,5 %) | sept-2026 (pub. 30-oct) | Eurostat vía prensa | [S] |
| Zona euro / UE | PIB flash | +0,4 % t/t (UE +0,5 %); +1,3 % i.a. (UE +1,5 %) | Q3-2026 (pub. 30-oct); 2.ª estimación 13-nov | Eurostat euro-indicators 2-30102026-ap | [S] |
| EE. UU. | IPC | 3,7 % i.a. (ago 3,4 %); subyacente 2,6 %; energía +20,4 %, gasolina +34,2 % | sept-2026 (pub. 14-oct) | BLS (cpi_10142026) | [S] (BLS enlazado por buscador) |
| EE. UU. | Paro / nóminas | 4,2 % (ago 4,1 %); +29.000 empleos | sept-2026 (pub. 2-oct) | BLS Employment Situation | [S] |
| Japón | IPC nacional | 2,1 % general y subyacente; sin alimentos frescos ni energía 2,4 %; BoJ 1,25 % | sept-2026 | Oficina estadística vía prensa | [S] |
| Japón | Paro | 2,5 % | ago-2026 | prensa | [S]/[VERIFICAR] sept |
| China | IPC | +0,9 % i.a.; PPI +5,0 % | sept-2026 | NBS vía prensa | [S] |
| China | PIB | Q3 +4,5 % i.a.; ene-sep +4,6 % (solo titular) | Q3-2026 (19-oct) | NBS vía Mysteel | [VERIFICAR] |
| Rusia | IPC | 6,35 % i.a. (Rosstat); semanal ~7,1-7,2 % a 5-oct tras tarifas; tipo BCR 14 %; previsión 2026: 7,1-7,6 % | sept-2026 / oct | Rosstat y BCR vía prensa | [S] (contradictorio: 6,35 vs ~7,1; distintas medidas) |
| Reino Unido | IPC / paro | Sin dato fiable de sept-2026 (un resultado habla de 3,5 % y paro 4,7 %, sin periodo) | — | — | [VERIFICAR] (ons.gov.uk) |
| India | IPC | Sin dato (solo WPI sept 11,39 %, no es IPC) | — | — | [VERIFICAR] (MoSPI) |
| Países Bajos, Polonia | Todos | no buscados | — | — | pendiente |

## Lectura (hechos vs opinión)
- HECHO (según prensa): choque energético generalizado (energía +20 % en zona euro y EE. UU.) lleva el IPC a 4,0-4,9 % en euro/España y 3,7 % en EE. UU.; la prensa lo vincula a la guerra de Irán [S].
- Definiciones distintas: IPCA vs IPC nacional vs PCE; España 4,9 % (IPC y IPCA coinciden en el adelantado). No ordenar países.
- Alcista (para ritmo de actividad): euro área +0,4 % t/t pese al choque. Bajista: nóminas EE. UU. +29 mil, paro juvenil euro 15,4 %, tipos altos en Rusia.

## Calendario (a verificar en fuente oficial antes de pasar a eventos/calendario.toml)
- INE IPC definitivo oct: 13-nov-2026 · Eurostat IPCA final oct: 18-nov · Eurostat PIB 2.ª estimación: 13-nov. No se ha tocado calendario.toml.

## Pendiente
Pobreza AROPE, Gini, deuda/déficit, salario mínimo; datos de DE/FR/IT/NL/PL de paro y PIB; UK e India; función `leer_indicadores()`.

---

# 2.ª pasada (10-nov-2026) — fuentes primarias por API

Método: consultas directas a las API públicas de Eurostat (dissemination 1.0), BLS (v1), OCDE (SDMX), FMI (DataMapper/WEO) y Banco Mundial (WDI). Nivel **[P]** = leído en la base primaria el 10-nov-2026. «e» = estimación rápida (flash). No se ordenan países ni se recomienda nada. Esta pasada **corrige/sustituye** las cifras [S] de arriba cuando difieren (se indica).

## 1. Inflación (variación anual, %)
| País/zona | Indicador | Valor | Periodo | Fuente |
|---|---|---|---|---|
| Zona euro (EA21) | IPCA general | 4,0 (e) · ant. 3,8 | oct-2026 | Eurostat prc_hicp_minr (act. 4-nov) [P] |
| UE-27 | IPCA general | 3,8 · ant. 3,2 | sep-2026 | Eurostat [P] (oct aún no publicado) |
| Alemania | IPCA | 2,8 (e) · ant. 3,3 | oct-2026 | Eurostat [P] |
| Francia | IPCA | 3,8 (e) · ant. 3,4 | oct-2026 | Eurostat [P] |
| Italia | IPCA | 5,6 (e) · ant. 4,2 | oct-2026 | Eurostat [P] |
| España | IPCA | 4,9 (e) · ant. 5,0 | oct-2026 | Eurostat [P] (INE IPC 4,9 % adelantado; definitivo 13-nov) |
| Países Bajos | IPCA | 3,3 (e) · ant. 3,0 | oct-2026 | Eurostat [P] |
| Polonia | IPCA | 4,0 · ant. 3,5 | sep-2026 | Eurostat [P] (oct no publicado) |
| EE. UU. | IPC-U (NSA) | 3,74 (calculado del índice 336,940 / 324,800) · ant. 3,40 (OCDE) | sep-2026 | BLS API CUUR0000SA0 [P]; OCDE 3,74 [P] |
| EE. UU. | IPC subyacente (sin alim. ni energía) | 2,56 (339,287 / 330,804) | sep-2026 | BLS API CUUR0000SA0L1E [P] |
| Reino Unido | IPC | **3,6** · ant. 3,3 | sep-2026 | OCDE (datos ONS) [P]. Difiere del 3,5 del 2-nov: [VERIFICAR] en ons.gov.uk |
| China | IPC | 0,9 · ant. 0,8 | sep-2026 | OCDE (datos NBS) [P] |
| India | IPC | 5,57 · ant. 4,96 (base nueva) | sep-2026 | OCDE (datos MoSPI) [P]; la prensa daba 5,54 |
| Japón, Rusia | IPC | OCDE no devuelve serie | — | [VERIFICAR] (e-Stat / Rosstat); se mantienen los [S] de arriba |

Calendario comprobado: **IPC EE. UU. de octubre sale hoy 10-nov** (BLS aún no lo tenía en la API a la hora de la consulta); INE definitivo 13-nov; Eurostat final oct 18-nov [P, confirmar en calendarios oficiales].

## 2. Empleo
| País/zona | Indicador | Valor | Periodo | Fuente |
|---|---|---|---|---|
| EE. UU. | Paro | **4,1 %** (sep 4,2 %) | oct-2026 | BLS API LNS14000000 [P] — actualiza el 4,2 de arriba |
| EE. UU. | Nóminas no agrícolas | +165.000 (oct); sep revisado a +60.000 (antes +29.000) | oct-2026 | BLS API CES0000000001 (diferencia de niveles) [P] |
| Zona euro (EA21) | Paro | 6,5 % | sep-2026 | Eurostat une_rt_m [P] |
| UE-27 | Paro | 6,2 % | sep-2026 | Eurostat [P] |
| Alemania | Paro | 4,1 % | sep-2026 | Eurostat [P] |
| Francia | Paro | 8,5 % (ago 8,3) | sep-2026 | Eurostat [P] |
| Italia | Paro | 6,3 % | sep-2026 | Eurostat [P] |
| España | Paro | 10,3 % (ago 10,2) | sep-2026 | Eurostat [P] |
| Países Bajos | Paro | 4,0 % | sep-2026 | Eurostat [P] |
| Polonia | Paro | 3,4 % | sep-2026 | Eurostat [P] |
| Reino Unido | Paro | 4,7 % (jun 4,9) | jul-2026 | OCDE [P] (dato más reciente en OCDE) |
| Japón | Paro | 2,4 % (ago 2,5) | sep-2026 | OCDE [P] |
| Paro juvenil (<25) | UE 15,5 · EA 15,4 · DE 7,5 · ES 22,8 · FR 21,9 · IT 19,9 · NL 8,8 · PL 11,3 | | sep-2026 | Eurostat [P] — Francia salta +1,1 pp en un mes: [VERIFICAR] revisión |
| China, India, Rusia | Paro | FMI WEO 2026: 5,1 / 5,0 / 2,2 (proyección) | 2026 | FMI [P] — sin dato mensual comparable |

## 3. Actividad (PIB real)
| País/zona | t/t | i.a. | Periodo | Fuente |
|---|---|---|---|---|
| UE-27 | +0,5 | +1,5 | 2026-T3 | Eurostat namq_10_gdp (act. 5-nov) [P] |
| Zona euro (EA20) | +0,4 | +1,3 | 2026-T3 | Eurostat [P] |
| Alemania | +0,2 | +1,2 | 2026-T3 | Eurostat [P] |
| España | +0,6 | +2,7 | 2026-T3 | Eurostat [P] |
| Francia | −0,1 | −0,1 | 2026-T3 | Eurostat [P] |
| Italia | 0,0 | +0,8 | 2026-T3 | Eurostat [P] |
| Países Bajos | +0,6 | +2,1 | 2026-T3 | Eurostat [P] |
| Polonia | +1,1 | +4,0 | 2026-T2 (T3 no publicado) | Eurostat [P] |

EE. UU. +3,4 % T3 **anualizado** (BEA, nota anterior) y China +4,5 % i.a. no son comparables con la tabla (distinta definición).

## 4. FMI WEO — proyección de crecimiento, inflación media, deuda y saldo (% PIB)
Fuente: FMI DataMapper API (`NGDP_RPCH`, `PCPIPCH`, `GGXWDG_NGDP`, `GGXCNL_NGDP`), edición vigente del WEO [P]; **[VERIFICAR]** que la edición sea Oct-2026 (la API no etiqueta la edición). Son proyecciones del FMI, no hechos: [ESPECULACIÓN] de organismo.
| País | PIB 2026 | PIB 2027 | IPC medio 2026 | Deuda bruta 2026 | Saldo 2026 |
|---|---|---|---|---|---|
| EE. UU. | 2,3 | 2,3 | 3,6 | 126,8 | −8,5 |
| China | 4,5 | 4,0 | 1,0 | 104,4 | −8,0 |
| Japón | 0,7 | 0,7 | 2,0 | 199,4 | −1,4 |
| India | 7,0 | 7,0 | 5,0 | 83,1 | −7,5 |
| Rusia | 0,9 | 0,9 | 6,1 | 19,3 | −3,2 |
| Reino Unido | 1,3 | 1,2 | 3,3 | 102,0 | −3,8 |
| Alemania | 1,3 | 1,1 | 2,7 | 64,6 | −4,3 |
| Francia | 0,4 | 0,7 | 2,4 | 118,5 | −5,4 |
| Italia | 0,8 | 0,6 | 3,3 | 137,9 | −2,9 |
| España | 2,5 | 1,8 | 3,7 | 97,6 | −2,4 |
| Países Bajos | 1,5 | 1,3 | 2,9 | 45,4 | −2,7 |
| Polonia | 3,4 | 2,5 | 3,2 | 66,6 | −7,2 |

Comparabilidad: deuda «bruta general del gobierno» del FMI puede diferir de la deuda Maastricht de Eurostat (tabla 5).

## 5. Deuda y déficit públicos observados (Maastricht, % PIB)
Fuente: Eurostat gov_10dd_edpt1 (act. 21-oct-2026) [P].
| País | Deuda 2024 | Deuda 2025 | Saldo 2024 | Saldo 2025 |
|---|---|---|---|---|
| Zona euro (EA20) | 86,6 | 87,7 | −3,0 | −3,0 |
| UE-27 | 80,3 | 81,5 | −3,1 | −3,1 |
| Alemania | 61,4 | 62,8 | −2,7 | −2,9 |
| España | 101,4 | 100,5 | −3,2 | −2,4 |
| Francia | 112,6 | 115,7 | −5,8 | −5,1 |
| Italia | 134,3 | 136,7 | −3,4 | −3,1 |
| Países Bajos | 44,0 | 44,7 | −0,7 | −1,6 |
| Polonia | 54,8 | 59,6 | −6,4 | −7,2 |

## 6. Pobreza, desigualdad y salario mínimo (UE, Eurostat [P])
| País | AROPE 2025 (%) | Gini renta disp. 2025 | Salario mín. mensual 2026-S2 (€) | Precio vivienda i.a. 2026-T2 (%) |
|---|---|---|---|---|
| UE-27 | 20,9 | 29,2 | — | +4,7 |
| Alemania | 21,2 | 30,1 | 2.343 | +0,6 |
| España | 25,7 | 30,8 | 1.425 | +12,1 |
| Francia | 20,8 | 30,4 | 1.867 | −0,8 |
| Italia | 22,6 | 31,0 | no existe mínimo legal | +4,0 |
| Países Bajos | 15,8 | 25,9 | 2.338 | +4,3 |
| Polonia | 15,0 | 24,9 | 1.119 (convertido a €) | +6,3 |
Fuentes: ilc_peps01n, ilc_di12, earn_mw_cur (act. 31-jul), prc_hpi_q (act. 1-oct). Gini fuera de la UE (Banco Mundial SI.POV.GINI, años distintos, no comparable con EU-SILC): EE. UU. 41,8 (2024), China 36,0 (2022), India 23,0 (2023, consumo, no renta), Japón 32,3 (2020), Rusia 33,0 (2023), R. Unido 32,4 (2021).

## Lectura (hechos vs interpretación)
- HECHO: el IPCA de la zona euro sube a 4,0 % (e) con dispersión grande: Italia 5,6 y España 4,9 frente a Alemania 2,8 y Países Bajos 3,3. En EE. UU. el IPC sube a 3,74 % mientras el subyacente es 2,56 %: el empuje es de energía, no generalizado (coincide con lo recogido en prensa, ahora con cifra primaria).
- Alcista: España +2,7 % i.a. y paro estable; EE. UU. paro 4,1 % y nóminas +165 mil. Bajista: Francia en contracción (−0,1 % i.a.), Italia plana, paro francés en alza; saldo público de EE. UU. proyectado −8,5 % y Polonia −7,2 %.
- Sesgo/limitación: proyecciones FMI y flash Eurostat son estimaciones; vivienda de España +12,1 % es dato oficial pero con riesgo de burbuja solo como [ESPECULACIÓN].

## Sigue pendiente
IPC Japón y Rusia (e-Stat/Rosstat directos); paro y PIB Q3 de China/India/Rusia mensual; Polonia PIB T3 (publicará Eurostat); verificar UK 3,6 vs 3,5 en ons.gov.uk; `leer_indicadores()` y `indicadores-manual.json`.
