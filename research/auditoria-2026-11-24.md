# Auditoría independiente · 24-nov-2026 · Fondos y bolsa → ETF cripto

Alcance: contenido nuevo del 22 al 24-nov (C368-C378). Auditoría de **solo lectura**: no se ha tocado código ni datos, ni se ha llamado a la API. Comprobaciones hechas con Python local sobre los mismos archivos que lee el tablero (`explorador.py` → `D.*`).

Leyenda: 🔴 error o riesgo · 🟡 mejora · 🟢 bien

---

## (a) Hallazgos por gravedad

### 🔴 1. `research/tareas.csv`: 9 filas se leen con las columnas desplazadas (estado basura)
- **Dónde:** `research/tareas.csv:499-509` (C368, C369, C370, C371, C374, C375, C376, C377, C378) y una línea en blanco en `:498`.
- **Qué pasa:** el campo `tema` lleva comas y no va entre comillas. `csv.reader` devuelve de 15 a 20 columnas en vez de 14; `tareas_csv.cargar()` (DictReader) asigna a `estado` trozos del tema: «confianza y qué lo confirmaría)», «13f», «nasdaq-100», «creativeone», «jane street +4 %»…
- **Consecuencias comprobadas:** `docs/movil/seguimiento.json` ya lleva esos estados basura (p. ej. C376 `"estado": "creativeone"`); el PLANNING dice «Hechas en 7 días (2): C355, C360» cuando en realidad se cerraron unas 11 tareas (C367-C378). El arreglo anterior (C374 pegada a C373) resolvió el salto de línea pero no las comas.
- **Además:** no existe la fila **C379** (hay commit `f61c1a8 C379…`, pero no está en el CSV, en el PLANNING ni en el seguimiento).
- **Arreglo:** reescribir esas 9 filas con `csv.writer` (QUOTE_MINIMAL) usando `tareas_csv.escribir()` en lugar de pegarlas a mano; borrar la línea en blanco; añadir C379. Y una salvaguarda en `tareas_csv.cargar()`: si `len(fila) != len(cabecera)` o `estado` no está en `ESTADOS`, avisar y parar (ya existe esa validación en `sincronizar()`, línea ~79, pero no en `cargar()`). Después regenerar `construir_movil.py` y `construir_seguimiento.py`.

### 🔴 2. Misma pestaña, dos cifras distintas del 13F para los mismos fondos
- **Dónde:** `xrpTotales()` (`explorador/vistas.html:2342-2369`) lee `explorador/etf-13f.json`; `etf13f()` (`:2594-2627`) lee `explorador/etf-flujos.json › 13f_3T`. Las dos tablas salen en Fondos y bolsa.
- **Diferencias comprobadas (3T, miles de $ / declarantes):**

| Fondo | etf-13f.json | etf-flujos.json |
|---|---|---|
| XRP | 139.784 | 139.730 |
| XRPC | 69.654 · 46 decl. | 66.625 · 45 decl. |
| XRPI | 13.978 · 44 decl. (2T: 41) | 13.617 · 42 decl. (2T: 39) |
| XRPR | 2T: 28 decl. · 5.096 | 2T: 27 decl. · 5.095 |

- Probablemente son dos lecturas de 13f.info en días distintos (siguen llegando 13F tardíos). Para Joel se ve como una contradicción.
- **Arreglo:** una sola fuente para los totales por fondo (la más reciente, `etf-13f.json`, leída el 21-nov), y que `etf13f()` tome de ahí declarantes y valores; o al menos una nota visible: «dos lecturas de 13f.info (fecha A y fecha B); la diferencia son 13F presentados tarde». Ojo: `pr3()` (`:2618`) calcula el precio del 3T con `etf-flujos.json`; si se unifica, el «Cambio 2T→3T» de las gestoras cambia muy poco (XRPC/XRPI), pero conviene volver a comprobar Goldman.

