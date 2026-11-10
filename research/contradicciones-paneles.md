# Contradicciones entre paneles (autogenerado 2026-11-10, no editar a mano)

Lo regenera `python scripts/contradicciones_paneles.py`. Compara la terminal (`explorador/paneles.json`) con el móvil (`docs/movil/data.json`). Una diferencia = el móvil está desfasado: `python scripts/construir_movil.py`.

- Cifras comparadas: **69** · diferencias: **0**

## Avisos (no son errores)

- Bonos 10 a. (valor): sin pareja en el otro lado → CHN, ITA
- Brent: terminal 97.86 (2026-11-06) y móvil 90.76 (2026-11-10) son de días distintos: no comparables
- Brent spot EIA 107.03 (2026-11-03) frente al futuro 97.86 (2026-11-06): son medidas distintas (spot fechado vs futuro), con fechas lejanas
