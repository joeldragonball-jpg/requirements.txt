# Auditoría numérica de los JSON de España del 17-nov-2026 (solo lectura)

Fecha: 2026-11-18 · Plantilla: `research/plantillas/auditoria-numerica.md` · Sin ediciones a los JSON, sin commit/push, sin API de Anthropic.

Alcance: `explorador/espana-macro.json`, `espana-energia.json`, `espana-vivienda.json`, `espana-pensiones.json`, `espana-investigaciones.json`, `espana-leyes.json`, `espana-presupuesto.json` (bloque `comparativa_2024_2025`), `espana-empleados.json`, `espana-contratacion.json`, `espana-subvenciones.json`. Contraste cruzado con `espana-manual.json`, `espana-politica.json` y los informes `informes/research/2026-11-17-*.md` (C229, C230, C231, C233, C238, C239, C241, C245, C69).

## Resumen

- Ninguna cifra clave resultó errónea frente a la fuente oficial. Todas las que se contrastaron en vivo (ver sección «Contraste con fuente oficial») coinciden.
- Todas las sumas y porcentajes recalculables cuadran, salvo diferencias de redondeo de 0,1 a 2 M€ y los casos listados abajo.
- Hallazgos: 0 graves · 4 medios · 11 bajos · 4 informativos (19 en total).
- Los 4 medios son de interpretación o etiquetado, no de cifra mal copiada: dos totales de «adjudicado» distintos en contratación, posibles duplicados de encargos (11,6 % del total), el total de art. 10 que oculta que Cortes Generales pesa el 54 % sin variar, y una cifra de prensa marcada como [P].
- Unidades y escala: explícitas en los 10 archivos. No hay mezcla M€ / mil M€ sin aviso (en pensiones, «14.540 M€» y «14,5 mil M€» aparecen juntos y cuadran). Los dos archivos de BDNS y PLACSP están en euros (escala 1) con nota de conversión.

## Hallazgos

Gravedad: ALTA = cifra o fecha falsa; MEDIA = puede inducir a error al leerla; BAJA = rotulado, redondeo o coherencia menor; INFO = observación sin acción.

