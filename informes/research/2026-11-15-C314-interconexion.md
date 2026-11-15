# C314 · Interconexión entre cadenas: ¿existe una capa pública común supervisable?

Fecha: 15-nov-2026 · Datos: `explorador/interconexion.json` · Niveles: P = fuente primaria leída, S = secundaria, V = por verificar.
Neutral: no es recomendación de compra/venta ni ranking de redes.

## Pregunta de trabajo (hipótesis de un lector, no se da por cierta)
¿Existe o se está construyendo una red/capa pública común que interconecte las blockchains y sirva de libro auditable por un supervisor (DTCC, bancos centrales, reguladores) de los contratos y transacciones de las demás?

Se separa en cuatro partes: **A** interconecta muchas cadenas · **B** es común/pública · **C** es libro de cuentas de lo que pasa en las demás · **D** un supervisor puede auditarlo.

## HECHOS: qué existe y en qué estado
| Iniciativa | Estado | Qué es (y qué no) | Partes | Nivel |
|---|---|---|---|---|
| Chainlink CCIP | producción | Mensajería y tokens entre cadenas; T2-2026: 4.900 M$ de volumen (Chainlink, 24-jul-2026). No es un libro común. | A | P |
| Circle CCTP | producción | Quema/emisión de USDC; en 2026 añade Stellar, Sui, Aptos V2, Arc, etc.; desde 16-sep-2026 también otros tokens registrados (Circle). | A | P |
| Canton Network | producción | Red institucional con privacidad por subtransacción; los Super Validators ordenan sin ver el contenido. No lee cadenas públicas. | C, D posible | P/S |
| DTCC (DTS) | producción | Servicio de Tokenización en marcha 28-oct-2026 con Canton y Besu privada; carta de no acción de la SEC (dic-2025); Stellar (1S-2027) y Solana (2S-2027) anunciadas; Collateral AppChain con Chainlink CRE prevista T4-2026 (S). Solo sus activos. | A, D | P |
| Libro de Swift | piloto vivo | 17 bancos, depósitos tokenizados; no sustituye la liquidación final (ver C309). | C | P |
| Proyecto Agorá (BIS) | prototipo + valor real | 7 bancos centrales, +40 entidades (BIS, 27-may-2026); jul-2026: unos 800.000 CHF en 30 transacciones (S). Permisionado. | C, D | P/S |
| Libro unificado (BIS 2023) | concepto | El BIS dice que no es «un libro para gobernarlos a todos»; admite una «red de redes». | — | P |
| Partior · Fnality | producción | Libros interbancarios permisionados (USD/SGD/EUR; GBP con cuenta ómnibus en el BoE). | C | S |
| Nexus | en construcción, 2027 | Une pagos inmediatos nacionales; sin blockchain. | A | S |
| Mandala · Guardian/BLOOM | PoC / pilotos | Cumplimiento integrado (BIS) y pilotos de MAS en varias redes. | D | S |
| IBC · Polkadot | producción | Interoperabilidad abierta (clientes ligeros / cadena relé); sin supervisor. | A, B | S/V |
| Wormhole · LayerZero | producción | Puentes con incidentes: Wormhole feb-2022 (120.000 wETH, unos 320 M$); Kelp/LayerZero 18-abr-2026 (unos 292 M$, configuración 1-de-1 DVN). | A | S |
| ISO 20022 · ISO 24165 (DTI) | en vigor | Estándares; MiCA (Reg. Del. 2025/421) exige DTI en libros blancos cuando exista. | D (datos) | S |

## Hipótesis: a favor y en contra (solo hechos)
**A favor:** varias capas ya conectan decenas de cadenas (CCIP, CCTP, IBC); DTC sigue una estrategia multicadena declarada; los bancos centrales prueban una plataforma compartida en la que participan (Agorá); Swift pilota un libro compartido; los identificadores comunes (DTI) avanzan por regulación.

**En contra:** el BIS rechaza expresamente un libro único; todo lo que tiene supervisor dentro es permisionado; lo que conecta cadenas públicas solo pasa mensajes y no tiene supervisor; coexisten varias redes rivales; los puentes han sufrido pérdidas grandes; DTCC conecta cada red por separado y solo para sus valores.

**Lectura (hecho):** ninguna iniciativa encontrada cubre a la vez A, B, C y D.

## Quién tiene visibilidad hoy
- **SEC**: DTC y sus valores tokenizados, vía la carta de no acción; sin fuente de nodo directo en Canton.
- **DTCC**: sus activos en Canton y Besu, no contratos ajenos.
- **Bancos centrales de Agorá, BoE (Fnality), MAS (pilotos)**: solo sus plataformas o pilotos.
- **ESMA/ANC bajo MiCA**: lo que reportan CASP y emisores (libros blancos con DTI, regla de viaje); no supervisan cadenas como tales.

## Huecos y lo que no sabemos
- No hay anuncio de conexión entre libros permisionados (Agorá, Swift, Canton/DTCC, Partior, Fnality): en el mapa aparecen como islas.
- Sin documentación técnica leída de cómo un regulador obtiene una vista en Canton [VERIFICAR].
- Cifras de CCIP/CCTP/IBC de las propias empresas o prensa; recuentos de cadenas sin fuente primaria.
- Pendiente: redes de DTCC en 2027, producción de Agorá (sin calendario), Fnality en USD/EUR, Collateral AppChain.

## OPINIONES
- [ESPECULACIÓN] Lo observado encaja más con una «red de redes» (libros permisionados + protocolos de mensajería + estándares) que con una capa pública única; cambiaría si DTCC, Agorá o Swift se conectan entre sí o a cadenas públicas con vistas para supervisores.
- [ESPECULACIÓN] Canton y las plataformas de bancos centrales podrían actuar de registro de referencia para activos regulados, con las cadenas públicas conectadas por pasarelas; no hay anuncio que lo confirme.

Fuentes principales: dtcc.com (28-oct-2026), bis.org (27-may-2026; AER 2023 cap. III), chain.link (24-jul-2026), developers.circle.com (CCTP 2026), EUR-Lex 2025/421; resto en el JSON.
