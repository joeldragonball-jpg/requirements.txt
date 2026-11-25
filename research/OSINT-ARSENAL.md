# Arsenal OSINT para verificar eventos que mueven mercado (25-nov-2026)

Uso: comprobar hechos de Ormuz/Irán, Ucrania, sanciones y cumbres antes de darlos por buenos en Cumbres y en «verificados». No es una recomendación de operar. Etiquetas: [P] dato leído por el repo hoy, [S] secundaria/sin contrastar, [VERIFICAR] pendiente.
Prueba de acceso: petición real con curl (User-Agent genérico) el 25-nov-2026. OJO: un 200 en una web con mapa o app es solo la «carcasa» (JavaScript); el dato útil exige API o navegador. Sin saltar anti-bots.

Leyenda de acceso: libre / API / Chrome (navegador real) / pago. «Script» = ¿puede leerlo el repo con curl/urllib?

## 1. Tráfico marítimo y petroleros (Ormuz)
| Fuente | Qué mide | URL | Acceso | Script (prueba 25-nov) | Fiabilidad y sesgo | Sirve para |
|---|---|---|---|---|---|---|
| IMF PortWatch | Tránsitos diarios por cuellos de botella (AIS): nº buques, petroleros, capacidad | portwatch.imf.org; API ArcGIS `services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query` | libre + API | **200, JSON** [P] | Alta (FMI/Oxford, método publicado); retraso de 2-3 días; el AIS puede apagarse en la flota en la sombra | Confirmar cierre/reapertura de Ormuz, Mar Rojo, Suez |
| MarineTraffic | Posición AIS en vivo | marinetraffic.com | libre limitado / pago API | 200 (carcasa JS, sin dato) | Media-alta; mapa gratis con retraso, detalle de pago | Mirar la zona a ojo; no cuantificar |
| VesselFinder | AIS en vivo | vesselfinder.com | libre limitado / pago | 200 (carcasa) | Media; cobertura costera irregular | Segunda opinión de AIS |
| TankerTrackers | Exportaciones de crudo iraní/ruso, almacenamiento flotante | tankertrackers.com | parte libre en redes, informes de pago | 200 (portada) | Media: empresa privada, cifras no auditables, vende suscripción [S] | Pista de exportaciones iraníes y flota en la sombra |
| Kpler / Vortexa | Flujos de crudo y GNL por buque | kpler.com, vortexa.com | pago (titulares libres vía prensa) | 200 (marketing) | Alta, pero cerrado: se cita a través de Reuters/Bloomberg [S] | Contrastar volúmenes con PortWatch |
| UKMTO | Avisos de incidentes y ataques a buques | ukmto.org | libre | no probado [VERIFICAR] | Alta (Royal Navy); solo incidentes | Fechar ataques a petroleros |

## 2. Frente de Ucrania
| Fuente | Qué mide | URL | Acceso | Script | Fiabilidad y sesgo | Sirve para |
|---|---|---|---|---|---|---|
| ISW (Institute for the Study of War) | Evaluación diaria de la ofensiva rusa, mapas | understandingwar.org | libre | **403** (Chrome o fuente secundaria) | Alta en método y fuentes abiertas; think tank favorable al apoyo a Ucrania; prudencia con «cambios de control» | Contrastar avances y declaraciones rusas |
| DeepState | Mapa de líneas de frente (voluntarios ucranianos) | deepstatemap.live; `deepstatemap.live/api/history/last` | libre + API no oficial | **200, GeoJSON** (524 elementos, versión del 24-nov 21:53 UTC) [P] | Media-alta; fuente ucraniana, sesgo previsible; API no documentada, puede cambiar | Fecha y tamaño del último cambio de línea |
| Oryx | Pérdidas de equipo confirmadas con foto | oryxspioenkop.com | libre | 200 (HTML) | Alta en lo que cuenta (solo con imagen); subestima pérdidas | Desgaste ruso/ucraniano |
| ACLED | Eventos de conflicto geolocalizados | acleddata.com | API con registro | 200 (portada); API sin clave no probada | Alta, método publicado; retraso semanal | Series de ataques por zona (también Irán/Oriente Próximo) |
| Defensa RU/UA | Partes oficiales | mil.gov.ua, mil.ru | libre | no probado [VERIFICAR] | Propaganda de parte; solo como «lo que dicen» | Anotar la versión oficial para cotejar |

