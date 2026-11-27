# C364 - Hoja de ruta del servicio de tokenización de DTCC (DTS)

Fecha de consulta: 2026-11-27. Solo hechos con fuente; sin recomendaciones. Leyenda: sin marca = fuente primaria leída (dtcc.com); [S] = prensa o secundaria; [VERIFICAR] = no contrastado.

## Resumen
- El 28-oct-2026 DTC (filial de DTCC) lanzó el DTCC Tokenization Service (DTS). Redes en producción: Canton Network y la red privada Besu de DTCC. "Redes adicionales" en 2027, sin nombrarlas en el comunicado del lanzamiento.
- Redes anunciadas aparte: Stellar (1.er semestre 2027), Solana (2.º semestre 2027). Circle Arc: solo prensa [S].
- XRPL: ninguna fuente primaria de DTCC lo menciona (ver sección propia).

## 1. Redes
| Red | Estado | Fuente |
|---|---|---|
| Canton Network (pública, Digital Asset) | Viva desde el piloto del 15-jul-2026 y en el lanzamiento | DTCC 15-jul y 28-oct-2026 |
| Besu (LFDT; red privada de DTCC) | Viva igual | DTCC 15-jul y 28-oct-2026 |
| Stellar (pública) | Previsto 1.er semestre 2027 ("1H27"); anunciado el 27-may-2026 con la Stellar Development Foundation | dtcc.com/press-releases/2026/tokenization-service-to-connect-with-stellar-public-blockchain-as-dtc-advances-multi-chain-strategy |
| Solana (L1) | Previsto 2.º semestre 2027; comunicado del 12-nov-2026; "esperado/planificado", no garantizado | dtcc.com/press-releases/2026/dtcc-tokenization-service-to-connect-with-solana |
| Circle Arc | "En 2027"; prensa lo sitúa en 2.º semestre [S]. No hallé comunicado propio de DTCC o Circle sobre el servicio en Arc. DTCC es validador fundador de Arc [S] | marketsmedia, Ledger Insights [S] [VERIFICAR] |

- Sobre Arc, [S]: la integración permitiría liquidación con stablecoin fuera de DTC contra activos tokenizados de DTC; requeriría aprobación previa de la cadena según la carta de no-acción [VERIFICAR].
- Blockchain de Canton, Besu, Arbitrum, Avalanche: NO he encontrado entradas de blog propias ni anuncios de DTCC que sitúen a Arbitrum o Avalanche en la hoja de ruta. Los blogs de Canton/Stellar/Solana no se leyeron más allá de los comunicados de DTCC y la página de Solana Foundation citada por la prensa (solana.com/news/dtcc-tokenization-service-to-connect-with-solana, no abierta directamente) [VERIFICAR].
- DTCC dice (Stellar, 27-may) que quiere "integrar múltiples redes L1 y L2" (Nadine Chakar). No nombra más.
- Hoja de ruta "indicativa" con compensación en cadena (netting), efectivo digital y corporate actions, y Collateral AppChain (T1 2027, Chainlink CCIP): solo en prensa [S] (CantonNews, coingabbar, etc.) [VERIFICAR]; no aparece en los comunicados leídos.

## 2. Participantes
- 28-oct-2026, 20 participantes DTC con acuerdo firmado: Alpaca, Apex Clearing, Barclays, Bank of America, BNP Paribas, Brown Brothers Harriman, Citadel Securities, Citi, Clear Street, DriveWealth, Edward Jones, Fidelity Investments, Interchange Clearing, J.P. Morgan, Marex, Mirae Asset Securities (USA), Morgan Stanley, State Street, UBS, Velocity Capital. Más usuarios "de forma gradual".
- Colaboradores/ecosistema (28-oct): BitGo, Blockdaemon, Broadridge, DFNS, DRW, Fireblocks, HIFI, Kaleido, Matter Labs, Ondo, Prometheum, Talos, Taurus, Temple Digital, Tradeweb, Transcend, Virtu.
- Proveedores de monedero en la página del servicio: BitGo, Blockdaemon, DFNS, Fireblocks, HashKey Group, Kaleido, Prometheum, Talos, Taurus, Temple, Tradeweb.
- Grupo de trabajo: más de 150 empresas (28-oct); 50+ en mayo; más de 100 en julio (cifras distintas según fecha).
- Piloto 15-jul-2026: más de 30 firmas (incl. BlackRock, Circle, CME, Goldman, Microsoft, Nasdaq, NYSE, Vanguard, Chainlink, Ondo...).
- Ripple Prime figura en el grupo de trabajo de mayo (lista de 4-may-2026), junto a Robinhood, Kraken (Payward), Schwab, etc.

