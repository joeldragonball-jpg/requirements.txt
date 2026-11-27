# Programas del 29-N-2026: PSOE, Vox y la izquierda, leídos en el texto original (27-nov-2026)

Neutral: ni recomendación de voto ni de operaciones. Niveles: [P] leído en el PDF del programa; [D] prensa/resumen; [VERIFICAR] no contrastado.
Sustituye, para estos tres bloques, la limitación del informe del 26-nov (`2026-11-26-programas-elecciones-29n.md`), que no pudo extraer el PDF del PSOE.

## Método y accesos (sin saltar bloqueos)
- Descargas simples con curl/WebFetch, sin trucos anti-bot. Texto extraído con `pdftotext`; búsqueda literal por regex en palabra completa (ojo: "MiCA" y "DLT" sin límite de palabra dan falsos positivos en "económica"/"adulto").
- Páginas citadas = nº de página del PDF (el pie impreso difiere: PSOE impreso = PDF+1; Vox impreso = PDF; Frente Amplio impreso ≈ PDF+5 [VERIFICAR]).
- Las webs oficiales de los partidos no se consultaron para el PSOE y Vox (no localicé el PDF en psoe.es / voxespana.es en las búsquedas); se usaron copias alojadas por medios:
  - PSOE: https://www.elindependiente.com/wp-content/uploads/2026/11/PROGRAMAPSOE29N26.pdf (114 págs.; 200 OK). La copia de democrata.es dio 403: no se insistió.
  - Vox: https://www.elindependiente.com/wp-content/uploads/2026/11/programa-elecct-vox.pdf (55 págs., "Es sentido común"; 200 OK).
  - Frente Amplio (Sumar + IU + Más Madrid + Catalunya en Comú, sin Podemos [D]): https://uh.gsstatic.es/sfAttachPlugin/4852063.pdf (copia en Última Hora, 151 págs., "Un programa como una casa"; 200 OK). La web oficial frenteamplio.info respondió 200 pero no seguí al PDF oficial [VERIFICAR que la copia coincide con la versión oficial].
  - Podemos (candidatura propia, Irene Montero [D]): NO LEÍDO. El único PDF localizado (democrata.es .../29n-programa-podemos-paz-casa-y-trabajo.pdf) devuelve 403 y podemos.info también 403. Marcado como no verificable. (Otro PDF que salió en búsquedas, ultimahora getContent/874005, es un programa antiguo "para un nuevo país", no el de 2026: descartado.)
- Fecha del programa (copias de medios, no oficial): no se comprobó contra el Congreso/JEC, donde los programas no se depositan como documento. [VERIFICAR] versión definitiva.

## Búsqueda literal de cripto y afines (cripto*, blockchain, tokeniz*, euro digital, MiCA, stablecoin, bitcoin, activos digitales, moneda(s) digital(es), DAC8)
HECHOS:
- PSOE: ninguna mención a criptoactivos, blockchain, tokenización, euro digital ni MiCA. Único hit: "criptografía poscuántica" (pág. 18, ciberseguridad): "facilitando la transición hacia soluciones de criptografía poscuántica". No es cripto-mercado. Relacionado con ahorro: medida 4 (pág. 15) "Poner en marcha la Cuenta de Ahorro e Inversión Financia Europa, con incentivos para canalizar el ahorro desde el ladrillo hasta inversión productiva" (sin detalle fiscal ni mención a activos digitales).
- Vox: cero coincidencias en las 55 páginas. (Tampoco "digital" asociado a dinero/finanzas; las coincidencias de "digital" son ventanilla única, menores en entornos digitales.)
- Frente Amplio: una sola mención, pág. 137 (capítulo UE): "Financiaremos el presupuesto europeo no solo con contribuciones nacionales, sino también con nuevos recursos propios, como por ejemplo la fiscalidad justa de las empresas digitales y de las criptomonedas." Es una propuesta de recurso propio de la UE, no una regulación nacional ni un tipo concreto. Sin MiCA, tokenización, euro digital ni blockchain.
- Podemos: [VERIFICAR] sin acceso al texto.

