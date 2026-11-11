# C243 · Empresas públicas y comparador de CCAA (10-nov-2026)

Estado: **en parte**. Salida: `explorador/espana-empresas.json` (generado por `scripts/leer_espana_empresas.py`, sin IA) y 2 bloques nuevos en España (Explorador › vistas).

## Hechos (con fuente)
- **Grupo SEPI 2025**: cifra de negocio 7.384 M€, resultado neto 130 M€, inversiones 529 M€, ≈87.000 profesionales; Grupo Correos = 28 % de la cifra de negocio. Fuente: nota de SEPI de 30-jun-2026 sobre las cuentas anuales aprobadas (nivel P por ser la propia entidad; no auditado aquí). Deuda y aportaciones del Estado: no leídas.
- **Aena 2025**: «ingresos totales» 6.379,2 M€ y EBITDA 3.785 M€ (web de inversores, sin fecha del documento). Resultado, deuda y plantilla: no leídos.
- **Ineco**: su web dice que no ha requerido deuda financiera; las cuentas 2025 y el detalle de subvenciones están en PDF de abril 2026 que no pude leer (sin librería PDF local).
- **Comparador de CCAA** (17 comunidades; Ceuta y Melilla excluidas): paro EPA 2T 2026 (INE, tabla 65334; de 4,63 % Baleares a 14,91 % Andalucía), población 1-ene-2025 (INE, tabla 56941) y deuda PDE 2T 2026 (Banco de España, ya cargada en paneles). Deuda por habitante calculada aquí: mezcla periodos distintos (deuda 2T 2026 / población enero 2025), orden de magnitud correcto, no cifra oficial.

## Sin leer [VERIFICAR]
Adif y Adif AV (adif.es da 403 a scripts), Renfe, Correos (cifra propia), Enaire (web vacía), deuda y aportaciones del Estado de todas, subvenciones en BDNS y contratos (dependen de C241), renta y precio de vivienda por CCAA, vínculo con las investigaciones de S1. No probé Chrome para Adif/Renfe (siguiente paso).

## Opiniones / sesgos
- Las cifras vienen de notas y webs de las propias empresas (autopromoción; «récord» es adjetivo de la fuente). Un resultado bajo o negativo no implica mala gestión: Renfe/Adif tienen función de servicio público.
- [ESPECULACIÓN] ninguna incluida. No se vincula ninguna empresa con investigaciones: no hay base para conclusiones de culpabilidad.

## Lecciones
1. Los sitios de Adif/Enaire bloquean o sirven páginas vacías a scripts: ir directo a Chrome o al Registro Mercantil.
2. Faltan herramientas para leer PDF local: valorar instalar `pypdf` (con OK de Joel).
3. La API Tempus del INE da CCAA fácilmente (tablas 65334 y 56941).
4. Los nombres de CCAA difieren entre INE y Banco de España: hay mapa en el script.

## Segunda pasada (10-nov, tarde)
- **Navantia 2025 (nivel P, nota en sepi.es, 3-jul-2026)**: cifra de negocio consolidada 1.978 M€, resultado consolidado -149 M€ (individual -119 M€), 6.761 personas, cartera 12.826 M€. Motivo de la pérdida no leído [VERIFICAR].
- **Correos 2025 (nivel S, prensa 3-mar-2026)**: 1.658 M€ de cifra de negocio sin ingresos electorales, beneficio 14,4 M€, EBITDA 76 M€. Que lo sostenga la compensación del servicio postal universal (>400 M€/año) es opinión de CCOO, no hecho leído.
- **Renfe 2025 (nivel S, prensa)**: beneficio 60,2 M€, EBITDA 528,6 M€, billetes ≈2.000 M€. Las fuentes discrepan en Renfe Viajeros.
- **Adif/Adif AV (S)**: deuda de Adif AV >21.300 M€ y pérdidas 193,4 M€ por prensa con ejercicio dudoso; CNMC: inversión 5.230 M€ en 2025 (extracto). Cuentas no leídas: adif.es da 403 a scripts y 404 en las rutas probadas con Chrome.
- **Enaire**: PDF oficiales 2025 localizados (cuentas, informe de gestión, deuda) pero ilegibles para las herramientas; solo coste medio de deuda 2,21 % y vida media 6,09 años (extracto). **Paradores** (error de certificado) e **Indra** (conexión rechazada): sin cifras.
- Deuda y aportaciones del Estado: siguen sin leerse en ninguna empresa (necesitan los PDF de cuentas con capa de texto o el OK de Joel para descargarlos e instalar `pypdf`, o IGAE/SEPI).
- Lección añadida: las cuentas de Enaire/Ineco están en PDF; sin lector de PDF local la vía oficial queda cerrada.

