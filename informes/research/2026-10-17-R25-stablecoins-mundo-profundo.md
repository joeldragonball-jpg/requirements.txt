# Stablecoins en el mundo: tamaño, regulación y qué cambia (2026-10-17, R25 profundo)

Plantilla: dossier-region (modo profundo). Etiquetas: **LEÍDO ENTERO** = documento primario leído completo o la parte relevante descargada; **API** = dato en vivo de un agregador (tercero, no auditado); **extracto** = solo lo que devuelve un buscador/resumen; **secundaria** = prensa o blog, sin primario [VERIFICAR]. Sin recomendaciones de compra/venta.

## Resumen
1. Según DefiLlama (agregador, 17-oct-2026) las stablecoins ligadas al dólar suman **~306 mil M$**; USDT (~183 mil M$) y USDC (~73 mil M$) son ~84 % del total. Más de la mitad corre sobre Ethereum (~144 mil M$) y Tron (~94 mil M$). XRPL tiene ~1.108 M$ y Stellar ~520 M$ (<1 % del total cada una).
2. En EE. UU. la GENIUS Act (firmada 18-jul-2025) aún no está en vigor: efectiva **~18-ene-2027**; desde **18-jul-2028** los intermediarios no podrán ofrecer stablecoins de emisores no autorizados. Treasury propuso la norma de emisión el 18-ago-2026; los comentarios **cierran el 19-oct-2026**.
3. La UE ya tiene un régimen en vigor (MiCA): el registro de ESMA lista **25 emisores de EMT** y **0 emisores de ART**; Tether (USDT) no figura. La polémica abierta es la "multi-emisión" (misma moneda emitida por entidad UE y de fuera): sin decisión formal de la Comisión [VERIFICAR].
4. Asia: Hong Kong ya licenció (HSBC y Anchorpoint, 10-abr-2026, ambos leídos en el registro de la HKMA); Singapur está en consulta (R24); Corea sigue en disputa entre bancos y fintech [secundaria]. Brasil trata las stablecoins como operación de cambio (Res. BCB 561/2026) [secundaria]. India: el RBI es hostil y el Gobierno estudia un marco distinto [secundaria].
5. Lo que más pesa: el tamaño del mercado es en dólares y casi todo USDT/USDC; las monedas locales son marginales (EURC ~500 M€, JPYC ~21 M, XSGD ~13 M según DefiLlama). XRP/XLM solo se tocan donde hay dato (RLUSD/USDC en sus cadenas).

