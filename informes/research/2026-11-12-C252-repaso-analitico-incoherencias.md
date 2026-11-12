# C252 · Repaso analítico: incoherencias entre informes y explorador, conexiones y cifras cruzadas (12-nov-2026)

Informativo; no es una recomendación de compra ni de venta. Modelo: Fable 5.2.

**Alcance y límite principal.** Repaso hecho **solo con lo que ya hay en el repo**: 1.000 hechos de `informes/hechos/lote-01…21.jsonl` (685 de nivel P), los JSON de `explorador/` leídos el 11-nov-2026 21:30 UTC y los informes del 10 al 12-nov. **Esta sesión no abrió ninguna fuente externa**: los niveles [P]/[S] son los que puso cada informe en su día, no una verificación nueva. Todo lo que aquí se propone corregir contra la fuente original va marcado [VERIFICAR]. Los porcentajes y restas son **cálculo propio** sobre cifras del repo.

Herramientas: `python scripts/cobertura_hechos.py` (ver fallo en §6), `python scripts/auditar_cobertura.py` → `research/COBERTURA.md` (regenerado hoy), `research/CRUCE-HECHOS.md` (9-nov).

## 1. Resumen en 8 líneas
1. **IPC de EE. UU. de octubre: el dato está en el repo desde el 10-nov y cuatro informes diarios posteriores lo dan por «no leído».** Es la incoherencia más clara (§2.1).
2. **El «Brent» del repo mezcla contratos**: diciembre (expiró el 30-oct a 117,64 $) y enero (113,43 $ ese día). De ahí salen cierres distintos para el mismo día y caídas semanales de −16 % que con el mismo contrato son −14 % (§2.2).
3. **Tres «medias de septiembre» del Brent incompatibles** (114,2 $, 102,02 $ y 91 $ implícitos): la tercera es un error de redacción copiado en 4 informes (§2.3).
4. **PCE subyacente de septiembre mal etiquetado en un hecho P** (3,6 % es el general; el subyacente es 3,1 %) (§2.4).
5. **Línea de tiempo con dos entradas del 4-nov que se contradicen** sobre el Senado de EE. UU., y tres composiciones previas de la Cámara que no suman 435 (§2.5).
6. **El planning marca como «✓ cubierto» eventos cuyo dato no se leyó** (STEO de noviembre de la EIA) (§2.6).
7. Conexión nueva sin informe: **las primas frente a Alemania se abrieron en octubre** (Francia +51 pb, Italia +38 pb, España +20 pb) según el propio panel de bonos (§3.1).
8. Conexión nueva sin informe: **las stablecoins en Stellar bajan un 56 % en un mes** en el panel (941 → 415 M$) y el total en dólares un 7 % (§3.2). [VERIFICAR] antes de darlo por hecho.

## 2. Incoherencias (hechos del repo que no cuadran entre sí)

### 2.1 IPC de EE. UU. de octubre: leído en W01b/W01c, «[VERIFICAR]» en los diarios
- HECHO [P según W01b y W01c, BLS USDL-26-1685 y FRED, 10-nov-2026]: general **+0,4 %** mensual (0,351 % sin redondear), subyacente **+0,3 %** (0,296 %); **sin tasa interanual oficial** porque la BLS no recogió precios en octubre de 2025. `informes/research/2026-11-10-W01b-ipc-dato.md` y `…W01c-ipc-fred-mercado.md`.
- INCOHERENCIA: `informes/2026-11-10-cierre.md`, `2026-11-11-apertura.md`, `2026-11-11-cierre.md` y `2026-11-12-apertura.md` (y sus R00) repiten «cifra del IPC de octubre: [VERIFICAR]» y «causas de los movimientos: [VERIFICAR]». W01c ya documentaba la reacción (10 años de 4,90 % a 5,02 % intradía, DXY +0,57 %, FedWatch del 9-dic: 84 % → 100 % de subida, con 11,5 % para +50 pb [P, CME leído en Chrome]).
- Causa probable (opinión): la rutina R00 busca en la web y no consulta `informes/research/` del mismo día.
- En el explorador: `paneles.json › inflacion` muestra EE. UU. `interanual: null` con fecha 2026-10 y `anterior: 3,7`. Es **correcto** (no hay interanual oficial), pero en pantalla un hueco sin explicación parece un fallo. `indicadores-manual.json › US › ipc` sigue en 3,7 % (sep-2026): correcto como último interanual oficial.
- Matiz de coherencia interna que sí cuadra: gasolina interanual 27,4 % (ago) → 34,2 % (sep) → 37,4 % (oct). El hecho de T17 («la gasolina subió 34,2 %») no dice que es interanual; otros dos hechos dan +9,1 % **mensual** para el mismo mes. No se contradicen, falta la etiqueta.

