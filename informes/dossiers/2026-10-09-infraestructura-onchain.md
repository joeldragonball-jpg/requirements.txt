# Dossier: Infraestructura on-chain (enmiendas del XRPL y protocolos de Stellar/Soroban) (9-oct-2026)

> Informativo. No es recomendación de compra ni venta. Fuentes **primarias** leídas: el propio ledger del XRPL (consultas JSON-RPC a un nodo público, rippled 3.4.1, ledger 107541414, 9-oct 15:14 UTC), notas de versión de `XRPLF/rippled` y `stellar/stellar-core` en GitHub, el repositorio `stellar/stellar-protocol` (CAPs) y Horizon (API de Stellar, protocolo y fechas de cambio). Secundarias: CoinDesk (9-oct) y xrpl.org (aviso de seguridad de feb-2026; lista de enmiendas, que no se carga completa). Lo no confirmado va como [VERIFICAR]; las predicciones, como [ESPECULACIÓN]. Los precios no entran aquí: la infraestructura no tiene efecto de precio demostrado.

## 1. Resumen ejecutivo
1. **BatchV1_1 ya está activada en el XRPL** (verificado en el ledger): ledger **107540993**, **9-oct-2026 14:47:52 UTC**. La "fecha del 23-oct" que usaban el calendario y el registro de predicciones **era un error mío de identificación** (ver sección 5).
2. El mismo día se activó **fixBatchV1_2** (ledger **107540481**, 14:15:21 UTC), arreglo asociado. **PermissionDelegationV1_1** estaba activada ya (CoinDesk dice 8-oct; no lo he comprobado en el ledger).
3. Lo que **sí está en cuenta atrás** ahora es **fixCleanup3_4_0** (paquete de arreglos de rippled 3.4.0): ganó mayoría el **9-oct 09:34:30 UTC**. Si la mantiene 2 semanas, se activaría **a partir del 23-oct ~09:35 UTC** [ESPECULACIÓN: depende de que no pierda la mayoría].
4. **Batch tiene historia de seguridad:** la primera versión (amendment `Batch`) tenía un fallo crítico de validación de firmas; rippled 3.1.1 (23-feb) la **desactivó** antes de activarse en mainnet. No se perdieron fondos (según el aviso de xrpl.org).
5. **Otras enmiendas soportadas pero sin mayoría:** LendingProtocol, SingleAssetVault, LendingProtocolV1_1, Sponsor, ConfidentialTransfer, DynamicMPT, entre otras (lista en sección 3).
6. **Stellar ya está en el Protocolo 29** desde el **1-oct-2026 17:00 UTC** (P28: 16-sep; P27: ~8-jul). Soroban recibe cambios cada pocas semanas.
7. **Candidatas al Protocolo 30 (estado "Accepted", versión "TBD"):** CAP-81 (orden de expulsión por TTL), CAP-84 (direcciones multiplexadas de contratos), CAP-87 (verificación de firmas ML-DSA, poscuánticas) y CAP-88 (tiempos de cierre en milisegundos). **No hay fecha de votación publicada.**

## 2. Qué es y por qué importa (sin exagerar)
- **XRPL — enmiendas:** los cambios de protocolo se votan por los validadores de la UNL (35 en la lista actual según CoinDesk). Una enmienda necesita **más del 80 %** de apoyo **durante 2 semanas seguidas** y se activa en el siguiente "ledger de bandera" (cada 256 ledgers, ~15 min). Se vio en esta misma tanda: mayoría 25-sep 14:12 → activación 9-oct 14:15 (fixBatchV1_2).
- **Batch (XLS-56):** permite agrupar varias transacciones en una atómica (todas o ninguna, o con otras reglas). Interés práctico para bancos/instituciones y flujos de pagos complejos. Es infraestructura: no genera por sí misma demanda de XRP.
- **Stellar — protocolo:** los validadores votan una "mejora de protocolo" (CAP) en la fecha acordada; la red entera pasa a la nueva versión en el mismo ledger. Soroban son los contratos inteligentes de Stellar.
- Relación con la cartera: son mejoras de capacidad de la red (comisiones, funciones para instituciones, seguridad). **No hay evidencia en este dossier de que muevan el precio de XRP o XLM.**

