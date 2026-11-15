# C283: España, energía y vivienda por script (14-nov-2026)

Script: `scripts/leer_espana_energia.py` (sin IA ni claves, urllib con reintentos y timeout de 60 s). Salida: `explorador/espana-energia-vivienda.json` (nivel P: leído de la API oficial por script). Nota: la tarea pedía el nombre `leer_espana_energia_vivienda.py`; se usó el acordado en la orden de ejecución.

## Qué contiene (unidades explícitas)
- `precios_electricidad`: PVPC y precio spot peninsular, media/mín/máx diaria en €/MWh, últimos días completos. Fuente REE REData (mercados/precios-mercados-tiempo-real). Ej.: 13-nov-2026, PVPC media 224,23 €/MWh (leído 14-nov).
- `demanda_electrica`: demanda peninsular mensual en GWh (REE, demanda/evolucion). El mes en curso va con `parcial: true`; el dato de REE tiene fecha de actualización propia (`actualizado_ree`).
- `generacion_electrica`: generación nacional por tecnología en GWh y % renovable (REE, estructura-generacion). Oct-2026: 22.694 GWh, 48,5 % renovable según la suma de tipos «Renovable» de REE; mes en curso parcial.
- `ipv_precios_vivienda`: IPV (INE, operación 15, base 2015=100, trimestral) para Nacional y 19 CCAA/ciudades; variación anual calculada aquí sobre el índice. Último periodo publicado que devuelve la API: 2025T4 (Nacional, variación calculada +12,9 %).
- `ipva_alquiler`: Índice de Precios de Vivienda en Alquiler (INE, operación 432, anual) para Nacional y 5 CCAA. La API solo devuelve hasta 2020 (Nacional 110,942, +0,9 % sobre 2019): es una serie corta y desactualizada, NO sirve como «alquiler actual». [VERIFICAR] si el INE publica una serie más reciente en otra tabla (por ejemplo, índice de referencia de arrendamientos, op. 481, no accesible por esta vía) o MIVAU: solo en Chrome y como [S].

## Cómo encajarlo (otra sesión; no se tocó espana.json ni ningún construir_*)
1. En `explorador.py`/el construir que genere `espana.json`: añadir `espana-energia-vivienda.json` a la lista de fuentes leídas y volcar `precios_electricidad.serie` (último día), `generacion_electrica.serie[-2]` (último mes completo) y `ipv_precios_vivienda.serie` (Nacional + CCAA) en el bloque de C230 (energía) y C233 (vivienda).
2. En `vistas.html`: tabla IPV por territorio (índice, variación anual) y mini serie de PVPC; mostrar siempre `leido`, `fuente` y `unidad`. Prefijo de ids sugerido: `esp-ene-` / `esp-viv-`.
3. Regenerar con el orden habitual (ver memoria «Regenerar espana.json tras tocar el manual»): `python scripts/leer_espana_energia.py` antes del construir.
4. Periodicidad: precios y demanda, diaria/semanal; generación, mensual; IPV, trimestral; IPVA, anual.

## Límites
- Precios spot en tramos de 15 min desde 2025; la media diaria exige ≥92 datos (se descartan días incompletos).
- Hechos, sin interpretación; sin recomendaciones.
