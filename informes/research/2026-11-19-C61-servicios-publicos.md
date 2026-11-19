# C61 · Servicios públicos en las fichas de países (19-nov-2026)

**Qué se hizo:** el campo `sistemas_publicos` de `explorador/paises.json` de los 12 países de C58 (ES, DE, FR, IT, NL, PL, US, CN, JP, IN, GB, RU) pasó de «[VERIFICAR] pendiente de C61» a un texto con sanidad, educación, pensiones, paro y estabilidad social. Los otros 13 países siguen en null (fuera del alcance de C58).

**Fuentes (nivel P, leídas el 19-nov-2026):** API del Banco Mundial (WDI: OMS GHED, UN IGME, OIT modelado, WGI) y los datos ya leídos en `explorador/estabilidad.json` (Eurostat, COFOG). Contraste: el gasto sanitario total de la API del Banco Mundial coincide con `estabilidad.json` en los 12 países (diferencia máx. 0,3 pp; ES 9,2 % en 2023, US 16,7 % en 2023, DE 12,3 % en 2024, IN 3,3 % en 2023, JP 10,7 % en 2023).

**Huecos (null, no rellenados):** edad de jubilación y gasto en pensiones fuera de la UE/GB (sin fuente leída; OCDE Pensions at a Glance no consultada); PISA; huelgas y protestas grandes salvo ES (huelga médica, nivel S) y US (recorte del Departamento de Educación, nivel S); vivienda no es parte de este campo.
**Notas de comparabilidad:** médicos y camas con definiciones nacionales; el paro de China, India y Rusia es modelado por la OIT; WGI es percepción agregada.
**Validación:** `revisar_explorador.py` 0 avisos; `validar_ids.py` 3 fallos previos y ajenos (elecciones.json: GM, NZ, NG).
