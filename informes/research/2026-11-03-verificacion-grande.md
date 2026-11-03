# Verificación grande del 2 y 3-nov-2026 (plantilla `research/plantillas/verificacion.md`)

Lectura hecha el 3-nov-2026 entre ≈19:40 y 21:00 (Madrid). Etiquetas: **[P]** confirmado con fuente primaria · **[S]** solo prensa · **[DISCREPA]** distinto de lo que decía el repo · **[NO VERIFICABLE]** no se pudo leer. Sin recomendaciones de compra ni venta. No se descargó ningún archivo ni PDF; no se usaron claves.

**Alcance honesto:** esta pasada cierra los puntos de mayor impacto (tipos oficiales, cifras macro de España que sustentan el tablero, regulación cripto, Ormuz). Los 193 marcadores `[VERIFICAR]`/`[S]` de `research/fuentes-nuevas/` incluyen muchas ausencias de calendario o URLs sin localizar que no son «hechos» comprobables hoy; quedan en la sección final «No alcanzado».

## 1. Tabla de resultados

| # | Punto | El repo decía | Fuente leída (URL, fecha de lectura) | Resultado | Etiqueta | Acción |
|---|---|---|---|---|---|---|
| 1 | RBA 3-nov | 4,85 % (+25 pb, 6-3) solo por prensa (apertura 3-nov) | Comunicado oficial `rba.gov.au/media-releases/2026/mr-26-30.html` (3-nov-2026) y tabla `rba.gov.au/statistics/cash-rate/` | «increase the cash rate target by 25 basis points to 4.85 per cent»; seis a favor y tres por mantener 4,60 %. Efectivo el 4-nov. Quinta subida de 2026 (feb, mar, may, sep, nov). | **[P]** | Ninguna. El rba.gov.au ya no da «Access Denied» desde curl con User-Agent identificado. |
| 2 | Selic 13,75 vs 14,25 | Selic 13,75 % (17-sep, −25 pb) | BCB SGS 432 `api.bcb.gov.br/dados/serie/bcdata.sgs.432` (3-nov) | 14,25 hasta 5-ago · 14,00 el 6-ago · 13,75 el 17-sep. **13,75 vigente [P]**; 14,25 es el nivel de antes de agosto. La serie trae filas con fecha futura (muestra 13,75 el 4-nov): no es la decisión del Copom, que se anuncia la tarde del 4-nov. BIS: 13,75 el 27-oct. | **[P]** | Ninguna. Falta ver la decisión del 4-nov. |
| 3 | Colombia (BanRep) | 12,25 «sin cambio» el 30-oct (Portafolio [S]) | BIS WS_CBPOL: 12,25 % el 23-oct. BanRep: reto anti-bots (curl) y Chrome redirige a otra página. | El 12,25 es el último dato del BIS (23-oct, previo a la reunión del 30-oct). La decisión del 30-oct no está en fuente oficial leída. | **[S]** | Ver «Necesita Chrome o acceso». |
| 4 | BCE depósito | 2,50 % | `data-api.ecb.europa.eu` FM.B.U2.EUR.4F.KR.DFR.LEV (3-nov) | 2,25 → **2,50 % desde 16-sep-2026**. | **[P]** | Ninguna. |
| 5 | Otros tipos | Norges 4,50 · BoE 3,75 · RBNZ 2,75 · Chile 4,50 · Perú 4,25 | Norges API oficial (4,5 el 2-nov) · BIS (BoE 3,75 el 26-oct; NZ 2,75 el 23-oct; CL 4,50 el 27-oct; PE 4,25 el 27-oct) | Coinciden. Norges [P] (API del banco); el resto [P] por BIS (agregador oficial de bancos centrales). | **[P]** | Ninguna. |
| 6 | IPCA España y euro | ES sept-2026 5,0 %, EA 3,8 % | Eurostat `prc_hicp_minr` (actualizado 16-oct-2026) | ES: ago 4,6 %, **sept 5,0 %**. EA: ago 3,2 %, **sept 3,8 %**. | **[P]** | Ninguna. |
| 7 | PIB España | 1T-26 440.992; 2T-26 448.442 M€ (corriente, desest.) | INE Tempus `CNTR6597` (3-nov) | Coinciden exactamente. La variación t/t y a/a sigue sin leerse (cálculo pendiente). | **[P]** (niveles) | Ninguna. |
| 8 | Paro EPA 3T-26 | 10,18 % «según prensa [S]» | Nota de prensa INE `ine.es/dyngs/Prensa/EPA3T26.htm` (27-oct, leída 3-nov) | «La tasa de paro fue del 10,18 %, 31 centésimas más que en el anterior»; activos 25.443.800 (+169.500). | **[P]** | Quitar `[S]` en el próximo repaso (la cifra ya es primaria). |
| 9 | Paro registrado y afiliación sept-26 | 2.379.505 (+23.587); 22,4 M afiliados (+92.327) [S] | Resumen MAPA/BBVA vía búsqueda (no la nota del Ministerio). Octubre aún no localizado (se publica el 3-nov). | Cifra de septiembre coincide en prensa y en informes ministeriales de segunda mano; en el repo aparece +23.587 y la búsqueda da ≈+23.600. | **[S]** | Leer la nota de Trabajo/Seguridad Social de octubre cuando salga. |
| 10 | Hipotecas INE ago-26 (vistas) | 33.841 (+2,3 % a/a), importe medio 181,3 mil €, tipo 3,08 % | INE Tempus HPT34618, HPT34565, HPT64408 (3-nov) | 33.841 vs 33.065 (+2,35 %); importe 6.134.856 mil € → 181,3 mil € (168,4 hace 12 m); tipo medio 3,08 % (2,88 % hace 12 m). Provisional. | **[P]** | Ninguna. |
| 11 | Deuda AAPP y CCAA 2T-26 | AAPP 101,4 % PIB; CCAA 20,4 % (355.241 M€); AAPP 1.762.936 M€ | Banco de España `bde.es/.../deuda-aapp-2026t2.html` (30-sep-2026) | Titular: «101,4 % del PIB, 1,8 pp menos que hace un año»; CCAA 20,4 %; Administración Central 92,8 %. Los importes en M€ no están en el HTML (están en la nota PDF). | **[P]** (porcentajes) / importes **[S]** | Ninguna. PDF de la nota: ver «Necesita OK de descarga». |
| 12 | DANA: fallecidos | 229 (aniversario 2025), 232 (auto de Catarroja, sept-2026), 237 (Defensor del Pueblo) | Búsqueda: moncloa.com (no oficial) para 232; mallorcadiario y otros para 237; Generalitat 229 (nov-2025) | Siguen tres cifras que no son contradictorias por sí solas (distinto criterio: lista judicial vs. suma de comunidades). El auto no se ha leído. | **[S]** | Ninguna: el informe H ya los separa. Pendiente el auto (CENDOJ/CGPJ). |
| 13 | Cloture CLARITY 49-50 | 49-50 el 15-sep-2026, «cloture» sin Demócratas (W05) | `senate.gov` roll call nº 234 → curl 403; Chrome: «Unauthorized: potential security risk». Prensa (The Defiant, Blockonomi, Coingape): 49 a favor (todos republicanos), 50 en contra, Coons sin voto; Tillis pidió reconsiderar; sin nueva votación a finales de oct. | No se pudo leer la fuente oficial. Prensa coherente en cifras y fecha (un titular erróneo dice «febrero»). | **[S]** | No saltar el bloqueo. Ver «Necesita Chrome o acceso». |
| 14 | Recompensas de stablecoins (CLARITY, compromiso de mayo) | «no consta como ley» | Sin texto de ley leído; la votación de cloture falló, luego no hay ley | Coherente con que la CLARITY sigue sin aprobarse. El contenido exacto del compromiso de mayo sigue solo en prensa. | **[S]** | Ninguna. |
| 15 | XRPL XLS-65/66 | «en votación, no activo» [VERIFICAR hoy] | Nodo público `s1.ripple.com:51234` método `feature` (3-nov) | **`LendingProtocol` y `SingleAssetVault`: `enabled = false`, `supported = true`** (el servidor los soporta pero la red no los ha activado). `fixCleanup3_2_0` y `fixCleanup3_3_0` sí activos. Hay `LendingProtocolV1_1` sin soporte. | **[P]** | Ninguna. El estado «no activo» queda confirmado el 3-nov. |
| 16 | ESMA y préstamo cripto | Q&A 2883 (18-jun-2026): MiCA no regula el préstamo (considerando 94) | `esma.europa.eu/publications-data/questions-answers/2883` (3-nov) | Texto confirmado: «MiCA does not address the lending and borrowing of crypto-assets (Recital 94)»; los CASP siguen sujetos a obligaciones generales; la salvaguarda MiCA no cubre lo prestado. Además, la respuesta de ESMA a la revisión de MiCA es del 30-sep-2026 (staking: reglas proporcionadas; préstamo: «black boxes»; prensa [S]). | **[P]** (Q&A 2883) | Ninguna. |
| 17 | Japón: FIEA | Pasó la Cámara Baja el 11-jun; «falta la Alta» (C42) | Búsqueda en japonés: Kyodo vía Kumanichi («改正法成立»), PwC Japón (28-jul), all-senmonka; tftc, sumsub. No se leyó la Dieta ni la FSA (las páginas no devolvieron texto útil). | **Aprobada por la Cámara Alta el 15-jul-2026** y convertida en ley según varias fuentes coincidentes: las cripto pasan de la Ley de Servicios de Pago a la FIEA. Vigencia 2027 (o dentro de un año desde la promulgación). El 20 % de tributación separada es otra ley (se prevé 2028). Una fuente en inglés dijo no poder reconciliarlo con la página de la FSA. | **[DISCREPA]** (el repo decía «falta la Alta») | **Corregido** (ver §2). La etiqueta pasa a [S]: texto final sin leer. |
| 18 | «Irán reabriría Ormuz en dos días» (2-nov) | «sin contrastar» | Al Jazeera 2-nov-2026 «Trump signals progress on Iran deal as Tehran pushes faster ceasefire»; investinglive; IBTimes; Seoul Economic Daily; Benzinga | Iran dice que puede reabrir el estrecho en **dos días** (antes eran siete) con mediación de Qatar, **si EE. UU. acepta condiciones** (levantar sanciones, fin del bloqueo naval, etc.). EE. UU. **no** las ha aceptado; Trump dice «no hay prisa». Brent −7,6 % a 104,77 $ y WTI −7,2 % a 96,63 $ según un despacho; otros dan −6 %. | **[S]** (es una declaración de Irán; la reapertura NO ocurrió) | Anotado en `verificados.json` como confirmado el hecho de la oferta. |
| 19 | «EE. UU. ataca objetivos iraníes en Ormuz» (3-nov) | «sin contrastar» (titular Google News) | CENTCOM (`centcom.mil`): los comunicados más recientes que aparecen son de julio-sept; Al Jazeera 3-nov: titulares sobre «Iran baulks at US reply» y propuestas de Qatar, sin ataque nuevo; varias búsquedas sin ninguna noticia del 3-nov. | No hay confirmación de ataque nuevo del 3-nov. Los ataques conocidos son anteriores (jul-sept). Probable titular reciclado o ubicado mal en fecha. | **[NO VERIFICABLE]** / dudoso | `verificados.json`: dudoso. No usar en el tablero hasta ver comunicado de CENTCOM. |
| 20 | Elecciones EE. UU. 3-nov | Solo hechos conocidos | No se buscaron resultados (aún no hay definitivos) | No aplica. | — | Ninguna. |

