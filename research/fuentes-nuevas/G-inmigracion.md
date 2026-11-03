# G. Inmigración en España: datos frescos, saldo fiscal y sesgos de las fuentes

Fecha de la investigación: 3-nov-2026. Autor: investigador de Joel (sin IA de pago en bots).
Leyenda: **[H]** hecho con fuente primaria leída; **[S]** dato de fuente secundaria (prensa, despacho jurídico, blog) que cita una oficial, sin abrir la oficial; **[VERIFICAR]** no contrastado; **[ESPECULACIÓN]** predicción u opinión.
No hay recomendaciones de compra/venta. Esto es contexto para decidir tú, no una tesis.
Ya existían en el repo (no rehecho): partidas 231H (Acciones a favor de inmigrantes), 23VE, 131P en `informes/research/2026-10-30-C66-presupuesto-y-beneficiarios.md` y `explorador/espana-presupuesto.json`; `origen_ascendencia` en `explorador/espana-manual.json`.

Limitación honesta: varias webs oficiales (interior.gob.es, migrationpolicy.org) devolvieron 403 al lector automático. **No** hice la prueba única con Claude in Chrome (queda pendiente, ver sección 9). Por eso muchas cifras de asilo y regularización son [S].

---

## 1. Población, afiliación, regularización y residentes

### 1.1 Población (INE, Estadística Continua de Población, 2.º trimestre 2026) [H por nota INE vía prensa; texto INE no abierto]
- Población total a 1-jul-2026: **49.801.559** (+104.178 en el trimestre; máximo de la serie).
- Nacionalidad extranjera: **7.437.543** (+87.197 en el trimestre) → ~14,9 %.
- Nacidos en el extranjero: **10.291.807** (incluye españoles nacionalizados) → ~20,7 %.
- Nacionalidad española: +16.981 en el trimestre. Los nacidos en España vuelven a bajar.
- Los datos de migraciones son una primera estimación provisional (el INE lo advierte).
- Fuente: nota INE https://www.ine.es/dyngs/Prensa/ECP2T26.htm (6-ago-2026); resumen en https://www.infobae.com/espana/agencias/2026/08/06/espana-roza-los-50-millones-de-habitantes-con-102-millones-de-personas-nacidas-fuera/
- Referencia anterior: 1-ene-2025 (Censo anual) 6.911.971 extranjeros = 14,1 % de 49.128.297 [S: cita en informe Disenso, ver 7.4]. 1-ene-2026 provisional ~7.243.561 [S, misma fuente].
- Matiz: «extranjero» (nacionalidad) y «nacido fuera» no son lo mismo; muchos nacionalizados (latinoamericanos, marroquíes) figuran como españoles en delincuencia, prestaciones, IMV y presos.

### 1.2 Afiliados extranjeros a la Seguridad Social
- **Septiembre 2026: 3.635.979** (+84.220 en el mes, +2,3 %; +547.637 interanual, +17,7 %; 16,2 % del total). Récord. [S] Onda Vasca, 14-oct-2026, citando al Ministerio de Inclusión: https://www.ondavasca.com/la-afiliacion-extranjera-bate-records-con-mas-de-36-millones-de-trabajadores/ (el titular dice «36 millones», error evidente de tipografía; el cuerpo da 3,64 M). [VERIFICAR en la nota oficial de inclusion.gob.es.]
- De ellos, **421.306** eran personas dadas de alta ligadas a la regularización extraordinaria a 30-sep-2026 (326.256 en Régimen General, 22.681 autónomos). [S, misma fuente.]
- Mayo 2026: 3.359.548 (+9,4 % interanual) [S] https://www.moncloa.com/2026/06/13/record-afiliados-extranjeros-seguridad-social-3384619/
- Enero 2026: ~3,04 M, ~+195.000 interanual [H, nota oficial] https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/Paginas/2026/130226-afiliados-extrnajeros-enero.aspx
- Lectura: el salto de agosto-septiembre coincide con las altas de regularizados (afloramiento de empleo ya existente en parte). **Parte del crecimiento es regularización de quien ya estaba trabajando en negro, no solo llegada nueva** [ESPECULACIÓN sobre la proporción; el Ministerio no la publica].
- Octubre 2026: se publica a mediados de noviembre (no disponible hoy).

### 1.3 Regularización extraordinaria 2026 (Real Decreto 316/2026) [S, parcial]
- Aprobada en Consejo de Ministros (adelantada en enero 2026); BOE 15-abr-2026; solicitudes desde el 16-abr (telemático) y 20-abr (presencial). Requisito central: estar en España antes del 1-ene-2026 y acreditar permanencia de al menos 5 meses; antecedentes penales = denegación (según prensa) [VERIFICAR texto BOE].
- Plazo: cerró el **30-jun-2026** (una fuente decía 30-jul: [VERIFICAR] pero la mayoría y el Ministerio apuntan a 30-jun).
- **Solicitudes: 1.174.978** (Elma Saiz, ministra de Inclusión; recogido el 2-jul-2026). [S] https://www.lavozdelanzarote.com/en/news/people/more-than-11-million-foreigners-request-regularization-in-spain-in-the-extraordinary-procedure_244472_102.html
  - Por CCAA (solicitudes): Cataluña 257.000; Madrid 202.000; C. Valenciana 167.000; Andalucía 160.001.
  - Por origen: Latinoamérica 67 %; Colombia 26 %; Marruecos 13,4 %; Venezuela 11,7 %; Perú 8,8 %.
