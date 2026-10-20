# Auditoría corta del 21-oct-2026 (radar v3/v4, calendario v2, mapamundi, comparador)

Solo comprobaciones automáticas con Python y Node, sin IA ni red. NO se probó la pantalla en el navegador (el servidor de Streamlit no se arrancó). Pedido: Joel, 20-oct.

## Radar (`explorador/regulacion.json`)
- HECHO: 112 celdas = 14 jurisdicciones × 8 temas, sin duplicadas ni faltantes, sin jurisdicción o tema fuera de lista.
- HECHO: fuente [P] 44, [S] 34, [VERIFICAR] 34; coincide con lo anotado (78 con dato). Todas las celdas con etapa tienen fuente y las [P] llevan informes.
- HECHO: ninguna celda tiene `revisado` vacío ni fechas futuras. 6+ fechas están en formato AAAA-MM (sin día): válido, pero el aviso de «30 días sin revisar» depende de `revisado`, que es AAAA-MM-DD en todas.
- Nota: `informes` de cada celda son etiquetas de texto («R25», «Radar v4 research (20-oct)»), no rutas; no se pueden comprobar con el sistema de archivos.

## Calendario (`eventos/calendario.toml`)
- HECHO: 66 eventos (13 alto, 29 medio, 24 bajo), 24 con fecha aproximada; sin duplicados, sin `hasta` anterior a `fecha`, todos con fuente.
- Aviso 1: la cabecera del archivo dice «impacto: alto | medio», pero hay 24 eventos «bajo»; `eventos/avisos.py:38` los pinta como 🟡 igual que «medio». Pendiente decidir si «bajo» debe avisar o no.
- Aviso 2: las fechas son texto, no fechas TOML; funciona, pero cualquier comparación debe convertirlas.
- Fines de semana (escrow 1-nov, OPEP+ 1-nov, HackMeridian 25-oct, etc.): plausibles, no son errores.

## Mapamundi y comparador
- HECHO: el JavaScript de `mapa.html` y de `mundo.html` compila sin errores de sintaxis (`node --check`). `datos.json` y `regulacion.json` cargan.
- NO COMPROBADO: apariencia, filtros y comparador de dos países en pantalla; `mundo.py` no se puede importar fuera de Streamlit en este entorno.

## Script de calidad
- `scripts/revisar_explorador.py`: 1 aviso (custodia de XRP en firmas cripto, [VERIFICAR] abierto).
