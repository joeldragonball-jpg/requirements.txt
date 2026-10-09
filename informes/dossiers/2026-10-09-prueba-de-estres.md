# Dossier: Prueba de estrés histórica de una mezcla XRP/XLM (09-10-2026)

> Informativo. No es recomendación de compra ni venta, ni una predicción: **describe qué pasó en el pasado**. Datos: cierres diarios en USD de Yahoo Finance (fuente no oficial, secundaria) desde 09-11-2017 (inicio de datos de XRP y XLM) hasta 09-10-2026. Mezcla de ejemplo: **80 % XRP / 20 % XLM**, rebalanceada cada día (un supuesto: en la práctica nadie rebalancea a diario). Sin comisiones ni impuestos y en dólares (tu coste real está en euros). Se calcula con `scripts/prueba_estres.py` (sin IA).

## 1. Resumen ejecutivo
1. **La mezcla ha llegado a perder 95 % desde su máximo** (pico 07-01-2018, suelo 12-03-2020). XRP y XLM tardaron años en recuperar algo: XRP lo hizo el 2025-07-17; XLM, no recuperado.
2. **Hoy** están a -61 % (XRP) y -78 % (XLM) de su máximo histórico (BTC: -34 %).
3. **Volatilidad anualizada** de la mezcla: 105 % (BTC: 67 %). Un día con caída superior al 10 % ocurrió 66 veces en 3256 días.
4. **Repartir entre XRP y XLM casi no reduce el riesgo**: su correlación diaria es de 0,7 y la caída máxima es parecida en cualquier reparto (§4).
5. **Con qué se mueve (§5):** la mezcla sigue sobre todo a BTC; con Nasdaq, dólar, Brent y tipos las correlaciones semanales son bajas o moderadas [lee la tabla: depende del periodo].
6. **Esto es historia, no destino.** El pasado incluye la burbuja de 2017-18 y un caso judicial de XRP; el futuro puede no repetirse en ninguna dirección.

## 2. Caída máxima y recuperación (cierres diarios)

| Activo | Caída máxima | Pico | Suelo | Recupera el pico |
|---|---|---|---|---|
| XRP | -95,9 % | 07-01-2018 | 12-03-2020 | 2025-07-17 |
| XLM | -96,3 % | 03-01-2018 | 12-03-2020 | no recuperado |
| BTC | -83,4 % | 16-12-2017 | 15-12-2018 | 2020-11-30 |
| Mezcla | -95,4 % | 07-01-2018 | 12-03-2020 | 2024-12-02 |

Nota: la mezcla rebalanceada a diario tiene un efecto estadístico ("ganar vendiendo lo que sube") que puede hacerla parecer mejor que lo que obtendría quien no rebalancea. XLM no ha vuelto a su máximo de 2018.

## 3. Peores ventanas de la mezcla y qué pasó

| Ventana | Peor caída | Terminó | Mediana | Percentil 5 |
|---|---|---|---|---|
| 7 días | -50,5 % | 23-12-2020 | -0,6 % | -16,9 % |
| 30 días | -73,7 % | 05-02-2018 | -2,5 % | -32,4 % |
| 90 días | -83,0 % | 07-04-2018 | -2,0 % | -45,1 % |
| 365 días | -87,4 % | 03-01-2019 | -0,7 % | -65,7 % |

- **Peor semana (termina el 23-12-2020):** coincide con diciembre de 2020, cuando la SEC demandó a Ripple (ver [dossier 10](2026-10-09-ripple-la-empresa.md)): una caída ligada a una noticia concreta de XRP, no al mercado en general [VERIFICAR la relación causal día a día].
- **Peor mes y peor trimestre:** terminan el 05-02-2018 y el 07-04-2018.

## 4. ¿Cambia el reparto entre XRP y XLM el riesgo?

| Reparto | Caída máxima | Volatilidad anual |
|---|---|---|
| 100 % XRP / 0 % XLM | -95,9 % | 111 % |
| 80 % XRP / 20 % XLM | -95,4 % | 105 % |
| 50 % XRP / 50 % XLM | -95,3 % | 102 % |
| 0 % XRP / 100 % XLM | -96,3 % | 109 % |

Lectura: son dos activos muy parecidos en comportamiento (mismo sector, mismas fases del mercado). **No es diversificación en el sentido habitual**; para reducir el riesgo habría que mirar activos de otra naturaleza, algo que este dossier no evalúa.

## 5. Con qué se mueve (correlación de retornos semanales)

| Periodo | Nasdaq | Dólar (DXY) | Tipo a 10 años (Δ pp) | Brent | Oro | BTC | Semanas |
|---|---|---|---|---|---|---|---|
| Todo el histórico | 0,18 | -0,11 | 0,03 | 0,09 | 0,05 | 0,49 | 465 |
| Ciclo de subidas 2022-23 | 0,24 | -0,06 | 0,05 | 0,10 | 0,13 | 0,49 | 71 |
| Últimos 12 meses | 0,34 | -0,22 | 0,15 | 0,10 | 0,12 | 0,84 | 53 |
| Últimos 6 meses | 0,20 | -0,34 | 0,02 | 0,03 | 0,52 | 0,84 | 27 |

Beta semanal de los últimos 12 meses: **1,25** frente a BTC y **1,26** frente al Nasdaq (por cada 1 % que se mueve BTC, la mezcla se movió de media ~1,25 % en el mismo sentido). Correlación no es causalidad, y con pocas semanas (50-70) el dato es poco estable.

## 6. Qué habría perdido la mezcla en esos episodios (porcentajes, no importes)

| Episodio histórico | Variación de la mezcla | Un 100 pasaría a |
|---|---|---|
| Peor semana | -50,5 % | 49 |
| Peor mes (30 días) | -73,7 % | 26 |
| Peor trimestre (90 días) | -83,0 % | 17 |
| Peor año (365 días) | -87,4 % | 13 |
| Caída máxima desde el pico | -95,4 % | 5 |

Para convertirlo a euros: multiplica el porcentaje por el valor de tu cartera. Es un **escenario histórico**, no un pronóstico ni un máximo posible.

## 7. Límites y sesgos
- **Pasado corto y atípico:** XRP y XLM tienen menos de 9 años de datos y una burbuja (2017-18) que domina las peores cifras.
- **Datos:** Yahoo Finance agrega precios de varias plataformas; los cierres de un día pueden diferir del de Kraken.
- **Dólares frente a euros:** tu rentabilidad real depende del tipo EUR/USD, que aquí no se aplica.
- **No incluye** comisiones, impuestos, liquidez al vender ni el riesgo de custodia.
- **No es recomendación**: no dice qué hacer con tu cartera, solo cuánto se ha movido en el pasado.

## 8. Lo que no sé
- Si el futuro se parecerá a algún tramo de este histórico.
- La causa exacta de cada caída (solo he señalado una).
- El efecto real de rebalancear con costes y la liquidez en los momentos de caída fuerte.
