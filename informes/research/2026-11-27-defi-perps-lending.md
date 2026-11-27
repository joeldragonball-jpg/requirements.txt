# DeFi, perps y lending a 27-nov-2026

Fuente principal: APIs públicas de DefiLlama (api.llama.fi, stablecoins.llama.fi, yields.llama.fi), consultadas el 27-nov-2026. Son datos agregados por un tercero: [S] salvo cotejo. Sin recomendaciones; hechos separados de opiniones.

Fiabilidad: DefiLlama es un agregador sin auditoría independiente; el volumen del día en curso queda incompleto hasta el cierre (el «-28 % en 1 día» de DEX es casi seguro un día parcial) [VERIFICAR].

## 1. TVL total y por cadena
HECHOS (DefiLlama /v2/chains y /v2/historicalChainTvl, 27-nov):
- TVL total DeFi (suma de cadenas): ~68,1 mM$ (serie histórica: 67,9 mM$ el 27-nov). Era ~91,5 mM$ el 29-sep, 84,7 el 27-oct, 78,2 el 10-nov, 71,0 el 17-nov, 69,2 el 24-nov. Caída ~26 % desde 29-sep y ~20 % desde 27-oct.
- Por cadena (mM$): Ethereum 36,4 · Solana 4,64 · Base 4,63 · Tron 4,31 · BSC 4,29 · Hyperliquid L1 2,24 · Bitcoin 2,22 · Arbitrum 1,21 · Robinhood Chain 0,99 · Monad 0,76 · Polygon 0,60 · Arc 0,59 · Ink 0,46 · Avalanche 0,43 · Sui 0,41.
- Solana: 6,41 mM$ (29-sep) -> 5,65 (27-oct) -> 4,62 (27-nov): -28 % en dos meses.
- XRPL: 30,3 M$ (de 45 M$ el 29-sep, -33 %). Stellar: 186 M$ (de 270 M$, -31 %).
Lectura (opinión): el TVL medido en dólares arrastra el precio de los activos; no distingue salida de capital de caída de precios [ESPECULACIÓN sobre la proporción].

## 2. Lending: Aave, Morpho, Sky (DefiLlama /protocols, yields.llama.fi)
TVL: Aave V3 15,36 mM$ (+6,2 % 7d), Aave V4 0,90 mM$ (+12,5 % 7d), Aave Horizon (RWA) 0,26; Morpho Blue 9,35 mM$ (+0,3 % 7d); Sky Lending 2,94 mM$ (+38 % 7d, [VERIFICAR] salto grande); Kamino Lend (Solana) 1,13 mM$.
Tasas de depósito (APY, 27-nov):
- Aave V3 Ethereum: USDC 3,05 %, USDT 2,88 %, sGHO 4,50 %.
- Sky: sUSDS 3,80 %; sDAI 1,25 %. Spark savings: USDT 4,25 %. Aparece un stUSDS con 50 % APY y SparkLend USDS 8,35 % (con base 0): probable recompensa temporal en pool pequeño, no representativo [VERIFICAR].
- Morpho (Robinhood Chain, steakUSDG): 7,04 % (3,51 % base + incentivos).
- Maple: USDC 5,25 %, USDT 4,94 %, USDG 4,86 %. Jupiter Lend (Solana): USDC 4,91 %.
- Ethena sUSDe: 4,84 %.
Sesgo: los APY mezclan tasa base e incentivos; los pools pequeños dan cifras extremas.

## 3. Stablecoins y rendimientos (stablecoins.llama.fi)
- Oferta total ~283,9 mM$. USDT 173,8 (de 181,8 hace un mes: -4,4 %), USDC 69,2 (de 71,3), USDe 4,93 (de 4,54), DAI 4,52, USDS 3,10 (de 6,66 hace un mes), USD1 2,85, RLUSD 2,84 (de 2,60), USDG 2,56.
- Lectura: la oferta de las dos grandes baja en el último mes; RLUSD (relevante para XRPL) sube ~9 % [S].
- Rendimiento: ~3-5 % en stablecoins en protocolos grandes; RWA tokenizados (Ondo OUSG en XRPL 3,82 %, USDY en Stellar 3,75 %, OpenEden TBL en XRPL 3,91 %) en línea con letras del Tesoro.

## 4. Staking líquido (yields.llama.fi)
Lido 16,17 mM$ (-2 % 1d; +3,1 % 7d), stETH APY 2,26 %; Binance WBETH 6,13 mM$ (2,33 %); ether.fi weETH 3,7 mM$ (2,37 %); Rocket Pool rETH 0,8 mM$ (1,84 %); Jito (SOL) 0,72 mM$, JitoSOL 4,74 %; Marinade mSOL 4,65 %. EigenCloud (restaking) 4,23 mM$.