- Estado de tramitación: el Gobierno decía haber procesado ~680.000 (casi 52 %) en julio; más del 70 % de los solicitantes (~840.000) habría recibido una primera autorización provisional de trabajo y residencia al admitirse a trámite [S, esdiario/elnuevodiario citando datos oficiales; confianza baja-media]. Resoluciones favorables finales: sin cifra oficial agregada que haya podido leer; un despacho de abogados (ARC Legal, 20-oct-2026) dice que **ni el Ministerio ni la UTEX ni las oficinas de extranjería facilitan información detallada de pendientes ni plazos** https://www.arc-legal.es/nuevas-resoluciones-de-expedientes-de-regularizacion-extraordinaria/ [S].
- Comparación histórica: la regularización de 2005 afectó a ~600.000 personas (Santa Lucía, ver 5.2). Esta es ~2 veces mayor en solicitudes.
- Cuidado con bulos: se difundió que los regularizados cobrarían «2.800 euros al mes durante 2 años»; Maldita dice que no hay rastro de tal ayuda: https://maldita.es/desinfo/20260429/pedro-sanchez-dara-a-los-inmigrantes-regularizados-2800-euros-al-mes-durante-2-anos-hasta-que-encuentren-trabajo/ [H del titular; cuerpo no leído].
- Sesgos: el Gobierno (PSOE-Sumar) presenta la medida como afloramiento fiscal y laboral; PP/Vox la presentan como «efecto llamada» y «amnistía». El estudio académico de 2005 (Elías, Monras, Vázquez-Grenno, 2025) no encontró efecto llamada a corto plazo y estimó ~4.000 € más de ingresos fiscales por regularizado, pero es **otro contexto** (exigía contrato; esta no) [S vía Santa Lucía].

### 1.4 Residentes con documentación en vigor (Ministerio de Inclusión, OPI)
- 30-jun-2026: **7.909.008** personas extranjeras con documentación de residencia en vigor; **3.885.177** en régimen de extranjería; 134.453 como familiar de español [S, ARC Legal; el OPI oficial no localizado para esa fecha] https://www.arc-legal.es/casi-79-millones-de-personas-extranjeras-tienen-documentacion-de-residencia-en-vigor-en-espana/ [VERIFICAR]. Nota: 7,9 M en documentación supera los 7,44 M del INE porque incluye residentes comunitarios por certificado y otras categorías de cómputo distinto; no son comparables sin leer la nota del OPI.

---

## 2. Asilo y llegadas irregulares

### 2.1 Protección internacional
- **2025 (Interior, balance de la OAR, 16-ene-2026): 144.396 solicitudes formalizadas; 160.951 expedientes resueltos (máximo histórico); Venezuela >85.000 (59 %); al cierre, 97.275 pendientes de admisión y 121.456 pendientes de resolución** [S: titular y cifras vía buscador; página Interior dio 403]. https://www.interior.gob.es/opencms/es/detalle/articulo/La-Oficina-de-Asilo-y-Refugio-resuelve-160.951-expedientes-de-proteccion-internacional-en-2025-la-mayor-cifra-de-su-historia/ y https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/interior/paginas/2026/160126-balance-oficina-asilo-2025.aspx
- 2025 enero-septiembre: 108.649 solicitudes [S, ARC Legal].
- **2026: 41.896 (ene-abr) y 50.285 (ene-may); Venezuela 29.244 y Colombia 3.296 hasta mayo** [S, ARC Legal y blogs que citan el avance de Interior]. Hasta septiembre no localizado → [VERIFICAR] en la estadística de la Dirección General de Protección Internacional. Tendencia: 2026 va por debajo de 2025 [S].
- Resoluciones favorables/denegadas 2023-2026: no pude leer el desglose oficial (estatuto de refugiado, protección subsidiaria, razones humanitarias). Dato conocido y matizable: en 2022-2025 buena parte de los venezolanos obtiene **«razones humanitarias» (autorización de residencia 1 año), no refugio**; esto infla la cifra de «solicitudes» frente a «refugiados reconocidos» [VERIFICAR con la tabla oficial].
- Sesgo: CEAR (ONG, recibe fondos públicos para gestionar plazas) subraya déficits de acogida y bajas tasas de reconocimiento; Interior destaca el volumen resuelto. Ambos tienen interés institucional.

