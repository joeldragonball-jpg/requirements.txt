# Guía G17: Cómo verificar noticias cripto (checklist para imprimir, 17-oct-2026)

> **Guía práctica, no es recomendación** de comprar ni vender nada. Resume lo que aprendimos en las sesiones de research del 14 al 17-oct-2026: las lecciones de `cerebro/documentos/patrones-de-bulos.md`, `fuentes-fiables-y-dudosas.md` y `catalizadores-xrp-xlm.md`, y las auditorías [R22](../research/2026-10-15-R22-auditoria-coherencia.md), [R31](../research/2026-10-17-R31-auditoria-coherencia-2.md) y [R38](../research/2026-10-17-R38-auditoria-numerica.md), más la corrección de [R21b](../research/2026-10-15-R21b-13f-segunda-pasada.md). **No hay ejemplos inventados**: cada error citado está documentado en el informe enlazado. Lo que «abre» o «no abre» es lo comprobado en esas fechas; las webs cambian [VERIFICAR antes de fiarse de la tabla]. Etiquetas: **[VERIFICAR]** = sin fuente primaria leída; **[ESPECULACIÓN]** = opinión o previsión; **cálculo mío** = aritmética propia sobre datos citados.

## 0. Resumen (5 líneas)
1. Casi ningún error que encontramos era un «bulo» puro: eran **cifras reales con la fecha, la serie, el intervalo o la base equivocados**, y varios eran **errores nuestros** al resumir.
2. La regla que más errores habría evitado: **toda cifra viaja con cinco cosas pegadas: fuente, fecha del dato, serie/métrica, ventana y etiqueta** (§1).
3. La fuente primaria casi siempre existe y muchas veces **sí se puede leer** (sec.gov con curl y User-Agent, Federal Register API, nodos XRPL y Horizon de Stellar, BLS, Fed); las que no abren están en la tabla (§2).
4. Los errores propios típicos: **el resumen es más fuerte que la tabla**, **«cero» tras buscar poco**, **horas convertidas a mano**, **totales que no son la suma**, **rótulos de intervalo inventados** (§3).
5. Cualquier cifra que vaya a pesar en una decisión se recalcula con un script de 10 líneas antes de citarla (§4).

---

## 1. Las 10 preguntas antes de creer una cifra

| # | Pregunta | Si la respuesta es «no» o «no sé» | Error real que la motivó |
|---|---|---|---|
| 1 | ¿Sé **quién** lo dice y si tiene interés (emisor, empresa, exchange, influencer)? | Etiquetar [PARTE INTERESADA] o tipo C/D | Ripple, SDF y 21Shares como fuente única de sus propias cifras (R31 §2) |
| 2 | ¿La **fecha del dato** es de hoy, o es un artículo de otro mes/año que el buscador devuelve como «noticia de hoy»? | Mirar fecha en URL/cuerpo; si no hay, descartar | «PPI 5,4 %» era agosto; septiembre fue 6,3 % (BLS) (cierre 15-oct) |
| 3 | ¿Es **hecho, propuesta o consulta**? Leer el verbo: *proposes* ≠ *considering* ≠ *will* | Etiquetar «propuesto» / «en consulta» | «Singapur prohíbe/aprueba» sobre la consulta MAS P015-2026 (R24) |
| 4 | ¿Es **acuerdo de «explorar» o lanzamiento**? ¿Tiene nombre y fecha en la nota primaria? | [VERIFICAR] hasta ver la nota | «Gran socio coreano» de Ripple sin nombre = reciclaje de Meritz (exploratorio) (14-oct) |
| 5 | ¿El texto primario **nombra el token** (XRP/XLM) o solo la red/la empresa? | No leer «adopción de XRP» | Notas de Ripple de oct-2026: hablan de XRPL, RLUSD, Custody; XRP solo en el menú (R34) |
| 6 | ¿Qué **serie / métrica** es? (spot vs futuro, distribuido vs representado, acumulado vs anual) | Pedir definición; no mezclar | Brent 105 $ (futuro BZ=F) vs 126 $ (spot EIA) (R29); RWA 39 / 371 / 292 mil M$ (R26); Ripple Payments «100 mil M$» acumulado (R28) |
| 7 | ¿Qué **ventana** cubre (24 h, 30 d, trimestre) y cuadra con las horas de la tabla? | Calcular el intervalo real | «-2 % en 36 h» eran 24,1 h (R38 n.º 4) |
| 8 | ¿Es un **dato de cierre** (13F, balance) o de un **momento**? ¿Permite decir «compró/vendió»? | Decir «a cierre de trimestre» | «Goldman vendió antes de la caída y recompró» no sale de un 13F (R21) |
| 9 | ¿Busqué **todo el universo** antes de decir «cero», «ninguno» o «no hay debate»? | Escribir «no localizado» + [VERIFICAR] | Goldman «a cero» en 1T: faltaba XRPR (R21b); Corea «sin debate» por silencio de la FSC (R30) |
| 10 | ¿La he **recalculado** (suma, %, días, hora UTC) con script, no a mano? | No citar todavía | Total 7.190.191 vs 7.390.191 (R38 n.º 1); 10:34 vs 09:34 UTC (R31) |

