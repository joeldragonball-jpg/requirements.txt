# W08 · Auditoría de coherencia y huecos (2-nov-2026)

Alcance: trabajo hasta el 1-nov (voces.json, regulacion.json, calendario.toml, `cerebro/documentos/`), más C13 de la auditoría del 24-oct. Excluidos los informes `2026-11-02-*` de las otras sesiones. Es un muestreo con scripts y lecturas parciales, no una revisión línea a línea. `python scripts/revisar_explorador.py`: 0 avisos en 13 capas y 102 movimientos; radar con 168 celdas, 44 sin dato.

## Resumen
Sin contradicciones de cifras en lo muestreado (Brent $105 en 4T-26 en EIA/voces/calendario; DTCC–Stellar 1S-2027; euro digital 2029/piloto 2027; Sibos 2027). Los problemas están en niveles de evidencia, plazos sin actualizar y diversidad de fuentes.

## Hallazgos
| Id | Gravedad | Hallazgo | Estado |
|---|---|---|---|
| A1 | Media | **Plazos sin actualizar en `voces.json`**: v002 (DTCC «octubre de 2026») sigue «pendiente» con resultado «sin confirmación a 23-oct», pero el calendario recoge el lanzamiento hecho el 28-oct (nota de DTCC [P]). v062 (Binance, reanudar retiradas «en 48 h», plazo 1-nov) sigue «pendiente» con fecha ya pasada y sin evento en el calendario | Abierto: `voces.json` lo está editando otra sesión (W06); propuesta: v002→`cumplido` con la nota del 28-oct; v062→comprobar y marcar |
| A2 | Media | **Nivel P con frases [S] dentro**: 12 celdas P llevan una o más frases marcadas [S]/[VERIFICAR] (EE. UU. stablecoins, SG ETF, HK stablecoins/ETF/tokenización/custodia, KR stablecoins/CBDC/política, JP ley marco/tokenización/custodia). Es coherente si el P cubre el hecho principal, pero el mapa solo enseña un nivel por celda. El peor caso es **HK ETF: nivel P, sin `url`** (ETF cripto al contado US$451 M, jun-2026). Los 7 «política» P sin url no tienen etapa | Abierto: propuesta, mostrar «P + novedades S» o añadir url a HK ETF |
| A3 | Media | **C13 (enlaces del radar)**: ya no es «cero enlaces». Voces: 58 de 59 con url (falta v036, nivel R, remite a v007). Radar: 108 celdas con url; de las 105 con etapa, **96 tienen url, faltan 9**: UE ETF (S), HK ETF (P), KR ETF/fiscal (S), BR CBDC (S), ID stablecoins/ley marco (S), EG CBDC (S), ET custodia (S). Las capas de `datos.json` no se han auditado en esta pasada | Parcial: antes faltaban 23. Abierto: 9 celdas |
| A4 | Baja | v036 (nivel R) cita «Ver Higgins (v007)» como fuente: sin url ni documento. Ejemplo de fuente por remisión | Abierto |
| A5 | Media | **Diversidad de opiniones**: de 38 voces con vídeo, las 38 son del mismo canal («Despeja La X»); 21 voces no tienen vídeo (research o notas oficiales). Voces con nivel S: 26 de 59; D: 12; P: 15. La capa de opinión crítica con XRP/Ripple es escasa (7 voces de Garlinghouse/Claver/otro). Riesgo de sesgo de selección del canal | Abierto: propuesta, 2-3 canales o analistas críticos o neutrales en el próximo lote de vídeos |
| A6 | Baja | Enlaces: 34 con 403 (anti-bots, ya clasificados), 3 con 429, 1 sin respuesta (`lg.gov.cn`, APEC), 1 roto (HKMA, calendario) | **Cerrado**: HKMA reparado; ver informe W07 |
| A7 | Media | **Huecos medidos del radar**: 44 de 168 celdas sin dato. Por país: Suiza 7, Egipto 6, Canadá 6, Australia 6, Etiopía 5, Reino Unido 5, Sudáfrica 4, Indonesia 4. Capas de voces con pocas entradas: deuda 2, depósitos tokenizados 4, puentes 6; regulación 19 y tokens 16 dominan. Huecos reconocidos en el propio JSON: Egipto/Etiopía sin fuente primaria en ETF, stablecoins, tokenización, custodia y fiscal; Arabia Saudí sin research; Reino Unido y Suiza fuera de la matriz (R18) | Abierto |
| A8 | Baja | **Plazos de voces sin evento de calendario**: v006 (2030) y v054 (2027-10) son opiniones de la dirección de Ripple, sin evento propio (correcto: son [ESPECULACIÓN], no fechas); v025 (2029) está recogido en el piloto del euro digital; v012 (BIS, 2027-09) en Sibos 2027. Binance (v062) falta | Abierto solo v062 |
| A9 | Baja | Archivo desfasado: el mapa de fuentes tenía FMI como 403 y el BIS como «candidato» (ya automatizado) | **Cerrado** (W07) |

## Correcciones aplicadas (solo seguras)
1. `eventos/calendario.toml`: enlace HKMA 404 → página de notas de prensa (200).
2. `research/MAPA-DE-FUENTES.md` actualizado.
3. `research/auditorias-estado.json`: entrada nueva (A6 cerrado; el resto abierto).
No se tocó `voces.json` ni `regulacion.json` (en uso por otras sesiones).

## Propuestas (para la sesión principal o Joel)
1. A1: poner v002 en `cumplido` («DTCC Tokenization Service Goes Live», 28-oct [P]) y revisar v062.
2. A2: añadir url oficial a HK ETF (SFC) o bajarla a S; mostrar el nivel principal y el de las novedades.
3. A3: url a las 9 celdas, empezando por HK ETF y UE ETF (ESMA).
4. A5: ampliar fuentes de opinión en el próximo lote de vídeos.
5. A7: completar Suiza/Reino Unido antes que Etiopía/Egipto (mayor peso para un inversor en España) [opinión].

## Coste real aproximado
W07 + W08: unas 40 llamadas a herramientas, sin IA externa. Aproximadamente 3-4 % de la cuota semanal en conjunto (estimación; no medido con `get_usage`).

## Hallazgos abiertos
A1 (media), A2 (media), A3 (media), A4 (baja), A5 (media), A7 (media), A8 (baja, solo v062).
