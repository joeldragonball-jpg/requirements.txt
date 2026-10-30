# C68 · Sueldos de cada cargo político: dónde se publican y dónde se desglosa el gasto (pedido de Joel, 30-oct-2026)

Joel pregunta: «¿dónde encuentro los sueldos de cada persona política y dónde se desglosa ese gasto?». Hoy el Explorador (pestaña España) tiene altos cargos y eventuales por ministerio (arts. 10 y 11 de cada sección del IGAE) y un bloque «Cargos políticos» con retribuciones de diputados y senadores. Falta el sueldo por cargo y por persona.

## Qué hacer (solo fuentes oficiales, sin memoria; [P]/[S]/[VERIFICAR])
1. **Presidente y ministros/as, secretarios de Estado, subsecretarios, directores generales:** retribución anual publicada (Ley de PGE prorrogada y RD de retribuciones de altos cargos; Portal de Transparencia, «Retribuciones de los altos cargos de la AGE»; BOE). Una fila por categoría con importe bruto anual, fecha y enlace.
2. **Una fila por persona** cuando la fuente la dé (Portal de Transparencia / agenda y declaraciones de bienes y rentas): nombre, cargo, retribución. Solo datos publicados; sin estimar ni inferir.
3. **Parlamento:** Congreso y Senado: asignaciones por cargo (Mesa, portavoces, presidentes de comisión); ya hay diputado y senador base (congreso.es/regecodip).
4. **Autonomías (opcional, 1-2 de muestra):** presidente autonómico y consejeros (portales de transparencia).
5. **Dónde se desglosa el gasto:** documentar el camino exacto (qué página, qué cuadro, qué sección y artículo) para que Joel lo encuentre solo: IGAE (arts. 10 y 11 por sección), Portal de Transparencia, BOE, Congreso/Senado.
6. **Contraste:** total del gasto en altos cargos (IGAE) frente a la suma de las retribuciones publicadas por cargo; decir qué falta por cuadrar.

## Dónde escribirlo
`explorador/espana-presupuesto.json` → `cargos_politicos` (añadir `por_cargo` y `por_persona`) y lectura en `explorador/vistas.html` (bloque «Cargos políticos», función `pEspana`). Regenerar `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`. Informe en `informes/research/AAAA-MM-DD-C68-sueldos-politicos.md`.

## Reglas
Solo cifras publicadas; sin recomendaciones; caso alcista/bajista solo si cambia la lectura; sin noticias de prensa como única fuente. Parar al 70 % de contexto.
