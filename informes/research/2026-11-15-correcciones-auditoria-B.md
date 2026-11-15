# Correcciones de la auditoría Opus (parte B: cadenas.json y vistas.html), 15-nov-2026

Hecho:
- cadenas.json, XDC `cumplimiento`: ahora «anunció la compra», 22-oct-2025, nivel P, enlace a EZ Newswire (igual que el hito). Parte interesada, sin cierre confirmado.
- cadenas.json, XDC `credito`: nivel P a S; los bancos (MUFG, ICBC, Bank of China, DBS) llevan «[VERIFICAR]»: solo constan en la web de TradeFinex.
- vistas.html, España vivienda: aviso visible «serie hasta 2020» en el alquiler (usa el campo `aviso` del JSON si existe; también para el IPV).
- vistas.html: bloque renombrado a «Fondos cripto (ETF y fideicomisos)»; GXLM marcado «fideicomiso OTC, no ETF en bolsa».
- vistas.html, OCDE/BIS: fecha por observación (ya salía), atenuado si pasa de 18 meses, China «LPR a 1 año» y nota.

No hecho / no procede:
- frescura.json no se usa en vistas.html (solo `manuales`), así que no hay nada que corregir allí.
- regulacion.json: sin cambios necesarios.
- IPV 2026T2 (tabla INE 79563), Plume/IOTA, GDELT y móvil: son de scripts/otros JSON.
