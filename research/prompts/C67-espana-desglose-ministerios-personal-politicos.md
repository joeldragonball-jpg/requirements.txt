# C67 · España: desglose por ministerio, gasto fuera de los ministerios y coste del personal público y de los cargos políticos (pedido de Joel, 30-oct-2026)

Objetivo: que al abrir un ministerio se vea de qué se compone su gasto, que se vea también el gasto que no pasa por los ministerios, y cuánto personal público y cuántos cargos políticos hay y cuánto cuestan. Solo datos oficiales publicados; si no existe el desglose, decirlo en vez de estimarlo. Hechos con fuente y año; [VERIFICAR] lo no leído; opiniones aparte. Cada cifra con su denominador (% del gasto total, por habitante, por empleado). Sin recomendaciones ni adjetivos: las cifras hablan solas.

Parte de `explorador/espana-presupuesto.json` (C66, ya tiene secciones, políticas y 19 programas): NO lo rehagas, amplíalo.

## Parte A · Dentro de cada ministerio
1. Por sección (ministerio) y por capítulo económico: personal (cap. 1), gastos corrientes en bienes y servicios (2), gastos financieros (3), transferencias corrientes (4), inversiones reales (6), transferencias de capital (7), activos y pasivos financieros (8-9). Fuente: Hacienda, Presupuestos Generales del Estado, Estado de gastos, y IGAE para lo ejecutado.
2. Por ministerio, los 5-8 programas o centros gestores mayores (secretarías de Estado, organismos autónomos, agencias) con su importe, y el destino de las transferencias grandes (a CCAA, ayuntamientos, familias, empresas, exterior).
3. Altos cargos y gabinete de cada ministerio: nº de altos cargos (ministro, secretarios de Estado, subsecretarios, directores generales), personal eventual (asesores) y su coste, según el Portal de Transparencia y las retribuciones publicadas en el BOE. Sueldos oficiales del presidente, ministros y altos cargos.

## Parte B · Fuera de los ministerios
1. Seguridad Social (pensiones, IMV, desempleo, incapacidad): gasto por función y su financiación (cotizaciones frente a transferencias del Estado).
2. Organismos y entes: Casa Real (partida de la Casa de Su Majestad), Cortes Generales (Congreso y Senado), Tribunal Constitucional, Consejo General del Poder Judicial, Tribunal de Cuentas, Defensor del Pueblo, Consejo de Estado, órganos reguladores (CNMC, CNMV, Banco de España), RTVE y agencias estatales.
3. Comunidades autónomas y ayuntamientos: gasto total por nivel de administración y por función (COFOG), y gasto de los parlamentos y gobiernos autonómicos.
4. Intereses de la deuda y transferencias a la UE: importes y peso sobre el total.

## Parte C · Personal público y cargos políticos
1. Empleo público: nº de empleados por administración (AGE, CCAA, entidades locales, universidades, Seguridad Social) y por colectivo (funcionarios de carrera, interinos, laborales, fuerzas y cuerpos de seguridad, sanidad, docentes). Fuente: Boletín Estadístico del Personal al Servicio de las AAPP (Función Pública), EPA (INE, empleo público) y Contabilidad Nacional (IGAE, remuneración de asalariados de las AAPP como % del PIB y del gasto).
2. Coste de personal: remuneración de asalariados de las administraciones públicas (cap. 1 y Contabilidad Nacional) total y por nivel; masa salarial por habitante.
3. Cargos políticos: nº de diputados (Congreso), senadores, eurodiputados españoles, diputados de los 17 parlamentos autonómicos, consejeros y altos cargos autonómicos, alcaldes y concejales (por tipo de municipio; Ministerio de Política Territorial), y su coste conocido (asignaciones, dietas y retribuciones publicadas; asignaciones a grupos parlamentarios y a partidos, subvenciones electorales). Dónde no se publique el total, decirlo.
4. Coste de la «clase política» como suma: presentar solo la suma de lo publicado, con el desglose de qué incluye y qué no, y su % sobre el gasto público total y sobre el PIB. Dejar claro lo que no es medible (consejos de administración de empresas públicas, cargos de confianza en entes locales sin publicar).
5. Comparativa UE si la hay (Eurostat gov_10a_exp, remuneración de asalariados por país y % PIB), para dar una vara de medir.

## Entregables
- Ampliar `explorador/espana-presupuesto.json` (claves nuevas: `capitulos_por_ministerio`, `fuera_de_ministerios`, `personal_publico`, `cargos_politicos`; cada dato con año, fuente y nivel P/S/VERIFICAR).
- Informe `informes/research/AAAA-MM-DD-C67-desglose-ministerios-personal-politicos.md` con tablas, lo que no existe y [VERIFICAR].
- Mostrarlo: despliegue por ministerio en la pestaña España del Panel (`explorador/vistas.html`) y en las tarjetas de España del móvil (`construir_movil.py`). No tocar `SECURITY_REPORT.md`.

## Cómo ejecutarlo
Sesión nueva con el relevo (`privado/relevo.md`). Lectura larga de PDF/Excel de Hacienda, Función Pública e INE: Opus esfuerzo alto si Joel lo autoriza, navegador integrado para webs con 403. Dividir en dos sesiones si hace falta (A+B y C). Parar al 70 % de contexto. Regenerar con `construir_movil.py` y `construir_seguimiento.py`.
