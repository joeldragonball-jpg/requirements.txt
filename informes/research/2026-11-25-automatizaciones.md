# W07 · Auditoría de automatización del tablero (25-nov-2026)

Sin IA ni claves. No se ha tocado ningún script ni workflow. Sondeos con curl el 25-nov-2026 (HTTP 200 salvo indicación).

## 1. Qué se actualiza solo hoy
- **paneles.yml (L-V 21:30 UTC)**: automatizar_manuales (indicadores-manual, tipos-manual), actualizar_paneles, precios_historico, indicadores_historia, valoracion_sectorial, leer_bolsas, leer_portwatch, leer_tokenizado, noticias_a_orbita, construir_*.
- **precios.yml (horario)**: precios/precios_vivos.json. **onchain/alertas/escrow/eventos**: avisos a Telegram (no escriben explorador/).
- **Vigilantes** (boe, edgar, federal-register; poder-judicial desactivado): solo alertas.
- Fresco por esto: bolsas, calendario-oficial, cadenas.json (verde).

## 2. Hoy a mano (frescura amarillo/rojo) aunque el script YA existe
Hay `scripts/leer_*.py` que no están en ningún workflow: leer_fiscal_eeuu, leer_ocde_bis, leer_gdelt, leer_rendimientos, leer_onchain, leer_validadores, leer_incidentes, leer_gobernanza, leer_xrpl, leer_etf_flujos, leer_pagos_espana, leer_bdns, leer_contratacion, leer_mortalidad_ine, leer_espana_empresas, leer_seguridad_eurostat, leer_votaciones_congreso, leer_comparativa/liquidez/profundidad. Es el grueso de los 43 amarillos y 11 rojos.
Rojos: bancos-eba (513 d), calificaciones (34), deuda-fmi (35), espana-empleados (298), espana-presupuesto (298), espana-votaciones (54), etf-13f-2T-edgar (148), mandatos (128), reservas (34), seguridad-eurostat (694), swift-liquidacion (34).

## 3. Tabla de candidatos (top 10)
| # | Archivo manual | Fuente candidata | URL probada | Respuesta | Esfuerzo | Prioridad |
|---|---|---|---|---|---|---|
| 1 | eeuu-fiscal.json | Treasury Fiscal Data (+CFTC) | api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?sort=-record_date&page%5Bsize%5D=1 | 200 JSON, dato 2026-11-24 (con `[` sin codificar devuelve vacío) | S (script existe, falta workflow) | Alta |
| 2 | rendimientos-defillama, cadenas-onchain, cadenas-incidentes, cadenas-token | DefiLlama | stablecoins.llama.fi/stablecoins ; api.llama.fi/v2/chains | 200 JSON | S (scripts existen) | Alta |
| 3 | cadenas-validadores, cadenas-gobernanza, estado XRPL | XRPL/Solana/Avalanche RPC + atoms GitHub | s1.ripple.com:51234 (POST server_info) | 200 JSON-RPC (GET da 400: es POST) | S | Alta |
| 4 | ocde-bis, indicadores-historia-fmi | BIS SDMX, OCDE SDMX | stats.bis.org/api/v2/data/dataflow/BIS/WS_CBPOL/1.0/D.ES?format=csv | 200 CSV | S (script existe) | Alta |
| 5 | reservas.json, swift-liquidacion (parte COFER) | FMI COFER SDMX | api.imf.org/external/sdmx/2.1/data/IMF.STA,COFER/all?lastNObservations=1 | 200 XML SDMX, trimestral | M (parsear XML) | Media-alta |
| 6 | seguridad-eurostat (694 d) | Eurostat API | ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/une_rt_m?... | 200 JSON-stat, updated 2026-11-24 | S (script existe) | Media (anual) |
| 7 | conflictos-gdelt | GDELT DOC 2.0 | api.gdeltproject.org/api/v2/doc/doc | no sondeado hoy (límite de tasa conocido) | S | Media |
| 8 | espana-mortalidad, espana-pensiones, indicadores España | INE Tempus | servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPC206449?nult=2 | 200 JSON | S/M | Media |
| 9 | espana-presupuesto/empleados (rojos), deuda | Banco de España CSV, World Bank | bde.es/webbe/es/estadisticas/compartido/datos/csv/be1101.csv ; api.worldbank.org/v2/country/ESP/indicator/NY.GDP.MKTP.KD.ZG | 200 CSV (Latin-1) / 200 JSON (lastupdated 2026-11-11) | M | Media |
| 10 | tipos-manual (zona euro), bonos-manual | BCE Data Portal SDMX | data-api.ecb.europa.eu/service/data/FM/B.U2.EUR.4F.KR.MRR_FR.LEV?lastNObservations=2&format=csvdata ; .../EXR/D.USD.EUR.SP00.A ; .../ICP/M.U2.N.000000.4.ANR | 200 CSV los tres | S | Alta |

Otros sondeos: CoinGecko público simple/price 200 (XRP 0,937 $, XLM 0,1275 $; límite de tasa, ya cubierto por precios_vivos); Stellar Horizon 200; Federal Register API 200 (ya hay vigilante); CFTC Socrata 200; REE apidatos (demanda eléctrica) 200 JSON, candidato nuevo para energía España; FRED fredgraph.csv: timeout desde este PC (código 0), pero automatizar_manuales.py ya lo usa en CI, no es bloqueo real; FMI DataMapper: 403 Access Denied (usar api.imf.org SDMX); SEC company_tickers: 429 por tasa (requiere User-Agent identificado, como ya hacen los scripts EDGAR); Congreso: el JSON diario probado da 404 (cuadrar con leer_votaciones_congreso); tesoro.es subastas.json: 404 (no existe).

## 4. Orden recomendado
1. **Sin código nuevo**: añadir a paneles.yml (o un workflow semanal) leer_fiscal_eeuu, leer_rendimientos, leer_onchain, leer_incidentes, leer_validadores, leer_ocde_bis, leer_gdelt. Cubre ~15 amarillos de golpe (S).
2. Ampliar automatizar_manuales con BCE SDMX (tipos y HICP, 3 URL probadas).
3. COFER (XML SDMX) para reservas.
4. Eurostat/INE/World Bank para rojos anuales (seguridad-eurostat, espana-*).
5. REE apidatos para energía España.

No automatizable fácil: bancos-eba (PDF anual), calificaciones (agencias sin API), mandatos, etf-13f (trimestral, EDGAR a mano), espana-votaciones (JSON diario del Congreso no localizado).
Riesgos: Actions que comiten en main chocan con otros bots; escalonar crons; límites de tasa en GDELT/CoinGecko/SEC.
