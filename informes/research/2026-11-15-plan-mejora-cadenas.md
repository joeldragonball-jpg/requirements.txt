# Plan de mejora de la pestaña «Cadenas» de la Órbita (15-nov-2026, solo lectura)

Alcance: `explorador/cadenas.json` (C264, 14-nov), `cadenas-onchain.json` (14-nov 22:19Z), `rwa-por-cadena-manual.json`, `etf-flujos.json`, `vistas.html` (`pCadenas`, `ocBloque`, CSS `.cad-*`) y los informes `2026-11-14-auditoria-orbita-cadenas.md`, `*-expansion-opus.md`, `C264`-`C278`. Nada editado salvo este archivo. Es un tablero de inteligencia general: información, no recomendación. Niveles: [P] primaria leída · [S] secundaria/agregador · [VERIFICAR] · [ESPECULACIÓN]. «Probado hoy» = petición HTTP hecha el 15-nov-2026 desde este equipo.

## 0. Estado actual (HECHOS)

- 16 redes × 8 capacidades (liquidez, seguridad, activos, cumplimiento, pagos, rendimiento, interop, regulación) = 128 celdas; 2 vacías (XDC·regulación, Quant·liquidez). Más 5 capas «¿necesita el token?», captura [RAZONADO], ISO 20022, hitos, sesgos, sin_dato, tipos de activo (RWA.xyz) y 5 relaciones.
- Solo 6 hitos marcados como futuros en 16 redes; 10 redes sin ningún hito futuro (Hedera, BNB, Avalanche, Polygon, Canton, Ondo, Algorand, XDC, IOTA, Plume).
- Captura «incierta» en 8 de 16 (XRPL, BNB, Avalanche, Algorand, XDC, Quant, IOTA, Plume).
- Celdas antiguas en la matriz: BNB·seguridad (2024-09-25), Quant·interop (2021-06), XRPL·interop (2025-06-30), Canton·regulación (2025-12-11), Algorand·regulación (2025-04-03), XDC·cumplimiento [V] (2025-10-23), Plume·liquidez [V] (2026-08). Regulación por red es casi toda de 2026-10-09 (dossier) y [S] en 6 redes.
- Lo automático hoy (`scripts/leer_onchain.py`) solo da TVL y stablecoins de DefiLlama para 13 redes + métricas nativas de XRPL y Stellar. Hedera, Ethereum, Solana, Avalanche, Algorand, XDC e IOTA tienen `nativo: null`.
- Plume sale con TVL 0 en DefiLlama y IOTA/Canton/Plume con stablecoins null: probablemente nombre de cadena mal emparejado (p. ej. «Plume Mainnet», «IOTA EVM») [VERIFICAR].

## 1. Información floja por red y dimensiones nuevas

### 1.1 Huecos por red (lo más visible primero)

| Red | Floja o falta | Nota |
|---|---|---|
| XRPL | Volumen ODL en XRP (no publicado); interop con dato de 2025; nº de enmiendas pendientes y votación | Enmiendas: legible por script (§2) |
| Stellar | Validadores/tier-1 (sin cifra); volumen de pagos vs DEX | Stellarbeat API no responde en las rutas probadas [VERIFICAR] |
| Hedera | Sin métricas nativas aunque hay mirror node público; noticias por ficha (C271) | Consejo: 25 nodos en el mirror node (probado hoy) |
| Ethereum | Validadores y concentración (Lido, CEX); L2 mezcladas con L1 | Beaconcha.in pide clave (401); L2BEAT redirige a otro dominio [VERIFICAR] |
| Solana | Nakamoto/concentración de stake; caídas históricas | RPC público: 661 validadores, 39 «delinquent», 18 validadores superan 1/3 del stake (probado hoy, [P] del propio nodo, foto puntual) |
| BNB | Seguridad con dato de 2024; nº de validadores sin cifra primaria | Hacks: 268 incidentes en DefiLlama (atribución multi-cadena) |
| Avalanche | Hitos futuros 0; validadores | P-Chain pública: 605 validadores (probado hoy) |
| Polygon | Separar PoS de Agglayer/zkEVM | |
| Canton | Sin TVL/stablecoins comparables; regulación 2025 | Red permisionada: no automatizable por API abierta [ESPECULACIÓN razonable] |
| Chainlink / Quant / Ondo | No son cadenas: la matriz les fuerza filas que no aplican (Quant·liquidez vacía) | Ver §3: separarlas visualmente |
| Algorand | Regulación de 2025; captura incierta | algonode público responde (probado hoy) |
| XDC | Regulación vacía; cumplimiento [V] | RPC: 108 masternodes (probado hoy) |
| IOTA | Sin ISO, sin stablecoins | RPC: 60 validadores activos, época 559 (probado hoy) |
| Plume | Liquidez [V]; TVL 0 en DefiLlama | Revisar emparejamiento de nombre |

