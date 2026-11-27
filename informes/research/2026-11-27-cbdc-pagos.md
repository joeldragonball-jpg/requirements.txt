# CBDC y pagos transfronterizos (27-nov-2026)

Alcance: euro digital, e-CNY, mBridge, Agorá, SWIFT, pagos transfronterizos (Ripple, Stellar, Wise, Visa/Mastercard), CBDC de India/Brasil/Rusia. Sin recomendaciones. Búsqueda web del 27-nov-2026; las páginas oficiales de ECB solo se leyeron en parte (ver «Bloqueos»). Marcas: [S] = fuente secundaria/no oficial, [VERIFICAR], [ESPECULACIÓN].

## 1. Euro digital (BCE / UE)

HECHOS (fuente oficial, ecb.europa.eu, página «progress», leída 27-nov-2026):
- Fase de preparación: nov-2023 a oct-2025. El 30-oct-2025 el Consejo de Gobierno pasó a la fase siguiente (preparación técnica, diálogo con el mercado, apoyo al proceso legislativo).
- Si los colegisladores adoptan el reglamento en 2026, el euro digital podría emitirse en 2029. La decisión de emitir llega solo tras acabar el proceso legislativo.
- Hitos previos: informes de progreso 24-jun-2024, 2-dic-2024, 16-jul-2025; informe de cierre 30-oct-2025.

HECHOS (fuentes secundarias, [S]):
- Consejo de la UE adoptó su posición negociadora el 19-dic-2025 (Eunews).
- Comisión ECON del Parlamento Europeo aprobó su posición el 23-jun-2026 por 43 a 14 y 1 abstención (CoinDesk, FinanceFeeds) [S].
- Pleno: la apertura de negociaciones se confirmó el 8 o 9-jul-2026 (las fuentes discrepan; una cifra citada: 416-169-22) [S] [VERIFICAR].
- Primer trílogo político: 13-jul-2026; temas abiertos: límites de tenencia y modelo de compensación (Betaalvereniging, Freshfields) [S].
- Límite de tenencia: sin cifra acordada. Según el borrador, el BCE recomienda un tope y el Consejo lo fija mediante decisión de ejecución; si el Consejo no la adopta, el BCE puede fijarlo. Varios Estados piden límite cero para personas jurídicas y autónomos; DIGITALEUROPE (4-ago-2026) defiende el cero para empresas. Cifras que circulan para particulares: entre 1.500 y 3.000 € (el BCE ha modelado hasta 3.000 €) [S] [VERIFICAR].
- Piloto de 12 meses: una fuente lo sitúa en el 2.º semestre de 2027 [S] [VERIFICAR]; la página del BCE leída no da fechas.
- Septiembre 2026: MLex indica que las comisiones siguen en discusión [S].
- No encontré acuerdo final de trílogo ni comunicado oficial de noviembre de 2026. Estado actual: [VERIFICAR] en europarl.europa.eu (procedimiento legislativo) y consilium.europa.eu.

Relación con el BCE mayorista (BCE, nota de 27-may-2026): lo aprendido en Agorá alimenta la iniciativa Pontes (enlazar plataformas DLT de mercado con TARGET), con puesta en marcha prevista en sept-2026 [S vía buscador; comprobar en ecb.europa.eu] [VERIFICAR] si ya está operativa.

## 2. Proyecto Agorá (BIS)

HECHOS (bis.org, vía buscador):
- 27-may-2026: informe principal del BIS Innovation Hub. Conclusión: es posible la liquidación atómica transfronteriza mayorista con reservas tokenizadas de bancos centrales y depósitos tokenizados de bancos comerciales; la tokenización no cambia la naturaleza jurídica de ambos.
- Prueba con valor real (jul-2026, según la página del proyecto): 28 instituciones financieras y bancos centrales de Asia, Europa y Norteamérica, unos 800.000 CHF en total; tiempo medio de iniciación a liquidación ~80 segundos, sin integrar con RTGS ni sistemas centrales. El Banco de Canadá se une. Es un prototipo exploratorio, no producción.
- Discrepancia: la nota de mayo trataba la prueba real como paso futuro y la página la da por hecha en julio. [VERIFICAR] leyendo bis.org/project/agora.

## 3. e-CNY y mBridge

- mBridge: más de 55.000 M$ de volumen acumulado y ~95 % en e-CNY (Reuters vía The Block/Cointelegraph, ene-2026) [S]. Bancos centrales participantes citados: China, Hong Kong, Tailandia, EAU, Arabia Saudí. El BIS salió del proyecto en 2024 [VERIFICAR con bis.org].
- Centro operativo internacional de e-CNY en Shanghai (lanzado sept-2025 según Atlantic Council) [S]; otra fuente de baja calidad lo describe como planificado, [VERIFICAR].
- 16-jun-2026: 26 instituciones firmaron acuerdos de participante directo con el centro de Shanghai para CBETS, plataforma de liquidación transfronteriza distinta de mBridge (CoinGeek) [S].
- 1-ene-2026: el e-CNY pasa a un marco de «depósito digital» en el que los bancos pagan intereses (The Block) [S] [VERIFICAR con PBoC].
- Dudas: el Atlantic Council cuestiona cuánta demanda extranjera real hay. SCMP: un banco ve +176 % de clientes corporativos mBridge en el 1.º semestre [S].
- [ESPECULACIÓN] Que esto reduzca el uso del dólar en liquidación es hipótesis, no dato.

## 4. SWIFT

