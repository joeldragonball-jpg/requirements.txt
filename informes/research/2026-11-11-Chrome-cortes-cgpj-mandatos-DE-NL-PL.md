# Chrome 11-nov-2026: plantillas Cortes/CGPJ y mandatos DE, NL, PL

Claude in Chrome, pestaña propia (cerrada), solo lectura, sin login/captcha/descargas. Sin recomendaciones de inversión. explorador/*.json y cerebro/ NO tocados (propuestas abajo).

## 1. Plantillas

| dato · antes · después · fuente |
|---|
| Senado: funcionarios de las Cortes Generales adscritos (personas) · sin dato · **262** (152 mujeres, 110 hombres; Letrados 21, Archiveros-Bibliotecarios 16, Asesores Facultativos 8, Redactores 28, Técnico-Administrativo 26, Administrativos 102, Ujieres 61) · senado.es/web/composicionorganizacion/administracionparlamentaria/secretariageneralestado/personalsenado/index.html, «Última actualización 14/10/2026», leído 11-nov-2026 · **P** |
| Senado: personal laboral (personas) · sin dato · **92** (16 M, 76 H) · misma fuente · **P** |
| Senado: personal adscrito del Gobierno (personas) · sin dato · **110** (seguridad 96, gabinete telegráfico 2, Correos 2, Parque Móvil 10) · misma fuente · **P** |
| Senado: personal eventual (personas) · sin dato · **104** (Mesa/Diputación Permanente 24 + grupos y senadores 80) · misma fuente · **P** |
| Senado: suma de las 4 categorías (cálculo mío) · sin dato · **568 personas** = 262+92+110+104; la web no da este total · derivado de la fuente anterior · P (suma de cifras P) |
| Congreso: composición numérica de Cuerpos y grupos laborales · tablas no leídas · **sigue sin total**: la página congreso.es/es/cem/acceso_empleo solo muestra los títulos; el contenido está en bloques desplegables/enlaces no extraíbles (no hay enlaces a PDF ni tabla en el DOM) y los datos por Cuerpo van en subpáginas por oposición (letrados2022, etc.) que solo traen convocatorias · congreso.es, 11-nov-2026 · S |
| Congreso: web de personal propia (equivalente a la del Senado) · — · no localizada (/es/cem/personal-congreso da 404) · S |
| CGPJ: RPT · RPT enero 2025, sin total sumado · sin cambio; la ruta de Transparencia probada da 404 y no se abrió el PDF en Chrome (suma pendiente con tabulado o Ley 19/2013) · poderjudicial.es · S (total) / P (existencia RPT) |
| TC y Consejo de Estado · sin cifra · no abordados en esta sesión (tiempo); sin cambio · S |

HECHOS: el Senado sí publica plantilla por categorías y fecha; es el primer órgano constitucional con cifra de personas leída en fuente oficial. Distinguir: son personas (no puestos con dotación). Los 262 son funcionarios de las Cortes adscritos al Senado, no todos los funcionarios de las Cortes (Congreso aparte). [VERIFICAR] si el personal adscrito (110) debe contarse como plantilla del Senado: depende orgánicamente de los Presidentes pero pertenece a Cuerpos de la AGE.

JSON propuesto (no aplicado), entrada del Senado:
`{"organo":"Senado (Cortes Generales)","personas":{"funcionarios":262,"laborales":92,"adscritos":110,"eventuales":104,"suma":568},"tipo":"personas","fuente":"https://www.senado.es/web/composicionorganizacion/administracionparlamentaria/secretariageneralestado/personalsenado/index.html","fecha":"actualizado 14-oct-2026, leído 11-nov-2026","nivel":"P"}`

## 2. Mandatos (explorador/mandatos.json, entradas previas nivel S)

Fuente NL: rijksoverheid.nl/regering/over-de-regering/kabinetten-sinds-1945 y subpáginas de cada kabinet, leídas 11-nov-2026.

| dato · antes · después · fuente |
|---|
| NL Balkenende, desde 2002-07-22 · S · **P** («Beëdiging kabinet: 22 juli 2002», kabinet-balkenende-i) |
| NL Balkenende, hasta 2010-10-14 · S · **P** (kabinet-Balkenende IV «regeerde van 22 feb 2007 tot 14 okt 2010») |
| NL Rutte, desde 2010-10-14 · S · **P** (kabinet-Rutte-Verhagen: beëdiging 14 oct 2010) |
| NL Rutte, hasta 2024-07-02 · S · **P por coherencia**: Schoof juró el 2-jul-2024; la página de Rutte-IV da solo su dimisión (7-jul-2023) y juramento 10-ene-2022, no el relevo explícito [VERIFICAR] si se quiere P literal |
| NL Schoof, desde 2024-07-02 · S · **P** («Op 2 juli 2024 was de beëdiging van het kabinet-Schoof») |
| NL Schoof, hasta 2026-02-23 · S · **P** (beëdiging kabinet-Jetten 23-feb-2026; ya figuraba P para Jetten) |
| NL: 32 gabinetes y 17 primeros ministros desde 1945 · — · P, dato de contexto · misma página |
| DE Schröder/Merkel/Scholz (días exactos) · S · **sin cambio**: bundeskanzler.de y bundesregierung.de redirigen a otro dominio y la herramienta corta la lectura (dos intentos); años ya P · S |
| PL Kopacz/Szydło/Morawiecki/Tusk 1.er periodo/2001-2007 (días) · S · **sin cambio**: gov.pl/web/premier/expos-poprzednich-premierow solo lista exposés sin fechas de toma de posesión; no hay histórico de nombramientos en gov.pl · S |

Propuesta: subir a P las 6 fechas NL de la tabla (la de Rutte hasta 2024-07-02, con nota «cierre = juramento Schoof»). DE y PL: seguir en S con años P; para subirlos hacen falta Sejm/Prezydent.pl (PL) y Bundestag/Bundespräsident (DE), no probados.

## Accesos
Funcionan: senado.es, congreso.es, rijksoverheid.nl (rutas /kabinetten-sinds-1945), gov.pl. 404: poderjudicial.es/Transparencia (ruta probada), rijksoverheid.nl/regering/bewindspersonen/mark-rutte (ex-ministros). Redirigen y se corta: bundeskanzler.de, bundesregierung.de. Había otra pestaña de Chrome en el grupo ("Nueva pestaña"), no mía, no tocada.

## Resumen
1. Senado: 568 personas (262 funcionarios + 92 laborales + 110 adscritos + 104 eventuales), P, actualizado 14-oct-2026; Congreso, CGPJ, TC y Consejo de Estado siguen sin total.
2. NL: seis fechas de inicio/fin de Balkenende, Rutte y Schoof sustentables en P con rijksoverheid.nl (la de fin de Rutte por coherencia).
3. DE y PL no se pudieron leer en día exacto; quedan en S.
