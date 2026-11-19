# KID/KIID IWDA y VWCE, Plume y Quant (18-nov-2026)

Sin recomendaciones. Nivel: P = documento del emisor leído (parte interesada); [VERIFICAR] = no contrastado.

## 1. Documentos descargados (research/fuentes/kid/)
- `iwda-kid.pdf`: KIID de iShares Core MSCI World UCITS ETF USD Acc, ISIN IE00B4L5Y983, versión Reino Unido, exacto a 9-feb-2026. Fuente: ishares.com/gls-download (enlace en la ficha del fondo). [P]
- `vwce-kiid.pdf`: KIID de Vanguard FTSE All-World UCITS ETF USD Acc, ISIN IE00BK5BQT80, exacto a 28-jul-2026. Fuente: fund-docs.vanguard.com (enlace en vanguard.co.uk). [P]

| Dato | IWDA | VWCE |
|---|---|---|
| Gastos corrientes | 0,20 % | 0,14 % (ejercicio dic-2025; rebaja desde 28-jul-2026) |
| Indicador de riesgo (escala 1-7 UCITS) | 6 | 6 |
| Periodo de mantenimiento | «medio a largo plazo», sin años | no consta |
| Rentabilidad 2025 / 2024 / 2023 / 2022 (USD, tras gastos) | 21,1 / 18,7 / 23,8 / -18,1 % | 22,6 / 17,2 / 22,0 / -18,1 % |

Límite: son KIID (UCITS), no el KID PRIIPs. No traen SRI de 7 niveles ni escenarios. La página ES de iShares redirige al directorio global y la ruta KID de Vanguard probada da 403. KID PRIIPs: [VERIFICAR] (probar en Chrome / bróker).
Vuelco: `explorador/fichas-activos.json`, ficha etf_mundial, 10 hechos nuevos (escenarios = null).

## 2. Plume (PLUME)
Fuente: docs.plume.org (páginas «PLUME ($PLUME)» y «Gas and Fees», leídas en Chrome 18-nov-2026; parte interesada; «actualizadas hace 1 año») [P].
- Papel: gas, gobernanza, staking e incentivos. Suministro total 10.000 M; 20 % circulante en el TGE; reparto 59 % comunidad/ecosistema/fundación, 21 % inversores iniciales, 20 % equipo.
- Gas: modelo tipo Arbitrum, tarifa base dinámica, propinas ignoradas, pagado en PLUME. No consta quema de comisiones ni reparto a poseedores.
- Sin dato: tasa de staking, desbloqueos de inversores/equipo.
- Registro SEC: sin cambios sobre lo ya anotado (Dinari TA en EDGAR; sin ficha de Plume) [VERIFICAR].

## 3. Quant / Overledger (QNT)
- Chrome 18-nov: quant.network/overledger-platform/ carga (ya no da 403) pero su texto no contiene QNT, licencia, precio ni comisión. /quant-net/ no se pudo leer (pestaña de Chrome perdida).
- Licencias de Overledger en QNT: sigue sin documento primario; solo Blockworks/ByteTree [S]. Abierto.

## Ficheros tocados
`explorador/fichas-activos.json`, `explorador/cadenas.json` (plume.captura.mecanismo, plume.sin_dato, quant.sin_dato), `research/fuentes/kid/*.pdf`, este informe.
