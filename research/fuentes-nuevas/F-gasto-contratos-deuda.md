# F · Mapa de fuentes oficiales del gasto público de España (3-nov-2026)

> Alcance: hasta dónde llegan los datos oficiales (contratos, subvenciones, CCAA, entidades locales, deuda, intereses, infraestructuras). No es recomendación de compra ni venta. Todo lo probado se probó hoy 3-nov-2026 con curl, sin clave. Lo que no pude comprobar va marcado [VERIFICAR]. No se ha guardado ningún archivo descargado en el repo.
> No repetido: IGAE por ministerio (`explorador/espana-presupuesto.json`, informes C65/C66/C69).

## 0. Cobertura de este mapa (honesto)
- **Probado con petición real hoy:** PLACSP (ATOM y ZIP mensual), BDNS (API REST), Banco de España (CSV de deuda CCAA), Eurostat (API gov_10a_main), notas de Hacienda y BdE (por web).
- **Solo por búsqueda web / prensa (sin lectura del original):** coste medio y vida media del Tesoro, recaudación AEAT 2026, contratos de Adif, FLA y condonación.
- **No investigado por falta de tiempo/herramienta:** Tribunal de Cuentas, AIReF, IGAE-Intervención, informes de AEC/ACEX, CIAF, SEITT, AENA, Puertos, Eurostat intereses por instrumento. Quedan como pendientes en la sección 8.
- Limitación técnica: no pude extraer texto de PDF (sin lector instalado), así que el PDF de la AEAT y el del Tesoro no se leyeron.

## 1. Plataforma de Contratación del Sector Público (PLACSP)

### 1.1 Qué es público y cómo bajarlo
| Recurso | URL probada hoy | Resultado | Notas |
|---|---|---|---|
| Página de datos abiertos | https://contrataciondelestado.es/wps/portal/DatosAbiertos | 200, HTML | Enlaza a la herramienta OpenPLACSP 2.2 (zip win/linux) y a su PDF de especificación `https://contrataciondelestado.es/datosabiertos/DGPE_PLACSP_OpenPLACSP_v.2.2.pdf` |
| Feed ATOM de licitaciones (excluye menores) | https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom | 200, `application/atom+xml`, ~815 kB, sin clave | `Last-Modified: 2-nov-2026 19:08 GMT`; campo `updated` 2-nov-2026 20:08 (hora local). Cada página enlaza con `rel="next"` hacia el fichero anterior (encadenado, p. ej. `..._20261102_200848.atom`) |
| ZIP mensual de licitaciones (año en curso) | https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_202610.zip | 200; servidor ignoró el rango y envió el fichero entero: **~194 MB** (oct-2026); sep-2026 **~279 MB** | Descarga completa a /dev/null, no guardada. Ficha oficial (Hacienda): ZIP anual hasta el año anterior (desde 2012) y mensual del año en curso; leer empezando por `licitacionesPerfilesContratanteCompleto3.atom` |
| ZIP mensual de contratos menores | https://contrataciondelestado.es/sindicacion/sindicacion_1143/contratosMenoresPerfilesContratantes_202610.zip | 200, `application/zip`, **~25 MB** (oct-2026) | Los nombres `.atom` de la carpeta 1143 y 1044 que probé devolvieron una página HTML de error (200 "Error"); usar los ZIP. [VERIFICAR] nombre del feed ATOM de menores |
| Dominio alternativo `contrataciondelsectorpublico.gob.es` | misma ruta `/sindicacion/...` | Conexión rechazada/reiniciada hoy (HEAD y GET) | Usar `contrataciondelestado.es` |
| Ficha en Hacienda | https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/LicitacionesContratante.aspx | 200 | Dice: actualización diaria (con lo ocurrido el día anterior), una licitación aparece tantas veces como modificaciones tenga, y "máximo 500 entradas" por fichero. En mi lectura de la página actual del ATOM conté **25 entradas** → [VERIFICAR] el tamaño real de página |
| Ficha en datos.gob.es | https://datos.gob.es/catalogo/e05250001-licitaciones-publicadas-en-los-perfiles-del-contratante-ubicados-en-la-plataforma-de-contratacion-del-sector-publico-excluyendo-los-contratos-menores | (por búsqueda) | La ficha recogió una incidencia de enlaces rotos de ZIP en julio-2026 (última actualización citada 28-jul-2026) con mensajes contradictorios sobre si está resuelta [VERIFICAR]. Hoy los ZIP de sep y oct respondieron 200 |

**Último mes disponible (HECHO):** ZIP de octubre-2026 existe (3-nov) y el ATOM se actualizó el 2-nov-2026. Latencia ≈ 1 día.