### 🔴 3. Flujo diario de SoSoValue: el 28 % de los días son «0» y los KPI de 5 días / 4 semanas pueden ser falsos
- **Dónde:** `explorador/etf-flujos-diarios.csv` (256 filas) y los KPI de `etfFlujoDiario()` (`vistas.html:2454-2456`).
- **Comprobado:** 72 de 256 días tienen flujo 0. En las últimas 4 semanas hay 10 ceros (23, 27 y 28-oct; 3, 4, 5, 6, 11, 12, 16, 18 y 19-nov) y los activos netos se quedan clavados en 1.080 M$ del 16 al 19-nov aunque el precio de XRP se mueve (0,95-0,98 $). Son días **sin actualizar**, no días sin flujo. El KPI «últimas 4 semanas: −26,5 M$» y «últimos 5 días: −11,1 M$» se presentan como hechos.
- La nota de la línea 2478 ya avisa («días sin actualizar, que salen a 0»), pero el KPI no.
- **Arreglo:** marcar como «sin dato» (no 0) los días con flujo 0 **y** activos iguales al día anterior; en los KPI, decir «N días sin dato en el periodo» o no mostrar el KPI si faltan más de 2 días; y una nueva lectura de SoSoValue de esos días [VERIFICAR].
- **Otros dos puntos del CSV [VERIFICAR]:** (1) el 11-dic-2025 los activos pasan de 939 a 1.170 M$ con un flujo de solo +16 M$ (el precio no lo explica: ¿se añadió un fondo al panel?); (2) la primera fila (13-nov-2025) tiene flujo 0 y la entrada de 243 M$ sale el 14-nov: puede haber un día de desfase en el estreno de XRPC. Comprobar con Canary/SoSoValue.

### 🟡 4. Textos fijos que ya no coinciden con lo calculado
- `vistas.html:2479`: «tres cifras distintas (≈ 980, ≈ 1.030 y ≈ 1.110 M XRP)». Con los datos de hoy, (1) sale **980,9** ✓, pero (2) «lo que tienen los fondos» sale **1.088** (989,61 M$ ÷ 0,9097 $), no 1.030. **Arreglo:** construir la frase con `last.cum`, `last.tok` y el `tM` de `etfPrecioMonedas()`.
- `:2476`: «997,7 M XRP» del vídeo y la lista «los cinco fondos (XRP, XRPZ, XRPC, TOXR, GXRP)» están fijos; la lista debería leerse de `#fuente=` del CSV.
- `:2431-2432` (comentario): dice «entre puntos se mantiene el último valor conocido», pero `interp()` (`:2500`) interpola en línea recta (y el texto de `:2553` lo dice bien). Solo es un comentario, pero confunde al revisar.
- `:2429` (lectura de `etfPrecioAcc`): frases fijas («entradas puntuales (XRPZ)», «rescates netos en GXRP») que pueden dejar de ser ciertas con la próxima lectura; mejor generarlas desde `sube`/`baja`, que ya se calculan en `:2426`.

### 🟡 5. Niveles de las fichas de gestoras (`explorador/gestoras-13f.json`)
- Las 10 fichas nuevas (Kovack, CreativeOne, Beacon Pointe, Kaleidoscope, IMC-Chicago, Teucrium, Tactive, Inscription, Realta, Mustico, Windle; en realidad son 11 sin CIK contando Virtu) tienen un hecho de nivel **P**: «Figura entre los principales tenedores… (etf-13f.json)». Pero `etf-13f.json` es 13f.info, nivel **S**, y el enlace es una búsqueda de EDGAR por nombre, no el 13F-HR leído. **Arreglo:** bajarlos a `S` hasta leer el 13F-HR (y entonces poner el CIK).
- Goldman, hecho del 19-nov («grupo de DTCC y asesora a Bullish»): `f: null` y nivel S sin [VERIFICAR]. Jane Street y Citadel tienen otro hecho sin fuente cada uno. **Arreglo:** añadir fuente o `S [VERIFICAR]`; y en `gestoraAbrir()` (`:2328`) poner «[sin fuente]» cuando `x.f` falta.
- `gestoraAbrir()` (`:2328`) convierte cualquier nivel que no empiece por P en «S»: un futuro `RAZONADO` o `ESPECULACIÓN` se mostraría como S. **Arreglo:** `nivelBadge(String(x.n).split(' ')[0])`.
- Faltan fichas de tenedores grandes que aparecen en las tablas: Morgan Stanley, BlackRock, JPMorgan, Wells Fargo, Bank of America, Citigroup, Cantor Fitzgerald, Brevan Howard, DRW, Mubadala (26 nombres sin ficha en total). No es un error: hoy salen como texto sin enlace.
- Lo bueno: la contradicción de la prensa sobre la salida de Goldman en el 1T está marcada «S [VERIFICAR]» y explicada.

