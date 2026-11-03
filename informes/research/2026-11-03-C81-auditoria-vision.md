# C81 · Auditoría de visión: terminal de inteligencia personal + cerebro de seguimiento (3-nov-2026)

## 0. Estado actual de la terminal (comprobado en ejecución, 3-nov-2026, 22:07-22:20)

**Arranque:** `streamlit run app.py` (puerto 8793, vía `.claude/launch.json`) **arranca sin errores**: 0 líneas de error en el log del servidor y 0 errores en la consola del navegador. Sin el secreto `SHEET_ID` en local no aparece la sección Cartera: el menú muestra solo **Cerebro · Seguimiento · Privado** (`app.py:492-498`). No se probó la Cartera ni «Privado» (necesitan datos privados). Luego se paró el servidor.

| Sección / pestaña (evidencia) | Qué lee | Estado hoy |
|---|---|---|
| **Cerebro › Explorador** (`explorador.py`): Resumen, Capas, Línea de tiempo, Calendario, Matriz país × tema, Noticias, Voces, Países, **España**, Paneles de datos (10 pestañas en pantalla) | `explorador/*.json` + `informes/` + `cerebro/` (solo lectura, sin IA) | Funciona; cabecera: «Datos reales: radar 2026-11-02 · Órbita 2026-10-27 · paneles 2026-11-03 18:45 UTC» |
| **Cerebro › Paneles de datos** (`paneles.py`) | `explorador/paneles.json` (153 elementos) + `paises/estabilidad/hitos_petroleo` | **Carga**. Renderizados y comprobados en el DOM: bonos por plazo, **hipotecas sobre viviendas (INE)**, **vivienda e hipotecas: precio, tipos y esfuerzo**, **precio de la vivienda España vs Europa (Eurostat `prc_hpi_q`)**, **Brasil (SGS/Focus)**. 0 `NaN`/`undefined` en el texto renderizado. Observación: el bloque de España en los paneles se ve (IPV 12,20 % interanual, 2T-2026), pero **Brasil SGS 25499 sigue [VERIFICAR]** (ya anotado en C82) |
| **Cerebro › Apuntes / Glosario / Datos / Mi cartera / Actualidad / Mapa / Dudas y chat / Dossiers / Consumo** (`cerebro.py:265-269`) | `cerebro/*.md`, `cerebro/documentos/*.md`, `cerebro/actualidad/*.md`, `informes/dossiers/*.md`, `informes/predicciones.md`, `informes/pdf` | Existen en el código; no se recorrieron una a una. «Dudas y chat» y Consumo usan la API de pago: no se ejecutaron |
| **Seguimiento** (`seguimiento.py`) | `research/tareas.csv` + Google Sheet publicada | Existe en el menú; no se abrió en esta prueba. `seguimiento.json` (generado 3-nov 21:06 UTC) cuenta 151 hechas y 33 pendientes tras añadir C86-C97 |
| **Privado** (`privado_vista.py`) | `privado/` (no se publica) | No abierta (privada) |

**Frescura de los datos** (fecha de lectura o modificación; hoy = 3-nov):
- **Al día (≤ 1 día):** `paneles.json` (3-nov 18:45 UTC), `precios_historico.json`, `valoracion.json`, `espana.json` (leído 2-nov), `noticias-archivo.json`, `data.json`/`seguimiento.json` (3-nov 21:06 UTC).
- **Con 2-5 días:** `elecciones.json` (30-oct), `paises.json`, `estabilidad.json` (leído 30-oct), `regulacion.json` (versión 25-oct, modificado 2-nov), `voces.json` (2-nov), `espana-presupuesto.json` (leído 30-oct), `calificaciones.json` (leído **22-oct**, modificado 2-nov: la fecha de lectura es de hace 12 días).
- **Viejos (> 7 días):** `reservas.json` (22-oct), `bancos-eba.json` (22-oct, sin fecha interna), `deuda-fmi.json` (21-oct), `liquidez-manual.json` (25-oct), `prueba-datos.json` (28-oct; es un fichero de prueba, no de producción).
- **Sin fecha interna** (no se puede saber su frescura sin mirar el mtime): `bonos-manual.json`, `espana-manual.json`, `estabilidad-manual.json`, `indicadores-manual.json`, `hitos_petroleo.json`, `bancos-eba.json`. Propuesta: añadir campo `leido` (entra en C93/C94).
- **Vacíos o sin conectar:** ningún JSON está vacío. Sin conectar: Cartera (falta `SHEET_ID` en local), Japón e-Stat (falta `appId`), CNMV/EUR-Lex/BOE (solo Chrome), Senado y congress.gov (bloqueadas).

