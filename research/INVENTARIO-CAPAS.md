# Inventario de capas, datos y cadencias (8-nov-2026)

Autogenerado a partir de `docs/movil/data.json` (`frescura_json`) el 8-nov-2026. **No sustituye** a `research/PLAN-ACTUALIZACION-DATOS.md` (cadencias oficiales de 3-nov) ni a `research/MAPA-DE-FUENTES.md`: este archivo los cruza con la antigüedad real de cada dato. Las cadencias de la tabla son [propuesta], no decisión; la decide C185 (Opus).

## 1. Capas y su antigüedad hoy

| Capa | Dato | Último dato | Antigüedad | Cadencia [propuesta] | Estado |
|---|---|---|---|---|---|
| Cripto/regulación | CBDC y blockchains | 2026-10-29 | 10 d | trimestral [propuesta] | al día |
| Cripto/regulación | RWA por cadena | 2026-10-29 | 10 d | semanal [propuesta] | al día |
| España | España | 2026-11-04 | 4 d | mensual, según publicación INE [propuesta] | al día |
| España | Presupuesto de España | 2026-10-30 | 9 d | anual (PGE) y trimestral (IGAE) [propuesta] | al día |
| Macro | Historia de indicadores | 2026-11-07 | 1 d | mensual [propuesta] | al día |
| Macro | Indicadores (manual) | 2026-11-07 | 1 d | mensual, tras cada publicación [propuesta] | al día |
| Macro | Liquidez (manual) | 2026-11-07 | 1 d | semanal [propuesta] | al día |
| Mercado | Paneles de mercado | 2026-11-08 | 0 d | diaria [propuesta] | al día |
| Mercado | Precios vivos | 2026-11-08 | 0 d | diaria [propuesta] | al día |
| Países/política | Elecciones | 2026-10-30 | 9 d | calendario oficial [propuesta] | al día |
| Países/política | Países | 2026-10-30 | 9 d | tras cada elección o remodelación [propuesta] | al día |
| Regulación | Mandatos | 2026-11-05 | 3 d | tras cada reunión [propuesta] | al día |
| Riesgo país | Calificaciones | 2026-10-22 | 17 d | tras cada revisión (S&P, Moody's, Fitch) [propuesta] | al día |
| Riesgo país | Deuda (FMI) | 2026-10-21 | 18 d | semestral (WEO abril/octubre) [propuesta] | al día |
| Riesgo país | Estabilidad | 2026-10-30 | 9 d | trimestral [propuesta] | al día |
| Riesgo país | Reservas | 2026-10-22 | 17 d | mensual (FMI COFER trimestral) [propuesta] | al día |
| Valoración | Valoración sectorial | 2026-11-07 | 1 d | mensual [propuesta] | al día |

## 2. Qué mide cada capa (resumen de lo que hay)
- **Mercado (móvil, `control`):** 6 grupos, 45 filas (más las cripto); 43 diarias y 2 mensuales; fuentes casi todas Yahoo Finance (energía, alimentos, metales, bolsas, ETFs) y BCE para divisas. Riesgo: una sola fuente para casi todo, sin segunda comprobación [VERIFICAR].
- **Macro y liquidez:** indicadores y liquidez en ficheros `*-manual.json`: dependen de que alguien los actualice.
- **Riesgo país:** calificaciones, reservas y deuda FMI llevan 17-18 días sin actualizar; son datos de cadencia lenta, pero conviene fijar disparador (revisión de agencia, WEO).
- **Países y política:** fichas con nivel S/P por país; los pendientes de C179 (Etiopía, Indonesia, Egipto) están en `research/tareas.csv`.

## 3. Preguntas que debe responder la valoración (C185, Opus)
1. ¿Qué capa ayuda de verdad a decidir a largo plazo y cuál es ruido?
2. ¿Qué datos necesitan segunda fuente (hoy una sola)?
3. ¿Qué research debe ser continuo, con qué disparador (calendario oficial, no reloj) y con qué coste de cuota?
4. ¿Qué falta por capa (huecos) y qué sobra?
5. ¿Qué datos manuales conviene automatizar primero?

Sin recomendaciones de compra o venta: solo utilidad de la información.
