---
tema: R23 Verificación SEC con curl (fuentes primarias)
etiquetas: [sec, regulacion, evernorth, xrp, xlm, verificacion]
actualizado: 2026-10-17
---
# R23: cierre de los [VERIFICAR] de la SEC (2026-10-17)

> Informativo. No es recomendación de compra ni venta. Todas las fuentes de abajo son **primarias leídas hoy** con `curl` + User-Agent identificado (sec.gov y federalregister.gov abren así; en R11P/R12P se dio por cerrado sin probar este método).

## Resultado en 5 líneas
1. **Interpretación SEC–CFTC (Rel. 33-11412, 17-mar-2026): CONFIRMADA y leída entera.** XRP **y Stellar (XLM)** figuran como ejemplos de *digital commodity* (texto literal en pág. 14). Cierra el [VERIFICAR] sobre Stellar del informe del 8-oct.
2. **Regulation Crypto Assets (S7-2026-27): CONFIRMADA** (Rel. 33-11434): firmada 18-ago, publicada en el Federal Register el 21-ago, **comentarios hasta el 20-oct-2026** (faltan 3 días). 5 M$ = *Startup Exemption*; 75 M$ = *Fundraising Exemption* (Tier 2; Tier 1 = 20 M$); "safe harbor" de *investment contract* es otra pieza.
3. **Propuesta de custodia (nota 2026-100, 1-oct): CONFIRMADA y CERRADA la fecha**: File S7-2026-35 (IA-7023 / IC-36353), publicada el **6-oct-2026**, **comentarios hasta el 7-dic-2026**. Sin mención de XRP/XLM.
4. **Evernorth (8-K y Form 425 en EDGAR): CONFIRMADO con cifras.** Cierre 9-oct, cotiza 12-oct. En especie se aportaron **388.910.554 XRP** (suma de las cinco partidas del 8-K); los "473 M" son de un 425 con fecha 31-dic-2025, **no** del 8-K.
5. **Hallazgo nuevo:** la CFTC publicó el 13-oct (FR) un *ANPRM* "Regulation Crypto Asset Transactions and Regulation Crypto Asset Markets", comentarios hasta el **14-dic-2026**. No estaba en el calendario.

