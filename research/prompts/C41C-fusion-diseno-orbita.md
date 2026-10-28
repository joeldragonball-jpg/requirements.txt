# C41C · Fusión del diseño de la Órbita (C41A Claude + C41B Gemini)

Coste estimado: ~4-5 % de la cuota semanal (fusión ~2 % + prototipo ~2-3 %) · Sin fecha · Requiere C41A y C41B hechas

## Pega esto en una sesión nueva (Opus o Sonnet, esfuerzo alto)

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, fuente y fecha en cada dato, etiquetas [P]/[S]/[VERIFICAR]/[ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no commit ni push sin mi «sube».

Tarea C41C: lee SOLO informes/research/*-C41A-diseno-orbita.md e informes/gemini/*-C41B-diseno.md (y sus maquetas si las necesitas). Compara las dos propuestas sin favorecer a ninguna:
1. Dónde coinciden (señal fuerte), dónde discrepan y quién tiene mejor argumento (con la referencia que lo apoya). Comprueba 3 referencias de Gemini abriéndolas; la etiqueta P de Gemini no es fiable hasta que tú la confirmes.
2. Lista fusionada de máx. 10 cambios ordenados por utilidad/esfuerzo, con orden de ejecución y dependencias (qué va antes de C30, C35 y C39; la estructura de datos o el índice primero, lo visual después).
3. Propón filas nuevas en research/COLA.md (una por cambio o grupo, con prompt corto en research/prompts/) y deja la decisión final a Joel: qué se hace, qué no y qué se pospone. Sin tocar mapa.html ni datos reales en esta tarea.
3b. PROTOTIPO VISUAL para que yo vea cómo quedaría ANTES de decidir: crea explorador/prueba-diseno.html (archivo nuevo e independiente, sin enlazarlo desde el resto). Solo para ordenador. Lee en modo lectura los datos reales que ya existen (datos.json, regulacion.json, noticias) con fetch; no escribas ni cambies ningún dato ni mapa.html, mundo.html ni paneles.html. Muestra los cambios fusionados más visibles: matriz país × tema con chips y ficha al pasar el ratón, línea de tiempo con panel lateral, noticias con caducidad, iconos de certeza y selector de densidad (semáforo/datos). Si algo no se puede probar con datos reales, usa datos marcados «EJEMPLO». Comprueba que abre sin errores (scripts/revisar_explorador.py no debe cambiar su resultado) y dime cómo abrirlo.
4. Salida: informes/research/AAAA-MM-DD-C41C-fusion-diseno.md (máx. 1,5 páginas), filas en COLA, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».
```
