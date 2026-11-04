# C133 · Países: datos más recientes, comparación histórica y «durante el mandato» (tamaño L)

Pedido de Joel (5-nov-2026), tras ver la vista nueva de Países:
1. **Datos más recientes posibles.** Hay indicadores de 2020-2024 (pobreza, Gini, paro juvenil, etc.). Busca 2025 y 2026 en Eurostat, Banco Mundial, FMI y OCDE. Cuando ya estén todos lo más actualizados posible, muestra todos los años aunque sean de 2-3 años distintos, con el año bien visible.
2. **Comparación histórica** en los indicadores donde tenga sentido (IPC, paro, paro juvenil, pobreza, pobreza infantil, deuda, déficit, PIB, Gini): valor frente a hace 2 años, hace 5 años y máximo/mínimo histórico de la serie, con el año del máximo.
3. **«Durante el mandato»**: para cada país, cambio del indicador entre el inicio del gobierno actual (fecha en `explorador/paises.json`, `ultima_eleccion`/toma de posesión) y el último dato. Redacción tipo: «Con X en el cargo desde AAAA-MM, el IPC pasó de a b (−c p.p.)». Señala los hitos grandes (máximos o mínimos de la serie).

## Reglas de rigor (obligatorias)
- Es un HECHO descriptivo (valor al inicio y valor ahora, con fuente y fecha). Atribuir la causa al gobernante es [ESPECULACIÓN]: pon siempre la advertencia «coincide con el mandato; no prueba que lo causara» y, cuando proceda, factores externos (guerra, energía, pandemia, BCE/Fed, ciclo).
- Sin juicios de valor ni recomendaciones. Contrasta caso a favor y en contra del gobierno cuando sea un hito grande.
- Sin series históricas fiables para un país/indicador → «sin serie»; no inventes.

## Dónde
- Datos: `scripts/indicadores.py` (Eurostat/Banco Mundial) y `explorador/indicadores-manual.json`; hoy solo guardan el último valor y el anterior. Amplía a una serie anual/mensual breve (últimos 15 años) en `explorador/paneles.json` o un JSON nuevo, sin romper el formato actual.
- Vista: `explorador/vistas.html`, función `pPaises` (vista por país: cifras grandes + lista; tablas plegadas).
- Colores: número en blanco; verde/rojo solo si hay subida o bajada frente al dato anterior y el sentido es claro; blanco si no cambia (ya aplicado el 5-nov).
Primero un plan corto a Joel (qué indicadores y qué fecha de inicio de cada gobierno, con fuente); implementa con su OK. Sin API de Anthropic. Sin commit ni push.
