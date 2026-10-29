# Accesos que fallan con curl o con el navegador integrado y se prueban con la extensión de Chrome (Claude in Chrome)

Regla de Joel (29-oct-2026): lo bloqueado para APIs o webs se intenta con la extensión de Chrome (navegador real, sin saltar controles anti-bots ni captchas). Descargar un archivo pide su OK. Estado de la prueba entre paréntesis.

| Tarea | Qué falta | Dónde probar con Chrome | Estado |
|---|---|---|---|
| D03 Francia | Curva OAT 2, 5 y 30 a | aft.gouv.fr: «OATs key figures» (`/en/principaux-chiffres-oat`) solo da histórico de subastas en XLS; TEC 10 en portada (4,94 % el 28-oct) | HECHO 29-oct: XLS descargado con OK de Joel (quedó como .tmp en Descargas) y volcado a `explorador/bonos-manual.json` (3, 5, 10 y 30 a de subasta). Falta curva secundaria diaria |
| D05 Francia 30 a | Subasta o secundario a 30 a | Mismo XLS de la AFT | HECHO 29-oct: 4,55 % (subasta 4-jun-2026, OAT 2057) |
| D02 Alemania | Serie Bund 2, 5, 10, 30 a (Svensson) | `api.statistiken.bundesbank.de` (clave `BBSIS.D.I.ZAR.ZI.EUR.S1311.B.A604.R10XX…`), Finanzagentur | Chrome no cargó (la navegación no salió de la página anterior); curl y navegador integrado: ECONNRESET. Repetir a mano en Chrome o desde otra red |
| D01 Italia | Serie diaria BTP 2/5/10/30 a | Banca d'Italia infostat/BDS y Borsa Italiana (consulta interactiva) | Sin probar |
| D06 Bancos | Cortes recientes de exposición soberana y alcance de «soberano» | `edap-public.eba.europa.eu` (Pillar 3 Data Hub) | Sin probar |
| C56 | PIB 3T y PCE sept. (BEA 29-oct) | bea.gov (release del 29-oct) | Sin probar (no indexado a las 10:00) |
| C56 | Moody's A2 a RLUSD | moodys.com | Sin probar |
| C56 | Documento OCC del banco de Ripple | occ.gov (decisiones corporativas) | Sin probar |
| W05/W08 | Sección 404 CLARITY, cloture, MEI y escala del ahorro en BOE | congress.gov, senate.gov, boe.es | Sin probar |

Resuelto por navegador: D04 China (ChinaBond, navegador integrado, 29-oct).