### 1.2 Dimensiones nuevas, por valor (OPINIÓN razonada)

1. **Descentralización/validadores** (nº, concentración, quién decide la lista: UNL, Consejo, stake). Alto valor y en buena parte automatizable.
2. **Uso real con comisiones** (fees 24h/30d, volumen DEX, tx por ledger). Distingue «valor aparcado» (TVL) de «uso».
3. **Incidentes de seguridad** (hacks por red, caídas, enmiendas de emergencia). Ya hay relación «mejoras e incidentes»; falta serie.
4. **Stablecoins por red desglosadas por emisor** (RLUSD, USDC, USDT…): ya hay total, falta composición y tendencia 30 d.
5. **Gobernanza y mejoras pendientes** (enmiendas XRPL, CAP de Stellar, HIP de Hedera, EIP; propuestas Snapshot donde aplique).
6. **Calendario de hitos** (releases y activaciones): enlazar con la pestaña Calendario.
7. **Actividad de desarrolladores** (releases/commits en repos núcleo). Valor medio; métrica fácil de manipular.
8. **Regulación por jurisdicción aplicada a la red** (MiCA: ¿qué CASP/EMT operan sobre ella?) usando `leer_esma_mica.py` ya existente.
9. **Interoperabilidad** (CCIP/CCTP/Axelar/Wormhole por red): ya parcialmente hecho el 15-nov; falta convertirlo en tabla.
10. **Cuota de RWA** ya existe (RWA.xyz, [S], manual); añadir solo serie mensual.

## 2. Qué se puede automatizar sin clave (probado hoy, 15-nov-2026)

| Dimensión | Endpoint | Resultado | Redes |
|---|---|---|---|
| Comisiones | `https://api.llama.fi/overview/fees/{Chain}?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true` | 200; Hedera total24h ≈ 3.522 $, 30d ≈ 142.742 $ [S] | todas las que DefiLlama empareje |
| Volumen DEX | `https://api.llama.fi/overview/dexs/{Chain}?…` | 200; Stellar 24h ≈ 3,0 M$, 30d ≈ 44,3 M$ [S] | ídem |
| Hacks | `https://api.llama.fi/hacks` | 200; 1.355 incidentes, campos `chain`, `amount`, `bridgeHack`, `returnedFunds`; último ≈ 14-nov-2026 [S] | todas; ojo nombres «XRPL» y «Ripple» duplicados, «BSC» y «Binance» |
| Stablecoins por emisor | `https://stablecoins.llama.fi/stablecoins?includePrices=false` (`chainCirculating`) | 200; XRPL: RLUSD 762,8 M$, USDV 72,8 M$; Stellar: USDC 345,8 M$; XDC: USDC 52,8 / USDf 49,8 M$ [S] | todas |
| Puentes | `https://bridges.llama.fi/bridges` | **402 (de pago)**: no usar | — |
| UNL XRPL | `https://vl.ripple.com` (blob base64) | 200; 35 validadores, secuencia 86 [P, parte interesada] | XRPL |
| Enmiendas XRPL | POST `{"method":"feature"}` a `https://s1.ripple.com:51234/` | 200; 115 conocidas, 96 activadas; pendientes incluyen LendingProtocol, ConfidentialTransfer [P] | XRPL |
| Nodos Hedera | `https://mainnet-public.mirrornode.hedera.com/api/v1/network/nodes?limit=50` y `/network/fees` | 200; 25 nodos con descripción («Hosted by …») y stake [P] | Hedera |
| Validadores Solana | POST `getVoteAccounts` a `https://api.mainnet-beta.solana.com` | 200; 661 / 39 / coef. 1/3 = 18 [P, nodo público, limitado por tasa] | Solana |
| Validadores Avalanche | POST `platform.getCurrentValidators` a `https://api.avax.network/ext/bc/P` | 200; 605 [P] | Avalanche |
| Validadores IOTA | POST `iotax_getLatestIotaSystemState` a `https://api.mainnet.iota.cafe` | 200; 60 activos [P] | IOTA |
| Masternodes XDC | POST `XDPoS_getMasternodesByNumber` a `https://rpc.xinfin.network` | 200; 108 [P] | XDC |
| Estado Algorand | `https://mainnet-api.algonode.cloud/v2/status` | 200 (nodo de tercero, Nodely) [S] | Algorand |
| Gas Ethereum | Etherscan v2 gasoracle sin clave | 200 pero «Missing/Invalid API Key, rate limit 1/5sec»: tolerado, frágil | Ethereum |
| Releases | `https://github.com/{org}/{repo}/releases.atom` | 200 (rippled, stellar-core). La API REST de GitHub dio 403 por límite de 60/h por IP | todas con repo público |
| Gobernanza off-chain | `https://hub.snapshot.org/graphql` | 200 | solo DAOs que usen Snapshot |
| No sirven | beaconcha.in (401), CoinGecko `developer_data` (null), api.stellarbeat.io v1/v2 (404), L2BEAT (301 a otro dominio) | [VERIFICAR] alternativas: radar de Stellar, endpoint nuevo de L2BEAT | — |

