# Repaso del cerebro: contradicciones y resúmenes (25-oct-2026)

Base: la revisión automática de hoy (`informes/2026-10-25-revision.md`, 12 hallazgos), el resumen semanal del bot (`cerebro/actualidad/2026-W43.md`) y los datos que se han leído esta semana. **No se ha modificado ningún archivo del cerebro** (regla 5 de CLAUDE.md): las correcciones vigentes van en un archivo nuevo, `cerebro/documentos/estado-vigente-y-correcciones.md`. Nivel: [P] primaria leída, [S] medios, [VERIFICAR] pendiente.

## Resultado de cada hallazgo de la revisión del bot
| # | Hallazgo | Veredicto hoy | Qué se hizo o falta |
|---|---|---|---|
| C1 | Adquisiciones de Ripple: «más de 4.000 M$» frente a ≈ 2.700 M$ con precio | Real; la corrección del propio cerebro es la válida | Cifra vigente: ≈ 2.700 M$ con precio conocido. El 4.000 no se sostiene. Falta fuente por adquisición [VERIFICAR] |
| C2 | Fed «en pausa 3,50-3,75 %» frente a 3,75-4,00 % | **Resuelto [P]**: el rango vigente es 3,75-4,00 % (Fed, tras la subida del 16-sep) | Ya en el archivo de estado vigente. El apartado «Timing» del archivo principal sigue con datos de mayo |
| C3 | CLARITY «fracasa/rechazada» el 15-sep | Real; fue una moción de cierre rechazada 49-50, no un rechazo definitivo | Redacción canónica en el archivo nuevo. Hay que corregir `catalizadores-xrp-xlm.md` (línea 2026-09-15) |
| C4 | Evernorth: 473 M XRP | La cifra de 473 M es pro forma de 2025; el 8-K confirma 388.910.554 XRP aportados en especie y cotización desde el 12-oct | Vigente en el archivo nuevo |
| C5 | Debut de XRPN −1,05 % | **No cuadra**: apertura 16,68 y cierre 16,91 es +1,4 % | No usar el −1,05 % hasta saber su base [VERIFICAR] |
| C6 | ITP joven de Cataluña (32 o 35 años, tramos) | Sin resolver | Research: leer la Agència Tributària de Catalunya |
| C7 | MEI 2026 | **Resuelto**: 0,90 % total (0,75 % empresa y 0,15 % trabajador), Orden PJC/297/2026, BOE-A-2026-7296, 31-mar-2026 [S: resúmenes y registro del BOE; no leí el BOE] | Quitar los valores dudosos de 2025 |
| C8 | Swell: [VERIFICAR] frente a confirmado | Resuelto: 27-29 oct en Nueva York (el calendario del repo lo tiene) | Retirar la línea antigua al consolidar |
| C9 | Brent y bonos de mayo en el resumen | **Resuelto con series [P]**: ver abajo | Datos vigentes en el archivo nuevo |
| C10 | SEC-CFTC nombra o no a XRP y XLM | Sin resolver: sec.gov bloquea la lectura automática | Research con el navegador integrado: leer el texto oficial del 17-mar |
| S1 | «Sección 404» de CLARITY | Sin fuente | Research: localizar el texto del borrador |
| D1 | El litigio SEC-Ripple se cuenta en 5 sitios | Real | Necesita una decisión tuya (ver abajo) |

## Contradicciones nuevas que he encontrado
1. **«El Treasury llegó al 5,34 %» (W43, sin plazo).** Con la serie diaria del Tesoro de EE. UU. [P, home.treasury.gov, leída hoy]: a 23-oct el 10 años está en **5,00 %** y el 30 años en **5,33 %**; máximos del año: 10 años 5,31 % (5-oct) y 30 años 5,67 % (7-oct). El 5,34 % es casi seguro el **30 años**, o se ha mezclado con el 10 años británico (5,33 % en nuestro panel). Mientras no tenga plazo, no es un dato utilizable.
2. **«Los flujos de crudo de Oriente Medio están cerca de niveles previos a la guerra» (Bloomberg, según W43).** Contradice al dato primario del FMI: el estrecho de Ormuz pasa de 78 barcos al día en febrero a 3,7 en la última semana [P, PortWatch hasta 18-oct]. Medidas distintas (crudo que sale por todas las rutas frente a barcos por el estrecho), pero no se pueden dar las dos sin explicación. [VERIFICAR] qué cifra de Bloomberg y de qué periodo.
3. **El resumen del bot repite titulares como hechos** («Irán afirmó que siete buques fueron impactados»): es una afirmación de una parte, [S].

## Cifras vigentes que ya tenemos con fuente primaria
- Fed 3,75-4,00 %. Bonos de EE. UU. a 23-oct: 2 años 4,69 %, 10 años 5,00 %, 30 años 5,33 % [P: Tesoro].
- Brent: futuro continuo 23-oct $111,97; spot de la EIA 20-oct $115,22 (series distintas, no comparar) [T18].
- Ormuz: tráfico hundido el 28-feb a 4-mar; media de octubre 3,6 al día [P: PortWatch].
- Sudáfrica: repo 7,25 % desde el 25-sep (BIS y prensa); OCC: norma final de la ley GENIUS publicada el 23-oct [P: Federal Register].

## Qué propongo (tú decides)
**Hacer ahora, sin gastar cuota:** el archivo `estado-vigente-y-correcciones.md` (hecho) como fuente única de lo vigente.

**Decisión tuya:** el archivo principal (`apuntes_xrp_macro_fiscalidad_2026.md`, ~80 KB) acumula afirmaciones antiguas junto a sus correcciones. Reescribirlo contradice la regla 5. Alternativas: (a) dejarlo y que el archivo nuevo mande; (b) permitir **una vez** una consolidación en un archivo nuevo `resumen-vigente-xrp.md` y marcar el viejo como histórico (lo hace una tarea Opus de ~4 %).

**Research a programar (lote de W05 del jueves, ~3 %):** C6 (ITP Cataluña), C10 (SEC-CFTC, navegador), S1 (sección 404), C1 (fuente de cada adquisición de Ripple) y C5 (base del −1,05 % de XRPN).

**Auditoría:** la mensual W08 (jueves/viernes, ~4 %) debería incluir un cruce automático de cifras de los resúmenes semanales del bot (W41-W43) con series primarias: hoy ha cazado dos fallos en un resumen.
