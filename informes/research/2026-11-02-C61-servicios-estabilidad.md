# C61 · Servicios públicos y estabilidad: qué métricas hay por país y qué se añade (2-nov-2026)

Continúa [2026-10-30-C61-estabilidad.md](2026-10-30-C61-estabilidad.md) (234 cifras, 12 países, en `explorador/estabilidad.json`). No se ha tocado ningún dato compartido: las filas nuevas están en `informes/research/2026-11-02-C61-filas.json` (186 filas, JSON válido) para que C39 las vuelque en los paneles existentes por país + dimensión. Nivel: [P] primaria o dato publicado por organismo · [VERIFICAR] sin dato o dudoso. Sin recomendaciones.

## 1. Métricas que YA hay por país (estabilidad.json)
| Dimensión | Métrica | Países | Años |
|---|---|---|---|
| Sanidad | Gasto total % PIB; gasto por habitante ($); esperanza de vida; mortalidad infantil; médicos y camas por 1.000 | 12 | 2020-2025 |
| Infraestructuras | Banda ancha fija; importaciones netas de energía | 12 | 2023-2024 |
| Trabajo | Empleo vulnerable | 12 | 2025 |
| Educación | Gasto público % PIB | 12 | 2021-2024 |
| Seguridad | Homicidios (UNODC); WGI estabilidad política, imperio de la ley, corrupción | 12 | 2020-2025 |
| Demografía | Natalidad, hijos por mujer, 65+, dependencia, migración neta | 12 | 2024-2025 |
| Vivienda | Sobrecarga del coste (Eurostat) | 6 UE | 2025 |
| Vivienda | Inicios, permisos y terminadas (Census) | solo EE. UU. | 2026-09 |

Fuentes: Banco Mundial (OMS GHED, UNODC, WGI, ONU) y Eurostat. Hitos por país: vacíos salvo 2 de vivienda en ES y US (`estabilidad-manual.json`).

## 2. Métricas nuevas en las filas (todas [P], con año y fuente en cada fila)
**12 países (Banco Mundial, datos de OMS/UNESCO/OIT/UN IGME):**
- Sanidad: gasto sanitario público % PIB y % del gasto del Estado; pago directo del paciente; probabilidad de morir a los 30-70 por enfermedad crónica; mortalidad menores de 5; mortalidad materna; vacunación de sarampión.
- Educación: educación % del gasto público; I+D % PIB. Trabajo: paro juvenil (OIT, modelado). Infraestructuras: formación bruta de capital fijo % PIB.
- **Seguridad (para ampliar con accidentes y muertes):** muertes por tráfico (OMS 2019) y por suicidio (OMS 2021), por 100.000 hab.

**6 países UE (Eurostat):** abandono escolar 18-24; gasto público en sanidad, orden público y seguridad, educación y vejez, todos COFOG, % PIB 2024.

### Cifras destacadas (para contrastar con la fuente)
- Pago directo del paciente: India 43,9 %, China 32,2 %, Rusia 28,4 %; Francia 9,2 %, Alemania 10,7 %. (Banco Mundial/OMS GHED 2023-24.)
- Gasto sanitario público % PIB 2023: Alemania 9,3, Reino Unido 9,0, EE. UU. 9,0; India 1,3.
- Muertes por tráfico 2019 por 100.000: China 17,4, India 15,6, EE. UU. 12,7, Rusia 12,0; Reino Unido 3,2, Alemania 3,8, España 3,9.
- Abandono escolar 2025: Alemania 13,1 %, España 12,8 %; Polonia 4,0 %.
- Gasto público en vejez 2024 (% PIB): Italia 13,9, Francia 13,4; Países Bajos 6,1. España 10,4.
- Paro juvenil 2025 (modelado OIT): España 24,8 %, Italia 20,6 %; Japón 3,9 %.

## 3. Sin dato primario o no comparable
- Sin dato en la serie del Banco Mundial: educación sobre gasto público (Japón, Rusia) e I+D (India) → filas con valor `null` [VERIFICAR].
- **No cargado (hace falta fuente nacional/OCDE, no accesible por API abierta aquí):** PISA (OCDE), tasa de sustitución y duración del subsidio de desempleo (OCDE), precio de la electricidad doméstica, LPI, vivienda fuera de la UE (precio/ingresos, alquiler), pensiones fuera de la UE, hitos y reformas por país, delincuencia distinta de homicidios.
- Comparabilidad: muertes por tráfico y suicidio son estimaciones OMS (2019 y 2021), no las cifras oficiales de cada país (p. ej. DGT, NHTSA). Paro juvenil OIT es modelado: difiere de Eurostat. COFOG solo UE. Años distintos entre países.
- Los WGI y la corrupción son percepciones.

## 4. Sesgos y lecturas
- Mucha "cobertura" no es calidad: gasto alto (EE. UU.) con resultados medios; gasto bajo (España, Italia) con vida larga. Las cifras no explican causas.
- China y Rusia: cifras de organismos internacionales sobre datos oficiales, no verificables aquí.
- Alcista/bajista: no aplica.

## Lecciones
- Eurostat API: filtrar todas las dimensiones (p. ej. `wstatus=POP`) o el cálculo de índices por país/año falla.
- Banco Mundial API con `mrv=3` da el último año disponible por país en una sola llamada.
