# W01c · IPC de EE. UU. de octubre-2026: contraste con FRED y reacción del mercado (10-nov-2026)

Cierra los [VERIFICAR] de `2026-11-10-W01b-ipc-dato.md`. Informativo; no es una recomendación de compra/venta. [P] = fuente oficial leída; [S] = agregador/prensa/datos de mercado de Yahoo; [VERIFICAR]; [ESPECULACIÓN]. Todas las horas de mercado están en **UTC** (Madrid = UTC+1 en noviembre). El IPC se publicó a las 13:30 UTC (14:30 Madrid, 08:30 ET). Lectura hecha entre las 17:25 y las 17:45 UTC (≈18:30–18:45 Madrid).

## 1. Contraste con FRED y con las tablas completas del BLS (resuelto)
**HECHOS [P]**
- FRED (St. Louis Fed) **ya refleja** la publicación de hoy: CPIAUCSL «Last Updated 2026-11-10 8:12 AM CST» (con último dato oct-2026) y CPILFESL «Updated Nov 10, 2026 8:13 AM CST». Fuente subyacente: BLS.
- Niveles desestacionalizados (1982-84=100), FRED:
  | Serie | Ago-26 | Sep-26 | Oct-26 | Sep→Oct (cálculo propio) | BLS dice |
  |---|---|---|---|---|---|
  | IPC-U general (CPIAUCSL) | 334,131 | 336,298 | 337,476 | **+0,351 %** → 0,4 % | +0,4 % ✔ |
  | Subyacente (CPILFESL) | 337,765 | 338,896 | 339,900 | **+0,296 %** → 0,3 % | +0,3 % ✔ |
  | General, Ago→Sep | | | | +0,649 % → 0,6 % | +0,6 % ✔ |
  | Subyacente, Ago→Sep | | | | +0,335 % → 0,3 % | +0,3 % ✔ |
- Sin desestacionalizar (CPIAUCNS): sep 336,940 y oct **337,511**, idéntico a la tabla del BLS (337,511). Subyacente NSA de septiembre (CPILFENS) 339,287, idéntico al BLS.
- Matiz: el general desestacionalizado sube **0,351 %**, muy cerca del umbral de redondeo (0,35); con un par de milésimas menos habría salido 0,3 %. Es un dato en el borde, no una cifra holgada.
- FRED tiene **octubre-2025 vacío** («.») tanto en CPIAUCSL como en CPILFESL: confirma que no hay tasa interanual oficial de ninguna de las dos series.
- **Gasolina +37,4 % a 12 meses: resuelto, no es un error de impresión.** La Tabla 1 del BLS (cpi.t01.htm) sí publica un índice de octubre-2025 para unas pocas series: gasolina (todos los tipos) **277,021**, coches nuevos 178,723 y coches usados 186,962. Gasolina oct-2026 = 380,510 → 380,510 / 277,021 = 1,3736 → **+37,4 %** (coincide). Coches nuevos +0,7 % y usados −3,3 % a 12 meses salen igual por esa vía. El resto de líneas (incluidas general, subyacente, vivienda, alimentos, energía) salen con «-». El comunicado no explica por qué esas series sí tenían índice de octubre-2025 [VERIFICAR el motivo; la ficha de «approximating missing data» del BLS solo describe la media geométrica para contratos y no lo aclara].
- Tabla 1 / Tabla 3 (BLS), niveles sin desestacionalizar de octubre-2026 que faltaban en W01b: alimentos 352,359; energía 340,061; subyacente (sin alimentos ni energía) 339,921; vivienda 432,745; servicios sin energía 449,901; electricidad 307,673; gas por red 263,875. Subyacente sin desestacionalizar sept→oct **+0,2 %**; gasolina −0,7 % sin desest.
- Otros detalles de la Tabla 3 (desestacionalizados, oct): servicios sin alquiler de vivienda **+0,5 %**; subyacente sin vivienda ni energía ni coches usados **+0,4 %**; transporte (servicios) +0,8 %; seguro del automóvil +0,7 %; coches usados −1,2 %.
- Cálculo propio no oficial (la BLS advierte de que estas aproximaciones no son oficiales): si se aproxima oct-2025 con la media geométrica de sep-2025 (324,245) y nov-2025 (325,063) de CPIAUCSL, sale 324,654 y un interanual aproximado del general de **≈ +3,9–4,0 %**. Coincide con el ≈4 % que citaba la prensa [S] en la previa, pero **no es dato oficial**.