### 2.2 Brent: contratos mezclados (explica varias verificaciones abiertas)
Dato que lo explica [S, CNBC, en `2026-11-02-cierre.md`]: el contrato de diciembre expiró el 30-oct en **117,64 $** y el de enero cerró ese día en **113,43 $** (4,21 $ de diferencia).
| Día | Cifras distintas en el repo | Informe |
|---|---|---|
| 28-oct | cierre 110,56 $ (−2,92 %) frente a 115,32 $ usado como cierre previo al día siguiente | `2026-10-28-cierre.md` / `2026-10-29-cierre.md` |
| 30-oct | 112,33 $ · 114,07 $ · 113,43 $ (enero) · 117,64 $ (diciembre) · spot EIA 120,15 $ | cierre 30-oct, W10 30-oct, cierre 2-nov, W10 7-nov |
| 23-oct | cierre 111,97 $ / 111,7 $; máximo intradía «sobre 116 $» frente a 114,4 $ | cierre 23-oct, W10 25-oct, C29, `hitos_petroleo.json` |
| 3-nov | cierre previo usado el 4-nov: 104,28 $, 103,60 $ o 104,06 $ | cierres 3 y 4-nov, C132 |
- Efecto en los porcentajes (cálculo propio): cierre del 6-nov 97,83 $ frente a 113,43 $ (mismo contrato) = **−13,8 %**; frente a 117,64 $ = −16,8 %. El «−16 % en la semana» de W01b y W10 [S, CNBC/Reuters] y el «19 % por debajo» del 4-nov comparan contratos distintos. Con el mismo contrato, el 4-nov es −16,3 %.
- El hecho «Futuro continuo del 23-oct: Brent 111,97 $» figura como **P con fuente EIA**, pero es un futuro (Yahoo): nivel y fuente mal puestos. Es además la verificación pendiente que el planning repite 4 veces.
- `hitos_petroleo.json` solo llega al 26-oct: no recoge la caída del 2 al 6-nov (de 113,43 a 97,83 $), que es el mayor movimiento del periodo.
- Propuesta: en cada cifra de Brent, anotar contrato (mes) o «spot EIA». No hace falta fuente nueva para arreglar las tablas, solo etiquetar.

### 2.3 Tres medias de septiembre del Brent que no pueden ser a la vez
- 114,2 $ (media del spot diario EIA/FRED DCOILBRENTEU, cálculo del dossier del 9-oct) [P].
- 102,02 $ (serie mensual del FMI en FRED, POILBREUSDM, `2026-11-04-C109`) [P]. 12 $ de diferencia para el mismo mes: [VERIFICAR] qué mide cada serie.
- 91 $ implícitos: T18 (24-oct), W10 (2 y 10-nov) y el dossier del 9-oct dicen que el STEO prevé 105 $ en el 4T, «+14 $ **vs. septiembre**». Los informes R46 y `2026-10-09-macro.md` dicen «+14 $ **respecto a la STEO anterior**». La segunda lectura es la coherente (la revisión es de la previsión, no del precio). **Error de redacción heredado**, [VERIFICAR] en eia.gov y corregir en el hecho del lote.
- Además, el STEO de octubre (105 $ de media en el 4T) queda viejo frente al mercado: spot EIA 107,03 $ el 3-nov y futuro ~98 $ el 6-nov.

### 2.4 PCE subyacente de septiembre
- Hecho P de `2026-11-02-C31-inflacion.md`: «PCE **subyacente** 3,6 % interanual (anterior 3,1 %); m/m 0,5 %».
- Tres informes con la nota de la BEA del 29-oct [P]: general 3,6 % (+0,5 % m/m), **subyacente 3,1 %** (+0,3 % m/m). El hecho de C31 mezcla el general con el subyacente. No ha llegado al explorador (el panel dice «PCE 3,6 %, anterior 3,4 %», bien). Corregir el hecho del lote.

