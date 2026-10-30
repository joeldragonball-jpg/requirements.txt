# C59 · Indicadores económicos y sociales por país (IPC, paro, pobreza…)

Coste estimado: ~3 % de la cuota semanal · Cuándo: sin día fijo, en sesión nueva; absorbe lo que falta de C31

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta ni predicción de resultados, cada dato con fuente y fecha, etiquetas [P] (primaria leída) / [S] (prensa o agregador) / [VERIFICAR] / [ESPECULACIÓN], contraste alcista/bajista y sesgos de la fuente, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes; para informes usa `python scripts/buscar_informes.py "<consulta>" -n 6`. Webs que dan 403 a curl: navegador integrado, sin saltar controles anti-bots. Todo lo nuevo en el móvil va en desplegables, cerrado por defecto. Cifras con símbolo delante y «mil M» (research/GUIA-ESTILO-CIFRAS.md). Al terminar: fila en research/COLA.md con coste real, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».

Tarea C59: panel de indicadores para 12 países: UE → España, Alemania, Francia, Italia, Países Bajos, Polonia; potencias → EE. UU., China, Japón, India, Reino Unido, Rusia. Ids de `explorador/elecciones.json` donde ya existan (no dupliques datos de elecciones: enlaza).
1. Indicadores: IPC (interanual y último mes), paro, crecimiento del PIB, deuda pública y déficit (% del PIB), tasa de pobreza (UE: AROPE de Eurostat; EE. UU.: Census; China, India, Japón, Rusia, Reino Unido: Banco Mundial/OCDE/oficina nacional, diciendo la definición), desigualdad (Gini), salario mínimo si existe. Cada uno con fecha del dato, fuente, nivel y próxima publicación.
2. Reutiliza `leer_inflacion()` de `scripts/actualizar_paneles.py` (C31: EE. UU., UK, Canadá, Brasil al día; zona euro y España desfasadas en dic-2025: prueba otra consulta o Eurostat directo; PCE, Japón y China dependen de FRED, que da timeout desde este PC: usa el workflow o una fuente alternativa). Añade una función `leer_indicadores()` que escriba en `explorador/paneles.json` (clave «indicadores»); si una fuente falla, conserva el dato anterior y avisa.
3. Apis abiertas sin clave: Eurostat, Banco Mundial (api.worldbank.org), OCDE, FMI DataMapper, ONS, StatCan, IBGE, BLS. Lo que no tenga API: dato manual con fuente y fecha en `explorador/indicadores-manual.json`, marcado [S] o [VERIFICAR].
4. Avisa siempre de definiciones distintas (pobreza relativa vs. absoluta, IPC vs. IPCA vs. PCE), periodos mezclados y revisiones; nada de ordenar países por «mejor» o «peor».
5. Calendario: fechas de publicación verificadas en la fuente oficial a `eventos/calendario.toml` (sin duplicar).
Informe en informes/research/AAAA-MM-DD-C59-indicadores.md (máx. 1 página; 3-5 cifras contrastadas con la nota oficial).
```