## Qué es hecho verificado
| Dato | Fuente | Fecha | Nivel / idioma |
|---|---|---|---|
| Stablecoins ligadas a USD: ~306,2 mil M$ en 423 activos | DefiLlama API `stablecoins.llama.fi/stablecoins` | 17-oct-2026 | API (tercero), inglés |
| USDT 183,45 mil M$ (semana ant. 184,28; mes ant. 183,24); USDC 72,76 (73,25; 73,66); USDS 7,05; DAI 4,72; USDe 4,70; USD1 4,07; USDG 3,02; PYUSD 2,83; RLUSD 2,43; BUIDL 2,17 | idem | 17-oct-2026 | API |
| Por cadena (USD): Ethereum 143,9 · Tron 94,5 · Solana 15,7 · BSC 13,1 · Hyperliquid L1 7,0 · Base 5,2 · XRPL 1,11 · (Stellar 0,52) mil M$ | DefiLlama `/stablecoinchains` | 17-oct-2026 | API |
| RLUSD: 2.433 M$ (Ethereum 1.404 M$; XRPL 1.030 M$). USDC en XRPL ≈ 5 M$; USDC en Stellar ≈ 494 M$ | DefiLlama (`chainCirculating`) | 17-oct-2026 | API |
| Monedas no-USD: EURC ≈ 500,5 M€; EUR total ≈ 0,84 mil M€ (EURCV 189 M, EURI 37 M, EURE 32 M); JPYC ≈ 21 M; XSGD ≈ 13 M; GYEN ≈ 6 M; AUDD ≈ 7 M; HKDAP ≈ 0,8 M | idem | 17-oct-2026 | API; unidades en moneda local, sin convertir |
| Tether, 30-jun-2026: activos 187,75 mil M$, pasivos 183,64 mil M$ (BDO); exceso de reservas 4,11 mil M$ frente a 8,23 mil M$ en 1T; beneficio operativo ~1,5 mil M$ | Forklog, Cryptobriefing, StablecoinInsider (informe de atestación de BDO) | 2T-2026 | **secundaria** [VERIFICAR]; no he leído la atestación; tether.io/news no mostró el dato |
| GENIUS Act: Ley Pública 119-27, promulgada 18-jul-2025; "payment stablecoin" excluye depósitos y valores | Treasury NPRM, Federal Register 2026-16796 (91 FR 53368-53391) | 18-ago-2026 | **LEÍDO ENTERO** las secciones I y de fechas/emisores extranjeros (193 KB descargados con curl); inglés |
| Fecha efectiva de la ley "prevista" **18-ene-2027** (18 meses tras la promulgación) | idem, nota 10 | 18-ago-2026 | LEÍDO |
| Desde **18-jul-2028** es ilegal que un proveedor de servicios de activos digitales (DASP) ofrezca/venda en EE. UU. una stablecoin no emitida por un emisor permitido (sec. 3(b)(1)) | idem | 18-ago-2026 | LEÍDO |
| Sec. 3(b)(2), aplicable desde la fecha efectiva: un DASP no puede ofrecer stablecoins de emisor extranjero salvo que éste tenga capacidad técnica de cumplir órdenes legales y acuerdos de reciprocidad (sec. 18) | idem | 18-ago-2026 | LEÍDO |
| Excepción de emisor extranjero (sec. 18): régimen extranjero que Treasury declare "comparable" + registro en la OCC | idem | 18-ago-2026 | LEÍDO |
| Exentas de la sec. 3: transferencias directas entre dos personas sin intermediario, cuentas propias del mismo grupo, y uso de wallet propia (self-custody) | idem, sec. 3(h) | 18-ago-2026 | LEÍDO |
| Plazo de comentarios de esa norma: **19-oct-2026** | idem | 18-ago-2026 | LEÍDO |
| Otros documentos del Federal Register sobre GENIUS (solo títulos y fechas): Fed "Implementing the Federal Reserve Board's Responsibilities" (29-sep); Fed solicitud de filiales de bancos asegurados (29-sep); "Stablecoin Certification Review Committee" formularios (30-sep); FDIC formularios de reporte (20-jul); OCC/Fed/FDIC solicitudes de licencia (27-jul); AML/CFT (9-jul) | Federal Register API | jul–sep-2026 | extracto (título+fecha); texto no leído |
| Hong Kong: Ordenanza de Stablecoins (Cap. 656) en vigor 1-ago-2025; primeras dos licencias el **10-abr-2026**: Anchorpoint Financial Ltd (FRS01) y HSBC (FRS02) | HKMA, registro y comunicado 20260410-4 | registro revisado 23-abr-2026 | **LEÍDO** (registro y comunicado, vía WebFetch); inglés |
| UE: registro de ESMA (`CASPS`-serie, fichero `EMTWP.csv`): 50 filas / **25 emisores de EMT** distintos (NL 10 filas, FR 8, DE 6, LU 5, MT 4, FI 4...); entre ellos Circle Internet Financial Europe SAS (FR, 1-jul-2024), Paxos Issuance Europe (FI), Société Générale-Forge (FR), AllUnity GmbH (DE, 20-jun-2026), Monerium (IS), StablR (MT), Banking Circle (LU); `ARTZZ.csv` (tokens referenciados a activos) **vacío** | ESMA interim MiCA register | descargado 17-oct-2026 | **LEÍDO ENTERO** (CSV con curl); Tether no aparece |
| Consulta MAS P015-2026 (stablecoins, Payment Services Act): sin mención a XRP/XLM/Ripple | ver R24 | 16-oct-2026 cierre | LEÍDO ENTERO en R24 |

Nota de método: las cifras de DefiLlama son de un agregador gratuito; "circulating" de monedas no-USD viene en unidades de esa moneda y para A7A5 (rublo) la unidad es ambigua (556,7 M "peggedRUB", pero Tron lista 549,8 M en esa categoría) → **[VERIFICAR]** antes de citar un valor en dólares.

## Qué está sin verificar o es opinión
- **Tether 2T-2026** (cifras de arriba): solo prensa especializada; una fuente dice que Tether encargó en mar-2026 una auditoría completa a una "Big Four" aún no entregada (una sola fuente) [VERIFICAR]. La atestación de BDO no es una auditoría.
- **Brasil** [secundaria]: la Res. BCB 561/2026 exigiría que la liquidación eFX con el exterior sea solo por operación de cambio o cuenta de no residente en reales, sin activos virtuales como "rail" (publicada 30-abr; vigente 1-oct, según un blog y Conjur). Las fuentes discrepan en fechas (2-feb vs mayo) y un IOF del 3,5 % solo lo cita una fuente. Ya cubierto en R03P (el sitio del BCB no se abre).
- **India** [secundaria]: informes de mayo-junio 2026 dicen que el RBI podría prohibir a bancos tener cripto y stablecoins privadas; el gobernador defiende CBDC; el Gobierno estudia un marco que podría divergir del RBI. Sin documento oficial leído. Ya cubierto en R02P.
- **Corea** [secundaria, sin fecha de oct-2026]: pugna BoK (consorcios con 51 % bancario) frente a FSC/fintech; capital mínimo 500 M KRW citado por una fuente. Ver R05P.
- **UE, multi-emisión** [secundaria]: Parlamento Europeo aprobó un informe de iniciativa propia no vinculante (390–86) a favor con garantías; BCE y EBA alertan de riesgos; la Comisión reconocería en su consulta (cerró a fin de sept-2026) que la multi-emisión está permitida, pero **no hay guía formal confirmada** [VERIFICAR]. Circle presiona a favor (parte interesada).
- **Sesgos**: DefiLlama y la mayoría de blogs viven de tráfico cripto; Tether, Circle y Ripple (RLUSD) son partes interesadas con incentivo a presentar el tamaño al alza; USD1 (World Liberty Financial) tiene un posible conflicto político-comercial que aquí no he verificado en primario [VERIFICAR]; kucoin.com y blogs de "explainers" repiten notas de prensa.

