# C66 · España: a dónde va cada euro y quién lo recibe (30-oct-2026)

Sin API de Anthropic. Datos en `explorador/espana-presupuesto.json` y en las claves nuevas de `explorador/espana-manual.json` (`poblacion_referencia`, `beneficiarios`, `requisitos_acceso`, `origen_ascendencia`, `violencia_genero`). Se ven en la pestaña **España** del Panel y en la pestaña **Datos** del móvil. Niveles: [P] fuente oficial leída · [S] secundaria · [VERIFICAR] no leído. Sin recomendaciones.

## Resumen
1. **Presupuesto [P]:** siguen prorrogados los PGE de 2023; 2025 y 2026 parten del mismo crédito inicial (380.822 M€). El Estado reconoció **423.336 M€** de obligaciones en 2025, pero esa cifra no es el gasto público: incluye 121.514 M€ de amortización de deuda y 71.889 M€ de transferencias internas.
2. **Ministerios [P]:** Inclusión (54.801 M€) y Defensa (18.806 M€) encabezan la lista. Igualdad obligó **481 M€, el 0,11 %**, y el 61 % de eso fue violencia de género.
3. **Beneficiarios:** los extranjeros son cerca del **17 % de los titulares del IMV** [S], el **11,8 % de los beneficiarios de paro** [P, 2024] y el **7,9 % de las pensiones no contributivas** [S, 2024], frente al **14,9 % de la población** [P, 2026].
4. **Lo que no existe:** no hay partida de enfermedades raras, ni becas por nacionalidad en lo publicado que se ha leído, ni estadísticas de prestaciones por «hijos de inmigrantes». No se ha estimado nada de esto.

## Parte A · Presupuesto

