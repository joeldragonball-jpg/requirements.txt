# C51 · CBDC dentro de blockchains: qué existe y quién puede pagar o recibir

Fecha: 2026-10-29 · Sin recomendaciones de compra/venta · Complementa R40, R08P, dossier del euro digital y R01P (no repite sus detalles).
Método: WebSearch estándar + una lectura directa de la página del BCE sobre Pontes. Casi todo lo demás es resumen de buscador/prensa, no lectura de PDF primario. Los datos que solo vienen de prensa quedan [S] o [VERIFICAR].

## Respuesta corta
- **Sí, hay CBDC mayoristas y dinero de banco central usado sobre registros distribuidos (DLT), pero en redes permisionadas operadas por bancos centrales o consorcios.** No he encontrado ninguna fuente primaria de que una CBDC real haya corrido en una blockchain pública (XRPL, Stellar, Ethereum, Solana).
- **Un particular no puede pagar ni recibir CBDC en una blockchain.** Los casos más sólidos son mayoristas (solo bancos/instituciones con cuenta en el banco central).
- Las noticias mezclan cuatro cosas: (a) CBDC propia, (b) depósitos bancarios tokenizados, (c) stablecoins reguladas, (d) liquidación de activos tokenizados contra reserva del banco central. Casi todo lo «tokenizado» actual es (b), (c) o (d).

## Tabla
Tipos: **a** CBDC en DLT · **b** depósito tokenizado · **c** stablecoin · **d** liquidación contra reserva. Nivel: [P] primaria leída o con enlace oficial · [S] secundaria.

| País / proyecto | Tipo | Tecnología | Quién participa | Estado | Fuente y fecha | Nivel |
|---|---|---|---|---|---|---|
| **Pontes (BCE)** | d (cash tokens / T2 ligado a plataformas DLT) | Enlace entre plataformas DLT de mercado y TARGET/T2; protocolo Hash-Link para DvP. No es una cadena pública | Entidades con acceso a T2; operadores DLT (CSD, CCP, etc.). Primeros operadores citados por prensa: Clearstream, SWIAT, Cashlink, Axiology | **Producción inicial desde 21-sep-2026** (servicios básicos). Volúmenes: no publicados que yo haya visto [VERIFICAR] | Página del BCE sobre Pontes (leída 29-oct-2026); operadores: posttrade360/Ledger Insights | [P] / [S] |
| **Appia (BCE)** | d, a largo plazo | Hoja de ruta | Eurosistema + mercado | Plan/blueprint 2028 | BCE, 11-mar-2026 (según dossier euro digital) | [P] (vía repo) |
| **Project Agorá (BIS + 7 bancos centrales + ~40 bancos)** | b + d (depósitos tokenizados y reservas) | Prototipo: cada banco central en su libro; capa compartida tokenizada | Bancos comerciales y centrales | **Prototipo/pruebas**, informe 27-may-2026; siguiente fase «valor real» con Banco de Canadá. Cifra de ~1 M$ en pruebas = [VERIFICAR] | BIS p260527 (por buscador; bis.org dio ECONNRESET en R08P); Orrick 29-may-2026 | [S] |
| **mBridge (China, HK, Tailandia, EAU, Arabia Saudí)** | a mayorista, transfronterizo | Cadena permisionada propia del consorcio; BIS salió en oct-2024 | Bancos comerciales participantes | **Operativo**; ~55,5 mil M$ acumulados, >4.000 operaciones, ~95 % e-CNY (Atlantic Council, ene-2026). Bank of China dice >600 mil M RMB acumulados a jun-2026 (sin verificar por fuente primaria). Arabia Saudí dice haber terminado su prueba (dossier euro digital) | Atlantic Council vía The Block/Cointelegraph (ene-2026); BoC vía Ledger Insights | [S] |
| **e-CNY (China)** | a minorista | No pública; operadores designados | Particulares y empresas vía bancos/operadores | Producción; paga interés desde 1-ene-2026 | Dossier euro digital (prensa, 2026) | [S] |
| **Helvetia (Suiza)** | a mayorista | SIX Digital Exchange (DLT regulada, infraestructura de mercado) | Bancos miembros de SDX | **Piloto en producción desde finales de 2023**, ampliado a mediados de 2027; el SNB aclara que no es compromiso permanente | SNB, página Helvetia pilot (por buscador) | [P] (snippet) |
| **Singapur: ensayo CBDC mayorista / BLOOM / MAS Bills** | a mayorista + b/c | SGD Testnet; BLOOM para pasivos bancarios tokenizados y stablecoins | DBS, OCBC, UOB | Liquidación en vivo de préstamo interbancario con wCBDC en nov-2025; letras MAS tokenizadas **planificadas 2026**, no confirmo que se hayan ejecutado [VERIFICAR] | MAS (página Tokenised MAS Bill; informe anual 2025-26) | [P] |
| **Hong Kong: Ensemble / EnsembleTX** | b (depósitos tokenizados) + d | Liquidación en HKD RTGS, 24/7 gradual | 7 bancos, 13 participantes | Piloto de valor real desde 13-nov-2025, durante 2026. **e-HKD:** sin información en esta búsqueda [VERIFICAR] | HKMA nota 13-nov-2025; discurso 12-mar-2026 | [P] |
| **Brasil: Drex** | a (originalmente) | Hyperledger Besu (permisionada); **en ago-2025 se aparcó la DLT** y el lanzamiento 2026 sería sin blockchain ni tokenización | Bancos | Proyecto reorientado; si salió algo en 2026 = [VERIFICAR] | Prensa (Jornal Contábil, Finadium, ago-2025) | [S] |
| **EAU: Digital Dirham** | a minorista (dos niveles) | Registro blockchain permisionado (según prensa) | Bancos autorizados + monederos | Piloto desde 11-nov-2025; lanzamiento previsto oct-dic 2026. ¿Ya lanzado? [VERIFICAR] | Prensa (Payments Intelligence, Khaleej Times, mar-2026) | [S] |
| **Rusia: rublo digital** | a minorista | Plataforma del Banco de Rusia (no pública) | Grandes bancos y comercios desde 1-sep-2026; resto 2027-28 | Despliegue masivo por fases, obligado por ley | Interfax/Glenbrook/unchained (ago-sep-2026) | [S] |
| **India e₹** | a | — | — | Sin datos en esta búsqueda | — | [VERIFICAR] |
| **Kazajistán: tenge digital** | a minorista | Piloto con registro tipo blockchain; en oct-2022 anunció pruebas con BNB Chain (pública/permisionada, según Binance) | Bancos de segundo nivel | Piloto con usuarios reales y gasto programable; no he visto que corra la CBDC en BNB Chain en producción | Banco Nacional de Kazajistán (informe piloto); The Block 27-oct-2022 | [S] |
| **Palau (Ripple, XRPL)** | c (stablecoin PSC, no CBDC) | **XRPL (pública)** | ~200 empleados públicos y comercios | Piloto 2023 (lanzado en jul-2023, emisión parada y red congelada en sept según Cointelegraph; fecha exacta [VERIFICAR]). Fue un token respaldado 1:1 por dólares, no moneda soberana | Business Wire/Forkast (jul-2023) | [S] (comunicado de empresa) |
| **Bután, Montenegro, Georgia, Colombia (Ripple)** | exploratorio / CBDC | Plataforma CBDC de Ripple (basada en tecnología XRPL permisionada) | Bancos centrales | Acuerdos y pilotos de 2021-2023; sin estado 2026 verificado [VERIFICAR] | The Block, Kitco, Fintech Futures (2021-2023) | [S] |
| **Ucrania e-hryvnia (Stellar)** | c/e-money | Stellar | TASCOMBANK + Bitt (no el banco central) | Piloto dic-2021; informe ene-2023; el NBU emitiría la e-hryvnia, así que es otro carril | Stellar.org (comunicado), NBU | [S] (promoción) |

