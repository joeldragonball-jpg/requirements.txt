# BORRADOR: reglas para el filtro del bot de noticias, a partir de la guía G17 (2026-10-18)

> **Borrador para decidir, NO aplicado.** No he tocado `noticias/noticias.py` ni `noticias/config.toml`. No sube a GitHub hasta que Joel lo diga. Informativo; sin recomendaciones de compra/venta. Base: [G17](dossiers/2026-10-17-G17-como-verificar-noticias-cripto.md), `noticias/config.toml` y `noticias/noticias.py` (funciones `lecciones_texto`, `alertas_urgentes`, `SYSTEM_SELECCION`) leídos el 18-oct-2026. Etiquetas: **HECHO** (leído en el código/archivo) · **PROPUESTA** (mía) · **[VERIFICAR]**.

## 1. Qué ya hace el bot (HECHO, leído en el código)
- Triaje barato (Haiku) sobre títulos; luego selección (Sonnet) sobre los supervivientes; tope de gasto 12 $/mes (gasto normal 4-6 $, según el propio config).
- **Ya lee las lecciones del cerebro**: `lecciones_texto()` mete en el prompt los archivos `fuentes-fiables-y-dudosas.md` y `patrones-de-bulos.md` (3.200 caracteres en total: la selección; 2.000 en las alertas urgentes). Las instrucciones dicen: descartar o puntuar bajo lo que repita un patrón de bulo, y avisar de que «conviene verificarlo».
- Sin IA: desduplicado por parecido, enfriamiento por tema, no repetir noticias de los últimos 4 días, tope por tanda de XRP/XLM.
- Alertas urgentes: se vigilan cada hora por palabras clave; solo se llama a la IA (modelo barato) si un titular contiene una.

## 2. Hallazgo importante: las líneas técnicas desplazan a las útiles (HECHO + simulación mía)
`lecciones_texto()` conserva las **2 primeras líneas** del archivo y rellena el resto con las **líneas más recientes** hasta un presupuesto de 1.600 caracteres por archivo. Simulando esa función sobre los archivos actuales (cálculo mío, replicando el código):
- En `fuentes-fiables-y-dudosas.md` (67 líneas) entran **3 líneas recientes**: las de R40, R44 y R45 del 17-oct. Las tres son sobre **cómo abrir webs** (oeil.europarl, CSV de ESMA, NIST): útiles para research, **casi inútiles para filtrar titulares**.
- En `patrones-de-bulos.md` (75 líneas) entran 3: R40, R44+R45 y R46, que sí describen bulos (monederos vs activos, «aprobado» preliminar, escenario vs dato).
- Lo que se queda fuera por falta de espacio incluye lecciones muy útiles para un filtro: la de series distintas (R38), el eco entre medios, el titular reciclado y los patrones de R41 a R43.

**Consecuencia:** el filtro de noticias recibe el 17-oct más «recetas de curl» que «señales de bulo». No cuesta más dinero (el presupuesto de caracteres es fijo), pero desperdicia las lecciones.

## 3. Propuestas (cada una con efecto y coste estimado)
| # | Propuesta | Qué haría | Coste API | Riesgo |
|---|---|---|---|---|
| A | **Separar las lecciones por uso.** Crear un archivo corto `cerebro/documentos/senales-de-bulo-para-filtro.md` (≤1.500 caracteres, solo señales de titular) y hacer que `lecciones_texto` lea ese en vez de los dos largos; las «recetas de curl» se quedan en `fuentes-fiables-y-dudosas.md` | El prompt recibe siempre las mejores señales, no las 3 últimas líneas | **Igual o menor** (mismo presupuesto de caracteres) | Hay que tocar `noticias.py` y probarlo sin API |
| B | **Alternativa sin tocar código:** poner las líneas técnicas en otro archivo nuevo (p. ej. `fuentes-como-abrir.md`) y dejar en `fuentes-fiables-y-dudosas.md` solo valoración de fuentes (A/B/C/D) | Mismo efecto que A solo moviendo texto (pero la regla 5 de CLAUDE.md prohíbe reescribir `cerebro/`, así que habría que añadir líneas nuevas, no mover) | 0 | Choca con la regla de solo añadir |
| C | **Etiquetar fuentes por tipo A/B/C/D** (escala de R15) en el prompt de selección: «parte interesada (Ripple, SDF, exchanges, 21Shares) = tipo C: cifras de impacto solo con segunda fuente» | Baja la nota de una cifra de impacto sin primaria; mismo prompt, +1 línea | ≈0 (unas decenas de tokens por llamada) | Puede subestimar noticias legítimas de la propia empresa |
| D | **Reglas sin IA (código)**: descartar antes del triaje titulares con patrones de G17 §3: «price prediction», «XRP news today» sin fecha, dominios tipo D (mexc, changelly, remittix), y artículos con fecha de más de N días en el feed | Menos titulares llegan a Haiku → menos tokens | **Ahorra** (tamaño depende del volumen; no medido) | Falsos descartes; revisar el log de descartados una semana |
| E | **Nota de verificación obligatoria**: en «por qué te importa», si la noticia contiene una cifra de impacto, que el modelo escriba «Cifra no verificada: [serie, fecha]» o «Primaria: [fuente]» | Hace visible la checklist G17 en cada aviso | +~30 tokens de salida por noticia (céntimos al mes) | El modelo puede inventar la etiqueta: pedir que cite del texto |
| F | **Revisar `palabras_urgentes`**: «crash», «default», «sanctions», «hack», «prohibe», «ban crypto» son muy amplias (alto riesgo de falsos positivos con titulares sensacionalistas). Exigir además una **fuente A/B** o dos fuentes independientes antes de enviar una urgente | Menos alertas falsas | Igual o menor (menos llamadas de IA) | Podría retrasar una alerta real |
| G | **Distinguir verbo (hecho/propuesta/consulta)** en el prompt: «proposes/considering/consultation ≠ approves/enacts»; «aprobación preliminar ≠ final» (OCC) | Evita titulares tipo «Singapur prohíbe» sobre una consulta | ≈0 | Ninguno relevante |
| H | **Prueba de nombre del token**: si el titular habla de «adopción de XRP» pero el texto solo nombra la red/la empresa, añadir «no nombra XRP» (G17 pregunta 5) | Evita sobreinterpretar notas de Ripple (R34) | ≈0 | Requiere descripción del RSS con suficiente texto |

