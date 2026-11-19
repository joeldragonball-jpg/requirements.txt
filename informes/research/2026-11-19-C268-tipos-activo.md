# C268 · Tipos de activo por red: comprobación del 19-nov-2026

Resultado: la tarea ya estaba implementada en sesiones anteriores (informes 2026-11-14-C268, 2026-11-15-C268-C271 y 2026-11-18-C268). En esta pasada no se añadieron datos nuevos; solo se auditó el estado.

## Qué hay
- `explorador/cadenas.json`: bloque `tipos_activo` en las 16 redes, con `tipos` (valor, nº de activos, detalle de productos), `emisores`, `estandar`, `liquidacion` y, en redes sin cifras, `cualitativo`. Celdas con t/f/u/d/n; sin dato = null. Todo [S] salvo estándar y liquidación [P] donde se leyó la fuente.
- `explorador/vistas.html` (líneas ~2328-2370): tabla «¿Qué se tokeniza en cada red?» con barras bajo la matriz, tooltip y acordeón de productos; fecha y reclasificación del XRPL (14 frente a 19-nov: 41,82 vs 430,96 mil M$ es el total de RWA.xyz, ver `brecha_rwa`).
- Cifras con cobertura numérica: XRPL, Stellar, Hedera, Ethereum, Solana, BNB, Avalanche, Polygon, Algorand (parcial), Plume.

## Huecos (sin fuente leída, quedan como sin dato)
- Canton, Chainlink, Ondo, XDC, Quant, IOTA: solo cualitativo, sin importes.
- Plume: sin emisores (null).
- IOTA: sin plazo de liquidación con fuente.
- Algorand: acciones e inmuebles sin detalle de productos.
- Las clases fuera del top 10 de RWA.xyz figuran como «sin dato», no como cero.
- Los importes son del 14-nov (clases por red); el 19-nov solo se releyeron totales por red en `brecha_rwa`.

## Validación
- `python scripts/revisar_explorador.py`: 0 avisos.
- `python scripts/construir_orbita.py`: OK (docs/orbita/index.html regenerado).
- No se revisó la vista en Chrome en esta pasada; sin commit/push.
