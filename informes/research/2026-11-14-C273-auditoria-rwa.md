# C273 · Auditoría de tipos_activo contra RWA.xyz (14-nov-2026)

Método: lectura en Chrome de app.rwa.xyz/networks/<red>, pestaña Asset Classes (as of 11/14/2026), de las 9 redes; muestra aleatoria (semilla 273) de 40 de las 49 celdas de `tipos_activo.tipos.*`. Para cada celda se sumaron las clases del paréntesis. Tolerancia ±3 %. Fuente [S] (tercero comercial). Las cifras en «mil M$» de RWA.xyz vienen redondeadas a 0,1 mil M$.

**Resultado: 0 celdas erróneas en las 40 (v y k coinciden; también las 9 no muestreadas coinciden al comparar). No se corrigió ninguna. Ninguna fila «Login to Unlock» entró en celdas (solo se cita en las notas). Las clases agrupadas corresponden a lo que dice el paréntesis en las 49.**

Observación: la tabla solo lista el top 10 de clases; las que no aparecen siguen siendo «sin dato» (no cero).

| Celda | Valor en cadenas.json (M$; nº) | Leído en RWA.xyz | Veredicto |
|---|---|---|---|
| hedera/fondos | 8.3; 2 | 8,3; 2 | OK |
| polygon/materias | 1.4; 3 | 1,4; 3 | OK |
| polygon/otros | 65.2; 10 | 65,2; 10 | OK |
| polygon/deuda | 191.2; 26 | 158,4+32,8 = 191,2; 11+15 = 26 | OK |
| hedera/acciones | 0.0001; 36 | 120 $; 36 | OK |
| ethereum/credito | 3249.2; 102 | 1,8 mil M$+556,8+520,3+372,1 ≈ 3.249,2; 19+6+31+46 = 102 | OK |
| polygon/fondos | 101.4; 7 | 101,4; 7 | OK |
| plume/fondos | 12.1; 5 | 12,1; 5 | OK |
| ethereum/fondos | 1800; 36 | 1,8 mil M$; 36 | OK |
| stellar/acciones | 27.3; 6 | 27,3; 6 | OK |
| hedera/credito | 0.0027; 3 | 2.687 $; 3 | OK |
| stellar/deuda | 2246.7; 23 | 2,0 mil M$ (redondeado)+246,7 ≈ 2.246,7; 17+6 = 23 | OK |
| avalanche/deuda | 378.0; 32 | 372,9+5,1 = 378,0; 28+4 = 32 | OK |
| plume/acciones | 0.0006; 735 | 565 $ (564,9); 735 | OK |
| avalanche/credito | 690.6; 40 | 361,1+270,2+40,4+18,9 = 690,6; 4+16+13+7 = 40 | OK |
| xrpl/inmuebles | 5.7; 10 | 5,7; 10 | OK |
| bnb/materias | 85.2; 39 | 85,2; 39 | OK |
| solana/materias | 43.8; 28 | 43,8; 28 | OK |
| solana/fondos | 34.2; 12 | 34,2; 12 | OK |
| solana/otros | 1100; 6 | 1,1 mil M$; 6 | OK |
| bnb/deuda | 4300; 37 | 4,3 mil M$; 37 | OK |
| solana/acciones | 572.9; 1971 | 572,9; 1971 | OK |
| bnb/credito | 39.0; 47 | 28,8+5,5+4,7 = 39,0; 3+32+12 = 47 | OK |
| stellar/otros | 26.9; 12 | 26,9; 12 | OK |
| avalanche/acciones | 216.2; 744 | 216,2; 744 | OK |
| solana/credito | 1453.0; 54 | 781,5+355,7+275,6+40,2 = 1.453,0; 10+4+27+13 = 54 | OK |
| hedera/otros | 18.7; 1 | 18,7; 1 | OK |
| hedera/deuda | 61.3; 10 | 56,4+4,9 = 61,3; 8+2 = 10 | OK |
| stellar/credito | 551.9; 10 | 516,8+30,6+4,5 = 551,9; 4+5+1 = 10 | OK |
| polygon/acciones | 0.56; 53 | 0,557; 53 | OK |
| polygon/credito | 8.31; 7 | 7,4+0,911 = 8,31; 6+1 = 7 | OK |
| plume/deuda | 6.5; 16 | 6,5; 16 | OK |
| ethereum/materias | 4800; 54 | 4,8 mil M$; 54 | OK |
| avalanche/otros | 9.2; 3 | 9,2; 3 | OK |
| ethereum/deuda | 4459.8; 87 | 4,3 mil M$+159,8 ≈ 4.459,8; 72+15 = 87 | OK |
| xrpl/otros | 58.7; 2 | 58,7; 2 | OK |
| ethereum/acciones | 742.6; 2876 | 742,6; 2876 | OK |
| plume/credito | 114.1; 29 | 76,7+21,8+15,6 = 114,1; 5+11+13 = 29 | OK |
| solana/deuda | 1900; 43 | 1,9 mil M$; 43 | OK |
| bnb/acciones | 1700; 2912 | 1,7 mil M$; 2912 | OK |

Cambios adicionales pedidos: `"cal": true` añadido a cadenas/4/hitos/3 (Solana, DTCC 2S-2027) y cadenas/13/hitos/2 (Quant, Clearing House 1S-2027), verificados por índice y texto.
