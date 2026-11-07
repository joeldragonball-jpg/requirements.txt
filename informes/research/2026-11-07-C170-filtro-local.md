# C170 · Filtro local sin IA para el bot de noticias (7-nov-2026)

Código: `noticias/filtro_local.py` (reglas + BM25 contra `temas`/`intereses` de `config.toml`; resumen = titular + 1.ª frase de la fuente; sin «por qué importa»). Offline; lee un JSON y escribe a archivo nuevo (`noticias/salida_filtro_local.json`). No llama a ninguna API. Datos: `noticias.json` de la rama `datos` (leído, no modificado).

## 1. Límite de los datos (importante)
`noticias.json` solo guarda las noticias **enviadas** (287, 4-oct a 7-nov), no el feed bruto: de los ~450 titulares/día que entran (`embudo`, 27-oct a 7-nov: 229-510/día, 65-98 pasan el triaje, 4-9 se envían) no se conserva el 99 %. Por tanto **mido cuántas de las enviadas por la IA rescata el filtro local (cobertura), pero NO puedo medir el ruido que añadiría** sobre el feed completo. [VERIFICAR con una semana en «modo sombra»: ejecutar el filtro local junto al bot y guardar sus descartes.]

## 2. Comparación con el bot con IA
| Medida | Resultado |
|---|---|
| Última semana (50 noticias enviadas), local con nota ≥ 5 y tope 6/día | **25 de 50 (50 %)** coinciden; **25 se pierden** |
| Las 287, nota local ≥ 4 / ≥ 5 / ≥ 6 / ≥ 7 | 83 % / 47 % / 16 % / 3 % |
| Duplicados que el local quitaría (Jaccard 0,55) | 4 de 287 (ya hay dedup en el bot) |
| Correlación de rangos con la nota de la IA (Spearman, sobre enviadas) | ≈ 0,05 (sin relación; rango de la IA solo 6-9, poco concluyente) |

**Qué pierde (ejemplos de la última semana, notas IA 8-9):** ataque de EE. UU. a objetivos iraníes en Ormuz (9), empleo de EE. UU. +165.000 (9), «Treasury corta a MEXC» (8), hackeo de Binance y su seguimiento (8, ×5 titulares), sanciones a firmas canadienses por vínculos cripto con Irán (8). Las reglas léxicas puntúan bajo noticias de gran impacto con vocabulario variado, y la **escala del local es otra** (máx. ~7,7; mediana 4,8): el umbral solo tiene sentido relativo.
**Qué ruido cabe esperar [ESPECULACIÓN, no medido]:** titulares genéricos de mercado («Ibex cae 0,5 %», previas semanales) con las mismas palabras clave que los útiles.
**Qué gana:** resumen reproducible y sin invención; pero en el 79 % de las noticias (220 de 277) la descripción está vacía o repite el titular (Google News), así que el resumen local será casi siempre solo el titular. Es el mayor argumento a favor de dejar un modelo para el resumen (B/C).

## 3. Ahorro (base: C16, octubre medido ≈ 5,82 $)
Noticias Sonnet 3,48 · urgentes Haiku 1,52 · triaje Haiku 0,50 · apuntes 0,23 · resumen semanal 0,08. (Mi recálculo con los tokens de `uso` da algo más: ≈ 7,2 $ en octubre [VERIFICAR; C16 y yo difiriendo por la forma de contar caché/periodo].)

| Opción | Gasto restante aprox. | Ahorro/mes | Calidad |
|---|---|---|---|
| A) Todo local | ≈ 0 $ | ≈ 5,8 $ (~70 $/año) | Mala: pierde ~50 % de lo importante y quita el «por qué importa» |
| B) Local + Gemini gratis solo resumen | urgentes ≈ 1,5 $ (si se mantienen) | ≈ 4,3 $ | La selección sigue siendo la débil; el free tier de Gemini y sus límites [VERIFICAR]; tu flujo Gemini hoy es manual, no automatizable sin API key |
| C) Local + Haiku solo urgentes con tope | ≈ 0,8-1,5 $ (con tope de tandas/día) | ≈ 4,3-5,0 $ | Igual de débil en selección diaria |

## 4. RECOMENDACIÓN (decide Joel)
Ninguna de las tres tal cual, hoy: **el filtro local solo cubre ~50 %** y sin datos de ruido. Si hay que elegir, **C**, pero **por fases**: (1) una semana en modo sombra (sin cambiar el gasto) para medir ruido y cobertura reales; (2) usar el local **como preselector barato antes del triaje** (sustituye al triaje Haiku, 0,50 $, y reduce lo que ve Sonnet) en vez de reemplazar a Sonnet; (3) mantener Sonnet solo para las ~25 finalistas y Haiku para urgentes con `max_alertas_urgentes_dia`. Ahorro realista de esa mezcla: ≈ 1-2,5 $/mes [ESPECULACIÓN], mucho menos que A, pero sin perder calidad. Con un gasto de 6 $/mes, el riesgo de A (perder la noticia de un ataque o un hackeo) pesa más que el ahorro. Alternativa de coste cero hoy: bajar `max_alertas_urgentes_dia` y recortar `palabras_urgentes` (ya señalado en C16).

## 5. Limitaciones
Sin negativos (descartes) no hay precisión; solo cobertura sobre ~1 mes de enviadas. Pesos de las reglas ajustados a mano, sin entrenamiento. Integrar el modo sombra exige tocar `noticias.py` (no hecho; tu decisión).
