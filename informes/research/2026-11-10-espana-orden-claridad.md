# España · orden y claridad de la Órbita (10-nov-2026)

Tarea C250 (el id C247 ya lo usaba otra tarea). Archivo tocado: `explorador/vistas.html` (función `pEspana`).

## Criterio de reparto

| Subpestaña | Qué responde | Entra |
|---|---|---|
| Economía y deuda | ¿Cuánto produce, ingresa, debe y paga de intereses el país? | macro INE, comparativa con zona euro, ingresos y gasto de las AAPP, recaudación, AIReF, deuda del Estado y de CCAA, intereses, dinero al exterior, rescate bancario |
| Presupuesto y gasto | ¿En qué se gasta y quién lo gasta? | presupuesto por ministerio, políticas, programas, Seguridad Social, altos cargos y empleados, personal público, cargos políticos, empresas públicas, comparador de CCAA, gasto en paro |
| Dónde va el dinero (nueva) | ¿A qué empresas y entidades llega? | contratos, subvenciones, registros por día, opacidad. Se separa porque es un tema propio (adjudicatarios) y evita que Presupuesto pase de 30 bloques |
| Política y leyes (nueva) | ¿Quién decide y qué normas salen? | Congreso, iniciativas, intereses de diputados, partidos, altos cargos (informe OCI), leyes del BOE |
| Servicios y sociedad / Seguridad y salud / Justicia | Resultados para las personas | sin cambios, salvo «Criminalidad registrada» (antes caía en Presupuesto por llevar «Ministerio» en el título) → Seguridad |

## Inventario antes → después

| Bloque | Antes | Después |
|---|---|---|
| Economía de España (INE), Deuda CCAA (PDE) | Economía | Economía |
| España frente a zona euro, Ingresos y gasto AAPP, AEAT, Recaudación récord, AIReF, Deuda del Estado, Intereses (x2), Dinero al exterior, Rescate bancario | Economía | Economía (reordenados de general a técnico) |
| Congreso, Iniciativas, Intereses diputados, Financiación partidos, Política: lo no leído | **Economía** | **Política y leyes** |
| Leyes y normas del BOE | **Economía** | **Política y leyes** |
| Altos cargos: informe OCI | **Presupuesto** | **Política y leyes** |
| Contratos, Subvenciones (Dónde va el dinero) | **Economía** | **Dónde va el dinero** |
| Subvenciones y contratación: registros por día, Hasta dónde llegan los datos oficiales | **Presupuesto** | **Dónde va el dinero** |
| Empresas públicas, Comparador de CCAA, Quién gasta cada cosa | **Economía** | **Presupuesto y gasto** |
| Gasto en paro | Economía | Presupuesto y gasto |
| Cómo leer el presupuesto, por ministerio, Programas, No aislable, Fuera de ministerios (x2), Altos cargos y eventuales, Personal público (x3), Cargos políticos, Consolidado 2023, Ejecución por políticas | Presupuesto | Presupuesto (reordenados) |
| Criminalidad registrada | **Presupuesto** | **Seguridad y salud** |
| Vivienda, Hipotecas, Quién recibe, Violencia de género, Inmigración, Resultados servicios, Listas de espera | Sociedad | Sociedad |
| Defunciones, Carretera, Delitos, DANA, Incendios, Siniestralidad vial y laboral | Seguridad | Seguridad |
| Justicia · casos en curso | Justicia | Justicia |

Contadores tras el cambio (comprobados en el navegador): Economía 12 · Presupuesto 17 · Dónde va el dinero 4 · Política y leyes 7 · Servicios 8 · Seguridad 8 · Justicia 1 (suman 57). Sin errores de consola; a 375 px no hay desbordamiento horizontal.

## Cómo está hecho
- `temaDe` pasa de una sola expresión a una lista ordenada `REG` (la primera regla que casa gana) y una lista `ORD` fija el orden dentro de cada subpestaña. Un bloque nuevo sin regla cae en Economía y va al final.
- No se tocó el interior de los bloques de política ni de contratos.

## Claridad
- Nuevo diccionario `EXPL` (en `pEspana`): cada bloque de Economía y de Presupuesto lleva bajo el título un párrafo «En claro:» de 3-4 frases (qué es, columnas, unidades, qué NO dice). Se ha usado un diccionario central en vez de `conL(...)` bloque a bloque: el resultado visible es el mismo, pero el texto no queda plegado por `corto()` ni obliga a editar código ajeno.
- Corregido: la cabecera «Altos cargos + eventuales sobre personal (M€)» era en realidad un % → ahora «…, %». El texto de «Altos cargos y personal eventual» deja claro que «Personal total» ya incluye altos cargos y eventuales (no se suman).
- Siglas traducidas la primera vez en cada bloque: PDE, IGAE, AIReF, AEAT, INE, EPA, IPC, PIB, CCAA, SEPI, COFOG, IMV, BOE, p.p., M€.

## Pendiente / avisos
- Los bloques **Pensiones y Seguridad Social, Demografía (INE), Energía en España y Deuda CCAA (manual)** existen en `espana-manual.json` y en el código, pero no se ven porque `explorador/espana.json` (campo `manual`) está desactualizado. Se arregla regenerándolo con `scripts/espana_fiscal.py` (usa red, Eurostat); no lo he lanzado. Sus reglas de subpestaña y su «En claro» ya están preparados (Pensiones → Presupuesto; Demografía → Servicios).
- Los textos «En claro» describen la estructura, no cifras; las cifras siguen saliendo de sus fuentes con su nivel P/S.
- Sin commit ni push.
