# C98 · Segunda pasada de la auditoría de visión (Opus, 3-nov-2026)

Segunda pasada sobre `informes/research/2026-11-03-C81-auditoria-vision.md` (C81). No repite lo que C81 ya dejó bien: lo verifica, lo corrige donde falla y profundiza en seguridad, en la elección entre app y web, en el modelo de cruces y en la medición. Nombres fijos: **cerebro de seguimiento** (móvil, `docs/movil/`) y **terminal de inteligencia personal** (escritorio, `app.py`).

Etiquetas: **HECHO** = comprobado hoy en el repo o con un comando (se cita archivo:línea). **OPINIÓN** = juicio mío. **[VERIFICAR]** = no se puede comprobar desde el repo. **[ESPECULACIÓN]** = previsión. No hay recomendaciones de compra o venta ni consejo legal.

Seguridad diaria (3-nov): `scripts/seguridad_rapida.py` da 🟢 **sin novedades** (78 paquetes, 1172 commits, 1 entrada KEV ya vista). Las 14 «observaciones de endurecimiento» del script se tratan en el §2.

## Resumen (5 líneas)
1. C81 acierta en el diagnóstico general, pero **se equivoca en los cimientos de los cruces**: no existe un `pais_id` común (hay **tres esquemas** de id de país) y los 108 eventos de `calendario.toml` **no tienen id**. C91 no puede empezar sin dos tareas previas pequeñas (C99 y C100).
2. **Fallo nuevo en seguridad (Medio):** la huella `?k=` de la terminal se envía con `postMessage(..., '*')` a **cualquier** página que tenga la app dentro de un marco, y además se guarda en `localStorage` del dominio `joeldragonball-jpg.github.io`, el mismo que usa el móvil. Es una contraseña permanente: no caduca y solo se anula cambiando `APP_CLAVE`, que además abre el chat de pago.
3. **Pasar el repo a privado tiene un coste que C81 no vio:** los bots se lanzan ~123 veces al día. En un repo público los minutos de Actions son gratis; en uno privado, solo los bots de cada 30 min ya pasarían la cuota gratuita [VERIFICAR cuota]. Además, «Pages privado» exige GitHub Enterprise Cloud.
4. **Medición:** hoy hay 58 predicciones (13 con resultado, 4 ya vencidas sin resolver). Con n=10, un 70 % de aciertos tiene un intervalo del 95 % de **40-89 %**: por eso no se puntúa a nadie todavía. Lo que sí se puede medir ya es la **exactitud de datos** (los lotes de verificación).
5. **Hoja de ruta:** 10 tareas nuevas (C99-C108). Propongo reordenar C86-C96 con la seguridad barata primero, fusionar C87 con C95 y reducir C90 a tamaño S, porque buena parte de esa revisión ya está hecha aquí.

---

## 1. Verificación de la primera pasada (12 afirmaciones)

