# Plan: versión móvil del Cerebro (idea del 25-oct-2026)

Objetivo de Joel: una versión **solo de consulta** pensada para móvil (Android y iPhone), visualmente distinta y más compacta, **sin tocar la estructura del Cerebro de ordenador** (`app.py`, `cerebro.py`, `explorador/`). Lo mínimo a controlar: tipos de interés, deuda, unos pocos precios, eventos, noticias, análisis de vídeos y voces.

## 1. Qué ya existe (no se rehace)
- `docs/` (GitHub Pages): página de entrada instalable (PWA) con `manifest.webmanifest`, `sw.js`, iconos y pantallas de arranque para iPhone; hoy carga la app de Streamlit en un iframe. Lección del 14-oct: en iPhone instalado hay que quitar `viewport-fit=cover` o aparece una banda inferior ([[ios-pantalla-completa-pwa]]).
- **Datos públicos ya generados por bots/scripts, sin IA:** `explorador/paneles.json` (tipos al día, bonos y curvas, deuda, stablecoins, índices, 4 digital assets; workflow L-V 21:30 UTC), `explorador/regulacion.json` (radar), `explorador/voces.json` (44 voces), `explorador/calificaciones.json`, `eventos/calendario.toml` (88 eventos), `noticias/noticias.json` (rama `datos`, noticias con nota 1-10), informes en `informes/` (R00, vídeos, research) y lecciones en `cerebro/documentos/`.
- **Aviso por Telegram** ya funciona (`eventos/avisos.py`, noticias del bot): sirve de canal de notificaciones sin necesitar notificaciones push de la web.

## 2. Regla de privacidad (no negociable)
El repo y GitHub Pages son **públicos**. La versión móvil publica **solo lo que ya es público**. La tesis de Joel, la cartera, `privado/` y `voces-tesis.json` **no** entran. Lo privado se sigue viendo en la app de Streamlit con contraseña (enlace desde el móvil) o en el ordenador. No se cifra la tesis para publicarla (riesgo innecesario).

## 3. Ideas tomadas de apps parecidas (búsqueda 25-oct, fuentes de reseñas, no oficiales)
- Apps de mercados (Yahoo Finance, MarketWatch, CNBC, Google Finance): **abren directamente en el contenido** (no en una portada), **barra inferior** con 3-5 pestañas (Inicio / Noticias / Mercados), **lista de seguimiento fija** (watchlist), **cinta horizontal de precios** encima del feed y **widgets** con un valor destacado y el resto debajo.
- Lectores de noticias (Inoreader, Feedly, Readwise Reader): **etiquetas, filtros y reglas**, y un **resumen diario** ("digest"); el mejor patrón para el feed del bot (filtrar por nota ≥ 7, por tema, por «sin confirmar»).
- Patrón de iOS Stocks: deslizar para quitar de la lista; pulsar abre el detalle.

## 4. Propuesta de pantallas (barra inferior de 5)
| Pestaña | Qué muestra (compacto, tarjetas plegables) |
|---|---|
| **Hoy** | Cinta de 4 digital assets + 4 índices; tipos clave (Fed, BCE, BoE, Brasil, Canadá); los 3 próximos eventos; titular del último R00 con su etiqueta de fuente; avisos (⚠ radar desactualizado, reunión pasada) |
| **Mercado** | Tabla de tipos de interés; bonos a 10 años y curvas; diferenciales; calificaciones; stablecoins y RWA |
| **Agenda** | Eventos por día, color por impacto, cuenta atrás, filtro por tema y país; los «aproximados» marcados |
| **Noticias** | Feed del bot con nota, tema y badge P/S; filtros «urgentes», «sin confirmar», cripto/macro/regulación |
| **Cerebro** | Voces (por persona, capa y nivel), análisis de vídeos, informes y lecciones, buscador local |