### 2.2 Llegadas irregulares (Interior, balance con corte 15-oct-2026) [S: RTVC/EFE del 16-oct-2026; el balance oficial dio 403]
- https://rtvc.es/la-llegada-de-migrantes-a-canarias-en-los-primeros-15-dias-de-octubre-triplica-la-de-2025-16-de-octubre-de-2026/
- **Canarias: 8.970 (vs 13.491 en 2025, −33,5 %)**; primera quincena de octubre: 1.837 (vs 643, +185 %). Al cierre del primer semestre el descenso era −67,2 %: la caída se está reduciendo.
- **Baleares: 6.741 (vs 6.104, +10,4 %).** Península marítima: 6.717 (+9,25 %).
- **Ceuta + Melilla (terrestre): 4.777 (vs 3.150, +51,7 %)**; Ceuta +41 %, Melilla +169,6 % (el artículo cita 7.010 para Melilla pero no cuadra con el total; el dato coherente es ~701).
- Total España **sin** la entrada masiva de Ceuta del 30-31 jul: −5,9 %; por mar −12,9 %.
- **Ceuta, 30-31 julio 2026:** entrada masiva a nado. Interior **no la incluye** en el balance quincenal; el presidente de Ceuta estimó 1.800-2.000 entradas a nado y 3.000-5.000 personas aún en la ciudad cuatro días después; un informe oficial del 30-jul habla de 1.109 intentos y 493 interceptados; cadáveres recuperados: 67 (EFE, 1-ago) y 88 según el Gobierno de Ceuta [S, cifras discrepantes; VERIFICAR] https://www.eldebate.com/espana/20260803/ceuta-estima-quedan-entre-3000-5000-inmigrantes-ciudad-entradas-masivas_446222.html ; https://www.lamoncloa.gob.es/consejodeministros/Documents/2026/situacion-ceuta/informes-GC/EM-3/20260730-Informe-presion-migratoria-Ceuta.pdf (no abierto).
- Ceuta a 31-ago: 4.076 entradas terrestres (+102,3 %) y Interior retira del cómputo a quienes siguen en «triaje» hasta cerrar el proceso, sin fecha pública https://www.moncloa.com/2026/09/03/llegadas-migrantes-ceuta-2026-interior-3425191/ [S]. **Implicación: el total oficial de 2026 está infraestimado por criterio, no necesariamente por ocultación.**
- Sesgo de lectura: «bajan las llegadas» (Gobierno) es cierto para Canarias en el acumulado pero esconde Ceuta/Melilla/Baleares y la reversión de octubre; «récord» (oposición) mezcla entradas con permanencia.

---

## 3. Acogida, menores y gasto

### 3.1 Presupuesto y ejecución (repo, C66, datos IGAE/PGE prorrogados) [H del repo]
- Programa 231H «Acciones a favor de inmigrantes»: 2025 inicial 745,4 M€; definitivo 1.393,9 M€; obligaciones 1.257,6 M€; 2026 definitivo 1.211,9 M€; hasta ago-2026 739,6 M€.
- 23VE (Plan de Recuperación, sistema de acogida): definitivo 126,5 M€; obligaciones 16,7 M€ (baja ejecución).
- 131P Asilo y apátridas (Interior): obligaciones 14,8 M€ (2025).
- Cooperación al desarrollo (143A) no es gasto en inmigración: no sumar.
- Cautela: 231H mezcla acogida, integración, CETI y subvenciones; no equivale a «coste de la inmigración» (no incluye sanidad, educación ni IMV, que están en otras partidas y CCAA).

### 3.2 Sistema de acogida de protección internacional [S]
- Resolución BOE de 23-jun-2026 (Dirección General de Atención Humanitaria y Sistema de Acogida) fija plazas y costes jul-2026/jun-2027 https://www.boe.es/boe/dias/2026/06/25/pdfs/BOE-A-2026-13877.pdf (no abierta: [VERIFICAR] tablas). Una línea (acogida integral) ~38,9 M€/año; prórroga de contratos 2026: 96.063.103,30 € (Hacienda) [S].
- Plazas: objetivo de mantener 53.500 plazas (Hacienda, 2025). «Más de 124.000 personas atendidas en 2025» (EUAA, dip.euaa.europa.eu/node/10721) [S].
- Subvención directa 268,7 M€ para protección internacional y atención sociosanitaria en CETI de Ceuta y Melilla (año no fijado en lo leído: [VERIFICAR]) https://www.inclusion.gob.es/w/el-gobierno-destina-268-7-millones-de-euros-para-proteccion-internacional-y-para-la-atencion-sociosanitaria-en-los-cetis-de-ceuta-y-melilla
- Entidades gestoras (según prensa/ministerio): Cruz Roja, Accem, CEPAIM, CEAR y otras 8 entidades colaboradoras. **Importes por entidad: no verificados** (habría que consultar PLACSP/BDNS; no accedí). [VERIFICAR]
- Sesgo: las ONG gestoras son a la vez proveedoras y voces de política migratoria (conflicto de interés declarado, no ilegal). Vox y parte del PP lo usan para hablar de «industria de la inmigración»; el dato verificable es la dependencia de fondos públicos, no malversación.

### 3.3 Menores extranjeros no acompañados (MENA)
- Reubicados entre CCAA (feb-2026): 1.019 desde Canarias, Ceuta y Melilla; pendientes 469 (Canarias), 128 (Ceuta), 9 (Melilla) [S, Ministerio Política Territorial] https://mptmd.gob.es/content/dam/mpt/prensa/notas_de_prensa/notas/2026/02/20260225_NP_CEUTA.pdf
- Fondos: Consejo de Ministros (jul-2026) autorizó **35 M€** para reforzar sistemas de acogida; 24,5 M€ proporcionales al resto [S]. Capacidad ordinaria fijada en **17.081 plazas** (ago-2026) [S, Onda Vasca].
- Coste por plaza: **sin cifra oficial actual**. Un cálculo periodístico antiguo da ~50.000 €/menor/año (20 M€ para 400 menores) [S, estimación; no usar como dato].
- Tras la entrada masiva de Ceuta (>100 menores según Guardia Civil en las primeras horas) la cifra actual de menores tutelados en Ceuta/Canarias en 2026 no está verificada [VERIFICAR] (Fiscalía/Registro MENA).

