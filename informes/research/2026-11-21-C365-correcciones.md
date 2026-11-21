# C365 · Correcciones del cotejo C362b en cadenas.json (21-nov-2026)

Solo se editó `explorador/cadenas.json` (campos t/f/d de 3 celdas). Cada cifra se leyó el 21-nov-2026 en Chrome antes de cambiarla. Revisión: `revisar_explorador.py` = 0 avisos.

## 1. chainlink/interop (nivel P)
- URL: https://docs.chain.link/ccip/directory/mainnet (solo se lee en navegador; 404 en WebFetch).
- Antes: 78 redes, 281 tokens, LINK en 65, USDC en 22, 3 verificadores (14-nov).
- Después (leído 21-nov): 77 redes, 281 tokens, LINK en 64, USDC en 23; verificadores CCTP 21 redes, Chainlink 70, Lombard 12. Fecha de la celda 2026-11-21.

## 2. ondo/rendimiento (nivel P)
- URLs: https://ondo.finance/usdy y https://ondo.finance/ousg.
- Antes: OUSG 3,70 % (30 d 3,7 %, 7 d 3,44 %); USDY 3,75 %, YTM 4,15 %, vencimiento medio 160 días.
- Después: USDY 3,75 % APY (fijado mensualmente), YTM 4,20 %, vencimiento medio ponderado 170,87 días (cartera 2.406,7 M$). OUSG 3,73 % APY (página oficial de OUSG, hoy); comisión de gestión limitada al 0,15 % y exenta hasta 1-ene-2027 (confirmada). Las cifras de OUSG a 30 d y 7 d no constan en la página: marcadas [VERIFICAR] en la celda. Se añadió la URL de OUSG en `f` (el campo `u` sigue siendo la de USDY).

## 3. xrpl/activos (nivel S)
- URL: https://app.rwa.xyz/networks/xrp-ledger (leída 21-nov).
- Antes: 642,8 M$ distribuidos (puesto 10), 5.210 M$ representados, Justoken ≈43 %.
- Después: 3,00 B$ distribuidos y 2,97 B$ representados; 456 activos RWA; 2.675 titulares. Se explica que RWA.xyz reclasificó el token de Justoken a «distribuido»; no se recalcula el 43 %. Se mantiene nivel S y se deja [VERIFICAR] porque la clasificación puede volver a cambiar. La marca anterior [VERIFICAR 21-nov] se sustituyó solo después de leer la cifra nueva.

## 4. Comprobaciones pedidas sin edición (las celdas están en regulacion.json, fuera del alcance «solo cadenas.json»)
- **ue/stablecoins «25 EMT»:** CSV de ESMA de emisores EMT (https://www.esma.europa.eu/sites/default/files/2024-12/EMTWP.csv, leído 21-nov): 26 emisores distintos por LEI (51 filas), sin Tether; CSV de ART (ARTZZ.csv): solo cabecera, 0 emisores. Es decir, «0 ART, sin Tether» coincide; «25 EMT» era el recuento del 22-oct y hoy son 26. La celda cita «registro del 22-oct», por lo que no es un error, pero conviene actualizar a 26 con fecha 21-nov. No editado.
- **eeuu/tokenizacion «AMM, cinco años»:** orden SEC 34-106402 (https://www.sec.gov/files/rules/exorders/2026/34-106402.pdf), leída extrayendo el texto del PDF: confirma exención temporal para negociar acciones NMS tokenizadas con AMM y pools de liquidez, y «expirará cinco años después de su publicación». Confirmado. El no-action de DTC del 11-dic-2025 NO aparece en esta orden (es otro documento de la SEC): sigue sin respaldo en esa URL. [VERIFICAR] pendiente en regulacion.json.

## Pendiente fuera de alcance
- regulacion.json ir/ley_marco: fecha 2024-12-08 → 2025-12-08 (corrección 4 del cotejo; no pedida en C365).
- bnb/seguridad (corrección 2 del cotejo) no estaba en el encargo de C365.
