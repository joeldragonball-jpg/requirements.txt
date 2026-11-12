# C230 · C59 — Contraste de paro, vivienda y tipos oficiales (12-nov-2026)

Método: 2 subagentes (WebSearch/WebFetch) + lectura directa de la API de Eurostat por el coordinador. Sin cambios en JSON: ya estaba cubierto.

## Paro (Eurostat une_rt_m, SA, sep-2026) [P]
ES 10,3 · DE 4,1 · FR 8,5 · IT 6,3 · US 4,2 (réplica Eurostat; BLS ya leído el 10-nov) · EA21 6,5. Octubre aún sin dato. Coincide con `indicadores.py` (automático).

## Vivienda (Eurostat prc_hpi_q, T2-2026, interanual) [P]
ES +12,1 · DE +0,6 · FR -0,8 · IT +4,0 · PT +16,5 · EA +4,0. Releído por el coordinador y coincide con `paneles.json › vivienda_eurostat` (ya existía; no duplicar).

## Tipos oficiales (agente; [P] banco central salvo lo marcado)
- Fed 3,75-4,00 % (28-oct: mantiene, votos 10-2); próxima 8-9-dic.
- BCE depósito 2,50 % (29-oct: mantiene); próxima dic [VERIFICAR día].
- BoE 4,00 % (5-nov: +25 pb); próxima 17-dic.
- BoC 2,50 % (agente: +25 pb el 28-oct; `paneles.json` dice 29-oct → [VERIFICAR] fecha); próxima 9-dic.
- BoJ 1,25 % (30-oct: mantiene, 8-1) [S]; próxima 17-18-dic. SNB 0 % (24-sep) [S]; próxima 10-dic [VERIFICAR].
- Japón y Suiza no están en `tipos_vivos`: hueco candidato a automatizar (no volcado por ser [S]).
- Contexto [S]: inflación zona euro sep 3,8 %; Lagarde saldría tras la reunión de febrero.

## Lecciones
1. Antes de lanzar agentes, grep del dato en `paneles.json`/`indicadores.py`: dos de tres ya estaban cubiertos.
2. Releer por API lo que un agente resume con WebFetch (hecho: coincide).
3. Revisar fechas de decisión (28 vs 29-oct) contra la nota del banco.

## RDL 28-36/2026 (C238, agente; BOE [P], votación [S])
- 12-nov: la Diputación Permanente (Cortes disueltas por RD 806/2026, elecciones 29-nov) convalidó el RDL 29 (35-34) y derogó el RDL 28 (alquileres, art. 10 LAU; vigor previsto 15-nov); recuento exacto del 28 [VERIFICAR]. Fuentes: idealista, Infobae [S]; sin ficha de congreso.es.
- RDL 30-36 (Ceuta, SS, Urda, DANA, ferroviario, familias, dependencia): sin votación localizada; plazo de 30 días hábiles (art. 86 CE) calculado, [VERIFICAR]. Volcado en `explorador/espana-leyes.json` (estados de 28 y 29 + aviso).
- Lección: tras disolución, convalida la Diputación Permanente; buscar su orden del día, no el del Pleno.