### 1.2 Campos (etiquetas CODICE/UBL vistas en la página ATOM de hoy)
- Identificación: `ContractFolderID` (expediente), `UUID`, `ContractFolderStatusCode` (estado), `ProcedureCode`, `UrgencyCode` (permite ver urgencia), `ContractingSystemCode`.
- Órgano: `LocatedContractingParty` (+`ParentLocatedParty`: jerarquía), `ContractingPartyTypeCode`, `ActivityCode`, `BuyerProfileURIID`.
- Objeto: `ProcurementProject` (`BudgetAmount`, `TaxExclusiveAmount`, `EstimatedOverallContractAmount`), `ItemClassificationCode` (**CPV**), `RealizedLocation` (NUTS), `PlannedPeriod`/`DurationMeasure`, `ContractExtension` (**prórrogas**/opciones), `FundingProgram`/`FundingProgramCode` (fondos europeos, p. ej. MRR) , `ProcurementProjectLot` + `ProcurementProjectLotID` (**lotes**).
- Resultado: `TenderResult` (`ResultCode`, `AwardDate`, `ReceivedTenderQuantity`, `SMEAwardedIndicator`, `LowerTenderAmount`/`HigherTenderAmount`), `WinningParty` con `PartyIdentification` (**NIF**) y `PartyName` (**adjudicatario**), `LegalMonetaryTotal` (`TaxExclusiveAmount`, `PayableAmount` = importe de adjudicación), `AwardedTenderedProject`.
- Criterios y recursos: `AwardingCriteria`, `ReceivedAppealQuantity`.
- **Modificaciones de contrato (importe modificado, plazo):** no vi una etiqueta específica en la página muestreada; la ficha dice que las modificaciones aparecen como nuevas versiones del mismo expediente. [VERIFICAR] si el XML trae la modificación contractual formal o solo cambios de estado.
- Nivel máximo: **contrato/lote y empresa (NIF)**. No hay facturas ni pagos. Cada expediente puede repetirse en varias versiones: hay que quedarse con la última por `ContractFolderID`+`UUID`.

### 1.3 Qué es opaco o incompleto (HECHO general, [VERIFICAR] cifras)
- **Contratos menores:** existe el ZIP (25 MB/mes) pero la ficha de Hacienda del conjunto principal los excluye; la cobertura de menores depende de que el órgano use la plataforma [VERIFICAR].
- **Perfiles fuera de PLACSP:** la ficha oficial indica que el conjunto de entidades con perfil en la plataforma ha crecido de forma progresiva y el periodo cubierto "no es homogéneo". Hay plataformas autonómicas/locales agregadas (nombre `PlataformasAgregadas...`) pero mi prueba de ese ATOM devolvió error [VERIFICAR].
- **Emergencia y encargos a medios propios (Tragsa, Tragsatec, etc.):** estos encargos no son licitación competitiva; su visibilidad en el feed es parcial o inexistente [VERIFICAR con una muestra de un expediente concreto antes de afirmar cobertura]. Para encargos a medios propios existe además publicidad en la propia plataforma (perfil) [VERIFICAR].
- Importes: los de adjudicación son valores del contrato, no ejecución ni pago.

## 2. BDNS (Base de Datos Nacional de Subvenciones)
Portal: https://www.infosubvenciones.es/bdnstrans/ · API REST sin clave (probada). Todas las llamadas con `vpd=GE`. Respuestas JSON paginadas (`pageSize`, `page`). Aviso legal en la respuesta sobre reutilización de datos.

| Endpoint (prefijo `https://www.infosubvenciones.es/bdnstrans/api/`) | Probado hoy | Qué devuelve |
|---|---|---|
| `convocatorias/ultimas?vpd=GE` | 200, ~23 kB | Últimas convocatorias (última recibida 2-nov-2026, Ayuntamiento de Benicarló) |
| `convocatorias/busqueda?vpd=GE&pageSize=1` | 200 | `totalElements` = **662.001** convocatorias; campos: id, numeroConvocatoria, descripcion, fechaRecepcion, nivel1/2/3 (LOCAL/AUTONÓMICA/ESTATAL, territorio, órgano), mrr (marca del Mecanismo de Recuperación) |
| `concesiones/busqueda?vpd=GE&pageSize=2&page=0&order=fechaConcesion&direccion=desc` | 200 | `totalElements` = **31.320.692** concesiones; campos: codConcesion, fechaConcesion, beneficiario, instrumento, importe, ayudaEquivalente, urlBR (bases reguladoras), numeroConvocatoria, convocatoria, nivel1/2/3, idPersona, fechaAlta. Última concesión vista: 2-nov-2026 |
| `concesiones/busqueda?...&fechaDesde=01/01/2026&fechaHasta=31/10/2026` | 200, total 8.139.659 | Filtro por fechas aparentemente aceptado (el total cambió); [VERIFICAR] nombres exactos de parámetros en la ayuda de la API |
| `sanciones/busqueda`, `minimis/busqueda`, `partidospoliticos/busqueda`, `grandesbeneficiarios/busqueda` | 200 JSON cada uno | Sanciones, ayudas de minimis, subvenciones a partidos (p. ej. grupos municipales), grandes beneficiarios (idPersona, beneficiario, ejercicio, ayudaETotal) |

Nivel de detalle: **concesión individual, beneficiario y órgano concedente, municipio/CCAA por `nivel2`**. Para personas físicas el nombre sale parcialmente enmascarado (`***8541** NOMBRE`); para personas jurídicas aparece el NIF. No incluye pago efectivo. [VERIFICAR] retraso de publicación por entidad y si las subvenciones nominativas/directas están completas.
Sesgo: tiene un enorme volumen de importes pequeños (ej. 1.300-2.300 € a personas físicas); agregar por `nivel1` e importe antes de sacar conclusiones.