## 3. XRPL: estado de las enmiendas (leído del ledger)
| Dato | Valor | Estado |
|---|---|---|
| Versión del nodo consultado | rippled **3.4.1**, 199 pares, 35 proponentes en el último cierre | **Primaria** (server_info) |
| Enmiendas conocidas por el nodo / activadas | **107 / 97** (eran 95 activadas a las 09:00 UTC; +2 hoy) | **Primaria** (`feature`). El recuento depende de las que conoce ese nodo |
| **fixBatchV1_2** | **Activada**, ledger 107540481, 9-oct 14:15:21 UTC | **Primaria** (pseudo-transacción EnableAmendment) |
| **BatchV1_1** | **Activada**, ledger 107540993, 9-oct 14:47:52 UTC | **Primaria** |
| **PermissionDelegationV1_1** | Activada (fecha exacta no verificada; CoinDesk dice 8-oct) | Primaria (estado), fecha [VERIFICAR] |
| **fixCleanup3_4_0** | **Con mayoría** desde 9-oct 09:34:30 UTC (campo Majorities); sin activar | **Primaria** |
| Soportadas, sin mayoría y sin activar | LendingProtocol, SingleAssetVault, LendingProtocolV1_1, Sponsor, ConfidentialTransfer, DynamicMPT, XChainBridge, CryptoConditionsSuite, fixXChainRewardRounding | Primaria (no tienen mayoría ahora). Si se "vetan" en validadores concretos: no visible [VERIFICAR] |
| Batch original (`Batch`, `fixBatchInnerSigs`) | Desconocidas para rippled actual ("Feature unknown") | Primaria |
| MPTokensV2, SmartEscrow | **No existen aún en el nodo**; xrpl.org las lista "en desarrollo" (SmartEscrow tiene redes de prueba "devnet" en etiquetas de GitHub) | Primaria + secundaria [VERIFICAR] |

**Qué incluye fixCleanup3_4_0** (notas de rippled 3.4.0, 17-sep-2026): bloqueo de `asfDisallowIncomingTrustline` en OfferCreate; arreglos de Permissioned DEX; arreglos de `AMMClawback` con MPT; invariantes de MPT que pasan de "solo log" a obligatorias; reglas de NFT y fondos de custodia (Vaults) y préstamos; hash distinto para firmas de contrapartes y "Sponsor"; y **rechazo de pagos `PaymentBurn` que cruzan balance cero**.

**Versiones de rippled/xrpld (GitHub):** 3.1.0 (28-ene: Lending Protocol y Single Asset Vaults), 3.1.1 (23-feb: desactiva Batch), 3.1.2 (12-mar), 3.1.3 (8-may), 3.2.0 (16-jun), 3.2.1 (1-ago), 3.3.0 (6-ago), **3.4.0 (17-sep)**. Existen etiquetas `3.5.0-custom-1/2`: 3.5.0 en preparación, sin fecha ni contenido publicado [VERIFICAR].

