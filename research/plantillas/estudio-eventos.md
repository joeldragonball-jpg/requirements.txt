# Plantilla: estudio de eventos (noticia → precio) y washouts

Salida: `informes/research/AAAA-MM-DD-<ID>-<tema>.md` y, si hace falta, un script en `scripts/` (Python, sin IA, reproducible).

**Objetivo:** ver qué noticias, decisiones o avances parecen haber movido el precio de XRP/XLM y cuáles no, y detectar caídas bruscas con rebote («washouts») y su relación con el calendario (fin de trimestre o de mes, vencimientos, escrow). **Sin recomendaciones de compra/venta.**

## Método (obligatorio)
1. **Lista de eventos:** mínimo 15, con fecha y hora UTC de la publicación y fuente primaria (no la prensa que lo repite). Sacarlos de `cerebro/documentos/catalizadores-xrp-xlm.md`, `eventos/calendario.toml`, `informes/research/` e `informes/predicciones.md`. Un evento por fila; si hay varios el mismo día, anotarlos juntos.
2. **Precios:** serie horaria de CoinGecko (`market_chart`, ver G17 §4) para XRP, XLM y BTC. Citar siempre ventana, hora UTC y fuente. Dos series del mismo activo no se mezclan.
3. **Ventanas:** −24 h a 0 (antes), 0 a +1 h, +24 h y +7 d. Calcular la variación con script, no a mano (G17 §4).
4. **Efecto relativo, no solo absoluto:** restar lo que se movió el mercado (BTC × beta; la prueba de estrés da beta ≈1,25 en 12 meses, revisar) para ver el movimiento propio de XRP/XLM.
5. **Tasa base:** antes de decir «subió un 20 %», calcular **con qué frecuencia** XRP/XLM se mueven así sin noticia (percentiles de variaciones de 24 h y 7 d, del dossier de estrés o recalculados). La volatilidad anual ronda el 100 %: un 20-30 % en una semana puede ser normal.
6. **Confusores:** FOMC, IPC, empleo, fines de semana, vencimientos, noticias del mismo día, movimientos de BTC. Anotar cuáles coinciden.
7. **Clasificación por evento (obligatoria):** «efecto directo probable» (movimiento relativo claramente fuera de la tasa base, inmediato y sin confusores), «efecto dudoso» (coincide con otros factores o está dentro de lo normal) o «sin efecto detectable». **No escribir «fue por eso» solo por la magnitud**: la coincidencia en el tiempo no es causa.
8. **Washouts:** definir el criterio antes de buscar (p. ej. caída ≥X % en ≤Y h con recuperación ≥Z % en ≤W h) y aplicarlo a toda la serie, no solo a los casos recordados. Cruzar con: fin de mes o trimestre, vencimientos (CME, opciones de Bybit; Deribit no lista XRP/XLM), escrow de Ripple (días 1), cierres de 13F y fines de semana. Liquidaciones: no hay serie pública (R42); usar OI y funding de la bolsa y la CFTC, y decir qué no se puede medir.
9. **Muestra pequeña:** con pocos eventos no hay estadística; decirlo y no extrapolar.

## Informe
- Tabla: evento | fecha/hora UTC | fuente primaria | variación XRP/XLM/BTC por ventana | efecto relativo | tasa base (percentil) | confusores | clasificación.
- Resumen: qué tipos de evento parecen mover más (regulación, ETF, macro, demandas, listados...) y cuáles casi nada, con la salvedad de la muestra.
- Secciones «Hechos y opiniones» y «Qué falta por buscar». Etiquetas [VERIFICAR] / [ESPECULACIÓN].
- Cierre: coste real en `research/COLA.md`; lecciones máx. 5 líneas por archivo; el script en `scripts/` sin claves.
