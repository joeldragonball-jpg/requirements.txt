# Auditoría de datos [P] nuevos (14-nov-2026)

Alcance: 11 datos de `explorador/cadenas.json` e `indicadores-manual.json`, releídos hoy en la página citada. No se ha cambiado ningún dato.

| Dato | Fuente | Resultado |
|---|---|---|
| Reino Unido IPC sep-2026 = 3,5 % (ago 3,1; jul 2,9) | ONS serie D7G7 (ons.gov.uk, CSV de la serie) | Correcto: valor, fecha y serie coinciden |
| Venezuela INPC oct-2026 = 376,9 % interanual | BCV, Excel «INPC desde 2008» (`4_5_7.xls`) | No verificable aquí: el Excel se descargó (modificado 3-nov-2026), pero no hay lector .xls en el entorno y se denegó instalar uno. Queda [P] a la espera de que alguien abra el Excel y recalcule oct-26/oct-25 |
| Irán IPC Mehr 1405 = 71,4 % | cbi.ir (Inflation_FA.aspx) | No verificable: el WAF del BCI rechaza las descargas automáticas («Request Rejected»). La ficha ya admite que la definición es dudosa [VERIFICAR]. Se recomienda abrirla con Chrome |
| Hedera: staking sin bloqueo, recompensa votada por el Consejo, tasa en HashScan | docs.hedera.com, Stake HBAR | Correcto (la página dice que el máximo lo vota el Consejo y que no es fijo) |
| Plume: gas en PLUME, no en ETH | docs.plume.org, Gas and Fees | Correcto |
| Ondo OUSG: mínimo 5.000 $, tope global 50 M$/24 h, individual 25 M$ | docs.ondo.finance, Instant Limits | Correcto |
| Chainlink CCIP: 16 operadores independientes por ruta | docs.chain.link, arquitectura CCIP | Correcto |
| Ethereum: ERC-3643 (T-REX) estándar de tokens de valores | eips.ethereum.org/EIPS/eip-3643 | Correcto. Estado «Final»; la ficha no lo dice y no hace falta |
| Algorand: proponente cobra 50 % de comisiones más un bono decreciente «insostenible» | dev.algorand.co, staking rewards | Correcto («currently 50 %»; el bono es «intentionally unsustainable») |
| Solana: tasa de staking como función del % de oferta en stake | docs.anza.xyz, staking-rewards | Correcto (tasa vigente no leída, como dice la ficha) |
| XDC: rewards de masternodes por épocas, documento «WIP», tasa no extraída | docs.xdc.network/xdcchain/rewards | Correcto. La página tiene una sección «Annual Reward Rates (APR Model)»: la tasa se puede extraer en otra pasada |

## Pendiente
- Venezuela y Irán siguen en [P] sin comprobación mía; no se bajan de nivel porque la sesión que los subió dice haber leído las fuentes. Conviene que alguien los compruebe con Chrome.
- No se ha ejecutado `revisar_explorador.py` ni los `construir_*`, porque no cambió ningún archivo de datos.
