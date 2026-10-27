# C26 · Cuadro de valoración sectorial automático — 27-oct-2026

Información para decidir tú; no es una recomendación de compra ni de venta.

## Qué se hizo
- `scripts/valoracion_sectorial.py` (sin IA, sin claves): 18 valores en 4 sectores (Defensa, Energía, Ciberseguridad, Semiconductores). Precio de Yahoo `v8 chart` [S] + SEC `companyfacts` [P]. Escribe `explorador/valoracion.json` con precio, capitalización, EV, PER, EV/EBITDA, FCF yield, periodo y notas por fila.
- Cálculo: TTM = año fiscal + acumulado actual − acumulado del año anterior; EBITDA = resultado operativo + D&A (en XOM, CVX y COP, antes de impuestos + intereses + D&A, marcado «aprox.»); n/d si falta algún dato. Entre etiquetas XBRL alternativas se usa la de periodo más reciente.
- Uso: `python scripts/valoracion_sectorial.py` (todos) o `... LMT NVDA` (solo esos, imprime sin guardar).

## Verificación (3 cifras contra otra fuente)
| Cifra | Script (SEC companyfacts) | Contraste | Resultado |
|---|---|---|---|
| NVDA beneficio neto 2T FY27 (a 26-jul-26) | 59.688 M$ | nota de prensa de NVIDIA, 8-K de 26-ago-26: 59.688 M$ | ✓ idéntica |
| LMT flujo de caja libre 9 meses 2026 | OCF 6.893 M$ (9M) → con FCF publicado 5.625 M$ el capex 9M sale 1.268 M$ | nota de prensa de Lockheed, 22-oct-26: FCF 9M 5.625 M$ | ✓ coherente (no es comparación directa de capex) |
| LMT capitalización | 231,0 M acciones (portada 19-oct) × 628,96 $ = 145,3 mil M$ | — | cálculo propio |
Las dos primeras son contraste real; NVDA TTM (192.880 M$) cuadra con la suma de trimestres publicados (58,5 + 59,7 + ~74,7 de los dos trimestres previos), pero esa suma no está contrastada trimestre a trimestre [VERIFICAR].

## Límites y [VERIFICAR]
- Periodos mezclados (XOM llega a mar-26, GD a abr-26): mira la columna `periodo`.
- PANW y ZS reportan año fiscal a jul-26 sin 10-Q posterior; PER de PANW (1.074), CRWD (6.111), AMD (142) y EV/EBITDA de PANW, ZS y AMD salen «no significativo» (beneficio casi nulo). CRWD sin D&A localizada.
- Acciones = portada del último 10-K/10-Q (sin diluidas). Deuda = etiqueta XBRL de cada empresa; si falta se cuenta 0 y se avisa.
- Los valores individuales los eligió el script como grandes representativos, no son posiciones tuyas ni sugerencias. ETF (CIBR, SMH, SOXX) y TSM siguen sin cubrir.
- La SEC pide identificar el User-Agent; el genérico funciona hoy. Si lo rechaza, `SEC_USER_AGENT` con contacto tuyo (decisión tuya).

## Falta
Automatizar el refresco (añadir al workflow `paneles.yml`, trimestral o semanal) y mostrarlo en el panel; no se ha hecho para no tocar workflows sin tu OK.

## Caso alcista / bajista (añadido 27-oct-2026, C27; sin predicción)
Tema: ¿merece la pena un cuadro automático?
- **A favor (alcista para el método):** coste cero de API, datos primarios de la SEC [P], refresco en un comando y dos cifras contrastadas con notas de prensa de las empresas.
- **En contra (bajista para el método):** etiquetas XBRL distintas por empresa (EBITDA aprox. en XOM, CVX y COP; CRWD sin D&A), periodos mezclados y acciones sin diluir; Yahoo [S] no tiene contrato de servicio y puede cambiar o cortar el acceso.
- **Sesgo:** la elección de los 18 valores es mía, no del mercado; el cuadro no sustituye a un análisis de cada empresa.