| N.º | Gravedad | Archivo | Clave | Valor actual | Valor correcto / propuesta | Fuente |
|---|---|---|---|---|---|---|
| 1 | MEDIA | espana-contratacion.json | `licitaciones.adjudicaciones_con_importe.importe` frente a `por_nivel_administrativo[].adjudicado` y `por_procedimiento[].adjudicado` | 17.636.833.848,14 € (n=32.962) en el resumen; 18.441.947.243,69 € al sumar niveles o procedimientos (misma suma en ambos desgloses) | Son dos medidas distintas con el mismo nombre «adjudicado». Diferencia: 805.113.395,55 € (4,6 %). Añadir nota que diga cuál se usa para qué (la concentración top-10 = 19,6 % usa 17,64 mil M€: 3.451.740.697,75 / 17.636.833.848 = 19,57 %). En menores pasa igual a escala pequeña: 217.686.776,50 frente a 217.697.051,28 (10.274,78 €). | Cálculo propio con python sobre el propio JSON |
| 2 | MEDIA | espana-contratacion.json | `licitaciones.expedientes_unicos`, `por_nivel_administrativo[ENTIDADES OTRAS].n` | 40.000 expedientes y 12.000 en «Otras entidades del sector público» (cifras redondas exactas); además `por_estado` suma exactamente 40.000 | Indicio de tope del extractor o del feed: no leer 40.000 como total mensual. El aviso de `c241_segunda` ya lo señala como [VERIFICAR]; falta propagarlo a `licitaciones` y a `historico_meses`. Propuesta: marcar `licitaciones.limites` y el panel con «posible tope» hasta confirmar contra el ZIP. | JSON + aviso interno |
| 3 | MEDIA | espana-contratacion.json | `encargos_medios_propios.importe_total` / `mayores_encargos` | 5.420.635.502,19 € (3.078 encargos) | Hay dos pares idénticos (215.807.030,45 € el 5-jun-2026; 98.051.280 € el 29-dic-2025). Si fueran duplicados, el total bajaría 627.716.620 € (11,6 %) a 4.792.918.882 €. El JSON ya dice «pueden ser duplicados [VERIFICAR]»; falta calcular el rango en el total. Propuesta: añadir `importe_total_sin_posibles_duplicados`. | Cálculo propio |
| 4 | MEDIA | espana-presupuesto.json | `comparativa_2024_2025.totales` (art10 +3,7 %, art11 +6,2 %) | Cortes Generales: art. 10 = 40,23 M€ en 2024 y 2025 (var. 0,0 %); art. 11 = 17,3 M€ en ambos años | Cortes pesan el 54,2 % del total art. 10 y no varían, lo que diluye la tendencia. Sin Cortes: art. 10 pasa de 31,30 a 33,98 M€ (+8,6 %); art. 11 de 57,68 a 62,36 M€ (+8,1 %). Propuesta: añadir esa lectura y marcar la fila de Cortes como [VERIFICAR] (cifras idénticas dos años seguidos con presupuesto prorrogado: puede ser la dotación fija y no obligaciones). | Cálculo propio con las 27 filas |
| 5 | MEDIA | espana-pensiones.json | `caso_alcista_vs_bajista.bajista[2]` | «Nómina +6,3 % interanual frente a afiliados +3,6 % [P; comparación propia]» | La nota oficial de la Seguridad Social (leída en vivo 18-nov) NO da la variación interanual de la nómina ni del número de pensiones; el +6,3 % procede de prensa (Artículo 14; `espana-manual.json` lo marca nivel S, y +1,6 % en nº de pensiones). Es coherente (1,046 × 1,016 = 1,063) pero es derivada de prensa. Cambiar a [S; cálculo propio con 4,6 % oficial y +1,6 % de prensa]. | revista.seg-social.es; espana-manual.json |
| 6 | BAJA | espana-pensiones.json | `demografia.natalidad[2]` (saldo vegetativo) | −122.167 | Es el dato del INE y es correcto, pero 321.164 − 446.982 = −125.818. El INE calcula el saldo con nacimientos de madres residentes y defunciones de residentes (nota 1 de la nota de prensa); −125.818 es el de la tabla por CCAA. `espana-manual.json` lo explica; pensiones no. Añadir esa frase. | ine.es/dyngs/Prensa/EDES_EMN2025.htm (leída 18-nov) |
| 7 | BAJA | espana-energia.json | `mix_generacion[0].valor` | 21,4 % (4.845 / 22.694 GWh) | 21,35 % al recalcular con las cifras redondeadas de la propia nota (redondea a 21,3). Diferencia de 0,1 pp; probable redondeo de GWh no enteros. Aclarar o dejar 21,3 si se usan solo los GWh citados. El resto (17,5; 21,0; 21,7) cuadra. | REE REData (no releído) |
| 8 | BAJA | espana-empleados.json | `secciones[CORTES GENERALES].empleados` (853) y `secciones[SENADO].empleados` (568) | Dos filas con el Senado dentro | 853 incluye 260 funcionarios y 94 laborales del Senado (según la web del Congreso); la fila Senado suma 262 + 92 + 110 adscritos + 104 eventuales = 568 con otra definición. Sumar ambas filas cuenta el Senado dos veces. Añadir `no_sumar_con` o separar Congreso y Senado. Además la fila Senado dice «262 funcionarios adscritos», que mezcla «funcionarios» y «adscritos». | JSON |
| 9 | BAJA | espana-empleados.json | `total_ministerios` | 98.224 | Cuadra con la suma de `empleados_ministerio` de las 26 secciones con dato (no incluye Fuerzas Armadas ni Policía/Guardia Civil). La suma de `empleados` (con FFAA y cuerpos policiales) es 383.077. Rotular qué total es cada uno para que el panel no use el equivocado. Todas las filas cumplen funcionarios + laborales + otro = empleados_ministerio y Defensa 12.391 + 123.504 = 135.895; Interior 29.827 + 78.740 + 82.609 = 191.176. | Cálculo propio |
| 10 | BAJA | espana-leyes.json | `aviso` | «recuentos de votos son [S]» y, más adelante, «recuento 12-nov … [P]»; `generado` = 2026-11-17 pero el aviso cita «18-nov» | Texto acumulado con frases contradictorias. Propuesta: quitar «recuentos de votos son [S]» y poner `generado` = 2026-11-18. El recuento (RDL 29: 35-34; RDL 28: 34-35) coincide con los estados de las dos filas. | congreso.es (nota de prensa, según el JSON) |
| 11 | BAJA | espana-leyes.json | `leyes[RDL 23/2026].publicacion` | «(RDL 8-sep)» | No es fecha ISO. Poner la fecha de publicación en BOE (BOE-A-2026-19845) o `null` [VERIFICAR]. | boe.es |
| 12 | BAJA | espana-leyes.json | `leyes[Verifactu].publicacion` | 2025-12-03 con `ref` BOE-A-2023-24840 | La fecha corresponde al RDL 15/2025 (que cambia los plazos), no al RD 1007/2023 de la referencia. Aclarar «RD 1007/2023; plazos modificados por RDL 15/2025 (publicado 2025-12-03 [VERIFICAR])». | boe.es |
| 13 | BAJA | espana-vivienda.json | `bloques.hipotecas` | `n_hipotecas_total_fincas_ago26` = 42.991 y `n_total_fincas_jul26` = 56.595 | Meses distintos y claves con nombres distintos para lo mismo (total de fincas). Un lector verá −24 % sin saber que son jul y ago. Unificar nombres o añadir `variacion_mensual_pct` con nota de estacionalidad. | INE HPT 13896 (no releído) |
| 14 | BAJA | espana-presupuesto.json | `totales.obligaciones_2025` / `cierre_definitivo.anios[2025].obligaciones` / suma de `capitulos_totales` | 423.336,4 / 423.336,3 / 423.336,5 M€ (y 2024: 408.563,7 / 408.563,6 / 408.563,6) | Redondeo de ≤ 0,2 M€; consistente con la nota («diferencia máxima 0,1 M€»). Sin acción salvo unificar a una sola cifra para citar. Cierre 2024: derechos − obligaciones = −18.189,4 frente a −18.189,5 publicado (0,1 M€). | IGAE |
| 15 | BAJA | espana-subvenciones.json | `c241_segunda_2026-11-17.recuento_semanal_concesiones_por_fecha_concesion` | Suma de las 10 semanas = 1.735.284; la ventana recontada es 1.723.685 | La diferencia (11.599) viene de las dos últimas semanas, que se salen de la ventana 11-sep a 9-nov (la de 6-nov llega hasta el 12-nov y la de 13-nov solo tiene 3.497 por retraso). Falta decir si la etiqueta de cada semana es el inicio o el fin. Añadir `nota` con el criterio. Los demás cálculos cuadran (1.723.685 − 1.643.342 = 80.343 = +4,9 %; septiembre 1.468.608 ≈ 1,47 M). | Cálculo propio |
| 16 | BAJA | espana-contratacion.json y espana-subvenciones.json | `generado` | 2026-11-10 en ambos | Los dos archivos se ampliaron el 17-nov (bloque `c241_segunda`, `encargos_medios_propios`, `ventanas_adicionales`) pero `generado` sigue en 10-nov. Un lector puede tomar los datos por antiguos; el JSON interno dice «leído 2026-11-17». Añadir `ampliado: 2026-11-17`. | JSON |
| 17 | BAJA | espana-contratacion.json | `encargos_medios_propios.por_anio_adjudicacion` | Años «0024» (1 encargo, 1.694.346,56 €) y «0026» (1 encargo, 502.145,78 €) | Años imposibles (errores de captura en la fuente PLACSP). Probablemente 2024 y 2026; no corregir a ciegas. Marcar como [VERIFICAR] o agrupar en «año no válido». El resto de años suma 3.078 encargos y 5.420.635.502,19 € (cuadra). | JSON |
| 18 | BAJA | espana-macro.json | `salarios_smi.salario_medio_aeat` | Clave «aeat» con el dato de la EAES del INE (29.540,26 €) | La nota lo aclara, pero la clave engaña. Renombrar a `salario_medio_eaes` en el próximo cambio de esquema (sin romper las vistas). Cifra verificada: EAES741 2024 = 29.540,26 y 2023 = 28.049,94 (+5,3 %). | INE Tempus |
| 19 | INFO | espana-manual.json frente a espana-macro.json | SMI «14 pagas» | Manual: «En 14 pagas equivale a 17.094 € (cálculo nuestro)»; macro: «14 pagas [VERIFICAR]» | Misma cifra, distinto grado de certeza. El BOE solo dice 1.221 €/mes y que la cuantía anual no puede ser inferior a 17.094 €; 1.221 × 14 = 17.094 cuadra, así que es un cálculo correcto, no un hecho del BOE. Igualar la redacción. | BOE-A-2026-3815 (leído) |

