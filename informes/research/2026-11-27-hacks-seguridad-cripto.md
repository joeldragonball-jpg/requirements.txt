# Hackeos y seguridad cripto — noviembre 2026 (corte 27-nov-2026)

Investigación para el tablero Órbita. Solo hechos con fuente; sin recomendaciones.
Leyenda: [S] = solo una fuente / secundaria, [VERIFICAR] = no contrastado, [ESPECULACIÓN] = hipótesis.
Nota de método: búsqueda web + lectura de páginas (WebFetch, que resume). No se abrieron los paneles de DeFiLlama/CertiK/Rekt directamente; las cifras de esos trackers llegan vía prensa. Fuentes con 403 (no evitado): thehackernews.com, cryptotimes.io.

## 1. Contexto clave: el robo a Binance del 29-oct (afecta a las cifras de noviembre)

HECHOS (fecha 29-oct-2026, atribución y acciones judiciales en noviembre):
- Robo de más de 6.000 M$ en hot wallets de Binance el 29-oct. Cifras citadas: ~6,3 B$ (BleepingComputer, Crypto Briefing 26-nov), 6,36–6,43 B$ (The Hacker News, DefiLlama según Altcoin Buzz). El Departamento de Justicia de EE. UU. dice "más de 6.000 M$".
- Atribución: el FBI (con Servicio Secreto e IRS-CI) lo atribuye a Corea del Norte, grupo «TraderTraitor» (descrito por el DOJ como miembros del ejército norcoreano). Fuente primaria: nota del DOJ 26-1356, 12-nov-2026 (justice.gov/opa/pr/justice-department-announces-actions-disrupt-north-koreas-massive-theft-cryptocurrency). Alerta del FBI fechada 31-oct según Latin Times [S]. Kim Yo Jong habría negado participación (referencia en Wikipedia, sobre Bybit; no verificado para este caso) [VERIFICAR].
- Recuperación (DOJ, 12-nov): congelados >2.700 M$ entre Gobierno y sector privado; autorización judicial para incautar/restringir >1.200 M$. Latin Times: demanda civil de decomiso el 23-nov por >1.100 M$ en USDC [S]. Crypto Briefing (26-nov): congelados ~2.82–2.85 B$; recuperados realmente ~32 M$ [S].
- Causa según Binance: portátil de un ingeniero DevOps comprometido (BleepingComputer) [S]. Altcoin Buzz dice que el inicio fueron «falsas entrevistas de trabajo» sin citar fuente [VERIFICAR].
- Usuarios: Binance dice que ningún cliente asume pérdidas; compromiso de >6.340 M$ desde SAFU, tesorería y fondo de seguros de futuros; retiradas reabiertas por fases desde el 1-nov, casi todas las redes a 26-nov (Crypto Briefing 26-nov) [S].
- Lavado: el FBI espera conversión a ETH y paso por puentes, mezcladores y exchanges.
- Mismo comunicado del DOJ: campaña «FaceStealer» (ingeniería social por videollamadas con deepfakes y falso "arreglo técnico" que instala malware; >400 M$ en ~18 meses; objetivos: trabajadores cripto/Web3 y desarrolladores open source). Hay web fbi.gov/facestealer según el DOJ.

Reserva: el tamaño (récord histórico) obliga a contrastar con el panel de DeFiLlama y la nota del FBI directamente. [VERIFICAR]

## 2. Totales del año

