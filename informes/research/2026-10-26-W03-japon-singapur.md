# W03 · Regulación por países: Japón (T06) y Singapur (T08)

Sesión del 25-oct-2026 (nombre de archivo del 26-oct según la rotación). Informativo: no es recomendación de compra ni de venta. Etiquetas: [P] = documento oficial leído; [S] = prensa o despacho; [VERIFICAR] = sin confirmar; [ESPECULACIÓN] = opinión o previsión.

## Resumen de lo cambiado en `explorador/regulacion.json`

| País | Tema | Antes | Ahora |
|---|---|---|---|
| Singapur | Ley marco | 5, [S] | 5, **[P]** (nota y directrices de la MAS sobre DTSP) |
| Singapur | ETF | sin dato | **0, [P]** (no hay ETF cripto para minoristas) |
| Singapur | Tokenización | 1, [P] | 1, [P]; letras vencidas el 23-oct, sin más subastas listadas |
| Singapur | Custodia | sin dato | **5, [P]** (PS-G03: cuenta fiduciaria y 90 % en frío) |
| Singapur | CBDC | 1, [S] | 1, **[P]** (comunicado de la MAS de 13-nov-2025 y web de letras) |
| Japón | Tokenización | sin dato | **5, [P]** (FSA, 20-oct-2026) |
| Japón | Custodia | sin dato | **4, [P]** (FSA, explicación de la reforma, abr-2026); el 95 % queda [VERIFICAR] |
| Japón | CBDC | sin dato | **1, [P]** (informe de progreso del Banco de Japón, jun-2026) |
| Japón | ETF | 0, [S] | sigue [S]: no consta decreto ni anuncio de la JPX |

## Singapur

**Hechos [P]**
- Letras tokenizadas: la web de la MAS lista solo dos: TD26100F (S$1 M, emisión 23-sep, vence 30-sep) y TD26101Z (S$10 M, emisión 9-oct, vence 23-oct), solo para institucionales y sin resultados publicados (mas.gov.sg, página de MAS Bills tokenizadas). La previsión anterior de «vence el 23-oct» ya está cumplida; no hay más subastas anunciadas.
- CBDC mayorista: el 13-nov-2025 la MAS anunció la primera emisión real de dólar de Singapur mayorista y el uso por DBS, OCBC y UOB para liquidar préstamos interbancarios a un día en la SGD Testnet. El 9-oct-2026 el director gerente (Chia Der Jiun) dijo que el siguiente paso es liquidar letras tokenizadas con CBDC mayorista y describió BLOOM como plataforma de liquidación con dinero digital (depósitos tokenizados y stablecoins reguladas); no da fechas.
- Stablecoins: el discurso del 9-oct repite que la MAS consultó el marco de stablecoins de una sola moneda (MAS-SCS), sin plazo de ley (ya recogido en la ficha, consulta P015-2026).
- Custodia: las directrices PS-G03 (2-abr-2024, revisadas el 19-sep-2024) exigen a los proveedores de DPT cuenta fiduciaria segregada para los activos de clientes, 90 % mínimo de los activos de clientes sin conexión a internet y restricciones a prestar o hacer staking con DPT de minoristas; capítulo de custodia efectivo el 4-oct-2024. La MAS avisa de que, aun así, la recuperación tras una quiebra puede tardar.
- Ley marco: desde el 30-jun-2025 los proveedores de servicios con tokens digitales solo a clientes de fuera (Parte 9 de la ley FSM) tienen que cesar; la MAS dijo que en general no daría licencia y no dio periodo transitorio. Esto significa que el servicio a clientes en Singapur sigue exigiendo licencia PS Act y el servicio solo al exterior desde Singapur queda restringido.
- ETF: respuesta parlamentaria de la MAS (5-abr-2021): los fondos de criptomonedas no están autorizados para minoristas. La consulta P014-2026 de jul-2026 sobre el Código de esquemas de inversión colectiva (leída entera con pdftotext) no menciona cripto. La declaración de ene-2024 sobre ETF de bitcóin al contado llegó por prensa [S].
- Política monetaria: la declaración de enero de 2027 saldrá «no más tarde del 29-ene» (calendario de la MAS); la de octubre fue el 14-oct.

**Caso a favor (de la postura de Singapur)**: reglas de custodia claras y exigibles, licencia obligatoria, pruebas de CBDC mayorista con bancos reales; da certidumbre a quien opera con licencia.
**Caso en contra**: acceso restringido para minoristas (sin ETF, sin staking ni préstamo), licencias escasas, pruebas pequeñas (S$1 M y S$10 M) y sin calendario de producción.
**Qué cambia para XRP/XLM**: nada directo en la ficha: ninguno de los documentos nombra XRP ni XLM. Lo relevante es que la liquidación con dinero tokenizado se hace en redes de la MAS, no en XRPL ni Stellar [S: sin notas de Ripple o Stellar sobre BLOOM en esta sesión]. Ripple tiene licencia MPI en Singapur (según Ripple y prensa; no se localizó el texto de la MAS sobre su ampliación [VERIFICAR]).