Observaciones sin numerar (ya correctas): `espana-investigaciones.json` tiene `unidad: EUR` mientras los textos usan M€ entre paréntesis (correcto, cada texto lleva la conversión); los hechos del caso 2 no están en orden cronológico; `por_abrir` es 0 (entero) y no lista.

## Correcciones seguras

Se pueden aplicar sin riesgo (cambian texto, rótulo o nivel, no cifras de fuente):

1. Hallazgo 5: en `espana-pensiones.json`, `bajista[2]`, cambiar «[P; comparación propia]» por «[S; cálculo propio con +4,6 % oficial y +1,6 % de prensa]».
2. Hallazgo 6: añadir a la nota de `natalidad[2]`: «El INE calcula el saldo con nacimientos de madres residentes y defunciones de residentes; la resta directa es −125.818 (tabla por CCAA)».
3. Hallazgo 10: en `espana-leyes.json`, `aviso`: quitar «recuentos de votos son [S];» y poner `generado` = 2026-11-18.
4. Hallazgo 11: `leyes[RDL 23/2026].publicacion` a `null` con nota «publicación en BOE [VERIFICAR]».
5. Hallazgo 12: reformular `publicacion` de Verifactu como indica la tabla.
6. Hallazgo 16: añadir `ampliado: "2026-11-17"` a `espana-contratacion.json` y `espana-subvenciones.json` sin tocar `generado`.
7. Hallazgo 17: añadir nota [VERIFICAR] a las dos filas de año imposible.
8. Hallazgo 15: añadir nota con el criterio de las etiquetas semanales (pendiente de confirmar si inicio o fin).
9. Hallazgo 8 y 9: añadir campos de texto `nota_no_sumar` y rótulo de qué total es cada uno (sin tocar cifras).
10. Hallazgo 19: igualar la redacción del SMI a «1.221 €/mes; 17.094 €/año como mínimo anual; 14 pagas = cálculo propio».
11. Hallazgos 1, 2, 3 y 4: añadir notas aclaratorias (no cambiar cifras): el cálculo de duplicados en el hallazgo 3 (4.792.918.882 €) y la lectura sin Cortes del hallazgo 4 (+8,6 % y +8,1 %) son recalculables y seguras como campos nuevos.

