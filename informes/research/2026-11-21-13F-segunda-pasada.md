# 13F de ETF cripto: segunda pasada (fondos públicos, ETF de BTC y flujos XRP/SOL) (21-nov-2026)

Sin recomendaciones. [P] = leído en EDGAR (sec.gov, primary_doc.xml e infotable) o en la web del emisor (parte interesada); [S] = agregador (13f.info); [VERIFICAR] = sin comprobar. Continúa `2026-11-21-13F-ETF-tenedores.md`. Datos en `explorador/etf-13f.json` y `explorador/etf-flujos.json` (campo `segunda_pasada_21nov`).

## 1. HECHOS del 13F (foto a 30-sep-2026) [P]
| Entidad | 13F-HR | Cartera 13F | ETF cripto declarados |
|---|---|---|---|
| State of Michigan Retirement System | 0000762152-26-000017 (27-oct) | 22.595 M USD, 966 pos. | ARKB 300.000 acc. (8,31 M$); GBTC 37.418 acc. (2,42 M$); ETHE 460.000 acc. (9,86 M$). Total 20,6 M$ (~0,09 %). Nada de XRP/SOL/XLM |
| Temasek | 0001021944-26-000015 (28-oct) | 36.701 M USD, 190 pos. | Ninguno por nombre del emisor |
| Wisconsin SWIB | 0001062993-26-006051 (16-nov) | 50.412 M USD, 2.658 pos. | Ninguno (3T ni 2T). Solo Bit Digital, una minera (0,3 M$) |
| Norges Bank | 0001374170-26-000090 (13-nov) | declara 1,011 bill. USD, 1.490 pos. | **Sin dato**: la tabla trae una sola fila ficticia (emisor «NA», valor 0) |
| GIC Private Ltd (CIK 936828) | no localizado | - | Sus 20 últimas presentaciones son 13G/A y Form 4, sin 13F-HR |

- Norges: el 13F-HR/A del 3T-2025 (0001374170-26-000088, presentado el 12-nov-2026) sí tiene la lista real (1.516 pos., 870.105 M USD) y no contiene ETF cripto spot, solo empresas (Coinbase, Circle, Galaxy, Block). Hecho: la lista del 3T-2026 no es pública hoy. [RAZONADO] Parece que Norges publica la lista real con un año de retraso; el motivo exacto no se leyó [VERIFICAR].
- Temasek: la única coincidencia de filtro, «VanEck ETF Trust» (1,18 M acc., 103,7 M$), parece un ETF no cripto por su CUSIP; no comprobado a fondo [VERIFICAR].
- El filtro fue por nombre del emisor (Bitcoin, Ether, XRP, Solana, Stellar, Crypto, Grayscale, Bitwise, Canary, 21Shares, ARK 21...), no por CUSIP: ausencia en el filtro no es ausencia de posición.

## 2. ETF de BTC no revisados antes [S] (13f.info, Q3 2026; totales redondeados por la web)
- **ARKB:** 154 declarantes (2T: 125), ~1,15 mil M$ (2T 608 M$), 41,4 M acc. Jane Street 323,7 M$, Schonfeld 242,4 M$, ARK Investment Management (gestora del propio ETF) 135,6 M$, Galaxy 105,9 M$, Intesa 54,9 M$.
- **BITB:** 315 (277), ~940 M$ (636 M$), 20,7 M acc. ParaFi 77,1 M$, Wells Fargo 72,6 M$, IMC 52,4 M$, Schonfeld 51,9 M$, PNC 44,3 M$.
- **GBTC:** 685 (613), ~1,34 mil M$ (1,26 mil M$); acciones totales bajan de 27,7 M a 20,7 M. Horizon Kinetics 276 M$, Susquehanna 70,6 M$, LPL 53,2 M$.
- **BTC mini (Grayscale):** 516 (473), ~1,88 mil M$ (910 M$), 51,0 M acc. Horizon Kinetics 718 M$, Bullish 167 M$, Wells Fargo 114 M$, Goldman 51,1 M$.
- ETH mini: no revisado (aporta poco).

## 3. Flujos y patrimonio con fecha (webs de emisores, 19/20-nov, viernes 20-nov) [P, parte interesada]
| ETF | Fecha | Acciones | NAV | AUM | Flujo calculado |
|---|---|---|---|---|---|
| Bitwise XRP | 19-nov | 36,44 M | 10,74 | 391,31 M$ | 0 (vs 17-nov) |
| BSOL | 19-nov | 73,36 M | 10,12 | 742,75 M$ | 0 (vs 17-nov) |
| GXRP | 20-nov | 2.660.100 | 17,16 | 45,64 M$ | 0 (vs 18-nov) |
| GSOL | 20-nov | 17.844.135 | 5,10 | 91,04 M$ | -1,02 M$ (2 días) |
| TOXR | 20-nov | no mostradas | 8,67 | 95,33 M$ | no calculable |
| TSOL | 20-nov | 510.000 | 6,64 | 3,39 M$ | 0 (estimado) |
| VSOL | 20-nov | no mostradas | 8,84 | 14,37 M$ | no calculable |
| QSOL | 20-nov | no leídas | - | 2,88 M$ (46.743 SOL) | no calculable |

- Las tenencias de Bitwise XRP (401,19 M XRP el 20-nov frente a 406,77 M el 18-nov, -1,4 %) y de BSOL (10,105 M SOL frente a 10,170 M, -0,6 %) bajan el 20-nov; con las ratios por acción implican ~0,5 M y ~0,5 M acciones menos (cálculo propio, **[VERIFICAR] con la web del lunes**, no mostradas).
- Contraste con agregadores: **no hecho**. Farside (farside.co.uk/xrp) da 404 en esa ruta; SoSoValue muestra la verificación anti-bot de Cloudflare, que no se sortea. Los flujos son solo del propio emisor.
- No legibles: XRPZ, XRPC, FSOL, SOLC, SOEZ.

## 4. LECTURA [RAZONADO] y límites
- Caso alcista: más declarantes en los ETF de BTC leídos (6 de 6 con más filas que el 2T, salvo GBTC en acciones) y entrada de bancos (Wells Fargo, PNC, Goldman). Caso bajista: gran parte son creadores de mercado, hedge funds y la propia gestora (ARK en ARKB); los fondos públicos tienen cantidades pequeñas (Michigan 0,09 % de su cartera, SWIB y Temasek cero por filtro) y los soberanos de Singapur y Noruega no se pueden leer.
- Los flujos de XRP/SOL de los dos últimos días son pequeños (0 a -1 M$) frente a una caída de precio del 8 % en GXRP el 20-nov: no hay señal de salida masiva en el dato del emisor, pero son pocos días y [ESPECULACIÓN] cualquier causa.
- El 13F no recoge posiciones cortas, derivados fuera de tabla ni inversores no EE. UU. (p. ej. gestoras europeas o asiáticas sin obligación 13F), llega con hasta 45 días de retraso y es previo a la caída de oct-nov.

## 5. Pendiente
- Repetir lectura de flujos el lunes 23-nov; GIC y Norges (3T-2026) quedan sin dato útil hasta que haya 13F real; 13F del 4T hacia 16-feb-2027.