### Vigencia
- PGE de 2023 prorrogados: [respuesta del Gobierno al Congreso, 2026](https://www.congreso.es/l15p/e12/e_0120891_n_000.pdf) y [criterios de la prórroga para 2026](https://www.hacienda.gob.es/es-es/prensa/noticias/noticiaspdf//426.pdf) [P].
- Techo de gasto para 2027: 226.032 M€, aprobado el 7-jul-2026 ([Hacienda](https://www.hacienda.gob.es/es-es/prensa/noticias/paginas/2026/20260707-np-cm-techo-gastos-2027.aspx)). **[VERIFICAR]** No he encontrado que se haya presentado un proyecto de PGE a 30-oct-2026.

### Por ministerio (M€, [IGAE, cierre de 2025](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/BOE%2012-25.pdf)) [P]
| Ministerio | Inicial | Definitivo | Obligaciones |
|---|---:|---:|---:|
| Inclusión, Seguridad Social y Migraciones | 45.613,6 | 55.100,0 | 54.800,7 |
| Defensa | 12.827,2 | 19.131,2 | 18.806,1 |
| Transportes | 11.450,6 | 12.808,0 | 11.506,1 |
| Interior | 10.259,3 | 11.838,7 | 11.144,4 |
| Industria y Turismo | 8.422,3 | 11.967,7 | 9.976,0 |
| Hacienda | 19.238,0 | 17.767,8 | 9.219,2 |
| Transición Ecológica | 11.302,1 | 10.991,3 | 8.974,3 |
| Transformación Digital y Función Pública | 5.476,3 | 7.027,9 | 6.394,2 |
| Derechos Sociales, Consumo y Agenda 2030 | 4.241,1 | 5.423,1 | 5.329,4 |
| Economía, Comercio y Empresa | 2.511,8 | 15.963,7 | 5.021,6 |
| Vivienda y Agenda Urbana | 3.484,5 | 4.989,7 | 4.781,0 |
| Educación, FP y Deportes | 6.730,8 | 5.807,1 | 4.725,3 |
| Ciencia, Innovación y Universidades | 7.448,3 | 7.090,8 | 4.684,0 |
| Presidencia, Justicia y Relaciones con las Cortes | 2.487,2 | 2.873,1 | 2.790,9 |
| Política Territorial y Memoria Democrática | 411,4 | 2.462,5 | 2.259,5 |
| Asuntos Exteriores, UE y Cooperación | 1.941,2 | 2.092,8 | 1.818,9 |
| Agricultura, Pesca y Alimentación | 1.079,9 | 1.699,2 | 1.565,8 |
| Sanidad | 1.272,0 | 1.460,6 | 1.235,1 |
| Cultura | 1.043,4 | 1.130,5 | 1.038,9 |
| Trabajo y Economía Social | 476,8 | 858,3 | 636,4 |
| Igualdad | 502,9 | 501,5 | 481,3 |
| Juventud e Infancia | 161,4 | 410,5 | 296,5 |

Fuera de los ministerios: deuda 156.336 M€ (solo 34.822 M€ son intereses), sistemas de financiación de CCAA y entes locales 54.825 M€, pensiones de clases pasivas 23.509 M€ y aportación a la UE 17.165 M€. El detalle hasta agosto de 2026 está en el JSON.

### Estado, Seguridad Social y CCAA (Eurostat, 2024, M€) [P]
Las columnas no están consolidadas: una transferencia entre administraciones cuenta en las dos, así que no suman el total.

| Función | Total AAPP | Estado | CCAA | Local | Seg. Social |
|---|---:|---:|---:|---:|---:|
| Gasto total | 725.001 | 357.732 | 268.013 | 97.105 | 252.803 |
| Sanidad | 102.942 | 3.585 | 96.501 | 883 | 1.973 |
| Educación | 65.862 | 2.665 | 59.766 | 3.419 | 12 |
| Protección social | 297.532 | 29.545 | 19.119 | 10.037 | 238.831 |
| Defensa | 14.233 | 14.233 | 0 | 0 | 0 |

Por eso comparar ministerios engaña en sanidad y educación: Sanidad obligó 1.235 M€, y las CCAA gestionan cerca del 94 % de la sanidad pública.

### Programas pedidos (M€, 2025) [P]
| Programa | Código | Inicial | Definitivo | Obligaciones | Definitivo 2026 | Hasta ago-2026 |
|---|---|---:|---:|---:|---:|---:|
| Violencia de género (Pacto y Delegación) | 232C | 259,7 | 294,4 | 293,5 | 303,6 | 12,8 |
| Igualdad de oportunidades | 232B | 204,1 | 167,4 | 151,8 | 158,4 | 27,8 |
| Aportación al IMV | 32.02.000X.424 | 3.096,9 | 4.955,9 | 4.955,9 | 5.641,7 | 4.231,2 |
| Aportación a pensiones no contributivas | 32.02.000X.42002 | 3.003,0 | 3.772,5 | 3.772,5 | 4.218,5 | 3.163,9 |
| Dependencia (cinco partidas, suma propia) | 29.03.000X | 3.522,3 | 4.108,8 | 4.108,8 | 5.875,2 | 2.348,2 |
| Becas y ayudas | 323M | 2.550,8 | 2.658,4 | 2.655,9 | 2.625,8 | 1.107,3 |
| Acciones a favor de inmigrantes | 231H | 745,4 | 1.393,9 | 1.257,6 | 1.211,9 | 739,6 |
| Sistema de acogida, Plan de Recuperación | 23VE | 0,0 | 126,5 | 16,7 | — | — |
| Asilo y apátridas (Interior) | 131P | 16,2 | 18,1 | 14,8 | 20,0 | 9,3 |
| Cooperación para el desarrollo | 143A | 300,1 | 303,6 | 73,8 | 301,8 | 29,9 |
| Ayudas a rehabilitación y acceso a vivienda | 261N | 959,5 | 1.004,2 | 913,9 | 1.361,2 | 1.090,8 |
| Línea ICO de vivienda social (préstamos) | 26BG | — | 3.300,0 | 3.300,0 | — | — |
| Innovación en defensa (en Industria) | 464B | 1.601,2 | 5.710,6 | 5.544,9 | — | — |

- **Pacto de Estado 2026 [P]:** 160 M€ a CCAA, Ceuta y Melilla ([BOE, 29-abr-2026](https://boe.es/boe/dias/2026/04/29/pdfs/BOE-A-2026-9355.pdf)) y 40 M€ a entes locales ([BOE, 25-jul-2026](https://www.boe.es/boe/dias/2026/07/25/pdfs/BOE-A-2026-16237.pdf)).
- **Inmigración [P]:** las partidas mayores de 231H en 2025 son el concierto social de atención humanitaria y protección internacional (829,6 M€) y las declaraciones de emergencia (277,3 M€). El crédito inicial casi se duplica durante el año.
- **Cooperación:** 143A no es toda la ayuda al desarrollo. La AOD de 2025 supera los 4.550 M€ ([Exteriores](https://www.exteriores.gob.es/en/Comunicacion/NotasPrensa/Paginas/2026_NOTAS_P/La-Ayuda-Oficial-al-Desarrollo-espa%C3%B1ola-alcanza-su-mayor-cifra-de-los-ultimos-15-a%C3%B1os.aspx)) [S].
- **Defensa:** la sección obligó 18.806 M€, y otros 5.545 M€ de innovación en defensa están en Industria. Con pagos efectivos, esa partida de Industria se queda en 2.468,5 M€.

### Enfermedades raras: qué se puede y qué no se puede aislar
- **No se puede:** no hay partida propia ni he encontrado desglose por enfermedad del gasto asistencial, que corresponde a las CCAA, ni una cifra agregada de medicamentos huérfanos.
- **Sí se puede, solo en investigación [P]:** 482 proyectos y 99,88 M€ en 2020-2023 ([respuesta del Gobierno](https://www.congreso.es/l15p/e3/e_0037467_n_000.pdf)).
- **Contexto, no comparable:** Ciencia transfirió 147,1 M€ al ISCIII en 2025, que cubre mucho más que enfermedades raras. **[VERIFICAR]** el importe anual del CIBERER.

### Violencia de género: casos frente a gasto
| Dato (2025) | Valor | Fuente |
|---|---:|---|
| Denuncias | 204.342 (+2,64 %) | [CGPJ](https://www.poderjudicial.es/cgpj/es/Poder-Judicial/En-Portada/Los-organos-judiciales-con-competencias-en-violencia-sobre-la-mujer-recibieron-en-2025-un-total-de-204-342-denuncias--de-las-que-el-71-61---fueron-presentadas-por-mujeres-victimas) [P] |
| Mujeres víctimas en denuncias | 185.188 | CGPJ [P] |
| Órdenes de protección solicitadas / acordadas | 47.944 / 32.840 (68,4 %) | CGPJ [P] |
| Sentencias / condenatorias | 60.942 / 82,36 % | CGPJ [P] |
| Víctimas con medidas u orden de protección | 33.373 (−3,8 %) | [INE](https://www.ine.es/dyngs/Prensa/EVDVG2025.htm) [P] |
| Feminicidios en pareja o expareja | 48 | [Delegación](https://violenciagenero.igualdad.gob.es/wp-content/uploads/Principales_datos_Diciembre_2025.pdf) [P] |
| Programa 232C por denuncia | 1.436 € (cálculo propio) | IGAE y CGPJ |

- La prensa de enero citó 46 feminicidios en 2025; el dato oficial de diciembre, ya actualizado, es 48. En 2026: 26 hasta junio ([Delegación](https://violenciagenero.igualdad.gob.es/wp-content/uploads/Principales_datos_Junio_2026.pdf)) [P] y 43 hasta el 24-oct ([prensa](https://www.moncloa.com/2026/10/24/mujeres-asesinadas-madrid-3453844/)) [S].
- CGPJ e INE no se contradicen: el INE solo cuenta asuntos con medidas cautelares u orden de protección.
- Desde octubre de 2025 los juzgados asumen también violencia sexual fuera de la pareja (3.272 denuncias en el trimestre), así que la serie no es del todo comparable.
- Los 1.436 € no son el coste por caso: 232C excluye Justicia, Interior y CCAA. **No existe una cifra única publicada del gasto total.**
- **[VERIFICAR]** el número de juzgados especializados. Prensa: 50 plazas nuevas en 2025, +42 % [S].

## Parte B · Quién recibe

### Denominadores
| Población | Valor | Peso | Fecha |
|---|---:|---:|---|
| Total | 49.801.559 | 100 % | [1-jul-2026, INE](https://www.ine.es/dyngs/Prensa/ECP2T26.htm), provisional [P] |
| Nacionalidad extranjera | 7.437.543 | 14,9 % | ídem |
| Nacidos en el extranjero | 10.291.807 | 20,7 % | ídem; incluye 3.370.854 españoles |
| Afiliados extranjeros | 3.038.158 | 14,1 % de los cotizantes | [ene-2026, Inclusión](https://www.inclusion.gob.es/en/w/la-seguridad-social-comienza-2026-con-cerca-de-200.000-afiliados-extranjeros-mas-que-hace-un-ano) [P] |

Riesgo de pobreza de adultos en 2025 ([Eurostat](https://ec.europa.eu/eurostat/databrowser/view/ilc_li31)) [P]: nacionales 14,3 %, extranjeros 39,6 %, de fuera de la UE 44,6 %. Es el denominador útil para prestaciones condicionadas a la renta.

### Beneficiarios
| Prestación | Total | Extranjeros | Requisito legal |
|---|---|---|---|
| **IMV** | 862.859 hogares y 2.631.545 personas; 538,7 €/mes por hogar; nómina de 500,2 M€ ([may-2026](https://www.inclusion.gob.es/documents/20121/0/20260508+NP+IMV+mayo.pdf/1401a0ee-6432-df57-9af8-d0e20947fc67?t=1780642280852)) [P] | ~17 % de los **titulares**, 16-17 % desde 2020 ([Maldita, datos de la Seguridad Social](https://maldita.es/prebunking/20260710/ingreso-minimo-vital-espa%C3%B1oles-extranjeros/)) [S] | 1 año de residencia legal y continuada, con excepciones ([art. 10, Ley 19/2021](https://www.boe.es/buscar/act.php?id=BOE-A-2021-21007)) |
| **Paro** | 1.857.263 ([jul-2026, Funcas](https://www.funcas.es/wp-content/uploads/2026/09/Afiliados-y-parados_2608.pdf)) [S] | 214.524 de media en 2024, **11,8 %** ([Anuario PEX](https://www.mites.gob.es/ficheros/ministerio/estadisticas/anuarios/2024/PEX/PEX_24.pdf)) [P] | Residentes, mismas condiciones que los españoles ([art. 14, LO 4/2000](https://www.boe.es/buscar/act.php?id=BOE-A-2000-544)) |
| **Pensión no contributiva** | 462.568 en dic-2025 ([Imserso](https://imserso.es/documents/20123/12025099/iai2025_cap2.pdf/ee39f373-3bc2-feaf-ff63-a62e75c1c9f8)) [P] | 36.447 en dic-2024, **7,91 %**; jubilación 10,97 % ([Maldita, citando al Imserso](https://maldita.es/malditobulo/20230424/no-no-pagamos-pensiones-a-mas-de-100-000-inmigrantes-que-jamas-cotizaron/)) [S] | Jubilación: 10 años de residencia. Invalidez: 5 años ([arts. 369 y 363 LGSS](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724)) |
| **Becas** | 3.079.706 y 3.991,6 M€; Ministerios 2.565,3 M€ ([curso 2024-25](https://www.educacionfpydeportes.gob.es/dam/jcr:fde16783-9b97-4170-9553-3f3074ed5d38/2024-25resumen.pdf)) [P] | **[VERIFICAR]** No aparece en el resumen ni en el informe metodológico | Español; UE, residente permanente o trabajador; resto, ley de extranjería ([art. 4, RD 1721/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2008-821)) |

- **IMV:** por comunidad y tipo de hogar hay [tabla del INSS](https://www.inclusion.gob.es/documents/20121/0/202605_IMV+-+N%C3%B3mina.xlsx/a1fa35e2-cc77-794a-8705-b0011640c4bb?t=1780642315271): Andalucía tiene 268.568 hogares; 590.959 hogares con menores y 144.540 monoparentales en total. La nacionalidad solo se conoce de los titulares, no de todos los beneficiarios.
- **Paro:** por país, Marruecos 42.368, Colombia 11.355 y Venezuela 7.668. Los extranjeros son el 16,2 % del nivel contributivo y el 8,4 % del subsidio. El anuario de 2025 no estaba en la ruta esperada. Prensa: 77.877 extranjeros con subsidio en 2025 ([Vozpópuli](https://www.vozpopuli.com/economia/record-de-parados-extranjeros-con-subsidio-los-beneficiarios-se-disparan-un-24.html), sin abrir) [S].
- **Afiliación:** 3.359.548 extranjeros en mayo de 2026 ([Junta de Extremadura](https://www.juntaex.es/documents/77055/46718143/AFEXSS_ND_2026_05.pdf/0e4b55e4-ec03-e845-2adc-a39c6f29332e)) [S]; la regularización influye en la subida ([Funcas](https://www.funcas.es/wp-content/uploads/2026/09/Afiliados-y-parados_2608.pdf)) [S].
- **[VERIFICAR]:** lo cotizado por extranjeros en euros y la dependencia por nacionalidad. No he encontrado cifra oficial de ninguna de las dos, y no las estimo.

### Origen e «hijos de inmigrantes»
- **Lo que no se puede cruzar:** los registros de prestaciones publican nacionalidad, no ascendencia. Un español naturalizado o hijo de inmigrantes cuenta como español. No se infiere por apellido ni por origen supuesto.
- **EPA [S]:** pregunta el país de nacimiento de los padres desde 2021 ([Funcas](https://www.funcas.es/wp-content/uploads/2025/09/Miyar_PS41.pdf)). Sirve para estudiar empleo, no quién cobra cada prestación.
- **ECV [S]:** el [módulo de 2019](https://ine.es/normativa/leyes/cse/cambio_meto_modulo_transmision_pobreza.pdf) incluye país de nacimiento y nacionalidad de los padres. Es una muestra. **[VERIFICAR]** si sigue en el módulo de 2023.
- **Censo [VERIFICAR]:** el encargo lo citaba como fuente, pero no he podido confirmar que publique este dato.

## Opinión [OPINIÓN]
- **Tamaño frente a eficacia:** Igualdad es el 0,11 % de las obligaciones del Estado. Eso mide cuánto se gasta, no si funciona: no he leído una evaluación que atribuya resultados al programa.
- **Prórroga:** a favor, las ampliaciones cubren compromisos reales como pensiones e IMV. En contra, con créditos de 2023 las Cortes no votan cambios de esta escala (Defensa +6.304 M€, Inclusión +9.486 M€ en 2025).
- **Peso de los extranjeros:** en el IMV están algo por encima de su peso en la población, pero con un riesgo de pobreza casi tres veces mayor. En paro están por debajo de su peso entre los cotizantes, comparando fechas distintas. La lectura cambia según el denominador, por eso van siempre juntos.
- **A vigilar [ESPECULACIÓN]:** el IMV exige un año de residencia, así que la regularización de 2026 aún no puede verse en sus datos.

## Sesgos de las fuentes
- **Maldita:** verificador con datos oficiales, pero publica para desmentir bulos. Sus cifras de IMV y pensiones no contributivas quedan en [S] hasta abrir las tablas originales.
- **Notas del Gobierno y CGPJ:** cifras oficiales, con titulares que eligen el ángulo («máximo histórico», «cifra más elevada»).
- **Vozpópuli:** titular orientado («récord de parados extranjeros»); la cifra no se ha contrastado.

## Pendiente de verificar
Proyecto de PGE 2027 · CIBERER · coste de CATE y CETI · juzgados especializados · tablas originales de nacionalidad del IMV y de pensiones no contributivas · anuario de paro de 2025 · becas por nacionalidad · ascendencia en ECV 2023 y Censo · cotizaciones por nacionalidad.
