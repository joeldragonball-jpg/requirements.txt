# Expansión de la Órbita: huecos, fuentes y sesiones nuevas (14-nov-2026, solo lectura)

Base: `research/PLANNING.md` (22:07 UTC), `informes/research/2026-11-14-auditoria-orbita-cadenas.md`, listado de `explorador/` (tamaños y fechas de modificación) y búsqueda con grep de qué fuentes ya se leen en `scripts/`, `noticias/`, `alertas/` y `explorador.py`. No se ha editado ningún archivo salvo este. Información para decidir, no recomendación. `graphify-out/GRAPH_REPORT.md` es del 4-nov (commit 003ffa18): está desfasado; conviene `graphify update .` (sin coste de API).

## 1. Huecos de cobertura y fuentes que los cubrirían

### 1.1 Datos que se están quedando viejos (fecha de modificación en `explorador/`)
| Archivo | Última modificación | Problema |
|---|---|---|
| `liquidez-manual.json` | 7-nov (dato «2026-09») | El dato más viejo de la cabecera; es manual |
| `deuda-fmi.json`, `reservas.json`, `bancos-eba.json` | 21-22 oct | Más de 3 semanas; EBA es semestral (vale), reservas no |
| `bonos-manual.json` | 29-oct | Manual |
| `calificaciones.json`, `estabilidad.json` | 2-nov | 12 días; las agencias publican en viernes programados |
| `seguridad-eurostat.json`, `centro.json` | 4-nov | 10 días |
| `paises.json` | 10-nov | 29 huecos en la matriz (ya hay C275) |
| `edgar.json` | 8-nov | El plazo del 13F del 3T vence el 16-nov |
| `voces.json` | 🔴 27 sin confirmar, 13 > 14 días | Ya lo cubre W06 |

### 1.2 Fuentes que NO aparecen en ningún script (grep = 0) y su valor
Orden por valor/coste. «Script» = se lee con python sin IA; «Chrome» = la web bloquea lectores o es SPA.

| # | Fuente (oficial y gratuita) | Qué cubre | Acceso | Clave | Valor/coste |
|---|---|---|---|---|---|
| 1 | ESMA, registro provisional MiCA (CSV de CASP, emisores ART/EMT, no conformes) | Radar regulatorio UE: quién está autorizado y dónde | Script (CSV) | No | Alto / bajo |
| 2 | fiscaldata.treasury.gov (API: deuda «to the penny», tipos medios, MTS) | EE. UU.: deuda y déficit diarios/mensuales | Script (JSON) | No | Alto / bajo |
| 3 | FRED (ya se usa): WALCL, RRPONTSYD, WTREGEN + BCE Data Portal (balance) | Sustituir `liquidez-manual.json` por serie automática | Script | FRED: sí (gratis, secreto) | Alto / bajo |
| 4 | CFTC Commitments of Traders (API Socrata publicreporting.cftc.gov) | Posicionamiento en futuros de BTC, ETH, oro, bonos, divisas | Script | No | Medio-alto / bajo |
| 5 | OCDE Data Explorer (sdmx.oecd.org) y BIS Data Portal (stats.bis.org API) | Indicadores adelantados, tipos oficiales, crédito, vivienda por país | Script (SDMX) | No | Alto / medio |
| 6 | Calendarios oficiales: BLS (.ics), BEA (calendario), Eurostat (release calendar), INE (calendario), Fed/BCE (páginas) | Calendario automático en vez de manual | Script (ics/JSON); Fed/BCE a veces Chrome | No | Alto / medio |
| 7 | REE REData (apidatos.ree.es) e INE Tempus (IPV, IPVA alquiler) | España: energía (C233) y vivienda (C230) | Script | No | Medio-alto / bajo |
| 8 | DefiLlama (ya se usa, ampliar a /v2/chains y stablecoins por cadena) + Horizon de Stellar / rippled público | Métricas on-chain de las 16 redes sin tocar `cadenas.json` | Script | No | Medio / bajo |
| 9 | Emisores de ETF (holdings/flujos diarios en sus webs) + EDGAR 13F (ya se usa) | Flujos de ETF de XRP/XLM/BTC (C210) | Script parcial; muchas webs en Chrome | No | Medio-alto / medio |
| 10 | GDELT DOC 2.0 (sin clave) y ACLED (registro gratuito) | Conflictos y geopolítica por país | GDELT script; ACLED requiere cuenta (Joel) | ACLED: sí | Medio / medio |
| 11 | BEA API | PIB/PCE por componente | Script | Sí (gratis) | Medio / bajo (ya hay FRED) |
| 12 | ESIOS (REE) y ENTSO-E | Precio eléctrico por zonas | Script | Sí (token; C111 ya lo espera) | Medio / bajo |
| 13 | congress.gov API (api.data.gov) | Estado de CLARITY y leyes cripto en EE. UU. (C80B bloqueado por 403) | Script | Sí (gratis) | Medio / bajo |
| 14 | UN Comtrade | Comercio por país (chips, energía) | Script | Sí (gratis) | Bajo-medio / medio |