## 2. Reacción del mercado hoy 10-nov (post-14:30 Madrid)
Fuente: Yahoo Finance, API de gráficos con barras de 5 min [S] (índices con retraso posible; futuros de tipos de CME vía Yahoo) y Tesoro de EE. UU. [P]. «Pre» = última barra antes del dato (13:25 UTC); «post» = primera barra tras el dato (13:35 UTC); «último» = 17:25–17:40 UTC. No se mezclan contratos: futuros del S&P/Nasdaq son los de diciembre (ES=F, NQ=F); Brent es el contrato frontal (BZ=F).
| Activo | Pre (13:25) | Post (13:35) | Último (≈17:30–17:40) | Cambio pre→último |
|---|---|---|---|---|
| Futuro S&P 500 (ES=F) | 7.579,25 | 7.536,75 | 7.514,50 | −0,85 % |
| Futuro Nasdaq 100 (NQ=F) | 27.929,75 | 27.706,00 | 27.651,00 | −1,00 % |
| Rendimiento Tesoro 10 años (^TNX) | 4,901 % | 4,934 % | 5,017 % | +11,6 pb |
| Rendimiento Tesoro 5 años (^FVX) | 4,716 % | 4,764 % | 4,843 % | +12,7 pb |
| Letra 13 semanas (^IRX) | 4,080 % | 4,107 % | 4,120 % | +4 pb |
| Índice dólar (DXY) | 101,765 | 101,982 | 102,350 | +0,57 % |
| EUR/USD | 1,1216 | 1,1189 | 1,1153 | −0,56 % |
| Bitcoin (BTC-USD) | 74.255 | 73.805 | 72.815 | −1,9 % |
| XRP (XRP-USD) | 1,0775 | 1,0695 | 1,0485 | −2,7 % |
| XLM (XLM-USD) | 0,1454 | 0,1443 | 0,1427 | −1,9 % |
| Ether (ETH-USD) | 2.093,6 | 2.063,4 | 2.015,8 | −3,7 % |
| Brent (BZ=F, frontal) | 90,32 | 89,27 | 91,92 | +1,8 % |

Índices al contado (se abren a las 14:30 UTC, es decir **después** del dato; comparación con el cierre del 9-nov): S&P 500 cierre 9-nov 7.549,94 → apertura 14:30 UTC 7.511,40 (−0,51 %) → 17:40 UTC **7.473,59 (−1,01 %)**; Nasdaq Composite 25.253,14 → 24.834,89 (**−1,66 %**); Dow Jones 52.389,75 → 52.041,52 (**−0,66 %**). Son datos intradía, no cierre.

