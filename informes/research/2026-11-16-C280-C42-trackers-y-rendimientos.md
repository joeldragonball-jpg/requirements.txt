# Informe 16-nov-2026: C280 (trackers) y C42 (rendimientos, cifras de mercado)

**C280.** Farside (`farside.co.uk/btc/`, leído en Chrome el 16-nov) [S]: flujo neto diario de los ETF spot de BTC en EE. UU., 9-nov −201,0 M$; 10-nov −95,0; 11-nov −299,8; 12-nov −284,1; 13-nov −185,4. Guardado en `explorador/etf-flujos.json › trackers_contraste`. Farside no tiene página de XRP (404) y SoSoValue exige verificación de bots (no se salta): flujos agregados de XRP [VERIFICAR]. Flujo XRP por acciones x NAV del emisor sigue `null` hasta leer el 13-nov (17-nov).

**C42 (parte de cifras).** `scripts/leer_rendimientos.py` (API pública de DefiLlama, sin clave) escribe `explorador/rendimientos-defillama.json` (nivel S, 16-nov, APY puntual):
- XRPL: Tesoro tokenizado OUSG (Ondo) 3,44 % con 185,8 M$ de TVL y TBL (OpenEden) 3,43 %; pools XRP-RLUSD 16,6 % con 3,8 M$ de TVL. Los pools pequeños con APY alto tienen poco TVL y riesgo de contrato [RAZONADO].
- Stellar: USDY (Ondo) 3,75 % (539,2 M$); Blend USDC 6,19 % (7,9 M$); pool XLM de 97,6 M$ ≈0 %.
- Referencia Ethereum: Aave v3 USDC 3,80 %, USDT 3,17 %; Lido stETH 2,38 %.
- XRP y XLM no tienen staking de protocolo; XLS-66 (préstamos nativos) sigue en votación [VERIFICAR estado actual].
Son datos de protocolos (parte interesada) y de un agregador [S]; no son una recomendación.

**Pendiente C42:** estado legal por jurisdicción (Japón, Corea, Emiratos, UK y EE. UU. en lending) con texto primario; XLS-66 en vivo; aceptación de colateral tokenizado.