## Japón

**Hechos [P]**
- Tokenización: los security tokens ya están regulados en la FIEA desde 2019 (definición «electronic record transferable rights», con la excepción para inversores restringidos). La FSA presentó el 20-oct-2026 (primera sesión del grupo de estudio sobre finanzas digitales y descentralizadas) sus temas: stablecoins y tokenización de depósitos, security tokens, DEX/DeFi, sistema de anotación en cuenta y liquidación más rápida; el foro de finanzas «on-chain» prepara una hoja de ruta con resumen intermedio a principios de 2027 (estrategia de la FSA del 21-jul-2026). El volumen acumulado de security tokens creció hasta dic-2025 (gráfico sin cifra legible en mi extracción: [VERIFICAR]).
- Custodia: la FSA, en su explicación de la reforma de abril de 2026, indica que la regulación actual (gestión «en principio en cold wallet») se traslada a la FIEA; añade fondo de responsabilidad (art. 46-5) para compensar fugas, regulación de proveedores de sistemas clave de custodia, control de externalización, préstamos de cripto de clientes como actividad regulada, y la obligación de no permitir transferencias inmediatas a billeteras no alojadas tras abrir cuenta (período de reflexión, a fijar por orden ministerial). El 95 % mínimo en cold wallet proviene de despachos de 2020 [S].
- Ley marco (ya en ficha): promulgada el 23-jul-2026. La FSA justifica la reforma [P, abr-2026] con que ya hay más de 14 millones de cuentas de cripto en Japón (cerca del 70 % de titulares con ingresos anuales inferiores a ¥7 M), que los ETF cripto cotizan en EE. UU. y que hacen falta reglas contra el uso de información privilegiada, que se crean en esta reforma.
- CBDC: el informe de progreso del Banco de Japón (jun-2026) concluye que «hoy no está decidido si se emitirá» y que se decidirá en el debate nacional; las pruebas de rendimiento llegaron a 50.000 transacciones por segundo con la carga mixta sin obstáculo técnico insalvable. Informe conjunto de ministerios y Banco el 19-jun-2026; 11.ª reunión del consejo de enlace con acta del 2-jul-2026.
- Política monetaria: reunión del BoJ el 29-30 oct con Informe de Perspectivas el 30-oct; siguiente 17-18 de diciembre (calendario oficial del BoJ).

**Caso a favor**: marco claro con registro y reglas de custodia reforzadas, camino hacia fiscalidad separada del 20 % (condicionada a la reforma) y hacia ETF, piloto de CBDC prudente.
**Caso en contra**: el cuerpo principal de la reforma aún sin fecha firme (como tarde el 23-jul-2027), ETF cripto todavía no permitidos y sin decreto localizado, el yen digital sin decisión y la tokenización de valores todavía en fase de estudio.
**Qué cambia para XRP/XLM**: el RLUSD en Japón vía SBI VC Trade ya consta en la ficha de stablecoins; la nueva custodia FIEA y la información obligatoria sobre cada criptoactivo afectan a qué listados mantienen los exchanges registrados (regla de «criptoactivos específicos» en la reforma fiscal). Sin dato nuevo sobre XRP o XLM en esta sesión.

## Qué quedó [VERIFICAR]
- Japón: cifra de security tokens emitidos; porcentaje de cold wallet en la norma vigente (e-Gov); orden del gabinete con la fecha del cuerpo principal; ETF.
- Singapur: texto de la MAS sobre la licencia ampliada de Ripple; enmiendas concretas al reglamento de servicios de pago sobre custodia; si hay productos cripto cotizados para acreditados en SGX; declaración de ene-2027 (día exacto).

## Nota de método
- Los PDF en japonés de FSA y Banco de Japón no se leen con `pdftotext` en este equipo (faltan las tablas de fuentes): se leyeron con pdf.js en el navegador integrado, abriendo una página local temporal que carga los PDF (no se saltó ningún control anti-bots; las webs respondieron 200 a curl).
- La web de la MAS y los PDF se leyeron con WebFetch/curl sin problemas.

## Seguridad
- No se escribió ninguna clave ni secreto; no se lanzó ningún workflow ni se llamó a la API de Anthropic.
- Se usó un servidor local temporal (127.0.0.1) solo para visor de PDF; no se subió nada al repo.
- Pendiente de commit (lo hace la sesión principal con el OK de Joel).
