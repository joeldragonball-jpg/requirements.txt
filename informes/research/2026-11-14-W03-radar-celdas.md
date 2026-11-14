# W03 Radar regulatorio: celdas sin dato (14-nov-2026)

Resultado: 0 celdas cerradas; las 10 siguen con etapa null. No se editó regulacion.json (sin fuente primaria leída no se rellena).

Celdas (jur.tema) y por qué siguen sin dato:
- ir.etf, ir.fiscal, ir.politica: solo prensa y guías comerciales (Iran International ene-2026 menciona un impuesto antiespeculación del banco central que incluiría cripto; sin tasa ni texto). No se leyó cbi.ir. [VERIFICAR]
- eg.fiscal: las fuentes secundarias coinciden en que la Ley 194/2020 restringe la cripto y no hay régimen fiscal cripto; cbe.org.eg y eta.gov.eg no leídos. [VERIFICAR con Chrome]
- et.fiscal: el aviso del NBE de 23-jul-2026 sobre activos virtuales aparece en prensa y bufetes; ninguna fuente trata fiscalidad. nbe.gov.et no leído.
- id.etf: ojk.go.id sigue en 403 (reintento del 14-nov ya anotado en la celda).
- ae.etf: sin cambios; SCA redirige a uaecma.gov.ae (no leído); sigue [S].
- brics.etf: «no aplica» (supranacional); se deja null.
- es.etf: cnmv.es devuelve 403 en WebFetch y error de ruta en Chrome (URL probada sin éxito); falta el criterio de la CNMV [VERIFICAR].
- es.politica: es la del BCE, se sigue desde su panel; null intencionado.

Incidencia: la primera navegación de Chrome reutilizó una pestaña existente (Órbita, localhost:8797); la devolví a su URL anterior.

Eventos leídos: 0
