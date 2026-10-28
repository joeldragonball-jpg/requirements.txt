# C41C · Fusión del diseño de la Órbita (C41A Claude + C41B Gemini)

Coste estimado: ~2 % de la cuota semanal · Sin fecha · Requiere C41A y C41B hechas

## Pega esto en una sesión nueva (Opus o Sonnet, esfuerzo alto)

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, fuente y fecha en cada dato, etiquetas [P]/[S]/[VERIFICAR]/[ESPECULACIÓN], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no commit ni push sin mi «sube».

Tarea C41C: lee SOLO informes/research/*-C41A-diseno-orbita.md e informes/gemini/*-C41B-diseno.md (y sus maquetas si las necesitas). Compara las dos propuestas sin favorecer a ninguna:
1. Dónde coinciden (señal fuerte), dónde discrepan y quién tiene mejor argumento (con la referencia que lo apoya). Comprueba 3 referencias de Gemini abriéndolas; la etiqueta P de Gemini no es fiable hasta que tú la confirmes.
2. Lista fusionada de máx. 10 cambios ordenados por utilidad/esfuerzo, con orden de ejecución y dependencias (qué va antes de C30, C35 y C39; la estructura de datos o el índice primero, lo visual después).
3. Propón filas nuevas en research/COLA.md (una por cambio o grupo, con prompt corto en research/prompts/) y deja la decisión final a Joel: qué se hace, qué no y qué se pospone. Sin tocar mapa.html ni datos reales en esta tarea.
4. Salida: informes/research/AAAA-MM-DD-C41C-fusion-diseno.md (máx. 1,5 páginas), filas en COLA, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».
```
