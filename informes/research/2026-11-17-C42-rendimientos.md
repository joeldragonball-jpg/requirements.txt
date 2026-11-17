---
titulo: C42 Rendimientos y colateral — cierre de huecos (Japón, Corea, Emiratos, UK, EE. UU.)
fecha: 2026-11-17
etiquetas: [rendimientos, colateral, staking, lending, xrpl, regulacion, rwa]
---
# C42 · Cierre de huecos (17-nov-2026)

Continúa `2026-11-02`, `11-11`, `11-11-C42b`, `11-12-lote-B2` y `11-16-C280-C42`. Informativo; no dice dónde operar ni qué contratar. Las plataformas y emisores que anuncian rendimientos son parte interesada. Nivel: **P** = fuente primaria leída; **S** = prensa/despacho/agregador. «P*» = la leyó un subagente por WebFetch/pdftotext y yo no la he recotejado: tratar como P provisional hasta verlo en Chrome. Lo no leído, [VERIFICAR]. Predicciones: [ESPECULACIÓN].

## 1. Hechos nuevos
**XRPL lending (XLS-66/65) — leído por mí hoy.** API pública de XRPScan (`api.xrpscan.com/api/v1/amendments`, 17-nov-2026) [S, tercero sobre datos del ledger]: `LendingProtocol` enabled=false, 22 apoyos de 35 validaciones (umbral 28; ≈63 %); `SingleAssetVault` enabled=false, 23 de 35 (≈66 %); aparece `LendingProtocolV1_1` (rippled 3.4.0), enabled=false, 22. **No están activos en mainnet.** El 80 % se exige durante 2 semanas [P, xrpl.org]. Que alcancen o no el umbral es [ESPECULACIÓN].

**Reino Unido [P*].** FCA PS26/11 (jun-2026): vigencia 25-oct-2027; ventana de solicitud 30-sep-2026 a 28-feb-2027. Lending/borrowing minorista permitido con protecciones: información previa, consentimiento expreso, test de idoneidad, sobrecolateralización y protección de saldo negativo. Staking minorista: información, consentimiento; el consentimiento puede cubrir auto-staking futuro con aviso anual. PS26/18 (sep-2026, perímetro) solo vista en un despacho [S]. https://www.fca.org.uk/publication/policy/ps26-11.pdf

**Emiratos.** VARA Dubái [P*]: el staking va dentro del rulebook de custodia, solo con autorización explícita en la licencia y tras instrucción específica del cliente; wallets segregadas, declaración de riesgos aparte. Rulebook de lending/borrowing vigente desde 19-jun-2025 (solo leí portada y versión; contenido y reglas minoristas [VERIFICAR]). ADGM: marco de staking final 29-abr-2026 (comunicado [P*], reglas completas no abiertas); sin marco específico de lending a feb-2026 [S]. CBUAE/SCA: sin dato.

**Japón [S].** Reforma FIEA/Ley de Pagos: aprobada en la Dieta 15-jul-2026, promulgada 23-jul-2026, vigencia en ≤1 año de la promulgación (fecha exacta [VERIFICAR]). Tomar prestado cripto como negocio entra en la actividad de intercambio con régimen simplificado; staking solo aparece de pasada (recompensa y uso de información privilegiada); staking/DeFi como servicio, normas secundarias de la FSA 2026-27 (prensa). El PDF de la FSA estaba cifrado: no leído. https://www.businesslawyers.jp/articles/1568

**Corea [S].** Sin fuente primaria sobre staking/lending. VAUPA (en vigor 19-jul-2024): staking no prohibido pero el proveedor debe poseer los activos (Chambers 2026). Guía de préstamo cripto de los reguladores (TF creado jul-2025); límites y tasa máx. del 20 % solo en un agregador sin fecha [VERIFICAR]. Digital Asset Basic Act aún en trámite a 2-nov-2026. Un comunicado FSC del 11-ago-2026 [P*] trata VASP/travel rule y no menciona staking ni lending.

**EE. UU.** GENIUS Act (S.1582, texto enrolado en govinfo, lectura parcial [P*]): sec. 4(a)(11) prohíbe al **emisor** de stablecoin de pago pagar «interés o rendimiento» por tenerla; exchanges/afiliados, zona gris [S]. CLARITY [S]: compromiso de mayo-2026 prohíbe recompensas equivalentes a interés por mero saldo y permite las ligadas a actividad; la moción de proceder en el Senado falló 49-50 el 15-sep-2026 (American Banker, ABA); sin dato posterior [VERIFICAR]. SEC/CFTC sobre lending/earn: sin fuente.

**Colateral tokenizado.** CFTC «Tokenized Collateral and Stablecoins», 23-sep-2025, consulta hasta 20-oct-2025 [P*] (cftc.gov/PressRoom/PressReleases/9130-25). Piloto de 8-dic-2025: FCM pueden aceptar BTC, ETH y USDC como margen [S, Willkie]. BUIDL aceptado como colateral en Binance, Deribit y Crypto.com [S, un blog] [VERIFICAR con las plataformas]. Fed/BCE/BoE: sin dato. 

**Letras tokenizadas.** app.rwa.xyz/treasuries, 17-nov-2026: ≈14,20 mil M$ distribuidos, APY 7 días ≈3,52 % [S, extracción resumida, [VERIFICAR] en Chrome]. Tasa BUIDL actual: sin dato (Securitize 404). Contraste: DefiLlama 16-nov, OUSG 3,44 % y USDY 3,75 % [S].

