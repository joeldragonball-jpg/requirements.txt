# Noticias por caducar, verificación y calendario (21-nov-2026)

Alcance: repaso de las noticias con `caduca` vencida o a ≤14 días (explorador/noticias-archivo.json, 129 archivadas; explorador/datos.json, movimientos 353-365 que caducan entre el 22-nov y el 4-dic) y de las pendientes de las tareas C173/C176/C247/C254. Las entradas `revisar:true` de regulacion.json caducan a partir del 18-ene-2027 y no estaban a ≤14 días. Las noticias de antes del 17-nov ya tenían fila en eventos/verificados.json; aquí se cubren las que no la tenían. Etiquetas: [P] primaria leída, [S] prensa o agregador, [VERIFICAR], [ESPECULACIÓN]. Regla de umbrales de W05 aplicada (mismo día, intradía, instrumento).

## 1. Tabla de confirmaciones y desmentidos (29 filas nuevas en verificados.json)

| Noticia (fecha) | Estado | Qué dice la fuente |
|---|---|---|
| MEXC aislado del sistema financiero de EE. UU. (6-nov) | Confirmada [P] | Orden de FinCEN (no OFAC), Tesoro sb0685 y Federal Register 2026-22962; efectiva 10-dic. |
| Sanciones a 8 empresas canadienses (7-nov) | Confirmada [P] | OFAC, Tesoro sb0686, fecha real 6-nov. |
| CFTC da 30 días a las plataformas (8-nov) | Confirmada [P] | CFTC 9323-26 del 5-nov; plazo ≈5-dic. |
| CFTC autoriza perpetuos sobre acciones (3-nov) | Confirmada [P] | CFTC 9319-26; solo en mercados con registro dual SEC/CFTC. |
| BCE avisa de riesgos (18-nov) | Confirmada [P] | Financial Stability Review y nota ecb.pr261118. |
| Cook (Fed): hacen falta subidas (20-nov) | Confirmada [P] | Discurso cook20261120a; disintió en octubre. Opinión personal. |
| España y Portugal, expediente UE (20-nov) | Confirmada [P] | Paquete de infracciones del 19-nov: España carta de emplazamiento MiCA/CRD V (INFR(2026)2153) y dictamen motivado DAC8 (INFR(2026)0060); Portugal dictamen motivado (INFR(2025)2039). |
| El Ibex pierde 5,7 % en la semana (20-nov) | Confirmada [S] | Yahoo ^IBEX: −5,73 %. |
| Bitcoin bajo 59.000 $ (20-nov) | Confirmada [S] | Mínimo 57.709 $ y cierre 58.799 $ (velas UTC). |
| Dólar en máximo desde abril 2025 (16-nov) | Confirmada [S] | DXY 103,55; último cierre igual o mayor: 2-abr-2025. |
| Nasdaq cae 3 % (20-nov) | Matizada | Era media sesión; el cierre fue −5,28 %. |
| Brent supera 93 $ (17-nov) | Matizada | Futuro cierra 93,14 (+0,76 %); spot EIA 92,94, no supera. |
| Bono a 10 años sobre 5 % «racha histórica» (17-nov) | Matizada | DGS10 ≥5 % del 12 al 19-nov; «histórica» es juicio; el 20-nov cae a ≈4,91 %. |
| Oro a mínimos de un año (16-nov) | Matizada | Cierre 3.853 $, mínimo desde sep-2025; «peor año desde 2015» sin verificar. |
| Bonos del Tesoro, «mayor racha en cinco meses» (20-nov) | Matizada | Racha de bajada de rendimientos cierta; el «cinco meses» sin verificar. |
| Binance logra orden de congelación de 6.500 M$ (19-nov) | Matizada [S] | 6.500 M$ es el tamaño del robo; ≈2.850 M$ congelados o interceptados; tribunal de Abu Dabi; audiencia 1-dic. |
| Hackers norcoreanos usaron el sistema de Sky (19-nov) | Matizada [S] | Informe de Inca Digital (518 M$ acumulados en años); el riesgo de congelación de ≈2.700 M$ es hipotético. |
| Evernorth reduce 60 % (17-nov) | Matizada [S] | Deterioro contable acumulado (847 M$ → 342 M$), no precio; EDGAR sin leer. |
| Candidata demócrata a la SEC pide norma formal (19-nov) | Matizada [S] | Opinión de Kristin Johnson en la audiencia del Senado. |
| Waller no descarta +0,50 pp (18-nov) | Matizada [S] | CNBC vía Decrypt; FedWatch 91 % para +0,25. |
| Musalem: varias subidas (17-nov) | Matizada | Postura real; fecha del 17-nov no confirmada. |
| APEC en Shenzhen (18-nov) | Matizada [S] | Trilateral Xi-Trump-Putin y «declaración de paz»; texto de APEC no leído. |
| Tanker en llamas en Ormuz (18-nov) | Matizada [P parcial] | UKMTO: informe tardío del 18-nov; «en llamas» no confirmado; dos petroleros golpeados el 21-nov (#215, #216). |
| CFTC «arquitectura de derivados» e investigación a Kalshi (18-nov) | Sigue sin verificar | Lista de comunicados 9292-9328 sin nada equivalente; sí demandas a Arkansas y Luisiana. |
| Bessent pide subida menor (20-nov) | Sigue sin verificar | Sin primaria del 20-nov. |
| Williams: no hace falta acción drástica (17-nov) | Sigue sin verificar | No localizado. |
| Irán prepara convoy en Kharg (20-nov) | Sigue sin verificar | Sin primaria; UKMTO no lo menciona. |
| EE. UU. ataca Qeshm (17-nov) | Sigue sin verificar | El episodio documentado es de 2-3-nov; posible reciclaje. |
| Desplome 19-20 nov: causa | Sigue sin verificar | Ver sección 2. |

Sin comprobar por falta de tiempo (siguen en archivo o en el bot, sin fila): J. P. Morgan prevé subidas, Paulson (Fed), minas navales del 17-nov, Binance «cuatro países» (ya consta que son España, Francia, Italia, Polonia y Suecia), Fed-OCC (ya dudosa: la Fed no publica nada), CLARITY 31 % (ya dudosa).

## 2. Desplome del 19-20 nov: hechos y causas

**Hechos** (cierres de Yahoo Finance [S]; FRED [P] solo llega al 19-nov):
- S&P 500: −2,02 % el 19-nov (7.175,83) y −3,70 % el 20-nov (6.910,39); séptima caída seguida. Nasdaq Composite −2,25 % y −5,28 % (22.617,73). Dow −1,93 % el 20-nov (48.147) [S, UPI].
- SOXX −2,76 % y −10,55 %; Nvidia −3,3 % y −14,0 %; AMD, Broadcom y Micron −13 a −14 % el 20-nov [S].
- VIX: 28,44 el 19-nov; 35,89 al cierre del 20-nov con máximo intradía de 40,03. La cifra de 38,8 del encargo no coincide con el cierre de Yahoo (puede ser otra hora o fuente) [VERIFICAR].
- Bonos: rendimiento a 10 años 5,04 % (19-nov, FRED) y ≈4,91 % (20-nov, ^TNX): hubo refugio en deuda, no presión de bonos. Dólar sin cambio (103,8-103,9).
- Petróleo sin shock: Brent futuro 91,98 → 92,57; WTI 83,21 → 83,98. Oro −4,6 % el 20-nov (3.515 $), bitcoin −5 % (58.799 $).
- Calendario y datos: Nvidia presentó resultados el 17-nov (ingresos 115.800 M$, previsión de 130.000 M$ [S]) y la acción cayó igualmente los días siguientes. Actas de la Fed (18-nov [P]): casi todos ven más subidas. Reclamaciones de desempleo 203.000 y Philly Fed flojo el 19-nov [S]. Cook (20-nov [P]) pide subir tipos; Jefferson (19-nov [P]) habla de choques de energía, aranceles e IA; el FOMC es el 8-9 dic.
- Empresas y política: salida de Jensen Huang de Nvidia (12-nov) y, según prensa, revisión de la SEC sobre Nvidia (WSJ el 17-nov; Reuters el 20-nov habla de cuestiones contables, con dos fuentes anónimas; no he encontrado ni leído el texto) [S]. Debut de Anthropic en bolsa el 19-nov (precio de salida 83 $, +17 % el primer día y −8,5 % el 20-nov; la mayor salida a bolsa por importe según el folleto) [S]. Informe de que Google compraría directamente memoria HBM para sus TPU en lugar de vía Broadcom [S, Bernstein vía TradingKey]. El BCE advirtió el 18-nov de valoraciones de IA y financiación con deuda [P].

**Hipótesis [ESPECULACIÓN]** (la prensa las cita, ninguna tiene fuente oficial que las vincule con el movimiento):
1. Liquidación de la operación «IA»: dudas sobre el retorno del gasto, deuda para financiar centros de datos, circularidad (la línea del BCE).
2. Choque de noticias en Nvidia y chips: salida del CEO, investigación de la SEC, el informe sobre HBM de Google, vínculos de AMD con empresas chinas vetadas [S].
3. Absorción de liquidez por la mayor oferta pública de la historia (81.340 M$ según investinglive [S]) justo cuando el mercado ya caía.
4. Subidas de la Fed (el mercado descuenta +0,25 pp el 9-dic con 91 %), con tipos a 10 años por encima del 5 %. Contra esta hipótesis: el 20-nov los rendimientos bajaron.
5. Efecto bola de nieve técnico: VIX por encima de 35, correcciones oficiales del S&P y el Dow (más de un 10 % desde máximos [S]) y órdenes automáticas.
Caso alcista: venta de pánico en un día, con bonos y refugio funcionando, resultados de Nvidia por encima de lo previsto. Caso bajista: el recorte del Nasdaq-100 roza el −20 % desde su máximo, hay riesgo regulatorio (SEC), subidas de tipos por delante y una salida a bolsa que no sostuvo el ánimo. Sesgos de fuente: gran parte de los medios son agregadores o de prensa financiera que atribuyen causas a posteriori; CoinDesk y TradingKey mezclan hechos y explicaciones.

## 3. Fuentes y sesgos
- Primarias leídas: tesoro (sb0685, sb0686), Federal Register, CFTC (9319, 9323, 9322, 9327), Comisión Europea (inf_26_2269, PDF), BCE (nota del 18-nov), Fed (discursos y actas), UKMTO (en Chrome, solo el listado), FRED, TreasuryDirect, BoE, EIA.
- Lectores que resumen (WebFetch) usados para CoinDesk, UPI, TradingKey, Motley Fool, investinglive y BCE: lo que figura como [S] no se ha cotejado literal. En BCE y Comisión se confirmó el texto literal con el PDF o la nota de prensa.
- Yahoo Finance y FRED: datos de mercado de agregador (Yahoo) y oficial (FRED); precios del futuro frente al spot siguen la regla del 12-nov.
- CoinDesk y Decrypt: medios del sector cripto con posible sesgo hacia el hype; las cifras se contrastan con documentos cuando existen.

## 4. Calendario: 10 eventos nuevos (eventos/calendario.toml)
23-25 nov subastas del Tesoro a 2, 5 y 7 años ($69, $70 y $44 mil M, TreasuryDirect); 1-dic audiencia de Abu Dabi sobre el hackeo a Binance [S]; ≈5-dic fin del plazo de la CFTC de 30 días; 8-dic STEO de la EIA; 10-dic entra en vigor la orden de FinCEN contra MEXC; 15-dic mesa redonda de la CFTC sobre negociación 24/7; 17-dic decisión del Banco de Inglaterra (Bank Rate 4,00 %); ≈19-ene-2027 fin del plazo de dos meses de España tras las cartas de la Comisión. Ya existían FOMC 9-dic, BCE 17-dic, BoJ 18-dic, IPC 10-dic, empleo 4-dic, PCE, Stellar P30 y G20. No he añadido plazos de ETF de la SEC ni 13F (el siguiente 13F vence a mediados de febrero) por falta de fecha oficial leída. APEC 18-nov marcado como revisado en revisados.json.

## 5. Qué queda [VERIFICAR] y por qué
- Causa del desplome: sin fuente oficial.
- Cifra VIX 38,8 (Yahoo da 35,89 de cierre y 40,03 de máximo).
- Reuters/WSJ sobre la SEC y Nvidia: no he podido leer el original.
- Evernorth (EDGAR), orden de Abu Dabi, audiencia del Senado y texto de APEC: sin primaria.
- Comunicados de Bessent y Williams, convoy de Kharg, ataque a Qeshm el 17-nov, CFTC/Kalshi: sin fuente.
- Ranking histórico del oro y «mayor racha en cinco meses» de bonos.
- UKMTO #215/#216 (21-nov): leídos en Chrome; detalle del informe del 18-nov no abierto.
- Fecha efectiva de la orden de FinCEN: leída en Federal Register (10-dic) [P].

Lección (≤5 líneas): los titulares con cifra de tamaño («6.500 M$ congelados») mezclan el total robado con lo congelado; los de «el Nasdaq cae 3 %» son de media sesión y el cierre suele diferir; mirar la fecha del comunicado oficial (la CFTC y el Tesoro anteceden 1-3 días a la noticia).
