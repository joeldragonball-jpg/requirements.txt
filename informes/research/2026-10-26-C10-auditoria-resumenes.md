# C10 · Auditoría de cifras de los resúmenes semanales del bot (W41-W43)

Fecha: 2026-10-26 · Etiquetas: [P] serie primaria leída, [S] agregador o prensa, [VERIFICAR]. Los resúmenes del bot NO se han modificado.

Series usadas (leídas el 25-oct-2026 con curl y User-Agent propio):
- Tesoro de EE. UU., curva diaria (CSV daily_treasury_yield_curve 2026) [P].
- FRED: CPIAUCSL, PPIFIS (demanda final), PPIACO, DCOILBRENTEU y DCOILWTICO (spot EIA), DGS10/DGS30, DFEDTARU/DFEDTARL, CBBTCUSD (Coinbase) [P/S].
- IMF PortWatch, Daily_Chokepoints_Data, Estrecho de Ormuz (hasta 18-oct) [P].
- Yahoo Finance (chart API): Brent futuro continuo BZ=F, Ibex, Nikkei [S].
- `docs/movil/data.json` (generado 25-oct 21:50 UTC): tipos de bancos centrales, bonos, Brent/WTI al 23-oct.

## Resultado
De 29 cifras o afirmaciones numéricas contrastadas: **15 coinciden, 4 no coinciden, 4 mezclan series o no dicen plazo, 6 no son verificables** con fuentes abiertas. Las cifras de IPC, PPI, Ibex, Bitcoin y Brent futuro (hasta el 23-oct) son correctas. Los fallos están en: (1) rendimientos sin plazo ni país, (2) mezcla de Brent futuro y spot, (3) titulares tratados como hechos (Ormuz «12 M b/d», «flujos prebélicos») y (4) hechos de semanas anteriores presentados como de la semana.

## Tabla

| Resumen | Cifra del bot | Serie primaria / contraste | Veredicto |
|---|---|---|---|
| W41 | Brent 101-105 $, ~103 $ | Futuro BZ=F 5-9 oct: 100,2-104,7 $ de cierre. Spot EIA (FRED) 5-9 oct: 125,5-130,2 $ | Coincide con el **futuro**; el spot iba 20-25 $ por encima (mezcla M1) |
| W41 | «Brent físico marcó un récord» | Spot EIA 130,18 $ el 8-oct; la serie leída no permite confirmar «récord» | No verificable [VERIFICAR] |
| W41 | Ibex «más de un 2 %» y «1,68 %» | Ibex: −1,68 % el 7-oct (coincide); −2,17 % fue el 1-oct, semana W40 | 1,68 % coincide; el «>2 %» es de la semana anterior (M5) |
| W41 | Bitcoin «bajo 84.000 $» | Coinbase 9-18 oct: 81.300-83.700 $ | Coincide |
| W41 | Golfo al 81 % del nivel prebélico (sin Irán) | Sin serie abierta localizada; PortWatch: Ormuz 2-8 buques/día en oct | No verificable [VERIFICAR] |
| W41 | Riad: 12 muertos, >300 heridos | Solo prensa | No verificable |
| W41 | Votación de septiembre unánime a favor de subir; otra subida antes de fin de año | FRED DFEDTARU/L: 3,50-3,75 % → **3,75-4,00 % el 17-sep-2026** (+25 pb) | Coincide |
| W41 | «[VERIFICAR] tipos 3,50-3,75 %» (apuntes) | Rango vigente 3,75-4,00 % desde el 17-sep (FRED; data.json `tipos`) | **Resuelto**: el apunte está desfasado |
| W42 | IPC septiembre 3,7 % interanual, mensual +0,6 % esperado | CPIAUCSL sep-26/sep-25: +3,72 %; mensual +0,65 % | Coincide |
| W42 | PPI 6,3 % interanual | PPIFIS (demanda final): +6,35 %. PPIACO (todas las materias): +12,8 % | Coincide solo con la serie de demanda final; el bot no dice cuál (M4) |
| W42 | Bitcoin ~81.000 $ | Coinbase 12-18 oct: 81.300-83.700 $ | Coincide |
| W42 | «Brent +3,72 %, rozó 110 $» | BZ=F 16-oct: +3,72 %, cierre 109,86 $ | Coincide (futuro) |
| W42 | «Crudo superó 110 $ por primera vez desde mayo» | Futuro: máximo 110,0 el 16-oct. Spot EIA ya >125 $ desde el 5-oct | Cierto solo para el futuro (M1) |
| W42 | «Flujo por Ormuz sube a 12 M b/d» | PortWatch: 2-7 buques/día y 0-2 petroleros/día en oct | **No coincide**; el bot lo marca [VERIFICAR] pero lo copia a «Cifras» (M6) |
| W42 | Fed «subió por primera vez desde 2023» (ABC) | Hecho real, pero del 17-sep, no de la semana | Fecha equivocada (M5) |
| W42 | Kospi −8 % | Yahoo no devolvió Kospi; Nikkei −4,9 % el 15-oct | No verificable |
| W42 | Déficit FY2026 ~2 billones; multa 1.200 M$ a BofA; probabilidad de subida 18 %→29 % | Solo prensa | No verificables |
| W42 | «Bonos por encima del 5 %» (CNBC) | 10 años: 5,31 % el 5-oct y 5,00 % el 23-oct; 30 años 5,29-5,67 % | Coincide, pero sin plazo (M2) |
| W42 | «[VERIFICAR] 10Y de mayo ~4,58 %» | 10 años 5,00 % (23-oct), máximo del año 5,31 % (5-oct) | **Resuelto**: 4,58 % desfasado |
| W43 | «El Treasury llegó al 5,34 %» (sin plazo) | Tesoro 23-oct: 10 años 5,00; 20 años 5,37; **30 años 5,33** (5,42 el 21-oct). Gilt 10 años (data.json): 5,334 % el 21-oct | **No coincide** con el 10 años; solo compatible, redondeando, con el 30 años o con el gilt (M2, M3) |
| W43 | Brent 114 → 116,72 → «máximo 117 $, el más alto desde abril» | Futuro BZ=F: máximo 113,49 $ (22-oct), cierre 113,17. Spot EIA 115,22 el 20-oct | **No coincide** con el futuro; se acerca al spot, que ya superó 125 $ en octubre (M1) |
| W43 | WTI tocó 109 $ | Spot EIA 110,0 el 19-oct; futuro WTI cierre 23-oct 103,27 $ | Coincide con el spot, no con el futuro (serie sin indicar) |
| W43 | «Brent a máximos de cinco meses» | Futuro: cierre 113,17 el 22-oct, el más alto de la serie leída | Plausible, no verificable más allá de un mes |
| W43 | Bloomberg: flujos de Oriente Medio «cerca de niveles prebélicos» | PortWatch Ormuz: 78 buques/día en febrero; 3,7 de media hasta el 18-oct | **No coincide** (~5 % del prebélico) (M6) |
| W43 | Bitcoin bajo 82.000 $ | Coinbase 22-24 oct: 80.700-81.200 $ | Coincide |
| W43 | Ibex −2,12 % y antes +0,28 % hasta 19.000 | Ibex 22-oct −2,12 %; 20-oct +0,28 % (cierre 19.092) | Coincide |
| W43 | Oro <4.000 $, CSI 300 −1,8 %, IPC UK 3,5 % | No consultadas (LBMA en FRED bloqueó; ONS no leída) | No verificables |
| W43 | «[VERIFICAR] tipos Fed 3,50-3,75 %» | 3,75-4,00 % desde el 17-sep; BCE 2,50 % | **Resuelto** |

