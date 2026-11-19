# C107 · Qué NO construir: lo que ya dan gratis OpenBB, Koyfin, TradingView, Finviz y similares (19-nov-2026)

Alcance: comparar funciones y precios publicados por cada proveedor con lo que ya tiene el repo (mapa en `graphify-out/GRAPH_REPORT.md`, 15-nov, y la lista de módulos `scripts/`, `explorador/`, `.github/workflows/`). Sin recomendaciones de compra/venta; no se compara con la tesis. Nivel: [P] = leído hoy en la web del proveedor; [VERIFICAR] = no leído.

## 1. Qué dice cada proveedor (leído el 19-nov-2026)

| Herramienta | Qué da gratis (según su web) | Qué es de pago | Fuente [P] |
|---|---|---|---|
| **OpenBB** | Código abierto (SDK → «Open Data Platform»). La empresa anunció el 25-ago-2026 que libera todo el catálogo con licencia permisiva; edición del 1-oct-2026: nace OpenBQ (organización sin ánimo de lucro, liderada por BrightQuery) y el código de Workspace pasaría a FINOS (Linux Foundation). Propone «Workspace Lite» y un Workspace alojado de BrightQuery en lista de espera. | Antes: Workspace alojado. Los datos de los proveedores se traen con las claves de cada uno. | openbb.co/products/odp (post del fundador) |
| **Koyfin** | Plan Free 0 $/mes: 2 años de financieros y 1 de estimaciones, carteras, gráficos avanzados, paneles de mercado y macro, 2 listas y 2 screeners, 2 paneles propios, noticias limitadas. | Plus 39 $/mes (ETF holdings, screeners ilimitados, transcripciones), Premium 79 $/mes (analítica de cartera, fórmulas propias). Precios «anual». | koyfin.com/pricing |
| **TradingView** | Plan Basic (gratis): 1 gráfico por pestaña, 2 indicadores por gráfico, 3 alertas de precio, 30 símbolos en lista, calendarios económico/resultados/dividendos/IPO y noticias, datos macro globales. | Essential 12,95 €/mes, Plus 29,95 €/mes, Premium 59,95 €/mes, Ultimate 199,95 €/mes (precios «especiales» anuales; más gráficos, alertas, exportar datos, replay). | tradingview.com/pricing |
| **Finviz** | Registro gratis: datos con retraso (1 min en NASDAQ/NYSE/AMEX), screener básico, 50 presets, 1 watchlist de 10 tickers, estados financieros de 3 años, ETF limitado. Solo mercados de EE. UU. | Elite 39,50 $/mes o 299,50 $/año (oferta Black Friday 149 $ el primer año): tiempo real, 8 años de estados, exportar CSV/Excel, alertas ilimitadas, holdings completos de ETF. | finviz.com/elite |

Sesgo de las fuentes: son páginas comerciales; muestran lo que quieren vender. Los límites del plan gratuito pueden cambiar sin aviso. Los precios de TradingView/Finviz incluyen ofertas temporales.

## 2. Lo que ya tiene este repo (hechos, de los archivos del propio repo)

- Cobertura de datos con lectores propios sin IA ni claves: FRED (csv público), BCE (SDMX), Eurostat, INE, Banco Mundial, BIS, FMI, DefiLlama, XRPL, Horizon (Stellar), Hedera, Solana, CoinGecko, EDGAR (`data.sec.gov`), GDELT, Federal Register (vigilante), BOE, Congreso, contratación y subvenciones de España, REE/OMIE, CFTC, ESMA/EBA, Tesoro de EE. UU., varios bancos centrales (frecuencia 16 workflows en `.github/workflows/`).
- Pantallas: Órbita (PC) y móvil (docs/), tablero con paneles de países, España a fondo, cadenas, ETF/flujos, estabilidad, predicciones con medición, noticias verificadas con nivel P/S, alertas, importador CSV multi-bróker, fiscalidad de ahorro e inversión en España (guías G1-G16), fichas por activo.
- Frescura: `explorador/frescura.json` marca 49 verdes, 19 amarillos, 6 rojos y 7 grises en 81 archivos (19-nov).

