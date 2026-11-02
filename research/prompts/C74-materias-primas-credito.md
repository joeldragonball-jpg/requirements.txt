# C74 · Materias primas y crédito bancario (reejecución)

Parte de `research/informes/C74-materias-primas-credito-bancario.md` (no lo releas entero; busca con `python scripts/buscar_informes.py "C74 crédito" -n 6`). Vincula los datos a la pestaña Tipos y a `scripts/actualizar_paneles.py`; sin pestañas ni capas nuevas.

## Qué hacer
1. Comprueba con `curl` que siguen abriendo: API del BCE `data-api.ecb.europa.eu/service/data/BLS/...`, SLOOS de la Fed (`/data/sloos.htm` y el ZIP del DDP, que puede retirarse), EBA Risk Dashboard, CSV `beNNNN.csv` del Banco de España, EIA (`hist_xls`), Banco Mundial Pink Sheet y CFTC.
2. Actualiza fechas y últimos datos (BLS, SLOOS, EPB y EBA trimestrales; EIA diario; Pink Sheet mensual; COT semanal).
3. Resuelve los [VERIFICAR] pendientes: códigos BLS (hogares, `ES`), tabla BE con morosidad, NPL y CET1 de la EBA, Brent spot (EIA) frente a futuro (Yahoo).
4. Solo si Joel lo pide, implementa por prioridad: BLS (API) → EIA y BdE → SLOOS → Pink Sheet.
5. Contrasta lectura alcista y bajista; separa HECHOS de OPINIONES; cita fuente y fecha; [VERIFICAR]/[ESPECULACIÓN]. Sin recomendaciones. No commit ni push sin «sube».