---

## 4. Prisiones y delincuencia: cómo leer los datos

### 4.1 Población reclusa extranjera [S, con cálculo cruzado]
- Cierre 2024 (SGIP, Informe General Penitenciario, vía Disenso): AGE 48.947 internos, 14.336 extranjeros (29,3 %); Cataluña (Generalitat) 8.594 / 4.437 (51,6 %); **total 57.541 / 18.773 = 32,6 %**.
- 2025 (El Debate, 28-ago-2026, citando SGIP): **20.524 extranjeros (+10,7 %), 33,2 % del total**; el mayor aumento anual desde 2009 [S]. https://www.eldebate.com/espana/20260828/cada-diez-presos-espana-marruecos-subiendo_452781.html Los dos datos son coherentes (18.773 × 1,107 ≈ 20.800).
- Por nacionalidad (ago-2025): Marruecos 6.188 presos (10,0 % de presos vs 1,9 % de la población); Colombia 3,4 % vs 1,2 %; Argelia 2,5 % vs 0,2 %; Albania 507 de 6.483 residentes [S].
- Prisión preventiva (cierre 2024): extranjeros 47,9 % (4.035 de 8.426) vs 25 % entre penados (9.815 de 39.283) [S vía Disenso, atribuye a Interior].
- Tendencia 2014-2024: españoles −3 %, extranjeros +20 % [S].
- Prisiones de Cataluña y País Vasco no están en el informe de la SGIP: el total nacional hay que sumarlo; Consejo de Europa/The Objective cita 52 % de extranjeros en cárceles catalanas.

### 4.2 Condenados (INE, publicación 14-jul-2026, año 2025) [H, nota INE leída]
- Adultos: **306.237 condenados; 70,2 % españoles, 29,8 % extranjeros (por diferencia)**. Tasa por 1.000 habitantes de 18+: españoles **6,1**, extranjeros **15,3** (×2,5).
- Menores (14-17): 13.245; 78,5 % españoles; tasas 5,6 vs 10,2.
- Para 2023 la tasa era 5,8 vs 14,6 (Santa Lucía, citando INE). Fuente 2025: https://ine.es/dyngs/Prensa/EPCAEPCM2025.htm

### 4.3 Cómo interpretarlo (sesgos y contexto)
Argumentos de quienes ven «sobrerrepresentación preocupante» (Disenso/Vox y parte del PP):
- Extranjeros ~14 % de la población pero ~40 % de detenidos/investigados en 2024 y ~33 % de presos; sobrerrepresentación ×2,1 en condenas, ×2,3 en presos, ×2,8 en detenciones (Disenso, Informe n.º 30, jun-2026). Argumentan que el filtro judicial no elimina la diferencia (37,7 % detenciones → 29,3 % presos → 28,6 % condenas firmes).
Argumentos de quienes piden cautela (Santa Lucía/Carrasco, mar-2026; criminólogos):
- La población extranjera es más joven y más masculina; los varones jóvenes delinquen más en cualquier país. Ajustando por edad/sexo la brecha se reduce (no he visto cifra española ajustada y publicada: [VERIFICAR]).
- Hay delitos que **solo** cometen extranjeros (infracciones de la Ley de Extranjería, entrada/estancia irregular con expulsión) y los **no residentes/turistas** (que no están en el denominador del padrón) inflan la cifra; delincuencia organizada transnacional con autores no residentes.
- Mayor uso de **prisión preventiva** con extranjeros por riesgo de fuga/falta de arraigo (47,9 % vs 25 %): afecta al stock de presos.
- Nacionalidad ≠ origen: los nacionalizados cuentan como españoles; los datos subestiman la «segunda generación».
- Posible sesgo policial (identificación, perfilado) en detenciones; pero ese sesgo no explica el tramo judicial.
- Correlación ≠ causalidad; el estudio de 1999-2007 (Alonso-Borrego et al.) no halló relación mecánica con el aumento de inmigración.
Sesgos de las fuentes: Disenso es el think tank de Vox (presidido por Santiago Abascal): selecciona métricas de mayor sobrerrepresentación (detenciones, delitos sexuales) y su informe la presenta como tesis; Santa Lucía es fundación aseguradora, pro-inmigración moderada; INE e Interior son oficiales pero publican poco desglose cruzado (nacionalidad × delito × sexo × edad no está en los informes ordinarios). Datos por delito concreto (p. ej. agresiones sexuales: Disenso cita 41,7 % de detenciones por penetración en 2024 y >60 % en Cataluña 2025) → [VERIFICAR] con Balance de Criminalidad de Interior.
Ratios por 100.000: con los datos de arriba, extranjeros presos ≈ 20.524/7,2 M ≈ **~280 por 100.000**; españoles ≈ (62.000−20.500)/42 M ≈ **~100 por 100.000** (cálculo mío aproximado, denominador de población total, sin ajustar edad/sexo). [VERIFICAR; 33,2 % de total estimado a ~61.800 internos.]