- Tesoro a 2 años: la curva oficial del Tesoro de hoy **aún no está publicada** (la última fila es la del 9-nov: 2 años 4,56 %, 10 años 4,88 %) [P]. Yahoo no da el 2 años intradía; el 5 años (+12,7 pb) es el proxy más cercano. Cifra del 2 años de hoy: [VERIFICAR] cuando el Tesoro publique la curva. (Ojo: ^TNX 10 años cerró el 9-nov en 4,864 % según Yahoo y 4,88 % según el Tesoro; son mediciones distintas.)
- **Probabilidad de la Fed en diciembre [P, CME FedWatch, leída en Chrome; datos de 10-nov-2026 11:35:49 CT = 17:35 UTC]:** reunión del 9-dic (contrato ZQZ6, precio medio 95,9225, rango actual 375–400 pb). **Sin cambio 0,0 %; subida 100 %**, repartida en **88,5 % para 400–425 pb (+25 pb)** y **11,5 % para 425–450 pb (+50 pb)**. Comparación de la propia tabla: el 9-nov (1 día antes) sin cambio 16,0 % / +25 pb 84,0 % / +50 pb 0,0 %; el 3-nov (1 semana) 22,6 % / 77,4 % / 0,0 %; el 9-oct (1 mes) 15,9 % / 69,8 % / 14,3 %. Es una probabilidad implícita en el mercado de futuros, no una decisión ni una previsión de la Fed. Por tanto, desde ayer la probabilidad de una subida pasó de 84 % a 100 % y apareció un 11,5 % para +50 pb. (Cuándo cambió exactamente, antes o después de las 13:30 UTC, no se puede separar con esta tabla: solo tiene cortes diarios.) Cálculo propio previo [S] con los futuros de fondos federales a 30 días de CME vía Yahoo: Dic-26 (ZQZ26) cotizó 95,945 a las 13:25 UTC y 95,915 a las 17:29 UTC (cierre del 9-nov 95,975); Nov-26 (ZQX26) 96,120 sin cambios; Ene-27 (ZQF27) 95,865 → 95,815. Tipo implícito = 100 − precio: Dic 4,055 % → 4,085 % (cierre previo 4,025 %), Nov 3,880 %. Es decir, **el mercado descuenta unos 3 pb más de tipo medio en diciembre que justo antes del dato (≈6 pb más que el cierre de ayer)**. Convertirlo en una probabilidad exacta exige supuestos (tipo efectivo vigente, días anteriores y posteriores al FOMC del 9-dic, posible ruido de fin de mes). Tomando Nov como tipo vigente (3,88 %), una subida de 25 pb el 9-dic daría una media de diciembre de ≈4,06 %, y el 4,085 % cotizado ya está **por encima** de eso: apunta a que el mercado da por muy probable una subida y parte de otra más adelante. Después se leyó FedWatch y confirma ese cálculo: 100 % de subida con 11,5 % de +50 pb.
- Atribución: no se puede asignar toda la caída al IPC. Los rendimientos y el dólar siguieron subiendo entre las 13:35 y las 17:25 UTC, mientras el Brent rebotaba desde 89,3 a 91,9 y el S&P venía de subir +2,35 % el 9-nov [S]; hay otros factores (petróleo, geopolítica, posicionamiento).

## 3. HECHOS vs OPINIONES
**HECHOS**
- [P] BLS 10-nov: general +0,4 % y subyacente +0,3 % mensuales desestacionalizados; FRED lo confirma con niveles (+0,351 % y +0,296 %). Sin tasa interanual oficial.
- [P] El subyacente lleva tres meses seguidos en +0,3 %; servicios sin alquiler de vivienda +0,5 %.
- [S] Tras las 13:30 UTC: rendimientos del Tesoro más altos (10 años +11,6 pb hasta 5,017 %), dólar más fuerte, renta variable y cripto más bajas, futuros de tipos descontando algo más de subida en diciembre.
- [P] Fed en 3,75–4,00 % (subida de 25 pb en septiembre; mantuvo el 28-oct con 10–2); próximo FOMC 8–9 dic; el IPC de noviembre sale el 10-dic, un día después.

**OPINIONES / [ESPECULACIÓN]**
- La reacción es coherente con «inflación más alta que lo esperado → más probabilidad de subida de tipos». Pero es un día, intradía, y mezcla factores.
- Si el petróleo cede (Brent −16 % en la semana al 6-nov [S]), el general de noviembre podría moderarse; hoy el Brent rebota.

## 4. Caso alcista y bajista para activos de riesgo y cripto (sin recomendar operar)
- **Bajista:** subyacente +0,3 % tres meses, servicios sin alquiler +0,5 %, rendimiento a 10 años por encima del 5 % y dólar más fuerte endurecen las condiciones financieras; la cripto (que cae más que el S&P: XRP −2,7 %, ETH −3,7 % frente a −0,85 % del futuro S&P) suele comportarse como activo de liquidez/beta alta [ESPECULACIÓN].
- **Alcista:** parte del general viene de energía y alimentos (volátiles), no de un repunte generalizado; vivienda no rebota; usados −1,2 %; el subyacente sin vivienda ni energía sube pero la media de tres meses del subyacente no acelera; los movimientos de hoy son moderados frente al +2,35 % del S&P ayer, y una subida de tipos ya estaba en gran parte descontada [ESPECULACIÓN].
- **Matiz:** un solo mes, sin comparación interanual oficial y con el general en el borde del redondeo (0,351 %). Una lectura aislada no cambia la tendencia; el IPC de noviembre (10-dic) llega después del FOMC.

