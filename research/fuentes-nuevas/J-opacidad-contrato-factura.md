# J · ¿Qué se ve a nivel de contrato y de factura, y qué no? (3-nov-2026)

> Complementa `F-gasto-contratos-deuda.md` (no repito PLACSP/BDNS/deuda). Todo lo marcado "probado" se pidió hoy 3-nov-2026 sin clave. Sin recomendaciones de compra/venta. No se descargó ningún ZIP ni archivo al repo; los 6 ficheros ATOM (~84 MB) se leyeron en la carpeta temporal y no se guardan.
> Etiquetas: HECHO (leído en la fuente) · [VERIFICAR] · [ESPECULACIÓN].

## 1. Muestreo real del feed ATOM de PLACSP (HECHO, probado)
Fuente: https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom y sus enlaces `rel="next"` (página 1 y 5 siguientes). Muestra de conveniencia, no aleatoria: cubre aprox. 30-oct a 2-nov-2026.

| Página | Tamaño | Entradas |
|---|---|---|
| actual (`...Completo3.atom`) | 0,8 MB | 25 |
| next 1 (`..._20261102_200848.atom`) | 15,0 MB | 499 |
| next 2 (`..._200848_1.atom`) | 16,4 MB | 498 |
| next 3, 4, 5 (`_200848_2`, `_20261030_202205`, `_20261030_202205_1`) | 15,9 / 17,2 / 18,0 MB | resto hasta 2.519 en total |

