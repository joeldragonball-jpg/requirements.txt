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
| W05/W08 | Sección 404 CLARITY, cloture, MEI y escala del ahorro en BOE | congress.gov, senate.gov, boe.es | BOE HECHO 31-oct (MEI y art. 66); congress.gov y senate.gov bloquean Chrome |

Resuelto por navegador: D04 China (ChinaBond, navegador integrado, 29-oct).

## 31-oct-2026 (W03 bloques A-C)
- **bcb.gov.br (normativos de Brasil): FUNCIONA con Chrome.** Abrir `exibenormativo?tipo=Resolução%20BCB&numero=NNN`, esperar 4 s y leer `document.body.innerText` con `javascript_tool` en trozos (la salida se corta a ~1.500 caracteres; buscar por `indexOf('Art. N')`). Leída la Res. 589.
- **PDF de finma.ch en Chrome: NO funciona** (el visor de PDF es una extensión de Chrome: `get_page_text` y las capturas fallan). Probar la página HTML de FINMA o descargar el PDF con el OK de Joel.
- **31-oct (verificaciones atrasadas), para probar con Chrome:** senate.gov (roll call del cloture 49-50) y congress.gov (sección 404 de CLARITY) dan 403 al lector; tse.jus.br (resultado de la 2.ª vuelta) y moodys.com (A2 de RLUSD) no cargan; BOE: art. 66 LIRPF (el texto se corta; abrirlo por su ancla en boe.es) y calendario del MEI (art. 127 bis LGSS dice 1,2 puntos sin año: buscar la disposición transitoria). Whitehouse.gov no recoge la frase de Trump del 9-oct.

## 31-oct-2026 (resultado de la prueba con Chrome)
- **boe.es: FUNCIONA.** `boe.es/buscar/act.php?id=BOE-A-...&tn=1` y leer `document.body.innerText` con `javascript_tool` (buscar con `lastIndexOf('Artículo N.')`; la salida se corta, pedir trozos). Última actualización del texto consolidado de la LIRPF: 07/10/2026.
  - **Art. 66 LIRPF (escala estatal del ahorro, 66.1): 9,5 % hasta 6.000 € · 10,5 % hasta 50.000 € · 11,5 % hasta 200.000 € · 13,5 % hasta 300.000 € · 15 % en adelante.** Para no residentes (66.2): 19/21/23/27/30 %. Última modificación: Ley 7/2024 (DF 7.1), con efectos desde 1-ene-2025. Sumada la parte autonómica de escala supletoria da 19-30 %. Cerrado (la parte autonómica depende de cada comunidad).
  - **MEI (LGSS, disp. transitoria 43.ª): 2026 = 0,90 puntos (0,75 empresa + 0,15 trabajador)**; 2027: 1,00; 2028: 1,10; 2029: 1,20; 2030-2050: 1,20. El art. 127 bis solo dice 1,2 (régimen final). Cerrado.
- **congress.gov: BLOQUEADO** (Cloudflare «Sorry, you have been blocked», Chrome también). Sección 404 de CLARITY sigue [VERIFICAR].
- **senate.gov: BLOQUEADO** («Unauthorized», alerta de seguridad al webmaster). Cloture 49-50 sigue [VERIFICAR]. No insistir ni saltar el control.
- **moodys.com: no encontró la página** (URL genérica); la calificación de RLUSD no está en la web pública sin cuenta. Sigue [VERIFICAR]; buscar nota de prensa de Ripple/Moody's.
- **resultados.tse.jus.br:** carga pero es una app que exige elegir elección a mano; no leída. Pendiente: probar con clic o fuente alternativa (g1/Agência Brasil como [S]).
