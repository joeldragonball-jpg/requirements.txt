# W05B · Lote corto con Chrome · 5-nov-2026 (noche)

Objetivo: cerrar las 4 verificaciones abiertas de W05 con Chrome. Resultado: 1 cerrada (parcial → P), 1 bloqueada, 2 sin resolver.

## 1. Canton Coin y la SEC — CERRADO (en parte) [P]
- **Hecho (fuente primaria, EDGAR):** ETF Opportunities Trust presentó el 15-oct-2026 un formulario 485BXT (post-effective amendment nº 1056) para el **REX-Osprey™ Canton Coin ETF**. Solo fija una nueva fecha de entrada en vigor: **13-nov-2026**, para la enmienda nº 486 presentada el 1-dic-2025. Un 485BXT anterior se presentó el 17-sep-2026 (misma serie de aplazamientos).
- Fuente: https://www.sec.gov/Archives/edgar/data/1771146/000177114626002033/etfot-rexospreycantoncoine.htm (leído hoy). Búsqueda de texto completo de EDGAR («Canton Coin», 1-sep a 5-nov): 25 documentos, de los que los relevantes son los 485BXT de ETF Opportunities Trust y un 8-K de Canton Strategic Holdings (29-oct, EX-99.1, no leído).
- **Matiz:** un 485BXT es un aplazamiento, no una aprobación; que entre en vigor el 13-nov no implica que cotice (depende de la estructura del fondo y de su listado) [VERIFICAR]. Tampoco prueba que la SEC «apruebe» Canton Coin como activo.
- Pendiente: leer el 8-K de Canton Strategic Holdings (CNTN) del 29-oct, que no es lo mismo que el token Canton Coin (posible confusión de nombre).

## 2. Cloture de CLARITY 49-50 y nombres de 4 republicanos — BLOQUEADO
- senate.gov devuelve «Unauthorized / potential security risk» a la navegación automatizada. No se esquiva. Sigue [S] (prensa): 49-50, 15-sep. Hay que abrirlo Joel a mano: https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm (buscar la votación de cloture de CLARITY del 15-sep).
- congress.gov no se probó (mismo tipo de bloqueo en el lote anterior).

## 3. Brent 94,6 $ vs 104,06 $ — SIN RESOLVER
- La EIA (RBRTED) publica el spot con retraso y su tabla no se pudo leer entera en el navegador (página de histórico sin las filas de 2026 en el texto). No se cierra con una fuente oficial. Mantener ambas copias como [VERIFICAR]; releer en la próxima actualización de paneles (precios_vivos.py).

## 4. Verificaciones antiguas (45)
- No tocadas en este lote (contexto y cuota reservados para C143).

## Lección (≤5 líneas)
- EDGAR full-text (efts.sec.gov/LATEST/search-index?q=...) funciona en Chrome y devuelve JSON; útil para vigilar ETFs/tokens.
- senate.gov bloquea Chrome automatizado: anotar en ACCESOS-CHROME.md como «manual».
- La página histórica de la EIA es enorme (50 000 caracteres de 1987): no usar get_page_text; usar la API o el xls con permiso.
