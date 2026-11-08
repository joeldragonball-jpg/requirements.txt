# Verificación de prensa del 4-6 nov (hecha el 8-nov-2026)

Siete titulares que quedaron sin contrastar tras la verificación del 7-nov. Detalle y fuentes en `eventos/verificados.json` (entradas con `verificado: 2026-11-08`). Esto no es una recomendación de compra ni de venta.

| # | Titular | Veredicto | Qué es HECHO / qué es OPINIÓN |
|---|---|---|---|
| 1 | CLARITY «31 %» | **No confirmada** | No son votos: sería la probabilidad de un mercado de predicciones (Polymarket) de que sea ley en 2026. No hay fuente primaria posible para una probabilidad. No hallé ningún 31 % fechado 4-6 nov; el único 31 % fechado es un mínimo de **julio**. Posible cifra reciclada. El hecho oficial sigue siendo el cloture 49-50 del 15-sep. «Cae por los demócratas» es causa atribuida. |
| 2 | Fed y OCC consultan a bancos | **Parcial** | Reportaje de Reuters (5-nov) con fuentes anónimas: llamadas a bancos desde el 2-nov. Sin nota en occ.gov ni federalreserve.gov. Sin pérdidas bancarias reportadas. «Investigan/sondean» de medios cripto es más de lo que dice la fuente. |
| 3 | Hackeo de Binance (~6.300 M$) | **Parcial (hecho muy corroborado; primaria no leída)** | Hackeo del 29-oct y reapertura de retiradas el 1-nov, por muchos medios (TechCrunch, AP, Khaleej Times). Comunicado de Binance y atribución del FBI no leídos en primaria [VERIFICAR]. El «90 %/95 % cubierto» es dato de la empresa. Salidas 4.700 M$ (brutas) vs 5.800 M$ (netas): medidas distintas. |
| 4 | Nasdaq −5,5 % | **Confirmada** | Una sola sesión, el 5-nov (FRED/Nasdaq Composite: 25.736,51 → 24.315,00 = −5,52 %); el 6-nov +1,09 %. Desde el máximo de cierre del 6-oct, −11,9 % (corrección real). **Error de prensa:** S&P 500 dicho −3,8 %; el cierre da −4,36 %. |
| 5 | Brent ~98 $ | **No confirmada** | EIA/FRED solo llega al 3-nov (107,03 $). El 98 $ será el futuro ICE (no leído) y no es comparable con el spot (el 23-oct difirieron ~11 $). Bajada de 120 → 107 $ (30-oct → 2-nov) sí es hecho. |
| 6 | Petróleo cae por 4.º día | **No confirmada** | Con el spot: bajadas 27-29 oct, **sube el 30-oct**, baja 2 y 3-nov. Los días 4-6 nov no están publicados. |
| 7 | Irán exime a China e India | **Parcial** | Lo dijo un parlamentario iraní (Hayat-Moghaddam) el 4-nov, no el gobierno; incluyó también **Irak y Qatar** (el titular los omite). Sin formalizar ni confirmar; el estrecho sigue cerrado de facto. Motivos = versión del parlamentario. |

## Errores detectados
- **Prensa:** S&P −3,8 % (real −4,36 % al cierre); exención iraní presentada como decisión y sin Irak/Qatar; «Fed y OCC investigan» donde la fuente dice «consultan».
- **Resumen de IA del repo (`cerebro/actualidad/2026-W45.md`):** trata el 31 % de CLARITY como dato vigente de CoinMarketCap sin fecha; mezcla spot y futuro en el Brent; suma «cuatro días de caídas» que la serie oficial no sostiene.

## Pendiente
- Leer en primaria: comunicado de Binance y del FBI; estado oficial de CLARITY (congress.gov/senate.gov siguen bloqueados, no insistir).
- Cierre del Brent y WTI del 4-6 nov cuando la EIA lo publique, y cierre ICE si hay acceso.
- S&P del 6-nov (FRED aún sin publicar).
- Fuentes de datos usadas: FRED (NASDAQCOM, SP500, DCOILBRENTEU, DCOILWTICO), EIA, RSS de la OCC, FDIC FIL del 3-nov.

## Cierre (tarde del 8-nov)

Nivel de acceso: Chrome (extensión) **no estaba conectado**; usé curl contra FRED y EIA (cargan) y el buscador web. congress.gov, senate.gov, GovTrack (desafío Cloudflare), fbi.gov y bleepingcomputer devuelven 403: lo de esas fuentes se apoya solo en fragmentos del buscador.