Trampa vista hoy: el feed de releases de rippled muestra etiquetas «3.5.0-custom-7», que no parecen versiones oficiales [VERIFICAR]; hay que filtrar por releases marcadas y no por etiquetas.

## 3. Presentación y usabilidad

HECHOS del código: la matriz tiene `min-width:1080px` (1.150 px bajo 700 px de ancho), celdas cortadas a 75 caracteres y el texto completo solo en `title` (hover); el aviso dice «Pasa el ratón», que no existe en tablet/móvil. La ficha sí trae el texto entero, pero hay que bajar.

Propuestas (OPINIÓN):
1. **Toque = abrir panel** con la celda completa y su fuente (como el arreglo de la Matriz país × tema de a9953e2); quitar dependencia de `title`.
2. **Móvil (<700 px)**: no la matriz de 1.150 px; lista por red con 8 chips de color (P/S/V/sin dato) que despliegan la celda. «Ver solo el semáforo» como vista por defecto en táctil.
3. **Separar en dos grupos**: «Cadenas» (13) y «Capas/servicios» (Chainlink, Quant, Ondo) con capacidades que sí les aplican; evita filas vacías «sin dato» que parecen debilidad.
4. **Frescura visible por celda**: atenuar celdas con fecha > 90 días y un contador «celdas antiguas» en los KPI.
5. **Columna «uso y seguridad» automática** (fees 30 d, validadores, hacks 12 m) con fecha y nivel [S]/[P], separada de la matriz manual.
6. Filtro por dimensión y buscador de red; ancla directa `#cad-<id>` compartible.
7. Unificar formatos (miles, M$) y el esquema de fechas (`d` vs `fecha`, meses sueltos), ya señalado en la auditoría del 14-nov.

## 4. Riesgos de sesgo y calidad del dato

- **Partes interesadas como [P]**: casi todas las primarias de una red son de su fundación o empresa (Ripple, SDF, Hedera, Polygon…). [P] dice «leído en origen», no «neutral». Sugerencia: marca «parte interesada» visible en la celda.
- **Agregadores con metodologías distintas**: stablecoins en XRPL 839 M$ (DefiLlama, 14-nov 22:19Z) frente a 807,5 M$ (RWA.xyz, 14-nov); hora e inclusión de emisores difieren. Mostrar siempre la fuente junto a la cifra y no mezclar en una misma suma.
- **Emparejamiento de nombres**: Plume TVL 0, IOTA/Canton sin stablecoins; en hacks «XRPL» y «Ripple», «BSC» y «Binance» van separados. Mapear nombres por red en un único diccionario.
- **Hacks atribuidos a varias cadenas**: un puente hackeado suma a todas sus cadenas (Avalanche ≈ 6.816 M$ acumulados en DefiLlama sugiere atribuciones de puentes [VERIFICAR]). No presentar como «inseguridad de la red» sin separar `bridgeHack` y protocolo vs. capa base.
- **Más datos = más visible**: Ethereum/Solana tienen más fuentes y parecerán «mejores»; redes permisionadas (Canton) parecerán vacías. Evitar rankings y colorear por nivel de evidencia, no por tamaño.
- **Métricas manipulables**: TVL, nº de tx (spam en XRPL/Solana), commits. Dar siempre contexto (comisiones pagadas pesan más que tx).
- **Nº de validadores ≠ descentralización**: Hedera 25 nodos con Consejo; XRPL UNL 35 publicada por una entidad; usar concentración (coef. 1/3) donde se pueda y explicar el modelo.
- **Fotos puntuales**: nodos públicos dan el instante; sin serie no hay tendencia. Guardar histórico diario como en `etf-flujos.json`.
- **Sesgo de la tesis**: la captura del token es la columna más proclive a lecturas de inversión; mantener [RAZONADO] y no añadir «ganador».

