# C241 · «Dónde va el dinero»: contratos públicos (PLACSP) y subvenciones (BDNS) — 10-nov-2026

> Datos, no recomendación de compra/venta. Todo leído en los ficheros oficiales con scripts locales sin IA (`scripts/leer_contratacion.py`, `scripts/leer_bdns.py`). Nivel **P** = leído en la fuente oficial; las lecturas/interpretaciones son mías. Importes: **M€ = millones de euros; mil M€ = miles de millones**, sin IVA en contratos.

## Qué se leyó (y su alcance)
- **PLACSP, mes oct-2026**: ZIP de licitaciones (194 MB, 124 ficheros ATOM, 61.762 entradas = **40.000 expedientes únicos** tras quedarse con la última versión) y ZIP de contratos menores (25 MB, **43.614** contratos). Fuente: contrataciondelestado.es/sindicacion (fichero mensual; leído 10-nov-2026) [P].
- **BDNS, 11-sep a 9-nov-2026 (60 días, por fecha de concesión)**: **1.643.342 concesiones** leídas por la API infosubvenciones.es [P]. El plan pedía «último año»: no se hizo porque la API tarda ~2 min por semana (≈ 7 M de concesiones/año); el script admite `--dias 365` y queda pendiente (ver «Sin leer»).

## HECHOS (10 con cifra; fuente y fecha)
1. **PLACSP oct-2026**: 32.962 adjudicaciones con importe suman **17.637 M€** (sin IVA; los acuerdos marco con ≥3 adjudicatarios de igual importe se cuentan una sola vez). Por nivel: entidades locales 6.290 M€ (17.137 expedientes), otras entidades del sector público 5.813 M€, Administración General del Estado 4.170 M€, CCAA 2.170 M€ [P, PLACSP oct-2026].
2. **Procedimiento**: abierto 46,3 % de los expedientes y abierto simplificado 38,2 %; **negociado sin publicidad 134 expedientes (0,3 %) con 523 M€ de presupuesto**; emergencia **202 expedientes (0,51 %)** [P, PLACSP oct-2026].
3. **Emergencia por órgano**: el que más acumula es la Dirección General de Biodiversidad y Bosques, con 29 expedientes de emergencia; ADIF-Presidencia, 13 [P, PLACSP oct-2026].
4. **Adif**: 404 expedientes con «Adif» en el órgano (incluye Adif AV), **1.569 M€ adjudicados**; Consejo de Administración de Adif 706 M€ (75 exp.) y de Adif Alta Velocidad 640 M€ (18 exp.), 16 expedientes de emergencia [P, PLACSP oct-2026]. Ejemplo con importe: expediente `3.25/20830.0277` de Adif AV, 199,7 M€ a dos UTE (cada una consta con ese importe: no sumables).
5. **Acuerdo marco de compra de medios publicitarios** (expediente `2023/01`, Dirección General de Racionalización y Centralización de la Contratación, adjudicado 2-nov-2023): consta un techo de **396 M€** para cada una de las 6+ agencias adjudicatarias (GroupM, Mindshare, Essence…). Es un techo común, **no 396 M€ por empresa** [P].
6. **Contratos grandes «movidos» en octubre pero adjudicados antes**: concesión de residuos de Tenerife (`LA0001752-LA0001750-2018-61`, 371,5 M€ a UTE Urbaser-FCC, adjudicada 23-mar-2021) y limpieza de espacios públicos de Madrid (`300/2020/00547`, 6 lotes, adjudicada 10-ago-2021, ~1.490 M€ sumando lotes) [P]. Aparecen porque se modificaron/actualizaron en el mes: el feed no es «lo adjudicado en el mes».
7. **Correos**: expediente `2026/40` «Servicios postales de notificaciones administrativas y judiciales», 308 M€ por negociado con publicidad, adjudicado 19-oct-2026 a Sociedad Estatal Correos y Telégrafos [P].
8. **Contratos menores oct-2026**: 43.614 contratos por **217,7 M€** (media ≈ 5.000 €); 106 marcados como emergencia (0,24 %); los 10 mayores adjudicatarios suman solo el 1,7 % del importe: muy atomizado [P].
9. **BDNS, 60 días**: 1.643.342 concesiones por **4.519,6 M€ = 4,52 mil M€**; el 94 % de las concesiones (1.549.345) va a personas físicas (enmascaradas) pero solo suman 1.423 M€ (31,5 % del importe). Por nivel: CCAA 2.993 M€, Estado 1.114 M€, local 406 M€ [P, BDNS 9-nov-2026].
10. **Un solo órgano concentra más de 1 M de concesiones**: Dirección General de Aviación Civil (Ministerio de Transportes y Movilidad Sostenible) — **1.110.057 concesiones por 186 M€** (≈ 168 € de media). El programa concreto [VERIFICAR] en la convocatoria; el dato es el recuento BDNS. Además, la concesión mayor del periodo: **56,9 M€** del Gobierno de Canarias (Consejería de Obras Públicas, Vivienda y Movilidad) al Cabildo de Tenerife (`SB159346201`) y 55,0 M€ al de Gran Canaria (`SB159346206`) [P, BDNS].
Extra: PAC en Castilla y León, DG de Política Agraria Comunitaria: 100.636 concesiones, 527 M€ en 60 días [P]. Sanciones: la API devuelve **solo 4 registros** [P]; partidos políticos: 6.638 registros, muestra de 2.000 por 161,2 M€ (sin agregar completo, [VERIFICAR]).

## OPINIONES / LECTURAS [ESPECULACIÓN]
- Caso «alcista» (transparencia): el sistema publica expediente, órgano, NIF e importe con latencia de un día; la emergencia (0,5 %) y el negociado sin publicidad (0,3 %) pesan poco en número.
- Caso «bajista»: en importe, una operación grande se esconde en pocos expedientes (neg. sin publicidad: 523 M€ de presupuesto); el feed no muestra ejecución, sobrecostes ni pagos; las CCAA/EELL con plataforma propia pueden faltar. **Una cifra alta de un adjudicatario repetido NO es indicio de irregularidad.**
- Sesgos de fuente: son datos del propio sector público (autodeclarados por el órgano); acuerdos marco duplican importes; relaciones trimestrales de menores se publican como una sola entrada.

## Sin leer / límites
- Solo oct-2026 de PLACSP; otros meses y el ATOM diario sin leer. Plataformas autonómicas/locales agregadas: no probadas [VERIFICAR].
- BDNS: ventana de 60 días, no 365; filtros por nivel e importe de la API se ignoran; pagos no existen en la fuente; partidos y grandes beneficiarios solo muestra.
- Encargos a medios propios (Tragsa, Tragsatec…), modificaciones de contrato (importe modificado) y vinculación con las investigaciones de C239: sin hacer (ver `falta` en C241).
- El criterio «Interior» incluye cualquier órgano con «policía» (p. ej. policías locales); «Sanidad», con «salud» (servicios autonómicos): vigilados por texto, [VERIFICAR].

## Lecciones (5 líneas)
1. La API de BDNS ignora filtros salvo fechas: planifica la ventana (≈ 2 min por semana de datos).
2. En PLACSP los acuerdos marco repiten el techo por adjudicatario: detecta importes idénticos antes de sumar.
3. El feed mensual trae contratos antiguos modificados: nunca llamarlo «adjudicado en el mes».
4. `python -I` falla aquí (falta `encodings` en este entorno); los ZIP se leyeron con `zipfile` sin ejecutar nada de ellos.
5. Borrar los volcados (ZIP) fuera del repo al terminar; en git solo van los JSON agregados.
