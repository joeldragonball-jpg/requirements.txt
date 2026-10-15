# Comparativa de plataformas y custodia (2026-10-15, R19)

Alcance: ¿Quién guarda tus XRP/XLM y con qué garantías legales? Informe de hechos y criterios, **sin recomendar ninguna plataforma** (decides tú). Foco global/UE; la fiscalidad, el registro CNMV y el acceso desde España quedan para R20.
Etiquetas: **LEÍDO ENTERO** (documento completo abierto) / **EXTRACTO** (parte del documento, o resumido por la herramienta de lectura) / **SECUND.** (prensa o buscador, sin abrir el primario).

## Resumen (5 líneas)
1. En la UE, desde el 1-jul-2026 solo pueden servir a clientes los proveedores con licencia MiCA; ESMA avisa de que la protección es **de la entidad legal concreta**, no del grupo ni de la marca (LEÍDO ENTERO).
2. El registro oficial de ESMA (CSV descargado hoy, 365 entidades, última alta real 6-oct-2026) incluye a Kraken, Coinbase, Bitstamp, Bitvavo, Bitpanda, Crypto.com, OKX, Bybit, Gemini, Revolut, BitGo y Ripple Payments Europe; **no aparecen Binance ni Bitget** (LEÍDO ENTERO).
3. Los ETF spot de XRP no te dan XRP: te dan acciones de un fideicomiso cuyo XRP guardan Coinbase Custody (Bitwise) o Gemini+BitGo (Canary); no hay seguro FDIC y parte puede estar en una cuenta omnibus (EXTRACTO de prospectos SEC).
4. La auto-custodia elimina el riesgo de plataforma pero añade otros: el 9-oct-2026 Ledger investiga pérdidas (72–86 M$ estimados por analistas, no confirmados) ligadas a un revendedor del sudeste asiático; la causa sigue sin confirmar (SECUND.).
5. Un punto específico de XRP/XLM: ambas redes exigen una reserva mínima en la cuenta propia (1 XRP + 0,2 por objeto; 1 XLM + 0,5 por subentrada), y sus transacciones son irreversibles (LEÍDO, docs oficiales).

## Qué es hecho verificado

