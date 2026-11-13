# C259 · España › Justicia ampliada (13-nov-2026)

**Qué se ha hecho:** `explorador/espana-judicial.json` pasa de 11 a **37 casos** y de 59 a **109 hechos de fuente oficial**, cada uno con fecha y enlace. Todos los casos llevan ya `tipo`, `responsables` («Cargo implicado») y `gobierno_epoca` («Gobierno en ese momento»).

**Método:** cinco subagentes (Sonnet) buscaron y devolvieron texto; Fable abrió en el navegador **todas** las notas oficiales citadas (unas 50) antes de escribir, porque el lector de los subagentes resume y no devuelve el texto literal. Solo Fable editó el JSON. Lo que no se pudo leer está en `pendiente` o como prensa [S].

## Casos nuevos (26)

| Tipo | Casos | Fuente oficial leída |
|---|---|---|
| Guardia Civil / UCO / instrucciones | Forestalia (Teruel) · Operación Kitchen · «caso Montoro» (Tarragona) · obras de la Guardia Civil en la C. Valenciana · Diputación de Almería* · Ayuntamiento de Soria* | Guardia Civil, Poder Judicial (TSJ Aragón, TSJ Cataluña, TSJ C. Valenciana, Audiencia Nacional) |
| UE | Fiscalía Europea: subvenciones de empleo en Zamora y Salamanca · pagos del Plan de Recuperación retenidos o condicionados | eppo.europa.eu, Comisión Europea (IP/26/1511), Hacienda, Moncloa |
| Presupuesto (Tribunal de Cuentas, 2026) | Rescate bancario (66.617 M€) · derivados de empresas públicas (Acuamed, Puerto de Valencia) · contratos menores en gasto social · gobernanza del Plan de Recuperación · ayudas COVID a autónomos · CNIO · Parques Nacionales | tcu.es (siete notas de prensa) |
| Accidente | Apagón del 28-abr-2025 · Alvia de Angrois (2013) · metro de Valencia (2006) · Yak-42 (2003) | Poder Judicial, CNMC, Moncloa |
| Histórico | Gürtel · ERE de Andalucía · Púnica · Palau de la Música · Nóos · tarjetas black y Bankia · caso Pujol | Poder Judicial (Supremo, Audiencia Nacional, audiencias provinciales) |

\* Almería y Soria solo constan por prensa: salen con la etiqueta «Sin comprobar» y sin ningún hecho.

**Caso ampliado:** la DANA suma seis hechos de la causa de Catarroja (dos ex altos cargos autonómicos investigados, 10-mar-2025; negativa a investigar al presidente de la Confederación Hidrográfica del Júcar, 30-jul-2025; archivo del Supremo de las querellas contra el Gobierno central, 31-jul-2025; 233 víctimas oficiales, 28-sep-2026).

## Avisos de lectura

- **Una fiscalización del Tribunal de Cuentas es una auditoría**, no un proceso penal. La del rescate bancario concluye que FROB, FGD y Banco de España «han cumplido adecuadamente la normativa».
- **`gobierno_epoca` solo sitúa en el tiempo.** Sale de las fechas de las legislaturas, no de cada nota; donde el año de los hechos no consta en fuente oficial va [VERIFICAR]. No atribuye responsabilidad.
- **Equilibrio:** hay casos con gobiernos del PSOE (Forestalia/Miteco, ERE, contratos menores, Plan de Recuperación) y del PP (Kitchen, Gürtel, Púnica, metro de Valencia, Yak-42), y varios que abarcan los dos (rescate bancario, derivados, Montoro según prensa, Zamora). Cortes disueltas y elecciones el 29-nov-2026: releer antes de compartir.
- **Sin sentencia a 13-nov-2026:** Kitchen y caso Pujol (juicios vistos para sentencia según prensa; no hay nota en el listado de la Audiencia Nacional).
- **Regla de umbrales (W05):** el «537 M€ retenidos» del sexto pago es cifra de prensa que no aparece ni en la nota de la Comisión ni en la de Hacienda; lo oficial es 5.700 M€ aprobados en parte, 7.021 M€ brutos anunciados y 6.234 M€ cobrados (conceptos distintos). Queda como [S/VERIFICAR].

## Correcciones a lo que trajeron los subagentes

- Séptima solicitud del plan: 146 hitos y objetivos (no 148).
- Fiscalía Europea, Zamora: comunicado fechado el 17-abr-2026 (la dirección web dice 16).
- Nota de la Sala Penal sobre Kitchen: 20-abr-2022 es correcta (el subagente la creyó errónea).
- Descartados por falta de fuente oficial: S-80, Castor, pulseras antimaltrato, cribados de Andalucía, residencias de Madrid, Rodalies de Gelida, informes del Tribunal de Cuentas Europeo 06/2026 y 14/2026, decisiones C(2025) 5442 y C(2026) 5643 de la Comisión.

## Cambios en la vista

`explorador/vistas.html`: solo tres textos (introducción, leyenda de etiquetas y título del bloque), porque decían «solo notas del Poder Judicial» y «casos en curso». Sin cambios de diseño. Comprobado en navegador: 37 tarjetas, 109 enlaces, sin NaN, sin desbordes, desplegables cerrados.

## Pendiente (para otra sesión)

1. Leer con Chrome los comunicados de la Fiscalía Europea de 2026 que dieron error 429 y su informe anual 2025 (cifras de España).
2. PDF completos del Tribunal de Cuentas (pulseras n.º 1695, beneficios fiscales n.º 1694) y los dos informes del Tribunal de Cuentas Europeo.
3. IGAE y AIReF: sin ningún caso todavía.
4. Notas oficiales de Almería y Soria; sentencias de Kitchen y Pujol cuando salgan.

## Lecciones (máx. 5)

1. El lector de los subagentes resume: las «citas literales» hay que cotejarlas en la página antes de publicarlas; con el navegador y un `fetch` por lotes se revisan 25 notas del Poder Judicial de una vez.
2. La web de la Fiscalía Europea devuelve 429 a los lectores automáticos; con el navegador se abre a la primera.
3. Las notas de Hacienda y de la Comisión sobre un mismo pago dan cifras distintas (bruto, neto, aprobado, cobrado): anotar siempre el concepto.
4. El vigilante de Telegram casa palabras clave como subcadenas del titular: usar claves largas («caso ere», no «ere»).
5. El listado de noticias de la Audiencia Nacional se pagina con `startAt` y `pag01`; sirve para comprobar que una sentencia aún no ha salido.
