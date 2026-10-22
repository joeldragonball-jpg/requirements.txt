# Plantilla: vídeos de un canal → tesis (privada) + órbita (pública)

Pensada para 4-6 vídeos (p. ej. del canal «Despeja La X») de una sola vez. Se usa en una sesión NUEVA de Claude Code abierta en esta carpeta; no hace falta pasarla por la conversación larga.

## 1. Antes de abrir la sesión (2 minutos, sin IA)
1. Crea el archivo `privado/videos/LISTA.md` (la carpeta `privado/` no se sube a GitHub) con una línea por vídeo:
   `URL | parte: tesis / órbita / las dos | lo que YA sé por experiencia (opcional, tus palabras)`
   Ejemplo: `https://youtu.be/XXXXXXXXXXX | las dos | llevo un año y medio viendo que lo que dicen de X se cumple con retraso de semanas`
2. Ejecuta el índice local (sin IA, sin descargar vídeo; solo subtítulos), una vez por vídeo:
   `python scripts/videos.py https://youtu.be/XXXXXXXXXXX`
   Deja la transcripción en `privado/videos/` y un índice con minutos de citas, organismos y frases de titular.

## 2. Etiquetas (las de siempre + una nueva)
| Etiqueta | Significa |
|---|---|
| [P] | Comprobado en fuente primaria (organismo, empresa, ledger, boletín oficial) |
| [S] | Lo dicen medios o agregadores fiables; sin primaria |
| [J] | **Observación de Joel o del canal, contrastada por Joel durante meses, sin fuente pública verificable.** Es información útil, pero NUNCA se presenta como hecho verificado ni se mezcla con [P]/[S] |
| [ESPECULACIÓN] | Predicción, opinión o «lo que podría pasar» |
| [VERIFICAR] | Se podría comprobar y aún no se ha hecho |
Regla: si una afirmación es [J], se escribe «según el canal / según Joel» y se deja dicho qué la confirmaría.

## 3. Prompt para la sesión nueva (copiar y pegar)
```
Sesión de VÍDEOS (máx. 20 min por vídeo). Sigue CLAUDE.md y la guía research/GUIA-ESTILO-CIFRAS.md. Lee research/plantillas/videos-tesis-y-orbita.md y privado/videos/LISTA.md. No leas la transcripción entera: usa python scripts/buscar_informes.py y el índice del vídeo, y lee solo los tramos que te señale.
Para CADA vídeo:
1. Extrae las afirmaciones concretas (quién, qué, cifra, fecha, minuto). Descarta promoción, relleno y frases de titular sin dato.
2. Clasifica cada una con las etiquetas de la plantilla. Las que se puedan comprobar, comprúebalas en fuente primaria (curl, navegador integrado, pdf.js dentro de la página; sin saltar controles anti-bots). Las que Joel marcó como ya contrastadas, ponlas como [J], con su nota.
3. Separa HECHOS de OPINIONES y contrasta alcista vs. bajista; señala sesgos del canal (promoción, conflicto de interés, hype).
4. Parte PÚBLICA (órbita): informes/videos/AAAA-MM-DD-tema.md en el formato de los de esa carpeta (solo fragmentos cortos con minuto, nunca la transcripción), y propón filas nuevas para explorador/datos.json (hechos, fecha, fuente, nivel) y calendario si hay fechas. NADA de la tesis aquí.
5. Parte PRIVADA (tesis): privado/AAAA-MM-DD-videos-vs-tesis.md con una tabla: afirmación | etiqueta | qué refuerza o contradice de la tesis (léela de privado/) | qué la confirmaría o la tumbaría. Solo en privado/.
6. Al final: lista de [VERIFICAR] pendientes y 5 líneas máximo por archivo de lecciones (patrones de bulos, fuentes, catalizadores).
Reglas: sin recomendaciones de compra/venta; nunca claves ni secretos; no lances workflows ni nada que llame a la API de Anthropic salvo esta sesión; no hagas commit ni push sin mi OK (enséñame git status y avisa de claves antes). Al terminar, 3 líneas de seguridad.
```

## 4. Modelo y coste (orientativo)
- **Sonnet, esfuerzo medio:** extraer afirmaciones, buscar fuentes y rellenar la parte pública. Suficiente para casi todo.
- **Opus, esfuerzo alto:** solo para el cruce final con la tesis (parte privada) y para decidir qué sube a la órbita. Si hay poca cuota, hacerlo en una segunda sesión corta.
- Cuota: calcular ~1-2 % semanal por vídeo con Sonnet; mejor repartir los 4-6 vídeos en dos sesiones.

## 5. Qué sube a GitHub y qué no
- Sube: `informes/videos/…`, filas de `datos.json`/calendario y líneas de lecciones.
- No sube nunca: `privado/` (lista, transcripciones completas por derechos de autor, cruce con la tesis).