## Mezclas de series detectadas

- **M1 · Brent futuro frente a spot.** En la semana W41 el futuro cotizó 100-105 $ y el spot EIA (Dated) 125-130 $: 20-25 $ de diferencia. El bot cita ambos sin decir cuál. En W43 el «máximo de 117 $ desde abril» solo cuadra con el spot de otra fecha; el futuro llegó a ~113,5 $.
- **M2 · Plazo del rendimiento.** El mismo día (23-oct): 10 años 5,00 %, 20 años 5,37 %, 30 años 5,33 %. «Bonos por encima del 5 %» (W42) y «Treasury 5,34 %» (W43) no indican plazo.
- **M3 · País.** 5,334 % es el gilt británico a 10 años (21-oct); 5,33 % el bono de EE. UU. a 30 años (23-oct). Sin país ni plazo no se puede atribuir.
- **M4 · PPI.** 6,3 % es PPI de demanda final; el PPI de materias primas da 12,8 %.
- **M5 · Fecha del hecho.** «Fed sube por primera vez desde 2023» (17-sep) e «Ibex cae >2 %» (1-oct) aparecen como hechos de la semana.
- **M6 · Titulares como hechos.** «Ormuz 12 M b/d» (W42) y «flujos prebélicos» (W43) contradicen PortWatch y aun así figuran en «Cifras y datos importantes».

## Regla automática propuesta para el bot de resúmenes (sin IA)

Aplicar en el script, antes de guardar el resumen:

1. **Rendimiento con plazo y emisor.** Si una línea contiene «Treasury», «bono», «rendimiento», «yield» o «gilt» junto a un número con %, exigir plazo (`\b(2|5|10|20|30)\s?(años|Y|-year)\b`) y emisor/país. Si falta, marcar «[SIN PLAZO]» y no copiar la cifra a «Cifras y datos importantes».
2. **Crudo con serie y fecha.** Toda cifra de Brent/WTI lleva `futuro|spot|físico` y fecha AAAA-MM-DD. «Máximo desde…» o «récord» exigen serie y fecha de comparación; si no, [VERIFICAR].
3. **Contraste numérico automático** con `docs/movil/data.json`, FRED y el CSV del Tesoro: si la cifra difiere más de ±0,05 pp (rendimientos) o ±3 % (precios), añadir «[NO COINCIDE CON <serie> <valor> <fecha>]».
4. **Titulares con un solo origen.** Una cifra de «según X» sin segundo origen se queda en «Explicación» con [S] y no pasa a «Cifras y datos importantes».
5. **Hechos con fecha.** «Por primera vez», «récord» o «máximo» exigen la fecha del suceso; si es anterior al lunes de la semana, anteponer «(anterior a la semana)».
6. **Limpieza de [VERIFICAR].** Si existe serie abierta para el nivel (tipos de la Fed, 10 años, Brent futuro), sustituir la duda por el valor y su fecha.

## Pendientes
- Kospi, oro, CSI 300, IPC UK: sin serie abierta leída (ONS, LBMA, Kospi).
- «Récord» del Brent físico y «81 % del Golfo»: faltan series largas (EIA/Kpler).
- Confirmar con la fuente original del bot a qué bono se refería el «5,34 %».
