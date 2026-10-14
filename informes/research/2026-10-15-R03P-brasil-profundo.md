# Brasil: Drex, Pix, Banco Central, CVM y Ripple/Stellar (2026-10-15, R03P profundo)

Modo: no existía informe rápido R03; este archivo hace de rápido + profundo. Marca de lectura: LEÍDO ENTERO / extracto / secundaria. Sin recomendaciones de compra/venta.

**Límite de acceso (anotado, no saltado):** `bcb.gov.br` solo devolvió el título (página JavaScript) y `normativos.bcb.gov.br` dio 404/400 con las URL que probé. Por tanto NINGÚN texto de resolución BCB se ha leído en la fuente oficial: todo sobre resoluciones es secundaria (despachos de abogados) con cita. La única fuente primaria leída entera es el comunicado de Ripple (empresa, parte interesada).

## Resumen (5 líneas)
1. El Banco Central (BCB) ya tiene marco completo para proveedores de cripto (Res. 519/520/521, vigentes desde 2-feb-2026): **el plazo para que las empresas existentes pidan autorización vence ~30-oct-2026** (cálculo mío: 270 días desde 2-feb), y quien no pida debe cesar en 30 días.
2. Las operaciones con stablecoins y activos referenciados a moneda fiat se tratan como **cambio** (Res. 521); la Res. 561 (publicada 30-abr-2026, vigente 1-oct-2026) prohíbe liquidar con stablecoins dentro del servicio eFX. La Res. 584 (7-ago-2026, vigente 1-ene-2027) añade retención de hasta 24 h en envíos > 10.000 USD a exterior o autocustodia [secundaria].
3. El Drex (CBDC con blockchain) quedó apagado: el BCB anunció en nov-2025 que desactivaba la plataforma; la nueva fase va por casos de uso (garantías de crédito), sin garantía de DLT.
4. Ripple **planea** pedir licencia PSAV (comunicado 17-mar-2026: "planeja solicitar"); una fuente posterior dice que ya la pidió: no verificado. Stellar: sin novedad regulatoria brasileña encontrada.
5. Sobre Pix: la investigación Sección 301 de EE. UU. terminó en arancel general del 25 % (vigente 22-jul-2026); Pix era solo uno de seis motivos [secundaria].

