---
tema: Cierre definitivo del presupuesto del Estado de 2023, 2024 y 2025 (Cuenta de la Administración General del Estado, IGAE) (S6 = C69)
etiquetas: [españa, igae, presupuesto, cierre, cuenta-general, vivienda, ico]
actualizado: 2026-11-13
---
# S6 · C69: el cierre definitivo de la IGAE confirma las cifras y corrige un programa

Lecturas del 13-nov-2026. M€ = millones de euros. Datos en `explorador/espana-presupuesto.json` (clave nueva `cierre_definitivo`, dos líneas nuevas en «Cómo leerlo» y corrección del programa 26BG).

## HECHOS

### El cierre definitivo existe y coincide con lo provisional [P]
La IGAE publica cada agosto el «Resumen de la Cuenta de la Administración General del Estado» (la cuenta rendida, firmada por el Interventor General). Leídos los de 2023 (2-ago-2024), 2024 (4-ago-2025) y 2025 (4-ago-2026).

| Año | Crédito inicial | Crédito definitivo | Obligaciones reconocidas | Derechos reconocidos netos | Saldo no financiero | Resultado presupuestario |
|---|---|---|---|---|---|---|
| 2023 | 386.088,1 M€ | 407.082,8 M€ | 371.288,9 M€ | 369.756,3 M€ | −40.799,6 M€ | −1.532,5 M€ |
| 2024 | 380.822,4 M€ | 433.163,4 M€ | 408.563,6 M€ | 390.374,2 M€ | −35.513,2 M€ | −18.189,5 M€ |
| 2025 | 380.822,4 M€ | 457.766,3 M€ | 423.336,3 M€ | 433.284,3 M€ | −35.178,5 M€ | +9.948,0 M€ |

- Variación de las obligaciones: +10,0 % en 2024 y +3,6 % en 2025 (cálculo nuestro).
- **Comparación con la Órbita:** las 37 secciones, las 26 políticas y los 9 capítulos de 2024, y las 37 secciones y los capítulos de 2025, coinciden con lo que ya estaba cargado desde los PDF mensuales de diciembre (diferencia máxima de 0,1 M€, por redondeo). El «cierre definitivo» no cambia ninguna cifra de sección.
- El saldo no financiero es derechos menos obligaciones sin activos ni pasivos financieros (cálculo nuestro para 2023 con los totales del documento). El resultado presupuestario total incluye la deuda emitida y amortizada: su paso de −18.189 a +9.948 M€ no significa superávit.
- Capítulos de 2024: personal 21.157,0 M€; bienes y servicios 5.793,4; intereses 35.454,0; transferencias corrientes 156.387,1; inversiones reales 11.371,3; transferencias de capital 18.532,6; activos financieros 41.750,4; amortización de deuda 118.117,8.

### Corrección: el préstamo ICO de vivienda (programa 26BG) [P]
- En 2024 se aprobó y se comprometió un crédito de 2.200 M€, pero **no se reconoció ninguna obligación** (IGAE, MENSUAL 12-24: columnas de obligaciones y pagos en blanco). La Órbita daba 2.200 M€ de obligaciones porque se había leído la columna de gastos comprometidos.
- Lo confirma el cierre definitivo: la sección de Vivienda reconoció 1.367,2 M€ en todo 2024 y dejó 2.625,5 M€ de remanentes comprometidos.
- En 2025 sí se reconocieron 3.300 M€, sin pagos ese año (MENSUAL 12-25). La variación correcta es de 0 a 3.300 M€, no «+50 %».
- El mismo JSON se contradecía: el desglose por ministerio ya daba 0 en 2024. Ahora coinciden.

### Las cuatro notas [VERIFICAR] de programas
- Igualdad de oportunidades (232B), cooperación (143A) y apoyo tecnológico a la defensa (464B): ya estaban verificadas el 4-nov contra el MENSUAL 12-24; el campo de pendientes del Seguimiento estaba desfasado.
- Vivienda-ICO (26BG): resuelta hoy (ver arriba).

### Dato nuevo: ejecución hasta septiembre de 2026 [P]
- La IGAE publicó el 4 y el 6-nov-2026 la ejecución hasta el 30-sep-2026: crédito definitivo 462.582,4 M€; obligaciones reconocidas 296.527,3 M€ (64,1 %); pagos 290.936,3 M€. La Órbita tenía agosto (280.337,1 M€). Anotado solo el total; el desglose por sección y programa a septiembre queda como tarea aparte.

## NO HECHO (y por qué)
- **SEPE 2024 mensual** y **euros reales por programa y centro (IPC)**: no tocados en esta sesión.
- **COFOG 2025:** Eurostat sigue sin publicarlo para España (comprobado el 12-nov-2026).

## OPINIÓN (mía)
- Lo que más pesa: tres años con el mismo presupuesto inicial prorrogado (380.822 M€ en 2024 y 2025) y un crédito definitivo que cada año se aleja más (+52.341 M€ de modificaciones en 2024; +76.944 M€ en 2025). A favor: las ampliaciones pagan compromisos reales (deuda, pensiones, financiación territorial). En contra: una quinta parte del gasto se decide por modificaciones de crédito, sin ley de presupuestos votada.
- El caso del ICO enseña a distinguir «comprometido» de «reconocido» y de «pagado»: 2.200 M€ anunciados en 2024 no eran gasto de 2024.

## Lecciones (máx. 5)
1. El cierre definitivo del Estado está en `…/CPE/rcasp/Documents/RESUMEN CAGE AAAA.pdf` (16 páginas); se publica a primeros de agosto.
2. La web de la IGAE corta las conexiones de scripts; el navegador integrado sí lee el PDF con pdf.js sin descargar nada.
3. En las tablas mensuales de la IGAE, antes de las obligaciones van «gastos autorizados» y «gastos comprometidos»: contar columnas.
4. Cuando el mismo dato está en dos claves de un JSON, compararlas: aquí una ya decía 0.
5. Validar toda transcripción de tabla con la suma contra el total del documento.

## Fuentes
- IGAE, Cuenta de la AGE 2024: https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/rcasp/Documents/RESUMEN%20CAGE%202024.pdf (2023 y 2025: misma ruta con el año)
- IGAE, MENSUAL 12-24 y 12-25: copias en `research/fuentes/`
- IGAE, ejecución a septiembre de 2026: https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/BOE%2009-26.pdf
- BOE-A-2025-15914 (31-jul-2025): referencia al Registro de cuentas anuales del sector público de 2024
