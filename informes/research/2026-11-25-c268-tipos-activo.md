# C268 tipos_activo: comprobación 25-nov-2026

Hechos (fuente y fecha):
- `explorador/cadenas.json` ya tiene el bloque `tipos_activo` en las 16 redes (trabajo del 14 y 15-nov: tipos, emisores, estándar y liquidación; productos principales por tipo en `detalle`). No se ha añadido nada nuevo en esta pasada: sin cambios en el JSON (git diff vacío para cadenas.json).
- RWA.xyz, ficha de Ethereum, leída en Chrome el 25-nov-2026 («as of 11/25/2026») [S]: distribuido 14,14 B$ (-13,08 % en 30 días), representado 71,77 M$, 3.378 activos. Las celdas del JSON siguen con el dato del 14-nov (15.153,5 M$ distribuidos): no se han sobrescrito porque la pestaña «Asset Classes» no se releyó entera.
- Franklin Templeton (ficha FOBXX): la página solo devuelve «Loading...» al lector, sin contenido. Securitize (nota de BUIDL): sin texto legible. Plazo contractual de BENJI/BUIDL/WTGXX sigue sin dato primario [VERIFICAR].

Validación: `python scripts/revisar_explorador.py` = 0 avisos.
Pendiente: refrescar cifras por clase al 25-nov y plazos contractuales de BENJI/BUIDL/WTGXX (probar PDF del prospecto).
