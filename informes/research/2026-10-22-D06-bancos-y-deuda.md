# D06 · Bancos y deuda: (a) deuda soberana que tienen, (b) deuda que emiten, (c) balances de bancos centrales (22-oct-2026)

Hecho por Claude (sin Gemini). Sin recomendaciones. El detalle por banco está en el panel «Deuda por banco» (`explorador/bancos-eba.json`, generado con `scripts/preparar_bancos_eba.py`).

## Resumen
- **(a) Deuda soberana en el balance de cada banco:** 116 bancos europeos suman €3.914 mil M de exposición soberana directa a 30-jun-2025 (EBA). Santander €212,7 mil M, BBVA €135,6, CaixaBank €102,5, BNP €366,2, UniCredit €149,4, Intesa €133,5. Los 10 bancos españoles de la muestra: €603 mil M, de ellos €302 mil M de deuda de España.
- **(b) Deuda que emiten los propios bancos** (bonos, cédulas y subordinada, en su pasivo): Crédit Agricole €366,6 mil M, BNP €346,5, BPCE €344,6, Santander €314,5 (€31,0 de subordinada), Société Générale €259,1; BBVA €77,1, CaixaBank €51,4, Intesa €129,4, UniCredit €109,2 [EBA, 30-jun-2025].
- **(c) Balances de bancos centrales:** Fed $4.570,6 mil M en bonos del Tesoro; Eurosistema €1.642,7 mil M (PSPP) + €1.268,8 mil M (PEPP); Banco de Japón ~50 % de los JGB (ver D07).

## Hechos verificables
| Dato | Fecha | Fuente | Tipo |
|---|---|---|---|
| Exposición soberana directa por banco y país emisor | 30-jun-2025 y 31-dic-2024 | EBA, ejercicio de transparencia 2025 (tr_sov.csv) | Oficial [P] |
| Deuda emitida por el banco («Debt securities issued» y subordinada) | 30-jun-2025 | EBA, tr_oth.csv, hoja Liabilities | Oficial [P] |
| Capital CET1 y activos totales | 30-jun-2025 | EBA, tr_oth.csv | Oficial [P] |
| Fed: bonos del Tesoro $4.570,6 mil M; total activos $6.755,6 mil M | 14-oct-2026 | Federal Reserve, H.4.1 | Oficial [P] |
| Eurosistema: PSPP €1.642,7 mil M; PEPP €1.268,8 mil M | 16-oct-2026 | BCE, estado semanal | Oficial [P] |

## Contradicciones y cuidados
- El ejercicio de transparencia de la EBA **se interrumpe desde junio de 2025**; la EBA remite al Pillar 3 Data Hub (en marcha desde el 26-ene-2026 para grandes entidades). El corte más reciente de esta fuente es 30-jun-2025: **hay un hueco de más de un año** frente a hoy.
- La «exposición soberana» de la EBA es valor contable bruto de activos no derivados (bonos **y préstamos**) frente a cada país, e incluye agregados regionales (p. ej. Latinoamérica es el mayor emisor de Santander). Su alcance exacto (administraciones centrales, regionales y locales; bancos centrales) no se ha leído en la guía de la EBA [VERIFICAR].
- La deuda emitida está medida a valor contable y a nivel consolidado: no equivale al saldo vivo de bonos de cada banco en los mercados.

## Qué NO he podido comprobar [VERIFICAR]
- Cortes posteriores a junio de 2025: están en el Pillar 3 Data Hub (portal edap-public.eba.europa.eu); no se ha podido procesar aquí.
- Detalle de cada emisión (importe, vencimiento, cupón) de los bonos de cada banco: se encuentra en sus folletos e informes anuales y no se ha leído.
- Balance del Banco de Japón actualizado (importe en yenes de JGB a fin de septiembre).

## Fuentes
eba.europa.eu/eu-wide-transparency-exercise-0 (tablas tr_sov.csv, tr_oth.csv, TR_Metadata.xlsx, leídas el 22-oct-2026); federalreserve.gov (H.4.1 del 15-oct-2026); ecb.europa.eu (estado financiero consolidado del Eurosistema a 16-oct-2026).

## Caso alcista / bajista (añadido 27-oct-2026, C27; sin predicción, solo con datos de este informe)
Tema: ¿es sana la relación entre los bancos europeos y la deuda soberana que tienen?
- **Alcista (sistema más sólido):** la exposición está repartida (116 bancos, €3.914 mil M) y la EBA publica el detalle por banco y país emisor; los grandes tienen deuda soberana propia de su país pero también diversificada (Latinoamérica es el mayor emisor de Santander).
- **Bajista (riesgo de contagio):** los 10 bancos españoles de la muestra acumulan €302 mil M de deuda de España, así que un problema del emisor golpea al banco; el último corte (30-jun-2025) tiene más de un año de retraso y no se puede comprobar si cambió [VERIFICAR].
- **Sesgo:** el dato mide valor contable bruto (bonos y préstamos), no pérdida potencial; ninguna de las dos lecturas sale solo de esta tabla.
