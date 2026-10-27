# C29 · Energía, Ormuz y guerra ↔ noticias ↔ Órbita

Coste estimado: ~3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa) / [VERIFICAR] / [ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes; para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Webs que dan 403 a curl: navegador integrado, sin saltar controles anti-bots. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Al terminar: fila en research/COLA.md con coste, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea C29: vincular el hilo petróleo-Ormuz-guerra con el research de noticias y con la Órbita.
1. Hilo diplomático: cronología fechada (fuente oficial o prensa fiable, [P]/[S]) de negociaciones, ceses de ataques, viajes y declaraciones (p. ej. la noticia de Trump a Teherán y la presencia de Irán en la mesa, y el aviso de no atacar durante las elecciones de EE. UU.). Sepáralo en HECHOS y OPINIONES.
2. Noticia ↔ precio: para cada hito, Brent y WTI antes y después (cierres, FRED/EIA/Yahoo), p. ej. la caída de ~5-6 % tras esa noticia. Mismo método que informes/research/2026-10-18-R48-estudio-eventos-noticia-precio.md; avisa de que correlación no es causalidad y de que spot y futuro no son comparables.
3. Órbita: amplía la capa «Energía y Ormuz» de explorador/datos.json con esos hitos (campo «informe» enlazado) y, si se puede, una marca de precio en la línea de tiempo. Corre `python scripts/revisar_explorador.py`.
4. Noticias: asegura que el tema «Petróleo y Ormuz» y «Geopolítica y política» de research/gemini/NOTICIAS-DIA.md pregunten por negociaciones, treguas y fechas (añade líneas, no reescribas).
5. Móvil: dentro de Mercado, desplegable «Petróleo y guerra: últimos hitos» con 5-8 hitos y su efecto en precio.
Informe en informes/research/AAAA-MM-DD-C29-energia-guerra-noticias.md (máx. 1 página).
```