- Sept-2025: anuncia un libro mayor compartido basado en blockchain; prototipo con Consensys; registrará, secuenciará y validará transacciones con datos de cumplimiento en ISO 20022 (swift.com, vía buscador).
- Mar-2026 (actualización de Swift): diseño completado, se construye la primera iteración; MVP con transacciones reales previsto en 2026. Jul-2026: trabaja con más de 40 instituciones (swift.com) [S vía buscador].
- Sin resolver: infraestructura (Linea, capa 2 de Ethereum, según BeInCrypto, frente a Hyperledger Besu según KuCoin). Un agregador afirma 17 bancos en piloto vivo sin fuente primaria. [VERIFICAR] en swift.com si el MVP ya está en producción.
- Relevancia ISO 20022: el estándar es el vínculo con la tesis de Joel; aquí solo consta que el libro mayor integra datos ISO 20022. No se infiere nada sobre XRP/XLM.

## 5. Pagos transfronterizos privados

- Ripple: 3-mar-2026 amplía Ripple Payments (pila completa de stablecoins: cobro, custodia, conversión, pago); la empresa dice >100.000 M$ procesados (ripple.com) [dato de empresa, sin auditar]. Jun-2026: ampliación con Bitso (MXNB y RLUSD, corredor EE. UU.-México) [S].
- Stellar: 5.500 M$ de volumen de pagos en el 1.T-2026, +72 % interanual [S]; MoneyGram lanzó MGUSD en Stellar en jun-2026 [S].
- Wise: no encontré anuncio propio de 2026; solo mención genérica de su interés en stablecoins (Activant Capital, 1.T-2026) [S].
- Mastercard: 3-jun-2026 añade liquidación con stablecoins regulados (USDC, RLUSD, PYUSD, USDG, USDP, SoFiUSD, según una fuente; ocho cadenas incluida XRPL) [S] [VERIFICAR] en mastercard.com. Compra de BVNK cerrada el 3-ago-2026 (hasta 1.800 M$ según una fuente) [S].
- Visa: ritmo anualizado de liquidación en stablecoins >20.000 M$ (8-sep-2026), >160 programas; producción sobre todo en Solana [S]. Una cifra de 25.000 M$ procede de una fuente débil (GitHub); no usar.
- 23-nov-2026: piloto B2B transfronterizo OCBC/StraitsX, solo titular [VERIFICAR].
- Sesgo: casi todo viene de comunicados de las propias empresas y prensa cripto.

## 6. India, Brasil, Rusia

- India (RBI): e₹ minorista en circulación 771,66 crore ₹ a 31-mar-2026 frente a 1.016,46 crore un año antes (-24 %); e₹ mayorista, cero (informe RBI, vía Business Standard/Devdiscourse) [S]. Agenda FY27: explorar piloto CBDC transfronterizo bi/multilateral; conversaciones con MAS (Singapur) y EAU; participa en Rialto y Mandala (BIS Hub). Ensayo de depósito tokenizado iniciado (jun-2026) [S].
- Brasil (Drex): la infraestructura blockchain de las fases 1-2 se cerró el 10-nov-2025 y el proyecto se reorienta hacia garantías/colateral; el estado 2026 es contradictorio entre fuentes [S] [VERIFICAR] en bcb.gov.br.
- Rusia (rublo digital): despliegue obligatorio para los mayores bancos y grandes comercios desde el 1-sep-2026, resto hacia 2028 (Interfax y otros) [S]. Límite mensual de recarga para particulares citado: 300.000 RUB. Demanda débil según una fuente [S]. Piloto offline previsto otoño 2027 (Crowdfund Insider, nov-2026) [S]. Que haya acceso público amplio desde el 1-sep lo afirma una sola fuente [VERIFICAR] en cbr.ru.

## 7. Bloqueos y límites de este informe
- La página ecb.europa.eu «timeline» no traía fechas; «progress» sí (usada). Páginas de bis.org y swift.com solo vistas a través del buscador, no leídas enteras.
- Sin 403/CAPTCHA que anotar. Muchas cifras vienen de prensa secundaria.
- No se contrastó caso alcista/bajista con fuentes primarias para stablecoins; los volúmenes de Visa/Mastercard/Ripple son de las propias compañías.

## Lista [VERIFICAR]
1. Estado real del trílogo del euro digital y fecha prevista de acuerdo (europarl.europa.eu, consilium.europa.eu); si hay acuerdo sobre límite de tenencia.
2. Fecha del voto del pleno del PE (8 o 9-jul-2026) y resultado exacto.
3. Fecha de inicio y duración del piloto del euro digital (ecb.europa.eu/euro/digital_euro/pilot).
4. Cifra del límite de tenencia (1.500-3.000 €) y trato a personas jurídicas.
5. Pontes (BCE): ¿en producción desde sept-2026?
6. Agorá: prueba con valor real, fecha (mayo vs julio) y cifras (28 entidades, 800.000 CHF, ~80 s) en bis.org.
7. mBridge: volumen, participantes y salida del BIS; estado del centro de Shanghai; marco «depósito digital» del e-CNY.
8. SWIFT: ¿MVP en producción?; cadena (Linea vs Besu); número de bancos (17 vs 40+).
9. Mastercard: lista de stablecoins/cadenas (¿incluye XRPL?) y cifra de BVNK; Visa: 20.000 M$.
10. Ripple (>100.000 M$), Stellar (5.500 M$ 1.T-2026), MGUSD, Wise (sin dato), OCBC/StraitsX.
11. India: cifras e₹ en informe oficial del RBI; Brasil: estado de Drex 2026; Rusia: alcance real del despliegue del 1-sep y cifras de uso.
