# W01 · Tipos de interés (lunes)

Sesión del 25-oct-2026 (archivo del 26-oct según la rotación). Informativo: no es recomendación de compra ni de venta. [P] = documento oficial leído; [S] = prensa o agregador; [VERIFICAR] = sin confirmar; [ESPECULACIÓN] = opinión.

## 1. Qué cambió en el radar (`explorador/regulacion.json`, celdas `politica`)

| País | Antes | Ahora | Fuente |
|---|---|---|---|
| Rusia | 14,00 %, sentido del último cambio sin verificar, reunión del 23-oct pendiente | **Mantiene 14,00 % el 23-oct** (segunda pausa tras la del 11-sep); próxima reunión **18-dic**; la previsión de inflación de 2026 sube a 7,1-7,6 % (antes 6-7 %) | [P] nota de cbr.ru (decisión y fecha); [S] Reuters/Moscow Times (previsión) |
| China | LPR 3,0 % / 3,5 % de jul-ago; fijación del 20-oct pendiente | LPR sin cambios el 20-oct (17.º mes); BIS 3,00 % | [S] Trading Economics; pbc.gov.cn no se abrió |
| Indonesia | 5,75 % «de septiembre» | **Mantiene 5,75 % el 21-oct**; sube la facilidad de depósito a 5,00 % (crédito 6,50 %); rupia −7,9 % en el año | [S] prensa indonesia/RRI; BIS 5,75 % |
| Sudáfrica | 7,25 %, sin próxima reunión | Próxima reunión del MPC: **19-nov** | [P] resbank.co.za («Upcoming Announcements») |

Sin cambios tras contrastar con el BIS (WS_CBPOL, leído a las 21:20 UTC del 25-oct): India 5,50 %, Corea 3,00 %, Japón 1,25 %, Hong Kong 4,25 %, México 6,50 %, Suiza 0,00 %. Fed 3,75-4,00 %, BCE 2,50 %, BoE 3,75 % y Canadá 2,25 % coinciden con el panel `tipos_vivos`.

## 2. Sudáfrica: no se pudo pasar el 7,25 % a [P]
- resbank.co.za respondió 404 en la URL del comunicado de septiembre y la página de tipos vino con el valor vacío (se carga con JavaScript). No usé el navegador integrado para saltar nada: solo fetch normal.
- El 7,25 % (subida de 25 pb con efecto el 25-sep, unánime 6-0) sigue en [S] prensa (EWN, Briefly) + BIS. La celda queda en [S] con el hueco anotado. Solo la fecha de la próxima reunión (19-nov) es [P].

## 3. Reuniones de bancos centrales, próximos 14 días (hasta el 8-nov)

| Fecha | Banco | Fuente oficial | En calendario |
|---|---|---|---|
| 28-oct | Fed (FOMC, decisión 14:00 ET) | federalreserve.gov | ya estaba |
| 28-oct | Banco de Canadá (09:45 ET) | bankofcanada.ca (calendario 2026) [P] | **añadido** |
| 29-oct | BCE (decisión) | ecb.europa.eu | ya estaba |
| 29-oct | HKMA y CBUAE replican a la Fed | por fórmula, sin reunión propia | **añadido** (aproximado) |
| 30-oct | Banco de Japón (29-30, Outlook Report) | boj.or.jp | ya estaba |
| 3-nov | RBA (2-3 nov, 14:30 Sídney) | rba.gov.au [P] | **añadido** |
| 3-4 nov | Copom (Brasil) | fecha de prensa; el calendario del BCB no cargó [VERIFICAR] | ya estaba (aproximado) |
| 5-nov | Banco de Inglaterra | bankofengland.co.uk («2026 confirmed dates») [P] | **añadido** |
| 19-nov (fuera de ventana) | MPC del SARB | resbank.co.za [P] | **añadido** |

[VERIFICAR] En el encargo se hablaba de un Copom el 28-29 oct: no consta; la fecha de prensa es 3-4 nov. Banxico (nov), Bank Indonesia (nov), Banco de Corea (26-nov, ya en radar) y Banco de Rusia (18-dic): solo Corea y Rusia tienen fecha oficial leída. Banxico: no localizada [VERIFICAR]. Nota menor: el calendario dice que el BCE subió el 10-sep y el radar 16-sep; la API da 16-sep como fecha de efecto.

## 4. Lectura (sin predecir precios)
- **Sesgo**: los que se mueven son hawkish o en pausa vigilante (Rusia mantiene pero sube su previsión de inflación; Indonesia mantiene pero endurece el depósito para defender la rupia; Corea abre la puerta a subir en nov). China es la excepción acomodaticia estable; Brasil recorta con cautela.
- **Liquidez**: la dirección global sigue siendo de endurecimiento con petróleo alto (Brent previsto $105 en el 4T según la EIA, ya en calendario); dólar y rendimientos altos (10 años 5,09 %) son el canal de la liquidez de riesgo.
- **Caso alcista / bajista para cripto**: alcista, si el FOMC del 28 mantiene y habla de pausa, bajaría la presión sobre dólar y bonos; bajista, si repite sesgo de subidas con energía +20 % interanual en el IPC. Es un escenario, no una previsión [ESPECULACIÓN]. El mercado daba ~8 % de subida para el día 28 (CME FedWatch, 22-oct [S]).

## Qué vigilar
1. FOMC (28-oct) y BCE/BoJ (29-30-oct): sesgo de la nota, no solo la decisión.
2. Pendiente de lectura primaria: SARB (comunicado), PBoC (LPR), Bank Indonesia (comunicado) y calendario oficial del Copom/Banxico.

## Seguridad
- Sin claves ni tokens tocados; solo lecturas con WebFetch/WebSearch, sin saltar anti-bots.
- No se lanzó ningún workflow ni API de Anthropic; sin commit ni push.
- Comprobación diaria de seguridad: no repetida en esta sesión (tarea de datos); no verificado si hay avisos nuevos hoy.
