# Auditoría Opus del lote 14-15-nov-2026 (explorador/ y Órbita)

Fecha: 15-nov-2026 · Alcance: commits af80682..d1cde1b (29 archivos de explorador/ y scripts/) · Solo lectura: no se ha editado nada aparte de este informe.
Método: se leyeron los JSON nuevos y los scripts `leer_*.py`; se cotejaron 33 cifras o hechos contra la fuente original (APIs oficiales con curl, 10-Q de EDGAR y webs de las notas de prensa). No hizo falta Chrome. El directorio CCIP se pinta con JavaScript y no se pudo leer sin navegador.

## 1. Cotejo con la fuente (33 comprobaciones)

| # | Dato en el repo | Fuente leída | Resultado |
|---|---|---|---|
| 1 | Deuda EE. UU. 40,609 billones $ (12-nov) | fiscaldata debt_to_penny | Confirmado |
| 2 | En manos del público 32,824 billones $ | ídem | Confirmado |
| 3 | Tipo medio de la deuda negociable 3,570 % (oct-26) | avg_interest_rates | Confirmado |
| 4 | MTS oct-26: ingresos 368,9 / gastos 773,0 mil M$ | mts_table_1, línea 16 (FY2027) | Confirmado (déficit 404,1). El script coge bien la fila del nuevo año fiscal. |
| 5 | Tipo Fed 3,88 % (oct-26) | BIS WS_CBPOL (punto medio 3,875) | Confirmado |
| 6 | Tipo del BCE 2,5 % (depósito) | BIS WS_CBPOL XM (facilidad de depósito desde el 18-sep-2024) | Confirmado |
| 7 | BoJ 1,25 % | BIS (desde el 24-sep-2026) | Confirmado |
| 8 | China 3,0 % | BIS (LPR a 1 año) | Cifra confirmada, pero la etiqueta «tipo oficial» no aclara que es la LPR y no el repo a 7 días |
| 9-11 | Fed: WALCL 6.758,9 · TGA 914,4 · RRP 0,152 mil M$ → neta 5.844,3 | FRED | Confirmado (el RRP ya es 0,325 el 13-nov: es más reciente, no un error) |
| 12-15 | MiCA: 407 CASP, 26 emisores EMT (51 filas), 216 no conformes, DE 130 | CSV de ESMA | Confirmado |
| 16 | IPV España 2025T4: índice 186,75, +12,9 % | INE Tempus IPV769 | La cifra existe, **pero la serie está descontinuada** (ver H1) |
| 17 | IPVA alquiler: último año 2020 | INE IPVA5 | La cifra existe, pero no sirve como dato actual (ya avisado en C283; la vista no lo advierte) |
| 18 | XRPZ 30-sep: 27.000.000 acciones, NAV 16,28, 439.606.153 $ | 10-Q en EDGAR | Confirmado |
| 19 | XRPC 30-sep: 23.350.000, NAV 15,79, 368.656.616 $ | 10-Q en EDGAR | Confirmado |
| 20 | GXLM 30-sep: 1.440.900, NAV 18,63, 26,848 M$, 118,5 M XLM | 10-Q en EDGAR | Cifras confirmadas. **Es un fideicomiso en OTCQX, no un ETF** (ver H4) |
| 21 | Canary HBR: CERT y 8-A12B el 27-oct-2025, 424B3 el 28-oct-2025 | Listado de EDGAR del CIK 2039458 | Confirmado; subir a P es correcto |
| 22 | CCTP: Avalanche 1, Polygon PoS 7, XDC 18, Plume 22; BNB solo USYC; sin Hedera ni Algorand | developers.circle.com | Confirmado (BNB Smart Chain = dominio 17) |
| 23 | Visa añade Polygon (29-abr-2026) | investor.visa.com | Confirmado |
| 24 | Ondo/Kinexys/Mastercard/Ripple, pata XRPL en menos de 5 s (6-may-2026) | ondo.finance | Confirmado (parte interesada) |
| 25 | GAVA cotiza desde el 11-mar-2026 | The Block, 12-mar ("began trading on Wednesday"; el 11-mar-2026 fue miércoles) | Confirmado [S] |
| 26 | XDC 2.0: bloque cada 2 s, finalidad de 3 bloques, 6 s | xdc.org | Confirmado (parte interesada) |
| 27 | XDC Ventures anuncia la compra de Contour (22-oct-2025) | EZ Newswire | Confirmado como **anuncio** (ver H6) |
| 28 | Starfish de IOTA en la red principal el 23-abr-2026 | blog.iota.org | Confirmado |
| 29 | T-REX Ledger; Apex, 100 mil M$ para jun-2027 | polygon.technology, 18-mar-2026 | Confirmado (es un objetivo, y así está escrito) |
| 30 | Recompensas de staking de Algorand, 23-ene-2025 | algorand.co | Confirmado |
| 31 | Quantoz EURQ/USDQ en Algorand con Folks, 3-abr-2025 | quantoz.com | Confirmado |
| 32 | DefiLlama: stablecoins en XRPL 839 M$, Stellar 398-400 M$ | stablecoins.llama.fi | Confirmado (la diferencia es solo de hora) |
| 33 | Plume: TVL 0 y stablecoins null | DefiLlama | **No confirmado**: falla el mapeo (ver H2) |

