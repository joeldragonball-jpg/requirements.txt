# Cola de research (global: macro, geopolítica y digital assets)

Cómo se usa: abre una sesión NUEVA (menos historial = menos cuota), cambia al modelo indicado en la columna "Modelo" y escribe `/research <ID>` (por ejemplo `/research R10`). El comando lee este archivo y la plantilla, hace el trabajo, guarda el informe en `informes/research/` y marca aquí el estado y el coste real. Para ver el menú escribe `/research` sin nada.

Costes = **estimación** en % de la cuota semanal (plan Pro). Se calibran con el uso real: al terminar cada tarea se anota el coste medido en "Real".
Tamaños (versión RÁPIDA, medida el 14-oct: R10 y R02 costaron <1 % cada una): S ≈ 1 %, M ≈ 2 %, L ≈ 4 %. La columna Est. usa estos valores.
Versión PROFUNDA (`/research R02P` = R02 profundo): lee fuentes primarias enteras con WebFetch, 2-3 pasadas (hechos, contraste, huecos), esfuerzo alto. Coste aún SIN medir; la primera (R02P) lo calibra. Se usa para gastar de verdad la cuota semanal.

Criterio de modelo (menos tokens, aunque tarde más): Haiku para rastreo y tablas, Sonnet para dossiers y análisis, Opus solo para escribir lo que se imprime o síntesis final. Una sola sesión en serie; nada de subagentes en paralelo salvo que yo lo pida (cada uno repite el arranque y gasta más). Esfuerzo bajo/medio salvo en auditorías.
Prueba A/B hecha (14-oct): R10 Haiku y R02 Sonnet salieron <1 % cada una; calidad de R02 buena pero con muchas fuentes secundarias. Siguiente prueba: R02P (profundo).

Reglas fijas: fuente primaria en su idioma original (traducida por mí, con enlace y fecha); lo que solo salga en prensa secundaria va [VERIFICAR]; hechos separados de opiniones; sin recomendaciones de compra/venta; España solo en R20.

