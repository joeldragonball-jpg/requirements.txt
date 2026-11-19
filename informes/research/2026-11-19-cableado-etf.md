---
tema: Cableado de los campos nuevos de etf-flujos.json en la Órbita y el móvil
fecha: 2026-11-19
etiquetas: [etf, solana, xrp, farside, movil, orbita]
---
# Cableado ETF (19-nov-2026)

Informativo; no es recomendación. Niveles tal como los dejó C343 segunda (P emisor/SEC, parte interesada; S agregador).

## Órbita (Paneles de datos > Fondos cripto), `nEtf` y `etfContraste` en explorador/vistas.html
- Nueva sección «Inicio de cotización y exención de comisión»: aviso de que el flujo diario solo existe en 2 de 17 fondos (XRP 0,00 M$ el 17-nov; GXRP -1,12 M$ el 18-nov) y tabla con inicio_cotizacion, exencion_vigente (con fecha de fin donde consta, p. ej. TSOL del 28-jul-2026 al 27-jul-2027), comisión y columna Aviso [VERIFICAR] (TSOL, VSOL, SOLC). Nota: la exención es temporal; GXLM cobra 2,50 % anual.
- Desplegable de instantáneas de Bitwise XRP (30-sep: 614,85 M$, NAV 16,62 cálculo propio; 12 a 17-nov) y QSOL (30-sep: 6,83 M$; 18-nov: 3,41 M$ con NAV 7,33), con origen y nivel.
- Bloque «Contraste de Solana» (nivel S): suma de 10 días hábiles (5 a 18-nov) -45,3 M$, serie diaria con BSOL y GSOL («sin dato» donde Farside no los desglosa), aviso de que Farside no incluye QSOL ni SOLC y que XRP no tiene contraste [VERIFICAR].

## Móvil (tarjeta «ETF cripto», scripts/construir_movil.py + docs/movil/index.html)
- Línea de cobertura de flujos, inicio y exención por fondo (con [VERIFICAR] conservado aunque se acorte el texto), instantáneas XRP/QSOL, y serie Farside de SOL con la suma -45,3 M$ y nota de nivel S.

## Comprobaciones
revisar_explorador.py: 0 avisos. construir_orbita.py y construir_movil.py sin errores. Navegador (orbita 8797, movil 8794): sin errores de consola ni 404; 0 «null/undefined/NaN» en el bloque; sin desborde horizontal en móvil. Se corrigió un error propio (sd sin definir en etfContraste) antes del cierre.

## Pendiente
- Los textos largos de inicio/exención se recortan en móvil (el detalle completo está en la Órbita).
- Cobertura diaria sigue limitada: Canary, Franklin y Fidelity sin web legible; segunda lectura pendiente en BSOL, GSOL, TSOL, VSOL, QSOL, TOXR.
