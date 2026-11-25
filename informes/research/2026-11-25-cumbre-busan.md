# Cumbre Trump–Xi en Busan (30-oct-2025): entrada histórica para Cumbres

Fecha de lectura: 25-nov-2026. Entrada propuesta en `ent-busan.json` (id `busan-trump-xi-2025-10-30`). Sin recomendaciones.

## Qué se leyó
- [P] Casa Blanca, hoja informativa (1-nov-2025): compromisos de ambas partes. Leída con lector de páginas (resumen).
- [P] MFA China, lectura de la reunión (30-oct-2025): leída resumida, no literal [VERIFICAR].
- [P] Declaración de Trump en Truth Social (30-oct-2025) vía American Presidency Project: resumida.
- [S] Al Jazeera y Foreign Policy (30-oct-2025): leídas.
- [P] Hoja informativa de la cumbre de Pekín (17-may-2026): leída resumida.
- No leído: texto íntegro de la lectura china, nota del Ministerio de Comercio chino, datos USDA.

## Hechos [P]
- EE. UU.: -10 puntos del arancel de fentanilo desde el 10-nov-2025; suspensión hasta el 10-nov-2026 del aumento de aranceles recíprocos (sigue el 10 %); suspensión de un año de la regla de afiliadas y de las medidas de la Sección 301 marítima.
- China: suspende los controles de tierras raras del 9-oct-2025 y da licencias generales; suspende represalias arancelarias desde el 4-mar-2025; frena precursores de fentanilo; compras de soja (12 Mt a finales de 2025; 25 Mt al año 2026-2028, solo en la versión de EE. UU.); reabre Nexperia.
- Reunión de unos 100 minutos [S]. Chips de Nvidia y Taiwán: no se trataron (palabras de Trump, Al Jazeera).

## Tregua actual y visita a Pekín
- La tregua de Busan expiraba el 10-nov-2026. China anunció el 9-nov-2026 una prórroga de dos meses hasta el 10-ene-2027 [S, informe interno C225 del 17-nov-2026; primaria no leída].
- En Shenzhen (19-nov-2026) no hubo anuncio de prórroga ni de rebaja de aranceles.
- Visita de Trump a Pekín: mediados de mayo de 2026 (hoja informativa de la Casa Blanca del 17-may-2026: 200 Boeing, al menos 17.000 M$ anuales en compras agrícolas 2026-2028, «Junta de Comercio»). Fechas 14-15 may: [S] informe interno.

## Mercado (cierres diarios, precios_historico.json, nivel S)
| Activo | 29-oct | 30-oct | 3-nov | Var. 29→30 | Var. 29→3-nov |
|---|---|---|---|---|---|
| S&P 500 | 6.890,6 | 6.822,3 | 6.852,0 | -1,0 % | -0,6 % |
| VIX | 16,92 | 16,91 | 17,17 | -0,1 % | +1,5 % |
| Oro ($) | 4.000,7 | 4.015,9 | 4.014,0 | +0,4 % | +0,3 % |
| Brent ($) | 64,92 | 65,00 | 64,89 | +0,1 % | 0,0 % |
| DXY | 99,22 | 99,53 | 99,87 | +0,3 % | +0,7 % |
| Bono 10 años (%) | 4,058 | 4,093 | 4,106 | +3,5 pb | +4,8 pb |
| Bitcoin ($) | 110.055 | 108.306 | 106.548 | -1,6 % | -3,2 % |
| XRP ($) | 2,552 | 2,440 | 2,309 | -4,4 % | -9,5 % |
| XLM ($) | 0,316 | 0,299 | 0,278 | -5,5 % | -11,9 % |

Soja y CNH: no hay datos en el repo [VERIFICAR]. Hubo otras noticias esos días (p. ej. la Fed el 29-oct [VERIFICAR]): no se atribuye causa. Nota: la columna del bono 10 años en el JSON del explorador mostrará % relativo, no puntos básicos.

## Lecturas
- Alcista: arancel medio ~57 % a ~47 %, tierras raras suspendidas, compras agrícolas, canal abierto.
- Bajista: todo temporal y reversible, sin chips ni Taiwán, cifras de soja no confirmadas por China, palanca de tierras raras intacta.

## Sesgos
Hoja informativa unilateral de EE. UU.; Trump anuncia por Truth Social antes de que haya textos; la lectura china omite concesiones; 57 %/47 % son cálculos de prensa.

## Nota técnica para el visor
El visor de Cumbres usa `mercado.desde`/`dia` y el último dato de la serie (hoy sería 25-nov-2026). Para esta entrada conviene que use `mercado.hasta` (2025-11-03) como tercer punto. No se ha tocado `vistas.html`.

## Lecciones
Cotejar cifras de soja con la lectura china íntegra y con el USDA antes de darlas por cumplidas.
