# R39 · Auditoría final corta (lo escrito después de R31/R38) — 2026-10-20

Alcance:
- Aperturas y cierre del 17-oct.
- Revisión semanal del cerebro del 18-oct.
- R48 y R49.
- Glosario ampliado y cruce de fichas del 19-oct.
- Radar regulatorio v1 y v2.
- Informes de Gemini T01, T02 y T04.

Sin búsquedas nuevas: todo se contrasta dentro del repo. Etiquetas: [P] / [S] / [VERIFICAR] / [ESPECULACIÓN]. Sin recomendaciones de compra/venta.

## Resumen (5 líneas)
1. **14 hallazgos.** El más importante: la clasificación «efecto directo» de R48 **no se sostiene en 5 de 11 pares** si se aplica su propia regla.
2. Tres contradicciones abiertas antes de R31/R38 ya están **resueltas**: CLARITY 49-50 (no 50-49), voto de la Fed 12-0 y posición del Consejo sobre el euro digital (19-dic-2025, [S]).
3. Hay **dos etiquetas demasiado fuertes** en el radar v2:
   - La celda UE · CBDC va como [P], pero la posición del Consejo es [S] (la página dio 403).
   - El «techo de tenencia» del Consejo figura como hecho, y T04 lo deja [VERIFICAR].
4. El glosario ampliado dice «370 entidades» en MiCA; la precisión de R31 da **365 entidades en 370 filas** y R44 (oct) da **375**. Cifras de fechas distintas, sin aclarar.
5. Los 12 hallazgos de la revisión del cerebro del 18-oct siguen **sin aplicar**. Solo se pueden corregir añadiendo líneas (regla de CLAUDE.md), así que quedan para que Joel decida.

## 1. R48: ¿se sostiene el «efecto directo»?
Regla de R48 (fijada antes de mirar):
- **Directo:** cola ≤ 5 % en 1 h (solo con hora tipo A y sin otro hecho de calendario en ±3,5 h), o cola ≤ 5 % en 24 h **sin confusores en 24 h**.
- **Tipo B:** con hora aproximada no se usa la ventana de 1 h.

| Par | Hora | Confusor anotado en la propia tabla | ¿Cumple la regla? | Veredicto R39 |
|---|---|---|---|---|
| E02 XRP / XLM (Jackson Hole) | A | ninguno | Sí (1 h: 0,009 / 0,012) | **Se sostiene** (2) |
| E11 XRP / XLM (cierre de debate de CLARITY) | A | FOMC al día siguiente, fuera de la 1.ª hora | Sí (1 h: 0,002 / 0,004) | **Se sostiene** (2); es el caso más limpio |
| E15 XRP (sentencia Torres) | B | ninguno | Sí en 24 h (cola 0,000; exceso +61 %) | **Se sostiene** (1): la magnitud domina la incertidumbre de la hora |
| E18 XRP (SEC y Ripple desisten) | B, hora desconocida (se usa 12:00) | ninguno | En el límite (24 h: 0,03) | **Débil** (1): sin hora no se sabe si la ventana de 24 h empieza antes o después de la noticia |
| E06 XRP / XLM (la Fed sube) | A | caída de −10 % en las 24 h previas | Formalmente sí (la caída previa no es «hecho de calendario») | **Baja a dudoso** (2): el propio informe dice que un rebote técnico es igual de posible |
| E17 XRP / XLM (arancel a China) | B | cascada de liquidaciones y fallo de precio en Binance | **No:** la regla de 24 h exige «sin confusores en 24 h» | **Baja a dudoso** (2): mal clasificado por su propia regla |
| E19 XLM (DTCC-Stellar) | B, hora desconocida | otras noticias de Stellar esa semana [VERIFICAR] | No se sabe si el confusor cae dentro de las 24 h | **Baja a dudoso** (1) hasta fechar esas noticias |

**Resultado:** 11 «directo» → **5 se sostienen + 1 débil + 5 dudosos**. Con 32 pares al 5 % se esperan 2-3 falsos positivos por azar, así que **5 casos sólidos apenas superan el ruido**. La nota de revisión de R48 («léase "salen de lo normal"») va en la dirección correcta, pero no basta: E17 incumple la regla y debería reclasificarse en la tabla.

**Corrección propuesta a R48** (añadir una nota, no reescribir): «Tras R39: E17 (XRP y XLM) pasa a dudoso por su propia regla (confusores en 24 h); E06 y E19, a dudoso por confusor plausible. Recuento revisado: 5 directos, 1 débil (E18), 11 dudosos y 15 sin efecto».

