# C239 · España: investigaciones y fondos públicos (Adif, Transportes, fondos UE, accidentes) — tercera pasada (12-nov-2026)

Bloque S1 de `research/LANZAR-FABLE-ESPANA.md`. Continúa `2026-11-09-C239-inventario.md` y `2026-11-10-C239-fichas.md`. Modelo: Fable 5.2. Lecturas del 12-nov-2026 (~11:50 UTC).

**Presunción de inocencia:** que un órgano investigue no significa que nadie sea culpable. Aquí solo consta quién investiga, qué, en qué fase y con qué fecha. [P] = fuente oficial leída hoy; [S] = prensa o resumen de buscador; [VERIFICAR] = no leído. M€ = millones de euros.

## Qué cambia respecto al 10-nov
- Las 10 fichas **ya estaban** en `explorador/espana-judicial.json` (caso `adif-transportes-fondos-ue`); la fila de tareas decía que faltaba pasarlas y estaba desfasada.
- Hoy se añaden **4 hechos de fuente oficial** que antes eran prensa o no constaban, y se reescribe la lista de pendientes del caso.
- La web del CIAF, que daba 403 al script, **abre en el navegador integrado**: no hizo falta Chrome.

## HECHOS

### Fiscalía Europea (EPPO) [P, eppo.europa.eu vía buscador limitado al dominio, 12-nov]
- Siguen constando dos investigaciones: 20-mar-2026 (mantenimiento del tramo de Adamuz) y 6-nov-2026 (seguridad, señalización y comunicaciones de la línea Madrid-Sevilla, de oficio, con la UCO y diligencias en Adif, la Agencia Estatal de Seguridad Ferroviaria y el Tribunal de Cuentas).
- **Sin novedades posteriores al 6-nov.** Los comunicados no dan importes, personas, empresas ni expedientes de contratación, y dicen que no se harán públicos más detalles por ahora.

### Accidente de Adamuz (18-ene-2026)
- [P, Poder Judicial, nota del 22-ene-2026] Identificadas **43 personas fallecidas**, «todas las encontradas hasta el momento»; 43 autopsias; 45 denuncias de desaparición. En el levantamiento: 28 en el Alvia Madrid-Huelva, 6 en sus vías, 6 en el Iryo Málaga-Madrid y 3 entre ambos trenes.
- [VERIFICAR] Cifra final: el titular de otra nota del Poder Judicial habla de 45 cuerpos; no se leyó.
- [P, CIAF, página leída hoy] Expediente 08/2026. Documentos: nota inicial (20-ene), actualizaciones del 23-ene, 12-feb, 27-feb y 10-mar-2026 y **recomendación previa de seguridad del 5-nov-2026**. Sin informe final.
- [S, resumen de buscador] La instrucción está en la Sección Civil y de Instrucción del Tribunal de Instancia de Montoro. Investigados: no constan en ninguna nota leída.

### Accidente de Urda (28-oct-2026)
- [P, TSJ de Castilla-La Mancha, 28-oct-2026] La investigación judicial corresponde a la **Sección Civil y de Instrucción del Tribunal de Instancia de Orgaz, plaza número 2**. Se activa el protocolo de víctimas múltiples (RD 32/2009), con magistrado coordinador y cinco equipos judiciales y forenses. La nota **no da número de fallecidos ni de investigados**.
- [P, TSJ de Castilla-La Mancha, 30-oct-2026] Refuerzo propuesto para que la jueza titular se dedique en exclusiva a esta causa.
- [S, resumen de buscador sobre otra nota del Poder Judicial, sin leer] Secreto de sumario, custodia de las cajas negras por la Policía Judicial y prohibición de acceso a 2 km de vía. [VERIFICAR].
- [P, CIAF, página leída hoy] Expediente 146/2026. Documentos: nota del accidente (29-oct), versión en inglés y corrección (1-nov) y **recomendación previa de seguridad del 7-nov-2026**. Sin informe final.
- Número de fallecidos (la prensa daba entre 64 y 69): sigue en [VERIFICAR]; ninguna nota oficial leída lo dice.

