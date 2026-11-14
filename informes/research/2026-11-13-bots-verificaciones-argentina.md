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

## Añadido el 14-nov (research en paralelo con 3 subagentes; los JSON los edita el coordinador)
- **Voces (W06)**: v159 (OCC NR 2026-92, vigor 18-ene-2027) y v161 (CFTC 9307-26, ANPRM) pasan a «confirmada» solo en su hecho de partida, tras leer yo las notas oficiales. v160 (SEC) queda sin confirmar: la web de la SEC rechazó mi lectura (límite de peticiones). Sin tocar: v138, v163, v059, v162, v137, v135, v131 (matices en el informe del subagente: Swift sin cifra, Binance solo TRM, Goldman sin 125 $).
- **Radar (W03)**: Corea/tokenización: la consulta cerró el 11-nov, `proxima` vaciada (la URL del JSON, 87653, difiere de la que leyó el subagente, 87834: comprobar). España/tokenización: etapa 4 [S] por la autorización de la CNMV a Bit2Me STX (28-oct; solo se leyó título y fecha). Egipto, Etiopía e India: sin etapa nueva (solo fuentes secundarias). Quedan 30 celdas sin dato.
- **Países (C260)**: 11 indicadores nuevos como [S]; Sudáfrica IPC [P] vía SAnews (agencia oficial). Los de Venezuela, Rusia (IPC), Irán y Emiratos no se vuelcan: fuentes contradictorias.
- Lecciones: los subagentes leen con un modelo pequeño (resúmenes), así que las páginas oficiales se cotejan antes de escribir; la web de la SEC limita las peticiones automáticas.
