# Valoración de capas y calendario de research continuo (C185 y C188, 8-nov-2026)

> **Cómo leer este archivo (añadido el 8-nov tras revisarlo con Joel).** Contiene tres pasadas, de la más antigua a la más reciente: (A) apartados 1-5, valoración de utilidad y calendario de research; (B) segunda pasada con el móvil primero (hallazgos y propuestas 1-22 = C189-C210); (C) tercera pasada con la **Órbita primero** (apartados 7-10 = C211-C223), que es la que manda para escritorio y tablet. **Si dos propuestas se solapan, vale la de la Órbita.** Solapes ya resueltos en `research/tareas.csv` (la antigua queda «cubierta por» la nueva): C202→C215, C200→C220, C204→C221, C207→C217, C192→C214, C199→C222, C187→C197. El móvil es solo una versión simplificada de seguimiento: sus propuestas se hacen al final.
> **Orden de ejecución recomendado (OPINIÓN):** C211, C212, C214, C215, C216 (usabilidad y confianza de la Órbita); después C213, C219, C220, C221; las grandes (C217 comparador de países, C205 tesis, C206 alertas, C222 Mercado, C223 rendimiento, C210 capas nuevas) las decide Joel.

Parte de `INVENTARIO-CAPAS.md`, `PLAN-ACTUALIZACION-DATOS.md` y `MAPA-DE-FUENTES.md` (no los rehace). Nada de esto es recomendación de compra ni venta: solo utilidad de la información para que Joel decida. Etiquetas: **HECHO** = está en los tres archivos de entrada; **OPINIÓN** = criterio mío, discutible; [ESPECULACIÓN] / [VERIFICAR] como siempre. Costes de cuota = [ESPECULACIÓN] (orden de magnitud, % de la cuota semanal; no medidos).

## 1. Hechos de partida
- 17 conjuntos de datos, todos dentro de la cadencia propuesta el 8-nov (HECHO, inventario).
- Mercado: 45 filas, 43 diarias; casi todo de Yahoo Finance, divisas del BCE; sin segunda comprobación (HECHO).
- Macro y liquidez dependen de `explorador/*-manual.json` (7 ficheros: bonos, españa, estabilidad, indicadores, liquidez, rwa-por-cadena, tipos) (HECHO).
- Cadencias de datos oficiales ya fijadas el 3-nov en el plan de actualización (HECHO); la tabla del inventario las deja como [propuesta].

## 2. Valoración de utilidad por capa (OPINIÓN, horizonte largo plazo)
Escala: **Alta** = cambia la conclusión de una tesis; **Media** = contexto útil; **Baja** = ruido salvo evento.

| Capa | Qué aporta a decidir | Utilidad | Qué sobra / qué falta |
|---|---|---|---|
| Cripto/regulación (CBDC, RWA por cadena) | Es el entorno directo de XRP/XLM: regulación por país, rivales (RWA en otras cadenas), CBDC como competidor o puente | **Alta** | Falta fecha/fuente por cada cifra RWA (manual, fuente única). Sobra detalle de CBDC en fase piloto sin cambios trimestrales |
| Mandatos (regulación) | Hitos reglamentarios con fecha (MiCA, GENIUS, etc.): son los disparadores reales de la tesis | **Alta** | Falta calendario de fechas límite de aplicación enlazado con cada mandato |
| Macro: indicadores + historia | Ciclo, inflación, tipos: marco de riesgo, no de entrada/salida | **Media-Alta** | Manual → riesgo de quedarse viejo. Sobra duplicar «historia» e «indicadores» si dicen lo mismo [VERIFICAR] |
| Macro: liquidez | M2/balances: contexto de largo plazo para activos de riesgo; correlación con cripto no estable [ESPECULACIÓN] | **Media** | Semanal es más de lo que aporta; mensual basta salvo cambio de balance de banco central |
| Mercado (cotizaciones, 6 grupos) | Referencia de precio, divisas, energía, metales, bolsas. Para largo plazo, el valor está en tendencia y correlaciones, no en el dato diario | **Media** (diario = ruido; semanal/mensual = señal) | Sobra «diaria» como cadencia de **lectura**; la recogida diaria es barata y conviene dejarla. Falta segunda fuente y marcar «dato retrasado» |
| Tipos de interés (tabla bancos centrales) | Coste del dinero, base de casi todo; útil con fuente primaria | **Alta** | Faltan RBA, RBNZ, Riksbank, Norges, CO, CL, PE (plan 3-nov). Ficha de Canadá aún a 2,25 % (oficial 2,50 %) |
| Riesgo país (calificaciones, deuda FMI, reservas, estabilidad) | Solvencia y dependencia de divisa; ayuda a juzgar CBDC/regulación por país | **Media** | Cadencia lenta: bien. Sobran reservas mensuales (FMI COFER es trimestral); falta fecha de revisión por agencia |
| Países/política y elecciones | Cambios de régimen regulatorio; relevante solo cuando hay elección o cambio de gobierno | **Media** | Mantener, pero ligado al calendario electoral, no a barrido periódico |
| España (INE, presupuesto IGAE/PGE) | Contexto personal (fiscalidad, vivienda, ahorro del inversor residente) | **Media-Alta** para decisiones propias | Falta IPC/PIB/paro como serie viva (códigos nuevos del plan 3-nov). Presupuesto: anual/trimestral basta |
| Valoración sectorial | Múltiplos como contexto de ciclo; poco accionable sin comparar con histórico propio | **Media-Baja** | Mensual basta; riesgo de falsa precisión [OPINIÓN] |
| Noticias (bot RSS+IA) | Detecta eventos; ya decidido mantener con IA (memoria 8-nov) | **Media** | No se toca en esta tarea |