## 4. Texto sugerido para el prompt de selección (borrador, NO aplicado)
```
CHECKLIST ANTI-BULO (G17), úsala antes de puntuar:
1. ¿Quién lo dice y gana algo? (emisor, empresa, exchange, influencer = parte interesada).
2. ¿La fecha del dato es reciente o es un artículo antiguo reciclado?
3. ¿Es hecho, propuesta o consulta? («proposes», «considering», «preliminary» no son «approves» ni «enacted»).
4. ¿El texto nombra XRP/XLM o solo la red o la empresa?
5. Cifra de impacto (volúmenes, adopción, flujos): ¿trae serie, ventana y fecha? Si no, puntúa bajo o avisa «cifra no verificable».
6. N medios que copian a uno = 1 sola fuente.
Nunca afirmes que algo «no existe» porque no aparezca en el titular.
```
Longitud aproximada: unos 900 caracteres (~250 tokens) por llamada de selección. Con 4 franjas diarias son ~1.000 tokens/día de entrada extra (Sonnet 5.5: 2 $ por millón de tokens de entrada según la tabla del propio `cerebro.py`) ⇒ **≈0,06 $ al mes** (cálculo mío: 1.000 × 30 / 1.000.000 × 2 $). Con caché podría ser menos.

## 5. Coste global estimado de aplicar las propuestas
| Cambio | Efecto en API |
|---|---|
| A (archivo de señales, mismo presupuesto) | ≈0 |
| C + G + H + E (líneas de prompt) | +0,05-0,15 $/mes (cálculo mío; no medido) |
| D + F (filtros sin IA / menos urgentes falsas) | Reduce llamadas; magnitud **no medida** [VERIFICAR con una semana de log] |
| Total | Dentro del tope de 12 $/mes; el gasto normal declarado es 4-6 $ |
**No he medido el gasto real** (para eso haría falta `registro de uso`, que vive en la rama `datos`). Antes de aplicar nada, mirar el gasto de las últimas 4 semanas y compararlo después.

## 6. Plan de aplicación propuesto (si Joel da el OK)
1. Añadir (no reescribir) un archivo nuevo de señales cortas (A) o ajustar `lecciones_texto` para leerlo.
2. Probar `noticias.py` **sin API**: ejecutar `lecciones_texto()` y mirar el texto que se enviaría; revisar el prompt final.
3. Aplicar C/G/H/E (líneas de prompt) en una rama o commit aparte, con la fecha, para poder revertir.
4. Una semana después: revisar el log de descartados (D), las urgentes enviadas (F) y el gasto del mes.
5. No lanzar el workflow de noticias a mano sin avisar (gasta API).

## 7. Qué no sé
- Cuánto gasta hoy exactamente el bot por franja y por urgentes (no lo he leído).
- Cuántos titulares son hoy de dominios tipo D (no hay estadística).
- Si el modelo respeta bien la nota «cifra no verificada» sin inventarla (hay que probar).
- Hasta dónde llega el RSS de Google News como descripción (a veces solo el título).