### 4.4 Coste por preso
- No encontré cifra oficial reciente. Estimaciones: ~58-71 €/día (~21.000-26.000 €/año) calculadas dividiendo presupuesto/internos o citadas por prensa (The Objective, 2022, citando Instituciones Penitenciarias ~71 €/día); el informe SPACE del Consejo de Europa da 65 €/día con datos de 2011 y The Objective cita 234,5 €/día con datos de 2022 (probablemente otro concepto). [VERIFICAR; rango muy dispar.] https://theobjective.com/espana/2022-04-12/espana-preso-euros-mes/
- Consecuencia: el coste anual de ~20.500 presos extranjeros sería del orden de **430-540 M€** con 21.000-26.000 €/año [ESPECULACIÓN aritmética mía; sin ajuste por Cataluña/País Vasco]. No es dato oficial.

---

## 5. Saldo fiscal: estudios y método

### 5.1 Resumen del debate (para contrastar)
- **Saldo positivo (o neutro-modesto):** los inmigrantes llegan en edad de trabajar, cotizan y consumen menos pensiones, sanidad y educación a corto plazo. Argumentan Oficina Nacional de Prospectiva y Estrategia (Moncloa), Funcas, Fedea, BBVA Research, Banco de España (en PIB), OCDE/JRC. **Sesgo**: ONPE es un órgano de la Presidencia (institucional, interés en la política migratoria del Gobierno); Fedea/Funcas/BBVA son centros independientes pero con marco consensual «necesitamos inmigración».
- **Saldo negativo (o dudoso):** el coste de baja cualificación + reagrupación familiar + prestaciones, y el efecto de largo plazo cuando envejecen. Argumentan Disenso (Vox), Fundación NEOS (coste de «30.000 M€» según un medio: ver 5.4) y parte de PP. **Sesgo**: think tanks partidistas, modelos con perfiles ejemplares y sin tasa de retorno.

### 5.2 Instituto Santa Lucía, Raquel Carrasco (mar-2026) [H, PDF leído]
- Conclusión: impacto fiscal medio «modesto y muy heterogéneo» según edad, empleo, salarios, familia y acceso a prestaciones. https://institutosantalucia.es/wp-content/uploads/2026/03/informe-efectos-economicos-inmigracion-espana.pdf
- JRC (Comisión Europea, datos de 2015, UE): impacto fiscal neto anual por persona: nativos ≈ −476 €, migrantes intra-UE ≈ −208 €, extra-UE ≈ −219 €; los migrantes aportan de media unos 250 €/año más que los nativos (saldo menos negativo) pero con grandes diferencias por país.
- España: Oficina Económica del Presidente (informe 1996-2006): en 2005 los inmigrantes aportaron 23.402 M€ e implicaron un gasto de 18.618 M€ → **+4.784 M€** (≈ la mitad del superávit público ese año). Dolado y Vázquez (2008): +2.000 M€/año hacia 2008, ~3.000 M€ hacia 2010. Datos antiguos, con inmigración joven y boom del empleo; no extrapolar a 2026.
- FIPROS (Seguridad Social, 2006-07): efecto sobre pensiones «limitado y transitorio»: exige flujos continuos.
- Sanidad: uso de atención primaria similar o algo menor que los nativos, menos especialista, algo más urgencias en algunos colectivos; al ser más jóvenes el gasto agregado es menor (Regidor, Llop-Gironés).

### 5.3 Oficina Nacional de Prospectiva y Estrategia (Moncloa): «España ante el reto migratorio. Dos futuros posibles» (borrador, mar-2026) [H, PDF leído]
- Método: escenarios 2026-2075; base vs. −30 % de flujos. **No son predicciones.** Grupo técnico con expertos de OCDE y universidades (Dumont, Damas de Matos, Amuedo-Dorantes, Christl…). Versión final prevista 2.º trimestre 2026 [VERIFICAR si ya se publicó y si cambian las cifras]. https://futuros.gob.es/sites/default/files/2026-03/España_ante_el_reto_migratorio_dos_futuros_posibles.pdf
- Con −30 % de inmigración: gasto en pensiones +1,2 % del PIB en 2075 (máximo ~+1,4 % entre 2050 y 2060); ≈ 9.500 M€ extra en 2035, 30.000 M€ en 2055, 32.000 M€ en 2075; cotizaciones +12 %.
- Saldo fiscal: la contribución neta de los inmigrantes caería **27 % en 2075 (~0,4 % del PIB)**; para compensar, +14 % en Impuesto de Sociedades o ~+6 % de IVA. La contribución neta «suele ser positiva y superior a la de la población nacida en España» (cita a OCDE IMO).
- Sesgo/limitación: el informe es institucional y compara dos escenarios; **no calcula un saldo fiscal total por año real**, sino la diferencia entre escenarios. No asume una vida laboral concreta de nuevos llegados (productividad, retorno, reagrupación).

