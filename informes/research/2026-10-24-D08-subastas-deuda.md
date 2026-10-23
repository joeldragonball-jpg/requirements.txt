# D08 Calendario de subastas de deuda (24-oct-2026)

Sin recomendaciones de compra/venta. Solo calendario: no hay predicción de demanda. [P] = web oficial leída el 24-oct.

## Qué se ha leído y qué no
| País | Fuente oficial | Estado | Nivel |
|---|---|---|---|
| EE. UU. | TreasuryDirect, API `securities/upcoming` (curl) | Leído: 2, 5 y 7 años y FRN con importes, más letras | P |
| Japón | Ministerio de Finanzas, calendario mensual (`2610e`, `2611e`, `2612e`) | Leído hasta dic-2026 | P |
| España | Tesoro Público, calendario de subastas (navegador integrado; curl da 403) | Leído hasta ene-2027 | P |
| Francia | AFT, calendarios indicativos (imagen PNG, leída en pantalla) | Leído oct-nov 2026 | P |
| Italia | MEF (dt.mef.gov.it): las rutas probadas dan 404 | **No localizado**; queda pendiente | — |

## Fechas añadidas a `eventos/calendario.toml` (12 eventos)
- **EE. UU.:** 26-oct notas a 2 años ($69 mil M), 27-oct a 5 años ($70 mil M), 29-oct a 7 años ($44 mil M); liquidación el 2-nov. Aún sin importe: 17, 4 y 8 semanas de la semana próxima.
- **Japón:** 29-oct 2 años; 5-nov 10 años; 10-nov 30 años; 25-nov 40 años.
- **España:** 3-nov Letras a 6 y 12 meses (10-nov a 3 y 9 meses); 5-nov Bonos y Obligaciones (siguientes: 19-nov, 10-dic y 17-dic).
- **Francia:** 5-nov OAT a largo plazo; 19-nov OAT a medio plazo e indexadas; BTF cada lunes (2, 9, 16, 23 y 30 de noviembre). La AFT puede cancelar o añadir subastas.

## Cautelas
- El calendario de Japón ya recoge la «Liquidity Enhancement Auction» (recompra/reapertura) el 27-oct y el 20-nov; no la he añadido al calendario por ser técnica.
- La AFT publica el calendario como imagen: lectura visual, comprobar contra el anuncio de cada subasta.
- Los importes de EE. UU. del 5 y 7 años pueden cambiar hasta la fecha solo en casos excepcionales; son los anunciados el 22-oct.
- Pendiente: Italia (BTP) y, si se quiere, el anuncio trimestral de refinanciación del Tesoro de EE. UU. de principios de noviembre (fecha no verificada).