## 3. Activos
- Carta de no-acción de la SEC (11-dic-2025): constituyentes del Russell 1000, ETF que replican índices principales, y Tesoro de EE. UU. (letras, notas, bonos) (DTCC 4-may-2026).
- Cifra de valores al lanzamiento: la página oficial del servicio dice 34 valores, sin lista. Prensa previa hablaba de 25 [S]. Cifra "30 billones de dólares" elegibles: prensa [S] [VERIFICAR] (DTC custodia más de 114 billones, dato oficial).
- Token 1:1 respaldado por valores en DTC, mismo CUSIP, mismos derechos e inversor protegido (DTCC).

## 4. Calendario
- 11-dic-2025: carta de no-acción SEC (3 años, piloto voluntario).
- 4-may-2026: avance + grupo de trabajo.
- 27-may-2026: anuncio Stellar.
- 15-jul-2026: operaciones reales limitadas (colateral, préstamo de valores, DVP Tesoro/repo, DVP y DVD renta variable, transferencia, margen CCP).
- 28-oct-2026: lanzamiento DTS.
- 12-nov-2026: anuncio Solana.
- 1S 2027 Stellar; 2S 2027 Solana; 2027 Arc [S].

## 5. Condiciones (carta SEC, por fuentes secundarias de bufetes: Sidley, Mayer Brown, Morgan Lewis, Carlton Fields; el PDF de la SEC no se pudo leer como texto)
- Piloto voluntario de 3 años; acceso solo para participantes DTC con acuerdo.
- Monederos registrados en DTC en blockchains aprobadas; tokens solo transferibles entre monederos registrados; DTC conserva un "monedero raíz" que puede convertir/transferir/crear/quemar tokens.
- Requisitos objetivos y públicos para cadenas y protocolos; procedimientos de reversión (errores, mala conducta).
- No crea un marco general ni da cobertura a otros participantes (Morgan Lewis).
- Se leyó en prensa que la carta exige cadenas preaprobadas [S].

## 6. Qué dice la fuente sobre XRPL
- Ninguno de los comunicados de DTCC leídos (4-may, 27-may, 15-jul, 28-oct, 12-nov-2026) ni la página del servicio menciona XRP Ledger. Tampoco hay nada de XRPL en los comunicados de Stellar y Solana consultados.
- Única mención a Ripple en fuente primaria: Ripple Prime como miembro del grupo de trabajo (4-may-2026). Eso no implica soporte de red.
- Prensa cripto [S]: afirma que patentes de DTCC de 2025 citan XRPL y Stellar como compatibles; cuentas de nicho que vinculan XRP con DTCC (KuCoin News, Bitcoinist, Digital Today). Sesgo: contenido promocional de mercado. [VERIFICAR] (no abrí las patentes).
- Conclusión: hoy no hay anuncio de DTCC de XRPL como red del servicio ni en 2027. Ausencia de anuncio, no prueba de exclusión.

## Huecos
- No se leyó la carta SEC en texto (PDF binario).
- No se abrieron blogs propios de Canton, Besu, Arbitrum ni Avalanche; no hay evidencia hallada de Arbitrum/Avalanche en la hoja de ruta.
- Arc, AppChain y "30 billones" quedan [S] / [VERIFICAR].
