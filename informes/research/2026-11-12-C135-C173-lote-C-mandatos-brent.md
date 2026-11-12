# C135 · C173 — Mandatos por país y cierre de Brent 23-oct (12-nov-2026)

Método: 2 subagentes con WebSearch/WebFetch; el coordinador aplicó. Todo [S] salvo lo marcado [P].

## Brent 23-oct-2026 (discrepancia cerrada)
- Spot EIA/FRED (Dated Brent, RBRTED): 128,30 $ [P]. Futuro front-month: 116,72 $ (Rio Times + Yahoo BZ=F) [S]; contrato exacto [VERIFICAR].
- Diferencia ≈ 11,6 $: instrumentos distintos (backwardation). 111,97 = máximo del 20-oct, no del 23. Entrada de `eventos/verificados.json` pasada a «matizado».

## Reino Unido
- PM Andy Burnham desde el 20-jul-2026: gov.uk [P] + AP [S]. Sin cambio detectado hasta finales de octubre.

## IPC España octubre
- Adelantado (INE 30-oct): 4,9 %, subyacente 3,1 %, mensual +0,6 % [S]. Definitivo y grupos: 13-nov [VERIFICAR].

## Mandatos (todas [S]; marcadas las de memoria)
| País | Cargo | Inicio | Próxima cita |
|---|---|---|---|
| Indonesia | Prabowo | 20-oct-2024 | 2029 (día [VERIFICAR]) |
| Egipto | Al-Sisi (3.er mandato) | 2-abr-2024 | 2030 (día [VERIFICAR]) |
| India | Modi | 9-jun-2024 [VERIFICAR] | Lok Sabha abr-may 2029 [ESPECULACIÓN] |
| Irán | Pezeshkian (30-jul-2024); Líder Supremo Mojtaba Jameneí (8-mar-2026, tras muerte de Ali Jameneí el 28-feb-2026) | — | Presidenciales 2028 [VERIFICAR] |
| Rusia | Putin (5.º) | 7-may-2024 | Presidenciales mar-2030 [ESPECULACIÓN]; Duma 18-20-sep-2026: Rusia Unida 349/450 |
| Polonia | Nawrocki (6-ago-2025); PM Tusk (13-dic-2023 [VERIFICAR]) | — | Legislativas como tarde nov-2027 |
| Alemania | Merz (6-may-2025) | — | Última federal 23-feb-2025 [VERIFICAR, de memoria]; próxima 2029 [ESPECULACIÓN] |
| Francia | Macron (14-may-2022); PM Lecornu (renombrado 10-oct-2025) | — | Presidenciales abr-2027 [VERIFICAR]; legislativas 30-jun/7-jul-2024 [VERIFICAR] |

Para pasar a [P]: kpu.go.id, eci.gov.in, kremlin.ru, prezydent.pl, bundeswahlleiterin.de, Interior (Francia).

## Lecciones
1. Fechas dadas «de memoria» por un agente quedan [VERIFICAR] y no van a los JSON.
2. Etiquetar siempre spot vs futuro en Brent.
3. La sucesión en Irán (marzo 2026) cambia el marco: situación actual [VERIFICAR].

## ETF, XRP y MSCI (agente 3, [S] salvo lo marcado)
- VWCE TER 0,14 % desde 28-jul-2026 (antes 0,19 %): Vanguard NL [P]; volcado en `fichas-activos.json › etf_mundial`. TradingView sigue con 0,19 % (desfasado).
- IWDA TER 0,20 %: solo agregadores [S]; leer ficha iShares [VERIFICAR].
- XRP escrow: liberación del 1-nov-2026 de 1.000 M XRP; re-bloqueo ~700 M [S, VERIFICAR]; en escrow 31.100–32.600 M (fuentes discrepantes) [VERIFICAR en XRPScan]. No volcado.
- MSCI World estándar: constituyentes y peso EE. UU. sin confirmar (PDF ilegible); dato previo de la ficha (1.249 valores, 30-sep) se mantiene. Variante Screened: EE. UU. 73,51 % (no es el índice estándar).
- Pendiente: extraer el PDF de MSCI con pdftotext o Chrome.
