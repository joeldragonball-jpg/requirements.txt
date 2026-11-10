# C242 · Congreso, partidos y altos cargos (10-nov-2026) — en parte (segunda pasada hecha)

Datos en `explorador/espana-politica.json` (generado por `scripts/leer_congreso.py`; cifras del Tribunal de Cuentas transcritas a mano de los PDF oficiales). Vista: España › 6 bloques (Congreso, iniciativas, intereses, financiación, altos cargos, pendientes). Comprobado en la Órbita local (puerto 8795): sin errores de consola, bloques renderizados.

## Hechos [P] — Congreso (datos abiertos, 10-nov-2026)
- «DiputadosActivos»: 137 diputados en alta (PP 54, PSOE 49, VOX 12, Sumar 12, resto 2 cada grupo); 275 bajas, 213 con fecha 6-oct-2026 (un día después del RD 806/2026 de disolución, BOE-A-2026-20742). El fichero no explica por qué unos constan activos: [VERIFICAR]. No es el reparto de 2023.
- Pleno 203 (2-oct-2026), convalidación de RDL: 26/2026 (vivienda) 172 sí, 178 no; 27/2026 (alquiler) 166 sí, 184 no; 0 abstenciones.
- XV legislatura: 115 proyectos de ley del Gobierno (22 aprobados, 88 caducados, 2 rechazados, 2 retirados, 1 en otra situación) y 371 proposiciones de ley (10 aprobadas con modificaciones, 213 caducadas, 56 rechazadas…). «Caducado» = efecto procesal, no votación.
- Registro de intereses del Congreso: 2.787 registros (actividades 1.224, fundaciones 972, donaciones 409, observaciones 182) de 403 personas. Solo recuentos, sin nombres.

## Hechos [P] — financiación de partidos (Tribunal de Cuentas, leídos en el PDF del Congreso)
- Informe n.º 1.573, cuentas de los partidos, ejercicio 2020 (Pleno 27-jun-2024): 25 partidos; 20 con salvedades; financiación pública 73 % / privada 27 %; subvenciones de funcionamiento 167,74 M€; aportaciones de grupos parlamentarios 64,61 M€ y locales 38,80 M€; recursos privados 65,88 M€ (donaciones 2,07 M€, 5.754 donantes); deuda bancaria 79,24 M€ (PSOE 29,56, PP 22,92, IU 13,29 M€). El Tribunal anota 102.048,30 € de Vox ingresados por cajero sin justificar: observación de fiscalización, no sanción.
- Informe n.º 1.642, fundaciones y entidades vinculadas 2021-2022 (Pleno 25-sep-2025): aportaciones privadas 3,81 M€ (2021) y 4,12 M€ (2022); subvenciones públicas 2,39 y 2,54 M€; 3 entidades sin cuentas; resolución de la Comisión Mixta 21-may-2026 (BOE 14-jul-2026, BOE-A-2026-15347).
- Altos cargos: informe semestral de la Oficina de Conflictos de Intereses, 1.er semestre 2026 (firmado 2-jul-2026): procedimientos sancionadores incoados y resueltos «NINGUNO». Lista nominal no reproducida ni contada.

## Sesgos y límites
- Fuente institucional: lo que el Congreso, el Tribunal y la Oficina registran; no mide la exhaustividad de las declaraciones. Sin rankings ni calificaciones; «salvedad» ≠ ilegalidad; investigación ≠ condena (no se cita ninguna).
- Desfase: las cuentas de los partidos más recientes son de 2020 (publicadas en 2024).
- Discrepancia interna del informe 1.642: entidades inscritas en el Registro de Partidos (15+3 en la conclusión 5; 18+3 en el seguimiento) [VERIFICAR].
- Cifras del PDF leídas con pdftotext; transcripción manual, no cruzada con los anexos III-V.

## Sin leer (en `falta`)
- Contenido de las declaraciones de bienes de altos cargos (Registro de Bienes y Derechos Patrimoniales / Portal de Transparencia); Senado; histórico de votaciones por sesión y voto por grupo; informe del Tribunal de Cuentas posterior a 2020 si existe; BDNS «partidospoliticos» descartado (devuelve entidades ajenas).

## Lecciones
1. Los ficheros del Congreso llevan sello de fecha: resolverlos por prefijo desde la página.
2. Probar un endpoint con muestra antes de agregarlo (BDNS «partidos» no era lo que decía).
3. Tras una disolución, «activos» y «bajas» no equivalen a escaños: no inferir.
4. Los informes del Tribunal están en el Congreso (`docu/inf_fiscTC/LegXV/`); `pdftotext` basta, no hace falta Chrome.
5. La búsqueda web solo orienta: cada cifra se contrastó leyendo el PDF.
