# C275 · Huecos de la matriz país × tema (17-nov-2026)

Origen: `explorador/regulacion.json` (176 celdas = 22 jurisdicciones × 8 temas). Listado hecho con python (celdas con `etapa` = null). Nivel: dato propio del repo; sin fuentes nuevas leídas hoy.

## Estado de los «29 —» (recuento del 17-nov)
- Hoy quedan **10 celdas sin dato** (las 21 de Política monetaria con `dir` ya se pintan; ver vistas.html del 16-nov).
- Los textos con «…»: 0 en `paises.json`; 1 en `regulacion.json` (Rusia, depositario digital, recorte editorial). El resto de «…» lo genera la vista al recortar a 120 caracteres (con `title` completo).
- «null» del aviso: no queda ninguna aparición en los JSON de origen ni en el aviso de vistas.html (se pinta «vacío»).

## Huecos abiertos (priorizados)
G20, UE, Singapur y Corea: **0 huecos**.
1. Emiratos · ETF: sca.gov.ae redirige a uaecma.gov.ae y la página de decisiones da 404 (intento 14-nov). Abierto [VERIFICAR].
2. España · ETF: cnmv.es 403 (14-nov). La celda dice que no consta ETF domiciliado; falta fuente primaria. Abierto.
3. Indonesia · ETF: ojk.go.id 403 / no carga (10-nov). Abierto.
4. Irán · ETF, fiscal y política monetaria; Egipto · fiscal; Etiopía · fiscal: sin fuente oficial accesible (3 intentos hasta el 15-nov). Deuda y saldo FMI de EG, ET e IR sí están (16-nov, datamapper FMI).
5. BRICS · ETF: no aplica (sin ETF supranacional).
6. España · política monetaria: no aplica (es la del BCE).

## Cerrados con dato hoy
Ninguno: las fuentes primarias siguen bloqueadas (403/404) y no se ha rellenado nada sin fuente leída. Los intentos de hoy se limitaron a revisar el estado; no se hicieron lecturas nuevas en Chrome.

## Comprobación
`python scripts/revisar_explorador.py`: 0 avisos en 13 capas. No se tocó ningún archivo de datos ni se hizo commit.
