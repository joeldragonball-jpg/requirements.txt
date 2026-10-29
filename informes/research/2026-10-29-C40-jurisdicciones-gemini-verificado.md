# C40 · Jurisdicciones fuera del radar: Reino Unido, Suiza, Canadá, Australia y Arabia Saudí (Gemini Deep Research, verificado por Claude)

Hecho el 29-oct-2026. El crudo de Gemini está en `informes/gemini/2026-10-29-DR-jurisdicciones-fuera-del-radar.md` (sin verificar). Aquí: qué datos comprobé en la fuente primaria, qué corrijo, y las celdas que propongo para `explorador/regulacion.json` (NO añadidas sin tu OK). Sin recomendaciones de compra/venta. Etiquetas: [P] leído en la fuente oficial; [S] prensa o despacho; [VERIFICAR] sin comprobar.

## 1. Verificación (6 datos contra fuente primaria, todos leídos hoy)
| # | Afirmación de Gemini | Resultado | Fuente |
|---|---|---|---|
| 1 | Banco de Canadá sube a 2,50 % el 28-oct; próxima decisión 9-dic | **Confirmado [P]** (el 2,50 % y la subida de 25 pb; la fecha 9-dic figura en su calendario 2026) | bankofcanada.ca, tipo objetivo a un día |
| 2 | RBA sube el cash rate a 4,60 % el 29-sep-2026 | **Confirmado [P]**: «increase the cash rate target by 25 basis points to 4.60 per cent»; el comunicado cita la ampliación del conflicto en Oriente Medio y la energía | rba.gov.au, Media Release 2026-27, 29-sep-2026 |
| 3 | SNB mantiene 0 % el 24-sep-2026 | **Confirmado [P]**: «leaves SNB policy rate unchanged at 0 %»; descuento de 0,25 pp sobre los depósitos por encima del umbral; dispuesto a intervenir en divisas. Inflación «ha subido desde junio» por la energía (la cifra de 0,8 % no se leyó) | snb.ch, evaluación del 24-sep-2026 |
| 4 | Banco de Inglaterra mantiene 3,75 % (voto 6–3); próxima: 5-nov | **Confirmado [P]**: 6–3, tres miembros querían subir a 4 %; «Next due: 5 November 2026» | bankofengland.co.uk, resumen de política monetaria del 17-sep-2026 |
| 5 | FCA: régimen cripto en vigor el 25-oct-2027; ventana de solicitudes hasta el 28-feb-2027 | **Confirmado [P]**: la ventana abrió el 30-sep-2026 y cierra el 28-feb-2027 (para quien quiera acogerse a las disposiciones transitorias); el régimen empieza el 25-oct-2027. **Corrección:** PS26/18 es la guía de perímetro («Cryptoasset Perimeter Guidance», sep-2026), con apartados sobre stablecoins del Reino Unido (UKQS); la descripción de Gemini («régimen conjunto FCA/BoE… prohibiendo fondos de respaldo no asignados») no figura en la parte leída y queda [VERIFICAR]. CP26/36 (oct-2026) es una consulta sobre más guía de perímetro (descentralización, salvaguarda, stablecoins, creadores de mercado) | fca.org.uk, PS26/18 y CP26/36 (PDF) |
| 6 | Canadá: ETF de XRP con prospectos aprobados por la CSA | **Confirmado [P] y más detallado**: tras el lanzamiento de futuros de XRP del CME (19-may-2025), la CSA dio recibo a los primeros ETF de XRP al contado de Norteamérica; **tres gestoras recibieron el prospecto definitivo y cotizan en la TSX desde el 16-jun-2025**; no hacen staking | osc.ca, OSC Staff Notice 81-741, 15-sep-2026 |

**Dato dudoso:** Arabia Saudí, repo SAMA 4,50 %. El propio Gemini dice que replica a la Fed; con el rango de la Fed en 3,75–4,00 % tras el 16-sep, 4,50 % no cuadra (si sigue el límite superior sería ≈ 4,00 %). Marcado [VERIFICAR]; no se usa. Además la fuente citada para el Proyecto Aber (centralbank.ae, 2020) es un informe de los Emiratos de 2020, no una nota actual de SAMA.