## 2. Correcciones aplicadas (antes → después)

1. `informes/research/2026-11-02-C42-rendimientos-colateral.md`, línea 60:
   - Antes: «pasó la Cámara Baja el 11-jun-2026; falta la Alta; vigencia…»
   - Después: se añade `[CORREGIDO 3-nov: varias fuentes (Kyodo vía Kumanichi, PwC Japón 28-jul-2026) dicen que la Cámara Alta la aprobó el 15-jul-2026, ley en vigor; ver informes/research/2026-11-03-verificacion-grande.md]` tras «falta la Alta» (no se borró el texto previo).
2. `informes/research/2026-11-02-C42-filas.json`, fila Japón, campo `estado`:
   - Antes: «…y por la Cámara Baja (11-jun-2026); falta la Cámara Alta; vigencia prevista…»
   - Después: «…y por la Cámara Baja (11-jun-2026); la Cámara Alta la aprobó el 15-jul-2026 según Kyodo/PwC Japón (S, verificación 3-nov; texto final sin leer); vigencia prevista…»
   - El `nivel` sigue «S [VERIFICAR]» y `norma` dice «(en trámite)»: **a ajustar por la sesión que vuelque C42/C39** (no se tocó el resto de campos ni `datos.json`/`paises.json`).
3. Nada más estaba «claramente mal». No se tocó `cerebro/` ni `vistas.html`/`paneles.html`.