## 5. Plan de tareas (provisional K01-K12; asignar C292+ al pasarlas a `research/tareas.csv`)

Orden por valor/esfuerzo. Regla: un solo escritor a la vez en `cadenas.json` y `vistas.html`.

| # | Tarea (prompt corto) | Modelo | Tam. | Depende | Archivos que toca |
|---|---|---|---|---|---|
| K01 | Corregir emparejamiento DefiLlama (Plume, IOTA, Canton) y crear diccionario único de nombres por red | Sonnet | S | — | `scripts/leer_onchain.py`, `explorador/cadenas-onchain.json` |
| K02 | Ampliar `leer_onchain.py` con fees y volumen DEX 24h/30d por red (DefiLlama overview) | Sonnet | S | K01 | `scripts/leer_onchain.py`, `explorador/cadenas-onchain.json` |
| K03 | Stablecoins por emisor y red (top 5, `chainCirculating`) con aviso de diferencia frente a RWA.xyz | Sonnet | S | K01 | `scripts/leer_onchain.py`, `cadenas-onchain.json` |
| K04 | Nuevo lector de validadores: UNL XRPL, nodos Hedera, Solana (coef. 1/3), Avalanche, IOTA, XDC, Algorand; histórico diario | Sonnet | M | — | `scripts/leer_validadores.py` (nuevo), `explorador/cadenas-validadores.json` (nuevo) |
| K05 | Lector de incidentes desde `api.llama.fi/hacks`: últimos 12 m por red, separando puentes y capa base | Sonnet | S | K01 (diccionario) | `scripts/leer_incidentes.py` (nuevo), `explorador/cadenas-incidentes.json` (nuevo) |
| K06 | Gobernanza y releases: enmiendas XRPL (`feature`), releases.atom de repos núcleo (filtrando etiquetas no oficiales) | Sonnet | M | — | `scripts/leer_gobernanza.py` (nuevo), `explorador/cadenas-gobernanza.json` (nuevo) |
| K07 | Vista: tocar celda = panel con texto y fuente; quitar «pasa el ratón»; semáforo por defecto en táctil | Sonnet | M | — | `explorador/vistas.html` (solo `pCadenas` y CSS `.cad-*`) |
| K08 | Vista móvil (<700 px): lista por red con chips en vez de tabla de 1.150 px | Sonnet | M | K07 | `explorador/vistas.html` |
| K09 | Mostrar bloque automático «uso y seguridad» en cada ficha (`ocBloque` ampliado) con nivel y fecha | Sonnet | M | K02-K06 | `explorador/vistas.html`, `explorador.py` o donde se cargue `D.cadenas_onchain` (Grep antes) |
| K10 | Separar «capas/servicios» (Chainlink, Quant, Ondo) de las cadenas y atenuar celdas > 90 días con contador en KPI | Sonnet | S | K07 | `explorador/vistas.html` |
| K11 | Refrescar celdas antiguas (BNB seguridad 2024, Quant interop 2021, XRPL interop 2025, regulación de Canton/Algorand/XDC) con primaria en Chrome | Opus | M | — | `explorador/cadenas.json` |
| K12 | Hitos futuros para las 10 redes sin ninguno (roadmaps oficiales, activaciones), con [ESPECULACIÓN] si es estimación; cruzar con Calendario | Sonnet | M | K11 (mismo archivo, en serie) | `explorador/cadenas.json` |

Paralelo seguro: K01→K02/K03 (mismo script, en serie) ‖ K04 ‖ K05 ‖ K06 ‖ K11→K12. Después K07→K08→K10 (vistas.html, en serie) y al final K09. Tras cada una: `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`. Ninguna llama a la API de Anthropic; todas sin clave. NO commit ni push sin «sube».

## 6. Limitaciones

- GitHub API REST agotada para esta IP (403, 60/h): la actividad de desarrolladores solo se probó por feeds Atom.
- No se probó en Chrome (no fue necesario); Stellarbeat, L2BEAT y validadores de Ethereum quedan [VERIFICAR].
- Las cifras probadas son fotos del 15-nov-2026 por la mañana y no se han escrito en ningún JSON.
