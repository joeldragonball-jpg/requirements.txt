# Auditoría visual Órbita y móvil · 7-nov-2026

Método: navegador integrado; cada pestaña medida con JS (desborde horizontal, texto <13 px, contraste) con la Órbita a 375, 768, 1024 y 1280 px y el móvil a 375 y 768. Tema oscuro en todo momento.

## Bug del solape (Resumen, «Mis activos», tablet)
- **Causa:** `.cols2` ponía XRP y XLM en dos columnas de ~351 px (mínimo `clamp(300px,34vw,520px)`), pero cada tabla de 4 columnas necesita 704 y 742 px (celdas «Valor» con `white-space:nowrap`). La tabla se salía de su celda y se pintaba encima de la columna vecina.
- **Arreglo** (`explorador/vistas.html`, regla `.mis`): dos columnas solo si caben 600 px cada una (apila en tablet), celdas con `overflow-wrap`, y `overflow-x:auto` como red de seguridad. Comprobado: 375, 768 y 1024 apilado; 1280 en dos columnas; desborde 0 en todos.

## Hallazgos

| Pestaña | Tamaño | Problema | Corregido |
|---|---|---|---|
| Resumen | 768 | Solape XRP/XLM | Sí |
| Resumen, Noticias | 375 | Tablas sin contenedor ensanchan la página (+93/+102 px de scroll horizontal) | Sí (tablas con scroll interno ≤820 px, salvo la matriz) |
| Voces | 375 | `select` de hilos más ancho que la pantalla (+25 px) | Sí (`max-width:100%`) |
| Noticias | 375 | Etiqueta de verificación larga se sale (+29 px) | Sí (`overflow-wrap`) |
| Línea de tiempo | 768 | Nombres de carril cortados con «…» | Sí (2 líneas) |
| Paneles | todos | `small` de valores a 12,5 px | Sí (13 px) |
| Móvil (todas) | 375/768 | ~30 textos a 12 px (nav, etiquetas, niveles) | Sí (13 px); caché `cerebro-movil-59` |
| Contraste | todos | Ningún texto <4,5:1 en oscuro en la Órbita (el aviso en «Paneles» es falso positivo de las barras) | — |
| Móvil | todos | Sin desborde horizontal ni en las 5 pestañas | — |

## Pendientes (no tocados)
1. **Móvil sigue el tema del sistema** (`prefers-color-scheme: light` activa el claro, líneas 188 y 655 de `docs/movil/index.html`). Joel prefiere oscuro por defecto: decidir si se fuerza `oscuro` salvo elección manual. En claro, `.sube` da 4,1:1.
2. Matriz país × tema a 375: cabeceras muy estrechas (24 px) con texto vertical/cortado; valorar versión en lista.
3. Capas/España/Paneles a 768: algunas filas KPI y tablas (hasta 1054 px) solo se ven con scroll horizontal; sin indicación visual de que hay más.
4. Filtros de la barra: «País» en Resumen no filtra casi nada del bloque «Mis activos»; revisar si debe ocultarse ahí.
5. Consola: 404 de recursos al servir `docs/` (rutas `/movil/` absolutas del service worker); no ocurre desde la raíz de `docs/movil`. Verificar en GitHub Pages.
