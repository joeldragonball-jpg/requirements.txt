# C36 · Rutina diaria de noticias manuales (2-nov-2026)

Sin API de Anthropic, sin red, sin scripts cambiados (no hizo falta `py_compile`). Comprobado en solo lectura que `construir_seguimiento.py` ya lee los temas nuevos (11 temas, incluidos los tres añadidos).

## Hecho
1. `research/gemini/NOTICIAS-DIA.md`: tres temas nuevos, añadidos sin tocar los existentes: `politica-elecciones`, `bancos-centrales`, `geopolitica-guerra` (preguntas concretas: encuestas frente a resultado oficial, actas y votos, negociaciones, treguas, licencias y plazos). No están en la rotación semanal; se piden por nombre o los activa un evento.
2. Prompt listo y **sin lanzar**: `research/gemini/listos/2026-11-02-evento-elecciones-mitad-mandato.md` (tema `evento`, 12 piezas máx., fecha 3-nov). Sirve como previa antes del cierre de urnas; tras los resultados se vuelve a pegar cambiando la fecha.
3. Nota en `research/prompts/C36-rutina-noticias-manual.md`.

## La rutina, paso a paso
Aviso: el 29-oct Joel decidió que las tandas normales las hace Claude (`research/prompts/NOTICIAS-claude.md`). Gemini se usa solo si Joel lo pide (hoy lo pidió para las elecciones). El resto de pasos es común.

| Cuándo | Quién | Qué |
|---|---|---|
| Día normal | Claude (WebSearch/WebFetch, 1-2 % de cuota) | Tema de la rotación: lun/dom xrp-xlm · mar macro-tipos · mié cripto-regulacion · jue etf-flujos · vie bulos · sáb energia-geopolitica; `tarde` a las 20:00 |
| Día de evento alto en ±1 día, o cuando falta fuente primaria | Claude, pasada `evento` (2-3 %) | Misma salida, hasta 15 piezas |
| Gemini (solo si Joel lo pide) | Joel | Copia el prompt de `research/gemini/listos/` o del Seguimiento (móvil) → lo pega en Gemini → pega la respuesta aquí |

Pasos con Gemini:
1. **Prompt**: el del día del Seguimiento o `research/gemini/listos/<fecha>-*.md`. Una sola consulta (~15 fuentes); si Gemini avisa de límite, se para y se anota en `parada`.
2. **Crudo**: guardarlo tal cual como `informes/gemini/AAAA-MM-DD-NOTICIAS-DIA-<tema>.md` con la cabecera de verificación (plantilla `research/plantillas/gemini-deep-research.md`); todo entra como [S].
3. **Verificar 3-5 datos** (los que más pesan): abrir la URL, comprobar que existe, la fecha de publicación y 1-2 cifras en la fuente primaria. Una etiqueta P solo si se leyó la primaria. Rebajar nota o poner VERIFICAR a lo no abierto. Descartar lo anterior a 24 h (bulos 7 días).
4. **Manuales**: solo lo verificado, nota ≥ 7, máx. 4-6 piezas (evento hasta 15), a `noticias/manuales/AAAA-MM-DD-<slug>.json` (formato `_ejemplo.json`, `generado_con` Gemini o Claude). Validar: `python scripts/validar_manuales.py <ruta>` (0 errores; `--lecciones` solo con bulos o fuentes nuevas). El bot las manda por Telegram sin IA de pago tras subirse («sube»).
5. **Órbita**: `python scripts/noticias_a_orbita.py --simular` primero y, si cuadra, sin `--simular` (usa git local, no la red). Pasan las de nota ≥ 7 de las últimas 72 h con tema que tiene capa; caducan a 2 días (24h), 14 (7d), 60 (30d) y van a `noticias-archivo.json`. Tope de 5 por capa. Si es importante: una línea nueva en `cerebro/` (solo añadir).
6. **Anotar en `research/gemini-uso.json`**: una entrada en `sesiones` con fecha, `prompt` = «NOTICIAS-DIA · <id del tema>» (el Seguimiento marca «hecho» si el id aparece), `fuentes_aprox`, y una nota con qué se verificó, qué falló y el enlace al informe crudo. Si el tema merece, actualizar su estado en `prompts` (`bueno`/`mejorar`).
7. **Cierre**: 5 líneas y «¿Actualizo el Seguimiento y el planning?». Sin commit ni push sin «sube».

## Qué pasa con cada tema en la Órbita (sin crear capas nuevas, regla de Joel)
`scripts/noticias_a_orbita.py` solo enruta estos temas a una capa existente: Petróleo y Ormuz→energía, Economía y mercados→liquidez, Regulación y Cripto y regulación→reg, XRP / Ripple y Stellar / XLM→puente. **«Geopolítica y política» no tiene capa** y sale en «sin capa». Por eso las piezas de elecciones, bancos centrales y guerra solo llegan a la Órbita si se etiquetan con uno de los temas mapeados:
- Bancos centrales → «Economía y mercados» (capa liquidez).
- Elecciones con efecto en la CLARITY Act → «Cripto y regulación».
- Guerra con efecto en petróleo → «Petróleo y Ormuz».
- El resto (política pura) queda en Telegram y en el cerebro.
El prompt de Gemini ya deja que elija entre los 8 temas del formato.

## Riesgos y sesgos para el prompt de las elecciones
- Antes del cierre de urnas (3-nov) no hay resultado oficial: las encuestas son opinión [ESPECULACIÓN]. El prompt lo exige en «fiabilidad».
- Medios y cuentas de X mezclan proyecciones con resultados; la fuente primaria son los organismos electorales de cada estado.
- Caso alcista/bajista para cripto: una mayoría proclive a la CLARITY Act frente a un bloqueo en el Senado; hacerlo solo si cambia la conclusión.
- Gemini ya dio URLs sin abrir y cifras de memoria (27-oct): verificar siempre 3-5 datos.

## Decisiones que le tocan a Joel
1. ¿Gemini solo para este evento (como pidió hoy) o vuelves a él en la rotación? Hasta que digas lo contrario, las tandas normales las hace Claude.
2. ¿Quieres que los tres temas nuevos entren en la rotación semanal (cambio pequeño en `GEMINI_DIAS` de `construir_seguimiento.py`) o que se pidan solo por nombre?
3. ¿Se enruta «Geopolítica y política» a alguna capa existente en `noticias_a_orbita.py` (cambio de una línea) o se deja sin capa?

## Archivos tocados
`research/gemini/NOTICIAS-DIA.md` (+3 líneas), `research/gemini/listos/2026-11-02-evento-elecciones-mitad-mandato.md` (nuevo), `research/prompts/C36-rutina-noticias-manual.md` (+nota), este informe.
