# C269 · Regla reproducible para «Captura del token» (Cadenas) · 14-nov-2026

Fuente: `explorador/cadenas.json` (campos `capas.*.token` y `captura.nivel`). Script: `scripts/regla_captura.py` (solo lee; no modifica datos). Todo lo que sigue es [RAZONADO]: un criterio propuesto, no un dato.

## Hallazgo sobre la regla escrita
La leyenda de la vista (clase `cad-ley` en `explorador/vistas.html`) dice que es «un juicio [RAZONADO] sin fórmula numérica» apoyado en la columna «Capas: ¿token?». Define alta/media/baja por texto y «incierta» = falta de dato público (volúmenes, papel del token). No indica cuántas capas ni qué umbral.

## Regla propuesta (v1)
- Puntos por capa (liquidación, emisión, seguridad, mensajería, custodia): sí=2, parcial=1, mínimo=0,5, no=0; «sin dato» se excluye.
- Menos de 3 capas con dato: **incierta**.
- Puntuación = suma / (2 × capas con dato).
- **alta**: puntuación ≥ 0,60 y liquidación o emisión en «sí». **media**: ≥ 0,35 o al menos un «sí». **baja**: el resto.
- Aviso aparte: si `sin_dato` cita volumen y el nivel es alta/media.

## Resultado (9 discrepancias de 16)
| Red | Nivel actual | Nivel por regla | Puntuación | Discrepancia |
|---|---|---|---|---|
| xrpl | incierta | baja | 0,15 | Sí |
| stellar | baja | baja | 0,15 | No |
| hedera | baja | baja | 0,31 | No |
| ethereum | media | alta | 0,70 | Sí |
| solana | media | media | 0,55 | No (aviso volumen) |
| bnb | incierta | alta | 0,69 | Sí |
| avalanche | incierta | media | 0,44 | Sí |
| polygon | baja | media | 0,56 | Sí |
| canton | media | media | 0,40 | No (aviso volumen) |
| chainlink | baja | baja | 0,20 | No |
| ondo | baja | baja | 0,00 | No |
| algorand | incierta | media | 0,56 | Sí |
| xdc | incierta | incierta | (1 capa con dato) | No |
| quant | incierta | baja | 0,20 | Sí |
| iota | incierta | media | 0,58 (3 capas) | Sí |
| plume | incierta | media | 0,44 | Sí |

## Lectura y propuesta de revisión [RAZONADO]
- La regla solo mira qué capas usan el token; el nivel escrito mezcla además «falta de dato de volumen». Por eso 7 de las 9 discrepancias son redes marcadas «incierta» a mano (xrpl, bnb, avalanche, algorand, quant, iota, plume). Decisión previa: ¿«incierta» = pocas capas con dato (regla) o = dato clave ausente como el volumen (juicio)? Si es lo segundo, la regla debería añadir una condición explícita (p. ej. «sin_dato» cita volumen y la capa de liquidación es «parcial»), lo que haría coincidir a xrpl.
- Revisar primero: **ethereum** (regla alta; hoy media, con liquidación y emisión en «sí»: ¿falta justificar por qué no es alta, p. ej. por stablecoins como activo de uso?), **polygon** (baja a mano con liquidación y seguridad en «sí»; el mecanismo escrito debería explicar la rebaja) y **bnb** (alta por regla, con la salvedad de dependencia de Binance en `sin_dato`).
- Revisar después: **iota** (solo 3 capas con dato, límite de la regla), **quant** (token en seguridad «parcial» pero el resto «no»: baja por regla frente a incierta escrita; el sesgo de la fuente pesa).
- Sin cambios necesarios: stellar, hedera, solana, canton, chainlink, ondo, xdc.
- Límite: umbrales (0,60 / 0,35) y pesos son elegidos por criterio, no calibrados; conviene fijarlos con Joel antes de escribir nada en la vista. No es previsión de precio ni recomendación.

Reproducir: `PYTHONIOENCODING=utf-8 python scripts/regla_captura.py` (`--json` para salida estructurada).
