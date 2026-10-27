# W02 · Deuda, subastas y calificaciones · D03 Francia (26-oct-2026)

## 1. Calificación de Francia (cierra C7)
- AFT, leída en directo el 26-oct [P]: Moody's Aa3 negativa, última acción 10-abr-2026, «próxima fecha» 23-oct (no actualizada). S&P A+ estable (29-may; próxima 27-nov). Fitch A+ estable (28-ago). DBRS AA negativa (18-sep). Scope A+ estable (18-sep). KBRA AA- estable (12-jun; próxima 11-dic). R&I AAA negativa (30-mar). JCR AAA negativa (12-dic-2025).
- Resultado de Moody's del 23-oct: **[VERIFICAR]**. No encontré comunicado en moodys.com ni noticia fechada el 23-oct (las búsquedas devuelven la del 10-abr y avances de Selectra). El dato «mantenida en Aa3 negativa el 23-oct» que me pasaron como «según prensa» no lo he podido confirmar [S]. Calificación, fecha y calendario quedan sin cambio de valor, con nota de que la tabla de la AFT no recoge la revisión.

## 2. D03: curva OAT por plazos (subastas AFT, tipo medio ponderado) [P]
Fuente: aft.gouv.fr/en/dernieres-adjudications (leída en navegador; curl da 403).
| Subasta | Bono | Plazo aprox. | Rendimiento |
|---|---|---|---|
| 15-oct | OAT 2,70 % feb-2031 | 4,3 a | 4,01 % |
| 15-oct | OAT 0 % nov-2031 | 5,1 a | 4,10 % |
| 15-oct | OAT 3,25 % feb-2032 | 5,4 a | 4,16 % |
| 15-oct | OAT 3,50 % nov-2033 | 7,1 a | 4,41 % |
| 1-oct | OAT 3,70 % nov-2036 | 10,1 a | 4,93 % |
| 1-oct | OAT 3,80 % jun-2037 | 10,7 a | 4,97 % |
| 1-oct | OAT 1,25 % may-2038 | 11,6 a | 5,06 % |
| 1-oct | OAT 2,00 % may-2048 | 21,6 a | 5,40 % |
- Hecho: no hay serie diaria de 2, 5 y 30 años en la AFT (solo TEC 10); las subastas dan puntos a ~4-22 años con fecha distinta (1 y 15-oct), no una curva del mismo día. No hay OAT a 2 ni 30 años en subasta de octubre. Para 2 y 30 años hace falta otra fuente (Banque de France / Webstat) [VERIFICAR].
- Demanda: cobertura 2,0-3,0 en largo plazo y 2,2-2,3 en medio plazo (OAT 2031-33). TEC 10 reciente 5,13-5,14 % (dato previo de la sesión principal, no releído) frente a 4,93 % en subasta del 1-oct: lectura coherente con subida del 10 años en octubre.

## 3. Subastas semana 26-30 oct
Ya estaban en el calendario (EE. UU. 5 y 7 años 27 y 29-oct; Japón 2 años 29-oct); no se duplican. Resultado EE. UU. 2 años (TreasuryDirect, 26-oct) [P]: $69 mil M, rendimiento máximo 4,708 %, cobertura 2,59, vence 31-oct-2028; añadido al evento. Francia: sin subasta localizada para la semana (calendario AFT es imagen) [VERIFICAR]. España, Italia, Japón: no revisados (cuota).

## Cambios en archivos
`explorador/calificaciones.json` (nota/fecha de Francia), `eventos/calendario.toml` (Moody's Francia y resultado 2 años EE. UU.), `research/auditorias-estado.json` (C7 cerrado).

## Caso alcista / bajista (añadido 27-oct-2026, C27; sin predicción, solo con datos de este informe)
Tema: deuda de Francia.
- **Alcista:** la demanda en las subastas del 1 y el 15-oct fue sólida (cobertura 2,0-3,0 en largo plazo y 2,2-2,3 en medio); la curva sube de forma ordenada con el plazo (4,01 % a ~4 años, 5,40 % a ~22).
- **Bajista:** el TEC 10 reciente (5,13-5,14 %) está por encima del 4,93 % de la subasta del 1-oct, lo que apunta a subida del 10 años en octubre; el resultado de Moody's del 23-oct sigue sin confirmar [VERIFICAR].
- **Sesgo:** las subastas dan puntos de fechas distintas, no una curva del mismo día.