**Truco de bolsillo:** si una de las preguntas 2, 6 o 7 falla, la cifra no es comparable con ninguna otra, aunque sea correcta.

---

## 2. Tabla de fuentes: cuáles abren y de qué tipo son

Escala de [R15](../research/2026-10-15-R15-mapa-de-actores.md): **A** primaria · **B** secundaria buena (con fecha y causa) · **C** parte interesada o agregador · **D** no usar. «Abre» = comprobado en la fecha indicada (fuente: `fuentes-fiables-y-dudosas.md`).

### 2.1 Primarias que SÍ abren (tipo A)

| Fuente | Cómo | Para qué | Comprobado |
|---|---|---|---|
| sec.gov (EDGAR, XML 13F, 8-K, comunicados, PDF de reglas, FAQ Form 13F) | **curl con User-Agent identificado**; WebFetch falla a veces | 13F, Evernorth, reglas, plazos 13F | 15 y 17-oct (R21, R22, R23, R31) |
| federalregister.gov/api/v1 (+ `raw_text_url`) | curl (`-g`, `%22` en vez de espacios) | Fecha de publicación y cierre de comentarios; texto entero | 17-oct (R23, R25, R31) |
| federalreserve.gov (comunicado, H.10, calendario FOMC) | curl + UA | Tipos, calendario, tipo de cambio | 15 y 17-oct (R22, R29) |
| bls.gov (IPC, PPI, empleo, calendario) | curl + UA | Mes y año exactos del dato macro | 15 y 17-oct |
| boj.or.jp, ecb.europa.eu (calendario; tabla de tipos vía WebFetch), eia.gov | curl / WebFetch | Calendario y tipos | 15 y 17-oct (R22, R29) |
| mas.gov.sg (+ PDF con `pdftotext -layout`), hkma.gov.hk, sfc.hk (PDF), fsc.go.kr/eng, rbi.org.in, cbr.ru/eng, vara.ae | WebFetch o curl + UA | Regulación Asia, Rusia, EAU | 15 y 17-oct (R04P, R24, R27, R30) |
| ESMA CSV (`esma.europa.eu/sites/default/files/2024-12/CASPS.csv`, EMTWP, ARTZZ) | curl | Registro MiCA (ojo: alguna fecha errónea) | 15 y 17-oct (R19, R25) |
| xrplcluster.com (JSON-RPC: `feature`, `ledger`, `account_objects`, `gateway_balances`) | curl POST | Amendments, escrow, saldos del ledger | 17-oct (R32) |
| horizon.stellar.org (`ledgers`, `fee_stats`) | curl | Fechar upgrades de protocolo | 17-oct (R33) |
| fsb.org (PDF), nexusglobalpayments.org, irs.gov, gov.uk, BOE (curl + sed) | curl / WebFetch | Pagos, fiscalidad | 17-oct (R28, R35) |

### 2.2 Útiles pero con matiz (tipo B/C)

| Fuente | Qué es | Cuidado |
|---|---|---|
| 13f.info/data/cusip/<CUSIP>/<año>/<trim> | Índice de EDGAR (B) | Cuadró 5 de 5 con EDGAR; verificar los grandes en el XML |
| CoinGecko API (diaria y horaria), DefiLlama (stablecoins por cadena) | Agregadores (C) reproducibles | Citar día y hora; DefiLlama excluye BUIDL/Franklin de RWA |
| app.rwa.xyz | Tercero comercial (C) | Definir «distribuido» vs «representado» |
| ripple.com, stellar.org, swell.ripple.com, meridian.stellar.org, dashboard.stellar.org | Parte interesada (C) | Primarias **de lo que dice la empresa**, no de cifras de impacto (R22 §2). En ripple.com/press-releases la fecha de la lista va desfasada una entrada: abrir cada nota (R34) |
| 21Shares (informe mensual, Bloomberg) | Emisor (C) | Solo ETP físicos; columnas mezcladas en pdftotext |
| Despachos (Gibson Dunn, Sidley, Lefosse, Cahill, Latham…) | B | Útiles cuando el regulador no abre; marcar opinión |
| CBS/CNBC (macro), CoinDesk, The Block, Decrypt | B | Con fecha y causa; falta la primaria |