## Caso alcista / caso bajista (sobre el sector de stablecoins, sin pronóstico)
- **Alcista**: marcos legales ya en vigor (MiCA, HK) o con fecha (GENIUS 18-ene-2027); crecimiento de nuevos emisores regulados (25 EMT en la UE; 2 licencias HK; RLUSD >2.400 M$ y BUIDL/USDG entre los 10 mayores); los bancos pueden emitir (filiales de bancos asegurados, solicitudes a la Fed).
- **Bajista**: concentración (USDT+USDC ≈ 84 %); el suministro de USDT y USDC bajó algo en el último mes según DefiLlama (USDC 73,66 → 72,76 mil M$; BUIDL 2,68 → 2,17 mil M$); reservas de Tether con colchón recortado a la mitad en 2T y con oro/BTC en el balance [secundaria]; incertidumbre regulatoria (multi-emisión UE; condición de "comparabilidad" para emisores extranjeros en EE. UU.); India y Brasil restringen; los bancos centrales prefieren CBDC (BIS/RBI).

## Qué cambia para los digital assets (XRP, XLM, stablecoins, CBDC, tokenización)
- **GENIUS** no regula XRP ni XLM: regula stablecoins de pago. Los efectos son indirectos: un emisor no permitido (o extranjero sin comparabilidad/OCC) no podrá ser ofrecido por exchanges de EE. UU. desde 2028; entre ahora y 2028 el filtro es la sec. 3(b)(2) (capacidad de cumplir órdenes). Habrá que ver si RLUSD (emisor: entidad de Ripple) y USDC (Circle) cumplen como emisores permitidos; no he leído ninguna aprobación [VERIFICAR].
- **Datos verificables en las cadenas** (API): XRPL ≈ 1.108 M$ de stablecoins, casi todo RLUSD (≈1.030 M$); Stellar ≈ 520 M$, casi todo USDC (≈494 M$). Son <1 % del total mundial. Esto es un hecho de oferta de stablecoins en esas cadenas, no una señal de precio de XRP/XLM; el uso real (volúmenes) no está medido aquí.
- **MiCA**: Circle (FR) y otros EMT ya autorizados; Ripple Payments Europe (LU) aparece como CASP (R19), no como emisor de EMT en este CSV [dato de la lista leída: RLUSD no aparece en EMTWP; VERIFICAR si tiene whitepaper aparte].
- **HK/Singapur**: licencias y reglas sobre reservas, redención en 1 día hábil (HK, según resumen de buscador) y reconocimiento de stablecoins extranjeras (SG, R24) condicionan dónde pueden operar RLUSD/USDC.
- **Monedas locales** apenas existen en volumen: la narrativa de "stablecoins en moneda local" por ahora es pequeña frente al dólar.

## Fechas próximas (catalizadores) con fuente
| Fecha | Evento | Fuente |
|---|---|---|
| **19-oct-2026** | Cierre de comentarios a la norma de emisión de GENIUS (Treasury) | Federal Register 2026-16796, leído |
| ~4Q-2026 / 1T-2027 | Normas finales de GENIUS (no hay calendario oficial leído) [VERIFICAR] | — |
| **18-ene-2027** (prevista) | Fecha efectiva de la GENIUS Act | NPRM, nota 10 |
| **18-jul-2028** | Prohibición a DASP de ofrecer stablecoins no permitidas | NPRM, sec. 3(b)(1) |
| Pendiente | Decisión de la Comisión sobre multi-emisión MiCA y revisión de MiCA (2027) | prensa [VERIFICAR] |
| Pendiente | Lanzamientos HKD de HSBC y Anchorpoint ("en los próximos meses" desde abril) | HKMA, comunicado 10-abr |
| Pendiente | Conclusiones de la consulta MAS P015-2026 | MAS (R24) |
| ~nov-2026 | Atestación de Tether 3T / informe mensual de reservas de Circle | emisores [VERIFICAR] |

## Qué falta por buscar
1. Leer la atestación de Tether (BDO) y el informe de reservas de Circle (la página `circle.com/transparency` carga por JS: el desglose no se pudo extraer con curl; hace falta PDF o captura).
2. Texto de la Res. BCB 561/2026 y de las 519-521 (BCB no abre) → PDF a `research/fuentes/`.
3. Documento del RBI (circular) y del Ministerio de Finanzas sobre stablecoins; texto del proyecto coreano.
4. Leer los NPRM de la Fed (29-sep) y de la OCC/FDIC para el calendario de la fecha efectiva; ver si RLUSD/Ripple solicitó licencia federal.
5. Aclarar la unidad de A7A5 y de otras stablecoins no-USD (convertir a dólares).
6. Guía final de la Comisión Europea sobre multi-emisión.
