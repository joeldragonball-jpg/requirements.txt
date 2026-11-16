# W09 · Resumen semanal (lunes 16-nov-2026) y plan del 17 al 23-nov

Etiquetas: [P] primaria leída · [S] prensa o agregador · [VERIFICAR] · [ESPECULACIÓN]. Informativo; no es recomendación de compra ni venta. Sin búsquedas nuevas: se apoya en el R00 de apertura y cierre del 16-nov, en W01, W13, W02, W05 y W06 de hoy. Parte de W09 del 13-nov (`2026-11-13-W09-resumen-semanal.md`); no repito lo allí.

## 1. Qué cambió de verdad (13 → 16-nov)
- **Tipos y deuda:** bono de EE. UU. a 10 años en **5,15 %** (13-nov) [P, Tesoro], +29 pb en la semana; subastas largas al 5,020 % (10 a) y 5,441 % (30 a) [P, TreasuryDirect]. Japón 2,899 % (+20 pb), Bund 3,43 % (+14 pb) [P, MoF y Bundesbank]; España +2 pb [P, Banco de España]. Cierre del 16-nov: bono 5,121 % [S].
- **Bolsa:** el 16-nov, S&P 500 −1,9 % (7.416,6), Nasdaq −2,5 %, chips (SOXX) −5,4 %, VIX 23,5 [S, script sobre Yahoo]. Causa **[VERIFICAR]**. El Nasdaq ya había perdido un 5,5 % el 5-nov [P, FRED].
- **Energía y oro:** Brent de 96,4 a 92,4 $ el 16-nov (−4,2 %, causa [VERIFICAR]); oro plano en ~3.850 $ [S].
- **Cripto:** BTC ~65.000 $, ETH ~1.820 $, XRP ~0,95 $, XLM ~0,137 $; miedo y codicia en 10 («miedo extremo») [S]. La cripto no se movió el 16-nov mientras caía la bolsa.
- **Regulación:** hoy vence el plazo del 13F del 3T; no leído aún (C280). Sin novedad en CLARITY.

Lectura alcista: el bono baja 3 pb y el petróleo cae un 4 % el 16-nov; la cripto no vende más. Lectura bajista: bolsa y chips caen con el bono sobre 5,1 % y miedo cripto en 10, sin catalizador visible. Ambas son [ESPECULACIÓN].

## 2. Qué se verificó
- W02: Bund por la API del Bundesbank (D02, [P]); subastas de EE. UU. del 10 y 12-nov [P]; letras de España el 10-nov, no el 17 [P].
- W05H: 7 puntos, 3 cerrados [P], 2 parciales, 2 sin cerrar.
- W06: fixCleanup3_4_0 activada en el ledger [P]; 3 voces nuevas (FMI, Banco de Inglaterra ×2), solo [S].
- W01 y W13 del 16-nov: reuniones de bancos centrales y cobertura sin correcciones (commits `fc28246`, `dc73619`).

## 3. Qué falló o quedó en [VERIFICAR]
- S&P Italia (13-nov), DBRS España (30-oct), Moody's Francia (fecha exacta); resultados oficiales de España (5-nov) y Japón.
- Causa de la caída de bolsa y chips y del Brent del 16-nov.
- Relock del escrow de Ripple del 1-nov: sin leer en el ledger.
- Reino Unido: la API del Banco de Inglaterra dio error 500; queda la lectura del 11-nov.

## 4. Fechas de la semana (17 → 23-nov) y qué lanzar
- 18-nov: IPC de Reino Unido (ONS) y IPCA definitivo de la zona euro (Eurostat) → W01; subasta de 20 años de EE. UU. ($16 mil M) y de Japón → W02. APEC en Shenzhen (18-19-nov) → W03.
- 19-nov: subasta de Obligaciones de España (objetivo 4.750-6.250 M€) y OAT de Francia; reapertura de la nota a 9 años y 8 meses de EE. UU.; decisión del SARB.
- 20-nov: LPR de China (W01) y Japón: subasta de refuerzo de liquidez.
- 23-nov: voto de mainnet del Protocolo 30 de Stellar (sin rutina: valorar `/research EV`).
- Toca lanzar: W01 (miércoles 18), W02 (martes 17), W05 (jueves 19), W06 y W09 (viernes 20), W03 (miércoles 18), W10 (fin de semana).

## 5. Coste real y cuota
- Hoy: W02 <1 % (85 %→85 %), W05H <1 %, W06 y W09 <1 % cada una; el semanal marca 86 % a falta de ~1 h para el reinicio. Las tareas ligeras cuestan mucho menos de lo estimado; las pesadas (C333, ~8 %) son las que mueven el contador.
- Plan: **modo normal** tras el reinicio, sin recortes.

## 6. Lecciones
- La API del Bundesbank exige `Accept: text/csv` (ya anotado en `fuentes-fiables-y-dudosas`). Sin otras lecciones nuevas.