### 2.5 Elecciones de EE. UU.
- `datos.json › movimientos` tiene dos entradas con fecha **2026-11-04**: «el Senado sigue abierto» y «los demócratas ganan la Cámara y el Senado (54–44 con 2 sin declarar)». La segunda usa datos de AP del 8 al 10-nov: está mal fechada, no es falsa. `auditar_cobertura.py` ya la marca como posible repetición.
- Composición de la Cámara **antes** de las elecciones: 218 R – 212 D – 4 vacantes (suma 434) [S, Ballotpedia]; 219–214 (suma 433) [S, CBS]; **218 R · 214 D · 1 I · 2 vacantes (suma 435) [P, clerk.house.gov, leído 11-nov]**. Vale la tercera; las otras dos siguen en los lotes sin nota.
- Resultado [S, sin certificar]: Cámara 254–162 con 19 sin adjudicar (AP) frente a 259–176 (NBC); Senado 54 (con 2 independientes) – 44 – 2. Cuadra con «+7 escaños» desde 47. `elecciones.json` lo deja bien en `en_recuento`; el planning lo da por «✓ revisado (hecho)» mientras C58 sigue esperando el recuento oficial.

### 2.6 «✓ cubierto» en el planning no significa «dato leído»
- STEO de la EIA (10-nov): el planning dice «✓ cubierto por W10 del 2026-11-10», pero `2026-11-10-W10-energia.md` (línea 6) dice que la edición de noviembre **no se pudo leer**. `COBERTURA.md` lo confirma por otra vía: la voz v061 (EIA) sigue «pendiente» con plazo vencido.
- Corea, tokenización: celda de la Matriz con «próxima fecha» 11-nov ya pasada (fin del plazo de comentarios de la FSC) sin anotar qué ocurrió.
- Propuesta: que `construir_seguimiento.py` distinga «rutina ejecutada» de «dato leído» (por ejemplo, exigir una marca en el informe).

### 2.7 Tipos oficiales: fechas con dos convenciones
- Fed: «subió el 16-sep» (comunicado; la mayoría de los hechos) y «el 17-sep» (fecha efectiva en FRED; varios hechos y `tipos_vivos`). El panel lo avisa en su nota; los hechos no.
- El hecho de `2026-11-09-auditoria-total.md` «BCE (16-sep), Fed (17-sep) y BoJ (18-sep)» mezcla convenciones: BCE decidió el 10-sep (efectivo el 16), Fed decidió el 16 (efectivo el 17), BoJ decidió el 18 (efectivo el 24).
- Banco de Inglaterra: un hecho P dice «antes 3,75 % **desde el 17-sep**» (`2026-11-06-cierre.md`), pero el 17-sep el banco **mantuvo** el 3,75 % (6-3). La fecha en que llegó a 3,75 % no consta en el repo: [VERIFICAR] en la serie IUDBEDR.
- Banco de Japón, venta de ETF: tres hechos y `regulacion.json` dicen que **sube** de ~330.000 a ~860.000 M¥ al año desde ene-2027; `2026-10-31-W03-C-ue-hk-jp-br-verificado.md` dice «**reducir** ventas». Tres contra uno y el explorador está en «sube»: corregir el hecho de W03-C ([VERIFICAR] en boj.or.jp si se quiere cerrar del todo).
- Panel y Matriz coinciden en todos los tipos (lo confirma `COBERTURA.md`). Frescura: Corea con `dato_de` 8-oct, India e Indonesia 19-oct (más de 3 semanas).