No tocar sin Joel: cifras de contratación (qué «adjudicado» es el oficial) y el rotulado de Cortes en presupuesto (hallazgo 4, requiere releer el PDF de IGAE).

## Contraste con fuente oficial (en vivo, 18-nov-2026, curl con User-Agent de navegador)

| Cifra | JSON | Fuente leída | Resultado |
|---|---|---|---|
| IPC oct-2026 general, mensual, impuestos constantes | 4,9 % · 0,6 % · 5,6 % | INE Tempus IPC290750/52, IPC292578 | Coincide (sep: 4,9; 0,3; 5,4). También grupos Vivienda 7,6, Transporte 10,3, Alimentos 2,4, subyacente 3,1, energía 29,0 |
| EPA 3T-2026 | paro 10,18 %; ocupados 22.852,6; parados 2.591,2; <25 años 23,33 | INE EPA452434/387796/387800/452436 | Coincide. Recalculado: 2.591,2 / (22.852,6 + 2.591,2) = 10,18 % |
| PIB 3T-2026 | 0,63 % trim. · 2,66 % anual | INE CNTR6653/6654 | Coincide (0,6347 y 2,6632) |
| SMI 2026 | 40,70 €/día · 1.221 €/mes · +3,1 % · 17.094 €/año | BOE-A-2026-3815 | Coincide (40,70 €/día o 1 221 €/mes; subida 3,1 %) |
| Euríbor oct-2026 | 12m 3,239; 6m 2,975; 3m 2,635; ¤STR 2,441 | CSV BdE be1901 (BE_19_1.x) | Coincide (sep: 3,247 / 2,922 / 2,635 / 2,440) |
| Pensiones oct-2026 | 10.565.782; 14.540 M€; 1.376,14 €; jubilación 1.577,6 €; altas 1.758 €; edad 65,4 | revista.seg-social.es (nota de octubre) | Coincide. Nómina por clases suma 14.539,9 M€ |
| Deuda CCAA jun-2026 | 355.241 M€ (jun-25: 342.799); Cataluña 92.770; Andalucía 42.070 | CSV BdE be1309 (miles de €) | Coincide (355.240.937 y 342.799.347 miles de €) |
| Población 1-oct-2026 | 49.935.642; +130.223; +435.551 | INE ECP3T26 | Coincide |
| Natalidad 2025 | 321.164 nacimientos; 446.982 defunciones; saldo −122.167 | INE EDES_EMN2025 | Coincide (ver hallazgo 6) |
| Gas almacenado 16-nov | 80,04 %; 28,68 TWh; capacidad 35,8318 TWh | API AGSI+ | Coincide (full 80,04; gasInStorage 28,6814; workingGasVolume 35,8318) |
| Dependencia energética 2024 | ES 68,9 % · UE 57,3 % (2023: 68,3 y 58,3) | Eurostat nrg_ind_id | Coincide (68,871; 57,286; 68,261; 58,342) |
| IRAV | 2,57 / 2,54 / 2,47 | INE IRAV1 | Coincide |
| RDL 34/2026, RDL 33/2026, RD 996/2026, resoluciones 23754/23755 | fechas de publicación y vigor | BOE XML | Coincide (RDL 34: vigor 11-nov, art. 1 el 11-may-2027; RD 996: vigor 18-nov) |
| EPPO abril y noviembre 2026 | detención 15-abr, 3,3 M€, 550.000 €; actuación 12-nov | eppo.europa.eu | Coincide (miércoles = 15-abr; comunicado 17-abr) |
| Salario medio EAES 2024 | 29.540,26 (2023: 28.049,94) | INE EAES741 | Coincide |

