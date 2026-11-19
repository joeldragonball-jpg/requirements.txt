---
tema: Cableado final de C339-C344 en la Órbita y el móvil
fecha: 2026-11-19
etiquetas: [cadenas, etf, solana, movil, voces, integracion]
---
# Cableado final (19-nov-2026)

Informativo; no es recomendación ni se compara con ninguna tesis. Los niveles son los que dejaron los agentes.

## Hecho
1. **Órbita, Paneles de datos > Fondos cripto (ETF)**: la tabla incluye ahora Activos netos en M$ con su fecha, Comisión anual (%), Custodio y Lanzamiento; salen los 8 fondos de Solana (BSOL, GSOL, FSOL, TSOL, VSOL, SOLC, SOEZ y QSOL) con «sin dato» donde no se leyó (QSOL, archivo 404; GXLM sin comisión). Resumen de Solana: suma de los 7 con cifras (≈1.830 M$, cálculo propio, nivel R) y peso de BSOL (≈72 %), datos del 10-Q a 30-sep (trimestrales, no flujos). Desplegable con comisión, custodio y fuente por fondo. Los textos con «null» de los JSON se muestran como «sin dato».
2. **Móvil**: cuatro tarjetas nuevas en Más > Datos (Cadenas: DTCC por red, préstamos y bóvedas, representado o distribuido, qué vigilar), con M$, nivel, fuente y fecha por fila; la tarjeta de ETF añade comisión, custodio, lanzamiento y los fondos de SOL.
3. **Reconciliación XRPL en cadenas.json** (valores no modificados): `rwa` y `tipos_activo` llevan `fecha_dato` = 14-nov-2026 y `reconciliacion_19nov` (nivel R); la fila XRPL de `rwa` marca `reclasificado_en` 19-nov; `brecha_rwa` lleva `fecha_dato` = 19-nov y `reclasificado_desde_14nov` (distribuido 642,8 a 3.008,4 M$; representado 5.207,0 a 2.976,5 M$; reclasificación de RWA.xyz, no flujo). Se pinta en «¿Cuánto se tokeniza?» y en «¿Qué se tokeniza?».
4. **vigilar**: la fila del 13F del 4T lleva la nota del festivo federal del 15-feb-2027 y [VERIFICAR con la SEC] (también visible en la tabla).
5. **Voces**: v212-v222 presentes (221 voces en total en la pestaña; se localizan Kash Dhanda, Scott Lucas, Equiniti, Jane Street y Goldman).

## Comprobaciones
revisar_explorador.py: 0 avisos. construir_orbita.py y construir_movil.py sin errores. Navegador (orbita 8797 y movil 8794): 0 «null/undefined/NaN» en Cadenas, Fichas por activo, Paneles, Voces y las tarjetas nuevas; sin errores de consola ni 404; sin desborde horizontal en móvil.

## Pendiente
- No hay ficha de Solana en fichas-activos.json (solo XRP, XLM, BTC, oro, ETF mundial); los fondos de SOL salen en la tabla de fondos.
- «Flujo diario» de la tabla de ETF sigue mostrando «vacío» (convención previa).
