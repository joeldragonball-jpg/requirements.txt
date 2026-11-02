# C68B · Cuadre de sueldos SE/subsecretarios/DG y complementos del Senado (2-nov-2026)

Continúa [2026-10-31-C68-sueldos-politicos.md](2026-10-31-C68-sueldos-politicos.md) (secciones 1-2 y bloque C68B). Nivel: [P] leído en original · [S] cálculo mío · [VERIFICAR] no contrastado. Sin recomendaciones.

## 1. Por qué el Portal supera a la tabla de la Ley (ya explicado el 31-oct, aquí solo el resumen)
- HECHO [P]: el art. 21.Dos de la Ley 31/2022 (BOE-A-2022-22128, texto consolidado informativo) da a secretarios de Estado, subsecretarios y directores generales sueldo + complemento de destino + complemento específico, y les asigna además un **complemento de productividad** que fija el titular del departamento sin importe en la Ley.
- Suma corregida 2026 [S]: SE €89.917 · subsecretario €79.683 · DG €68.342 al año.
- Diferencia con el Portal 2025 (medianas): ≈€48.000 (SE), ≈€50.600 (subsecretario), ≈€37.000 (DG). Productividad + trienios es la explicación razonada [ESPECULACIÓN]: no hay desglose por persona publicado que lo pruebe [VERIFICAR].
- No he tenido acceso a la cuenta de resultados de un caso concreto; el CSV del Portal da solo cargo + ministerio + total.

## 2. Cuadre con el gasto agregado (IGAE)
Cálculo propio [S] con medianas del Portal 2025 (informe del 31-oct) y número de filas:

| Categoría | n | Mediana | Total ≈ |
|---|---|---|---|
| Presidente, vicepresidentes y ministros | ~24 | ~€85.000 | €2,0 M |
| Secretarios de Estado | 41 | €137.899 | €5,7 M |
| Subsecretarios | 24 | €130.274 | €3,1 M |
| Directores generales y asimilados | 167 | €105.454 | €17,6 M |
| **Suma** | | | **≈€28,4 M** |

Frente a **€25,6 M** del art. 10 (altos cargos) de los ministerios en 2025, sin tribunales ni fiscalía (Explorador, `suma_publicada`, fuente IGAE MENSUAL 12-25; C69 da €85,4 M oficiales en 2024 con tribunales y fiscalía).
- Lectura: mismo orden de magnitud (+11 %). La mediana por n sobrestima porque las filas incluyen ceses y altas parciales y trienios, y el art. 10 puede no incluir toda la productividad ni la cuota patronal (esa va a otro artículo) [VERIFICAR].
- No cuadra al céntimo: haría falta sumar las ~755 filas de 2025 del CSV y compararlas por ministerio con su art. 10. **Queda abierto.**

## 3. Senado: complementos por cargo (senado.es, régimen económico, leído 2-nov-2026) [P]
Fecha de la página no confirmada [VERIFICAR]. Todo en 14 pagas, € al mes.
- Asignación constitucional (todos): €3.417,54.
- Presidente del Senado: asignación €3.738,69 + complemento €5.457,72.
- Vicepresidentes: €1.471,72 + €3.335,16. Secretarios: €1.149,12 + €3.064,88.
- Portavoces de grupo €3.245,51; portavoces adjuntos €2.534,75.
- Comisiones: presidentes €1.738,36; vicepresidentes y portavoces €1.270,96; secretarios y portavoces adjuntos €847,30.
- Indemnización exenta: €2.193,50 (fuera de Madrid) y €1.046,08 (Madrid). Dietas: €150/día en el extranjero, €120/día en España (no por ir a sesiones). Tarjeta taxi hasta €3.000/año.
- Complementos incompatibles entre sí, salvo presidente del Senado con presidente de comisión y portavoces de grupo con cargo en comisión.
- Comparación con el Congreso (congreso.es, 2026): asignación €3.366,99 frente a €3.417,54 del Senado (+1,5 %).

## 4. Autonomías (no hecho)
Presidente y consejeros de 1-2 comunidades: no abordado en esta sesión; ruta en el informe del 31-oct, sección 5.

## Sesgos y lecturas
- Ley (retribución fijada) y Portal (total pagado) miden cosas distintas; no se mezclan.
- Alcista/bajista: no aplica.

## Lecciones
- Con python en Bash, usar `PYTHONIOENCODING=utf8`; no usar `-I` aquí (rompe el intérprete).
- El JSON del Explorador reserializa exacto con `indent=1, ensure_ascii=False`.

## Addendum (2-nov-2026): cuadre con la suma real de las filas del Portal
**Método [P/S]:** exportación del Portal de Transparencia («Retribuciones de altos cargos», transparencia.gob.es/servicios-buscador, categoría `retribuciones_ind`), una consulta por cada uno de los 25 grupos de entes de la AGE listados en la portada, leída el 2-nov-2026 (lo publicado a 19-ene-2026). Filas de 2025: **692** únicas (el grupo de Hacienda llegó al tope de 1.000 filas, pero ordenado por año descendente, así que 2025 está completo). Suma propia con la columna «Retribución (€)»; nada de lo descargado se ejecutó. La cifra de ≈755 filas de la sesión del 31-oct venía de una exportación recortada y mezclada; esta la sustituye.

| Categoría (2025) | Filas | Suma | Media |
|---|---|---|---|
| Presidente del Gobierno | 1 | €0,10 M | €95.944 |
| Vicepresidentes (con ministerio) | 6 | €0,86 M | €142.973 (hay filas por cambio de titular) |
| Ministros/as | 19 | €1,58 M | €83.176 |
| Secretarios/as de Estado | 33 | €4,05 M | €122.610 |
| Subsecretarios/as | 22 | €2,66 M | €120.820 |
| Directores/as generales | 115 | €11,14 M | €96.851 |
| **Subtotal cargos del art. 10 «clásicos» (1-6)** | **196** | **€20,38 M** | |
| Otros (presidentes de organismos, secretarios generales, gabinetes, embajadores y mandos militares, Consejo de Seguridad Nuclear, AEPD…) | 496 | €42,71 M | €86.115 |
| **Total de las 692 filas** | **692** | **€63,09 M** | |

**Comparación con la IGAE (art. 10, altos cargos de los ministerios, 2025, sin tribunales ni fiscalía: €25,6 M):**
- Con el subtotal de cargos clásicos: €20,38 M frente a €25,6 M → faltan **€5,2 M (−20 %)**. No cuadra.
- Con las 692 filas: €63,09 M → sobran €37,5 M (+147 %), pero «Otros» incluye organismos con presupuesto propio (CSN, AEPD), embajadores y mandos militares, que no son altos cargos de las secciones ministeriales del Estado [VERIFICAR qué parte va al art. 10 y qué parte a otros artículos o secciones].
- Lectura: la cifra aproximada anterior (≈€28,4 M con medianas) sobrestimaba; la suma real de los cargos clásicos queda por debajo del art. 10. Causas posibles sin probar [ESPECULACIÓN]: el art. 10 incluye otros altos cargos asimilados clasificados en «Otros» (p. ej. secretarios generales y delegados del Gobierno) y parte de la productividad pagada por otras vías. Hace falta la suma por ministerio contra la sección IGAE de cada uno para acotarlo.
- Salvedades: la columna es lo pagado (incluye trienios y ceses/altas parciales); las filas no llevan nombre; el Portal no incluye cuota patronal, que va a otro artículo.

**Cuadra:** no. Diferencia −€5,2 M (cargos clásicos) con la IGAE. **Abierto:** cuadre por ministerio y clasificación de «Otros».
