# Auditoría de dossiers, guías, calendario y predicciones (13-oct-2026)

> Revisión informativa, **no es una recomendación** de inversión ni asesoramiento fiscal. Se han revisado los 15 dossiers de `informes/dossiers/2026-10-09-*`, el anexo de prueba de estrés, las guías G1-G5, G8, G9 y G12, `MAPA.md`, `informes/predicciones.md`, `eventos/calendario.toml` y `cerebro/documentos/catalizadores-xrp-xlm.md`. **No se ha modificado ningún documento**: aquí solo se proponen correcciones.
> **Método.** Lectura completa de todos los archivos y recálculo a mano de los ejemplos. Para verificar se usaron fuentes primarias consultadas el 13-oct-2026 entre las 15:00 y las 15:10 (hora de Madrid): texto consolidado del BOE (Ley 35/2006, RIRPF, Ley 19/1991, Ley 37/1992, Ley 5/2019 y RDL 29/2026), federalreserve.gov, ecb.europa.eu, bls.gov, ine.es, govinfo.gov (BILLSTATUS y PLAW-119publ27), esma.europa.eu, el nodo público `xrplcluster.com` (JSON-RPC: `server_info`, `feature`, `account_objects`, `gateway_balances`) y la API de DefiLlama.
> **Fuentes bloqueadas:** congress.gov y senate.gov (error 403), y el texto íntegro de la opinión de ESMA (solo se ve el titular).

## 0. Resumen

- **Hallazgos:** 34 en total. **ALTA: 6**, **MEDIA: 14**, **BAJA: 14**.
- **Los 5 más graves:**
  1. G4 dice que vender un bono o una obligación antes del vencimiento genera una ganancia o pérdida patrimonial. Según el art. 25.2 de la LIRPF es **rendimiento del capital mobiliario**. Esto cambia cómo se compensa una pérdida.
  2. G4 dice que el reembolso de un fondo **no lleva retención** para residentes. El art. 97 del RIRPF fija un **19 %**, y G4 contradice así a G12 y a G5.
  3. G5 §4.2 atribuye a los **ETF UCITS** el régimen del art. 94 (traspasos sin tributar). El propio art. 94 **excluye los fondos cotizados**.
  4. G2 y G4 dicen que el FGD **no cubre valores ni fondos**. El FGD tiene una garantía de valores **aparte**, de hasta 100.000 €, para el caso de que la entidad no los devuelva (no cubre pérdidas de mercado).
  5. El dossier 8 llama «Brent spot» (~103,9 $) a lo que en realidad es el **futuro**. El spot de la EIA estaba en **125,44 $** (6-oct).
- **Los 20 datos verificados:** 18 correctos (en 4 de ellos algún documento los cita mal o con [VERIFICAR] de más), 1 desactualizado (Euríbor de septiembre en G1) y 1 sin verificar en fuente primaria (el plazo de ESMA del 8-ene-2027). Comprobaciones extra: RLUSD en el XRPL está desactualizado, el debut de XRPN no se ha podido verificar y el RDL 29/2026 es correcto (su convalidación no consta).

## 1. Contradicciones entre documentos