Resumen OPINIÓN: lo que más pesa para decidir (cripto/regulación, mandatos, tipos) es también lo que hoy tiene más fuente única o manual. Lo que sobra no son capas enteras sino **cadencias demasiado rápidas** (liquidez semanal, mercado diario como lectura).

## 3. Calendario de research continuo (C188)
Disparador = calendario oficial (HECHO: regla del plan 3-nov). Coste en % de cuota semanal [ESPECULACIÓN] si se hace con agente; "0" = script sin IA.

| Qué se actualiza | Disparador | Fuente primaria | Segunda fuente (a añadir) | Coste |
|---|---|---|---|---|
| Cotizaciones del Mercado | Cada día hábil (script) | Yahoo Finance | Energía: EIA (ya hay `_spot_eia`, con ~3 d de retraso); divisas: BCE (ya); bolsas/ETF/metales: Stooq o FRED/CSV [VERIFICAR acceso]; cripto: otra API abierta [VERIFICAR] | 0 |
| Curvas de bonos EE. UU. | Diario (script) | Tesoro XML (✅) | FRED `fredgraph.csv` | 0 |
| Tipos de bancos centrales | Día de decisión y siguiente (fechas del apartado 3 del plan) | Fuente primaria de Fed, BCE, BoE, BoC, Brasil; BIS de respaldo | BIS cruzado contra primaria: alerta si difieren >1 día | 0 script; ~0,3 % por ronda manual (RBA, RBNZ) |
| España: IPC, paro/afiliación, hipotecas, deuda PDE, PIB | Fechas INE/Banco de España (IPC 13-nov, hipotecas 25-nov, PIB 23-dic…) | INE `wstempus` | Eurostat `prc_hicp_minr` (no la `manr`, congelada) | 0 una vez automatizado |
| EE. UU.: empleo, IPC, PCE | 6-nov, 10-nov, 25-nov… | `api.bls.gov` / FRED | FRED vs BLS | 0 |
| Indicadores macro (manual) | Tras cada publicación | Oficial por país | Banco Mundial API v2 / FMI DataMapper | ~0,5 % por ronda hoy; 0 si se automatiza |
| Liquidez | Mensual (bajar de semanal) | FRED M2SL, BCE BSI | Balance del banco central propio | 0 |
| Calificaciones | Tras cada revisión de agencia | Comunicados de agencia (muchos ⛔) → [S] | Prensa fiable; marcar nivel S | ~0,5 % por ronda |
| Deuda FMI | Abril y octubre (WEO) | FMI DataMapper | Banco Mundial | ~0,5 % por ronda |
| Reservas | Trimestral (COFER) | FMI | Banco central del país | ~0,3 % |
| Mandatos / regulación | Tras cada reunión o publicación en boletín oficial | Federal Register, EUR-Lex (navegador), BOE | Prensa especializada (nivel S) | ~1 % por ronda de mandatos |
| RWA por cadena | Mensual (bajar de semanal); extra si hay hito | rwa.xyz u otra [VERIFICAR] | Segunda plataforma + datos de cadena | ~0,5 % |
| CBDC y blockchains | Trimestral | BIS, bancos centrales | Atlantic Council tracker [VERIFICAR] | ~1 % por ronda |
| Elecciones y países | Fecha de cada elección + 1 semana | Organismos electorales (algunos sin acceso) | Prensa | ~0,5–1 % por elección |
| Estabilidad / valoración sectorial | Trimestral / mensual | Índices públicos | — | ~0,5 % |

Segunda fuente con prioridad (OPINIÓN): (1) cotizaciones, hoy casi todo Yahoo; (2) tipos de interés, ya hay base BIS y primaria; (3) RWA y cifras cripto, hoy manual y fuente única.

## 4. Qué datos manuales automatizar primero (OPINIÓN, por utilidad ÷ esfuerzo)
| Orden | Fichero | Por qué | Cómo (fuente ya ✅ en el mapa) |
|---|---|---|---|
| 1 | `tipos-manual.json` | Utilidad alta; ya existe código que lo mezcla con BIS; fuentes primarias con API (Riksbank, Norges, SNB, BCRP) | Ampliar `URL_BIS_TIPOS` + APIs abiertas; RBA/RBNZ siguen a mano |
| 2 | `indicadores-manual.json` | Macro; lo cubren Banco Mundial, FMI DataMapper y FRED | Script con series por país y fecha de publicación |
| 3 | `liquidez-manual.json` | Solo JP y CN manuales; resto ya automático | Fuentes de BoJ/PBoC; PBoC ⛔ → posible que siga manual [VERIFICAR] |
| 4 | `espana-manual.json` | INE/BdE con API; evita datos congelados (IPC251856) | `wstempus` con códigos nuevos (`IPC290750`) |
| 5 | `bonos-manual.json` | Extensión de la curva de EE. UU. a FR/ES/IT/CN; aft.gouv.fr ⛔ | Parcial: Bundesbank/Banco de España; el resto manual |
| 6 | `rwa-por-cadena-manual.json` | Alta utilidad pero fuente única y sin API probada | Primero fijar fuente y segunda fuente; luego automatizar [VERIFICAR] |
| 7 | `estabilidad-manual.json` | Cadencia trimestral, poco coste a mano | Dejar manual |

