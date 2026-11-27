# IA y chips: controles de exportación, Nvidia, TSMC, ASML, rondas, electricidad y regulación (27-nov-2026)

Método: búsqueda web + lectura de páginas. Sin acceso a bis.doc.gov ni sec.gov directos (no se abrieron); casi todo viene de prensa y despachos de abogados. Nada de esto es recomendación. Leyenda: [S] = fuente secundaria sin confirmar en primaria; [VERIFICAR] = datos contradictorios o sin primaria; [ESPECULACIÓN] = opinión o predicción. Los resultados de búsqueda eran densos en afirmaciones muy llamativas (dimisión de Huang, sonda SEC, salida a bolsa de Anthropic): tratarlas con cautela hasta ver la nota oficial.

## 1. Controles de exportación de EE. UU. a China (estado nov-2026)

HECHOS (con fuente):
- 15-ene-2026: BIS cambia la política de revisión de licencias de chips de IA avanzados hacia China/Macao, de presunción de denegación a caso por caso para chips por debajo del tope de rendimiento, con prueba previa en laboratorio independiente de EE. UU. Fuente: Federal Register 15-ene-2026 (govinfo.gov, doc. 2026-00789); resumen Morgan Lewis y Covington (ene-2026).
- H200: Trump lo aprobó en dic-2025 con una comisión del 25 % para el Estado [S]. Hacia mediados de mayo-2026 se habrían autorizado unas 10 empresas chinas (Alibaba, ByteDance, Tencent, JD) [S, Tom's Hardware/NBC].
- 16-nov-2026: BIS publica la norma provisional final "Addressing Remote Access to Advanced Semiconductors" (doc. FR 2026-23529; publicación prevista 19-nov). Nueva sección 744.24: licencia para centros de datos en cualquier país con más de 12.000.000 de TPP agregado para empresas con sede en China, Macao u otros D:5; cinco destinos nuevos con licencia (Indonesia, Malasia, Singapur, Tailandia, Brasil); presunción de denegación general; centros ya existentes con 90 días para pedir licencia; rescinde formalmente la «AI Diffusion Rule» (incl. ECCN 4E091). Comentarios a 60 días. Fuente: Gibson Dunn (18-nov-2026) y Skadden (nov-2026) [S, falta el texto del FR].
- La ley Remote Access Security Act (H.R. 2683) pasó la Cámara el 12-ene-2026; no es ley [S, Gibson Dunn].

Nvidia y China:
- 17-nov-2026, resultados 3T del ejercicio 2027: según prensa (Reuters/Bloomberg Government, vía TimesLive 18-nov), la CFO Colette Kress dijo en la llamada «we are no longer shipping licensed Hopper data center products to China»; los envíos Hopper a China fueron 2.400 M$ en el trimestre (~2 % de ingresos) y la guía excluye ingresos de computación de centros de datos en China. H20 y H200 son Hopper. Blackwell y Rubin siguen sin poder venderse a China [S]. Motivo: no explicado; la prensa apunta a que Pekín restringió las importaciones de H200, y Reuters habló de unos 600.000 H200 almacenados en Hong Kong esperando aprobación [S] [VERIFICAR].
- Cifras del trimestre según fourweekmba (web de baja fiabilidad, 403 al abrir): ingresos 115.800 M$ (+103 % interanual), guía 4T 130.000 M$ ±3 %, margen bruto previsto 71-72 % [S][VERIFICAR contra nvidianews.nvidia.com].
- B30A (Blackwell recortado): no hallé confirmación de estado de licencia [VERIFICAR].

## 2. Respuesta de China

- Tierras raras: China suspendió en nov-2025 las ampliaciones de controles de oct-2025 (anuncios 61/62 de MOFCOM); según The National (9-nov-2026) y Global Trade Alert, en nov-2026 la pausa se prolongó hasta enero de 2027 (Anuncio 2026/58) [S]. Las licencias de abril de 2025 para tierras raras medias y pesadas siguen vigentes. Tom's Hardware daba otras fechas de fin (27-nov-2026 para tecnología; 10-nov para la norma de producto extranjero): fechas sin reconciliar [VERIFICAR en MOFCOM].
- Huawei Ascend: BIS advirtió en 2025 que usar Ascend puede infringir controles de EE. UU. (Covington, ago-2025). No obtuve datos nuevos de producción o ventas de Ascend en nov-2026 [VERIFICAR].
- Pekín restringe la importación de H200 [S, ver arriba]; Tom's Hardware había informado antes de aprobaciones caso por caso para ByteDance y Tencent. Se contradicen en el tiempo.

## 3. Investigaciones en EE. UU. sobre Nvidia

- Dimisión de Jensen Huang: según nota de Nvidia (investor.nvidia.com, 12-nov-2026, "NVIDIA Announces CEO Transition") dimitió como presidente, CEO y consejero con efecto inmediato; Colette Kress, CEO interina; Harvey C. Jones, presidente del consejo. Prensa: el presidente del consejo dijo que no pretenden reincorporarlo (SCMP, ~17-nov). CONTRADICCIÓN: la portada de nvidianews.nvidia.com leída hoy mostraba un titular de 23-nov «NVIDIA Board Reinstates Jensen Huang as President, CEO and Board Director»; una segunda búsqueda no lo encontró [VERIFICAR con urgencia en la nota oficial].
- Causa reportada de la salida: personal (relaciones con una ejecutiva ligada a Megaspeed), según prensa [S] [VERIFICAR]; no repito detalles personales sin fuente primaria.
- SEC: el Wall Street Journal habría informado de una investigación civil sobre si Nvidia engañó a inversores en sus divulgaciones de ventas internacionales (cambio de metodología, dejó de desglosar ingresos vía Singapur). Ni la SEC ni Nvidia lo confirman. No hay fuente que hable de contabilidad de ingresos en sentido estricto [S][VERIFICAR]. Antecedente verificable: acuerdo de 5,5 M$ de la SEC con Nvidia en 2022 (cripto-minería).
- Contrabando: DOJ cerró la red «Operation Gatekeeper» (Houston): Hao Global se declaró culpable en oct-2025 de exportar ≥160 M$ en H100/H200; dos chinos acusados en dic-2025 (justice.gov). Investigación penal del DOJ sobre el cliente de Nvidia Megaspeed (Singapur) por posible desvío (SCMP/The Hill, 2026) [S]. Supermicro: segunda citación de la SEC (28-abr-2026) [S, Fortune 13-may-2026]. BIS: ~420 M$ en sanciones y decomisos por contrabando de chips en 12 meses [S, Fortune].

## 4. TSMC y aranceles Taiwán

- Ventas de octubre 2026: 586.890 millones de NT$ (nota de TSMC pr.tsmc.com/english/news/3349, 10-nov-2026; 6-K en sec.gov): +14,7 % mensual, +59,7 % interanual; enero-octubre 4,486 billones de NT$ (+43,3 %). Máximo del año. Guía 4T según prensa: 52.300-54.300 M$ [S].
- Aranceles: acuerdo de comercio recíproco EE. UU.-Taiwán (hoja informativa USTR, feb-2026): tope del 15 %; trato preferente en el futuro arancel Sección 232 a chips (cuota libre de arancel hasta 2,5 veces la capacidad prevista en EE. UU. durante la construcción, 1,5 veces después); 250.000 M$ de inversión taiwanesa. No he verificado si el legislativo taiwanés lo ratificó ni si el 232 de chips se ha emitido [VERIFICAR].

## 5. ASML

- 3T 2026 (prensa, fechas dispares 14 o 27-oct): ventas récord ~11.700 M€, margen bruto 57,5 %, beneficio ~5.000 M€; guía 2026 elevada a 44.000-45.000 M€; 4T 14.200-15.200 M€; la oferta para 2027-2028 no cubre la demanda [S, Yahoo/Pulse2]. Pedidos del trimestre y peso de China en 2027: no encontrados [VERIFICAR en asml.com].

## 6. Rondas y valoraciones

- OpenAI: según Bloomberg (vía SiliconANGLE, 6-nov-2026), ~11.000 M$ recaudados a 1,25 billones de $, con hasta ~9.000 M$ más previstos; ronda previa de 122.000 M$ a 852.000 M$ en marzo [S, filtración con fuentes anónimas].
- Anthropic: ronda privada de 65.000 M$ a 965.000 M$ en mayo-2026 [S, Yahoo/Euronews]. S-1 público el 26-oct-2026 (TechCrunch) con ingresos 1S-2026 de 16.300 M$ y beneficio operativo trimestral; precio de salida a bolsa 83 $/acción el 18-nov y debut en Nasdaq (ANT) el 19-nov, ~1,5 billones de $ diluido, apertura 111,50 $ [S, TechCrunch/TechRepublic; cifras varían entre medios]. [VERIFICAR en EDGAR]. Nota de sesgo: yo soy un modelo de Anthropic; contrastar con fuentes independientes.
- xAI: sin ronda nueva en nov-2026; según una fuente fue absorbida por SpaceX el 2-feb-2026 a 250.000 M$ [S][VERIFICAR].
- Cautela [ESPECULACIÓN]: las valoraciones de 1-1,5 billones dependen de crecimiento futuro; caso bajista = burbuja/recorte de gasto; caso alcista = ingresos creciendo >10x interanual.

## 7. Electricidad de centros de datos

- PJM: el monitor de mercado atribuye ~29.400 M$ de costes de capacidad a la demanda de centros de datos y estima otros 5.000-10.000 M$ en la subasta de diciembre 2026 (para 2029/30); recomendó aplazarla. La subasta 2028/29 cerró en el tope de 325 $/MW-día; déficit de capacidad 6.831 MW [S, S&P Global 12-nov-2026]. FERC rechazó una subasta de reserva. Fecha exacta de la subasta: no confirmada [VERIFICAR en pjm.com].
- Modo Energy (10-nov-2026): 231 GW de centros de datos operativos y planificados (92 % en planificación/construcción) [S].
- EIA (Today in Energy id 67344): ventas récord de electricidad en 2026 por centros de datos e industria; ERCOT y PJM con mayor crecimiento hasta 2027 [S]. Precio residencial de 17,3 a 18,2 c/kWh según Shipley Energy [S].

## 8. Regulación de IA en EE. UU. (preemption federal)

- Orden Ejecutiva 14365 (11-dic-2025, "Ensuring a National Policy Framework for AI"): crea un grupo de litigio del DOJ contra leyes estatales; no anula leyes por sí sola; pide recomendación legislativa; excepciones: seguridad infantil, infraestructura de centros de datos, uso estatal (DLA Piper, Jenner).
- Abril-2026: xAI demandó a Colorado (9-abr) y el DOJ se sumó (24-abr) contra la ley SB24-205; Colorado avanzaba una ley que la sustituya (Axios, Jenner) [S]. No hallé demanda del DOJ contra California [VERIFICAR].
- Congreso: sin ley de preemption; precedente del voto 99-1 del Senado (2025); borrador "Great American AI Act" (Obernolte-Trahan) sin presentar formalmente; Markey presentó proyecto contra la orden [S, resultados hasta ~jun-2026]. Estado en nov-2026: no verificado [VERIFICAR].

## Lista [VERIFICAR]
1. ¿Huang reincorporado el 23-nov o no? Leer nvidianews.nvidia.com y 8-K en sec.gov.
2. Cifras del 3T FY27 de Nvidia (ingresos 115,8 mM$, guía 130 mM$) en la nota oficial; motivo del cese de envíos Hopper a China.
3. Existencia y alcance de la sonda de la SEC (solo WSJ, sin confirmar) y la de Megaspeed.
4. Texto del Federal Register 2026-23529 (fecha de publicación efectiva) en federalregister.gov/bis.doc.gov.
5. Fechas exactas de fin/extensión de la pausa china de tierras raras (MOFCOM 2026/58).
6. Estado de B30A, Huawei Ascend y las 600.000 H200 en Hong Kong.
7. Ratificación taiwanesa del pacto comercial y estado del arancel 232 a chips.
8. ASML: pedidos 3T 2026 y peso de China; fecha de la publicación.
9. Ronda OpenAI (1,25 billones; Bloomberg anónimo) y cifras de la OPV de Anthropic en EDGAR.
10. xAI: absorción por SpaceX y valoración.
11. Fecha y resultado de la subasta PJM de diciembre.
12. Proyectos de ley de preemption y litigios DOJ en curso (Colorado, California) a nov-2026.

Acceso: fourweekmba.com devolvió 403 (no se evitó). No se abrieron bis.doc.gov ni sec.gov directamente.
