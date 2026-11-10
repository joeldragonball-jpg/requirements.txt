# PLANNING (autogenerado, no editar a mano) · 2026-11-10 03:31 UTC

Lo regenera `python scripts/construir_seguimiento.py` (el mismo que alimenta el Seguimiento del móvil y del PC), así que **Seguimiento y planning no pueden diverger**. `/research` sin argumento lee SOLO este archivo; con un ID, lee la fila de `research/COLA.md` y el prompt indicado aquí. Cuota: se mide con get_usage, no está aquí.

## Vista en 5 grupos (C131)
**Hoy (máx. 3):** R00 Apertura del día · Gemini Evento: Inflación EE. UU. (IPC de octubre)
**Periódicas (próxima):** W02 11-10 · W03 11-11 · W04 11-12 · W05 11-12 · W06 11-13 · W09 11-13 · W10 11-14 · W01 11-16 · W08 11-25 · W07 12-05
**Bloqueadas (6):** C79 (4-nov: AEAT OK. IGAE BOE y MENSUAL 12-24 OK con Ch) · C80B (Chrome no conectado; senate.gov y congress.gov blo) · C137 (Chrome para leer fechas oficiales) · C139 (Decidir con Joel si se añaden como países nuevos a) · C140 (Chrome conectado) · C235 (Joel pasa podcasts, canales y personas que sigue)
**Parciales (35):** C30 falta: Fechas oficiales de EE. UU., Francia, Italia, Arge · C58 falta: Recuento oficial de las midterms; escaños por grup · C59 falta: pendiente (servicios públicos van en C61; función  · C61 falta: pendiente (pedido de Joel 30-oct; datos en explora · C68 falta: Resolver por qué el Portal paga a SE/Subsecretario · C69 falta: Cierre definitivo 2024, AEAT 2024 en la fuente y C · …
**Hechas en 7 días (41):** C147, C150, C151, C152, C153, C159, C160, C145, C129, C131, C133, C134, C136, C141, C32

## Hoy (mar 2026-11-10): solo lo casi obligatorio
- R00 apertura ⏳ pendiente · cierre ⏳ pendiente (desde las 22:00, cierre de EE. UU.) · racha 2 días
- Sin rutina fija hoy: elige por prioridad en las secciones de abajo.

## 🟣 Gemini del día (gratis, 1 consulta ligera de ~15 fuentes; Claude da el prompt, tú lo pegas en Gemini)
- Gemini del día: toca **Evento: Inflación EE. UU. (IPC de octubre)** · prompt `research/gemini/NOTICIAS-DIA.md` · ⏳ pendiente
- Norma: 1 consulta ligera al día (unas 15 fuentes), sin repetirla. Rutina G (C20): una rotación por día; si Gemini avisa de límite o llegas al 80 %, se para por hoy y se anota en «parada». La cuota se comparte con NotebookLM.
- Aviso de límite (antes del 2026-10-27): Una consulta de ~47 fuentes lanzada 2-3 veces agotó el límite; la cuota ya estaba gastada en NotebookLM.
- Aviso de límite (2026-10-27): Tras W03 Sudáfrica+Indonesia, Deep Research queda desactivado hasta las 04:00 (hora de Madrid) del 27-oct, con el uso general en ~4 %. Hizo 200+ búsquedas web aunque el prompt pedía máx. 15 fuentes: el tope del prompt no se respeta. Límite oficial de Deep Research sin confirmar; de momento, 1 Deep Research por ventana (reinicio 04:00).
- Aviso de límite (2026-10-31): Joel propone probar 2 Deep Research al dia (lleva ~7 % semanal con Pro alto). Se prueba unos dias; si Gemini avisa de limite, vuelta a 1. Anotar en sesiones cada lanzamiento y si hubo aviso.

## Rutinas W: lo que falta este periodo (sin día fijo; se hacen cuando haya hueco, de más atrasada a menos)
Hechas en este periodo: W01, W02, W03, W04, W05, W06, W07, W08, W09, W10

## Research nuevo pendiente (por sección)
**Centro y revisión del cerebro (C)**
- C101 ◐ en parte · Centro · Endurecer workflows: permisos mínimos, requirements con hashes, Actions · Sonnet S · ~~1 % · ``
- C102 · Centro · Inventario de secretos y tokens fuera del repo (plantilla en privado/;  · Sonnet S · ~~1 % · ``
- C103 · Centro · Auditar el Worker de votos (Joel pega el código sin secretos) · Sonnet S · ~~1 % · ``
- C105 · Centro · Copias y recuperación: git bundle semanal y ensayo de restauración · Sonnet S · ~~1 % · ``
- C106 · Centro · Bots frecuentes al Worker (requisito si el repo pasa a privado) · Sonnet M · ~~3 % · ``
- C107 · Centro · Qué NO construir: ver qué hacen ya gratis OpenBB, Koyfin, TradingView y · Sonnet M · ~~3 % · ``
- C108 ◐ en parte · Centro · Criterios de medición y relleno de las 58 predicciones · Sonnet M · ~~3 % · ``
- C111 · Nivel C · Electricidad Europa por zonas con ENTSO-E · Sonnet S · ~~2 % · `Tras recibir el token de ENTSO-E como secreto, añade las zonas ES/FR/DE/IT/PT a leer_electricidad() sin mostrar el token`
- C117 · Nivel C · RAM/DRAM y centros de datos: ficha manual con fuentes [S] y proxy MU · Sonnet M · ~~4 % · `Busca solo fuentes públicas sobre precios DRAM/NAND y consumo eléctrico de centros de datos (IEA, EIA, comunicados); guarda en explorador/chips-manual.json con nivel S y fecha; marca [ESPECULACIÓN] en ciclos`
- C118 · Nivel C · Fertilizantes y agua por zonas: Pink Sheet BM e INE · Sonnet M · ~~4 % · `Con OK de Joel para descargar el xlsx del Pink Sheet del Banco Mundial, extrae urea/amoníaco/potasa/DAP; busca precio del agua por CCAA en INE/AEAS y marca [VERIFICAR] lo no oficial`
- C127 ◐ en parte · Tablero · Auditoría visual: Cifras clave más legibles y agrupadas, España ordena · Sonnet M · ~~3 % · `research/prompts/C127-auditoria-visual-tablero.md`
- C135 ◐ en parte · Países · Refrescar la historia con el bot de paneles, mini-serie bajo las 4 cifr · Sonnet M · ~~3 % · `Lee informes/research/2026-11-05-C133-paises-historia-mandatos.md (sección Pendiente). Añade scripts/indicadores_historia.py al flujo de actualizar_paneles sin API de Anthropic; en pPaises pon spark() de la serie bajo cada cifra grande; verifica en webs oficiales las fechas de mandato marcadas S en explorador/mandatos.json y súbelas a P solo si las lees.`
- C137 ◐ en parte · Países · Mandatos anteriores en el resto de países (como España): presidentes o  · Sonnet M · ~~4 % · `research/prompts/C137-mandatos-anteriores-paises.md`
- C138 ◐ en parte · Países · Cómo va la zona euro, la UE, las potencias y los BRICS: panel de bloque · Sonnet M · ~~4 % · `research/prompts/C138-bloques-euro-potencias-brics.md`
- C139 ◐ en parte · Países · Vigilar El Salvador y Argentina (indicadores, historia, mandatos) y, co · Sonnet L · ~~6 % · `research/prompts/C139-latam-el-salvador-argentina-venezuela-cuba.md`
- C140 ◐ en parte · Países · Leer en fuente oficial las fechas de mandato [S] (9 países) y las de Az · Sonnet S · ~~2 % · ``
- C144 ◐ en parte · Centro · Research a fondo: APIs y datos gratis (GitHub, Reddit, documentación of · Sonnet L · ~~6 % · `research/prompts/C144-apis-gratis-automatizar.md`
- C162 ◐ en parte · Órbita · Niveles y fallos legibles: etiquetar los 8 k vacíos de capas[].xrp, exp · Sonnet M · ~~2 % · `Etiqueta los k vacíos de capas[].xrp en datos.json (con la fuente que lo sostiene, no a ojo), explica en una línea los fallos de paneles.json y unifica la leyenda de niveles en un pie común`
- C172 · Órbita y móvil · Pendientes de la auditoría visual: móvil con tema oscuro por de · Sonnet S · ~~2 % · `Lee informes/research/2026-11-07-auditoria-visual-tablet-pc.md (sección Pendientes). Fuerza el tema oscuro por defecto en docs/movil/index.html (líneas con prefers-color-scheme) salvo elección manual del usuario; matriz país×tema como lista a 375 px; sombra o indicador de scroll horizontal en tablas anchas; oculta el filtro País en «Mis activos»; verifica rutas del service worker en GitHub Pages`
- C173 ◐ en parte · Centro · Verificar noticias pendientes de prioridad alta y de más de 14 días (7- · Sonnet S · ~~3 % · ``
- C176 ◐ en parte · Centro · Verificar prensa 4-6 nov (7 noticias) · Sonnet S · ~~1 % · ``
- C179 ◐ en parte · Países · W11 refresco de 6 fichas políticas (China, Brasil, Sudáfrica, Indonesia · Sonnet S · ~~2 % · ``
- C181 · Móvil · Mercado: separar divisas por tipo (pares con euro, dólar, refugio, emerg · Opus M · ~~3 % · ``
- C186 · Research con Gemini (manual): qué muestran los mejores paneles de inversor parti · Sonnet S · ~~2 % · ``
- C189 · Quitar duplicados en Verificaciones pendientes y poner «hace N d» junto a cada c · Sonnet S · ~<0,3 % · ``
- C190 · Corregir «1 días de racha» y mover racha y % de plan a Más · Sonnet S · ~<0,2 % · ``
- C191 · Mostrar XRP/XLM una sola vez en Hoy · Sonnet S · ~<0,2 % · ``
- C193 · Separar «Divisas y tipos» del Mercado en Divisas, Tipos oficiales y Bonos · Sonnet S · ~<0,3 % · ``
- C194 · Mover «Frescura de los datos» bajo los precios en Mercado y dejar resumen · Sonnet S · ~<0,2 % · ``
- C195 · Etiqueta común de fecha del dato en Energía y Alimentos · Sonnet S · ~<0,2 % · ``
- C196 · Aviso ámbar a 7 días en RWA manual; anotar que congress.gov sí cargó con Chrome  · Sonnet S · ~<0,2 % · ``
- C203 · Fichas por activo (XRP, XLM, BTC, oro, ETF mundial) con fuente, nivel, hechos y  · Sonnet M · ~~2 % · ``
- C205 · Vista de tesis privada en privado/ con evidencia a favor, en contra y sin dato · Opus L · ~~5 % · ``
- C206 · Alertas por umbral y por evento (Telegram) para datos en rojo, tipos y noticias  · Opus L · ~~3 % · ``
- C208 · Capa «Mi cartera» sin importes con el importador CSV · Opus L · ~~4 % · ``
- C209 · Modo familia: vista reducida sin racha ni IA · Opus L · ~~2 % · ``
- C210 · Capas nuevas: flujos de ETF de XRP/XLM, stablecoins, vivienda y combustibles UE · Opus L · ~~4 % · ``
- C213 · Órbita: enlaces entre datos (Calendario, Línea de tiempo, Matriz, Voces y ficha  · Sonnet M · ~~1,5 % · ``
- C217 · Órbita: comparador de países como vista (2-4 países, mismo periodo) · Opus L · ~~3 % · ``
- C218 · Órbita: comparador de capas lado a lado · Sonnet M · ~~2 % · ``
- C219 · Órbita: modo foco en Resumen (solo lo que cambió y lo que caduca) · Sonnet M · ~~0,8 % · ``
- C220 · Órbita: Calendario con filtros por capa, país y mi cartera, y exportar .ics · Sonnet M · ~~0,8 % · ``
- C221 · Órbita: glosario flotante y definición en cada cifra · Sonnet M · ~~1 % · ``
- C222 · Órbita: pestaña Mercado con divisas por tipo, hora real por dato y segunda fuent · Sonnet M · ~~2 % · ``
- C223 · Órbita: rendimiento con muchos datos (carga por pestaña, listas virtualizadas) · Opus L · ~~3 % · ``
- C225 ◐ en parte · Research de noticias más fuerte: grandes potencias y España, conflictos y guerra · Sonnet L · ~~5 % · ``
- C229 ◐ en parte · Órbita · España: pack macro (IPC desglosado, EPA, afiliación, salarios/SMI y Eur · Sonnet L · ~~4 % · ``
- C230 ◐ en parte · Órbita · España: vivienda (precio, alquiler, esfuerzo por CCAA), deuda autonómic · Sonnet L · ~~4 % · ``
- C231 ◐ en parte · Órbita · España: pensiones (gasto, déficit contributivo, fondo) y demografía (na · Sonnet M · ~~3 % · ``
- C232 ◐ en parte · Órbita · España: fiscalidad cripto (modelos 172/173/721), MiCA y CASP autorizado · Opus M · ~~3 % · ``
- C233 ◐ en parte · Órbita · España: energía (precio eléctrico OMIE/REE, combustibles vs UE, gas y d · Sonnet M · ~~3 % · ``
- C235 · Voces de otros ámbitos (bancos centrales, energía, política, economía) fichadas  · Opus M · ~~3 % · ``
- C236 ◐ en parte · IPC de EE. UU.: etiquetar «desestacionalizado / sin desestacionalizar» en móvil  · Sonnet S · ~~0,5 % · ``
- C237 ◐ en parte · Revisar research/CRUCE-HECHOS.md: decidir qué hechos P van a la Línea de tiempo, · Opus M · ~~3 % · ``
- C238 ◐ en parte · Órbita · España: leyes nuevas y modificaciones (BOE, Congreso): estado, vigor y  · Sonnet L · ~~5 % · `research/prompts/C238-espana-leyes-boe.md`
- C239 ◐ en parte · Órbita · España: investigaciones y fondos públicos (Adif, Ministerio de Transpor · Sonnet L · ~~5 % · `research/prompts/C239-espana-investigaciones-fondos.md`
- C24 · Centro · Fiscal y legal: confirmar que el vigilante del Federal Register manda u · Joel S · ~0 % · ``
- C240 ◐ en parte · Formato de cifras: unidad y escala explícitas (M€, mil M€), punto de miles y com · Sonnet M · ~~2 % · `research/prompts/C240-formato-cifras-unidades.md`
- C241 · Órbita · España: «a dónde va el dinero» (contratación pública PLACSP y subvencio · Fable L · ~~6 % · `research/LANZAR-FABLE-ESPANA.md`
- C242 · Órbita · España: Congreso, partidos y altos cargos (votaciones, iniciativas, fin · Fable L · ~~5 % · `research/LANZAR-FABLE-ESPANA.md`
- C243 · Órbita · España: empresas públicas (SEPI, Adif, Renfe, Correos…) y comparador de · Fable L · ~~5 % · `research/LANZAR-FABLE-ESPANA.md`
- C245 ◐ en parte · Órbita · España: empleados de órganos constitucionales (Cortes, T. Cuentas, CGPJ · Sonnet S · ~~2 % · `Buscar la plantilla (nº de empleados) de Cortes Generales, Tribunal de Cuentas, CGPJ, Tribunal Constitucional, Consejo de Estado y Casa de Su Majestad el Rey en sus portales de transparencia/memorias/RPT y en el anexo de personal de los PGE; completar explorador/espana-empleados.json con fuente, fecha y nivel (P solo si se lee la fuente oficial; puestos presupuestados ≠ personas: [VERIFICAR]). Las 9 partidas de gasto sin plantilla (Deuda, Clases Pasivas, UE, entes territoriales, etc.) quedan null.`
- C30 ◐ en parte · Centro · Política y elecciones por país · Sonnet M · ~3 % · `research/prompts/C30-politica-elecciones.md`
- C31 · Centro · Inflación (IPC) por país · Sonnet M · ~3 % · `research/prompts/C31-inflacion.md`
- C36 · Centro · Rutina de noticias manuales (Claude y Gemini) · Sonnet M · ~3 % · `research/prompts/C36-rutina-noticias-manual.md`
- C39 · Centro · Volcar al panel lo ya investigado sin movimiento (países T07-T16 y W03E · Sonnet S · ~2 % · `research/prompts/C39-volcado-orbita.md`
- C42 · Centro · Rendimientos y colateral: staking, lending CeFi/DeFi, AMM XRPL/Stellar, · Sonnet M · ~3 % · `research/prompts/C42-rendimientos-colateral.md`
- C58 ◐ en parte · Centro · Fichas políticas de 12 países (UE: España, Alemania, Francia, Italia, P · Sonnet M · ~3 % · `research/prompts/C58-fichas-politicas-paises.md`
- C59 ◐ en parte · Centro · Indicadores económicos por país (IPC, paro total y juvenil, PIB, deuda, · Sonnet M · ~3 % · `research/prompts/C59-indicadores-sociales-economicos.md`
- C61 ◐ en parte · Centro · Servicios públicos y estabilidad social por país: sanidad (gasto, hitos · Sonnet M · ~3 % · `research/prompts/C61-servicios-publicos-estabilidad.md`
- C68 ◐ en parte · Centro · España · Sueldos de cada cargo político (presidente, ministros, secreta · Sonnet L · ~~6 % · `research/prompts/C68-sueldos-por-persona-politicos.md`
- C68B ◐ en parte · Centro · España · Cuadrar sueldos de secretarios de Estado, subsecretarios y dir · Sonnet M · ~~3 % · `research/prompts/C68B-cuadrar-sueldos-segundo-nivel.md`
- C69 ◐ en parte · Centro · España · España: cada partida con 2024 y 2025 y su variación (IGAE 2024 · Sonnet L · ~~6 % · `research/prompts/C69-espana-2024-vs-2025.md`
- C77 ◐ en parte · Centro · España: gasto público y deuda por ministerio, comunidad, municipio y co · Opus L · ~ · ``
- C79 · Centro · España: PDF del Tesoro, AIReF, IGAE y AEAT (requieren OK de descarga),  · Sonnet M · ~ · ``
- C80B ◐ en parte · Centro · Fuentes Fase 2: catálogo con estado (API/Chrome/bloqueada/manual) y cad · Sonnet M · ~ · ``
- C87 · Centro · Separar público/privado: auditoría del repo público y plan de repo priv · Opus M · ~~3 % · ``
- C88 · Centro · Endurecer el Worker de Cloudflare y los bots de pago: token fine-graine · Sonnet S · ~~1 % · ``
- C89 · Centro · Endurecer candado() de app.py: cerrado por defecto, cookie/sesión en ve · Sonnet S · ~~2 % · ``
- C90 · Centro · Revisión XSS: texto externo inyectado como HTML en docs/movil/index.htm · Sonnet S · ~~2 % · ``
- C92 ◐ en parte · Centro · Medición: normalizar predicciones (fecha límite, fuente_id), script de  · Sonnet M · ~~3 % · ``
- C95 · Centro · Plan de salida a producción para la familia: auth, hosting, copias, avi · Opus M · ~~3 % · ``
- C96 · Centro · Consulta regulatoria de monetización [VERIFICAR con asesor/CNMV]: pregu · Sonnet S · ~~1 % · ``
**Países y temas (T)** · detalle en `research/COLA-TEMAS-GEMINI.md`
- T25 · Tema libre
**Deuda y bonos (D)** · detalle en `research/COLA-DEUDA-BONOS.md`
- D06 · (parcial) Bancos y deuda: exposición soberana de 116 bancos europeos (
**Otros research (R)** · detalle en `research/COLA.md`
- R17 · Resumen semanal de 1 página (para imprimir)
- R36 · PROFUNDO: Segunda pasada con los PDFs que haya en research/fuentes/ (R
- R39 · Auditoría final corta (18-19 oct): solo lo escrito después de R31/R38 

## Auditorías abiertas
- A1 (Media): Abierto: voces.json lo está editando otra sesión (W06); propuesta: v002→cumplido con la nota del 28-oct; v062→
- A2 (Media): Abierto: propuesta, mostrar «P + novedades S» o añadir url a HK ETF
- A3 (Media): Parcial: antes faltaban 23. Abierto: 9 celdas
- A4 (Baja): Abierto
- A5 (Media): Abierto: propuesta, 2-3 canales o analistas críticos o neutrales en el próximo lote de vídeos
- A7 (Media): Abierto
- A8 (Baja): Abierto solo v062
- A9 (Baja): Cerrado (W07)
- Auditoría mensual W08: última semana del mes (miércoles)

## Verificaciones abiertas ([VERIFICAR]; las cierra W05 o W08)
- [VERIFICAR] Precio y cierre de cada adquisición de Ripple sin precio publicado (Standard Custody, Palisade, Solvexia) y cierre de BC Payments Australi
- [VERIFICAR] Vigencia 2026 de la escala del ahorro (art. 66 LIRPF) y texto definitivo de los modelos 172/175/721 y de DAC8 en el BOE. → W05
- [VERIFICAR] Consulta DGT V0648-24 leída en petete; fiscalidad de tokens LP de AMM.
- [VERIFICAR] Integración de Chainlink CCIP en producción en SWIFT.

## Verificaciones pendientes con antigüedad (noticias de prensa sin contrastar y [VERIFICAR]; se anotan en eventos/verificados.json)
- [alta] 2026-11-07 (3 d) · Incendio de dos petroleros en el estrecho de Ormuz.
- [alta] 2026-11-08 (2 d) · Irak pacta con EE. UU. poder exportar crudo por Ormuz.
- [alta] 2026-11-09 (1 d) · El Brent cae más de un 3 % y baja de 95 $.
- [alta] 2026-11-09 (1 d) · El Brent cae casi un 5 % hasta 93,72 $.
- [media] 2026-10-12 (29 d) · Mayor lote de listados de sanciones contra Rusia hasta la fecha (~1.569 personas y entidades); el 20.º paquete
- [media] 2026-10-13 (28 d) · Inflación de septiembre: 1,9 % mensual (agosto 1,7 %), 23,6 % acumulada en 2026 y 33,4 % interanual. El FMI (2
- [media] 2026-10-22 (19 d) · hutiES a Arabia Saudi
- [media] 2026-10-22 (19 d) · hutiES a Arabia Saudi
- … y 76 más en el Seguimiento

## Qué se está quedando viejo (frescura)
- 🔴 Radar regulatorio: Fechas previstas ya pasadas sin actualizar (3) → W03 · BR/politica; AE/politica; BRICS/ley_marco
- 🟡 Radar regulatorio: Celdas sin dato (29) → W03 · Más huecos: EG 5, ES 5, ET 4, IN 2, BRICS 2
- 🟡 Voces: Voces sin confirmar (4) → W06 · 3 llevan más de 14 días

## Bots con problema
- Verificación mensual

## Calendario: ya pasaron (10 días) y qué falta decidir
- 2026-11-01 · OPEP+ (7 países): reunión mensual (medio) → ✓ cubierto por W10 del 2026-11-10
- 2026-11-03 · EE. UU.: elecciones de mitad de mandato (alto) → ✓ revisado (hecho)
- 2026-11-03 · Australia: decisión del RBA sobre el tipo de efectivo (medio) → ✓ revisado (hecho)
- 2026-11-04 · Tesoro de EE. UU.: anuncio trimestral de refinanciación (medio) → ✓ cubierto por W02 del 2026-11-10
- 2026-11-04 · Zona euro: IPCA adelantado de octubre (Eurostat) (medio) → ✓ cubierto por W01 del 2026-11-10
- 2026-11-05 · Reino Unido: decisión del Banco de Inglaterra (Bank Rate 3,75 % → 4,00 (alto) → ✓ cubierto por W01 del 2026-11-10
- 2026-11-06 · Empleo EE. UU. (informe de octubre) (alto) → ✓ cubierto por W01 del 2026-11-10
- 2026-11-06 · Brasil: bancos y entidades de pago no podrán operar con proveedores cr (medio) → ✓ cubierto por W03 del 2026-11-10
Para los «SIN research»: pide `/research EV <fecha> <título>`; usa `research/prompts/EV-post-evento.md`. Descartar o marcar hecho: `eventos/revisados.json`.

## Calendario: próximos 14 días de impacto y qué los cubre
- 2026-11-10 · Inflación EE. UU. (IPC de octubre) (alto) → cubre W01 (Datos macro y tipos)
- 2026-11-10 · EIA: perspectivas de energía a corto plazo (STEO) (medio) → cubre W10 (Energía y geopolítica)
- 2026-11-10→11-11 · Abu Dabi: conversaciones trilaterales EE. UU.–Ucrania–Rusia (medio) → sin rutina: valorar research EV
- 2026-11-11 · SEC: plazo sobre opciones de ETFs cripto (SR-ISE-2026-42) (medio) → cubre W04 (ETF y flujos)
- 2026-11-11 · Corea: fin de comentarios de la FSC sobre tokenización de va (medio) → sin rutina: valorar research EV
- 2026-11-11 · OPEP: informe mensual del mercado petrolero (noviembre) (medio) → cubre W10 (Energía y geopolítica)
- 2026-11-13 · AIE: informe mensual del mercado petrolero (noviembre) (medio) → cubre W10 (Energía y geopolítica)
- 2026-11-13 · España: IPC definitivo de octubre (INE) (medio) → cubre W01 (Datos macro y tipos)
- 2026-11-16 · Plazo del 13F del 3T (quién tiene ETF de XRP/XLM) (medio) → cubre W04 (ETF y flujos)
- 2026-11-18→11-19 · APEC en Shenzhen: cumbre de líderes (medio) → cubre W03 (Regulación por países)
- 2026-11-18 · Reino Unido: IPC de octubre (ONS) (medio) → cubre W01 (Datos macro y tipos)
- 2026-11-18 · Zona euro: IPCA definitivo de octubre (Eurostat) (medio) → cubre W01 (Datos macro y tipos)

## Predicciones que vencen en 14 días
- ninguna

## Próximas fechas clave
- 2026-11-10 · Inflación EE. UU. (IPC de octubre)
- 2026-11-10 · EIA: perspectivas de energía a corto plazo (STEO)
- 2026-11-10 · Abu Dabi: conversaciones trilaterales EE. UU.–Ucrania–Rusia
- 2026-11-11 · Corea: fin de comentarios de la FSC sobre tokenización de valores
- 2026-11-13 · AIE: informe mensual del mercado petrolero (noviembre)
- 2026-11-16 · Plazo del 13F del 3T (quién tiene ETF de XRP/XLM)
- 2026-11-18 · APEC en Shenzhen: cumbre de líderes
