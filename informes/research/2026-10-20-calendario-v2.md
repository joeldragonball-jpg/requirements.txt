# Calendario v2: fechas nuevas del radar y comprobación de avisos y mapamundi (2026-10-20)

Se añaden **10 fechas** a `eventos/calendario.toml` (de 56 a 66 eventos). No se borra ni se cambia ninguna. Sin IA ni red para los avisos; no se ha enviado nada por Telegram. Informativo, sin recomendaciones de compra/venta.

## 1. Fechas añadidas
| Fecha | Evento | Sale de | ¿Aproximado? | Por qué |
|---|---|---|---|---|
| 22-oct-2026 | Banco de Corea: reunión sobre el tipo base | Radar v2 (kr · política) | Sí | La fecha viene de un mercado de predicción y de prensa; el calendario del Banco de Corea no se leyó |
| 31-oct-2026 | OCC: objetivo de la norma final de la GENIUS Act | Radar v3/v4 (EE. UU. · stablecoins) | Sí | Declaración del Comptroller recogida por prensa |
| 3-4-nov-2026 | Copom (Selic 13,75 %) | Radar v2 (br · política) | Sí | Fecha de prensa brasileña; calendario oficial no leído |
| 20-nov-2026 | China: fijación del LPR | Radar v3 (cn · política) | Sí | Patrón mensual (día 20), no calendario leído |
| 1-ene-2027 | Brasil: retención de 24 h (Res. 584) | Radar (br · stablecoins), R03P, v4 | Sí | La Res. 584 está confirmada por el BCB, pero la fecha de vigencia sale de prensa [VERIFICAR] |
| 28-feb-2027 | Sudáfrica: fin del primer periodo del CARF | Radar v3 (za · fiscal) | **No** | SARS, fuente oficial |
| 1-jul-2027 | Rusia: solo operar a través de organizadores autorizados | Radar v4 (ru · ley marco) | **No** | Ley 282-ФЗ en kremlin.ru |
| 10-jul-2027 | UE: el AMLR se aplica a los CASP | Radar (ue · ley marco), R06P | Sí | Fecha del Reglamento 2024/1624 según analistas; EUR-Lex no se leyó hoy |
| 23-jul-2027 | Japón: fecha máxima de entrada en vigor de la FIEA | Radar v3 (jp · ley marco) | Sí | «Como tarde un año» lo dice un despacho; la FSA no lo publica |
| 1-sep-2027 | Rusia: segunda fase del rublo digital | Radar (ru · CBDC), R40, R01P | Sí | Prensa rusa; texto de la ley no leído |

**No se añaden porque ya estaban:**
- Comentarios de la Fed sobre GENIUS (30-nov) y fecha efectiva (18-ene-2027).
- Euro digital: acuerdo político (31-dic).
- Brasil: plazo de octubre (30-oct, aproximado).
- CFTC (14-dic) y custodia de la SEC (7-dic).
- Corea (11-nov y 4-feb-2027).
- Banco de Rusia y MAS (23-oct).
- Fed, BCE, BoJ y RBI.
- DAC8 y ESMA (8-ene-2027).

T03 solo aporta el 14-dic, que ya estaba.

**No se añaden por falta de día o por ser demasiado especulativas:**
- Informe de Estabilidad del RBI («dic-2026», sin día).
- Impuesto japonés del ~20 % («ene-2028», previsión).

**Propuesta sin aplicar** (no se tocan entradas existentes): el detalle del plazo de Brasil (30-oct) podría decir que el Voto 107/2026 del BCB confirma «octubre de 2026» (radar v4).

## 2. Avisos por Telegram (`eventos/avisos.py`), probado en seco
Se ejecutó `python eventos/avisos.py AAAA-MM-DD` sin `TELEGRAM_TOKEN` ni `TELEGRAM_CHAT_ID`, para que solo imprima. Fechas probadas: 21-oct-2026, 22-feb, 27-feb, 28-feb, 30-jun y 1-jul-2027.

- **Antelación:**
  - Aviso el **día antes** («Mañana»).
  - Aviso el **mismo día** («Hoy»).
  - Los **lunes**, resumen de los **próximos 7 días**.
  - No hay más antelación (ni una semana antes salvo en lunes, ni un mes).
