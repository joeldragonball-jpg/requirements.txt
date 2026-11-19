# Cableado de rendimientos.json y de `_bloques` (19-nov-2026)

Tarea de código, sin datos nuevos, sin API, sin commit.

## Cambios
1. `scripts/revisar_explorador.py`: `rendimientos` en la lista de JSON de comprobación mínima (fecha, fuente, nivel) y un bloque nuevo que valida cada fila de `rendimientos.json` con `celda_cadena` (formato `{t,f,u,d,n}`), ids únicos y `modalidad`/`activo`/`riesgo` presentes. Resultado: **0 avisos** en 13 capas y 336 movimientos.
2. `explorador.py`: carga `rendimientos` (lista de capas de datos) y `indicadores_bloques` (= clave `_bloques` de `indicadores-manual.json`).
3. `explorador/vistas.html`:
   - Cadenas › caja «Rendimientos: staking, préstamos y AMM por plataforma» (id `cad-rendimientos`, tras «Qué vigilar»; entra sola en el «Ir a:»). Una tabla con botones por modalidad (Todos 14, Staking 4, Préstamo 5, AMM 3, Colateral 1, Fiscalidad 1), en vez de listas largas. Cada fila: modalidad, activo, cifra leída, fuente/fecha/nivel, riesgo.
   - `nBloques()` dentro de Paneles › «Comparar países» (sin pestaña ni capa nueva): 5 pestañas compactas: Zona euro y UE-27 (6 indicadores), Potencias (FMI, 7 países), BRICS (FMI, 10), Agregados FMI (5 grupos) y Reservas y pagos (COFER USD/RMB, Swift RMB). Cada celda con tooltip fecha·fuente·nivel; proyecciones FMI rotuladas «2026 = proyección»; tablas con scroll horizontal si faltan píxeles.
4. Móvil: `scripts/construir_movil.py` genera `rend` (14 filas) y `bloq` (27 filas) en `data.json`; `docs/movil/index.html` pinta dos tarjetas («Rendimientos: staking, préstamos y AMM» y «Países: zona euro, UE-27, potencias y BRICS»).
5. `python scripts/construir_orbita.py` regenerado (4837 KB). Los dos JSON de datos no se tocaron.

## Comprobación (Chrome headless sobre `docs/orbita/index.html`; el panel del navegador y Chrome-extension no alcanzaban localhost)
- Sin errores de JS en la página.
- Cadenas: `#cad-rendimientos` existe, 15 filas (cabecera + 14), ancho 732 px, fondo oscuro rgb(14,20,32); pestaña AMM = 4 filas, 1 botón activo; el «Ir a:» incluye «Rendimientos».
- Bloques: zona euro IPC 4 % / paro 6,5 % / deuda 87,3 %; BCE 2,5 %; China 4,5 % PIB, 1 % IPC, 104,4 % deuda; mundo PIB 3,1 %; COFER USD 56,7 %, RMB 2,11 %, Swift RMB 2,18 %.
- Un fallo propio (potencias y BRICS salían «—») corregido y reverificado.
- Móvil: sintaxis JS de `index.html` correcta; `data.json` con rend=14 y bloq=27 (el aviso del CSV «eur» es anterior y se conserva el dato previo).
- No revisado a mano a ≤1180 px en pantalla (usa las mismas clases `cad-sel`/`scrollX` ya responsivas) [VERIFICAR] a ojo.