### 2.3 NO abren (comprobado) → usar alternativa o pedir el PDF a Joel

| Fuente | Fallo | Alternativa |
|---|---|---|
| bis.org | ECONNRESET / sin respuesta (15 y 17-oct) | Nota del BCE, The Block/Orrick con cita |
| fatf-gafi.org, swift.com, pib.gov.in, incometaxindia.gov.in, congress.gov | 403 | Secundaria con cita + [VERIFICAR] |
| fca.org.uk | Abrió el 15-oct (R18) y dio 403 el 17-oct (R30) | Reintentar; si no, despachos |
| rbidocs.rbi.org.in | Captcha (no saltar) | Pedir la tabla a Joel |
| bcb.gov.br / normativos | JavaScript / 404 | Despachos brasileños + PDF |
| EUR-Lex (WebFetch), etfmarket.cboe.com/canada, circle.com/transparency | Vacío / socket / JS | PDF del DOUE; emisor |

### 2.4 Tipo D: descartar

Páginas «XRP news today» sin fecha (mirrors SEO), MEXC-news, Changelly (predicciones de precio), publirreportajes de tokens ajenos (Remittix), cuentas anónimas, vídeos que ponen la fecha y la conclusión del presentador sobre una cita real (Despeja La X, 15-oct: 4 vídeos = 1 sola fuente).

---

## 3. Errores reales que cometimos (o casi) y cómo se detectaron