## Redes públicas (apartado 3)
- **XRPL:** consta el piloto de Palau (stablecoin del gobierno, no CBDC, 2023, comunicado de Ripple). Para Bután, Montenegro, Georgia y Colombia sólo hay acuerdos/pilotos de plataforma CBDC de Ripple, sin pruebas fechadas de dinero real en el ledger público [VERIFICAR].
- **Stellar:** el piloto de Ucrania fue de un banco comercial con dinero electrónico, no CBDC emitida por el banco central.
- **Ethereum / Solana:** no encontré en esta búsqueda ninguna CBDC de banco central operando ahí [VERIFICAR; no he mirado pruebas del BIS ni Banque de France].
- **XRP o XLM como activo en estos proyectos:** sin fuente que lo diga. En mBridge, Agorá y Pontes no hay XRP ni XLM (ver R40/dossier).

## Qué falta para pagar o recibir CBDC desde una blockchain pública
1. **Política del banco central:** los diseños actuales eligen registros permisionados o plataformas propias; el euro digital no usará cadena pública (según prensa del 2025-26).
2. **KYC/AML y Travel Rule:** en cadenas públicas las direcciones son pseudónimas; haría falta acceso solo a participantes identificados.
3. **Interoperabilidad:** pasarelas seguras entre la CBDC permisionada y la cadena pública (Pontes/Agorá avanzan en eso, pero hacia plataformas de mercado reguladas, no públicas).
4. **Marco legal:** curso legal, responsabilidad ante hackeos, privacidad.
5. **Estándares de «cuenta en banco central»:** hoy las wCBDC son para quienes tienen cuenta en el banco central.

## Caso alcista y bajista para XRPL y Stellar (sin recomendación)
- **Alcista:** el interés de los bancos centrales en la tokenización (Pontes, Agorá, Hong Kong) abre la puerta a que cadenas con funciones de cumplimiento participen como capa de mercado; Ripple y SDF tienen antecedentes de trabajo con bancos centrales.
- **Bajista:** los casos sólidos y con volumen (mBridge, Pontes, Helvetia) no usan ni XRPL ni Stellar ni sus tokens; los proyectos con XRPL/Stellar son pilotos pequeños, antiguos o de stablecoin; incluso con CBDC en cadena, la liquidación no requiere XRP/XLM.
- **Sesgos de las fuentes:** comunicados de Ripple y Stellar (promoción), agregadores cripto que repiten la cifra de 55 mil M$ de mBridge, titulares de «10 acuerdos CBDC» sin datos de uso, y artículos que confunden depósitos tokenizados con CBDC.

## [VERIFICAR] pendiente
Estado real de Pontes (volúmenes), cifras de mBridge con fuente primaria, Drex y Digital Dirham en 2026, e-HKD, India e₹, y pruebas BIS/bancos centrales en Ethereum/Solana/otras públicas. Los PDFs del BIS no se pudieron abrir (ECONNRESET en R08P).
