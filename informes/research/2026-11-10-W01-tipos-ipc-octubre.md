# W01 · Tipos de interés — previa del IPC de EE. UU. de octubre (10-nov-2026)

Escrito a las ~01:40 (hora local) del 10-nov, ANTES de la publicación (8:30 ET = 14:30 Madrid). Informativo, sin recomendación de compra/venta. [P] = oficial leído; [S] = prensa/agregador; [VERIFICAR]; [ESPECULACIÓN].

## 1. Estado de la publicación
- [P] bls.gov/news.release/cpi.nr0.htm seguía mostrando el comunicado de septiembre (publicado 14-oct) cuando lo leí; bls.gov/schedule/news_release/cpi.htm da el de octubre para el **martes 10-nov, 08:30**, y el de noviembre para el 10-dic.
- **El dato de octubre NO está incluido aquí.** Hay que releer el comunicado oficial tras las 14:30 (Madrid) y rellenar la tabla del punto 4. [VERIFICAR]

## 2. Por qué no habrá tasa interanual (HECHOS, [S] Private Banker 9-nov, investingLive 9-nov)
- Cierre de gobierno de 43 días (1-oct a 12-nov-2025): la BLS no recogió precios de octubre-2025 y nunca publicó ese índice.
- La BLS no publicará variación interanual de octubre-2026 en los índices sin base: general, subyacente, energía, alimentos y alquiler. Sí en gasolina y vehículos nuevos/usados.
- Vivienda: la base de oct/nov-2025 es una estimación (alquileres arrastrados desde abril-2025), lo que distorsiona comparaciones.
- Estimaciones externas (FactSet, mediana, [S]): general ≈4 % interanual (sept 3,7 %), subyacente ≈2,8 % (sept 2,6 %). No son oficiales y dependen de cómo imputa cada casa [VERIFICAR].

## 3. Qué espera el mercado ([S], no oficial)
| Concepto | Previsión | Fuente |
|---|---|---|
| IPC general, mensual | +0,3 % (FXStreet e investingLive hablan de ~+0,2 %) | Private Banker; FXStreet; investingLive, 9-nov |
| Subyacente, mensual | +0,2 % (Private Banker cita +0,3 % para bancos: discrepancia) | ídem |
| Nowcast Fed de Cleveland | general 0,24 %, subyacente 0,21 % | FXStreet 9-nov |
| Gasolina | EIA semanal: ~4,35 → 4,27 $/gal en octubre; explica buena parte de la desaceleración del general (sin desestacionalizar) | FXStreet |
| Vivienda | riesgo de rebote tras la fuerza de sept (OER); alquiler Zillow +0,35 % m/m | FXStreet, investingLive |
| Otros riesgos al alza | fletes, aranceles reinstaurados, billetes de avión, hoteles; PPI sept +1,3 % m/m (+6,3 % a/a) | investingLive, FXStreet |

Previo oficial [P, BLS 14-oct]: septiembre general +0,6 % m/m y +3,7 % a/a; subyacente +0,3 % y +2,6 %; energía +5,2 % m/m y +20,4 % a/a; gasolina +9,1 % m/m; vivienda +0,4 %; alimentos 0,0 %.

## 4. Tabla a rellenar tras la publicación
| | Dato real | Previsión | Sorpresa |
|---|---|---|---|
| General m/m | _pendiente_ | +0,2/0,3 % | |
| Subyacente m/m | _pendiente_ | +0,2 % | |
| Energía / gasolina m/m | _pendiente_ | a la baja | |
| Vivienda m/m | _pendiente_ | | |

## 5. Fed y tipos: contexto
- Fed: 3,75–4,00 % tras +25 pb el 16/17-sep; mantuvo el 28-oct con votación 10–2 (Cook y Hammack querían +25 pb) [P, nota FOMC, ya leída en el W01 del 8-nov]. Próximo FOMC: **8-9 dic** [S, Private Banker; coincide con el calendario del proyecto]; el IPC de noviembre sale el 10-dic, un día después.
- Probabilidad de subida en diciembre: ~65 % en futuros de fondos federales a inicios del 6-nov (antes del informe de empleo) [S]; un titular enlazado habla de «80 %», sin fecha ni cuerpo leído [VERIFICAR]. No he leído CME FedWatch directamente.
- Empleo de octubre (6-nov) [P, ya recogido el 8-nov]: +165.000, paro 4,1 %, salarios +0,4 % m/m.
- Rendimientos: 10 años ≈4,84–4,95 % y 2 años 4,46 % (FRED, semana del 2 al 5-nov) [P, del W01 del 8-nov]; hoy no releídos. 5y5y de inflación 2,17 % (6-nov) [S].
- BoE 4,00 % (+25 pb el 5-nov), BCE 2,50 % (mantenido el 29-oct), Banco de Canadá 2,50 %, RBA 4,85 % (+25 pb el 3-nov): coinciden con `tipos_vivos` (panel de `paneles.json`, datos del 6-9 nov). El panel no pudo leer el BCE hoy (HTTP 504) [P: BCE por calendario, sin releer].
- Países sin lectura automática (Corea, Japón, China LPR, India, HK, Emiratos, Indonesia, Singapur, Rusia, Sudáfrica): **no revisados** en esta pasada; el foco fue el IPC. No he tocado `regulacion.json` ni el calendario. Próximas reuniones ya en radar: SARB 19-nov, Corea 26-nov.

## 6. Escenarios para leer el dato (razonamiento, [ESPECULACIÓN]; no son predicciones de precio)
- **Más restrictivo** (subyacente ≥0,3–0,4 % o vivienda al alza): refuerza a Cook/Hammack y las probabilidades de subida de diciembre; endurece la liquidez (dólar y 2 años altos). Caso bajista para activos de riesgo.
- **Neutral** (general 0,2–0,3 %, subyacente 0,2 %, «en línea»): mantiene el escenario actual; el empleo fuerte del viernes sigue pesando.
- **Más blando** (subyacente ≤0,1–0,2 % con gasolina a la baja): rebaja la urgencia de subir en diciembre; caso alcista para activos de riesgo, pero un solo mes con base distorsionada no cambia la tendencia.
- Sesgo de fuentes: las previas son de agregadores y medios de mercado, con discrepancias entre sí (consenso subyacente 0,2 vs 0,3 %); el consenso no es un dato.

## 7. Qué vigilar
1. Subyacente mensual y vivienda (OER) frente a +0,2 %; si la BLS añade nota sobre la base de octubre-2025.
2. Reacción del 2 años y del precio de la subida de diciembre (CME FedWatch) tras el dato; discurso de miembros del FOMC esta semana.

## Seguridad
- Sin claves ni secretos; solo lecturas web (BLS y prensa). Sin workflows ni API de Anthropic; sin commit ni push; no se editó COLA/PLANNING ni se regeneró seguimiento. No se ejecutó `revisar_explorador.py` porque no se tocó el explorador.
