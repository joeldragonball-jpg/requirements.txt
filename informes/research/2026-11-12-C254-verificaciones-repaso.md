# C254 · Verificación en fuente de las seis dudas abiertas por C252 (12-nov-2026)

Informativo; no es una recomendación de compra ni de venta. Modelo: Fable 5.2. Lecturas hechas el 12-nov-2026 entre las 11:25 y las 11:45 UTC. [P] = fuente oficial leída hoy; [S] = agregador o resumen; [VERIFICAR] = no leído. Los porcentajes son cálculo propio.

Cómo se leyó: API pública del Banco de Inglaterra, nodo público del XRP Ledger (xrplcluster.com), Horizon de Stellar y página del STEO con un script de solo lectura; Banco de España y AIE con lectura web de la página oficial. **No hizo falta Chrome**: ningún sitio bloqueó.

## Resultado en una tabla
| Duda de C252 | Resultado | Nivel |
|---|---|---|
| (a) STEO de noviembre | Leído. Brent spot «cerca de 100 $/b» lo que queda de 2026; 77 $/b en el 4T-2027 | P |
| (a) «+14 $ vs. septiembre» | **Sin resolver**: la edición de octubre ya no está en la página y no se leyó el PDF | VERIFICAR |
| (b) Stablecoins en Stellar −56 % | **Falso positivo de C252**: la cifra de partida (941 M$) no cuadra con ninguna serie; no hay tal caída | P + S |
| (c) RLUSD en el XRPL | **Caída real**: 1.140,1 M (9-oct) → 885,2 M (12-nov), −22,4 % | P |
| (d) Bank Rate en 3,75 % | Desde el **18-dic-2025**, no desde el 17-sep-2026 | P |
| (e) Banco de España | PIB 2,6 % y 2,2 % confirmados; el déficit de 2026 es **2,6 %**, no 2,3 % | P (parte en VERIFICAR) |
| (f) Ormuz: AIE frente a PortWatch | Las dos cifras están bien copiadas y **siguen sin poder describir lo mismo** | P frente a P |

## HECHOS

### (a) STEO de noviembre de la EIA [P, eia.gov/outlooks/steo, leído 12-nov]
- Publicado el 10-nov-2026; previsión cerrada el 5-nov; próxima edición el 8-dic-2026.
- Brent spot: se espera «cerca de 100 $ por barril» durante el resto de 2026 y una bajada gradual hasta una media de 77 $/b en el 4T-2027. Tabla resumen: media anual 2026 = 97 $, 2027 = 86 $ (2024: 81; 2025: 69).
- Frente a la edición de octubre, según lo que ya tenía el repo (R46): 2026 de 96 a 97 $; 2027 de 84 a 86 $; 4T-2027 de 74 a 77 $. La cifra del 4T-2026 pasa de «105 $» a «cerca de 100 $».
- Otros datos de la portada: los precios del crudo subieron por tercer mes seguido en octubre; inventarios comerciales de crudo de EE. UU. en 410 millones de barriles a fin de octubre, el nivel más bajo para esa fecha desde 2014; diésel de 2027 a 5,03 $/galón (+12 % frente a la edición anterior); producción de EE. UU. de 14,3 mb/d en 2027.
- **No resuelto:** si el «+14 $» de octubre era frente al precio de septiembre o frente a la edición anterior. La página solo muestra la edición vigente. [VERIFICAR] en el PDF de archivo de octubre.
- Esto cierra la voz v061 (plazo 10-nov) y el «✓ cubierto» del planning, que hasta hoy no tenía el dato.

