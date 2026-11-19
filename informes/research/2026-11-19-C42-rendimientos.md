---
titulo: C42 rendimientos y colateral, cifras vigentes (19-nov-2026)
fecha: 2026-11-19
etiquetas: [rendimientos, staking, lending, amm, colateral, xrpl, stellar]
---
# C42 · Cifras vigentes (19-nov-2026)

Informativo; no recomienda nada. P = leido por mi hoy en el panel oficial (Chrome); S = tercero o marketing de plataforma; [VERIFICAR] = no leido. Las plataformas son parte interesada. Datos en `explorador/rendimientos.json` (nuevo). No se tocó cadenas.json.

## Hechos
- **Lido** [P]: APR medio de 7 dias de stETH 2,33 % (12 al 18-nov, API eth-api.lido.fi). Comision no leida.
- **Rocket Pool** [P]: rETH 1,86 % APR (7 d); nodo 3,79 % + RPL; 534.464 ETH, 16.702 validadores; boveda RockSolid 2,86 %+.
- **Aave v3 Core** [P]: depositos 28,02 mil M$, prestamos 11,54 mil M$. USDC 4,42 % oferta / 5,23 % prestamo; USDT 3,16 / 4,15; ETH 1,47 / 2,07; DAI 3,00 / 4,73; RLUSD 2,46 / 4,68; WBTC y wstETH <0,01 % oferta.
- **Compound III USDC** [P]: oferta 3,22 %, prestamo 3,98 %; factores de colateral/liquidacion ETH 83/88, wstETH 82/86, WBTC 80/85. compound.finance redirige a compound.xyz.
- **Blend (Stellar)** [P]: un pool visible, 203,66 mil $ suministrados y 49,78 mil $ prestados (mercado diminuto). Terminos: excluye EE. UU., Script3 sin registro regulador.
- **AMM XRPL** [P, docs]: media geometrica 0,5, comision votada 0-1 %, 8 votantes cuentan, subasta 24 h, enmienda activada 22-mar-2024; riesgo de divisa; congelacion de activo congela LP tokens. DefiLlama 16-nov [S]: XRP-RLUSD 16,57 % APY con 3,75 M$ TVL.
- **AMM Stellar** [P, docs]: producto constante, comision fija 0,30 %, participaciones intransferibles, retirada automatica si el emisor revoca la autorizacion.
- **Coinbase** [S, marketing]: ETH 1,71 %, SOL 3,20 %, ADA 1,36 %, AVAX 3,13 %, DOT 2,00 %, ATOM 12,93 %, XTZ 2,57 % APY; USDC 4,1 % de recompensa y prestamo hasta 7,42 % (Morpho en Base). XRP y XLM no estan en su lista de staking.
- **Bitvavo** [P, su web]: staking y lending NO regulados por MiCA aunque la entidad tiene licencia CASP de la AFM; tasas no publicadas sin sesion; su web dice no dirigirse a espanoles (bitvavo.es) [VERIFICAR condiciones].
- **XRPL/Stellar**: sin staking de protocolo; lending nativo XRPL sin activar (ver cadenas.json).
- **DGT V0648-24** [S, hallazgo de la sesion, no releida]: no cubre colateral ni lending.

## Caso alcista / bajista
- Alcista: paneles de Aave y Compound son publicos y auditables en cifras; el AMM de XRPL y Stellar esta documentado con fees fijos o votados; MiCA y la FCA estan acotando el perimetro.
- Bajista: tasas bajas en ETH (1,5-2,3 %) frente a riesgo de contrato; Blend es minusculo; Bitvavo muestra que el lending/staking queda fuera de MiCA; sin criterio fiscal espanol para colateral y lending.

## Limites
Coinbase solo marketing; Bitvavo sin tasas; Lido sin comision leida; Morpho, Binance, Kraken y Stellar Blend por activo no leidos; DGT no releida. Comparar con cadenas.json para XLS-65/66. Sin commit, sin construir_*.
