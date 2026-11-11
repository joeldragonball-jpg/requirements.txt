# C245 · Plantillas de órganos constitucionales (11-nov-2026)

Resultado: **ninguna cifra de personas ni de puestos totales verificada a nivel P para los 6 órganos**. Se localizaron las fuentes oficiales exactas y por qué no dan total. Puestos presupuestados ≠ personas: [VERIFICAR]. Chrome no hizo falta (sin 403).

| Órgano | Cifra | Tipo | Fuente | Fecha | Nivel |
|---|---|---|---|---|---|
| Cortes Generales (Congreso/Senado/JEC) | sin total publicado en texto; la web remite a «Composición numérica de Cuerpos...» (congreso.es/cem/acceso_empleo), que son tablas/imágenes no legibles | — | congreso.es/es/organos/secretaria-general | consulta 11-nov-2026 | S |
| Cortes: plantilla orgánica Sec. Gral. Congreso | PDF de 240 pp. con columna «Dotación» por puesto; no he sumado (el extractor de texto no separa bien las columnas: mi suma aproximada 842 sobre 462 filas NO es fiable) | puestos (plantilla orgánica) | congreso.es/docu/igualdad/Puestos_Plantilla_CDconsolidado_jun2022.pdf | jun-2022 (desfasada) | S [VERIFICAR] |
| Cortes: Intervención CCGG | ~43 puestos (suma aproximada, 37 filas; no fiable) | puestos | congreso.es/docu/igualdad/Puestos_Plantilla_CCGG.pdf | 19-jul-2021 | S [VERIFICAR] |
| Tribunal de Cuentas | sin cifra de personal en la Memoria 2025 (leída entera con pdftotext: solo cita Pleno que aprueba RPT, formación, igualdad «muy equilibrada»; sin nº) | — | Memoria anual 2025, congreso.es/docu/inf_fiscTC/LegXV/250-7.pdf (aprobada 25-mar-2026) | 25-mar-2026 | P (ausencia de dato) |
| CGPJ | RPT oficial publicada (19 pp., «RPT OFICIAL ENERO 2025», última modificación Pleno 18-jul-2024). Subtotales por unidad (p. ej. Apoyo a Presidencia 8 puestos, Oficina de Comunicación 36); sin total general en el documento; no sumado | puestos (RPT, con columna «puestos con dotación presupuestaria») | poderjudicial.es/stfls/CGPJ/TRANSPARENCIA/FICHEROS/20250313 RPT OFICIAL ENERO 2025.pdf | 13-mar-2025 | P (fuente) / sin total |
| Tribunal Constitucional | no encontrado; la plantilla solo se modifica vía Ley de Presupuestos (LOTC, disp. trans.); memoria 2024 no localizada | — | LOTC (BOE-A-1979-23709 consolidado) | — | S |
| Consejo de Estado | 24 letrados en activo (memoria 2013, citada por Público; sin leer la original); sin dato reciente | personas (solo letrados) | publico.es (secundaria) | 2013 | S [VERIFICAR] |
| Casa de S.M. el Rey | sin nº de personas; Informe del Interventor 2024 solo da capítulo 1: crédito total 4.763.437 euros (leído, pdftotext) | euros, no plantilla | casareal.es/ES/Documents/InformeIntervencion_Ejercicio 2024.pdf | ejercicio 2024 | P (solo euros) |

## Hechos útiles
- Los PGE no traen anexo de personal por órgano constitucional comparable (no localizado); la plantilla del TC se fija en la Ley de Presupuestos, pero no la he encontrado en texto.
- La EPSAP/RCP excluye estos órganos (ya anotado en el JSON existente).
- Casa Real: 4.763.437 euros de capítulo 1 (2024) es crédito, no personas ni coste medio.

## Siguiente paso propuesto (si Joel quiere)
1. Abrir en Chrome las tablas de «Composición numérica» del Congreso y del Senado (probable nivel P).
2. Sumar la columna «Puestos con dotación» de la RPT CGPJ con tabulado (pdfplumber) o pedirlo por Ley 19/2013.
3. Buscar la plantilla del TC en el BOE de la Ley de PGE y la memoria del Consejo de Estado en consejo-estado.es.

## JSON propuesto (no aplicado; explorador/*.json intacto)
```json
{
 "organos_constitucionales": [
  {"organo":"Tribunal de Cuentas","empleados":null,"tipo":"sin dato","nota":"Memoria 2025 no publica nº de personal [VERIFICAR]","fuente":"https://www.congreso.es/docu/inf_fiscTC/LegXV/250-7.pdf","fecha":"25-mar-2026","nivel":"P"},
  {"organo":"CGPJ","empleados":null,"tipo":"puestos (RPT)","nota":"RPT enero 2025 publicada, total no sumado; puestos con dotación ≠ personas [VERIFICAR]","fuente":"https://www.poderjudicial.es/stfls/CGPJ/TRANSPARENCIA/FICHEROS/20250313%20RPT%20OFICIAL%20ENERO%202025.pdf","fecha":"13-mar-2025","nivel":"S"},
  {"organo":"Casa de S.M. el Rey","empleados":null,"cap1_credito_euros":4763437,"nota":"solo euros (cap. 1, 2024), no plantilla","fuente":"https://www.casareal.es/ES/Documents/InformeIntervencion_Ejercicio%202024.pdf","fecha":"ej. 2024","nivel":"P"},
  {"organo":"Cortes Generales","empleados":null,"nota":"tablas de composición numérica en congreso.es/cem/acceso_empleo, no leídas [VERIFICAR]","nivel":"S"},
  {"organo":"Tribunal Constitucional","empleados":null,"nivel":"S"},
  {"organo":"Consejo de Estado","empleados":null,"letrados_activos_2013":24,"nota":"secundaria, 2013 [VERIFICAR]","nivel":"S"}
 ]
}
```

Resumen: 1) Seis órganos siguen sin cifra de personas verificada; no hay dato nuevo que cambie el JSON salvo notas. 2) Fuentes oficiales localizadas: RPT CGPJ (ene-2025), plantillas orgánicas del Congreso/Cortes (PDF 2021-22) y capítulo 1 de la Casa Real (4.763.437 euros, 2024). 3) Falta sumar la RPT del CGPJ y leer en Chrome las tablas del Congreso/Senado y la plantilla del TC en BOE.
