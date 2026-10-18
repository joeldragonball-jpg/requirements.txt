# Cruce de las fichas del analista (8 capas del Explorador) con dossiers, apuntes y vídeos

Fecha: 2026-10-19 · Sin búsquedas web ni API: solo documentos del repo · Sin recomendaciones de compra/venta.

**Qué se ha cruzado.** Las fichas de `explorador/datos.json` salieron de los informes R25, R26, R27, R29, R40, R43 y R44 (17-oct). Aquí se contrastan con:
- **Dossiers del 9-oct** (`informes/dossiers/`): Euro digital y CBDC, Stablecoins, Tokenización de fondos y deuda, Stellar RWA y DTCC, Infraestructura on-chain, ETF cripto, CLARITY Act, Macro, Custodia y seguridad, Pagos transfronterizos y Evernorth.
- **Apuntes del cerebro** (`cerebro/documentos/` y `cerebro/apuntes_xrp_macro_fiscalidad_2026.md`, este último solo con búsquedas).
- **Vídeos** (`informes/videos/`, los cinco del canal Despeja La X, 7-oct). Solo sirven de contraste: son un único canal con posición declarada en XRP y XLM, titulares de gancho y conclusiones de precio sin datos. Que coincidan entre sí no cuenta como confirmación.

**Cómo leerlo.** Los dossiers son de hace 10 días. Una cifra distinta no es siempre una contradicción: muchas veces es la misma serie medida en otra fecha. Solo se marcan como contradicción los casos en los que no hay forma de que las dos cosas sean ciertas a la vez, o en los que la ficha dice más que su fuente.

## 1. Contradicciones y afirmaciones que necesitan corrección

| # | Capa | Qué dice la ficha | Qué dice el otro documento | Conclusión |
|---|---|---|---|---|
| 1 | CBDC | «Falta la posición del Consejo» sobre el euro digital (R40) | El dossier Euro digital (9-oct) y el apunte `euro-digital-calendario-y-pontes` dicen que el Consejo fijó su posición el **19-dic-2025** (secundaria, comunicado no leído, 403) | No pueden ser ciertas las dos. R40 se basa en que el Observatorio legislativo no la muestra. **[VERIFICAR]** en consilium.europa.eu. La ficha recoge las dos versiones |
| 2 | Depósitos tokenizados | Madurez: «un solo caso relevante, JPMD» (R44) | El dossier Pagos transfronterizos recoge el **libro mayor de Swift con depósitos tokenizados de 17 bancos**, en piloto desde el 9-jul-2026. El apunte grande (línea 146) dice que **BNY lanzó depósitos tokenizados el 9-ene-2026** en red privada, con Ripple Prime entre los primeros participantes | La ficha se queda corta: JPMD es el único caso **en producción** que cita R44, pero hay más pilotos. Se añaden los dos y se mantiene la madurez 2 (valoración propia; Joel decide si cambiarla). BNY sin fuente citada en el apunte: **[VERIFICAR]** |
| 3 | Fondos | ETF de XRP en EE. UU. ≈ **2.178 M$** (R27, 30-sep) | El dossier ETF da **1.560 M$** de activos netos en los 5 ETF spot a 8-oct (SoSoValue) | Para que cuadre, XRP tendría que haber caído ~28 % entre el 30-sep y el 8-oct, y ningún informe lo recoge (el dossier solo atribuye al precio la bajada del 6 al 8-oct, de 1.697 a 1.560 M$). Puede que R27 cuente más productos que los 5 spot, pero no lo dice. **[VERIFICAR]** la definición de la tabla de R27 |
| 4 | Fondos | «Hong Kong crece un 55 % desde el lanzamiento», dentro de «entradas netas de XRP» | R27: el +55 % es la capitalización de los **11 ETF cripto** de Hong Kong; la SFC **no nombra XRP** | La ficha mezclaba los dos datos. Se corrige |
| 5 | Puente | «Gran parte del tráfico de Stellar son bots y tokens exóticos» (hecho) | R43: el patrón (79 % de operaciones contra pools, ledger al 98 %) es **compatible** con bots de arbitraje, pero «no puedo separar usuarios de bots» **[ESPECULACIÓN]** | La ficha afirmaba más que su fuente. Se rebaja a especulación |
| 6 | Tokenización | Servicio de DTC «previsto para 2S-2026» (R26) | El apunte grande (línea 149) dice «lanzamiento comercial previsto para octubre de 2026 (**confirmado** en octubre de 2026)». R16 (15-oct) no encontró ningún comunicado de DTCC que lo confirme | El apunte afirma una confirmación que ningún informe tiene. **[VERIFICAR]**. La fecha de la ficha (2S-2026) es compatible con octubre |
| 7 | CBDC (apuntes) | Piloto del euro digital en la **2.ª mitad de 2027**; emisión posible en 2029 (R40, BCE leído) | Dos apuntes repiten fechas del vídeo de Despeja La X: `regulacion-por-jurisdicciones-y-detonante-2027` («objetivo de lanzamiento: 1.ª mitad de 2027») y `xrp-stablecoins-cbdc-bis-fmi` («lanzamiento minorista a mediados de 2027») | Los apuntes confunden piloto con lanzamiento y adelantan la fecha. La ficha está bien. Los apuntes no se tocan (regla de CLAUDE.md); queda anotado aquí |
| 8 | Stablecoins | (No está en la ficha) Fecha de las propuestas de la Fed bajo la GENIUS Act | R08P y el apunte de catalizadores: **24-sep**. Dossier Stablecoins: **29-sep** (Federal Register 2026-19860 y 2026-19899) | Probablemente 24-sep es el anuncio y 29-sep la publicación oficial, pero ningún documento lo dice. **[VERIFICAR]**. El glosario ampliado (R16, 19-oct) usa 24-sep |