### 🟡 6. Divisiones sin protección en el motor de cambios
- `xrpTotales()` `:2349` `cambio((t3/t2-1)*100)` y `:2353` `cambio((r.v3/r.v2-1)*100)`: si `v2` es 0 o falta (un fondo nuevo que no cotizaba en el 2T, p. ej. una futura serie), sale `▲ +∞ %` (`cambio()` en `:505` filtra NaN, pero no Infinity). Además `nvc(r.v2/1000)` con `v2=null` muestra «0», no «vacío». **Arreglo:** `r.v2?cambio(...):'nuevo'` y `r.v2==null?'vacío':nvc(r.v2/1000,1)`; en `cambio()`, `if(!isFinite(v))return el('span','igual','—')`.
- `etfPrecioMonedas()` `:2514` y `seg()` `:2544`: el «Cambio vs 30-sep» del TOTAL suma la última cifra de **todos** los fondos y compara con el 30-sep solo de los que tienen ese punto (`r.b?…:0`). Si falta el 30-sep de un fondo, el cambio total sale inflado. Hoy no ocurre (los 5 fondos tienen 30-sep en la serie usada), pero es frágil. **Arreglo:** usar en el TOTAL solo los fondos que tienen las dos fechas y decirlo.
- `etfFlujoDiario()` `:2449`: si el precio fuera plano en el tramo (`pMax==pMin`), `stepN(0)` da NaN y el eje sale vacío. Caso raro; basta con `Math.max(ε, …)`.

### 🟡 7. Motor `tabla()` con unidad en cada celda (`vistas.html:520-535`)
- Funciona con todos los títulos actuales (comprobado: ninguno usa «(algo, M$)»). Dos riesgos latentes:
  1. `:529`: si `c.f` devuelve un **DocumentFragment** (como `dlt()`), se mide `v.textContent` **después** de `td.append(v)`, cuando el fragmento ya está vacío → nunca añade la unidad. Si devuelve un **nodo de texto** numérico, `v.append(...)` lanza error (los nodos Text no tienen `append`) y se rompe la tabla entera. **Arreglo:** leer el texto antes del `append` y añadir la unidad con `td.append(' '+unidad)`.
  2. `:524`: la expresión `(?:[^()]*, )?` borra también lo que vaya antes de la coma («Valor (3T, M$)» → «Valor», se pierde «3T»). **Arreglo:** dejar en la cabecera lo de antes de la coma: `replace(UM, (m)=>…)`.
- La cifra con signo menos tipográfico (−) no recibiría unidad; hoy `num()` usa el guion normal, así que no pasa.

### 🟡 8. Pantalla estrecha
- `.t13c{overflow:visible}` (`vistas.html:385`): en el móvil (375 px) las tablas de `xrpTotales()` (6-7 columnas con números `nowrap`) y la tabla de gestoras de `etf13f()` para `<1300 px` (con «Reparto por fondo») desbordan la página y crean desplazamiento horizontal de toda la vista. En tablet (C377) va bien. Como la Órbita es para PC y el móvil va aparte, es prioridad baja; arreglo barato: `@media(max-width:600px){.t13c{overflow-x:auto}}`.
- `window.innerWidth<1000` / `<1300` (`:2353`, `:2359`, `:2624`) se evalúan una sola vez: al girar la tablet no se reajusta hasta recargar.
- `etfFlujoDiario()` en móvil: viewBox de 440 px con letra 11 → unos 8,5 px reales; la etiqueta del eje derecho «1000 M XRP» (≈ 60 px) no cabe en `R=56` y se corta. **Arreglo:** en móvil, eje derecho solo con el número y la unidad en la leyenda.
- `ResizeObserver` (`:2475`) nunca se desconecta; al volver a pintar la vista quedan observadores huérfanos (fuga pequeña).
- `num()` con `es-ES` no agrupa números de 4 cifras: los KPI dicen «1778 M$» y el eje «1000 M XRP», mientras los textos dicen «1.030». Usar `miles(num(...))` como en el resto.

### 🟡 9. Enlaces sin validar el esquema
- `lkx()` (`vistas.html:2244`) pone `a.href=u` sin comprobar que empiece por `https://`. Hoy todas las URL de `gestoras-13f.json` son https (comprobado), pero los bots escriben en el repo y el repo es público. **Arreglo:** `if(!/^https?:\/\//.test(u))return el('span',null,t)`.

