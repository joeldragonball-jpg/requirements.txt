# BIS, FMI y bancos centrales (Agorá, mBridge, CBDC, tokenización) — informe único rápido+profundo (2026-10-15, R08P)

> **Nota 2026-10-18 (R40):** el Observatorio Legislativo del Parlamento Europeo (2023/0212(COD)) muestra votación en comisión el 23-jun-2026 y confirmación del mandato de negociación por el pleno el 9-jul-2026; etapa vigente "Awaiting Parliament's position in 1st reading". No hay acuerdo final. Donde este informe dice "el trílogo sigue abierto" o lo deja como pendiente de comprobar, vale esta precisión. Ver informes/research/2026-10-17-R40-cbdc-por-pais-profundo.md.

Etiquetas: **LEÍDO** = página oficial abierta con WebFetch (resumen del extractor, no PDF entero) · **extracto** = ficha/buscador de la fuente oficial · **secundaria** = prensa/despacho que cita la fuente. No es recomendación de compra/venta.

**Acceso:** `bis.org` devolvió **ECONNRESET** en 5 intentos (comunicados p260527, p260623, ficha de Agorá y de mBridge): los datos del BIS vienen del texto que cita el buscador y de la nota del BCE. `ecb.europa.eu` (piloto euro digital, nota Agorá, página Pontes) e `imf.org` (blog y página del GFSR) SÍ abrieron. `federalreserve.gov` abrió solo el índice de 2026. Los PDFs de 97 páginas (informe Agorá), AER 2026 y GFSR cap. 3 **no se leyeron**; faltan en `research/fuentes/`.

## Resumen (5 líneas)
1. **Agorá (BIS, 27-may-2026):** el prototipo demostró liquidación atómica transfronteriza con reservas tokenizadas + depósitos tokenizados; **siguiente fase: valor real**, con el Banco de Canadá entrando. Es un experimento, no producción (7 bancos centrales, >40 entidades).
2. **BCE:** **Pontes arrancó el 21-sep-2026** (LEÍDO en ecb.europa.eu); el piloto del euro digital (36 PSP, 12 meses) empieza en el 2.º semestre de 2027 y la emisión "posible" en **2029 si el Reglamento se adopta en 2026**; el trílogo sigue abierto.
3. **BIS Informe Anual (28-jun-2026):** las stablecoins actuales "no pasan" los criterios de dinero (singularidad, elasticidad, interoperabilidad, integridad); propone un **libro mayor unificado anclado en dinero de banco central**. Es postura institucional, no hecho de mercado.
4. **FMI (GFSR oct-2026, cap. 3, 8-oct):** la tokenización es aún pequeña y fragmentada, con riesgo de amplificar ventas forzadas; **no mencionó stablecoins** en el blog leído. Pide neutralidad tecnológica y liquidación en "dinero seguro".
5. **EE. UU.:** la Fed publicó el **24-sep-2026** dos propuestas de reglas bajo la GENIUS Act (reservas, capital, solicitud de emisores bancarios) para comentario; "cuentas de pago" (skinny master accounts) con meta Q4-2026 según Waller (secundaria). **Ninguna fuente menciona XRP/XLM/Ripple/Stellar en estos proyectos de bancos centrales.**