Sin verificar: los carriles y tokens de XDC en el directorio CCIP (la página se pinta con JS), el 2 % de emisión de POL (PIP-26), Archax/Hedera, ADAPT/IOTA y el registro de Plume como agente de transferencia. Los dos últimos ya llevan [S] o «socios sin confirmar».

Balance: 30 confirmados (2 de ellos con una salvedad de etiqueta), 1 con un error de datos (Plume) y 2 cifras reales pero caducadas presentadas como «último dato» (IPV e IPVA).

## 2. Incoherencias (HECHOS)

- **H1. IPV de España caducado.** En sep-2026 el INE cambió de base. La serie de base 2015 (IPV769…) se acaba en 2025T4, y la nueva tabla 79563 (IPV1209 índice, IPV1376 variación anual) ya llega a **2026T2: +12,2 %**. El explorador muestra 2025T4, +12,9 %, como el dato actual, y el informe C283 dice que es el «último periodo publicado», lo cual es falso.
- **H2. Mapeo de DefiLlama incorrecto.** En `/v2/chains`, «Plume» es un nombre antiguo con TVL 0. La red viva es «Plume Mainnet» (TVL ≈ 1,1 M$ y stablecoins ≈ 10,8 M$). En el caso de IOTA, las stablecoins están en «IOTA EVM» (≈ 0,4 M$) y el repo pone null.
- **H3. El IPC de OCDE/BIS no es comparable entre países.** España, Francia, Italia, Países Bajos y Polonia están a 2025-12, Sudáfrica a 2025-01, Japón a **2021-06** y Rusia a 2022-03, todos en la misma columna. El propio script detecta que había un dato de España más reciente (`comparacion_frescura`: antes hasta 2026-10, ahora 2025-12), pero aun así publica el viejo.
- **H4. GXLM figura como ETF.** El 10-Q dice que cotiza en OTCQX y que no está registrado en ninguna bolsa. Aun así está en `etfs[]`, y la vista se titula «ETF de XRP y XLM», un título que tampoco encaja porque ya hay fondos de BTC (IBIT, FBTC y EZBC).
- **H5. Móvil desfasado en liquidez.** `docs/movil/data.json` → `liquidez.manual` incrusta la copia del 4-nov (Japón M2 sep-26 +2,0 %; China [S] de prensa, con el aviso «valores a mano…»). En cambio, `liquidez-manual.json` ya tiene Japón oct-26 +1,7 % [P] y China [P] del PBoC. Ocurre porque `actualizar_paneles.py` mete el manual dentro de paneles.json, y ese archivo no se ha regenerado.
- **H6. XDC-Contour aparece con dos niveles y dos fechas.** El hito está en P (22-oct-2025, «anuncia»), mientras que la ficha `cumplimiento` sigue en V (e27, 23-oct-2025) y dice «compró», en firme. Además, la ficha `credito` de XDC está en **P** con bancos (MUFG, ICBC, Bank of China, DBS) que solo constan en la web de TradeFinex, una parte interesada. Debería ser [VERIFICAR]/S.
- **H7. Frescura.** `frescura_explorador.py` mide la fecha de lectura (`leido`/`generado`), no la del dato, aunque su descripción diga «fecha del DATO». Por eso ocde-bis sale en verde con IPC de 2021 y espana-energia con IPVA de 2020. Además, `_actualizado` no está entre las claves que reconoce, así que cadenas-onchain sale en gris.
- **H8. GDELT llama «media 90 d» a algo que no lo es.** La serie tiene 68 días, no 90: la «media 90 d» es en realidad de 68 días, y la «media 30 d» son los últimos 30 puntos, no los últimos 30 días naturales.

## 3. Fragilidad de los scripts

- Certificados: **no** hay `verify=False`, `CERT_NONE` ni contextos sin verificar en ningún `leer_*.py`. Correcto.
- Lo único en http plano es el PBoC (`leer_liquidez.py:100`, `http://www.pbc.gov.cn`): no está cifrado ni se comprueba la integridad.
- Varios scripts **sobrescriben los datos buenos aunque falle la lectura**: `leer_onchain.py:80` escribe todo a null si cae DefiLlama y no tiene campo `fallos`; `leer_gdelt.py:84` escribe con temas/países vacíos si GDELT devuelve 429 sin `--completar`; `leer_fiscal_eeuu.py:107` escribe aunque fallen todos los bloques, y la vista se queda sin `deuda`. Lo hacen bien `leer_espana_energia` y `leer_liquidez` (conservan el dato anterior y lo marcan) y `leer_esma_mica` (solo escribe si hay CASP).
- `leer_ocde_bis.py:44-55` (`ultimos`) acepta cualquier observación por antigua que sea, sin un umbral.
- `leer_espana_energia.py:24-31` usa códigos fijos de series del INE. Cuando el INE cambia de base, el script sigue «funcionando» pero da datos viejos, sin dar error.
- `leer_esma_mica.py`: depende de los nombres de columna `ae_*`/`ac_*` sin comprobarlos. Si ESMA los cambia, los conteos salen a 0 o vacíos en silencio. La página ya enlaza un fichero de muestra de MIDAS (oct-2026), señal de que el registro va a migrar.
- `leer_etf_flujos.py:43-44` calcula el flujo entre dos instantáneas cualesquiera. Si se suma una lectura diaria a XRPZ/XRPC/GXLM, que tienen un 10-Q trimestral, saldría como «flujo diario» la diferencia de un trimestre. Además, FBTC usa acciones derivadas y Bitwise mezcla un NAV del 11-nov con acciones del 12-nov.
- `leer_calendario_oficial.py`: el BLS se lee de una copia `.ics` hecha a mano con Chrome (curl da 403), así que caducará sin avisar.