### A. Marco legal UE (MiCA)
| Dato | Fuente | Fecha | Etiqueta |
|---|---|---|---|
| El periodo transitorio MiCA termina el 1-jul-2026 en toda la UE; quien preste servicios cripto a clientes UE sin licencia incumple la ley y debe cesar. "any entity providing crypto-asset services to EU clients without a MiCA licence will be in breach of EU law" | [ESMA75-113276571-1679](https://www.esma.europa.eu/sites/default/files/2026-04/ESMA75-113276571-1679_Statement_on_the_end_of_transitional_periods_under_MiCA.pdf) | 17-abr-2026 | LEÍDO ENTERO (3 págs., inglés) |
| Aviso a consumidores: comprobar al proveedor en el registro provisional; "MiCA protections only apply to the specific authorised legal entity in the EU – not to other companies of the same group, and not to non-EU entities" (Las protecciones solo valen para la entidad concreta autorizada, no para otras del grupo ni fuera de la UE). Ojo: misma marca puede operar con varias sociedades | ídem | 17-abr-2026 | LEÍDO ENTERO |
| Entidades de fuera de la UE no pueden prestar servicios MiCA a inversores UE (salvo "reverse solicitation") ni siquiera B2B; los CASP no pueden externalizar la **custodia** en entidades no autorizadas como CASP | ídem | 17-abr-2026 | LEÍDO ENTERO |
| Si tu proveedor no está autorizado: "transfer your crypto assets to an authorised provider or a self-hosted wallet, or consider closing your positions" | ídem | 17-abr-2026 | LEÍDO ENTERO |

### B. Registro provisional MiCA de ESMA (fichero de CASP autorizados)
Descargado hoy con curl: `https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv` (370 filas, 365 LEI distintos; última actualización con fecha plausible 6-oct-2026; una fila lleva fecha 11-sep-2028 = error de dato del registro). **LEÍDO ENTERO** (CSV, inglés). Selección de plataformas conocidas (autorización notificada | país | entidad):

| Plataforma | Entidad legal en el registro | País | Autorización | Servicios clave listados |
|---|---|---|---|---|
| Kraken | Payward Global Solutions Ltd (plataforma de negociación) y Payward Europe Solutions Ltd (custodia, cambio, órdenes, transferencias, gestión de cartera) | IE | 25-jun-2025 | dos sociedades con funciones distintas |
| Coinbase | Coinbase Luxembourg S.A. | LU | 20-jun-2025 | custodia, cambio, órdenes, colocación, transferencias |
| Bitstamp | Bitstamp Europe S.A. | LU | 15-may-2025 | custodia, plataforma, cambio, órdenes, transferencias |
| Bitvavo | Bitvavo B.V. | NL | 26-jun-2025 | custodia, plataforma, transferencias |
| Bitpanda | Bitpanda GmbH (AT), Bitpanda Asset Management (DE), BP23 CA Ltd (MT) | AT/DE/MT | 27-ene-2025 a 9-abr-2025 | tres sociedades |
| Crypto.com | Foris DAX MT Ltd | MT | 27-ene-2025 | |
| OKX | OKX Europe Ltd | MT | 27-ene-2025 | |
| Bybit | Bybit EU GmbH | AT | 28-may-2025 | |
| Gemini | Gemini Intergalactic EU Ltd | MT | 21-ago-2025 | custodia, cambio, órdenes, transferencias |
| Revolut | Revolut Digital Assets (Europe) Ltd | CY | 20-oct-2025 | |
| Robinhood | Robinhood Europe UAB | LT | 29-may-2025 | |
| BitGo | BitGo Europe GmbH | DE | 9-may-2025 | custodia, cambio, órdenes, transferencias |
| Ripple | Ripple Payments Europe S.A. | LU | 29-jun-2026 (actualizado 7-jul-2026) | cambio cripto-fiat, cambio cripto-cripto, transferencias; **sin custodia** |
| KuCoin | KuCoin EU Exchange GmbH | AT | 27-nov-2025 | |

- **No aparecen** en el fichero (0 coincidencias para Binance, Bitget, Bitso, Uphold, Ledger, Anchorage, Stellar). "No aparece" no equivale a "prohibido": puede haber otra entidad con otro nombre o un fichero de no conformes aparte (no localizado).
- Coherencia con apunte previo: la nota de prensa de Ripple dice 6-jul-2026 (R09P); el registro da 29-jun-2026 como fecha de notificación y 7-jul como última actualización. Son fechas distintas del mismo hecho (la licencia existe).
- En el registro figura también una veintena de entidades españolas (bancos y fintech); su análisis queda para R20.

### C. Custodia de los ETF spot de XRP (EE. UU.)
| Dato | Fuente | Fecha | Etiqueta |
|---|---|---|---|
| **Bitwise XRP ETF**: el custodio es Coinbase Custody Trust Company, LLC (fiduciaria bajo la ley bancaria de Nueva York, "not insured by the FDIC"). Cuentas segregadas del patrimonio propio del custodio. Efectivo: BNY Mellon. Comisión **0,34 %** anual. Sin staking ni rendimiento sobre el XRP | [424B3](https://www.sec.gov/Archives/edgar/data/0002039525/000121390026104143/ea0306697-424b3_bitwisexrp.htm) | 28-sep-2026 | EXTRACTO (primeros 100.000 de ~625.000 caracteres; resumido por herramienta) |
| Bitwise: una parte puede estar en un **"Trading Balance"** con Coinbase Inc. (Prime Execution Agent) donde el fondo "does not have an identifiable claim to any particular XRP" (reparto proporcional de un saldo común); además el XRP "may be subject to a lien" por líneas de crédito con Coinbase Credit, Inc. | ídem | 28-sep-2026 | EXTRACTO |
| Bitwise: el seguro es una póliza de crimen de la matriz Coinbase Global; "does not cover, insure or guarantee the performance of the Trust" | ídem | 28-sep-2026 | EXTRACTO |
| **Canary XRP ETF**: custodios Gemini Trust Company y BitGo Trust Company; efectivo U.S. Bank; comisión unificada **0,50 %**; "A majority of the XRP… will be held in offline (cold) storage" (porcentaje no publicado); el patrocinador puede cambiar el reparto entre custodios "at any time and without notice"; custodios no asegurados por FDIC | [424B3](https://www.sec.gov/Archives/edgar/data/2039505/000199937125017549/canaryxrp-424b3_111225.htm) | 12-nov-2025 (puede estar desactualizado) | EXTRACTO (100.000 de ~535.000 caracteres) |
| **21Shares (TOXR)**: Coinbase Custody, Anchorage Digital Bank y BitGo Trust como custodios | [The Block](https://www.theblock.co/amp/post/382224/new-xrp-etf-hits-the-market-with-launch-of-21shares-toxr) / buscador | 2025 | SECUND. [VERIFICAR] en el prospecto vigente |
| Coinbase Custody aparece como custodio y Coinbase Inc. como prime broker de varios ETF de XRP rivales: el propio prospecto lo marca como riesgo de concentración | Bitwise 424B3 / buscador sobre el 10-K 2025 | 2026 | EXTRACTO |

No hay ETF spot de Stellar cotizando en EE. UU. confirmado (R21).

### D. Reglas de las redes (afectan a cualquier custodia)
| Dato | Fuente | Fecha de consulta | Etiqueta |
|---|---|---|---|
| XRPL: reserva base **1 XRP** por cuenta y **0,2 XRP** por cada objeto que posea (trust lines, ofertas…) | [xrpl.org – Reserves](https://xrpl.org/docs/concepts/accounts/reserves) | 15-oct-2026 | LEÍDO (página, vía herramienta; no incluía el coste de borrar cuenta) |
| Stellar: reserva base **0,5 XLM**; mínimo para existir 2 reservas = **1 XLM**; +0,5 XLM por trustline, oferta, firmante o dato | [developers.stellar.org](https://developers.stellar.org/docs/learn/fundamentals/lumens) | 15-oct-2026 | LEÍDO (página, vía herramienta) |
| Trezor tiene un centro dedicado a XRP/XLM con artículos sobre destination tags/memos al enviar | [trezor.io](https://trezor.io/learn/supported-assets/xrp-xlm) | 15-oct-2026 | LEÍDO solo el índice (sin advertencias concretas) |

### E. Estado de la regulación de custodia en EE. UU.
- SEC SAB 122 rescindió SAB 121 (obligaba a registrar un pasivo por salvaguarda de cripto): [sec.gov](https://www.sec.gov/rules-regulations/staff-guidance/staff-accounting-bulletins/staff-accounting-bulletin-122) | enero 2025 (la fecha exacta varía entre fuentes: 23 o 30-ene) | EXTRACTO de buscador.
- OCC: aprobación **condicional** (no final) de cartas de banco fiduciario nacional el 12-dic-2025 para BitGo, Fidelity Digital Assets, Ripple National Trust Bank, First National Digital Currency Bank (Circle) y Paxos; más Crypto.com y otras en 2026; Coinbase solicitó en oct-2025 sin decisión localizada | [Baird Holm](https://www.bairdholm.com/blog/occ-approves-trust-charters-for-five-crypto-firms/), [ICBA](https://www.independentbanker.org/w/occ-approves-icba-opposed-national-trust-charter-applications) | SECUND. [VERIFICAR en occ.gov].

## Qué está sin verificar o es opinión
- **Binance en la UE** [VERIFICAR]: según prensa (Reuters vía The Block/FT, junio-2026) retiró su solicitud en Grecia el 24-jun-2026 y dijo que seguirá buscando licencia; avisó a clientes franceses de que cesaría servicios el 1-jul-2026. No he leído ningún comunicado de Binance, ESMA ni de la HCMC; webs agregadoras que afirman "perdió el acceso" no citan primario. Solo consta (primario) que **no está en el CSV**.
- **Incidente Ledger/CryptoBilis** (SECUND.: [The Block 9-oct-2026](https://theblock.co/news/business/2026-10-09-ledger-cryptobilis-fund-losses-418163), Cointelegraph, Decrypt): Ledger pidió al revendedor parar ventas, recomienda no iniciar el dispositivo si se compró allí en los últimos 90 días y, si ya se configuró, mover los activos a un signer nuevo con semilla nueva. Pérdidas: >72 M$ (tanuki42) y >86 M$ (Specter), estimaciones de analistas, no de Ledger; las cadenas citadas son Bitcoin, Ethereum y Tron (no se citó XRP ni XLM). Causa: sin confirmar; solo un medio (Genfinity) dice que Ledger confirmó un implante de hardware en un dispositivo → [VERIFICAR]. Ledger sostiene que su infraestructura no fue comprometida.
- Incidente de datos de Ledger vía Global-e (ene-2026) y caídas de Stellar en Ledger (mar, jun, jul-2026): una sola web de baja fiabilidad cada uno → no usar.
- Soporte de XRP y XLM en Ledger: **no verificado** en esta sesión. Trezor: foros antiguos dicen que XRP no funciona en Model One y que XLM requiere app de terceros; posiblemente obsoleto → [VERIFICAR] en las fichas oficiales.
- 21Shares: custodios por prensa [VERIFICAR].
- **Hackeos como lección** (SECUND., y la fuente Onramp es una empresa de custodia con interés comercial): Bybit, feb-2025, ~1.400–1.500 M$ robados pese a tener prueba de reservas mensual; moraleja: una "prueba de reservas" es una foto en un momento y no muestra quién puede mover los fondos. Caso Bitget (sept-2026) ya recogido en R15 (fondo de reposición >464 M$ no verificado).
- Opinión de la industria bancaria (ICBA, Bank Policy Institute) contra las cartas OCC: postura de parte interesada.

## Caso alcista / caso bajista (sobre la seguridad del activo, no sobre el precio)
**Alcista:** (1) MiCA da por primera vez un perímetro legal único con 365 entidades autorizadas y sanciones para quien opere sin licencia; (2) los grandes (Kraken, Coinbase, Bitstamp, Bitvavo, Bitpanda, Gemini, BitGo) están en el registro; (3) en EE. UU. los ETF usan custodios fiduciarios regulados con cuentas segregadas y sin staking ni préstamos (Bitwise); (4) la rescisión de SAB 121 y las cartas OCC abren la custodia a bancos; (5) el incidente de Ledger parece acotado a un canal de venta, no a la red de firma.
**Bajista:** (1) la protección MiCA es por **sociedad**: Kraken y Bitpanda operan con varias entidades y el contrato dice cuál te sirve; (2) el registro puede ir con retraso y no es un seguro ni una prueba de solvencia; (3) concentración: los ETF de XRP dependen de Coinbase Custody, BitGo y Gemini; Coinbase es a la vez custodio y prime broker en varios; (4) parte del ETF puede estar en cuentas **omnibus** con gravamen posible, sin FDIC y con seguro compartido que "no garantiza" al fondo; (5) auto-custodia: pérdida de semilla, cadena de suministro (Ledger/CryptoBilis), errores irreversibles y destination tags/memos olvidados; (6) las cartas OCC son condicionales y los bancos grandes amenazan con litigar [ESPECULACIÓN sobre el resultado].

## Qué cambia para los digital assets (XRP, XLM, stablecoins, CBDC, tokenización)
- XRP: el vehículo regulado más líquido (ETF spot) concentra la custodia en 3–4 firmas; Ripple obtiene licencia MiCA (cambio y transferencias, **no custodia**) y carta OCC condicional: son infraestructura de la empresa, no demanda demostrada de XRP (patrón ya recogido en R13/R09P).
- XLM: sin ETF spot en EE. UU.; la opción regulada es exchange MiCA o auto-custodia. El requisito de 1 XLM de reserva y 0,5 por trustline implica que parte del saldo queda inmovilizado en la cuenta propia.
- Stablecoins/RWA: la custodia de reservas pasa a bancos fiduciarios nacionales (Circle, Paxos, Ripple vía OCC), dato por confirmar en occ.gov.

## Criterios de comparación (checklist de hechos, no recomendación)
1. ¿Qué **sociedad concreta** firma tu contrato y figura en el registro de ESMA con servicio "custodia y administración" (código a)?
2. ¿Segregación de cuentas de clientes y quién responde si hay pérdida? (apartado MiCA no leído: ver "Qué falta").
3. ¿Hay saldo omnibus, préstamos de tus activos o gravámenes? (en ETF: sí posible, ver Bitwise).
4. ¿Seguro: qué cubre, quién es el asegurado, importe y si es compartido entre clientes?
5. ¿Prueba de reservas con auditor y con pasivos, o solo un snapshot de activos?
6. ¿Historial de incidentes y cómo repusieron fondos?
7. Auto-custodia: compra solo en canal oficial, semilla generada por ti, y prueba con importe pequeño; para XRP/XLM, comprobar tag/memo y reserva mínima.
8. ¿Aparece XRP/XLM realmente listado en esa entidad de la UE? (no comprobado aquí).

## Fechas próximas (catalizadores) con fuente
- Resultado de la investigación de Ledger sobre CryptoBilis: sin fecha (Ledger "informará"; The Block 9-oct-2026, SECUND.).
- Posible nueva solicitud MiCA de Binance "en los próximos meses" (cita de su co-CEO; The Block 24-jun-2026, SECUND.).
- Actualizaciones del registro ESMA: periódicas (sin calendario oficial leído).
- 13F del 3T 2026 (custodia/propiedad institucional de ETF): hacia el 14-nov (R21).
- Aprobaciones finales OCC: sin fecha.

## Qué falta por buscar
1. Texto de MiCA, art. 75 (segregación, registro de posiciones, responsabilidad por pérdida de claves): EUR-Lex devolvió página vacía; leer vía PDF oficial (OJ L 150, 9-jun-2023).
2. Fichero de **no conformes** de ESMA (no localizada su URL) y confirmación oficial de Binance/Bitget.
3. Lista completa de qué plataformas UE listan XRP/XLM y qué custodia ofrecen para cada activo.
4. Prospecto vigente de 21Shares, Grayscale y Franklin (custodios y comisiones); resto de los 424B3 de Bitwise/Canary (cláusulas de quiebra del custodio; Canary solo leí 19 %, Bitwise 16 %).
5. Fichas oficiales de Ledger y Trezor: modelos, apps y soporte de XRP/XLM; comunicado oficial de Ledger sobre CryptoBilis.
6. Estado final OCC (Coinbase, Ripple, BitGo) en occ.gov.
7. Estado de bancos y fintech españoles (BBVA, CaixaBank, Bit2Me, Prosegur Crypto…) y fiscalidad → **R20**.