## Qué es hecho verificado (tabla)
| Dato | Fuente primaria | Fecha | Idioma | Lectura |
|---|---|---|---|---|
| Agorá: informe del prototipo publicado; liquidación atómica con reservas y depósitos tokenizados; "next step: real-value testing" | Nota del BCE (ecb.europa.eu, "Tokenisation can improve wholesale cross-border payments…") | 27-may-2026 | EN | LEÍDO (nota BCE); BIS p260527 = extracto vía buscador |
| Participantes Agorá: BoE, NY Fed, Banque de France (Eurosistema), BoJ, BoK, Banxico, SNB; Banco de Canadá se suma; >40 entidades; arquitectura "unifying ledger" (depósitos) + libros jurisdiccionales (reservas) | Comunicado BIS p260527 | 27-may-2026 | EN | extracto (cita de buscador, 2 medios coinciden) |
| Pontes: "initial launch… took place 21 September 2026"; acceso a entidades con acceso a T2; operadores DLT elegibles (CSD, DSS/DTSS, CCP, entidades de crédito, etc.) | BCE, página Pontes | 21-sep-2026 | EN | LEÍDO (página) |
| Pontes hará de puente entre plataformas DLT y TARGET; Agorá alimenta Pontes y Appia | BCE (nota Agorá) | 27-may-2026 | EN | LEÍDO |
| Euro digital: piloto de 12 meses desde el 2.º semestre de 2027, 36 PSP seleccionados de >50, 19 bancos centrales nacionales; comercios pueden manifestar interés hasta el **27-oct-2026**; emisión posible en 2029 "si el Reglamento se adopta en 2026" | BCE, página del piloto | oct-2026 | EN | LEÍDO |
| Euro digital en la UE: comité ECON 23-jun (43–14–1), pleno 9-jul (cifras 416–169–22 en un medio), 1.er trílogo 13-jul; temas abiertos: límites de tenencia y compensación; aspiración de acuerdo a fin de 2026 | Freshfields y medios (Sumsub, Ground News) | jun–jul-2026 | EN | secundaria; **no hay acuerdo final** [VERIFICAR en Legislative Observatory 2023/0212(COD)] |
| Informe Anual BIS 2025/26 y AER publicados el 28-jun-2026; comunicado previo el 23-jun: stablecoins no cumplen "singleness"; propuesta de libro mayor unificado | BIS p260623 (por buscador) | 23/28-jun-2026 | EN | extracto; 5 medios (The Block, Cointelegraph, CFOtech…) |
| GFSR oct-2026 "Resilience, Risk, and Transformation": cap. 3 "Scaling Tokenization": mercados tokenizados "pequeños y fragmentados", 4 limitaciones (seguridad jurídica, claridad regulatoria, interoperabilidad, activos de liquidación) | FMI, página del GFSR | 8–13-oct-2026 | EN | LEÍDO (página) |
| Blog FMI (8-oct): repos = mayor parte de la actividad (≈300.000–350.000 M$ diarios); ≈65.000 M$ en crédito, fondos monetarios y acciones tokenizadas; ≈80 % de operaciones de acciones tokenizadas < 1 acción; >50 % fuera del horario | FMI, blog (Fernandez Dionis, Ferreira, Leika, Vamvakidis) | 8-oct-2026 | EN | LEÍDO. **Ambigüedad:** el extractor dijo "65.000 M$ diarios"; ChainCatcher/Decrypt lo dan como stock "a 31-jul" → [VERIFICAR] |
| Fed: 24-sep-2026, dos propuestas bajo la GENIUS Act (emisores de stablecoins de pago supervisados por la Junta) abiertas a comentario | federalreserve.gov, índice de comunicados 2026 | 24-sep-2026 | EN | LEÍDO (título); texto sin leer |
| Fed: propuesta de "payment accounts" (enmiendas a Reg. A y D) el 20-may-2026 | Despachos (ABA, Steptoe, Ledger Insights) | may-2026 | EN | secundaria; no aparece en índice de la Fed → [VERIFICAR] |
| mBridge: BIS "graduated out" oct-2024, discurso 31-oct-2024; Arabia Saudí confirmó que ya no participa (FT 20-sep-2026) | BIS (discurso); FT vía The Standard | 2024/2026 | EN | extracto / secundaria (ver R01P) |
| IMF Notes 26/01 "Tokenized Finance" (abril 2026) | eLibrary IMF (título en buscador) | abr-2026 | EN | extracto |

