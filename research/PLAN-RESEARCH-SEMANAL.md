# Plan de research recurrente (desde el 26-oct-2026)

Objetivo: seguir **aumentando y verificando** la información del Cerebro con un ritmo fijo y barato, en vez de lanzar tareas sueltas. Cada tarea tiene un prompt listo para pegar en `research/prompts/` (W01-W10). El estado se ve en la sección **Seguimiento** (ordenador y móvil). Todo con la cuota del plan Pro: la semana se reinicia los **martes a las 03:00 (hora española)**.

## 1. Lo que ya tenemos (25-oct-2026)
| Qué | Cantidad | Estado |
|---|---|---|
| Informes (`informes/`) | 163 (80 research, 33 dossiers G1-G15, 7 de vídeos, R00 diarios) | Buenos; muchos [VERIFICAR] sin cerrar |
| Marcas [VERIFICAR] | ≈ 1.655 en 155 archivos (picos: G12 fiscalidad 66, G8 inmobiliaria 65, G3 avales 54, G4 renta fija 50, G11 startups 41) | Hace falta un consolidado y priorizar por relevancia |
| Radar regulatorio | 136 celdas; **53 sin dato** (Irán 8, Egipto 7, Etiopía 6, Sudáfrica 5, Indonesia 5, Emiratos 4, Japón 3, India 3) y 28 solo [S] | Huecos por tema: ETF 11, custodia 10, tokenización 9, fiscal 8, CBDC 7 |
| Voces | 44 (P 14, D 12, S 13, C 2, R 1, E 2); 6 sin confirmar; 29 de un solo canal | Falta diversidad (escépticos, analistas de ETF, rating) |
| Predicciones | 47 registradas (42 sin resolver) | Se comprueban al llegar su fecha |
| Calendario | 79 eventos futuros (23 aproximados) | Semana FOMC/BCE/BoJ 27-30 oct; Brasil 30-oct; 13F 14-16 nov; Corea 11-nov |
| Datos automáticos | tipos (Fed, BCE, BoE, Brasil, Canadá), bonos, deuda, stablecoins, RWA, índices, petróleo, 4 cripto | Workflow `paneles.yml` L-V 21:30 UTC |
| Temas T / deuda D pendientes | T06, T08-T10, T12-T16, T23, T25 · D01-D06 | Ver Seguimiento |
| Calificaciones soberanas | leídas el 22-oct | Moody's Francia (23-oct) sin reflejar |

## 2. Ritmo semanal (modo normal ≈ 25 % de la cuota semanal)
| Día | Tarea | Coste |
|---|---|---|
| Lunes | R00 apertura + **W01 tipos de interés** (reuniones de la semana, radar y países manuales) | 2 % |
| Martes | R00 + **W02 deuda, subastas y calificaciones** (una tarea D por semana) | 2 % |
| Miércoles | R00 + **W03 países** (2 por sesión: huecos del radar → [P]) | 4 % |
| Jueves | R00 + **W05 verificación por lotes** (15-20 [VERIFICAR]) + **W04 ETF/flujos** cada 2 semanas | 3 % (+3 %) |
| Viernes | R00 cierre + **W06 voces y predicciones** + **W09 resumen semanal** | 3 % + 1,5 % |
| Sábado / domingo | R00 ligero + **W10 energía y geopolítica** | 2 % |
| Mensual | **W07 fuentes** (1.ª semana) y **W08 auditoría de coherencia** (última semana) | 3 % + 4 % |
R00 diario: < 1 % cada uno (≈ 5 % a la semana). Total aproximado: 25 % por semana más ≈ 2 % de las mensuales.
**Modo ahorro (≈ 15 %):** solo R00, W01, W02, W05 y W09; W03, W04, W06 y W10 en semanas alternas.

## 3. Rotaciones para que no se repita todo
- **W03 países (4 semanas):** 1) Japón + Singapur; 2) Hong Kong + India; 3) China + Rusia; 4) Emiratos + BRICS/organismos. Luego Irán, Egipto, Etiopía, Sudáfrica, Indonesia.
- **W02 deuda (6 semanas):** D03 Francia (OAT) → D01 Italia (BTP) → D02 Alemania (Bund) → D04 China → D05 30 años ES/IT → D06 bancos.
- **W05:** primero cripto, regulación, ETF, macro y fiscalidad cripto de España; después renta fija; inmobiliaria y startups al final.

## 4. Qué NO hace falta pagar con Claude
- La primera pasada de W03 puede hacerla **Gemini** (Deep Research con el prompt completo, no el código «Txx»); Claude solo verifica fuentes y actualiza.
- Los tipos de Fed, BCE, BoE, Brasil y Canadá ya se leen solos; Claude solo revisa los que no tienen fuente abierta.
- Los precios y curvas ya son automáticos (sin IA).

## 5. Cómo se usa
1. El lunes mira Seguimiento: «Hoy toca».
2. Abre una sesión NUEVA (menos historial = menos cuota) y pega el prompt (`research/prompts/W0x-….md`).
3. Al acabar: coste real en la fila de `research/COLA.md`, revisión de `git status` y commit por nombre de archivo con tu OK.
4. El viernes, W09 resume la semana y propone la siguiente.

## 6. Pendiente de decidir contigo
- Hasta cuándo dura tu suscripción, para repartir este plan en bloques (cada bloque = 4 semanas).
- Si quieres un aviso por Telegram el día de cada reunión de un banco central (ya hay avisos del calendario; añadirlo cuesta < 1 %).
- Si activamos el modo ahorro cuando el semanal pase del 60 % el miércoles.

## 7. Huecos del Centro (C01-C07, desde el 25-oct-2026)
Salen del plano del Centro (`explorador/centro.json`, pestaña «Centro» del móvil). Cada una tiene su prompt en `research/prompts/C0x-*.md` y su fila en `research/COLA.md` (se ven en el Seguimiento).
- **Hechas el 25-oct:** C01 gasto en defensa y C02 liquidez M2 (informes en `informes/research/`; falta ponerlas en el panel).
- **Orden propuesto, una por semana en la ranura de fin de semana (donde W10 deje hueco) y solo si el semanal está por debajo del 70 %:** C03 matriz de riesgos (3 %) → C05 archivo de precedentes (3 %) → C04 cuadro de valoración (3 %) → C06 vigilante de EDGAR (código, sin IA) → C07 suscripciones (Joel aporta datos; en `privado/`).
- Al acabar cada una se actualiza el estado en `explorador/centro.json` y se regenera con `python scripts/construir_movil.py`.
- **Tras el repaso del cerebro (25-oct):** C08 consolidar el archivo principal (4 %, Opus, sesión nueva tras el martes 27-oct), C09 lote de verificación de dudas del cerebro (3 %, jueves con W05) y C10 auditoría cruzada de los resúmenes semanales del bot (3 %, junto a la W08 de fin de mes).
