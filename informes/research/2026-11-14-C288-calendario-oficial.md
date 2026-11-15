# C288 · Calendario oficial automático (14-nov-2026)

**Resultado:** `explorador/calendario-oficial.json` (130 eventos, 14-nov-2026 a 12-feb-2027) generado por `python scripts/leer_calendario_oficial.py` (sin IA, sin claves, certificados verificados). Nivel P: cada evento lleva su URL oficial.

| Organismo | Origen | Eventos en periodo | Nota |
|---|---|---|---|
| BLS | bls.ics | 17 | curl da 403; leído con Chrome (misma URL, `fetch` dentro de bls.gov) y guardado en `explorador/calendario-oficial-bls.ics`. El .ics del BLS solo llega a 30-dic-2026. Para refrescar: repetir en Chrome o `--bls ruta.ics` |
| BEA | bea.gov/news/schedule | 11 | hora ET; la página no trae año (se infiere) y solo cubre ~6 semanas |
| Eurostat | iCal oficial, solo «Euro indicators» | 37 | sin hora (el iCal solo da fecha) |
| INE | calenHTML.htm (2026) | 59 | sin hora en la tabla; aún sin calendario 2027 |
| Fed | fomccalendars.htm | 2 | decisión a las 14:00 ET (habitual, no en la tabla). 27-ene-2027 = `aproximado:true` (calendario del año siguiente) |
| BCE | calendario Consejo de Gobierno | 5 | reuniones de política monetaria: 16-17 dic-2026 y 3-4 feb-2027 (+ 25-nov no monetaria, excluida de la lista de tipos) |

## Comparación con docs/movil/data.json (solo lectura, heurística por tema, ±12 días)
- Coinciden 4 temas clave; **0 fechas distintas**.
- **Faltantes (13):** FOMC 27-ene-2027; Eurostat flash IPCA 1-dic, 6-ene, 2-feb e IPCA definitivo 17-dic y 19-ene; INE IPC avance 27-nov y 30-dic, IPC 15-dic, IPCA, y PIB trimestral T3 el 23-dic. Detalle en `comparacion` del JSON.
- Limitación: la heurística busca palabras en el título; un evento cargado con otro título podría figurar como faltante. Revisar a mano.

## Cómo cruzarlo con el calendario (sin tocar calendario.toml)
1. `python scripts/leer_calendario_oficial.py` (semanal; `--seco` para solo mirar).
2. Leer `comparacion.faltantes` y añadir a `eventos/calendario.toml` solo lo que interese, copiando `fecha`, `fuente` = `url` y poniendo hora en el detalle (los `hora` del JSON llevan su `zona_horaria`).
3. Para un evento ya cargado, comparar su fecha con `eventos[].fecha` de ese organismo: `clave:true` marca los de mayor interés.
4. Los `aproximado:true` no deben tratarse como fecha firme.

## Pendientes / [VERIFICAR]
- Horas de Eurostat, INE y BCE: no figuran en sus calendarios; no se inventan (null).
- Refresco de la copia BLS depende de Chrome mientras bls.gov bloquee scripts.