## Qué está sin verificar o es opinión
- **"Agorá = CBDC mayorista de EE. UU.":** el BIS habla de *reservas tokenizadas*, no de CBDC; la NY Fed participa "de forma exploratoria" y el texto de Waller (confirmando que EE. UU. seguirá) viene de Ledger Insights sin fecha clara. Cato argumenta que la distinción es fina: **opinión**.
- **"Nexus en producción en 2026":** el único plazo hallado es de marzo 2024 (BSP, julio 2026); **sin confirmación**. [VERIFICAR] antes de dar fecha.
- **Cifras de stablecoins ("320 mil M$") atribuidas al BIS:** vienen de un resumen de prensa, no leídas en el informe. [VERIFICAR]
- Cifras de volumen mBridge: ver R01P (solo secundaria).
- Sesgos: KuCoin/MEXC/The Block son medios de industria con tendencia a titulares; Steelldy y Kaleido son promocionales; el banco central (BIS/BCE) promueve su propia hoja de ruta (tokenización con dinero de banco central) y compite con las stablecoins privadas: **conflicto de interés institucional**.

## Caso alcista / caso bajista
**Alcista (para infraestructura de liquidación tokenizada):** tres bancos centrales G10 ya probaron atómica con valor real en preparación; Pontes está vivo; el FMI reconoce que la tokenización necesita "dinero seguro" para liquidar; EE. UU. regula stablecoins con reglas de reservas, lo que legitima el sector.
**Bajista:** el BIS excluye a las stablecoins privadas del núcleo del sistema; el modelo de Agorá y Pontes se basa en **dinero de banco central y depósitos bancarios**, es decir, en rails ya existentes; el FMI avisa de que la tokenización puede amplificar crisis; las fases de valor real y de 2028 (Pontes ampliado) están lejos; la regulación del euro digital sigue sin cerrar.

## Qué cambia para los digital assets (XRP, XLM, stablecoins, CBDC, tokenización)
- **Hecho:** el liquidador elegido por bancos centrales para pagos transfronterizos mayoristas es un "libro mayor unificado" **permisionado**, con reservas y depósitos de bancos comerciales; las fuentes leídas no nombran XRP, XLM, Ripple ni Stellar.
- **Lectura mía (no recomendación):** esto reduce el espacio de los puentes de liquidez públicos en el segmento mayorista de bancos centrales y lo desplaza a *tokenización de activos y pagos no bancarios*. Para RLUSD/stablecoins reguladas, lo relevante a vigilar es la **GENIUS Act** (reglas de la Fed, comentario 60 días tras Federal Register) y si las "payment accounts" abren acceso directo a emisores [ESPECULACIÓN]. Sin efecto de precio medido.

## Fechas próximas (catalizadores) con fuente
| Fecha | Evento | Estado |
|---|---|---|
| 27-oct-2026 | Cierre de manifestaciones de interés de comercios para el piloto del euro digital | LEÍDO (BCE) |
| ~fin de nov-2026 (aprox.) | Cierre del plazo de comentarios a las propuestas GENIUS de la Fed (60 días tras publicarse en Federal Register; fecha exacta sin confirmar) | [VERIFICAR] |
| Q4-2026 | Meta de Waller para operar las "payment accounts" | secundaria [VERIFICAR] |
| fin de 2026 | Aspiración de acuerdo final del Reglamento del euro digital (UE) | secundaria |
| 2.º sem. 2027 | Inicio del piloto de 12 meses del euro digital | LEÍDO |
| 2028 | Versión ampliada de Pontes (24/7 según medios; la página BCE no la menciona) | [VERIFICAR] |
| 2029 | Posible primera emisión del euro digital | LEÍDO (condicional) |
| sin fecha | Fase de valor real de Agorá (con Banco de Canadá) | extracto |

## Qué falta por buscar
1. PDFs: informe Agorá (bis.org/publ/…), AER 2026 cap. sobre dinero y stablecoins, GFSR oct-2026 cap. 3 completo, Fed (dos propuestas del 24-sep) → Joel los descarga a `research/fuentes/` (lista final).
2. Confirmar en fuente primaria el estado de Nexus (BSP/BIS) y la fecha de "payment accounts".
3. Postura actual del Banco de Inglaterra y del Banco de Japón sobre dinero tokenizado (solo aparecen como participantes).
4. Cifra de stablecoins según el propio BIS y aclarar si 65.000 M$ del FMI es stock o flujo.
5. Estado exacto del trílogo del euro digital (Legislative Observatory) tras el verano.