**Investigación reciente que NO aparece (o aparece solo de forma indirecta) en la terminal:**
| Investigación | Dónde está | ¿Aparece? |
|---|---|---|
| `research/fuentes-nuevas/` A-K (11 archivos) | `research/fuentes-nuevas/` | Ahora **sí en el índice** (`scripts/indice_investigacion.py` ampliado por la sesión principal: 11 menciones en `indice-investigacion.md`); la terminal lo lee en Apuntes, pero solo como enlace/frase, no como pestaña ni dossier |
| `research/CATALOGO-FUENTES.md` (Fase 2) | `research/` | Una mención en el índice; sin vista propia |
| Informe C77 España (gasto, inmigración, DANA) | `informes/research/2026-11-03-C77-…md` | En el índice (1) |
| C78 (hecha según `tareas.csv`; su salida está en `research/fuentes-nuevas/`) y C79 (pendiente, necesita OK de descarga) | `research/fuentes-nuevas/` | C78 no tiene informe propio en `informes/research`; el índice no menciona C78 ni C79 por ID, solo los archivos A-K |
| `informes/research/` (más de 300 informes, 19 MB en `informes/`) | `informes/research` | **Solo vía índice y búsqueda**: la pestaña Dossiers lee únicamente `informes/dossiers/*.md` (`cerebro.py:20, 375, 398`), así que los de `informes/research` no tienen vista propia |
| `research/verificaciones/` (lotes 2-nov) | `research/verificaciones` | Solo si el índice los cita; sin vista |
| `informes/gemini/` (crudos) | `informes/gemini` | No |

Conclusión: la terminal **funciona y está bastante al día**; el hueco no es de datos sino de **navegación**: lo investigado en `informes/research`, `fuentes-nuevas` y `verificaciones` solo se encuentra por el índice, y varios JSON manuales no dicen su fecha.

## Resumen
- **Qué es cada app hoy.** *Cerebro de seguimiento* = PWA estática en `docs/movil/` (lee `data.json` y `seguimiento.json`, sin servidor). *Terminal de inteligencia personal* = `app.py` (Streamlit) con las secciones Cartera, Cerebro, Seguimiento y Privado; Cerebro, Seguimiento y Privado solo salen en el ordenador (existe `privado/`) o con el secreto `MOSTRAR_CEREBRO` (`app.py:481-496`). La app desplegada enseña solo la cartera.
- **Lo más sólido:** muchos datos vivos con API abierta, ids por país (`pais_id`) ya presentes en cuatro ficheros, bots de coste cero casi todos, 0 secretos en 728 commits (SECURITY_REPORT, 30-oct).
- **Lo más urgente antes de abrir a familia o terceros:** (1) el repo es público y contiene todo el research y la memoria operativa; (2) la contraseña de la terminal es opcional y la «huella» `?k=` en la URL equivale a una contraseña permanente; (3) el Worker de Cloudflare guarda un token de GitHub con permiso de lanzar workflows (si se filtra, puede lanzar bots que llaman a la API de pago); (4) no hay medición de aciertos: solo 14 de ~57 predicciones tienen resultado.
- **Cruces:** el modelo mínimo es un **registro de enlaces** (`pais_id` + `evento_id` + `activo` + `tesis_ref` privado) sobre archivos ya existentes, sin capa nueva.
- **Hoja de ruta:** 12 filas (C86-C97) al final, listas para `research/tareas.csv`.

