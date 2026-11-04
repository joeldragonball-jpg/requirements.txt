# C129 · Auditoría visual y de explicaciones del tablero (para Opus)

Modelo recomendado: Opus (revisión de diseño fuerte). Estimación ~6-8 % semanal. No toques datos ni fuentes: solo presentación y textos.

## Contexto
Joel (4-nov-2026) dice que sigue sin ver mejoras suficientes en el tablero del PC (`explorador/vistas.html`, visto en la pestaña «🧠 Cerebro» de `app.py` en localhost:8793). Quejas concretas:
1. **Tablas liosas y pequeñas**: filas con 3 líneas por celda, letra de 8-9 px, tablas de 6 columnas por 10-13 filas (Países, Presupuestos, Capas, Voces).
2. **Presupuestos demasiado minimalistas o «raros»**: no encajan con el resto del ambiente visual (las pestañas de Cifras clave y España ya usan tarjetas con color).
3. **Las explicaciones**: textos largos de método o de sesgo antes del dato; deben ser cortos, con el dato primero y la explicación plegable.
4. Quiere una mejora continua: cada vez que toques una pantalla, deja anotadas 2-3 mejoras más para la siguiente pasada.

## Qué hacer
1. Abre el tablero con Claude in Chrome (el navegador integrado no abre localhost). Las pestañas están en `Resumen, Capas, Línea de tiempo, Calendario, Matriz, Noticias, Voces, Países, España, Paneles de datos`. El contenido está en iframes anidados; usa `javascript_tool` si hace falta.
2. Recorre TODAS las pestañas y las 4 subpestañas de España (Economía y deuda, Presupuesto y gasto, Servicios y sociedad, Seguridad y salud). Para cada una, anota en una tabla: qué se ve mal, tamaño de letra real (mide con `getComputedStyle`), y una solución concreta.
3. Presta atención especial a **Presupuesto y gasto** (tablas de presupuesto, ministerios, altos cargos, programas) y a **Capas**.
4. Prioriza por impacto: «se ve ya en la primera pantalla» antes que «detalle interior».
5. Aplica los arreglos más rentables en `explorador/vistas.html` (sintaxis con `node --check`, nunca saltes la comprobación en Chrome) siguiendo los patrones ya existentes: `kpi()/kpis()`, `bloque()`, tarjetas `.cc-b`, desplegables `<details>`. Mínimo de letra: 13 px en cuerpo, 12 px en etiquetas.
6. Las explicaciones: en cada bloque, deja 1-2 líneas visibles y el resto en un `<details>` «Cómo se lee / sesgos / fuente».
7. Guarda el informe en `informes/research/AAAA-MM-DD-C129-auditoria-visual.md` con: problemas por pestaña, qué arreglaste, qué queda para la siguiente pasada (2-3 mejoras por pestaña).

## Reglas
- Español. Sin recomendaciones de compra/venta. No toques `cerebro/`, `privado/` ni claves.
- No añadas dependencias ni librerías externas. La vista debe seguir funcionando con `vistas.html` embebido en Streamlit.
- Tras cada bloque de cambios: `node --check` del JS extraído y comprobación visual en Chrome. No hagas commit ni push; enseña `git status`.
