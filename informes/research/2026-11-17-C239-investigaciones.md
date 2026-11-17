# C239 · España: investigaciones y fondos públicos — pasada del 17-nov-2026

**Entrega:** `explorador/espana-investigaciones.json` (2 casos nuevos). Complementa, sin duplicar, el caso `adif-transportes-fondos-ue` de `explorador/espana-judicial.json` (ya cubría Fiscalía Europea 20-mar/6-nov, Tribunal de Cuentas PRTR-Adif, CIAF Adamuz/Urda y la pieza de obra pública de la Audiencia Nacional). Presunción de inocencia: nadie aparece como culpable; investigar o pedir documentos no es condena. M€ = millones de euros.

## 1. Adif / Transportes: qué cambia
- **Sin novedad oficial** localizada tras el comunicado de la Fiscalía Europea del 6-nov-2026. Limitación: el listado general de la web de la Fiscalía Europea devolvió error 404 al filtrar por país, así que «sin novedad» se apoya en búsquedas [VERIFICAR].
- Lo posterior a la nota oficial del 2-feb-2026 sobre la pieza de obra pública (Audiencia Nacional) sigue solo por prensa [S]: unificación de causa con 14 imputados (mar-2026), petición de 10 expedientes a Transportes (abr-2026), envío de un nuevo contrato por Adif (sep-2026). No se ha leído ninguna de esas crónicas entera [VERIFICAR].

## 2. Hallazgo nuevo: pulseras de violencia de género (Igualdad)
**Hechos (nivel P, leídos enteros):**
- **12-nov-2026.** La Fiscalía Europea (Madrid, con la UCO) realiza «medidas de investigación» en el Ministerio de Igualdad y en el Tribunal de Cuentas por un posible fraude con fondos de la UE destinados a pulseras telemáticas. La investigación «se inició el pasado año». Sin contrato, personas ni importe. [Comunicado](https://www.eppo.europa.eu/media/news/spain-investigative-actions-ministry-equality-and-court-auditors-probe-fraud-involving-monitoring-2026-11-12_en)
- **22-sep-2026 (nota 23-sep).** El Tribunal de Cuentas (informe n.º 1695, auditoría no penal) analiza los contratos de 2018, 2021 y 2023: 102,6 M€ en total, 42,6 M€ el de 2023 (financiado en parte con el PRTR). Fallos de dispositivos y geolocalización, 123 requerimientos judiciales sin respuesta hasta oct-2024, ocho recomendaciones. [Nota](https://www.tcu.es/es/Comunicacion-y-Espacio-Divulgativo/El-Tribunal-de-Cuentas-detecta-deficiencias-en-la-contratacion-y-seguimiento-del-sistema-telematico-de-medidas-de-alejamiento-para-proteger-a-las-victimas-de-violencia-de-genero/)
- **BOE-B-2023-34723.** Contrato de 2023 adjudicado el 10-oct-2023 a Vodafone España, S.A.U. por 35.226.395,43 € (35,2 M€), 2 ofertas, procedimiento abierto acelerado, marcado como fondos UE (programa C22.I04.P03). [BOE](https://www.boe.es/diario_boe/xml.php?id=BOE-B-2023-34723)
- Comprobación de unidades (inferencia mía [VERIFICAR]): 35,23 M€ × 1,21 = 42,6 M€, que coincide con la cifra del Tribunal de Cuentas; probablemente 35,2 M€ es sin IVA y 42,6 M€ con IVA.

**Lo que NO consta en fuente oficial:** que el contrato investigado sea el de 2023 (inferencia por objeto y fondos UE), el importe investigado, las personas o empresas investigadas y el tipo de diligencia (registro o requerimiento).

**Prensa [S] y sesgos:** las cifras circulan contradictorias (6,4 M€ Artículo 14; 45 M€ OKDiario; 100 M€ ESdiario) y no se atribuyen a la investigación. Artículo 14 habla de una UTE Vodafone-Securitas; el BOE solo recoge a Vodafone. Según crónicas, Igualdad dice que la UCO fue a pedir documentación, que los fondos se usaron «correctamente» y que los fallos se corrigieron en 2024 (versión del Ministerio, no verificada). Hay medios muy críticos con el Gobierno y otros afines; sirven solo para localizar fuente oficial. Solo leí titulares y extractos de la prensa.

**Caso alcista/bajista (para quien siga el gasto público, sin opinión de inversión):** a favor de la gestión, el propio Tribunal de Cuentas dice que las graves deficiencias «han sido resueltas» y que se pidió auditoría externa en nov-2025; en contra, que la Fiscalía Europea ya investigaba desde 2025 y el Tribunal registra fallos durante casi toda la vigencia del contrato.

## 3. Contexto: otros casos de la Fiscalía Europea en España (2026)
Tres comunicados leídos: condena firme del 28-sep (95.000 € de indemnización a Murcia), condena firme del 5-oct (daño 26.000 €) y dos detenidos el 15-abr por 3,3 M€ en Zamora y Salamanca. Son fraudes de particulares a subvenciones; no se relacionan con Adif ni Igualdad.

## 4. Pendiente [VERIFICAR]
1. PDF completo del informe 1695 (importes por contrato, penalidades).
2. Expediente del contrato posterior (adjudicación 2026) en la Plataforma de Contratación.
3. Nota oficial de Igualdad y posibles comparecencias en el Congreso.
4. BSC (ordenador cuántico) y mascarillas con la Fiscalía Europea: solo por prensa en esta pasada.
5. Sin acceso al listado de comunicados por país; revisar a mano.

## 5. Catálogo de fuentes (para MAPA-DE-FUENTES.md; no lo edité)
| Fuente | Uso | Estado |
|---|---|---|
| `eppo.europa.eu/media/news/<slug>` | Comunicados de la Fiscalía Europea | Chrome/navegador: OK por URL directa; listado con filtro: 404 |
| `tcu.es/.../resultados-de-las-fiscalizaciones/` | Informes con enlaces a PDF, resumen y nota | Chrome: OK (enlaces por JavaScript); API: no |
| `boe.es/diario_boe/xml.php?id=BOE-B-AAAA-NNNNN` | Anuncios de formalización | OK por script y navegador |
