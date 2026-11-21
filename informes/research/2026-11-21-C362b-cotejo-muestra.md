# C362b · Cotejo de una muestra de 30 celdas con su fuente (21-nov-2026)

Método: muestra con semilla fija sobre `explorador/cadenas.json` (matriz de capacidades; 12 con nivel P, 8 con nivel S) y `explorador/regulacion.json` (10 celdas con nivel P: 5 de EE. UU./UE/Asia y 5 de otros). Solo lectura: no se ha editado ningún dato. Cada URL se abrió con WebFetch y, si bloqueaba o era dinámica, con Chrome (lector de texto o JavaScript). Lectura hecha el 21-nov-2026.

Estados: **coincide** · **parcial** (las cifras principales coinciden, pero algún detalle de la celda no consta en la URL citada) · **difiere** · **no verificable** (motivo indicado). Lo que no se pudo leer no se da por correcto.

## Tabla A · Cadenas, nivel P (12)

| # | Celda (cadena/campo) | URL (resumida) | Estado | Valor correcto / observación |
|---|---|---|---|---|
| 1 | ondo/cumplimiento | docs.ondo.finance/…/eligibility-and-onboarding.md | parcial | Coincide >5 M$ (personas) y >25 M$ (entidades). La prohibición de USDY a EE. UU./Canadá no consta en esa página (hay que citar otra URL). |
| 2 | ondo/liquidez | docs.ondo.finance/…/instant-limits.md | parcial | Coincide: mínimo 5.000 $, tope global 50 M$/24 h, individual 25 M$. «Solo en Ethereum» no consta en la página. |
| 3 | stellar/pagos | stellar.org/blog/…q2-2026… | parcial | Coincide 11.400 M$ y +72 %. «Cierre ~5 s y 100 stroops» no está en el blog (solo «una centésima de céntimo»). |
| 4 | chainlink/interop | docs.chain.link/ccip/directory/mainnet | difiere (leve) | Hoy: 77 redes (celda 78), 281 tokens y 3 verificadores coinciden, LINK en 64 redes (celda 65), USDC en 23 (celda 22). WebFetch da 404; solo se lee en Chrome. |
| 5 | canton/cumplimiento | dtcc.com/press-releases/2026/dtcc-tokenization-service-goes-live | coincide | «28 de octubre de 2026», integrado con Canton y una red Besu privada. |
| 6 | bnb/seguridad | docs.bnbchain.org/…/introduction/ | difiere | Coincide 45 validadores y 21 Cabinets (la página dice 21 Cabinet + 24 Candidates). No consta «18 Cabinets + 3 Candidates por época» ni la elección diaria tras las 00:00 UTC: citar otra fuente o marcar [VERIFICAR]. |
| 7 | hedera/pagos | docs.hedera.com/…/mainnet/fees | coincide | 0,0001 $ / 0,001 $ / 0,0008 $ / 1 $. |
| 8 | algorand/pagos | dev.algorand.co/…/fees/ | coincide | 0,001 ALGO; 0,003 con Falcon. |
| 9 | bnb/regulacion (VBNB) | vaneck.com/…/bnb-etf-vbnb/overview/ | parcial | Coincide inicio 7-may-2026 y comisión 0,39 %. Las cifras del 17-nov (NAV 22,84 $; 77,66 M$; -8,64 %; 0,65 %) no se pueden comprobar: la web solo muestra el último dato (20-nov: 20,75 $; 70,56 M$; -16,99 %; 0,51 %). |
| 10 | avalanche/interop | build.avax.network/docs/cross-chain | parcial | Existen ICM e ICTT. «Warp Messaging activo desde Durango, mar-2024» no consta en la página. (WebFetch: demasiadas redirecciones; leído con el lector alternativo.) |
| 11 | ondo/rendimiento | ondo.finance/usdy | difiere | La URL solo trata USDY. USDY APY 3,75 % coincide; YTM hoy 4,20 % (19-nov; celda 4,15 %) y vencimiento medio 170,87 días (celda 160). OUSG (3,70 %, 30 d, 7 d, comisión 0,15 % hasta 1-ene-2027) no consta: URL equivocada para OUSG. |
| 12 | polygon/cumplimiento | polygon.technology/blog/apex-group-… | coincide | 18-mar-2026; 100.000 M$ hasta junio de 2027; ERC-3643; Agglayer. |

## Tabla B · Cadenas, nivel S (8)

Todos son agregadores en vivo: solo se puede comparar con el valor de hoy (21-nov), no con el de la lectura del 14-nov. La diferencia puede ser deriva temporal; lo marcado «difiere» es material (>5 %) o un cambio de clasificación.