| # | Tema | Documento A (cita literal) | Documento B (cita literal) | Versión más fiable y por qué |
|---|---|---|---|---|
| C1 | Precio del Brent | `2026-10-09-macro.md` l.36: «Brent spot \| ~103,9 $ (9-oct 13:45 UTC) \| \| Yahoo Finance» | `geopolitica` l.26 y `G9` l.234: «último dato **125,44 $ (6-oct)**» (EIA vía FRED) | **EIA**. El dato de Yahoo es el futuro. El propio dossier 11 (l.43) avisa del error, pero el dossier 8 sigue sin corregir. |
| C2 | RLUSD en el XRPL | `ripple-la-empresa` l.40: «**1.131.214.698 RLUSD** … ledger 107541545» | `pagos` l.26: «**1.140.114.698** … ledger 107541076»; `stablecoins` l.26: «1.140 M$» | Ninguna de las dos se puede reproducir ahora. El patrón de dígitos (131.214 frente a 140.114) apunta a un error de copia. El ledger da hoy **1.034.073.795** (ledger 107628795, 13-oct). Las dos cifras están desactualizadas. |
| C3 | Norma final de la OCC (GENIUS) | `stablecoins` l.34: «OCC publicará la norma final "**antes de noviembre**"» | `predicciones.md` #15: «publicará la norma final… **en noviembre de 2026**» | Es la misma declaración (19-ago), citada de forma distinta. Hay que releer la fuente; mientras tanto conviene usar «hacia noviembre» [VERIFICAR]. |
| C4 | Fecha de las minutas del FOMC | `catalizadores` l.13: «2026-10-08: … minutas FOMC (otra subida a fin de año)» | `macro` l.48, `predicciones` #18: 7-oct | **7-oct**: así figura en el calendario del FOMC de federalreserve.gov. |
| C5 | Reacción del mercado el 8-oct | `catalizadores` l.13: «BTC -2,4 % … XRP -5 % (1,35 $), XLM -5 %» | `macro` l.49: «-1,9 % \| -2,9 % \| -4,2 %» | **Dossier 8**: usa velas diarias de Kraken, con un método explícito. La nota de lecciones mezcla ventanas de tiempo distintas. |
| C6 | XLM en lo que va de año | `stellar-rwa` l.9: «**~-11 % en el año**» (CoinGecko vía prensa) | `geopolitica` l.12: «XLM **-7,9 %**» (Kraken, de 0,2084 a 0,1918) | **Dossier 11**: es un cálculo propio con precios inicial y final explícitos. |
| C7 | Retención al reembolsar un fondo | `G4` l.158: «sin retención para residentes [VERIFICAR]» | `G12` l.134 y `G5` l.184: «retención del 19 %» | **G12/G5**. El art. 97 del RIRPF dice: «… instituciones de inversión colectiva será el resultado de aplicar a la base de retención el porcentaje del 19 por ciento». |
| C8 | Venta de un bono antes del vencimiento | `G4` l.153: «la diferencia entre precio de venta y de compra es **ganancia o pérdida patrimonial**» | Art. 25.2.b LIRPF (BOE): «En el caso de transmisión, reembolso, amortización… de valores, se computará **como rendimiento**…» | **BOE**. El ejemplo de G4 (l.155, «pérdida patrimonial ≈ 44,5 €») está mal calificado. |
| C9 | ETF y traspasos | `G5` l.116: «ETF UCITS (UE) \| Régimen de IIC (art. 94 LIRPF)» | `G5` l.183 y BOE art. 94.1.a: el diferimiento no se aplica a participaciones de «fondos de inversión cotizados» | **BOE**. Es una contradicción dentro de la propia G5. |
| C10 | Exención de dividendos suprimida | `G8` l.203: «no hay la exención de **5.000 €** de dividendos (eliminada en 2015)» | `G12` l.92: «No hay exención de **1.500 €** desde 2015» | **G12**: la exención era de 1.500 € (antiguo art. 7.y, suprimido por la Ley 26/2014) [VERIFICAR en el historial del BOE]. |
| C11 | Reducción del alquiler | `G12` l.112 (50/60/70/90 %) y `G8` §14.1: «G12 deba revisarse» | BOE, DT del RDL 29/2026: los contratos celebrados «entre … la Ley 12/2023 y el 1 de diciembre de 2026» siguen el art. 23.2 «en su redacción vigente a 31 de diciembre de 2025» | **Las dos son correctas en parte**: G12 vale para los contratos firmados antes del 1-dic-2026 y G8 para los nuevos. La fecha de G8 (l.159, «no lo leí en el BOE») **ya está confirmada en el BOE**. |
| C12 | Euríbor de septiembre | `G1` l.55: «Aún no publicada oficialmente» (guía del 10-oct) | BOE-A-2026-20519 (publicado el 2-oct): **3,247 %**. `G8` l.234 lo marca como «web comercial … [VERIFICAR]» | **BOE**. G1 estaba desactualizada el mismo día en que se escribió. |
| C13 | Fecha de la subida del BCE en junio | `G1` l.153: «subida el **17-jun-2026** (+25 pb) y otra el 10-sep (efectiva el 16-sep)» | Tabla del BCE: el 17-jun-2026 es la fecha **de efecto** | El BCE. G1 mezcla en la misma frase una fecha de efecto (junio) y una de decisión (septiembre). La fecha exacta de la decisión de junio [VERIFICAR]. |
| C14 | Enmienda en cuenta atrás | `catalizadores` l.15: «BatchV1_1 gana mayoría 9-oct 09:34 UTC: activación posible >= 23-oct» | `infraestructura` l.6-8 y la línea 17 de corrección | **Ledger**: `fixCleanup3_4_0` tiene mayoría desde el 9-oct a las 09:34:30 UTC (activación posible el 23-oct a las 09:34:30) y `BatchV1_1` ya está activada. La línea 15 sigue ahí, sin marca de error. |
| C15 | Situación de la CLARITY Act | `catalizadores` l.6: «CLARITY Act **fracasa** en el Senado (49-50)» | `clarity` l.6: «**bloqueada pero no muerta**» | **govinfo**: lo que fracasó (49-50) fue el «cloture on the motion to proceed», y Tillis pidió reconsiderar la votación. La ley sigue viva. |
| C16 | Cronología de la CLARITY Act | `clarity` l.17: «5-ago-2026 Thune no presenta el cierre de debate» | govinfo BILLSTATUS: «2026-08-08 Cloture motion on the motion to proceed… presented» | No hay contradicción, pero **falta un hito**: la moción de cierre se presentó el 8-ago. |
| C17 | Remisión a otra guía | `G8` l.206: «(**G14 de custodia** y G15 de asesores…)» | `MAPA.md` l.43: G14 = «Errores del inversor y sesgos» | La custodia está en el **dossier 14**, no en la G14. Remisión rota. |
| C18 | Estado de G8 y G9 | `G5` l.285: «Pendientes de la serie: G13, **G8, G9**»; `G8` l.303: «G9 (commodities, **pendiente**)» | `MAPA.md` l.37-38: G8 y G9 «✅ hecha» (13-oct) | **MAPA**. Son referencias obsoletas. |
| C19 | Tramos del ahorro | `G1` l.123: «según fuentes secundarias … [VERIFICAR]»; `G4` l.144: «a verificar» | `dossier 13` l.26 (BOE) y BOE art. 66 hoy | **BOE** (verificado, ver V1). El [VERIFICAR] de G1/G4 sobra. |
| C20 | Cobertura del FGD | `G2` l.80: «**No cubre:** fondos de inversión, valores, acciones y bonos»; `G4` l.139: «El FGD … cubre depósitos, no bonos ni fondos» | fgd.es y RDL 16/2011 art. 10.2: garantía de **valores** depositados en una entidad de crédito, hasta 100.000 €, **independiente** de la de depósitos (solo si la entidad no los devuelve, no por pérdidas de mercado) | **FGD**. G2 y G4 inducen a error por omisión. |
| C21 | Debut de XRPN | `predicciones` #10: «Sin resolver» (fecha límite 12-oct); `calendario` l.179: 12-oct | — | La fecha límite ya ha pasado. Falta resolver la predicción; el resultado no se ha podido verificar (ver V-extra). |
| C22 | RLUSD total | `stablecoins` l.25: 2.466,5 M$; `pagos` l.27: ~2.456; `panorama` l.43: 2.440 (todas del 9-oct) | DefiLlama hoy: 2.413,6 M$ | Las diferencias vienen de la hora y del agregador. **Hay que dar siempre la hora** y no presentar estas cifras como contradictorias. |
| C23 | Aportación periódica (DCA) | `G5` l.15: «**perdió menos** la aportación periódica en las peores» | `G5` l.209: a 5 años, DCA **−41 %** frente a entrada única −36 % (el DCA perdió más) | **La tabla**: la frase del resumen solo es cierta a 12 meses y a 10 años. |
| C24 | Peor caso a 10 años del DCA | `G5` l.212: «−7 % frente a −23 % a 10 años» («el peor caso, ene-2000») | `G5` l.210: «−10 % / −31 %» | Probablemente sean ventanas distintas, pero el texto llama «peor caso» a algo que no lo es. Hay que aclararlo. |
| C25 | Rentabilidad neta del ejemplo de alquiler | `G8` l.10: «después ~2,4 %» | `G8` l.135: 2,45 %; l.245: «~2,5 % neto» | Mismo cálculo (2,45 %). Hay que unificar el redondeo. |
| C26 | Decretos-ley de 2026 | `G8` l.190: «**4** decretos-ley en 2026: 8/2026, 26/2026, 29/2026 y los posibles posteriores» | — | Solo enumera 3. La prensa cita también el RDL 27/2026 (rechazado el 2-oct) [VERIFICAR]. |
| C27 | Cuentas de escrow de Ripple | `ripple-la-empresa` l.48: «20 cuentas del xrp-ledger.toml» | El toml publica hoy **21** direcciones `[[ACCOUNTS]]` | El total (98 escrows, 31.400 M XRP) **coincide**. Solo cambia el recuento de cuentas. |
| C28 | Protocolo 26 de Stellar | `stellar-rwa` l.32: «Protocolo 26 "Yardstick" (congelar claves comprometidas, aritmética más segura)» | `infraestructura` l.43: «CAP-80 (BN254) y CAP-82 (enteros de 256 bits)» | **Dossier 9** (CAPs en GitHub). La descripción de Nansen no coincide. |