## 5. Pendientes y [VERIFICAR]
- [VERIFICAR] Segunda fuente de cotizaciones (Stooq/FRED): no probada aquí.
- [VERIFICAR] Fuente y API de RWA por cadena; qué mide cada «CBDC y blockchains» frente a Mandatos.
- [VERIFICAR] Selic: SGS 432 (13,75 %) frente a prensa (14,25 %) — abierto en el plan 3-nov.
- Cambio de cadencia propuesto para decidir por Joel: liquidez y RWA de semanal a mensual; reservas a trimestral.
- Costes de cuota son estimaciones [ESPECULACIÓN]; medir tras la primera ronda real.

---

# Segunda pasada: revisión de la app real y propuestas (8-nov-2026, noche)

**Cómo se hizo (HECHO):** navegador integrado, servidor local de `docs/movil` (Hoy, Seguimiento, Agenda, Mercado, Más) a 375 px, y `docs/orbita` (10 pestañas) a 375 y 1280 px. `explorador/vistas.html` abierto como archivo: es una plantilla que dice «Sin datos: esta plantilla se abre desde la Órbita», así que no se puede juzgar por separado. Medí desbordes y texto con JavaScript; las capturas a escala reducida servían poco, así que **el juicio de «se entiende en 5 segundos» es OPINIÓN mía sobre el texto y la estructura, no una prueba con usuarios**. El móvil a 1280 px no se revisó pantalla por pantalla [VERIFICAR].

## 1. Hallazgos por pantalla y panel

| # | Pantalla › panel | Qué se ve (HECHO) | Problema / valoración (OPINIÓN) |
|---|---|---|---|
| H1 | Móvil › Hoy › cabecera (9 fichas) | XRP, XLM, Brent, Fed, BCE, IPC ES/euro/EE. UU., BTC con variación y «a 05/11» | Se entiende rápido. Pero XRP/XLM salen **tres veces** en la misma pantalla (cabecera, «Mis activos», «Digital assets»): ruido. «a 05/11» es la fecha del dato, sin decir que es la decisión del banco |
| H2 | Móvil › Hoy › Ormuz | Aviso: último dato 25-oct, hace 15 días, «es un dato que falta» | **Bien resuelto** (dato viejo avisado). Copiar el patrón a todos los datos ámbar |
| H3 | Móvil › Hoy › racha | «2 días», «1 días de racha», «87 % plan hecho» | Gamificación sin relación con decidir; error gramatical «1 días». Es ruido en la pantalla de decisión [OPINIÓN] |
| H4 | Móvil › Seguimiento › cabecera | «72 % · 148 hechas · 22 pendientes» | No cuadra con `seguimiento.json` regenerado (212 hechas, 56 pendientes): dos universos distintos sin explicar [VERIFICAR] |
| H5 | Móvil › Seguimiento › Verificaciones pendientes | «hutiES a Arabia Saudi» **dos veces**; «Brent cierra en $111,97» dos veces | Duplicados visibles; el «Brent a $111,97» choca con Brent $98,32 de Mercado y no dice que es de hace 16 días |
| H6 | Móvil › Seguimiento › «Qué se está quedando viejo» | 2 urgentes, «30 celdas sin dato», «7 fechas previstas pasadas» | Útil como control interno, **no ayuda a decidir sobre inversión**; mejor en «Más» [OPINIÓN] |
| H7 | Móvil › Agenda | ~40 eventos en lista plana, filtros Alto/Medio/Bajo, «fecha aproximada» | Muy útil (es el disparador del research). Falla: no separa «mi cartera» (XRP/XLM: escrow 1-dic, Protocol 30 el 23-nov) de macro; sin .ics ni aviso |
| H8 | Móvil › Mercado › «Frescura de los datos» | 17 conjuntos, 8 en verde, 9 en ámbar/rojo | Excelente idea; ocupa la primera pantalla antes de ver un solo precio y mezcla precios con research |
| H9 | Móvil › Mercado › Bolsas | «sesión 6-nov · 1 día», nivel S, Yahoo | Hoy es domingo y dice «1 día» (hábil): bien. **Falta la hora**; Kospi −6,0 % y Nikkei −5,96 % sin contexto [VERIFICAR con segunda fuente] |
| H10 | Móvil › Mercado › Divisas y tipos | 5 pares + DXY + 3 tipos oficiales + 3 bonos + Euríbor, **un solo grupo de 14 filas** | Mezcla divisas, tipos y bonos; sin separar pares con euro, refugio, emergentes (apartado 2) |
| H11 | Móvil › Mercado › Metales y Alimentos | Oro 4.074 $, plata, cobre; trigo, maíz, arroz, FAO… | Oro solo en dólares (para un residente español importa en €); arroz y azúcar de «5-nov», el resto «6-nov»: fechas distintas en un mismo grupo |
| H12 | Móvil › Mercado › Energía | Brent, WTI, Henry Hub, luz OMIE y PVPC (7-nov) | El texto es honesto: «Falta el gas europeo TTF (C111) y gasolina y diésel». Luz y petróleo con fecha distinta en el mismo bloque |
| H13 | Móvil › Más | 7 tarjetas (Datos, Noticias, Centro, Voces, Vídeos, Informes, Buscar) | Claro. Faltan Glosario y Ajustes |
| H14 | Órbita › cabecera (todas las pestañas) | «radar 2026-11-04 · Órbita 2026-11-06 · paneles 2026-11-08 21:01 UTC · en vivo 23:15» | Cuatro fechas en una línea: transparente pero difícil de leer. Falta «lo más viejo es X» |
| H15 | Órbita › Resumen | «Qué cambia hoy» y «Mis activos: XRP y XLM» con nivel S/P por cifra y fuente | **El mejor panel de la app** para decidir: dato + fuente + nivel. Cuesta ver lo importante porque debajo van 74 novedades de research |
| H16 | Órbita › Capas | 7 capas (Dinero digital 12, Tipos/liquidez/deuda 17, Crédito 7, Energía/alimentos/chips 16, Raíles y custodia 16, Tokenización 9, Reglas 26) | Estructura buena; cada capa abre con texto largo y denso; el desplegable comparador es lo más claro |
| H17 | Órbita › Noticias | «Últimas 24 h (0) · Nada en este tramo»; noticias con «caduca 2026-11-08» y «Dudoso» siguen visibles | El estado vacío está bien explicado. **Desborde horizontal a 375 px** (421 px frente a 361). Noticias caducadas aún en pantalla |
| H18 | Órbita › Matriz país × tema | 118 de 168 celdas; «Política monetaria» casi todo «—» | Útil para regulación; una columna vacía parece abandonada |
| H19 | Órbita › Países / España | Ficha de España con IPC, paro, PIB, deuda y 60 meses de historia | Muy completa; no permite comparar con otro país en la misma vista |
| H20 | Órbita › Paneles de datos | Spreads vs Alemania, Focus, stablecoins XRPL/Stellar, RWA por cadena (manual, leído 29-oct) | Cada bloque dice qué mide, unidad, fuente y fecha: la referencia de «cómo debe ser un panel». El RWA manual de hace 10 días no tiene aviso ámbar propio |
| H21 | Órbita › Línea de tiempo | 103 movimientos, 91 con reacción de precios | Interesante para la tesis; a 375 px la página mide solo 1.801 px de alto: parece reducida sin avisar [VERIFICAR] |
| H22 | Vistas (`explorador/vistas.html`) | Filtros País/Tema/Certeza; «Sin datos» si se abre sola | Mensaje claro; no explica cómo llegar desde la Órbita |

