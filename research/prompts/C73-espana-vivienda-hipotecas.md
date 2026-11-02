# C73 · España: vivienda, hipotecas y esfuerzo de acceso (explicado)

Enlaza con el panel de euríbor e hipotecas (C71) y con las fichas de España. Una sola página, sin capas nuevas: vincula los datos al panel de Tipos y a España.

## Qué hacer
1. Precios: Índice de Precios de Vivienda (INE, `ine.es`, trimestral), precio por m² (Ministerio de Vivienda / Registradores) y compraventas (INE o Notarios). Cada cifra con fuente y fecha.
2. Hipotecas: nuevas hipotecas y su importe medio (INE), cuota estimada con el euríbor y el diferencial del panel C71 (fórmula visible, ejemplo de 150.000 € a 25 años; es un EJEMPLO, no una predicción).
3. Salud del crédito: morosidad bancaria (Banco de España, `bde.es`, mensual) y esfuerzo de acceso a la vivienda (BdE o Eurostat, relación entre precio e ingresos).
4. Explica en 10 líneas cómo se conectan euríbor, cuota, crédito nuevo y precios, separando HECHOS de OPINIONES [ESPECULACIÓN]. Caso alcista y bajista del mercado de la vivienda, con sesgos de las fuentes (inmobiliarias, promotores).
5. Si hay datos abiertos por API, añade lectura automática a `scripts/actualizar_paneles.py`; si no, a mano en `explorador/espana-manual.json` con su etiqueta [P]/[S].
6. Informe en `informes/research/AAAA-MM-DD-C73-vivienda.md`.
