# C357 · Cadenas y voces: pistas sin concretar (21-nov-2026)

Archivo producido: `explorador/cadenas-pistas.json` (30 pistas). No se tocó cadenas.json ni voces.json.

## Método y límites
- Se recorrieron las 225 voces de `explorador/voces.json` y se cruzaron con actores y redes de `cadenas.json` (16 cadenas, 5 relaciones) e `interconexion.json`.
- Búsquedas y lecturas con WebSearch/WebFetch (no Chrome: no hizo falta salvo el 403 de Mastercard, que queda [VERIFICAR]). Leídas literalmente en página oficial: db.com (16-sep), Citi (2-sep), Visa (29-abr), FF News sobre SG-FORGE. El resto son resúmenes de buscador [S], marcados.
- HECHOS: lo que dicen las notas oficiales. OPINIONES: lecturas del canal («se salta Swift») y de directivos citados por prensa.

## Tabla de pistas

| id | actor | estado | nivel | qué falta concretar |
|---|---|---|---|---|
| pista-db-ripple | Deutsche Bank | sin_confirmar | S | token, red, producto |
| pista-db-salta-swift | Deutsche Bank | matizada | S | token, red, producto |
| pista-db-custodia | Deutsche Bank | confirmada_concreta | P | red |
| pista-db-hedera | Deutsche Bank | sin_confirmar | S | token |
| pista-swift-ledger-17 | Swift (17 bancos piloto) | matizada | S | token |
| pista-citi-swift | Citi | confirmada_concreta | P | token, red |
| pista-citi-token-services | Citi | confirmada_sin_concretar | S | token |
| pista-citi-solana | Citi | sin_confirmar | S | token |
| pista-jpmd-canton | JPMorgan (Kinexys) | matizada | S | — |
| pista-jpm-dtcc-cme | J.P. Morgan (con DTCC) | confirmada_concreta | P | token |
| pista-kinexys-8-divisas | JPMorgan (Kinexys) | confirmada_sin_concretar | S | token, red |
| pista-barclays-dtcc | Barclays | confirmada_sin_concretar | S | token |
| pista-bofa-dtcc | Bank of America | confirmada_sin_concretar | P | token |
| pista-dtcc-stellar-solana | DTCC | confirmada_concreta | P | token |
| pista-dtcc-l1 | DTCC (Frank La Salla) | confirmada_sin_concretar | S | token, red, producto |
| pista-ripple-prime-dtcc | Ripple Prime | confirmada_sin_concretar | P | token, red |
| pista-socgen-xrpl | Société Générale (SG-FORGE) | confirmada_concreta | S | — |
| pista-mastercard-rlusd | Mastercard | confirmada_concreta | S | — |
| pista-visa-9-cadenas | Visa | confirmada_concreta | P | red |
| pista-euroclear-clearstream | Euroclear / Clearstream / DTCC | confirmada_sin_concretar | S | token, red, producto |
| pista-pontes | BCE / Eurosistema | confirmada_concreta | S | token, red |
| pista-goldman-bny-mmf | Goldman Sachs y BNY | confirmada_concreta | S | token |
| pista-goldman-13f | Goldman Sachs | confirmada_concreta | P | token |
| pista-franklin-dbs-ripple | Franklin Templeton, DBS y Ripple | confirmada_concreta | S | — |
| pista-ripple-bce | Ripple (Qivalis / BCE) | desmentida | S | token, red, producto |
| pista-old-glory | Old Glory Bank | desmentida | S | — |
| pista-usbank-stellar | U.S. Bank | confirmada_concreta | P | — |
| pista-moneygram-stellar | MoneyGram | confirmada_concreta | S | — |
| pista-bis-xrpl | BIS | confirmada_concreta | P | token |
| pista-csdbr-btg | CSD BR, Ripple y BTG Pactual | confirmada_concreta | P | token |

## Hallazgos clave
- **Deutsche Bank + Ripple**: V01 la dio por confirmada sin concretar; aquí solo hay prensa derivada de Der Aktionär (feb-2026), sin comunicado de DB ni de Ripple. Se marca `sin_confirmar`, nivel S, token/red/producto «sin concretar». Conviene revisar la nota de v186/v193. Lo confirmado de DB: custodia propia (db.com 16-sep, proveedores sin nombrar) y participación en el diseño del libro mayor de Swift.
- **Caso alcista**: bancos grandes usan ya software ligado a Ripple (SG-FORGE EURCV en XRPL con Ripple Custody, DZ Bank, Mastercard con RLUSD en XRPL). **Caso bajista**: Visa (9 cadenas) y DTCC (Canton, Besu, Stellar, Solana) no nombran XRPL; la mayoría de piezas son pilotos o capacidades, sin volumen, y el uso de software no implica demanda del token.
- **Sesgos**: Ripple y Stellar comunican sus propias alianzas; agregadores XRP amplifican; Taurus y Mastercard son comunicación corporativa.

## Sin verificar
- Mastercard (403), Swift 9-jul (stack Linea o Besu), Citi Token Services, Pontes y discurso de Cipollone, Goldman/BNY: leídos solo en buscador.
- JPMD en Canton: solo intención; ninguna emisión viva localizada.
- Citi-Solana, DB-Hedera: una fuente secundaria cada una.
- Red de depósitos tokenizados de The Clearing House (BofA, Citi, Wells Fargo, JPMorgan): solo prensa.
- Sin cubrir por tiempo: Euroclear nota propia, Bitwise/Jupiter, Canton, Stellar-DBS; las voces v187-v188/v198 siguen en voces.json sin pista.

## Cableado propuesto (coordinador)
Mostrar en la ficha de cada cadena (`red_o_ambito`) las pistas con etiqueta «sin concretar» en el campo no precisado; las de `red_o_ambito: null` van a la vista de actores. Ejemplos: Deutsche Bank en xrpl (pista-db-ripple) y hedera (pista-db-hedera).
