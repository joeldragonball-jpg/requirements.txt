# XRP Ledger a fondo (2026-10-17, R32 profundo)

> **Corrección (R31, 17-oct):** donde este informe dice 10:34 UTC para la mayoría de `fixCleanup3_4_0`, es **09:34:30 UTC** del 9-oct (ledger 844853670); la posible activación es hacia el 23-oct ~09:34 UTC.
Etiquetas: **LEDGER** = leído por mí hoy en el ledger (nodo público xrplcluster.com, rippled 3.4.1, ledger 107.720.958-107.720.963, 17-oct-2026 ~17:28 hora de España) · **PRIM-LEÍDA** = página oficial (xrpl.org, GitHub XRPLF, ripple.com) leída entera o la parte citada · **TERCERO** = xrpscan, VHS (data.xrpl.org), prensa. Sin recomendaciones de compra/venta.

## Resumen (5 líneas)
1. Hecho: el 9-oct se activaron `fixBatchV1_2` y `BatchV1_1` tras un parche de emergencia (xrpld 3.4.1, 25-sep). xrpl.org informa de dos fallos, uno de ellos "crítico" (desbordamiento de 64 bits que podía **crear XRP**) y dice que no se ha encontrado evidencia de explotación ni pérdida de fondos [parte interesada: lo cuenta el propio ecosistema].
2. Hecho (LEDGER): de 107 amendments conocidos por el nodo, 97 están activos y 10 no. El siguiente en cruzar es `fixCleanup3_4_0`: tiene mayoría desde el 9-oct 10:34 UTC (26 de 32 validaciones; umbral 25). Si la mantiene 14 días, se activaría **~23-oct 10:34 UTC** (cálculo mío, [ESPECULACIÓN] sobre si mantendrá el apoyo: el margen es de 1 voto).
3. Hecho (LEDGER): Ripple mantiene 31.400 M XRP en 98 escrows en 8 cuentas, con liberaciones de 1.000 M cada 1 de mes desde el 1-nov-2026 hasta el 1-may-2029 y 400 M el 1-jun-2029. Ninguno tiene CancelAfter ni condición.
4. Hecho (LEDGER): suministro total 99.985.590.042,39 XRP; quemados por comisiones desde los 100.000 M iniciales: 14.409.957,61 XRP (cálculo mío).
5. Lo grande que sigue sin activarse: Lending Protocol (XLS-66) y Single Asset Vault (XLS-65), 17 y 19 votos de 32 (necesitan 25) tras ~9 meses abiertos a voto. No hay hoja de ruta oficial publicada en xrpl.org (el blog no la lista).

