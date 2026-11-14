# C276 · Cruce de hitos futuros de Cadenas con el Calendario (14-nov-2026)

Método: hitos `futuro:true` de explorador/cadenas.json comparados con eventos/calendario.toml; fuentes releídas en Chrome el 14-nov-2026. Solo se editó eventos/calendario.toml.

| Hito (cadenas.json) | Fecha cadenas | En calendario | Fuente releída | Resultado |
|---|---|---|---|---|
| XRPL: reinicio Testnet/Devnet (cal) | 2026-11-25 | Sí, misma fecha | xrpl.org/blog, entrada 9-nov [P] | Vigente (miércoles 25-nov). Detalle del evento ampliado |
| Ethereum Glamsterdam (cal) | 2026-12-31 aprox. | Sí, misma fecha | Everstake, actualizado 4-nov [S] | Sin fecha en mainnet; Hoodi aplazada el 22-oct; 4T-2026 «no confirmado». El detalle del evento decía «dos retrasos en Sepolia» (inexacto): corregido |
| DTCC Collateral AppChain (cal) | 2026-12-31 aprox. | Sí | DTCC, nota 12-may [P] | «Expected to go live in Q4 2026»; sin noticia de salida en vivo. Vigente |
| DTCC activos en Stellar (cal) | 2027-06-30 aprox. | Sí | DTCC, nota 27-may [P] | «1H27». Vigente |
| DTCC activos en Solana (sin cal) | 2027-12-31 aprox. | No estaba: añadido | DTCC, nota 12-nov [P] | «2S-2027». Evento nuevo (aproximado) |
| Quant: red Clearing House (sin cal) | 2027-06-30 aprox. | No estaba: añadido | Quant [P] | «1S-2027». Evento nuevo (aproximado) |
| Stellar Bell (Protocol 30) | n/a en cadenas | Sí (3-nov y 23-nov) | stellar.org, 20-oct [P] | Fechas vigentes (sujetas a cambio). Ver duplicado abajo |
| Swift: 19 bancos a fin de 2026 | n/a | Sí | Markets Media: el texto no pudo extraerse | Se mantiene [S] |

Contexto: DTCC lanzó el servicio el 28-oct-2026 (Canton y Besu; más redes en 2027) [P]. Apex jun-2027 y Sibos 2027: Sibos ya está; Apex no aparece en cadenas.json ni en el calendario: sin fuente leída, no se añade.

## Cambios en eventos/calendario.toml
- Glamsterdam: detalle corregido (Hoodi aplazada 22-oct, EIP-8037/8038), con [ESPECULACIÓN] sobre más retraso.
- XRPL reinicio: detalle con la fecha de la entrada (9-nov).
- Nuevos: DTCC-Solana (2027-12-31, aprox.) y Quant (2027-06-30, aprox.).

## Pendiente / lista para cadenas.json (no editado aquí)
1. Hito de Solana (cadenas/4/hitos/3, 2027-12-31): añadir `"cal": true` (ya está en el calendario).
2. Hito de Quant (cadenas/13/hitos/2, 2027-06-30): añadir `"cal": true`.
3. Hito de Glamsterdam: el texto ya recoge la aplazada en Hoodi; sin cambio de fecha.
4. Calendario: ids duplicados semánticamente del voto mainnet de Stellar Bell (23-nov): `ev-2026-11-23-stellar-voto-mainnet-protocol-30` y `ev-2026-11-23-stellar-protocolo-30-bell-voto-mainnet`; conviene eliminar uno (no se borró por prudencia).

Verificación: revisar_explorador.py 0 avisos; construir_movil.py y construir_seguimiento.py ejecutados.