## Qué es hecho verificado (tabla)
| Dato | Fuente | Fecha | Idioma / marca |
|---|---|---|---|
| Res. BCB 519 (autorización de PSAV), 520 (funcionamiento, 3 tipos: intermediaria, custodia, corretora) y 521 (cambio y capitales) publicadas juntas | [Lefosse](https://lefosse.com/noticias/alerta/banco-central-regulamenta-o-uso-de-ativos-virtuais-e-o-funcionamento-das-prestadoras-de-servicos-de-ativos-virtuais/) (despacho); [Finsiders](https://finsidersbrasil.com.br/?p=351190) | 10-nov-2025 | PT; secundaria (texto oficial NO leído) |
| Vigencia 2-feb-2026; reglas de reporte y códigos de finalidad desde 4-may-2026 | Lefosse (el texto trae un "2926" que parece errata) | 2025-26 | PT; secundaria |
| Entidades que ya operan: solicitar autorización en 270 días (≈30-oct-2026, cálculo propio); pueden seguir operando; sin solicitud en plazo, cesar en 30 días | Lefosse | — | PT; secundaria |
| Dos fases de revisión para quien ya opera (fase 1: actividad previa, reputación, capital mínimo; fase 2: resto de requisitos). Directivos deben residir en Brasil | Lefosse | — | PT; secundaria |
| Res. 521: pagos/transferencias internacionales con activos virtuales, transferencias desde/hacia autocustodia y compra/venta/canje de activos virtuales referenciados a fiat entran en el mercado de cambio; tope 100.000 USD si la contraparte no es institución autorizada a cambio; las PSAV hoy NO están autorizadas a operar en cambio | Lefosse | — | PT; secundaria. La palabra "stablecoin" no aparece en el texto según Lefosse; el BCB lo dijo en rueda de prensa (ver Finsiders) |
| El BCB dijo que no aceptará stablecoins con algoritmos de respaldo ("não vamos aceitar esses ativos virtuais que tenham algoritmos como controle do lastro") y que el IOF lo define la Receita, no el BCB | [Finsiders](https://finsidersbrasil.com.br/?p=351190) | 10-nov-2025 | PT; secundaria (prensa especializada) |
| Res. BCB 561/2026: en eFX la liquidación con el exterior solo por operación de cambio o cuenta en reales de no residente; vedado usar activos virtuales y compensar. Publicada 30-abr-2026, vigente 1-oct-2026. Proveedores sin autorización pueden seguir solo si piden autorización hasta 31-may-2027. No prohíbe stablecoins en el mercado de cambio, solo dentro del eFX | [Demarest](https://www.demarest.com.br/banco-central-promove-alteracoes-nas-regras-relativas-ao-servico-de-pagamento-e-transferencia-internacional-efx/) (despacho, 5-may-2026); [Conjur](https://www.conjur.com.br/2026-jul-01/o-cerco-do-banco-central-as-stablecoins/) (cita "vedado o uso de ativos virtuais como trilho de liquidação"; origen: Voto 57/2026 y Consulta Pública 124/2025) | 30-abr-2026 | PT; secundaria (2 fuentes independientes de coincidencia) |
| 23-jun-2026: el BCB notificó a bancos y fondos que ciertas operaciones de cambio para importar activos virtuales vía fondos son ilegales; spread de stablecoins subió de ~0,1 % a 0,7 % (a veces >1 %) | Conjur (1-jul-2026) | 23-jun-2026 | PT; secundaria |
| Res. BCB 584 (7-ago-2026): retención preventiva de hasta 24 h en envíos > 10.000 USD (operación o suma diaria) hacia PSAV extranjeras o autocustodia; vigente 1-ene-2027 | [Judit](https://judit.io/legislacao-atualizacoes-regulatorias/resolucao-bcb-584-retencao-criptoativos/) / [Blocktrends](https://blocktrends.com.br/bc-exige-retencao-24h-transferencias-cripto-acima-10-mil/) (buscador) | 7-ago-2026 | PT; extracto de buscador, [VERIFICAR] número y fechas en el texto oficial. Conjur (1-jul) lo trataba aún como propuesta con vigencia prevista oct-2026: hubo cambio de calendario |
| Drex: reunión del 4-nov-2025 donde el BCB comunica que desactiva la plataforma (Hyperledger Besu) a partir del 10-nov-2025; motivos citados: privacidad/secreto bancario, LGPD, coste | [Portal de Prefeitura](https://portaldeprefeitura.com.br/brasil/nem-bem-nasceu-e-ja-morreu-banco-central-desativa-drex-e-anuncia-fim/607502/) (5-nov-2025, LEÍDO ENTERO); [Mundocoop](https://mundocoop.com.br/destaque/banco-central-desligara-plataforma-drex-para-criar-nova-infraestrutura/) | 4-5-nov-2025 | PT; secundaria. No hay comunicado oficial leído |
| Plan nuevo del Drex: empezar por casos de uso (garantías de crédito/gravámenes, Open Finance, Pix); primera entrega simplificada sin tokenización prevista 2.º semestre 2026; ya en ago-2025 el BCB había dicho que abandonaría DLT en la fase 3 | [Convergência Digital](https://convergenciadigital.com.br/governo/drex-insatisfeito-com-privacidade-banco-central-muda-foco-e-fase-3-sera-sobre-garantia-de-credito/); [Seu Dinheiro](https://www.seudinheiro.com/2025/economia/drex-abandonara-blockchain-na-proxima-fase-para-entregar-solucao-em-2026-diz-jornal-gmda/) (2025) | jun-nov 2025 | PT; secundaria. NO encontré anuncio oficial de 2026 sobre la fase 3 |
| Receita Federal: DeCripto (IN RFB 2.291, 14-nov-2025) sustituye a la IN 1.888/2019; alinea con CARF/OCDE; operaciones desde jul-2026; incluye proveedores extranjeros que sirven a brasileños | [Ozai](https://www.ozai.com.br/criptoativos-e-stablecoins-serao-reportados-para-a-receita-federal/) / buscador | nov-2025 | PT; extracto, [VERIFICAR] contra el texto en gov.br |
| Stablecoins = 71,7 % (1,13 de 1,58 billones de R$) de lo declarado a la Receita ago-2019 a dic-2025; USDT 88,7 % de las stablecoins, USDC 7,1 %, BRZ 3,4 % | [BP Money](https://bpmoney.com.br/mercado/stablecoins-representam-mais-de-80-das-operacoes-com-cripto-declaradas-a-receita-federal/) (título dice ">80 %", otra fuente ~80 % en 2025: cifras divergentes) | 2026 | PT; secundaria |
| Ripple, 17-mar-2026 (São Paulo): amplía servicios en Brasil (pagos, custodia, prime, tesorería); "planeja solicitar a licença de PSAV"; clientes: Banco Genial (RLUSD), Braza Bank (stablecoin BBRL en XRPL), Nomad (+3 M usuarios), Azify, ATTRUS, Frente, CRX, Justoken (>1.700 M USD tokenizados en XRPL); RLUSD >1.500 M USD cap.; listado/soportado en Mercado Bitcoin, Foxbit, Ripio | [Ripple (comunicado PT)](https://ripple.com/ripple-press/ripple-reforca-seu-compromisso-com-o-brasil-com-uma-oferta-ampliada-de-servicos-de-pagamentos-e-o-pedido-de-licenca-de-psav/) | 17-mar-2026 | PT; LEÍDO ENTERO (fuente interesada: cifras son autodeclaradas) |
| CVM: Res. 88 (crowdfunding) usada por oficios 04/2023 y 06/2023 para ofertas de tokens de recebíveis; consulta pública para reformarla cerró en ene-2026 y se analizan las respuestas; no hay ley de tokens mobiliarios | [Capital Aberto](https://capitalaberto.com.br/regulacao/2026/05/tokenizacao-cvm-regulacao) | 21-may-2026 | PT; LEÍDO ENTERO (secundaria) |
| Tokenización: ofertas ~R$ 4.000 M a fin de 2025 (x20 en dos años); AmFi R$ 5,31 mil millones tokenizados | Capital Aberto | 21-may-2026 | PT; secundaria. Otra fuente de buscador (RWA Monitor): 684 activos y R$ 6,87 mil M hasta julio-2026 [VERIFICAR] |
| EE. UU.: investigación Sección 301 abierta 15-jul-2025; USTR propuso 25 % el 1-jun-2026; Trump lo aceptó 15-jul-2026; vigente 22-jul-2026 con exenciones (café, carne, zumo de naranja, piezas de aeronave, tierras raras...); Pix era uno de seis motivos | [Covington](https://www.cov.com/news-and-insights/insights/2026/06/results-of-us-section-301-investigation-into-brazil-proposed-us-tariffs-and-renewed-bilateral-tensions); [GT Law](https://www.gtlaw.com/de/insights/2026/7/ustr-announces-section-301-tariffs-on-brazil-new-25-duties-to-take-effect-july-22) | jun-jul 2026 | EN; extracto de buscador de despachos; [VERIFICAR] lista de exenciones en el Federal Register |

## Qué está sin verificar o es opinión
- **"Ripple ya pidió la licencia"**: una reportagem de sept-2026 (citada por el buscador) lo da por hecho; la única fuente primaria (Ripple, 17-mar) dice "planea". No hay confirmación del BCB. [VERIFICAR]
- **Autorización concedida a alguien**: no encontré lista oficial de PSAV autorizadas. [VERIFICAR] en el registro del BCB.
- **Pix amenazado por EE. UU.**: es opinión/contexto político; el arancel final es general, no específico de Pix.
- **PL 4.308/2024 (stablecoins)**: prohibiría stablecoins algorítmicas y fijaría pena de hasta 8 años por emisión ilegal según un blog del sector (blockeden.xyz) [VERIFICAR; fuente anónima/promocional]. Lo confirmado: Anbima (13-mar-2026) comentó un substitutivo del relator Lucas Ramos; audiencia pública el 1-jul-2026; el BCB sostiene que son "moneda de emisión privada" y el sector que son activos virtuales (Conjur, 22-jul-2026). Sin votación en pleno localizada.
- **IOF 3,5 % sobre stablecoins/cripto** (exención hasta R$ 10.000/mes): proyecto de decreto con consulta pública; no encontré decreto publicado. [VERIFICAR] Diario Oficial.
- **Blog blockeden.xyz** afirma que Brasil es "el primer banco central del G20" en excluir stablecoins de su perímetro de cambio regulado: afirmación de una sola fuente, tono promocional. NO usar.
- **"Guía Antecipa Fácil" (Drex 2026 con B3 y Visa, despliegue amplio 2027)**: contradice las noticias de 2025; sin fuente oficial. Descartado.
- Opinión de Isac Costa (Conjur, 1-jul-2026): el BCB crea un "cerco cambial" y la retención de 24 h es evitable por fraccionamiento o autocustodia. Es opinión de un abogado.

## Caso alcista / caso bajista
**Alcista (para el uso regulado de cripto/stablecoins en Brasil):** hay marco claro y licenciable (519/520); las firmas con licencia tendrán ventaja competitiva; Ripple, Braza Bank y Justoken ya operan sobre XRPL en Brasil con volumen real (cifras autodeclaradas); la tokenización crece rápido; la Receita ya tiene datos (DeCripto) lo que normaliza el sector.
**Bajista:** el BCB trata stablecoins como cambio y restringe su uso en remesas (eFX), retiene transferencias grandes a autocustodia/exterior y puede encarecer (IOF, spreads 0,7-1 %); el plazo del 30-oct puede sacar del mercado a empresas pequeñas; el Drex como CBDC con blockchain se descartó, lo que reduce el caso de una gran red pública oficial en Brasil; la evidencia de adopción de XRP (el activo) es indirecta: casi todo lo citado es RLUSD, BBRL o tokenización, no XRP como puente.

## Qué cambia para los digital assets (XRP, XLM, stablecoins, CBDC, tokenización)
- **XRP:** el vínculo con Brasil es la infraestructura de Ripple (Payments, Custody, RLUSD, stablecoin BBRL en XRPL) y Justoken tokenizando sobre XRPL. Los hechos no demuestran demanda de XRP como activo puente en corredores brasileños [ESPECULACIÓN si se afirma lo contrario]. Un riesgo regulatorio concreto: la Res. 561 cierra la vía de stablecoins en eFX, que es justo el caso de uso de pagos transfronterizos con stablecoin.
- **XLM:** no encontré novedad regulatoria brasileña ni alianza nueva. Históricamente: Mercado Bitcoin y SDF en el LIFT Challenge del Real Digital (2022), BRLT de Settle Network y USDC en Stellar vía Mercado Bitcoin (secundaria, sin fecha clara). Estado actual en Brasil: [VERIFICAR].
- **Stablecoins:** USDT domina lo declarado; el BCB las incluye en cambio y rechaza las algorítmicas. Efecto directo en coste y en quién puede ofrecerlas.
- **CBDC:** Drex apagado; el sucesor será probablemente una solución de garantías de crédito para instituciones financieras, cartórios y corretoras, no una moneda digital minorista.
- **Tokenización:** vía CVM Res. 88 por atajo regulatorio; la reforma pendiente podría subir límites (R$ 15 M por oferta hoy según una fuente, [VERIFICAR]).

## Fechas próximas (catalizadores) con fuente
| Fecha | Evento | Fuente |
|---|---|---|
| **≈30-oct-2026** | Fin del plazo de 270 días para pedir autorización PSAV (cálculo propio desde 2-feb) y fecha citada por una sola fuente para actualizar cadastro Unicad de eFX | Lefosse; blog sector [VERIFICAR] |
| ≈30-nov-2026 | Quien no presentó solicitud debe cesar (30 días después del plazo) | Lefosse |
| 1-ene-2027 | Vigencia de la retención de 24 h (Res. 584) | Judit [VERIFICAR] |
| 31-may-2027 | Límite para que proveedores eFX no autorizados pidan autorización | Demarest |
| 2.º sem. 2026 | Primera entrega simplificada del nuevo Drex (garantías), sin tokenización | Seu Dinheiro / Convergência (2025) [VERIFICAR vigencia] |
| Sin fecha | Decisión CVM sobre la reforma de la Res. 88; votación del PL 4.308; decreto IOF | Capital Aberto; Conjur |

## Qué falta por buscar
1. Textos oficiales de Res. BCB 519, 520, 521, 561 y 584 (la web del BCB no se pudo leer): pedir a Joel los PDF.
2. Lista oficial de PSAV autorizadas / solicitudes presentadas, y si Ripple presentó la suya.
3. Comunicado oficial del BCB sobre el cierre del Drex y estado real de la "fase 3" en 2026.
4. Texto de IN RFB 2.291 (gov.br/receitafederal) y estado del decreto IOF.
5. Tramitación actual del PL 4.308/2024 (camara.leg.br).
6. Stellar/XLM en Brasil: novedades 2025-2026 en stellar.org.
7. Consulta CVM sobre la Res. 88: resultados y borrador.