## 2. Qué se salva y qué no del crudo
- **Se salva [P]:** los cinco tipos oficiales de arriba (Reino Unido 3,75 %, Suiza 0 %, Canadá 2,50 %, Australia 4,60 %) con su fecha y próxima cita; el calendario FCA; los ETF de XRP en Canadá.
- **Queda [S]:** ETF cripto del Reino Unido (cETN profesionales, de 2024, vía dailycoin: tema antiguo y de agregador); fiscalidad de Canadá (CRA, 2023) y Australia (ATO) sin fecha de revisión; tokenización de Reino Unido (DLA Piper).
- **Huecos que Gemini declara y siguen abiertos:** CBDC del Reino Unido, Suiza, Canadá y Australia; ETF cripto en Suiza, Australia y Arabia Saudí; fiscalidad de Suiza; XRP/XLM en Reino Unido, Suiza y Arabia Saudí; calendario de SAMA.
- **Hallazgo ASIC sobre «Ripple NSW Pty Ltd»:** es un aviso sobre una empresa con ese nombre; no prueba relación con Ripple Labs. [VERIFICAR] antes de tomarlo como dato de Ripple.
- **Sesgos:** la mayoría de los enlaces de «ley marco» son despachos de abogados (LawBEAM, DLA Piper) con interés comercial; la prensa australiana usa lenguaje alarmista sobre el RBA.

## 3. Celdas propuestas para `explorador/regulacion.json` (pendiente de tu OK)
Jurisdicciones nuevas: `uk` (GB), `ch` (CH), `ca` (CA), `au` (AU); Arabia Saudí (`sa`) queda fuera hasta tener fuente actual de SAMA. Solo propongo celdas con dato [P] leído hoy:

| jur | tema | etapa | valor / estado (resumen) | fecha | próxima |
|---|---|---|---|---|---|
| uk | politica | 4 | Bank Rate 3,75 % (6–3, tres querían subir a 4 %), mantiene | 2026-09-17 | 2026-11-05, decisión del BoE |
| ch | politica | 4 | Tipo SNB 0 %, sin cambio; dispuesto a intervenir en divisas | 2026-09-24 | 2026-12-10 [S: calendario de agregador; falta leerlo en snb.ch] |
| ca | politica | 4 | Tipo a un día 2,50 % (+25 pb) | 2026-10-28 | 2026-12-09 |
| au | politica | 4 | Cash rate 4,60 % (+25 pb) | 2026-09-29 | 2026-11-03 |
| uk | ley_marco | 3 | Reglamento FSMA (Cryptoassets) 2026: en vigor el 25-oct-2027; ventana de solicitudes 30-sep-2026 a 28-feb-2027 | 2026-10 | 2027-02-28 |
| ca | etf | 4 | ETF de XRP al contado cotizando en la TSX desde el 16-jun-2025 (tres gestoras) | 2026-09-15 | — |

Si dices «sí, añádelas», las creo con `nivel: P`, `revisado: 2026-10-29` y los enlaces de arriba, y corro `revisar_explorador.py`. Si prefieres solo las de política monetaria (las más sólidas y cortas), añado esas cuatro.

## 4. Contraste alcista / bajista para un tenedor de XRP y XLM
- **Alcista:** Canadá ya tiene ETF de XRP al contado desde junio de 2025 (acceso regulado); el Reino Unido fija una fecha clara (25-oct-2027) y una ventana de autorización; Suiza ofrece seguridad jurídica para tokenización y custodia (según Gemini, sin leer FINMA hoy).
- **Bajista:** tres de las cuatro economías subieron o presionan al alza los tipos (Canadá y Australia subieron; en el Reino Unido tres miembros del comité querían subir), con energía cara: condiciones financieras más duras; el régimen británico exige autorización a las plataformas que sirvan a residentes y puede fragmentar el acceso.
- **No concluyente:** XRP/XLM en el Reino Unido, Suiza, Australia y Arabia Saudí sin hechos verificados.

## 5. Coste y notas de método
- Gemini Deep Research: 1 consulta (anotada en `research/gemini-uso.json`). Verificación por Claude: ~6 lecturas de fuentes oficiales (RBA, SNB, BoE y BoC en Chrome; FCA y OSC en PDF).
- Lección: rba.gov.au da 403 a curl pero abre en Chrome (sin saltar controles); y la fuente que Gemini cita para el Proyecto Aber es de otro país y año (Emiratos, 2020). El criterio fue abrir cada enlace en la sesión y no fiarse del resumen de Gemini.