| ID | Tema | Plantilla | Modelo | Esfuerzo | Tam. | Est. | Real | Estado |
|----|------|-----------|--------|----------|------|------|------|--------|
| R00 | Apertura/cierre diario (macro + XRP/XLM) | sesion-diaria | Sonnet | bajo | S | 3 % | | recurrente |
| R01 | BRICS y pagos transfronterizos (BRICS Pay, mBridge, yuan/rublo digital) | dossier-region | Sonnet | medio | L | 4 % | | pendiente (cubierto por R01P) |
| R01P | BRICS PROFUNDO (informe único rápido+profundo; PIB y brics2026.gov.in dan 403: declaración leída vía prensa con cita) | dossier-region (profundo) | Sonnet | alto | L+ | sin medir | ~1 % semanal (36 → 37 %, medidor sin decimales; 5h: 6→9 %, ~50k tokens de contexto) | hecho 2026-10-15 |
| R02 | India (RBI, e₹, UPI, fiscalidad y regulación cripto) | dossier-region | Sonnet | medio | M | 2 % | <1 % (33 → 33 %, medidor sin decimales; 5h: 33→34 %) | hecho 2026-10-14 (prueba A/B) |
| R02P | India PROFUNDO: cubrir los 8 huecos de 'Qué falta por buscar' de R02 leyendo fuentes primarias enteras (RBI, NPCI, sansad.in, incometax.gov.in, BIS) | dossier-region (profundo) | Sonnet | alto | M+ | sin medir | <1 % semanal (34 → 34 %, medidor sin decimales; 5h: 35→37 %, ~109k tokens de contexto) | hecho 2026-10-15 (varias fuentes primarias bloqueadas: captcha/403; nivel máximo = secundaria con cita) |
| R03 | Brasil (Drex, Pix, Banco Central, CVM, pilotos Ripple/Stellar) | dossier-region | Sonnet | medio | M | 2 % | | pendiente (cubierto por R03P) |
| R03P | Brasil PROFUNDO (informe único rápido+profundo; BCB no legible: secundaria con cita) | dossier-region (profundo) | Sonnet | alto | M+ | sin medir | <1 % semanal (34 → 34 %, medidor sin decimales; 5h: 38→40 %) | hecho 2026-10-15 (bcb.gov.br JS y normativos 404/400: resoluciones leídas vía despachos) |
| R04 | Singapur (MAS, Project Guardian, stablecoins, tokenización) | dossier-region | Sonnet | medio | M | 2 % | | pendiente (cubierto por R04P) |
| R04P | Singapur PROFUNDO (informe único rápido+profundo; mas.gov.sg legible, PDF de la consulta no leídos) | dossier-region (profundo) | Sonnet | alto | M+ | sin medir | <1 % semanal (34 → 34 %, medidor sin decimales; 5h: 40→42 %) | hecho 2026-10-15 |
| R05 | Corea del Sur (FSC, ley de activos digitales, won stablecoin, XRP minorista) | dossier-region | Sonnet | medio | M | 2 % | | pendiente (cubierto por R05P) |
| R05P | Corea del Sur PROFUNDO (informe único rápido+profundo; fuentes oficiales coreanas no abiertas: prensa con cita) | dossier-region (profundo) | Sonnet | alto | M+ | sin medir | ~1 % semanal en la última tarea (34 → 35 %; lote R03P+R04P+R05P entero: 34 → 35 %, 5h: 38→43 %, ~190k tokens de contexto) | hecho 2026-10-15 |
| R06 | Rusia y sanciones (cripto en comercio exterior) | dossier-region | Sonnet | medio | M | 2 % | | pendiente (cubierto por R06P) |
| R06P | Rusia y sanciones PROFUNDO (informe único; Tesoro EE. UU. leído entero; consilium.europa.eu 403, sozd.duma.gov.ru/cbr.ru/tks.ru/ppt.ru no abrieron: ley rusa y paquetes UE vía secundaria con cita) | dossier-region (profundo) | Sonnet | alto | M+ | sin medir | <1 % semanal (38 → 38 %, medidor sin decimales; 5h: 19→20 %, ~50k tokens de contexto) | hecho 2026-10-15 |
| R07 | Japón, Emiratos y Hong Kong (centros regulatorios) | dossier-region | Sonnet | medio | M | 2 % | | pendiente (cubierto por R07P) |
| R07P | Japón, Emiratos y Hong Kong PROFUNDO (informe único; sin abrir: texto de la ley japonesa, comunicado HKMA 10-abr, CBUAE/VARA/FSRA y ripple.com 404; casi todo vía secundaria con cita) | dossier-region (profundo) | Sonnet | alto | M+ | sin medir | <1 % semanal (38 → 38 %, medidor sin decimales; 5h: 20→22 %, ~35k tokens de contexto; lote R06P+R07P entero: 5h 19→22 %, semanal 38 → 38 %) | hecho 2026-10-15 |
| R08 | BIS, FMI y bancos centrales (Agorá, mBridge, CBDC) | dossier-region | Sonnet | medio | L | 4 % | | pendiente (cubierto por R08P) |
| R08P | BIS/FMI/bancos centrales PROFUNDO (informe único; bis.org dio ECONNRESET en 5 intentos: BIS vía nota del BCE y buscador; ecb.europa.eu e imf.org sí abren) | dossier-region (profundo) | Sonnet | alto | L+ | sin medir | <1 % semanal (37 → 37 %, medidor sin decimales; 5h: 9→11 %, ~45k tokens de contexto) | hecho 2026-10-15 |
| R09 | Ripple y Stellar por región (alianzas, licencias, sesiones) | dossier-region | Sonnet | medio | L | 4 % | | pendiente (cubierto por R09P) |
| R09P | Ripple y Stellar por región PROFUNDO (informe único; ripple.com y stellar.org abren, son parte interesada; occ.gov/cssf.lu/dtcc.com no leídos; businesswire y taiwannews 403) | dossier-region (profundo) | Sonnet | alto | L+ | sin medir | <1 % semanal (37 → 37 %, medidor sin decimales; 5h: 11→12 %, ~30k tokens de contexto) | hecho 2026-10-15 |
| R10 | Calendario único de catalizadores a 90 días | calendario | Haiku | bajo | M | 2 % | <1 % (33 → 33 %, medidor sin decimales) | hecho 2026-10-14 (prueba A/B) |
| R11 | Verificación en bloque de los [VERIFICAR] pendientes | verificacion | Haiku | bajo | L | 4 % | | pendiente (cubierto por R11P) |
| R11P | Verificación en bloque PROFUNDA (informe 2026-10-15-R11P-verificacion.md; hecha en Sonnet por continuidad del lote; sec.gov/bis.org/cbr.ru no abrieron: casi todo secundaria) | verificacion | Sonnet | alto | L+ | sin medir | <1 % semanal (37 → 37 %, medidor sin decimales; 5h: 14→15 %, ~30k tokens de contexto) | hecho 2026-10-15 |
| R12 | Auditoría cruzada del cerebro contra fuentes primarias | auditoria | Sonnet | alto | L | 4 % | | pendiente (cubierto por R12P) |
| R12P | Auditoría cruzada PROFUNDA (8 apuntes, 17 filas; informe 2026-10-15-R12P-auditoria-cerebro-profundo.md; plantilla generica/auditoria; fuentes oficiales parcialmente cerradas) | generica (auditoria) | Sonnet | alto | L+ | sin medir | <1 % semanal (37 → 37 %, medidor sin decimales; 5h: 12→14 %, ~45k tokens de contexto) | hecho 2026-10-15 |
| R13 | Casos bajistas por tesis | caso-bajista | Sonnet | medio | M | 2 % | | pendiente |
| R14 | Backtest de predicciones (informes/predicciones.md) | backtest | Sonnet | medio | S | 1 % | | pendiente |
| R15 | Mapa de actores y conflictos de interés | actores | Sonnet | medio | M | 2 % | | pendiente |
| R16 | Glosario verificado (RWA, DTCC, CBDC, mBridge…) | glosario | Haiku | bajo | S | 1 % | | pendiente |
| R17 | Resumen semanal de 1 página (para imprimir) | resumen-semanal | Opus | medio | S | 1 % | | pendiente |
| R18 | Nueva guía G16+ por jurisdicción | dossier-region | Opus | medio | L | 4 % | | pendiente |
| R19 | Comparativa de plataformas y custodia | dossier-region | Sonnet | medio | M | 2 % | | pendiente |
| R20 | Auditoría España (BOE/AEAT), solo semanal o mensual | verificacion | Haiku | bajo | S | 1 % | | pendiente |
| R21 | 13F y exposición institucional a XRP/XLM: quién tiene ETF y valores ligados, trimestre a trimestre (1T, 2T ya; 3T tras ~14-nov). Fuente: EDGAR (sec.gov abre desde aquí). Los 13F solo muestran posición a cierre de trimestre: no cuándo ni a qué precio compraron; no incluyen cripto en sí | 13f | Sonnet | alto | M | 2 % | | pendiente (tras R06P/R07P) |

