# Seguridad cripto, noviembre de 2026 (corte 27-nov-2026)

Metodología: búsqueda web y lectura de páginas. Los lectores resumen, así que las cifras y citas son [S] hasta cotejarlas en la página oficial. No se pudo abrir rekt.news ni DefiLlama directamente en esta pasada; no se intentó evitar bloqueos. CCN devolvió 403 (anotado, no evitado). Este documento no contiene recomendaciones.

## 1. Resumen

- El «hackeo de Binance» es REAL y está confirmado por Binance, pero ocurrió el 29-30 oct 2026, NO en noviembre. Sus efectos (congelaciones, blanqueo, reapertura de retiradas) se prolongan en noviembre. [P] (comunicado propio de Binance + FBI + firmas forenses)
- Importe perdido en noviembre (solo noviembre): CertiK, panel actualizado el 27-nov: 259,5 M$ brutos, 239,9 M$ ajustados, 58 incidentes, 19,6 M$ congelados o devueltos. Mes aún abierto, la cifra subirá. [D] Fuente: https://www-cn.certik.com/certik-report/dashboard (WebFetch 27-nov). Un resumen previo del mismo panel (21-nov) daba 231,6 M$ y 48 incidentes. [S]
- Sin la cola de Binance, noviembre es un mes «normal-alto». Octubre fue 6,48 mil M$ según PeckShield (56 hacks), casi todo Binance. Fuente: https://cryptonews.net/news/security/33697861/ [S]
- No encontré hackeo del XRPL ni de Stellar en noviembre. [VERIFICAR] (ausencia en búsquedas, no prueba).

## 2. Binance (hecho confirmado, fuera de noviembre)