### 5.4 Funcas (monográfico, feb-2026), Banco de España, Fedea
- Funcas, «La inmigración en España: retos, impacto y políticas» (coord. Carrasco y Torres, ene-feb 2026) [H, PDF parcialmente leído]: la incorporación de fuerza laboral extranjera explicaría **~47 % del avance del PIB desde 2022** (4,2 puntos). No da saldo fiscal agregado en lo que he podido buscar; subraya integración laboral de mujeres inmigrantes (≈247.000 mujeres con menor participación; coste de oportunidad ~9.880 M€/año, cálculo Funcas). https://www.funcas.es/wp-content/uploads/2026/02/Estudios-de-la-Fundacion-111.pdf
- Banco de España (Pilar Cuadrado, jul-2026): inmigrantes aportaron ~1,7 pp al crecimiento anual medio del PIB (3,7 %) y ~0,5 pp al PIB per cápita (2,7 %) en 2022-2025; antes, boletín: 0,4-0,7 pp del PIB per cápita 2022-2024 [S: Europa Press/Bolsamanía] https://www.bolsamania.com/noticias/economia/economia--los-inmigrantes-aportaron-17-puntos-al-alza-del-pib-espanol-entre-2022-y-2025-y-05-puntos-al-pib-per-capita--22906098.html . **PIB per cápita no es saldo fiscal.** No localicé un saldo fiscal del Banco de España.
- Fedea (feb-2026 y 2024): inmigración no afecta significativamente a empleo y salarios de nativos; uso del SNS similar a españoles de misma edad [S]. Sin cifra fiscal localizada.
- BBVA Research y CaixaBank Research: no localicé estudio con cifra fiscal 2026 [VERIFICAR].
- OCDE, International Migration Outlook 2025 (3-nov-2025): España añadió 368.000 residentes permanentes en 2024 (−1,8 %); 5.º país OCDE por inmigración permanente [S]. Edición 2026: no localizada hoy [VERIFICAR; suele salir en noviembre].
- AIReF: eleva la previsión de inmigración neta a ~625.000 personas (frente a 400.000) [S, noticia sin fecha clara; VERIFICAR].

### 5.5 Disenso (Vox), «La inmigración y su impacto económico negativo en el Estado de bienestar» (presentado en el Congreso, sep-2025) [S: The Objective, 26-sep-2025]
- Método: contribución neta vitalicia con perfiles simulados (impuestos y cotizaciones menos gasto público, incl. pensiones). Escenarios: varón africano nacido en España, salario medio de su origen 20.060 €/año: **−422.946 €**; llegado a los 18: −158.044 €; familia con dos hijos: −1.496.502 €. Umbral de saldo positivo: 45.150 €/año de salario medio (31.670 € si llegó a los 18). https://theobjective.com/espana/politica/2025-09-26/vox-inmigrante-africano-estado/
- Críticas (elDiario.es y expertos citados en prensa): perfiles elegidos, supuestos que inflan el gasto y ausencia de tasa de retorno [S, no leído en origen]. Es un think tank partidista; **utilidad: muestra qué supuestos hacen negativo el saldo (bajo salario + familia + larga vida).**
- Otro: «Fundación NEOS (2025): exceso de inmigración cuesta ≥30.000 M€/año». Maldita lo tiene como afirmación a comprobar: https://maldita.es/buloteca/claim/el-exceso-de-inmigrantes-cuesta-30-000-millones-al-ano-a-espana [H del titular; cuerpo no leído, desenlace del chequeo = [VERIFICAR]].

### 5.6 Prestaciones, pensiones, cotizaciones, educación
- IMV: Seguridad Social (vía transparencia citada por Maldita): ~82 % de titulares con nacionalidad española y ~17 % extranjeros en 2025 y en el 1.er semestre de 2026; los españoles superan a los extranjeros desde 2020. No hay desglose de nacionalidad de los beneficiarios (solo titulares); «españoles» incluye nacionalizados. Junio 2026: 860.458 titulares/hogares y 2.627.344 personas; agosto 2026: >2,7 M personas, 894.000 hogares (Moncloa). [S] https://maldita.es/prebunking/20260710/ingreso-minimo-vital-espa%C3%B1oles-extranjeros/ (cifras vía resumen de buscador; cuerpo no leído: [VERIFICAR]). El repo (C66) ya indica que los extranjeros están algo por encima de su peso en la población en el IMV, con riesgo de pobreza ~3 veces mayor.
- Cotizaciones: 3,64 M de afiliados extranjeros (16,2 %); prestación contributiva por desempleo: por debajo de su peso entre cotizantes (C66). No hay estadística oficial pública de «cotización neta menos pensión pagada por nacionalidad» fácil de reproducir.
- Pensiones: España paga pensiones a quienes cotizaron en el extranjero por convenios; el bulo «pagamos pensiones a más de 100.000 inmigrantes que nunca cotizaron» fue desmentido por Maldita en 2023 (referenciado ya en `espana-manual.json`).
- Educación: cifra de alumnado extranjero (Estadística de enseñanzas no universitarias, Ministerio de Educación) **no localizada hoy** [VERIFICAR].
- Sanidad: Tribunal de Cuentas / gasto sanitario en extranjeros irregulares: **no localizado**; solo evidencia de uso (5.2). Cualquier cifra de «coste de sanidad a inmigrantes» que circule sin fuente = [VERIFICAR].

