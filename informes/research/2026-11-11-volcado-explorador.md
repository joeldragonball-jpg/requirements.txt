# C39 · Volcado mecánico al Explorador (11-nov-2026)

Solo se editaron JSON existentes de `explorador/` (sin ficheros, paneles ni capas nuevas). Niveles P/S/[VERIFICAR] copiados del informe de origen; nada se subió de nivel. Todos validan con `json.load`; diffs pequeños; CRLF/LF y formato originales conservados. Sin commit.

## Qué entró, por archivo
- `indicadores-manual.json` · CN IPC pasa a oct-26 0,7 % (anterior 0,9 %, nivel S: NBS no leído; sep seguía en P). Nuevo bloque BR (único país de C59/C31 que existe en `paises.json`): IPCA-15 oct 4,62 %, paro 5,4 % (T2), PIB T2 +0,5 %, todo S. `_actualizado` a 11-nov.
- `estabilidad-manual.json` · 9 hitos S de C61 en `hitos` (antes vacíos): US sanidad (OBBBA) y educación; DE sanidad (GKV); FR educación; IT educación; ES sanidad (huelga médica); GB sanidad (BMA); JP sanidad y educación. Las cifras de gasto ya estaban en P (venían de ahí).
- `espana-presupuesto.json` · nota del SE (por_cargo): releído art. 21.Dos, brecha Ley/Portal con medias del 2-nov (≈32.700/41.100/28.500 €) y resoluciones del Consejo de Transparencia [S]. Las cifras de C68B ya estaban volcadas.
- `regulacion.json` · 10 hitos nuevos: ESMA 30-sep (ue custodia), ADGM staking 29-abr [P] (ae custodia; resuelve un [VERIFICAR]), MAS comunicado 2023 [P] (sg custodia), SFC stablecoins mayo-26 [S] (hk), Corea ley marco 22-oct [S], Japón FIEA/tributación [S], EE. UU. ETF staking [S] y SR-ISE-2026-42 aprobada [P], DGT staking España [S], euro digital BCE FAQ (ue cbdc).
- `fichas-activos.json` · XRP: sin staking nativo, AMM XLS-30 [P], XLS-66/65 en votación a 16-sep [P], TVL XRPL 32,9 M [P]. XLM: sin staking, TVL Stellar 212,6 M y Blend 117,2 M [P]. Un [VERIFICAR] nuevo (estado XLS-66). `actualizado` 11-nov.
- `elecciones.json` · FR sube a P (18-abr/2-may-2027, Interior); notas de lectura 11-nov en US (218-214-1 [P]; resultados S), IT, AR, JP (reglas 4/6 años [P]), DE, GB. `leido` 11-nov.
- `prueba-datos.json` (calendario) · ISE-42: «aprobada el 10-nov», `aprox` false; FOMC dic con Waller/Bowman; euro digital trílogo y piloto con el FAQ del BCE.
- `hitos_petroleo.json` · `nota`: spot EIA 22/23-oct y 3-10-nov (Brent 90,16, WTI 89,62 el 10-nov) [P], marcado como no comparable con los futuros de los hitos.

## Sin sitio (no forzado)
- IPC/paro/PIB de DE, FR, IT, ES, euro, UE: el origen es `indicadores-historia.json`, autogenerado por script (no se toca a mano); su dato oct-26 ya llega por Eurostat. IPC EE. UU.: lo escribe `automatizar_manuales.py`.
- IPC de MX, CA y los datos de paro/PIB de UK, JP, ZA...: no hay MX/CA en `paises.json`; UK/JP/CN ya estaban iguales o más nuevos en el manual.
- Tablas 2026 de cargos de C68B, ya presentes. Brasil en C61 (sin datos primarios) y gasto sanitario BR ~9,7 %: BR no existe en `estabilidad-manual.json`.
- Deuda/déficit FMI (C59): ya en `deuda-fmi.json` (autogenerado). Proyecciones 2026 = [ESPECULACIÓN] no se duplican.
- Filas JSON «propuestas» de C42/C42b (tabla por modalidad): no hay panel de rendimientos; se repartieron en hitos/fichas (se pidió no crear panel).
- Abu Dabi 10-11 nov (todo S, sin resultado de fondo): no hay tema de conflicto en los JSON; solo existe una noticia en `datos.json` (generado por bot).
- Chirac y otros mandatos C140: ya volcados (commit anterior). Fed 10-nov en `tipos-manual.json`: ese archivo es para tipos sin API, no para discursos.

## Dudas
- CN IPC: bajé de P (sep) a S (oct) al usar el último dato; si prefieres mantener P, revertir a sep.
- IT: fecha del JSON 2027-12-31 (aprox.) vs ~oct-2027 del informe: son compatibles (fin de legislatura + 70 días) pero no se unificó.
- Fecha 2026-06-01 (JP tarifas) y 2026-03-01 (SEC-CFTC) en hitos son aproximadas por falta de día exacto.

Resumen: 8 JSON editados (indicadores-manual, estabilidad-manual, espana-presupuesto, regulacion, fichas-activos, elecciones, prueba-datos, hitos_petroleo); todo validado sin reformateo.
Niveles respetados; lo no contrastado sigue [VERIFICAR]/S. Datos autogenerados o sin país/panel quedaron «sin sitio».
Pendiente tuyo: regenerar Órbita/móvil con los scripts y decidir lo de CN IPC.
