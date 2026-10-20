# Auditoría de los informes de Gemini T01 (CLARITY), T02 (GENIUS) y T04 (euro digital) — 2026-10-20

Se auditan las versiones verificadas del repo (`informes/gemini/2026-10-18-T0*.md`; **no se tocan**) contra el repo y contra fuentes abiertas hoy. Los originales de Gemini están en Drive y no se han releído. Etiquetas: [P] / [S] / [VERIFICAR] / [ESPECULACIÓN]. Sin recomendaciones de compra/venta.

## Resumen (5 líneas)
1. **11 hallazgos.** Ningún error grave de hecho: las tres verificaciones aguantan en lo esencial.
2. **Dos [VERIFICAR] de T02 y T04 quedan resueltos con fuente primaria:**
   - La OCC publicó el boletín el **25-feb-2026** y la propuesta salió en el Federal Register el **2-mar-2026** (91 FR 10202).
   - Los **36 proveedores** del piloto del euro digital salen de una **nota del BCE del 14-jul-2026**, no del discurso de Cipollone.
3. **T01 se queda corto en la causa del fallo de CLARITY:** atribuye todo a la ética con una sola fuente, y otras fuentes añaden stablecoins y alineación con la Cámara. Además hay un conflicto sobre los cuatro republicanos del «no»: Collins (registro del Senado) o Rand Paul (Reuters).
4. **Etiquetas:** T04 pone [P] a un dato que el BCE publica en otra nota (correcto, pero mal citado). T02 marca [P] el boletín sin fecha de comentarios. T01 deja la moción de Tillis «sin fecha», y otra fuente la data el 15-sep a las 15:01.
5. Una afirmación de T04 sin fuente útil, «el límite está fijado en cero para los comercios» (OMFIF), queda **[VERIFICAR]**.

## Hallazgos
| # | Informe | Tipo | Hallazgo | Fuente abierta hoy | Propuesta |
|---|---|---|---|---|---|
| 1 | T01 | Fecha | T01 dice que la moción de Tillis «no tiene fecha» porque el artículo de FinTech Weekly no la da. Otra fuente la sitúa el **15-sep-2026 a las 15:01**, tras votar no por motivo procedimental | The Defiant (vía buscador) [S] | Fechar la moción el 15-sep [S] (el radar ya lo hace) |
| 2 | T01 | Causa incompleta | «La disputa fue sobre ética» viene de una sola fuente. Otras añaden stablecoins y alineación con la Cámara; una dice que Tillis estaba satisfecho con la ética pactada con la Casa Blanca | CryptoSlate, Bitcoin.com, StockTwits (vía buscador) [S] | Redactar «la ética fue el principal escollo, no el único» [S] |
| 3 | T01 | Contradicción entre fuentes | Republicanos del «no»: Collins, Hawley, Moran y Tillis según el registro del Senado citado por prensa; Reuters habría nombrado a Rand Paul en lugar de Collins. Coons (D) no votó: 49 + 50 = 99 | Spaziocrypto, Bitrue (vía buscador) [S]; registro del Senado no abierto | [VERIFICAR] en senate.gov (roll call) |
| 4 | T01 | Etiqueta | La valoración «prevalece la postura de los despachos» ya va como [ESPECULACIÓN]. Correcto | — | Sin cambios |
| 5 | T02 | **[VERIFICAR] resuelto** | Boletín OCC 2026-3 fechado el **25-feb-2026** (leído); la propuesta aparece en el Federal Register el **2-mar-2026**, documento 2026-04089, 91 FR 10202 (URL y PDF en occ.gov) | occ.gov (leído) [P]; federalregister.gov (URL con fecha, vía buscador) [P] | Cerrar el [VERIFICAR]: 25-feb es el anuncio y 2-mar la publicación |
| 6 | T02 | Afirmación no sostenida | «Diferencia estrictamente el capital operativo de las reservas 1:1»: el boletín lista «Reserve assets» y «Capital and operational backstop» sin cifras. **Confirma a T02**: no hay 1:1 en el boletín | occ.gov [P] | Mantener [VERIFICAR] hasta leer el texto del Federal Register |
| 7 | T02 | Dato nuevo | Plazo de redención: el proyecto fijaría en general un **máximo de dos días hábiles** (§ 15.12), según el resumen del buscador | Buscador sobre occ.gov y federalregister.gov [S] | Añadir como [S] si se usa |
| 8 | T02 | Etiqueta | El boletín no da fecha límite de comentarios: T02 no la pone (correcto), pero el radar dice «comentarios cerrados el 1-may», que sale del dossier de stablecoins | Dossier Stablecoins 9-oct [P] | Coherente; sin cambios |
| 9 | T04 | **Fuente mal citada** | Los **36 proveedores** y el «piloto de 12 meses en el 2S-2027» están en la **nota de prensa del BCE del 14-jul-2026** (más de 50 solicitudes; lista añadida el 15-sep). T04 los atribuye al discurso de Cipollone | ecb.europa.eu, nota del 14-jul-2026 (leída) [P] | Citar la nota del BCE como fuente primaria |
| 10 | T04 | Año inferido | «Trílogos desde el 13-jul-2026»: OMFIF dice «13 de julio» sin año explícito; el año es inferencia (coherente con el mandato del 9-jul-2026) | — | Dejar [S] con nota de año inferido |
| 11 | T04 | Sin fuente | «El límite está fijado en cero para los comercios» (OMFIF): ni la nota del BCE ni otra fuente lo recogen | ecb.europa.eu (sin mención de límites) | **[VERIFICAR]** |

