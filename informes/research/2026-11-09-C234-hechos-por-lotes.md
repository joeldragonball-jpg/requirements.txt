# C234 · Hechos de todos los informes, por lotes (9-nov-2026)

**Qué se hizo:** 369 informes (`informes/`, `dossiers/`, `gemini/`, `research/`, `videos/`) en 21 lotes de ~18, del más reciente al más antiguo. Un agente Sonnet por lote extrajo hechos con fecha, fuente y nivel a `informes/hechos/lote-NN.jsonl`: **1.000 hechos** (584 P, el resto S/V), 271 informes con al menos un hecho. Cruce local sin IA con la Línea de tiempo: `scripts/cruzar_hechos.py` → `research/CRUCE-HECHOS.md`.

**Cruce:** 131 cubiertos, 869 «faltan» (584 P). Esa cifra **sobrestima**: solo compara con la Línea de tiempo (123 movimientos) y no con la Matriz de regulación, `paises.json`, `estabilidad` ni los tipos. Hay 24 pares repetidos y 9 de cifras distintas.

**Contradicciones que repitieron varios agentes (sin resolver; van a C237):** BoE 3,75 % vs 4,00 % · fecha de la subida de la Fed (16 vs 17-sep) · Brent spot EIA vs futuro · Evernorth 473 M vs 388,9 M XRP · RWA de Stellar (3.060 vs 30.600 M$) · sec. 404 de CLARITY · Sudáfrica 7,00 vs 7,25 % · BatchV1_1 y fixCleanup3_4_0 (fechas de activación).

**Límites:** los agentes copian el nivel que marca cada informe; no se ha releído ninguna fuente primaria. Nada se ha volcado a `explorador/` ni a `cerebro/`.
