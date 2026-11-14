# Cadenas: sexta pasada de huecos (14-nov-2026)

Solo se editó `explorador/cadenas.json`. Pasada cortada por el límite de uso. `revisar_explorador.py`: 0 avisos. Sin dato: 21 → 13. [VERIFICAR]: 6 → 2.

## Rutas nuevas que funcionaron
- `llms.txt` / `llms-full.txt` de IOTA, BNB, Polygon, Plume, Stellar; repos de GitHub clonados (XinFinOrg/Docs, algorandfoundation/devportal); comunicado de inversores de Visa; Claude in Chrome abre quant.network (curl no).
- No funcionó: solana.com (429 por curl; en Chrome el índice no trata interoperabilidad), EDGAR (403), api.github.com (límite), developer.algorand.co y Hedera Council (la lista de miembros no sale en el HTML).

## Celdas
| Red | Celda | Hecho | Fuente |
|---|---|---|---|
| IOTA | interop | LayerZero OFT V2 y puente IOTA EVM | docs.iota.org |
| XDC | interop | XDC Zero (subred↔red principal) | XinFinOrg/Docs |
| Algorand | interop | State Proofs; ARC-89 prevé NTT de Wormhole | algorandfoundation/devportal |
| Hedera | cumplimiento (V→P) | Council con voto igual y límites de mandato; sin cifra de miembros | hedera.com/council |
| BNB | cumplimiento | Pila de privacidad (Privacy Pool, ZKredit, FHE); posicionamiento propio | docs.bnbchain.org |
| Polygon | regulación | Open Money Stack: KYC/KYB/AML; sin licencia concreta | docs.polygon.technology |
| Plume | regulación | Reg. D y OFAC/AML en su doc; registro SEC como agente de transferencia sigue [V] | docs.plume.org |
| Stellar | rendimiento | Inflación terminada el 28-oct-2019; Blend/BENJI sin leer | developers.stellar.org |
| Avalanche | pagos (V→P) | Soportada en el piloto de liquidación de Visa (29-abr-2026) | investor.visa.com |
| Quant | pagos, activos, cumplimiento, regulación | Descripciones propias; sin licencia consta | quant.network |

## Sigue faltando
Solana interop; liquidez de Chainlink, XDC, IOTA y Quant; activos de IOTA; pagos de Ondo y XDC; regulación de Algorand, IOTA y XDC; seguridad y rendimiento de Quant; [V]: Plume liquidez, XDC cumplimiento (Contour). Datos descriptivos, sin ranking ni comparación con la tesis.