## 2. Verificación de los 20 datos clave

| # | Dato | Dónde aparece | Valor verificado | Fuente primaria (consulta del 13-oct-2026) | Veredicto |
|---|---|---|---|---|---|
| V1 | Escala del ahorro 19/21/23/27/30 % | dossier 13 l.7; G12 l.67-74; G1 l.123-130; G9 l.181 | Parte estatal: 9,5 % (6.000), 10,5 % (50.000), 11,5 % (200.000), 13,5 % (300.000), 15 % en adelante. Duplicada con la autonómica da 19/21/23/27/30 % | [BOE, Ley 35/2006, art. 66](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) (versión consolidada del 7-oct-2026) | **CORRECTO** (sobra el [VERIFICAR] de G1/G4) |
| V2 | Escala general estatal | G12 l.56-64 | 9,5 % hasta 12.450 €; 12 % hasta 20.200 €; 15 % hasta 35.200 €; 18,5 % hasta 60.000 €; 22,5 % hasta 300.000 €; 24,5 % en adelante | BOE, art. 63.1 | **CORRECTO** (sobra el [VERIFICAR] de G12 l.64) |
| V3 | Compensación de pérdidas con límite del 25 % y 4 años | dossier 13 l.8; G12 l.155-158; G5 l.190 | «con el límite del 25 por ciento de dicho saldo positivo … en los cuatro años siguientes» | BOE, art. 49.1 | **CORRECTO** |
| V4 | Traspasos sin tributar (art. 94) y exclusión de los ETF | G12 l.133; G5 l.181-183; G4 l.158 | Diferimiento para las IIC de la Ley 35/2003; no se aplica a «fondos de inversión cotizados» | BOE, art. 94.1.a | **CORRECTO** (pero G5 l.116 es **incorrecto**, ver C9) |
| V5 | Retención del 19 % | G12 l.174; G5 l.169/184; G4 l.152/158 | 19 % sobre el capital mobiliario (art. 90 RIRPF) y sobre las ganancias por reembolso de IIC (art. 97 RIRPF) | [BOE, RIRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | **CORRECTO** (G4 l.158 es **incorrecto**) |
| V6 | Patrimonio: mínimo exento de 700.000 €, vivienda habitual hasta 300.000 € y obligación de declarar con más de 2 M€ | G12 l.213-217; dossier 13 l.133 | Art. 28.Dos: 700.000 €; art. 4.Nueve: 300.000 €; art. 37: cuota a ingresar o bienes de más de 2.000.000 € | [BOE, Ley 19/1991](https://www.boe.es/buscar/act.php?id=BOE-A-1991-14392) | **CORRECTO** (sobra el «de memoria» de G8 l.174) |
| V7 | IVA: oro de inversión exento y plata al tipo general | G9 l.174-177; G12 l.149-150 | Art. 140 bis.Uno.1.º: exentas «las entregas… de oro de inversión»; art. 90.Uno: «al tipo del 21 por ciento» | [BOE, Ley 37/1992](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) | **CORRECTO** (la duda del 21 % de G9 l.176 y l.295 queda resuelta) |
| V8 | Comisiones por amortización anticipada (Ley 5/2019) | G3 l.14, l.165-176 | Variable: 0,15 % los 5 primeros años o 0,25 % los 3 primeros; fijo: 2 % los 10 primeros años y 1,5 % después; novación a fijo: 0,05 % los 3 primeros años y nada después | [BOE, Ley 5/2019, art. 23](https://www.boe.es/buscar/act.php?id=BOE-A-2019-3814) | **CORRECTO** |
| V9 | Mínimos de impago para el vencimiento anticipado | G3 l.15, l.181-184 | 3 % del capital o 12 cuotas en la primera mitad del plazo; 7 % o 15 cuotas en la segunda | BOE, Ley 5/2019, art. 24 | **CORRECTO** |
| V10 | Tipos del BCE: 2,50 / 2,65 / 2,90 % | G1 l.6, l.35-37; macro l.26 | En vigor desde el 16-sep-2026; el tramo anterior, 2,25 / 2,40 / 2,65 %, desde el 17-jun-2026 | [BCE, tipos oficiales](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html) | **CORRECTO** (sobra el [VERIFICAR texto] de macro l.26; ver C13) |
| V11 | Fed: 3,75-4,00 %, subida de 25 pb, 12-0 | macro l.24; catalizadores l.11; G9 l.240 | «decided to raise the target range… by 1/4 percentage point», 3-3/4 a 4 %, votación 12-0 | [Fed, 16-sep-2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm) | **CORRECTO** |
| V12 | Calendario de la Fed y del BCE | calendario l.21-34, l.71-92; macro l.61-72 | FOMC: 27-28 oct (sin proyecciones) y 8-9 dic (con proyecciones); minutas de septiembre el 7-oct. BCE: 28-29 oct y 16-17 dic, con rueda de prensa el segundo día | [Fed, calendario](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm); [BCE, calendario](https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html) | **CORRECTO** |
| V13 | IPC de EE. UU. de agosto y fecha del de septiembre | macro l.27-28; calendario l.6, l.52, l.81 | Agosto: 3,4 % interanual, +0,4 % mensual, subyacente 2,4 %, gasolina +27,4 %. Septiembre: 14-oct a las 08:30 ET; PPI el 15-oct; IPC de octubre el 10-nov y de noviembre el 10-dic | [BLS, nota](https://www.bls.gov/news.release/cpi.nr0.htm); [BLS, calendario de octubre](https://www.bls.gov/schedule/2026/10_sched.htm) | **CORRECTO** |
| V14 | IPC de España (adelantado de septiembre) | G1 l.8, l.95-98; G4 l.180 | 4,9 % general, 3,1 % subyacente, IPCA 5,0 %; el dato definitivo «el próximo mes», sin día concreto | [INE, 29-sep](https://www.ine.es/dyngs/Prensa/adIPC0926.htm) | **CORRECTO** |
| V15 | Euríbor a 12 meses | G1 l.52-55; G8 l.234 | Agosto: 2,954 % (BOE-A-2026-18507). **Septiembre: 3,247 %** (BOE-A-2026-20519, publicado el 2-oct) | [BOE, 2-oct-2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20519) | Agosto **CORRECTO**; septiembre en G1 **DESACTUALIZADO** |
| V16 | CLARITY Act (H.R. 3633) | clarity l.6, l.15-18; predicciones #1-#7 | Aprobada por la Cámara 294-134 (17-jul-2025); comité del Senado (14-may-2026); moción de cierre (8-ago); cloture 49-50 (15-sep, voto 234); moción de reconsiderar de Tillis. **No es ley** | [govinfo, BILLSTATUS](https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr3633.xml) (actualizado el 17-sep). congress.gov dio 403 | **CORRECTO** |
| V17 | GENIUS Act: firma y entrada en vigor | stablecoins l.14, l.50; euro digital l.62 | Public Law 119-27, «Approved July 18, 2025»; entra en vigor en la fecha más temprana entre 18 meses (es decir, el 18-ene-2027) y 120 días después de las normas finales | [govinfo, PLAW-119publ27](https://www.govinfo.gov/content/pkg/PLAW-119publ27/html/PLAW-119publ27.htm) | **CORRECTO** (sobra el [VERIFICAR en el texto de la ley]) |
| V18 | ESMA sobre stablecoins no conformes y plazo del 8-ene-2027 | stablecoins l.9, l.35; calendario l.157 | Confirmado el titular del 8-oct-2026: «ESMA sets out supervisory expectations on services related to unauthorised stablecoins». El plazo de 3 meses (8-ene-2027) solo aparece en prensa (Cointelegraph, crypto.news, Lovguiden) | [ESMA, noticias](https://www.esma.europa.eu/press-news/esma-news) | Fecha **CORRECTA**; plazo **NO VERIFICABLE** en fuente primaria |
| V19 | Enmiendas y reservas del XRPL | infraestructura l.6-8, l.23-29; calendario l.127; predicciones #19; panorama l.71 | rippled 3.4.1; 107 enmiendas conocidas y 97 activadas. BatchV1_1, fixBatchV1_2, PermissionDelegationV1_1, Credentials, PermissionedDEX, TokenEscrow, MPTokensV1 y DeepFreeze **activadas**. **fixCleanup3_4_0** con mayoría desde el 9-oct a las 09:34:30 UTC (activación posible a partir del 23-oct a las 09:34:30). LendingProtocol y SingleAssetVault sin activar. Reserva base 1 XRP y 0,2 XRP por objeto; comisión base 0,00001 XRP | Nodo `xrplcluster.com` (`feature`, `server_info`), ledger 107628771 | **CORRECTO** (sobra el [VERIFICAR hoy] de custodia l.80) |
| V20 | Escrow de Ripple: vencimiento del 1-nov | ripple l.11, l.48-49; calendario l.187; predicciones #23 | 98 escrows con 31.400.000.000 XRP en las cuentas del toml; los `FinishAfter` más próximos son el 1-nov-2026 a las 00:00 UTC (dos) y el 1-dic-2026 | Nodo `xrplcluster.com` (`account_objects`) y ripple.com/.well-known/xrp-ledger.toml | **CORRECTO** |

**Comprobaciones extra:**
- **RLUSD en el XRPL:** 1.034 M (ledger 107628795, 13-oct), frente a los 1.131-1.140 M citados el 9-oct. **DESACTUALIZADO** (ver C2).
- **DefiLlama, total de stablecoins en dólares:** 312,9 MM$; USDT 184,0 MM$, USDC 72,8 MM$ y EURC 493,6 M€. Coincide con el dossier 7.
- **Debut de XRPN el 12-oct:** solo hay prensa que repite la fecha prevista. Una web dice que abrió a 10,50 $, pero sin datos de bolsa. **NO VERIFICABLE**.
- **RDL 29/2026:** el BOE confirma el nuevo art. 23.2 (reducciones del 100 % al 15 %), la deducción del 10 % para el inquilino con base inferior a 33.007,20 € y el régimen transitorio para los contratos anteriores al 1-dic-2026. **CORRECTO**. La **convalidación no consta**. Según la prensa (sin verificar, RTVC y Euronews), las Cortes estarían disueltas por elecciones el 29-nov-2026 y la votación correspondería a la Diputación Permanente [VERIFICAR en congreso.es y en el BOE]. Si se confirma, afectaría a lo que se dice de los «Presupuestos 2027» (G12 l.326 y l.342).

## 3. Calidad y riesgos

### 3.1 Frases que pueden leerse como recomendación
| Archivo y línea | Texto literal | Problema |
|---|---|---|
| G3 l.111 | «No recomiendo solicitarla.» | Es una recomendación en negativo. Choca con la regla de no recomendar. |
| G12 l.206 | «no es un producto recomendable «por la deducción»» | Es una valoración de producto, aunque vaya etiquetada como opinión. |
| G5 l.219 | «el dinero que **necesitarás en pocos años no debería estar** en renta variable» | Es una pauta de asignación personal; el «no es recomendación» que sigue no la neutraliza. |
| custodia l.140 | «No dejar más en el exchange que lo que necesitas operar (criterio general, no consejo)» | Es una instrucción disfrazada. Mejor describir el riesgo en lugar de decir qué hacer. |
| clarity l.45 | «**Mi lectura:** lo más probable es C o B» | Está etiquetada como opinión, pero conviene marcarla con [ESPECULACIÓN]. |

### 3.2 Causalidad no demostrada
- `catalizadores` l.12-13: «Macro manda.»
- `evernorth` l.61: «Los movimientos recientes se explican sobre todo por macro y petróleo.»
- `etfs` l.12: «En 2026 mandan macro y petróleo.»
- `pagos` l.67: «Estos días mandan macro y petróleo.»

Estas frases afirman una causa, mientras que el dossier 8 (l.51) y el dossier 11 (l.12, con correlación diaria entre −0,07 y −0,13) dicen que **no hay causalidad demostrada**. Propuesta: «coincidió con días de macro y petróleo; causalidad no medida».

### 3.3 Cifras precisas sin fuente o mal descritas
- **G2 l.94:** «MREL: … al menos el 8 % del balance». El 8 % de pasivos totales y fondos propios (TLOF) es el **bail-in mínimo para acceder al Fondo Único de Resolución**, no la definición del MREL.
- **G4 l.102:** «Impago \| D (S&P) / **C (Fitch)**». En Fitch el impago es «RD/D»; «C» es la nota previa al impago.
- **G8 l.202:** «la Ley 7/2024 pudo introducir un gravamen sobre beneficios no distribuidos» de las SOCIMI. Por lo que se conoce, ese gravamen del 15 % viene de la **Ley 11/2021** [VERIFICAR en el BOE].
- **G5 l.153-154:** «Si el dólar pierde un 10 %… EUR/USD a 1,2312 … −81 €». Con 1,2312 el dólar pierde un **9,1 %**; con una caída del 10 % la pérdida sería de unos **−89 €** (804 €). Hay que precisar si sube el euro o baja el dólar.
- **panorama l.67:** «XRPL ~3-4 s (15 ledgers: 59 s)». 59 s entre 14 intervalos son unos **4,2 s**.
- **ripple l.53**, «200–400 M XRP por trimestre», y **G3 l.190**, «44.000 M€» de exposición al IRPH: van marcadas con [VERIFICAR], pero tienen pinta de dato oficial. Conviene citar el medio y la fecha.

### 3.4 Recálculo de los ejemplos numéricos

| Guía | Ejemplo | Resultado del documento | Mi recálculo | ¿Cuadra? |
|---|---|---|---|---|
| G1 §3 | Cuota de 150.000 € a 25 años al 3 / 4 / 5 % | 711 / 792 / 877 € | 711,3 / 791,8 / 876,9 € | Sí |
| G1 §6 | Real del 3 % con IPC del 4,9 %; neto tras el 19 % | −1,8 % y −2,5 % | −1,81 % y −2,47 % | Sí |
| G3 §6.3 | Cuota, intereses, 1.ª y 2.ª cuota; 52,7 % de interés | 711,3; 63.390; 375 / 336,3; 374,16 | Igual | Sí |
| G3 §7 | Comisiones: 0,25 % de 20.000 €; 2 % de 20.000 €; 0,05 % de 100.000 € | 50 / 400 / 50 € | Igual | Sí |
| G4 §3-4 | Bono del 3 % a 5 años, valorado al 4 % y al 2 %; duración | 955,5 / 1.047,1; 4,7 / 4,6 | 955,48 / 1.047,13; 4,717 / 4,58 | Sí (la **calificación fiscal** está mal, ver C8) |
| G4 §7 | Letra al 3,026 %: precio, ganancia y neto | 970,6; 29,4; neto 238 € (2,45 %) | 970,63; 29,37; 238,1 € | Sí |
| G5 §5.3 | Efecto del TER del 0,2 % frente al 1,5 % (20 y 30 años, aportación única y mensual) | 30.883 / 24.117; 54.271 / 37.453; 88.684 / 76.832; 188.012 / 149.413 | 30.883 / 24.117; 54.271 / 37.453; ≈88.686 / 76.832; ≈188.012 / 149.413 | Sí |
| G5 §5.4 | Divisa | −81 € con un dólar «−10 %» | −81 € equivale a un dólar −9,1 % | **Impreciso** |
| G5 §8.1 | DCA frente a entrada única | Resumen: el DCA pierde menos en los peores casos | La tabla lo contradice a 5 años | **No cuadra** (C23-C24) |
| G8 §1.3 | Deuda pendiente, intereses y escenarios A y B | 137.336; 51.144; 52.782; 80.398; 146.750 / 249.744; 97.442 / 149.092 | Igual (diferencia de ±1 €) | Sí |
| G8 §4.8 | Intereses y capital amortizado del primer año | 5.940 / 5.441 € | ≈5.926 / 5.455 € | Error pequeño (unos 14 €) |
| G8 §4 | Rentabilidad bruta y neta; IRPF | 4,80 %; 2,56 %; 313 €; 2,45 % | Igual | Sí (la reducción del 50 % es correcta para contratos anteriores al 1-dic-2026) |
| G9 §2 | Prima y horquilla; contango y backwardation | 8,2 %; −21,2 % / +27,4 % | 8,25 %; −21,15 % / +27,43 % | Sí |
| G9 §4.3 | Máximo del oro de 1980 en dólares de 2026 | ~3.641 $ | 850 × 334,1 / 78,0 = 3.640,8 $ | Sí (el dato de 850 $ es de fuente secundaria) |
| G12 §1.6 | Ejemplos A, B y C | 6.111 / 1.980 / 12.680 € | Igual | Sí |
| G12 | Alquiler, fondos, venta de inmueble, compensación, Patrimonio y Sucesiones | 2.700 / 540; 1.250; 14.980; 570; ≈1.665; 51.397,81 | Igual (Patrimonio: 1.664,37) | Sí |
| Estrés | Recuperación de la mezcla en 2024 sin que se recuperen sus componentes | Mezcla recuperada el 2-dic-2024 | Es plausible por el efecto del rebalanceo diario (≈+6 %/año con σ≈1,05 y ρ=0,7) | Sí, aunque es poco intuitivo; el documento ya lo advierte |

## 4. Correcciones propuestas, por prioridad

### ALTA
| # | Archivo | Texto actual (literal) | Texto propuesto | Fuente |
|---|---|---|---|---|
| A1 | G4 l.153 | «**Venta antes del vencimiento**: la **diferencia entre precio de venta y de compra** es **ganancia o pérdida patrimonial** (base del ahorro)» | «Venta o amortización antes del vencimiento: la diferencia entre el valor de transmisión y el de adquisición es **rendimiento del capital mobiliario** (art. 25.2.b LIRPF), en la base del ahorro. Los rendimientos negativos se compensan primero con otros rendimientos del capital mobiliario y, después, con ganancias, con el límite del 25 % (art. 49). Si se compran activos homogéneos en los 2 meses anteriores o posteriores, la pérdida se difiere.» | [BOE, art. 25.2.b y 49](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) |
| A2 | G4 l.155 | «pérdida patrimonial ≈ 44,5 €, que se compensa con ganancias patrimoniales del año» | «rendimiento negativo del capital mobiliario ≈ 44,5 €, que se compensa con intereses y dividendos del año (y, con el límite del 25 %, con ganancias)» | Ídem |
| A3 | G4 l.158 | «sin retención para residentes [VERIFICAR]» | «con **retención del 19 %** sobre la ganancia (art. 97 RIRPF); en los traspasos no hay retención» | [BOE, RIRPF art. 97](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) |
| A4 | G5 l.116 | «Régimen de IIC (art. 94 LIRPF) [VERIFICAR para fondos extranjeros]» | «**Sin traspaso**: el art. 94.1.a excluye los fondos cotizados; se tributa al vender (ver §7.2)» | BOE, art. 94.1.a |
| A5 | G2 l.80 y G4 l.139 | G2: «**No cubre:** fondos de inversión, valores, acciones y bonos.» G4: «El Fondo de Garantía de Depósitos (G2) cubre depósitos, no bonos ni fondos.» | «El FGD tiene **dos garantías independientes**: depósitos, hasta 100.000 €, y **valores confiados** a la entidad de crédito, hasta 100.000 €, solo si la entidad no los devuelve. **No cubre pérdidas de valor.** En las empresas de servicios de inversión, la garantía equivalente es el FOGAIN.» | [FGD, valores](https://www.fgd.es/en/general-information/whats-deposit-guarantee-fund-fgd/securities-held-on-deposit/guaranteed-deposits-securities/); RDL 16/2011, art. 10.2 |
| A6 | macro l.36 y l.10 | «Brent spot \| ~103,9 $ (9-oct 13:45 UTC)»; «Brent hoy ~104 $ (Yahoo Finance)» | «Brent **de futuros** ~103,9 $ (Yahoo). El spot de la EIA (Dated Brent) estaba en 125,44 $ el 6-oct; la previsión del STEO (105 $) se refiere al spot» | [EIA vía FRED, DCOILBRENTEU](https://fred.stlouisfed.org/series/DCOILBRENTEU); dossier 11 |

### MEDIA
| # | Archivo | Texto actual (literal) | Texto propuesto | Fuente |
|---|---|---|---|---|
| M1 | G1 l.55 | «Aún no publicada oficialmente (saldrá a principios de octubre en el BOE)» | «**3,247 %** (septiembre; BOE-A-2026-20519, 2-oct)» | [BOE](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20519) |
| M2 | G8 l.234 | «septiembre no verificado (una web comercial da 3,247 %: [VERIFICAR])» | «septiembre **3,247 %** (BOE-A-2026-20519)» | Ídem |
| M3 | G8 l.159 y l.267 | «… desde el 1-dic-2026 … [VERIFICAR; **no lo leí en el BOE**]» | «Verificado en el BOE: los contratos celebrados entre la Ley 12/2023 y el 1-dic-2026 mantienen el art. 23.2 en su redacción a 31-dic-2025; el nuevo esquema se aplica a los contratos posteriores. Convalidación pendiente [VERIFICAR]» | [BOE, RDL 29/2026, DT](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823) |
| M4 | G12 l.116 | «Según fuente secundaria, las nuevas reglas se aplicarían a contratos desde el **1-dic-2026**» | «Según el propio RDL 29/2026 (BOE), …; la tabla 50/60/70/90 % sigue siendo la aplicable a los contratos firmados antes de esa fecha» | Ídem |
| M5 | G8 l.203 | «no hay la exención de 5.000 € de dividendos (eliminada en 2015)» | «no hay la exención de 1.500 € de dividendos (suprimida desde 2015)» | G12 l.92; Ley 26/2014 [VERIFICAR el historial del art. 7] |
| M6 | ripple l.40 / pagos l.26 | «1.131.214.698 RLUSD» / «1.140.114.698» | «~1.131-1.140 M el 9-oct (cifras que no coinciden entre sí: [VERIFICAR]); **1.034 M el 13-oct** (ledger 107628795)» | Nodo XRPL, `gateway_balances` |
| M7 | predicciones #15 | «en noviembre de 2026» | «hacia noviembre (otra lectura: "antes de noviembre", dossier 7) [VERIFICAR la cita del 19-ago]» | Stablecoins l.34 |
| M8 | predicciones #10 | «Sin resolver» | «**Pendiente de comprobar**: fecha límite pasada (12-oct); no hay confirmación primaria de la primera cotización» | Búsqueda del 13-oct; prensa sin datos de Nasdaq |
| M9 | G5 l.15 | «pero **perdió menos** la aportación periódica en las peores (§8.1)» | «la aportación periódica perdió menos en el peor caso a 12 meses y a 10 años, pero **más** a 5 años (§8.1)» | G5 l.208-210 |
| M10 | G5 l.212 | «En el **peor** caso (empezar en ene-2000), el DCA perdió menos: −7 % frente a −23 %» | «Empezando en ene-2000: −7 % frente a −23 %. El peor caso de la tabla es −10 % frente a −31 % (otra ventana)» | G5 l.210 |
| M11 | catalizadores (añadir una línea; la regla 5 del CLAUDE.md impide editar las existentes) | l.13: «minutas FOMC» el 8-oct; l.6: «fracasa» | Línea nueva: «CORRECCIÓN 2026-10-13 (auditoría): minutas del FOMC el 7-oct (Fed); el 15-sep falló el cloture del motion to proceed (49-50), no la ley; la reacción del 8-oct según Kraken (dossier 8) fue BTC −1,9 %, XRP −2,9 %, XLM −4,2 %.» | Fed; govinfo |
| M12 | G3 l.111; G5 l.219; custodia l.140; G12 l.206 | Ver §3.1 | Sustituirlas por la descripción del riesgo, sin indicar qué hacer | CLAUDE.md, reglas de análisis |
| M13 | evernorth l.61; etfs l.12; pagos l.67 | «Los movimientos recientes se explican sobre todo por macro y petróleo» (y variantes) | «Coincidieron con días de noticias macro y de petróleo; la causalidad no está medida (dossier 8 §4, dossier 11 §7)» | Dossiers 8 y 11 |
| M14 | G1 l.123 y l.186; G4 l.144 y l.196 | «según fuentes secundarias para 2026 [VERIFICAR…]» | «verificado en el BOE (arts. 66 y 76; consolidado a 7-oct-2026)» | BOE, art. 66 |

### BAJA
| # | Archivo | Texto actual (literal) | Texto propuesto | Fuente |
|---|---|---|---|---|
| B1 | G8 l.206 | «(G14 de custodia y G15 de asesores y reclamaciones, cuando existan)» | «([dossier 14 de custodia](2026-10-09-custodia-y-seguridad.md) y G15 de asesores y reclamaciones, cuando exista)» | MAPA l.21 y l.43 |
| B2 | G5 l.285; G8 l.303 | «Pendientes de la serie: G13 (gestión patrimonial), G8, G9.» / «G9 (commodities, pendiente)» | «Pendientes: G6, G7, G10, G11, G13-G15» / «[G9](2026-10-13-G9-commodities.md)» | MAPA |
| B3 | G1 l.153 | «subida el 17-jun-2026 (+25 pb)» | «subida con efecto el 17-jun-2026 (+25 pb; fecha de la decisión [VERIFICAR])» | Tabla del BCE |
| B4 | G1 l.151 | «0 % → **4,00 %**» | «−0,50 % → 4,00 % (la primera subida lo llevó al 0 %)» | BCE, tabla histórica [VERIFICAR] |
| B5 | G4 l.102 | «D (S&P) / C (Fitch)» | «D (S&P) / RD-D (Fitch)» | Escala de Fitch [VERIFICAR] |
| B6 | G2 l.94 | «(al menos el 8 % del balance en el planteamiento general)» | «el 8 % de pasivos totales y fondos propios es el bail-in mínimo para acceder al Fondo Único; el MREL se fija banco a banco» | BRRD/SRMR [VERIFICAR] |
| B7 | G5 l.154 | «Si el dólar pierde un 10 % frente al euro (EUR/USD a 1,2312)» | «Si el euro sube un 10 % frente al dólar (EUR/USD a 1,2312; el dólar pierde un 9,1 %)» | Cálculo |
| B8 | G8 l.136 | «intereses del primer año son ≈ 5.940 € y el capital amortizado ≈ 5.441 €» | «≈ 5.926 € y ≈ 5.455 €» | Cálculo con el sistema francés |
| B9 | G8 l.10 | «después ~2,4 %» | «después ~2,45 %» | G8 §4 |
| B10 | G8 l.190 | «(4 decretos-ley en 2026: 8/2026, 26/2026, 29/2026 y los posibles posteriores)» | Enumerar los que se hayan verificado, incluido el 27/2026 si se confirma [VERIFICAR] | Prensa del 2-oct |
| B11 | macro l.26; stablecoins l.14; G9 l.176 y l.295; custodia l.80 | [VERIFICAR] ya resueltos (tipos del BCE, fecha de la GENIUS Act, IVA del 21 %, reservas del XRPL) | Marcarlos como verificados, con la fuente | V7, V10, V17, V19 |
| B12 | clarity l.17 | Falta un hito | Añadir la fila «8-ago-2026: se presenta la moción de cierre (cloture) sobre el motion to proceed (CR S4557)» | govinfo BILLSTATUS |
| B13 | ripple l.48 | «Escrow en las 20 cuentas del `xrp-ledger.toml`» | «… en las 21 direcciones listadas (13-oct)» | ripple.com/.well-known/xrp-ledger.toml |
| B14 | stellar-rwa l.32 | «Protocolo 26 "Yardstick" (congelar claves comprometidas, aritmética más segura)» | «Protocolo 26: CAP-80 (BN254) y CAP-82 (enteros de 256 bits), según el dossier 9» | stellar-protocol (dossier 9) |

## 5. Lo que no se ha podido verificar
- **congress.gov y senate.gov** dieron 403. La CLARITY Act se verificó con govinfo (BILLSTATUS a 17-sep); no hay datos más recientes.
- **Texto íntegro de la opinión de ESMA del 8-oct**: solo se ve el titular; el plazo del 8-ene-2027 depende de la prensa.
- **Debut y primera cotización de XRPN**: no hay comunicado de Evernorth ni datos de Nasdaq.
- **Convalidación del RDL 29/2026** y la noticia de elecciones el 29-nov-2026 con las Cortes disueltas: solo prensa.
- **No revisado en fuente primaria:** ITP por comunidad, bonificaciones autonómicas de Patrimonio y Sucesiones, ITSGF (carácter indefinido y escala), sanciones del 720, ficha del MSCI World, cifras de SoSoValue y rwa.xyz, precios de Yahoo y del oro LBMA, IPV del INE, decisión exacta del BCE en junio, informe de Fitch sobre España y cifras de RLUSD del 9-oct (el ledger solo da el valor actual).
- **Cifras históricas de los dossiers** (velas de Kraken, prueba de estrés, series de G5 y G9): se ha comprobado su coherencia interna y aritmética, no los datos de origen.
