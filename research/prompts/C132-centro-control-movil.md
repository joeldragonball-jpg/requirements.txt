# C132 · Centro de control para el móvil (tamaño L, Opus recomendado para el diseño)

Objetivo (Joel, 4-nov-2026): un tablero de inteligencia reducido para el móvil (`docs/movil/`) para controlar de un vistazo bolsas, ETFs, fondos indexados, materias primas (petróleo, gas, electricidad, soja, trigo, maíz, café, cobre, oro), energía y todo lo que mueve una sociedad y un país. Diseño pensado para el móvil (una columna, números grandes, etiqueta ARRIBA de cada cifra), sin copiar el tablero del PC.

Pasos:
1. Lee `docs/movil/index.html` y `docs/movil/data.json` solo en las partes necesarias (Grep). Revisa antes C90 (XSS: texto externo como HTML) y no empeores esa superficie: usa `textContent`.
2. Lista de paneles propuestos: Bolsas (S&P, Nasdaq, Dow, Euro Stoxx, Nikkei, IBEX), ETFs y fondos indexados (VWCE/IWDA/SPY como referencia, sin recomendar), Materias primas (energía, agrícolas, metales), Divisas y tipos, Cripto de Joel (XRP, XLM). Fuente de datos: lo que ya leen `scripts/actualizar_paneles.py` y `explorador/paneles.json`; indica qué falta.
3. Cada cifra: valor grande, variación con flecha (verde/rojo solo si el sentido es claro), fecha y nivel [P]/[S].
4. Propón primero un esquema (sin código) y enséñaselo a Joel; implementa solo con su visto bueno. Sin API de Anthropic. Sin commit ni push.
