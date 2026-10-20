# Radar regulatorio v4: de [S] a [P] con fuente oficial (2026-10-20)

Actualiza `explorador/regulacion.json` (112 celdas) y una cifra de `explorador/datos.json`. Búsquedas web, páginas y documentos oficiales; sin API de Anthropic. Informativo, sin recomendaciones de compra/venta. Niveles: [P] / [S] / [VERIFICAR] / [ESPECULACIÓN].

## Resumen (6 líneas)
1. **6 celdas pasan de [S] a [P]:**
   - Rusia: ley marco y custodia.
   - Brasil: ley marco y custodia.
   - India: CBDC.
   - Emiratos: ley marco.
   Además, Rusia · stablecoins pasa de «sin dato» a etapa 4 [P].
2. **Brasil:** el Voto 107/2026 del Banco Central (leído entero) confirma que **octubre de 2026** es el plazo final de la Res. 520 para que los proveedores existentes pidan autorización. Sustituye al cálculo propio «≈ 30-oct» [VERIFICAR] de R03P.
3. **Corea:** se queda en [S]. La FSC no tiene nota sobre los proyectos de ley de activos digitales ni del won stablecoin; solo menciona la ley de stablecoins como «pendiente» en la hoja de ruta de tokenización y en la agenda antiblanqueo de KoFIU.
4. **Egipto, Etiopía e Irán:** ninguno llega a 3 celdas fiables y siguen en «huecos», ahora con lo encontrado.
5. **MiCA:** sigue sin guía de la Comisión sobre la multi-emisión. El CSV oficial de ESMA de hoy da **376 entidades** y **194 con custodia**, frente a las 215 de R44. La discrepancia queda abierta.
6. **GENIUS:** la norma final de la OCC **sigue sin publicarse** a 20-oct-2026. El script de calidad pasa con el único aviso conocido.

## Cambios (antes → después)
| Celda | Antes | Después | Fuente |
|---|---|---|---|
| Rusia · ley marco | 4 [S] | 4 **[P]**: Duma 21-jul, Consejo de la Federación 24-jul, firma 4-ago y vigor 1-sep-2026. Pagos con cripto prohibidos salvo comercio exterior; desde 1-jul-2027 solo a través de organizadores | publication.pravo.gov.ru, kremlin.ru, cbr.ru (extractos) |
| Rusia · custodia | 4 [S] | 4 **[P]**: depositarios digitales regulados; sin transferencias directas entre particulares ni a monederos no custodiados (desde 1-jul-2027) | kremlin.ru, cbr.ru |
| Rusia · stablecoins | Sin dato | **4 [P]**: la ley no define «stablecoin»; las extranjeras son monedas digitales o «instrumentos digitales extranjeros» | cbr.ru (página del mercado cripto) |
| Brasil · ley marco | 4 [S]; plazo ≈ 30-oct [VERIFICAR] | 4 **[P]**: plazo de autorización en **octubre de 2026** (Res. 520) | Voto 107/2026 del BCB (PDF leído entero) |
| Brasil · custodia | 4 [S] | 4 **[P]**: desde el 1-oct-2026, aviso al Coaf de transferencias de 10.000 US$ o más a monederos autocustodiados (propuesta del voto) | Voto 107/2026 |
| Brasil · stablecoins | 4 [S] | 4 [S]: se confirma la Res. 584 (7-ago-2026) [P], pero **la Res. 561 no se localiza** en bcb.gov.br | Voto 107/2026 |
| India · CBDC | 1 [S] | 1 **[P]**: el e₹ sigue en piloto (preguntas frecuentes del RBI, 1-oct-2026); la cifra del −24 % sigue [S] | rbi.org.in; el PDF del Informe Anual pide **captcha** (no se esquivó) |
| Emiratos · ley marco | 5 [S] | 5 **[P]**: el Decreto-Ley 6/2025 cubre tokens de pago y DeFi; el art. 184 da un año de adaptación prorrogable; sin prórroga publicada | rulebook.centralbank.ae, uaelegislation.gov.ae |
| UE · custodia | 215 entidades [P] (R44) | **194** entidades con custodia [P] (CSV del 20-oct, actualizado el 15-oct); diferencia con R44 [VERIFICAR] | esma.europa.eu, CASPS.csv (descargado y contado) |
| UE · ley marco | — | Hito: 376 entidades en 379 filas, 3 con fecha de autorización futura | Igual |
| UE · stablecoins | Guía de multi-emisión pendiente | Sigue pendiente; la Comisión «trabaja en ella»; la JERS y el BCE piden salvaguardas | BBVA, Reed Smith, Ledger Insights [S] |
| EE. UU. · stablecoins | Norma final de la OCC pendiente | Sigue pendiente a 20-oct (objetivo «fin de octubre») | KuCoin, GN Crypto, ICBA [S] |
| datos.json · cifra de custodia | 215 | 194, con nota de la diferencia [VERIFICAR] | Igual que UE · custodia |