## 2. Contradicciones y etiquetas (lo nuevo desde R31/R38)
| # | Dónde | Problema | Estado o propuesta |
|---|---|---|---|
| 1 | Apertura del 17-oct, §3 | CLARITY «49-50 (Decrypt) o 50-49 (Finance Magnates) [VERIFICAR]» | **Resuelto: 49-50** (R18, dossier CLARITY, T01, radar v2) |
| 2 | Apertura del 17-oct, §2 | Voto unánime de la Fed [VERIFICAR] | **Resuelto: 12-0** (R29, leído entero en federalreserve.gov) |
| 3 | Cruce de fichas, contradicción 1 | Posición del Consejo sobre el euro digital | **Resuelto en [S]:** 19-dic-2025 (radar v2 y T04); el texto oficial dio 403 |
| 4 | Radar v2, UE · CBDC | Celda con nivel [P] pese a que la posición del Consejo es [S] | Añadir [S] en la frase del Consejo (aplicado en la auditoría del Explorador) |
| 5 | Radar v2, UE · CBDC | «Techo de tenencia fijado por el BCE dentro de un máximo del Consejo», contado como hecho. T04 lo deja [VERIFICAR]; la fuente del radar es un resumen de buscador de Lewis Silkin | Marcar [S] (aplicado en la auditoría del Explorador) |
| 6 | Radar v2, EE. UU. · ley marco | Hitos desordenados (23-sep después de 5-oct) | Ordenar por fecha (aplicado) |
| 7 | T01 frente al radar v2 | T01: la moción de Tillis «sin fecha». Radar: 15-sep, por el registro del Senado según prensa (The Defiant, «3:01 p. m.») | No es contradicción: T01 dice que el artículo no la fecha y otra fuente sí la fecha; se mantiene el 15-sep [S] |
| 8 | Glosario ampliado, MiCA | «370 entidades»: R31 precisa 365 entidades en 370 filas (15-oct) y R44 cuenta 375 entidades en 378 filas (oct) | Propuesta: añadir línea con «365 (15-oct) / 375 (oct)» |
| 9 | Cruce de fichas, contradicción 8 | Fed y GENIUS: 24-sep (R08P) o 29-sep (Federal Register) | Sigue [VERIFICAR]. T02 confirma el 29-sep como publicación en el Federal Register; el 24-sep sería el anuncio, sin fuente leída |
| 10 | Apertura del 17-oct, §4 | «473 M XRP» en el cuerpo y en el caso alcista | Ya anotado con la nota de R23 (388,9 M en especie); correcto |
| 11 | Apertura-b del 17-oct, §2 | «Presidente Kevin Warsh» en una fuente secundaria | Sigue [VERIFICAR]; no se usó como dato (correcto) |
| 12 | Aperturas y cierre del 17-oct | Swell / XRPL Apex «27-29 oct [VERIFICAR]» | El calendario lo tiene el 27-oct; Meridian el 28-29 (R09P, R37). Sin fuente oficial de Ripple leída: sigue [VERIFICAR] |
| 13 | Revisión del cerebro del 18-oct | 12 hallazgos (Fed 3,50-3,75 % en el resumen, total de 4.000 M$ de Ripple, Cataluña, Evernorth 473 M…) sin aplicar | Para Joel: solo se puede corregir **añadiendo** líneas (CLAUDE.md) |
| 14 | R49 | Correcto tras su nota de revisión: «entre 47 y 61 %» y la hora como momento, no como «presión de venta» | Sin cambios |

## 3. Correcciones propuestas (resumen)
- **R48:** nota de reclasificación (sección 1). Es la más importante: cambia «11 directos» por «5 + 1 débil».
- **Radar UE · CBDC:** [S] en el Consejo y en el techo de tenencia. Aplicado junto con la auditoría del Explorador.
- **Glosario ampliado:** precisar el número de entidades MiCA con su fecha.
- **Cerebro:** decidir la redacción canónica de CLARITY («cierre de debate fallido», no «ley rechazada») y actualizar el resumen de la Fed. Solo añadiendo líneas.

## 4. Qué sigue [VERIFICAR] tras esta auditoría
- Texto oficial de la posición del Consejo (403).
- Anuncio de la Fed del 24-sep.
- Fecha y hora de las noticias de Stellar de la semana del 27-may.
- Hora de la sentencia Torres y del desistimiento SEC-Ripple.
- Swell en ripple.com.
- Kevin Warsh.
