# C37 · Enlaces a la fuente primaria que faltan en el radar regulatorio (23 celdas con etapa; actualizado 27-oct noche)

Objetivo: añadir el campo `url` (https, página que se abre y dice lo que dice la celda) en `explorador/regulacion.json` a las celdas con etapa que aún no lo tienen. `mapa.html` ya muestra «Fuente: dominio». Informe de partida: `informes/research/2026-10-27-C13-urls-radar.md`.

Reglas: abrir la página antes de añadirla (anotar si no abre y es enlace canónico: [VERIFICAR] a mano); si solo hay prensa, dejar la celda sin `url` y decirlo; no cambiar el texto de `estado`. Al terminar: `python scripts/revisar_explorador.py` (0 avisos), `construir_movil.py` y `construir_seguimiento.py`, y actualizar el informe y la fila C37 de `research/COLA.md`.

## Celdas que faltan (por país) y por dónde empezar
- **Hong Kong (HK, 4: ETF, custodia, CBDC, fiscal):** SFC (ETF cripto al contado, consulta de custodios 24-dic-2025), HKMA (e-HKD mayorista), IRD (DIPN 39).
- **Sudáfrica 3, Indonesia 3, Egipto 1, Etiopía 1, Irán 2:** países del hueco del radar (W03E bloqueado por PDF de Joel); primero el research, después los enlaces.
- **India (IN 2):** MAS ya está; falta RBI/SEBI/Ministerio de Finanzas según las celdas.
- **Brasil (BR 2: tokenización, CBDC):** CVM (Res. 88), Banco Central (Drex, comunicado oficial no localizado).
- **Corea (KR 2: ETF, fiscal):** ETF es una ausencia (sin página que enlazar); fiscal: proyecto del 3-ago-2026 del Ministerio de Economía y Finanzas.
- **EE. UU. (2: ETF, tokenización) y UE (1: ETF):** la nota de la SEC de estándares genéricos y la orden de la exención del 17-sep-2026; informe de 21Shares.
- **Capas de `explorador/datos.json`:** campo de fuente sin enlace (misma auditoría, hallazgo C13).

Estimación: ~1,5 % de cuota por tandas de 6-8 celdas; mejor con Chrome para las webs oficiales que bloquean WebFetch (recetas que funcionaron el 27-oct: buscar en html.duckduckgo.com desde Chrome y sacar los enlaces con JavaScript quitando el «?» para que la herramienta no bloquee; abrir cada página con get_page_text; los PDF se bajan con curl y se leen con pdftotext).
