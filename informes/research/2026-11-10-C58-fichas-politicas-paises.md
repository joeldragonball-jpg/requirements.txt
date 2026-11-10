# C58 · Fichas políticas por país: revisión 10-nov-2026

**Estado:** `explorador/paises.json` ya existe (23 países, incluidos los 12 pedidos: ES, DE, FR, IT, NL, PL, US, CN, JP, IN, GB, RU), generado en sesiones del 30-oct, 2-nov y 8-nov. No se rehízo. Informe de origen: `informes/research/2026-10-30-C58-fichas-politicas.md`.

## Qué cambia con los hechos de esta semana
- **EE. UU. (US):** la ficha debe reflejar las midterms del 3-nov [S]. Senado 54 D - 44 R con 2 escaños sin declarar (Alaska y Mississippi) y Cámara con mayoría demócrata (254-162 según AP/Wikipedia; 259-176 según NBC). Recuento oficial sin certificar: [VERIFICAR]. Detalle en `2026-11-10-C30-politica-elecciones.md`. Los campos `apoyo` y `ultima_eleccion` de `US` deberían pasar a esos valores marcados [S]; no se editó el JSON en esta sesión.
- **España (ES):** la ficha ya recoge el RD 806/2026 y las urnas del 29-nov-2026 [P, BOE-A-2026-20742]. Nada nuevo verificado hoy.
- **Resto (DE, FR, IT, NL, PL, CN, JP, IN, GB, RU):** no se contrastaron cambios hoy. Los campos de elecciones enlazan a `elecciones.json` por id, sin duplicar datos.

## Qué no se cubrió
- No se leyeron fuentes primarias (parlamentos, comisiones electorales) en esta pasada: el tiempo se fue en el recuento de EE. UU.
- `sistemas_publicos` sigue en [VERIFICAR] en varias fichas (pendiente de C61).
- No se ejecutó `scripts/revisar_explorador.py` porque no se cambió ningún JSON.

## Datos contrastados hoy (todos [S], ninguno [P])
1. Senado 54-44 con 2 sin declarar (AP vía NBC/Fox, 10-nov).
2. Mississippi: Colom 49,1 % frente a Hyde-Smith 48,8 %, con el 97,4 % escrutado (NBC).
3. Alaska: Peltola 48,2 % frente a Sullivan 47,9 %, con el 74,1 % escrutado (NBC). Voto por orden de preferencia: puede tardar.
4. Cámara: las cifras difieren de 254-162 a 259-176. Discrepancia entre fuentes sin resolver.

La lectura de las fichas es [ESPECULACIÓN] y no ordena países.