## 2. Coincidencias (refuerzan la ficha)

- **CBDC.** Pontes arrancó el 21-sep-2026 (BCE leído en el dossier Pagos y en R08P). El e-CNY paga interés desde el 1-ene-2026. mBridge suma ≈ 55,5 mil M$ con el e-CNY por encima del 95 % (dossier Euro digital y R40, ambos de fuente secundaria). Ninguna CBDC europea usa XRP ni XLM (dossier Euro digital).
- **Stablecoins.** Las fechas de la GENIUS Act coinciden (comentarios del Tesoro hasta el 19-oct y de la Fed hasta el 30-nov; fecha efectiva ≈ 18-ene-2027), igual que el debate de la «multi-emisión» en la UE. La concentración se mantiene: USDT+USDC ≈ 82 % el 9-oct y ≈ 84 % el 17-oct.
- **Puente.** XRPL tenía 107 enmiendas y 97 activas tanto el 9-oct (dossier Infraestructura, ledger) como el 17-oct (R45). fixCleanup3_4_0 tiene mayoría desde el 9-oct a las 09:34 UTC y podría activarse a partir del 23-oct. No hay cifra oficial de ODL: el dossier Pagos califica de dudosa la de «35.000 M$».
- **Tokenización.** DTCC tiene tres plazos distintos: el servicio de DTC (2S/oct-2026), la Collateral AppChain (4T-2026) y los activos en Stellar (1S-2027). Coinciden el dossier Stellar RWA, R26 y la entrevista de un vídeo. El «retraso a 2027» que dio otro vídeo no se confirma: es otro producto.
- **Custodia.** Las aprobaciones del OCC son condicionales: el apunte grande (línea 540) recoge las de Ripple, BitGo, Circle, Fidelity y Paxos (dic-2025).
- **Regulación.** CLARITY: la Cámara la aprobó 294-134 (17-jul-2025) y el cierre de debate en el Senado falló 49-50 (15-sep-2026). Lo dicen el dossier CLARITY, R18 y dos vídeos. Fed (3,75–4,00 %) y BCE (2,50 %) coinciden con el dossier Macro. El subyacente sube de 2,4 % (agosto, dossier) a 2,6 % (septiembre, R29): es un dato nuevo, no una contradicción.
- **Fondos.** No hay ETF spot de XLM, solo el trust GXLM en OTC (≈ 21,8 M$ a 30-jun, dossier ETF). Evernorth cotiza desde el 12-oct (R23, 8-K). Los 473 M XRP son del Form 425 (a 31-dic-2025); el 8-K confirma 388,9 M aportados en especie (R23 y la corrección del dossier Evernorth).

## 3. Vídeos: qué aportan y qué no

| Vídeo (Despeja La X) | Coincide con la ficha | Choca o exagera |
|---|---|---|
| Euro digital y Pontes (28-sep) | Pontes el 21-sep | Titular «1.ª mitad de 2027» frente a la 2.ª mitad del BCE; usa un discurso de Lagarde de 2018 como si fuera actual |
| Stellar y cumplimiento (1-oct) | ~4.000 M$ de RWA (otra métrica que rwa.xyz), DTCC en Stellar en 1S-2027 | «Habrá demanda de XLM» sin dato [ESPECULACIÓN]; voz de la propia Stellar |
| Próximas criptos (30-sep) | CSD BR refleja en el XRPL fondos de BTG con MPT, en entorno con permisos | «Retraso de la AppChain de DTCC a 1T-2027», sin confirmar |
| Custodia SEC y CLARITY (2 y 5-oct) | Propuesta de custodia de la SEC (1-oct), cierre de debate 49-50 | «300 votos» (fueron 294), «17-sep» (fue el 18-ago), «más escasez de XRP» sin dato |
| Evernorth y CFTC (6-7-oct) | CTX/CAM de la CFTC son un ANPRM, no una norma | Cálculo de la prima con supuestos del canal |

Conclusión: los vídeos no aportan ningún hecho que no esté ya en un dossier o informe con mejor fuente. Sus desviaciones van siempre en la misma dirección: fechas más tempranas y efectos sobre el precio sin datos. Encaja con `cerebro/documentos/patrones-de-bulos.md`.

## 4. Cambios propuestos en `explorador/datos.json`

- Cada línea de las 8 fichas lleva su origen al final entre paréntesis: informe, dossier o apunte.
- Las contradicciones 1 a 6 se reflejan en la línea afectada con [VERIFICAR] o [ESPECULACIÓN].
- Se añaden pocas líneas nuevas, todas con fuente en el repo: los pilotos de Swift y BNY en Depósitos tokenizados, la bajada de RLUSD en XRPL, la concentración en Stellar, la pérdida latente media de los ETF de XRP y las fechas de Swell y Meridian.
- La lista «Informes de origen» de cada ficha añade los dossiers usados.
- No se cambia ninguna nota de madurez (es valoración propia).
- El archivo vuelve a saltos de línea LF. El commit 48fccb0 lo había pasado a CRLF por error, junto con unas comas mal colocadas; el contenido era válido.

## 5. Lo que no se ha podido comprobar (sin salir del repo)

- La posición del Consejo de la UE sobre el euro digital (punto 1).
- Qué productos cuenta la tabla de ETF de R27 (punto 3).
- El lanzamiento real del servicio de DTC (punto 6).
- El origen de la línea de BNY en el apunte grande (punto 2).
- La regla de día hábil del plazo del 13F del 3T. Son 45 días tras el 30-sep, que caen en sábado 14-nov; el apunte de catalizadores dice ~14-nov y la ficha 16-nov.