Hechos según el informe preliminar de Binance (https://www.binance.com/square/post/384314395829022, leído por WebFetch 27-nov) [P]:
- Incidente el 30-oct-2026 (UTC+8); otras fuentes sitúan el inicio hacia las 20:05 UTC del 29-oct. Activos implicados: unos 6,34 mil M$. Salieron, entre otros, 233,46 M de XRP, ~970.500 SOL, 44,2 M de OP, 18.270 BTC y 2.961,9 ETH.
- Congelado o interceptado: ~2.850 M$, cifra aún en conciliación.
- Binance asume la pérdida (no los usuarios): según el informe, 98 % de los activos repuestos a 31-oct. Al Jazeera (1-nov): ~90 % repuesto, con SAFU de 1.000 M$, reserva en BTC, parte del fondo de seguros de futuros y tesorería. https://aljazeera.com/news/2026/11/1/fbi-blames-north-korea-for-record-6-3bn-crypto-heist
- Cadena de ataque (según Binance): instalador manipulado en junio, ingeniería social con falsa entrevista de trabajo en septiembre, herramienta de IA interna usada para llegar a otros equipos el 20-oct, ataque al servicio de firma el 30-oct. Se abusó de autorizaciones EIP-7702 maliciosas, que Binance revocó. Binance dice que el informe es preliminar y habrá revisión independiente. [P] por ser declaración propia; la veracidad completa de la causa está por contrastar.
- Atribución: Binance cita al FBI; el FBI (comunicado del sábado 1-nov, vía Al Jazeera) señala a Corea del Norte / TraderTraitor, que según cryptonews.net lo niega. TRM y Elliptic también lo atribuyen: https://www.trmlabs.com/resources/blog/binance-hack-update-north-korea-launders-proceeds-through-self-minted-tokens-and-chained-bridges y https://elliptic.co/insights/how-north-korea-is-laundering-the-6-4-billion-stolen-from-binance/ [D]
- Retiradas: reapertura por fases desde las 06:00 UTC del 1-nov. [S] (resumen de búsqueda del comunicado)
- Blanqueo (TRM, publicado 3-nov, modificado 17-nov): ~6,36 mil M$ salieron en diez cadenas; ~2.700 M$ congelados por Tether, Circle, Ripple, World Liberty Financial y el Arbitrum Security Council; el atacante conservaba ~2.400 M$ en ETH y BTC; usa tokens autoacuñados en TRON y swaps encadenados entre puentes. [D]
- Controversia: ICIJ recoge que Chainalysis dijo que el informe y la nota de prensa de Binance omitían categorías de delito, incluidos hacks. https://www.icij.org/investigations/coin-laundry/tracing-firms-say-binances-clean-up-claims-left-out-key-crime-stats/ [S] (solo titular y resumen).
- Discrepancias de cifra: 6,3 mil M$ (Binance co-CEO, FBI), 6,34 (informe), 6,36 (TRM), 6,43 (Elliptic). Diferencias por criterio de valoración. [D]

### Qué toca a XRP
- 233,46 M XRP salieron de monederos de Binance (informe de Binance, ~4,7 % del total según TRM vía agregadores, ~296 M$ al valor del momento). Fuentes agregadoras dicen que no se puede congelar el XRP nativo; Ripple congeló ~40,5 M RLUSD vinculados. https://coinstats.app/news/84b7c7d3cdc5237bf733169d4bcef1baccf6873753b61904bb1fb63467ad208f_Binance-hacker-spreads-23346-million-stolen-XRP-over-six-wallets-Ripple-has-no-power-to-freeze/ [S]
- Lo ocurrido es un robo de claves/infraestructura de Binance, no un fallo del XRP Ledger. Ninguna fuente leída apunta a vulneración del protocolo. [D] (inferencia de las descripciones; sin cotejo en explorador)
- Paradero actual de ese XRP: fuentes contradictorias (seis monederos vs. un único monedero). [VERIFICAR] en un explorador del XRPL.
- Posible riesgo de «bulo»: titulares que digan «el XRP se hackeó» mezclan el robo en Binance con el protocolo.

## 3. Hackeos de noviembre con fuente

| Fecha | Caso | Importe | Fuente y fiabilidad |
|---|---|---|---|
| 2-nov | Mercado Bitcoin (Brasil) | 38 M$ según la propia empresa; 46 M$ The Block; ~49 M$ trazados por Chainalysis en 17 cadenas | https://theblock.co/news/defi/2026-11-02-mercado-bitcoin-hack-46-million-brazil-exchange-432333 ; criptonoticias; CoinStats. Empresa confirmó el incidente y que cubrirá pérdidas. ~10-11 M$ congelados [S]. Vínculo con BitMart: no probado [ESPECULACIÓN]. Reapertura prevista 9-nov en solo lectura [S] |
| 16-nov | Multisig Safe vía Zodiac Roles | ~6,45 M$ (PeckShield), 6,44 M$ (Unchained) | https://cryptoticker.io/en/safe-multisig-zodiac-roles-theft-6-45-million/ ; parte pasó a Monero. [D] firma forense |
| nov (s/f) | «Institución financiera de Europa occidental» | ~130 M$ rastreados por ZachXBT; víctima sin identificar | cryptonews.net (resumen de octubre/nov). [S] [VERIFICAR] |
| nov (s/f) | Cryptio (brecha, infraestructura compartida) | sin importe | https://cryptonews.net/news/security/33815195/ solo titular. [VERIFICAR] |
| 24-26 nov | Reclamación de hackeo de monedero de Ansem; reembolsos Chainflip | sin datos | Solo titulares en la barra lateral de CryptoSlate. No hallé cobertura. [VERIFICAR] |

Nota: una búsqueda sobre «Chainflip 12 M$ en noviembre» no halló nada; el incidente de Chainflip hallado es de septiembre (736.442 USDT en TRON). [D] https://crypto.news/chainflip-loses-736442-usdt-in-tron-exploit/ . No dar por cierto lo de noviembre.

## 4. Contexto del año (para escalar)
- CertiK hasta septiembre: ~2,68 mil M$ brutos, 658 incidentes; septiembre 766,5 M$ (PeckShield 766,49 M$, 55 incidentes; CertiK 768,4 M$, 97 incidentes: metodologías distintas). https://cryptoslate.com/crypto-hackers-have-taken-2-7-billion-in-2026-and-the-losses-are-alarmingly-concentrated/ [D]
- Mayores casos 2026 (CertiK): Bitget 387,5 M$, Liquid Network 318,7 M$, KelpDAO 291,3 M$, Drift 285,3 M$. [D]
- Corea del Norte: TRM dice 7.400 M$ robados en 2026 (12.800 M$ histórico). https://www.trmlabs.com/resources/blog/north-korea-has-stolen-usd-128-billion-in-crypto-usd-74-billion-of-it-in-2026 [D] según titular. Elliptic: >1.000 M$ en 51 incidentes hasta septiembre (antes de Binance). Con Binance, el peso norcoreano sube mucho. [D]
- Otras cifras de año completo circulan (8,78 mil M$ en 328 hacks; 9,2-9,57 mil M$ CertiK) y no cuadran entre sí. [VERIFICAR] antes de citar.

## 5. Lazarus / Corea del Norte en noviembre
- Actividad confirmada en noviembre: el blanqueo del botín de Binance (TRM, Elliptic, FBI). No encontré un hackeo NUEVO atribuido a Lazarus fechado en noviembre. [D] (ausencia en búsqueda)
- El FBI publicó direcciones sospechosas y pidió a los proveedores de activos virtuales que bloqueen transacciones (Al Jazeera, 1-nov). [S]
- Ojo: el hackeo de Upbit (~30 M$) y la atribución a Lazarus son de nov-2025, no de 2026. Algunos resultados se confunden con esa fecha.

## 6. Estafas y deepfakes
- Patrón recurrente, sin caso nuevo de nov-2026 hallado: vídeos deepfake de Brad Garlinghouse que prometen duplicar XRP si se envía a una dirección (primer caso nov-2023; variante 2025 de «100 M XRP» desmentida por David Schwartz). Ripple: nunca pide enviar fondos. https://cryptoslate.com/ripple-ceo-brad-garlinghouse-warns-of-deepfake-scams-targeting-the-xrp-community/ [D] histórico; [VERIFICAR] si hay oleada actual.
- Cuentas de X hackeadas que difunden falsas alianzas (caso Watcher Guru, 21-mar-2025, falso acuerdo SWIFT-Ripple). https://invezz.com/news/2025/03/21/watcher-guru-x-account-hacked-false-xrp-swift-claim-spreads-across-platforms/ [D] histórico.
- Bulos recurrentes de XRP: «SWIFT integra XRP», «650 billones fluirán al XRPL», «ISO 20022 = XRP». Un ex desarrollador de Ripple dice que no hay nada de ISO 20022 en el código del XRPL (https://bitcoinist.com/xrp-iso-20022-complete-charade-ex-ripple-developer/) [S]. Sin fecha de nov-2026 confirmada.
- XLM: webs falsas de «recompensas Stellar», estafa de «1:5» para robar claves, falsos tokens PI en un supuesto DEX de Stellar (Prashu, suspendido). Sin comunicado de la SDF en 2026 hallado, y las fechas son inciertas. https://beincrypto.com/fake-pi-tokens-stellar-scam-rumors [S] [VERIFICAR]
- Aviso general a la comunidad XRP por oleada de estafas a usuarios de Xaman (titular, sin fecha verificada): https://cryptorank.io/news/feed/70623-xrp-community-hit-with-warning-amid-fresh-xaman-user-scam-wave [VERIFICAR]
- Ledger: usuarios que compraron dispositivos con spyware vía el revendedor CryptoBilis perdieron ~90 M$ (octubre; cryptonews.net). [S]

## 7. Hecho confirmado vs. rumor

| Afirmación | Estado |
|---|---|
| Binance sufrió un hackeo de ~6.300 M$ | Confirmado por Binance, FBI y firmas forenses; fecha 29-30 oct |
| Ocurrió en noviembre | Falso: fue a finales de octubre; la reapertura y el blanqueo son de noviembre |
| Fondos de usuarios perdidos | Binance dice que no (cubre con fondos propios) [P] declaración de parte interesada |
| Fue Lazarus/Corea del Norte | Atribución del FBI y de TRM/Elliptic; el grupo lo niega. Alta, no judicial [D] |
| El XRPL fue hackeado | No hay evidencia; el XRP robado era de Binance |
| Binance «quebró» | Sin base en lo leído; PoR 1:1 publicado según Al Jazeera [S] |
| Mercado Bitcoin conectado con BitMart | Rumor [ESPECULACIÓN] |

## 8. Sesgos
- Binance es parte interesada: minimiza riesgo para el usuario y cita al FBI. CertiK y PeckShield difieren por metodología y por contar o no estafas. Agregadores (CoinStats, tech-insider, edgeX) amplifican sin fuente primaria. El panel de CertiK mezcló cifras en una lectura (231,6 M$ frente a 6,41 mil M$ de octubre). Todo debe tomarse con cautela.

## Pendiente
Abrir CertiK/PeckShield a fin de mes; ver rekt.news y DefiLlama hacks en el navegador (ACCESOS-CHROME); explorador del XRPL para los 233,46 M XRP; informe final de Binance.

[VERIFICAR]
