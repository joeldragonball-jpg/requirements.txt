# Contradicciones entre paneles (autogenerado 2026-11-23, no editar a mano)

Lo regenera `python scripts/contradicciones_paneles.py`. Compara la terminal (`explorador/paneles.json`) con el móvil (`docs/movil/data.json`). Una diferencia = el móvil está desfasado: `python scripts/construir_movil.py`.

- Cifras comparadas: **68** · diferencias: **0**

## Avisos (no son errores)

- Bonos 10 a. (valor): sin pareja en el otro lado → CHN, DEU, ITA
- Brent: terminal 89.87 (2026-11-20) y móvil 89.53 (2026-11-23) son de días distintos: no comparables
- Brent spot EIA 92.94 (2026-11-17) frente al futuro 89.87 (2026-11-20): son medidas distintas (spot fechado vs futuro), con fechas lejanas