| # | Celda | URL | Estado | Valor hoy / observación |
|---|---|---|---|---|
| 13 | xrpl/activos | app.rwa.xyz/networks/xrp-ledger | difiere | Hoy RWA.xyz muestra 3,00 B$ distribuidos y 2,97 B$ representados (celda: 642,8 M$ y 5.210 M$). Justoken (JMWH, 2,4 B$) pasó a «Distributed». Cambio de clasificación del agregador: la tesis «mayor representado = 43 %» ya no es válida tal cual. |
| 14 | stellar/activos | app.rwa.xyz/networks/stellar | difiere (leve) | Distribuidos 4,87 B$ (+33,9 %) frente a 4.662,8 M$ (+31,6 %); Spiko 2,2 B$ (celda 2.100 M$), Franklin 1,4 B$ (1.300), Circle 330 M$ (378). Sigue 4.ª o similar; deriva de una semana. |
| 15 | plume/liquidez | app.rwa.xyz/networks/plume | parcial | RWA distribuidos 142,87 M$ (142,58), 987 activos (986), titulares 257.101 (257.175): coincide. Representados 24,54 M$ (25,94), stablecoins 13,25 M$ (14,06) y transferencias 207,6 M$ (232,5): derivan 6-11 %. |
| 16 | canton/liquidez | genfinity.io/2026/09/11/… | coincide | «351.000 M$ de media diaria» (agosto) coincide; el artículo lo toma de la web de Broadridge (autorreferencia, no verificado de forma independiente). |
| 17 | polygon/liquidez | app.rwa.xyz/networks | coincide | Hoy 2,82 B$ (celda 2.771 M$): +1,8 %. |
| 18 | ethereum/liquidez | app.rwa.xyz/networks | coincide | Hoy 133,30 B$ (celda 135.765 M$): -1,8 %. |
| 19 | xdc/liquidez | stablecoins.llama.fi/stablecoinchains | coincide | Hoy 101,55 M$ (celda 103,2 M$): -1,6 %. No se revisó el TVL de 1,9 M$. |
| 20 | stellar/liquidez | app.rwa.xyz/networks/stellar | difiere | Hoy 401,3 M$ de capitalización (celda 445,4) y 23.460 M$ transferidos (23.710). |

## Tabla C · regulacion.json, nivel P (10)

| # | Celda (jur/tema) | URL | Estado | Valor correcto / observación |
|---|---|---|---|---|
| 21 | ue/stablecoins | esma.europa.eu/…/mica | no verificable | La página lista CSV de emisores EMT/ART con «última actualización 18-nov-2026» (la celda cita el registro del 22-oct); no muestra recuentos, así que «25 EMT, 0 ART, sin Tether» no se pudo comprobar. Hay que abrir el CSV. |
| 22 | sg/tokenizacion | mas.gov.sg/…/tokenised-mas-bill | coincide | TD26100F S$1 M (23-sep a 30-sep); TD26101Z S$10 M (9-oct a 23-oct); CBDC mayorista (SGD Testnet); solo institucionales. |
| 23 | eeuu/tokenizacion | sec.gov/…/innovation-exemption | parcial | Confirma la orden del 17-sep-2026 (Release 34-106402, 91 FR 60168). No consta AMM, «cinco años» ni el no-action de DTC del 11-dic-2025 (están en la orden en PDF, no leída). |
| 24 | jp/cbdc | boj.or.jp/paym/digital/dig260610c.pdf | no verificable | PDF binario sin texto extraíble (WebFetch y Chrome). «50.000 TPS» y «sin decisión de emitir» sin comprobar. |
| 25 | hk/ley_marco | sfc.hk/…/Lists-of-virtual-asset-trading-platforms | coincide | 13 plataformas licenciadas (lista de 13 nombres). La celda cita el informe trimestral de abr-jun, la lista de hoy da 13 igualmente. |
| 26 | ir/ley_marco | cbi.ir/showitem/34044.aspx | difiere (campo fecha) | El texto coincide (política aprobada en aban-1403; instrucción a corredores 5 mehr 1404 = 27-sep-2025; página del 17 azar 1404 = 8-dic-2025). Pero el campo `fecha` de la celda es **2024-12-08**: debería ser 2025-12-08 (año equivocado). |
| 27 | ch/etf | finma.ch/…/20260112-finma-aufsichtsmitteilung-01-2026.pdf | no verificable | PDF sin texto extraíble. §3.4 y condición de garantía a minoristas sin comprobar. |
| 28 | ru/cbdc | cbr.ru/PSystem/dr/faq/ | coincide | 1-sep-2026: mayores bancos y comercios >120 M₽; 1-sep-2027: bancos con licencia universal y comercios >30 M₽. Matiz: ambos umbrales aplican a clientes de esos bancos, y desde 1-sep-2028 hay otra fase (20-30 M₽). |
| 29 | ca/cbdc | bankofcanada.ca/digitaldollar/ | coincide | «scaling down its work on a retail CBDC» y orientación a investigación de pagos. |
| 30 | br/custodia | bcb.gov.br/…/exibenormativo?…numero=520 | no verificable | Confirmada la Res. BCB 520 (10-nov-2025, DOU 11-nov-2025). El texto de los artículos (art. 88 III, vigencia 2-feb-2026) no se muestra en la página (contenido dinámico/PDF). |

