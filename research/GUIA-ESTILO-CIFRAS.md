# Guía de estilo: cifras y monedas en el Explorador y los paneles (21-oct-2026)

Objetivo: que se vea siempre de qué moneda y de qué magnitud es una cifra. Aplica a `explorador/datos.json`, `explorador/regulacion.json`, `eventos/calendario.toml`, `paneles.json` y al código de `mapa.html` y `paneles.html`.

## Monedas (símbolo delante, sin espacio)
| Moneda | Símbolo | Ejemplo |
|---|---|---|
| Dólar de EE. UU. | `$` (`US$` cuando en la misma frase hay otros dólares) | `$2.000 M` |
| Euro | `€` | `€50.000` |
| Libra esterlina | `£` | `£1 M` |
| Yen japonés | `¥` | `¥1 M` |
| Yuan chino (RMB) | `CN¥` | `CN¥16,7 billones` |
| Won coreano | `₩` | `₩5.000 M` |
| Rupia india | `₹` | `₹1.000` |
| Real brasileño | `R$` | `R$35.000` |
| Rublo | `₽` | `₽30 M` |
| Dólar de Singapur / Hong Kong | `S$` / `HK$` | `S$10 M` |
| Rupia indonesia | `Rp` | `Rp23,16 billones` |
| Franco suizo, dirham de los EAU, rand | `CHF`, `AED`, `R` | (código, sin símbolo propio) |

## Magnitudes
- `M` = millones (`$954 M`). `mil M` = miles de millones (`$306 mil M`). No usar `MM`, `MM$` ni `B` (en español «billón» son 10^12 y «MM» es ambiguo).
- Se pasa a `mil M` desde 10.000 M (`$39,3 mil M`); por debajo se deja en `M` (`$2.000 M`).
- Tasas y precios: `$126 por barril`, `3,75–4,00 %` (espacio antes de `%`).
- Separadores españoles: punto para miles y coma para decimales; en pantalla se fuerza el punto de miles también en 4 cifras (`9.332`).

## Cómo se aplicó
- Los textos antiguos se convirtieron con `scripts/normalizar_monedas.py` (`python scripts/normalizar_monedas.py prueba` muestra los cambios; `aplicar` los escribe) (regla segura: solo patrones `M$`, `MM$`, `USD`, `R$`, `KRW`, etc.). Lo nuevo se escribe ya en este formato.
- Los símbolos de token (USDT, USDC, RLUSD) no son monedas: se dejan como están.