- Altcoin Buzz, 12-nov (cita api.llama.fi/hacks, DefiLlama): 8,78 B$ en 328 hackeos a principios de noviembre; el Binance supondría ~72 %. Sin Binance quedarían ~2,5 B$. El propio análisis detecta incoherencias (recuperaciones casi todas nulas; cita de Immunefi que apunta a un informe de préstamos) [S].
- Otro dato citado en prensa: enero–octubre 8,74 B$ en 325 incidentes; octubre ~6,50 B$; febrero el mes mínimo, 21 M$ (resumen de búsqueda, fuente secundaria) [S][VERIFICAR].
- CertiK (vía CryptoSlate, 2-oct-2026): 2,68 B$ brutos en ~658 incidentes hasta septiembre; ~420 M$ congelados o devueltos (ajustado ~2,26 B$). Mayores: Bitget 387,5 M$; Liquid Network 318,7 M$ (gran parte recuperada); KelpDAO 291,3 M$; Drift 285,3 M$; víctima no identificada 284,8 M$. Top 5 ≈ 59 % del total. Septiembre ~766–768 M$ (PeckShield 766,49 M$ en 55 hackeos; CertiK 768,4 M$ en 97).
- CertiK, parcial de noviembre (a 6-nov, resumen de búsqueda): 171,7 M$ ajustados en 11 incidentes [S][VERIFICAR; no hay cierre mensual de noviembre en ninguna fuente].
- Diferencia metodológica: CertiK (~2,7 B$ a septiembre) y DefiLlama (~8,7 B$ con Binance) no son comparables sin ajustar por Binance y criterios de clasificación. [VERIFICAR]
- Un resultado sobre "hackeos en descenso, 65 M$" sin fecha probablemente es de otro año: descartado.
- No encontré totales de noviembre de PeckShield, Immunefi, Hacken ni Chainalysis.

## 3. Incidentes de noviembre 2026 (principalmente de cryptoticker.io/crypto-hack-news y DefiLlama vía búsqueda; cifras difieren entre fuentes) [S]

| Fecha | Víctima | Importe | Atribución | Recuperación |
|---|---|---|---|---|
| 2-nov | Mercado Bitcoin (exchange, Brasil) | La empresa: ~38 M$; Hypernative >40 M$; DefiLlama 40 M$; Cointelegraph >46 M$; Chainalysis ~49 M$ en 17 cadenas (vía CoinStats) | No nombrada | ~11 M$ congelados (empresa); >9 M$ USDT congelados con ayuda de Chainalysis, Tether, Circle, Ripple (Coinpaper); la empresa dice que solo hot wallets y clientes sin pérdida |
| 2-nov | BitMart | ~391.000 $ (Base, Arbitrum, Optimism) | No nombrada | Plan de acreedores revisado |
| 1-nov | Sovryn DEX 539.000 $; Premia V3 437.000 $ | — | No nombrada | — |
| 5-nov | TENDRIL ~550.000 $ (BSC) | — | — | — |
| 6-nov | Keplr (login social vía Web3Auth) | Desde ~700.000 $ a varios millones, sin cifra oficial | No nombrada | Login social pausado; seed phrase y hardware wallets no afectadas |
| 8-nov | ACryptoS ~665.000 $ | — | — | — |
| 10-nov | Arcus Perps (Robinhood Chain) ~2,23 M$; Across (dominio secuestrado, sin cifra); Initia 615.000 $ (clave) | — | No nombrada | Arcus cubierto con tesorería |
| 14-nov | Kava Lend ~3,3–3,7 M$ | — | No nombrada | Axelar bridge pausado |
| 16-nov | Safe multisig (Zodiac Roles) ~6,45 M$ (PeckShield); 6,44 M$ (Unchained) | Clave de rol «probablemente comprometida» (Zodiac); Bitquery ve similitudes con Lighter, sin vínculo directo | Sin recuperación; ~0,8–1 M$ pasaron a XMR1 en Hyperliquid |
| 16-nov | Lighter (perps) 10,39 M$ (DefiLlama) a ~15,5 M$ | Código de firma de un trader que reutilizaba nonces | ~5 M$ USDC devueltos al trader; retiradas reabiertas |
| 17-nov | Hegic ~1 M$ | — | Compensación prometida |
| 18-nov | K3 Capital / Reental (sBOLD, Liquity V2) ~3,43 M$ (Blockaid) | Flash loan según Blockaid | Contratos pausados |
| 18-nov | Gonka AI (puente) ~1,05 M$ | — | Sin plan de recuperación |
| 20-nov | Wagyu XMR1 (Hyperliquid) ~13,2–13,5 M$ | Clave del deployer; el hosting 1984.hosting reporta brecha | Fundador cubrirá con fondos propios |
| 21-nov | Chainflip ~4,86 M$ (520 ETH, 3,25 M USDC, 758.000 USDT) | Clave compartida de validadores, probable; fondos a Tornado Cash | Clave rotada, modo seguro |
| 22-nov | Fusionist/Endurance bridge (ACE) ~1–2 M$ + ~3,7 M$ por operadores | — | Gate revierte operaciones |
| 24-nov | Bullpen (terminal de trading) ~2,15–2,57 M$ | Clave privada importada de la cartera de un influencer | Servicio offline |

