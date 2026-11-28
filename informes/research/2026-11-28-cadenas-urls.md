# Cadenas: celdas sin URL, propuestas y comprobación (28-nov-2026)

Alcance: `explorador/cadenas.json`. Hay 40 celdas (objetos con `t` y `n`) sin `u` o con `u` vacío. Solo se han abierto las URL de la tabla; no se ha inventado ninguna. Se priorizaron las celdas con afirmación fáctica externa. Etiquetas: [P] leída y coincide, [S] no comprobada o solo parcial. WebFetch devuelve un resumen de la página, no el texto literal.

## Tabla de propuestas

| id/celda | afirmación | URL propuesta | comprobada | observación |
|---|---|---|---|---|
| cadenas/0/matriz/seguridad (XRPL) | UNL de 35 validadores publicada por Ripple | https://vl.ripple.com | parcial [S] | Carga: lista firmada (blob base64, secuencia 86). El lector no pudo decodificar el blob; estimó ~35 entradas sin garantía. No consta la autoría de Ripple en la propia página. Falta decodificar con `base64 -d \| jq '.validators \| length'`. |
| cadenas/1/matriz/seguridad (Stellar) | Consenso SCP | https://developers.stellar.org/docs/learn/fundamentals/stellar-consensus-protocol | sí [P] en SCP; [S] en el resto | Describe SCP (FBA, quórums, votación federada). NO menciona «nivel 1» ni «congelar y recuperar por línea de confianza»; esas dos partes siguen sin fuente. |
| cadenas/3/matriz/pagos (Ethereum) | Bloques de ~12 s | https://ethereum.org/en/developers/docs/blocks/ | sí [P] | Confirma slots de 12 s. «L2 más rápidos» y «comisión variable» no comprobados [S]. |
| cadenas/11/interconexion + interconexion_27nov/filas/1 (CCTP) | CCTP V2: Ethereum, Solana y Stellar (solo transferencia estándar); Hedera, XRPL y Canton no figuran | https://developers.circle.com/cctp/concepts/supported-chains-and-domains | sí [P] | Coincide exactamente: Ethereum (dominio 0), Solana (5), Stellar (27, solo estándar); Hedera, XRPL y Canton ausentes. Fuente primaria (Circle). |
| interconexion_27nov/filas/2 (DTCC) | Servicio de tokenización lanzado 28-oct-2026; Solana en 2S-2027; XRPL sin mención | https://www.dtcc.com/press-releases/2026/dtcc-tokenization-service-to-connect-with-solana | parcial [P]/[S] | Nota del 12-nov-2026: «DTS launched on Oct. 28», Solana prevista 2S-2027, sin XRP/XRPL/Ripple. NO menciona Canton ni Besu: esa parte necesita otra nota DTCC (listado «DTCC Tokenization Service Goes Live», 28-oct). |
| cadenas/8/matriz/rendimiento (DTCC pruebas 15-jul) | Margen y colateral tokenizados en las pruebas | https://www.dtcc.com/press-releases (índice) | no [S] | El índice carga pero no se abrió la nota del 15-jul; no hay URL directa confirmada. |
| interconexion_27nov/filas/0 (Chainlink CCIP) | Canton en producción 14-jul-2026; Hedera mainnet 8-abr-2025; Stellar anunciado; XRPL sin evidencia | https://docs.chain.link/ccip/directory/mainnet y /ccip/directory y /ccip/supported-networks | no [S] | Las tres rutas dieron 404. Sin URL válida; hay que localizar el directorio actual de CCIP. |
| cadenas/0/matriz/regulacion, cadenas/1, cadenas/4 (SEC-CFTC «digital commodity», 17-mar-2026) | XRP, XLM, SOL nombrados | https://www.sec.gov/newsroom/press-releases | no [S] | El índice carga (28-sep a 25-nov-2026); la interpretación de marzo no sale en esa página. `.../2026-30` dio 404 (adivinada, descartada). Hay que paginar el índice o buscar en sec.gov. |
| cadenas/4/matriz/cumplimiento (Mastercard-Solana, 3-jun-2026) | Liquidación de stablecoins en Solana | https://www.mastercard.com/news/press/ | no [S] | 403 Forbidden (bloqueo del sitio; no se evadió). Probar en Chrome. |
| cadenas/4/matriz/pagos (Solana ~1.868 tx/s, comisiones) | Medición propia + comisiones de fracciones de céntimo | https://solana.com/docs/core/transactions/fees | no [S] | 429 Too Many Requests. Reintentar más tarde. Los tx/s son una medición propia del 9-oct: no tienen fuente pública estable. |

## Resto de celdas sin URL (sin propuesta, con motivo)

No tienen URL porque son deducciones [R], resultados negativos «Sin integración primaria encontrada» [V], o citan un archivo interno (`i`) en lugar de fuente pública. No se inventó enlace.

- Deducciones o reglas internas: contexto_iso/8 y /9, relaciones/0/hechos/3, relaciones/2/hechos/3, relaciones/3/hechos/3, relaciones/4/hechos/4, brecha_rwa/brecha, rwa/reconciliacion_19nov, cadenas/0/tipos_activo/reconciliacion_19nov, brecha_rwa/lectura_actual/por_que/4, dtcc_ruta/marco/3 y dtcc_ruta/redes/3/celda (negativos sobre 8 documentos ya citados en otras celdas).
- Negativos [V] «Sin integración primaria con Swift/ISO 20022»: cadenas/1/iso/1, 2/iso/2, 4/iso/0, 5/iso/0, 6/iso/0, 7/iso/0, 10/iso/0, 11/iso/0. Un negativo no tiene URL: se documenta con la fecha de búsqueda.
- ETF spot (dossier interno, fuente SoSoValue / SEC): cadenas/0 (5 ETF XRP), 1 (GXLM OTCQX), 2 (HBAR), 3 (11 ETH), 6 (AVAX), 9 (LINK), 4 (9 SOL). Pendiente: buscar el listado de ETF en el emisor o en la SEC.
- Otros: cadenas/3/matriz/seguridad (validadores de ETH), cadenas/11/matriz/liquidez (USDC 62 M$ DefiLlama), vigilar/filas/3 (fecha 13F ≈15-feb-2027, sin cotejar con la SEC), interconexion_27nov/filas/3 (Swift, The Block/prensa vía agente).

## Resumen

- 40 celdas sin URL. Comprobadas con éxito [P]: 2 (CCTP de Circle; bloques de 12 s de Ethereum). Parciales: 4 (UNL de Ripple, SCP de Stellar, nota DTCC 12-nov, y partes de otras celdas).
- Bloqueos: Mastercard 403, Solana docs 429, Chainlink 404 (3 rutas), SEC 404 en el enlace adivinado.
- Sugerencia: añadir como `u` las URL con [P] (Circle, ethereum.org, DTCC 12-nov para la parte de Solana/XRPL) y dejar el resto como [S]/[V] hasta su cotejo en Chrome.