## 5. DEX y perps
DEX (api.llama.fi/overview/dexs): volumen 24 h 5,93 mM$ (día probablemente incompleto), 7d 57,5 mM$, 30d 259,9 mM$; cambio 30d -15,8 %. Por protocolo 24 h: Aerodrome Slipstream 0,79 mM$, Uniswap V3 0,65, Uniswap V4 0,65, PancakeSwap V3 0,32, THORChain 0,24.
Perps (api.llama.fi/overview/open-interest; el endpoint de volumen de derivados devuelve 402 de pago: no evadido):
- Open interest total medido: 13,74 mM$ el 27-nov frente a ~17,7-18,5 mM$ a mediados/finales de octubre (-22 % en un mes).
- Hyperliquid Perps: OI 5,15 mM$ (-32 % en 1 mes). Aster Perps: 1,13 mM$ (-22 %). trade[XYZ] 4,18 mM$ (+5 %). Lighter 0,37 mM$ (-31 %). dYdX V4: 0,04 mM$ (+25 % 7d, -8 % 1m).
- Ingresos (fees) 24 h: Hyperliquid Perps 2,21 M$ (30d: 101,7 M$); Aster Perps 0,16 M$; dYdX V4 0,003 M$.
- Hyperliquid spot: volumen 92,6 M$ 24 h. Hyperliquid L1 TVL 2,24 mM$; puente 5,71 mM$.
[VERIFICAR] volúmenes nominales de perps (Hyperliquid, Aster, dYdX) contra sus paneles oficiales; solo tengo OI y fees.

## 6. Liquidaciones de la caída de noviembre
Resumen de búsqueda web (agregadores citando Coinglass; cifras no consolidadas, ventanas distintas) [VERIFICAR]:
- 13-nov: >225 M$ en una hora (Crypto Briefing); ~681 M$ en 24 h (TechFlow).
- 14-nov: 1,23 mM$ en 24 h, capitalización cripto -5,75 % a 2,33 B$, 82,7 % longs (BeInCrypto).
- 15-nov: 1,96 mM$ en 24 h, ~313.000 traders, 85,9 % longs (CoinCentral).
- 5-nov: varios tramos con >200 M$ de longs.
Advertencia: los buscadores mezclan noviembre de 2025 y 2026 (varios resultados de 2025); no hay total mensual autoritativo. Consistente con la caída del OI y TVL de arriba (desapalancamiento) [ESPECULACIÓN en la causalidad].

## 7. Solana y su ETF
- Cadena: TVL 4,64 mM$ (ver §1); Kamino 1,13 mM$; Jupiter Lend USDC 4,91 %.
- ETF spot de SOL (EE. UU., lanzados oct-2025): 16-nov-2026 entrada neta de 11,7 M$, 7d -12,6 M$ (CoinPerps); 10-nov salida neta de 10,56 M$, con BSOL de Bitwise -8,17 M$ (ChainCatcher/RootData). Acumulado: 1,42 mM$ (ChainCatcher) vs 1,65 mM$ titular y 1,36 mM$ en tabla (CoinPerps): discrepancia sin resolver [VERIFICAR]. Sin total mensual de noviembre.

## 8. XRPL
- DEX nativo XRPL DEX: 3,80 M$/24 h, 52,1 M$/7d (DefiLlama). TVL de la cadena 30,3 M$ (muy pequeño frente a Solana). Pools: xrpl-dex XRP-RLUSD 4 M$ TVL con 4,75 % APY; XRP-crypto 5 M$ con 0,1 % [S]. Tokenizados: Ondo OUSG 186 M$, OpenEden TBL 11 M$.
- Lending Protocol (XLS-66, sobre XLS-65 Single Asset Vaults): entró en votación de validadores el 28-ene-2026 (rippled 3.1.0); fuentes de jun-2026 aún lo ponen en devnet/testnet pendiente de aprobación; no he encontrado fecha de activación en mainnet [VERIFICAR en el tracker de enmiendas]. Diseño: préstamos de plazo fijo, sin colateral, amortización prefijada. Re-auditoría de Halborn (ene-2026); fixCleanup3_1_3 activada el 27-may-2026; borrador «AMM Swappable Curves» del 26-may-2026. Fuentes: RippleX (dev.to), Ripple Insights, Decrypt, OneKey/KuCoin (secundarias).
- Sesgo: casi todo es material de Ripple o prensa cripto promocional; sin cifra de TVL de lending en XRPL en DefiLlama.

## 9. Stellar DeFi
TVL 186 M$ (DefiLlama). Ondo USDY 540 M$ (3,75 %), Blend v2: XLM 89 M$ (APY 0), USDC 8 M$ (6,26 %), Aquarius DEX 0,64 M$/24 h (12,6 M$/7d); Curve en Stellar volumen irrelevante. Gami Labs EARNUSDC 32 M$ con 10 % (pool pequeño) [VERIFICAR]. Nota: el TVL de Stellar está dominado por un RWA (USDY), no por DeFi nativo [S].

## Límites
- Endpoint de volumen de derivados de DefiLlama: 402 (de pago). /overview/perps: 500. No se evadió.
- Búsqueda web con fechas mezcladas 2025/2026; no cotejado en Coinglass ni Farside directamente.

## Lista [VERIFICAR]
1. Volumen nominal perps de Hyperliquid, Aster y dYdX en sus paneles oficiales.
2. Total de liquidaciones de noviembre en Coinglass directo (rango 13-15 nov y mes completo).
3. Salto de +38 % 7d de TVL en Sky y APYs anómalos (stUSDS 50 %, SparkLend 8,35 %).
4. Flujos del ETF de SOL (Farside/emisores) y discrepancia de acumulado 1,36/1,42/1,65 mM$.
5. Estado de mainnet de XLS-65/66 (tracker de enmiendas XRPL / xrpl.org).
6. Volumen DEX del día 27-nov (cifra parcial).
7. Causa de la caída del TVL: precios vs salidas netas (DefiLlama en unidades nativas).
