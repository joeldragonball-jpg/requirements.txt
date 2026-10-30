# C63 · Refresco de datos de países (30-oct-2026) · PARCIAL

**Alcance hecho:** auditoría de frescura, IPC (la causa del atasco en dic-2025) y las cifras de la UE de sanidad y educación. **No hecho:** noticias de 30-60 días, cifras de países fuera de la UE, vivienda construida (`sts_cobp_a` sin datos con los filtros probados). Sin IA ni workflows; solo APIs abiertas de Eurostat y Banco Mundial.

## 1. Auditoría (`python scripts/auditoria_frescura_paises.py`)
Umbral 12 meses (anual) o 3 (mensual/trimestral). Antes: 169 de 342 cifras viejas o sin dato; después: 159. Muchas «viejas» son el último año que publica el Banco Mundial para países fuera de la UE (2023-2024), no un fallo de lectura.

## 2. Por qué el IPC seguía en dic-2025 [P]
Desde enero de 2026 Eurostat usa ECOICOP ver. 2 y base 2025=100; las tablas antiguas (`prc_hicp_manr`, y la serie `ICP` del BCE) quedaron congeladas en dic-2025. La serie viva es `prc_hicp_minr` con `coicop18=TOTAL`, `unit=RCH_A` (actualizada el 16-oct-2026). Fuente: Eurostat, «Information on data» (HICP). Arreglado en `scripts/indicadores.py` y `leer_inflacion` de `scripts/actualizar_paneles.py`.

| IPCA interanual | Antes (dic-2025) | Ahora (sep-2026) | Mes anterior (ago) |
|---|---|---|---|
| España | 3,0 | 5,0 | 4,6 |
| Alemania | 2,0 | 3,3 | 2,9 |
| Francia | 0,7 | 3,4 | 2,6 |
| Italia | 1,2 | 4,2 | 3,2 |
| Países Bajos | 2,5 | 3,0 | 2,8 |
| Polonia | 2,5 | 4,0 | 3,5 |
| Zona euro | 1,9 | 3,8 | 3,2 |

El IPC del INE puede diferir del IPCA. Polonia: PIB 2026-Q2 ya es el último publicado.

## 3. Sanidad y educación UE (Eurostat sustituye al Banco Mundial si el año es más nuevo)
| País · cifra | Antes | Ahora |
|---|---|---|
| ES gasto sanitario % PIB | 9,22 (2023) | 9,2 (2024) |
| ES médicos /1.000 | 4,29 (2022) | 4,64 (2024) |
| ES camas /1.000 | 2,91 (2023) | 2,83 (2024) |
| ES educación % PIB | 4,59 (2022) | 4,1 (2024) |
| DE gasto sanitario | 12,3 (2024) | 12,7 (2025) |
| DE médicos / camas / educación | 4,53 / 7,55 / 5,24 | 4,75 / 7,59 / 4,5 |
| FR gasto sanitario | 11,5 (2024) | 11,5 (2025) |
| FR médicos / camas / educación | 3,28 / 5,65 / 5,32 | 3,94 / 5,34 / 5,1 |
| IT gasto sanitario | 8,44 (2024) | 8,4 (2025) |
| IT médicos / camas / educación | 4,19 / 3,06 / 4,07 | 5,75 / 3,12 / 4,0 |
| NL gasto sanitario | 10,0 (2024) | 10,2 (2025) |
| NL médicos / camas / educación | 3,88 / 2,42 / 5,18 | 3,96 / 2,21 / 5,1 |
| PL médicos / camas / educación | 4,03 / 6,04 / 4,31 | 3,86 / 6,28 / 5,6 |

**Cautelas [VERIFICAR]:** (a) la educación de Eurostat (COFOG, administraciones públicas) no es la misma definición que la del Banco Mundial: los saltos (DE 5,24→4,5; PL 4,31→5,6) son de definición, no de política; no comparar con China, India, etc. (b) Médicos de Italia (5,75) y la media de «médicos en ejercicio» varían por definición nacional. (c) Los años de sanidad 2025 son provisionales de Eurostat. Las lecturas de ES, DE y NL en `estabilidad-manual.json` se actualizaron con las cifras nuevas.

## 4. Vivienda
Sobrecarga del coste de la vivienda (`ilc_lvho07a`) ya estaba al día (2025): ES 7,2 %, DE 11,2 %, FR 6,4 %, IT 5,0 %, NL 6,5 %, PL 4,1 %. Obras de vivienda (`sts_cobp_a`) y homicidios (`crim_hom_soff`): filtros pendientes de ajustar.

## 5. Sigue sin dato o viejo
- EE. UU., China, Japón, India, Reino Unido, Rusia: último año del Banco Mundial (2023-2024); falta contrastar con CMS (gasto sanitario), Census (pobreza, housing starts), NBS, MoSPI, Rosstat.
- Salario mínimo EE. UU. (7,25 $, 2009) y pobreza EE. UU./Japón: nivel V en `indicadores-manual.json`.
- Fallos de lectura en inflación: PCE de EE. UU., Japón y China (FRED agotó el tiempo; se conservó el dato anterior).
- Noticias de 30-60 días (presupuestos, planes de vivienda, pensiones, huelgas): sin hacer.