**Contraste y tamaño (HECHO):** ningún texto por debajo de 11 px en Órbita; sin desborde horizontal salvo H17. Tema oscuro por defecto (decisión de Joel).

## 2. Mercado en concreto
**Divisas por tipo (propuesta, OPINIÓN):**

| Subgrupo | Pares / datos | Hoy |
|---|---|---|
| Euro frente a… | EUR/USD, EUR/GBP, EUR/CHF, EUR/JPY, EUR/CNY | Ya (BCE, 5 pares) |
| Dólar (fuerza) | DXY, USD/JPY, USD/CNH, USD/CAD | Solo DXY (Yahoo, S) |
| Refugio | CHF, JPY, oro en € | CHF y JPY frente al euro; falta oro en € |
| Emergentes | USD/BRL, USD/MXN, USD/INR, USD/TRY, USD/ZAR, USD/KRW | **Nada**; el BCE publica referencias de varias de estas monedas (mismo origen que ya se usa) [VERIFICAR lista] |
| Cripto | XRP/EUR, XLM/EUR, XRP/BTC | Sin XRP/BTC |

**Activos que faltan para un inversor español de largo plazo con XRP/XLM (OPINIÓN):** gas TTF y combustibles (ya anotado C111); bono alemán a 10 años y spread España–Alemania en Mercado (hay panel en Órbita); bono italiano; curva de EE. UU. a 2 años; oro en euros; ETF de renta fija en euros y de bolsa europea (hay VWCE/IWDA/VUSA); dominancia de BTC, oferta de stablecoins, flujos de ETF de XRP/XLM (Mercado muestra solo precio); S&P 500 en euros (efecto divisa); inflación real (IPC menos tipo del Estado a 10 años).

**Hora real de actualización por dato (propuesta):** hoy cada fila dice «sesión 6-nov · 1 día» (solo fecha). Añadir al JSON de cada dato `leido_utc` (cuándo lo leyó el script) y `valor_fecha_hora` (cuándo cotizó). En pantalla, al tocar la fila: «cotizó 6-nov 22:00 · leído 8-nov 22:01»; en la fila, solo un punto de color (verde < 1 día hábil, ámbar 2-3, rojo ≥ 4) y «hace 2 d hábiles». En fin de semana, «mercado cerrado» en vez de «1 día». Cripto: «en vivo» más la hora del navegador.

## 3. Propuestas priorizadas (22)
Cuota = % de la cuota semanal con agente [ESPECULACIÓN]; 0 = sin IA. Riesgo = de romper la app o de inducir a error.

### Bloque A: arreglo rápido (< 30 min cada una)
| # | Qué cambia | Por qué ayuda a decidir | Esf. | Cuota | Riesgo |
|---|---|---|---|---|---|
| 1 | Quitar duplicados en «Verificaciones pendientes» (H5) y poner «hace N d» junto a cada cifra citada | Evita creer un Brent de $111 de hace 16 días | S | <0,3 % | Bajo |
| 2 | Corregir «1 días de racha» y mover «racha» y «% plan hecho» de Hoy a Más (H3) | Menos ruido en la pantalla de decisión | S | <0,2 % | Bajo |
| 3 | Mostrar XRP/XLM una sola vez en Hoy (H1) | Libera sitio para «qué cambió» y fechas | S | <0,2 % | Bajo |
| 4 | Arreglar el desborde de Órbita › Noticias a 375 px y ocultar caducadas por defecto con interruptor (H17) | Lectura en móvil sin desplazar | S | <0,3 % | Bajo |
| 5 | Separar «Divisas y tipos» en Divisas, Tipos oficiales y Bonos (H10) | Se entiende de un vistazo qué es cada cosa | S | <0,3 % | Bajo |
| 6 | Mover «Frescura de los datos» bajo los precios y dejar un resumen («3 datos en rojo») (H8) | Precio primero; control de calidad después | S | <0,2 % | Bajo |
| 7 | Etiqueta común de fecha del dato en Energía y Alimentos (H11, H12) | No comparar dos fechas como si fueran la misma | S | <0,2 % | Bajo |
| 8 | Aviso ámbar a los 7 días en el RWA manual (H20) y corregir la nota de congress.gov (apartado 6) | Datos manuales viejos no pasan por buenos | S | <0,2 % | Bajo |