## 4. Correcciones priorizadas (máx. 15)

1. `scripts/leer_espana_energia.py:24-28` y `:105-114`: cambiar a la tabla INE 79563 (IPV1209 y los códigos de las CCAA en base nueva) y usar la variación anual oficial (IPV1376) en vez de calcularla. Regenerar el JSON y corregir el informe C283 (línea 9).
2. `explorador/vistas.html:1864-1868`: no mostrar el IPVA como dato vigente (es de 2020); ocultarlo o poner un aviso «serie hasta 2020».
3. `scripts/leer_onchain.py:12`: `"plume": "Plume Mainnet"`; añadir en `ALIAS_STABLE` el alias `IOTA`→`["IOTA","IOTA EVM"]`.
4. `scripts/leer_onchain.py:80`: no escribir si `chains` y `st` vienen vacíos; añadir `fallos` y conservar el dato previo.
5. `scripts/leer_ocde_bis.py:44-55`: descartar observaciones con más de 6 meses (12 para las trimestrales) y dejarlas en null con su motivo. Hoy afecta al IPC de ES/FR/IT/NL/PL/ZA/JP/RU y al tipo de AR.
6. `scripts/frescura_explorador.py:8`: añadir `_actualizado`; y, para que sea verdad que mide «la fecha del dato», usar el campo `fecha`/`ultimo_periodo` de cada serie cuando exista, no `leido`/`generado`.
7. `explorador/etf-flujos.json` (entrada GXLM) y `explorador/vistas.html:1176` y `:2030`: marcar GXLM como «fideicomiso OTC, no ETF» y renombrar el bloque a «Fondos cotizados de XRP, XLM y BTC».
8. `scripts/leer_etf_flujos.py:43-44`: calcular el flujo solo si las dos instantáneas son de días hábiles consecutivos y de la misma fuente o tipo; si no, `flujo_usd: null` con el motivo.
9. `explorador/cadenas.json:3295-3300` (XDC `cumplimiento`): pasar a «anunció la compra», fecha 2025-10-22 y enlace a EZ Newswire, para alinearlo con el hito en P.
10. `explorador/cadenas.json:3441-3446` (XDC `credito`): bajar a S o marcar los nombres de bancos con [VERIFICAR] (la única fuente es la web de TradeFinex, parte interesada).
11. `scripts/leer_gdelt.py:44-50`: rellenar los días que faltan, calcular las medias por fecha natural (30 y 90 días) y llamar `media_periodo` a la de 68 días, o exigir al menos 80 días.
12. `scripts/leer_gdelt.py:84` y `scripts/leer_fiscal_eeuu.py:103-107`: si todo falla, no sobrescribir; conservar los bloques previos con `conservado_sin_actualizar`.
13. Móvil (`docs/movil/data.json` → `liquidez.manual`): regenerar paneles.json con `actualizar_paneles.py`, o que `construir_movil.py` lea `liquidez-manual.json` directamente en vez de la copia que va dentro de paneles (`actualizar_paneles.py:678`).
14. `explorador/ocde-bis.json`, China `tipo_oficial`: añadir la nota «LPR a 1 año (referencia del BIS), no repo a 7 días» en `scripts/leer_ocde_bis.py`, donde se escribe la nota del BIS.
15. `scripts/leer_liquidez.py:100`: probar `https://www.pbc.gov.cn`; si no responde, dejar anotado en el JSON que la lectura es por http sin cifrar.

## OPINIONES y límites

- [Opinión] Lo más grave son H1 y H3: cifras «P» bien citadas pero caducadas que se presentan como dato actual. Es justo el tipo de error que la regla «titulares con umbral» intenta evitar.
- [Opinión] Subir Hedera ETF a P (EDGAR) está justificado. Subir XDC-Contour a P solo vale para «anunció»: no prueba que se cerrara la compra ni que haya actividad.
- Límites: no se abrieron en navegador las páginas SPA de los emisores (Bitwise, 21Shares, iShares, Fidelity, Grayscale); sus cifras se revisaron solo por coherencia interna (acciones × NAV ≈ AUM, y un precio de XRP implícito de ≈ 1,02-1,03 $ igual en Bitwise, TOXR y GXRP), sin cotejarlas con la fuente.
