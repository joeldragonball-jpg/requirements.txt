# Gemini · NOTICIAS-DIA · Elecciones EE. UU. 3-nov (previa) · 2026-11-02

Ejecutado por Joel en Gemini (Pro alto o Deep Research, sin precisar). Respuesta cruda abajo; verificación mía debajo del JSON.

```json
{
  "evento": "Evento: EE. UU.: elecciones de mitad de mandato",
  "fecha": "2026-11-03",
  "nivel": "ligera",
  "generado_con": "Gemini",
  "noticias": [
    {"titulo": "Election results, 2026: U.S. Senate", "fuente": "Ballotpedia", "url": "https://ballotpedia.org/Election_results,_2026:_U.S._Senate", "fecha": "2026-11-02T17:00:00Z",
     "resumen": "Para estas elecciones, 35 de los 100 escaños del Senado están en la boleta, de los cuales 13 están clasificados como campos de batalla reñidos; los republicanos llegan defendiendo 53 escaños frente a los 47 demócratas.",
     "etiqueta": "VERIFICAR", "tema": "Geopolítica y política", "nota": 7, "bulo": false},
    {"titulo": "US midterm elections 2026: What they are, why they matter and when results will be out", "fuente": "Times of India", "url": "https://timesofindia.indiatimes.com/world/us/us-mid-term-elections/news/us-midterm-elections-2026-what-they-are-why-they-matter-and-when-results-will-be-out/articleshow/135451106.cms", "fecha": "2026-11-02T10:00:00Z",
     "resumen": "Se requiere una ganancia neta de 4 escaños en cada cámara para cambiar el control partidista; se advierte que la certificación del recuento estatal podría demorarse semanas, requiriendo que contiendas no resueltas sean decididas por la nueva Cámara en enero.",
     "etiqueta": "VERIFICAR", "tema": "Geopolítica y política", "nota": 7, "bulo": false}
  ]
}
```
(Campos `fiabilidad` y `motivo_bulo` omitidos aquí por brevedad; el crudo íntegro se pegó en el chat.)

## Verificación (Ballotpedia, «United States Congress elections, 2026», leída en Chrome el 2-nov; es agregador [S], no el organismo electoral)
| Dato de Gemini | Resultado |
|---|---|
| 35 escaños del Senado en juego | ✔ 33 regulares + 2 especiales (el de Rubio y el de J. D. Vance) = 35 [S] |
| Republicanos defienden 53 frente a 47 demócratas | ✔ matizado: 53 R frente a 45 D + 2 independientes que votan con los demócratas (47) [S] |
| 13 escaños «campos de batalla» | ✘ Ballotpedia sigue **12** (3 demócratas, 9 republicanos). La clasificación es una opinión de la web [S] |
| «Ganancia neta de 4 escaños en cada cámara» | ✘ Senado: sí, +4 para los demócratas (los republicanos pueden perder como máximo 2). **Cámara: +3** (hoy 218 R – 212 D, 4 vacantes) [S] |
| Certificación «semanas» y Cámara decide en enero | No verificado: no abrí el artículo de Times of India ni un texto estatal oficial [VERIFICAR] |

## Notas
- Ninguna fuente primaria (organismo electoral, secretarías de estado) leída: senate.gov devuelve 403 y no se contrastó con las webs estatales. Todo queda [S].
- Gemini marcó sus dos piezas como VERIFICAR, correcto. Fallos: cifra de campos de batalla (13 frente a 12) y +4 en ambas cámaras.
- Sin datos de XRP/XLM ni de mercado en la respuesta; no cambia ninguna conclusión de cartera.
- Pasa a `noticias/manuales/` solo lo verificado ([S]) y corregido: ver `noticias/manuales/2026-11-02-elecciones-previa.json`.