## 3. Necesita Chrome o acceso

- **Chrome estado:** la extensión Claude in Chrome SÍ estaba conectada (se creó un grupo de pestañas propio). Se usó **una vez por fuente**:
  - `senate.gov` roll call nº 234 (cloture CLARITY): bloqueada también en Chrome («Unauthorized: potential security risk», referencia 18.b8593a17…). No se saltó. Alternativa: que Joel abra a mano `https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00234.htm` en su navegador, o leer el registro en `congress.gov` (la API pide clave gratuita, sin usar).
  - `banrep.gov.co` (decisión del 30-oct y tipo vigente): reto anti-bots; Chrome redirigió a otra página y falló la lectura. Alternativa: nota de la Junta Directiva en la web o el comunicado en la página de prensa; pendiente de prueba manual de Joel.
- **Sin acceso útil desde curl:** FSA Japón y las páginas de la Dieta (no devolvieron texto), Notarios (404), MIVAU (403), INE `SERIES_OPERACION/293` (tiempo agotado: la tasa de paro viva se leyó en la nota de prensa).
- Pendiente de comprobar con Chrome (no se hizo por falta de tiempo): BCCh/BCRP calendarios; RBNZ bloquea Chrome según la fuente A.

## 4. Necesita OK de descarga (no descargados)

