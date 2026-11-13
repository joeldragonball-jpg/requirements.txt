# W09 · Resumen semanal (viernes 13-nov-2026) y plan del 14 al 22-nov

Rutina desatendida. Etiquetas: [P] primaria leída · [S] prensa o agregador · [VERIFICAR] · [ESPECULACIÓN]. Informativo; no es recomendación de compra ni venta. Sin búsquedas propias: se apoya en los R00 del 9 al 13-nov, los W de la semana y el W06 de hoy. Parte del W09 del 10-nov (`2026-11-10-W09-resumen-semanal.md`); no repito lo de allí.

## 1. Qué cambió de verdad (10 → 13-nov)
- **Tipos y deuda:** el bono de EE. UU. a 10 años pasó de 4,86 % (9-nov) a 4,98 % (10-nov, +12 pb) y a **5,10 %** el 13-nov a las 07:07 UTC, máximo de la serie del repo [S, Yahoo vía `precios_r00.json`; AP da 5,07 %; dato oficial del Tesoro sin leer]. El IPC de octubre de EE. UU. salió el 10-nov: general +0,4 % mensual, subyacente +0,3 %, **sin tasa interanual oficial** [P, BLS y FRED, `2026-11-10-W01b-ipc-dato.md`].
- **Bolsa:** S&P 500 en máximo de la serie el 11-nov (+1,3 %, chips +6 %) y −0,4 % el 12-nov (7.592,4) tras la dimisión del consejero delegado de Nvidia [S, AP; motivo exacto **[VERIFICAR]**, no darlo por hecho]. VIX 17,5 → 18,7.
- **Energía:** Brent de 90,7 $ (10-nov) a **96,5 $** (13-nov, +4,1 % en 24 h) después de que Trump dijera que ya no le interesa un acuerdo con Irán [S, AP]. Ormuz: 8 barcos el 1-nov frente a ~125 diarios antes de la guerra [S, Windward].
- **Oro:** de 4.125 $ (10-nov) a 3.900 $ (13-nov): cuatro caídas seguidas, mínimo de la serie del repo [S].
- **Cripto:** BTC de 74,5 k a 69,1 k (−6,0 % en las últimas 24 h; mínimo ~67.568 $ [S]); ETH bajo 2.000 $; miedo y codicia en 20 («miedo extremo»). **XRP** 1,085 → **1,026 $** y **XLM** 0,148 → 0,1447 $: nuevos mínimos de la serie, pero el 12-13 nov cayeron menos que BTC y ETH (causa [VERIFICAR]).
- **Regulación (EE. UU.):** sin votación programada de la Clarity tras las elecciones [S, W06]. Blumenthal fija dos fechas a Binance, Tether, World Liberty y Fight Fight Fight: 30-nov y 4-ene-2027 [S]. Trump en 60 Minutes (8-nov): «está lo cripto, y antes estuvo el petróleo» [S, cita localizada].
- **ETF:** los ETF de XRP rondan $1,47 mil M de activos con entradas casi nulas a 5-nov [S, W04 del 12-nov]; un medio da salidas de $10,42 M en un día (~10-nov) [VERIFICAR].
- **España (trabajo del 12-13 nov, pendiente de subir por Joel):** informes C232 (fiscalidad cripto y CASP), C237, C239 (Adamuz/Urda), C242 (votaciones), C243 (Renfe y Correos) y S6 (recaudación). No los resumo aquí: no forman parte de esta rutina.

Lectura alcista: la bolsa absorbió dos sustos (Nvidia, Irán) con −0,4 %; XRP y XLM aguantaron mejor que BTC en la última caída. Lectura bajista: petróleo y tipos largos suben a la vez, la combinación que más aprieta a los activos de riesgo; XRP ha perdido todos los soportes que citaba el canal salvo 1 $. Ambas son [ESPECULACIÓN].

## 2. Qué se verificó
- IPC de octubre de EE. UU. [P] (cerró el [VERIFICAR] que arrastraban los R00 del 10 al 12-nov; nota C253).
- W05 (12-nov): 7 puntos, 0 cerrados con primaria, 5 parciales, 2 abiertos.
- W06 (hoy): v086 (Trump) pasa a cita confirmada; v082, v098 y v107 a «compatible»; 4 voces nuevas (v165-v168); predicciones #68-#70.
- W03 (11-nov): Japón y Singapur; W04 (12-nov): pasada corta, todo [S].

## 3. Qué falló o quedó en [VERIFICAR]
- Cierres de Asia del 13-nov: no reconstruibles. 10 años oficial (Tesoro), cifra de liquidaciones cripto, motivo de la salida de Huang, fecha del IPP.
- W04 sin EDGAR: 13F del 3T sin leer; Evernorth (XRPN) con datos que se contradicen (¿cotiza ya o SPAC pendiente?).
- W06: nada pasó de [S] (faltan CBS, cartas del Senado, fsb.org); el vídeo del 10-nov sigue sin subtítulos.
- Relock del escrow del 1-nov: sigue sin leer en el ledger.
- Seguridad: `seguridad_rapida.py` dio 🔴 el 13-nov por una entrada nueva de CISA KEV (Chromium); no es del código del repo, pero queda para Joel.
- Git: el R00 de hoy se subió desde otra copia y esta carpeta tenía trabajo de anoche sin subir; hubo que reconciliar a mano (detalle en `informes/rutinas/2026-11-13-W06.md`).

