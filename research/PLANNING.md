# PLANNING (autogenerado, no editar a mano) · 2026-10-26 22:10 UTC

Lo regenera `python scripts/construir_seguimiento.py` (el mismo que alimenta el Seguimiento del móvil y del PC), así que **Seguimiento y planning no pueden diverger**. `/research` sin argumento lee SOLO este archivo; con un ID, lee la fila de `research/COLA.md` y el prompt indicado aquí. Cuota: se mide con get_usage, no está aquí.

## Hoy (lun 2026-10-26): solo lo casi obligatorio
- R00 apertura ✓ · cierre ⏳ pendiente (desde las 15:00) · racha 10 días
- Fija de hoy (lunes: semana de bancos centrales): **W01 Tipos de interés** (~2 %) · último 2026-10-26 · `research/prompts/W01-*.md`

## Rutinas W: lo que falta este periodo (sin día fijo; se hacen cuando haya hueco, de más atrasada a menos)
- W05 · Verificación por lotes · ~3 % · cada jueves · último 2026-10-23 · `research/prompts/W05-*.md`
- W09 · Resumen semanal · ~1,5 % · cada viernes · último 2026-10-25 · `research/prompts/W09-*.md`
- W10 · Energía y geopolítica · ~2 % · fin de semana · último 2026-10-25 · `research/prompts/W10-*.md`
Hechas en este periodo: W01, W02, W03, W04, W06, W07, W08

## Research nuevo pendiente (por sección)
**Centro y revisión del cerebro (C)**
- C04 · Cuadro de valoración por sector (PER, EV/EBITDA, FCF yield) · Sonnet M · ~3 % · `research/prompts/C04-valoracion.md`
- C05 · Archivo de precedentes históricos (formato fijo) · Sonnet M · ~3 % · `research/prompts/C05-precedentes.md`
- C06 · Vigilante de SEC EDGAR (ETF, DTCC, 13F) · Sonnet M · ~<1 % · `research/prompts/C06-edgar.md`
- C07 · Control de suscripciones y software (privado) · Sonnet S · ~<1 % · `research/prompts/C07-suscripciones.md`
**Países y temas (T)** · detalle en `research/COLA-TEMAS-GEMINI.md`
- T09 · Hong Kong · vence/ocurre 2026-10-29 (Hong Kong y Emiratos: la HKMA (4,25 %) y)
- T13 · Emiratos Árabes · vence/ocurre 2026-10-29 (Hong Kong y Emiratos: la HKMA (4,25 %) y)
- T14 · China · vence/ocurre 2026-11-20 (China: fijación mensual del LPR (hoy 3,0)
- T10 · India · vence/ocurre 2026-12-02 (Reunión del RBI (India))
- T12 · Rusia
- T15 · BRICS sin cubrir
- T16 · Organismos internacionales
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
- W01B · Tipos de interés: segunda pasada tras las decisiones de la Fed, el BCE

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
- 🟡 Radar regulatorio: Celdas sin dato (45) → W03 · Más huecos: IR 7, EG 6, ZA 5, ID 5, ET 5
- 🟡 Voces: Voces sin confirmar (6) → W06 · 3 llevan más de 14 días

## Bots con problema
- ninguno

## Calendario: ya pasaron (10 días) y qué falta decidir
- 2026-10-21 · EE. UU.: la OCC publica su norma final de la GENIUS Act (alto) → ⏳ SIN research: decidir (EV)
- 2026-10-23 · Francia: revisión de Moody's prevista el 23-oct, resultado sin confirm (medio) → ✓ cubierto por W02 del 2026-10-26
Para los «SIN research»: pide `/research EV <fecha> <título>`; usa `research/prompts/EV-post-evento.md`. Descartar o marcar hecho: `eventos/revisados.json`.

## Calendario: próximos 14 días de impacto y qué los cubre
- 2026-10-27→10-29 · Swell 2026 (Ripple), Nueva York (medio) → sin rutina: valorar research EV
- 2026-10-27→10-28 · Reunión de la Fed (FOMC) (alto) → cubre W01 (Tipos de interés)
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
- 2026-10-27 · Swell 2026 (Ripple), Nueva York
- 2026-10-27 · Reunión de la Fed (FOMC)
- 2026-10-28 · Reunión del BCE
- 2026-10-28 · Meridian 2026 (Stellar), Lisboa
- 2026-10-28 · Canadá: decisión del Banco de Canadá sobre el tipo oficial
- 2026-10-29 · PIB de EE. UU. (3T, avance) y gasto en consumo PCE de septiembre
- 2026-10-29 · Reunión del Banco de Japón