## Resumen

- **Coincide: 12 de 30 (40 %)** · parcial: 6 (20 %) · difiere: 8 (27 %) · no verificable: 4 (13 %).
- Si se cuentan coincide + parcial: 60 %. Por grupo: cadenas P 4 coincide, 5 parcial, 3 difiere; cadenas S 4 coincide, 4 difiere; regulación 4 coincide, 1 parcial, 1 difiere, 4 no verificable.
- Sesgo de la muestra: se priorizaron celdas con cifras; las diferencias son sobre todo de detalle, no de la idea principal. Una muestra de 30 no permite extrapolar un porcentaje fiable al total (solo orden de magnitud). [RAZONADO]

### Errores sistemáticos
1. **Detalle que no consta en la URL citada (6 de 12 en nivel P):** la cifra principal está en la fuente, pero el complemento (Ethereum como única cadena de OUSG, 5 s/100 stroops, 18+3 validadores por época, Durango/mar-2024, AMM y 5 años de la SEC) procede de otra parte o de memoria. Hay que citar la URL concreta o rebajar a [VERIFICAR].
2. **Cifras de agregadores en vivo sin hora de corte:** las fichas de RWA.xyz y DefiLlama derivan 2-11 % en una semana y la clasificación cambió (caso XRPL: 2.373 M$ de Justoken ahora «distribuido»). Una celda S sin fecha de lectura visible no es comparable; hay que mostrar «leído el…» y no usarla en comparaciones entre redes.
3. **Páginas que solo muestran el último dato** (VanEck, Ondo, Chainlink): las cifras fechadas (17-nov, 14-nov) no se pueden volver a comprobar; guardar captura o histórico.
4. **Fechas:** un campo `fecha` con año equivocado (Irán 2024 en vez de 2025). Conviene un chequeo automático «fecha del campo = fecha citada en el texto».
5. **URLs/lectura:** Chainlink devuelve 404 a WebFetch pero funciona en Chrome; 3 PDF oficiales (BoJ, FINMA y la orden SEC) y la normativa del BCB no son legibles con herramientas de texto: anotar en la celda «leído en PDF por [persona]» o dejar [VERIFICAR]. Ninguna URL de la muestra estaba rota (404 real).
6. **Unidades:** sin errores de M$/mil M$ en la muestra (los importes con rublos y reales sí traían la moneda).

### 5 correcciones recomendadas (NO aplicadas; las revisas tú)
1. **cadenas.json xrpl/activos (celda 13):** actualizar a lectura del 21-nov (3,00 B$ distribuidos / 2,97 B$ representados), explicar el cambio de clasificación de Justoken y retirar «≈ 43 % del total representado» o recalcularlo.
2. **cadenas.json bnb/seguridad (6):** conservar 45 validadores = 21 Cabinets + 24 Candidates (dato de la fuente); el «18 Cabinets + 3 Candidates por época» y la elección diaria deben marcarse [VERIFICAR] o enlazar su fuente.
3. **cadenas.json ondo/rendimiento (11):** separar USDY (3,75 % APY; YTM 4,20 % y vencimiento medio 170,87 días a 19-nov) de OUSG, y buscar la URL de OUSG; ahora la URL no respalda las cifras de OUSG.
4. **regulacion.json ir/ley_marco (26):** corregir `fecha` de 2024-12-08 a 2025-12-08.
5. **cadenas.json chainlink/interop (4):** actualizar a 77 redes, LINK en 64 y USDC en 23 (o poner «leído 14-nov» visible) y avisar de que la URL solo se lee en navegador. Complementaria: regulacion.json ue/stablecoins (21) y eeuu/tokenizacion (23): abrir el CSV de ESMA (actualizado 18-nov) y la orden de la SEC en PDF antes de dar por buenas «25 EMT» y «AMM, cinco años».

Pendientes de lectura humana/Chrome con PDF: jp/cbdc (24), ch/etf (27), br/custodia (30).
