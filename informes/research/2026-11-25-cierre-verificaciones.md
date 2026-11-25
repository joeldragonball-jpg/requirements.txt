# Cierre de verificaciones (25-nov-2026)

Alcance: 8 de ~40 entradas abiertas de `eventos/verificados.json` (índices 53, 59, 85, 97, 116, 117, 118, 123), leídas con Chrome (extensión) y la API de sumarios del BOE. Historia conservada: lo nuevo se añadió al final de «con» tras «|| 25-nov». Ningún cambio de estado salvo el índice 53. Sin commit/push ni construir_*.

| Entrada | Antes | Después | Fuente leída (25-nov) |
|---|---|---|---|
| 59 CLARITY «31 %» (4-nov) | dudoso | dudoso (más datos) | Polymarket gamma-api + historial CLOB: mercado «signed into law in 2026?» 0,7 % hoy, ~3 % el 4-nov (mín. 2,05 % el 3-nov); no hay 31 % en ese mercado. Kalshi no leída. [S, mercado] |
| 117 Fed sin votación oct-2027 | matizado | matizado | federalreserve.gov/fomccalendars (Last Update 18-nov): 26-27 oct 2027 = «Monetary Policy Strategy Meeting»; la Fed no dice «sin votación» |
| 118 Préstamos XRPL (XLS-66) | matizado (22/35 el 10-nov) | matizado: LendingProtocol 25/35 (71,43 %), V1_1 26/35 (74,29 %), SAV 71,43 % | data.xrpl.org/v1/network/amendments/vote/main (vía xrpl.org known-amendments, que carga estados por script). Ninguna activada; umbral 28/35 dos semanas [P] |
| 123 BOE modelos 172/175/721 y DAC8 | dudoso | dudoso | BOE sumarios 14 a 25-nov (15 y 22 domingo): ninguna disposición; solo contratos de cifra de Defensa e ICEX [P, ausencia] |
| 97 DAC8 | matizado | matizado | Igual que 123 |
| 53 «Fed pausa, gran subida 9-dic» | dudoso | matizado | Polymarket «Fed Decision in December?»: +25 pb 93,5 %, sin cambio 4,45 %, +50 pb 2,25 % [S]. «Gran» sigue siendo del titular. Pausa del 28-oct ya confirmada en federalreserve.gov |
| 85 BCE y Fed subirán en diciembre | matizado | matizado | Polymarket (Fed 93,5 %); BCE no comprobado |
| 116 Hammack 12-nov | matizado | matizado (reforzado) | Cleveland Fed «Speeches»: 12-oct, 5-nov, 17-nov (Brookings); ninguno el 12-nov |

## Intentadas y no cerradas
- CME FedWatch (probabilidad 9-dic): la página carga, pero las probabilidades van en un iframe de QuikStrike que rechaza la carga directa («null referrer»); no se intentó saltarlo. Solo se leyeron los futuros (ZQJ7 95,585). Se usó Polymarket como [S].
- Warsh presidente de la Fed (54, ya «desmentido»), Hungría/Magyar, kremlin.ru 19-nov, cierre de Rail, Kalshi: no abordadas por tiempo; siguen como estaban.
- Otras abiertas sin tocar: 119/124 (radar Baréin, CENTCOM redirige), 121 (Tesoro EE. UU.), 106 (BNY), 108 (BoJ), 115, 122, el bloque de Ormuz.
