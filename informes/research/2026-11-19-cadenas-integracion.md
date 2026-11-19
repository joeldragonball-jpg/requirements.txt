---
tema: Integración de C339-C341 en la pestaña Cadenas
fecha: 2026-11-19
etiquetas: [cadenas, dtcc, xrpl, rwa, integracion]
---
# Integración C339-C341 en explorador/cadenas.json (19-nov-2026)

Informativo; no es recomendación ni se compara con ninguna tesis. Los niveles son los de los agentes (no se ha subido ninguno).

## Qué se añadió a cadenas.json (esquema de celdas {t,f,u,d,n})
- `dtcc_ruta`: hoja de ruta DTCC por red (Canton en vivo 28-oct-2026 [P]; Stellar 1S-2027 [P]; Solana 2S-2027 [P]; XRPL «no consta» [R]; Ethereum sin dato). Besu y Arc van en un bloque aparte («otras»), no son cadenas del explorador. Incluye carta SEC 11-dic-2025, lanzamiento y ficha At-a-Glance. Las notas leídas con lector que resume conservan su cautela [VERIFICAR].
- `rendimiento_redes`: XRPL LendingProtocol y SingleAssetVault sin activar el 19-nov (25/35 y 24/35, umbral 28; votos [S] de xrpscan; estado enabled=false [P]); Blend (Stellar, TVL 104,4 M$, prestado 32,5 M$), Kamino y Jupiter Lend (Solana) [S, DefiLlama]. También sustituye `matriz.rendimiento` de XRPL por la celda de C340 (P).
- «22 de 29»: no se añadió como hito (no es un evento); queda como corrección dentro de la celda de votos (24-25 de 35 a 19-nov, no coincide con la voz de vídeo).
- `brecha_rwa`: totales RWA.xyz 19-nov (472.800 M$; distribuido 41.840), tabla por red (Ethereum, Solana, Stellar, XRPL, Avalanche, Canton) con distribuido, representado, % distribuido, DeFi RWA, stablecoins y TVL de cadena en M$; cotejo de la cifra de Jupiter; trampas: reclasificación de XRPL 14→19-nov (representado 5.207→2.976 y distribuido 643→3.008 M$, no es flujo), Canton 89,3 % del representado, stablecoins separadas y cobertura parcial de DefiLlama. Celdas de cálculo propio (R) apuntan al informe, no a la URL del agregador.
- `vigilar`: tabla «Qué vigilar»: XRPL enmienda (sin fecha; umbral 28 de 35 y 2 semanas con >80 %), Stellar 1S-2027, Solana 2S-2027 y 13F del 4T ≈15-feb-2027.

## Cautelas
- 13F del 4T: la fecha sale solo del documento interno cerebro/documentos/catalizadores-xrp-xlm.md («≈15-feb-2027»), nivel V; el 15-feb-2027 es festivo federal en EE. UU., así que el plazo real puede correrse un día [VERIFICAR con la SEC].
- La tabla 14-nov del bloque `rwa` y `tipos_activo` NO se tocó: siguen con datos del 14-nov; los de 19-nov están en `brecha_rwa`. XRPL difiere entre ambos por la reclasificación de RWA.xyz.
- No hay «tabla de seguimiento» propia en la pestaña: la línea «Qué vigilar» se pintó como bloque de la pestaña Cadenas. No se tocó research/tareas.csv ni el Seguimiento.
- Sin dato (null): Canton stablecoins; Ethereum en DTCC; préstamos en XRPL por otras vías; definición del 3.400 M$ de Jupiter; desglose DeFi por red de RWA.xyz.

## Pintado y comprobaciones
- vistas.html: cuatro cajas nuevas en Cadenas (ids cad-dtcc, cad-prestamos, cad-brecha, cad-vigilar), tablas con desplazamiento horizontal, M$ explícitos y «sin dato»/«sin protocolo» en vez de null. Comprobado en el navegador («orbita», marco de 1100 px): sin desbordes de página, 0 «null/undefined/NaN», sin errores de consola.
- revisar_explorador.py: 0 avisos (se añadió validación de los 4 bloques nuevos; antes dio 2 avisos por niveles distintos en una misma URL, resueltos apuntando las celdas R al informe).
- construir_orbita.py y construir_movil.py ejecutados sin errores. construir_movil no pinta los bloques nuevos (solo lee `rwa` del 14-nov); pendiente si se quiere en móvil.
