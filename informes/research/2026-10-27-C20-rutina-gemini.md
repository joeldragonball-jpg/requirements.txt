# C20 · Rutina G: Gemini gratis en días sin evento (27-oct-2026)

**Qué es:** hasta 1 consulta ligera de Gemini al día (sin repetir), con prompt autocontenido; Claude no investiga, solo VERIFICA. Flujo manual (Gemini CLI no funciona con tu cuenta): Claude te da el prompt → lo pegas en la app de Gemini → me devuelves la respuesta (pegada o en Drive) → yo la guardo cruda en `informes/gemini/` y la verifico → solo lo verificado pasa a `noticias/manuales/` (formato C18) y el bot lo envía.

## Rotación (una por día; en días con evento alto manda `EV-post-evento`)
| Día | Prompt | Tema |
|---|---|---|
| lun y dom | `research/gemini/G01-xrp-xlm-24h.md` | noticias XRP/XLM últimas 24 h |
| mar | `G03-macro-tipos.md` | macro y tipos |
| mié | `G02-cripto-regulacion.md` | cripto y regulación |
| jue | `G04-etf-flujos.md` | ETF y flujos |
| vie | `G05-bulos-semana.md` | bulos y desmentidos de la semana |
| sáb | `G06-energia-geopolitica.md` | energía y geopolítica |
Salida de cada uno: 3 líneas + JSON de C18 (nivel `ligera`, 0-8 piezas, solo nota >= 7; en G05 los bulos desde nota 5).

## Verificación (Claude, 3-5 afirmaciones)
1. Elegir las de mayor impacto para la cartera. 2. Abrir la fuente primaria (navegador integrado si da 403; sin saltar anti-bots). 3. Marcar confirmado / corregido / [VERIFICAR]. 4. Pasar al JSON solo lo confirmado o corregido (`etiqueta` P o S); lo no contrastado se descarta o queda VERIFICAR con nota baja. 5. `python scripts/validar_manuales.py --lecciones` (máx. 5 líneas por archivo del cerebro).

## Parada por límite
`research/gemini-uso.json`: `parar_al_pct = 80`. Si Gemini muestra un límite o llegas al 80 %, anota `"parada": {"fecha": "AAAA-MM-DD", "nota": "..."}`; el planning muestra «⏸ parada por límite» ese día y no se pide más. [Aviso] Gemini no ignora solo el límite: hoy hizo 200+ búsquedas pese a pedirle ~15; 1 Deep Research por ventana (reinicio 04:00).

## Seguimiento
`scripts/construir_seguimiento.py`: rotación nueva y «Gemini del día: toca X» en `research/PLANNING.md` (también en el móvil). En `research/COLA.md`: filas G61-G66 (recurrentes, con su prompt) y C20 hecha.

## Vigilar
1. La rotación no se ha probado con una respuesta real de Gemini: la primera hay que validarla con `validar_manuales.py` (Gemini suele romper el JSON o inventar URLs).
2. La cuota de Gemini se comparte con NotebookLM: si hay NotebookLM ese día, salta la rutina G.

## Seguridad
Sin claves ni API; las respuestas crudas de Gemini son públicas en el repo: no pegues datos privados ni tu tesis en los prompts.