| Archivo | URL | Nombre sugerido en `research/fuentes/` | Para qué |
|---|---|---|---|
| Nota de prensa BdE «Deuda AAPP 2T-2026» | `https://www.bde.es/f/webbe/GAP/Secciones/SalaPrensa/NotasInformativas/26/presbe2026-86.pdf` (nº por confirmar) | `bde-deuda-aapp-2026t2.pdf` | importes en M€ (1.762.936; 355.241) |
| Registradores ERI 2T-2026 | `https://www.registradores.org/documents/d/guest/eri_2t_2026` (9,3 MB) | `registradores-eri-2t-2026.pdf` | compraventas e hipotecas del 2T |
| INE EPA 3T-2026 (nota) | `https://www.ine.es/dyngs/Prensa/EPA3T26.pdf` | `ine-epa-3t26.pdf` | solo si se quiere archivar; la cifra ya es [P] por HTML |
| Resumen de empleo MAPA (septiembre) | `https://www.mapa.gob.es/es/dam/jcr:08e79425-b9ac-4236-9f41-bd41ce2aa4df/AyP_Serie_Empleo_n176_EPA_3T2026_CON%20CREDITOS_TRIM.b20c023e819426d8d4124c440bbf42c8.pdf` | `mapa-empleo-n176.pdf` | contraste secundario |
| Auto del Juzgado de Catarroja (DANA) | por localizar en CENDOJ/CGPJ | `catarroja-auto-dana-232.pdf` | fijar la cifra judicial |

## 5. No alcanzado (queda abierto)

- **España:** recaudación frente a infraestructuras (I), opacidad contrato-factura (J), DANA por municipio (H: defunciones semanales INE, MNP, ES-Alert 17:35), sueldos C68/C68B, C69 (IGAE 2024-25), SEPE/Seguridad Social octubre, IPC INE vivo (códigos de base nueva), tasas t/t y a/a del PIB.
- **Tipos:** calendarios 2026-27 que dependen de web por JS (BoC, Norges, RBNZ, Banxico, BCCh, BCRP, Copom); decisión del Copom del 4-nov; BoE 5-nov.
- **Regulación:** compromiso de mayo de CLARITY sobre rewards (texto), FIEA (texto final), XRPL staking/AMM TVL (R43), DGT V0648-24, DAC8, escala del ahorro 2026 (W05).
- **Petróleo:** cierre Brent/WTI del 3-nov y estado real del bloqueo naval.
- **Elecciones EE. UU.:** esperar a los resultados oficiales (Cámara de Representantes 4-nov).
- **Ripple:** precios de adquisiciones sin precio publicado; Chainlink CCIP en SWIFT [VERIFICAR] siguen igual.

## 6. Lecciones (máx. 5 líneas)
- `rba.gov.au` y el BIS/SGS/Eurostat/INE/BdE/ECB/ESMA se leen bien con curl y User-Agent identificado; `senate.gov` y `banrep.gov.co` bloquean también a Chrome: no insistir.
- La serie SGS 432 del BCB trae filas futuras; la decisión del Copom no está hasta la tarde del día 4.
- Para estado de enmiendas XRPL, `feature` en un nodo público es primaria y gratis.
- Una búsqueda en el idioma original (japonés) resolvió lo que el inglés dejó contradictorio.