## 2. Sesiones nuevas propuestas (C279-C288)

Cada sesión escribe en un archivo NUEVO de `explorador/` (o en uno que hoy no toca ninguna otra fila), para no chocar con `cadenas.json` (C267/C270/C273/C274/C277), `datos.json` (C278) ni `vistas.html` (C268/C272). La conexión a la Órbita se hace en una sesión aparte o al final, cuando no haya otro agente en `vistas.html`.

```csv
id,origen,tema,estado,tipo,modelo,tam,est,real,prompt,cuando,falta,bloqueo,detalle
C279,C,"Radar regulatorio: registro provisional MiCA de ESMA (CASP, emisores ART/EMT, no conformes) por país, leído por script",pendiente,datos,Sonnet,M,~3 %,,"Sigue CLAUDE.md. Repo PÚBLICO; sin recomendaciones. Busca en esma.europa.eu la página del «Interim MiCA Register» y sus CSV (CASPS, ART, EMT, OTHER, NCASP). Crea scripts/leer_esma_mica.py (requests, sin IA, verificación de certificados activa) que descargue los CSV, cuente por país de origen y servicio, y guarde explorador/mica-registro.json con {fuente,url,fecha_lectura,nivel:P} y la lista de entidades (nombre, país, servicios, fecha de autorización). Si ESMA bloquea, ábrelo en Chrome y anota el motivo. No toques regulacion.json ni vistas.html: deja en el informe la propuesta de cómo mostrarlo en Radar regulatorio. python scripts/revisar_explorador.py (0 avisos). Informe en informes/research/. NO commit ni push.",15-nov,,,"expansión 14-nov; archivo nuevo"
C280,C,"ETF de XRP, XLM y BTC: flujos y patrimonio diarios desde las webs de los emisores y titulares del 13F del 3T (EDGAR)",pendiente,datos,Sonnet,M,~4 %,,"Sigue CLAUDE.md. Repo PÚBLICO; sin recomendaciones ni comparar con tesis. Tras el plazo del 13F (16-nov), usa scripts/leer_edgar.py (no lo reescribas: crea scripts/leer_etf_flujos.py) para listar quién declara ETF de XRP/XLM/BTC al 30-sep. Para cada ETF spot de XRP y XLM vivo, localiza en la web del emisor el CSV o la tabla de participaciones (acciones en circulación, NAV, tenencia en monedas) y calcula el flujo diario como variación de acciones × NAV; si la web es SPA, léela en Chrome y anótalo. Guarda explorador/etf-flujos.json con fuente, fecha y nivel por cifra (emisor = parte interesada). Agregadores (Farside, SoSoValue) solo como contraste [S]. Informe en informes/research/. NO commit ni push.",17-nov,,,"expansión 14-nov; archivo nuevo; cubre parte de C210"
C281,C,"EE. UU. fiscal y posicionamiento: Treasury Fiscal Data (deuda diaria, tipos medios, MTS) y CFTC COT (BTC, ETH, oro, bonos, divisas) por script",pendiente,datos,Sonnet,M,~3 %,,"Sigue CLAUDE.md. Repo PÚBLICO. Crea scripts/leer_eeuu_fiscal.py sin IA: API api.fiscaldata.treasury.gov (debt_to_penny, avg_interest_rates, mts_table_1) y API Socrata de publicreporting.cftc.gov (Commitments of Traders, informes legacy y TFF) para BTC y ETH de CME, oro, T-Note 10 años, EUR y JPY. Guarda explorador/eeuu-fiscal.json con series cortas (12 puntos), fuente, fecha y nivel P. Sin claves. Explica en el informe qué mide el COT y sus límites (posición neta ≠ previsión). No toques paneles.json ni vistas.html. revisar_explorador.py (0 avisos). NO commit ni push.",18-nov,,,"expansión 14-nov; archivo nuevo"
C282,C,"Países: OCDE (indicadores adelantados, paro, IPC) y BIS (tipos oficiales, crédito, vivienda) por SDMX para refrescar la ficha de cada país",pendiente,datos,Sonnet,M,~4 %,,"Sigue CLAUDE.md. Repo PÚBLICO. Crea scripts/leer_ocde_bis.py sin IA que lea sdmx.oecd.org (CLI, desempleo armonizado, IPC) y la API de stats.bis.org (WS_CBPOL tipos oficiales, WS_CREDIT_GAP, WS_SPP vivienda) para los países de explorador/paises.json. Guarda explorador/ocde-bis.json con último dato, fecha del dato, fuente y nivel P; marca qué indicadores de paises.json/indicadores-historia.json quedarían más frescos. No edites paises.json (C275 trabaja en él). revisar_explorador.py (0 avisos). Informe con tabla país × indicador (antes/después). NO commit ni push.",19-nov,,,"expansión 14-nov; archivo nuevo; no chocar con C275"
C283,C,"España: energía y vivienda por script (REE REData: precio, demanda y generación; INE Tempus: IPV e índice de alquiler) para C230/C233",pendiente,datos,Sonnet,M,~3 %,,"Sigue CLAUDE.md. Repo PÚBLICO. Crea scripts/leer_espana_energia_vivienda.py sin IA: apidatos.ree.es (mercados/precios-mercados-tiempo-real, demanda, estructura de generación, mensual) y la API JSON de INE Tempus (IPV por CCAA, índice de precios de vivienda en alquiler). Guarda explorador/espana-energia-vivienda.json con unidades explícitas (€/MWh, índice base, %), fuente, fecha y nivel P. Si MIVAU o Notariado se necesitan, solo en Chrome y como [S]. No toques espana.json ni espana-manual.json: deja en el informe cómo encajarlo (regenerar espana.json lo hace otra sesión). NO commit ni push.",19-nov,,,"expansión 14-nov; archivo nuevo"
C284,C,"Cadenas: métricas on-chain sin IA para las 16 redes (DefiLlama TVL y stablecoins por cadena, comisiones; Horizon de Stellar y rippled público) en archivo aparte",pendiente,datos,Sonnet,S,~2 %,,"Sigue CLAUDE.md. Repo PÚBLICO. Crea scripts/leer_cadenas_onchain.py sin IA: api.llama.fi/v2/chains, stablecoins.llama.fi/stablecoinchains y, para XRPL y Stellar, el servidor público de rippled (server_info) y Horizon (ledgers, fee_stats). Mapea las 16 ids de explorador/cadenas.json (solo leerlo) y guarda explorador/cadenas-onchain.json con TVL, stablecoins, fecha y nivel S (agregador). NO edites cadenas.json ni vistas.html (otras sesiones los usan). Documenta en el informe que DefiLlama cambia de metodología y que TVL ≠ uso real. NO commit ni push.",21-nov,,,"expansión 14-nov; archivo nuevo"
C285,C,"Liquidez global automática: sustituir liquidez-manual.json (dato de sep-2026) por series de FRED (balance Fed, repo inverso, TGA) y BCE Data Portal",pendiente,datos,Sonnet,S,~2 %,,"Sigue CLAUDE.md. Repo PÚBLICO; nunca muestres la clave de FRED (debe estar como secreto/variable de entorno; si no existe, para y avisa). Busca con Grep cómo se lee hoy FRED en scripts/ y reutilízalo. Crea scripts/leer_liquidez.py: WALCL, RRPONTSYD, WTREGEN (FRED) y el balance del Eurosistema (BCE Data Portal, ILM). Calcula liquidez neta Fed = balance − RRP − TGA, con unidad (mil M$) y fecha de cada serie. Escribe explorador/liquidez.json (nuevo) y deja liquidez-manual.json intacto; en el informe indica qué línea de la Órbita debe leer el nuevo. revisar_explorador.py (0 avisos). NO commit ni push.",15-nov,,,"expansión 14-nov; dato más viejo de la cabecera"
C286,C,"Geopolítica: intensidad de conflictos por país con GDELT DOC 2.0 (sin clave) y, si Joel crea cuenta, ACLED",pendiente,datos,Sonnet,M,~3 %,,"Sigue CLAUDE.md. Repo PÚBLICO. Crea scripts/leer_conflictos.py sin IA con la API DOC 2.0 de GDELT (timelinevol por país y tema: conflicto, sanciones, Ormuz, Taiwán, Ucrania) para los países de paises.json, ventana 30 días frente a 90 días. Guarda explorador/conflictos.json con nivel S (volumen de prensa, no hechos) y aviso de sesgo hacia medios en inglés. ACLED: solo si Joel ha creado la cuenta y la clave está como secreto; si no, déjalo en «falta». No escribir en datos.json. Informe con 5 picos y la noticia primaria que los explica (P solo si la lees). NO commit ni push.",21-nov,,"ACLED: cuenta de Joel","expansión 14-nov; archivo nuevo"
C287,C,"Frescura de todo explorador/: script que mide la fecha del dato (no la del archivo) de cada JSON y la pinta en «Qué se está quedando viejo» del planning",pendiente,mejora,Sonnet,S,~2 %,,"Sigue CLAUDE.md. Repo PÚBLICO. Mira scripts/auditoria_frescura_paises.py y scripts/indice_datos.py y crea scripts/frescura_explorador.py: para cada explorador/*.json, fecha máxima de dato (campos d, fecha, fecha_lectura, generado), fecha de archivo, periodicidad esperada (diaria, semanal, mensual, trimestral, semestral, según una tabla en el propio script) y semáforo. Salida en explorador/frescura.json. Propón en el informe el cambio mínimo en construir_seguimiento.py para leerlo; aplícalo solo si ninguna otra sesión lo está editando (git status). NO commit ni push.",15-nov,,,"expansión 14-nov"
C288,C,"Calendario oficial automático: BLS (.ics), BEA, Eurostat, INE, Fed y BCE en un solo JSON con fuente por evento, para alimentar la pestaña Calendario",pendiente,datos,Sonnet,M,~3 %,,"Sigue CLAUDE.md. Repo PÚBLICO. Espera a que C276 esté hecha (toca el Calendario). Crea scripts/leer_calendarios_oficiales.py sin IA: ics de bls.gov (schedule), calendario de BEA, release calendar de Eurostat, calendario del INE, fechas FOMC de federalreserve.gov y reuniones de política monetaria del BCE (si dan 403, Chrome y anótalo). Guarda explorador/calendario-oficial.json (fecha, hora, organismo, evento, url, nivel P) para los próximos 90 días y compara con los eventos ya cargados en docs/movil/data.json: lista faltantes y fechas distintas. No edites data.json ni vistas.html. NO commit ni push.",22-nov,,"tras C276","expansión 14-nov; archivo nuevo"
```