Etiquetas: HECHO = visto en el repo hoy; [VERIFICAR] = no comprobado; [ESPECULACIÓN] = juicio mío. Sin recomendaciones de compra/venta.

## 1. Inventario real (qué dato llega a cada app)

| Dato | Fuente / productor | Frecuencia | Móvil (`docs/movil`) | Terminal (`app.py`) |
|---|---|---|---|---|
| Precios, índices, tipos de bancos centrales (BIS + primarias), liquidez, inflación, petróleo, bonos, España INE/hipotecas, Brasil SGS/Focus, vivienda Eurostat | `scripts/actualizar_paneles.py` → `explorador/paneles.json` (workflow `paneles.yml`, lanzado por el Worker 3 veces/día L-V) | diaria / mensual | Sí (`data.json`: `mercado`, `tipos`, `inflacion`, `bonos`…) | Sí (Cerebro > Explorador/Paneles) |
| Países, política, elecciones, estabilidad, calificaciones, regulación (8 temas) | `explorador/paises.json` (12), `elecciones.json` (15), `estabilidad.json` (12), `calificaciones.json` (7), `regulacion.json` | manual por research (W/T/C) | Sí (`paises`, `elecciones`, `regulacion`) | Sí |
| Voces y fuentes (62 voces) | `explorador/voces.json` | manual | Sí (`voces`) | Sí |
| Eventos / calendario | `eventos/calendario.toml`, `vinculos.json` (regla evento → rutina W) | diaria (`eventos.yml`) | Sí (`eventos`) | Sí |
| Informes (≈330 en `informes/`, 19 MB) | sesiones /research | diaria | Solo lista de recientes (`informes`, `investigacion`) | Búsqueda + índice (`cerebro/documentos/indice-investigacion.md`) |
| Apuntes del cerebro (`cerebro/`, 17 documentos + apuntes + actualidad) | bot `cerebro.yml` (API de pago) + manual | semanal | No | Sí (los lee `cerebro.py` y los bots de IA enteros) |
| Predicciones (`informes/predicciones.md`) | manual | al detectar | Sí (`predicciones` en seguimiento.json) | Sí (texto) |
| Catálogo de fuentes y accesos | `research/CATALOGO-FUENTES.md`, `MAPA-DE-FUENTES.md`, `ACCESOS-CHROME.md` | por fase | No | No |
| Fuentes nuevas Fase 1 | `research/fuentes-nuevas/A..K` (11 archivos) | puntual | No | **No** (hueco ya detectado) |
| Seguimiento de tareas | `research/tareas.csv` / Google Sheet | continua | Sí (`seguimiento.json`, fetch de la hoja) | Sí (sección Seguimiento) |
| On-chain XRPL/Stellar, escrow, EDGAR, Federal Register | `onchain.yml`, `escrow.yml`, `edgar.yml`, `federal-register.yml` | 30 min – diaria | Alertas por Telegram; panel parcial | Alertas; parcial |
| Cartera real (posiciones, transacciones) | Google Sheet publicada (`SHEET_ID` secreto) + `privado/` local | manual | **No** | Sí, solo local/desplegada con contraseña |
| Tesis y mapa de riesgos | `privado/` | manual | No (por diseño) | Sí, solo en local |

Workflows: 12 en `.github/workflows/`; 4 llaman a la API de Anthropic (`cerebro`, `noticias`, `revision`, `verificar`); el resto no cuesta nada.

## 2. Huecos entre lo investigado y lo mostrado