## 3. Hacienda: CCAA, entidades locales, deuda territorial

### 3.1 CCAA
- Ejecución presupuestaria mensual de CCAA: https://www.hacienda.gob.es/es-ES/Areas%20Tematicas/Financiacion%20Autonomica/Paginas/DatosPresupuestarios.aspx (200 hoy). La página dice que se publica en los dos meses siguientes al mes de referencia, con cada fase de ejecución (créditos, obligaciones, pagos, derechos), por CCAA, resumen ejecutivo y serie desde 2011. Formato XLS y PDF (según ficha de datos.gob.es); no hay API. No extraje enlaces de ficheros concretos [VERIFICAR].
- Liquidaciones de presupuestos de CCAA: avance (1.er trimestre del año siguiente) y datos definitivos (2.º trimestre) en la misma página.
- Contabilidad nacional (déficit): nota de prensa 30-sep-2026 https://www.hacienda.gob.es/es-ES/Prensa/Noticias/paginas/2026/20260930-np-ejecucion-presupuestaria-estado-agosto-y-consolidado-julio.aspx (200). **HECHOS (Hacienda, 30-sep-2026):** CCAA reducen un 74,3 % su déficit en ene-jul, hasta 429 M€ (0,02 % del PIB); Fondos de la Seguridad Social elevan su superávit un 40,3 %, hasta 12.113 M€ (0,68 %); AAPP ex. Administración Local: 1,84 % del PIB (1,91 % un año antes); AAPP en el 1.er semestre: 2,14 % del PIB; Corporaciones Locales: déficit 0,26 % del PIB al cierre del 2.º trimestre; Estado a fin de agosto: 2,35 % del PIB (41.978 M€ de necesidad de financiación según la búsqueda web; confirmar en la nota).
- Último mes disponible: CCAA julio-2026 (publicado 30-sep); Estado agosto-2026. La nota de septiembre se espera a finales de octubre/noviembre; no la encontré [VERIFICAR].

