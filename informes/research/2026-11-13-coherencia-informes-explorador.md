---
tema: Pasada final de coherencia entre informes y explorador tras el bloque C (España, XRP, XLM)
etiquetas: [coherencia, auditoria, explorador, españa, xrp, xlm]
actualizado: 2026-11-13
---
# Coherencia entre informes y explorador: qué se contradecía y cómo queda

Local, sin IA, 13-nov-2026. Método: buscar la misma cifra o el mismo hecho en todos los `explorador/*.json` y comparar con el informe más reciente; después, `python scripts/cobertura_hechos.py` y `python scripts/auditar_cobertura.py`.

## Contradicciones encontradas y corregidas
| # | Dónde | Qué decía | Cómo queda | Fuente |
|---|---|---|---|---|
| 1 | `espana-presupuesto.json`, programa 26BG | 2.200 M€ de obligaciones en 2024 (y 0 en otra clave del mismo archivo) | 0 en 2024; 3.300 M€ en 2025 | IGAE, MENSUAL 12-24 y Cuenta de 2024 [P] |
| 2 | `fichas-activos.json`, XRP | Aprobación final de la OCC «sigue pendiente» (dos sitios) frente a «concedida el 26-oct» en la Línea de tiempo | Condicional confirmada en occ.gov; la final solo por comunicado de Ripple [VERIFICAR] | occ.gov, 13-nov-2026 |
| 3 | `fichas-activos.json`, XRP | Evernorth: ≈ 388,1 M XRP en especie, con aviso de discrepancia con 388,9 | 388,91 M (388.910.554), con desglose; 388,1 era la misma suma sin 800.000 | SEC, 424B3 del 9-nov-2026 [P] |
| 4 | `espana-judicial.json`, Adamuz | Cuatro notas que seguían diciendo «sin leer» o «cifra final [VERIFICAR]» | Remiten a las entradas ya leídas; víctimas cerradas en 46 | BOJA y Poder Judicial [P] |
| 5 | `datos.json`, Línea de tiempo (MiCA en España) | 16 CASP con origen en España | Añadido: 17 en la lectura del 12-nov-2026 | Registro de ESMA (informe C232) [P] |
| 6 | Informe C237 del 13-nov (tercera pasada) | «El FIFO ya está en la Matriz» | No estaba; añadido a la celda España · fiscal | AEAT, Manual de Renta 2025 [P] |
| 7 | Lote de hechos 18 | «Art. 97 del Reglamento: retención del 19 %» | El tipo está en el art. 101.6 de la Ley; el 97 es la base | BOE consolidado [P] |

## Comprobado y coherente (sin cambios)
- Presupuesto del Estado de 2024 y 2025: secciones, políticas y capítulos iguales al cierre definitivo (ver informe S6).
- Adamuz: ningún JSON conserva «45 fallecidos» como cifra final. Urda: 69 en las cuatro menciones.
- Evernorth: 388,9 M en `datos.json` y `voces.json`; los «473 M» de las voces son el total (especie + comprados), ya conciliado.

## Medidor de cobertura, antes y después (hechos de nivel P)
| Ámbito | Está | Dudoso | Falta |
|---|---|---|---|
| XRP | 26 → 29 | 21 → 18 | 15 → 15 |
| XLM | 9 → 10 | 7 → 6 | 3 → 3 |
| España | 60 → 62 | 22 → 22 | 5 → 3 |

El medidor sigue sobrestimando: los «faltan» y «dudosos» que quedan son estados intermedios ya superados, hechos que están con otro formato de número o lecturas pasajeras (detalle en el informe C237, cuarta pasada).

## Huecos honestos que siguen abiertos
- Nota oficial del fallecimiento del 30-ene-2026 en Adamuz (la explicación del 46 es de nivel S; las cifras, de nivel P).
- Aprobación final de la OCC al banco de Ripple en una fuente de la OCC.
- Cifra exacta de RWA en Stellar; aplazamiento de Verifactu a 2028 (no consta en el BOE).
- Cuentas de 2025 de Adif: C243 no ejecutada, el PDF no está en el repo.
- Ejecución del Estado a septiembre de 2026: solo el total; falta el desglose (tarea C258).
- Coherencia de los ámbitos no revisados a mano: tipos, empresa, deuda, macro, geopolítica, energía, ETF y cripto.

## Lecciones (máx. 5)
1. Tras cada volcado, buscar la frase antigua en TODOS los JSON: la ficha, la Línea de tiempo y la Matriz repiten el mismo hecho con redacción distinta.
2. Un «[VERIFICAR]» resuelto deja rastro en otras entradas del mismo caso: repasarlas en la misma sesión.
3. `cobertura_hechos.py` toma su primer argumento como archivo de salida: no pasarle `--help`.
