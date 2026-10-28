# C49 · Stablecoins del XRPL y Stellar con fuente primaria (29-oct-2026)

**Qué se hizo:** `scripts/stablecoins_primarias.py` (sin IA) lee el propio ledger y guarda `stablecoins_primarias` en `explorador/paneles.json`; el panel «Stablecoins» lo muestra junto a DefiLlama. Si una lectura falla, conserva el dato anterior.

## Direcciones de emisor (de la web oficial, no de agregadores) [P]
- RLUSD (XRPL): `rMxCKbEDwqr76QuheSUMdEGf4B9xJ8m5De` — docs.ripple.com/products/stablecoin/overview/token-addresses
- USDC (XRPL): `rGm7WCVp9gb4jZHWTEtGUr4dd74z2XuWhE` · USDC (Stellar): `GA5ZSEJY…KZVN` — developers.circle.com/stablecoins/usdc-contract-addresses
- EURC (Stellar): `GDHU6WRG…NPP2` — developers.circle.com/stablecoins/eurc-contract-addresses (Circle no lista EURC en XRPL).

## Cifras (leídas 28/29-oct-2026)
| Moneda | En cadena [P] | DefiLlama [S] | Diferencia |
|---|---|---|---|
| RLUSD XRPL | 977,6 M$ (`gateway_balances`) | 977,6 M$ | ≈ 0 % |
| USDC XRPL | 4,47 M$ | 4,47 M$ | ≈ 0 % |
| USDC Stellar | 342,6 M$ (Horizon: cuentas+contratos+pools+reclamables) | 338,1 M$ | DefiLlama −1,3 % |
| EURC Stellar | 3,96 M€ | 4,92 M$ | no comparable directo (euros vs dólares) |

## Contraste con el emisor
- Ripple (transparencia, 22-oct-2026): 2.382,8 M$ de RLUSD en **todas** las cadenas y 2.528,0 M$ de reservas. El XRPL (≈978 M$, ≈41 %) es solo una parte; no se pueden comparar directamente. La página no da desglose por cadena. HECHO.
- Circle: no se contrastó la atestación (da el total global de USDC, no por cadena) [VERIFICAR].
- Sesgo: las páginas de los propios emisores son fuente primaria del dato de su emisión, pero no son auditoría independiente; las atestaciones son mensuales y llevan retraso.

## Diferencias y límites
- XRPL: DefiLlama coincide con el ledger. Stellar USDC: DefiLlama queda ~1,3 % por debajo (probablemente no cuenta algunos saldos de contratos/pools o usa otra fecha) [ESPECULACIÓN].
- El dossier del 17-oct (1.029 M$ RLUSD) frente a 977,6 M$ hoy: bajó la emisión en el XRPL (obligaciones netas), mismo método.
- **[VERIFICAR]:** direcciones oficiales de USDV, EURCV, YLDS y demás monedas que DefiLlama lista; no se leyeron.
- No engancha a `paneles.yml` (a la espera de tu OK). Se ejecuta con `python scripts/stablecoins_primarias.py`.
