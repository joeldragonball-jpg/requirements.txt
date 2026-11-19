# C233 + C229 · España: energía y macro (19-nov-2026)

Información, no recomendación. Archivo editado: `explorador/espana-energia.json` (leido 2026-11-19). `explorador/espana-macro.json` NO se tocó: no hay lectura oficial nueva desde la pasada del 18-nov.

## HECHOS nuevos (nivel P, leídos hoy)
- **Error corregido (importante):** las medias OMIE de pasadas anteriores usaban la columna de PORTUGAL de `marginalpdbc` (columna 5), no la de España (columna 6). Cifras corregidas, en €/MWh (media simple de medias diarias, cálculo propio sobre ficheros OMIE): oct-2026 166,66 (antes 168,93); oct-2025 75,33 (antes 76,02; solo 30 de 31 ficheros cargaron); sep-2026 143,25 (antes 143,90); 1-18 nov-2026 170,22 (el «1-16 nov» era 186,08 en PT; en ES 184,21). Octubre 2026 ≈ 2,2 veces octubre 2025.
- Tendencia diaria OMIE España: 246,01 €/MWh (4-nov, máx.) a 52,13 (18-nov); 19-nov (publicado el 18): 32,68.
- **PVPC** (REData, precio horario de la energía, €/MWh): media 1-18 nov 208,98 (mín. −8,1; máx. 427,62); octubre 199,21. No es la factura final.
- **Mix 1-18 nov** (REData, 13.565 GWh): eólica 29,5 %, ciclo combinado 19,9 %, nuclear 18,9 %, FV 13,8 %, hidráulica 7,9 %.
- **Boletín Petrolero UE** (publicado 19-nov, precios del 16-nov, con impuestos): gasolina 95 ES 1,624 €/l vs UE-27 1,829; gasóleo ES 1,837 vs UE-27 2,050. Interanual (17-nov-2025: 1,485 y 1,443): gasolina ≈ +9 %, gasóleo ≈ +27 %.
- **Discrepancia a vigilar:** la pasada del 17/18-nov anotó para el 9-nov gasolina ES 1,73 y gasóleo 1,898; el histórico actual da 1,688 y 1,879 (UE 1,872 / 2,094). Se usa el histórico actual; causa (revisión o lectura errónea) [VERIFICAR].
- **MIBGAS PVB Day Ahead** (entrega 19-nov): 79,65 €/MWh (antes 83,96, el signo del cambio no se lee en la página); Month Ahead dic 79,89; balance de noviembre 79,70; Day Ahead PT 79,96.

## Sin cambio / no accesible
- IPC oct (4,9 %, subyacente 3,1 %), EPA 3T, afiliación oct, SMI, paro registrado, Euríbor mensual BdE: ya cargados el 18-nov con fuente oficial; sin publicación nueva. Próximas: IPC adelantado de noviembre (fin de mes), afiliación/paro de noviembre (2-3 dic) [VERIFICAR calendario].
- Gas almacenado (AGSI+): la API ahora devuelve «Invalid or missing API key»; se mantiene el 80,04 % del 16-nov. No se usó ninguna clave.
- Euríbor diario: sigue en euribor-rates.eu [S]; €STR del BCE no se pudo releer por CSV.
- Embalses: siguiente nota MITECO esperada el 24-nov.
- REData `precios-mercados-tiempo-real` con `time_trunc=day` da error 400; con `hour` funciona.

## Pendiente para quien regenere
Las cifras OMIE erróneas (168,93; 186,08; 143,9; 76,02) siguen en `docs/movil/data.json`, `docs/orbita/index.html`, `explorador/datos.json`, `explorador/espana-leyes.json` (a revisar si es contexto) e informes previos (`2026-11-17-C233`, `2026-11-18-C238`, auditoría de España, W12). Hay que regenerar con construir_* (no ejecutado aquí) y corregir `datos.json`.

Validación: `python scripts/revisar_explorador.py` → 0 avisos.
Nota de método: la pestaña de Chrome de otra sesión del grupo se navegó una vez por error; la mía se cerró.
