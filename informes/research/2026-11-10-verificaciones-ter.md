# Verificaciones pendientes (3.ª tanda, 10-nov-2026)

Alcance: «Verificaciones pendientes con antigüedad» del Seguimiento (noticias de prensa sin contrastar). Método: búsqueda web (agregadores y prensa; fuentes oficiales solo vistas como resultado de búsqueda, no abiertas) + cierres de futuros de `explorador/precios_historico.json` (Yahoo, nivel [S]). Registrado todo en `eventos/verificados.json` (19 entradas nuevas, 84 en total).

## Alta (3)
| Noticia | Estado | Hecho verificado |
|---|---|---|
| Irak pacta con EE. UU. exportar crudo por Ormuz (8-nov) | **Matizada** [S] | Reuters 8-nov: el ministro Fuad Hussein dice a Al Jazeera que hay «entendimientos» con EE. UU. (carril cercano a Omán). Declaración de una parte, no pacto publicado; sin comunicado de Washington. |
| Brent cae >3 % y baja de 95 $ (9-nov) | **Confirmada** [S] | Futuro Brent: 98,32 $ (6-nov) → 92,57 $ (9-nov) = −5,8 %; 90,96 $ el 10-nov. |
| Brent cae casi 5 % hasta 93,72 $ (9-nov) | **Matizada** [S] | 93,72 $ es un nivel intradía; el cierre fue 92,57 $. No citar 93,72 como cierre. |

## Media (más de 14 días y otras de la tanda)
- **Confirmadas:** sanciones UE 12-oct, 1.569 listados (826 empresas + 743 directivos; Decisión PESC 2026/2279) [P vía SEAE]; IPC Argentina sept. 1,9 % / 33,4 % i.a. [S]; Moody's Francia Aa3 negativa (continuación, no cambio) [S]; IPC adelantado España 4,9 % [P, INE]; IPCA euro 4,0 % [S]; paro octubre 2.422.633 [P/S]; Binance cierra cuentas FR/ES/IT/PL el 31-dic [S]; tregua EE. UU.–China hasta 10-ene-2027 [S].
- **Matizadas:** subasta del Tesoro 5-nov (cifras coherentes en 2 medios, falta resultado oficial); candidatos a presidir el BCE (solo Hernández de Cos y Knot según prensa; resultado del Eurogrupo del 9-nov no hallado); elecciones de EE. UU. (Senado 54–44 con 2 sin declarar; Cámara llamada por AP en versiones posteriores; sin certificar).
- **Sin verificar:** petroleros incendiados 7-9 nov (nada fechado en noviembre salvo lo de W10); conversaciones de Abu Dabi 10-11 nov (solo hallada la ronda de enero).
- **Ya registradas antes como dudosas** (hutíes/Arabia Saudí 22-oct, Brent 111,97 del 23-oct, Chainlink-SWIFT, adquisiciones de Ripple, art. 66 LIRPF, DGT V0648-24, CLARITY 404 y cloture): no re-verificadas en esta tanda; siguen [VERIFICAR] con los intentos ya anotados. Las [baja] no se han abierto (el Seguimiento solo muestra media/alta en la lista).

## Hechos vs opiniones
- Hechos: cifras de IPC, paro, sanciones, cierres de futuros, el anuncio de Binance. Opiniones/atribuciones: la causa de la caída del Brent (esperanzas de paz con Irán, según prensa), «mina» como causa de los incendios (versión del IRGC), «entendimientos» iraquíes como acuerdo [ESPECULACIÓN] hasta que haya texto.
- Sesgos: Irak y el IRGC son partes interesadas; agregadores mezclan contrato/momento del Brent.

## Propuestas de corrección (no aplicadas a `explorador/datos.json`)
- Si la Línea de tiempo recoge «Brent 93,72 $» el 9-nov como cierre → cambiar a «Brent cierra en 92,57 $ (futuro, −5,8 %); 93,72 $ fue intradía». No he comprobado si la entrada existe (no se toca el archivo).
- Si recoge «Irak pacta/acuerda con EE. UU.» → reformular a «Irak dice tener entendimientos con EE. UU. (declaración del ministro, 8-nov)».
- Si recoge «prórroga de la tregua EE. UU.–China» con fecha 9-nov → la prórroga se anunció el 23-24-sep.

## Lecciones (5 líneas)
1. La búsqueda web no tiene crónicas del 9-nov; para precios, los cierres de `precios_historico.json` son la mejor referencia disponible [S] hasta el spot de la EIA (12-nov).
2. «Intradía» y «cierre» se mezclan en titulares: anotar siempre cuál es.
3. «Entendimientos» ≠ acuerdo: graduar la certeza según quién lo dice.
4. Noticias «de hoy» que repiten un hecho antiguo (tregua de septiembre): comprobar cuándo se anunció.
5. Las primarias (INE, SEAE, Seguridad Social) solo se vieron por resumen de búsqueda; abrirlas con Chrome en la siguiente tanda.

## Ampliación (2.ª pasada, mismo día): cripto, energía, España
- **Brent 111,97 $ (23-oct): desmentido como cierre** [S]. El futuro continuo cerró a 116,72 $ (Yahoo BZ=F; coincide con CNBC); 22-oct 113,17; 26-oct 115,81.
- **Chainlink CCIP en SWIFT: sigue dudosa.** Piloto ampliado (17 bancos, ledger de Swift activo desde jul-2026 según Genfinity [S]; Sibos 2026 sin hablar de «producción plena»); «11.000 bancos» sin respaldo. Falta nota de Swift/Chainlink.
- **Adquisiciones de Ripple: sigue sin precio** (Solvexia, Palisade, Standard Custody no divulgados). Cifras públicas solo de otras compras (GTreasury ≈1.000 M$, Hidden Road 1.250 M$, Rail 200 M$) [S].
- **Art. 66 LIRPF: confirmada [P]** (escala estatal 9,5-15 %, BOE leído en Chrome el 31-oct; combinada con la autonómica da 19-30 %).
- **DAC8 / modelos 172, 175, 721: sin publicar en el BOE** (solo proyectos de Hacienda de mar-2026; dudas sobre si el 172 se deroga) [VERIFICAR].
- **DGT V0648-24: existe** (11-abr-2024, DeFi) [S]; texto literal sin leer.
- **Sin cambios (siguen dudosas):** hutíes/Shaybah y Ras Tanura, petroleros de Ormuz, Abu Dabi 10-11 nov: la búsqueda web no devuelve nada nuevo; hace falta Chrome sobre UKMTO/comunicados.
- **Propuesta de corrección (Línea de tiempo, no aplicada):** si aparece «Brent cierra en 111,97 $» el 23-oct → «Brent cierra en 116,72 $ (futuro)».
