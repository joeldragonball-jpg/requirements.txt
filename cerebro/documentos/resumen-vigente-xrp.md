---
tema: Resumen vigente de XRP, regulación, macro y fiscalidad
etiquetas: [XRP, XRPL, Ripple, RLUSD, CLARITY-Act, SEC, CFTC, MiCA, Evernorth, Fed, BCE, Ormuz, tokenizacion, colateral, IRPF, ITP, MEI, DAC8, estado-vigente]
actualizado: 25/10/2026
---
# Resumen vigente de XRP, regulación, macro y fiscalidad

Consolida `cerebro/apuntes_xrp_macro_fiscalidad_2026.md` (que pasa a HISTÓRICO) con lo vigente según `cerebro/documentos/estado-vigente-y-correcciones.md` y el informe `informes/research/2026-10-25-revision-cerebro-contradicciones.md`. Cada dato aparece una sola vez. Niveles: **[P]** primaria leída · **[S]** prensa o agregador · **[VERIFICAR]** · **[ESPECULACIÓN]**. Si algo choca con `estado-vigente-y-correcciones.md`, manda ese archivo (es más reciente cuando se amplía).

## Resumen
- **Regulación EE. UU.:** el litigio SEC-Ripple está cerrado (multa de $125 M e injunction en pie). El 17-mar-2026 la SEC, con la CFTC, publicó una interpretación que nombra a XRP y XLM entre 16 *digital commodities* [P]. La CLARITY Act no es ley: el 15-sep-2026 falló una moción de cierre de debate (49-50) y sigue viva para el lame-duck tras el 3-nov [S].
- **Ripple ≠ XRPL ≠ XRP.** Ripple ha montado una pila institucional (≈ $2.700 M en adquisiciones con precio conocido), pero eso no prueba demanda del token.
- **Macro (oct-2026) adversa para activos sin flujo de caja:** Fed 3,75-4,00 % tras subir el 16-sep [P], bono a 10 años 5,00 % y a 30 años 5,33 % (23-oct) [P], Brent > $110 y Ormuz casi cerrado (~4 barcos al día frente a 78 en febrero) [P].
- **España:** vender, permutar, pagar con cripto o sufrir la liquidación de un colateral tributa en la base del ahorro (19-30 %). El territorio (comunidad, municipio, residencia) cambia mucho la factura.
- **Riesgo principal de ejecución:** que el precio suba y se venda sin carpeta fiscal y AML, sin tramos escritos y sin reserva para impuestos.

## Explicación
**1. Qué es cada cosa.** Ripple es una empresa; el XRPL, una red pública que liquida en 3-5 s con AMM nativo (XLS-30) y *permissioned domains*; XRP, su token nativo; RLUSD, la stablecoin en dólares de Ripple.

**2. Quién puede congelar qué** (de más a menos resistente): XRP nativo en autocustodia (sin *freeze* de emisor; riesgos: claves, errores, contrapartes sancionadas) → tokens emitidos en el XRPL (el emisor puede congelarlos) → RLUSD y stablecoins reguladas (congelación y listas negras) → XRP en exchange, bróker o banco (KYC, límites, retenciones) → ETF (no tienes tokens, tienes participaciones). La resistencia es técnica, no patrimonial: banco, notario o Hacienda pueden exigir euros y trazabilidad.