### 2.8 XRP, XLM y ETF
- **ETF de XRP en EE. UU.**: el lote da 2.178 M$ (30-sep) como **P** («emisor 21Shares»); `datos.json` dice que esa cifra «no se pudo rastrear hasta su origen» y usa ~1.430 M$ (22-oct) y 1.560 M$ (8-oct) [S, SoSoValue]. Mismo dato, nivel P en un almacén y «no rastreable» en otro: bajar el hecho a S o [VERIFICAR].
- **Evernorth (XRPN)**: un hecho de `2026-10-28-W05` lo llama «el **ETF** XRPN». Según el 8-K [P] es una sociedad cotizada tras fusión con una SPAC, no un ETF. El explorador lo trata bien («cotizada»).
- **Coincidencia a vigilar**: «1.560 M$» aparece como oferta total de RLUSD a 30-jun [S, KuCoin/MEXC] y como activos de los ETF de XRP a 8-oct [S, SoSoValue]. Puede ser casualidad; [VERIFICAR] que una no se copió de la otra (la de RLUSD está en `voces.json`).
- **RLUSD en XRPL**: 1.140 M (ledger, 9-oct) [P], 1.034 M (auditoría del 13-oct) y 874 M$ en el panel (DefiLlama, 11-nov) [S]. Bajada del 9 % en 4 días sin explicar y fuentes distintas: [VERIFICAR] en el ledger.
- **Autorización MiCA de Ripple**: dos fechas para un hecho (29-jun en el registro de ESMA; 6-jul en la nota de Ripple). Y dos descripciones: la nota de Ripple dice «CASP **completa**»; el registro, cambio y transferencias **sin custodia**. Sesgo de fuente: la nota de prensa es promoción de la empresa; vale el registro.
- **Escrow de Ripple**: `datos.json` muestra 31.400 M XRP (13-oct); ya hubo liberación el 1-nov. Cuadra con 32.600 M a 30-jun (ritmo neto de ~300 M/mes, cálculo propio) pero está un ciclo atrasado.
- **RWA en Stellar**: 3.996 M$ (29-ago, Dune vía Cointelegraph), 3.550 M$ (7-oct, rwa.xyz) y **6,9 M$** en `paneles.json › rwa` (DefiLlama, solo TVL DeFi). La nota del panel lo explica, pero la cifra sola confunde: factor 500 entre metodologías.
- **Enmiendas del XRPL**: el hecho «107 enmiendas, 97 activas» lleva fecha 20-abr-2026 (la de la hoja de ruta), pero es un estado de octubre (95 activas hasta el 9-oct, 97 después). Fecha del hecho mal atribuida.
- Calendario: el voto de Protocol 30 de Stellar (23-nov) está **dos veces** en el planning.
- Mínimo de XRP del 10-nov: R00 dice 1,064 $; W01c registró 1,0485 $ a las 17:30 UTC del mismo día [S, Yahoo].

### 2.9 España
- Previsiones: Banco de España [S, nota 2026-94 vía prensa] PIB 2,6 % (2026) y 2,2 % (2027), déficit 2,3 %; AIReF [P, 4-nov] **los mismos 2,6 % y 2,2 %** y déficit 2,8 %; FMI [P] 2,5 % y 1,8 %. Que dos organismos den cifras idénticas de PIB puede ser cierto o una mezcla al resumir: [VERIFICAR] la nota del Banco de España (es la que está en S). La diferencia de déficit (2,3 % frente a 2,8 %) es de 0,5 puntos del PIB.
- IPV del 2T-2026: INE +12,2 %, Eurostat 12,1 %. Diferencia de una décima entre fuentes oficiales; no es error.
- Sueldos: secretario de Estado 89.917 € (cálculo propio de C68B) por encima de ministro 85.513 € [P]. Ya está abierto en C68.

## 3. Conexiones entre temas (cifras del explorador; la interpretación es opinión)