- Un resumen de búsqueda mencionó "Chainflip 12 M$ por compromiso de clave" (web3isgoinggreat); no pude fecharlo; el dato fechado más sólido es 4,86 M$ el 21-nov. [VERIFICAR]
- «Cyber bridge anomaly 21-nov», «Wagyu XMR1 20-nov» y «Cryptio, ataque fallido» salen del registro de SlowMist (resumen de búsqueda) [S].
- Fin de octubre (no noviembre): Polymarket ~2,7 M$ el 29-oct (script secuestrado de DebugBear); Chainalysis filtró datos de personal de clientes el 30-oct (sin pérdida financiera).
- Patrón señalado en las fuentes: claves privadas/accesos comprometidos y cadena de suministro (scripts, dominios, hosting, login social) más que fallos de contrato. Es una lectura mía a partir de la tabla [ESPECULACIÓN].

## 4. Atribución (solo con fuente)

- Binance, 29-oct: Corea del Norte, TraderTraitor (FBI/DOJ, 12-nov). Hecho atribuido oficialmente; la negativa norcoreana no está contrastada.
- Elliptic (vía CryptoSlate, 2-oct): >1.000 M$ robados en 2026 por actores sospechosos de ser de Corea del Norte (>51 incidentes); Bitget «muy probablemente» vinculado, Drift vinculado anteriormente. CryptoSlate no atribuye explícitamente los incidentes de 2026 a «Lazarus».
- Altcoin Buzz dice que Kelp DAO fue atribuido a Lazarus sin fuente [VERIFICAR].
- Mercado Bitcoin, Safe/Zodiac, Lighter, Chainflip, Wagyu, Bullpen: sin atribución pública.

## 5. XRPL y Stellar

XRPL:
- Fallo de desbordamiento de entero de 64 bits en el motor de pagos (afecta xrpld ≤3.4.0; posiblemente desde ~2015): permitiría gastar XRP inexistente más allá del tope de 100.000 M. Reportado el 22-sep por Cayden Liao (Veria Labs) vía bug bounty; parche xrpld 3.4.1 el 25-sep; detalles públicos el 9-oct (Crypto Briefing). Sin evidencia de explotación ni pérdida de fondos. El parche se desplegó sin votación de validadores. Veria dice que la detección/exploit se hizo con un agente de IA [S].
- Un resumen de búsqueda sitúa la activación de «fixCleanup3_4_0» el 4-nov 14:52 UTC; la relación con el parche de septiembre es probable pero no confirmada. [VERIFICAR]
- Otros (no de noviembre): puente Coreum–XRPL ~199.916 XRP en agosto; cartera XRP Healthcare ~267.000 XRP el 3-sep (fuentes menores, tech-insider/whale-alert) [S].
- Noviembre: no encontré hackeo del protocolo XRPL. Ripple participó en las congelaciones de Mercado Bitcoin (Coinpaper).

Stellar:
- Mercado Bitcoin 2-nov: la dirección del atacante en Stellar tenía ~6,71 M XLM y ~979.527 USDC (Bitquery, vía Coinpaper 3-nov). Sin evidencia de compromiso de la cadena Stellar; el XLM nativo no es congelable por emisor; no se reportó respuesta de la SDF [S].
- Binance: desconozco si hay exposición de XRP/XLM en los fondos robados [VERIFICAR].

## 6. Estafas (pig butchering) y otras amenazas

