# Chrome 11-nov-2026: EIA (Brent/WTI), Fed 10-nov y mandatos C140

Leído con Claude in Chrome, solo lectura (sin login, captcha, cookies ni descargas). Sin recomendaciones de inversión.

## 1. EIA, precios spot (USD/barril)
Fuentes: eia.gov/dnav/pet/hist/RBRTED.htm (Brent) y RWTCD.htm (WTI Cushing), leídas 11-nov; tabla diaria eia.gov/petroleum/prices (fuente de los datos: Refinitiv, según EIA).

| dato · antes · después · fuente |
|---|
| Brent 22-oct · sin dato en el repo · **125,39** · EIA RBRTED |
| Brent 23-oct · sin dato en el repo · **128,30** · EIA RBRTED |
| WTI 22-oct · sin dato en el repo · **104,27** · EIA RWTCD |
| WTI 23-oct · sin dato en el repo · **109,72** · EIA RWTCD |
| Brent 3-nov / 4-nov / 5-nov / 6-nov · — · 107,03 / 91,84 / 97,96 / 97,83 · EIA tabla diaria |
| Brent 9-nov / 10-nov (último disponible) · — · **91,03 / 90,16** · EIA tabla diaria |
| WTI 9-nov / 10-nov (último disponible) · — · **90,40 / 89,62** · EIA tabla diaria |

HECHOS: semana 19-23 oct, Brent 118,82 / 115,22 / 117,37 / 125,39 / 128,30 y WTI 110,01 / 107,89 / 103,95 / 104,27 / 109,72 (lun-vie). Máximo Brent de la serie visible reciente: 130,18 (8-oct). Caída 3-nov a 4-nov: Brent -15,19 USD (107,03 a 91,84).
Nota: la página de histórico solo llega hasta el 3-nov; el 4 a 10-nov salen de la tabla diaria corta. Brent-WTI 10-nov: 0,54 USD (el diferencial era ~19 USD el 23-oct). [VERIFICAR] si el dato spot de Brent EIA/Refinitiv difiere del futuro ICE.

## 2. Fed, 10-nov-2026 (federalreserve.gov/newsevents/speeches-testimony.htm)
Tres intervenciones ese día: Waller (Bank of England Watchers Conference, Londres), Bowman (CFR, Washington; mismas palabras en Unleash Prosperity Now).

| dato · antes · después · fuente |
|---|
| Waller: ¿subir tipos? · — · SÍ: «leaning toward» +25 pb en la reunión de diciembre; si el IPC de octubre (publicado ese día) repite ~0,3 % mensual en el núcleo, cree que debería considerarse +50 pb (ya que +25 pb pondría en riesgo la credibilidad) · federalreserve.gov/newsevents/speech/waller20261110a.htm |
| Waller: reunión de octubre · — · votó con la mayoría por mantener; dice que lo esencial es que las subidas comunicadas se ejecuten, no el calendario exacto («no hace falta subir en reuniones consecutivas») · misma fuente |
| Bowman: rango vigente · — · 3-3/4 a 4 % (mantenido en octubre); menciona «the recent rate increase» · .../bowman20261110a.htm |
| Bowman: postura · — · prioridad a la inflación («more attentive to the inflation side»), pero «el beneficio de más endurecimiento hay que sopesarlo» por condiciones financieras más duras; la política «no está en una senda fijada» · misma fuente |
| Bowman: inflación · — · PCE subyacente 12 m probable 3,3 % en octubre (según el IPC de hoy); desempleo 4,1 % (oct) · misma fuente |
| Bowman: petróleo · — · Brent «por encima de 110» en 2.ª mitad de octubre y caída fuerte la semana pasada por esperanza de acuerdo EE. UU.-Irán tras las midterms · misma fuente (concuerda con EIA) |
| Waller: energía · — · seguros y trasbordos por Ormuz añaden 20-30 USD/barril, según informes [VERIFICAR] · waller20261110a |

Respuesta a la pregunta: SÍ hay uno que habla de subir más rápido: Waller (opinión suya, no del FOMC; las notas al pie dicen que son vistas propias). Bowman es más cauta y no propone subir más rápido. [ESPECULACIÓN] que diciembre acabe en +25 o +50: depende del IPC y de los datos posteriores; no hay decisión.

## 3. C140, mandatos con nivel [S] en explorador/mandatos.json
Hay 62 entradas con `"nivel": "S"` (previos de DE, FR, NL, PL y otros). Verificadas 3:

| dato · antes · después · fuente |
|---|
| FR Chirac, desde 17-may-1995 · S · **P** (investidura, fecha leída) · elysee.fr/jacques-chirac |
| FR Chirac (mandato 1995-2007), Sarkozy (2007-2012), Hollande (2012-2017) · S · años P (lista oficial de presidentes); días de fin 16-may-2007, 15-may-2012 y 14-may-2017 siguen S · elysee.fr/la-presidence/les-presidents-de-la-republique |
| FR Sarkozy: elección 6-may-2007 (53,06 %) · — · P como elección, no como inicio del mandato · elysee.fr/nicolas-sarkozy |
| FR Hollande: «Mai 2012» llega a la presidencia · S · P solo el mes · elysee.fr/francois-hollande |
| PL gov.pl/web/premier · S · sin cambio: la portada solo muestra a Tusk actual, sin histórico (no sube) · gov.pl |
| NL Rijksoverheid (Balkenende/Rutte/Schoof) · S · sin cambio: las rutas de kabinetten dan 404 (no sube) · rijksoverheid.nl |
| DE bundeskanzler.de (días exactos Schröder/Merkel/Scholz) · S · sin cambio: la página redirige a otro dominio y la herramienta corta la lectura (no sube) · bundeskanzler.de |

Propuesta de cambio (no aplicada; explorador/*.json no se toca): subir a P solo «Jacques Chirac desde 1995-05-17» (si el esquema distingue desde/hasta); dejar el resto en S con nota «años P, día S».

## Accesos
EIA, federalreserve.gov, elysee.fr y gov.pl: FUNCIONAN en Chrome (EIA: la tabla se lee con `javascript_tool` por celdas; la salida con guiones largos se bloquea, sustituirlos por `/`). rijksoverheid.nl: rutas probadas 404. bundeskanzler.de: redirige y se corta. Sin captcha ni login. Pestaña propia cerrada; otra pestaña de CNMV apareció en el grupo y no es mía (no se cerró).

## Resumen
1. EIA: Brent 125,39 y 128,30 (22 y 23-oct), WTI 104,27 y 109,72; último dato 10-nov: Brent 90,16, WTI 89,62.
2. Fed 10-nov: Waller se inclina por +25 pb en diciembre y +50 pb si el IPC de octubre sale alto (opinión suya); Bowman, más cauta, sopesa el coste de endurecer.
3. C140: solo Chirac desde 17-may-1995 sube a P; DE, NL y PL no se pudieron leer.
