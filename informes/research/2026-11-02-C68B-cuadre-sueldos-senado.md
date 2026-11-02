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
