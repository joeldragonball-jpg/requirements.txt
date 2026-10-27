# Prueba comparativa · EV-noticias-ligera con Claude (tanda de tarde 27-oct-2026)

Mismo prompt que Gemini (`research/gemini/EV-noticias-ligera.md`), ejecutado por Claude con WebSearch/WebFetch (~13 llamadas, nivel «ligero»). NO enviado a `noticias/manuales/` (no se manda a Telegram). Comparar con `informes/gemini/2026-10-27-tanda-tarde-verificado.json`.

## Piezas (nota ≥ 7 salvo indicado)

1. **Ripple obtiene la aprobación final de la OCC para su banco fiduciario nacional (RNTB)** · nota 8 · etiqueta P
   - Fuente primaria: nota de Ripple, https://ripple.com/ripple-press/ripple-receives-final-occ-approval-to-establish-national-trust-bank/ (abierta). Anuncio del 26-oct-2026; la prensa lo recoge el 27-oct (CoinDesk, Cointelegraph, FXStreet).
   - Hechos: gestiona reservas segregadas de RLUSD, es fiduciario de colateral y custodia de activos digitales. Sigue emitiendo RLUSD Standard Custody & Trust (NYDFS); BNY es custodio principal de reservas. Aprobación condicional de dic-2025.
   - Sesgo: la nota es de la propia empresa (promoción); la OCC la confirma por otra vía según la prensa. CoinDesk (27-oct): el anuncio **no ha movido el precio de XRP**.
2. **Janus Henderson y Centrifuge lanzan JQQQ, fondo tokenizado licenciado del Nasdaq-100, sobre Stellar** · nota 8 · etiqueta S
   - Fuente: CoinDesk 27-oct-2026 (URL en resultados de búsqueda; contenido leído vía titulares y resúmenes de 6 medios, no el artículo completo). Solo para inversores institucionales no estadounidenses cualificados, mínimo $100.000. Sin AUM ni volumen publicados.
   - Sesgo: lanzamiento anunciado por los emisores; «primer fondo licenciado» es afirmación del lanzamiento, sin verificación independiente. Relevante para el caso de uso de Stellar (RWA); no implica demanda de XLM por sí sola.
   - **Gemini NO recogió esta pieza.**
3. **Bitcoin cae por debajo de $80.000 al empezar la reunión de dos días de la Fed** · nota 7 · etiqueta VERIFICAR
   - Solo titulares de CoinDesk («latest news», 27-oct); sin abrir el artículo ni cotización primaria. Contexto de riesgo para XRP/XLM.
4. **Fed (FOMC 27-28 oct, decisión 28-oct 14:00 ET): el consenso era mantener 3,75 %-4,00 %** · nota 7 · etiqueta VERIFICAR
   - Probabilidades (~80-83 % mantener, ~17-20 % subir) proceden de datos de principios de octubre en agregadores; **desfasadas**. No hay comunicado del FOMC todavía en federalreserve.gov (último: actas del 7-oct). Revisar tras las 20:00 h Madrid del 28-oct.

## No verificado / descartado
- Pedidos de bienes duraderos de septiembre (+1,8 %, $345,4 mil M) que dio Gemini: **no lo pude confirmar** (census.gov devolvió 404; la búsqueda solo trae agosto, $338,6 mil M). Si el dato es correcto, el aumento respecto a agosto coincide en orden de magnitud (338,6→345,4 = +2,0 %, no +1,8 %: discrepancia por revisiones o redondeo, [VERIFICAR]).
- Ripple y los 1.000 M de XRP sin mover (99Bitcoins vía TradingView, dato de Gemini): no localizado por Claude; fuente de baja calidad.
- Menores (nota < 7): Keystone destruirá ~19.000 dispositivos tras brecha (25.964 registros); stablecoin en yenes de Japón no alcanzó su objetivo anual.
- XRP/XLM/CLARITY/Ormuz/BRICS: la búsqueda web estándar no devolvió nada fechado el 27-oct (mucho contenido SEO sin fecha). Última referencia fiable de CLARITY: voto procedimental de septiembre; estado actual sin confirmar.

## Comparación con Gemini
| | Gemini (Google Search) | Claude (WebSearch/WebFetch) |
|---|---|---|
| Piezas útiles | 4 (1 desfasada: Fed del 16-sep) | 2 sólidas + 2 de contexto |
| Aportó solo él | Duraderos (no verificado), 1.000 M XRP | **JQQQ en Stellar** (relevante para XLM) |
| Fuentes primarias | OCC vía CoinDesk | Nota de Ripple abierta |
| Debilidad | Enlaces y fechas no siempre abiertos; cifras sin comprobar | Búsqueda web pobre en noticias del mismo día; Census 404 |
| Mejor uso | Barrido amplio de titulares | Verificar con fuente primaria y leer páginas concretas (CoinDesk/Ripple/Fed) |

Conclusión: se complementan. Lo que mejor funcionó aquí fue **leer páginas de portada con fecha** (CoinDesk «latest») y luego buscar cada titular; las búsquedas genéricas por fecha fallan. La noticia JQQQ prueba que Gemini se deja piezas de nota alta.