**3. Regulación EE. UU.**
- *SEC-Ripple:* demanda dic-2020; fallo parcial jul-2023 (ventas programáticas a minoristas no son contratos de inversión; las institucionales sí); sentencia ago-2024 con multa de $125 M (la SEC pedía $2.000 M) e injunction; en jun-2025 la jueza no rebajó la multa y en ago-2025 ambas partes retiraron las apelaciones. **Estado único y final.** [S]
- *SEC 2026:* 30-ene, un valor tokenizado sigue siendo un valor; 17-mar (Release 33-11412), taxonomía de criptoactivos con 16 *digital commodities* que incluyen XRP y Stellar (XLM); el «18» que circuló no está en el texto [P: sec.gov/files/rules/interp/2026/33-11412.pdf].
- *CLARITY Act (H.R. 3633):* Cámara jul-2025 (294-134); Comité de Agricultura del Senado ene-2026; Comité de Banca 14-may-2026 (15-9). Pleno 15-sep-2026: cloture rechazado 49-50 (hacían falta 60), voto procedimental, no rechazo definitivo [S]. Faltan pleno, conciliación y firma. Contenido del borrador: *network tokens* (fuera de la SEC) y *ancillary assets*; artículo 604 (protege a desarrolladores y validadores no custodios); *Fast Lane* (registro provisional; sin él, implantación estándar de 360 días).
- *Sección 404:* existe en el texto de compromiso Tillis-Alsobrooks (may-2026): prohíbe pagar rendimiento «solo por mantener» stablecoins y permite recompensas por actividad [S: Consumer Federation of America, 8-may-2026] [VERIFICAR el texto en congress.gov].
- *Banca:* la OCC dio aprobación condicional de carta fiduciaria nacional a Coinbase el 2-abr-2026 (antes, dic-2025, a Ripple, BitGo, Circle, Fidelity Digital Assets y Paxos) [S]; norma final de la OCC sobre la ley GENIUS publicada el 23-oct-2026 [P: Federal Register].
- *ETF:* existen ETF de XRP al contado (desde nov-2025) con ~$1,4 mil M acumulados hacia mar-2026 mientras el precio caía ~54 % desde el estreno [S]. Presencia documental o entradas ≠ subida de precio.

**4. Europa (MiCA).** Periodo transitorio acabado el 1-jul-2026 (aviso de ESMA del 17-abr-2026): operar con proveedores sin licencia CASP da menos protección. Fricción con stablecoins multiemisión (USDC, USDG), posible aplazamiento a la revisión de MiCA de 2027. El BCE prefiere depósitos bancarios tokenizados. Consecuencia: la ruta XRP → stablecoin → banco no está garantizada en la UE.

**5. Infraestructura de Ripple y tokenización.**
- Adquisiciones con precio: Hidden Road $1.250 M (2025, hoy Ripple Prime) + GTreasury $1.000 M (oct-2025) [P: ripple.com] + Metaco $250 M (2023) + Rail $200 M (anunciada 7-ago-2025) [S] = **≈ $2.700 M**. Sin precio: Standard Custody (2024), Palisade (3-nov-2025), Solvexia; BC Payments Australia anunciada el 11-mar-2026 como adquisición propuesta, cierre no confirmado por Ripple. Fortress Trust: cancelada en oct-2023 [S].
- Ronda de $500 M con valoración de $40 mil M (nov-2025) [S]. Ripple Prime: calificación BBB de KBRA (2-abr-2026; deuda senior BBB estable el 8-jul-2026) [P: kbra.com]. Ripple Prime acepta XRP como colateral solo dentro de su bróker; el CME no lo acepta [S].
- Hechos recientes en el XRPL: Standard Chartered custodia RLUSD (12-oct); Franklin añadió ≈ $150 M de su fondo tokenizado en una cartera del XRPL (22-oct) [S]. Ninguno movió el precio de XRP de forma atribuible (ver `catalizadores-xrp-xlm.md`).
- Banca y mercado: BNY, depósitos tokenizados en red privada desde el 9-ene-2026 (Ripple Prime entre los primeros participantes; un depósito tokenizado es pasivo del banco). DTCC: tokenización con lanzamiento comercial previsto en oct-2026. SWIFT terminó la coexistencia MT/ISO 20022 el 22-nov-2025. Nada de esto obliga a usar XRP.
- RWA: fondos de letras tokenizados (BUIDL mínimo $5 M; OUSG $100.000; USDY $1) [S] rinden cerca del tipo de la Fed (3,75-4,00 %); rentabilidades del 15-18 % solo con capas de riesgo añadidas.

**6. Evernorth (XRPN).** Tesorería cotizada de XRP: 388.910.554 XRP aportados en especie y cotiza en Nasdaq desde el 12-oct-2026 [P: 8-K]. El «473 M XRP» era pro forma de 2025. Debut: apertura $16,68, cierre $16,91; el −1,05 % se mide frente al cierre previo ≈ $17,09 [S: Bitcoin.com]; desde la apertura fue +1,4 %. Detalle en `evernorth-xrpn-tesoreria-xrp.md`.

**7. Macro.** Cadena: Ormuz → petróleo y GNL → inflación esperada → Fed/BCE → rendimientos → liquidez de riesgo → BTC/XRP. Con petróleo y rendimientos altos, XRP puede no subir pese a buenas noticias regulatorias. Confirmar con datos físicos (tráfico, Brent/WTI, seguros), no con titulares. Desdolarización: gradual (dólar del 72 % de las reservas en 2001 a ~57 % en 2025) [S].

