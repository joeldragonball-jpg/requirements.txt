# C260 · Indicadores de Países (14-nov-2026) — parcial

Lectura con Chrome de fuentes oficiales. Sin recomendaciones; solo hechos con fuente y fecha.

| País | Indicador | Resultado | Nivel |
|---|---|---|---|
| Reino Unido | IPC (ONS, serie D7G7) | 3,5 % interanual en sep-2026 (ago 3,1 %; jul 2,9 %); publicado 21-oct, próximo 18-nov. La OCDE da 3,6 %: se queda el dato del ONS | P |
| Irán | Inflación (Banco Central, cbi.ir/Inflation) | 71,4 % en Mehr 1405 (23-sep a 22-oct-2026); anterior 68,4 %. Año 1404: 48,3 %. [VERIFICAR] si es punto a punto o media de 12 meses | P |
| Emiratos | IPC (FCSC) | fcsc.gov.ae devuelve bloqueo de Cloudflare; sin dato | null |
| Indonesia | Paro y IPC (BPS) | bps.go.id en «verificación de seguridad» (anti-bots); no se salta. Siguen [S] vía prensa | S |
| Venezuela | IPC (BCV) | El BCV publica el INPC solo en Excel (`/estadisticas/consumidor`); no descargado sin OK. Sigue 467,9 % media 2026 FMI [S] | S |
| Argentina | Paro juvenil (INDEC) | El informe 2T-2026 (17-sep) y las series están en PDF/xls; no leídos. Sigue solo el dato por sexo [S] | S |

## Pendiente (necesita OK de Joel para descargar)
- BCV: Excel de INPC (variaciones mensual/anual).
- INDEC: «Mercado de trabajo. Tasas e indicadores socioeconómicos, 1T-2017 a 2T-2026» (xls) para el paro de 14-29 años.
- Emiratos y BPS: probar desde otra red o con el calendario de publicación.

Cambios: `explorador/indicadores-manual.json` (GB.ipc releído, nueva clave IR). `revisar_explorador.py`: 0 avisos. Regenerados Órbita, móvil y seguimiento. Sin commit.