### (b) Stablecoins en Stellar
- [P, Horizon, ledger 65.439.356, 12-nov 11:27 UTC] USDC emitido en Stellar: **344,0 M** (223,6 M en cuentas, 117,9 M en contratos, 2,4 M en fondos de liquidez). EURC: 4,45 M.
- [S, DefiLlama, serie histórica por cadena leída hoy] Stablecoins en dólares en Stellar: 392,4 M$ el 9-oct, máximo de 481,5 M$ el 20-oct, 329,7 M$ el 1-nov y **392,4 M$ el 12-nov**. Es decir, igual que hace un mes.
- Conclusión: el «941 M$ a 9-oct» del dossier `2026-10-09-panorama-competitivo.md` no coincide con la serie actual del mismo agregador para ese día (392,4 M$). **La caída del 56 % que señalé en C252 §3.2 no existe**; salía de comparar con una cifra de partida errónea o de otra métrica. Origen de los 941 M$: [VERIFICAR] en el dossier.
- Los 344 M de USDC leídos en el propio ledger son coherentes con los 335,8 M$ del panel.

### (c) RLUSD en el XRP Ledger [P, gateway_balances del emisor, ledger 108.281.104, 12-nov 11:27 UTC]
- RLUSD en circulación en el XRPL: **885.245.927**. El 9-oct eran 1.140.114.698 [P, ledger 107.541.076, dossier de pagos]: **−254,9 M, −22,4 %** en 34 días.
- [S, DefiLlama] Total de stablecoins en el XRPL: 1.247,7 M$ (9-oct) → 951,8 M$ (12-nov). La mayor parte de la bajada es de **un solo día: −283,8 M$ el 31-oct**.
- La bajada es real y coincide en ledger y agregador. **Causa: [VERIFICAR]** (no se ha leído ninguna nota de Ripple ni el desglose por cadena de RLUSD; no se sabe si se amortizó o se movió a otra red).

### (d) Bank Rate del Banco de Inglaterra [P, serie IUDBEDR, 726 datos diarios hasta el 11-nov-2026]
- Cambios: 5,25 → 5,00 (1-ago-2024) → 4,75 (7-nov-2024) → 4,50 (6-feb-2025) → 4,25 (8-may-2025) → 4,00 (7-ago-2025) → **3,75 (18-dic-2025)** → **4,00 (5-nov-2026)**.
- El hecho de `2026-11-06-cierre.md` («antes 3,75 % desde el 17-sep») es incorrecto: el 17-sep-2026 solo se mantuvo. El tipo estuvo en 3,75 % casi once meses.

### (e) Banco de España: proyecciones del 3T-2026 [P, bde.es, leído 12-nov]
- Publicadas el **9-oct-2026** (cierre de datos 2-oct). No aparece en la página ningún número de nota de prensa: el «nota 2026-94» y la fecha del 15-oct del repo quedan sin confirmar.
- PIB: **2,6 % en 2026 y 2,2 % en 2027** (tabla del recuadro 6). Coincide con la AIReF: la igualdad que parecía sospechosa en C252 es real.
- Déficit de las AAPP en 2026: **2,6 % del PIB** (frase literal del recuadro 5). El repo tenía 2,3 % [S, prensa]: no coincide.
- Inflación (IAPC): 3,9 % en 2026 y 3,7 % en 2027 (tabla del recuadro 6).
- [VERIFICAR] (solo en un resumen automático de la página, sin leer la frase): déficit de 2027 en 2,2 % y deuda del 98,5 % (2026) y 96,2 % (2027).
- Con esto, la distancia entre organismos en el déficit de 2026 es de 0,2 puntos (Banco de España 2,6 %; AIReF 2,8 %), no de 0,5.

### (f) Ormuz [P, AIE, Oil Market Report de octubre, publicado el 14-oct-2026]
- Frase literal: los transbordos buque a buque en el golfo de Omán ayudaron a subir los flujos totales de petróleo por el estrecho «by 3.7 mb/d to 10.9 mb/d» (párrafo sobre septiembre). Exportaciones de crudo de los productores del Golfo: +4,4 mb/d hasta 13,9 mb/d en septiembre; desvío por oleoducto: +970 kb/d hasta 5,6 mb/d. Demanda mundial de 2026: −2,6 mb/d, hasta 102,4 mb/d.
- **La página no explica cómo mide ese flujo** (ni si incluye buques con el transpondedor apagado, ni crudo y productos por separado).
- [P, PortWatch, panel `ormuz`] Septiembre: 3,6 barcos al día, **1,1 petroleros al día**; agosto 1,9. Febrero: 43,5 petroleros al día.
- Cálculo propio: 10,9 mb/d repartidos entre 1,1 petroleros al día serían unos 10 millones de barriles por barco; el mayor petrolero habitual (VLCC) lleva unos 2 millones. Además, la AIE ve subir el flujo de agosto a septiembre y PortWatch ve bajar los petroleros. **No miden lo mismo.**

