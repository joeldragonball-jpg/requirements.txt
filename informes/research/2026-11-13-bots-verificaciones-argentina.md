# 2026-11-13 · Bot de paneles, verificaciones de alta prioridad y Argentina (C260 parcial)

## Hecho
- **Paneles de datos**: el paso «Descargar los datos» se colgaba 15 min porque `scripts/indicadores.py` pedía al Banco Mundial ~300 datos uno a uno (cada uno hasta 40 s + reintento). Ahora va en 6 hilos con tope de 150 s (lo que no llega conserva el dato anterior) y el paso tiene `timeout-minutes: 8`. Prueba local: 2 min 42 s. Falta ver un run verde en GitHub tras la subida.
- **Verificación mensual**: marcaba rojo por una cancelación manual del 2-nov; `construir_seguimiento.py` ya no cuenta las canceladas manuales de ese bot. No se lanzó nada que gaste API.
- **Verificaciones** (`eventos/verificados.json`): Fed dividida = confirmado [P] (nota del 28-oct: Cook y Hammack votaron por subir); stablecoins −14.200 M$ = matizado (DefiLlama: −14.498 / −14.878 M$ el 11/12-nov; −16.185 M$ el 13-nov; mayor caída a 30 días desde 2022) [S]; petroleros en Ormuz = matizado (UKMTO 2-6-nov; incidente del 12-nov no hallado).
- **Argentina** (INDEC, serie oficial leída en Chrome): IPC oct-2026 33,1 % interanual (2,2 % mensual; 26,3 % acumulado). Dic/dic: 2018 47,6 · 2019 53,8 · 2020 36,1 · 2021 50,9 · 2022 94,8 · 2023 211,4 · 2024 117,8 · 2025 31,5. Pico interanual 289,4 % (abr-2024). El «72→219» eran medias anuales del Banco Mundial (2022 y 2024), no dic/dic. Paro 7,9 % (2T-2026) y pobreza 32,3 % (1S-2026) como [S] vía prensa.

## Lecciones
- Las medias anuales y el dic/dic no se mezclan: cada serie lleva su unidad y la otra va en la nota.
- Los scripts con muchas peticiones lentas necesitan tope total, no solo timeout por petición.
- Una cancelación manual no es un fallo del bot; una cancelación por tiempo sí.