## 4. Stellar/Soroban: protocolos (Horizon + stellar-core + CAPs)
| Protocolo | Entra en la red (Horizon) | stellar-core | Contenido (notas oficiales) |
|---|---|---|---|
| **27** | ~8-jul-2026, ledger 63386819 [VERIFICAR; búsqueda binaria con una consulta fallida] | v27.0.0 (5-jun) | **CAP-71:** delegación de autenticación y credenciales de Soroban ligadas a la dirección |
| **28** | **16-sep-2026 17:00:06 UTC**, ledger 64458446 | v28.0.0 (13-ago), 28.0.1 (1-sep) | **CAP-83** (los validadores pueden votar descartar el conjunto de transacciones del ledger en curso), **CAP-85** (ejecutables de contrato gestionados externamente: mejoras atómicas de muchos contratos), **CAP-86** (funciones para mapas con claves Symbol) |
| **29** | **1-oct-2026 17:00:07 UTC**, ledger 64717645 | v29.0.0 (5-oct; la versión interna, 1-oct) | "Mejora de precisión del cruce de ofertas en el DEX" y cambios de mensajería (límites de tamaño) [VERIFICAR el CAP asociado: las notas no lo citan] |
| P26 (anterior) | — | — | CAP-80 (funciones BN254 para pruebas de conocimiento cero) y CAP-82 (enteros de 256 bits con comprobación de desbordamiento), según el estado "Final" de cada CAP |
| Horizon ahora | Protocolo **29**, ledger ~64.854.638, 9-oct 15:16 UTC | | **Primaria** |

**Candidatas al siguiente protocolo (P30)** (repositorio `stellar-protocol`, carpeta `core`, 9-oct):
| CAP | Título | Estado | Qué hace |
|---|---|---|---|
| 81 | TTL-Ordered Eviction | Accepted | La expulsión de entradas de Soroban se ordena por caducidad (TTL) |
| 84 | Muxed Contract Addresses | Accepted | Un contrato puede representar muchos balances "virtuales" off-chain (creado 24-jun) |
| 87 | ML-DSA signature verification | Accepted (9-oct, tras FCP del 30-sep) | Verificación de firmas poscuánticas (FIPS 204) en Soroban |
| 88 | Millisecond-Resolution Close Times | Accepted (30-sep) | Tiempo de cierre con milisegundos; permitiría acortar el ciclo de 5 s a menos (por ejemplo 4,5 s) |
"Protocol version: TBD" en los cuatro. **No he encontrado una fecha de votación de P30** en fuentes primarias. Cadencia observada de este año: P28 → P29 en 15 días; irregular, así que **no se puede inferir** la fecha.

## 5. Corrección importante a mis informes anteriores
- Los informes del 9-oct (intradía) y la entrada `2026-10-23` de `eventos/calendario.toml` / fila 9 de `predicciones.md` decían que **BatchV1_1 tenía mayoría desde el 9-oct 09:34 y podía activarse el 23-oct**. **Es falso.** Lo que tenía mayoría a las 09:34:30 UTC era **fixCleanup3_4_0** (hash `98433DD0…`, comprobado con el campo `majority` del ledger). **BatchV1_1 tenía mayoría desde el 25-sep (14:46 UTC) y se activó hoy.** Cause: yo cité el hash a ojo sin resolver el nombre. [Aprendizaje: resolver siempre el hash a nombre antes de afirmar.]
- **Discrepancia con CoinDesk:** el artículo (9-oct 12:21 EDT) dice que "el arreglo de PaymentBurn tenía 27 de 35 votos y necesitaba 29 para empezar la cuenta atrás". Pero el ledger ya mostraba mayoría de fixCleanup3_4_0 (que incluye ese arreglo según las notas de 3.4.0) desde las 09:34 UTC. Posibles causas: CoinDesk usó un panel desfasado o cuenta otro umbral [VERIFICAR]. **El dato del ledger prevalece.**

## 6. Cómo leerlo: caso alcista vs. bajista (sin consejos)
| Caso | Argumentos |
|---|---|
| **A favor** | Batch (atomicidad) y delegación de permisos son funciones que piden bancos y emisores; hay ritmo alto de versiones (8 en 8 meses); la vulnerabilidad de Batch se detectó antes de activarse; Stellar entrega 3 protocolos en ~3 meses con hojas de ruta públicas (CAPs) |
| **En contra / riesgo** | Un fallo crítico en una función nueva (Batch) llegó hasta la fase de votación: más funciones = más superficie de ataque; la propia nota de CoinDesk avisa de un riesgo con `PaymentBurn` hasta que active el arreglo; Lending/Vaults/Sponsor siguen sin mayoría tras meses (adopción lenta); las mejoras técnicas no garantizan uso real ni precio |
| **Sesgos de las fuentes** | CoinDesk resume paneles que pueden ir desfasados; las notas de versión son del equipo y no miden adopción; "nodo público" = un solo punto de vista (aunque el ledger validado es el mismo para todos) |