## Qué es hecho verificado
| Dato | Fuente | Fecha | Etiqueta |
|---|---|---|---|
| Nodo en `build_version` 3.4.1, ledger validado 107.720.958, 35 proposers en el último cierre, reserva base 1 XRP, incremento 0,2 XRP, comisión base 0,00001 XRP | xrplcluster.com `server_info` | 17-oct-2026 | LEDGER |
| Suministro total 99985590042391679 gotas (= 99.985.590.042,39 XRP); 100.000.000.000 − eso = 14.409.957,61 XRP quemados | xrplcluster.com `ledger` (total_coins) | 17-oct-2026 | LEDGER + cálculo |
| 107 amendments en `feature`: 97 `enabled:true`, 10 `enabled:false` (todas `supported:true`): ConfidentialTransfer, fixXChainRewardRounding, LendingProtocol, DynamicMPT, SingleAssetVault, CryptoConditionsSuite, fixCleanup3_4_0, LendingProtocolV1_1, Sponsor, XChainBridge | xrplcluster.com `feature` | 17-oct-2026 | LEDGER |
| Recién activados: `fixBatchV1_2` (9-oct 14:15 UTC, ledger 107.540.481), `BatchV1_1` (9-oct 14:47, ledger 107.540.993), `PermissionDelegationV1_1` (8-oct 21:29), `fixCleanup3_3_0` (11-sep), `fixCleanup3_2_0` (29-jul), `fixCleanup3_1_3` (27-may), `PermissionedDEX` (18-feb), `TokenEscrow` (12-feb), `PermissionedDomains` (4-feb) | api.xrpscan.com/api/v1/amendments | 17-oct-2026 | TERCERO (coincide con el `feature` del nodo en qué está activo) |
| Votos de los no activados (apoyo/umbral): fixCleanup3_4_0 26/25 con mayoría desde ledger 844853670 (ripple-time) = 9-oct 10:34:30 UTC; ConfidentialTransfer 19/25; SingleAssetVault 19/25; LendingProtocol 17/25; LendingProtocolV1_1 17/25; DynamicMPT 15/25; Sponsor 9/25; XChainBridge 4/25; fixXChainRewardRounding 11/25; Batch (antiguo) 12/28 y PermissionDelegation 1/28 son restos obsoletos | api.xrpscan.com/api/v1/amendments | 17-oct-2026 | TERCERO (xrpscan agrega los votos de los validadores de confianza; el `feature` del nodo público no los da) |
| Se necesita 80 % de la UNL durante 2 semanas seguidas para activar | xrpl.org (Known Amendments, Amendments) | leído hoy | PRIM-LEÍDA |
| `fixCleanup3_4_0` = colección de arreglos (Vaults, Lending, AMM, DEX con permisos, trust lines, NFT, MPT, Escrow, Sponsorship, delegación); entre ellos "EscrowCancel y EscrowFinish liberan la reserva del propietario antes de recrear la tenencia" | xrpl.org/resources/known-amendments | leído hoy | PRIM-LEÍDA |
| Versiones: 3.1.0 (28-ene: Vaults y Lending), 3.1.1 (23-feb: desactiva Batch por un bug grave), 3.1.2 (12-mar), 3.1.3 (14/8-may), 3.2.0 (15-jun), 3.2.1 (31-jul), 3.3.0 (6-ago), 3.4.0 (16/17-sep), 3.4.1 (emergencia, 25/26-sep; publicada GitHub 10-oct) | xrpl.org/blog y GitHub XRPLF/rippled releases | leído hoy | PRIM-LEÍDA (fechas con ±1 día entre blog y GitHub: ver discrepancias) |
| Informe de vulnerabilidades 3.4.1 (9-oct): (1) Batch con campo envoltorio distinto de `RawTransaction` podía aceptarse (3.3.0 y 3.4.0; BatchV1_1 no estaba activo; sin pérdida de fondos); (2) desbordamiento de suma de 64 bits en el motor de pagos podía pagar a los dueños de ofertas más de lo cobrado al comprador = acuñar XRP; afecta a 3.4.0 y anteriores; "no hay evidencia de explotación en ninguna red pública"; corregido sin amendment, al actualizar; reportado vía bug bounty (Cayden Liao, Veria AI) | xrpl.org/blog/2026/vulnerabilitydisclosurereport-bug-20261009 | 9-oct-2026 | PRIM-LEÍDA |
| >80 % de la UNL por defecto ya ejecutaba 3.4.1 el 25-sep; los servidores antiguos quedaron "amendment blocked" el 9-oct | mismo informe | 9-oct-2026 | PRIM-LEÍDA |
| Otros avisos de seguridad 2026 en el blog: Batch no autorizado (26-feb), manejo de conjuntos de transacciones (23-mar), Manifest Flood (18-ago), XLS-68 Sponsored Fees (21-sep) | xrpl.org/blog (lista; no leí cada informe) | leído hoy | extracto |
| UNL por defecto de Ripple (vl.ripple.com): 35 validadores, secuencia 85, caduca el 4-jun-2027 (ripple-time convertido; mi PC usa formato día/mes) | vl.ripple.com | 17-oct-2026 | LEDGER/VL |
| De los 35 de la UNL, el VHS (data.xrpl.org) asigna dominio a 35: ripple.com, bitso.com, bitrue.com, gatehub.net, xrpl-labs.com, interledger.org, unic.ac.cy, universidades (Berkeley, Kansas, Waterloo, UNC, ANU), blockdaemon, xrpscan, bithomp, etc.; **un solo dominio ripple.com** | data.xrpl.org/v1/network/validators/main | 17-oct-2026 | TERCERO |
| **Escrow de Ripple (LEDGER):** 98 objetos Escrow, 31.400.000.000 XRP, en 8 cuentas (r9UUEX…, rB3WNZ…, rDdXiA…, rKDvgG…, rKwJaG…, rN8pqR…, rNASJd…, rU9qmG…); 0 con CancelAfter; 0 con condición; 8 destinos | account_objects tipo `escrow` en xrplcluster.com | 17-oct-2026 | LEDGER (la atribución a Ripple se apoya en la etiqueta "Ripple" de xrpscan well-known = TERCERO) |
| Calendario de liberación en el ledger: 1.000 M XRP cada 1 de mes (01:00 UTC) de 1-nov-2026 a 1-may-2029; 400 M el 1-jun-2029 (3-4 escrows por mes) | mismo cálculo (FinishAfter) | 17-oct-2026 | LEDGER |
| Ripple declara a 30-jun-2026: 32.600 M XRP en escrow, 37.656.053.914 en su poder, 62.329.587.596 distribuidos | ripple.com/xrp ("Facts about XRP") | 30-jun-2026 | PRIM-LEÍDA, parte interesada |
| Diseño original: 55.000 M XRP bloqueados en dic-2017 en escrows que liberan 1.000 M/mes durante 55 meses; el sobrante se re-bloquea en un escrow nuevo; no figura ninguna dirección en el artículo | ripple.com/insights/explanation-ripples-xrp-escrow (David Schwartz) | 16-dic-2017 | PRIM-LEÍDA |
| `TokenEscrow` permite escrow de tokens de trust line y MPT (requiere flags del emisor; siempre con CancelAfter; el emisor no puede escrowar sus propios tokens) | xrpl.org/docs/concepts/payment-types/escrow | leído hoy | PRIM-LEÍDA |

