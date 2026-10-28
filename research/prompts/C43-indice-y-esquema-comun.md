# C43 · Índice de datos y esquema común (sale de C41C)

Coste estimado: ~3 % · Hacer ANTES de C35 y C39 si es posible.

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, fuente y fecha en cada dato, nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no commit ni push sin mi «sube».

Tarea C43: (1) crea scripts/indice_datos.py que genere explorador/indice/ (por país, por tema, cambios a 7 y 30 días) y explorador/indice/INDICE.md («dato → archivo → campo»), solo lectura de los JSON. (2) Amplía scripts/indice_investigacion.py para cubrir TODOS los informes por tema y país. (3) Añade campos opcionales nuevos sin renombrar los viejos: pais_id (ISO2), nivel (P/S/V), fecha, url, revisar, caduca, sesgo, perspectivas; empieza por regulacion.json y datos.json; revisar_explorador.py debe seguir en 0 avisos. Detalle: informes/research/2026-10-28-C41C-fusion-diseno.md §2 cambios 1-2.
```
