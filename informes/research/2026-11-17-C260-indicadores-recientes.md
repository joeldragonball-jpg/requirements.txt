# C260 · Indicadores recientes por país (17-nov-2026)

Alcance: países prioritarios ya presentes en el panel. Singapur, Corea, Canadá, Australia, México, Arabia Saudí, Turquía y la UE como agregado **no están en `paises.json`**: añadirlos exige alta de país (otra tarea), no un indicador.

## Cerrado hoy
- **Japón, PIB real 3T-2026** [P]: -0,0 % trimestral desestacionalizado (caída menor de 0,05 %) y -0,1 % anualizado; abr-jun +0,4 % (+1,7 % anualizado). Fuente: Oficina del Gabinete (ESRI), 1.ª estimación preliminar publicada el 16-nov-2026. Cotejado por mí en los CSV oficiales `ritu-jk2631.csv` y `nritu-jk2631.csv` (fila «7- 9.», columna GDP gasto). Guardado en `explorador/indicadores-manual.json` → `JP.pib`. Preliminar, sujeta a revisión.
- Ya cerrado en pasadas anteriores (13-16-nov, ver informes C260 previos): IPC y paro de EE. UU., Reino Unido, China, Japón, Brasil, Sudáfrica, India (IPC), Argentina, Venezuela, Irán; PIB de EE. UU., Reino Unido, China, Brasil, Emiratos (1S-2026). Alemania, Francia, Italia ya traen IPC/paro/PIB mensuales o trimestrales (Eurostat/OCDE) más frescos que la media anual del Banco Mundial.

## Abierto
- **Rusia** IPC oct-2026 y paro (hoy [S]): cbr.ru devolvió 404 en las rutas probadas; Rosstat da error de certificado (no se salta). Pendiente probar cbr.ru/key-indicators con Chrome.
- **India** paro PLFS mensual y PIB trimestral: no leído (mospi.gov.in).
- **Sudáfrica** PIB trimestral (Stats SA P0441): página dinámica, no leída.
- **Indonesia** (BPS): 403 / anti-bots, sin saltar; IPC y paro siguen [S].
- **Emiratos** IPC y paro: FCSC bloqueada por Cloudflare (403); sin dato.
- Corea, Singapur, G20 restantes: requieren alta de país.
- Fallo transitorio del clasificador de herramientas impidió un 2.º intento de lectura; no es bloqueo de las webs.

## Verificación
`python scripts/revisar_explorador.py` → 0 avisos. No se ha hecho commit.
