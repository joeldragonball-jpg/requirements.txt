---
tema: Fuentes primarias que el canal "Despeja La X" y otros suelen citar (dónde mirar directamente)
etiquetas: [fuentes, primarias, verificacion, bis, fsb, blackrock, ripple, stellar, sec, bce, fed, despeja-la-x]
actualizado: 2026-10-14
---
# Fuentes primarias recurrentes (para no depender del vídeo)

## Resumen
Cuando un vídeo dice "BIS pone fecha" o "BlackRock confirma", lo útil es ir a la fuente que cita y leer el original. Esta lista recoge las fuentes primarias más repetidas, qué mirar en cada una y si se puede abrir con las herramientas del proyecto. Un canal que cita a varios organismos sigue siendo UNA fuente: lo que cuenta es el documento original.

## Explicación
Estado de acceso: "curl" = prueba del 14-oct-2026 con navegador simulado; "WebFetch" = lo que ya se pudo leer en sesiones de research. Un 403 de curl no implica que el navegador de Joel no abra la página.

| Fuente | Dirección | Qué mirar | Acceso |
|---|---|---|---|
| FSB (hoja de ruta G20 de pagos transfronterizos) | https://www.fsb.org/work-of-the-fsb/market-and-institutional-resilience/cross-border-payments/ | Objetivos de 2027, informes de progreso | curl 200 |
| BIS / CPMI | https://www.bis.org/cpmi/ y https://www.bis.org/press/ | Actas, informes del grupo de interoperabilidad, discursos | curl sin respuesta; WebFetch OK (actas CPMI leídas el 14-oct) |
| Swift / Sibos (fechas y vídeo de entrevistas) | https://www.swift.com/sibos | Fechas oficiales de Sibos 2026 y 2027, Sibos TV | curl 403 y WebFetch 403: mirar a mano |
| BlackRock (notas de prensa) | web corporativa de BlackRock y Business Wire | Comunicados sobre fondos tokenizados (BSTBL, BRSRV) | La dirección de prensa probada dio 404 [VERIFICAR la dirección actual] |
| SEC | https://www.sec.gov/newsroom/press-releases | Comunicados, Crypto Task Force | curl 403: probar a mano |
| CFTC | https://www.cftc.gov/PressRoom/PressReleases | Comunicados, criptoderivados | curl 200 |
| Ripple | https://ripple.com/insights/ | Comunicados y alianzas (Meritz, RLUSD…) | curl 200 |
| XRP Ledger | https://xrpl.org/blog | Enmiendas, versiones de `xrpld` | curl 200 |
| Stellar | https://stellar.org/blog | Anuncios, RWA, validadores | curl 200 |
| BCE (euro digital) | https://www.ecb.europa.eu/euro/digital_euro/html/index.en.html | Calendario, decisiones | curl 200 |
| Reserva Federal (calendario FOMC) | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | Fechas de reuniones, actas | curl 200 |
| BLS (IPC, PPI) | https://www.bls.gov/news.release/cpi.nr0.htm y https://www.bls.gov/news.release/ppi.nr0.htm | Dato oficial del día | WebFetch OK; curl 403 |
| EIA (petróleo) | https://www.eia.gov/outlooks/steo/ | STEO mensual | curl 200 |
| CME FedWatch | https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html | Probabilidades de tipos | 403: usar fuente secundaria con hora |
| AIE (informe petrolero) | https://www.iea.org/topics/oil-market-report | Informe mensual | 403: usar notas de prensa o la EIA |
| Congreso de EE. UU. | https://www.congress.gov/ | Estado de la ley CLARITY | 403: mirar a mano |
| CNMV | https://www.cnmv.es/ | Advertencias, normativa | curl 200; WebFetch 403 en algunas páginas |

## Puntos clave
- Para cada afirmación de un vídeo: (1) apuntar el minuto con `python scripts/videos.py <enlace>` (sin IA); (2) abrir la fuente primaria; (3) marcar [VERIFICADO fecha] o [VERIFICAR] en el apunte.
- Los fondos de BlackRock, las alianzas de Ripple o las entrevistas de Sibos TV se confirman en su comunicado o en el vídeo original, no en el resumen de un tercero.
- Si una fuente da 403 a las herramientas, no se infiere nada: se anota "no abierta" y se usa una secundaria con fecha y hora.

## Conceptos
Fuente primaria = documento o comunicado original del organismo. Fuente secundaria = prensa o canal que lo comenta. El mismo canal citando varios organismos no suma confirmaciones.

## Cifras y datos importantes
Sin cifras: es una lista de dónde mirar. Las direcciones se probaron el 14-oct-2026 y pueden cambiar.

## Opiniones y predicciones
Ninguna.

## Relación con mi cartera (XRP / XLM)
Es el camino para distinguir catalizadores reales (comunicados, leyes, actas) de titulares de canal. No contiene recomendaciones.

## Fiscalidad en España
No aplica. Fuentes fiscales: BOE y aeat.es (ver los dossiers de fiscalidad).

## Dudas y datos a verificar
- Dirección actual de las notas de prensa de BlackRock [VERIFICAR].
- Si Swift permite leer las fechas de Sibos 2027 sin navegador.
- Revisar esta lista cada mes con la auditoría.