## 3. Vuelos y ADS-B
| Fuente | Qué mide | URL | Acceso | Script | Fiabilidad y sesgo | Sirve para |
|---|---|---|---|---|---|---|
| OpenSky Network | Estados ADS-B en vivo e históricos | `opensky-network.org/api/states/all?lamin=..` | API libre (límite de ritmo) | **200, JSON** [P] (25-nov 11:48 UTC, aviones sobre el Golfo) | Alta; huecos de cobertura; aviones militares sin transpondedor | Espacio aéreo cerrado o desviado sobre Golfo e Irán |
| FlightRadar24 | Vuelos en vivo | flightradar24.com | libre limitado / pago | 200 (carcasa) | Media-alta; filtra algunos vuelos militares | Cancelaciones de aerolíneas en la región |
| ADS-B Exchange | Vuelos sin filtrar (incluye militares) | globe.adsbexchange.com | libre / API de pago | 200 (carcasa) | Alta en cobertura; voluntarios | Aviones cisterna, vigilancia, tráfico militar |

## 4. Imágenes de satélite
| Fuente | Qué mide | URL | Acceso | Script | Fiabilidad y sesgo | Sirve para |
|---|---|---|---|---|---|---|
| Sentinel Hub EO Browser | Sentinel-1/2 (radar y óptico, 10 m) | apps.sentinel-hub.com/eo-browser | libre con cuenta | 200 (app JS) | Alta (Copernicus); nubes y revisita de ~5 días | Humo, puertos, refinerías, depósitos |
| NASA FIRMS | Focos de calor/incendios casi en tiempo real | firms.modaps.eosdis.nasa.gov | libre; API con clave gratuita | 200 (portada) | Alta; detecta calor, no causa (puede ser quema de gas industrial) | Ataques a infraestructura energética |
| Planet (muestras) | Imagen diaria de 3 m | planet.com | pago; solo muestras/educación | 200 (marketing) | Alta; casi todo de pago | Citar imágenes ya publicadas por la prensa |

## 5. Sanciones y flota en la sombra
| Fuente | Qué mide | URL | Acceso | Script | Fiabilidad y sesgo | Sirve para |
|---|---|---|---|---|---|---|
| OFAC SDN (Tesoro EE. UU.) | Lista de sancionados, con buques y direcciones cripto | `sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.CSV` | libre | **200** tras un 302 a un enlace firmado (no copiarlo); última lista publicada el 20-nov [P] | Oficial; hecho, no valoración | Comprobar si un buque, empresa o dirección está sancionado |
| UE, ficheros de sanciones financieras | Lista consolidada UE | webgate.ec.europa.eu/fsd/fsf | libre con token | **401** | Oficial | Paquetes de sanciones de la UE |
| OpenSanctions | Listas agregadas (OFAC, UE, ONU…) | data.opensanctions.org | libre (uso no comercial) | **200, JSON** | Alta; agregador, cotejar con el original | Cruce rápido por nombre |
| Trackers de flota en la sombra | Buques, banderas falsas, transbordos | TankerTrackers, listas de think tanks | mixto | ver §1 | Media [S] | Evasión de sanciones a crudo ruso/iraní |
| GDELT | Noticias mundiales codificadas | data.gdeltproject.org | libre | 200 | Media: automático, ruido | Ver cobertura mediática, no hechos |

## 6. On-chain cripto
| Fuente | Qué mide | URL | Acceso | Script | Fiabilidad y sesgo | Sirve para |
|---|---|---|---|---|---|---|
| XRPL (explorador oficial + JSON-RPC) | Libro mayor: pagos, emisores, RLUSD | livenet.xrpl.org; `xrplcluster.com` | libre + API | explorador 200 (JS); RPC ya usado por el repo ✅ | Alta (dato primario) | Emisiones y movimientos de carteras |
| XRPSCAN | Explorador con etiquetas de carteras | xrpscan.com | libre | **403** (Chrome) | Media-alta; etiquetas de la comunidad | Identificar carteras grandes |
| Etherscan | Ethereum y tokens | etherscan.io; API | API con clave gratuita | 200, pero sin clave la API no da dato [VERIFICAR] | Alta en datos; etiquetas parciales | Movimientos de USDT y de A7A5 |
| Chainalysis / TRM Labs | Informes públicos de flujos ilícitos y sanciones | chainalysis.com/blog, trmlabs.com | libre (informes) | 200 (HTML) | Alta pero con interés comercial [S] | Evasión de sanciones vía cripto |
| A7A5 / Garantex (Grinex) | Rublo-stablecoin sancionado y su cambio | informes de TRM, Elliptic; comunicados OFAC/UE | libre | vía informes | Media [S]: cifras de empresas privadas | Eludir sanciones a Rusia con cripto |