## Tabla de verificación
| Archivo:línea | Afirmación | Resultado | Fuente (primaria) | Fecha |
|---|---|---|---|---|
| informes/2026-10-08-intradia.md:40 | XRP clasificado digital commodity (Rel. 33-11412) y **Stellar en la lista** [VERIFICAR] | **CONFIRMADO**: "Examples of digital commodities include … Stellar (XLM) … and XRP (XRP)" y nota 51: ejemplos elegidos porque tienen futuros en un mercado regulado por la CFTC; "no es necesario" tener futuros para serlo | [SEC 33-11412 (PDF, texto conformado al Federal Register)](https://www.sec.gov/files/rules/interp/2026/33-11412.pdf) pág. 14 | 17-mar-2026; efectiva 23-mar-2026 |
| dossiers/2026-10-09-etfs-cripto.md:48 | Efectiva 23-mar-2026; File | **CONFIRMADO** la fecha. **Matiz**: el File es **S7-2026-09** (no S7-2026-27, que es otra norma). Acción: "Final rule; interpretation; guidance" | ídem | 17-mar-2026 |
| cerebro …rusia-europa…:77 / R11P:27 / R12P:25 | Regulation Crypto Assets 18-ago, FR 21-ago, S7-2026-27, comentarios hasta 20-oct; 5 M$ Startup, 75 M$ Tier 2 | **CONFIRMADO** (era SECUND; ahora **PRIM-LEÍDA**). Sigue sin ser la "Innovation Exemption" | [SEC 33-11434 (PDF)](https://www.sec.gov/files/rules/proposed/2026/33-11434.pdf), [comunicado 2026-76](https://www.sec.gov/newsroom/press-releases/2026-76-sec-proposes-new-regulation-crypto-assets), [página S7-2026-27](https://www.sec.gov/rules-regulations/2026/08/s7-2026-27) | 18/21-ago-2026 |
| dossiers/2026-10-09-etfs-cripto.md:57 y cerebro …:71 | Propuesta de custodia 1-oct; comentarios 60 días desde FR (fecha **[VERIFICAR]**) | **CORREGIDO/CERRADO**: FR **6-oct-2026** (doc. 2026-20466); cierre **7-dic-2026**; S7-2026-35 | [SEC nota 2026-100](https://www.sec.gov/newsroom/press-releases/2026-100-sec-proposal-would-address-how-investment-advisers-funds-can-custody-crypto-assets-under-federal), [página S7-2026-35](https://www.sec.gov/rules-regulations/2026/10/s7-2026-35), [Federal Register 2026-20466](https://www.federalregister.gov/documents/2026/10/06/2026-20466/adviser-and-regulated-fund-custody-rules-crypto-custody-rules) | 1 y 6-oct-2026 |
| dossiers/2026-10-09-etfs-cripto.md:27 | "autocustodia solo como último recurso" | **MATIZ, SIGUE SIN VERIFICAR**: la nota oficial dice "permitir la autocustodia **en ciertas circunstancias**" y custodios fiduciarios estatales; "último recurso" **no aparece** en la nota. El texto de la propuesta (cientos de páginas) no se leyó | nota 2026-100 | 1-oct-2026 |
| videos/2026-10-07-evernorth…:52 | "Más de 473 M XRP" (Form 425) | **CONFIRMADO con matiz de fecha**: el 425 dice "over 473 million XRP … as of December 31, 2025", no "al cierre" del 9-oct | [Form 425 EDGAR](https://www.sec.gov/Archives/edgar/data/2092592/000095010326004974/dp244512_425.htm) | 2026 (cifra a 31-dic-2025) |
| evernorth-xrpn…:17 y R11P:32 | Cierre 9-oct, cotiza 12-oct; ~80,3 % de acciones públicas redimidas (~195 M$) | **CONFIRMADO** literal: 18.463.753 acciones SPAC, ~80,3 %, ~10,58 $/acción, ~195,39 M$; "began trading on Nasdaq on October 12, 2026" | [8-K EDGAR, CIK 2092592](https://www.sec.gov/Archives/edgar/data/2092592/000119312526419146/d24481d8k.htm) | 9-oct (fecha del evento y de la firma); presentado 13-oct según R22 |
| R13:66 | ~388 M XRP en especie; ~84 M comprados con dinero a ~2,54 $ | **CONFIRMADO lo en especie**: 388.910.554 XRP (ver desglose). Lo comprado con dinero (~84 M) es **resta mía** 473 M − 388,9 M; el precio de ~2,54 $ viene del S-4/A, **no está en el 8-K** | 8-K | oct-2026 |

## Desglose de XRP en especie (8-K, "Private Placements" y "Contribution Agreement")
| Partida | XRP | % de lo aportado en especie* |
|---|---|---|
| Sponsor (Serie C) | 211.319.096 | 54,3 % |
| Ripple (Contribution Agreement; 18.139.927 *Company Units*; precios revisados el 12-ago) | 126.791.458 | 32,6 % |
| Entidad relacionada del contribuyente | 50.000.000 | 12,9 % |
| Suscriptores de financiación adelantada | 600.000 | 0,15 % |
| Suscriptores de financiación diferida | 200.000 | 0,05 % |
| **Total en especie** | **388.910.554** | 100 % |

\*Cálculo mío. Precios de referencia del propio 8-K: **Signing XRP Price 2,36609 $**; **Closing XRP Price 1,43069 $** (media de 3 días del índice CME CF XRP-Dollar). Valor de los 388,9 M XRP: ≈ **556 M$** a 1,43069 $ frente a ≈ **920 M$** a 2,36609 $ (cálculo mío). Las partidas sumadas son 388,9 M, ≈ 82 % de los 473 M de la cifra de prensa/425 (el resto no figura en el 8-K).
Otros datos del 8-K: Ripple Labs Inc. posee 1.581.112 acciones Clase A (7,1 %); Arrington XRP Capital Fund, LP 19,9 % de la Clase A y 91,0 % de la Clase C (no voto); SBI Holdings 39,9 % de la Clase A. Es un **vehículo de tesorería, no un ETF**.

## Hechos vs. opiniones
- **Hechos:** textos literales de las normas y del 8-K, fechas del Federal Register, cifras de XRP en especie.
- **Interpretación (mía):** que Ripple aportó un tercio de lo aportado en especie y que el Sponsor más de la mitad significa que gran parte de la "demanda" de XRP de Evernorth no fue compra en mercado. Es coherente con R13 (T6), pero la parte comprada con dinero no se leyó aquí.
- **[ESPECULACIÓN]:** cualquier efecto de precio de estas normas. La clasificación como *digital commodity* es una **interpretación** de la SEC (no una ley); la propia nota 51 dice "a la fecha de este documento" y puede cambiar. CLARITY sigue bloqueada en el Senado (apertura 17-oct, secundaria).

## Caso alcista vs. bajista (lectura de las normas)
- Alcista: XRP y XLM nombrados como *digital commodity* por la SEC con CFTC; Regulation Crypto Assets y la custodia crean vías formales para ofertas y fondos.
- Bajista: son **propuestas** (comentarios abiertos hasta 20-oct y 7-dic); la interpretación no es ley y se puede revisar; la CFTC solo está en fase de *ANPRM* (14-dic); Evernorth compró ≈ 18 % con dinero según R13 y la acción cayó de la prima inicial.

## Sesgos de fuente
Los textos de la SEC y el 8-K son primarios; el 8-K lo presenta la propia empresa (parte interesada: Ripple es accionista). La nota 2026-100 incluye la cita del presidente de la SEC, que es opinión institucional, no dato.

## Qué sigue sin verificar [VERIFICAR]
- Texto de la propuesta de custodia (S7-2026-35): condiciones exactas de la autocustodia y fecha de cierre ya cerrada, pero no si menciona XRP/XLM (la nota no lo hace).
- Cifra de XRP **comprados con dinero** y su precio medio (S-4/A en EDGAR; no leído hoy).
- XRP totales que Evernorth tiene **tras el cierre** (el 8-K no da un total; solo el 425 con fecha 31-dic-2025).
- ANPRM de la CFTC (13-oct): solo leída su portada vía Federal Register; no si menciona XRP/XLM.
- Ediciones de archivo: no he modificado `informes/2026-10-08-intradia.md` (informe fechado); su etiqueta sobre Stellar queda superada por este informe.

## Cambios hechos en archivos existentes (diff)
1. `informes/dossiers/2026-10-09-etfs-cripto.md:57`: `(fecha de publicación [VERIFICAR])` → `(publicada en el Federal Register el 6-oct-2026; plazo hasta el 7-dic-2026; File S7-2026-35; verificado en R23)`.
2. `cerebro/documentos/fuentes-fiables-y-dudosas.md`: +1 línea (lección sec.gov/curl y Federal Register API).

## Fuentes (todas leídas hoy)
- [SEC 33-11412](https://www.sec.gov/files/rules/interp/2026/33-11412.pdf) · [SEC 33-11434](https://www.sec.gov/files/rules/proposed/2026/33-11434.pdf) · [2026-76](https://www.sec.gov/newsroom/press-releases/2026-76-sec-proposes-new-regulation-crypto-assets) · [2026-100](https://www.sec.gov/newsroom/press-releases/2026-100-sec-proposal-would-address-how-investment-advisers-funds-can-custody-crypto-assets-under-federal)
- [S7-2026-35](https://www.sec.gov/rules-regulations/2026/10/s7-2026-35) · [Federal Register custodia](https://www.federalregister.gov/documents/2026/10/06/2026-20466/adviser-and-regulated-fund-custody-rules-crypto-custody-rules) · [Federal Register CFTC ANPRM](https://www.federalregister.gov/documents/2026/10/13/2026-20888/regulation-crypto-asset-transactions-and-regulation-crypto-asset-markets)
- [8-K Evernorth](https://www.sec.gov/Archives/edgar/data/2092592/000119312526419146/d24481d8k.htm) · [Form 425](https://www.sec.gov/Archives/edgar/data/2092592/000095010326004974/dp244512_425.htm)
