# C64 (parcial) · Refresco de países fuera de la UE: EE. UU. (30-oct-2026)

Continúa `2026-10-30-C63-refresco-paises.md`. Etiquetas: [P] primaria leída · [S] prensa · [VERIFICAR]. Sin recomendaciones.

## Antes → ahora (EE. UU., fuentes oficiales leídas con el navegador integrado)
| Cifra | Antes | Ahora | Fuente |
|---|---|---|---|
| IPC | 2,9 % (media anual de 2024, Banco Mundial) | **3,7 % interanual, sep-2026** (agosto 3,4 %); subyacente 2,6 % [P] | BLS, 14-oct-2026 |
| Pobreza oficial | sin dato | **10,2 % en 2025** (−0,5 puntos); medida suplementaria SPM 13,1 %, sin cambio significativo [P] | Census, 15-sep-2026 (CB26-151) |

- El IPC subió por la gasolina (+9,1 % en septiembre, más de la mitad del aumento mensual). Es la serie del IPC-U; el PCE de septiembre fue 3,6 % (BEA, 29-oct), otra medida.
- Pobreza: la encuesta (CPS ASEC) tiene una tasa de respuesta del 61,3 %, por debajo de antes de la pandemia; el Census avisa de posible sesgo [P]. La tasa oficial no incluye impuestos ni créditos fiscales.
- Renta mediana de los hogares: $87.460 en 2025, máximo histórico en términos reales desde 1967 [P, Census].

## Dato nuevo que no cabe en el Panel (queda en el informe)
- **Obras de vivienda, septiembre de 2026** [P, Census, 20-oct]: inicios 1.221.000 anualizados, −5,2 % mensual y −7,4 % interanual (margen de error ±11,8 %: no es significativo); permisos 1.400.000 (−3,0 % interanual); viviendas terminadas 1.192.000 (−14,0 % interanual). El Panel no tiene campo de obras todavía.

## Qué se tocó
`explorador/indicadores-manual.json` (US: `ipc` y `pobreza` pasan a nivel P) y `explorador/paneles.json` (bloque «indicadores», solo esas dos cifras de EE. UU.).

## Sigue sin hacer de C64
- Salario mínimo federal de EE. UU. (7,25 $ desde 2009-07, nivel V): la página del Departamento de Trabajo que probé devuelve «no encontrada»; **[VERIFICAR]**.
- Gini de EE. UU., China, Japón, India, Reino Unido y Rusia; pobreza de China, Japón, India y Reino Unido (datos de 2011-2022 del Banco Mundial; las oficinas oficiales no se han mirado).
- Gasto sanitario de EE. UU. (CMS), housing de China/India/Rusia (NBS, MoSPI, Rosstat).
- Noticias de 30-60 días de sanidad, educación, vivienda y pensiones: **sin hacer**. Las búsquedas web de hoy no devuelven prensa fechada de forma fiable.
- Obras de vivienda UE (`sts_cobp_a`) y homicidios (`crim_hom_soff`): filtros pendientes.
- Nota de auditoría: el script marca como «VIEJO» datos de 2024 que son el último año publicado (p. ej. sanidad de España); no hay nada más nuevo en la fuente.

## Seguridad
Solo lecturas públicas; sin claves; sin workflows ni API de Anthropic.
