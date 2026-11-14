# C272: RWA por cadena (manual) y CBDC, 14-nov-2026

Fuente: https://app.rwa.xyz/networks, tabla Networks, «as of 11/14/2026», sin stablecoins; leída en Chrome (texto del DOM). Nivel [S] (agregador, cambia cada hora).
Métrica: columnas «RWA Value (Distributed)» y «RWA Value (Represented)». Distribuido y representado no se suman.

| Red | Distribuido antes (28-oct) | Distribuido ahora | Representado antes | Representado ahora |
|---|---|---|---|---|
| Ethereum | 15.947 M$ | 15.153,5 M$ | 107 M$ | 99,8 M$ |
| Solana | 4.890 M$ | 5.144,6 M$ | 126 M$ | 125,9 M$ |
| Stellar | 3.768 M$ | 4.662,8 M$ | 78 M$ | 77,4 M$ |
| XRPL | 642 M$ | 642,8 M$ | 4.798 M$ | 5.207,0 M$ |

Por qué difieren las fuentes: son lecturas de momentos distintos (el agregador cambia con cada recálculo; cadenas.json dice 5.210 en XRPL frente a 5.207,0 hoy, ±0,1 %), y el 29-oct se leyó con un resumen de modelo, no con la tabla. Ethereum en RWA.xyz agrega L2 [VERIFICAR].

Cambios: explorador/rwa-por-cadena-manual.json (cifras, leido 2026-11-14, campo nuevo `metrica`, nota). explorador/cbdc-blockchains.json: sin cifras RWA.xyz; solo nota «histórico 29-oct, no releído». Su `leido` sigue en 29-oct a propósito.

Propuestas (no aplicadas): en vistas.html, titular «Ethereum y L2» y nota «distribuido ≠ representado, no se suman» junto a Canton/Avalanche; en cadenas.json, nada.
Lectores: explorador.py (clave rwa_cadena_manual/cbdc_blockchains), scripts/construir_movil.py (cabecera «hace N d»).
Cierre: revisar_explorador 0 avisos; construir_orbita y construir_movil ejecutados.