- **Aclaración sobre F:** la página "actual" tiene 25 entradas, pero cada página enlazada tiene ~500 (coincide con "máximo 500" de Hacienda). La cadena avanza hacia atrás en el tiempo; una sola descarga de la "actual" NO sirve para ver el día.
- **2.519 entradas = 2.257 expedientes distintos** (un expediente sale varias veces: una por cada versión/cambio de estado). Hay que deduplicar por `ContractFolderID`.
- Estados (`ContractFolderStatusCode`): RES (resuelto) 746 · PUB (publicado) 678 · EV (en evaluación) 678 · ADJ (adjudicado) 398 · PRE 15 · ANUL 4.
- **Adjudicatario + NIF + importe:** 1.084 entradas traen `WinningParty` y las 1.084 incluyen NIF/CIF e importe (`PayableAmount`, con IVA; también `TaxExclusiveAmount`). ADJ+RES = 1.144 → ~95 % de las adjudicadas/resueltas traen ganador completo (las demás: desiertas, lotes, etc. [VERIFICAR]).
- **Prórrogas/opciones** (`ContractExtension`): 893 entradas (35 %), pero casi todas son la previsión del pliego ("se prevé un plazo de 24 meses"), no una prórroga ejecutada.
- **Modificaciones** (`ContractModification`): 68 entradas (2,7 %), 67 en estado RES; 65 traen importe modificado (`ContractModificationLegalMonetaryTotal`) y plazo (`ContractModificationDurationMeasure`, `FinalDurationMeasure`, `FinalLegalMonetaryTotal`). Corrige F: **sí existe etiqueta específica de modificación**.
- **Procedimiento** (`ProcedureCode`, lista oficial CODICE 2.07 leída en https://contrataciondelestado.es/codice/cl/2.07/SyndicationTenderingProcessCode-2.07.gc): 1 Abierto 1.304 · 9 Abierto simplificado 900 · 3 Negociado sin publicidad 164 · 2 Restringido 91 · 7 Derivado de acuerdo marco 32 · 100 Normas internas 17 · 8 Concurso de proyectos 5 · 4 Negociado con publicidad 3 · 999 Otros 2 · 13 Licitación con negociación 1. **Contrato menor (6): 0** → los menores no están en este feed (están en el ZIP aparte, ver F).
- **Urgencia** (`UrgencyCode`, lista DiligenceTypeCode 1.04: 1 ordinaria, 2 urgente, 3 emergencia): ordinaria 2.434 · urgente 71 · **emergencia 14** (las 14 con adjudicatario, NIF e importe).
- **Órganos:** 285 a 320 órganos distintos por página de ~500. Los más repetidos: Tragsa 74 expedientes (85 entradas), Ente Público Extremeño de Servicios Educativos Complementarios 56, Ciudad Autónoma de Melilla 28, Serveis de Salut de les Illes Balears 19, Ayto. de Vigo 19. Solo 141 entradas (5,6 %) tienen "Ministerio" en la cadena de órganos padre; el feed es mayoritariamente local/autonómico/entes instrumentales.
- Tipos de contrato (`TypeCode`): servicios 1.173 · suministros 752 · obras 487 · resto minoritario.

### 1.1 Ejemplo: emergencia de Adif (HECHO, expediente 3.26/27507.0068; actualizado 30-oct-2026)
Campos que salen: órgano "ADIF - Presidencia" (cadena de padres hasta Ministerio de Transportes), objeto "Emergencia de las obras y de los servicios motivados por graves daños en el túnel número 15, punto kilométrico…", CPV 45221242, NUTS ES512, plazo 4 meses, `ProcedureCode=3`, `UrgencyCode=3`, motivo "Art. 120 Ley 9/2017: Contrato de emergencia", **fecha de adjudicación 2026-03-03**, fecha de formalización/alta **2026-10-30**, 1 oferta recibida, adjudicatario **Nortunel SA (A01310630)**, base 1.706.250 € / con IVA 2.064.562,5 €. El expediente hermano 3.26/27507.0069 (asistencia técnica) → Team Ingeniería y Consultoría SL (B48422547), base 261.450 €.
- Lectura: el importe estimado de licitación sale con `TotalAmount=0`; lo útil es el importe adjudicado. **Retraso de publicación aquí: ~8 meses entre adjudicación (3-mar) y publicación (30-oct)** (dos fechas leídas en el XML; un caso, no media).
- **Mantenimiento de Adif (CPV 50xxx):** en la muestra NO hay ningún contrato de mantenimiento de Adif ya adjudicado. Sí salen en estado PUB (sin ganador todavía): 4.26/23108.0173 "mantenimiento del material rodante ferroviario…" (CPV 50221000) y 2.26/23108.0207 "mantenimiento de instalaciones en terminales de mercancías" (50700000). Lo ya adjudicado de Adif en la muestra es de otro tipo (software, sillas de ruedas, traslado de equipamiento 50312600, un acuerdo marco de vegetación). Los grandes contratos de mantenimiento ferroviario por acuerdos marco/ lotes [VERIFICAR] no se pudieron localizar en la muestra: haría falta buscar por `ContractFolderID` en el ZIP anual.

### 1.2 Ejemplo: emergencia de un ministerio (HECHO, EC-V-26011-L2bis)
Demarcación de Carreteras del Estado en Valencia → DG Carreteras → Sª Gral. Transporte Terrestre → Sª Estado → **Ministerio de Transportes**. Obras de reparación de un túnel (CPV 45221241). `UrgencyCode=3`, procedimiento 3 (negociado sin publicidad), 3 ofertas invitadas, 2 recibidas (1.032.744,48 € la menor; 1.115.485 € la mayor), criterio 100 % precio, adjudicación 2026-10-27 a **GEOTUNEL, S.L. (B95357380)**, 1.032.744,48 € sin IVA / 1.249.620,82 € con IVA; documento de pliego enlazado (URL del sistema de ficheros de PLACSP). Retraso: ~1 semana.
- Otros emergencias en la muestra: Conselleria de Medio Ambiente (Comunitat Valenciana) CMAYOR/2026/44Y05/0067, PAVASAL (A46015129) 1.200.000 € con IVA; Carreteras del Estado en Cataluña 38-GI-260013 y ampliación de obras DANA 72-T-260007; Subdelegación del Gobierno en Tenerife (papeletas electorales, adjudicado en emergencia); Ayto. de Madrid (obras en ejecución subsidiaria); Agencia Balear del Agua EM0082026.

### 1.3 Ejemplo: modificación de contrato (HECHO, ACUAMED ADO/01/24, Ministerio Transición Ecológica)
Asistencia técnica a obras (fondos PRTR "Proyecto tractor, componente 5"). Lote 1 → **TYPSA (A28171288)**, adjudicado 22-may-2024, 919.900 € sin IVA, 2 ofertas. Modificaciones: nº1 "prevista" +73.592 € y +7 meses (total 993.492 €); nº2 +110.388 € y +6 meses ("ampliación… hasta 18-mayo-2027"), total final 1.103.880 €. Lote 2 → Hispánica Prevención (B81427882), modificación +4.734 €. **Se ve el importe final y el motivo en una nota; no se ve la justificación jurídica completa ni el pago.** Actualizado en el feed el 2-nov-2026 → la modificación se publica con retraso variable.

### 1.4 Qué NO sale en el feed (HECHO/[VERIFICAR])
- Facturas, pagos, certificaciones de obra, % ejecutado, sobrecostes reales: ningún campo.
- Contratos menores (0 en la muestra); contratos de entes con plataforma propia no agregada [VERIFICAR].
- Encargos a medios propios (Tragsa): Tragsa aparece como **órgano que licita** (74 expedientes) en la muestra, pero el encargo que recibe de un ministerio no es un contrato adjudicado. Se publica aparte en el Portal de Transparencia ("encargos a medios propios"). Lo que se ve de Tragsa es su subcontratación.
- Emergencia: sale el adjudicatario y el importe, pero con fecha de publicación tardía (caso Adif) y sin expediente justificativo.

## 2. BDNS (API probada) — consultas que funcionan
Base: `https://www.infosubvenciones.es/bdnstrans/api/`. Totales hoy: concesiones 31.334.912; grandes beneficiarios 153.076 filas (persona×ejercicio).
- **Parámetros descubiertos** (los desconocidos se ignoran en silencio; los conocidos con formato malo devuelven `ERR_VALIDACION` con el nombre del parámetro): `vpd=GE`, `page`, `pageSize` (hasta 1000 probado), `order` + `direccion=desc|asc` (campos `importe` en concesiones; `ayudaETotal` en grandes beneficiarios), `nifCif=<NIF>` (ambos endpoints), `fechaDesde` / `fechaHasta` en formato **dd/mm/aaaa codificado `01%2F01%2F2025`** (solo concesiones), `tipoAdministracion=C|A|L` (C = Estado, A = autonómica, L = local; `E` da error), `organos=<código>`, `descripcion=<texto>` (busca en la convocatoria, no en el beneficiario).
- **NO funcionan (ignorados):** `ejercicio`, `importeDesde/Hasta`, `nivel1`, `beneficiario` (da error de formato), `idPersona`. Por tanto no hay filtro de importe mínimo; hay que ordenar y paginar.
- **Aviso:** combinar `fechaDesde` + `order=importe` en todo el año tumbó el servicio ("ERR_MANTENIMIENTO_BBDD") tras 60 s. Evitarlo: consultas pesadas = una por NIF, o ordenar sin fechas.

### 2.1 Top beneficiarios por ejercicio (HECHO, `grandesbeneficiarios`, ayuda equivalente, 3-nov-2026)
Consulta: `grandesbeneficiarios/busqueda?vpd=GE&pageSize=1000&page=0&order=ayudaETotal&direccion=desc` y filtrar `ejercicio` en cliente.
- **2025 (M€):** Red Eléctrica de España 761,9 · Generalitat de Catalunya 588,8 · Univ. de València 448,7 · UP Valencia 361,4 · CSIC 328,6 · Ayto. de València 298,5 · Comunidad de Madrid 283,2 · Iberdrola Clientes 261,7 · Gob. de Canarias 259,8 · CI ETF I Renato PTX Holdco 245,0 · … · **Cruz Roja Española 211,4**; Ayto. de Catarroja 219,5 y Paiporta 212,2 (zona DANA).
- **2024 (M€):** Univ. de València 494,4 · CSIC 386,9 · UP Valencia 377,0 · Telefónica Móviles 298,4 · Unión Profesional 200,0 · … · Cruz Roja 157,0 · Powerco Battery Spain 152,9.
- Sesgo: la cifra acumula muchas concesiones por año; incluye administraciones que reciben transferencias de otras (en 2022 el Ministerio de Sanidad figura con 1.202,5 M€ como beneficiario). No es "dinero a empresas" sin más.

### 2.2 ONG de acogida y entidades (HECHO, por NIF)
Consulta: `grandesbeneficiarios/busqueda?vpd=GE&nifCif=<NIF>&pageSize=10`.
| Entidad (NIF) | 2022 | 2023 | 2024 | 2025 | 2026 (parcial) |
|---|---|---|---|---|---|
| Cruz Roja Española (Q2866001G), M€ | 464,8 | 154,2 | 157,0 | 211,4 | 46,0 |
| Accem (G79963237), M€ | 110,8 | 15,2 | 14,1 | 10,6 | 4,9 |
| Cáritas Española (R2800560A), M€ | 21,4 | 23,3 | 10,0 | 8,2 | – |
| Adif-Alta Velocidad (Q2802152E), M€ | – | 0,18 | 3,4 | 33,6 | 0,23 |
| Adif (Q2801660H), M€ | – | 0,28 | 0,25 | 6,9 | 0,28 |
CEAR: no localizada con el NIF que probé (G28722437 no devuelve nada) [VERIFICAR NIF correcto antes de concluir que no recibe]. Adif recibe poco por subvención: su dinero entra por transferencias/contratos-programa/encomiendas, que **no** son BDNS [VERIFICAR].
- Detalle de concesión (Cruz Roja, `concesiones/busqueda?vpd=GE&nifCif=Q2866001G&pageSize=6&order=importe&direccion=desc`): 183,99 M€ (4-nov-2022) vía **Real Decreto 590/2022 de concesión directa**; 63,08 M€ (jun-2022) "Atención humanitaria a personas inmigrantes"; 57,25 M€ (jul-2022) "Subvención nominativa para programas de protección internacional"; en 2025, 17,55 M€ de la Generalitat Valenciana (decreto de subvención directa) y 17,20 M€ de la Región de Murcia. Cada fila trae instrumento, órgano concedente y enlace a bases (BOE/DOGV/BORM).
- **Corrige/matiza F ("nominativas y directas [VERIFICAR]"): sí salen las nominativas y las de concesión directa por real decreto**; lo que no consta es si todas las que existen están cargadas.

### 2.3 Qué NO sale en BDNS
Pago efectivo y fecha de cobro (solo concesión); justificación y reintegros salvo sanciones/minimis en endpoints aparte; convenios y encomiendas (no son subvenciones); contratos; subvenciones exentas del ámbito de la ley o no declaradas [VERIFICAR alcance]; personas físicas enmascaradas (`***1099**`). Una concesión no es dinero gastado.

## 3. Facturas: ¿hay registro público?
- **Factura concreta (HECHO por normativa, [VERIFICAR] ausencia de excepciones): no es pública.** FACe (Punto General de Entrada de Facturas Electrónicas de la AGE) y los registros contables de factura de cada administración (Ley 25/2013, que derogó el art. 5 de la Ley 15/2010 según el BOE citado en la búsqueda) son sistemas internos; contienen datos del proveedor y no hay consulta pública por factura. Una factura solo se obtiene vía solicitud de acceso (Ley 19/2013), con riesgo de denegación por datos personales/secreto comercial.
- **FACe, agregados:** Hacienda publicó informes PDF "Facturas electrónicas presentadas a las Administraciones Públicas" (hay uno de abril de 2020 en `https://www.hacienda.gob.es/CDI/FACe/`); no comprobé una edición reciente [VERIFICAR].
- **Periodo Medio de Pago (PMP), Hacienda (HECHO):** nota de 22-oct-2026 https://www.hacienda.gob.es/es-ES/Prensa/Noticias/Paginas/2026/20261022-NP-PMP-AGOSTO.aspx — **agosto-2026:** Adm. Central 26,46 días (+4,65 vs julio); CCAA 27,05 (+1,63); Entidades Locales (modelo de cesión) 30,15; Seguridad Social 9,50. CCAA >30 días: Baleares 53,42, Murcia 42,38, Cantabria 38,51, Asturias 32,86, Cataluña 32,00. Deuda comercial: 4.817,6 M€ (0,27 % del PIB). Pagos comerciales de agosto: 6.038,6 M€ (3.947 M€ sanitarios). Entidades locales: facturas pendientes a 31-ago, 44,89 días; de 157 entidades obligadas, 117 ≤30 días, 29 entre 30 y 60, 11 >60.
- **Dónde bajarlo:** página PMP de todas las AAPP (`/es-ES/CDI/Paginas/PeriodoMedioPago/InformacionAAPPs/PMPdelasAAPP.aspx`, XLSX mensual `/cdi/pmp/publicacion-pmp-AAAA-MM.xlsx`; la página citaba "septiembre 2026" como último mes, contradictorio con la nota de agosto del 22-oct → [VERIFICAR] si el XLSX de septiembre ya existe). Consulta por entidad (CCAA y corporaciones locales): aplicación SGCIEF/PMP_NET y visores `buscadorcdi.gob.es/AresPortal/Visualizacion/10017` (CCAA) y `/10018` (local). Retraso: **~7 semanas** (agosto publicado el 22-oct).
- **Morosidad (Ley 15/2010):** informe trimestral de tesorería por entidad y anual de intervención; cada ayuntamiento lo publica en su portal de transparencia (ejemplos de la búsqueda: Sagunto, Cáceres-Diputación, Motril), no hay repositorio nacional único [VERIFICAR].
- **Qué sí/no:** SÍ agregados por subsector, CCAA y entidad local (días de pago, factura pendiente). NO: proveedor, importe de una factura, ni qué contrato la originó.

## 4. Control externo y transparencia
### 4.1 Tribunal de Cuentas (HECHO leído en listado/resúmenes; [VERIFICAR] fechas de 2026)
- Informe nº 1.682, **25-jun-2026**: sistemas de planificación por objetivos de la AGE en ciencia (listado de tcu.es; solo leí el título, no la conclusión).
- **18-dic-2025:** Cuenta General y cuentas del sector público de Murcia 2023; Informe global del sector público autonómico 2022; reordenación del sector público institucional local 2014-2023 (búsqueda; fechas de Pleno citadas, no leí los informes).
- **25-mar-2026:** Ceuta, cuenta general 2023; mismo día, Memoria anual 2025 y modificación del programa de fiscalizaciones 2026.
- **28-abr-2025:** Declaración sobre la Cuenta General del Estado **2023** (búsqueda) → el informe del año N sale en N+2 (≈16 meses tras el cierre). La del 2024 estaba en la Comisión Mixta con ponencia desfavorable por mayoría y votación prevista 23-jun-2026 (resultado no encontrado) [VERIFICAR].
- **Partidos/fundaciones:** informe de aportaciones a fundaciones vinculadas a partidos, Pleno 25-sep-2025; contabilidad electoral de las generales de 23-jul-2023, Pleno 27-mar-2025 (búsqueda). No hallé informe sobre partidos aprobado en 2026.
- **Medios propios:** informe nº 1.558, Pleno 29-feb-2024, actividad de Tragsa 2021-2022. Según prensa: encargos de más de 100 entidades (95 % de la actividad); en el 34 % de expedientes no hay correlación entre encargo y cualificación del personal; 242 contratos de incendios de CCAA/diputaciones 2021-22 [VERIFICAR en el texto del Congreso `251-101.pdf`].
- **Emergencia COVID (leído el texto):** informe nº 1.481, Pleno **28-jul-2022**, ministerios y OOAA: 347 contratos de emergencia en 2020 por 64,1 M€; se analizaron 100 (48,2 M€, 75 % del importe). Conclusiones: 4 casos sin vínculo con el COVID o con alternativa menos restrictiva; en 4 % no se justificó la dación de cuenta al Consejo de Ministros, 12 % fuera de plazo y 39 % sin acreditar plazo; en 28 % no consta comunicación a la Intervención Delegada; 21 % de contratos con denominaciones distintas entre perfil, relación y plataforma del Tribunal (dificulta cruzar datos). **Retraso: ~2 años y 4 meses** tras los hechos de 2020.
- **Retraso típico:** 2 años de media entre el ejercicio y el informe (cuentas: N+2; emergencias 2020 → 2022). Estimación propia sobre 4 casos, no cifra oficial [ESPECULACIÓN de generalización].

### 4.2 AIReF
- Web airef.es, últimas publicaciones leídas: previsiones macro de los presupuestos 2027 de País Vasco (7-oct-2026), Madrid y Galicia (9-oct) y Andalucía (15-oct); la nota dice que "avala" las previsiones; sin conclusiones visibles. Agenda: informe sobre proyectos y líneas fundamentales de presupuestos 2027 (semana del 4-nov-2026).
- Julio 2026: "Informe sobre ejecución presupuestaria, deuda y regla de gasto de las AAPP 2026" (título en la web; no leí el contenido) y 5.ª opinión del Ingreso Mínimo Vital. No conseguí la conclusión → [VERIFICAR]. Mayo 2026: regla de gasto de pensiones cumplida pero "no garantiza la sostenibilidad", gasto medio 13 % del PIB 2022-2050 (resumen de prensa). Agosto 2026: informes individuales de Aragón, Asturias, Canarias y CyL; en Asturias advierte riesgo de incumplir la regla de gasto (prensa).
- **Spending Review:** Hacienda 21-abr-2026 https://www.hacienda.gob.es/es-ES/Prensa/Noticias/Paginas/2026/20260421-NP-CM-SPENDING-REVIEW.aspx formaliza la fase III 2022-2026 con dos áreas nuevas (políticas de empleo; ejes 1-2 del FEDER 2014-2020); informes definitivos de la fase III presentados en feb-2026 (sin cifras de ahorro en la nota). Sobre subvenciones: primer estudio (2019) cifra ~14.000 M€ de subvenciones, ~10.000 M€ de CCAA, con falta de coordinación (prensa). Seguimiento: 100 de 277 propuestas implementadas (36 %), según prensa, sin fecha y sin verificar [VERIFICAR].

### 4.3 IGAE, Portal de Transparencia y CTBG
- **IGAE:** plan anual de control financiero permanente y plan de auditorías y control financiero de subvenciones (se aprueban por resolución anual; la de 2025 está en igae.pap.hacienda.gob.es). El de 2026 no lo localicé; prensa (El Debate, mar-2026) dice que incluye comprobar que no reciban ayudas inhabilitados [VERIFICAR]. Memorias IGAE 2024 y 2025 en resumen. Resultado de las auditorías por beneficiario: no es público individualmente, salvo lo que llegue a informes del Tribunal.
- **Portal de Transparencia** (https://transparencia.gob.es/, leído): Presupuestos (gastos hasta 2022; ingresos 2023-2024), ejecución, informes de fiscalización, cuentas anuales 2013-2024, contratos (con estadísticas), contratos basados en acuerdos marco, convenios y encomiendas, subvenciones, subvenciones a partidos, planes estratégicos de subvenciones y **encargos a medios propios**. Retribuciones: solo altos cargos, en sección aparte. Datos de publicidad activa: buena para listar, pobre para cruzar (varios años desfasados).
- **CTBG (Memoria 2025, nota 9-jul-2026):** récord de 2.767 reclamaciones (+40,2 %): 1.778 estatales (+27,3 %) y 989 autonómicas/locales (+71,7 %); resolvió 2.234; silencio administrativo: 45,5 % en estatales y 75,3 % en autonómicas/locales; en lo estatal, 65,9 % acabaron favorables al reclamante (40,3 % de ellas por motivos formales: la información se dio tras reclamar). Interior encabezó con 193 reclamaciones; cumplimiento de resoluciones por la AGE: 84,8 % (prensa; la nota lo da por separado) [VERIFICAR]. Primer semestre 2026: 1.758 reclamaciones, +60 % (prensa, 6-ago-2026). No leí resoluciones concretas sobre contratos ni subvenciones.

## 5. De lo general a lo concreto
| Nivel | Fuente | ¿Público? | Retraso observado |
|---|---|---|---|
| Total AAPP / déficit | IGAE contabilidad nacional, Eurostat | Sí | 1-3 meses (Hacienda 30-sep: datos a julio/agosto) |
| Ministerio / programa | IGAE ejecución por ministerio, PGE (los de 2023 prorrogados) | Sí, agregado | meses; tabla de gasto del Portal de Transparencia hasta 2022 |
| Órgano / entidad | PLACSP (jerarquía de órganos), BDNS (nivel3), Portal de Transparencia | Sí | PLACSP ~1 día salvo publicación tardía (caso Adif 8 meses) |
| Contrato | PLACSP ATOM/ZIP: ganador, NIF, importe adjudicado, modificaciones, emergencia | Sí (no menores en el feed) | días a meses |
| Subvención/concesión | BDNS API | Sí (incluye nominativas y directas por RD) | días a semanas (concesiones del 2-nov-2026 ya presentes) |
| Factura | FACe / registro contable | **No** (solo agregados PMP) | PMP ~7 semanas |
| Pago efectivo | Tesorería / contabilidad de cada ente | **No**, salvo PMP agregado y acceso Ley 19/2013 | – |
| Control posterior | Tribunal de Cuentas, IGAE, AIReF | Sí, informes | ~2 años (Tribunal) |

## 6. Ocho consultas reproducibles (sin clave)
1. Última página del feed y siguiente: `curl -s "https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom"`; seguir `<link rel="next">` (cada página ~15-18 MB; filtrar `UrgencyCode=3` para emergencias y `ContractModification` para modificaciones).
2. Listas de códigos: `https://contrataciondelestado.es/codice/cl/2.07/SyndicationTenderingProcessCode-2.07.gc` y `http://contrataciondelestado.es/codice/cl/1.04/DiligenceTypeCode-1.04.gc`.
3. Concesiones de una entidad por NIF: `https://www.infosubvenciones.es/bdnstrans/api/concesiones/busqueda?vpd=GE&nifCif=Q2866001G&pageSize=6&order=importe&direccion=desc`.
4. Año completo (sin ordenar, ligero): `.../concesiones/busqueda?vpd=GE&pageSize=3&fechaDesde=01%2F01%2F2025&fechaHasta=31%2F12%2F2025` (totalElements = 19.696.582 concesiones en 2025).
5. Ranking de grandes beneficiarios: `.../grandesbeneficiarios/busqueda?vpd=GE&pageSize=1000&page=0&order=ayudaETotal&direccion=desc`, filtrar `ejercicio`.
6. Grandes beneficiarios de un NIF: `.../grandesbeneficiarios/busqueda?vpd=GE&nifCif=G79963237&pageSize=10` (Accem).
7. Concesiones del Estado/autonomía/local: `.../concesiones/busqueda?vpd=GE&pageSize=2&tipoAdministracion=C` (C = Estado 20.003.128; A = autonómica 9.271.140; L = local 1.886.311).
8. PMP mensual por subsector: nota https://www.hacienda.gob.es/es-ES/Prensa/Noticias/Paginas/2026/20261022-NP-PMP-AGOSTO.aspx y XLSX `https://www.hacienda.gob.es/cdi/pmp/publicacion-pmp-2026-09.xlsx` (nombre según la página; [VERIFICAR] existencia).

## 7. Pendientes y cautelas
- Muestra PLACSP de 4 días: no extrapolar porcentajes (emergencia 0,6 %, modificaciones 2,7 %) al año.
- Cruzar contratos de emergencia 2026 con el ZIP anual y con el Portal de Transparencia no se hizo.
- Leer conclusiones reales de AIReF (julio 2026) y del plan IGAE 2026 antes de citarlos.
- Opinión (no hecho): la ausencia de datos de factura/pago es lo que impide verificar ejecución real de un contrato [ESPECULACIÓN de utilidad; el Tribunal de Cuentas sí menciona la dificultad de cruce].
