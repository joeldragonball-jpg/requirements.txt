# Guía G2: Cómo funciona un banco (España y zona euro, 10-oct-2026)

> **Guía educativa, no es recomendación** de contratar, mantener o cambiar ninguna cuenta, producto o entidad. Foco en España, para un inversor particular a largo plazo. Fuentes **primarias** leídas hoy: Fondo de Garantía de Depósitos (FGD), Banco de España (coeficiente de reservas; decisión del BCE; notas del Informe de Estabilidad Financiera). Lo demás procede de **búsquedas y fuentes secundarias** y va con [VERIFICAR]. Predicciones: [ESPECULACIÓN]. Los ejemplos numéricos son **ilustrativos y cálculo mío**, no datos de ningún banco real. Complementa a la [G1](2026-10-10-G1-tipos-e-inflacion.md) (tipos e inflación).

## 0. Resumen en 8 líneas
1. Un banco **toma dinero a corto plazo (depósitos) y lo presta a más largo plazo**. Ese desfase de plazos es su negocio y su principal fragilidad.
2. Opera con **poco capital propio** (apalancamiento alto): una pérdida relativamente pequeña sobre los activos se come el capital.
3. El banco **no guarda tu dinero en una caja**: solo mantiene una pequeña parte en reservas (el BCE exige un coeficiente mínimo del **1 %** sobre determinados pasivos).
4. **Fondo de Garantía de Depósitos (FGD): hasta 100.000 € por depositante y entidad.** No cubre fondos de inversión, acciones ni bonos (FGD).
5. Si un banco es inviable, no se "rescata con dinero público" por defecto: se aplica la **resolución** y primero pierden **accionistas y acreedores** (bail-in).
6. La normativa (Basilea III, en la UE con **CRR3/CRD6**, mayoría de disposiciones desde el 1-ene-2025) obliga a más capital y liquidez [VERIFICAR].
7. Según el Banco de España (Informe de Estabilidad Financiera, primavera 2026), la **rentabilidad bancaria mejoró moderadamente en 2025 con menor margen de intereses**; cifras de solvencia y morosidad **no las he podido leer** [VERIFICAR].
8. Cripto: **un exchange no es un banco** y no está cubierto por el FGD (ver §9).

## 1. Glosario corto
| Término | Significado sencillo |
|---|---|
| **Depósito** | Dinero que dejas al banco; el banco te debe devolverlo y te paga (o no) un interés. |
| **Activo / pasivo** | Activo = lo que el banco posee o le deben (préstamos, bonos). Pasivo = lo que debe (depósitos, deuda). |
| **Capital (fondos propios)** | Lo que absorbe pérdidas antes que los depositantes. |
| **CET1** | Capital de máxima calidad (acciones y reservas) en relación con los activos ponderados por riesgo. |
| **Liquidez** | Capacidad de pagar retiradas de dinero a corto plazo. |
| **LCR / NSFR** | Ratios de liquidez de Basilea III: a 30 días / a un año. |
| **Reservas mínimas (coeficiente de caja)** | Porcentaje de ciertos pasivos que el banco debe mantener en el banco central. |
| **FGD** | Fondo de Garantía de Depósitos: paga hasta 100.000 € por depositante y entidad si el banco quiebra. |
| **Resolución** | Procedimiento ordenado para gestionar un banco inviable sin pararlo. |
| **Bail-in** | Pérdidas asumidas por accionistas y acreedores del banco (en lugar de los contribuyentes). |
| **MREL** | Colchón mínimo de pasivos que pueden absorber pérdidas o convertirse en capital en una resolución. |
| **FROB / JUR** | Autoridad de resolución ejecutiva en España / Junta Única de Resolución (zona euro). |

## 2. Qué hace un banco y cómo gana dinero
**Hechos (explicación general)**
- **Intermediación:** capta ahorro (depósitos, deuda) y concede crédito (hipotecas, empresas, consumo) y compra bonos.
- **Margen de intereses:** diferencia entre lo que cobra por los préstamos y lo que paga por los depósitos y la deuda. Es su ingreso principal en un banco comercial.
- **Comisiones:** cuentas, tarjetas, gestión de fondos, seguros, medios de pago.
- **Efecto de los tipos:** si suben, el banco suele cobrar más por los préstamos, pero compite por los depósitos y puede sufrir más impagos. Su efecto neto depende de cada entidad (ver G1). Según el BdE, el **margen de intereses descendió en 2025** (momento de tipos más bajos) [VERIFICAR con el informe completo].

