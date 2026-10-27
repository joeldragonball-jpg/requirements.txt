# C36 · Rutina de noticias manuales (Claude y Gemini)

Coste estimado: ~2-3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P]/[S]/[VERIFICAR]/[ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes; usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Al terminar: fila en research/COLA.md con coste, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea C36: rutina de noticias manuales que cubra días casuales y eventos, con el mínimo gasto de API.
1. Revisa research/gemini/NOTICIAS-DIA.md (8 temas) y añade temas de Política y elecciones, Bancos centrales y Geopolítica/guerra con preguntas concretas (negociaciones, treguas, licencias, decisiones) sin reescribir lo existente.
2. Define cuándo toca cada cosa: Gemini del día (gratis) en días normales; pasada de Claude (WebSearch/WebFetch, ligera) en días de evento del calendario o cuando Gemini no encuentre piezas con fuente primaria. Regla de piezas: solo con fuente primaria o dos fuentes fiables, nota ≥ 7, máx. 4-6 por tanda.
3. Salida de cada tanda: noticias/manuales/AAAA-MM-DD-*.json (se envía por Telegram sin IA de pago, formato en noticias/manuales/_ejemplo.json) y, si es importante, una línea en cerebro/ (solo añadir, nunca reescribir) para que quede como contexto del cerebro.
4. Comprobar con python scripts/ de validación de manuales antes de dejarlas.
Informe corto en informes/research/AAAA-MM-DD-C36-rutina-noticias.md.
```
