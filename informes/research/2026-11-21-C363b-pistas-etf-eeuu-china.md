# C363b · Pistas de voces sobre ETF/13F, EE. UU. y China (21-nov-2026)

Sin recomendaciones de compra o venta. Las voces son PISTAS: se registran, se contrastan y se marca el resultado. Fuente de las pistas: vídeos de Despeja La X (David Martínez) en `informes/videos/` y `explorador/voces.json`. En el repo no aparece ninguna voz llamada «Raúl Martínez» [VERIFICAR si es otra fuente]. Las lecturas de EDGAR se hicieron hoy en Chrome, leyendo el XML de cada 13F-HR (nivel P). Se añadieron 9 pistas nuevas a `explorador/cadenas-pistas.json` (de 39 a 48); no se tocó ninguna existente.

## Resultado del contraste

| Pista | Estado | Dato leído hoy |
|---|---|---|
| Goldman: historial dic-2025 / mar / jun | matizada | 4T-2025: 153,8 M$; 1T: 1,21 M$ (110.000 acc. XRPR, no cero); 2T: 87,4 M$ |
| Goldman: 3T ≥144 M$ | confirmada sin concretar | 145,34 M$ en 6 ETF de XRP (13F-HR 0000886982-26-000647, 16-nov) |
| Jane Street >20 M$ | confirmada sin concretar | 20,86 M$ (Bitwise, Franklin, Canary, XRPR); es creador de mercado |
| JPMorgan «abre posición» | matizada | 539 acciones Bitwise = 8.996 $ (insignificante) |
| Morgan Stanley «entra» | matizada | 116.097 $ entre Franklin, XRPR y Bitwise |
| Fed «último apretón» (13-nov) | sin confirmar [ESPECULACIÓN] | FOMC 28-oct mantuvo 3,75-4 %; la predicción no se puede contrastar |
| Clarity «vuelve a la mesa» | sin confirmar [ESPECULACIÓN] | Fuente anónima; abierta hasta el 3-ene-2027 |
| China «ya no compra deuda de EE. UU.» | sin confirmar (no verificable hoy) | El archivo TIC abierto tenía datos de 2022-2023 |
| BRICS «su propio sistema» (mBridge) | matizada | BIS: «handing the project over to the partners» (oct-2024) |

Ninguna pista nueva queda desmentida del todo. «Marzo = cero» de Goldman es la parte falsa de la primera.

## Goldman Sachs: cuál es el CIK correcto

- CIK 769993 (Goldman Sachs & Co. LLC) solo presenta 13F-NT: último, 16-nov-2026 (0000769993-26-000059), listado de EDGAR leído hoy.
- Las tenencias se declaran en Goldman Sachs Group Inc (CIK 886982). Su 13F-HR del 3T (periodo 30-sep-2026, firmado 16-nov-2026) tiene 14.139 filas. Cinco ETF de XRP más XRPR suman 145,34 M$ y 8,68 M acciones.
- La serie completa coincide con `2026-10-15-R21b-13f-segunda-pasada.md`. Goldman nunca llegó a cero: conserva 110.000 acciones de XRPR.

| Fecha de cierre | Valor en ETF de XRP |
|---|---|
| 31-dic-2025 | 153,8 M$ |
| 31-mar-2026 | 1,21 M$ |
| 30-jun-2026 | 87,4 M$ |
| 30-sep-2026 | 145,3 M$ |

## Caso alcista y bajista

- **Alcista:** los datos 13F que da el canal son reales; hay más declarantes y Goldman mantiene ~145 M$ tras la caída de septiembre.
- **Bajista:** el 13F es una foto del 30-sep, no muestra la reacción a la caída de noviembre. Los nombres de más peso (JPMorgan, Morgan Stanley) son importes mínimos. Jane Street es creador de mercado. Un 13F no separa cartera propia, de clientes o cobertura.
- **Sesgos:** el canal es tenedor de XRP, usa nombres de prestigio sin importes y presenta como convicción lo que puede ser función de mercado.

## Pendiente

- Series de China (TIC) del Tesoro en una copia actual: [VERIFICAR].
- 13F del 2T de JPMorgan y Morgan Stanley para saber si sus posiciones eran nuevas.
- 13F del 4T-2026 (≈15-feb-2027).
- No se contrastó en esta tanda nada de e-CNY ni regulación china por voces: no hay voz concreta en el repo salvo la de mBridge.
