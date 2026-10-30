# PLANNING (autogenerado, no editar a mano) · 2026-10-30 15:27 UTC

Lo regenera `python scripts/construir_seguimiento.py` (el mismo que alimenta el Seguimiento del móvil y del PC), así que **Seguimiento y planning no pueden diverger**. `/research` sin argumento lee SOLO este archivo; con un ID, lee la fila de `research/COLA.md` y el prompt indicado aquí. Cuota: se mide con get_usage, no está aquí.

## Hoy (vie 2026-10-30): solo lo casi obligatorio
- R00 apertura ✓ · cierre ⏳ pendiente (desde las 22:00, cierre de EE. UU.) · racha 14 días
- Fija de hoy (viernes: resumen semanal): **W09 Resumen semanal** (~1,5 %) · último 2026-10-25 · `research/prompts/W09-*.md`

## 🟣 Gemini del día (gratis, 1 consulta ligera de ~15 fuentes; Claude da el prompt, tú lo pegas en Gemini)
- Gemini del día: toca **Bulos y desmentidos de la semana** · prompt `research/gemini/NOTICIAS-DIA.md` · ⏳ pendiente
- Norma: 1 consulta ligera al día (unas 15 fuentes), sin repetirla. Rutina G (C20): una rotación por día; si Gemini avisa de límite o llegas al 80 %, se para por hoy y se anota en «parada». La cuota se comparte con NotebookLM.
- Aviso de límite (antes del 2026-10-27): Una consulta de ~47 fuentes lanzada 2-3 veces agotó el límite; la cuota ya estaba gastada en NotebookLM.
- Aviso de límite (2026-10-27): Tras W03 Sudáfrica+Indonesia, Deep Research queda desactivado hasta las 04:00 (hora de Madrid) del 27-oct, con el uso general en ~4 %. Hizo 200+ búsquedas web aunque el prompt pedía máx. 15 fuentes: el tope del prompt no se respeta. Límite oficial de Deep Research sin confirmar; de momento, 1 Deep Research por ventana (reinicio 04:00).

## Rutinas W: lo que falta este periodo (sin día fijo; se hacen cuando haya hueco, de más atrasada a menos)
- W09 · Resumen semanal · ~1,5 % · cada viernes · último 2026-10-25 · `research/prompts/W09-*.md`
- W10 · Energía y geopolítica · ~2 % · fin de semana · último 2026-10-25 · `research/prompts/W10-*.md`
Hechas en este periodo: W01, W02, W03, W04, W05, W06, W07, W08