## 2. Caso alcista / bajista
- Alcista: el Reino Unido, ADGM y Hong Kong fijan reglas de conducta en vez de prohibir; el colateral tokenizado ya tiene piloto de la CFTC; las letras tokenizadas superan 14 mil M$.
- Bajista: Japón y Corea sin norma primaria sobre lending/staking; CLARITY bloqueada en el Senado; XLS-66 lleva 10 meses sin 80 %; las tasas son de partes interesadas y fluctúan.

## 3. Filas propuestas (NO volcadas; el panel espera tu OK)
```json
[
{"modalidad":"Lending nativo + vaults","activo":"XRP","jurisdiccion":"Global (XRPL)","estado":"No activo: 22/35 y 23/35 apoyos (umbral 28)","norma":"XLS-66 / XLS-65","fecha":"2026-11-17","fuente":"XRPScan API","url":"https://api.xrpscan.com/api/v1/amendments","nivel":"S","riesgo":"retraso, contrato","revisar":"2026-12-01"},
{"modalidad":"Staking/lending minorista","activo":"Cripto","jurisdiccion":"Reino Unido","estado":"Permitido con protecciones; vigencia 25-10-2027","norma":"FCA PS26/11","fecha":"2026-06-30","fuente":"fca.org.uk","url":"https://www.fca.org.uk/publication/policy/ps26-11.pdf","nivel":"P*","riesgo":"aún no vigente","revisar":"2027-01-15"},
{"modalidad":"Staking custodial","activo":"VA","jurisdiccion":"Dubái (VARA)","estado":"Solo con autorización explícita en licencia","norma":"Custody Services Rulebook, Parte IV","fecha":"2025-05-19","fuente":"rulebooks.vara.ae","url":"https://rulebooks.vara.ae/entiresection/361","nivel":"P*","riesgo":"custodia","revisar":"2027-02-01"},
{"modalidad":"Lending/borrowing","activo":"VA","jurisdiccion":"Dubái (VARA)","estado":"Actividad con licencia; reglas minoristas sin leer","norma":"Lending and Borrowing Services Rulebook","fecha":"2025-06-19","fuente":"rulebooks.vara.ae","url":"https://rulebooks.vara.ae/rulebook/lending-and-borrowing-services-rulebook","nivel":"VERIFICAR","riesgo":"contraparte","revisar":"2026-12-15"},
{"modalidad":"Lending/staking","activo":"Cripto","jurisdiccion":"Japón","estado":"Ley FIEA promulgada; sin régimen específico de staking; reglamento 2026-27","norma":"Reforma FIEA/Pagos","fecha":"2026-07-23","fuente":"businesslawyers.jp (bufete)","url":"https://www.businesslawyers.jp/articles/1568","nivel":"S","riesgo":"reglamento pendiente","revisar":"2027-01-15"},
{"modalidad":"Staking/lending","activo":"VA","jurisdiccion":"Corea","estado":"Sin ley marco; staking propio permitido; guía de préstamo [VERIFICAR]","norma":"VAUPA 2024; Digital Asset Basic Act en trámite","fecha":"2026-11-02","fuente":"Chambers 2026; prensa","url":"https://chambers.com/practice-guides/guides/fintech-2026/south-korea/trends-and-developments","nivel":"S","riesgo":"vacío normativo","revisar":"2026-12-15"},
{"modalidad":"Rendimiento de stablecoins","activo":"Stablecoin","jurisdiccion":"EE. UU.","estado":"El emisor no puede pagar interés; CLARITY sin aprobar (49-50, 15-sep-2026)","norma":"GENIUS Act s.4(a)(11)","fecha":"2025-07-18","fuente":"govinfo.gov","url":"https://www.govinfo.gov/content/pkg/BILLS-119s1582enr/html/BILLS-119s1582enr.htm","nivel":"P*","riesgo":"zona gris de afiliados","revisar":"2026-12-15"},
{"modalidad":"Colateral tokenizado","activo":"Tesoro tokenizado, BTC, ETH, USDC","jurisdiccion":"EE. UU.","estado":"Consulta CFTC (sep-2025) y piloto de margen (dic-2025)","norma":"CFTC PR 9130-25","fecha":"2025-09-23","fuente":"cftc.gov","url":"https://www.cftc.gov/PressRoom/PressReleases/9130-25","nivel":"P*","riesgo":"operativo y legal","revisar":"2027-01-15"},
{"modalidad":"Letras tokenizadas","activo":"Fondos del Tesoro","jurisdiccion":"Global","estado":"≈14,20 mil M$; APY 7d ≈3,52 %","norma":"","fecha":"2026-11-17","fuente":"app.rwa.xyz","url":"https://app.rwa.xyz/treasuries","nivel":"S","riesgo":"emisor, liquidez, acceso","revisar":"2026-11-24"}
]
```

## 4. Cerrado y abierto
Cerrado: estado de XLS-66 hoy; UK con PS y fechas; VARA staking; GENIUS/CLARITY; CFTC colateral; cifra rwa.xyz del día. Abierto: FSA (PDF cifrado), guía coreana de préstamo, contenido del rulebook de lending de VARA, CBUAE/SCA, SEC/CFTC sobre earn, tasa de BUIDL, aceptación de colateral por plataformas, Fed/BCE/BoE, y recotejar los «P*» en Chrome.