**Celdas de [S] a [P]: 6.** De «sin dato» a [P]: 1 (Rusia · stablecoins).

## Por qué otras celdas no suben a [P]
- **Corea (stablecoins, ley marco, ETF, custodia):** fsc.go.kr no tiene nota sobre los proyectos de ley; los datos vienen de prensa coreana.
- **India (stablecoins, ley marco, fiscal):** sin documento oficial del RBI ni del Ministerio de Finanzas leído; incometax.gov.in daba 403 en R35.
- **Brasil (tokenización, CBDC, fiscal):** sin comunicado del BCB, la CVM ni la Receita localizados; bcb.gov.br sirve páginas sin texto.
- **Emiratos (fiscal):** la FTA no tiene guía de activos virtuales (R35).

## Contradicciones entre fuentes
- **ESMA:** 215 entidades con custodia (R44, 17-oct) frente a 194 (CSV de hoy). R44 pudo contar otro campo o usar otra versión del registro. Hay que recontar con el mismo método [VERIFICAR].
- **Brasil:** el «≈ 30-oct» de R03P y del calendario era un cálculo de 270 días; el BCB habla de «octubre» sin día. El calendario sigue en 30-oct como aproximado.
- **Irán:** una sola fuente (Wikipedia) habla de una prohibición total en dic-2025; no se usa.
- **Etiopía:** las fechas de los bloqueos de mayo y junio-2026 no coinciden entre medios.

## Sigue [VERIFICAR]
- Norma final de la OCC.
- Prórroga del CBUAE.
- Texto de la Res. 561.
- Tabla del e₹ (captcha).
- Recuento de custodia en ESMA (215 o 194).
- Proyectos de ley coreanos.
- Guía de la Comisión sobre multi-emisión.
- Egipto, Etiopía e Irán.

## Páginas que no abrieron
- rbidocs.rbi.org.in: captcha.
- bcb.gov.br (nota 2639): página sin texto.
- normativos.bcb.gov.br: sí sirvió el PDF.
- consilium.europa.eu: 403 (ya anotado en v3).

## Fuentes
[publication.pravo.gov.ru (282-ФЗ)](http://publication.pravo.gov.ru/document/0001202608040007) · [kremlin.ru (282-ФЗ)](http://www.kremlin.ru/acts/bank/53543) · [cbr.ru (mercado cripto)](https://www.cbr.ru/develop/cryptocurrency/) · [BCB, Voto 107/2026](https://normativos.bcb.gov.br/Votos/BCB/2026107/Voto_do_BC_107_2026.pdf) · [BCB (nota 2639)](https://www.bcb.gov.br/en/pressdetail/2639/nota) · [RBI, preguntas frecuentes del e₹](https://www.rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=3686) · [RBI, Informe Anual 2026](https://rbidocs.rbi.org.in/rdocs/AnnualReport/PDFs/0AR29052026F5B979AF274E445ABB1593EB226906335.PDF) (captcha) · [CBUAE, Decreto-Ley 6/2025](https://rulebook.centralbank.ae/en/rulebook/federal-decree-law-no-6-2025-regarding-central-bank-regulation-financial-institutions-and) · [UAE Legislation](https://uaelegislation.gov.ae/en/legislations/3284/download) · [FSC (hoja de ruta y KoFIU)](https://www.fsc.go.kr/eng/pr010101/86222) · [ESMA, CASPS.csv](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv) · [BBVA (MiCA)](https://www.bbva.com/en/economy-and-finance/one-year-of-mica-the-market-in-figures-and-the-challenges-ahead/) · [Reed Smith](https://www.reedsmith.com/our-insights/blogs/viewpoints/102luce/eu-third-country-stablecoin-multi-issuance-schemes-under-micar/) · [Ledger Insights](https://www.ledgerinsights.com/eu-commission-opens-mica-review-takes-aim-at-multi-jurisdiction-stablecoins) · [GN Crypto (OCC)](https://www.gncrypto.news/news/occ-targets-october-end-for-genius-act-stablecoin-rules/) · [ICBA (OCC)](https://www.icba.org/w/comptroller-genius-act-final-rule-will-be-out-by-november) · [Andersen Egipto](https://eg.andersen.com/legality-cryptocurrency-in-egypt/) · [Ahram (CBE)](https://english.ahram.org.eg/News/572566.aspx) · [Launchbase Africa (Etiopía)](https://launchbaseafrica.com/2026/07/23/from-binance-unblocks-to-total-ban-ethiopia-targets-crypto-wallets-in-expanding-digital-asset-ban/) · [Willkie (OFAC e Irán)](https://complianceconcourse.willkie.com/articles/ofac-designates-irans-largest-digital-asset-exchanges/)