- Sin cifras de noviembre. Datos del año (todos secundarios) [S][VERIFICAR]: FBI IC3 2025 (abril 2026) ~20,9 B$ en estafas online; Chainalysis (informe 2026) ~17 B$ en estafas cripto de 2025 (vía blog); FinCEN ~12,7–13 B$ ligados a centros de estafa asiáticos (~1.300 instituciones); CertiK 370,3 M$ de estafas en enero 2026; abril 2026: 276 detenciones en operaciones coordinadas EE. UU./EAU/China/Tailandia.
- Vectores de noviembre: FaceStealer (deepfakes en videollamada, DOJ 12-nov); suplantación tras el apagón de Microsoft 365 del 12-nov (Microsoft, detectado 13-nov; no es de cripto); aviso de CertiK sobre exploit iOS «DarkSword» contra carteras (6-nov, cryptotimes; página con 403, solo titular) [VERIFICAR].
- Consejo repetido por cryptoticker: usar solo canales oficiales e ignorar ofertas de «reembolso» no solicitadas (es una fuente de noticias, no un aviso de exchange).

## 7. Avisos de exchanges

- No encontré avisos de seguridad específicos de Coinbase, Kraken, Binance o Bitvavo en noviembre. Hay comunicados de incidente: Binance (reembolso total, proof-of-reserves acelerado, retiradas por fases), Mercado Bitcoin (retiradas suspendidas, sin pérdida de clientes), BitMart (plan de acreedores), Lighter (retiradas reabiertas) [VERIFICAR en las webs oficiales].

## Lista [VERIFICAR]
1. Cifra final del robo a Binance (6,0 / 6,3 / 6,43 B$) y totales congelados/recuperados (2,7–2,85 B$ congelados vs ~32 M$ recuperados) en la nota original del FBI/DOJ.
2. Causa del robo a Binance (portátil DevOps vs «entrevistas falsas»).
3. Total de noviembre de DeFiLlama/CertiK/PeckShield (no publicado aún); 171,7 M$ de CertiK es parcial a 6-nov.
4. Totales anuales: 8,78 B$ (DefiLlama, con Binance) vs 2,68 B$ (CertiK a septiembre); metodologías distintas.
5. Cifra de Mercado Bitcoin (38 / 40 / 46 / 49 M$) y si la atribución es pública.
6. Chainflip: 4,86 M$ (21-nov) vs «12 M$» sin fecha.
7. Lighter: 10,4 vs 15,5 M$; Keplr: importe real.
8. Activación «fixCleanup3_4_0» el 4-nov en XRPL y su relación con el parche 3.4.1.
9. Atribución de Kelp DAO a Lazarus (sin fuente).
10. Exposición de XRP/XLM en el robo a Binance o en fondos de Mercado Bitcoin (6,7 M XLM del atacante: ¿movidos?).
11. Avisos oficiales de exchanges (Coinbase, Kraken, Bitvavo, Binance) sobre phishing/FaceStealer.
12. Aviso DarkSword de CertiK (página inaccesible, 403).

## Fuentes principales
- DOJ, 12-nov-2026: https://www.justice.gov/opa/pr/justice-department-announces-actions-disrupt-north-koreas-massive-theft-cryptocurrency
- Crypto Briefing, 26-nov: https://cryptobriefing.com/binance-restores-withdrawals-after-record-hack/
- BleepingComputer: https://www.bleepingcomputer.com/news/security/fbi-links-63-billion-binance-crypto-heist-to-north-korean-hackers/
- Altcoin Buzz, 12-nov: https://www.altcoinbuzz.io/8-78-billion-lost-to-328-hacks-crypto-s-record-2026
- CryptoSlate, 2-oct: https://cryptoslate.com/crypto-hackers-have-taken-2-7-billion-in-2026-and-the-losses-are-alarmingly-concentrated/
- CryptoTicker (lista de incidentes): https://cryptoticker.io/en/crypto-hack-news/
- CryptoTicker, Safe/Zodiac: https://cryptoticker.io/en/safe-multisig-zodiac-roles-theft-6-45-million/
- Coinpaper, 3-nov (Stellar/Mercado): https://coinpaper.com/38264/stellar-hack-alert-6-7-million-xlm-traced-to-attacker-after-40-million-mercado-bitcoin-breach
- Crypto Briefing (bug XRPL): https://cryptobriefing.com/xrp-ledger-overflow-bug-extra-xrp/