No contrastados en vivo (dependen de fuentes con descarga pesada o sin API): OMIE, Boletín Petrolero UE, MITECO embalses, PLACSP (ZIP de 194 MB) y BDNS (API paginada). Sus sumas internas sí se recalcularon y cuadran, salvo lo indicado.

## Recálculos que cuadran (sin acción)

- espana-macro: SMI 40,70 × 30 = 1.221; 1.221 × 14 = 17.094; 3,1 % frente a IPC 4,9 % = 1,8 pp; cuartil inferior EAES 17.457,47 − 17.094 = 363,47 (se dice 363); afiliados +3,6 % = 784.573 / (22.624.165 − 784.573).
- espana-vivienda: 17 CCAA suman 355.243 M€ frente a 355.241 M€ del total (jun-26) y 342.798 frente a 342.799 (jun-25), diferencias de redondeo; las 17 variaciones interanuales y las 17 ratios deuda/PIB cuadran a 0,1 pp.
- espana-energia: +122 % (168,93 / 76,02 = 2,22); gasolina +17,1 % y gasóleo +33,2 % interanual; diferencias con la UE 0,147 y 0,199 €/l; 11,6 puntos de dependencia; gas 28,68 / 35,83 = 80,0 %.
- espana-pensiones: 10.565.782 × 1.376,14 = 14.540 M€; 73,5 % jubilación; 22.624.165 / 10.565.782 = 2,14; 10.632.438 / 49.935.642 = 21,3 %; 10.632.438 / 6.679.430 = 159,2; dependencia 53,1 % y 32,6 %; 10,4 + 2,2 = 12,6 y 10,6 + 1,4 = 12,0 % PIB; saldo −7.387 = 232.782 − 240.169; fondo 15.267 / 14.540 = 1,05 meses; 56.946 y 61.881 M€ con 3,4 y 3,7 % del PIB (PIB ≈ 1,68 billones, coherente con la suma de CCAA).
- espana-investigaciones: 47.000 + 48.000 = 95.000 €; 35.226.395,43 × 1,21 = 42,6 M€ (= cifra del Tribunal de Cuentas); informe n.º 1695: 102,6 M€ en total (42,6 el de 2023).
- espana-presupuesto: las 27 filas cumplen var_abs y var_pct (tolerancia 0,01 y 0,1); sumas 71,53 / 74,21 y 74,98 / 79,66 exactas; capítulos: variaciones cuadran y la suma 2025 de capítulos / 2024 = +3,6 %; gasto per cápita 8.403,3 y 8.617,0 €.
- espana-contratacion: por_estado, por_nivel y por_procedimiento suman 40.000 expedientes; menores 43.614; urgencia 38.941 + 857 + 202 = 40.000; todos los `pct_expedientes` cuadran.
- espana-subvenciones: por nivel e instrumento suman 1.643.342 y 4.519.627.436,04 €; concentración top-10 = 10,07 % (se dice 10,1); ventana 10-16 nov suma 11.488 y 181.459.877,38 €.
- espana-empleados: todas las filas suman funcionarios + laborales + otro = empleados_ministerio.
- espana-leyes: 30 normas; las fechas de vigor derivadas se recalcularon (RD 957: 5-nov + 2 meses = 5-ene-2027; RDL 34: 11-nov + 6 meses = 11-may-2027). 29-nov-2026 es domingo y 6-oct + 54 días = 29-nov (plazo electoral coherente).
- Días de la semana: 9-nov-2026 y 10-nov-2025 son lunes (Boletín Petrolero); 15-abr-2026 es miércoles.