| # | Qué dice C81 | Evidencia hoy | Veredicto |
|---|---|---|---|
| 1 | «0 secretos en 728 commits» | `seguridad_rapida.py` (3-nov): **1172 commits**, 0 hallazgos; `git log --all --name-only` nunca contiene `privado/`, `.env` ni `secrets.toml` | **Corregida** (la cifra es del 30-oct; la conclusión se mantiene) |
| 2 | «12 workflows» | `.github/workflows/*.yml` = **13** | **Corregida** |
| 3 | «4 llaman a la API de Anthropic» | `ANTHROPIC_API_KEY` solo en `cerebro`, `noticias`, `revision` y `verificar`. Matiz: `votos.yml:25` instala `anthropic` sin usarlo | **Confirmada** |
| 4 | «El Worker lanza paneles 3 veces al día, de lunes a viernes» | `cloudflare-lanzador-bots.js:14,20`. **Omite** que el Worker lanza también `noticias.yml` (bot de pago) cada hora (`:24`) y alertas + onchain cada 30 min (`:7-10`) | **Confirmada pero incompleta** |
| 5 | «`pais_id` en paises/elecciones/estabilidad/regulación, con valores `eeuu`, `ue`, `br`» | `paises`, `elecciones` y `estabilidad` usan el campo **`id` en ISO-2** (`ES`, `US`, `BR`). `calificaciones` usa **ISO-3** (`ESP`, `USA`). `regulacion.jurisdicciones` tiene `id` en minúsculas (`eeuu`) y `pais_id` en ISO-2 (`US`). `pais_id` como nombre de campo solo existe en `regulacion.json`, `datos.json` y `indice/*` | **Corregida**: hay 3 esquemas |
| 6 | «`evento_id` con formato AAAA-MM-DD-slug, igual que `calendario.toml`» | `calendario.toml` tiene 108 eventos con `fecha`, `titulo`, `detalle`, `impacto` y `fuente` (más `hasta` y `aproximado`). **Ningún `id`**. `eventos/revisados.json` usa otra clave: `AAAA-MM-DD\|primeras palabras` | **Corregida** |
| 7 | «~57 predicciones; 43 sin resolver; ~14 con resultado» | `informes/predicciones.md`: **58** filas; 45 «Sin resolver» y **13** con resultado; **4 vencidas sin resolver** (#7, #25, #31, #44); 3 sin fecha | **Corregida** (cifras cercanas) |
| 8 | «`time.sleep(1)` tras el fallo, `app.py:~397`» | `app.py:400`. Solo frena a esa sesión: otra pestaña o una recarga empiezan de cero | **Confirmada**; el riesgo real es mayor de lo que dice C81 |
| 9 | «Candado opcional; cerrarlo es cambiar una línea» | El hecho se confirma (`app.py:370-371`). El arreglo no: `candado()` se ejecuta (`:478`) **antes** de calcular `_LOCAL` (`:483`), así que cerrar por defecto sin más también bloquearía el uso en el ordenador | **Hecho confirmado; arreglo corregido** |
| 10 | «[VERIFICAR] que todo el texto del móvil pase por `esc()`» | `docs/movil/index.html`: `esc()` aparece 271 veces; hay 4 `innerHTML`, todos montados con `esc`. Sin escapar quedan solo números (`int()` en `construir_movil.py:131`) y constantes internas. **Hueco:** `href="${esc(c.u)}"` (`:240`) no filtra `javascript:`. No hay CSP | **Verificada** (ver S8) |
| 11 | «Dossiers lee solo `informes/dossiers` (`cerebro.py:20`)» | `cerebro.py:20` | **Confirmada** |
| 12 | «Pages privado» como opción para la familia | Según la documentación de GitHub, el acceso privado a Pages solo existe con **GitHub Enterprise Cloud** y en repos de una organización | **Corregida** |

Otras ya resueltas o confirmadas: los ids duplicados C80/C81 quedaron arreglados (commit `37d8531`; hoy hay 0 duplicados en 226 filas). `voces.json` tiene 62 voces y `GRAPH_REPORT.md` es del 18-oct (confirmado por la fecha del archivo).

---

## 2. Seguridad a fondo

Gravedad = impacto × probabilidad **hoy** (uso personal, repo público). Entre paréntesis, cómo cambia si se abre a la familia o a terceros.

| ID | Hallazgo | Gravedad | Evidencia | Arreglo concreto |
|---|---|---|---|---|
| **S1** | La **huella `?k=` es una contraseña permanente que se filtra**: (a) `listo()` la manda con `postMessage(..., '*')`, de modo que una web ajena que meta la app en un marco y consiga que escribas la contraseña la recibe; (b) se guarda en `localStorage` de `joeldragonball-jpg.github.io`, el mismo origen que el móvil y que cualquier otro Pages de tu cuenta; (c) no caduca, y la única forma de anularla es cambiar `APP_CLAVE`, que también abre el chat de pago | **Media** (Alta al compartir enlaces) | `app.py:373-374, 398, 466`; `docs/index.html:75, 97-98` | 1) En `listo()`, `postMessage(..., 'https://joeldragonball-jpg.github.io')`. 2) Huella con caducidad: `HMAC(clave, "v2\|AAAA-MM")`, aceptando el mes actual y el anterior. 3) No guardarla en `localStorage` o guardarla con fecha de caducidad. 4) A medio plazo, sustituirla por un inicio de sesión de verdad (§3) |
| **S2** | **Límite de intentos solo por sesión**, tanto en la app como en el chat. El `sleep(1)` no frena intentos en paralelo | **Media** (Alta si la clave es corta) | `app.py:400`; `cerebro.py:640-648` | Lo más barato: una `APP_CLAVE` de ≥ 16 caracteres aleatorios hace inviable la fuerza bruta. Además, llevar un contador persistente en la rama `datos` |
| **S3** | **Por defecto, abierta**: sin `APP_CLAVE`, la app queda abierta y el chat **también** (`chat_desbloqueado` avisa, pero devuelve `True`) | **Media** | `app.py:370-371`; `cerebro.py:634-637` | Calcular `_LOCAL` **antes** de `candado()`. Si no es local y falta la clave, `st.stop()` con un mensaje genérico. En el chat, devolver `False` |
| **S4** | El **tope del chat (40 preguntas al día) solo vale entre sesiones si hay `GITHUB_TOKEN` en los Secrets de Streamlit**; sin él, cuenta por sesión y una recarga lo pone a cero. Ese token, si existe, escribe en un repo público | **Media** | `cerebro.py:628, 662-664, 739-744` | [VERIFICAR] en Streamlit si el secreto existe. Token fine-grained solo con `contents:write` en este repo. **Tope mensual de gasto en la consola de Anthropic** como red final [VERIFICAR la opción exacta] |
| **S5** | **Workflows:** 5 sin bloque `permissions` (alertas, despertador, escrow, eventos, onchain); 7 hacen `pip install` sin versión; Actions fijadas por etiqueta (`@v4`/`@v5`), no por SHA. En un mismo job conviven la clave de Anthropic, el token de Telegram y `contents: write` | **Media** (cadena de suministro) | Resumen por workflow (comando de esta sesión); salida de `seguridad_rapida.py` | `permissions: contents: read` por defecto y `write` solo donde haga falta. `requirements-bots.txt` con versiones fijas y `--require-hashes`. Actions por SHA. Quitar `anthropic` de `votos.yml` |
| **S6** | **Worker lanzador:** **no** se puede lanzar desde fuera (`fetch()` solo devuelve un texto, `:44-46`): bien. El riesgo está en su token: con `Actions: write`, un token fine-grained puede lanzar **cualquier** workflow del repo, también los 4 de pago, y no hay forma de limitarlo a uno solo | **Media-baja** | `cloudflare-lanzador-bots.js:28-37` | Token fine-grained: solo este repo, solo Actions, caducidad de 90 días y recordatorio para rotarlo. Opcional: un input `origen=worker` que los bots de pago ignoren salvo `noticias` |
| **S7** | **Segundo Worker (votos de Telegram), sin código en el repo.** Se autentica con `Bearer sha256(TELEGRAM_TOKEN)`: si se filtra el token de Telegram, también queda abierto el Worker | **Desconocida** [VERIFICAR] | `noticias/noticias.py` (`worker_cabeceras`, `WORKER_URL`); `votos.yml:35` | Copiar su código al repo (sin secretos) para auditarlo y comprobar que valida la cabecera `X-Telegram-Bot-Api-Secret-Token` del webhook |
| **S8** | **XSS en el móvil:** riesgo bajo con los datos actuales (S1 lo agrava, porque comparten origen). Enlaces sin filtro de esquema; no hay Content-Security-Policy | **Baja** (Media si entran enlaces de RSS) | `docs/movil/index.html:211, 240`; ninguna etiqueta CSP | Función `url()` que acepte solo `https:`. `<meta http-equiv="Content-Security-Policy">` con `connect-src` limitado a CoinGecko, docs.google.com, api.github.com y raw.githubusercontent.com |
| **S9** | **Hoja de tareas publicada en el móvil** (intencionado). Si es **el mismo documento de Google** que la cartera y se publicó «el documento entero», con ese id y otro `gid` se leen las pestañas de la cartera | **Desconocida → Alta si coinciden** [VERIFICAR] | `docs/movil/index.html` (`HOJA_CSV`); `app.py:553` | Joel: en Google Sheets → Archivo → Compartir → Publicar en la web, comprobar que el documento de tareas **no** es el de la cartera y que solo está publicada la pestaña necesaria |
| **S10** | **Privacidad del repo público:** no hay secretos ni importes. Búsqueda en `main`: 0 correos de Gmail, 0 IBAN, 0 teléfonos +34, 0 `chat_id` y 0 frases del tipo «tengo N XRP». Pero el nombre «Joel» aparece en **150 archivos**, junto con el usuario de GitHub y la dirección de la app de Streamlit (`docs/index.html:72`): el perfil inversor es atribuible a una persona. La rama `datos` es pública (`noticias.json`, `uso/*.json`); el uso del chat guarda solo tokens, no las preguntas (`cerebro.py:729-732`) | **Baja** hoy (Media si hay familiares) | `git grep` de esta sesión; `git ls-tree origin/datos` | Entra en C87/C95: separar contenido y motor (§3) |
| **S11** | **Resiliencia:** el móvil llama a `api.github.com` sin autenticar, con un límite de 60 peticiones por hora e IP. Esta misma auditoría chocó hoy con ese límite desde esta IP. En una red de casa compartida, el refresco de rutinas falla sin avisar (`catch` vacío) | **Baja** | `docs/movil/index.html:619-624` | Que `construir_movil.py` escriba las fechas en `seguimiento.json` y quitar esa llamada |

