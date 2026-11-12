# C68B · Sueldos SE / subsecretarios / DG: Ley vs Portal (12-nov-2026)

Continúa los informes del 2, 6, 10 y 11-nov. Nivel: P = fuente oficial leída · S = prensa o cálculo propio · [VERIFICAR]. Solo hechos; sin recomendaciones.

## Datos (euros brutos/año)
| Dato | Valor | Periodo | Fuente | Nivel |
|---|---|---|---|---|
| SE · retribución fija (sueldo+CD+CE+2 extras) | 89.917 € | 2026 | Hacienda, cuantías 2026 (art. 21.Dos, Ley 31/2022 prorrogada) | P (suma propia S) |
| Subsecretario · fija | 79.683 € | 2026 | ídem | P/S |
| DG · fija | 68.342 € | 2026 | ídem | P/S |
| SE / Subs. / DG · fija 2025 estimada (2026 / 1,015) | ≈88.600 / 78.500 / 67.300 € | 2025 | derivado; supone que el +1,5 % de 2026 afecta a todos los conceptos | S [VERIFICAR] |
| Portal, mediana 2025: SE / Subs. / DG | 137.899 / 130.274 / 105.454 € | 2025 (act. 19-ene-2026) | transparencia.gob.es, retribuciones_ind | P (lectura previa) |
| Brecha mediana Portal − fija 2025 estimada | ≈49.300 / 51.800 / 38.100 € | 2025 | cálculo propio | S |
| Suma Portal cargos clásicos (196 filas) vs IGAE art. 10 | 20,38 M€ vs 25,6 M€ (faltan 5,2 M€, −20 %) | 2025 | Portal / IGAE (informe 2-nov) | P/S |
| Senado: asignación 3.417,54 €/mes; presidente: 3.738,69 + complemento 5.457,72 €/mes | | 2026 | senado.es, régimen económico (leído 2-nov) | P |

Contexto normativo nuevo leído: Resolución de 2-jul-2025 de la SEPG (BOE-A-2025-13617, BOE 3-jul-2025): instrucciones de pago del +0,5 % adicional del RDL 4/2024 con efectos de 1-ene-2024, aplicable expresamente a altos cargos (apartado III). No contiene tabla de cuantías [P].

## Qué se puede afirmar
- HECHO [P]: el art. 21.Dos da sueldo, CD y CE y "el complemento de productividad que, en su caso, se asigne" (sin importe en la Ley); trienios aparte. Ninguno está en la suma fija.
- HECHO [S]: la brecha se mantiene en ≈38.000-52.000 € por cargo con cualquier año base; el orden de magnitud no depende de los años distintos.
- ESPECULACIÓN: productividad + trienios la explican. Sin desglose por persona (el Portal da cargo, ministerio y total) no se puede probar. Los 2-3 casos concretos del CSV no aportan más: no hay columna de conceptos.
- Contraste: el Portal es lo pagado (ceses, altas parciales, trienios); la Ley es lo fijado. No comparables al céntimo.

## Huecos / bloqueado
- No localizada la tabla oficial 2025 de Hacienda (solo búsquedas; las resoluciones del Consejo de Transparencia R CTBG 2024-1271 devolvieron 404/redirección).
- Desglose individual de productividad: solo por solicitud de acceso (Ley 19/2013), texto en research/MANUAL-PARA-JOEL.md.
- Cuadre por ministerio contra cada sección IGAE y clasificación de «Otros» (496 filas, 42,71 M€): pendiente [VERIFICAR].
- Presidentes/consejeros de CCAA: no tocados.

## Lecciones
- Con python en Bash usar `python` (sin `-I`: rompe el intérprete en esta máquina).
- `pdftotext -layout` + iconv latin1→utf-8 lee bien los PDF del BOE guardados por WebFetch en tool-results.
- Cuarta sesión sin cerrar el cuadre: el dato que falta no es público; no repetir lecturas, pedir el acceso.