1. **`research/fuentes-nuevas/` (A-K) no está en el índice** del cerebro: el índice solo recorre `informes/`, `informes/research`, `informes/dossiers`, `informes/videos` (`scripts/indice_investigacion.py`, constante `CARPETAS`). Tampoco entran `research/verificaciones/`, `research/CATALOGO-FUENTES.md` ni `informes/gemini/`. Ya existe un cambio sin subir en ese script; revisar que lo cubra.
2. **Móvil sin cuerpo de informes:** solo lista de recientes; el detalle vive en el ordenador. Coherente con la decisión «PC = profundidad, móvil = seguimiento» (memoria), pero conviene que cada tarjeta del móvil enlace a su fuente primaria.
3. **El índice ve el *título + una frase***, no las cifras. Un dato nuevo (p. ej. escaños UK, Colombia/NZ) solo es consultable si alguien abre el informe.
4. **Rutas de datos duplicadas:** hay tres formatos de «índice» (`explorador/indice/*`, `eventos/vinculos.json`, `indice-investigacion.md`) que se generan por separado y no se cruzan.
5. **Tareas con IDs repetidos:** en `research/tareas.csv` el ID **C80 y C81 aparecen dos veces** (filas 207-208 y 214-215: tareas «Joel 3-nov» y las del plan C). Esto puede romper cualquier enlace o regeneración que use el ID como clave. Propuesta C97.
6. **Cero paridad para «lo privado»:** la tesis no aparece en móvil (bien) ni tiene referencias estables desde el repo público (ver §3).

## 3. Cruces que faltan (país ↔ evento ↔ activo ↔ tesis)

**Estado:** `pais_id` ya existe en `paises.json`, `elecciones.json`, `estabilidad.json`, `regulacion.json` (`jurisdicciones[].pais_id`) y `por-pais.json`. `eventos/vinculos.json` enlaza evento → rutina (no evento → país). `voces.json` enlaza con `tokens` y `capas` pero no con `pais_id` ni con `evento`. `predicciones.md` es texto libre sin ids.

**Modelo mínimo (sin capa nueva):** un solo fichero `explorador/enlaces.json`, autogenerado donde se pueda, con filas `{pais_id, evento_id, activo, voz_id, prediccion_n, informe, nivel}`:
- `pais_id`: el que ya existe (`eeuu`, `ue`, `br`…).
- `evento_id`: `AAAA-MM-DD-slug`, igual que `eventos/calendario.toml`.
- `activo`: `XRP`, `XLM`, `BTC`, `EUR`, `bono-10a-US`… (lista corta).
- `voz_id` (`v045`…) y `prediccion_n` (fila de `predicciones.md`).
- **La tesis NO entra.** Su enlace va en un fichero espejo en `privado/enlaces-tesis.json` con `{enlace_id → tesis_ref}`; el público no conoce la tesis, solo el id del enlace. Se consulta solo en local (`privado_vista.py`).
- Se muestra como un filtro/columna «relacionado» en las vistas existentes (Centro, Países, Voces), no como panel nuevo (coherente con «una sola página, sin capas nuevas»).
- Coste: poblar ≈ 12 países × ~5 eventos + 62 voces + ~57 predicciones; semiautomático con `pais_id` ya presente.

## 4. Medición (aciertos de fuentes, predicciones, hipótesis)

- **HECHO:** `informes/predicciones.md` tiene ~57 filas (60 líneas de tabla); 43 figuran «Sin resolver»; ~14 con algún resultado o matiz (acertó, falló, mal planteada). El borrador del 18-oct ya concluía que **con tan pocas resueltas no se puede puntuar a nadie con porcentajes**; criterio propio: ≥5-10 resueltas por fuente [ESPECULACIÓN].
- **Qué falta para puntuar:** (a) campo `fecha_limite` normalizada y `fuente_id` (`voz_id`) en cada fila; (b) un script que, cada día, marque las que vencen y las ponga en cola de comprobación (hoy W06 lo hace a mano); (c) criterio de «acertó/falló/parcial» escrito y fijo; (d) separar **hechos anunciados** (calendario) de **opiniones** (precio): solo las primeras son comprobables sin sesgo; (e) una línea por fuente: n.º de predicciones, n.º resueltas, resultado; **sin ranking ni porcentaje hasta n≥5-10** (nunca «cuenta anónima A acierta 0 %»).
- **Hipótesis de la tesis:** su medición es privada (`privado/contraste-tesis.json`). Falta una regla pública mínima: para cada hipótesis, un disparador comprobable con fecha. Se queda fuera del repo público.
- Acierto de **datos** (verificaciones): hay lotes (`research/verificaciones/2026-11-02-*`, `verificaciones-consolidado.md`); falta un contador agregado (verificadas / contradichas / siguen [VERIFICAR]) visible en el Seguimiento.