### 3.2 Deuda de CCAA (Banco de España) - HECHO, API/CSV sin clave
- CSV: https://www.bde.es/webbe/es/estadisticas/compartido/datos/csv/be1309.csv (200; "PDE (SEC 2010). CCAA. Deuda PDE. Total", **miles de euros, trimestral**, desde dic-1994, con las 17 CCAA). Codificación Latin-1.
- Otros CSV relacionados que respondieron 200: `be1310.csv` y `be1312.csv` (mismas series con sufijos `P0000P`; probablemente % del PIB o por instrumento) [VERIFICAR], `be1307.csv`, `be1306.csv`, `be0807.csv` (contenido no inspeccionado).
- Serie total CCAA (mM€): mar-25 338,2 · jun-25 342,8 · sep-25 338,8 · dic-25 341,6 · mar-26 346,9 · **jun-26 355,2**.
- Jun-26 por CCAA (mM€, BdE): Cataluña 92,8; C. Valenciana 64,6; Madrid 42,3; Andalucía 42,1; Castilla-La Mancha 17,0; Castilla y León 14,8; Murcia 14,3; Galicia 13,4; País Vasco 11,7; Aragón 9,4; Baleares 8,7; Canarias 6,9; Extremadura 5,6; Asturias 4,1; Cantabria 3,3; Navarra 2,4; La Rioja 2,0.
- Nota BdE 2.º trimestre 2026 (https://www.bde.es/wbe/es/noticias-eventos/actualidad-banco-espana/deuda-aapp-2026t2.html): AAPP 101,4 % del PIB (1,8 pp menos que hace un año, según el titular); CCAA 20,4 % del PIB (resumen web, [VERIFICAR] en la nota).
- Nivel: **por CCAA, trimestral**. No baja a municipio.

### 3.3 Entidades locales
- Presupuestos y liquidaciones EELL (Oficina Virtual de Coordinación Financiera con las EELL): https://www.hacienda.gob.es/en-GB/Areas%20Tematicas/Administracion%20Electronica/OVEELL/Paginas/ConsultaPresupuestosYLiquidaciones.aspx (URL de la búsqueda; mi comprobación directa no concluyó [VERIFICAR]). La web de Hacienda anuncia datos definitivos de liquidación de 2024 y avances a lo largo de 2025 (vía derecholocal.es). Conjuntos en datos.gob.es: "Presupuestos y liquidaciones de las Entidades Locales. Datos individuales" y "Datos agregados": https://datos.gob.es/en/catalogo/e05250001-presupuestos-y-liquidaciones-de-las-entidades-locales-datos-individuales (las fechas visibles son antiguas, 2002-2012 [VERIFICAR] si están actualizados).
- Nivel esperado: **por entidad (municipio, diputación, cabildo...) y capítulos de ingresos/gastos, con deuda viva**; formato de consulta web con exportación [VERIFICAR]. Retraso: liquidación definitiva ≈ año y medio.
- Deuda viva de EELL a nivel agregado: BdE (`be1309` no; serie de AAPP territoriales en `be13xx`) [VERIFICAR código]. Por municipio: en el portal de la OVEELL [VERIFICAR].

### 3.4 Fondos de liquidez (FLA / Fondo de Financiación)
- Hacienda (nota CDGAE 2-dic-2025, https://www.hacienda.gob.es/es-ES/Prensa/Noticias/Paginas/2025/20251202-CDGAE.aspx), según el resumen de búsqueda: Fondo de Financiación a CCAA con 26.575 M€ asignados en 2025 y 3.465,2 M€ para el 1.er trimestre de 2026 [VERIFICAR en el original].
- Peso del FLA en la deuda autonómica: ~59 % según BBVA Research (publicación 2023-2024, dato antiguo). Condonación de FLA (anteproyecto de 83.252 M€ para régimen común, 17.104 M€ Cataluña, según Diario de Tarragona): **medio de prensa, [VERIFICAR] estado legal**.
- Nivel: por CCAA y compartimento; no por municipio (el fondo local es distinto) [VERIFICAR].

## 4. Intereses de la deuda

### 4.1 Eurostat (HECHO, API sin clave, actualizado 21-oct-2026)
Endpoint: `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_main?format=JSON&lang=EN&geo=ES&sector=S13&freq=A&sinceTimePeriod=2019&unit=MIO_EUR&na_item=D41PAY`
| Año | Intereses D41 pagados, AAPP (M€) | % PIB |
|---|---|---|
| 2019 | 28.231 | 2,3 |
| 2020 | 25.127 | 2,2 |
| 2021 | 26.170 | 2,1 |
| 2022 | 31.775 | 2,3 |
| 2023 | 35.551 | 2,4 |
| 2024 | 38.903 | 2,4 |
| 2025 | 40.432 | 2,4 |
Sustituyendo `unit=PC_GDP` se obtiene el % del PIB. Son AAPP consolidadas (S13), no solo el Estado.

### 4.2 Tesoro (prensa/búsqueda; el original no se leyó)
- Vida media de la deuda del Estado: 7,93 años en 2025 (Ministerio de Economía, vía prensa); otra cifra de 2026: 7,83 años con coste medio de cartera 2,318 % (sin fecha clara) [VERIFICAR].
- Coste de la deuda en circulación: 2,21 % (2024) → 2,31 % (2025), "datos del Tesoro citados en prensa" [VERIFICAR].
- Necesidades 2026: emisión neta prevista de 55.000 M€, de ellos 50.000 M€ a medio y largo plazo (prensa) [VERIFICAR].
- Estadísticas del Tesoro: PDF "Estadísticas de la deuda del Estado" con datos a 31-ago-2026 (según la búsqueda); la URL de la búsqueda `https://www.tesoro.es/sites/default/files/estadisticas/Estadisticas_ES.pdf` me devolvió **404** al pedirla con curl; página de estadísticas mensuales en XLSX/PDF: https://www.tesoro.es/en/deuda-publica/estad%C3%ADsticas-mensuales (no verificada) [VERIFICAR].
- Contexto presupuestario: los PGE de 2023 siguen prorrogados (la autorización de endeudamiento se extiende a 2026) según los resultados de búsqueda. La partida de intereses de los PGE y su ejecución 2026: **no localizada**; ver sección 8.

### 4.3 Tenedores
- Composición por tenedor (BdE) y deuda por instrumento: no comprobado hoy. Candidatos: tablas de la sección "Deuda de las AAPP" en bde.es (CSV `be13xx`) [VERIFICAR].

## 5. Infraestructuras: inversión vs mantenimiento

### 5.1 Dato macro (Eurostat, HECHO, mismo endpoint con `na_item` distinto)
Millones de euros, AAPP España (S13):
| Año | P51G inversión bruta | P51C consumo de capital fijo | Inversión neta (P51G − P51C, cálculo mío) | P5 formación bruta de capital |
|---|---|---|---|---|
| 2019 | 27.206 | 28.850 | −1.644 | 27.296 |
| 2020 | 29.694 | 29.191 | +503 | 30.247 |
| 2021 | 33.591 | 30.919 | +2.672 | 33.343 |
| 2022 | 37.350 | 34.076 | +3.274 | 38.140 |
| 2023 | 44.696 | 35.529 | +9.167 | 44.115 |
| 2024 | 43.253 | 37.729 | +5.524 | 43.107 |
| 2025 | 50.628 | 39.764 | +10.864 | 50.608 |
Lectura (hecho + cautela): la inversión bruta supera la depreciación contable desde 2020 y el diferencial es mayor en 2023 y 2025, años con fondos europeos (MRR) [VERIFICAR el efecto del MRR con la marca `mrr`/`FundingProgram`]. **El consumo de capital fijo no es "gasto de mantenimiento"**: es depreciación estimada del stock; el mantenimiento real está en consumos intermedios (reparaciones) y obras de conservación, que Eurostat no separa aquí. Para decir "se invierte menos de lo que se desgasta" haría falta stock y mantenimiento por activo, y de momento el dato macro **no** lo respalda en agregado.

### 5.2 Adif, Transportes, SEITT, AENA, Puertos (parcial, prensa/notas)
- Adif: adjudicación de mantenimiento de infraestructura y vía (líneas convencionales y ancho métrico) y de líneas de alta tensión por **más de 448 M€** (nota de prensa de Adif sin fecha confirmada: https://www.adif.es/en/-/adif-destina-otros-450-millones-de-euros-al-mantenimiento-de-diversos-elementos-de-la-red-ferroviaria); mantenimiento de alta tensión zona Norte de Adif y Adif AV, **12,3 M€ a 3 años** (https://www.adif.es/w/adif-adjudica-12-3-m%E2%82%AC-mantenimiento-lineas-alta-tension-adif-adif-av-zona-norte); proyectos de refuerzo y mejora de estructuras **13 M€** (8-may-2026, Infobae/agencias); mantenimiento de locomotoras logísticas **>30 M€**, autorizado para licitar por el Consejo de Ministros el 27-oct-2026 (https://www.transportes.gob.es/ministerio/comunicacion/sala-prensa/mar-27102026-1336), todavía no adjudicado. Un aviso TED de ene-2026 recoge mantenimiento de señalización por 11.055.506,23 EUR (https://ted.europa.eu/es/notice/84645-2026/pdf o relacionados).
- **No localizadas:** cuentas anuales 2025 de Adif/Adif AV, presupuesto de mantenimiento total ni adjudicatarios principales agregados. Camino: PLACSP (filtrar órgano Adif + CPV 50xxx/45xxx) y cuentas depositadas en el Registro Mercantil/Adif transparencia [VERIFICAR].
- Carreteras (Transportes), SEITT, AENA, Puertos del Estado: no investigados.
- Informes de asociaciones (AEC: déficit de conservación; ACEX/CEOE): **no consultados**. Aviso de sesgo previsto: son asociaciones sectoriales con interés en más licitación, tratarlas como [S: emisor interesado].
- CIAF: no consultado (solo hechos de informes publicados).

### 5.3 Recaudación frente a inversión (AEAT)
- Informes mensuales (PDF, URL patrón sin clave): https://sede.agenciatributaria.gob.es/static_files/AEAT/Estudios/Estadisticas/Informes_Estadisticos/Informes_mensuales_recaudacion_tributaria/2026/IMR_26_09_es_es.pdf (también `IMR_26_08`, `IMR_26_07`: 200). Catálogo: https://sede.agenciatributaria.gob.es/Sede/datosabiertos/catalogo/hacienda/Informe_mensual_de_Recaudacion_Tributaria.shtml. No pude leer el PDF (sin extractor).
- Según un resumen del informe de septiembre-2026 hallado por búsqueda (no leído en el original): ingresos tributarios netos de septiembre **18.049 M€ (+13,5 %)**; enero-septiembre **+10 %** (ingresos brutos +7,6 %, devoluciones −1,9 %), +8 % en términos homogéneos [VERIFICAR contra el PDF]. No obtuve la cifra absoluta acumulada ni confirmé que sea "récord"; no usarlo como tal sin verificar.

## 6. Tribunal de Cuentas, IGAE, AIReF, Banco de España
**No investigado en esta pasada** (sin lecturas hechas). Pendiente: Tribunal de Cuentas (informes de fiscalización 2025-2026 sobre contratación, subvenciones y sector público), AIReF (informes de ejecución trimestral y opinión sobre senda de gasto), IGAE (cuentas y auditorías de subvenciones), BdE (Informe Anual 2025, Boletín Económico). Hecho comprobado solo: el BdE publica notas trimestrales de deuda AAPP (sección 3.2).

## 7. Qué sí es público / qué es opaco
| Tema | Sí es público | Opaco o dudoso |
|---|---|---|
| Contratos | Licitaciones y adjudicaciones con órgano, NIF, CPV, lotes e importe en PLACSP (ATOM diario, ZIP mensual) | Ejecución real, facturas, pagos; menores fuera de plataforma; emergencia y encargos a medios propios [VERIFICAR] |
| Subvenciones | Convocatorias y concesiones individuales en BDNS, con beneficiario (NIF si empresa), órgano e importe | Pago efectivo; personas físicas enmascaradas; retrasos por entidad [VERIFICAR] |
| CCAA | Ejecución mensual por CCAA; deuda PDE trimestral (BdE) | Detalle por proveedor o contrato (sólo vía PLACSP y portales autonómicos) |
| EELL | Presupuestos y liquidaciones por entidad (OVEELL) | Retraso ~1,5 años; formato no API [VERIFICAR] |
| Deuda | Total y por CCAA trimestral; Eurostat anual; Tesoro por instrumento | Partida de intereses en PGE y ejecución 2026 (no localizada); FLA por CCAA [VERIFICAR] |
| Infraestructuras | Inversión y depreciación agregada (Eurostat) | Gasto real de mantenimiento por activo; cuentas Adif 2025 no localizadas |

## 8. Series automatizables sin clave (priorizadas)
1. **Eurostat intereses, inversión y depreciación (probado):** `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_main?format=JSON&geo=ES&sector=S13&freq=A&na_item=D41PAY|P51G|P51C|P5&unit=MIO_EUR|PC_GDP` (una llamada por `na_item`). Anual, actualizado 21-oct-2026.
2. **Deuda PDE por CCAA, BdE (probado):** `https://www.bde.es/webbe/es/estadisticas/compartido/datos/csv/be1309.csv`. Trimestral, último jun-2026.
3. **BDNS concesiones recientes (probado):** `https://www.infosubvenciones.es/bdnstrans/api/concesiones/busqueda?vpd=GE&pageSize=100&page=0&order=fechaConcesion&direccion=desc` (+ filtros de fecha [VERIFICAR] nombres).
4. **BDNS convocatorias últimas (probado):** `https://www.infosubvenciones.es/bdnstrans/api/convocatorias/ultimas?vpd=GE`.
5. **BDNS grandes beneficiarios (probado):** `https://www.infosubvenciones.es/bdnstrans/api/grandesbeneficiarios/busqueda?vpd=GE&pageSize=100`.
6. **PLACSP ATOM diario (probado):** `https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom` (seguir `rel="next"`).
7. **PLACSP ZIP mensual (probado, 194-279 MB):** `.../licitacionesPerfilesContratanteCompleto3_AAAAMM.zip` — procesar en streaming, no guardar en el repo.
8. **PLACSP contratos menores ZIP (probado, ~25 MB):** `https://contrataciondelestado.es/sindicacion/sindicacion_1143/contratosMenoresPerfilesContratantes_AAAAMM.zip`.
9. **BdE series hermanas (existen, contenido no analizado):** `be1310.csv`, `be1312.csv` (posiblemente % PIB / deuda por instrumento) [VERIFICAR].
10. **AEAT informes mensuales PDF (existen, sin extractor):** patrón `.../2026/IMR_26_MM_es_es.pdf`; requiere extracción de texto de PDF (no es API).

## 9. Siguiente paso sugerido (pendiente)
- Leer la nota BdE 2.º trimestre 2026 y el PDF del Tesoro con un extractor de PDF para fijar coste medio, vida media y tenedores.
- Muestrear un mes de PLACSP (ZIP de menores, 25 MB) para contar entradas y ver cobertura.
- Ejecutar la sección 6 (TCu, AIReF, IGAE) y 5.2 (AEC, CIAF, Puertos, AENA).
- Registrar la cobertura en `research/COLA.md`; ¿Actualizo el Seguimiento y el planning?

## 10. Completado (3-nov-2026)
> Corrige y amplia las secciones 4.2 y 5.2 y rellena la 6. [ORIGINAL] = leido en la fuente primaria hoy; [PRENSA] = resumen de busqueda web/prensa. No pude extraer texto de los PDF de AIReF, Tribunal de Cuentas y AEAT (compresion), asi que de ellos solo hay metadatos y resumenes.

### 10.1 Tesoro: fuente original [ORIGINAL] (boletin estadistico, XLSX sin clave)
Indice: https://www.tesoro.es/en/deuda-publica/estad%C3%ADsticas-mensuales (ultimo boletin listado: **septiembre 2026**). XLSX (leidos desde la carpeta temporal, no guardados en el repo): `https://www.tesoro.es/documents/d/tesoro/01i-xlsx` (deuda viva nominal), `02i-xlsx` (vida media), `03i-xlsx` (tipo medio de la deuda viva), `04i` a `07i` (por tenedor), `09i` a `14i` (financiacion 2026, subastas, perfil de vencimientos 2026-2071). Mismo patron con `-pdf`.
| Dato (fin de periodo) | Dic-2025 | Jun-2026 | Sep-2026 |
|---|---|---|---|
| Deuda bruta del Tesoro, valor nominal (M€) | 1.516.859 | 1.570.105 | **1.585.361** |
| Tipo de interes medio de la deuda viva (%) | 2,316 | 2,431 | **2,453** |
| Vida media (años) | 7,87 | 7,91 | **7,85** |
- Detalle sep-2026 (03i): Letras 2,381 %; bonos 2-7 años 2,476 %; bonos 10-50 años 2,478 %; deuda asumida 2,725 %. Cierre 2024 (01i): 1.440.970 M€. El tipo medio sube mes a mes en 2026 (ene 2,372 % → sep 2,453 %). Serie historica: 2019 2,202 %; 2021 1,642 %.
- Correccion a la seccion 4.2: la prensa citaba «vida media 7,93 años en 2025»; en el boletin 7,93 es **enero de 2025**; a dic-2025 es 7,87. El 2,31 % de la prensa coincide con 2,316 % de dic-2025.
- Tenedores (07i, deuda en cartera, nominal; fila de julio, el fichero no mostro la cabecera del año, probablemente 2026 [VERIFICAR]): entidades de credito residentes 223.140 M€ (14,9 %); Banco de España 304.075 M€ (20,4 %); aseguradoras 95.479 M€ (6,4 %); fondos de pensiones 8.996 M€ (0,6 %); otra columna 30.409 M€ (2,0 %, etiqueta no leida). Fuente: Banco de España (Securities Holdings Statistics), ruptura de serie en 2016. No suma el 100 % (faltan no residentes, etc.) [VERIFICAR columnas].
- Intereses pagados: Eurostat D41 AAPP 2025 = 40.432 M€ (2,4 % del PIB) (seccion 4.1, API actualizada 21-oct-2026).
- **Intereses en PGE y ejecucion 2026: no localizados en la fuente original.** Contexto [PRENSA]: PGE 2023 prorrogados tambien en 2026 (tercera prorroga); segun IGAE citada por Cronica Economica, las modificaciones de credito de deuda publica suman 30.200 M€ a agosto-2026 (sobre todo amortizacion) dentro de 81.300 M€ de modificaciones totales (https://cronicaeconomica.com/igae-demasiadas-modificaciones-de-credito) [VERIFICAR contra IGAE]. Ruta oficial: ejecucion mensual del Estado (IGAE, capitulo 3 «gastos financieros»).

### 10.2 Tribunal de Cuentas [PRENSA/BOE; PDF no leidos en detalle]
- **N.º 1.670, contratacion menor del Area de Gasto 2 (proteccion y promocion social) de los PGE 2024**, aprobado por el Pleno el **26-feb-2026** (https://www.eldebate.com/uploads/files/2026/03/03/I1670.pdf). La introduccion advierte del riesgo de fraccionamiento. El Debate (20-mar-2026) titula que el Tribunal señala a Igualdad por asignar cientos de contratos «a dedo» (https://www.eldebate.com/sociedad/20260320/tribunal-cuentas-senala-igualdad-asignar-cientos-contratos-dedo-justificar_397818.html) [PRENSA de linea editorial propia; VERIFICAR en el PDF].
- **N.º 1.635, contratacion de universidades**: BOE 13-jul-2026 (https://www.boe.es/boe/dias/2026/07/13/pdfs/BOE-A-2026-15275.pdf).
- BOE 21-abr-2026 (Comision Mixta, 24-feb-2026): informes sobre contratos de la AGE (n.º 1.611, subcontratacion en obras; otro de Justicia, Defensa y Exteriores) y TGSS 2022 (n.º 1.587): https://www.boe.es/boe/dias/2026/04/21/pdfs/BOE-A-2026-8760.pdf, `-8763.pdf`, `-8767.pdf` [VERIFICAR contenido].
- **Emergencia**: serie COVID (n.º 1.473, 1.488, 1.542) de 2021-2022; no hallé informe de emergencia de 2026. **Medios propios**: no hallé informe 2025-2026. **Subvenciones**: un informe aprobado el 23-oct-2025 (copia en la Diputacion de Badajoz, alcance sin confirmar) y ninguno de 2026 [VERIFICAR en https://www.tcu.es].
- Retraso tipico de 1-3 años sobre el ejercicio fiscalizado (1.670 audita 2024; 1.587, 2022).

### 10.3 AIReF [metadatos + resumen de busqueda]
- **Informe sobre ejecucion presupuestaria, deuda publica y regla de gasto 2026** (127 paginas; PDF generado 20-jul-2026, informe fechado 15-jul-2026 segun busqueda): https://www.airef.es/wp-content/uploads/2026/07/Informes-ejecuci%C3%B3n-2026/Informe-Ejecucion-Presupuestaria-2026.pdf. Complementos: prevision de cierre `.../Informe-Prevision-Cierre_2026_RIO_45_26.pdf` e informes por CCAA (https://www.airef.es/es/centro-documental/informes/informes-individuales-sobre-la-ejecucion-presupuestaria-la-deuda-publica-y-la-regla-de-gasto-2026-de-las-comunidades-autonomas-ccaa/).
- Conclusiones [PRENSA, VERIFICAR en el PDF]: la AIReF sigue apreciando **riesgo de incumplimiento de la regla de gasto** en 2026 y mantiene su prevision global de gasto a cierre. Informe de presupuestos iniciales (15-abr-2026): gasto computable +7,3 % en 2026 (https://www.airef.es/wp-content/uploads/2026/04/Presupuestos-iniciales-2026/260415.-Informe_pptos_iniciales_2026_VD-1.pdf) [VERIFICAR]. Menciona que la inflacion eleva los intereses de la deuda indexada; sin cifra comprobada.
- No localicé informe de AIReF de octubre-2026.

### 10.4 IGAE
- [PRENSA, VERIFICAR] The Objective (25-oct-2026, https://theobjective.com/economia/2026-10-25/gobierno-euros-inversion-publica/), con datos de IGAE: la AGE cerro agosto-2026 con 14.446 M€ de inversion publica sin ejecutar (titular: «73 %»). Cuidado: ejecucion parcial a agosto no es ejecucion anual (estacionalidad); el medio lo atribuye en parte a la prorroga.
- A automatizar: ejecucion mensual del Estado y contabilidad nacional del IGAE [VERIFICAR URL de descarga].

### 10.5 Adif y Transportes: inversion vs mantenimiento
- [PRENSA 9-feb-2026, VERIFICAR en el convenio oficial] Acuerdo Transportes-sindicatos tras la huelga de maquinistas: **861 M€ de mantenimiento de Adif en 2026, hasta 1.179 M€ en 2030**, y 5.266 M€ (Adif) + 2.887 M€ (Adif AV) de inversion de mantenimiento 2026-2030; evaluar reinternalizar contratos al vencer (https://www.noticiasdenavarra.com/economia/2026/02/09/claves-acuerdo-transportes-maquinistas-desconvocar-renfe-10680262.html; https://www.railjournal.com/financial/spain-increases-infrastructure-maintenance-spend/).
- Contratos recientes (seccion 5.2): >448 M€ mantenimiento via/alta tension (nota Adif sin fecha), 12,3 M€ AT zona Norte, >30 M€ locomotoras (autorizacion de licitacion 27-oct-2026).
- Carreteras: conservacion «cerca de 2.000 M€ anuales» segun la AEC citando al Ministerio [PRENSA]; limites de compromiso de actuaciones de carreteras 381/489/461 M€ (2024/25/26) en una nota de Consejo de Ministros (https://www.hacienda.gob.es/GabineteMinistro/Notas%20Prensa/2025/CONSEJO-MINISTROS/25-03-25-NP-CM-Actuaciones-carreteras.pdf) [VERIFICAR]. Anuncio de 600 M€ del ministro Puente: solo prensa [VERIFICAR].
- Lectura contrastada: **a favor** de que se invierte, Eurostat (5.1) muestra inversion bruta por encima de la depreciacion desde 2020 y el acuerdo de Adif fija mantenimiento creciente; **en contra**, el sector estima déficit de conservacion (10.6) y la ejecucion a agosto es baja (10.4). Ninguna fuente aqui prueba causa-efecto.

### 10.6 Asociacion Española de la Carretera (AEC): sesgo marcado
- Informe AEC (ene-2026), segun prensa: deficit acumulado de conservacion **13.500 M€**; 52 % de la red (≈54.000 km de 101.700 km) necesita actuacion en ≤4 años; «34.000 km» de reconstruccion urgente (Infobae 21-feb-2026, https://www.infobae.com/espana/2026/02/21/las-carreteras-espanolas-estan-en-el-peor-momento-de-su-historia-reciente-por-la-falta-de-inversion-34000-kilometros-necesitan-reconstruccion-urgente/; elEconomista ene-2026, https://www.eleconomista.es/infraestructuras-servicios/noticias/13741917/01/26/el-deficit-en-la-conservacion-de-las-carreteras-se-duplica-en-una-decada-y-alcanza-los-13500-millones.html).
- Cifras discordantes en prensa: 13.500, 8.300 (entrevista) y 13.000 M€ (oct-2026) [VERIFICAR cual es la vigente y si cubre red estatal o total].
- **Sesgo del emisor**: la AEC agrupa a empresas y entidades del sector de la carretera con interes en mas licitacion; es una estimacion de necesidad, no un gasto medido. Contraste posible: licitaciones de conservacion en PLACSP (CPV 45233141, 50230000 y afines [VERIFICAR codigos]).

### 10.7 CIAF: solo hechos publicados
- **Adamuz (Córdoba), enero 2026**: avance CIAF del 23-ene-2026 con la rotura de via como hipotesis; informe a la jueza del 28-abr-2026 situa la rotura de carril en el p.k. 318,681 (https://www.elindependiente.com/espana/2026/04/28/guardia-civil-rotura-via-causa-accidente-adamuz/). Datos «provisionales hasta el informe final»; **no localicé informe final**. 46 fallecidos segun esa fuente (balance provisional de 39 en enero segun el Defensor del Pueblo Andaluz) [VERIFICAR cifra oficial].
- El avance listaba «otras causas» (sabotaje, falta de mantenimiento, materiales) sin concluir: **no se puede afirmar que el mantenimiento fuera la causa** [HECHO: sin conclusion publica].
- Una ficha de Wikipedia indica que la CIAF dejo de investigar el 15-jul-2026 por cambio de organismo [VERIFICAR en BOE/Transportes].

### 10.8 Recaudacion frente a inversion (actualiza 5.3)
- AEAT, septiembre-2026 (PDF no leido; resumen [PRENSA]): neto de septiembre 18.049 M€ (+13,5 %); enero-septiembre +10 % (brutos +7,6 %, devoluciones −1,9 %); homogeneo +8 %. Sin cifra absoluta acumulada: [VERIFICAR] antes de llamarlo «record».
- Orden de magnitud: recaudacion +10 %; inversion bruta de AAPP 50.628 M€ en 2025 (Eurostat); intereses 40.432 M€ en 2025. El mantenimiento especifico (Adif 861 M€; carreteras ~2.000 M€ segun prensa) es una fraccion; no existe un total oficial unico de mantenimiento.

### 10.9 Pendientes
Leer con extractor de PDF los informes de AIReF, TCu 1.670 y AEAT; localizar la partida de intereses de la prorroga PGE-2023 y su ejecucion IGAE 2026; cuentas anuales 2025 de Adif/Adif AV; confirmar el tamaño de pagina del ATOM de PLACSP y la cobertura de menores/emergencia con una muestra.