## PSOE ("La fuerza de seguir avanzando") [P]
HECHOS (cita literal breve, pág. PDF):
- IRPF/ahorro: "Mantener intactos los dos primeros tramos (19% hasta 6.000 y 21% hasta 50.000) y elevar los tipos a partir de ahí, llegando progresivamente a un tipo máximo del 35% para rentas del capital superiores a 300.000" (medida 130, pág. 48). Hoy ya "elevado al 30%" por encima de 300.000 (pág. 36). Mínimo exento por descendiente convertido en "crédito fiscal reembolsable" (134, pág. 49). Deducción estatal en IRPF "condicional a la evolución de los precios" (88, pág. 37). Exención IRPF de ganancias por venta de vivienda a proveedores asequibles (46, pág. 28).
- IVA: sin rebaja comprometida; solo seguimiento a que "cualquier rebaja del IVA de los alimentos básicos llegue al precio final" (94, pág. 38).
- Sociedades: no hay cambio de tipo general; "Ley de Salarios Justos": más tributación a cotizadas con ratio ejecutivo/mediana >100 a 1 y tramo superior desde 200 a 1 (133, pág. 48).
- Patrimonio: "tributación complementaria de los grandes patrimonios" como fuente de ingresos (127, pág. 47); en págs. 36 recuerda medidas contra bonificaciones autonómicas del Impuesto sobre el Patrimonio. Sin tipos nuevos en el texto.
- Otros impuestos: tasa a "tecnooligarcas"/IA (131); tasa a viajes de lujo (132); tasa Tobin "del 0,2% al 0,4%", sobre cotizadas con capitalización >1.000 M€ (pág. 49).
- Déficit/deuda: "Hemos reducido el déficit público desde el entorno del 10 % del PIB de la pandemia hasta menos del 2,5 % en 2025" (pág. 47); "Mantendremos una senda decreciente de las ratios de deuda y déficit sobre PIB" (126); Plan Fiscal y Estructural de Medio Plazo a Bruselas en primavera de 2027 con previsiones avaladas por AIReF (125); asunción parcial por el Estado de 83.000 M€ de deuda autonómica (231, pág. 61); financiación autonómica con 21.000 M€ adicionales (229, pág. 60). Sin cifra objetivo de déficit.
- Pensiones: "Blindar constitucionalmente el sistema público de pensiones y su revalorización conforme al IPC" (100, pág. 40); aportación de empresas con beneficios que hagan ERE (pág. 40).
- Vivienda: "parque público estatal de 100.000 viviendas" (42, pág. 28); programa TU CASA 10.000 M€ con préstamos de hasta 50.000 € sin intereses (ya lanzado, pág. 26).
OPINIONES/SESGOS: texto de campaña en primera persona; atribuye logros al propio Gobierno ("hemos…") sin fuente. Las cifras de déficit de 2025 son suyas [VERIFICAR con IGAE/Eurostat]. Cuantificación de ingresos de las nuevas figuras: no figura en el texto [VERIFICAR].

## Vox ("Es sentido común") [P]
HECHOS:
- IRPF: "Simplificación y bajada del IRPF. Reducción del tipo aplicable del IRPF para cada contribuyente o familia en función del número de hijos" (medida 2, pág. 7). No fija tipos ni tramos.
- IVA: "Rebaja del tipo reducido y del tipo general del IVA atendiendo prioritariamente a productos esenciales" (pág. 7); IVA 0 % en primera vivienda habitual nueva (34, pág. 20).
- Sociedades: "Reducir el tipo del Impuesto de Sociedades" sin cifra (pág. 7).
- Patrimonio/Sucesiones: no figura mención a esos impuestos (búsqueda "Patrimonio", "Sucesiones", "Donaciones": solo patrimonio histórico/inmobiliario/natural). Fiscalidad "agravada y disuasoria" para compradores no comunitarios y operaciones especulativas de fondos o sociedades (pág. 21).
- Déficit/deuda: "Reducción de la deuda pública. Compatibilizar la rebaja de impuestos con la financiación de los servicios públicos esenciales, mediante el control del déficit, la eliminación del gasto superfluo e ideológico y el impulso del crecimiento" (3, págs. 7-8). Sin cifras.
- Pensiones: "Garantizar la sostenibilidad del sistema de pensiones… Una economía más productiva es la garantía de sostenibilidad de las pensiones" (7, pág. 8). Sin mención a la revalorización con el IPC.
- Vivienda: bonificación 100 % del ITP en primera vivienda habitual de segunda mano, recuperar deducción por inversión en vivienda habitual (34, pág. 20); desalojo de okupación "en menos de 24 horas" (31, pág. 20); acceso con "prioridad nacional" a vivienda protegida (27, pág. 19); autónomos: cuota cero si ingresos < SMI y desde 50 € (pág. 7); gravamen sobre remesas (21, pág. 16).
OPINIONES/SESGOS: sin costes ni compensación de ingresos; no hay estimación de impacto fiscal en el texto. Cualquier valoración de cuadre (p. ej. de Rankia) es [D] ajena al programa.