## 5. Calidad (contradicciones, cifras viejas, secundarias, [VERIFICAR])

- **[VERIFICAR] acumulados:** conteo por archivo en `cerebro/`: `apuntes_xrp_macro_fiscalidad_2026.md` 40, `catalizadores-xrp-xlm.md` 27, `archivo-de-precedentes.md` 12 y otros menores. Los antiguos deberían tener fecha de apertura para poder caducarlos.
- **Cifras con fecha:** `graphify-out/GRAPH_REPORT.md` es del 18-oct (stale respecto a `main`; `graphify update .` es sin coste). Los paneles ya llevan campo `leido`; los manuales (`*-manual.json`) dependen de `scripts/validar_manuales.py` y `auditoria_frescura_paises.py` (frescura en el Seguimiento).
- **Fuentes secundarias donde debería haber primaria:** el catálogo (CATALOGO-FUENTES) marca como **Bloqueada** `senate.gov`, `congress.gov`, `bls.gov`, `sec.gov` web, `pbc.gov.cn`, `rba.gov.au`, OCDE SDMX → se lee vía prensa [S]; el cloture 49-50 sigue [VERIFICAR]. Pendiente de Joel: `appId` de e-Stat y OK de 3 PDF.
- **Contradicciones:** W08 (2-nov) no halló contradicciones de cifras en lo muestreado; pero el muestreo no cubre `fuentes-nuevas/` ni los `*-manual.json` entre sí. Un lote C-nuevo (contradicciones automáticas entre paneles y manuales) es barato (sin IA).
- **Naturaleza del repo:** el Worker de Cloudflare apunta a `joeldragonball-jpg/requirements.txt` (`scripts/cloudflare-lanzador-bots.js:6`); es el nombre de repo que hay, pero es un nombre que invita a error: [VERIFICAR] que es intencionado.

## 6. Seguridad y salida a producción

**Estado actual (HECHO):** 0 vulnerabilidades en 79 paquetes, 0 secretos en 728 commits, 0 verificaciones TLS desactivadas (SECURITY_REPORT, 22-30 oct). `.gitignore` protege `.env`, `privado/`, `secrets.toml`.

**Lista de 20 puntos de Joel aplicada a lo que hay**

| Punto | Estado hoy | Riesgo |
|---|---|---|
| 1-2 secretos y frontend | Cumple en el repo. El `SHEET_ID` va en secretos de Streamlit. El móvil no lleva claves. | Bajo |
| 3-4,11,14,15 (BD, roles, propiedad, lista blanca) | N/A: no hay BD ni usuarios | Aparece al abrir a terceros |
| 5 rate limiting | Solo `time.sleep(1)` tras fallo en la contraseña (`app.py:~397`); sin límite global | **Medio-alto** si se abre |
| 7-8 validar entradas / no HTML | `st.markdown(..., unsafe_allow_html=True)` extendido; datos externos (RSS, voces) llegan a plantillas HTML del móvil: [VERIFICAR] que todo pasa por `esc()` (el móvil usa `esc`, `mdHTML`) | Medio (XSS por datos externos) |
| 9,19 contraseñas | Comparación `hmac.compare_digest`, no hay hash/bcrypt (una sola clave compartida) | Medio |
| 10 tokens/cookies | **No cumple:** la huella `?k=` va en la URL (favoritos, historial, referer); no es cookie httpOnly | **Alto** al compartir |
| 12 CORS | N/A (estático) | Bajo |
| 13 email, 16 webhooks | N/A hoy | — |
| 17 errores genéricos | Streamlit enseña errores si fallan los secretos (`app.py:551`) | Bajo |
| 18 dependencias | Revisadas en el informe de seguridad; sin workflow que avise de nuevas CVE salvo `seguridad_rapida.py` manual | Medio |