### OLAF [P, anti-fraud.ec.europa.eu vía buscador, 12-nov]
- Ningún resultado sobre Adif. Esto **no prueba** que no haya investigación: la OLAF no suele anunciar las que tiene en curso.

### Vínculo con contratos (añadido de S1)
- **Sin vincular.** Ningún comunicado oficial identifica un expediente de PLACSP ni un contrato. Las cifras de prensa del 10-nov (111 M€, 131,14 M€, 48 M€) siguen sin poder atribuirse a las investigaciones.

## OPINIONES (mías)
- Más grave: dos investigaciones europeas en ocho meses sobre la misma línea y dos recomendaciones previas del CIAF en la misma semana (5 y 7-nov) son señales poco habituales. Su contenido no se ha leído.
- Menos grave: sigue sin haber importes, personas ni contratos señalados por ninguna fuente oficial, y el Tribunal de Cuentas calificó los sistemas de gestión de «adecuados» (dic-2025).
- El vínculo entre los fondos investigados y la causa de los accidentes es [ESPECULACIÓN]: ninguna fuente oficial lo afirma.
- Sesgo: la prensa sobre este asunto está muy polarizada; solo sirve para localizar la nota oficial.

## Corrección de cifras frente a fichas anteriores
- JUD-2 decía «Juzgado de Instrucción n.º 2 de Orgaz» [S]; el nombre oficial es Sección Civil y de Instrucción del Tribunal de Instancia de Orgaz, plaza número 2 [P].
- La nota del TSJ sobre Urda lleva fecha 28-oct-2026 (día del accidente); la ficha del 10-nov fechaba la apertura el 29-oct.

## Pendiente
1. Leer los PDF del CIAF (recomendaciones previas de 137 KB y 125 KB y notas): **requiere tu OK de descarga**.
2. Fallecidos de Urda y cifra final de Adamuz en nota oficial.
3. Autos de la Audiencia Nacional (otra causa); informe completo del Tribunal de Cuentas; BOE de ceses.
4. Vigilar eppo.europa.eu: si nombra contratos, enlazar entonces con PLACSP.

## Lecciones (máx. 5)
1. Antes de trabajar una fila «en parte», comprobar el JSON: lo que «faltaba» ya estaba hecho.
2. Un 403 al script no es un bloqueo: la misma página abre en el navegador integrado.
3. El buscador limitado al dominio oficial localiza la nota; el nivel P solo llega al leerla entera.
4. En lo judicial, anotar también lo que la nota **no** dice (investigados, cifras) evita rellenarlo con prensa.

## Seguridad
Sin claves ni secretos. Sin descargas de archivos. Sin API de Anthropic ni workflows. Sin commit ni push. Tocados: `explorador/espana-judicial.json` (un caso), `research/MAPA-DE-FUENTES.md` (filas nuevas) y `research/tareas.csv`.

## Fuentes
- Fiscalía Europea: https://www.eppo.europa.eu/media/news/spain-eppo-launches-second-investigation-possible-fraud-involving-eu-funds-maintenance-madrid-2026-11-06_en
- CIAF Adamuz: https://www.transportes.gob.es/organos-colegiados/ciaf/investigaciones-en-curso/adamuz
- CIAF Urda: https://www.transportes.gob.es/organos-colegiados/ciaf/investigaciones-en-curso/urda
- Poder Judicial, Adamuz (22-ene-2026): https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Sala-de-Prensa/Archivo-de-notas-de-prensa/El-servicio-de-criminalistica-de-la-Guardia-Civil-finaliza-las-identificaciones-de-todos-los-cuerpos-recibidos-tras-el-accidente-de-Adamuz
- TSJ de Castilla-La Mancha, Urda (28-oct-2026): https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunales-Superiores-de-Justicia/TSJ-Castilla-La-Mancha/En-Portada/Informacion-sobre-las-actuaciones-judiciales-relacionadas-con-el-accidente-ferroviario-ocurrido-en-Urda--Toledo-
- TSJ de Castilla-La Mancha, refuerzo (30-oct-2026): https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunales-Superiores-de-Justicia/TSJ-Castilla-La-Mancha/Oficina-de-Comunicacion/Notas-de-prensa/La-Sala-de-Gobierno-del-TSJCLM-acuerda-la-ampliacion-de-las-medidas-de-refuerzo-para-el-Tribunal-de-Instancia-de-Orgaz-que-investiga-el-accidente-ferroviario-de-Urda--Toledo-
- OLAF: https://anti-fraud.ec.europa.eu/