## Orden sugerido para esta semana (hasta el 20-oct)
R02P (profundo, mide coste) → según su coste, repetir en versión profunda: R01, R08, R09, R11, R12 → R00 diario → R17 (día 19). Como las versiones rápidas cuestan ~1-2 %, para aprovechar la cuota usar la versión profunda. Reserva: dejar ~10 % para una auditoría final.

## Antes de dejar el ordenador solo (30-60 min)
Los permisos de búsqueda web y escritura en `informes/research/` deben estar aprobados de antemano, o la sesión se para esperando. Confirma qué permisos te pide la tarea antes de irte.

## Lotes predefinidos (para `/research-lote`)
Un ID con P es la versión PROFUNDA de la fila base (mismo tema, fuentes primarias leídas, esfuerzo alto). Coste medido hasta ahora: ~1 % semanal por tarea profunda mediana; las grandes pueden costar más (se medirá).
- **grandes**: R01P → R08P → R09P → R12P → R11P (mayor peso primero; conviene Sonnet, esfuerzo alto; R11P puede ir en Haiku).
- **regiones**: R03P → R04P → R05P → R06P → R07P (Sonnet, esfuerzo alto).
- Tope de seguridad del lote: parar al 90 % semanal o al 85 % de la ventana de 5 horas. La reserva para la auditoría final es del ~10 %.
- Lo no leído por captcha/403 se apunta como hueco: Joel descarga el PDF a `research/fuentes/` y se lee en otra tarea.