| # | Punto | Veredicto tras el cierre | Qué se pudo y qué no |
|---|---|---|---|
| 1 | Hackeo de Binance | **Se mantiene parcial.** Primarias *localizadas*, texto no leído | HECHO (existe): alerta del FBI en fbi.gov (listada el 31-oct, «North Korea Responsible for $6 Billion+ Binance Attack», TraderTraitor, «on or about» 29-oct, con USSS e IRS-CI). Binance: hilo «Security Incident» en @binance y mensajes de Richard Teng (reanudación por fases el 1-nov, ~95 % repuesto, Binance absorbe la pérdida). **No leí ninguno de los textos** [VERIFICAR]. No hallé comunicado del DOJ: la atribución es del FBI. El FBI dice «más de 6.000 M$»; los 6.300 M$ salen de prensa/Binance sin primaria leída. |
| 2 | CLARITY Act | **Sin cambio: cifra del 31 % no confirmada; estado oficial [VERIFICAR]** | Nivel alcanzado: solo prensa (Bitcoin.com: tras el 49-50 sigue en el calendario del Senado; voto aplazado a septiembre). Ningún 31 % fechado 4-6 nov. Sin primaria. |
| 3 | Brent / WTI 4-6 nov | **Sin cambio: no confirmada** | La EIA indica «Release Date 11/4/2026, Next Release Date **11/12/2026**»: el spot del 4-6 nov no existe publicado hasta el 12-nov (FRED depende de la EIA). Último dato: Brent 107,03 $ y WTI 99,64 $ (3-nov). Futuro ICE: sin acceso primario. Una nota secundaria (Brent futuro 95,20 / WTI futuro 96,57, fecha ambigua) **se descarta**. |
| 4 | S&P 500 del 6-nov | **Sin dato** | FRED SP500 termina el 5-nov (7.353,73). No obtenido de S&P Dow Jones Indices. El −4,36 % del 5-nov se mantiene. |

**HECHOS vs OPINIONES.** Hecho: la alerta del FBI existe y atribuye a Corea del Norte. Opinión/disputa: Kim Yo-jong rechaza la atribución (Yonhap vía The Block, 2-nov); la atribución es posición oficial, no una prueba forense pública. Causa de la ruta de intrusión (portátil de un ingeniero DevOps): dato de Binance, informe post-incidente pendiente.

**Sigue sin fuente:** texto de la alerta del FBI y de los posts de Binance; estado oficial de H.R.3633; spot y futuro del petróleo 4-6 nov (reintentar el 12-nov); S&P 500 del 6-nov (reintentar cuando FRED lo publique).

`eventos/verificados.json`: entradas CLARITY, Binance, Nasdaq/S&P, Brent y «cuarto día» actualizadas (campo `actualizado: 2026-11-08` y nota añadida a `con`); ningún `estado` cambiado.

## Cierre con Chrome (8-nov, noche)
- **Hackeo de Binance → CONFIRMADO [P] en lo esencial.** Alerta del FBI leída entera (fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack, fechada 31-oct-2026): Corea del Norte (TraderTraitor) robó «más de 6.000 M$» en activos virtuales a Binance «on or about» 29-oct-2026; fondos convertidos sobre todo en ETH; FBI, USSS e IRS-CI piden bloquear las direcciones listadas. Los 6.300 M$ siguen sin primaria (el FBI dice «más de 6.000 M$»). Posts de Binance no leídos [VERIFICAR]. La atribución es posición oficial, no prueba forense pública.
- **CLARITY Act (H.R.3633) → estado oficial leído [P]** en congress.gov (all-actions): aprobada en la Cámara el 17-jul-2025 (294-134); en el Senado, en el calendario desde el 1-jun-2026 (Calendar No. 423). El 15-sep-2026 la cloture sobre la moción de proceder **no se invocó, 49-50** (Record Vote 234) y Tillis presentó moción de reconsideración. Último acto registrado: 15-sep-2026. La cifra del «31 %» sigue sin fuente (no es dato legislativo; sería de un mercado de predicción) [VERIFICAR].
- **Egipto (NEA, elections.eg):** la web carga; en portada constan las resoluciones nº 1 y nº 2 de 2026 con el resultado final de las repeticiones (19 y 27 distritos). Texto de las resoluciones y participación 32,41 % no leídos aún.
- **Etiopía (NEBE):** error 523 de Cloudflare también con VPN (servidor de origen caído). **Indonesia (OJK):** la página redirige a otro dominio y no se puede leer.
