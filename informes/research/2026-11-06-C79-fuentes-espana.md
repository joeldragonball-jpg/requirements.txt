# C79 · Fuentes de España probadas con Chrome (6-nov-2026)
Solo lectura; sin descargas. Chrome accedió sin captcha ni anti-bot en todas.

| Fuente | Resultado | Dato | Nivel | URL |
|---|---|---|---|---|
| Tesoro, estadísticas mensuales | Se lee el índice; PDF/XLSX no legibles (visor sin texto). Boletín disponible: octubre 2026 | Listado de series (nominal, vida media, tipo medio, financiación 2026, vencimientos 2026-2071) | P | https://www.tesoro.es/deuda-publica/est%C3%A1disticas-mensuales (enlace real: `/deuda-publica/estad%C3%ADsticas-mensuales`) |
| Tesoro, valores en circulación | Se lee completo | Letras: 12 emisiones (dic-2026 a nov-2027), saldos 4.173-9.299 M€ cada una, datos a 06/11/2026. Bonos/Obligaciones: saldos por ISIN a 31/10/2026 (p. ej. 30/10/2030 1,25%: 30.246 M€; 31/10/2071 1,45%: 9.161 M€; BTP 2064 4,00%: 1.000 M€) | P | https://www.tesoro.es/deuda-publica/valores-del-tesoro/valores-en-circulacion |
| Tesoro, vida media / tipo medio / emisiones del año | No leído (PDF/XLSX) | Pendiente: Joel descarga `/documents/d/tesoro/02-pdf`, `03-pdf`, `09-pdf`, `11-pdf` | VERIFICAR | https://www.tesoro.es/documents/d/tesoro/02-pdf |
| AIReF, nota 4-nov-2026 | Se lee (con JS) | Previsión déficit 2,8 % PIB en 2026 y 2,6 % en 2027 (3 % en 2031); deuda a 95,4 % del PIB en 2031; PIB 2026 2,6 % y 2027 2,2 %; crecimiento medio del gasto primario neto 5,7 % (2026-28) frente a 3,2 % comprometido; prevé incumplimiento del plan fiscal europeo desde 2026 y riesgo de incumplir la regla de gasto nacional en 2026-27 (Administración Central y casi todas las CCAA) | P | https://www.airef.es/es/la-airef-preve-el-incumplimiento-del-plan-fiscal-comprometido-con-europa-desde-2026-pese-a-los-mecanismos-de-flexibilidad/ |
| IGAE, plan de control | Inicio y menú abren; planes de control en PDF (no legibles). | Sin cifra | VERIFICAR | https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Control/Paginas/Control.aspx |
| BDNS (CEAR) | API de lectura responde (200) pero `beneficiario` exige un formato que no conseguí (400 con NIF/nombre; 15530 devuelve 0 filas, id al azar, sin valor) | Sin datos de CEAR | VERIFICAR | https://www.infosubvenciones.es/bdnstrans/GE/es/concesiones/busqueda |
| Transportes cap. 6 / Adif | Sitios abren; no se halló la página de presupuesto (404; transparencia/economica redirige a la home) | Sin cifra | VERIFICAR | https://www.adif.es/sobre-adif/transparencia/economica |

Nota: el sesgo de AIReF es de organismo independiente oficial; sus cifras son previsiones [ESPECULACIÓN] frente a los hechos de Tesoro.
Nota: al navegar al PDF `02-pdf` puede haberse descargado un archivo en Descargas del navegador; revisar y borrar si aparece.

## Filas propuestas para `explorador/espana-manual.json` (no editado)
```json
{"airef_informe_nov2026": {"fecha": "2026-11-04", "deficit_2026": 2.8, "deficit_2027": 2.6, "deficit_2031": 3.0, "deuda_2031_pib": 95.4, "pib_2026": 2.6, "pib_2027": 2.2, "gasto_primario_neto_medio_2026_28": 5.7, "gasto_comprometido": 3.2, "conclusion": "prevé incumplimiento del plan fiscal europeo desde 2026 y riesgo en la regla de gasto de Administración Central y casi todas las CCAA en 2026-27", "nivel": "P", "fuente": "https://www.airef.es/es/la-airef-preve-el-incumplimiento-del-plan-fiscal-comprometido-con-europa-desde-2026-pese-a-los-mecanismos-de-flexibilidad/"}},
{"tesoro_circulacion": {"fecha_letras": "2026-11-06", "fecha_bonos": "2026-10-31", "letras_emisiones": 12, "nota": "saldo por ISIN; sumar para el total antes de publicar", "nivel": "P", "fuente": "https://www.tesoro.es/deuda-publica/valores-del-tesoro/valores-en-circulacion"}}
```
Pendiente (Joel, descarga): vida media, tipo medio, emisiones 2026 del Tesoro; cap. 6 de Transportes; beneficiario CEAR en BDNS.