## Cruces entre archivos e informes (sin contradicciones de cifra)

- Informes C229, C230, C231, C233, C239, C241: las cifras citadas coinciden con los JSON. Única diferencia: el informe C229 dice que el Euríbor de octubre (3,239 %) «no se releyó», mientras el JSON dice «releído el 17-nov»; el JSON es el correcto (verificado hoy en be1901).
- espana-manual.json (pensiones, SMI, saldo vegetativo, Fondo de Reserva 14.100 / 14.283 M€) es coherente con pensiones y macro; el manual marca nivel S lo que pensiones marca P en parte (hallazgo 5).
- Las Cortes disueltas el 6-oct-2026 (RD 806/2026) y elecciones el 29-nov aparecen igual en leyes, empleados, política, votaciones y presupuesto.

## Cierre

Estado del trabajo: auditoría completada, solo lectura. Ningún JSON modificado. Pendiente de Joel: decidir si se aplican las «correcciones seguras» y si se relee el PDF de IGAE para la fila de Cortes Generales (hallazgo 4).

## Aplicado 18-nov

Solo texto, rótulos y notas; ninguna cifra de fuente cambiada. Cada JSON carga con python y `scripts/revisar_explorador.py` da 0 avisos.

- espana-pensiones: nivel de «+6,3 % de nómina» a [S; cálculo propio con +4,6 % oficial y +1,6 % de prensa] (h. 5); nota del saldo vegetativo con la explicación −122.167 (INE, residentes) frente a −125.818 (resta directa) (h. 6).
- espana-leyes: `aviso` sin «recuentos de votos son [S]», `generado` = 2026-11-18 (h. 10); RDL 23/2026 `publicacion` = null con `nota_publicacion` [VERIFICAR] (h. 11); Verifactu reformulado (h. 12).
- espana-contratacion y espana-subvenciones: `ampliado: 2026-11-17` sin tocar `generado` (h. 16); contratacion: `nota_adjudicado` (17,64 frente a 18,44 mil M€, h. 1), `nota_posible_tope` (h. 2), `nota_duplicados` con el rango 4,79 a 5,42 mil M€ (h. 3) y nota [VERIFICAR] en los años «0024» y «0026» (h. 17); subvenciones: `nota_semanas` (h. 15).
- espana-empleados: `total_ministerios_rotulo` (98.224 frente a 383.077) y `nota_no_sumar` en las filas CORTES GENERALES y SENADO (h. 8 y 9).
- espana-macro: SMI en 14 pagas igualado a «cálculo propio (1.221 × 14), no texto del BOE», en la nota y en `pendiente` (h. 19).
- espana-presupuesto (h. 4): releídos los PDF oficiales de la IGAE (MENSUAL 12-24 y 12-25, servicios 0201 a 0205). Las Cortes tienen cifras idénticas en 2024 y 2025 en la propia fuente (crédito inicial = definitivo = obligaciones; Congreso 110.421.300 €, Senado 64.136.450 €, Cortes 72.052.850 €, JEC 478.770 €, Defensor 20.917.800 €). No es error de extracción: se mantiene la fila y se añade `comparativa_2024_2025.nota_cortes_generales` con la lectura sin Cortes (art. 10: 31,30 a 33,98 M€, +8,6 %; art. 11: 57,68 a 62,36 M€, +8,1 %, recalculado) y el motivo (¿prórroga?) como [VERIFICAR].
- No tocado: nombres de clave (h. 18), unificación de claves de vivienda (h. 13), redondeos (h. 7 y 14), ni vistas, construir_*, tareas.csv, commit o push.
