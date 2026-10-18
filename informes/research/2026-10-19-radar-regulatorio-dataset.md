# Radar regulatorio: dataset por país y tema (sesión 1, 2026-10-19)

Archivo nuevo: `explorador/regulacion.json`. Vista: pendiente (sesión 2, `mapa.html` sin tocar). Sin búsquedas web ni API: todo sale de informes, dossiers, apuntes y `eventos/calendario.toml`. Informativo, sin recomendaciones de compra/venta.

## Qué contiene
- **12 filas**: EE. UU., UE, Singapur, Hong Kong, Corea del Sur, Japón, India, Brasil, Rusia, Emiratos, China y BRICS/BIS (supranacional).
- **6 temas**: stablecoins, mercado y ETF, tokenización, custodia, CBDC y fiscal.
- **Por celda**:
  - `etapa`: 0-5, o `null` si no hay dato.
  - `estado`: frase completa.
  - `fecha`: último cambio, en AAAA, AAAA-MM o AAAA-MM-DD según la precisión de la fuente.
  - `fuente`: P, S o VERIFICAR.
  - `proxima`: fecha y qué pasa, o `null`.
  - `falta`, `hitos` (fecha y qué pasó) e `informes` de origen.
- **Escala de etapas**:
  - 0: sin marco o prohibido.
  - 1: propuesta, consulta o piloto sin norma.
  - 2: en trámite.
  - 3: aprobada sin vigor.
  - 4: en vigor.
  - 5: en vigor con licencias o supervisión activa.
  - Los pilotos oficiales sin ley específica (MAS, e₹, Agorá) se clasifican en 1.
- **Lista `huecos`**: zonas sin research.

## Resultado: 72 celdas, 47 con dato y 25 sin dato

| Jurisdicción | Stablecoins | Mercado y ETF | Tokenización | Custodia | CBDC | Fiscal |
|---|---|---|---|---|---|---|
| EE. UU. | 3 [P] | 4 [P] | 4 [P] | 4 [P] | 0 [P] | 5 [P] |
| Unión Europea | 5 [P] | 5 [P] | 4 [P] | 5 [P] | 2 [P] | 4 [P] |
| Singapur | 1 [P] | 5 [S] | 1 [P] | — | 1 [S] | 4 [P] |
| Hong Kong | 5 [P] | 5 [P] | — | — | — | — |
| Corea del Sur | 2 [S] | 2 [S] | 3 [P] | 4 [S] | — | — |
| Japón | 5 [S] | 3 [S] | — | — | — | 4 [S] |
| India | 0 [S] | 1 [S] | — | — | 1 [S] | 5 [S] |
| Brasil | 4 [S] | 4 [S] | 1 [S] | 4 [S] | 0 [S] | 4 [S] |
| Rusia | — | 4 [S] | — | 4 [S] | 5 [P] | — |
| Emiratos | 5 [P] | 5 [S] | — | — | — | 4 [S] |
| China | — | — | — | — | 4 [S] | — |
| BRICS / BIS | 1 [S] | 0 [S] | 1 [S] | — | 1 [S] | — |

— = sin dato (etapa `null`, fuente VERIFICAR, salvo Hong Kong/tokenización, que tiene un dato [P] pero no basta para clasificar).

Fuentes de las 72 celdas: 21 [P], 27 [S] y 24 VERIFICAR. Ninguna celda [S] se ha subido a [P] sin que un informe lo diga.

## Decisiones que conviene revisar (criterio propio, discutible)
- **EE. UU., mercado = 4.** Los ETF y la interpretación SEC-CFTC funcionan con la ley vigente, pero la ley de estructura de mercado (CLARITY) está bloqueada. Si se mira solo la ley, sería 2.
- **Corea, mercado = 2 y custodia = 4.** Los exchanges y custodios están registrados ante KoFIU (registro antiblanqueo), pero la ley de la 2.ª fase no está aprobada.
- **China, CBDC = 4.** El e-CNY es formalmente un piloto, pero desde el 1-ene-2026 tiene una regla (depósito remunerado). El e₹ indio se queda en 1 porque el repo no recoge su base legal.
- **Japón, stablecoins = 5.** Se basa en el marco de 2023 y en la aprobación de RLUSD por la JFSA, todo [S].
- **BRICS/BIS, mercado = 0.** No hay marco vinculante, solo estándares (GAFI, FSB, IOSCO).
- **UE, CBDC = 2.** Se mantiene la contradicción sobre la posición del Consejo (ver el cruce de fichas del 19-oct).

## Celdas sin dato (25)
- **Hong Kong:** tokenización (solo la circular de la SFC), custodia, CBDC y fiscal.
- **Corea del Sur:** CBDC (proyecto Hangang no revisado) y fiscal.
- **Japón:** tokenización, custodia y CBDC.
- **India:** tokenización (solo un piloto mayorista del RBI, secundaria) y custodia.
- **Rusia:** stablecoins (categoría solo en un extracto), tokenización y fiscal.
- **Emiratos:** tokenización, custodia y CBDC (solo el anuncio del dirham digital).
- **China:** stablecoins, mercado, tokenización, custodia y fiscal.
- **BRICS / BIS:** custodia y fiscal.
- **Singapur:** custodia.

## Huecos (sin research en el repo)
- Sudáfrica, Indonesia, Egipto, Etiopía e Irán: miembros o socios de BRICS sin informe propio.
- Arabia Saudí: solo consta su salida de mBridge.
- Reino Unido y Suiza: están en R18 pero fuera de la matriz. El régimen británico entraría en vigor el 25-oct-2027 [P].
- Canadá: solo por los ETF de XRP. Australia: sin research.
- La custodia cripto fuera de EE. UU. y la UE no la trata ningún informe.

## Comprobaciones nuevas en `scripts/revisar_explorador.py`
- Campos obligatorios en cada celda.
- Jurisdicción y tema conocidos, sin celdas repetidas ni que falten.
- Etapa 0-5 o `null`.
- Fechas válidas en celdas, próximas fechas e hitos.
- `estado` y `falta` empiezan con mayúscula y acaban en punto; también los hitos.
- Fuente P, S o VERIFICAR, e informes de origen en las celdas con dato.
- Las celdas sin dato no cuentan como aviso: el script las resume en una línea.
- Probado metiendo cinco errores a propósito: los detectó todos. Con el archivo correcto, el script da los mismos 8 avisos previos del Explorador y ninguno del radar.

## Siguientes pasos (no hechos)
1. Sesión 2: la vista del radar en `mapa.html`.
2. Rellenar las celdas sin dato con research nuevo, con prioridad para China, Japón (tokenización y custodia), Hong Kong y Emiratos.
3. Cada nuevo informe R que cambie una norma debería actualizar la celda y añadir un hito.
