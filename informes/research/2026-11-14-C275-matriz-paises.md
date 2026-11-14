# C275 · Huecos de la matriz país × tema (14-nov-2026)

Origen: explorador/regulacion.json (22 jurisdicciones × 8 temas = 176 celdas; ninguna falta).

## Los «29 huecos»
- 21 son Política monetaria: esas celdas llevan `dir` (sube/mantiene/baja) y `etapa` = null por diseño; la vista (vistas.html, línea ~1443) pinta «—» si etapa es null. Es un fallo de vista, no de datos. Propuesta para el agente de vistas: mostrar `dir` en esas celdas.
- 8 son huecos reales (sin fuente): AE ETF, BRICS ETF (no aplica), ID ETF, EG fiscal, ET fiscal, IR ETF, IR fiscal, ES ETF. G20 principales, UE, Singapur y Corea no tienen ninguno.

## Intentos 14-nov (sin dato nuevo)
- ES ETF: cnmv.es 403. AE ETF: sca.gov.ae redirige (301) a uaecma.gov.ae y la página de decisiones da 404. ID ETF: ojk.go.id 403 (ya anotado). Se añadió la nota del intento a AE y ES. Sin fuente leída, siguen vacíos (nunca relleno).
- EG/ET/IR fiscal, IR ETF: no intentados (sin sitio oficial accesible conocido; quedan [VERIFICAR]).

## Textos con «…»
No están en los JSON (0 coincidencias en paises.json): los genera vistas.html (línea 353, recorte de celdas >120 caracteres con title completo; línea 1482). Cambio de vista, no de datos.

## Para vistas.html (no tocado)
Sustituir «null» del aviso por «vacío»; pintar `dir` en Política monetaria.

Estado: 8 abiertos, 0 cerrados con dato. Sin commit.