## Añadido el 12-nov (tarde): las dos recomendaciones previas, leídas enteras
Con el OK de Joel. El servidor devuelve 403 a la descarga por script y no se insistió; los PDF se leyeron **dentro del navegador integrado**, sin guardar ningún archivo en disco. Nivel [P]. Son documentos de un órgano técnico: **son preventivos, no fijan causas ni responsabilidades** (lo dicen expresamente los dos).

### Adamuz · recomendación previa 08/2026-1 (firmada el 28-oct-2026; publicada el 5-nov-2026; 5 páginas)
- **Qué pasó según la investigación técnica:** el Iryo 6189 (Málaga-Madrid) descarriló tras una **rotura franca de carril** junto a los cambios de la estación de Adamuz; parte del tren invadió la vía contigua y chocó con el Alvia 2384 (Madrid-Huelva).
- **La rotura no se detectó durante unas 22 horas:** los registros de mantenimiento muestran una caída de tensión en el circuito de vía a las 21:47 del 17-ene-2026, tras el paso de un tren; hasta el accidente pasaron **47 circulaciones** por el punto. Varios trenes tienen marcas de golpes compatibles.
- **Causa de la rotura: sin determinar** (muestras de carril pendientes de laboratorio).
- **Circuitos de vía:** los originales (finales de los años 80) se sustituyeron en **2024** por otros nuevos; los ensayos previos confirmaron que no podían garantizar la detección de una rotura, y la sustitución «no resolvió la limitación».
- **Matriz de riesgos del proyecto de 2024:** el riesgo de no detectar una rotura figuraba con severidad «catastrófico», frecuencia «ocasional» y aceptación «intolerable», pero su mitigación **no formaba parte del alcance del proyecto**; Adif-AV lo consideraba mitigado con inspecciones y auscultaciones, que el documento califica de necesarias pero no suficientes.
- **Dato de Adif citado:** desde 2017, **44 roturas francas** en la red de alta velocidad: 18 (41 %) detectadas por circuitos de vía, 17 (39 %) por personal y 9 (20 %) por maquinistas.
- **Recomendación** (a la Agencia Estatal de Seguridad Ferroviaria; ejecutor Adif-AV): implantar medidas que detecten roturas francas antes del paso del siguiente tren.

### Urda · recomendaciones previas 146/2026-1, 2 y 3 (firmadas el 6-nov-2026; publicadas el 7-nov-2026; 3 páginas)
- **Qué pasó:** el 28-oct-2026 a las 8:53, **colisión por alcance** en el punto kilométrico 118+800 de la línea Madrid-Sevilla entre el Iryo 6076, detenido ante la señal de entrada de Urda, y el AVE 2080 de Renfe. «Numerosas víctimas mortales y heridos»: **el documento no da cifra**.
- **Antes del choque:** a las 8:31 hubo una pérdida de transmisión del sistema de seguridad de la línea (LZB) y se pasó al sistema de respaldo (bloqueo de señalización lateral). El centro de regulación y los maquinistas se comunicaron por telefonemas.
- **Recomendaciones:** (1) marcha a la vista provisional al reanudar la circulación tras ese cambio de sistema; (2) revisar los protocolos de los centros de regulación; (3) evaluar los riesgos de la transición entre sistemas.