## ¿Fechas mal atribuidas o etiquetas demasiado generosas?
- **Mal atribuidas:**
  - T01: moción de Tillis «23-sep» en Gemini; T01 la dejó «sin fecha» y la fecha correcta parece el 15-sep.
  - T04: discurso de Cipollone 13-oct (publicación) frente a 6-oct (pronunciado); T04 ya lo corrige.
  - T02: OCC 25-feb (boletín) frente a 2-mar (Federal Register); **resuelto**.
- **Demasiado generosas:** ninguna grave. Los tres informes ya entran como [S] por defecto. El caso discutible es T04 #4 ([P] por el discurso), que es correcto en el dato pero no en la fuente original.
- **Sin fuente:** T04 #11 y el «techo de tenencia que exige el Consejo» (T04, ya [VERIFICAR]). El radar v2 lo daba como hecho y se marca [S] en la auditoría del Explorador.

## Páginas que no abrieron
- consilium.europa.eu (403, ya anotado).
- federalregister.gov (redirige a una página de desbloqueo; no se siguió, como en T02).
- La nota de FinTech Weekly no apareció en el buscador; su contenido coincide con otras fuentes.
- El webcast de MNI no se encontró.

## Fuentes
[OCC Bulletin 2026-3](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-3.html) · [Federal Register 2026-04089](https://www.federalregister.gov/documents/2026/03/02/2026-04089/implementing-the-guiding-and-establishing-national-innovation-for-us-stablecoins-act-for-the) · [BCE, nota del 14-jul-2026](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260714~8cd07d9d45.en.html) · [BCE, página del piloto](https://www.ecb.europa.eu/paym/digital_euro/pilot/html/index.en.html) · [The Defiant](https://thedefiant.io/news/regulation/senate-blocks-clarity-act-49-50-with-no-democratic-votes-to-proceed) · [CryptoSlate](https://cryptoslate.com/clarity-act-needs-3-more-senators-and-a-race-against-the-clock-for-a-2026-revival/) · [Spaziocrypto](https://en.spaziocrypto.com/usa/clarity-act-senate-vote-fails-49-50-cloture-threshold/) · [Bitcoin.com](https://news.bitcoin.com/clarity-act-republican-senators-fail-white-house-ethics/) · [StockTwits](https://stocktwits.com/news-articles/markets/equity/clarity-act-thom-tillis-white-house-ethics-senate-vote-coinbase-circle/cZt72BCRJz4)