**Lo que está bien (HECHO):** las entradas de los workflows pasan por `env:` y no por `${{ }}` dentro de `run:`, así que no hay inyección de scripts (`cerebro.yml:45-49`). No hay disparadores peligrosos (`pull_request_target`, `issue_comment`). `SHEET_ID` solo se usa en el servidor (`app.py:553, 667`). La página de entrada comprueba el origen de los mensajes (`docs/index.html:92`). La clave se compara con `hmac.compare_digest`.

**Orden de arreglo (OPINIÓN):** S9 (5 min, lo hace Joel) → S1(1) + S3 (≈30 líneas, una tarea S) → S5 → S6/S4 (paneles de Cloudflare, GitHub y Anthropic: lo hace Joel) → S7 → S8 → S11.

---

## 3. Arquitectura de salida: app vs web

C81 ya comparó app nativa y PWA (la nativa no compensa). Aquí se comparan las **tres formas reales** de cerrar lo que ya existe.

| | **A. PWA estática + Cloudflare Access** | **B. Repo privado + espejo público mínimo** | **C. Streamlit desplegada con inicio de sesión (`st.login`, OIDC de Google + lista de correos)** |
|---|---|---|---|
| Qué protege | Móvil y página de entrada (y `data.json`) | El contenido: informes, cerebro, research, memoria operativa | La terminal (cartera, cerebro, chat) |
| Coste fijo | Dominio propio ~10-15 €/año [VERIFICAR]; Access gratis hasta **50 usuarios** (página de precios de Cloudflare) | Minutos de Actions: hoy ≈ 96 lanzamientos al día de alertas/onchain + 24 de noticias + 3 de paneles ≈ **≥ 3.700 min/mes** (mínimo 1 min por job) frente a la cuota gratuita de los repos privados (2.000 en Free; 3.000 en Pro) [VERIFICAR cuota y duración real] | 0 € en Community Cloud [VERIFICAR límite de apps privadas] |
| Esfuerzo | Medio: mover `docs/` a Cloudflare Pages y servir todo desde allí (el móvil hoy lee `raw.githubusercontent` y `api.github.com`) | Alto: dividir el repo; bots y Pages apuntando al privado; reescribir rutas | Bajo-medio. **Pero `st.login` no funciona con la app dentro de un marco** (documentación de Streamlit): la página de entrada `docs/index.html` dejaría de servir y habría que abrir la app directamente |
| Cómo se tumba: DoS | Muy difícil (CDN de Cloudflare) | Igual que hoy | Fácil: Community Cloud duerme, tiene poca memoria y no tiene SLA. Para la familia vale; para terceros no |
| Cómo se tumba: abuso de la API de pago | No aplica (estática) | Baja el riesgo al ocultar los workflows | El chat queda detrás del inicio de sesión; falta un tope persistente por usuario (S4) |
| Cómo se tumba: fuga de datos | Por una regla de Access mal configurada | Por una mezcla accidental en el espejo | Por el correo del invitado comprometido o la cookie de 30 días |

