# W03 · Huecos del radar regulatorio (20-nov-2026)

Objetivo: cerrar 9 celdas con etapa null (ETF: BRICS, ID, IR, ES, AE; fiscal: EG, ET, IR) con fuente primaria leída. Resultado: **0 celdas cerradas; `explorador/regulacion.json` no se modificó** (sin fuente primaria legible, las celdas quedan vacías, como pide la regla).

## Intentos de hoy
- ES (CNMV): Chrome redirige cnmv.es a otro dominio y el lector bloquea la lectura (control de seguridad); con curl, `Preguntas-Frecuentes-Criptoactivos` devuelve error CVFE (página inexistente). La búsqueda solo devuelve el documento de 2018 (ya recogido [P]) y prensa. Circular 2/2025 (publicidad cripto) existe según prensa [S], pero no es norma de ETF. Sin etapa.
- ID (OJK): ojk.go.id responde «Request Rejected» (WAF) a curl; no se sortea. bi.go.id y peraturan: sin respuesta. Sin etapa.
- AE: sca.gov.ae/securities.sca.gov.ae sin respuesta; dfsa.ae 403; vara.ae carga pero el Registro no lista ETF cripto (ya anotado). Sin etapa.
- IR: seo.ir y tax.gov.ir no responden (código 000). EG: fra.gov.eg carga, sin nada cripto en lo leído antes. ET: mofed.gov.et responde 200 pero no se encontró norma fiscal cripto. Sin etapa.
- BRICS ETF: «no aplica» (no hay ETF supranacional); se deja así.

## Estado
Las 9 celdas siguen vacías con nivel V/S [VERIFICAR]. Es el 5.º intento acumulado; los bloqueos son de red/WAF, no de contenido. Se necesita acceso desde una red local (Indonesia, Emiratos, Irán) o consulta humana en CNMV/OJK.

## Validación
Sin cambios en el JSON; no se ejecutan construir_*.