| Error | Qué pasó | Cómo se detectó | Regla que deja | Origen |
|---|---|---|---|---|
| **Goldman «a cero» en 1T / XRPR** | R21 buscó solo los 5 CUSIP de ETF spot y concluyó que Goldman no tenía XRP en 1T. Conservaba **110.000 acciones de XRPR** (CUSIP 26923N231; 1,21 M$) | La suma con XRPR (152,165 + 1,647 = 153,8 M$) **cuadraba con la prensa** (154 M$): la discrepancia era la pista | Antes de «cero», listar todos los CUSIP de la familia y cuadrar con la cifra ajena | [R21b §1, §7](../research/2026-10-15-R21b-13f-segunda-pasada.md) |
| **«Goldman vendió antes de la caída y recompró»** | Lectura de prensa de un 13F | Un 13F solo da cierres de trimestre y Goldman declara a nivel de grupo (fila del bróker-dealer, `otherManager` = 1) | Decir «a cierre de trimestre», nunca «compró/vendió» ni «apuesta» | R21, [R21b §9](../research/2026-10-15-R21b-13f-segunda-pasada.md) |
| **473 M XRP de Evernorth** | Varias líneas (12, 14, 15 y 17-oct) citaban 473 M como si fuera el saldo al cotizar | Lectura del **8-K**: 388.910.554 XRP en especie (suma de 5 partidas); los 473 M venían de un Form 425 a **31-dic-2025** | Una cifra pro forma de otra fecha no es el dato de hoy; «84 M comprados» era una resta entre dos fechas | [R23](../research/2026-10-17-R23-verificacion-sec.md), [R31 §1](../research/2026-10-17-R31-auditoria-coherencia-2.md), [R38 n.º 7](../research/2026-10-17-R38-auditoria-numerica.md) |
| **10:34 vs 09:34 UTC** | R32 y R37 dieron la mayoría de `fixCleanup3_4_0` a las 10:34 UTC; R14 tenía 09:34:30 | Conversión con script: `majority` 844853670 + 946684800 = **9-oct-2026 09:34:30 UTC** | Tiempos del ledger XRPL (segundos desde 1-ene-2000) siempre con script; un error repetido en varios informes **parece confirmado sin serlo** | [R31 §1](../research/2026-10-17-R31-auditoria-coherencia-2.md) |
| **Series de Brent** | ~105 $ (futuro frontal BZ=F, Yahoo, 13-oct) y ~126 $ (spot FOB Europa, EIA, 14-oct) | Al cruzar R29 con la apertura: ~20 $ de diferencia que es de mercado, no de error | Citar siempre qué serie; un salto de +20 $ en un día (135,5 $, 2-oct) pide segunda serie [VERIFICAR] | R29, `catalizadores-xrp-xlm.md` (aviso de series) |
| **36 h vs 24 h** | «XRP cayó ~2 % en 36 h (1,34 → 1,31 $)»; la tabla iba de 15-oct 23:00 a 16-oct 23:07 UTC = **24,1 h** | Recalcular el intervalo entre la primera y la última columna | El % estaba bien; el rótulo no. Otra tabla llamaba «24 h» a una base de 48 h (-3,4 % en vez de -1,5 %) | [R38 n.º 3 y 4](../research/2026-10-17-R38-auditoria-numerica.md) |
| **Total que no es la suma** | Goldman 2T: total 7.190.191 acciones; las 5 filas suman **7.390.191** (+6,3 %, no +3,4 %) | Script de sumas; los dólares sí cuadraban | Que cuadre una columna no prueba la otra | [R38 n.º 1](../research/2026-10-17-R38-auditoria-numerica.md) |
| **Día de la semana** | «mar 21-oct-2026»: es miércoles | Script (37 de 38 fechas cuadraban) | Fechas con día de semana, comprobadas con script | [R38 n.º 2](../research/2026-10-17-R38-auditoria-numerica.md) |
| **Resumen más fuerte que la tabla** | «95 % del mBridge en yuan», «ya probaron con valor real», «91.500 M$ en ene-2026» (el Tesoro dice «a enero de 2026») | Auditoría R22: la tabla bien etiquetada, el resumen y el caso alcista/bajista sin etiqueta | Al resumir, **copiar la etiqueta junto a la cifra** | [R22 §1-2](../research/2026-10-15-R22-auditoria-coherencia.md) |
| **Misma métrica, tres tamaños** | RWA en Stellar: 3.000 / 4.000 / 3.550 M$ según fuente y fecha; BUIDL -1,4 % (RWA.xyz, 30 d) vs -19 % (DefiLlama, 1 mes); ETF XRP 1.440 vs 2.178 M$ | Cruce entre informes en R31/R38 | No son bulos, pero sin métrica + ventana + fecha no se comparan | [R38 n.º 5 y 6](../research/2026-10-17-R38-auditoria-numerica.md) |
| **Titular reciclado** | «Noticias de hoy» de otros años (BTC 125 k$, ETF XRP «el 18-oct»), Nasdaq sobre Evernorth de 2025 | El contexto no encajaba con la fecha | Si el contexto no cuadra con la fecha, descartar | `patrones-de-bulos.md` (14 y 17-oct) |
| **Eco entre medios** | Crypto Briefing, KuCoin y mexc repetían a Bloomberg sobre Goldman; 4 vídeos de un canal = 1 fuente | Buscar el origen común | N medios que copian a uno = 1 fuente | `fuentes-fiables-y-dudosas.md` (R21, 15-oct) |
| **Agregador vs serie horaria** | «XRP -4,5 % a 1,29 $» de un agregador; CoinGecko horario daba mínimo 1,31 $ | Contraste con `market_chart` horario | Movimientos de precio siempre con datos horarios | `patrones-de-bulos.md` (apertura 17-oct) |
| **Afirmación de «ausencia»** | «No hay debate» de la ley del won stablecoin porque la FSC no publica en inglés | No se miró la Asamblea | Silencio de una web ≠ ausencia; [VERIFICAR] | R30 |
| **Ley propuesta como vigente** | Brasil 17,5 % (MP 1.303, probablemente caducada) y Japón 20 % (propuesto) en guías fiscales | Texto de la autoridad no localizado | Tipo y plazo solo con texto oficial | R35 |

**Patrón común (R22 y R31):** la tabla de cada informe suele estar bien; el error aparece **al resumir** (5 líneas, caso alcista/bajista, línea al cerebro) o **al copiar entre informes**.

---

## 4. Plantilla de comprobación de una cifra (paso a paso)

**Paso 1 · Anotar la cifra tal cual** con fuente, URL, fecha del artículo y fecha del dato.

**Paso 2 · Buscar la primaria** (tabla §2.1). Ejemplos de comandos que funcionaron (sustituir `<…>`; el User-Agent debe identificar a la persona, como pide la SEC):

```bash
curl -s -A "Nombre Apellido contacto@ejemplo.com" "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<CIK>&type=8-K"
```