## 3. Mapa: qué NO conviene construir (porque ya existe gratis y mejor)

| Idea posible | Quién ya lo da (gratis o casi) | Veredicto |
|---|---|---|
| Gráficos técnicos interactivos con 100+ indicadores y dibujo | TradingView Basic, Koyfin Free | NO construir. Enlazar. Tu valor no es el análisis técnico. |
| Screener de acciones/ETF con filtros | Finviz Free (solo EE. UU., con retraso), TradingView Basic, Koyfin Free (2 screeners) | NO construir. Un screener propio exige datos de fundamentales de pago o frágiles. |
| Cotizaciones en tiempo real y premarket | Brokers y TradingView/Finviz de pago | NO construir. Los precios de `precios_vivos.py` (Yahoo/CoinGecko, con retraso) bastan para un panel de contexto. |
| Heatmaps y treemaps de bolsa | Finviz, TradingView | NO construir. |
| Calendario económico general y de resultados | TradingView Basic; tu repo ya tiene `calendario-oficial.json` + `.ics` BLS | NO ampliar a un calendario genérico; mantener solo hitos oficiales que cambian tu panorama. |
| Estados financieros a 10 años y comparables de empresas | Koyfin Plus, Finviz Elite (de pago) | NO construir. EDGAR XBRL (gratis) sirve para una empresa concreta si hace falta, no para una base general. |
| Terminal tipo OpenBB (SDK con 100 proveedores) | OpenBB ODP, código abierto | NO reimplementar. Si quieres una función puntual, usar OpenBB como librería local (código abierto) en vez de copiarla. Riesgo: la empresa se ha desmantelado/transferido (ago-oct 2026); el mantenimiento pasa a OpenBQ/FINOS [VERIFICAR estado de releases]. |
| Seguimiento de cartera con rendimiento | Koyfin Free (carteras), TradingView (3 carteras en Plus), Finviz Free (1 cartera de 20 posiciones) | Ya tienes importador CSV sin importes. No sumar analítica avanzada (atribución, benchmarks): lo da Koyfin Premium por 79 $/mes. |
| Alertas de precio | TradingView (3 gratis), brokers | NO construir más; el bot `alertas/` ya cubre lo que importa a los hechos. |

## 4. Lo que SÍ es diferencial (lo que ellos no hacen)

- Fuentes primarias con nivel P/S y fecha, y ligadas a hechos verificados (ninguna de las cuatro herramientas lo ofrece).
- España a fondo: BOE, presupuesto IGAE, contratación, subvenciones, votaciones, fiscalidad del ahorro; Koyfin/Finviz/TradingView cubren poco España.
- Capas de cadenas/tokenización, ISO 20022, XRPL/Stellar/Hedera on-chain, flujos de ETF cripto; RWA.xyz es la referencia externa (ver C144).
- Predicciones con criterio de medición y registro de errores.
- Mandatos y política de países, conflictos (GDELT) y energía.

## 5. Recomendación de proceso (sin recomendar activos)

1. Para gráficos y screeners: enlace en el tablero a TradingView/Finviz/Koyfin (gratis) en vez de construirlos.
2. Congelar cualquier tarea de la COLA que sea «gráfico técnico», «screener» o «mapa de calor»; si aparece una similar, recordar este informe.
3. Si más adelante se quiere un cuadro de fundamentales de una empresa: EDGAR XBRL `companyfacts` (gratis, sin clave) en lugar de pagar Finviz Elite/Koyfin Plus.
4. Mirar de nuevo OpenBB dentro de 3 meses: el estado de su licencia y quién mantiene el código es incierto [VERIFICAR].

## 6. Límites de este informe

- No se leyeron las condiciones de uso/licencia de cada herramienta (por ejemplo, si el plan gratuito permite uso comercial o raspado): [VERIFICAR] antes de enlazar datos incrustados.
- No se probó ninguna herramienta con sesión iniciada; los límites son los publicados.
- Las cifras de precios son de hoy y con ofertas temporales; Koyfin muestra precios «anual».
