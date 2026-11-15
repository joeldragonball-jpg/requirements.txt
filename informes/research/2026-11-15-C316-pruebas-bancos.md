# C316 · Pruebas y despliegues de bancos, bancos centrales, depositarias y gestoras por red (15-nov-2026)

Datos en `explorador/pruebas-bancos.json`. Neutral: inventario con fuente, sin recomendación ni ranking. Un piloto no es adopción. Niveles: P = página de la entidad (o de una parte) abierta y leída el 15-nov-2026; S = prensa o fuente no abierta; [VERIFICAR] = sin confirmar. No se tocó `privado/` ni otros JSON.

## HECHOS (por red, solo lo contado: banco, banco central, supranacional, depositaria o gestora)

| Red | Hechos P | Hechos S | Liquidación P / S | Entidades con hecho P |
|---|---|---|---|---|
| XRPL | 3 | 2 | 1 / 1 | DBS, Franklin Templeton, J.P. Morgan |
| Stellar | 3 | 2 | 0 / 0 | Franklin Templeton, DTCC, SG-FORGE |
| Ethereum | 5 | 4 | 3 / 0 | BEI, Banque de France, BlackRock, J.P. Morgan, SG-FORGE |
| Solana | 5 | 0 | 2 / 0 | J.P. Morgan, Franklin Templeton, DTCC, SG-FORGE, BlackRock |
| Hedera | 2 | 1 | 1 / 1 | Banco de Inglaterra, Apex Group |
| Avalanche | 1 | 3 | 0 / 0 | BlackRock |
| Polygon | 1 | 2 | 0 / 2 | BlackRock (el piloto MAS DBS/JPM/SBI es S para la cadena) |
| BNB Chain | 1 | 1 | 0 / 0 | BlackRock |
| Canton | 2 | 0 | 2 / 0 | DTCC, BNP Paribas |
| Algorand, Plume | 0 | 1 y 2 | 0 / 0 | solo S (VersaBank; UBS AM y WisdomTree) |
| XDC, IOTA | 0 | 0 | 0 / 0 | sin banco ni banco central con fuente |

Hechos de liquidación con fuente P (leídos):
- XRPL: reembolso transfronterizo de OUSG, activo en XRPL <5 s y pago en USD por Kinexys (6-may-2026, piloto; fuente: Ondo, parte del acuerdo).
- Ethereum: bono de 100 M€ del BEI en Ethereum pública con pago representado por CBDC del Banque de France (27-abr-2021, completado); JPM Coin en Base (L2), producción de acceso limitado.
- Solana: papel comercial de Galaxy tokenizado, entrega contra pago en USDC arreglado por J.P. Morgan (11-dic-2025, completado).
- Canton: operaciones de producción de DTCC (jul-2026) y servicio lanzado el 28-oct-2026; BNP Paribas como prestamista de valores.
- Hedera: desafío del Banco de Inglaterra y el BIS (oct-2025), sin resultados publicados.

Diversificación de divisas (moneda distinta del USD, P): EURCV de SG-FORGE (Ethereum, Solana; en Stellar y XRPL solo anuncio P y lanzamiento S); bono en EUR del BEI; CBDC piloto australiana (RBA; la cadena Hedera sale de S). Piloto de MAS Guardian con JPY y SGD: P para el piloto, S para la cadena (Polygon).

Fuera de todo recuento por no nombrar cadena pública: Swift (17 bancos, 9-jul-2026, P), Proyecto Mariana (BIS, Banque de France, MAS, SNB; "una cadena pública", P) y el trabajo exploratorio del Eurosistema 2024 (S).

## Contraste pedido (solo recuento, sin conclusión)
Liquidación con fuente P: Ethereum 3, Solana 2, XRPL 1, Stellar 0. Con S añadido: Ethereum 3, Solana 2, XRPL 2, Stellar 0. En lo hallado, Ethereum y Solana no tienen menos hechos de liquidación de bancos que XRPL y Stellar. Esto mide lo que comunican las entidades y lo que pude abrir; no calidad, volumen ni cuota. Varios hechos de XRPL son planes (DBS/Franklin) o pilotos de una operación.

## OPINIONES / lagunas [VERIFICAR]
- Sesgo de fuente: las gestoras (BlackRock, Franklin) y las fundaciones/cadenas publican sus propios comunicados; el hecho de liquidación de XRPL viene del blog de Ondo, no de JPMorgan.
- SG-FORGE en XRPL y Stellar: solo anuncios de 2024 y 2025 leídos; el lanzamiento (18-feb-2026 en XRPL) es S.
- MAS/Ripple BLOOM (25-mar-2026), cadenas de VersaBank (CADVB) y la cadena de Acacia (RBA no nombra Hedera) pendientes de fuente directa.
- No cargó el anexo del BCE (demasiado grande) ni páginas de varios bancos centrales; Bután, Montenegro, Georgia, Colombia y Palau se reutilizan de `cbdc-blockchains.json` (S).
- Lista no exhaustiva: busqué comunicados de entidades, no todos los bancos posibles (p. ej. HKMA Ensemble queda sin cadena identificada).

## Fuentes principales (todas leídas 15-nov-2026)
DBS (18-sep-2025) · Ondo (6-may-2026) · SG-FORGE (14-nov-2024; 20-feb-2025) · Stellar/Franklin · DTCC (27-may, 28-oct, 12-nov-2026) · Canton blog (8-sep-2026) · J.P. Morgan (11-dic-2025; Kinexys 11-may-2026) · BEI 2021-141 · BlackRock/Securitize (13-nov-2024; 14-nov-2025) · MAS (2-nov-2022) · RBA 2026-13 · Hedera/Banco de Inglaterra (28-oct-2025) · Visa (29-abr-2026) · Swift (9-jul-2026) · BIS/Banque de France (Mariana). URLs en el JSON.
