# Dossier: Stellar, tokenización (RWA) y DTCC (9-oct-2026)

> Informativo. No es recomendación de compra ni venta. Fuentes mayormente secundarias; las cifras de RWA cambian según quién las mida. Lo no confirmado va como [VERIFICAR]; las predicciones, como [ESPECULACIÓN].

## 1. Resumen ejecutivo
1. Los **activos tokenizados (RWA) en Stellar** han crecido mucho en 2026: de **~869 M$ a finales de 2025 a casi 4.000 M$ a finales de agosto** (+360 %, panel Dune de Stellar). Otra medida, rwa.xyz, daba **3.550 M$ distribuidos** el 7-oct. **Son métricas distintas**.
2. El crecimiento está **muy concentrado**: **Spiko = 1.550 M$ (~39 %)** y los **cinco mayores emisores suman ~93 %** (cálculo mío con datos de agosto).
3. **DTCC** conectará su servicio de tokenización a Stellar, con activos de DTC disponibles en la red en la **primera mitad de 2027**: es un plan anunciado, **no está en producción**.
4. **XLM no ha seguido el ritmo:** cotiza cerca de **0,18-0,19 $** y acumula **~-11 % en el año** (CoinGecko, según prensa). **Que crezcan los RWA no demuestra más demanda de XLM.**
5. Tres cosas que sí están confirmadas: el piloto de **U.S. Bank** (stablecoin USBDC, interno), la **tarjeta de MoneyGram** con stablecoin en Colombia y el **CCTP de Circle** en Stellar.

## 2. Qué son los RWA y por qué importan para Stellar
- Un **RWA** es un activo del mundo real (deuda pública, fondos monetarios, bonos) representado como token en una cadena. Stellar los aloja porque ofrece **liquidación rápida (3-5 s), comisiones mínimas (~0,00001 XLM)** y herramientas de cumplimiento (congelar, recuperar, KYC) que piden los bancos.
- **Importante:** la mayoría son redes con permisos (solo clientes verificados). Que existan no significa que se **compre XLM**: el XLM se usa para comisiones y como puente, y esas comisiones son minúsculas.

## 3. Cifras (con su matiz)
| Dato | Valor | Fuente / matiz |
|---|---|---|
| RWA tokenizados en Stellar (Dune/SDF) | **3.996 M$** a 29-ago-2026 (+360 % YTD; 868,8 M$ a finales de 2025) | [Cointelegraph](https://cointelegraph.com/news/stellar-tokenized-rwa-market-nears-4b-after-fourfold-2026-growth), secundaria |
| RWA "distribuidos" según rwa.xyz | **3.550 M$** a 7-oct (+6,9 % en 30 días) | Sesión de research; otra métrica y fecha [VERIFICAR en rwa.xyz] |
| Spiko | 1.550 M$ | Datos de agosto |
| Realiz / Tradable / Franklin Templeton / Ondo | 559 / 548 / 546 / 535 M$ | Datos de agosto |
| Deuda pública no estadounidense | ~490 M$ (CETES mexicanos, bonos brasileños vía Etherfuse) | SDF citando rwa.xyz |
| Crecimiento semanal de RWA (RWA Foundation, 4-oct) | +36,4 M$ en Stellar, 62 % del total de 10 cadenas | Secundaria |
| XLM en el año | ~-11 % (cerca de 0,18-0,19 $) | CoinGecko, vía prensa |

**Discrepancias a tener en cuenta:** una página tiene un error tipográfico (8.688 M$ en vez de 868,8 M$) y la RWA Foundation daba 3.000 M$ acumulados en julio con otro método. Siempre hay que mirar **qué mide cada cifra** (distribuido o representado).

## 4. Hitos de 2026
| Fecha | Hito | Estado |
|---|---|---|
| 6-may | Protocolo 26 "Yardstick" (congelar claves comprometidas, aritmética más segura) | Secundaria (Nansen) |
| 19-may | **CCTP de Circle** en Stellar (USDC nativo entre cadenas) | Secundaria |
| May | **DTCC** anuncia que conectará su servicio de tokenización a Stellar (1S 2027) | Nota de DTCC, citada por prensa |
| 10-sep | **MoneyGram + Rain:** tarjeta Visa con USDC empezando en Colombia | [The Block](https://theblock.co/news/business/2026-09-10-moneygram-card-stablecoin-visa-colombia-414137) |
| 1-oct (aprox.) | **U.S. Bank:** piloto interno de su stablecoin USBDC (sin clientes ni fecha comercial) | Cointelegraph y nota del banco |
| 18-jun / 8-jul | Protocolo 27 "Zipper": testnet 18-jun y votación prevista 8-jul | No he confirmado si salió a producción [VERIFICAR] |

## 5. DTCC: tres plazos distintos (no son contradictorios)
| Producto | Plazo |
|---|---|
| Servicio de tokenización de DTC | Octubre de 2026 (tras pilotos de julio) |
| Collateral AppChain (con Chainlink, sobre Besu) | 4T de 2026 |
| **Activos de DTC en la red Stellar** | **1S de 2027** |
El "retraso a 2027" que se oyó en un vídeo **no está confirmado**; es otro producto.

## 6. Riesgos y matices
- **Concentración:** un emisor pesa casi 40 % y cinco, el 93 %; si uno se va, la cifra baja mucho.
- **Métricas distintas:** "4.000" y "3.550" no son comparables sin saber qué cuentan.
- **Redes con permisos:** que el activo sea tokenizado no implica que el público lo use ni que se mueva con XLM.
- **XLM por detrás:** el precio no ha reaccionado; los artículos que dicen lo contrario son de baja calidad.
- **Piloto no es adopción:** USBDC es interno; la entrevista a Stellar es una **voz interesada**.
- **Compañía del canal:** parte de la información de vídeos viene de un solo canal con posición en XLM.

## 7. Escenarios [ESPECULACIÓN]
| Escenario | Qué pasaría | Señales |
|---|---|---|
| **A. La tokenización escala** y se diversifica | Más emisores y volumen, aunque el XLM siga sin reaccionar | Menos peso de Spiko; DTCC en producción en 1S 2027 |
| **B. Se estanca o se concentra aún más** | Cifras estables, dependientes de 2-3 emisores | Caída de emisores o de saldo distribuido |
| **C. Los RWA crecen y XLM empieza a reflejar uso** | Más actividad en pagos con XLM como puente | Más volumen de pagos con XLM, no solo emisiones |

## 8. Qué implica para XLM (sin consejos)
Es positivo para el **ecosistema**, pero la demanda de **XLM** depende de que el XLM se use como puente o para comisiones, y eso **no está demostrado**. Hoy XLM figura entre los commodities digitales de la interpretación SEC-CFTC de marzo (lista oficial de 16 activos, fuente primaria en sec.gov).

## 9. Qué vigilar
rwa.xyz y el panel de Stellar (con la misma métrica en cada comparación), nuevos emisores y la caída o subida de Spiko, el estado de DTCC en Stellar (1S 2027), la producción de USBDC y la actividad en pagos con XLM.

## 10. Lo que no sé
La cifra actual de RWA por emisor, el estado exacto del Protocolo 27, los validadores de nivel 1 (MoneyGram, Figure, Range) con fuente oficial y el efecto real en la demanda de XLM.
