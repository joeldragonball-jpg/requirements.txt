# PLANNING (autogenerado, no editar a mano) · 2026-11-05 21:38 UTC

Lo regenera `python scripts/construir_seguimiento.py` (el mismo que alimenta el Seguimiento del móvil y del PC), así que **Seguimiento y planning no pueden diverger**. `/research` sin argumento lee SOLO este archivo; con un ID, lee la fila de `research/COLA.md` y el prompt indicado aquí. Cuota: se mide con get_usage, no está aquí.

## Vista en 5 grupos (C131)
**Hoy (máx. 3):** Gemini Evento: Reino Unido: decisión del Banco de Inglaterra (Bank Rate 3,75 
**Periódicas (próxima):** W05 11-05 · W06 11-06 · W09 11-06 · W07 11-07 · W10 11-07 · W01 11-09 · W02 11-10 · W03 11-11 · W04 11-12 · W08 11-25
**Bloqueadas (16):** C79 (4-nov: AEAT OK. IGAE BOE y MENSUAL 12-24 OK con Ch) · C80B (Chrome no conectado; senate.gov y congress.gov blo) · C87 (Propuesta de la auditoría C81 (informes/research/2) · C88 (Propuesta de la auditoría C81 (informes/research/2) · C89 (Propuesta de la auditoría C81 (informes/research/2) · C90 (Propuesta de la auditoría C81 (informes/research/2) · …
**Parciales (19):** C30 falta: Fechas oficiales de EE. UU., Francia, Italia, Arge · C58 falta: Recuento oficial de las midterms; escaños por grup · C59 falta: pendiente (servicios públicos van en C61; función  · C61 falta: pendiente (pedido de Joel 30-oct; datos en explora · C68 falta: Resolver por qué el Portal paga a SE/Subsecretario · C69 falta: Cierre definitivo 2024, AEAT 2024 en la fuente y C · …
**Hechas en 7 días (36):** C129, C131, C133, C134, C136, C141, C32, C86, C91, C93, C94, C99, C100, C109, C110

## Hoy (jue 2026-11-05): solo lo casi obligatorio
- R00 apertura ✓ · cierre ✓ · racha 4 días
- Sin rutina fija hoy: elige por prioridad en las secciones de abajo.

## 🟣 Gemini del día (gratis, 1 consulta ligera de ~15 fuentes; Claude da el prompt, tú lo pegas en Gemini)
- Gemini del día: toca **Evento: Reino Unido: decisión del Banco de Inglaterra (Bank Rate 3,75 %)** · prompt `research/gemini/NOTICIAS-DIA.md` · ⏳ pendiente
- Norma: 1 consulta ligera al día (unas 15 fuentes), sin repetirla. Rutina G (C20): una rotación por día; si Gemini avisa de límite o llegas al 80 %, se para por hoy y se anota en «parada». La cuota se comparte con NotebookLM.
- Aviso de límite (antes del 2026-10-27): Una consulta de ~47 fuentes lanzada 2-3 veces agotó el límite; la cuota ya estaba gastada en NotebookLM.
- Aviso de límite (2026-10-27): Tras W03 Sudáfrica+Indonesia, Deep Research queda desactivado hasta las 04:00 (hora de Madrid) del 27-oct, con el uso general en ~4 %. Hizo 200+ búsquedas web aunque el prompt pedía máx. 15 fuentes: el tope del prompt no se respeta. Límite oficial de Deep Research sin confirmar; de momento, 1 Deep Research por ventana (reinicio 04:00).
- Aviso de límite (2026-10-31): Joel propone probar 2 Deep Research al dia (lleva ~7 % semanal con Pro alto). Se prueba unos dias; si Gemini avisa de limite, vuelta a 1. Anotar en sesiones cada lanzamiento y si hubo aviso.

## Rutinas W: lo que falta este periodo (sin día fijo; se hacen cuando haya hueco, de más atrasada a menos)
- W09 · Resumen semanal · ~1,5 % · cada viernes · último 2026-10-30 · `research/prompts/W09-*.md`
Hechas en este periodo: W01, W02, W03, W04, W05, W06, W07, W08, W10

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
- C120 ◐ en parte · Nivel B · Fichas manuales: Interior (criminalidad), DGT, siniestralidad laboral  · Sonnet M · ~~4 % · `Con Chrome, comprueba y documenta en research/ACCESOS-CHROME.md las fuentes de Interior, DGT, Trabajo y EFFIS; no saltes anti-bots; guarda lo verificado en espana-manual.json`
- C127 ◐ en parte · Tablero · Auditoría visual: Cifras clave más legibles y agrupadas, España ordena · Sonnet M · ~~3 % · `research/prompts/C127-auditoria-visual-tablero.md`
- C135 ◐ en parte · Países · Refrescar la historia con el bot de paneles, mini-serie bajo las 4 cifr · Sonnet M · ~~3 % · `Lee informes/research/2026-11-05-C133-paises-historia-mandatos.md (sección Pendiente). Añade scripts/indicadores_historia.py al flujo de actualizar_paneles sin API de Anthropic; en pPaises pon spark() de la serie bajo cada cifra grande; verifica en webs oficiales las fechas de mandato marcadas S en explorador/mandatos.json y súbelas a P solo si las lees.`
- C137 ◐ en parte · Países · Mandatos anteriores en el resto de países (como España): presidentes o  · Sonnet M · ~~4 % · `research/prompts/C137-mandatos-anteriores-paises.md`
- C138 ◐ en parte · Países · Cómo va la zona euro, la UE, las potencias y los BRICS: panel de bloque · Sonnet M · ~~4 % · `research/prompts/C138-bloques-euro-potencias-brics.md`
- C139 ◐ en parte · Países · Vigilar El Salvador y Argentina (indicadores, historia, mandatos) y, co · Sonnet L · ~~6 % · `research/prompts/C139-latam-el-salvador-argentina-venezuela-cuba.md`
- C140 ◐ en parte · Países · Leer en fuente oficial las fechas de mandato [S] (9 países) y las de Az · Sonnet S · ~~2 % · ``
- C24 · Centro · Fiscal y legal: confirmar que el vigilante del Federal Register manda u · Joel S · ~0 % · ``
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
- [VERIFICAR] Cloture CLARITY 49-50 en fuente oficial (senate.gov). → W05
- [VERIFICAR] Vigencia 2026 de la escala del ahorro (art. 66 LIRPF) y texto definitivo de los modelos 172/175/721 y de DAC8 en el BOE. → W05
- [VERIFICAR] Consulta DGT V0648-24 leída en petete; fiscalidad de tokens LP de AMM.
- [VERIFICAR] Integración de Chainlink CCIP en producción en SWIFT.

## Verificaciones pendientes con antigüedad (noticias de prensa sin contrastar y [VERIFICAR]; se anotan en eventos/verificados.json)
- [media] 2026-10-22 (14 d) · hutiES a Arabia Saudi
- [media] 2026-10-22 (14 d) · hutiES a Arabia Saudi
- [media] 2026-10-23 (13 d) · El futuro continuo del Brent cierra en $111,97, con máximo del día sobre $116.
- [media] 2026-10-23 (13 d) · Titulares de «114 $» y «117 $» por ataques a infraestructura saudí. Brent 113,08 → 111,7 $ (-1.2 %), WTI 99,29
- [media] 2026-10-25 (11 d) · [VERIFICAR] Precio y cierre de cada adquisición de Ripple sin precio publicado (Standard Custody, Palisade, So
- [media] 2026-10-25 (11 d) · [VERIFICAR] Integración de Chainlink CCIP en producción en SWIFT.
- [media] 2026-10-25 (11 d) · [VERIFICAR] Vigencia 2026 de la escala del ahorro (art. 66 LIRPF)
- [media] 2026-10-25 (11 d) · [VERIFICAR] Consulta DGT V0648-24 leída en petete
- … y 45 más en el Seguimiento

## Qué se está quedando viejo (frescura)
- 🔴 Radar regulatorio: Fechas previstas ya pasadas sin actualizar (4) → W03 · BR/politica; RU/stablecoins; AE/politica; BRICS/ley_marco
- 🔴 Voces: Voces sin confirmar (8) → W06 · 4 llevan más de 14 días
- 🟡 Radar regulatorio: Celdas sin dato (30) → W03 · Más huecos: EG 5, ET 4, UK 4, ZA 3, ID 3
- 🟡 Países (política): Fichas con datos de más de 90 días o sin fecha (12) → W11 · China, Brasil, Sudáfrica, Indonesia, Egipto, Etiopía

## Bots con problema
- Verificación mensual, Paneles de datos

## Calendario: ya pasaron (10 días) y qué falta decidir
- 2026-10-27 · Reunión de la Fed (FOMC) (alto) → ✓ revisado (hecho)
- 2026-10-28 · Reunión del BCE (alto) → ✓ revisado (hecho)
- 2026-10-28 · DTCC: lanzamiento del servicio de tokenización de DTC (hecho el 28-oct (medio) → ✓ revisado (hecho)
- 2026-10-28 · Canadá: decisión del Banco de Canadá sobre el tipo oficial (medio) → ✓ revisado (hecho)
- 2026-10-29 · PIB de EE. UU. (3T, avance) y gasto en consumo PCE de septiembre (alto) → ✓ revisado (hecho)
- 2026-10-29 · Reunión del Banco de Japón (alto) → ✓ cubierto por W01 del 2026-11-02
- 2026-10-30 · Brasil: último día para que los proveedores cripto existentes pidan au (medio) → ✓ cubierto por W01 del 2026-11-02
- 2026-11-01 · OPEP+ (7 países): reunión mensual (medio) → ✓ cubierto por W10 del 2026-11-02
- 2026-11-03 · EE. UU.: elecciones de mitad de mandato (alto) → ✓ revisado (hecho)
- 2026-11-03 · Australia: decisión del RBA sobre el tipo de efectivo (medio) → ✓ revisado (hecho)
- 2026-11-04 · Tesoro de EE. UU.: anuncio trimestral de refinanciación (medio) → ⏳ SIN research: decidir (EV)
- 2026-11-04 · Zona euro: IPCA adelantado de octubre (Eurostat) (medio) → ⏳ SIN research: decidir (EV)
Para los «SIN research»: pide `/research EV <fecha> <título>`; usa `research/prompts/EV-post-evento.md`. Descartar o marcar hecho: `eventos/revisados.json`.

## Calendario: próximos 14 días de impacto y qué los cubre
- 2026-11-05 · Reino Unido: decisión del Banco de Inglaterra (Bank Rate 3,7 (alto) → cubre W01 (Tipos de interés)
- 2026-11-06 · Empleo EE. UU. (informe de octubre) (alto) → cubre W01 (Datos macro y tipos)
- 2026-11-06 · Brasil: bancos y entidades de pago no podrán operar con prov (medio) → cubre W03 (Regulación por países)
- 2026-11-10 · Inflación EE. UU. (IPC de octubre) (alto) → cubre W01 (Datos macro y tipos)
- 2026-11-10 · EIA: perspectivas de energía a corto plazo (STEO) (medio) → cubre W10 (Energía y geopolítica)
- 2026-11-11 · SEC: plazo sobre opciones de ETFs cripto (SR-ISE-2026-42) (medio) → cubre W04 (ETF y flujos)
- 2026-11-11 · Corea: fin de comentarios de la FSC sobre tokenización de va (medio) → sin rutina: valorar research EV
- 2026-11-11 · OPEP: informe mensual del mercado petrolero (noviembre) (medio) → cubre W10 (Energía y geopolítica)
- 2026-11-13 · AIE: informe mensual del mercado petrolero (noviembre) (medio) → cubre W10 (Energía y geopolítica)
- 2026-11-16 · Plazo del 13F del 3T (quién tiene ETF de XRP/XLM) (medio) → cubre W04 (ETF y flujos)
- 2026-11-18→11-19 · APEC en Shenzhen: cumbre de líderes (medio) → cubre W03 (Regulación por países)
- 2026-11-18 · Reino Unido: IPC de octubre (ONS) (medio) → cubre W01 (Datos macro y tipos)

## Predicciones que vencen en 14 días
- ninguna

## Próximas fechas clave
- 2026-11-05 · Reino Unido: decisión del Banco de Inglaterra (Bank Rate 3,75 %)
- 2026-11-06 · Empleo EE. UU. (informe de octubre)
- 2026-11-06 · Brasil: bancos y entidades de pago no podrán operar con proveedores cripto no autorizados 
- 2026-11-10 · Inflación EE. UU. (IPC de octubre)
- 2026-11-10 · EIA: perspectivas de energía a corto plazo (STEO)
- 2026-11-11 · Corea: fin de comentarios de la FSC sobre tokenización de valores
- 2026-11-13 · AIE: informe mensual del mercado petrolero (noviembre)
