# C08 · Consolidación del archivo principal del cerebro (25-oct-2026)

Opción B autorizada por Joel el 25-oct-2026 (una sola vez). No se ha borrado ni reescrito nada: se creó `cerebro/documentos/resumen-vigente-xrp.md` y se añadió una línea final a `cerebro/apuntes_xrp_macro_fiscalidad_2026.md` marcándolo como HISTÓRICO. Base: el propio archivo (leído por secciones), `cerebro/documentos/estado-vigente-y-correcciones.md` (incluidas las verificaciones C09) y `informes/research/2026-10-25-revision-cerebro-contradicciones.md`. Sin búsquedas web nuevas: todo dato sale de lo ya verificado en el repo.

## Qué se fusionó (una sola versión de cada dato)
| Tema | Veces en el archivo viejo | Versión vigente |
|---|---|---|
| Litigio SEC-Ripple | 5 (Explicación, Cifras, Dudas, Verificado oct, Correcciones 21-oct) | Multa $125 M + injunction; apelaciones retiradas ago-2025 [S] |
| CLARITY 15-sep | 6 («rechazó», «estancada», «fracasa», canónica) | Cloture fallido 49-50, no rechazo definitivo; viva para el lame-duck [S] |
| Fed | 4 (pausa 3,50-3,75 % de mayo y correcciones) | 3,75-4,00 % desde 16-sep-2026 [P] |
| Adquisiciones de Ripple | 5 («más de $4.000 M», «Rail y Palisade ~$200 M», correcciones) | ≈ $2.700 M con precio; lista de las que no tienen precio |
| SEC-CFTC 17-mar | 3 (nota, [VERIFICAR], C09) | 16 digital commodities con XRP y XLM [P: Release 33-11412] |
| Sección 404 | 4 | Existe en el compromiso Tillis-Alsobrooks [S]; texto literal [VERIFICAR] |
| MEI | 4 (0,7 / 0,8 / 0,90) | 0,90 % (0,75 + 0,15), Orden PJC/297/2026 [S] |
| ITP Cataluña | 5 (10 %/11 %, 10-13 %, jóvenes 32 o 35) | Escala 10-13 %, 20 % grandes tenedores; jóvenes 5 % hasta 35 años, base ≤ €36.000 [P: ATC] |
| Evernorth | (no estaba en el viejo; venía del estado vigente) | 388.910.554 XRP; −1,05 % con su base explicada |
| Bonos, Brent, Ormuz | mayo-2026 | Series de octubre con fuente primaria |
| IVA recaudado | 2 | €99.532 M (2025) [P: AEAT] |

## Qué se descartó y por qué
- **Instantáneas de mercado de mayo-2026** (oro, Brent ~$100-112, 10 años ~4,58 %, BTC, XRP, DXY, BCE con 3 subidas descontadas, hitos EE. UU.-Irán de mayo, Polymarket 65 → 54 %): superadas; queda una línea que las marca como históricas.
- **Fiscalidad general española no ligada a cripto** (cotizaciones detalladas, ruta de 100 €, ejemplo de nómina de Osona, vivienda por comunidades, IBI, plusvalía, recaudación por impuesto, dividendos escalonados): no es «vigente sobre XRP» y sigue íntegra en el archivo histórico. Se conservaron solo cotizaciones/MEI, IVA y la parte cripto, patrimonio, residencia e ITP.
- **Fundamentos didácticos** (interés compuesto, TIN/TAE, letras, Lombard) y la mayoría de los ~75 conceptos: siguen en el histórico; se dejaron 12 conceptos útiles para XRP.
- **Plan patrimonial personal** (escenario de importe, cartera de destino, plan de salida, Andorra como opción personal): no se copia por la regla de privacidad de la tesis (repo público). Queda en el histórico tal cual y en `privado/`.
- **Contradicciones ya resueltas** («multa rebajada a $50 M», «58,7 %» de la ruta de 100 €, fecha del BCE 29 vs. 30-abr, «20 % del volumen de SWIFT» sin fuente): resueltas o sin fuente; no aportan al estado vigente.
- **Opiniones de terceros** («la revolución es inminente», «la ley saldrá pase lo que pase», «fin del petrodólar»): resumidas en caso alcista/bajista y predicciones ajenas, todo [ESPECULACIÓN].

## Lo que queda abierto
Listado en «Dudas y datos a verificar» del resumen vigente, con la tarea que lo cerrará (W05 o W08). De la lista original del prompt, C09 ya cerró tres (ITP de Cataluña, SEC-CFTC y XRP/XLM, base del −1,05 % de XRPN); siguen la sección 404 (texto literal) y la fuente y precio de cada adquisición de Ripple.

## Coste de la app (procesar.py lee todos los .md de `cerebro/`)
- Antes: 243.547 bytes (≈ 238 KB) de Markdown en `cerebro/`.
- Después: 261.556 bytes (≈ 255 KB): **+18.009 bytes (+7,4 %)**; el archivo viejo solo crece una línea (~100 bytes).
- Para que el ahorro sea real habría que excluir el archivo histórico de lo que lee procesar.py (−78 KB, ≈ −30 %). Es un cambio de código: no se ha hecho; decisión de Joel.