**8. Colateral sin vender.** Préstamo = valor × LTV. Con $4.000 de deuda sobre $10.000 (LTV 40 %), una caída del 30 % lleva el LTV al 57,1 %, del 50 % al 80 % y del 60 % al 100 %. Prestamistas institucionales: LTV ~50 % y *haircuts* de hasta el 50 % sobre XRP. Una reserva en el mismo activo no protege; un *lock-up* de 30-90 días no sirve ante un *margin call*.

## Puntos clave
- La tesis de XRP es una cadena condicional: claridad legal → infraestructura → liquidez real → uso del token → aceptación comercial → salida con estructura fiscal.
- Infraestructura de Ripple, BNY o DTCC no equivale a demanda de XRP; lo que cuenta es un papel concreto **del token**, volumen spot, profundidad y flujos.
- CLARITY: ni aprobada ni rechazada; vigilar el lame-duck tras el 3-nov.
- XRP y XLM están nombrados como *digital commodities* en la interpretación SEC-CFTC del 17-mar-2026 [P].
- Macro de octubre (Fed subiendo, 10 años al 5 %, Brent > $110) pesa más que las noticias propias a corto plazo.
- Capitalización ≠ liquidez: mirar profundidad de libro a ±1/2/5 %.
- Con LTV del 40 %, una caída del 60 % liquida el préstamo, y la liquidación tributa.
- En España, cualquier permuta (también XRP → stablecoin) es transmisión fiscal.
- La residencia fiscal solo cuenta si es real y anterior a la venta.

## Conceptos
- **Activo puente:** conecta dos monedas o redes sin ruta directa eficiente.
- **AMM / pérdida impermanente:** pool automático de liquidez / peor resultado que mantener cuando el precio se mueve mucho.
- **Velocidad de rotación:** veces que se reutiliza un token; reduce la capitalización necesaria para mover volumen.
- **Digital commodity (SEC-CFTC):** criptoactivo que no es valor por sí mismo salvo que se venda mediante contrato de inversión.
- **Network token / ancillary asset (CLARITY):** valor derivado de la red / aún dependiente de un emisor.
- **Cloture:** votación para cerrar el debate en el Senado (60 votos).
- **Depósito tokenizado:** saldo bancario en blockchain; pasivo del banco, no stablecoin.
- **CASP:** proveedor de criptoactivos autorizado bajo MiCA.
- **LTV / haircut / margin call:** deuda sobre colateral / descuento al colateral / exigencia de reponer garantía.
- **Permuta:** cambiar un activo por otro; fiscalmente es transmisión.
- **FIFO:** se venden primero las unidades compradas antes.
- **MEI:** cotización finalista para pensiones.

