# Contradicciones entre paneles (autogenerado 2026-11-04, no editar a mano)

Lo regenera `python scripts/contradicciones_paneles.py`. Compara la terminal (`explorador/paneles.json`) con el móvil (`docs/movil/data.json`). Una diferencia = el móvil está desfasado: `python scripts/construir_movil.py`.

- Cifras comparadas: **66** · diferencias: **0**

## Avisos (no son errores)

- Bonos 10 a. (valor): sin pareja en el otro lado → CHN, ITA
- Brent: terminal 106.53 (2026-11-03) y móvil 103.75 (2026-11-04) son de días distintos: no comparables
- Brent spot EIA 123.1 (2026-10-27) frente al futuro 106.53 (2026-11-03): son medidas distintas (spot fechado vs futuro), con fechas lejanas