## Lo que sale de cruzar los datos [cálculo mío, no dato publicado]
- **Salida neta de escrow**: Ripple declaró 32.600 M a 30-jun y el ledger muestra 31.400 M el 17-oct → 1.200 M netos en ~3,5 meses (liberaciones del 1-jul, 1-ago, 1-sep y 1-oct menos lo re-bloqueado), unos ~300 M/mes de media. Es coherente con el rango de 200-300 M/mes que cita la prensa, pero esa prensa es secundaria y solo orientativa [VERIFICAR con una serie por trimestre de los informes de Ripple/Messari].
- **No hay ningún escrow con vencimiento en octubre-2026**: el primero pendiente es el 1-nov; la liberación del 1-oct ya ocurrió (y su re-bloqueo ya está en la lista).
- **El horizonte de liberaciones llega a jun-2029**, más allá de los 55 meses originales (dic-2017 + 55 meses = jul-2022): eso significa que los re-bloqueos han ido empujando el calendario hacia delante [inferencia mía].
- **Una cuenta (rKL9wc…) tiene un escrow de importe 0 en XRP** (probablemente un escrow de token): no lo he identificado.

## Qué está sin verificar o es opinión
- Cuántos validadores de la UNL son independientes de Ripple: el VHS asigna dominios, pero no dice quién los controla; `ripple.com` aparece una vez (cuántas claves de Ripple hay en la UNL: [VERIFICAR] con la lista pública de validadores de Ripple).
- Que `fixCleanup3_4_0` se active el 23-oct: depende de que se mantenga ≥25 votos 14 días; con margen de 1 voto, es frágil [ESPECULACIÓN].
- Cifras de re-bloqueo (60-80 %, ~700 M) y saldo "32 mil millones" de fuentes de prensa (kucoin, mexc, pluang): sin metodología; contradictorias entre sí.
- "Lending (Open for Voting)" en la navegación de xrpl.org: es estado de voto, no activación.
- Interpretaciones de que Lending/Vaults "atraerán capital institucional": [ESPECULACIÓN] (prensa tipo AOL/CoinTurk, sin dato).
- "Proof of Association" (término que usa ripple.com para el consenso de XRPL): la documentación técnica llama al mecanismo "XRP Ledger Consensus Protocol"; es etiqueta de marketing, no un cambio técnico [VERIFICAR terminología].

