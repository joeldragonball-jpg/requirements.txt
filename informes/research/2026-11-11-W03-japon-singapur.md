# W03 · Japón y Singapur: comprobación de huecos (11-nov-2026)

Informativo; no es recomendación de compra ni venta. Etiquetas: [P] documento oficial leído · [S] prensa · [VERIFICAR].

## HECHOS
- **Japón · ETF (celda sigue en [S]).** Las «Prioridades estratégicas de la FSA, jul-2026 a jun-2027» (15-sep-2026; PDF en fsa.go.jp, leído [P]) solo mencionan vigilar a los proveedores de cripto y actuar contra los no registrados; no citan ETF. La estrategia de servicios financieros 2026 del Gobierno (cas.go.jp, leída [P]) habla de «revisar los marcos de stablecoins, tokenización y DeFi», sin ETF. La lista de notas de prensa de la FSA hasta el 6-nov-2026 no trae decreto ni anuncio sobre ETF cripto. Sin fuente primaria que lo apruebe: la celda no sube a [P].
- **Singapur · stablecoins y ETF.** Chrome conectado; el listado de notas de prensa de la MAS (consultado 11-nov) no muestra ninguna nota sobre cripto o stablecoins posterior a la consulta del 16-oct (la última es del 10-nov, sobre oro). Respuesta a la consulta y ley final: sin publicar [P, por ausencia en el listado; primera página solamente].
- Plazos nuevos al calendario: ninguno.

## Caso a favor / en contra (sin recomendar)
- A favor: Japón mantiene la dirección hacia permitir ETF (reforma fiscal ya prevista) y Singapur avanza en su marco de stablecoins.
- En contra: sin decreto ni fecha, ambas siguen sin producto minorista; plazo 2027-28 [S].
- Para XRP/XLM: sin cambio medible hoy; un ETF japonés sería a lo sumo un canal futuro.

## [VERIFICAR]
Decreto de la FSA sobre ETF; resultados de la consulta de la MAS; fuentes de la MAS dan error con curl (usar Chrome).

## Lecciones
- mas.gov.sg: curl devuelve página de mantenimiento; Chrome sí abre el listado, pero el texto de la nota concreta no cargó con get_page_text.
- `python -I` falla en este entorno; PDF con `pdftotext`.