## OPINIONES (mías, no de las fuentes)
- (f) La explicación más simple es que PortWatch, que cuenta barcos por su señal AIS, no ve buena parte del tráfico y que la AIE estima volúmenes con otros datos (cargas, transbordos). Es una hipótesis: ninguna de las dos fuentes lo dice. [ESPECULACIÓN]. Mientras no se aclare, el panel `ormuz` debería avisar de que el recuento de barcos no equivale a barriles.
- (c) Una salida de 284 M$ en un día parece una operación concreta (amortización o traslado entre redes) más que una fuga gradual. [ESPECULACIÓN]; hace falta leer el desglose por red.
- (a) El STEO baja la referencia del 4T de 105 a ~100 $ cuando el futuro ya cotiza por debajo (≈92 $ hoy en el móvil [S]): la previsión oficial sigue por encima del mercado.

## Qué hay que corregir en el repo (no aplicado aquí)
1. `informes/research/2026-11-12-C252-…md` §3.2 y línea 8 del resumen: la caída de Stellar no existe (nota añadida al final de ese informe).
2. Hecho «Banco de España… déficit 2,3 %» (`2026-11-09-noticias-fuertes.md`): 2,6 % y fecha 9-oct.
3. Hecho del Bank Rate «desde el 17-sep»: 18-dic-2025.
4. Hecho y dossier «Stellar 941 M$ a 9-oct»: marcar [VERIFICAR].
5. `datos.json` / `voces.json`: RLUSD en XRPL 885 M (12-nov) y STEO de noviembre (v061).
6. Panel `ormuz`: aviso de que barcos AIS ≠ barriles, con la cifra de la AIE al lado.

## [VERIFICAR] que quedan
- «+14 $» del STEO de octubre (PDF de archivo).
- Causa de la bajada de RLUSD del 31-oct.
- Déficit 2027 y deuda del Banco de España (tramo de la página no leído).
- Método de la AIE para el flujo de Ormuz.

## Lecciones (máx. 5)
1. Antes de publicar una «conexión» llamativa hay que comprobar la cifra de partida: los 941 M$ de Stellar no aguantaban ni la serie del propio agregador.
2. Las API oficiales (Banco de Inglaterra, Horizon, XRPL) responden a un script sencillo; no hizo falta Chrome.
3. La portada del STEO solo guarda la edición vigente: para comparar ediciones hay que archivar el texto el día que sale.
4. Dos fuentes P pueden chocar (AIE y PortWatch) si miden cosas distintas; hay que anotar qué mide cada una.
5. Un dato de prensa [S] sobre un organismo (déficit 2,3 %) se cierra en minutos leyendo la página del organismo.

## Seguridad
Sin claves ni secretos; peticiones de solo lectura con agente de usuario genérico y sin datos personales. Sin workflows ni API de Anthropic. Sin commit ni push. No se tocó `privado/`, `cerebro/` ni ningún JSON de `explorador/`.

## Fuentes
- EIA, STEO: https://www.eia.gov/outlooks/steo/
- Banco de Inglaterra, Bank Rate (IUDBEDR): https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp
- Banco de España, proyecciones 3T-2026: https://www.bde.es/wbe/en/publicaciones/analisis-economico-investigacion/proyecciones-macro-informe-trimestral/proyecciones-e-informe-trimestral-de-la-economia-espanola-tercer-trimestre-2026.html
- AIE, Oil Market Report de octubre de 2026: https://www.iea.org/reports/oil-market-report-october-2026
- Horizon (Stellar): https://horizon.stellar.org/ · XRP Ledger: https://xrplcluster.com/ · DefiLlama: https://stablecoins.llama.fi/
