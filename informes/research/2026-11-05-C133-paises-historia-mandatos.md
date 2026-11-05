# C133 · Países: datos 2025-2026, historia y «durante el mandato» (5-nov-2026)

Modelo: Opus. Plan aprobado por Joel el 5-nov, con 4 cambios: «máximo de la serie AAAA-AAAA», nota del mandato previo en Putin, Trump y Xi, fechas de Jetten, Takaichi y Burnham con fuente oficial y aviso si el mandato dura menos de 2 años, y China y Rusia como [S]. Sin IA y sin subir.

## HECHOS: qué hay ahora

**Series (nuevo `scripts/indicadores_historia.py` → `explorador/indicadores-historia.json`, 100 series)**
- UE (ES, DE, FR, IT, NL, PL), de Eurostat [P], desde 2010:
  - IPC mensual, que une `prc_hicp_manr` (antigua) con `prc_hicp_minr` (ECOICOP 2).
  - Paro y paro juvenil mensuales (`une_rt_m`) y PIB trimestral (`namq_10_gdp`).
  - Deuda y déficit anuales (`gov_10dd_edpt1`).
  - Pobreza AROPE y **pobreza infantil (nuevo, menores de 18)** (`ilc_peps01n`, serie desde 2015) y Gini (`ilc_di12`, desde 2014).
  - Últimos datos: IPC a oct-2026, paro a sep-2026, PIB a 3T-2026, deuda, déficit, pobreza y Gini a 2025.
- Resto (US, CN, JP, IN, GB, RU), del Banco Mundial [P], anual:
  - IPC, paro, paro juvenil y PIB hasta 2025 (IPC de EE. UU., hasta 2024).
  - Pobreza (línea nacional, irregular) y Gini. EE. UU. y Japón no tienen pobreza con línea nacional en el Banco Mundial: «sin serie».
- Deuda y déficit fuera de la UE: del FMI WEO de octubre de 2026, leído en el navegador (el FMI da 403 a los scripts). Están en `explorador/indicadores-historia-fmi.json`. Solo se usan años cerrados; 2025 puede ser estimación.
- Comprobación: el IPCA de España sale 1,8 % en oct-2024 y 5,4 % en oct-2021, que coinciden con lo publicado por Eurostat. La deuda de Japón en 2025 (204,8 %) coincide con `deuda-fmi.json`.

**Fechas de mandato (`explorador/mandatos.json`)**

| País | Quién | Desde | Nivel | Fuente |
|---|---|---|---|---|
| NL | Rob Jetten | 2026-02-23 | P | rijksoverheid.nl (leído 5-nov-2026) |
| JP | Sanae Takaichi | 2025-10-21 | P | japan.kantei.go.jp, Previous Prime Ministers: 104.ª PM; 2.º gabinete desde 18-feb-2026 |
| GB | Andy Burnham | 2026-07-20 | P | gov.uk, página del Prime Minister |
| ES | Pedro Sánchez | 2018-06-02 | S | lamoncloa.gob.es (sin leer hoy) |
| DE | Friedrich Merz | 2025-05-06 | S | bundesregierung.de |
| FR | Emmanuel Macron | 2017-05-14 | S | elysee.fr |
| IT | Giorgia Meloni | 2022-10-22 | S | governo.it |
| PL | Donald Tusk | 2023-12-13 | S | gov.pl |
| US | Donald Trump | 2025-01-20 | S | whitehouse.gov · nota: mandato previo 2017-2021 |
| CN | Xi Jinping | 2013-03-14 | S | gov.cn · nota: secretario general del PCCh desde 15-nov-2012 |
| IN | Narendra Modi | 2014-05-26 | S | pmindia.gov.in |
| RU | Vladímir Putin | 2012-05-07 | S | kremlin.ru · nota: presidente 2000-2008, primer ministro 2008-2012; en el poder desde agosto de 1999 |

En los regímenes parlamentarios cuenta el jefe de Gobierno; en EE. UU., Francia, Rusia y China, el jefe de Estado. [S] = fecha de dominio público sin leer la fuente oficial en esta sesión.

**Vista (Países → ficha del país, `explorador/vistas.html`)**
- **Historia**: cada indicador con el último dato, hace 2 años y hace 5 años (mismo mes, trimestre o año), «Máximo de la serie» y «Mínimo de la serie» con su periodo y el rango visible («serie 2010-2026») y una mini-serie. La fuente y el nivel salen al pasar el ratón.
- **Durante el mandato**: una frase por indicador («con X en el cargo desde AAAA-MM, pasó de a (periodo) a b (periodo): ±c p. p.»). El valor inicial es el último periodo que termina antes de la toma de posesión; el final, el último periodo que empieza después. Si no lo hay: «aún no hay un periodo publicado…».
- Cada frase lleva **«Coincide con el mandato; no prueba que lo causara.»** y un **contraste**: la mediana del cambio de los otros países del grupo entre los mismos dos periodos. Si todos se movieron igual, apunta a un factor común.
- Hitos: ★ si el máximo o el mínimo de la serie caen dentro del mandato.
- Factores externos que se solapan con el mandato (pandemia, guerra de Ucrania y energía, subidas de tipos del BCE y la Fed, aranceles de EE. UU.), presentados como contexto y no como explicación.
- Avisos en pantalla:
  - «⚠ Mandato de menos de 2 años» (hoy: DE 18 meses, US 22, JP 13, NL 9, GB 4).
  - China y Rusia, [S], con una nota sobre la fiabilidad de sus estadísticas oficiales.
- Comprobado en el navegador (1600 px): los 12 países sin errores, letra mínima de 13 px y sin desplazamiento horizontal.

## OPINIÓN y límites

- Lo de cada país es descriptivo. Atribuir un cambio al gobernante es [ESPECULACIÓN]. La mediana del grupo ayuda a ver si el cambio fue común o propio, pero no lo demuestra.
- Las series de fuera de la UE son anuales: con mandatos cortos casi no hay dato «durante el mandato» (Japón y Reino Unido, ninguno todavía).
- [ESPECULACIÓN] Las cifras de China (PIB, paro) y de Rusia desde 2022 pueden estar suavizadas o incompletas: van como [S].
- El IPC de la UE une dos datasets de Eurostat (cambio a ECOICOP 2 en 2026); puede haber un pequeño salto metodológico en la unión.

## Pendiente (en `research/tareas.csv`, C135)

- Lanzar `indicadores_historia.py` junto con el bot de paneles (hoy es manual) y releer el FMI tras cada WEO.
- Mini-serie bajo las 4 cifras grandes de cada país, usando estas series.
- Leer en la web oficial las fechas de los 9 mandatos [S].