---

## 6. Noticias rectificadas, desmentidos y bulos (solo con URL de verificación)
| Tema | Qué se difundió | Qué dice la verificación | URL | Confianza |
|---|---|---|---|---|
| Ayudas a regularizados | «Sánchez dará 2.800 €/mes durante 2 años» | Maldita: sin rastro de tal ayuda | https://maldita.es/desinfo/20260429/pedro-sanchez-dara-a-los-inmigrantes-regularizados-2800-euros-al-mes-durante-2-anos-hasta-que-encuentren-trabajo/ | media (cuerpo no leído) |
| Delitos en Cataluña | «El 49 % de los delitos son de extranjeros» | Maldita lo analiza como afirmación a contextualizar; desenlace no leído | https://maldita.es/malditobulo/20251027/extranjeros-49-delitos-cataluna/ | baja |
| Coste de inmigración | «Cuesta 30.000 M€ al año» (NEOS) | En la buloteca de Maldita; desenlace no leído | https://maldita.es/buloteca/claim/el-exceso-de-inmigrantes-cuesta-30-000-millones-al-ano-a-espana | baja |
| Pensiones a inmigrantes | «>100.000 cobran sin haber cotizado» | Maldita, 24-abr-2023 | https://maldita.es/malditobulo/20230424/no-no-pagamos-pensiones-a-mas-de-100-000-inmigrantes-que-jamas-cotizaron/ | media |
| Tasa de condenas | «14,6 vs 5,8 por 1.000» | Cifra real del INE 2023 (con matices de edad/sexo) | https://maldita.es/buloteca/claim/la-tasa-de-condenas-en-extranjeros-es-de-14-6-por-cada-1-000-habitantes-mientras-que-la-de-espanoles-es-de-5-8-por-cada-1-000 | media |
| Entrada masiva Ceuta (20-ago) | «Marroquíes organizan nueva entrada masiva el 20-ago-2026» | Aparece en la buloteca de Maldita | https://maldita.es/buloteca/claim/marroquies-organizan-una-nueva-entrada-masiva-a-ceuta-el-20-de-agosto-de-2026 | baja |
- Cifras corregidas: el balance de Interior de Ceuta/Melilla **sube y baja** por criterio de triaje (ver 2.2); no es rectificación, sino cambio de cómputo.
- No encontré en hemeroteca/Newtral rectificaciones de medios grandes sobre cifras de inmigración en 2026 con URL verificable. No las incluyo.

---

## 7. Contrastes alcista/bajista (sin recomendación)
Caso «saldo fiscal positivo/crecimiento»:
- La población española crece solo por extranjeros (INE T2/2026); 47 % del PIB desde 2022 (Funcas); +0,5 pp al PIB per cápita (Banco de España); con −30 % de flujos, el gasto en pensiones sube ~1,2 % del PIB en 2075 (ONPE).
- Regularizados: 421.306 en alta en septiembre; en 2005 aumentó la recaudación ~4.000 €/regularizado (Elías et al., vía Santa Lucía).
Caso «saldo incierto o negativo»:
- Impacto fiscal «modesto» y dependiente de salarios (Santa Lucía); los beneficios sobre pensiones son «limitados y transitorios» (FIPROS); empleo concentrado en sectores de salario bajo; IMV con riesgo de pobreza ~3× (C66); efecto en vivienda y servicios locales no capturado en el saldo estatal; reagrupación familiar y envejecimiento del colectivo.
Zonas de acuerdo entre ambos: el saldo depende de edad, empleo formal y salario; el efecto agregado en el Estado central es pequeño frente al PIB (≈0,4 % del PIB en el escenario de ONPE).

---

