# W06 · Voces y predicciones (16-nov-2026)

Etiquetas: [P] primaria leída hoy · [S] prensa o resumen de búsqueda · [VERIFICAR]. Informativo; no es recomendación. Parte de W06 del 13-nov: no repito lo allí resuelto.

## 1. Predicciones
- **#19 (fixCleanup3_4_0 del XRPL): confirmada la activación [P].** `xrplcluster.com`, método `feature`, 16-nov 23:43 UTC: `enabled: true`. Antes era [S] (prensa). La fecha exacta (4-nov ~14:52 UTC según prensa) sigue sin leer en el ledger [VERIFICAR].
- **#23 (escrow de Ripple del 1-nov):** intenté leer los escrows en el ledger con la cuenta que cito de memoria y no devolvió objetos; no es prueba de nada (cuenta no confirmada en el `xrp-ledger.toml`). Sigue [VERIFICAR].
- **#24 (Ormuz) y #68 (Blumenthal, 30-nov):** sin cambios desde el 13-nov; plazo 30-nov.

## 2. Voces
- **v176 (lending y vaults del XRPL)** [P]: LendingProtocol, LendingProtocolV1_1 y SingleAssetVault siguen con `enabled: false` y sin mayoría registrada (16-nov). No cambia el nivel (es un «vigilar»); añadida la nota.
- **v174 (Bitvavo, 95 % en billeteras frías)**: bitvavo.com da 403 a lectores; sigue [S]/sin confirmar. **v137 (Binance)**: la URL de TRM da 404; sin atribución oficial leída.
- **Voces nuevas (3, nivel S, de fuentes distintas a las usadas):** v178 FMI (Georgieva, 28-ago-2026, riesgo de desintermediación bancaria), v179 Banco de Inglaterra (Wilkins, 15-sep-2026, stablecoins y dominio del dólar), v180 Banco de Inglaterra (Bailey, may-2026, choque regulatorio con EE. UU. y reembolsos). Solo resúmenes de búsqueda; no abrí los textos originales [VERIFICAR]. No hallé discurso de la Fed ni informe ECB de nov-2026.

## 3. Cierre
- Tocados: `explorador/voces.json` (179 voces), `informes/predicciones.md` (#19). `revisar_explorador.py`: 0 avisos.
- Vigilar: 30-nov (#24 y #68) y el estado de LendingProtocol/SingleAssetVault en el ledger.
- Seguridad: sin claves; solo RPC público del XRPL y páginas abiertas.