### 🟢 Lo que está bien
- **Flujo acumulado en XRP equivalentes:** recalculado con `precios_historico.json` → **980,9 M XRP** a 20-nov y **992,6 M XRP** a 13-nov (el vídeo: 997,7). Cuadra con el rango 981-993 esperado. Entradas netas acumuladas: 1.778 M$.
- **13F 2T→3T a precio constante (EDGAR):** Goldman 145,34 frente a 124,42 M$ → **+16,8 % ≈ +17 %** ✓; Jane Street +4,0 %, Susquehanna +1.552 %, Marex +27,3 %, Millennium +0,1 %, Intesa +32,7 %: coinciden con C378. Los 6 CIK del 2T están en `lecturas_edgar` y ningún ticker del 2T queda sin precio del 3T.
- La suma de Goldman en su ficha (38,4+47,8+33,3+14,5+10,1+1,3 = 145,4 M$) cuadra con EDGAR.
- **XSS:** en el tramo `vistas.html:2300-2660` no hay `innerHTML`; `el()` usa `textContent` y los SVG usan `textContent` en `sv()`. Bien.
- **CSV de flujos:** sin fines de semana, sin fechas repetidas y ordenado; `explorador.py` lo lee con cabecera `#clave=valor`.
- Las aclaraciones de método están: «2T a precio 3T» para separar compra de precio, «declarantes ≠ gestoras únicas», «13F no dice motivo ni fecha», «emisor = parte interesada», «correlación no es causa», caso alcista y bajista en `etfPrecioAcc`. Sin recomendaciones de compra o venta.
- `gestoraDe()`: los 23 alias están en minúsculas y no chocan entre sí; todos los nombres de 13f.info y EDGAR de las fichas encajan.

---

## (b) Seguimiento y organización

- **El seguimiento no es fiable ahora mismo** por el 🔴 1: 9 tareas recién hechas aparecen con estados basura en el móvil y el PC, y «Hechas en 7 días» dice 2 cuando son unas 11. Es el arreglo más urgente y barato (≈ 10 min).
- **Estados poco uniformes:** además de `hecha` (340) hay `hecho` (12), `hecho 2026-11-15` (3), `hecho 2026-10-30`, `hecho 2026-10-31`. Conviene unificar en `hecha` y poner la fecha en `cuando`.
- **¿Inflado?** Sí, algo: **57 parciales** + 30 pendientes + 11 vigiladas, y el PLANNING muestra 49 parciales. Muchas parciales llevan semanas con el «falta» sin cambios (C30, C39, C42, C58…). Según la norma de no inflar el planning: antes de crear filas nuevas, cerrar o archivar las parciales cuyo «falta» depende de algo bloqueado (Chrome, PDF, OK de Joel) y pasar a `vigilada` las que solo esperan una fecha.
- **Duplicidades en ETF:** C210 (pendiente, «capas nuevas: flujos de ETF de XRP/XLM…») ya está cubierta en buena parte por C373-C378; C280 (parcial) se solapa con C375/C376. Propuesta: cerrar C210 como `cubierta` y dejar C280 solo con lo que falta (EZBC, FBTC, XRPZ…).
- Las filas recientes son largas y mezclan qué se hizo con qué falta en el `tema`; eso es lo que mete las comas. Regla práctica: `tema` corto (≤ 90 caracteres, sin comas) y el detalle en `detalle`/`falta`.

---

## (c) Las 5 tareas siguientes con más valor

1. **Arreglar `tareas.csv`** (comillas en C368-C378, línea en blanco, añadir C379) y poner la validación de ancho y estado en `tareas_csv.cargar()`; regenerar móvil y planning. *Sonnet S · ~0,5 %.*
2. **Una sola fuente para los totales del 13F** (etf-13f.json frente a etf-flujos.json) y nota visible de fecha de lectura; volver a comprobar el «Cambio 2T→3T». *Sonnet S · ~1 %.*
3. **Días sin dato en el flujo diario:** distinguir 0 real de «sin actualizar», reflejarlo en KPI y gráfico, y nueva lectura de SoSoValue de oct-nov ([VERIFICAR] 11-dic-2025 y 13/14-nov-2025). *Sonnet S · ~1 %.*
4. **Textos generados desde datos** (las «tres cifras» de `:2479`, lista de fondos de `:2476`, lectura de `:2429`) y protección de `cambio()`/`tabla()` frente a Infinity, fragmentos y esquemas de URL. *Sonnet S · ~1 %.*
5. **Fichas y niveles de gestoras:** bajar a S los hechos de las 10 fichas nuevas, buscar su CIK y leer su 13F-HR (pasa a P), fuentes de los 3 hechos sin enlace, y fichas de los grandes que faltan (Morgan Stanley, BlackRock, JPMorgan, Wells Fargo, Mubadala). Opcional en el mismo bloque: cargar el 13F del 4T-2025 y del 1T-2026 de las 6 gestoras con lectura en EDGAR. *Sonnet M · ~3 %.*

*Auditoría hecha el 24-nov-2026 con datos leídos del repo local (`main`, último commit fde6eda). Cifras recalculadas con Python; no se han consultado fuentes externas.*