## Research nuevo pendiente (por sección)
**Centro y revisión del cerebro (C)**
- C24 · Centro · Fiscal y legal: confirmar que el vigilante del Federal Register manda u · Joel S · ~0 % · ``
- C30 ◐ en parte · Centro · Política y elecciones por país · Sonnet M · ~3 % · `research/prompts/C30-politica-elecciones.md`
- C31 · Centro · Inflación (IPC) por país · Sonnet M · ~3 % · `research/prompts/C31-inflacion.md`
- C32 · Centro · Móvil: pantalla principal de precios, tipos, petróleo e inflación + aud · Sonnet M · ~3 % · `research/prompts/C32-movil-principal.md`
- C36 · Centro · Rutina de noticias manuales (Claude y Gemini) · Sonnet M · ~3 % · `research/prompts/C36-rutina-noticias-manual.md`
- C39 · Centro · Volcar al panel lo ya investigado sin movimiento (países T07-T16 y W03E · Sonnet S · ~2 % · `research/prompts/C39-volcado-orbita.md`
- C42 · Centro · Rendimientos y colateral: staking, lending CeFi/DeFi, AMM XRPL/Stellar, · Sonnet M · ~3 % · `research/prompts/C42-rendimientos-colateral.md`
- C58 ◐ en parte · Centro · Fichas políticas de 12 países (UE: España, Alemania, Francia, Italia, P · Sonnet M · ~3 % · `research/prompts/C58-fichas-politicas-paises.md`
- C59 ◐ en parte · Centro · Indicadores económicos por país (IPC, paro total y juvenil, PIB, deuda, · Sonnet M · ~3 % · `research/prompts/C59-indicadores-sociales-economicos.md`
- C61 ◐ en parte · Centro · Servicios públicos y estabilidad social por país: sanidad (gasto, hitos · Sonnet M · ~3 % · `research/prompts/C61-servicios-publicos-estabilidad.md`
**Países y temas (T)** · detalle en `research/COLA-TEMAS-GEMINI.md`
- T25 · Tema libre
**Deuda y bonos (D)** · detalle en `research/COLA-DEUDA-BONOS.md`
- D06 · (parcial) Bancos y deuda: exposición soberana de 116 bancos europeos (
**Otros research (R)** · detalle en `research/COLA.md`
- R17 · Resumen semanal de 1 página (para imprimir)
- R36 · PROFUNDO: Segunda pasada con los PDFs que haya en research/fuentes/ (R
- R39 · Auditoría final corta (18-19 oct): solo lo escrito después de R31/R38 
**Pasadas puntuales de rutinas (W)** · detalle en `research/COLA.md`
- W11 · Política y elecciones: revisión semanal corta (fechas oficiales, encue

## Auditorías abiertas
- C13 (Media): Cero enlaces: el campo fuente solo vale P/S/VERIFICAR. No hay forma de pulsar y llegar a la fuente. (voces.jso
- Auditoría mensual W08: última semana del mes (miércoles)

## Verificaciones abiertas ([VERIFICAR]; las cierra W05 o W08)
- [VERIFICAR] Texto literal de la **sección 404** de CLARITY en congress.gov (hoy solo [S]). → W05
- [VERIFICAR] Precio y cierre de cada adquisición de Ripple sin precio publicado (Standard Custody, Palisade, Solvexia) y cierre de BC Payments Australi
- [VERIFICAR] Cloture CLARITY 49-50 en fuente oficial (senate.gov). → W05
- [VERIFICAR] MEI 2026 leído en el propio BOE (hoy [S]). → W05
- [VERIFICAR] Vigencia 2026 de la escala del ahorro (art. 66 LIRPF) y texto definitivo de los modelos 172/175/721 y de DAC8 en el BOE. → W05
- [VERIFICAR] Consulta DGT V0648-24 leída en petete; fiscalidad de tokens LP de AMM.
- [VERIFICAR] Integración de Chainlink CCIP en producción en SWIFT.

## Verificaciones pendientes con antigüedad (noticias de prensa sin contrastar y [VERIFICAR]; se anotan en eventos/verificados.json)
- [alta] 2026-10-29 (1 d) · Lagarde dejará la presidencia del BCE el 7 de febrero.
- [media] 2026-09-30 (30 d) · ETF de XRP en EE. UU. ≈ $1.430 M a 22-oct [S]; ETP europeos de XRP ≈ $914 M y de Stellar ≈ $104 M.
- [media] 2026-10-09 (21 d) · Trump dice que no atacará Irán antes de las elecciones del 3-nov (titular del bot; fuente primaria sin abrir).
- [media] 2026-10-21 (9 d) · El bot recoge «el Brent supera 110 $ al fallar las conversaciones con Irán» (15:20 UTC). Brent 109,34 → 110,04
- [media] 2026-10-22 (8 d) · Ataques hutíes a Arabia Saudí (dron en Shaybah de Aramco); Irán dice que alcanzó 7 petroleros, CENTCOM lo desm
- [media] 2026-10-23 (7 d) · El futuro continuo del Brent cierra en $111,97, con máximo del día sobre $116.
- [media] 2026-10-23 (7 d) · Titulares de «114 $» y «117 $» por ataques a infraestructura saudí. Brent 113,08 → 111,7 $ (-1.2 %), WTI 99,29
- [media] 2026-10-25 (5 d) · Lula gana la 2.ª vuelta con ~51,7 % frente a ~48,2 % de Flávio Bolsonaro, que no reconoce el resultado.
- … y 28 más en el Seguimiento

## Qué se está quedando viejo (frescura)
- 🔴 Radar regulatorio: Fechas previstas ya pasadas sin actualizar (4) → W03 · UE/cbdc; HK/politica; AE/politica; EG/politica
- 🟡 Radar regulatorio: Celdas sin dato (49) → W03 · Más huecos: CH 7, AU 7, UK 6, CA 6, EG 5
- 🟡 Países (política): Fichas con datos de más de 90 días o sin fecha (4) → W11 · Países Bajos, Polonia, China, India
- 🟡 Voces: Voces sin confirmar (4) → W06 · 1 llevan más de 14 días

## Bots con problema
- Votos de noticias, Paneles de datos

## Calendario: ya pasaron (10 días) y qué falta decidir
- 2026-10-21 · EE. UU.: la OCC publica su norma final de la GENIUS Act (alto) → ✓ revisado (hecho)
- 2026-10-23 · Francia: revisión de Moody's prevista el 23-oct, resultado sin confirm (medio) → ✓ cubierto por W02 del 2026-10-29
- 2026-10-27 · Reunión de la Fed (FOMC) (alto) → ✓ revisado (hecho)
- 2026-10-28 · Reunión del BCE (alto) → ⏳ SIN research: decidir (EV)
- 2026-10-28 · DTCC: lanzamiento del servicio de tokenización de DTC (hecho el 28-oct (medio) → ✓ revisado (hecho)
- 2026-10-28 · Canadá: decisión del Banco de Canadá sobre el tipo oficial (medio) → ✓ revisado (hecho)
- 2026-10-29 · PIB de EE. UU. (3T, avance) y gasto en consumo PCE de septiembre (alto) → ⏳ SIN research: decidir (EV)
Para los «SIN research»: pide `/research EV <fecha> <título>`; usa `research/prompts/EV-post-evento.md`. Descartar o marcar hecho: `eventos/revisados.json`.

## Calendario: próximos 14 días de impacto y qué los cubre
- 2026-10-29→10-30 · Reunión del Banco de Japón (alto) · EN CURSO → cubre W01 (Tipos de interés)
- 2026-10-30 · Brasil: último día para que los proveedores cripto existente (medio) → cubre W01 (Tipos de interés)
- 2026-11-01 · OPEP+ (7 países): reunión mensual (medio) → cubre W10 (Energía y geopolítica)
- 2026-11-03 · EE. UU.: elecciones de mitad de mandato (alto) → cubre W11 (Política y elecciones)
- 2026-11-03 · Australia: decisión del RBA sobre el tipo de efectivo (medio) → cubre W01 (Tipos de interés)
- 2026-11-03 · Stellar: voto de testnet de Protocol 30 (Bell) (medio) → sin rutina: valorar research EV
- 2026-11-04 · Tesoro de EE. UU.: anuncio trimestral de refinanciación (medio) → cubre W02 (Deuda y subastas)
- 2026-11-05 · Reino Unido: decisión del Banco de Inglaterra (Bank Rate 3,7 (alto) → cubre W01 (Tipos de interés)
- 2026-11-06 · Empleo EE. UU. (informe de octubre) (alto) → cubre W01 (Datos macro y tipos)
- 2026-11-06 · Brasil: bancos y entidades de pago no podrán operar con prov (medio) → cubre W03 (Regulación por países)
- 2026-11-10 · Inflación EE. UU. (IPC de octubre) (alto) → cubre W01 (Datos macro y tipos)
- 2026-11-10 · EIA: perspectivas de energía a corto plazo (STEO) (medio) → cubre W10 (Energía y geopolítica)

## Predicciones que vencen en 14 días
- #31 · 2026-11-01 · OPEP+ (7 países, comunicado)
- #7 · 2026-11-03 · CEO de Solana Policy Institute
- #25 · 2026-11-03 · Donald Trump (Truth Social, citado por CNBC)

## Próximas fechas clave
- 2026-10-30 · Brasil: último día para que los proveedores cripto existentes pidan autorización al Banco 
- 2026-11-01 · OPEP+ (7 países): reunión mensual
- 2026-11-03 · EE. UU.: elecciones de mitad de mandato
- 2026-11-03 · Australia: decisión del RBA sobre el tipo de efectivo
- 2026-11-03 · Stellar: voto de testnet de Protocol 30 (Bell)
- 2026-11-05 · Reino Unido: decisión del Banco de Inglaterra (Bank Rate 3,75 %)
- 2026-11-06 · Empleo EE. UU. (informe de octubre)