**Recomendación por fases (OPINIÓN):**
- **Fase 0 (ya, coste 0):** S1-S5 y S9. Con eso, el uso actual (solo Joel) queda razonablemente cerrado.
- **Fase 1 (familia):** opción **C** para la terminal, abriéndola directamente sin marco, y opción **A** para el móvil. Las dos con Google como identidad y una lista de 3-5 correos.
- **Fase 2 (solo si se monetiza):** opción **B**, pero **antes** sacar los bots frecuentes (alertas y onchain) de Actions a un Worker que haga el trabajo él mismo (el plan gratuito de Workers admite muchas peticiones al día [VERIFICAR]). Si no, el repo privado sale caro en minutos. [ESPECULACIÓN: los bots de alertas y onchain son llamadas HTTP más un aviso por Telegram; encajan en un Worker.]
- **Qué NO hacer:** una app nativa; «Pages privado» (exige Enterprise); un backend propio con base de datos antes de tener usuarios.

---

## 4. Modelo de cruces `país ↔ evento ↔ activo ↔ voz ↔ predicción`

**Ids comunes** (la mitad ya existe; los nuevos los aportan C99 y C100):
- `pais`: **ISO-2 en mayúsculas** (`ES`, `US`, `BR`; `EU` para la UE), que ya usan 4 ficheros. Una tabla `explorador/ids/paises.json` con alias (`ESP→ES`, `eeuu→US`), para no reescribir `calificaciones.json`.
- `evento`: `ev-AAAA-MM-DD-slug`, escrito **una sola vez** como campo `id` en `calendario.toml`. No se deriva del título, porque si el título cambia se rompe el enlace.
- `activo`: una lista cerrada y corta (`XRP`, `XLM`, `BTC`, `ETH`, `BRENT`, `EURUSD`, `UST10Y`, `SELIC`…).
- `voz`: `v###` (ya existe). `pred`: `p###` = la columna `#` de `predicciones.md`, congelada. `informe`: la ruta.
- **Tesis:** nunca va en el repo. `privado/enlaces-tesis.json` relaciona `{id_enlace → referencia de hipótesis}`; el repo público solo conoce el `id_enlace`.