## Frente Amplio (Sumar/IU/Más Madrid/Comuns) [P, copia de medio]
HECHOS:
- IRPF: "Bajaremos el IRPF a las rentas del trabajo de hasta 27.000 euros" y que quien cobre el SMI no pague IRPF; "elevaremos progresivamente los tipos marginales hasta alcanzar el 52 % para rentas a partir de 300.000 euros"; eliminar deducciones por planes de pensiones privados individuales (apartado 3.3, pág. 46). Acercar rentas del capital a las del trabajo (hoy 19-30 % vs 19-47 %, según el texto).
- IVA: bajar IVA a peluquerías y veterinarios (general a reducido), pañales (a superreducido), sin gluten 0 %; "IVA progresivo de la luz" (3.4, pág. 47).
- Sociedades: "tipo mínimo efectivo del 20 % sobre el resultado contable ajustado" para grandes grupos; recuperar gravamen especial del 1,2 % a la banca (3.1, pág. 44); fin del régimen especial de SOCIMI y EDAV (págs. 17, 44); Impuesto sobre Servicios Digitales hasta el 15 % (pág. 45).
- Patrimonio: Impuesto de Solidaridad de las Grandes Fortunas desde 1 M€ con mínimo del 2 %, +2 puntos y +3 desde 50 M€ (3.2, pág. 45); "Tasa Zucman" del 3 % anual sobre patrimonio neto >50 M€ (pág. 45); impuesto estatal a grandes herencias (págs. 45-46).
- Déficit/deuda: sin objetivo de déficit ni senda fiscal en las búsquedas ("déficit", "reglas fiscales", "senda"); sí condonación de deuda autonómica y alivio local (cap. 11.2/12.2, índice pág. 4) [VERIFICAR contenido: no lo leí entero]. Gasto comprometido: sanidad 8 % del PIB, educación 7 % del PIB (2030), vivienda 1 % del PIB (~17.000 M€/año), prestación por crianza 200 €/mes por menor, medioambiente 3,5 % del PIB (págs. 7-8, 10, 19, 21).
- Pensiones: "blindaje constitucional… de su revalorización" con el IPC y "pensión mínima igual al SMI" (4.3, pág. 57); mejorar ingresos de la Seguridad Social con destope progresivo de bases (pág. 47).
- Vivienda: "1 % del PIB anual (aprox. 17.000 M/año)" para "un gran parque público de 1,5 millones de viviendas en alquiler asequible" (págs. 7, 10); tope de alquiler vinculado al 25 % de ingresos del hogar (págs. 7, 13).
OPINIONES/SESGOS: programa muy extenso (151 págs.; "909 propuestas" según agregadores [D]); la recaudación esperada no se cuantifica de forma agregada en lo leído [VERIFICAR].

## Podemos
[VERIFICAR] No leído (403 en democrata.es y podemos.info). Solo resumen de prensa [D]: lema "Así de básico: paz, casa y trabajo", alquileres un 40 % más baratos por ley, SMI 1.800 €, jornada de 30 horas (democrata.es/elecciones-generales-espana/programa-electoral-podemos-29n/). Sin dato sobre cripto.

## Lectura cruzada (sin juicio de valor)
- Cripto/tokenización/MiCA/euro digital: ninguno de los tres programas leídos (PSOE, Vox, FA) trata la regulación cripto; el único dato es la propuesta de FA de gravar "criptomonedas" como recurso propio de la UE. [D, del informe del 26-nov] Vox presentó enmienda de devolución a la ley de transposición de DAC8: no está en su programa.
- Fiscalidad del ahorro: PSOE (hasta 35 % en rentas del capital >300.000 €) y FA (acercar capital a trabajo; 52 % marginal >300.000 €) suben; Vox solo anuncia bajadas genéricas.
- Todos blindan o garantizan pensiones salvo Vox, que no cita el IPC; PSOE y FA proponen blindaje constitucional.
- [ESPECULACIÓN] No se evalúa viabilidad ni impacto en mercados.

## Pendiente
- Leer Podemos desde fuente accesible; comprobar la web oficial del PSOE/Vox/FA; leer FA caps. 11-12 (deuda autonómica).