## Tercera pasada: aportaciones del Estado (solo extractos, nivel S/[VERIFICAR])
- **Adif**: la adenda al convenio 2021-2025 prevé 1.384,2 M€ de la AGE en 2026 (1.011,7 M€ MRR + 372,5 M€ otras). Visto solo como extracto de búsqueda de nota de Hacienda/BOE: no leído entero.
- **Renfe**: PGE prorrogados con 1.009 M€ de compensación por obligaciones de servicio público (previsto, no ejecutado); crédito extraordinario autorizado de hasta 671 M€ en 2026; Transportes pagó 307,8 M€ de ayudas al servicio de Renfe en 2025. El Tribunal de Cuentas fiscalizó estas ayudas (2022-2023; BOE 9-jun-2026): sin leer.
- **Correos, Enaire, Navantia**: no se localizó ninguna cifra de aportaciones; Correos solo con la cifra de CCOO/prensa (>400 M€/año del servicio postal universal) = [S/opinión]. La deuda por empresa sigue sin leer; falta IGAE (sector público empresarial) y las memorias de los PGE (PDF).

## Cuarta pasada con Chrome (10-nov): qué se leyó entero y qué no
- **Leído entero en Chrome (nivel P)**: nota de Hacienda del 9-dic-2025 (hacienda.gob.es). Aportaciones de la AGE para la prórroga 2026 del convenio 2021-2025: **Adif 219,77 M€** y **Adif Alta Velocidad 1.011,69 M€** (156,66 + 627,89 + 227,14 M€), solo la parte del Mecanismo de Recuperación (compromiso máximo de gasto, no ejecutado). **Corrección**: la cifra de 1.384,2 M€ (con 372,5 M€ «otras») de la pasada anterior venía de un extracto de búsqueda y no se ha podido confirmar; se retira.
- **Intentado y no posible**: PDF de Enaire (Deuda 2025, cuentas, informe de gestión): Chrome abre el visor de PDF y `get_page_text` no devuelve texto (ya anotado en ACCESOS-CHROME); las herramientas de lectura tampoco decodifican el PDF. Cuentas de Adif y Renfe, memorias de los PGE e IGAE: PDF o webs sin ruta localizada; no se leyeron.
- Sigue sin leerse la **deuda** de cada empresa. Hace falta descargar los PDF con OK de Joel y leerlos con una librería (`pypdf`) o con OCR.
- Lección: Chrome sí lee las notas HTML de Hacienda/Consejo de Ministros; no sirve para PDF.

