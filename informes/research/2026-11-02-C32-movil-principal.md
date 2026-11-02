# C32 · Móvil: fila de resumen en «Hoy» (2-nov-2026)

**Hecho (solo `docs/movil/index.html` y `sw.js` v50→v51; sin commit):** al principio de «Hoy» hay una rejilla de 9 tarjetas (3×3) que se ve de un vistazo: XRP, XLM, BTC (€ al cambio del BCE, % en 24 h), Brent ($, % en 1 d), Fed y BCE (tipo y fecha del dato) e IPC de España, zona euro y EE. UU. (interanual, valor anterior y mes). Cada tarjeta lleva a «Mercado». Debajo sigue todo lo anterior y el desglose (Ormuz, liquidez, inflación, defensa, valoración) ya estaba en el desplegable cerrado de «Mercado».
Prueba a 375 px en el navegador integrado: sin scroll horizontal, sin texto cortado, sin errores de JavaScript.

**Datos y fuentes:** precios y Brent de `data.json` (2-nov); tipos de `tipos` (Fed dato 28-oct; BCE dato 16-sep); IPC de `inflacion` (sep-2026, nivel [P]: BLS y Eurostat). El IPC de España es el IPCA de Eurostat y puede diferir del IPC del INE.

**Avisos [VERIFICAR]**
- Brent aparece con −11,1 % en 1 día (104,6 $) y WTI con −7,3 %: es una caída muy grande; puede ser dato real o un salto de contrato. Comprobar antes de fiarse.
- Los colores verde/rojo no se usan en el IPC (subir la inflación no es «bueno»); solo flecha y valor anterior.

**Auditoría (lista corta, sin aplicar salvo la 1)**
1. ✔ Fila de resumen arriba (hecho).
2. Mostrar la fecha de cada cripto (el 24 h no dice a qué hora): añadir hora de `generado`.
3. Pasar los precios de la watchlist (VUSA, IWDA…, último cierre 29-oct) a la fila de resumen si Joel los quiere ahí.
4. Los tipos del BIS y la curva de bonos no están en «Hoy»: valorar un resumen de 3 líneas.
5. Revisar el panel «Defensa» y «Valoración» (cifras de años concretos): comprobar con su informe cuando haya tiempo.
6. Deuda y elecciones: ya están, solo falta comprobar a mano que no se cortan en pantallas pequeñas.

**Decisiones de Joel:** ¿qué 9 tarjetas quiere fijas (¿watchlist, BIS, Ormuz?)? ¿Quito BTC? ¿Subo el sw (ya a v51) cuando haga «sube»?