## Cifras y datos importantes
| Dato | Valor | Fecha | Fuente |
|---|---|---|---|
| Fed, rango objetivo | 3,75-4,00 % (subida 12-0) | desde 16-sep-2026 | Fed [P] |
| Bono EE. UU. 2 / 10 / 30 años | 4,69 % / 5,00 % / 5,33 % | 23-oct-2026 | Tesoro de EE. UU. [P] |
| Máximos del año 10 / 30 años | 5,31 % (5-oct) / 5,67 % (7-oct) | 2026 | Tesoro [P] |
| Brent, futuro continuo | $111,97 | 23-oct-2026 | Yahoo [S] |
| Brent, spot EIA | $115,22 | 20-oct-2026 | EIA [P] |
| Ormuz, barcos al día | 78 (feb) → 3,7 (7 días hasta 18-oct) | 2026 | IMF PortWatch [P] |
| CLARITY, cloture en el Senado | 49-50 (hacían falta 60) | 15-sep-2026 | prensa [S] |
| SEC-CFTC, digital commodities | 16, incluidos XRP y XLM | 17-mar-2026 | Release 33-11412 [P] |
| SEC-Ripple | multa $125 M + injunction | final ago-2025 | prensa [S] |
| Adquisiciones de Ripple con precio | ≈ $2.700 M | 2023-2025 | ripple.com [P] + prensa [S] |
| Ronda de Ripple | $500 M, valoración $40 mil M | nov-2025 | prensa [S] |
| Evernorth XRPN | 388.910.554 XRP; Nasdaq desde 12-oct | oct-2026 | 8-K [P] |
| ETF de XRP al contado | ~$1,4 mil M acumulados | hacia mar-2026 | prensa [S] |
| Mercado de divisas | $9,6 billones diarios | abr-2025 | BIS [P] |
| Yuan digital acumulado | CN¥16,7 billones (≈ $2,3 billones) | nov-2025 | PBoC vía prensa [S] |
| XRP / XLM | $1,30 / ≈ $0,176 | 23-oct-2026 | R00 cierre [S] |
| Base del ahorro IRPF | 19 / 21 / 23 / 27 / 30 % (tramos 6.000 / 50.000 / 200.000 / 300.000 €) | 2025-2026 | AEAT, manual IRPF 2025 [P] |
| Cotizaciones 2026, indefinido | empresa 30,65 % · trabajador 6,50 % | 2026 | Orden PJC/297/2026 [S] |
| MEI 2026 | 0,90 % (0,75 % empresa + 0,15 % trabajador) | BOE-A-2026-7296, 31-mar-2026 | [S] |
| IVA recaudado 2025 | €99.532 M (+9,9 %) | 2025 | informe anual AEAT [P] |
| Ingresos tributarios 2025 | €325.356 M (+10,4 %) | 2025 | AEAT [P] |
| ITP Cataluña, general | 10 % (≤ €600.000), 11 % (≤ €900.000), 12 % (≤ €1,5 M), 13 % (más); 20 % grandes tenedores | desde 2025 | Decreto-ley 5/2025; ATC [P] |
| ITP Cataluña, jóvenes | 5 % para ≤ 35 años (antes 32), base ≤ €36.000, vivienda habitual | desde 27-jun-2025 | Agència Tributària de Catalunya [P] |

Precios y niveles de mayo-2026 (oro, Brent ~$100-112, 10 años ~4,58 %, BTC ~$77.000-81.000, XRP $1,36-1,50) son **históricos**: no usarlos como estado actual.

## Opiniones y predicciones
**Caso alcista [ESPECULACIÓN]:** si la CLARITY sale en el lame-duck con *Fast Lane*, la entrada institucional se acelera; la clasificación como *digital commodity* y la pila de Ripple (prime brokerage, custodia, tesorería) facilitarían que bancos y fondos usen XRP como colateral o puente; tesorerías como Evernorth retiran oferta del mercado.

**Caso bajista [ESPECULACIÓN]:** la CLARITY puede pasar a 2027 con un Congreso nuevo; Fed subiendo, bonos al 5 % y petróleo caro drenan liquidez de riesgo; la tokenización avanza con redes privadas, stablecoins y depósitos tokenizados sin necesitar XRP; no hay mecanismo directo (comisiones o quemas) que ligue el negocio de Ripple al precio del token; las entradas en ETF no frenaron la caída.

**Predicciones ajenas que circulan (sin base verificable) [ESPECULACIÓN]:** XRP a $8-10 a final de 2026 (exigiría multiplicar por ~6 en dos meses); «precio de diseño» de cientos o miles de dólares; transmisión de XRP por radio o satélite (sin respaldo técnico). Las predicciones con fecha están en `informes/predicciones.md`.

**Sesgos de fuente:** Ripple («etapa institucional», 17-abr-2026) es fuente interesada; canales de vídeo y cuentas cripto tienden a leer cada titular como confirmación.

## Relación con mi cartera (XRP / XLM)
- **Qué mediría avance real:** papel concreto del **token** en anuncios de Ripple, BNY, DTCC o bancos; volumen spot y profundidad; AUM y flujos netos de ETF; uso on-chain; prestamistas regulados con LTV y coste razonables. Precio sin volumen = solo alerta técnica.
- **Contexto de timing (oct-2026):** con Fed 3,75-4,00 % y subiendo, 10 años al 5 % y Brent > $110, la regulación positiva puede no bastar a corto plazo.
- **Custodia:** separar autocustodia (resistente) de saldos en exchange y stablecoins (bloqueables); repartir el riesgo de plataforma.
- **Colateral:** LTV bajo, nunca toda la posición, reserva fuera del mismo activo y sin bloqueo; la liquidación forzosa tributa.
- **Salida:** tramos escritos, carpeta fiscal y AML lista, banco receptor avisado, varias rutas (exchange con licencia MiCA, OTC, más de una stablecoin) y reserva fiscal separada al vender.
- **XLM:** nombrado junto a XRP como *digital commodity* (17-mar-2026) [P]; mismos criterios (separar red, fundación y token; exigir uso real) y misma fiscalidad.
- Los planes personales de cartera no se copian aquí (repo público); siguen en el archivo histórico y en `privado/`.

