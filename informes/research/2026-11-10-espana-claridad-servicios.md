# España · claridad en Servicios y sociedad, Seguridad y salud y Justicia (10-nov-2026)

Archivo tocado: `explorador/vistas.html` (solo estos bloques). Ayudante nuevo `claro(texto)` (párrafo siempre visible, sin plegar) y diccionario `CLX`.

## Qué se hizo
Cada tabla lleva ahora un párrafo «Qué es … Qué NO dice» de 3-4 frases, con siglas traducidas (INE, EDeS, ISCIII/MoMo, ICCS, DANA, IMV, TAE, HPI, EFFIS, DGT, SNS, UE-27, TSJCV, EPPO, CIAF) y unidades en columnas y KPI.

- **Servicios y sociedad (8):** Hipotecas INE, Precio vivienda Eurostat, Vivienda e hipotecas, Quién recibe, Violencia de género, Inmigración, Resultados servicios UE, Listas de espera y abandono escolar.
- **Seguridad y salud (8):** Defunciones semanales (exceso ≠ defunciones totales), Muertos en carretera, Delitos registrados (registrado ≠ condena), DANA, Incendios, Siniestralidad vial, Accidentes de trabajo, Criminalidad (Interior).
- **Justicia (1 bloque, 10 tarjetas):** párrafo de «Cómo leerlo» (no hay cifras; lista no exhaustiva ni orden de gravedad; siglas y términos: suplicatorio, ejecutoria, aforamiento). Presunción de inocencia ya estaba; neutralidad intacta, no se tocaron los hechos.
- Unidades: columnas «(n.º de personas)», «por millón de habitantes», «(n.º de delitos)», «Variación anual (%)»; KPI de resumen con «n.º de personas/casos».

## Comprobado
Navegador integrado (puerto 8795, Órbita → España): los 17 bloques de las tres subpestañas con explicación; sin errores de consola; a 375 px sin desbordamiento horizontal. Escritorio restaurado.

## Observaciones (no movido)
- «Violencia de género» (cifras de denuncias, órdenes, sentencias) estaría igual de bien en Justicia o Seguridad; hoy está en Servicios y sociedad.
- «Listas de espera y abandono escolar» y «Resultados de los servicios» mezclan sanidad y educación: podrían ir a una subpestaña «Sanidad y educación».
- «Inmigración» mezcla población, prisión y gasto; encajaría también en Seguridad/Justicia en parte.
- «Hipotecas», «Precio vivienda» y «Vivienda e hipotecas» pertenecen más a Economía que a Servicios y sociedad.
- Cifra de DANA: pendiente de comprobar series INE por municipio y DGT (ya figura en el bloque).

## Pendiente
Los bloques de otras subpestañas (Economía, Presupuesto, Política, Contratos) no se tocaron. Nota en `research/tareas.csv` (fila C248; C247 ya estaba ocupada por otra tarea).
