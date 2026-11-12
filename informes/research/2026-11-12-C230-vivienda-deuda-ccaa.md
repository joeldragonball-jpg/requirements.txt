# C230 · Vivienda y deuda autonómica (12-nov-2026)

Completa el informe del 10-nov (INE IPV, hipotecas, condonación siguen vigentes ahí). Nivel: P = fuente oficial leída · S = prensa · [VERIFICAR]. Sin recomendaciones.

## 1. Deuda PDE por CCAA, 2T26 [P]
Fuente: Banco de España, CSV oficial be1309 (serie DTNPDE2010_...): https://www.bde.es/webbe/es/estadisticas/compartido/datos/csv/be1309.csv ; nota 30-sep-2026: https://www.bde.es/wbe/es/noticias-eventos/actualidad-banco-espana/deuda-aapp-2026t2.html
Total CCAA: 355.241 M€ en jun-2026 (342.799 M€ jun-2025; +3,6 %) = 20,4 % del PIB.
| CCAA | M€ jun-26 | % interanual | % PIB regional |
|---|---|---|---|
| Cataluña | 92.770 | +2,3 | 28,1 |
| Comunidad Valenciana | 64.593 | +6,4 | 40,0 |
| Andalucía | 42.070 | +1,5 | n/d |
| Madrid | 42.296 | +7,2 | 12,3 |
| Castilla-La Mancha | 17.029 | +1,7 | 28,1 |
| Castilla y León | 14.778 | +1,5 | n/d |
| Murcia | 14.254 | +7,0 | 30,8 |
| Galicia | 13.357 | +3,7 | n/d |
| País Vasco | 11.679 | +8,8 | 11,7 |
| Aragón | 9.407 | -0,2 | n/d |
| Baleares | 8.691 | +1,8 | n/d |
| Canarias | 6.897 | +2,0 | 10,9 |
| Extremadura | 5.570 | +2,3 | n/d |
| Asturias | 4.095 | -1,5 | 12,5 |
| Cantabria | 3.325 | -0,3 | n/d |
| Navarra | 2.446 | -10,6 | 8,4 |
| La Rioja | 1.986 | +6,1 | n/d |
Los 9 ratios (% PIB) quedan confirmados en la nota del BdE (antes [VERIFICAR]); Castilla-La Mancha y Cataluña coinciden en 28,1 %. Cinco CCAA bajo el 13 % de referencia de la Ley de Estabilidad: Navarra, Canarias, País Vasco, Madrid, Asturias. Próxima publicación 3T26: 15-dic-2026.

## 2. Precio €/m² por CCAA, 2T26 [P]
Fuente: Registradores, ERI 2T26 (PDF leído con pdftotext): https://www.registradores.org/documents/d/guest/eri_2t_2026
- España: 2.487 €/m² (+2,4 % trim.); nueva 2.636 (-0,7 %), usada 2.448 (+3,5 %). Interanual (media móvil 12 m): 2.392 €/m², +9,2 %. Compraventas 2T: 167.934 (-5,7 % trim., -2,3 % interanual); 12 meses 698.684 (+1,0 %). Compras de extranjeros: 15,98 % del total, máximo histórico.
- Mayores precios 2T: Madrid 4.477, Baleares 4.311, País Vasco 3.616, Canarias 3.052, Cataluña 2.995 €/m². Menores: Extremadura 947, Castilla-La Mancha 1.081, Castilla y León 1.421, La Rioja 1.462, Murcia 1.514 €/m².
- Interanual (precio 12 m, con var.): Cantabria 2.236 (+18,1 %), Asturias 1.651 (+15,7 %), Murcia 1.457 (+16,1 %), Aragón 1.839 (+12,4 %), Madrid 4.305 (+12,1 %), C. Valenciana 1.933 (+12,3 %), Baleares 4.166 (+9,7 %), Cataluña 2.849 (+8,5 %), Andalucía 2.021 (+7,8 %).
- Nota de método: el PDF mezcla filas en la extracción (p. ej. la fila "Cantabria" trimestral repite la de A Coruña); uso solo la tabla anual y los textos. Los precios del Registro son declarados en escritura; no son el IPV del INE.

## 3. Alquiler (INE IPVA, experimental) [P parcial]
INE IPVA 2024 (nota 2025, vista por resumen de búsqueda): +3,5 % nacional; mayores: C. Valenciana +5,0 %, Baleares +4,0 %, Andalucía +3,8 %; menores: Asturias +2,7 %, CyL +3,0 %. Es dato de 2024, basado en IRPF; la edición 2025 no se leyó [VERIFICAR] (https://www.ine.es/dyngs/Prensa/IPVA2024.htm).

## 4. Esfuerzo (BdE)
- BdE, Informe Anual 2025 (vía OCU [S]): hogares en alquiler destinan de media 26,7 % de su renta neta (2024).
- BdE, IEF primavera 2026, recuadro 4.1 (leído [P]): sin cifras por CCAA en el texto; define baja capacidad financiera como no poder pagar entrada del 20 % + costes + 1 año de consumo, o DSTI ≥ 35 % de renta neta. Panel de Hogares 2016-2023, sin Navarra ni País Vasco. 
- Funcas / Fotocasa-InfoJobs: ver informe 10-nov [S]; metodologías distintas, sin ranking firme.

## Huecos / bloqueado
- Esfuerzo por CCAA del BdE (Informe Anual 2025, sec. 3.2): PDF no leído. IRAI Registradores y IPVA 2025 por CCAA: no extraídos. Ratios % PIB de las 8 CCAA sin cifra en la nota: calcular con PIB regional INE [VERIFICAR]. Estado legislativo de la condonación: sin verificar.

## Lecciones
- El CSV be1309 del BdE da la deuda PDE por CCAA en miles de €; más fiable que la nota.
- `curl` al PDF + `pdftotext -layout` funciona donde WebFetch devuelve binario (Registradores).
- Caso alcista/bajista: precios al alza (+9,2 % interanual) con compraventas a la baja (-2,3 %); lectura no concluyente [ESPECULACIÓN].