- **Las aproximadas no se avisan** (`aproximado = true` se salta). De las 10 nuevas, solo se avisarán **Sudáfrica (28-feb-2027) y Rusia (1-jul-2027)**. Comprobado: salen el día antes, el mismo día y en el resumen del lunes 22-feb-2027.
- **Riesgo de avisos repetidos (ya existía, no es de esta tanda):** un evento con «hasta» sale en «Hoy» **todos los días** de su rango. El Modelo 721 (1-ene a 31-mar-2027) avisaría unos 90 días seguidos, y la campaña de la renta (abr-jun) lo haría si deja de ser aproximada.
  - Propuesta: avisar solo el primer y el último día del rango, o una vez por semana mientras dure. No se toca `avisos.py`, porque no es de esta tarea.
- **Sin duplicados** entre las 10 nuevas y las existentes (comprobado por fecha y título).

## 3. Mapamundi (`mundo.py`): clasificación de las 10 fechas nuevas
Se probó `mundo._paises()` y `explorador._tema_y_capa()` sobre las 10 entradas, sin editar ninguno de los dos archivos.

| Entrada | País | Tema | ¿Correcto? |
|---|---|---|---|
| Banco de Corea | kr | Regulación | **Tema mal:** debería ser macro |
| OCC y GENIUS | us | Regulación | Bien |
| Copom | br | Regulación | **Tema mal:** debería ser macro |
| LPR de China | cn | Macro | Bien |
| Brasil, Res. 584 | br | Regulación | Bien |
| Sudáfrica, CARF | za | Macro | **Tema mal:** debería ser fiscal |
| Rusia, organizadores | ru | Macro | **Tema mal:** debería ser regulación |
| UE, AMLR | **int** | Macro | **País y tema mal:** debería ser eu y regulación |
| Japón, FIEA | jp | Macro | **Tema mal:** debería ser regulación |
| Rusia, rublo digital | ru | CBDC | Bien |

**Correcciones propuestas** (para la sesión que lleva el mapamundi; aquí no se aplican):
1. **País, en `mundo.py` (`CLAVES_PAIS`):** añadir `"ue:"` y `" ue "` a la lista de `eu`. El texto plano de «UE:» no coincide hoy con ninguna clave.
2. **Tema, en `explorador.py` (`PALABRAS_TEMA`):** «corea» y «brasil» están en la lista de regulación, así que **cualquier** evento de esos países sale como regulación. Dos opciones:
   - Añadir al principio un grupo macro específico: `("macro", ["copom", "selic", "tipo base", "tipo clave", "banco de corea", "banco de rusia"])`.
   - O quitar «corea» y «brasil» de regulación.
3. **Fiscal:** añadir `"carf"` a la lista de fiscal.
4. **Regulación:** añadir `"fiea"`, `"282"`, `"antiblanqueo"`, `"amlr"` y `"organizadores"`.
5. **Duplicados en el mapamundi:** quita repetidos por fecha, país y los primeros 60 caracteres del título. La misma fecha llega a veces del calendario y del radar con títulos distintos (por ejemplo, CFTC del 14-dic: «CFTC: fin de comentarios…» y «Próxima fecha: Cierre de comentarios…»), así que **saldrá dos veces**. Propuesta: no añadir las «próximas» del radar si ya hay un evento del calendario ese día y en ese país.

## 4. Dudas que quedan
- Fechas oficiales del Banco de Corea (22-oct) y del Copom (3-4 nov): leer los calendarios oficiales para quitar «aproximado».
- AMLR (10-jul-2027): confirmar en EUR-Lex.
- Res. 584 (1-ene-2027): vigencia en el texto del BCB.
- Rublo digital (1-sep-2027): texto de la ley.
- Japón: orden del Gabinete con la fecha real.

## Comprobaciones
- `python -c "import tomllib;tomllib.load(open('eventos/calendario.toml','rb'))"`: **válido**, 66 eventos.
- Finales de línea LF.
- Solo se tocaron `eventos/calendario.toml` y este informe.
