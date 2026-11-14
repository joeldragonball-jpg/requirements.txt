# C268 · Qué se tokeniza en cada red por tipo de activo (14-nov-2026)

Estado: **parcial** (6 de 16 redes; plazo de liquidación sin dato en todas).

## Hechos (HECHOS, no opiniones)
- Añadido `tipos_activo` a las 6 redes con más tokenización en `explorador/cadenas.json` (Ethereum, BNB Chain, Solana, Stellar, Avalanche, XRPL): valor y nº de activos por tipo, emisores principales y estándar de contrato.
- Fuente de las cifras: RWA.xyz, pestañas «Asset Classes» y «Platforms» de la ficha de cada red, leídas en el navegador el 14-nov-2026 [S] (tercero comercial, sin auditoría). Las clases de RWA.xyz se agrupan en: deuda (US Treasury + no-US), fondos y estrategias (Active Strategies), acciones, materias primas, crédito privado (activo respaldado, corporativo, diversificado, financiación especializada), inmuebles, otros (private equity, venture, cripto).
- Estándares leídos en fuente primaria [P]: ERC-3643 (EIP final, 2021-07-09); SEP-57 T-REX de Stellar (Draft v0.4.0, actualizado 2026-09-08, basado en ERC-3643); MPT del XRPL (enmienda MPTokensV1). BNB Chain, Solana y Avalanche: estándar sin dato (no leído).

## Trampas de RWA.xyz (heredadas de C264)
1. La tabla de clases y la de plataformas INCLUYEN stablecoins (p. ej. Ethereum: 136.000 M$ de stablecoins frente a 15.150 M$ de «distribuido» sin ellas); aquí se excluyen.
2. Solo se ven las 10 mayores clases: lo que falta es «sin dato», no cero. Las cifras ≥ 1.000 M$ están redondeadas a 0,1 mil M$ en la web (p. ej. «$4.3B»).
3. «Distribuido» ≠ «representado»: el XRPL tiene 5.207 M$ representados (≈43 % un token de materias primas) que esta tabla no muestra; Avalanche 11.403 M$ y Canton 374.118 M$ representados. No se suman.
4. Sin sesión, RWA.xyz oculta la variación a 30 días («Login to Unlock»): no se usa.
5. Orden de magnitud: deuda y letras del Tesoro es el mayor tipo en BNB Chain (4,3 mil M$), Stellar (2,0 mil M$ en Treasury) y Solana; en Ethereum domina materias primas (4,8 mil M$, sobre todo oro: XAUT, PAXG según la tabla de activos) y deuda (4,3 mil M$). No es un ranking de «mejor red».

## Pendiente
- Plazo de liquidación (T+0/T+1) por emisor: no leído en fuente → null en las 6 redes.
- Estándar de contrato en BNB Chain, Solana, Avalanche; nº exacto de emisores; las otras 10 redes (Hedera, Polygon, Base, Arbitrum, Algorand, Canton…).
- Cotejar con páginas oficiales de Franklin, Ondo, Securitize, Spiko (productos y plazos).

## Interfaz
Tabla «¿Qué se tokeniza en cada red?» bajo la matriz de la pestaña Cadenas (`explorador/vistas.html`): barras por tipo, sin desbordar a 768 px; estándar, emisores y plazo debajo. Comprobado a 768 px y escritorio, sin NaN ni «undefined»; `revisar_explorador.py`: 0 avisos.
