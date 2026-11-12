# C138 · Bloques (zona euro, UE, potencias, BRICS) · 12-nov-2026

Fuente de todas las cifras: FMI DataMapper API pública, WEO oct-2026 (GGXWDG_NGDP deuda bruta y GGXCNL_NGDP saldo, % PIB), leída hoy vía WebFetch [P con salvedad: el lector resume la respuesta; cifras coinciden con `explorador/deuda-fmi.json` donde se solapan, lo que las respalda]. Eurostat (IPC, paro, PIB) NO se ha leído en esta sesión: [VERIFICAR]. Proyecciones 2026-2030 = estimaciones del FMI, no hechos.

## Tabla (deuda / saldo, % PIB)
| Bloque / país | Deuda 2024 | 2026e | 2030e | Saldo 2024 | 2026e | 2030e |
|---|---|---|---|---|---|---|
| Zona euro (EURO) | 86,3 | 88,0 | 89,9 | -3,0 | -3,6 | -3,3 |
| UE (EU) | 81,6 | 83,6 | 85,9 | -3,1 | -3,7 | -3,3 |
| EE. UU. | 122,3 | 126,8 | 140,7 | -7,8 | -8,5 | -8,4 |
| China | 90,5 | 104,4 | 119,5 | -7,2 | -8,0 | -8,0 |
| India | 84,8 | 83,1 | 77,0 | -7,9 | -7,5 | -6,8 |
| Brasil | 87,0 | 97,0 | 104,5 | -6,3 | -8,1 | -6,4 |
| Rusia | 14,8 | 19,3 | 29,1 | -1,6 | -3,2 | -3,2 |
| Sudáfrica | 76,0 | 78,0 | 79,7 | -5,7 | -4,4 | -3,5 |
| Arabia Saudí / EAU / Irán | 25,9 / 33,2 / 31,2 | 35,4 / 32,8 / 39,1 | 45,9 / 27,0 / 42,7 | -2,5 / 6,2 / -2,7 | -6,5 / 1,5 / -7,1 | -4,6 / 3,6 / -3,7 |
| Egipto / Etiopía / Indonesia | 90,9 / 33,5 / 40,2 | 84,0 / 40,7 / 41,7 | 75,0 / 29,7 / 41,6 | -7,1 / -2,0 / -2,3 | -11,4 / -2,0 / -2,9 | -3,5 / -1,6 / -2,8 |
| Latam: Argentina / México / Colombia / Chile / Perú | 84,6 / 59,0 / 61,0 / 41,8 / 32,1 | 69,3 / 62,1 / 59,5 / 42,8 / 28,6 | 56,7 / 64,3 / 65,7 / 48,1 / 30,1 | 0,5 / -5,8 / -6,0 / -2,8 / -3,5 | 0,4 / -4,2 / -6,9 / -2,0 / -1,5 | 1,0 / -3,3 / -3,1 / -1,8 / -1,6 |

## Caso alcista vs. bajista (HECHOS FMI; lectura = OPINIÓN)
- **Zona euro/UE.** Alcista: déficit agregado (-3,0 % en 2024) y deuda (86 %) bastante menores que EE. UU. (-7,8 %; 122 %). Bajista: el FMI proyecta deuda al alza hasta 2030 y déficit ~-3,6 %; heterogeneidad: Francia 112,6 → 123,2 % y déficit -5,8 %; Alemania sube de 61,4 a 73,6 % (gasto en defensa/inversión [ESPECULACIÓN] como causa); España 101,4 → 90,7 %, Italia 134,7 → 135,8 % (con saldo -3,4 → -2,5 %).
- **Potencias.** EE. UU.: mayor déficit del G7 (-8,5 % en 2026e) y deuda a 140,7 % en 2030e; ventaja: reserva de valor y tamaño [OPINIÓN]. China: la deuda del FMI sube 90,5 → 119,5 % y déficit ~-8 %, muy por encima de lo que muestran las cifras oficiales nacionales [S: definición de gobierno general del FMI incluye fondos locales; cifras de China discutidas]. Japón: deuda en descenso 213,6 → 190,1 %, pero el saldo empeora (-0,7 → -3,6 %).
- **BRICS.** India: única gran economía del bloque con deuda a la baja (84,8 → 77,0 %), aunque con déficit alto (-7,5 %). Brasil: deuda 87 → 104,5 % y déficit ~-8 %, el más delicado del bloque. Rusia: deuda baja (19 %) pero déficit creciente tras -1,6 % y datos poco fiables/guerra [S]. Sudáfrica: deuda estable ~78 %, déficit en mejora. Nuevos miembros: Egipto con déficit -11,4 % en 2026e; EAU y Etiopía sólidos; Arabia Saudí y Irán con déficit creciente.
- **Latinoamérica.** Argentina pasa de 153,4 % (2023) a 84,6 % (2024) y superávit [P FMI]; México y Colombia, déficit alto (Colombia -6,9 % en 2026e); Chile y Perú, deuda baja.

## Diferencias con `explorador/deuda-fmi.json` (edición oct-2026, leída 21-oct)
- Los 14 países del JSON (USA, JPN, GBR, DEU, FRA, ITA, ESP, CHN, IND, BRA, KOR, SGP, RUS, ZAF) coinciden al 100 % con la API en 2023-2030 (deuda y saldo): sin revisión desde el 21-oct.
- Huecos del JSON: no incluye agregados EURO/EU/BRICS ni Latinoamérica (ARG, MEX, COL, CHL, PER), ni Indonesia, Arabia Saudí, EAU, Irán, Egipto, Etiopía. Esta tabla sirve para ampliarlo (no tocado).
- La API devuelve para Irán, Egipto y Etiopía valores completos; Líbano, Senegal, Ecuador y Venezuela: «—» en 2026-2030 (sin dato).

## Huecos
Eurostat EA20/EU27 (IPC, paro, PIB), Banco Mundial para BRICS y deuda privada/oculta de China: no leídos. Falta total BRICS agregado: el FMI no publica «BRICS».

## Lecciones
1. La API DataMapper responde por WebFetch (no curl: 403); un solo URL con 15 países cabe en una lectura.
2. Todo lo de 2026+ es proyección del FMI: citar siempre «e».
3. Los datos de China y Rusia se mantienen en [S] por definición y opacidad.
4. Coincidencia exacta con el JSON = señal de que no hace falta releer hasta el WEO de abril-2027.
