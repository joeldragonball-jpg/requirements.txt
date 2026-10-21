# Verificación con Chrome y descargas directas (sesión del 21-oct-2026)

Objetivo: cerrar celdas del radar que seguían [S] por páginas oficiales que daban 403. Método: Chrome (extensión) solo para **localizar la URL oficial y abrir páginas que bloquean a mi lector**; cuando el PDF o la API estaban abiertos, `curl` + `pdftotext` (más barato). No se inició sesión en ninguna cuenta.

| Tema | Fuente oficial leída | Resultado | Etiqueta |
|---|---|---|---|
| UE · Euro digital (posición del Consejo) | Nota de prensa del Consejo, 19-dic-2025 (Chrome; el texto extraído solo dio el pie de página, se leyeron los párrafos con `find`) | Confirmada: «Council agrees position on the digital euro and on strengthening the role of cash»; límites de tenencia, uso sin conexión, tarifas máximas y entrada en negociación con el Parlamento | [P] (no texto íntegro) |
| GAFI · 7.ª actualización | Página oficial, 16-jul-2026 (Chrome) | Fecha y resumen confirmados: avances, brechas, fraude industrializado, mal uso de stablecoins, P2P, offshore y DeFi. El PDF de 3 MB no se leyó, así que las cifras del 83 % y ~40 % siguen sin comprobar | [P] el resumen; cifras [VERIFICAR] |
| BRICS · Declaración de Nueva Delhi | PDF oficial de brics2026.gov.in (URL hallada en Chrome; descargado con `curl`, 45 páginas) | Fecha 12-sep-2026. Párr. 90: interoperabilidad de pagos, monedas locales, «sin talla única». **No aparecen** CBDC, stablecoin, cripto ni activos digitales (búsqueda en todo el texto) | [P] |
| India · fiscal | Páginas oficiales de las secciones 115BBH y 194S (Chrome; `curl` da Access Denied) | 115BBH: 30 % sobre la transferencia de activos digitales virtuales, sin deducciones salvo el coste y sin compensar pérdidas. 194S confirmada, el 1 % no se vio en el elemento leído. La numeración en la Income-tax Act 2025 no se localizó | [P] 30 %; 1 % [S] |
| Brasil · Banco Central | API oficial de normas del BCB (con `curl`) | Res. 521 (10-nov-2025): lleva a los prestadores de activos virtuales al mercado de cambios. Res. 561 (30-abr-2026, DOU 5-may-2026): prohíbe usar activos virtuales para liquidar el eFX; vigente desde 1-oct-2026. Res. 584 (7-ago-2026, DOU 11-ago-2026): retención de 24 h en transferencias a entidades extranjeras de activos virtuales o carteras autocustodiadas, desde 1-ene-2027, con umbral de 10.000 USD o política de riesgos | [P] |

Corrección de lo que decía el radar: la Res. 584 NO es un tema aparte de «envíos de más de 10.000 USD» en general, sino de **activos virtuales** hacia entidades extranjeras o carteras autocustodiadas; el [VERIFICAR] sobre su fecha queda cerrado (vigencia 1-ene-2027).

## Lo que aprendí del método
- Chrome sirve para **encontrar la URL oficial** y para páginas con 403; después, si es un PDF o una API abierta, `curl` lo lee sin gastar contexto. El texto de `get_page_text` a veces solo devuelve el pie de página (sitios del Consejo de la UE): usar `find` con una frase concreta y no `read_page` completo (gasta mucho por los menús).
- La API del BCB (`bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolução BCB&p2=NÚMERO`) devuelve el texto del normativo en JSON.
- `incometaxindia.gov.in` bloquea `curl`; solo se leyó con Chrome.

## Sigue pendiente
Indonesia (OJK), Egipto y Etiopía (textos oficiales), cifra de ~40 % de supervisión en el PDF del GAFI y numeración de la ley india de 2025. (China y Hangang se cerraron después; ver la ampliación de abajo.)

## Ampliación (misma sesión): Hangang, GAFI y China
| Tema | Fuente leída | Resultado |
|---|---|---|
| Corea · Hangang Fase 1 | PDF oficial del Banco de Corea (74 páginas, `curl`; URL sacada de la ficha del documento con WebFetch) | Piloto real abr-jun 2025, 7 bancos, hasta 100.000 usuarios, ~81.000 monederos y ~1.640 millones de wones convertidos [P] |
| GAFI · 7.ª actualización | Nota de prensa HTML del GAFI (Chrome; el PDF da 403 a `curl` y Chrome no lo muestra como texto) | 83 % con Travel Rule (73 % en 2025), 11 más en marcha, ~97 % del mercado; stablecoins dominan la actividad ilícita identificada. La cifra de ~40 % de supervisión no aparece [VERIFICAR] |
| China · Notice 42 (银发〔2026〕42号) | Texto íntegro en pbc.gov.cn (Chrome; `curl` no conecta con csrc.gov.cn) | 19 artículos leídos: prohibición de cripto y de RWA salvo aprobación, stablecoins ligadas al RMB sin permiso, bancos sin servicios, minería cerrada, derogación de 银发〔2021〕237号 [P] |

## Japón (verificación del 21-oct, tarde)
| Tema | Fuente leída | Resultado |
|---|---|---|
| RLUSD en Japón | Web de SBI VC Trade (`sbivc.co.jp/rlusd`, WebFetch) y titular de la nota de SBI Holdings del 24-jun-2026; registro de la FSA (PDF, 27-ago-2026); comunicado de Ripple | SBI lo presenta como «la primera stablecoin de 4.º tipo (4号電子決済手段) de Japón» [P de la empresa, parte interesada]; solo Ethereum por ahora (XRPL «previsto»), tope de ¥1 millón por retiro, sin comisiones de depósito y retiro; emisor Standard Custody & Trust (filial de Ripple). El registro de la FSA lista a SBI VC Trade con USDC, RLUSD y JPYSC [P]. **Corrección de mi corrección del 20-oct:** «Type 4» y «solo Ethereum» SÍ constan en fuente de la empresa distribuidora; lo que no consta es una nota de aprobación de la FSA |
| ETF cripto | Documento de debate de la FSA, 10-abr-2025 (PDF, `curl`) | Con las leyes vigentes los criptoactivos no son «activos especificados» de un fondo de inversión y no se pueden constituir ETF cripto (art. 3 del decreto de la ley de fondos) [P, de 2025]. La reforma fiscal de 2026 ya prevé tributación separada para los ETF cripto; no se localizó el decreto ni un anuncio de la JPX o de gestoras [S, VERIFICAR] |
| Fiscalidad (20 %) | Revista Access FSA n.º 270 (PDF dañado en la descarga, vía resumen del buscador) | Hoy cripto: base general, máximo 55 %; valores: 20 % separado; con la reforma, separación «en enero del año siguiente a la entrada en vigor de la FIEA reformada». El 20 % para cripto sigue [S] |
