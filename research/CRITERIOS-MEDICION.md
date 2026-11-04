# Criterios de medición de predicciones y fuentes (C108, 4-nov-2026)

Objetivo: puntuar a quien predice **sin inventar porcentajes**. Todo lo de abajo son reglas de trabajo [OPINIÓN de diseño]; las predicciones son [ESPECULACIÓN], no hechos. Lo cuenta `python scripts/medicion_predicciones.py` (→ `research/medicion-predicciones.md`). Registro: `informes/predicciones.md`.

## 1. Qué entra en el registro
Entra si tiene las cuatro cosas: **quién** (el que habla, no el que cita), **qué** (enunciado comprobable), **fecha límite** y **cómo se comprueba** (fuente primaria nombrada). Sin fecha límite o sin forma de medirlo, se anota como «sin puntuar» y **no cuenta** para ninguna tasa.

## 2. Estados (cerrados)
| Estado | Cuándo |
|---|---|
| abierta | la fecha límite no ha llegado, o ha llegado y aún no se ha comprobado |
| acertó / falló | comprobado con la fuente primaria del campo «cómo se comprueba»; se anota fecha y enlace |
| resuelta mal planteada | el enunciado no se podía medir o ya era cierto al anotarlo (no puntúa ni a favor ni en contra) |
| sin puntuar | sin fecha, aspiración o juicio no medible (p. ej. «estándar de oro institucional») |

Regla de vencimiento: pasada la fecha límite, la predicción pasa a «vencida» y W06 la comprueba en la semana siguiente. «Parece que falló» no es estado: o se comprueba o sigue abierta.

## 3. Criterios de acierto por tipo
- **Binaria con fecha** («se aprobará antes de X»): acierta si ocurre antes de la fecha, según la fuente primaria. Una aprobación posterior = falló.
- **Cifra o umbral** («Brent a 90 $ en diciembre»): se fija el dato y el día de lectura **al anotarla** (p. ej. cierre diario Yahoo/EIA del 31-dic). Un cruce intermedio no cuenta.
- **Probabilidad** (Polymarket, Kalshi, «~10 %»): no es acierto/fallo. Se guarda la probabilidad y el resultado (0/1) y se evalúa con el **error de Brier** solo cuando haya ≥ 20 de ese tipo [VERIFICAR el umbral]; hasta entonces, solo se muestra la lista.
- **Rango** («entre 1,00 y 1,12 $»): acierta solo si la lectura queda dentro del rango en la fecha fijada.
- **Escenario condicional** («si X, entonces Y»): si la condición no se cumple, queda «sin puntuar», no acertó.

## 4. Cuántas hacen falta
- **n mínimo por fuente para mostrar un %: 5 resueltas** (acertó + falló, sin «mal planteadas» ni «sin puntuar»). Con 5–9, el % se muestra con la nota «muestra pequeña, no concluyente». Hoy ninguna fuente llega a 5 (máximo: DTCC con 1).
- **Nunca** se mezcla la tasa de una fuente con la de otra por tema distinto sin nota.
- Una fuente que repite la misma predicción en varios vídeos cuenta **una vez**.

## 5. Sesgos a vigilar al puntuar
- **Quien cita ≠ quien predice**: «Goldman (vía Despeja La X)» puntúa a Goldman solo si se lee la nota original; si no, se anota la fuente que cita y se marca [VERIFICAR].
- **Supervivencia**: si solo se anotan las predicciones llamativas, el acierto sale inflado. Anotar también las aburridas o fallidas del mismo canal.
- **Plazos largos** (2029, 2031): no puntúan hasta su fecha; no se usan para decir «va acertando».
- **Datos de prensa** [S] no sirven para cerrar; hace falta fuente primaria.

## 6. Relleno de las 58: qué se puede hacer y qué no
Hecho el 4-nov: solo la propuesta; **no se ha reescrito `predicciones.md`** (lo decide W06 con fuente primaria).
| # | Hoy | Propuesta (a confirmar con fuente primaria) |
|---|---|---|
| 1, 13, 50 | sin fecha límite | #1: poner fecha 2026-12-31 (la propia fila dice «revisar en dic»); #13 y #50: dejar «sin puntuar» salvo que alguien fije fecha |
| 9 | «resuelta / mal planteada» | pasar a ese estado cerrado |
| 20 | «contradicho por el ledger [VERIFICAR el panel]» | comprobar qué panel se usó antes de puntuar a CoinDesk |
| 52 | «contradicha por las fuentes [S]» | pasa a «falló» solo con fuente primaria (BCE) |
| 54 | parte alcista ya superada; nota de Goldman no leída | buscar la nota original; hasta entonces no puntúa a Goldman |
| 55, 56, 57 | aspiración / no medible | «sin puntuar» |
| 7, 25 | vencidas el 3-nov sin resultado | comprobar el 4-nov (resultado de las elecciones y de la votación) |

## 7. Lo que sigue (C92)
Añadir al registro las columnas `fuente_id` (la `v###` de `voces.json` cuando exista) y `fecha_limite` normalizada, y que `medicion_predicciones.py` las use. Hasta entonces la fuente se deduce del texto de «Quién».