**Riesgos concretos**
1. **Repo público = todo es público:** informes, `eventos/`, memoria de workflows, metodología y los nombres de secretos. Para la familia no es un problema de secreto, sí de **privacidad y de valor** (cualquiera copia el trabajo). Para monetizar, el diseño actual regala el producto.
2. **Candado opcional:** si `APP_CLAVE` no existe, la app queda abierta (docstring de `candado()`). Una despliegue sin secreto expone cartera real. Cambiar a «cerrado por defecto» es un cambio de una línea [propuesta C89].
3. **Bots con API de pago:** `cerebro`, `noticias`, `revision`, `verificar` pueden lanzarse con `workflow_dispatch`. Quien consiga el token de GitHub del Worker (secreto `GITHUB_TOKEN` en Cloudflare) puede lanzarlos en bucle. Mitigación: token de **alcance mínimo y por repo (fine-grained, solo Actions)**, límites de gasto en la cuenta de Anthropic y un tope diario dentro de `noticias/config.toml` (ya hay topes).
4. **Caídas/DoS:** el móvil es estático (GitHub Pages) → muy resistente; el riesgo está en la terminal (Streamlit Community Cloud: duerme, sin SLA) y en el Worker (cuota del plan gratuito). Para uso familiar basta; para terceros hace falta hosting con SLA.
5. **Fuga de datos de cartera:** la hoja Google «publicada en la web» es pública para quien tenga el enlace; el `SHEET_ID` solo es secreto de oscuridad. Alternativa: hoja privada con cuenta de servicio.
6. **Cadena de suministro:** dependencias sin fijar por hash; Actions por versión de etiqueta. Fijar por SHA es barato.

**App vs web (PWA)**

| | App nativa | Web/PWA (hoy) |
|---|---|---|
| Distribución | Tiendas (revisión, coste, cuentas) | URL, sin intermediarios |
| Actualizaciones | Con revisión | Instantáneas |
| Seguridad | Sandboxing; almacén local seguro | Depende de la cabecera/HTTPS y de tu servidor |
| iOS/Android | Dos bases de código o framework | Una; ya usada (`viewport-fit`, memoria iOS) |
| Offline | Mejor | Service worker (ya hay `sw.js`) |
| Monetización | Tienda cobra comisión | Pagos propios (más trabajo fiscal) |
| Para familia | Sobredimensionada | **Suficiente y ya funcionando** |

**Recomendación de arquitectura [ESPECULACIÓN, mío]:** quedarse en PWA; para familia, cuenta privada de GitHub + Pages privado/ Cloudflare Access (login por email) sin tocar la lógica. Solo plantear nativa si se necesitaran notificaciones push fiables en iOS o almacenamiento cifrado.

**Si se monetiza:** difundir información financiera a terceros puede tener implicaciones regulatorias (CNMV/ESMA, MiFID II sobre «recomendaciones de inversión», protección de datos RGPD, IVA/autónomos, avisos legales). **[VERIFICAR con asesor / CNMV]**; no es consejo legal. Mantener «sin recomendaciones» ayuda a la separación pero no sustituye la consulta.

## 7. Hoja de ruta (valor / coste / riesgo)

Orden sugerido: seguridad barata primero, luego cruces y medición.

