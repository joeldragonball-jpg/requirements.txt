# C32 · Móvil: pantalla principal y auditoría de paneles (4-nov-2026)

cubre: C32 · Probado en el navegador integrado a 375 px (`docs/movil/`, servidor local), sin llamar a ninguna API.

## 1. Pantalla principal («Hoy»): ya cumple lo pedido
- HECHO (comprobado en `docs/movil/index.html`, función `vHoy`): arriba hay una fila compacta con XRP, XLM, BTC, Brent, tipo de la Fed, del BCE, IPC de España, de la zona euro y de EE. UU., cada uno con flecha y fecha (`a dd/mm` = fecha del dato del tipo oficial).
- Debajo, el desglose va en desplegables cerrados (`vMercado`): Ormuz, liquidez, inflación por país, defensa, valoración, hitos de petróleo. No hubo que reescribir nada de la pantalla.

## 2. Prueba a 375 px
- Sin scroll horizontal en Hoy, Seguimiento, Agenda y Mercado (`scrollWidth` = 375). La barra de filtros del Seguimiento sí se desliza de lado, a propósito (`overflow-x: auto`).
- Consola: solo 4 avisos 404, todos de las comprobaciones «¿ya está el R00 de hoy en el repo?», que dan 404 mientras el informe de hoy no existe. No son un fallo.

## 3. Auditoría de los paneles (lista corta, por utilidad)
| # | Hallazgo | Estado |
|---|---|---|
| 1 | **El tipo del BCE sale «a 16/09»** (49 días) aunque el dato es vigente: la serie del BCE solo trae los días de cambio y el script ponía esa fecha como «fecha del dato». Parece viejo y no lo es | **Corregido** en `scripts/actualizar_paneles.py` (`dato_de` = día de lectura; el cambio sigue en `ultimo_cambio`). Se verá tras la próxima ejecución de `paneles.yml` |
| 2 | Ormuz: último dato del 25-oct (10 días) | Es el retraso de PortWatch (FMI), no un fallo; ya lleva la fecha visible. Sin acción |
| 3 | Inflación y liquidez: datos de sep-2026 | Normal (un mes de retraso de publicación); llevan el mes. Sin acción |
| 4 | Bonos: Francia del 22-oct (13 días); China e Italia están en la terminal pero no en el móvil | Abierto: decidir si el móvil debe llevar los 8 de la terminal |
| 5 | Brent: terminal 106,53 $ (3-nov) y móvil 103,92 $ (4-nov) son de días distintos | Ver `research/contradicciones-paneles.md`; no es contradicción |
| 6 | Brent spot EIA 123,1 $ (27-oct) frente a futuro ≈ 104 $ | Medidas distintas (spot fechado frente a futuro); solo hay que rotularlo bien al mostrarlo en el móvil |

## 4. Lo que no se ha tocado
- `index.html` no ha cambiado, así que no se sube la versión de caché de `sw.js`.
- Ningún panel parece sin uso; para decidirlo haría falta medir toques reales, y hoy no se miden [VERIFICAR].
