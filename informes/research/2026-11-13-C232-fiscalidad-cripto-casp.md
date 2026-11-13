---
tema: Fiscalidad cripto en España y CASP bajo MiCA (C232, tercera pasada)
etiquetas: [fiscalidad, cripto, españa, irpf, modelo-721, dac8, mica, casp, esma]
actualizado: 2026-11-13
---
# C232 · Fiscalidad cripto y CASP: lo que ya está leído en la fuente (INFORMATIVO, no es asesoramiento fiscal)

Lecturas del 12-nov-2026. [P] = fuente oficial leída entera o en el artículo citado; [S] = secundaria; [VERIFICAR] = sin leer. Datos volcados en `explorador/regulacion.json` (celdas España › fiscal y España › ley marco).

## HECHOS

### Escala del ahorro (cierra el [VERIFICAR] del 11-nov)
- [P] Arts. 66 y 76 de la Ley 35/2006 (LIRPF), texto consolidado del BOE (API de legislación consolidada, última versión: Ley 7/2024, con efectos desde el 1-ene-2025). Tramo estatal: 9,5 % hasta 6.000 €; 10,5 % hasta 50.000 €; 11,5 % hasta 200.000 €; 13,5 % hasta 300.000 €; 15 % por encima. El tramo autonómico (art. 76) tiene la misma tabla.
- Suma de ambos: **19 % / 21 % / 23 % / 27 % / 30 %**. La cuota acumulada a 300.000 € es 71.880 € (35.940 € en cada tramo). La escala combinada es una suma nuestra de dos artículos leídos, no una tabla literal del BOE.
- [P] Art. 49 LIRPF: las pérdidas patrimoniales se compensan con los rendimientos del ahorro con el límite del 25 % y el resto en los cuatro años siguientes.
- No hay modificación posterior de esos artículos en el texto consolidado a 12-nov-2026: la escala de 2026 es la misma que la de 2025.

### Modelo 721 (cripto en el extranjero)
- [P] Orden HFP/886/2023 (BOE-A-2023-17429): se presenta «entre el 1 de enero y el 31 de marzo del año siguiente»; primera vez, ejercicio 2023.
- [P] Art. 42 quater del RD 1065/2007 (redacción del RD 249/2023): no hay obligación si los saldos a 31 de diciembre no superan en conjunto **50.000 €**; se vuelve a declarar si suben más de **20.000 €** respecto de la última declaración.

### DAC8 y los modelos nuevos (042, 172, 175, 721)
- [P, con límite] En los sumarios del BOE del 1-ene al 12-nov-2026 (60.780 títulos leídos por la API oficial) **no hay ninguna disposición** cuyo título mencione «criptoactivos», «modelo 172», «modelo 175», «modelo 721» ni la Directiva 2023/2226. Límite: es una búsqueda por título; una norma con otro título se escaparía.
- Sigue siendo un proyecto (audiencia pública de marzo de 2026, ya leído el 11-nov).

### CASP: registro interino de ESMA (fichero CASPS.csv, última fila actualizada el 11-nov-2026)
- [P] 407 filas, 404 entidades distintas (LEI). Por país de origen: Alemania 130, Francia 36, Países Bajos 29, Chipre 26, Malta 24, **España 17**.
- [P] Las 17 españolas (todas con la CNMV): 7 entidades financieras por notificación del art. 60 (BBVA 5-mar-2025; Openbank y Cecabank 24-jul-2025; Renta 4 21-nov-2025; Kutxabank y CaixaBank 27-mar-2026; ABANCA 6-nov-2026) y 10 autorizadas por el art. 63 (Bit2Me 31-oct-2025; Due 12-jun-2026; Crossmint y Criptan 26-jun; Minos Global y Prosegur Crypto 30-jun; Iqana 10-jul; Fazil Crypto y Cryptopocket 31-jul; Goin Crypto 9-oct-2026).
- [P] 134 entidades incluyen España entre los países donde prestan servicio (coincide con la cifra de Finect para el 1-jul-2026, que era [S]).
- [P] Con pasaporte a España: Coinbase y Bitstamp (LU), Bitpanda y Bybit (AT), Crypto.com y OKX (MT), Revolut y eToro (CY), Trade Republic (DE), Ripple Payments Europe (LU, 29-jun-2026).
- [P] **Binance y Bitget no aparecen** en el fichero. [VERIFICAR] La fila de Kraken (IE) no lista España en la columna de países.

## OPINIÓN (mía) y sesgos
- Que una entidad no esté en el registro interino no prueba por sí solo que no pueda operar: lo decide el supervisor y el fichero cambia cada semana. No es una lista de «seguras» e «inseguras».
- Caso a favor de la claridad: escala, plazo y umbral ya están en el BOE y no dependen de gestorías. Caso en contra: la pieza que más cambia el día a día (la orden de DAC8 con los modelos nuevos) sigue sin publicarse, así que todo calendario de 2027 es [ESPECULACIÓN].
- Las guías de exchanges y calculadoras fiscales venden servicios: tienden a exagerar sanciones o a simplificar.

## Pendiente
Criterios de la DGT sobre staking, lending y airdrops leídos en la base de consultas; recuento de la lista propia de la CNMV (≈197) y por qué difiere de ESMA; sanciones del 721 tras la sentencia C-788/19.

## Lecciones (máx. 5)
1. La API de legislación consolidada del BOE da el artículo con todas sus versiones: basta leer la última.
2. El buscador web del BOE rechaza consultas por script; la API de sumarios permite construir un índice local de títulos en un minuto.
3. El umbral de un modelo informativo suele estar en el reglamento, no en la orden que aprueba el modelo.
4. El registro de ESMA es un CSV público: contar es mejor que citar a un medio.

## Fuentes
- LIRPF consolidada: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 (arts. 49, 66 y 76)
- Orden HFP/886/2023: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-17429
- RD 1065/2007, art. 42 quater: https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984
- ESMA, registro interino MiCA: https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv
