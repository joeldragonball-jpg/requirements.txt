# C311 · Detalle de activos tokenizados por red y tipo (15-nov-2026)

Qué hay: en `explorador/cadenas.json` cada `tipos_activo.tipos[tipo]` de 8 redes (Ethereum, Solana, BNB Chain, Stellar, XRPL, Avalanche, Polygon, Hedera, Plume: 9 en total) lleva ahora `detalle`: lista de {producto, emisor, subtipo, importe_musd, modo (distribuido/representado), n, f, d}. 136 filas. Donde RWA.xyz tiene activos representados grandes fuera de los tipos de la tabla (XRPL y Polygon: materias primas de Justoken, diamantes) van en `tipos_activo.aparte`.

Método: RWA.xyz, ficha de cada red, tabla de activos con el filtro de clase (Chrome, 15-nov-2026). Nivel [S] (agregador). «Emisor» = columna Platform de RWA.xyz; no prueba custodia. Hedera, XRPL, Avalanche, Polygon y Plume se leyeron sin filtro (listas cortas, primeras 25 filas) y se descartaron las stablecoins.

Confirmado por el emisor [P]: solo PAXG (paxos.com: 1 onza troy de oro London Good Delivery por token, custodia de Paxos Trust Company). XAUT: la página de Tether no se pudo leer (bloqueada) → custodia sin confirmar.

Hechos destacados (todo [S]):
- Oro/plata: XAUT 2.901 M$ y PAXG 1.708 M$ en Ethereum; también AZG, XAUm (Matrixdock), SLVon (réplica de ETF de plata, Ondo).
- Deuda EE. UU.: USDY (Ondo), WTGXX (WisdomTree), USTB (Superstate/Invesco), BUIDL (Securitize/BlackRock), JLTXX (JPMorgan/Kinexys, 742 M$ en Solana), USYC (Circle, 1.981 M$ en BNB), BENJI/iBENJI/sgBENJI (Franklin).
- Deuda no EE. UU.: fondos HKD/RMB de ChinaAMC (Libeara), EUTBL/UKTBL (Spiko), AGB (Aviva/Licuido), NRW1 (Cashlink).
- Crédito: Maple (syrupUSDC), Hastra, Centrifuge/Securitize (CLO AAA), Huma, OnRe (reaseguro); en XRPL casi todo es crédito brasileño representado (CRX Digital, VERT).
- Capital privado: tokens sobre SpaceX/Revolut/Anthropic (Republic, Colb Finance, Ctrl Alt), cosa a vigilar como riesgo de promoción.

[VERIFICAR]: JMWH (Justoken, 2.229 M$ representado en XRPL: qué materia es), materias agrícolas de Justoken en Polygon (deducidas del ticker), plataforma de TPT30 en Stellar (nombre truncado), AZX1 (Bridgetown, cobre; RWA.xyz muestra 335 M$ distribuidos y 10,7 mil M$ representados), emisor exacto de NRW1, plazos y rentabilidad (no se leyeron: no están en la tabla sin sesión). Las listas son parciales (primeros activos por valor) y no suman el total del tipo.

Vista: Órbita › Cadenas, bajo la tabla «¿Qué se tokeniza en cada red?»: desplegables por red y tipo (táctiles), con nivel y fecha en cada fila.
