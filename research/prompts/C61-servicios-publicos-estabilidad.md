# C61 · Servicios públicos y estabilidad social por país (sanidad, vivienda, infraestructuras, empleo, seguridad)

Coste estimado: ~3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva; después de C58 y C59, antes de C60

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta ni predicción de resultados, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes; para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Webs que dan 403 a curl: navegador integrado, sin saltar controles anti-bots. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Cifras con símbolo delante y «mil M» (research/GUIA-ESTILO-CIFRAS.md). Al terminar: fila en research/COLA.md con coste real, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea C61: para los 12 países de C58 (UE: España, Alemania, Francia, Italia, Países Bajos, Polonia; EE. UU., China, Japón, India, Reino Unido, Rusia), reunir las cifras PUBLICADAS que sirven para valorar la estabilidad de una sociedad, en un solo sitio y comparables. REGLA CLAVE (Joel, 30-oct): NO inventes índices propios ni puntuaciones; coge las cifras que ya publican organismos (OCDE, Eurostat, Banco Mundial, OMS, ONU/PNUD, FMI, UNODC, oficinas nacionales) con su año, definición y fuente, y deja que cada país se lea con ellas. Si una cifra no es comparable (definiciones distintas), dilo en la celda.
Dimensiones (usa estas; si falta un país o dato, «sin dato», no lo rellenes):
1. Sanidad: sistema (público tipo Beveridge, seguro social tipo Bismarck, mixto/privado, cobertura), gasto sanitario % PIB y por habitante (OMS GHED / OCDE Health at a Glance), esperanza de vida y mortalidad infantil, médicos y camas por 1.000 hab., gasto público en I+D de salud si existe, y hitos: reformas, grandes inversiones públicas, aprobaciones o avances (fecha y fuente).
2. Vivienda: precio de la vivienda sobre ingresos, alquiler sobre ingresos, sobrecarga del coste de la vivienda (Eurostat), viviendas iniciadas o terminadas por 1.000 hab. (Eurostat, Census, oficinas nacionales), vivienda pública o protegida, y política en marcha (plan, fecha, cifra).
3. Infraestructuras y energía: inversión pública (formación bruta de capital público % PIB), logística (LPI del Banco Mundial), banda ancha, dependencia energética y precio de la electricidad doméstica, grandes obras (fecha y presupuesto).
4. Trabajo y protección: paro total y juvenil, empleo informal, subsidio de desempleo (duración y tasa de sustitución, OCDE), pensiones (gasto % PIB y edad de jubilación), salario mínimo.
5. Educación: gasto % PIB, PISA y abandono escolar.
6. Seguridad y gobernanza: homicidios por 100.000 hab. (UNODC), indicadores de gobernanza del Banco Mundial (estabilidad política, imperio de la ley, control de la corrupción), Índice de Percepción de la Corrupción de Transparencia Internacional [S, es percepción], protestas o huelgas grandes si hay fuente fiable [S].
7. Demografía y migración: natalidad, edad media, migración neta, ratio de dependencia.
Salida: `explorador/estabilidad.json` (lista «paises»; por país y dimensión una lista de «cifras» {nombre, valor, unidad, anio, fuente, nivel P/S/VERIFICAR, nota de comparabilidad} y «hitos» {fecha, texto, fuente, nivel}) y, por país, una «lectura» de 3-4 líneas escrita por ti: puntos fuertes y vulnerabilidades según esas cifras, con caso a favor y en contra y marcada como [OPINIÓN]/[ESPECULACIÓN] cuando sea juicio; nunca «mejor/peor país» ni recomendaciones de inversión.
No dupliques lo de C59 (IPC, PIB, deuda, pobreza AROPE, Gini): enlaza con el mismo id de país.
Informe en informes/research/AAAA-MM-DD-C61-estabilidad.md (máx. 1 página: qué dimensiones se cubrieron, huecos y 3-5 cifras contrastadas con la fuente oficial). Si el volumen no cabe en una sesión, para al 70 % del contexto, deja anotado qué países y dimensiones faltan en la fila de COLA y dame el relevo.
```