**Esquema mínimo de `explorador/enlaces.json`** (cada fila es un «hilo» que une varias cosas, no una relación de dos):
```json
{"id": "e0003", "tema": "CLARITY Act", "pais": ["US"], "evento": ["ev-2027-01-03-fin-119-congreso"],
 "activo": ["XRP", "XLM"], "voz": ["v018", "v019", "v020", "v059", "v008"], "pred": ["p001", "p002", "p006", "p051"],
 "informe": ["informes/research/2026-11-02-W05b-clarity-seccion-404.md"], "nivel": "relacionado", "revisado": "2026-11-03"}
```
`nivel` solo dice «relacionado» o «fuente de»; **nunca un efecto en el precio** (eso sería opinión y va en el informe).

**Tres casos hechos a mano con datos reales del repo:**

| Hilo | País | Eventos (de `calendario.toml`) | Activo | Voces | Predicciones | Informes y datos | Hueco que destapa |
|---|---|---|---|---|---|---|---|
| **e0001 Brasil: autorización de proveedores cripto** | `BR` (elecciones `BR` 25-oct; regulación `br`) | Copom (hasta el 4-nov); 6-nov (Res. BCB 589: bancos sin proveedores no autorizados); **29-nov** (cese de quien no pidió autorización); 1-ene-2027 (Res. BCB 584, retención de 24 h) | `SELIC`, cripto en general | **ninguna** | ninguna | `2026-10-24-T11-brasil.md`, `2026-11-02-C30-elecciones-eeuu-brasil.md`, `2026-10-15-R03P-brasil-profundo.md`; panel Brasil SGS/Focus | Hay 4 fechas reguladas y **ninguna voz ni predicción**: tema sin seguimiento de fuentes |
| **e0002 Ormuz y petróleo** | `US` (Irán no está en `paises.json`) | OPEP 11-nov; AIE 13-nov; OPEP+ 1-nov | `BRENT` | **ninguna** en `voces.json` | `p017` (EIA, Brent a 105 $ en el 4T), `p024` (Araqchi, Ormuz, **límite 30-nov**), `p027`, `p054` (Goldman, 90 $) | `2026-10-17-R46-geopolitica-energia-ormuz-profundo.md`; panel `ormuz` (`ultimo`, `media_7d`); `hitos_petroleo.json`; verificación `2026-11-02-A-ormuz-petroleo` | EIA, Goldman y Araqchi «predicen», pero **no existen como voces**: no se les puede seguir el historial |
| **e0003 CLARITY Act** | `US` | Fin del 119.º Congreso (3-ene-2027) | `XRP`, `XLM` | `v008`, `v018` (McHenry), `v019`, `v020`, `v059` | `p001` (Lummis), **`p002` (McHenry)**, `p006` (Polymarket), `p051` | `2026-11-02-W05b-clarity-seccion-404.md`; regulación `US` | La predicción `p002` es de McHenry = `v018`, pero **hoy nada las une** (la columna «Quién» es texto libre) |

