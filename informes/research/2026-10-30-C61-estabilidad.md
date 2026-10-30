# C61 · Servicios públicos y estabilidad social de 12 países (30-oct-2026)

Código: `scripts/estabilidad.py`. Resultado: `explorador/estabilidad.json` (19-20 cifras por país, 234 en total); lecturas en `explorador/estabilidad-manual.json`. Sin claves ni IA.

**Fuentes [P]:** Banco Mundial (OMS GHED, UNODC, WGI, ONU) para los 12 países; Eurostat (sobrecarga del coste de la vivienda, ilc_lvho07a) para los 6 de la UE. Solo cifras publicadas, con año y nota de comparabilidad; ningún índice propio ni ranking.

**Cubierto:** sanidad (gasto, por habitante, vida, mortalidad infantil, médicos, camas), banda ancha y dependencia energética, empleo vulnerable, gasto en educación, homicidios y gobernanza (WGI), demografía y migración; sobrecarga de vivienda en la UE. Lectura de 3-4 líneas por país [OPINIÓN].

**Huecos:** sin datos de vivienda fuera de la UE; faltan inversión pública, LPI, precio de la electricidad, pensiones, subsidio de desempleo, PISA, abandono escolar, natalidad y migración de fuentes nacionales, IPC de Transparencia Internacional y los hitos/reformas por país (campo «hitos» vacío, [VERIFICAR]). Años distintos entre países (2020-2025).

**Cifras para contrastar con la fuente oficial:** vida en España 83,9 años (2024), gasto sanitario de EE. UU. 16,7 % del PIB (2023), sobrecarga de vivienda en Alemania 11,2 % (2025), homicidios en EE. UU. 5,76 por 100.000 (2023), población de 65 años o más en Japón 30,0 % (2025).

**Cuidado:** los WGI y la corrupción son percepciones; China y Rusia (homicidios, sanidad) son cifras de organismos internacionales sobre datos oficiales, no verificables aquí.