## 3. Programación (sin choques de archivos)

Regla: un solo escritor a la vez en `cadenas.json`, `datos.json`, `vistas.html`, `paises.json` y `construir_seguimiento.py`. Las sesiones C279-C288 escriben en archivos nuevos y pueden ir en paralelo con las de Cadenas.

**Domingo 15-nov**
- Mañana, en paralelo: C274 (único escritor de `cadenas.json`) · C285 (`liquidez.json`) · C287 (`frescura.json`; aplicar en `construir_seguimiento.py` solo si nadie más lo edita).
- Tarde: C279 (`mica-registro.json`) · C273 (`cadenas.json`, cuando acabe C274).
- Noche: R00 cierre + Gemini del día. Regenerar planning una sola vez al final (no en cada sesión en paralelo).

**Semana**
| Día | Sesiones nuevas | Ya previstas que no deben solaparse |
|---|---|---|
| 16-nov (lun) | — (13F vence hoy) · C276 | W01 |
| 17-nov | C280 (ETF; tras el 13F) | W02 |
| 18-nov | C281 (EE. UU. fiscal + COT) | W03 (APEC) · C278 (`datos.json`) |
| 19-nov | C282 (OCDE/BIS) · C283 (España energía/vivienda) | W05 · C275 (`paises.json`) no a la vez que conectar C282 |
| 20-nov | conectar C279/C285/C287 a la Órbita (único escritor de `vistas.html`) | W06, W09 (`voces.json`) |
| 21-nov | C284 (on-chain) · C286 (conflictos) | C277 (`cadenas.json`) |
| 22-nov | C288 (calendario oficial; tras C276) | C268 (`vistas.html`) en otro día |
| 23-nov | Voto de Protocol 30 «Bell» en Stellar: valorar `/research EV` | — |

