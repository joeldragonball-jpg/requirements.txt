# Verificación de noticias de prensa «sin contrastar» (14-nov-2026)

Alcance: los 16 puntos `sin_contrastar` de `docs/movil/seguimiento.json` (12 noticias de prensa + 4 [VERIFICAR] del resumen vigente). Todo anotado en `eventos/verificados.json` (verificado = 2026-11-14, salvo AP, que arrastra la lectura del 10-nov). Tras anotar: 0 `sin_contrastar`. Sin commit ni push; no se lanzó ningún workflow ni la API de Anthropic.

## Resultado

| Noticia (fecha) | Estado | Fuente clave |
|---|---|---|
| ChinaAMC: 1.ª negociación secundaria de fondos tokenizados en HK (26-oct) | **confirmado** | SFC [P], nota 26PR174; SCMP |
| Petroleros incendiados cerca de Ormuz (7-9 nov) | matizado | UKMTO [P] #199 y #200: dos petroleros, «proyectil desconocido»; sin minas |
| AP: demócratas ganan Cámara y Senado (10-nov) | matizado | arrastra la lectura del 10-nov; proyección, no certificado |
| SEC y CFTC: regulación cripto rápida (10-nov) | matizado | listas oficiales SEC/CFTC: nada «rápido»; es lectura de prensa |
| Binance cierra cuentas en España el 31-dic (10-nov) | **confirmado** [S] | Cinco Días leído entero; «cerrar» = tratar como inactiva |
| Nvidia se hunde / Ibex defiende 20.000 (12-nov) | matizado | NVDA −14 % intradía pero cierre −4,3 %; Ibex cerró 19.965,5 |
| Hammack: tipos más restrictivos (12-nov) | matizado | postura real (12-oct, 5-nov); no hay discurso el 12-nov en la Cleveland Fed |
| Fed: octubre 2027 sin votación de tipos (12-nov) | matizado | calendario Fed [P]: 26-27 oct-2027 = «Monetary Policy Strategy Meeting»; «sin votación» es inferencia |
| Préstamos de Ripple cerca de lanzarse en XRPL (12-nov) | matizado [S] | 22/35 validadores el 10-nov, hace falta 28/35 dos semanas; no son «bancarios» |
| Irán ataca radar de EE. UU. en Baréin (13-nov) | **dudoso** | nada hallado de esa fecha; CENTCOM no legible |
| Bitcoin mínimos de 12 semanas (13-nov) | matizado | Yahoo: cierre 68.249 (−4,3 %); los 1.600 M$ de liquidaciones sin contrastar (CoinDesk bloquea) |
| Tesoro EE. UU. contra subir tipos (13-nov) | **dudoso** | postura habitual de Bessent; titular del 13-nov no hallado |

[VERIFICAR] del resumen vigente:

- **DGT V0648-24 → confirmado [P].** Petete ya responde (antes 502). Leída entera: staking (V1766-22), pools de liquidez de AMM y préstamos = capital mobiliario art. 25.2 (base del ahorro, valor de mercado en euros); airdrops = ganancia patrimonial art. 37.1.l (base general); permutas y compraventas = ganancia/pérdida patrimonial con FIFO; gas y comisiones suman al valor de adquisición o transmisión. **Bridges: no se pronuncia.**
- **Tokens LP de AMM → matizado.** Los *rendimientos* del pool son capital mobiliario, pero la consulta excluye expresamente «la obtención y reembolso de los LP tokens»: esa fiscalidad sigue sin resolver. Entrada propia.
- **Escala del ahorro art. 66 LIRPF 2026:** ya estaba confirmada (10-nov); se retira de la lista de pendientes.
- **DAC8 / modelos 172-175-721 en BOE:** sigue **dudoso** (solo borradores). La búsqueda en el BOE de hoy falló (formulario inválido): pendiente leer BOE/AEAT.
- **Chainlink CCIP en SWIFT** y **precio de adquisiciones de Ripple:** siguen **dudosos** sin fuente nueva; ya tienen entrada «dudoso» visible en el Seguimiento y se retiran como líneas duplicadas de [VERIFICAR] (`resueltos_resumen`).

## Regla de titulares con umbral
Ninguna noticia queda «desmentida». Los matices de Nvidia, Ibex y Bitcoin son de **instrumento/momento** (intradía frente a cierre; mínimo frente a cierre): el titular es defendible con su umbral, solo que no es el cierre.

## Límites
- CoinDesk (anti-bot de Vercel) y CENTCOM (redirección) no se pudieron leer; no se saltó ninguna protección.
- Ripple, Hammack, Tesoro y Baréin se apoyan en búsqueda web y páginas oficiales de listas, no en el texto de la noticia original.
- Entrada de AP no releída hoy.

## Cambios en archivos
- `eventos/verificados.json`: 13 entradas nuevas, 2 actualizadas (V0648-24), 4 frases en `resueltos_resumen`.
- Regenerados: `docs/movil/*` (`construir_movil.py`) y Seguimiento/planning (`construir_seguimiento.py`).