## Caso alcista / caso bajista (sobre el ledger, no sobre el precio)
**Alcista:** parche de emergencia coordinado en 9 días con >80 % de la UNL actualizada al día 0; bug bounty que funciona (el fallo crítico lo encontró un externo); escrow 100 % legible en el ledger sin cancelación ni condición; nuevas funciones activadas en 2026 (TokenEscrow, PermissionedDomains, PermissionedDEX, Batch, delegación); 97 amendments activos.
**Bajista:** un fallo que podía crear XRP existió en versiones hasta 3.4.0 (la fecha de introducción del fallo no consta: [VERIFICAR] cuánto tiempo estuvo latente); cinco avisos de seguridad en 2026 y Batch tuvo que desactivarse en 3.1.1; Lending/Vaults llevan ~9 meses sin llegar a 25 votos (17 y 19); 10 amendments sin activar, 4 de ellos casi sin apoyo (XChainBridge 4/25); mayor dependencia del equipo de Ripple/RippleX (los dos hallazgos críticos los confirmaron RippleX y la XRPL Foundation); el escrow depende de la decisión de Ripple de re-bloquear cada mes y su calendario llega a 2029: la presión de oferta potencial es reglada pero discrecional.

## Qué cambia para los digital assets (XRP, XLM, stablecoins, tokenización)
- XRP: sin cambio en el modelo de suministro (solo se quema, ~14,4 M XRP acumulados); el calendario de escrow está en el ledger y es auditable por cualquiera, pero Ripple decide el re-bloqueo; no hay dato de precio aquí.
- Stablecoins/tokenización en XRPL: `TokenEscrow` activo desde el 12-feb; MPT en uso; `ConfidentialTransfer` (privacidad para MPT, EC-ElGamal y pruebas ZK) 19/25 y `DynamicMPT` 15/25 siguen pendientes → las funciones de privacidad institucional no son realidad todavía.
- XLM/Stellar: no se tocó en este informe (R33).

## Fechas próximas (catalizadores) con fuente
| Fecha | Evento | Estado |
|---|---|---|
| ~23-oct 10:34 UTC | Posible activación de `fixCleanup3_4_0` (si mantiene ≥25 votos de 32 hasta entonces) | [ESPECULACIÓN]: depende del apoyo; fuente: xrpscan (TERCERO) + xrpl.org |
| 1-nov-2026 01:00 UTC | Primera liberación de escrow pendiente (1.000 M XRP; 2 escrows) | LEDGER |
| 1-dic-2026 y cada día 1 | Siguientes liberaciones de 1.000 M | LEDGER |
| 4-jun-2027 | Caducidad de la lista UNL de Ripple (secuencia 85) | LEDGER/VL |
| sin fecha | Votación de Lending (XLS-66), Vault (XLS-65), ConfidentialTransfer, DynamicMPT, Sponsor | sin calendario oficial |

## Discrepancias detectadas
- xrpld 3.4.1: el blog de xrpl.org la fecha el 25-sep; GitHub dice que se publicó como binarios el 26-sep y como release el 10-oct. Se trata de la misma versión, con distinto momento de publicación.
- 3.1.3 en el blog es 14-may; GitHub 8-may (la fecha del tag de GitHub es previa a la entrada del blog).
- En los resultados de búsqueda de la prensa, el saldo de escrow del 1-sep (31.280 M) y "~32.000 M" tras el re-bloqueo no coincide con 32.600 M de Ripple a 30-jun ni con 31.400 M del ledger: las cifras de prensa deben tomarse como aproximadas.

## Qué falta por buscar
- Quién controla cada validador de la UNL de Ripple (y la lista del XRPL Foundation/otras UNL); ¿cuántos de Ripple?
- Cuándo se introdujo el fallo del desbordamiento (¿versión concreta?) y cuántos validadores seguían en <3.4.1 el 9-oct (VHS tiene server_version por nodo).
- Serie histórica de liberación vs re-bloqueo por mes (data de ledger: leer EscrowFinish del día 1 de cada mes en 2026).
- Contenido de los otros informes de seguridad de 2026 (Manifest Flood, XLS-68).
- Hoja de ruta oficial de XRPL Foundation/RippleX (no aparece en xrpl.org); XLS-82 (MPT-DEX) y XLS-100 (Smart Escrows) figuran "en desarrollo".
- Si Lending se activará: seguir voto en xrpscan o con un nodo propio (`feature`).
