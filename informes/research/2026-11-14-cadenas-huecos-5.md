# Cadenas: quinta pasada de huecos (14-nov-2026)

Solo se editó `explorador/cadenas.json`. Fuentes leídas con curl (User-Agent de navegador) en sus endpoints `.md` / `llms.txt`; no hizo falta Chrome ni hubo diálogos de descarga.

## Resultado
- Sin dato: 26 → 21. En [VERIFICAR]: 10 → 6. `revisar_explorador.py`: 0 avisos.

## Celdas nuevas o subidas a P (todas con documentación del propio proyecto, salvo EIP)
| Red | Celda | Hecho | Fuente |
|---|---|---|---|
| Hedera | rendimiento (V→P) | staking sin bloqueo ni «slashing»; el Consejo vota la recompensa máxima (no fija); tasa vigente en HashScan, no leída. Se retira el «2,5 %» del resumen de buscador | docs.hedera.com/learn/core-concepts/staking/ |
| Plume | interop | puente de Arbitrum, puente de pUSD y Stargate/LayerZero (100+ cadenas) | docs.plume.org, Bridges |
| Ondo | cumplimiento (V→P) | OUSG: «Qualified-Access» (patrimonio >5 M$ personas / >25 M$ entidades, criterios más comunes); USDY prohíbe EE. UU., Canadá y otras. La cifra antigua de 100.000 $ no figura | docs.ondo.finance |
| Ondo | regulación | OUSG bajo Reg. D 506(c) y exención 3(c)(7) (autodeclaración) | docs.ondo.finance, Regulatory Compliance |
| Ondo | liquidez | OUSG instantáneo solo en Ethereum: mín. 5.000 $, tope global 50 M$/24 h, individual 25 M$ | docs.ondo.finance, Instant limits |
| Chainlink | activos | SmartData (reservas, NAV, AUM); la doc avisa del riesgo de fuente única | docs.chain.link/data-feeds/smartdata |
| Ethereum | cumplimiento (V→P) | estándar ERC-3643 (T-REX); JPMD en Base se retira de la celda por no verificado y pasa a `sin_dato` | eips.ethereum.org/EIPS/eip-3643 |
| Solana | rendimiento (V→P) | recompensa a validadores según % de oferta en stake (documento de diseño de Agave); sin tasa vigente | docs.anza.xyz/implemented-proposals/staking-rewards |

## Sigue faltando (y por qué)
- Quant (7): web sin acceso (ver pasada 4); no se reintentó.
- Sin dato porque las docs oficiales leídas no lo tratan (ausencia ≠ prueba): interop de Algorand, IOTA y XDC (docs.xdc.network sin llms.txt ni página de puentes localizada); interop de Solana (solana.com da 429; docs.anza.xyz solo cubre el cliente).
- Regulación de Algorand, IOTA, XDC y Polygon; liquidez de IOTA y XDC; pagos de Ondo y XDC; activos de IOTA; liquidez de Chainlink: piden fuentes terceras (RWA.xyz, DefiLlama) o regulador.
- [V] restantes: Stellar rendimiento (informe institucional no leído), Hedera cumplimiento (nº de miembros del Consejo), Avalanche pagos (Visa), XDC cumplimiento (Contour), Plume liquidez y regulación (registro SEC en EDGAR sin leer).

## Avisos
- Datos descriptivos; sin ranking ni comparación con la tesis. Nada escrito en `privado/`.
- Lección: muchas docs (Mintlify, GitBook) sirven Markdown limpio añadiendo `.md` a la URL o vía `/llms.txt`; evita el ruido del HTML.
