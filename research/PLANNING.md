# PLANNING (autogenerado, no editar a mano) · 2026-10-28 13:03 UTC

Lo regenera `python scripts/construir_seguimiento.py` (el mismo que alimenta el Seguimiento del móvil y del PC), así que **Seguimiento y planning no pueden diverger**. `/research` sin argumento lee SOLO este archivo; con un ID, lee la fila de `research/COLA.md` y el prompt indicado aquí. Cuota: se mide con get_usage, no está aquí.

## Hoy (mié 2026-10-28): solo lo casi obligatorio
- R00 apertura ⏳ pendiente · cierre ⏳ pendiente (desde las 15:00) · racha 11 días
- Fija de hoy (último miércoles del mes: auditoría mensual): **W08 Auditoría mensual** (~4 %) · último 2026-10-24 · `research/prompts/W08-*.md`

## 🟣 Gemini del día (gratis, 1 consulta ligera de ~15 fuentes; Claude da el prompt, tú lo pegas en Gemini)
- Gemini del día: toca **Evento: Reunión del BCE** · prompt `research/gemini/NOTICIAS-DIA.md` · ⏳ pendiente
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
- C29 · Centro · Energía, Ormuz y guerra ↔ noticias ↔ Órbita · Sonnet M · ~3 % · `research/prompts/C29-energia-guerra.md`
- C30 · Centro · Política y elecciones por país · Sonnet M · ~3 % · `research/prompts/C30-politica-elecciones.md`
- C31 · Centro · Inflación (IPC) por país · Sonnet M · ~3 % · `research/prompts/C31-inflacion.md`
- C32 · Centro · Móvil: pantalla principal de precios, tipos, petróleo e inflación + aud · Sonnet M · ~3 % · `research/prompts/C32-movil-principal.md`
- C33 · Compactación semanal: repasar los informes de la semana, consolidar en el cerebr · Sonnet M · ~3 % · ``
- C34 ◐ en parte · Bots · Noticias: el cron horario de GitHub solo se ejecutó 5-6 veces al día (27- · Joel+Claude S · ~~0 % cuota (el coste de API lo limitan las franjas del bot) · ``
- C35 · Centro · Noticias en la Órbita · Sonnet M · ~3 % · `research/prompts/C35-noticias-en-orbita.md`
- C36 · Centro · Rutina de noticias manuales (Claude y Gemini) · Sonnet M · ~3 % · `research/prompts/C36-rutina-noticias-manual.md`
- C37 ◐ en parte · Centro · Auditoría C13: enlace a la fuente primaria en cada celda del radar regu · Sonnet S · ~1,5 % · `research/prompts/C37-urls-radar-pendientes.md`
- C39 · Centro · Volcar a la Órbita lo ya investigado sin movimiento (países T07-T16 y W · Sonnet S · ~2 % · `research/prompts/C39-volcado-orbita.md`
- C40 · Radar · Jurisdicciones fuera del radar: Reino Unido, Suiza, Canadá, Australia y  · Sonnet M · ~3 % · `research/prompts/C40-jurisdicciones-fuera-del-radar.md`
- C41B · Centro · Diseño de la Órbita: vista independiente con Gemini (búsqueda de Google · Gemini S · ~0 % · ``
- C41C · Centro · Fusión del diseño de la Órbita (C41A + C41B): coincidencias, discrepanc · Opus S · ~2 % · `research/prompts/C41C-fusion-diseno-orbita.md`
- C42 · Centro · Rendimientos y colateral: staking, lending CeFi/DeFi, AMM XRPL/Stellar, · Sonnet M · ~3 % · `research/prompts/C42-rendimientos-colateral.md`
**Países y temas (T)** · detalle en `research/COLA-TEMAS-GEMINI.md`
- T25 · Tema libre
**Deuda y bonos (D)** · detalle en `research/COLA-DEUDA-BONOS.md`
- D01 · Italia: rendimientos diarios de BTP a 2, 5, 10 y 30 años con fuente of
- D02 · Alemania: rendimientos diarios de Bund (2, 5, 10, 30 a): Bundesbank (A
- D03 · Francia: curva OAT por plazos (2, 5, 10, 30 a) además del TEC 10 y des
- D04 · China: rendimientos de los bonos del Estado (1, 2, 5, 10, 30 a) de Chi
- D05 · 30 años de España e Italia (y Francia si D03 no lo trae): bono a 30 añ
- D06 · (parcial) Bancos y deuda: exposición soberana de 116 bancos europeos (
**Otros research (R)** · detalle en `research/COLA.md`
- R17 · Resumen semanal de 1 página (para imprimir)
- R36 · PROFUNDO: Segunda pasada con los PDFs que haya en research/fuentes/ (R
- R39 · Auditoría final corta (18-19 oct): solo lo escrito después de R31/R38 
**Pasadas puntuales de rutinas (W)** · detalle en `research/COLA.md`
- W01B · Tipos de interés: segunda pasada tras las decisiones de la Fed, el BCE · 📅 programada 2026-10-29
- W03E ◐ en parte · Países: Irán, Egipto y Etiopía (huecos del radar) · bloqueo: PDF de Joel en research/fuentes/ (relanzar sin los PDF no lo

## Auditorías abiertas
- C13 (Media): Cero enlaces: el campo fuente solo vale P/S/VERIFICAR. No hay forma de pulsar y llegar a la fuente. (voces.jso
- Auditoría mensual W08: última semana del mes (miércoles)

## Verificaciones abiertas ([VERIFICAR]; las cierra W05 o W08)
- [VERIFICAR] Texto literal de la **sección 404** de CLARITY en congress.gov (hoy solo [S]). → W05
- [VERIFICAR] Precio y cierre de cada adquisición de Ripple sin precio publicado (Standard Custody, Palisade, Solvexia) y cierre de BC Payments Australi
- [VERIFICAR] Fecha de Palisade: 3-nov frente a ~4-nov-2025 (unificar con ripple.com). → W05
- [VERIFICAR] Cloture CLARITY 49-50 en fuente oficial (senate.gov). → W05
- [VERIFICAR] MEI 2026 leído en el propio BOE (hoy [S]). → W05
- [VERIFICAR] Vigencia 2026 de la escala del ahorro (art. 66 LIRPF) y texto definitivo de los modelos 172/175/721 y de DAC8 en el BOE. → W05
- [VERIFICAR] Consulta DGT V0648-24 leída en petete; fiscalidad de tokens LP de AMM.
- [VERIFICAR] El «Treasury al 5,34 %» del resumen W43 (casi seguro el 30 años, 5,33 %) y la cifra de Bloomberg sobre flujos de crudo frente a PortWatch.
- [VERIFICAR] Integración de Chainlink CCIP en producción en SWIFT.

## Qué se está quedando viejo (frescura)
- 🔴 Radar regulatorio: Fechas previstas ya pasadas sin actualizar (1) → W03 · UE/cbdc
- 🟡 Radar regulatorio: Celdas sin dato (26) → W03 · Más huecos: EG 5, IR 5, ET 4, ZA 3, ID 3
- 🟡 Voces: Voces sin confirmar (4) → W06 · 1 llevan más de 14 días

## Bots con problema
- Paneles de datos

## Calendario: ya pasaron (10 días) y qué falta decidir
- 2026-10-21 · EE. UU.: la OCC publica su norma final de la GENIUS Act (alto) → ✓ revisado (hecho)
- 2026-10-23 · Francia: revisión de Moody's prevista el 23-oct, resultado sin confirm (medio) → ✓ cubierto por W02 del 2026-10-26
Para los «SIN research»: pide `/research EV <fecha> <título>`; usa `research/prompts/EV-post-evento.md`. Descartar o marcar hecho: `eventos/revisados.json`.

## Calendario: próximos 14 días de impacto y qué los cubre
- 2026-10-27→10-29 · Swell 2026 (Ripple), Nueva York (medio) · EN CURSO → sin rutina: valorar research EV
- 2026-10-27→10-28 · Reunión de la Fed (FOMC) (alto) · EN CURSO → cubre W01 (Tipos de interés)
- 2026-10-28→10-29 · Reunión del BCE (alto) → cubre W01 (Tipos de interés)
- 2026-10-28→10-29 · Meridian 2026 (Stellar), Lisboa (medio) → sin rutina: valorar research EV
- 2026-10-28 · Canadá: decisión del Banco de Canadá sobre el tipo oficial (medio) → cubre W01 (Tipos de interés)
- 2026-10-29 · PIB de EE. UU. (3T, avance) y gasto en consumo PCE de septie (alto) → cubre W01 (Datos macro y tipos)
- 2026-10-29→10-30 · Reunión del Banco de Japón (alto) → cubre W01 (Tipos de interés)
- 2026-10-30 · Brasil: último día para que los proveedores cripto existente (medio) → cubre W01 (Tipos de interés)
- 2026-10-31 · DTCC: lanzamiento previsto del servicio de tokenización de D (medio) → cubre W04 (ETF y flujos)
- 2026-11-01 · OPEP+ (7 países): reunión mensual (medio) → cubre W10 (Energía y geopolítica)
- 2026-11-03 · EE. UU.: elecciones de mitad de mandato (alto) → cubre W06 (Voces y predicciones)
- 2026-11-03 · Australia: decisión del RBA sobre el tipo de efectivo (medio) → cubre W01 (Tipos de interés)

## Predicciones que vencen en 14 días
- #44 · 2026-10-31 · DTCC (nota de prensa)
- #31 · 2026-11-01 · OPEP+ (7 países, comunicado)
- #7 · 2026-11-03 · CEO de Solana Policy Institute
- #25 · 2026-11-03 · Donald Trump (Truth Social, citado por CNBC)

## Próximas fechas clave
- 2026-10-28 · Reunión del BCE
- 2026-10-28 · Meridian 2026 (Stellar), Lisboa
- 2026-10-28 · Canadá: decisión del Banco de Canadá sobre el tipo oficial
- 2026-10-29 · PIB de EE. UU. (3T, avance) y gasto en consumo PCE de septiembre
- 2026-10-29 · Reunión del Banco de Japón
- 2026-10-30 · Brasil: último día para que los proveedores cripto existentes pidan autorización al Banco 
- 2026-11-01 · OPEP+ (7 países): reunión mensual