### Cruces con lo que ya había (cálculo y lectura propios)
- Cuadra con la nota del Poder Judicial del 22-ene: víctimas en un Alvia Madrid-Huelva y un Iryo Málaga-Madrid.
- La recomendación de Adamuz lleva fecha del **28-oct-2026, el mismo día del accidente de Urda**, y se publicó el 5-nov.
- Los dos accidentes son en la misma línea (Madrid-Sevilla) pero de naturaleza distinta según estos documentos: vía en Adamuz, operación con el sistema de respaldo en Urda.

### OPINIÓN (mía) y límites
- La segunda investigación de la Fiscalía Europea (6-nov) trata de fondos para «seguridad, señalización y comunicaciones» de esta línea, y la recomendación de Adamuz describe un proyecto de señalización de 2024 en ella. **Ninguna fuente oficial dice que sea ese el proyecto investigado**: relacionarlos es [ESPECULACIÓN]. Sirve solo como pista para buscar el expediente en PLACSP.
- Que un riesgo figurase como «intolerable» y quedase fuera del alcance de un proyecto es un hecho documental; si hubo o no responsabilidad de alguien lo decidirán la investigación técnica final y los juzgados.
- El encabezado del documento es de la «Autoridad Administrativa Independiente para la Investigación Técnica de Accidentes e Incidentes ferroviarios, marítimos y de aviación civil» (Ley 2/2024); la web sigue llamándola CIAF. [VERIFICAR] el nombre vigente.
- Sin leer: las notas intermedias de Adamuz y la nota de Urda del 29-oct (puede traer la cifra de víctimas).

Fuentes: [recomendación de Adamuz](https://www.transportes.gob.es/recursos_mfom/paginabasica/recursos/recomendacion-previa-adamuz.pdf) · [recomendaciones de Urda](https://www.transportes.gob.es/recursos_mfom/recomendacion_previa_informe_de_urda.pdf)

## Añadido el 12-nov (2): nota oficial de Urda a las 24 horas
Con el OK de Joel; leída entera en el navegador, sin guardar archivo. Nota de la AITAT publicada el 29-oct-2026 (5 páginas). Nivel [P]. La propia nota advierte de que no contiene conclusiones y de que el órgano no determina culpas.

- **Víctimas:** **69 fallecidos y más de 200 heridos** «al momento de redacción»; cifras **no definitivas**. Cierra el [VERIFICAR] de la prensa (64-69) con dato oficial provisional.
- **Trenes:** Iryo 6076 Madrid-Sevilla, 147 viajeros y 5 tripulantes; AVE 2080 Madrid-Sevilla, 379 viajeros y 7 tripulantes. En total 538 personas a bordo (suma propia).
- **Colisión:** a las 8:53 en el punto kilométrico 118+800, vía 2; el Iryo estaba detenido ante la señal de entrada y fue alcanzado por detrás a una velocidad **estimada entre 160 y 200 km/h**, pendiente de los registradores.
- **Antes:** avería del sistema LZB desde las 8:31; circulación con el sistema de respaldo; instrucciones por telefonemas. Frase literal: la cadena de averías, instrucciones y acciones «eventualmente habrían conducido a la colisión, sin que hubiesen actuado las barreras mitigadoras necesarias». **Todas las hipótesis siguen abiertas.**
- **Investigación:** registradores bajo custodia de la Guardia Civil; el volcado se hará según disponga el Tribunal de Instancia de Orgaz, plaza 2. A la fecha de la nota no se había entrevistado a maquinistas ni a responsables de circulación. Plazo orientativo del informe final: un año.
- **Nombre del órgano:** la nota confirma que es la AITAT (Ley 2/2024); la web mantiene la ruta «ciaf».
- Cuadra con la recomendación previa del 6-nov (hora, punto kilométrico, trenes y secuencia de la avería).

Fuente: [nota de Urda a las 24 horas](https://www.transportes.gob.es/recursos_mfom/nota-accidente-urda-24h.pdf)