## 7. Calendario y eventos
| Fecha | Evento | Estado |
|---|---|---|
| **9-oct** | BatchV1_1 + fixBatchV1_2 activadas en el XRPL | **Hecho** (ledger) |
| **~23-oct 09:35 UTC o después** | Posible activación de **fixCleanup3_4_0** (incluye arreglo de `PaymentBurn`) | Aproximada [ESPECULACIÓN]: solo si conserva >80 % de votos 14 días |
| 27–29-oct | Swell 2026 (Ripple, Nueva York): posibles anuncios de XRPL | Ya en el calendario |
| Sin fecha | Votación del Protocolo 30 de Stellar | No publicada |
| Sin fecha | rippled 3.5.0; MPTokensV2; SmartEscrow | En desarrollo |

### Eventos que propongo para `eventos/calendario.toml` (NO añadidos; tú decides)
1. **Corrección** de la entrada existente de `2026-10-23` (líneas 126–132): título "XRPL: posible activación de fixCleanup3_4_0" y detalle "Ganó mayoría el 9-oct (09:34 UTC). Si la mantiene (>80 %) 14 días, se activaría a partir de esta fecha (cálculo del research). Incluye arreglos de Permissioned DEX, MPT, vaults y PaymentBurn. BatchV1_1 ya se activó el 9-oct." Mantener `aproximado = true`, `impacto = "bajo"`, fuente: `https://github.com/XRPLF/rippled/releases/tag/3.4.0`.
2. Nueva (informativa, hecho pasado, opcional): `2026-10-09` "XRPL: BatchV1_1 activada" con fuente el propio ledger. Probablemente innecesaria en un calendario futuro.
3. **No propongo** entrada para el P30 de Stellar: sin fecha publicada. Se añadirá cuando exista.

## 8. Escenarios [ESPECULACIÓN]
| Escenario | Qué pasaría | Señales |
|---|---|---|
| **A. Sin incidentes** | fixCleanup3_4_0 se activa ~23-oct; P30 en el cuarto trimestre | Mayoría estable; votación anunciada en el foro de Stellar |
| **B. Pierde la mayoría** | El contador vuelve a cero (ya ocurrió con PermissionDelegation en septiembre, según CoinDesk) | Campo Majorities vacío en un ledger de bandera |
| **C. Bug en función nueva** | Aviso de seguridad y versión de emergencia (precedente: rippled 3.1.1) | Avisos en xrpl.org / GitHub |

## 9. Qué vigilar
Campo `Majorities` del ledger (comando `ledger_entry` del objeto Amendments) hasta el 23-oct; publicación de rippled 3.5.0; anuncios en Swell (27–29-oct); la próxima votación de Stellar (P30) y el estado de CAP-87/88.

## 10. Lo que no sé
- Fecha exacta de activación de PermissionDelegationV1_1 en el ledger.
- Cuántos validadores apoyan cada enmienda hoy (CoinDesk dice 27/35 para el arreglo de PaymentBurn; el ledger lo contradice).
- Qué CAP concreto incluye el Protocolo 29 (las notas no lo nombran).
- Fecha del Protocolo 30; si CAP-81/84/87/88 entrarán todos juntos.
- La fecha exacta del P27 (consulta con un fallo intermedio en mi búsqueda).
- Estado real de MPTokensV2 y SmartEscrow (solo xrpl.org y etiquetas de GitHub).
- Impacto en precio o en uso: no medido.
