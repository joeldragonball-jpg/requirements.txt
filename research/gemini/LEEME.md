# Research sin Claude: prompts para Gemini Deep Research

Cada archivo es un prompt AUTOCONTENIDO (sin rutas ni herramientas de Claude) equivalente a una rutina de `research/prompts/`. Úsalos cuando la suscripción de Claude haya terminado.

| Archivo | Rutina | Cuándo |
|---|---|---|
| `W01-tipos.md` | Tipos de interés | lunes y tras cada reunión de bancos centrales |
| `W02-deuda.md` | Deuda, subastas, calificaciones | martes |
| `W03-paises.md` | Regulación por países | miércoles (di el país) |
| `W05-verificacion.md` | Verificar [VERIFICAR] | jueves (pega la lista) |
| `W06-voces.md` | Voces y predicciones | viernes (pega las que vencen) |
| `W10-energia.md` | Energía y geopolítica | fin de semana |
| `EV-post-evento.md` | Tras un evento del calendario | cuando `research/PLANNING.md` diga «SIN research» |
| `EV-noticias-evento.md` / `EV-noticias-ligera.md` | Noticias manuales en JSON (C18) | día de evento / tanda de tarde 20:00 |
| `G01`…`G06` | Rutina G (C20), 1 por día | lun/dom XRP-XLM · mar macro · mié cripto-reg · jue ETF · vie bulos · sáb energía |

Pasos: 1) abre el archivo y copia el bloque de código; 2) pégalo en Gemini Deep Research y añade lo que pida (país, evento o lista); 3) contrasta 2-3 datos clave con la fuente primaria antes de fiarte (Gemini puede inventar enlaces); 4) vuelca el resultado al repo siguiendo el apartado final de cada archivo. Ver también `MANTENIMIENTO.md`.

**Noticias del día (27-oct-2026):** `NOTICIAS-DIA.md` es el prompt único de noticias con tema (xrp-xlm, macro-tipos, cripto-regulacion, etf-flujos, bulos, energia-geopolitica, tarde, evento). Sustituye a G01-G06, EV-noticias-ligera, EV-noticias-evento y EV-post-evento, que quedan en `antiguos/`. Se copia desde el Seguimiento del móvil (tarjeta «Tarea para Gemini»).