## 4. Riesgos

- **Fuentes sesgadas**: webs de emisores de ETF, redes y fundaciones son parte interesada (marcar siempre); DefiLlama y RWA.xyz son agregadores con metodología cambiante (nivel S; «representado ≠ distribuido»); GDELT mide volumen de prensa, sesgado a medios en inglés, no hechos; COT de la CFTC describe posiciones, no predice precio [no usar como señal].
- **Costes de API**: todo lo propuesto se lee por script sin IA. No convertir ninguno en workflow con API de Anthropic. Claves gratuitas (FRED, BEA, ESIOS, ENTSO-E, congress.gov, ACLED) solo como secretos, nunca en el repo ni en la salida. ACLED tiene licencia no comercial: choca con la posible rentabilidad futura de la terminal [VERIFICAR licencia antes de publicar sus datos].
- **Datos viejos**: grafo de graphify del 4-nov; `liquidez-manual.json` con dato de sep-2026; deuda-FMI/reservas de 21-22 oct; calificaciones y estabilidad del 2-nov. Riesgo de mostrar dos cifras distintas para lo mismo (ya pasó con RWA): cada archivo nuevo debe convivir como «fuente única» o rotularse histórico.
- **Bloqueos**: SEC exige User-Agent identificable (reutilizar el de `leer_edgar.py`, sin datos personales nuevos); ESMA, Fed y emisores pueden dar 403 a scripts → Chrome; RWA.xyz y webs de ETF son SPA.
- **Repo público**: nada de `privado/` ni de la tesis; los JSON nuevos solo con hechos y fuente.
