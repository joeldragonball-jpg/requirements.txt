# C67 · España: dentro de cada ministerio, fuera de los ministerios, personal público y cargos políticos (30-oct-2026)

Sin API de Anthropic. Amplía `explorador/espana-presupuesto.json` con `capitulos_por_ministerio`, `fuera_de_ministerios`, `personal_publico` y `cargos_politicos`. Se ve en la pestaña **España** del Panel y en **Datos** del móvil. Niveles: [P] fuente oficial leída · [S] secundaria · [VERIFICAR] no leído. Sin recomendaciones.

## Resumen
1. **Dentro de los ministerios [P]:** están el capítulo, los programas, los centros y el destino de las transferencias de las 37 secciones. El personal pesa muy distinto: Interior 79,9 % de su gasto, Inclusión 0,1 %.
2. **Fuera de los ministerios [P]:** el Estado transfirió a la Seguridad Social 47.815 M€ en 2025, además de un préstamo de 10.004 M€; las cotizaciones fueron 176.918 M€.
3. **Personal [P]:** 3.071.725 efectivos en enero de 2026 y 181.502 M€ de remuneración en 2025, el 10,7 % del PIB. En 2024, España era la 18.ª de 27 con el 10,8 % (UE-27: 10,2 %).
4. **Cargos políticos:** la suma de lo publicado a nivel del Estado es **382,9 M€** (7,69 € por habitante, 0,050 % del gasto de las AAPP). **No es el coste total:** faltan CCAA y ayuntamientos, para los que no hay total publicado.
5. **Contexto nuevo [P]:** el [Real Decreto 806/2026](https://boe.es/boe/dias/2026/10/06/pdfs/BOE-A-2026-20742.pdf) disolvió las Cortes y convocó elecciones para el 29-nov-2026. Esto actualiza el [VERIFICAR] sobre el PGE que dejó C66: no he encontrado proyecto presentado.

## Parte A · Dentro de cada ministerio
Fuente: [IGAE, cierre de 2025](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf). Obligaciones reconocidas en M€. Capítulos: tabla oficial de la IGAE por programas y capítulos. Centros gestores, destinos y artículos 10 y 11: suma propia de las 11.950 partidas del mensual de la IGAE. «partidas_sin_leer» es lo que esa suma no alcanza frente al total oficial; la mayor diferencia es Defensa (254 M€) y Economía (236 M€). En Presidencia y Justicia, el artículo 10 no cuenta los 16,45 M€ del programa 112A (Tribunales de Justicia y Ministerio Fiscal). Solo presupuesto del Estado: los organismos autónomos y las agencias tienen presupuesto propio y aquí solo aparece lo que el ministerio les transfiere.

| Ministerio | Total | Personal | Bienes y serv. | Transf. corr. | Inversiones | Transf. cap. | Act. fin. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| INCLUSIÓN, S.S. Y MIGRACIONES | 54.800,7 | 61,2 | 1.198,5 | 43.236,9 | 37,2 | 62,1 | 10.204,5 |
| DEFENSA | 18.806,1 | 6.364,1 | 1.986,1 | 613,3 | 9.148,8 | 681,2 | 12,7 |
| TRANSPORTES Y MOVILIDAD SOSTENIBLE | 11.506,1 | 181,3 | 62,7 | 6.125,8 | 3.149,1 | 713,2 | 1.273,5 |
| INTERIOR | 11.144,4 | 8.899,9 | 1.369,7 | 317,6 | 551,0 | 6,0 | 0,2 |
| INDUSTRIA Y TURISMO | 9.976,0 | 36,6 | 13,3 | 68,0 | 15,4 | 2.547,1 | 7.295,8 |
| HACIENDA | 9.219,2 | 390,5 | 98,6 | 2.646,5 | 85,6 | 175,9 | 5.821,7 |
| TRANSICIÓN ECOLÓGICA Y RETO DEMOGR. | 8.974,3 | 110,0 | 28,4 | 948,5 | 486,0 | 6.676,3 | 725,1 |
| PARA LA TRANSF. DIGITAL Y LA FUNCIÓN PÚBL. | 6.394,2 | 84,9 | 31,1 | 95,7 | 347,2 | 523,9 | 5.311,2 |
| DERECHOS SOC., CONSUMO Y AGENDA 2030 | 5.329,4 | 34,7 | 20,2 | 5.140,1 | 4,3 | 130,2 | 0,0 |
| ECONOMÍA, COMERCIO Y EMPRESA | 5.021,6 | 158,4 | 102,9 | 680,2 | 11,0 | 338,9 | 3.447,4 |
| VIVIENDA Y AGENDA URBANA | 4.781,0 | 22,0 | 4,0 | 1,4 | 18,5 | 1.118,6 | 3.616,1 |
| EDUCACIÓN, F. PROFESIONAL Y DEPORTES | 4.725,3 | 525,7 | 45,4 | 4.071,7 | 15,9 | 66,2 | 0,0 |
| CIENCIA, INNOVACIÓN Y UNIVERSIDADES | 4.684,0 | 29,8 | 12,2 | 1.397,0 | 6,1 | 2.637,8 | 601,0 |
| PRESIDENCIA, JUSTICIA Y REL. CORTES | 2.790,9 | 2.131,9 | 224,5 | 172,8 | 234,1 | 26,4 | 0,4 |
| POLÍTICA TERRITORIAL Y MEM. DEMOCR. | 2.259,5 | 306,5 | 61,4 | 12,0 | 18,1 | 1.858,7 | 0,4 |
| ASUNTOS EXT., U. E. Y COOPERACIÓN | 1.818,9 | 386,3 | 191,5 | 1.084,4 | 103,6 | 47,5 | 5,6 |
| AGRICULTURA, PESCA Y ALIMENTACIÓN | 1.565,8 | 80,3 | 27,6 | 656,6 | 309,8 | 354,7 | 136,9 |
| SANIDAD | 1.235,1 | 55,4 | 215,6 | 764,8 | 57,9 | 141,4 | 0,0 |
| CULTURA | 1.038,9 | 94,1 | 49,9 | 683,6 | 37,7 | 173,1 | 0,5 |
| TRABAJO Y ECONOMÍA SOCIAL | 636,4 | 58,8 | 35,4 | 442,7 | 74,9 | 24,6 | 0,0 |
| IGUALDAD | 481,3 | 12,2 | 8,9 | 421,3 | 28,5 | 10,4 | 0,0 |
| JUVENTUD E INFANCIA | 296,5 | 9,4 | 2,3 | 261,3 | 0,9 | 22,7 | 0,0 |

Ejemplos del despliegue (el resto está en el JSON y en el Panel):
- **INCLUSIÓN, S.S. Y MIGRACIONES:** centros: SECRETARÍA DE ESTADO DE SEGURIDAD SOCIAL Y PENSIONES 53.158,6 M€; SECRETARÍA DE ESTADO DE MIGRACIONES 1.318,8 M€; MECANISMO DE RECUPERACIÓN Y RESILIENCIA 284,9 M€. Destinos: Seguridad Social 43.203,4 M€; Exterior 50,4 M€; Familias e ISFL 40,3 M€.
- **IGUALDAD:** centros: S.E. DE IGUALDAD Y CONTRA LA VIOLENCIA DE GÉNERO 376,9 M€; DELEGACIÓN DEL GOBIERNO CONTRA LA VIOLENCIA DE GÉNERO 94,1 M€; MINISTERIO, SUBSECRETARÍA Y SERVICIOS GENERALES 10,3 M€. Destinos: CCAA 322,3 M€; Familias e ISFL 47,9 M€; Entidades locales 40,1 M€.
- **DEFENSA:** centros: SECRETARÍA DE ESTADO DE DEFENSA 10.690,3 M€; MINISTERIO Y SUBSECRETARÍA 6.377,4 M€; EJÉRCITO DE TIERRA 525,5 M€. Destinos: Otras entidades estatales 856,9 M€; Exterior 184,9 M€; Organismos autónomos 110,4 M€.
- **EDUCACIÓN, F. PROFESIONAL Y DEPORTES:** centros: DIRECCIÓN GENERAL DE PLANIFICACIÓN Y GESTIÓN EDUCATIVA 2.779,9 M€; SECRETARÍA GENERAL DE FORMACIÓN PROFESIONAL 862,5 M€; MINISTERIO, SUBSECRETARÍA Y SERVICIOS GENERALES 591,3 M€. Destinos: Familias e ISFL 2.690,7 M€; CCAA 1.212,4 M€; Organismos autónomos 221,3 M€.

### Destino de todas las transferencias corrientes (cap. 4) [P]
Seguridad Social 47.815 · CCAA 33.288 · familias e ISFL 29.063 · entidades locales 26.645 · exterior 18.426 · otras entidades estatales 3.601 · empresas y fundaciones públicas 3.171 · organismos autónomos 2.519 · empresas privadas 955. Total: 165.483 M€.

### Altos cargos y eventuales: coste por ministerio (M€, 2025) [P]
| Ministerio | Altos cargos | Eventuales | Personal total | % de personal |
| --- | ---: | ---: | ---: | ---: |
| PRESIDENCIA, JUSTICIA Y REL. CORTES | 3,24 | 27,70 | 2.131,9 | 76,4 |
| POLÍTICA TERRITORIAL Y MEM. DEMOCR. | 2,55 | 7,54 | 306,5 | 13,6 |
| ASUNTOS EXT., U. E. Y COOPERACIÓN | 1,79 | 1,52 | 386,3 | 21,2 |
| TRANSICIÓN ECOLÓGICA Y RETO DEMOGR. | 1,40 | 1,36 | 110,0 | 1,2 |
| TRABAJO Y ECONOMÍA SOCIAL | 0,85 | 1,36 | 58,8 | 9,2 |
| PARA LA TRANSF. DIGITAL Y LA FUNCIÓN PÚBL. | 1,19 | 1,16 | 84,9 | 1,3 |
| INCLUSIÓN, S.S. Y MIGRACIONES | 0,89 | 1,14 | 61,2 | 0,1 |
| INTERIOR | 1,10 | 0,96 | 8.899,9 | 79,9 |
| INDUSTRIA Y TURISMO | 0,79 | 0,96 | 36,6 | 0,4 |
| HACIENDA | 1,54 | 0,91 | 390,5 | 4,2 |
| VIVIENDA Y AGENDA URBANA | 0,67 | 0,91 | 22,0 | 0,5 |
| SANIDAD | 0,88 | 0,91 | 55,4 | 4,5 |
| CULTURA | 0,60 | 0,90 | 94,1 | 9,1 |
| TRANSPORTES Y MOVILIDAD SOSTENIBLE | 1,20 | 0,89 | 181,3 | 1,6 |
| EDUCACIÓN, F. PROFESIONAL Y DEPORTES | 0,74 | 0,89 | 525,7 | 11,1 |
| IGUALDAD | 0,64 | 0,88 | 12,2 | 2,5 |
| DERECHOS SOC., CONSUMO Y AGENDA 2030 | 0,87 | 0,87 | 34,7 | 0,7 |
| JUVENTUD E INFANCIA | 0,46 | 0,87 | 9,4 | 3,2 |
| CIENCIA, INNOVACIÓN Y UNIVERSIDADES | 0,77 | 0,86 | 29,8 | 0,6 |
| AGRICULTURA, PESCA Y ALIMENTACIÓN | 1,02 | 0,85 | 80,3 | 5,1 |
| DEFENSA | 1,41 | 0,77 | 6.364,1 | 33,8 |
| ECONOMÍA, COMERCIO Y EMPRESA | 1,04 | 0,61 | 158,4 | 3,2 |

- El personal eventual del servicio Presidente del Gobierno suma 25,5 M€ de los 27,7 M€ de Presidencia y Justicia.
- He separado 16,45 M€ del artículo 10 de Presidencia y Justicia porque están en el programa 112A (Tribunales de Justicia y Ministerio Fiscal), que no son cargos de Gobierno. Es una decisión propia, y el JSON conserva el importe aparte.
- **[VERIFICAR] número por ministerio:** no he encontrado tabla oficial. No se ha encontrado una tabla oficial con el número por ministerio. Prensa: 799 altos cargos en 2024 (The Objective) y 1.626 personas de designación política a finales de 2023 (Crónica Económica); fuentes críticas con el Gobierno, sin tabla oficial detrás que se haya leído.

### Sueldos oficiales ([art. 21 de la Ley de PGE 2023](https://www.iberley.es/legislacion/articulo-21-2023-pge)) [P]
| Cargo | € al año |
| --- | ---: |
| Presidente del Gobierno | 90.010,20 |
| Vicepresidente del Gobierno | 84.600,72 |
| Ministro | 79.415,16 |
| Secretario de Estado | 77.893,18 |
| Subsecretario | 69.059,68 |
| Director general | 59.048,40 |

Secretarios, subsecretarios y directores: suma propia de sueldo, destino y específico, sin antigüedad ni pagas extra. **[VERIFICAR]** cuantías de 2026: el [RDL 14/2025](https://laadministracionaldia.inap.es/noticia.asp?id=1261940) sube el sector público, pero no he leído cómo se aplica a cada cargo. La [prensa](https://www.eldebate.com/espana/20260102/estos-son-siete-presidentes-autonomicos-suben-sueldo-2026_370622.html) mantiene al presidente en 90.010,20 € en enero de 2026 [S].

## Parte B · Fuera de los ministerios

### Seguridad Social
- **Cotizaciones sociales:** 176.918 M€ (2025, [P](https://www.inclusion.gob.es/en/w/el-deficit-de-la-seguridad-social-se-reduce-al-0-4-del-pib-su-nivel-mas-bajo-desde-2011-gracias-al-incremento-de-los-ingresos-por-cotizaciones-sociales)). 10,5 % del PIB; +6,9 %. Incluye 4.935 M€ del Mecanismo de Equidad Intergeneracional.
- **Saldo de la Seguridad Social que publica el Ministerio:** -7.387 M€ (2025, [P](https://www.inclusion.gob.es/en/w/el-deficit-de-la-seguridad-social-se-reduce-al-0-4-del-pib-su-nivel-mas-bajo-desde-2011-gracias-al-incremento-de-los-ingresos-por-cotizaciones-sociales)). 0,4 % del PIB, ya contando las transferencias del Estado.
- **Transferencias corrientes del Estado a la Seguridad Social:** 47.815,30 M€ (2025, [P](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)). Incluye IMV 4.955,9 M€, pensiones no contributivas 3.772,5 M€, complementos de mínimos 8.732,3 M€ y protección familiar 1.766,5 M€.
- **Préstamo del Estado a la Seguridad Social:** 10.003,80 M€ (2025, [P](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)). Capítulo 8: activo financiero, no transferencia.
- **Gasto en vejez del subsector Seguridad Social:** 135.654 M€ (2024, [P](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp)). Eurostat, COFOG.
- **Enfermedad e invalidez:** 36.112 M€ (2024, [P](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp)). Incluye incapacidad; Eurostat.
- **Desempleo:** 23.737 M€ (2024, [P](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp)). Eurostat incluye al SEPE en el subsector Seguridad Social.
- **Saldo sin transferencias corrientes del Estado (Seguridad Social Ampliada):** -67.819 M€ (2024, [S](https://documentos.fedea.net/pubs/ap/2026/ap2026-03.pdf)). Fedea, con definición propia que suma clases pasivas: 172.543 M€ de cotizaciones y 58.301 M€ de transferencias en 2024. No se compara con el saldo del Ministerio.

### Organismos: lo que aporta el Estado en 2025 [P]
Lo que el Estado reconoce a cada uno en 2025. Sus ingresos propios no están aquí.

| Organismo | M€ | % del Estado | € por habitante | Partida |
| --- | ---: | ---: | ---: | ---: |
| Corporación RTVE | 556,4 | 0,131 | 11,17 | Transferencia corriente |
| Agencia Española de Cooperación (AECID) | 556,4 | 0,131 | 11,17 | Transferencia corriente |
| CSIC | 482,0 | 0,114 | 9,68 | Transferencia corriente |
| Centro Nacional de Inteligencia | 337,8 | 0,080 | 6,78 | Transferencia corriente |
| CNMC | 274,0 | 0,065 | 5,50 | Transferencia corriente |
| UNED | 111,8 | 0,026 | 2,24 | Transferencia corriente |
| Congreso de los Diputados | 110,4 | 0,026 | 2,22 | Servicio 0202 |
| Tribunal de Cuentas | 75,1 | 0,018 | 1,51 | Sección 03 |
| Instituto Cervantes | 74,1 | 0,018 | 1,49 | Transferencia corriente |
| Cortes Generales (común) | 72,1 | 0,017 | 1,45 | Servicio 0201 |
| Consejo General del Poder Judicial | 70,4 | 0,017 | 1,41 | Sección 08 |
| Senado | 64,1 | 0,015 | 1,29 | Servicio 0203 |
| Tribunal Constitucional | 30,1 | 0,007 | 0,60 | Sección 04 |
| Agencia Estatal de Meteorología | 28,9 | 0,007 | 0,58 | Transferencia corriente |
| Agencia Estatal de Investigación | 28,4 | 0,007 | 0,57 | Transferencia corriente |
| Defensor del Pueblo | 20,9 | 0,005 | 0,42 | Servicio 0205 |
| Agencia Espacial Española | 14,0 | 0,003 | 0,28 | Transferencia corriente |
| Consejo de Estado | 12,1 | 0,003 | 0,24 | Sección 05 |
| Casa de Su Majestad el Rey | 8,7 | 0,002 | 0,17 | Sección 01 |
| Junta Electoral Central | 0,5 | 0,000 | 0,01 | Servicio 0204 |

- **Banco de España:** [VERIFICAR] (2025, [VERIFICAR](https://www.bde.es)). Se financia con sus resultados; no se ha encontrado transferencia del Estado en la IGAE. Presupuesto propio no leído.
- **CNMV:** [VERIFICAR] (2025, [VERIFICAR](https://www.cnmv.es)). No se ha encontrado transferencia en la IGAE. Presupuesto propio no leído.
- **Presupuesto total de RTVE y de la CNMC:** [VERIFICAR] (2025, [VERIFICAR](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)). Solo se ha leído la aportación del Estado.

### Por nivel de administración (Eurostat, 2024, M€) [P]
Gasto por función y nivel (Eurostat, COFOG, 2024). Columnas sin consolidar: las transferencias entre administraciones se cuentan en las dos.

| Función | Total AAPP | Estado | CCAA | Local | Seguridad Social |
| --- | ---: | ---: | ---: | ---: | ---: |
| Gasto total | 725.001 | 357.732 | 268.013 | 97.105 | 252.803 |
| Servicios generales | 92.551 | 253.081 | 49.138 | 32.140 | 8.844 |
|   · Órganos ejecutivos y legislativos, asuntos financieros y exteriores | 21.444 | 15.526 | 2.374 | 3.544 | 0 |
|   · Intereses de la deuda | 39.644 | 34.179 | 6.758 | 1.289 | 311 |
| Defensa | 14.233 | 14.233 | 0 | 0 | 0 |
| Orden público y seguridad | 28.628 | 14.956 | 7.038 | 6.634 | 0 |
| Asuntos económicos | 80.908 | 34.121 | 25.538 | 18.106 | 3.143 |
| Medio ambiente | 15.539 | 1.976 | 3.469 | 10.094 | 0 |
| Vivienda y servicios comunitarios | 7.613 | 195 | 3.101 | 4.317 | 0 |
| Sanidad | 102.942 | 3.585 | 96.501 | 883 | 1.973 |
| Cultura y ocio | 19.193 | 3.375 | 4.343 | 11.475 | 0 |
| Educación | 65.862 | 2.665 | 59.766 | 3.419 | 12 |
| Protección social | 297.532 | 29.545 | 19.119 | 10.037 | 238.831 |
|   · Vejez | 165.050 | 18.563 | 6.722 | 4.111 | 135.654 |
|   · Enfermedad e invalidez | 44.019 | 1.416 | 4.674 | 1.817 | 36.112 |
|   · Desempleo | 24.077 | 286 | 25 | 29 | 23.737 |
|   · Familia | 15.294 | 5.073 | 2.717 | 1.927 | 5.577 |
|   · Exclusión social | 10.878 | 1.262 | 3.915 | 1.913 | 3.788 |

- **Gasto agregado de parlamentos y gobiernos autonómicos:** [VERIFICAR] (2024, [VERIFICAR](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp)). No se ha encontrado un agregado publicado. Lo más cercano: «órganos ejecutivos y legislativos, asuntos financieros y exteriores» de las CCAA, 2.374 M€ en 2024, que no equivale a parlamentos más gobiernos. Hay que sumar los presupuestos de cada cámara.

### Intereses y UE
- **Intereses de la deuda del Estado:** 34.822,10 M€ (2025, [P](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)). 8.2 % de las obligaciones del Estado; 4.5 % del gasto de las AAPP; 699 € por habitante.
- **Intereses de todas las administraciones:** 39.644 M€ (2024, [P](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp)). 5.5 % del gasto de las AAPP de 2024.
- **Aportación al presupuesto de la UE:** 17.164,80 M€ (2025, [P](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)). 4.1 % de las obligaciones del Estado; 2.2 % del gasto de las AAPP; 345 € por habitante. Es lo pagado; lo recibido se ve aparte y su saldo sigue en [VERIFICAR].

## Parte C · Personal público y cargos políticos

### Cuántos son ([EPSAP, enero de 2026](https://digital.gob.es/content/dam/portal-mtdfp/funcion-publica/rcp/boletin/2026_01/revision-agosto-2026/EPSAP_Enero_2026%20.pdf)) [P]
Registro Central de Personal (EPSAP). Universidades a 31-dic-2024; Cataluña a 1-jul-2025. «Otro personal» agrupa lo que no es funcionario de carrera ni laboral; el resumen no separa interinos.

| Administración | Efectivos | % del total | Funcionario de carrera | Laboral | Otro personal |
| --- | ---: | ---: | ---: | ---: | ---: |
| Sector público del Estado | 546.554 | 17,79 | 428.847 | 82.937 | 34.770 |
| · Ministerios | 98.224 | 3,20 | 66.924 | 22.561 | 8.739 |
| · Organismos autónomos | 62.492 | 2,03 | 47.102 | 12.306 | 3.084 |
| · Entidades públicas empresariales | 24.698 | 0,80 | 3 | 24.625 | 70 |
| · Agencias estatales | 21.190 | 0,69 | 10.197 | 10.640 | 353 |
| · Otros entes de derecho público | 36.149 | 1,18 | 25.845 | 10.133 | 171 |
| · Fuerzas Armadas | 123.504 | 4,02 | 116.852 | 0 | 6.652 |
| · Policía Nacional | 78.740 | 2,56 | 73.068 | 0 | 5.672 |
| · Guardia Civil | 82.609 | 2,69 | 76.539 | 0 | 6.070 |
| · Tribunales de instancia | 14.381 | 0,47 | 10.044 | 467 | 3.870 |
| Comunidades autónomas | 1.930.273 | 62,84 | 1.040.611 | 251.306 | 638.356 |
| · Universidades transferidas | 192.720 | 6,27 | 69.128 | 114.443 | 9.149 |
| Administración local | 594.898 | 19,37 | 217.309 | 287.802 | 89.787 |
| TOTAL | 3.071.725 | 100,00 | 1.686.767 | 622.045 | 762.913 |

**EPA, 3T-2026 ([INE](https://www.ine.es/jaxiT3/Tabla.htm?t=65193)) [P], miles:** Total sector público 3.736,8 · Comunidades autónomas 2.135,5 · Local 725,9 · Administración central 585,8 · Empresas e instituciones públicas 208,1 · Otro tipo 40,3 · Seguridad Social 36,2 · No sabe 5,0. EPA: es una encuesta e incluye empresas públicas, por eso no coincide con el registro. 89.900 más que en el 2T ([S], prensa sobre la nota del INE).

- **Efectivos de sanidad y docencia en las CCAA:** [VERIFICAR] (ene-2026, [VERIFICAR](https://digital.gob.es/content/dam/portal-mtdfp/funcion-publica/rcp/boletin/2026_01/revision-agosto-2026/EPSAP_Enero_2026%20.pdf)). No se ha extraído una tabla agregada por sector. Como aproximación de coste, ver la remuneración por función.

### Cuánto cuesta (Eurostat) [P]
Remuneración de asalariados (D1), cuentas nacionales. Incluye cotizaciones de empleador. Por nivel sin consolidar. El denominador por empleado mezcla perímetros: cuentas nacionales frente al registro.

| Nivel | 2025, M€ | 2024, M€ | % de su gasto | € por habitante |
| --- | ---: | ---: | ---: | ---: |
| Todas las administraciones | 181.502 | 172.737 | 23,7 | 3.645 |
| Comunidades autónomas | 113.282 | 107.998 | 39,6 | 2.275 |
| Estado | 32.574 | 30.617 | 8,7 | 654 |
| Local | 32.491 | 31.000 | 31,6 | 652 |
| Seguridad Social | 3.155 | 3.122 | 1,2 | 63 |

Por efectivo: 59.088 € en 2025. Capítulo 1 del Estado: 22.740,3 M€.

| Función | M€ | % de la remuneración |
| --- | ---: | ---: |
| Sanidad | 46.251 | 26,8 |
| Educación | 43.635 | 25,3 |
| Orden público y seguridad | 23.724 | 13,7 |
| Servicios generales | 17.894 | 10,4 |
| Asuntos económicos | 14.951 | 8,7 |
| Protección social | 9.127 | 5,3 |
| Defensa | 7.218 | 4,2 |
| Cultura y ocio | 5.684 | 3,3 |

### Comparación con la UE [P]
Remuneración de asalariados públicos, % del PIB, 2024. España es la 18.ª de 27 con el 10.8 %; la UE-27, 10.2 %. Depende de cuánto servicio público presta directamente cada país.

| País | % PIB 2024 | % PIB 2019 |
| --- | ---: | ---: |
| Dinamarca | 14,3 | 15,1 |
| Finlandia | 13,4 | 12,6 |
| Letonia | 13,2 | 11,2 |
| Croacia | 13,0 | 11,7 |
| Suecia | 12,6 | 12,7 |
| Bélgica | 12,5 | 12,3 |
| Francia | 12,4 | 12,4 |
| Estonia | 12,2 | 10,7 |
| Polonia | 11,7 | 10,2 |
| Lituania | 11,6 | 10,1 |
| Eslovaquia | 11,4 | 10,3 |
| Austria | 11,3 | 10,6 |
| Bulgaria | 11,3 | 10,0 |
| Eslovenia | 11,3 | 11,4 |
| Chipre | 11,2 | 11,7 |
| Rumanía | 11,2 | 11,4 |
| Luxemburgo | 11,1 | 10,2 |
| España | 10,8 | 10,7 |
| Portugal | 10,5 | 10,8 |
| Grecia | 10,4 | 11,8 |
| Hungría | 10,3 | 10,4 |
| Chequia | 9,6 | 9,8 |
| Malta | 9,6 | 10,4 |
| Italia | 9,0 | 9,6 |
| Países Bajos | 8,7 | 8,3 |
| Alemania | 8,3 | 8,1 |
| Irlanda | 6,1 | 6,6 |

### Cargos políticos: número
- **Diputados:** 350 escaños (XV Legislatura, [P](https://www.congreso.es/es/cem/regecodip)). Cortes disueltas el 6-oct-2026; elecciones el 29-nov-2026 (RD 806/2026).
- **Senadores:** 265 escaños (XV Legislatura, [P](https://www.senado.es/web/composicionorganizacion/senadores/regimeneconomico/index.html)). Suma de los grupos que publica el Senado.
- **Eurodiputados españoles:** 61 escaños (2024-2029, [VERIFICAR](https://www.europarl.europa.eu/spain/es/)). Sin fuente leída. Los paga el Parlamento Europeo, no el presupuesto español.
- **Diputados de los 17 parlamentos autonómicos:** [VERIFICAR] (2026, [VERIFICAR](https://www.ine.es/uc/4oGQNHVo)). No se ha encontrado un total publicado. Hay que sumar la composición de cada cámara.
- **Consejeros y altos cargos autonómicos:** [VERIFICAR] (2026, [VERIFICAR](https://www.ine.es/uc/4oGQNHVo)). Sin total publicado.
- **Alcaldes:** 8.131 municipios (2023, [S](https://mpt.gob.es/dam/es/portal/prensa/notas_de_prensa/notas/2023/06/20230617EELL.pdf)). Nota del Ministerio de Política Territorial vista en buscador; no se pudo abrir.
- **Concejales:** 66.964 concejales (2023, [S](https://mpt.gob.es/dam/es/portal/prensa/notas_de_prensa/notas/2023/06/20230617EELL.pdf)). Misma nota. Otra fuente da 67.319. Reparto por tipo de municipio: [VERIFICAR].

### Retribuciones
- **Diputado: asignación constitucional:** 3.366,99 € al mes (2026, [P](https://www.congreso.es/es/cem/regecodip)). Igual para todos, con retención de IRPF.
- **Diputado: indemnización de gastos fuera de Madrid:** 2.162,85 € al mes (2026, [P](https://www.congreso.es/es/cem/regecodip)). Exenta de IRPF. Por Madrid: 1.032,38 €. Las preguntas frecuentes de la misma web dan cifras anteriores.
- **Presidente del Congreso: complemento de Mesa:** 3.683,74 € al mes (2026, [P](https://www.congreso.es/es/cem/regecodip)). Se suma a la asignación; hay otros complementos por cargo.
- **Senador: asignación constitucional:** 3.417,54 € al mes (2026, [P](https://www.senado.es/web/composicionorganizacion/senadores/regimeneconomico/index.html)). 14 pagas. Fecha de la página no confirmada.
- **Senador: indemnización fuera de Madrid:** 2.193,50 € al mes (2026, [P](https://www.senado.es/web/composicionorganizacion/senadores/regimeneconomico/index.html)). 14 pagas. Por Madrid: 1.046,08 €.
- **Subvención a grupos del Congreso:** 30.346,72 € al mes por grupo (2026, [P](https://www.congreso.es/es/cem/regecodip)). Más 1.746,16 € al mes por diputado.
- **Alcaldes y concejales: total:** [VERIFICAR] (2023, [VERIFICAR](https://www.newtral.es/sueldos-alcaldes-2/20250306/)). ISPA publica sueldo por ayuntamiento, sin total. Unos 1.357 municipios no informaron en 2024 ([S], Newtral).
- **Parlamentos autonómicos: total de retribuciones:** [VERIFICAR] (2026, [VERIFICAR](https://www.ine.es)). Sin total publicado.

### Partidos
- **Subvención de funcionamiento a partidos:** 52,70 M€ (2025, [P](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)). Ley Orgánica 8/2007. Mismo importe en 2026 según el BOE y prensa.
- **Asignación a partidos para seguridad:** 2,70 M€ (2025, [P](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)).
- **Subvención de gastos electorales:** 2,50 M€ obligados (2025, [P](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)). Crédito 56,1 M€. Varía mucho según haya elecciones.
- **Procesos electorales:** 9 M€ obligados (2025, [P](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)). Crédito inicial 347,0 M€, reducido a 57,5 M€. Programa 924M completo: 68,0 M€.
- **Fundaciones de partidos:** 1,60 M€ (2025, [P](https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/MENSUAL%2012-25.pdf)). Exteriores, partida 1203.143A.486.
- **Subvención electoral del 29-nov-2026 por escaño:** 21.167,64 € por escaño (2026, [S](https://www.diariodeleon.es/nacional/261008/2099659/elecciones-generales-leon-2026-boe-confirma-son-ayudas-recibiran-partidos-escano-elecciones.html)). Más 0,81 € por voto al Congreso y 0,32 € al Senado. Prensa citando al BOE.

### Suma de lo publicado, Estado, 2025
Solo la suma de lo publicado a nivel del Estado en 2025. No es el coste total de los cargos políticos: faltan las comunidades autónomas y los ayuntamientos.

| Parte | M€ |
| --- | ---: |
| Congreso, Senado, Cortes común y Junta Electoral (presupuesto completo, con su personal) | 247,1 |
| Altos cargos de los ministerios (art. 10, sin tribunales ni fiscalía) | 25,6 |
| Personal eventual de los ministerios (art. 11) | 54,8 |
| Partidos: funcionamiento y seguridad | 55,4 |
| **Total** | **382,9** |

0,050 % del gasto de las AAPP de 2025 · 0,023 % del PIB · 7,69 € por habitante.

**No incluye:** Parlamentos, gobiernos y altos cargos autonómicos; Alcaldes, concejales, diputaciones y cabildos; Altos cargos y eventuales de organismos autónomos, agencias y empresas públicas; Consejos de administración de empresas públicas; Cargos de confianza de entes locales sin publicar; Eurodiputados (los paga la UE); Cotizaciones del empleador si no figuran en estos artículos.

## Opiniones
[OPINIÓN] La tabla de la suma mide lo que está publicado, no el coste real: la parte que falta (CCAA y ayuntamientos) puede ser mayor que la sumada, pero no hay dato para decir cuánto. Tampoco es comparable con otros países con estos datos.

## Sesgos de las fuentes
- **Fedea:** análisis independiente con definición propia (Seguridad Social Ampliada); suele destacar la presión sobre las pensiones. Su saldo no se compara con el del Ministerio.
- **Ministerio de Inclusión:** titula con el déficit tras transferencias, que es la lectura más favorable.
- **The Objective, Crónica Económica y El Debate:** titulares críticos con el Gobierno, y solo [S] aquí.
- **Newtral:** verificador que usa datos de ISPA; útil para ayuntamientos, sin total agregado.

## Pendiente de verificar
Número de altos cargos y eventuales por ministerio · cuantías de 2026 de cada cargo · presupuestos propios de RTVE, CNMC, CNMV y Banco de España · total de diputados, consejeros y altos cargos autonómicos · gasto de parlamentos y gobiernos autonómicos · retribuciones totales de alcaldes y concejales, y su reparto por tipo de municipio · efectivos de sanidad y docencia · eurodiputados · 490 M€ de partidas de Defensa y Economía sin clasificar por centro y destino.