## Pasada con PDF (10-nov, tarde): ENAIRE y Adif leídos [P]
Con el OK explícito de Joel («sí, descarga los PDF de C243») se bajaron a una carpeta temporal fuera del repo, se extrajo el texto con `pdftotext` y se borraron.
- **ENAIRE (cuentas individuales 2025, miles de €; 2025 frente a 2024):** total activo 5.561.763 (5.088.320); deudas a largo plazo 1.565.149 (1.941.672); deudas a corto plazo con entidades de crédito 708.678 (10.430); resultado 887.521 (606.890). De ese resultado, 737.020 son dividendos de Aena y 150.501 la operativa de ENAIRE: el beneficio individual es sobre todo el dividendo de la participada (sesgo a tener en cuenta al compararlo con otras empresas).
- **Grupo ENAIRE (informe de gestión, M€):** cifra de negocio 7.135,0 (+7,4 %) y EBITDA 4.132,7 (+9,4 %).
- **Adif y Adif Alta Velocidad (BOE 6-feb-2026, BOE-A-2026-2807 y -2808):** compromisos del Estado para 2026 por convenio: Adif 219,77 M€ (aportación patrimonial para amortizar deuda a largo plazo); Adif AV 1.011,69 M€ del Mecanismo de Recuperación y Resiliencia, 1.384,18 M€ en total de la AGE. Son importes comprometidos, no ejecutados.
- **Sin leer:** deuda y aportaciones ejecutadas de Renfe, Correos y Navantia; cuentas anuales 2025 de Adif. La búsqueda no devolvió sus PDF oficiales de 2025 (Renfe: solo prensa y el informe del Tribunal de Cuentas sobre ayudas de transporte). Siguen [VERIFICAR].

## Cuarta pasada (11-nov, tarde): matices de Renfe, Navantia y Correos (solo prensa, nivel S)
- **Renfe 2025** [S]: beneficio neto consolidado 60,2 M€ (provisional ≈50 M€; 2024: -2,9 M€); Renfe Viajeros más de 70 M€ (5,4 M€ en 2024); ingresos por billetes ≈2.000 M€ (+19 %), 531,4 millones de viajeros; Mercancías -44,8 M€; liquidez 1.059,5 M€ (654,3 M€ en 2024). Las fuentes discrepan en cuántos años llevaba en pérdidas (cinco o seis) ([Democrata](https://www.democrata.es/economia/renfe-logra-60-millones-de-beneficio-en-2025-impulsada-por-un-19-mas-de-ingresos-en-billetes/)). Cuentas anuales oficiales sin leer [VERIFICAR]. Sesgo: la cifra viene de la propia compañía vía prensa.
- **Navantia 2025** [S]: pérdida consolidada 149 M€ (121 M€ en 2024); matriz -119 M€ (mejora del 9,6 %). Defensa.com la atribuye sobre todo a las filiales internacionales (Reino Unido) en el primer año del Plan Operativo; Finantres añade la integración de activos industriales de enero de 2025. Cartera récord 12.826 M€ y contratación 6.627 M€ ([Defensa.com](https://www.defensa.com/espana/contratacion-record-6-627-millones-euros-navantia-cartera-12-826)). Motivo detallado: cuentas anuales sin leer [VERIFICAR].
- **Grupo SEPI 2025** [S]: beneficio neto 130 M€ y cifra de negocio récord de 7.384 M€; Navantia es la excepción con pérdidas ([Capital Riesgo](https://capital-riesgo.es/es/articles/el-grupo-sepi-obtiene-130-millones-de-beneficios-en-2025-y-alcanza-una-cifra-de-negocio-r-cord-de-7-384-millones-de-euros-/)).
- **Correos 2025** [S]: beneficio provisional 14,4 M€ (2024: -94 M€), pendiente de aprobación definitiva. Posturas enfrentadas: The Objective lo atribuye a ayudas públicas millonarias; CCOO, a recorte de costes, plantilla y financiación pública (más de 400 M€ anuales a servicio postal universal y otros servicios). La CNMC verifica la compensación año a año (2019: 177,3 M€; 2020: 176,5 M€, con cantidades pendientes). Compensación de 2025: no consta [VERIFICAR] ([The Objective](https://theobjective.com/economia/transporte/2026-03-13/correos-maquillaje-cuentas-dinero-publico-precios/)).
- Sin conclusión de culpabilidad ni de gestión: son resultados contables y su causa está sin confirmar en cuentas oficiales.
