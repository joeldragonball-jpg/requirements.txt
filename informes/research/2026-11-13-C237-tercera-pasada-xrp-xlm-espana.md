---
tema: Coherencia entre informes y datos: tercera pasada de XRP, XLM y España (C237)
etiquetas: [coherencia, xrp, xlm, españa, fichas, cobertura]
actualizado: 2026-11-13
---
# C237 · Tercera pasada: qué hechos verificados faltaban de verdad en la Órbita

Local, sin IA. Medido con `python scripts/cobertura_hechos.py` (12-nov-2026) y revisado a mano con búsquedas del identificador de cada hecho en `explorador/*.json`.

## Medición (hechos de nivel P)
| Ámbito | Está | Dudoso | Falta (según el medidor) | Faltaban de verdad |
|---|---|---|---|---|
| XRP | 21 | 20 | 21 | 4 temas |
| XLM | 9 | 7 | 3 | 0 |
| España | 56 | 22 | 9 | 2 temas |

El medidor sigue sobrestimando: de los 21 «faltan» de XRP, 9 eran estados intermedios de la misma enmienda (fixCleanup3_4_0), ya superados por su activación del 4-nov, y otros 7 ya estaban en `datos.json` (BatchV1_1, Meritz, cierre del litigio) o eran lecturas del estado del nodo sin valor duradero. Varios de España estaban con otro formato de número (18806.1 en lugar de 18.806).

## Volcado

### XRP → `explorador/fichas-activos.json` (ficha XRP, de 14 a 21 hechos)
- Litigio SEC-Ripple: sube a nivel P con la cifra exacta (multa de 125.035.150 USD; apelaciones desistidas el 7-ago-2025; SEC LR-26369).
- XRP en poder de Ripple a 30-jun-2026: 37.656 M (32.600 M en escrow); distribuidos 62.329 M (declarado por Ripple).
- Evernorth, S-4/A n.º 6 (12-ago-2026): 84,37 M XRP comprados por 214 M USD (media 2,5366 USD) y ≈388,1 M aportados en especie.
- RLUSD: 977,6 M USD en el XRPL (29-oct-2026); 2.382,8 M en todas las cadenas y 2.528,0 M de reservas declaradas (22-oct-2026).
- XRPL: LendingProtocol y SingleAssetVault no activados (3-nov-2026).

### XLM
- Nada que volcar: BVNK, USDT0, validadores de nivel 1 y Protocolo 29 ya estaban en `datos.json`.

### España → `explorador/espana-manual.json` (bloque nuevo `cotizaciones_y_tributos`)
- SMI 2026: 1.221 €/mes en 14 pagas (RD 126/2026, **releído hoy en el BOE**: «40,70 euros/día o 1.221 euros/mes»).
- Autónomos 2026: tipo total 31,50 %, base mínima 653,59 €/mes y máxima 5.101,20 €/mes (Orden PJC/297/2026); MEI 0,90 puntos.
- Cataluña: ITP del 5 % para menores de 36 años con base de hasta 36.000 €.

## No volcado (y por qué)
- Verifactu (plazos de 2027), campaña de la renta 2025 y criterio FIFO del Manual de Renta: son fechas o criterios, no cifras, y el bloque de la vista solo admite valores numéricos. El FIFO ya está en la Matriz de regulación.
- Dudosos de XRP y XLM (27): no revisados uno a uno en esta pasada.
- Discrepancia abierta: Evernorth 388,1 M (S-4/A) frente a 388,9 M en otro informe [VERIFICAR].

## Coherencia detectada entre almacenes
1. `espana.json` llevaba 8 días sin regenerar: cuatro bloques manuales no llegaban a la Órbita (arreglado, ver informe S6).
2. `leer_espana_empresas.py` habría pisado lo leído a mano en ENAIRE y Adif al ejecutarse de nuevo: ahora respeta las fichas con campo `revisado`.
3. La Matriz decía «16 CASP españoles» y «134 queda superada»: el registro de ESMA da hoy 17 y 134 (ver informe C232).

## Lecciones (máx. 5)
1. Antes de volcar, buscar el identificador (número de ledger, de release, importe exacto), no fiarse del medidor.
2. Una serie de estados intermedios de un mismo hecho cuenta como uno.
3. Si un script regenera un JSON que también se edita a mano, hay que marcar lo manual para que no se pierda.