## 8. Tabla de cifras clave
| Dato | Valor | Fecha | Fuente | Confianza |
|---|---|---|---|---|
| Población total | 49.801.559 | 1-jul-2026 | INE ECP T2/2026 (nota) | alta |
| Extranjeros (nacionalidad) | 7.437.543 (≈14,9 %) | 1-jul-2026 | INE ECP | alta |
| Nacidos en el extranjero | 10.291.807 | 1-jul-2026 | INE ECP | alta |
| Afiliados extranjeros SS | 3.635.979 (+17,7 % interanual) | sep-2026 | Inclusión vía Onda Vasca | media |
| Altas de regularizados | 421.306 | 30-sep-2026 | Inclusión vía Onda Vasca | media |
| Solicitudes regularización | 1.174.978 | 16-abr a 30-jun-2026 | M. Elma Saiz vía La Voz de Lanzarote | media |
| Documentación de residencia en vigor | 7.909.008 | 30-jun-2026 | ARC Legal (OPI) | baja-media |
| Solicitudes de asilo 2025 | 144.396 (Venezuela >85.000) | 2025 | Interior (balance OAR) | media |
| Solicitudes de asilo 2026 | 50.285 (ene-may) | 31-may-2026 | blogs que citan Interior | baja-media |
| Canarias llegadas 2026 | 8.970 (−33,5 %) | 15-oct-2026 | Interior vía RTVC | media |
| Baleares llegadas 2026 | 6.741 (+10,4 %) | 15-oct-2026 | Interior vía RTVC | media |
| Ceuta+Melilla terrestres | 4.777 (+51,7 %) | 15-oct-2026 | Interior vía RTVC | media |
| Entrada masiva Ceuta 30-31 jul | 1.800-2.000 (estimación local) | jul-ago-2026 | Gob. Ceuta vía El Debate | baja |
| Partida 231H (obligaciones 2025) | 1.257,6 M€ | 2025 | IGAE/PGE (repo C66) | alta |
| Presos extranjeros | 20.524 (33,2 %) | 2025 | SGIP vía El Debate | media |
| Presos extranjeros AGE+Cataluña | 18.773 de 57.541 (32,6 %) | 31-dic-2024 | SGIP+Generalitat vía Disenso | media |
| Preventivos extranjeros | 47,9 % (vs 25 % penados) | 31-dic-2024 | Interior vía Disenso | media |
| Condenados extranjeros adultos | 29,8 % (tasa 15,3 vs 6,1/1.000) | 2025 | INE (14-jul-2026) | alta |
| Titulares IMV extranjeros | ~17 % | 2025-1S 2026 | SS vía Maldita | media |
| Saldo fiscal 2005 | +4.784 M€ | 2005 | OEP vía Santa Lucía | media (antiguo) |
| Caída de la contribución neta con −30 % flujos | −27 % (~0,4 % PIB) | 2075 | ONPE (borrador mar-2026) | media (escenario) |
| Aporte al PIB 2022-25 | 1,7 pp (PIB), 0,5 pp (per cápita) | jul-2026 | Banco de España vía Bolsamanía | media |
| Saldo vitalicio perfil «africano 22 años» | −422.946 € | sep-2025 | Disenso/Vox vía The Objective | baja (partidista) |

---

## 9. Opaco o no publicado / pendiente
- Resoluciones finales de la regularización (aprobadas/denegadas/pendientes): sin cifra oficial agregada; el Ministerio no publica plazos (según ARC Legal).
- Fracción de afiliación nueva que es afloramiento de economía sumergida vs llegada nueva.
- Desglose de nacionalidad × delito × sexo × edad en prisiones e INE; prisión preventiva por nacionalidad actualizada.
- Coste real por preso y por plaza de MENA (Interior/CCAA no publican serie oficial reciente).
- Importes por entidad (Cruz Roja, Accem, CEAR, CEPAIM…) en PLACSP/BDNS: **no consultados**; hacer consulta directa.
- Gasto sanitario a extranjeros por situación administrativa; informes del Tribunal de Cuentas sobre ello: no localizados.
- Alumnado extranjero (Educación): no obtenido.
- Saldo fiscal oficial agregado por nacionalidad (no existe estadística pública): solo estimaciones de terceros.
- Tarjeta/certificado de residencia a 30-jun-2026 en la nota oficial del OPI; asilo ene-sep 2026; balance quincenal de Interior directo (403 en interior.gob.es).
- Pendiente de la regla del proyecto: probar Claude in Chrome en interior.gob.es, migrationpolicy.org y OPI (una sola prueba por sitio).
- OCDE International Migration Outlook 2026 (probablemente nov-2026); informe final ONPE (2.º trim. 2026).

---
## Resumen para Joel (12 líneas)
1. Población: 49,8 M; 7,44 M extranjeros (14,9 %) y 10,29 M nacidos fuera (INE, 1-jul-2026).
2. Afiliados extranjeros: 3,64 M en septiembre (+17,7 %), con 421.306 altas de regularizados (fuente secundaria).
3. Regularización RD 316/2026: 1.174.978 solicitudes, cerró 30-jun; sin cifra oficial de resoluciones finales.
4. Asilo: 144.396 solicitudes en 2025 (Venezuela 59 %); 2026 ~50.285 hasta mayo, más bajo que 2025 (secundario).
5. Llegadas irregulares a 15-oct-2026: Canarias −33,5 %, Baleares +10,4 %, Ceuta/Melilla +51,7 %; la entrada masiva de Ceuta (30-31 jul) no se cuenta.
6. Presos: 33,2 % extranjeros en 2025; condenados 2025: 29,8 % con tasa 2,5 veces la de españoles; matices: edad, sexo, preventiva, nacionalidad vs origen.
7. Gasto: partida 231H 1.257,6 M€ obligados en 2025; importes por ONG no verificados.
8. Saldo fiscal: ONPE (borrador) dice que bajar 30 % los flujos recorta ~0,4 % del PIB la contribución neta en 2075; Santa Lucía lo ve «modesto»; Disenso (Vox) da saldos vitalicios negativos con perfiles simulados.
9. PIB: Funcas 47 % del avance desde 2022; Banco de España +0,5 pp al PIB per cápita. No es lo mismo que saldo fiscal.
10. Bulos verificados: «2.800 €/mes a regularizados» (Maldita); «>100.000 pensionistas sin cotizar» (Maldita 2023).
11. Opaco: resoluciones de la regularización, coste por preso/plaza, contratos por entidad, gasto sanitario, alumnado.
12. Siguiente: probar Chrome en sitios con 403, abrir la tabla del BOE 23-jun-2026 y PLACSP/BDNS, esperar IMO 2026 y publicación de octubre de afiliación (mediados de nov).