```bash
curl -s -A "Nombre Apellido contacto@ejemplo.com" "https://13f.info/data/cusip/<CUSIP>/2026/2"
```

```bash
curl -s -X POST https://xrplcluster.com -H "Content-Type: application/json" -d '{"method":"feature","params":[{}]}'
```

```bash
curl -s "https://horizon.stellar.org/ledgers?order=desc&limit=1"
```

```bash
curl -s "https://api.coingecko.com/api/v3/coins/ripple/market_chart?vs_currency=usd&days=2"
```

**Paso 3 · Clasificar:** hecho / propuesta / consulta / estimación; serie y ventana; parte interesada sí/no.

**Paso 4 · Recalcular con Python** (nunca a mano). Script usado hoy para comprobar esta guía (resultados reales en el comentario; en este PC `python -I` falla, usar `python` normal):

```python
from datetime import datetime, timezone
# 1) Hora del ledger XRPL (segundos desde 1-ene-2000) -> UTC
print(datetime.fromtimestamp(844853670 + 946684800, tz=timezone.utc))  # 2026-10-09 09:34:30+00:00
# 2) Día de la semana
print(datetime(2026, 10, 21).strftime('%A'))                           # Wednesday
# 3) ¿El total es la suma de las filas?
filas = [2208949, 2238407, 1759090, 806126, 377619]
print(sum(filas), round((sum(filas) / 6952239 - 1) * 100, 1))         # 7390191  6.3
# 4) Intervalo real entre la primera y la última columna
a, b = datetime(2026, 10, 15, 23, 0), datetime(2026, 10, 16, 23, 7)
print((b - a).total_seconds() / 3600)                                  # 24.1 h
```

**Paso 5 · Cuadrar con la cifra ajena.** Si la prensa da otra cosa, la diferencia es una pista (caso XRPR): buscar qué falta antes de decidir quién se equivoca.

**Paso 6 · Escribir la cifra con sus cinco cosas:** «XRP 1,31 $ (CoinGecko horario, 16-oct 23:07 UTC; -2,2 % en 24,1 h; [PRIMARIA de agregador])». Si falta algo, **[VERIFICAR]**.

**Paso 7 · Al resumir:** copiar la etiqueta con la cifra. Si el resumen dice algo que la tabla no dice, el resumen está mal.

### Hoja de una cara (para recortar)
- [ ] ¿Quién lo dice y qué gana?
- [ ] ¿Fecha del dato (no del artículo)?
- [ ] ¿Hecho, propuesta o consulta? (verbo)
- [ ] ¿Nombra XRP/XLM o solo la red/la empresa?
- [ ] ¿Qué serie, qué ventana?
- [ ] ¿Cierre de periodo o momento?
- [ ] ¿Universo completo antes de «cero»?
- [ ] ¿Recalculado con script (suma, %, días, UTC)?
- [ ] ¿Cuadra con la cifra ajena? Si no, ¿por qué?
- [ ] ¿El resumen lleva la etiqueta?

---

## 5. Hechos y opiniones de esta guía
- **HECHOS** (documentados en los informes enlazados): todos los errores de §3, las conversiones y sumas de §4 (recalculadas hoy con script) y la lista de webs que abrieron o no en las fechas indicadas.
- **OPINIÓN mía:** que la mayoría de errores vienen del resumen y no de la fuente es un patrón de **dos auditorías** (R22, R31) sobre unos 40 informes; con otra muestra podría cambiar [ESPECULACIÓN]. El orden de las 10 preguntas es una elección práctica, no un estándar.

## 6. Dudas y datos a verificar
- Si fca.org.uk, bis.org y fatf-gafi.org siguen cerrados para curl/WebFetch (la tabla §2.3 puede quedar vieja en semanas) [VERIFICAR].
- La discrepancia de prensa «+83 M$ de Goldman frente al 1T» sigue abierta (R21b §7) [VERIFICAR].
- Las dos series de ETF de XRP (SoSoValue/KuCoin 1.440 M$ a fin de agosto vs 21Shares/Bloomberg 2.178 M$ a 30-sep) no se han reconciliado [VERIFICAR].
- Causa del salto de stablecoins en Stellar (425 → 545 M$ entre el 12 y el 17-oct, DefiLlama) [VERIFICAR].
- La base del «-1,05 %» de XRPN el día de su estreno no está citada (R38 n.º 8) [VERIFICAR].