### 3.1 Primas de riesgo europeas: se abren en octubre y no hay informe
`paneles.json › bonos › mensual10` (media mensual del 10 años, BCE) [P]:
| País | Sep-26 | Oct-26 | Prima vs Alemania sep → oct (cálculo propio) |
|---|---|---|---|
| Alemania | 3,473 % | 3,416 % | — |
| España | 3,927 % | 4,066 % | 45 → **65 pb** (+20) |
| Italia | 4,362 % | 4,680 % | 89 → **126 pb** (+38) |
| Francia | 4,440 % | 4,890 % | 97 → **147 pb** (+51) |
- Francia paga más que Italia (21 pb). El TEC 10 de la AFT en `bonos-manual.json` (4,7–4,9 % en octubre) [P] es coherente con el 4,89 %, pero ese archivo se leyó el 22-oct.
- Ningún informe de noviembre menciona este movimiento (W02 del 10-nov habla de calendario y de Moody's Aa3 negativa [S]). Subasta de España del 5-nov: 3,345 % marginal frente a 2,949 % la anterior [S, sin leer el PDF].
- A la vez, el diferencial de alto rendimiento de EE. UU. está en 3,48 % (panel `spreads`, leído el 8-nov), por debajo del umbral de aviso de 5.
- Caso bajista (opinión): tipos al alza de BCE, Fed, BoE, Canadá, Australia y Suecia más déficit francés = más prima para la deuda periférica y de Francia. Caso alcista (opinión): el crédito privado no muestra tensión y el petróleo cae. [ESPECULACIÓN] en ambos.

### 3.2 Liquidez cripto: menos stablecoins mientras suben los tipos
| Dato | 9-oct [S, DefiLlama] | 11-nov [S, panel] | Cambio (cálculo propio) |
|---|---|---|---|
| Stablecoins ligadas al dólar | 313.300 M$ | 290.774 M$ | **−7,2 %** |
| USDT | 184.200 M$ | 175.670 M$ | −4,6 % (el panel da −4,54 % a 30 días) |
| Stablecoins en XRPL | 1.212 M$ | 966 M$ | −20 % |
| Stablecoins en Stellar | 941 M$ | 415 M$ | **−56 %** |
- [VERIFICAR] la caída de Stellar antes de usarla: puede ser un cambio de cómputo de DefiLlama (agregador) y no una salida real. Fuente para cerrarlo: Horizon o Circle.
- En el mismo periodo (cálculo propio sobre precios del repo): XRP 1,358 $ (13-oct) → 1,0485 $ (10-nov) = −23 %; XLM 0,1900 → 0,1427 = −25 %; BTC 83.309 → 72.815 = −13 %. Tipo a 10 años de EE. UU.: 4,859 % el 6-nov [S, Yahoo] y 4,98 % el 10-nov [P, Tesoro]; FedWatch al 100 % de subida el 10-nov.
- Los paneles `depeg` y `spreads` son del **8-nov** (los demás, del 11-nov): el aviso de «4 stablecoins despegadas» del R00 del 12-nov se apoya en un dato de 4 días.

### 3.3 Petróleo físico frente a futuro, y Ormuz según quién lo mida
- Diferencia spot EIA − futuro: ~21 $ el 6-oct (125,44 frente a ~104), 6,7 $ el 30-oct, **2,75 $ el 3-nov** (107,03 frente a 104,28). La prima del físico casi desaparece en un mes. C74 la dejaba «sin explicar»; W10 la atribuye a fletes. [ESPECULACIÓN]: menos tensión física.
- Tensión entre fuentes oficiales: la AIE [P, OMR de octubre] cifra el flujo por Ormuz en **10,9 mb/d** (más de la mitad de lo normal) y CENTCOM dice que pasa el 95 % de los buques; PortWatch [P] cuenta **3–4 barcos al día frente a 78** en febrero (≈5 %). No pueden describir lo mismo. Hipótesis sin fuente en el repo: transpondedores apagados o transbordos fuera del estrecho. [VERIFICAR]; mientras tanto, el panel `ormuz` solo enseña la versión de PortWatch.

### 3.4 España: tres cruces que salen de sumar lo que ya hay
- Déficit de 2025 = gasto 766.296 M€ − ingresos 725.655 M€ = **40.641 M€** (2,4 % del PIB) [P, Eurostat]; intereses 40.432 M€ [P, Eurostat]. **El déficit de 2025 es prácticamente igual a la factura de intereses**: saldo primario ≈ −0,2 mil M€ (cálculo propio).
- Deuda: 1.762.936 M€ = 101,4 % del PIB; el panel usa PIB de 1.738.374 M€ y cuadra. CCAA +3,6 % interanual: cuadra con 355.241 / 342.799.
- Hipotecas nuevas al 2,99 % (sep) [P, BdE/BCE] por **debajo** del Euríbor a 12 meses (3,247 %) y casi un punto por debajo del bono a 10 años (3,927 %). Es un retraso habitual (se firman con precios pactados meses antes), pero indica hacia dónde irían los tipos nuevos si el Euríbor no baja [ESPECULACIÓN].
- Revalorización de pensiones 2,7 % [P, RDL 3/2026] = IPC medio de 2025 +2,67 % [P, INE, C69]: cuadra.
- Gasto por habitante 8.403 → 8.617 €, −0,5 % real: rehecho y cuadra (+3,6 % nominal, +1,0 % población, deflactor 3,05 %).

## 4. Cifras rehechas que **sí** cuadran
Adquisiciones de Ripple con precio (1.250 + 1.000 + 250 + 200 = 2.700 M$) · XRP de Ripple 37.656 M + distribuidos 62.329 M = 99.985 M · CME 7.613 contratos × 50.000 = 380,65 M XRP · Goldman 87,4 de 179,3 M$ = 48 % · Brent 2-nov −7,6 % desde 113,43 $ · RWA Stellar +360 % desde 868,8 M$ · subyacente de EE. UU. +2,14 % ene→oct ≈ 2,9 % anualizado · Cámara AP 254 + 162 + 19 = 435.

## 5. Cobertura: dos medidas del repo que dan respuestas opuestas
| Medida | Hechos P «cubiertos» | Qué compara |
|---|---|---|
| `research/CRUCE-HECHOS.md` (9-nov) | 101 de 685 (15 %) | solo la Línea de tiempo |
| `cobertura_hechos.py` (hoy) | 474 «está», 146 «dudoso», 65 «falta» (69 % / 21 % / 9 %) | todos los JSON de `explorador/` |
- Peor ámbito: **xrp** (21 está, 19 dudoso, 22 falta de 62). Después empresa (11/10/2) y xlm (9/7/3). Mejor: tipos (105 de 116) y deuda (38 de 49).
- Los lotes de hechos acaban el 9-nov: lo publicado del 10 al 12-nov (IPC de octubre, FedWatch, elecciones actualizadas) no entra en ninguna de las dos medidas.
- `COBERTURA.md` (hoy): 21 de 190 movimientos sin nivel, 26 sin informe; 5 países con ficha y 0 hechos (Indonesia, Egipto, Etiopía, Venezuela, Cuba); 9 celdas P recientes de la Matriz sin hecho cerca; «Depósitos tokenizados» lleva 309 días sin movimiento.

## 6. Fallos de herramienta vistos
- `python scripts/cobertura_hechos.py` **sin argumento falla** (`IndexError` en la línea 33): exige la ruta de salida. Hoy se ejecutó con una ruta temporal. Arreglo de una línea pendiente de tu OK (ruta por defecto).
- Bots con problema según el planning: «Paneles de datos» y «Verificación mensual»; coincide con `depeg` y `spreads` parados en el 8-nov y FRED sin respuesta para el PCE.

## 7. Correcciones propuestas (ninguna aplicada; no se tocó ningún JSON)
1. Diarios R00: enlazar W01b/W01c y quitar el [VERIFICAR] del IPC de octubre. Sin fuente nueva.
2. `datos.json`: refechar la entrada «54–44» del 4-nov a 8/10-nov. Sin fuente nueva.
3. Lotes de hechos: PCE subyacente (C31), «reducir» ETF del BoJ (W03-C), «ETF XRPN» (W05), «+14 $ vs. septiembre» (4 sitios), Brent 111,97 $ como P/EIA, nivel de los 2.178 M$.
4. Brent: etiqueta de contrato en tablas y `hitos_petroleo.json` hasta el 6-nov.
5. [VERIFICAR] con fuente: STEO de noviembre (eia.gov), stablecoins en Stellar (Horizon), RLUSD en el ledger, serie IUDBEDR del BoE, nota 2026-94 del Banco de España, flujo de Ormuz AIE frente a PortWatch.
6. Informe corto de primas de riesgo (dato ya en el panel) dentro de W02.

## Lecciones (máx. 5)
1. Los diarios no leen el research del mismo día: el dato existía y se marcó como pendiente cuatro veces.
2. «Brent» sin contrato ni tipo (spot/futuro) no es comparable entre días; la mitad de las verificaciones pendientes de petróleo salen de ahí.
3. Una frase mal resumida («vs. septiembre») se copia de informe en informe; conviene corregirla en el lote, que es de donde beben los demás.
4. «Cubierto» en el planning mide que la rutina corrió, no que el dato se leyó.
5. Las dos medidas de cobertura no son comparables; citar siempre cuál.

## Seguridad
Sin claves ni secretos. Sin red, sin workflows y sin API de Anthropic. Sin commit ni push. No se tocó `privado/`, `cerebro/` ni ningún JSON de `explorador/`. Único archivo regenerado por script: `research/COBERTURA.md`.

## Corrección posterior (C254, 12-nov-2026)
- **§3.2 y punto 8 del resumen, stablecoins en Stellar: la caída del 56 % no existe.** La serie histórica de DefiLlama da 392,4 M$ tanto el 9-oct como el 12-nov [S], y Horizon da 344,0 M de USDC [P]. Los 941 M$ de partida no cuadran con ninguna serie.
- §2.7, Banco de Inglaterra: el Bank Rate está en 3,75 % desde el 18-dic-2025 [P, IUDBEDR].
- §2.8, RLUSD: la bajada sí es real, 885,2 M en el ledger el 12-nov [P].
- §2.9, Banco de España: PIB 2,6 % y 2,2 % confirmados; déficit de 2026 del 2,6 % [P].
- Detalle y fuentes: `informes/research/2026-11-12-C254-verificaciones-repaso.md`.