## 4. Fechas que importan (14 → 27-nov) y qué lanzar
| Fecha | Evento | Prompt |
|---|---|---|
| 16-nov (lun) | Plazo del 13F del 3T (quién tiene ETF de XRP/XLM) | W04 (con Chrome/EDGAR) |
| 18-nov | IPC de octubre del Reino Unido (ONS); subastas a 20 años de EE. UU. ($16 mil M) y Japón; APEC en Shenzhen (18-19) | W01, W02 |
| 19-nov | Banco de la Reserva de Sudáfrica; subastas de España y Francia | W01, W02 |
| 20-nov | China: LPR mensual | W01 |
| 23-nov | Stellar: voto de mainnet de Protocol 30 (Bell) | EV posterior |
| 25-nov | PCE de octubre y PIB de EE. UU. (2.ª estimación); Korea Fintech Week | W01, W08 (último miércoles) |
| 26-27 nov | Banco de Corea; S&P revisa Francia; 2.ª subasta de BTP | W01, W02 |
| 29-30 nov | Elecciones en España; OPEP+; plazo de Ormuz (#24) y de World Liberty (#68) | W11, W10, W06 |

## 5. Coste de la semana y cuota
- Semana de cuota: del 10-nov al 17-nov (00:59 UTC). Semanal al empezar esta rutina: **77 %** (Fable 71 %). Reserva del 10 %: quedan ~13 puntos utilizables.
- Costes anotados por las rutinas: R00 ≈ 0-2 % cada una; W02 ≈ 1,5 %; W03 < 1 %; W04+W05 < 1-2 %; W12/W13 ≈ 0-1 %. El grueso (de ~33 % el 12-nov por la mañana a 76 % el 13-nov) se fue en los lotes B/C y en el trabajo de España del 12-13 nov, no en las rutinas.
- Coste de W06+W09 de hoy: ver `informes/rutinas/2026-11-13-W06.md`.

## 6. Lecciones (propuestas; no escritas en `cerebro/documentos/`)
- **patrones-de-bulos:** una cifra redonda en boca de un político («70 millones tienen cripto») puede ser una cifra real mal recordada (67 millones) y de otra fuente: buscar el número, no la frase.
- **fuentes-fiables-y-dudosas:** los resúmenes de búsqueda mezclan años (el Informe de Estabilidad de la Fed «del 4-nov» podía ser de 2025): sin fecha en la URL o en el texto, no vale como dato de este mes.
- **catalizadores-xrp-xlm:** en la caída del 12-13 nov XRP y XLM bajaron menos que BTC; sin catalizador propio comprobado, es una observación, no una señal.

## 7. Plan de la semana siguiente
Propuesta: **modo ahorro hasta el reinicio del 17-nov** (quedan ~13 puntos) y modo normal después.
1. Hasta el 16-nov: solo R00 y W10 (energía, por Brent e Irán). Nada de lotes grandes.
2. 17-nov en adelante: W04 con Chrome para el 13F (plazo 16-nov) y Evernorth; W01 (tipos: 10 años sobre 5 %, PCE el 25-nov); W02 (subastas del 18-19 nov).
3. W05: cerrar con primaria los [VERIFICAR] de esta semana (Nvidia 8-K, curva del Tesoro, PortWatch).
4. W06 del 20-nov: abrir originales de CBS, cartas de Blumenthal y fsb.org para subir v086, v107 y v168 a [P].
5. Pendiente de decisión de Joel: subir el trabajo de España del 12-13 nov que sigue en local.

## 8. Resumen (5 líneas) y vigilar
1. Tipos largos de EE. UU. por encima del 5 % y Brent a 96,5 $: sube el coste del dinero y de la energía a la vez.
2. Cripto en miedo extremo: BTC 69,1 k (−6 %), XRP 1,026 $ y XLM 0,1447 $ en mínimos de la serie.
3. Bolsa resistente: máximo el 11-nov y solo −0,4 % tras Nvidia e Irán.
4. Clarity sin calendario; presión demócrata (Blumenthal: 30-nov y 4-ene) y cita de Trump localizada.
5. Cuota semanal al 77 %: modo ahorro hasta el 17-nov.

Vigilar: (a) si el 10 años se mantiene sobre 5,1 % con el PCE del 25-nov a la vista; (b) el 30-nov: Ormuz, OPEP+, World Liberty y las elecciones en España del 29-nov.

## 9. Seguridad
Sin claves ni secretos en lo escrito · sin API de Anthropic ni workflows · `privado/` y los apuntes de `cerebro/` sin tocar.
