# Auditoría 2-nov-2026 (tras W08): CLARITY 404, C71/C72, Gemini elecciones, BIS JP/CN, «De dónde sale»

Etiquetas: [P] fuente primaria leída hoy · [S] prensa/agregador · [VERIFICAR] · [ESPECULACIÓN]. Sin recomendaciones.
Commits revisados: fa069d3 (W05b), bda6ade (Gemini elecciones), 32b4139 (C71), 6cfaf41 (C72). Sin commit ni push; sin API de Anthropic.
No se tocaron: research/COLA.md, research/tareas.csv, movil, seguimiento, PLANNING, paneles.html/json, scripts (C72-C74 en paralelo).

## Hallazgos por severidad

### MEDIA
1. **CLARITY «sección 404»: conclusión de W05b a medias.** Lo [P] se confirma: descargué de nuevo los textos de govinfo (EH y RFS). SEC. 404 = «Registration of digital commodity exchanges»; «yield» e «interest or yield» = 0; «payment stablecoin» = 76; RFS recibido en el Senado el 18-sep-2025 (cuadra). Pero la frase «sería del borrador del Senado (Lummis, 14-sep-2026), con otra numeración» es [ESPECULACIÓN] y la prensa la contradice: la «Section 404» sobre rendimiento de stablecoins es la del texto de compromiso del Senado Tillis–Alsobrooks, publicado el 1-may-2026 [S: The Block; Consumer Federation of America, 8-may-2026; carta de ABA/ICBA]. El número 404 sí existe, pero en el texto del Senado, no en el de la Cámara. Además la CFA sostiene que ese texto en la práctica deja legales varias formas de rendimiento [S, opinión], así que «prohíbe» a secas exagera.
   - Fuentes: https://www.govinfo.gov/content/pkg/BILLS-119hr3633rfs/html/BILLS-119hr3633rfs.htm · https://consumerfed.org/clarity-act-section-404-ban-on-stablecoin-yield-not-found/ · https://www.theblock.co/post/408144/us-banking-groups-urge-stablecoin-provisions-clarity-act · https://www.theblock.co/post/399780/coinbase-says-deal-reached-on-clarity-act-stablecoin-yield-clearing-path-to-long-stalled-senate-markup
   - Coherencia: W05b añadió su nota solo a `cerebro/apuntes_xrp_macro_fiscalidad_2026.md`, que está marcado HISTÓRICO; el estado vigente (`cerebro/documentos/resumen-vigente-xrp.md`, línea 136) seguía diciendo «[VERIFICAR] en congress.gov» sin el resultado. Corregido con notas añadidas (abajo).
2. **«De dónde sale» → Inflación dice «BCE», pero el código descarga Eurostat** (`prc_hicp_minr`, vía `indicadores._eurostat`) para zona euro y España. Lo mismo en `paneles.json → inflacion.fuente`. Hay que cambiar «BCE» por «Eurostat» en `PROC.inflacion` (paneles.html, línea 420) y en el texto de fuente de `leer_inflacion`. No lo toqué: paneles.html y el script los está editando el agente de C72.
3. **C71 no tiene informe.** Solo hay una nota en `research/tareas.csv` (fila C71). Ningún `informes/research/2026-11-02-C71-*.md` con cifras, fuentes y fechas. Las 8 series del BCE se comprueban en el propio JSON, pero no hay lectura escrita ni avisos.

