# C50 · Valor tokenizado por blockchain: mejor fuente (29-oct-2026)

Nivel: [S] = agregador/prensa; [P] = emisor o fuente oficial; [VERIFICAR] = sin contrastar. Información, no recomendación.

## Tabla propuesta «por blockchain»

| Cadena | DefiLlama (TVL en protocolos RWA DeFi) [S], 29-oct | RWA.xyz «distributed» [S], 28-oct | RWA.xyz «represented» [S], 28-oct | Emisores con cifra |
|---|---|---|---|---|
| Ethereum | ~$1.900 M | $15.947 M | $107 M | BUIDL, Ondo, BENJI (sin cifra por cadena verificada) [VERIFICAR] |
| Solana | ~$607 M | $4.890 M | $126 M | Ondo, BENJI (sin cifra por cadena) [VERIFICAR] |
| Stellar | ~$7 M (puesto 20) | $3.768 M | $78 M | BENJI (Franklin Templeton): ~$563 M (Allium, jun-2026) / $654 M (caso Stellar, sin fecha) [S]; WisdomTree WTGXX, YLDS: sin cifra [VERIFICAR] |
| XRPL | fuera del ranking | $642 M | $4.798 M | Ondo OUSG: «>$670 M TVL» según Ripple (fecha por confirmar, es en toda la oferta, no solo XRPL) [VERIFICAR]; OpenEden TBILL, Archax (compromiso de $1.000 M a mediados de 2026, sin confirmar cumplimiento), Guggenheim DCP: sin cifra [VERIFICAR] |

Fuente RWA.xyz: https://app.rwa.xyz/networks (leída vía WebFetch; el resumen lo hizo un modelo, así que cifras = [S] hasta comprobarlas a mano en pantalla).

## Por qué difieren
- **DefiLlama** cuenta el TVL bloqueado en protocolos DeFi con categoría RWA. Un fondo tokenizado que solo se mantiene en carteras (p. ej. BENJI en Stellar) no es «TVL» → Stellar sale ~$7 M frente a $3.768 M.
- **RWA.xyz «distributed»** = activo emitido y transferible en la cadena (incluye fondos de bonos del Tesoro, crédito, etc.). **«Represented»** = activos registrados on-chain pero no transferibles/sin liquidación on-chain: por eso XRPL tiene $4.798 M «represented» y solo $642 M «distributed».
- Cifras de prensa para XRPL ($1,75 M–$4,1 mil M, sin fecha) mezclan ambas métricas → no usar sin etiqueta de métrica [VERIFICAR]. Un dato de la Fundación Stellar (~$490 M, 20-ago) solo parece cubrir deuda pública no estadounidense.
- Los emisores multicadena (BENJI: ~$1.980 M en 9 cadenas, jun-2026 [S]; Ondo ~$2.700 M, mar-2026 [S]) no se pueden sumar por cadena sin su atestación/direcciones.

## Qué se pudo contrastar
Con fuente primaria: nada completo. Pendiente en webs oficiales (franklintempleton.com, stellar.org, ripple.com, ondo.finance, BlackRock BUIDL) y explorador de cadena.

## Automático vs manual
- **Automático (semanal, ya existe):** DefiLlama por cadena [S].
- **Manual (mensual, Claude/Gemini):** RWA.xyz distributed y represented por cadena (sin API gratuita), con fecha.
- **Manual (mensual/trimestral):** cifras de emisores [P] desde su web o atestación; anotar fecha y si es total multicadena o por cadena.
- Mostrar siempre las dos métricas de RWA.xyz y un pie con la definición.