## Fiscalidad en España
**Cripto**
- Vender, permutar (también XRP → USDC/USDT) o pagar con cripto genera ganancia o pérdida patrimonial en la base del ahorro (Modelo 100), coste por FIFO (art. 37.2 LIRPF).
- Escala del ahorro: 19 % hasta €6.000; 21 % hasta €50.000; 23 % hasta €200.000; 27 % hasta €300.000; 30 % por encima (tramo estatal art. 66 LIRPF + autonómico) [P: AEAT 2025] [VERIFICAR vigencia 2026 en el BOE consolidado].
- Préstamo con colateral cripto: entregar y recuperar el colateral no es transmisión; **la liquidación sí** tributa; los intereses no son deducibles (DGT V0648-24, vía despachos) [S] [VERIFICAR leyendo la consulta en petete].
- Staking: rendimiento del capital mobiliario (art. 25.2 LIRPF), valorado en euros el día de cobro [S]. Tokens LP de AMM y recompensas DeFi: sin criterio claro [VERIFICAR].
- Modelo 721 (cripto en el extranjero > €50.000) y DAC8 (datos desde 1-ene-2026, primera declaración en 2027): el proyecto de orden de mar-2026 reorganiza los modelos 172, 175 y 721; la ley de transposición de DAC8 no consta aprobada [VERIFICAR en el BOE].
- Impuesto de salida (art. 95 bis): no incluye criptomonedas ordinarias (DGT V0666-2025) [S].

**Patrimonio, residencia y territorio**
- Patrimonio en Cataluña: mínimo exento €500.000 (+ €300.000 vivienda habitual), sin bonificación general [S]; Solidaridad por encima de €3 M; tipos 0,2-3,5 %.
- Sucesiones en Cataluña: 99 % fijo solo para cónyuge/pareja estable; resto de Grupos I y II, bonificación decreciente del 99 % (hasta €100.000) al 20 % (más de €3 M) [P: atc.gencat.cat].
- Residencia fiscal (art. 9 LIRPF): más de 183 días, núcleo de intereses o presunción familiar; no se prorratea. España-Andorra tiene convenio de doble imposición (2016); la aplicación concreta a ganancias cripto requiere asesor [VERIFICAR].
- ITP de vivienda usada: Cataluña ver tabla; Madrid 6 %; C. Valenciana 9 % desde 1-jun-2026; Baleares 8-13 % por tramos [S].

## Dudas y datos a verificar
**Resueltas por C09 (26-oct-2026)** — ya integradas arriba: ITP joven en Cataluña, SEC-CFTC y XRP/XLM, base del −1,05 % de XRPN, cifra de adquisiciones con precio.

**Siguen abiertas (las cierra el lote W05 o la auditoría W08):**
- [VERIFICAR] Texto literal de la **sección 404** de CLARITY en congress.gov (hoy solo [S]). → W05
- [VERIFICAR] Precio y cierre de cada adquisición de Ripple sin precio publicado (Standard Custody, Palisade, Solvexia) y cierre de BC Payments Australia; cifras de Hidden Road, Metaco y Rail solo en prensa. → W05
- [VERIFICAR] Fecha de Palisade: 3-nov frente a ~4-nov-2025 (unificar con ripple.com). → W05
- [VERIFICAR] Cloture CLARITY 49-50 en fuente oficial (senate.gov). → W05
- [VERIFICAR] MEI 2026 leído en el propio BOE (hoy [S]). → W05
- [VERIFICAR] Vigencia 2026 de la escala del ahorro (art. 66 LIRPF) y texto definitivo de los modelos 172/175/721 y de DAC8 en el BOE. → W05
- [VERIFICAR] Consulta DGT V0648-24 leída en petete; fiscalidad de tokens LP de AMM.
- [VERIFICAR] El «Treasury al 5,34 %» del resumen W43 (casi seguro el 30 años, 5,33 %) y la cifra de Bloomberg sobre flujos de crudo frente a PortWatch. → W08 (cruce de resúmenes con series primarias)
- [VERIFICAR] Integración de Chainlink CCIP en producción en SWIFT.