### Bloque B: medio (horas)
| # | Qué cambia | Por qué ayuda a decidir | Esf. | Cuota | Riesgo |
|---|---|---|---|---|---|
| 9 | Hora real por dato (apartado 2) en `actualizar_paneles.py` y en la ficha | Sabes cuán viejo es lo que miras | M | ~0,8 % | Medio (toca el script) |
| 10 | Segunda fuente en cotizaciones (Stooq o FRED) con aviso si difieren más de 1 % (H9) | Detecta errores como un Kospi −6 % falso | M | ~1 % | Medio: [VERIFICAR] acceso y licencia |
| 11 | Subgrupos de divisas del apartado 2 con emergentes del BCE | Ver fuerza del dólar y riesgo emergente | M | ~0,8 % | Bajo |
| 12 | Agenda: filtro «Mi cartera» (escrow, Protocol 30, ETF, SEC) y exportar .ics (H7) | Calendario como recordatorio personal | M | ~0,6 % | Bajo |
| 13 | Automatizar `tipos-manual.json` e `indicadores-manual.json` (apartado 4 de la primera pasada) | Menos datos a mano que envejecen | M | ~2 % una vez | Medio |
| 14 | Una frase «lo más viejo es X (hace N d)» en la cabecera de Órbita en lugar de cuatro fechas (H14) | Leer la frescura de un vistazo | S-M | ~0,3 % | Bajo |
| 15 | Fichas por activo (XRP, XLM, BTC, oro, ETF mundial): precio, fuente, nivel, últimos hechos, próximas fechas y riesgos | Extiende el nivel de «Mis activos» (H15) a todo lo que sigue Joel | M | ~2 % | Medio (no deslizar a «recomendar») |
| 16 | Glosario tocable («spread», «EFFR», «RWA», «COFER») en móvil y Órbita | Comprensión en 5 s y uso en familia | M | ~1 % | Bajo |

### Bloque C: grande (días, solo si Joel lo decide)
| # | Qué cambia | Por qué ayuda a decidir | Esf. | Cuota | Riesgo |
|---|---|---|---|---|---|
| 17 | Vista de tesis (privada, en `privado/`): cada pilar con su evidencia, fecha de la última prueba y señal a favor / en contra / sin dato | Contrasta caso alcista y bajista con datos | L | ~5 % | Alto: no volcar la tesis al repo público |
| 18 | Alertas por umbral y por evento (Telegram ya existe): dato en rojo, cambio de tipo oficial, noticia de nivel P sobre XRP/XLM | Avisa solo de lo que cambia la conclusión | L | ~3 % + bot | Medio (coste del bot) |
| 19 | Comparador de países (riesgo, tipo, deuda, calificación) y de ETF mundiales | Ver dónde está el riesgo con datos homogéneos | L | ~3 % | Medio |
| 20 | Capa «Mi cartera» sin importes (pesos, divisa, riesgo país, riesgo cripto) con el importador CSV existente | Ver la exposición real | L | ~4 % | Alto: datos privados |
| 21 | Modo familia: vista reducida (sin racha, solo precios, calendario, glosario y «qué cambió») | Uso por la familia; menos sobrecarga | L | ~2 % | Medio (no exponer lo privado) |
| 22 | Capas nuevas: flujos de ETF de XRP/XLM, oferta de stablecoins, vivienda (INE/Registradores), combustibles UE | Cubre los huecos del apartado 2 | L | ~4 % | Medio ([VERIFICAR] fuentes) |

**Research que alimentaría cada idea:** (9–11) series de BCE, BIS y Stooq; (12) calendario oficial y `eventos/calendario.toml`; (15) fichas del cerebro y Mercado; (17) tesis en `privado/` y evidencia pública; (18) tipos de banco central y noticias de nivel P; (19) calificaciones, FMI, Banco Mundial; (22) EIA, TTF (C111), INE, flujos de ETF [VERIFICAR fuente].

**Orden recomendado (OPINIÓN):** 1-8 de golpe en una sesión; después 9 → 10 → 11; las grandes solo tras elegir Joel (17 y 18 primero por su peso en la decisión).