## 5. Sesgos y límites de las fuentes
- Yahoo Finance es agregador [S]: datos intradía con posible retraso, sin hora oficial de cierre; los futuros de tipos vía Yahoo no son CME FedWatch. El Tesoro y el BLS/FRED son [P].
- Las horas son barras de 5 minutos; «pre/post» tienen una resolución de 5 min, no de segundos.
- Los movimientos de cripto y renta variable pueden deberse a noticias distintas del IPC (hay 4 horas entre «post» y «último»).
- Mi interanual aproximado (≈4 %) es un cálculo propio no oficial.

## 6. [VERIFICAR] que quedan
Cerrados con fuente primaria: contraste con FRED, la rareza de la gasolina (Tabla 1 del BLS) y la probabilidad de la Fed de diciembre (CME FedWatch, leída en Chrome; la primera lectura con script devolvía la página vacía, la segunda en navegador con pantalla sí cargó la herramienta).
1. **No se puede abrir aún (a las 17:50 UTC):** la fila del 10-nov de la curva del Tesoro (2 años); la publica el Tesoro tras el cierre y la tabla termina en el 9-nov (2 años 4,56 %). Se intentó también un futuro de rendimiento a 2 años en Yahoo (2YY=F) y no devolvió datos. Cifra del 2 años de hoy: [VERIFICAR] mañana.
2. **No se puede abrir aún:** el cierre de las bolsas de EE. UU. de hoy (cierran a las 21:00 UTC); las cifras de índices son intradía.
3. Motivo por el que el BLS tiene índice de octubre-2025 solo para gasolina, coches nuevos y usados: la tabla lo muestra, el comunicado y la ficha de datos faltantes no lo explican. [VERIFICAR] con el BLS (cpi_info@bls.gov o nota técnica de la Tabla 1).

## Seguridad
Sin claves ni secretos; solo lectura web de BLS, FRED, Tesoro y Yahoo (sin iniciar sesión). Sin workflows ni API de Anthropic; sin commit ni push; no se tocó `privado/` ni `cerebro/`.

## Contraste adicional: serie CPILFESL descargada por Joel (10-nov-2026)
Fuente: archivo `CPILFESL.csv` de FRED (St. Louis Fed; datos del BLS) que Joel bajó a mano; ene-oct 2026, índice 1982-84=100. Nivel P para los niveles (copia fiel de la serie oficial); los cambios son cálculo propio sobre esos niveles.

| Mes | Índice | Cambio mensual (cálculo propio) |
|---|---|---|
| Ago-2026 | 337,765 | +0,290 % |
| Sep-2026 | 338,896 | +0,335 % |
| **Oct-2026** | **339,900** | **+0,296 %** |

- **Confirma el dato de octubre:** 339,900 y +0,296 % coinciden con lo leído en FRED y con el +0,3 % del BLS. Queda cerrado ese [VERIFICAR].
- **Septiembre ya era +0,335 %**, redondeado a +0,3 %: dos meses seguidos por encima de 0,29 %. Junio fue −0,017 % y marzo-abril +0,196 % y +0,376 %: la serie es irregular.
- **Sin interanual:** el archivo empieza en enero de 2026 y no trae octubre-2025 (el BLS no recogió precios por el cierre del Gobierno), así que no se puede calcular el +X % a 12 meses. Lo que sí sale (cálculo propio, no cifra oficial): enero→octubre +2,14 % (≈ +2,9 % anualizado en 9 meses) y últimos 3 meses ≈ +3,7 % anualizado [ESPECULACIÓN si se lee como tendencia: tres meses son pocos datos y los meses sueltos oscilan].
- **Lectura prudente:** la subyacente mensual lleva un ritmo algo superior al del arranque de año; un solo mes no cambia la conclusión sobre la Fed. Caso alcista para activos de riesgo: el +0,3 % encaja con el escenario de inflación contenida. Caso bajista: dos meses seguidos por encima de 0,29 % refuerzan a quienes esperan tipos altos más tiempo. Sin recomendación de operar.
