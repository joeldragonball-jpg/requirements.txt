# NOTICIAS-claude · Noticias manuales hechas por Claude (sustituye en la práctica a la versión de Gemini)

Decisión de Joel (29-oct-2026): la versión de Gemini no convenció; las noticias manuales las hace Claude con búsqueda web real. Mismo formato de salida que Gemini (`noticias/manuales/AAAA-MM-DD-<slug>.json`, validado por `scripts/validar_manuales.py`), así que el bot, el móvil y la Órbita no cambian.

Cómo se pide: «noticias <tema>» o `/research NOTICIAS <tema>`; sin tema, el de la rotación del día. Coste: ~1-2 % de cuota por tanda ligera (máx. 20 min); `evento` ~2-3 %.

## Rotación diaria (la misma que usaba Gemini)
lun y dom `xrp-xlm` · mar `macro-tipos` · mié `cripto-regulacion` · jue `etf-flujos` · vie `bulos` · sáb `energia-geopolitica` · `tarde` (20:00 España) · `evento` si hay evento de impacto alto en ±1 día (calendario del PLANNING). Las preguntas de cada tema están en `research/gemini/NOTICIAS-DIA.md` (sección «Temas»): úsalas tal cual, sin reescribirlas.

## Instrucciones para Claude (esto es lo que hay que hacer)
1. **Buscar de verdad, nada de memoria.** WebSearch (modo `standard`; `extended` solo si un tema sale vacío o dudoso) y WebFetch para abrir cada enlace. Si una web bloquea (Cloudflare, 403), prueba la extensión de Chrome sin saltar captchas; si no abre, la pieza va como VERIFICAR con la nota bajada.
2. **Ventana temporal estricta:** solo piezas publicadas en las últimas 24 h (bulos: 7 días; evento: desde el anuncio). Comprueba la fecha de publicación de cada una antes de incluirla; una más vieja no entra aunque sea importante.
3. **Fuente primaria primero:** comunicado del banco central, regulador, tribunal, empresa, SEC/EDGAR, BOE, etc. Prensa solo como [S] y, si es la única, con nota ≤ 7. Dos fuentes independientes fiables equivalen a una primaria.
4. **Filtro de calidad:** 0 a 6 piezas por tanda (evento: hasta 15); solo nota ≥ 7 para un inversor a largo plazo con XRP y XLM; sin duplicados de lo ya enviado en `noticias/manuales/` de los últimos 3 días (mira los títulos antes). Mejor 2 buenas que 6 flojas; si no hay nada, devuelve cero y dilo.
5. **Cada pieza lleva el contraste:** qué lectura alcista y bajista admite (en `resumen`, máx. 600 caracteres) y el sesgo de la fuente en `fiabilidad` (promoción, conflicto de interés, hype, cuenta anónima, titular sin dato, o «primaria sin sesgo relevante»). Hechos separados de opiniones; predicciones y opiniones = etiqueta VERIFICAR [ESPECULACIÓN].
6. **Bulos:** si algo circula sin fuente primaria, `bulo: true` con `motivo_bulo` y, si enseña un patrón, `leccion_bulo`. No des por falso lo que solo no pudiste confirmar: eso es VERIFICAR, no bulo.
7. **Formato** (idéntico a `noticias/manuales/_ejemplo.json`): `{"evento": "...", "fecha": "AAAA-MM-DD", "nivel": "ligera|evento", "generado_con": "Claude", "noticias": [{"titulo", "fuente", "url", "fecha" (ISO UTC), "resumen", "etiqueta": "P|S|VERIFICAR", "tema" (uno EXACTO de: XRP / Ripple | Stellar / XLM | Cripto y regulación | Economía y mercados | Geopolítica y política | Petróleo y Ormuz | BRICS y dinero global | Regulación), "nota" (1-10), "fiabilidad", "bulo", "motivo_bulo", "leccion_bulo"?, "fuente_nueva"?}]}`. URLs reales abiertas en esta misma sesión; cifras con símbolo delante y «mil M»; sin recomendaciones de compra/venta; nada de `privado/` ni de la tesis.
8. **Guardar y validar:** escribir `noticias/manuales/AAAA-MM-DD-<slug>.json`; ejecutar `python scripts/validar_manuales.py <ruta>` y corregir hasta 0 errores; con `--lecciones` solo si hay bulos o fuentes nuevas (máx. 5 líneas, solo añadir).
9. **Cierre (5 líneas):** cuántas piezas, cuáles son las 2 más importantes con su fuente, qué se descartó y por qué, qué quedó VERIFICAR, y «¿Actualizo el Seguimiento y el planning?». No hacer commit ni push sin «sube» (enseñar `git status`): el bot manda las manuales por Telegram sin IA de pago en su siguiente franja tras subirse.

## Mejoras frente a la versión de Gemini
- Búsqueda y apertura de enlaces comprobables en la sesión (Gemini daba URLs sin abrir y cifras de memoria; el 27-oct hubo errores como un 4,72 % en vez de 4,92 % en el bono francés).
- Contraste alcista/bajista y sesgo de fuente obligatorios, en línea con CLAUDE.md.
- Control de duplicados y de ventana de fecha antes de escribir.
- Validación con el script y lecciones de bulos solo cuando aportan.
