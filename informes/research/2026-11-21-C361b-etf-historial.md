# C361b — Serie histórica de ETF de XRP/XLM (21-nov-2026)

Archivo: `explorador/etf-historial.jsonl` (una línea por fecha+ticker). Script: `scripts/etf_historial.py` (idempotente; sin IA). Uso diario: `PYTHONUTF8=1 python scripts/etf_historial.py` (añade el último punto de cada fondo de etf-flujos.json); siembra: `--todos --sec`.

## Nivel y límites
- **P** = dato leído en fuente primaria (web del emisor o SEC), pero el emisor es parte interesada y el 10-Q no está auditado. Los puntos SEC se leyeron por XBRL `data.sec.gov/api/xbrl/companyfacts/CIK##########.json` (consultado 21-nov-2026), no en el .htm del 10-Q; la fecha es la del cierre de periodo (31-dic-2025, 31-mar, 30-jun y 30-sep-2026).
- Los puntos de nov-2026 vienen de las webs de emisores ya volcadas en `etf-flujos.json` (ver su campo `fuente` y `nota`); algunos NAV y acciones tienen fechas distintas dentro de la misma web (ver notas del JSON).
- No hay cierres diarios históricos publicados en las webs (solo muestran el último día); entre trimestres no se inventa nada: huecos = sin dato. Flujo diario aún no calculable salvo entre días consecutivos de nov.
- `tenencia_monedas` solo donde el 10-Q da unidades cripto en XBRL (XRPZ, XRPC). Para XRP/TOXR/GXRP/GXLM queda null.
- Nota: en XRP (30-jun) y algunos 10-Q se citan reexpresiones en presentaciones posteriores; el accn de cada línea es el principal del dato, [VERIFICAR] si alguna cifra se reexpresó.

## Puntos por fondo (acciones | NAV | AUM USD | fecha)

### XRP (9 puntos)

| Fecha | Acciones | NAV | AUM USD | Monedas | Nivel/fuente |
|---|---|---|---|---|---|
| 2025-12-31 | 11,800,000 | 20.46 | 241,369,000 | — | P, SEC XBRL |
| 2026-03-31 | 17,420,000 | 15.03 | 261,855,000 | — | P, SEC XBRL |
| 2026-06-30 | 25,660,000 | 11.66 | 299,146,000 | — | P, SEC XBRL |
| 2026-09-30 | 36,990,000 | 16.62 | 614,850,000 | — | P, SEC XBRL |
| 2026-11-12 | 36,440,000 | 11.53 | 416,890,393 | 406,770,577.61 | P, web emisor |
| 2026-11-13 | 36,440,000.00 | 11.44 | 416,890,393.00 | 406,770,577.61 | P, web emisor |
| 2026-11-16 | 36,440,000.00 | 10.68 | 389,140,000.00 | 406,770,577.61 | P, web emisor |
| 2026-11-17 | 36,440,000.00 | 10.77 | 392,630,000.00 | 406,770,577.61 | P, web emisor |
| 2026-11-19 | 36,440,000.00 | 10.74 | 391,310,000.00 | — | P, web emisor |

### TOXR (9 puntos)

| Fecha | Acciones | NAV | AUM USD | Monedas | Nivel/fuente |
|---|---|---|---|---|---|
| 2025-12-31 | 13,890,000 | 17.83 | 247,658,271 | — | P, SEC XBRL |
| 2026-03-31 | 10,850,000 | 13.10 | 142,148,631 | — | P, SEC XBRL |
| 2026-06-30 | 11,110,000 | 10.16 | 112,916,689 | — | P, SEC XBRL |
| 2026-09-30 | 11,020,000 | 14.49 | 159,727,044 | — | P, SEC XBRL |
| 2026-11-13 | 11,000,000 | 9.98 | 109,770,671.56 | 107,073,960.56 | P, web emisor |
| 2026-11-16 | 11,000,000.00 | 9.32 | 102,477,649.44 | 107,073,960.56 | P, web emisor |
| 2026-11-17 | 11,000,000.00 | 9.40 | 103,349,306.45 | — | P, web emisor |
| 2026-11-18 | — | 9.40 | 103,379,823.89 | — | P, web emisor |
| 2026-11-20 | — | 8.67 | 95,325,354.05 | — | P, web emisor |

### XRPZ (6 puntos)

