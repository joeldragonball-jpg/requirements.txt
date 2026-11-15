# C315 · Corredores de pago: estado operativo, participantes y monedas (15-nov-2026)

Análisis neutral de infraestructura; sin recomendación. Niveles: P = fuente primaria, S = secundaria, V = sin verificar. Datos en `explorador/corredores-liquidez.json` (campos nuevos `operativo`, `participantes_detalle`, `cuota_moneda`; los antiguos se mantienen).

## Estado operativo (HECHOS)
| Corredor | Estado | Fuente primaria leída |
|---|---|---|
| mBridge | En producción (socios, tras traspaso del BIS en oct-2024) | BIS: https://www.bis.org/about/bisih/topics/cbdc/mcbdc_bridge.htm (estado «Concluded», piloto real 2022, MVP 2024) |
| Project Agorá | Anunciado, sin lanzar (prototipo) | BIS 27-may-2026: https://www.bis.org/media-releases/20260527-project-agora-shows-how-tokenisation-can-improve-wholesale-cross-border-payments-work-will (pruebas de valor real solo planificadas, sin calendario) |
| Nexus | Anunciado, sin lanzar (objetivo 2027) | MAS, informe anual 2025-26: https://www.mas.gov.sg/publications/annual-report/2026/annual-report-2025-2026/innovative-and-inclusive-financial-centre/payment-innovation ; BIS https://www.bis.org/project/nexus |
| CIPS | En producción | Web de CIPS (sep-2026): 214 directos, 1.651 indirectos; http://www.cips.com.cn/kjjqgsyyingw/index/index.shtml |
| Ripple Payments/ODL | En producción comercial privada [S/P parcial] | Ripple: FCA ene-2026, CSSF 2-feb-2026 |
| Swift GPI | En producción [S] | Swift dio 403 y el PDF no tiene texto (WebFetch y Chrome) |
| Partior | En producción [S] | Sin comunicado primario localizado |

Lo observado externamente se confirma: de Agorá solo hay nota primaria del informe (BIS), sin lanzamiento; CIPS y mBridge operan. Matiz: la prensa secundaria cita pruebas de jul-2026 de Agorá (28 bancos, ~1 M$) sin nota primaria del BIS: [VERIFICAR].

## Participantes (resumen)
- mBridge: CN-CNY, HK-HKD, TH-THB, AE-AED (P, BIS); Arabia Saudí (SAR) SALIÓ tras una prueba de concepto el 13-may-2025, conocido el 20-sep-2026 por el FT [S], aunque la página del BIS aún la lista; Macao (MOP) se unió y opera desde 2-jun-2026 con 11 bancos [S, Caixin]; Mongolia solo en una fuente [V].
- Agorá: GB-GBP, US-USD, FR/Eurosistema-EUR, JP-JPY, KR-KRW, MX-MXN, CH-CHF, CA-CAD (se unió después, fecha [VERIFICAR]).
- Nexus: IN-INR, MY-MYR, PH-PHP, SG-SGD, TH-THB, ID-IDR (Bank Indonesia pleno desde 2-feb-2026; resuelve el [VERIFICAR] previo).
- CIPS: indirectos por región (Asia 1.176, de ellos 528 China continental; Europa 271; África 112; Norteamérica 35; Sudamérica 32; Oceanía 25). La web discrepa consigo misma en la sección Asia (148/1.157).

## Cuotas por moneda
Fórmula visible: HHI = Σ(cuota_i²), cuota en %. mBridge 95 % CNY [S] da HHI 9.025-9.050; CIPS 100 % CNY por diseño = 10.000 [S]. Agorá, Nexus, Ripple, Swift GPI y Partior: null con motivo (sin volúmenes publicados, o cifras de Swift incompatibles según la base: 59,1 % frente a 51 % de USD).

## Huecos
Atlantic Council (cuota mBridge) no leído; comunicado propio de SAMA; lista oficial de corredores ODL; tracker PDF de Swift; web de Partior. [ESPECULACIÓN]: ninguna incluida.