Coste de poblarlo (OPINIÓN): ~1 % semanal con Sonnet, una vez hechos C99 y C100. Unas 20-30 filas cubren los temas que ya se siguen. Se muestra como un filtro «relacionado» en las vistas que ya existen (Países, Voces, Centro), **sin capa nueva**.

---

## 5. Medición: qué falta para puntuar sin inventar porcentajes

**HECHO:** 58 predicciones: 13 con resultado, 45 sin resolver (4 ya vencidas: #7, #25, #31 y #44) y 3 sin fecha. Fechas límite: 9 en nov-2026, 13 en dic-2026 y 8 en jun-2027. **La primera tanda grande para puntuar llega a principios de enero de 2027.**

**Por qué no hay porcentajes (matemáticas, no opinión):** intervalo de Wilson al 95 % para un 70 % observado:
- n = 10 → **40-89 %**. No distingue a una fuente buena de una que acierta por azar.
- n = 30 → **52-83 %**. Empieza a servir.

Regla propuesta: mostrar los **recuentos** (n, aciertos, fallos) y no mostrar un % hasta n ≥ 10 resueltas por fuente. El % siempre va con su intervalo.

**Lo que falta (en orden):**
1. **Criterio escrito antes de resolver:** cada predicción lleva `fecha_limite`, `fuente_resolucion` (primaria) y `criterio` («se cumple si…»). Sin esto, quien resuelve sesga el resultado.
2. **Clases** (cada una se puntúa aparte):
   - **A**, hecho programado («¿se aprueba X antes de F?»).
   - **B**, cifra con rango («Brent medio del 4T entre…»).
   - **C**, direccional sin fecha («subirá mucho»): **no se puede puntuar**; queda archivada como opinión.
3. **Resultados posibles:** acierto / fallo / parcial / anulada (mal planteada) / vencida sin dato.
4. **Una referencia ingenua contra la que comparar** («no cambia nada» o «sigue el statu quo»). Acertar que la CLARITY no se aprueba en 2026 vale poco si esa era ya la referencia. Solo se acredita lo que mejora a la referencia.
5. **Puntuación de Brier solo cuando la fuente dio una probabilidad** (p. ej., `p006` Polymarket, 15-23 %); casi ninguna voz la da.
6. **`voz_id` en cada fila** (depende de C91), para sumar por fuente.
7. **Exactitud de datos ≠ acierto de predicciones.** La primera ya se puede medir con los lotes de `research/verificaciones/` (confirmado / corregido / sigue [VERIFICAR]) y acumula n mucho más rápido. Es el primer contador que merece aparecer en el Seguimiento.

---

## 6. Research profundo que lanzar y reordenar C86-C97

**Tareas nuevas (ninguna duplica C86-C97):**

| ID | Qué | Valor | Coste | Riesgo | Prompt de una línea |
|---|---|---|---|---|---|
| C99 | Unificar ids de país (ISO-2 + tabla de alias) | Alto (desbloquea C91) | Sonnet S ~1 % | Bajo | «Crea `explorador/ids/paises.json` con ISO-2 y alias de `calificaciones` y `regulacion`; valida que todos los ficheros resuelven; sin renombrar campos existentes.» |
| C100 | `id` estable en los 108 eventos de `calendario.toml` | Alto (desbloquea C91) | Sonnet S ~1 % | Bajo | «Añade `id = "ev-AAAA-MM-DD-slug"` a cada evento; script que falle si falta o se repite; migra `revisados.json`.» |
| C101 | Endurecer workflows (S5) | Alto | Sonnet S ~1 % | Bajo | «`permissions` mínimos en los 13, `requirements-bots.txt` con hashes, Actions por SHA, quitar `anthropic` de `votos.yml`; sin lanzar nada.» |
| C102 | Inventario de secretos y tokens fuera del repo | Alto | Joel + Sonnet S | Bajo | «Plantilla en `privado/` con secreto, dónde vive, alcance, caducidad y fecha de rotación (Streamlit, 2 Workers, GitHub, Anthropic, Telegram); Joel la rellena; nunca valores.» |
| C103 | Auditar el Worker de votos (S7) | Medio | Sonnet S ~1 % | Bajo | «Joel pega el código sin secretos en `scripts/`; revisa la autenticación, la validación del webhook y las rutas expuestas.» |
| C104 | Parche S1 + S3 en `app.py` y `cerebro.py` | Alto | Sonnet S ~1,5 % | Bajo | «`postMessage` con origen fijo, huella con caducidad mensual, cerrado por defecto fuera del PC, chat cerrado sin clave; prueba local.» |
| C105 | Copias y recuperación | Medio | Sonnet S ~1 % | Bajo | «`git bundle` semanal de `main` + `datos` a disco local y Drive; ensayo de restauración; qué pasa si GitHub suspende la cuenta.» |
| C106 | Bots frecuentes al Worker (requisito de B) | Medio (solo si hay repo privado) | Sonnet M ~3 % | Medio | «Diseña alertas y onchain como Worker sin Actions; cuota del plan gratuito; sin desplegar.» |
| C107 | Qué NO construir: comparativa con terminales existentes | Medio | Sonnet M ~3 % (web) | Bajo | «Compara OpenBB, Koyfin, TradingView y paneles de bancos centrales frente a la terminal: qué hacen gratis y qué aporta solo la tuya (cruces, voces, España).» |
| C108 | Criterios de medición y relleno de las 58 predicciones | Alto | Sonnet M ~3 % | Bajo | «Añade criterio, fuente de resolución, clase A/B/C y referencia a cada fila; resuelve las 4 vencidas; sin porcentajes.» |

**Reordenación de las existentes (OPINIÓN):**
1. **Primero (seguridad barata):** S9 (Joel) → C104 → C101 → C88 → C102 → C103.
2. **Después:** **C89 queda absorbida por C104** (sobra como tarea aparte). **C90 baja a S**: solo la función `url()` y la CSP, porque el resto ya está verificado aquí.
3. **Cimientos:** C99 → C100 → C91 → C108 → C92 (C92 pasa a ser solo el script de vencimientos y el contador).
4. **Navegación:** C86, y C94 sin la parte de graphify, que es un comando.
5. **Decisión de arquitectura:** **fusionar C87 con C95** en una sola tarea Opus M, que parta de este §3 y del inventario de C102.
6. **Al final:** C93 y C96. C96 conviene prepararla con las fuentes oficiales (CNMV/ESMA sobre recomendaciones de inversión y *finfluencers*) **antes** de ir al asesor [VERIFICAR].

**Falta en la hoja de ruta (y queda cubierto arriba):** copias de seguridad (C105) y una auditoría que tenga en cuenta el coste de los minutos de Actions.

---

## 7. Visión a gran escala

**HECHO (lo que ya hay y es raro de encontrar junto):** datos vivos de bancos centrales y estadísticas públicas (`paneles.json`, 153 elementos); un registro de voces con nivel; un registro de predicciones con fecha límite; calendario de eventos; verificación con fuente; y todo versionado en git, de modo que cada cifra tiene historial.

**Lo que haría falta para que sea de verdad una terminal de inteligencia (OPINIÓN, por orden):**
1. **Cruces (§4):** sin ellos es un archivo, no una terminal.
2. **Medición (§5):** saber a quién creer es lo que la distingue de un lector de noticias.
3. **Avisos por cambio de estado,** no por noticia: «el evento ev-… venció», «la predicción p024 vence en 7 días», «el dato X contradice al panel Y». Todo sin IA.
4. **Seguridad e identidad por usuario** antes de cualquier familiar (§2-3).

**Qué NO merece la pena (OPINIÓN):** gráficos de mercado en tiempo real (TradingView ya los da gratis), una app nativa, un modelo propio de puntuación de «sentimiento», más paneles sin cruce, o un backend con base de datos antes de tener más de 5 usuarios.

**Monetización:** [ESPECULACIÓN] el valor está en el método (cruces + medición), no en los datos, que son públicos. Riesgos que hay que consultar **[VERIFICAR con asesor/CNMV]**: si el contenido llegara a encajar como «recomendación de inversión» (MAR y su reglamento delegado sobre presentación objetiva); la normativa de publicidad y *finfluencers*; el RGPD si hay usuarios; y la fiscalidad de cobrar. Mantener «sin recomendaciones» ayuda, pero no sustituye esa consulta. **No es consejo legal.**

## Limitaciones
- No se pudo cargar la app desplegada en el navegador integrado (se quedó cargando): no sé si `APP_CLAVE` está puesta en producción [VERIFICAR].
- La API pública de GitHub devolvió límite de peticiones: los minutos de Actions son una estimación (≥ 1 min por job) [VERIFICAR en Settings → Billing].
- No se leyeron enteros `app.py` ni `cerebro/apuntes_*.md`; solo los trozos citados.
- No se ejecutó ningún workflow ni se llamó a la API de Anthropic.

Fuentes externas (consultadas el 3-nov-2026): [GitHub Docs, visibilidad de Pages](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site) · [Cloudflare Access, precios](https://www.cloudflare.com/en-au/products/cloudflare-access) · [Streamlit, autenticación](https://docs.streamlit.io/develop/concepts/connections/authentication) · [Streamlit, `st.login`](https://docs.streamlit.io/develop/api-reference/user/st.login).