| Fecha | Acciones | NAV | AUM USD | Monedas | Nivel/fuente |
|---|---|---|---|---|---|
| 2025-11-23 | 100,000 | 24.40 | 2,440,079 | — | P, SEC XBRL |
| 2025-12-31 | 10,900,000 | 19.85 | 216,376,202 | — | P, SEC XBRL |
| 2026-03-31 | 14,700,000 | 14.63 | 215,061,670 | 159,659,740.02 | P, SEC XBRL |
| 2026-06-30 | 20,750,000 | 11.39 | 236,440,941 | 225,368,820.73 | P, SEC XBRL |
| 2026-09-30 | 27,000,000 | 16.28 | 439,606,153 | — | P, SEC XBRL |
| 2026-11-02 | 28,600,000 | — | — | — | P, SEC XBRL |

### XRPC (5 puntos)

| Fecha | Acciones | NAV | AUM USD | Monedas | Nivel/fuente |
|---|---|---|---|---|---|
| 2025-12-31 | 16,490,000 | 19.58 | 322,819,725 | 175,625,441 | P, SEC XBRL |
| 2026-03-31 | 18,540,000 | 14.28 | 264,767,022 | 197,214,584 | P, SEC XBRL |
| 2026-06-30 | 21,770,000 | 11.08 | 241,173,971 | 231,279,303 | P, SEC XBRL |
| 2026-09-30 | 23,350,000 | 15.79 | 368,656,616 | — | P, SEC XBRL |
| 2026-11-09 | 22,920,000 | — | — | — | P, SEC XBRL |

### GXLM (4 puntos)

| Fecha | Acciones | NAV | AUM USD | Monedas | Nivel/fuente |
|---|---|---|---|---|---|
| 2025-12-31 | 1,389,200 | 16.69 | 23,191,000 | — | P, SEC XBRL |
| 2026-03-31 | 1,398,200 | 14.01 | 19,596,000 | — | P, SEC XBRL |
| 2026-06-30 | 1,414,200 | 15.38 | 21,753,000 | — | P, SEC XBRL |
| 2026-09-30 | 1,440,900 | 18.63 | 26,848,000 | 118,504,621.50 | P, SEC XBRL |

### GXRP (9 puntos)

| Fecha | Acciones | NAV | AUM USD | Monedas | Nivel/fuente |
|---|---|---|---|---|---|
| 2025-12-31 | 6,300,100 | 35.45 | 223,364,000 | — | P, SEC XBRL |
| 2026-03-31 | 2,360,100 | 26.06 | 61,516,000 | — | P, SEC XBRL |
| 2026-06-30 | 2,840,100 | 20.22 | 57,413,000 | — | P, SEC XBRL |
| 2026-09-30 | 3,380,100 | 28.82 | 97,417,000 | — | P, SEC XBRL |
| 2026-11-13 | 3,000,100.00 | 19.78 | 59,343,931.00 | 58,060,446.31 | P, web emisor |
| 2026-11-16 | 2,720,100.00 | 18.48 | 50,271,127.00 | 52,640,033.69 | P, web emisor |
| 2026-11-17 | 2,720,100.00 | 18.72 | 50,922,796.00 | 52,639,528.93 | P, web emisor |
| 2026-11-18 | 2,660,100 | 18.70 | 49,758,550.00 | 51,477,911.91 | P, web emisor |
| 2026-11-20 | 2,660,100 | 17.16 | 45,637,279.00 | 51,476,924.66 | P, web emisor |

## Fuentes
- SEC EDGAR companyfacts: CIK 2039525 (Bitwise XRP), 2028835 (21Shares XRP/TOXR), 2059438 (Franklin XRP/XRPZ), 2039505 (Canary XRP/XRPC), 2037427 (Grayscale XRP/GXRP), 1761325 (Grayscale XLM/GXLM).
- Webs de emisores: bitwiseetfs.com, 21shares.com, etfs.grayscale.com (vía `etf-flujos.json`).
- SOL: solo se sembraron los puntos ya existentes en etf-flujos.json (1-3 por fondo); no se ampliaron en esta tarea.

## Pendientes
- Ampliar SOL por EDGAR igual que XRP.
- Enganchar `etf_historial.py` tras `leer_etf_flujos.py` en la rutina diaria (no hecho; no se tocan workflows).
- Si alguna web publica histórico diario descargable, rellenar entre trimestres.