**Balance simplificado (ejemplo ilustrativo, cálculo mío)**
| Activo | Importe | Pasivo y capital | Importe |
|---|---|---|---|
| Préstamos | 70 | Depósitos de clientes | 85 |
| Bonos | 20 | Deuda emitida | 5 |
| Caja y reservas | 10 | Capital | 10 |
| **Total** | **100** | **Total** | **100** |
- El capital es el **10 %** del balance: si el 10 % de los activos se vuelve incobrable (por ejemplo, préstamos impagados), el capital desaparece y empiezan a perder los acreedores. Por eso importan la calidad de los préstamos y el capital.
- Si los clientes retiran el **15 %** de los depósitos de golpe (12,75 de 85) y en caja solo hay 10, el banco tiene que vender activos con prisa o pedir liquidez al banco central. Eso es una **corrida bancaria** (*bank run*).

## 3. ¿Dónde está tu dinero? Reservas y creación de crédito
- **Reservas mínimas:** el BCE fija un coeficiente que desde 2012 es del **1 %** (antes 2 %) sobre determinados pasivos, depositado en el banco central ([Banco de España](https://www.bde.es/wbe/es/areas-actuacion/politica-monetaria/politica-monetaria-area-euro/tipos-interes-bce/que-es-el-coeficiente-de-caja-o-coeficiente-de-reservas.html)). La página leída no dice si se remuneran [VERIFICAR].
- **No hay "caja con tu dinero":** cuando un banco concede un préstamo, abona el importe en la cuenta del cliente y así **aparece un depósito nuevo**. Los bancos crean dinero con el crédito, dentro de los límites de capital y liquidez. Es la explicación habitual de bancos centrales (el BCE y el Banco de Inglaterra la han publicado) [VERIFICAR fuente exacta].
- **Consecuencia práctica:** un depósito es un **derecho de cobro frente al banco**, no una propiedad guardada. La protección real viene de capital, supervisión, FGD y resolución (secciones siguientes).

## 4. Riesgos de un banco
| Riesgo | Qué es | Ejemplo (hecho) |
|---|---|---|
| **Crédito** | Que los prestatarios no paguen | Crisis financiera 2008-2012 en España (cajas y promoción inmobiliaria) |
| **Liquidez** | Que no pueda atender retiradas | Corrida en SVB, marzo 2023 |
| **Tipo de interés** | Que subidas de tipos reduzcan el valor de los bonos que tiene | SVB tenía bonos que habían perdido valor tras la subida de tipos de 2022 (G1) |
| **Concentración** | Pocos clientes/sectores | SVB dependía de clientes del sector tecnológico (de memoria) [VERIFICAR] |
| **Operativo / ciber** | Fallos, fraude | — |
| **Contagio** | Un problema se extiende | Credit Suisse, adquirido por UBS el 19-mar-2023 tras SVB |
Fuente de las fechas de 2023: resumen de prensa por buscador (SVB cae el 10-mar; Signature, el 12-mar; Credit Suisse, el 19-mar) [VERIFICAR].

## 5. Regulación y supervisión (capital y liquidez)
**Hechos**
- **Basilea III** (acuerdo del Comité de Basilea tras 2008) exige más capital de calidad, un colchón de liquidez (LCR) y financiación estable (NSFR).
- En la UE se aplica con **CRR/CRD**. La actualización **CRR3/CRD6** se publicó a mediados de 2024 y **la mayoría de sus disposiciones son aplicables desde el 1-ene-2025**; el llamado *output floor* se introduce de forma gradual hasta **2030** [VERIFICAR: fuente secundaria].
- **Supervisión:** el **BCE** supervisa directamente a los bancos grandes (Mecanismo Único de Supervisión); el **Banco de España** supervisa el resto y colabora con el BCE.
- **Ratio de capital (CET1):** cuanto más alto, más pérdidas aguanta. No hay un número "seguro" universal; depende del perfil de riesgo de cada banco [ESPECULACIÓN si se interpreta como garantía].

**Situación actual (España)**
- Según la presentación del Banco de España del Informe de Estabilidad Financiera de primavera 2026 (14-mayo-2026), la **rentabilidad (ROA) mejoró moderadamente en 2025**, con **descenso del margen de intereses**; el endeudamiento y la carga financiera de **hogares** se mantienen en niveles históricamente reducidos y la deuda **empresarial** continúa bajando ([BdE](https://www.bde.es/wbe/es/publicaciones/estabilidad-financiera-politica-macroprudencial/informe-estabilidad-financiera/informe-de-estabilidad-financiera-primavera-2026.html)).
- **No he podido leer** las cifras de CET1, morosidad ni liquidez: el PDF no se descargó como texto [VERIFICAR en el capítulo 3 del informe].
- Desde entonces (G1) el BCE ha subido tipos dos veces (junio y septiembre de 2026) y la inflación en España es del 4,9 %: el efecto sobre morosidad y margen se verá en el informe de otoño [ESPECULACIÓN].

## 6. El Fondo de Garantía de Depósitos (FGD)
**Hechos (fuente primaria: [FGD](https://www.fgd.es/es/))**
- Garantiza **hasta 100.000 € por depositante y por entidad**. Se **suman** todos tus depósitos en la misma entidad (cuenta corriente, ahorro, depósito a plazo).
- **Excepciones temporales:** durante **tres meses** tras ciertas operaciones (venta de vivienda habitual, matrimonio/divorcio, jubilación, despido, invalidez o muerte, indemnizaciones o seguros) la cobertura puede ser **superior** al límite.
- **No cubre:** fondos de inversión, valores, acciones y bonos. Tampoco depósitos de ciertas entidades (aseguradoras, sociedades de inversión).
- **Moneda extranjera:** se convierte al tipo de cambio de la fecha de la declaración de insolvencia.
- **Aviso del FGD sobre neobancos y fintech:** la cobertura de tus fondos **puede proceder de otro sistema de garantía distinto** del español. Hay que comprobar cuál protege tu dinero.
- **Plazo de reembolso:** **7 días hábiles desde el 1-ene-2024** (fuentes de entidades; [VERIFICAR en el FGD]).
- **Cuentas conjuntas:** el límite se aplica a **cada titular** por separado (fuentes de entidades) [VERIFICAR].

**Ejemplo numérico (cálculo mío).** María tiene en el mismo banco 90.000 € en una cuenta de ahorro y 20.000 € en una corriente: total 110.000 €; el FGD cubre 100.000 € y 10.000 € quedan fuera (se recuperarían, en su caso, como acreedor ordinario en el proceso). Si repartiera lo mismo entre dos bancos distintos, cada uno estaría por debajo de 100.000 €. **Esto describe el mecanismo; no es un consejo de repartir ni de no repartir.**

**Quién lo financia.** El FGD se nutre de aportaciones de las propias entidades, no del presupuesto del Estado (explicación general) [VERIFICAR].

## 7. Resolución bancaria: qué pasa si un banco falla
**Hechos**
- Marco europeo: la **BRRD** (2014), transpuesta a España. Autoridades: **Banco de España** (preventiva) y **FROB** (ejecutiva); para bancos grandes, la **Junta Única de Resolución (JUR)**, con un **Fondo Único de Resolución (FUR)** que alcanzó unos **78.000 M€** a fin de 2023, el nivel objetivo (1 % de depósitos garantizados) [VERIFICAR: fuente secundaria].
- **Bail-in:** las pérdidas se reparten entre accionistas y acreedores antes de usar dinero público.
- **MREL:** cada banco debe tener un volumen mínimo de pasivos "absorbibles" (al menos el 8 % del balance en el planteamiento general) [VERIFICAR].
- **Orden de pérdidas (simplificado, de memoria)** [VERIFICAR]: 1) accionistas → 2) bonos de capital (AT1/CoCos) → 3) deuda subordinada → 4) deuda senior no preferente y otros acreedores → 5) depósitos **por encima de 100.000 €** (con prelación para personas y pymes) → **los depósitos cubiertos (hasta 100.000 €) no sufren pérdidas** en un bail-in: los cubre el FGD.

**Caso real: Banco Popular (junio de 2017).** El 7-jun-2017 la JUR resolvió el banco: se **amortizó el 100 % de las acciones**, se convirtieron en acciones los instrumentos de capital adicional de nivel 1 y el capital de nivel 2 (deuda subordinada), y el banco se vendió a **Banco Santander por 1 €** ([resumen de prensa y Caixabank Research por buscador] [VERIFICAR en la JUR/FROB]). Los depositantes mantuvieron su dinero; los accionistas y los tenedores de ciertos bonos perdieron. Fue un hecho; si fue **justo** o si la gestión de la información fue adecuada es **opinión** y hubo litigios [ESPECULACIÓN].

## 8. Qué significa en la práctica (marco, sin recomendar nada)
Preguntas que conviene hacerse **antes** de contratar cualquier cosa (no son un consejo, son un esquema):
1. ¿Es un **depósito** o es otra cosa (fondo, bono, producto estructurado)? Solo los depósitos están dentro del FGD.
2. ¿Qué **entidad** es y qué **sistema de garantía** la cubre (español u otro país)?
3. ¿Cuánto tengo **en total** en esa entidad (suma de todo)?
4. ¿Qué **rentabilidad real** me da (G1) y cuál es la **comisión**?
5. ¿Cuándo puedo **retirar** el dinero y con qué penalización?
6. ¿Quién **custodia** lo que tengo (banco, bróker, exchange)? Los fondos de inversión y valores se mantienen **separados** del balance del banco, de modo que la quiebra del banco no los arrastra, pero esa protección tiene sus matices y límites (por ejemplo, el Fondo de Garantía de Inversiones) [VERIFICAR en la CNMV, ver G5/G8].
7. Productos de renta fija "como depósitos" (**bonos del propio banco**, participaciones preferentes) **no son depósitos** y pueden sufrir pérdidas; es un patrón histórico de venta inadecuada [VERIFICAR con CNMV].

## 9. Relación con cripto (XRP / XLM)
- Un **exchange o plataforma cripto no es un banco**: no tiene licencia bancaria, su efectivo **no está cubierto por el FGD** y los criptoactivos no son depósitos. En la UE, **MiCA** regula a los proveedores de servicios de criptoactivos, pero no equivale a una garantía de depósitos [VERIFICAR alcance].
- Si tu euro se queda en la cuenta de la plataforma, puede estar en una cuenta bancaria segregada o no; hay que leer las condiciones [VERIFICAR].
- Para custodia y seguridad de XRP y XLM, ver el [dossier de custodia](2026-10-09-custodia-y-seguridad.md). Para stablecoins y su "respaldo", el [dossier de stablecoins](2026-10-09-stablecoins.md). Para el euro digital, el [dossier de euro digital](2026-10-09-euro-digital-cbdc.md).

## 10. Errores comunes y señales a vigilar
**Errores comunes**
1. **Creer que todo lo que vende un banco está garantizado.** Solo los depósitos (hasta 100.000 €).
2. **Olvidar sumar** todas las cuentas de la misma entidad al contar el límite del FGD.
3. **Confundir "banco" con "neobanco/fintech/exchange"**: puede cubrir otro país o ninguno.
4. **Pensar que una corrida bancaria es solo "pánico irracional"**: puede reflejar un problema real de liquidez o de bonos.
5. **Buscar solo la rentabilidad más alta** sin mirar el sistema de garantía y la inflación (G1).
6. **Creer que el "rescate" es automático**: en la UE el diseño es que paguen primero accionistas y acreedores.
7. **Mirar un único dato** (por ejemplo, el CET1) sin contexto: capital, liquidez y calidad de los activos van juntos.

**Señales a vigilar (calendario y datos)**
| Qué | Cuándo / dónde | Qué mirar |
|---|---|---|
| **Informe de Estabilidad Financiera (otoño 2026)** | Banco de España, normalmente en noviembre [VERIFICAR] | CET1, morosidad, margen, impacto de la subida de tipos |
| **Reunión del BCE** | 28-29-oct y 16-17-dic | Tipos y proyecciones (G1); efecto en márgenes y crédito |
| **Resultados trimestrales de bancos** | Finales de octubre (3T) [VERIFICAR] | Morosidad, provisiones, margen de intereses |
| **Test de estrés de la EBA / BCE** | Periódico | Resistencia a escenarios adversos [VERIFICAR calendario] |
| **FGD / FROB / JUR** | Comunicados oficiales | Cualquier resolución o intervención |
| **Condiciones de tu entidad** | Contrato y ficha del FGD | Qué sistema de garantía te cubre |

## 11. Lo que no sé / no he podido verificar
- **Cifras actuales de solvencia (CET1), morosidad y liquidez** de la banca española: el PDF del Banco de España no se pudo leer. Hay que consultar el capítulo 3 del Informe de Estabilidad Financiera.
- Plazo exacto de reembolso del FGD y tratamiento de **cuentas conjuntas**: citado por fuentes de entidades, no por el FGD.
- **Orden detallado** del bail-in y reformas recientes del marco europeo (revisión CMDI) y su estado de transposición.
- **Tamaño del FUR** más allá de 2023.
- Detalle de CRR3/CRD6 y calendario del *output floor*.
- Si las **reservas mínimas** se remuneran hoy y a qué tipo.
- No evalúo la solidez de ninguna entidad concreta, ni recomiendo ni desaconsejo entidades.

## 12. Guías relacionadas
G1 ([tipos e inflación](2026-10-10-G1-tipos-e-inflacion.md)), G4 (depósitos y cuentas), G5 (hipotecas), G8-G9 (inversión), G12 (fiscalidad), G15 (asesores y reclamaciones). Ver [MAPA](MAPA.md).