| ID | Qué | Valor | Coste | Riesgo | Prompt (resumen) |
|---|---|---|---|---|---|
| C86 | Indexar `research/fuentes-nuevas`, `verificaciones` y `CATALOGO-FUENTES` en el cerebro del escritorio | Alto | Bajo (S, sin IA) | Bajo | «Amplía `CARPETAS` de `scripts/indice_investigacion.py` o añade un índice paralelo; regenera; comprueba que salen A-K y el catálogo; sin tocar `cerebro/` existente.» |
| C87 | Separar público/privado: auditoría de qué hay en el repo público y plan de repo privado + Pages privado/Cloudflare Access | Alto | Medio | Medio | «Lista lo que no debería ser público (memoria operativa, rutas, nombres de secretos); diseña migración a repo privado manteniendo Pages; sin ejecutarla.» |
| C88 | Endurecer el Worker: token fine-grained, límite de lanzamientos, tope de gasto, rotación | Alto | Bajo | Bajo | «Revisa `cloudflare-lanzador-bots.js` y los workflows de pago; propón permisos mínimos y topes; Joel ejecuta los cambios en Cloudflare/GitHub.» |
| C89 | Endurecer `candado()`: cerrado por defecto, sustituir `?k=` por cookie/sesión, límite de intentos | Alto | Bajo | Bajo | «Cambios mínimos en `app.py:candado` (leer solo ese trozo); tests locales; sin subir.» |
| C90 | Revisión XSS: dónde se inyecta texto externo como HTML en `docs/movil/index.html` y `app.py` | Medio | Bajo | Medio | «Grep de `innerHTML`, `unsafe_allow_html`; lista de rutas con datos externos y su escape; casos de prueba.» |
| C91 | Modelo de enlaces `enlaces.json` (+ espejo privado) y filtro «relacionado» | Alto | Medio | Bajo | «Genera enlaces iniciales desde `pais_id`, `calendario.toml`, `voces.json`, `predicciones.md`; sin capa nueva; tesis solo en `privado/`.» |
| C92 | Medición: normalizar `predicciones.md` (fecha límite, fuente_id), script de vencimientos y tabla por fuente sin porcentajes hasta n≥5 | Alto | Medio | Bajo | «Convierte el registro a CSV/JSON conservando el MD; script diario de vencimientos; contador agregado en el Seguimiento.» |
| C93 | Caducidad de [VERIFICAR]: fechar cada uno y cola de revisión | Medio | Medio | Bajo | «Extrae los [VERIFICAR] de `cerebro/`; añade fecha de apertura y prioridad; propón cuáles caducan.» |
| C94 | Regeneración de graphify y contradicciones automáticas paneles ↔ manuales | Medio | Bajo (sin IA) | Bajo | «`graphify update .`; script que compare cifras repetidas entre `paneles.json` y `*-manual.json`.» |
| C95 | Plan de salida a producción para familia: auth, hosting, copias, dominio, avisos legales | Medio | Medio | Medio | «Compara Cloudflare Access / Streamlit privado / repo privado; coste mensual; plan de recuperación.» |
| C96 | Consulta regulatoria de monetización [VERIFICAR con asesor/CNMV] | Medio | Bajo (Joel) | Alto si se ignora | «Lista de preguntas para asesor: MiFID II, aviso legal, RGPD, IVA; no es consejo legal.» |
| C97 | Reparar IDs duplicados de `tareas.csv` (C80 y C81 repetidos) | Medio | Bajo | Bajo | «Renumera las filas «Joel 3-nov» duplicadas sin romper enlaces del Seguimiento; revisar `construir_seguimiento.py`.» |

## Limitaciones
No leí `app.py` ni `apuntes_*.md` enteros; el recuento de [VERIFICAR] y predicciones es aproximado. No se probó el Worker ni los workflows (sin ejecutar nada ni llamar a la API). Qué hace la hoja de Google publicada y la configuración de Streamlit Cloud/Cloudflare no son visibles desde el repo: [VERIFICAR].