### BAJA
4. «De dónde sale», omisiones frente al código: **Bonos** no cita al Banco de España (`URL_BDE`, app.bde.es); **Deuda** no cita al Banco de Inglaterra (`URL_BOE`); **Liquidez** no cita las cifras manuales de M2 de Japón (BoJ, PDF) y China (PBoC vía prensa, [S]); **Indicadores** no cita las cifras manuales (p. ej. IPC de Japón vía investinglive [S], paro de China vía prensa [VERIFICAR]). El resto cuadra: TIC (ticdata.treasury.gov), DefiLlama, CoinGecko, Yahoo (índices, materias, watchlist), tipos al día (NY Fed, BCE, BoE, BCB, BoC), BIS (WS_CBPOL), Banco Mundial (defensa), PortWatch (servidor ArcGIS del FMI), crédito (BCE + Freddie Mac + BoE). «Sin claves»: correcto (no hay variables de entorno ni API keys en el script). Cadencia «L-V 21:30 UTC»: cuadra con `paneles.yml` (cron 30 21 * * 1-5).
5. `paneles.json → credito`: `fuente` global = BCE y `nivel` = P, aunque ahora incluye Freddie Mac y BoE. Menor (las tres son primarias), pero la fuente global se queda corta.
6. Código muerto: `fred_oecd()` en `leer_inflacion` ya no se usa tras pasar JP/CN al BIS.
7. Crédito a hogares en España (BSI): la serie trae un hueco en jun-2026 (3,22 % entre 4,90 % y 4,96 %). **Es así en la API del BCE** (comprobado hoy [P]), no un error del script. Causa sin explicar (¿reclasificación o venta de cartera?) [VERIFICAR]. Conviene un aviso en el panel.
8. Gemini elecciones: la pieza de `noticias/manuales/` dice «218 R frente a 212 D con 4 vacantes: necesitan +3». La cuenta no sale con la Cámara actual (212 + 3 = 215 < 218): el «+3» de Ballotpedia se mide desde el resultado de 2024 (215 D), no desde hoy. Es coherente con el informe de Gemini, pero hay que aclararlo [VERIFICAR en Ballotpedia; hoy no se dejó leer de forma automática]. El resto es coherente entre `informes/gemini/` y `noticias/manuales/`: 35 escaños (33 + 2 especiales), 53 R / 45 D + 2 independientes, 12 reñidos (no 13), etiqueta [S] y Ballotpedia como agregador. La certificación «semanas» queda fuera de la pieza manual (bien, estaba [VERIFICAR]).

### OK (sin cambios)
- **C72** (`informes/research/2026-11-02-C72-credito.md`): Freddie Mac comprobado hoy en el CSV PMMS [P]: 7,24 % (29-oct-2026), 7,32 % (22-oct), 7,40 % (15-oct y 8-oct), 6,17 % (30-oct-2025). Reino Unido: la serie del JSON da 3,93 % en ene-2026 → 5,13 % en sep-2026 y aprobaciones 66.277 → 53.443 (−19,4 %). Cuadra con el informe. Etiquetas y avisos de método correctos; lo pendiente (Fed H.8, BoJ) queda bien marcado.
- **Inflación JP/CN vía BIS** (WS_LONG_CPI, comprobado hoy): Japón 120,649/118,170 = +2,1 % (sep) y +1,9 % (ago); China +0,9 % (sep) y +0,8 % (ago). Coincide con el panel. El índice de Japón de ago = sep (120,649287) se confirma: el aviso de «posible arrastre» de W05b sigue en pie [VERIFICAR con la Oficina de Estadística de Japón]. Nota: el panel de indicadores muestra el IPC subyacente de Japón (sin alimentos frescos, ago 1,7 %), que no es comparable con el 1,9 % general del BIS. No es un error, pero son dos series distintas.

## Qué se corrigió (solo añadido; nada borrado ni reescrito)
- `cerebro/apuntes_xrp_macro_fiscalidad_2026.md`: nota de corrección al final (404 = compromiso Tillis–Alsobrooks [S]; «otra numeración» = [ESPECULACIÓN]; matiz de la CFA).
- `cerebro/documentos/resumen-vigente-xrp.md`: nota al final con el resultado de W05b + esta auditoría.
- `cerebro/documentos/blackrock-efectivo-tokenizado-y-stablecoins.md`: nota de que su «VERIFICADO vía Baker McKenzie» es [S], no el texto oficial.

## Queda [VERIFICAR]
- Texto oficial del compromiso Tillis–Alsobrooks (sección 404) y qué borrador del Senado sigue vivo (Lummis 14-sep frente al de mayo).
- Cloture 49-50 del 15-sep-2026 (senate.gov bloqueado).
- IPC de Japón de ago-2026 frente a sep-2026 en la fuente oficial (estat.go.jp).
- Causa del hueco de jun-2026 en el crédito a hogares de España (BCE, BSI).
- Base del «+3» en la Cámara (Ballotpedia) y plazos de certificación (Times of India sin abrir).

## Para quien siga (sin tocar ahora por los agentes en paralelo)
- `explorador/paneles.html` → `PROC`: inflación «BCE» → «Eurostat»; añadir BdE en Bonos, BoE en Deuda y «cifras manuales» en Liquidez e Indicadores.
- `scripts/actualizar_paneles.py`: borrar `fred_oecd` si no se va a usar; fuente de `inflacion` → Eurostat.
- Escribir `informes/research/2026-11-02-C71-credito-materias.md` con las cifras del panel y sus fechas.