## 4. Referentes [S]
**HECHO (lo que devolvieron dos búsquedas el 8-nov; son páginas de comparación y reseñas, **no** hilos de Reddit ni de Bogleheads, que no aparecieron):**
- FRED se cita como la fuente gratuita de referencia para macro, pero «es una base de datos, no un panel»: hay que montar la vista ([findmymoat.com](https://www.findmymoat.com/free/macro-data)) [S].
- Koyfin gratis: paneles macro, gráficos básicos y datos con retraso, que para largo plazo casi nunca importa ([quantroutine.com](https://quantroutine.com/tools/koyfin/)) [S].
- TradingView para largo plazo: guardar 3-4 gráficos macro como «Macro Dashboard» y revisarlos una vez al mes ([kotakneo.com](https://www.kotakneo.com/stockshaala/trading-view/long-term-investors-watchlists-notes-and-macro-indicators/)) [S].
- TradingView ofrece un mapa de calor de divisas gratis con fortaleza y debilidad relativa ([financemagnates.com](https://www.financemagnates.com/forex/technology/tradingview-unveils-another-terminal-feature-launches-forex-heat-map-widget/)) [S].
- **No encontré** cómo agrupan majors, cruces y emergentes ni qué ven las comunidades de inversión a largo plazo [VERIFICAR]: lo cubre C186 (Gemini manual).

**OPINIÓN (qué se puede copiar):** (a) revisión mensual con 3-4 gráficos fijos en vez de vigilancia diaria, que encaja con bajar la cadencia de lectura; (b) mapa de calor de divisas (propuesta 11); (c) la app ya supera a esos terminales gratuitos en lo que aquí importa (nivel P/S, fuente y fecha por cifra); le falta presentación y comparadores, no más datos.

## 5. Filas añadidas a `research/tareas.csv`
C189–C210 (22 filas, pendientes): C189 = propuesta 1, …, C210 = propuesta 22.

## 6. Nota sobre `informes/research/2026-11-09-auditoria-datos-y-research.md` (no se toca el informe)
Dice que congress.gov y senate.gov no sirven con Chrome. **Corrección (dato que pasa la sesión que me lo pidió; no lo verifiqué yo):** congress.gov **sí** cargó con Chrome y VPN y se leyó H.R.3633. Ajustar la fila «aft.gouv.fr, bls.gov, congress.gov, senate.gov…» (⛔) de `MAPA-DE-FUENTES.md` cuando Joel lo confirme; senate.gov sigue sin probar con VPN [VERIFICAR].

---

# Corrección de prioridad (8-nov, noche): la Órbita primero, el móvil al final

**Qué cambia:** la revisión de arriba empezó por el móvil por un error del encargo. Esta sección es la central: la **Órbita** (`docs/orbita/index.html`) para ordenador y tablet. Los apartados 1 a 3 de la «Segunda pasada» siguen valiendo para el móvil; las propuestas 1–22 se reordenan abajo (la Órbita pasa delante).

**Cómo se hizo (HECHO):** navegador integrado a 1440, 1280, 1024 (tablet horizontal) y 768 px (tablet vertical). Recorrí las 10 pestañas, midiendo con JavaScript: desbordes, tablas más anchas que su contenedor, controles de menos de 28 px de alto, filtros, buscadores, enlaces y altura de página. `explorador/vistas.html` y `explorador/paneles.html` son **plantillas** (se abren desde la Órbita; la segunda pone el título de cada país), sin contenido propio: no hay nada que juzgar por separado. Las capturas se redujeron mucho, así que los juicios de «se entiende rápido» son OPINIÓN sobre texto y estructura, no pruebas con usuarios. Los gráficos SVG internos (hay 97 en el documento) no se inspeccionaron uno a uno [VERIFICAR].

## 7. Órbita: qué hay, pestaña por pestaña

| Pestaña | Qué muestra (HECHO) | Controles (HECHO) | Valoración (OPINIÓN) |
|---|---|---|---|
| Resumen | «Qué cambia hoy», «Mis activos: XRP y XLM» (precio, cambio 24 h, capitalización, stablecoins, ETF, 13F, con fuente y nivel P/S), cifras clave por bloque (cripto, tipos y deuda, energía, miedo y chips, España), mayores movimientos, últimos movimientos, próximas fechas, 74 novedades de research | 2 botones; sin filtros ni selector | **El mejor punto de entrada.** Pero 5.000 px de alto a 1440 y 7.900 a 768: lo urgente y lo histórico conviven. Falta una línea «lo que cambia la conclusión hoy» |
| Capas | 7 capas (Dinero digital 12, Tipos/liquidez/deuda 17, Crédito 7, Energía/alimentos/chips 16, Raíles y custodia 16, Tokenización 9, Reglas 26), «Datos al día», «Pendiente de verificar», «Hechos por estado» (en producción 7, piloto 4, plan 3), documentos (19) y glosario (10 términos) | Filtro de país (22), filtro de certeza (3), 5 desplegables, 6 enlaces internos | La estructura es buena y es el sitio natural para cruzar datos; **el glosario de 10 términos está enterrado al final**. Dos tablas desbordan a 768 px |
| Línea de tiempo | 103 movimientos en 13 capas, 91 con reacción de precios (superponer Brent, bitcoin, stablecoins a 3 a la vez) | Buscador de texto, filtro de país, rango (3), 4 casillas, 28-32 botones | **Es la vista más cercana a un terminal**; casi no tiene enlaces fuera (0). Altura fija de ~1.000-1.700 px: con 103 puntos hay solapes [VERIFICAR] |
| Calendario | Próximos meses desde 2026-11 a 2027-07, «lo más próximo (impacto alto)» | Ninguno (sin filtros, sin países, sin .ics) | Sirve, pero a 1440 px es una lista de 4.400 px; sin filtro por capa, país ni «mi cartera» |
| Matriz país × tema | 118 de 168 celdas, escala 0-5, P/S, 8 temas, huecos conocidos | País, tema, certeza, «solo cambios en 30 días» | Buena para regulación; la columna Política monetaria es casi todo «—». Sin enlaces a la ficha del país ni al dato que sustenta cada celda |
| Noticias | Últimas 24 h (0), hasta 7 días (16), hasta 30 días (27), archivo (58) con caducidad | 1 filtro | Buena idea (caducidad); la caducada sigue visible; vacío de 24 h bien explicado |
| Voces | 73 declaraciones con nivel P/D/S/C/R/E y confirmación | Buscador y 4 filtros (tipo, nivel, confirmación, capa), 72 enlaces | **La vista mejor equipada en filtros**; es la referencia para el resto |
| Países | Grupos UE, Potencias, BRICS, Latinoamérica; fichas por país (España, Alemania, Francia, Italia, Países Bajos, Polonia en UE), cifras por bloque, historia 2/5 años, máximos y mínimos, mandatos por presidente | Botones de grupo y de país, 30 desplegables, «Comparar todos los países (tablas completas)» | Muy rica; **comparar es una tabla escondida al final**, no una vista; «Vivienda · 1 cifras» (gramática) y bloques de 1 cifra parecen incompletos. Tablas anchas |
| España | Entrada, destino de cada euro y beneficiarios; US aparte con otra definición | 21 desplegables | Es de las más claras; la advertencia «cifras de otra definición: no se suman» es un buen patrón |
| Paneles de datos | Spreads vs Alemania, Focus, stablecoins en XRPL y Stellar, DefiLlama (automático), RWA (manual, 29-oct) | 24 desplegables, 25 tablas | **La mejor ficha técnica** (qué mide, unidad, fuente, fecha). 7.200 px de alto; sin buscador ni índice lateral |

### Hallazgos transversales (HECHO medido / OPINIÓN)
| # | Hallazgo | Evidencia |
|---|---|---|
| O1 | **No hay buscador global**: solo Línea de tiempo y Voces tienen texto de búsqueda | 2 de 10 pestañas con campo de texto |
| O2 | **Pocos enlaces entre datos**: Calendario, Matriz y Línea de tiempo tienen 0 enlaces; Capas 6; solo Voces tiene 72 | Conteo de enlaces visibles por pestaña |
| O3 | **Los filtros no se comparten entre pestañas**: «País» existe en Capas, Línea de tiempo y Matriz, cada uno por su lado; la elección no se guarda al recargar [VERIFICAR el cambio de pestaña] | Mismo `fpais` (22 países) en 3 pestañas; `localStorage` vacío |
| O4 | **Controles pequeños en tablet**: 45 (Voces), 66 (España) y 51 (Paneles) controles de menos de 28 px a 1024 px | Medición de alto de botones, enlaces y campos |
| O5 | **Tablas que desbordan** a 768 px: Países 10, Paneles 9, Capas 2, España 1 | Tablas con ancho mayor que su contenedor |
| O6 | **Páginas muy largas** sin índice lateral: Paneles 7.200 px, Capas 6.500 px, Voces 5.900 px (1440 px); el «Ir a:» de Capas es la excepción | Altura medida |
| O7 | **Cuatro fechas en la cabecera** y ninguna dice «lo más viejo»; el pie ya explica P/S/V/ESP y semáforo (bien) | Cabecera común a todas las pestañas |
| O8 | **Sin vista de comparación** de países ni de capas lado a lado, aunque los datos están | «Comparar todos los países» es solo una tabla plegada |
| O9 | **Sin tesis, sin alertas, sin «mi cartera»**: es una vista de lectura; las decisiones de Joel están fuera del tablero | Ninguna pestaña lo contiene |
| O10 | **Desborde a 375 px** solo en Noticias (421 px), no en tablet | Medida a 375/768/1024/1280/1440 |
| O11 | **Mercado en la Órbita:** hay bloque de cifras (cripto, tipos y deuda, energía, miedo y chips), sin pestaña propia de mercado, sin divisas ni emergentes | Resumen › «Cifras clave» |

**Comportamiento con mucha información (OPINIÓN):** la densidad se resuelve con desplegables (bien) pero la jerarquía es plana: todo parece igual de importante. No hay modo «foco» (solo lo que cambió), ni fijar un panel, ni dos paneles a la vez; en pantalla grande (1440) el ancho se desaprovecha en listas largas de una columna, y en tablet vertical (768) las tablas pasan a deslizamiento horizontal.

## 8. Propuestas priorizadas con la Órbita primero
Las propuestas 1–22 de arriba siguen en `research/tareas.csv` (C189–C210). Aquí se añade lo específico de la Órbita (C211–C224) y se **reordena** la prioridad.

| Orden | Propuesta | Esf. | Cuota | Ayuda a decidir porque… | Research que la alimenta |
|---|---|---|---|---|---|
| 1 | **Buscador global** y barra «Ir a» común a todas las pestañas (O1) | M | ~0,8 % | Encontrar un dato o declaración sin saber en qué pestaña está | Ninguno nuevo |
| 2 | **Filtro de país, capa y certeza compartido** entre pestañas, guardado en el navegador (O3) | M | ~0,6 % | Mirar «Japón» en todas las vistas a la vez | Ninguno |
| 3 | **Enlaces entre datos**: Calendario ↔ Línea de tiempo ↔ Matriz ↔ Voces ↔ ficha de país (O2) | M | ~1,5 % | De un evento ves quién lo dijo, qué país afecta y qué reacción tuvo el precio | Índice de identificadores ya existente en `explorador/ids` [VERIFICAR] |
| 4 | **Arreglos de tablet**: controles ≥ 40 px, tablas con sombra de deslizamiento y primera columna fija, desborde de Noticias (O4, O5, O10) | S-M | ~0,5 % | Lectura cómoda a 768 y 1024 px | Ninguno |
| 5 | **Cabecera con «lo más viejo es X (hace N d)»** y semáforo de frescura clicable que lleva a ese dato (O7) | S-M | ~0,3 % | Sabes qué no creer hoy | Ninguno |
| 6 | **Índice lateral fijo** en pestañas largas (Paneles, Capas, Voces) (O6) | S-M | ~0,4 % | Navegar 7.000 px sin perderte | Ninguno |
| 7 | **Comparador de países** (2-4 países, indicadores elegidos, mismo periodo) como vista, no tabla plegada (O8) | L | ~3 % | Contrastar riesgo, tipo, deuda y calificación con datos homogéneos | Países, calificaciones, FMI, Banco Mundial |
| 8 | **Comparador de capas** (dos capas lado a lado con sus hechos recientes) | M-L | ~2 % | Ver cómo se cruzan, por ejemplo, tipos y stablecoins | Ya existente |
| 9 | **Modo «foco»** en Resumen: solo lo que cambió en 24 h/7 días y lo que caduca | M | ~0,8 % | Jerarquía: lo que cambia la conclusión primero | Ninguno |
| 10 | **Panel de tesis** privado en `privado/` (pilares, evidencia, señal a favor/en contra/sin dato, fecha de última prueba) | L | ~5 % | Contrasta caso alcista y bajista sin recomendar | Tesis privada + evidencia pública |
| 11 | **Fichas por activo** (XRP, XLM, BTC, oro, ETF mundial) con mercado, fuente, hechos, fechas, riesgos | M | ~2 % | Un solo sitio por cada activo que sigue Joel | Mercado + capas |
| 12 | **Calendario con filtros** (capa, país, «mi cartera») y exportación .ics; marcar lo que ya tiene research | M | ~0,8 % | Convierte el calendario en recordatorio y en lista de research | `eventos/calendario.toml` |
| 13 | **Glosario flotante** y subido a la cabecera, con «¿qué es esto?» en cada cifra | M | ~1 % | Entender «spread», «EFFR», «RWA» sin salir | Glosario existente (10 términos) |
| 14 | **Alertas** (Telegram existente) por dato en rojo, cambio de tipo oficial y noticia de nivel P sobre XRP/XLM | L | ~3 % + bot | Avisa solo de lo que cambia la conclusión | Tipos y noticias |
| 15 | **Pestaña Mercado en la Órbita** con divisas por tipo (euro, dólar, refugio, emergentes), hora real por dato y segunda fuente (aplica lo del apartado 2) | M-L | ~2 % | Es el hueco O11; reutiliza lo ya hecho en el móvil | BCE, FRED, Stooq [VERIFICAR] |
| 16 | **Modo familia**: vista reducida con precios, calendario, glosario y «qué cambió», sin lo privado | L | ~2 % | Uso por la familia | Contenido existente |
| 17 | **Rendimiento con muchos datos**: cargar por pestaña (no todo el documento: hoy son 2,1 MB con 97 SVG), listas virtualizadas en Voces y Línea de tiempo | L | ~3 % | Abre rápido y no se cuelga al crecer | Ninguno |
| 18 | **Capas nuevas** (flujos de ETF de XRP/XLM, vivienda, combustibles UE, comercio) | L | ~4 % | Cierra huecos de datos | Plan de actualización de datos |

**Prioridad de ejecución (OPINIÓN):** 1, 2, 4, 5, 6 son la base (usabilidad y confianza) y encajan en una o dos sesiones; luego 3, 9, 12, 13; las grandes (7, 10, 14, 15, 17, 18) tras decidir Joel. Lo del móvil (propuestas 1–8 de arriba) se hace al final y es de poco esfuerzo.

## 9. Referentes de escritorio [S]
**HECHO (búsqueda del 8-nov; son páginas de comparación y reseñas, muchas de proveedor o generadas, no hilos de comunidades):**
- Koyfin: nivel gratuito con paneles, gráficos, pantallas de análisis y macro global; se vende como alternativa barata a Bloomberg ([G2](https://www.g2.com/compare/bloomberg-terminal-vs-koyfin), [rfp.wiki](https://www.rfp.wiki/investment/bloomberg-terminal/koyfin)) [S].
- OpenBB: terminal abierto y autoalojable con un Workspace para analistas; no está claro si incluye enlaces entre widgets ni alertas ([TechCrunch](https://techcrunch.com/2024/10/07/fintech-openbb-aims-to-be-more-than-an-open-source-bloomberg-terminal/), [dev.to](https://dev.to/k-adi/financial-freedom-through-open-source-openbb-vs-proprietary-tools-2l6j)) [S].
- Bloomberg: se cita como «imbatible en información»; no devolvió nada sobre su diseño [S].
- TradingView y FRED (de la pasada anterior): el primero propone 3-4 gráficos macro fijos con revisión mensual; el segundo es «una base de datos, no un panel».
- **No encontré** (queda [VERIFICAR]): cómo enlazan widgets, qué filtros comparten y cómo guardan vistas esos terminales, ni qué dicen los foros de inversores a largo plazo (Bogleheads, Reddit). C186 (Gemini manual) puede cubrirlo.

**OPINIÓN — qué se puede copiar** (patrones generales de terminales de escritorio; **no verificados aquí**): (a) un contexto común (país, activo, rango) que afecta a todas las vistas; (b) lista de seguimiento y fichas por activo; (c) comparar dos entidades lado a lado; (d) vistas guardadas por tema; (e) alertas por regla. La Órbita ya supera a las herramientas gratuitas en lo propio (nivel P/S/V, fuente y fecha por cifra, caducidad de noticias, aviso de dato que falta); lo que le falta es **navegar y cruzar**, no más datos.

## 10. Filas añadidas a `research/tareas.csv`
C211–C223 (13 filas pendientes): propuestas 1–9, 12, 13, 15 y 17 de la tabla del apartado 8. Las de tesis, fichas por activo, alertas, comparador de países genérico, modo familia y capas nuevas ya están como C203, C205, C206, C207, C209 y C210 (la prioridad de la Órbita sobre el móvil queda en el orden del apartado 8).