## 7. Energía
| Fuente | Qué mide | URL | Acceso | Script | Fiabilidad y sesgo | Sirve para |
|---|---|---|---|---|---|---|
| ENTSO-E Transparency | Generación, carga y flujos eléctricos UE | transparency.entsoe.eu | API con token gratuito | 200 (portada) | Alta (operadores) | Efecto de shocks de gas en electricidad |
| GIE AGSI+ | Gas almacenado en la UE | agsi.gie.eu | API con clave gratuita | 200 (portada) | Alta | Nivel de llenado de gas en invierno |
| EIA | Brent/WTI al contado, inventarios | eia.gov (HTML); `api.eia.gov` | HTML libre; API con clave | web 200; **API 403 sin clave** | Alta; retraso ~3 días (ya automatizado) | Precio físico del crudo tras Ormuz |

## 8. Bulos y verificación
| Fuente | Qué mide | URL | Acceso | Script | Fiabilidad y sesgo | Sirve para |
|---|---|---|---|---|---|---|
| Bellingcat | Investigación abierta y guías | bellingcat.com | libre | 200 | Alta en método; foco en Rusia/Siria | Aprender a geolocalizar y comprobar |
| EUvsDisinfo | Desinformación prorrusa (UE) | euvsdisinfo.eu | libre | **403** (Chrome) | Media-alta; organismo de la UE, con encuadre institucional | Narrativas rusas sobre sanciones |
| Reuters Fact Check | Verificaciones | reuters.com/fact-check | libre | **401** (Chrome) | Alta | Cotejar imágenes virales |
| Maldita.es | Verificación en español | maldita.es | libre | 200 | Alta (IFCN) [VERIFICAR pertenencia] | Bulos que afectan a España |
| Newtral | Verificación en español | newtral.es | libre | 200 | Alta (IFCN) [VERIFICAR pertenencia] | Idem |

## 9. Documentos oficiales
| Fuente | Qué mide | URL | Acceso | Script | Fiabilidad y sesgo | Sirve para |
|---|---|---|---|---|---|---|
| Federal Register | Órdenes y normas de EE. UU. | `federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D=` | API libre | **200, JSON** [P] | Oficial | Textos de sanciones y aranceles |
| EUR-Lex | Reglamentos UE | eur-lex.europa.eu | libre | **202** (solo navegador) | Oficial | Paquetes de sanciones UE |
| BOE | Legislación española | boe.es; datos abiertos | libre + API | web 200; el endpoint de sumario probado dio **400** (ruta o cabecera) [VERIFICAR] | Oficial | Efectos en España |

## Cinco reglas de uso
1. OSINT es pista, no prueba: orienta la búsqueda; el hecho exige fuente oficial o dos independientes.
2. Triangular con al menos 2 fuentes independientes (p. ej. AIS + agencia + dato oficial); si comparten origen, cuentan como una.
3. Marcar [S] todo lo que descanse en una sola fuente OSINT o privada (TankerTrackers, trackers, cuentas anónimas) y [VERIFICAR] lo que no se pudo leer.
4. No difundir imágenes ni vídeos sin verificar (fecha, lugar, autor); no subirlas al repo público sin contraste.
5. Riesgos legales y éticos: respetar términos de uso, no saltar anti-bots ni paywalls, no identificar a personas privadas ni geolocalizar objetivos con riesgo para civiles; datos personales fuera del repo (público).

## Qué leería primero hoy (25-nov-2026, ~11:50 UTC)
1. **Ormuz, IMF PortWatch** (API): último dato 22-nov: 1 buque y 0 petroleros; 21-nov: 4 buques (1 petrolero); 20-nov: 4; 19-nov: 3; 15-nov: 2. Referencia: del 1 al 10-ene-2026 hubo 49-74 tránsitos diarios. [P] Hecho medido por AIS: el tráfico es muy inferior al de enero. [VERIFICAR] la causa (¿cierre, guerra, AIS apagado?) con UKMTO y agencias; PortWatch no explica el motivo.
2. **Frente de Ucrania, DeepState** (`/api/history/last`): versión generada el 24-nov a las 21:53 UTC, 524 elementos. [P] Confirma que el mapa se actualizó anoche; qué cambió exige comparar con la versión anterior o leer ISW por Chrome (403 a script). [S] Sesgo: fuente ucraniana.
3. **Espacio aéreo, OpenSky** (cuadro 24-30 N, 50-58 E): respuesta del 25-nov 11:48 UTC con aviones activos (varios indios) sobre el Golfo. [P] Hay tráfico civil a esa hora; sin referencia de una semana normal, no se concluye nada: [VERIFICAR].
Extra: SDN de OFAC con última publicación del 20-nov [P].
Siguiente paso: leer ISW y UKMTO por Chrome y cotejar con el titular de Cumbres que toque.