Diseño: modo oscuro, tipografía grande, tablas que pasan a **tarjetas** (1 columna), gráficos mínimos, un solo gesto principal (pulsar para desplegar). Nada de la órbita 3D en móvil: se sustituye por la lista de capas.

## 5. Opciones técnicas y recomendación
| Opción | Android | iPhone | Coste | Veredicto |
|---|---|---|---|---|
| **PWA (web instalable) en `docs/movil/`** | Sí | Sí (instalada en la pantalla de inicio) | 0 € | **Recomendada**: un solo código; sin tienda ni revisión |
| Envoltorio Android (TWA/Capacitor) | Sí (APK propio o Play, $25 único) | — | 0-25 $ | Opcional más adelante, solo si hacen falta widgets |
| App nativa iPhone | — | Sí | $99/año + Mac/Xcode | **No compensa** |
- Notificaciones push web: en iPhone solo funcionan con la app instalada (iOS 16.4+); como ya hay Telegram, **no hace falta** montarlas.
- Si en el futuro se quiere un widget (Android), se puede hacer con un envoltorio; no es prioritario.

## 6. Cómo se construye sin tocar lo de ordenador
1. Un script **sin IA** (`scripts/construir_movil.py`) copia a `docs/movil/data.json` un resumen de los datos públicos ya existentes (recortado: lo que cabe en móvil). Corre en el mismo workflow que `paneles.yml`.
2. `docs/movil/` tiene su propio `index.html` + CSS + JS, sin Streamlit. El Cerebro de escritorio **no se modifica**.
3. `sw.js` guarda la última foto de datos: se ve sin conexión.
4. Buscador local en JS sobre títulos y resúmenes (como `buscar_informes.py`, sin red).

## 7. Fases y coste estimado (Sonnet; porcentaje de cuota semanal, orientativo)
| Fase | Qué | Estimación |
|---|---|---|
| F0 | Decidir pantallas, datos y estilo con maqueta en HTML | 1-2 % |
| F1 | Script de datos + workflow | 2 % |
| F2 | Pestañas Hoy y Mercado | 4 % |
| F3 | Agenda y Noticias | 3 % |
| F4 | Cerebro (voces, vídeos, informes) y buscador | 4 % |
| F5 | PWA instalable, caché sin conexión, prueba en iPhone y Android | 2 % |
| F6 (opcional) | Envoltorio Android | 2 % |

## 8. Riesgos
- **Datos de terceros publicados** en una página pública: los índices vienen de Yahoo Finance (no oficial): conviene mostrarlos como «[S] referencia» y valorar quitarlos de la versión pública; CoinGecko pide mencionar la fuente.
- **iPhone instalado** tiene rarezas de pantalla ([[ios-pantalla-completa-pwa]]): probar siempre en el iPhone de Joel.
- **Datos de pantalla pequeña:** más de 3-4 columnas no caben; hay que decidir qué se sacrifica.

## 9. Decisiones de Joel (25-oct-2026)
- **Móviles:** iPhone 15 y Samsung S21 Ultra (probar en ambos).
- **Pestañas:** 5 por ahora (Hoy, Mercado, Agenda, Noticias, Cerebro); se amplían más adelante si hace falta.
- **Estilo:** muy **visual y bonito**, con **animaciones**; **fácil de leer, de entender y de buscar**; la información principal en primera plana; nada de «pulsas y sale un montón de letra» como en la cartera actual.
- Sin contestar aún (se asumen los valores por defecto y se pueden cambiar): cinta de 4 digital assets (BTC, ETH, XRP, XLM) y 4 bolsas (S&P 500, Nasdaq, Euro Stoxx 50, Ibex 35); índices de Yahoo como «[S] referencia»; empezar la construcción tras el reinicio del 27-oct.

## 10. Maqueta (F0)
`research/maqueta-movil/` (no se publica): `construir.py` recoge los datos públicos ya existentes y genera `maqueta.html` (una sola página, 5 pestañas) para ver el diseño en el navegador con tamaño de móvil antes de construir la versión real en `docs/movil/`.
