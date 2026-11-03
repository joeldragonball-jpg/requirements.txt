# Datos vivos automatizados (3-nov-2026)

Funciones nuevas en `scripts/actualizar_paneles.py`; salida en `explorador/paneles.json` (claves nuevas). Si una fuente falla se conserva el dato anterior. Sin claves; certificados verificados. Nada es recomendación.

## Claves nuevas
| Clave | Fuente (API abierta) | Último dato | Cadencia |
|---|---|---|---|
| `espana_hipotecas` | INE Tempus: HPT34618 (nº), HPT34565 (importe, miles €), HPT64408 (tipo medio); importe medio calculado | ago-2026 (provisional): 33.841 hipotecas de vivienda (+2,3 % a/a), importe medio 181,3 mil € (168,4 hace 12 m), tipo medio 3,08 % | mensual; próxima 25-nov |
| `vivienda_eurostat` | Eurostat `prc_hpi_q` (a/a) | 2T-2026: EA 4,0 %, ES 12,1 %, DE 0,6 %, FR -0,8 %, IT 4,0 %, PT 16,5 %, NL 4,3 % | trimestral |
| `brasil` | BCB SGS 432, 20774, 25499 + Olinda/Focus | Selic 13,75 % (4-nov); SGS 20774 = 11,31 % (sep); SGS 25499 = 0,90 % (sep); Focus 30-oct: IPCA 2026 5,22 % / 2027 4,76 %, PIB 1,76 % / 1,20 %, Selic fin-2026 13,50 % / fin-2027 12,50 %, USD/BRL 5,34 / 5,40 | mensual / semanal (Focus) |

## Pendiente [VERIFICAR]
- **SGS 20774 y 25499**: el plan los daba como «tipos de financiación inmobiliaria». 20774 (~11 %) encaja con un tipo; 25499 (~0,9 %) parece más bien morosidad. Definición exacta en el catálogo del BCB sin confirmar; las etiquetas lo dicen.
- Focus = expectativas [ESPECULACIÓN], no dato.
- INE: los importes están en miles de euros según la tabla; coherente con el importe medio ~181 mil €, pero [VERIFICAR] la unidad con la nota del INE.

## Huecos de C31
- **PCE EE. UU.**: ya existía vía FRED (`PCEPI`); hoy FRED sí respondió (sep-2026: 3,6 % a/a). Con timeouts el código lo omite y conserva el dato previo.
- **Japón**: el e-Stat Dashboard (API abierta) dio 502 en dos intentos; sigue el IPC del BIS [S] (2,1 %). No hay alternativa abierta localizada (e-Stat oficial pide appId).
- **China**: la NBS no ofrece API; sigue BIS [S] (0,9 %).
- **Contraste con fuente oficial** (cifras de `inflacion`): ES IPCA 5,0 % y EA 3,8 % (sep-2026) = Eurostat según `C-espana.md`; Brasil 4,58 % = IBGE según `E-sudamerica.md`; IPC INE de España oct-2026 4,9 % (aparte, serie `IPC290750`); EE. UU. IPC 3,7 % y PCE 3,6 % sin contrastar con nota oficial BLS/BEA en esta sesión [VERIFICAR].

## Notas de ejecución
- El run completo omitió `credito` y `materias` por superar los 200 s (BCE con 500/504, FRED lento) y `ormuz` falló (`KeyError: 'features'`): preexistentes, se conservó lo anterior.
