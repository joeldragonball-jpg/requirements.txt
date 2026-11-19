# PLANNING (autogenerado, no editar a mano) · 2026-11-19 08:10 UTC

Lo regenera `python scripts/construir_seguimiento.py` (el mismo que alimenta el Seguimiento del móvil y del PC), así que **Seguimiento y planning no pueden diverger**. `/research` sin argumento lee SOLO este archivo; con un ID, lee la fila de `research/COLA.md` y el prompt indicado aquí. Cuota: se mide con get_usage, no está aquí.

## Vista en 5 grupos (C131)
**Hoy (máx. 3):** W05 Verificación por lotes · Gemini ETF y flujos
**Periódicas (próxima):** W05 11-19 · W06 11-20 · W09 11-20 · W10 11-21 · W01 11-23 · W02 11-24 · W08 11-25 · W04 11-26 · W03 12-02 · W07 12-05
**Bloqueadas (6):** C79 (4-nov: AEAT OK. IGAE BOE y MENSUAL 12-24 OK con Ch) · C80B (Chrome no conectado; senate.gov y congress.gov blo) · C137 (Chrome para leer fechas oficiales) · C139 (Decidir con Joel si se añaden como países nuevos a) · C140 (Chrome conectado) · C235 (Joel pasa podcasts, canales y personas que sigue)
**Parciales (50):** C30 falta: Leer en ine.mx, eci.gov.in, CNE y gov.uk; confirma · C39 falta: 17-nov: 20 movimientos volcados a datos.json (305) · C42 falta: 18-nov 3.ª: ESMA, SFC y MAS leídos; VARA parcial.  · C58 falta: 18-nov: Rusia a P (Duma 450), India Lok Sabha 540/ · C59 falta: 17-nov: salario mínimo y fichas añadidos a indicad · C61 falta: 18-nov: vivienda vacía CN/IN/RU en null (sin fuent · …
**Hechas en 7 días (13):** C205, C206, C262, C264, C265, C266, C258, C259, C252, C253, C256, C257, C255

## Hoy (jue 2026-11-19): solo lo casi obligatorio
- R00 apertura ✓ · cierre ⏳ pendiente (desde las 22:00, cierre de EE. UU.) · racha 12 días
- Sin rutina fija hoy: elige por prioridad en las secciones de abajo.

## 🟣 Gemini del día (gratis, 1 consulta ligera de ~15 fuentes; Claude da el prompt, tú lo pegas en Gemini)
- Gemini del día: toca **ETF y flujos** · prompt `research/gemini/NOTICIAS-DIA.md` · ⏳ pendiente
- Norma: 1 consulta ligera al día (unas 15 fuentes), sin repetirla. Rutina G (C20): una rotación por día; si Gemini avisa de límite o llegas al 80 %, se para por hoy y se anota en «parada». La cuota se comparte con NotebookLM.
- Aviso de límite (antes del 2026-10-27): Una consulta de ~47 fuentes lanzada 2-3 veces agotó el límite; la cuota ya estaba gastada en NotebookLM.
- Aviso de límite (2026-10-27): Tras W03 Sudáfrica+Indonesia, Deep Research queda desactivado hasta las 04:00 (hora de Madrid) del 27-oct, con el uso general en ~4 %. Hizo 200+ búsquedas web aunque el prompt pedía máx. 15 fuentes: el tope del prompt no se respeta. Límite oficial de Deep Research sin confirmar; de momento, 1 Deep Research por ventana (reinicio 04:00).
- Aviso de límite (2026-10-31): Joel propone probar 2 Deep Research al dia (lleva ~7 % semanal con Pro alto). Se prueba unos dias; si Gemini avisa de limite, vuelta a 1. Anotar en sesiones cada lanzamiento y si hubo aviso.

## Rutinas W: lo que falta este periodo (sin día fijo; se hacen cuando haya hueco, de más atrasada a menos)
- W10 · Energía y geopolítica · ~2 % · fin de semana · último 2026-11-14 · `research/prompts/W10-*.md`
Hechas en este periodo: W01, W02, W03, W04, W05, W06, W07, W08, W09

## Research nuevo pendiente (por sección)
**Centro y revisión del cerebro (C)**
- C101 ◐ en parte · Centro · Endurecer workflows: permisos mínimos, requirements con hashes, Actions · Sonnet S · ~~1 % · ``
- C102 · Centro · Inventario de secretos y tokens fuera del repo (plantilla en privado/;  · Sonnet S · ~~1 % · ``
- C103 · Centro · Auditar el Worker de votos (Joel pega el código sin secretos) · Sonnet S · ~~1 % · ``
- C105 · Centro · Copias y recuperación: git bundle semanal y ensayo de restauración · Sonnet S · ~~1 % · ``
- C106 · Centro · Bots frecuentes al Worker (requisito si el repo pasa a privado) · Sonnet M · ~~3 % · ``
- C107 · Centro · Qué NO construir: ver qué hacen ya gratis OpenBB, Koyfin, TradingView y · Sonnet M · ~~3 % · ``
- C108 ◐ en parte · Centro · Criterios de medición y relleno de las 58 predicciones · Sonnet M · ~~3 % · ``
- C111 · Nivel C · Electricidad Europa por zonas con ENTSO-E · Sonnet S · ~~2 % · `Tras recibir el token de ENTSO-E como secreto, añade las zonas ES/FR/DE/IT/PT a leer_electricidad() sin mostrar el token`
- C117 · Nivel C · RAM/DRAM y centros de datos: ficha manual con fuentes [S] y proxy MU · Sonnet M · ~~4 % · `Busca solo fuentes públicas sobre precios DRAM/NAND y consumo eléctrico de centros de datos (IEA, EIA, comunicados); guarda en explorador/chips-manual.json con nivel S y fecha; marca [ESPECULACIÓN] en ciclos`
- C135 ◐ en parte · Países · Refrescar la historia con el bot de paneles, mini-serie bajo las 4 cifr · Sonnet M · ~~3 % · `Lee informes/research/2026-11-05-C133-paises-historia-mandatos.md (sección Pendiente). Añade scripts/indicadores_historia.py al flujo de actualizar_paneles sin API de Anthropic; en pPaises pon spark() de la serie bajo cada cifra grande; verifica en webs oficiales las fechas de mandato marcadas S en explorador/mandatos.json y súbelas a P solo si las lees.`
- C137 ◐ en parte · Países · Mandatos anteriores en el resto de países (como España): presidentes o  · Sonnet M · ~~4 % · `research/prompts/C137-mandatos-anteriores-paises.md`
- C138 ◐ en parte · Países · Cómo va la zona euro, la UE, las potencias y los BRICS: panel de bloque · Sonnet M · ~~4 % · `research/prompts/C138-bloques-euro-potencias-brics.md`
- C139 ◐ en parte · Países · Vigilar El Salvador y Argentina (indicadores, historia, mandatos) y, co · Sonnet L · ~~6 % · `research/prompts/C139-latam-el-salvador-argentina-venezuela-cuba.md`
- C140 ◐ en parte · Países · Leer en fuente oficial las fechas de mandato [S] (9 países) y las de Az · Sonnet S · ~~2 % · ``
- C144 ◐ en parte · Centro · Research a fondo: APIs y datos gratis (GitHub, Reddit, documentación of · Sonnet L · ~~6 % · `research/prompts/C144-apis-gratis-automatizar.md`
- C162 ◐ en parte · Órbita · Niveles y fallos legibles: etiquetar los 8 k vacíos de capas[].xrp, exp · Sonnet M · ~~2 % · `Etiqueta los k vacíos de capas[].xrp en datos.json (con la fuente que lo sostiene, no a ojo), explica en una línea los fallos de paneles.json y unifica la leyenda de niveles en un pie común`
- C173 ◐ en parte · Centro · Verificar noticias pendientes de prioridad alta y de más de 14 días (7- · Sonnet S · ~~3 % · ``
- C176 ◐ en parte · Centro · Verificar prensa 4-6 nov (7 noticias) · Sonnet S · ~~1 % · ``
- C179 ◐ en parte · Países · W11 refresco de 6 fichas políticas (China, Brasil, Sudáfrica, Indonesia · Sonnet S · ~~2 % · ``
- C186 · Research con Gemini (manual): qué muestran los mejores paneles de inversor parti · Sonnet S · ~~2 % · ``
- C203 ◐ en parte · Fichas por activo (XRP, XLM, BTC, oro, ETF mundial) con fuente, nivel, hechos y  · Sonnet M · ~~2 % · ``
- C208 · Capa «Mi cartera» sin importes con el importador CSV · Opus L · ~~4 % · ``
- C209 · Modo familia: vista reducida sin racha ni IA · Opus L · ~~2 % · ``
- C210 · Capas nuevas: flujos de ETF de XRP/XLM, stablecoins, vivienda y combustibles UE · Opus L · ~~4 % · ``
- C217 · Órbita: comparador de países como vista (2-4 países, mismo periodo) · Opus L · ~~3 % · ``
- C218 · Órbita: comparador de capas lado a lado · Sonnet M · ~~2 % · ``
- C221 ◐ en parte · Órbita: glosario flotante y definición en cada cifra · Sonnet M · ~~1 % · ``
- C222 · Órbita: pestaña Mercado con divisas por tipo, hora real por dato y segunda fuent · Sonnet M · ~~2 % · ``
- C223 · Órbita: rendimiento con muchos datos (carga por pestaña, listas virtualizadas) · Opus L · ~~3 % · ``
- C225 ◐ en parte · Research de noticias más fuerte: grandes potencias y España, conflictos y guerra · Sonnet L · ~~5 % · ``
- C229 ◐ en parte · Órbita · España: pack macro (IPC desglosado, EPA, afiliación, salarios/SMI y Eur · Sonnet L · ~~4 % · ``
- C230 ◐ en parte · Órbita · España: vivienda (precio, alquiler, esfuerzo por CCAA), deuda autonómic · Sonnet L · ~~4 % · ``
- C233 ◐ en parte · Órbita · España: energía (precio eléctrico OMIE/REE, combustibles vs UE, gas y d · Sonnet M · ~~3 % · ``
- C235 · Voces de otros ámbitos (bancos centrales, energía, política, economía) fichadas  · Opus M · ~~3 % · ``
- C236 ◐ en parte · IPC de EE. UU.: etiquetar «desestacionalizado / sin desestacionalizar» en móvil  · Sonnet S · ~~0,5 % · ``
- C238 ◐ en parte · Órbita · España: leyes nuevas y modificaciones (BOE, Congreso): estado, vigor y  · Sonnet L · ~~5 % · `research/prompts/C238-espana-leyes-boe.md`
- C239 ◐ en parte · Órbita · España: investigaciones y fondos públicos (Adif, Ministerio de Transpor · Fable L · ~~5 % · `research/prompts/C239-espana-investigaciones-fondos.md`
- C24 · Centro · Fiscal y legal: confirmar que el vigilante del Federal Register manda u · Joel S · ~0 % · ``
- C240 ◐ en parte · Formato de cifras: unidad y escala explícitas (M€, mil M€), punto de miles y com · Sonnet M · ~~2 % · `research/prompts/C240-formato-cifras-unidades.md`
- C241 ◐ en parte · Órbita · España: «a dónde va el dinero» (contratación pública PLACSP y subvencio · Sonnet L · ~~6 % · `research/LANZAR-FABLE-ESPANA.md`
- C245 ◐ en parte · Órbita · España: empleados de órganos constitucionales (Cortes, T. Cuentas, CGPJ · Sonnet S · ~~2 % · `Buscar la plantilla (nº de empleados) de Cortes Generales, Tribunal de Cuentas, CGPJ, Tribunal Constitucional, Consejo de Estado y Casa de Su Majestad el Rey en sus portales de transparencia/memorias/RPT y en el anexo de personal de los PGE; completar explorador/espana-empleados.json con fuente, fecha y nivel (P solo si se lee la fuente oficial; puestos presupuestados ≠ personas: [VERIFICAR]). Las 9 partidas de gasto sin plantilla (Deuda, Clases Pasivas, UE, entes territoriales, etc.) quedan null.`
- C247 ◐ en parte · Centro · Verificar prensa pendiente (3.ª tanda 10-nov: Irak/Ormuz, Brent, UE, IP · Sonnet S · ~~3 % · ``
- C254 ◐ en parte · Centro · Verificar con fuente las dudas abiertas por C252 (STEO de noviembre, st · Fable M · ~~3 % · ``
- C260 ◐ en parte · Países · Indicadores con la fecha más reciente (no solo media anual del Banco Mu · Sonnet L · ~~5 % · ``
- C261 ◐ en parte · Alertas de datos (C206): ajustar los umbrales de tipos y comprobar el primer avi · Sonnet S · ~~1 % · `Joel: pon tus umbrales en la sección [datos.umbrales_tipos] de alertas/config.toml (ahora son ejemplos: Fed 3,50/4,50 % y BCE 2,00/3,00 %). Tras el «sube», el workflow diario «Aviso de eventos» ejecuta alertas/datos.py: la 1.ª vez solo memoriza. Cuando llegue el primer aviso real, comprueba que los enlaces abren, que no pasa de 8 líneas y que no repite avisos; si sobra ruido, apaga partes en [datos] (rojos, tipos, noticias_p) o baja noticias_dias. Sin IA y sin lanzar workflows salvo que Joel lo pida.`
- C263 ◐ en parte · Cerrar huecos [VERIFICAR] del marco por cadenas: volumen de ODL, PDF del 3T-2026 · Sonnet M · ~~3 % · `Lee la lista «huecos» de privado/marco-iso20022.json (solo en el PC) y busca fuente primaria para cada uno: Ripple (volumen de ODL en XRP), PDF del informe del 3T-2026 de la SDF (stellar.org/quarterly-reports; la descarga abre un diálogo: pide a Joel que lo guarde en research/fuentes/), PDF del informe final de Project Acacia en rba.gov.au, docs de Ondo Chain, docs.canton.network (dominios privados y tráfico), documento primario de Quant, Swift sobre XDC, docs.hedera.com y Avalanche. Escribe los resultados SOLO en privado/marco-iso20022.json (con fuente, fecha y nivel) y regenera con python scripts/construir_tesis_privada.py; después python scripts/huellas_privado.py y python scripts/revisar_explorador.py. Nada de la tesis en el repo público.`
- C267 ◐ en parte · Órbita › Cadenas: tercera pasada de huecos públicos (Quant, XDC, IOTA, Plume, Po · Sonnet M · ~~3 % · `Sigue CLAUDE.md. Repo PÚBLICO: solo hechos con fuente. Lee la columna «falta» de la fila C264 en research/tareas.csv y las celdas null o con n=V de explorador/cadenas.json. Busca fuente PRIMARIA y léela en el navegador (Chrome si la web bloquea lectores: quant.network da 403; dtcc.com/news da 404 a lectores): licencias de Overledger en QNT, masternodes y Swift en XDC, socios de ADAPT/TWIN de IOTA en sus webs, papel de PLUME y registro en la SEC (EDGAR), finalidad, staking y comisiones de Polygon y BNB Chain, interoperabilidad de Hedera, si Stellar es la 1.ª o 2.ª red pública de DTC. Edita SOLO explorador/cadenas.json (celdas {t,f,u,d,n}; sin dato = null, nunca relleno) y, si cambia algo de la tesis privada, avisa para C263 sin escribir en privado/. Cierre: python scripts/revisar_explorador.py (0 avisos), construir_orbita.py, construir_movil.py, construir_seguimiento.py y esta fila a «hecha» con el recuento de celdas cerradas. Sin workflows ni API de Anthropic; commit y push solo con «sube».`
- C268 ◐ en parte · Órbita › Cadenas: qué se tokeniza en cada red por tipo de activo (deuda, accione · Sonnet L · ~~6 % · `Sigue CLAUDE.md y research/NORMAS-DETALLE.md. Repo PÚBLICO: solo hechos con fuente y fecha; nada de privado/ ni comparación con la tesis; sin «ganador». Contexto: la pestaña Cadenas (explorador/cadenas.json, vistas.html) ya responde «si la red se usa, ¿el token se demanda?» (columna Captura), pero NO dice qué tipos de activo se tokenizan en cada red. Joel lo ve así: cada red sirve más para deuda/bonos, acciones, materias primas (RWA), fondos o ETF, inmuebles, según los contratos que ofrece, el plazo de liquidación y el valor o la cantidad tokenizada. Tarea: añadir en cadenas.json un bloque «tipos_activo» por red con, para cada tipo (deuda y letras del Tesoro, fondos monetarios y ETF, acciones, materias primas/oro, crédito privado, inmuebles, otros), el valor tokenizado, nº de emisores o activos, los 2-3 productos principales, el estándar de contrato (p. ej. ERC-3643, permisos del XRPL, Stellar SEP) y el plazo de liquidación citado por la fuente. Fuentes: RWA.xyz (cuidado con las métricas «distribuido» y «representado»: ya hay trampas anotadas en la fila C264), páginas oficiales de los emisores (Franklin, BlackRock, Ondo, WisdomTree, Securitize, Superstate…), informes de las redes. Cada celda {t,f,u,d,n}; sin dato = null, nunca relleno; nivel P solo si lees la fuente. En vistas.html añade bajo la matriz una tabla «¿Qué se tokeniza en cada red?» con barras por tipo de activo, legible en tablet (≤1180 px; mira el semáforo cad-sm y el método de comprobar en el navegador, puerto 8797 de .claude/launch.json con la configuración «orbita» y construir_orbita.py antes de recargar). Cierre: python scripts/revisar_explorador.py (0 avisos), construir_orbita.py, construir_movil.py, construir_seguimiento.py, informe en informes/research/ y esta fila a hecha. Sin workflows ni API de Anthropic; commit y push solo con «sube».`
- C275 ◐ en parte · Países: revisar los 29 huecos de la matriz país × tema (celdas con «—») y los te · Sonnet L · ~~5 % · `Sigue CLAUDE.md. Repo PÚBLICO. En docs/orbita, pestaña Matriz país × tema hay 29 celdas vacías («—») y Países tiene 11 textos con «…». Lista con python los huecos desde el JSON de origen (explorador/paises.json o equivalente), prioriza por relevancia (G20, UE, Singapur, Corea, Emiratos) y rellena SOLO con fuente primaria oficial leída (banco central, supervisor, boletín oficial), con fecha y nivel; lo demás queda vacío (nunca relleno). Sustituye «null» del aviso por «vacío». Informe con huecos cerrados/abiertos. NO commit ni push.`
- C280 ◐ en parte · ETF de XRP, XLM y BTC: flujos y patrimonio diarios desde las webs de los emisore · Sonnet M · ~~4 % · `Sigue CLAUDE.md. Repo PÚBLICO; sin recomendaciones ni comparar con tesis. Tras el plazo del 13F (16-nov), usa scripts/leer_edgar.py (no lo reescribas: crea scripts/leer_etf_flujos.py) para listar quién declara ETF de XRP/XLM/BTC al 30-sep. Para cada ETF spot de XRP y XLM vivo, localiza en la web del emisor el CSV o la tabla de participaciones (acciones en circulación, NAV, tenencia en monedas) y calcula el flujo diario como variación de acciones × NAV; si la web es SPA, léela en Chrome y anótalo. Guarda explorador/etf-flujos.json con fuente, fecha y nivel por cifra (emisor = parte interesada). Agregadores (Farside, SoSoValue) solo como contraste [S]. Informe en informes/research/. NO commit ni push.`
- C30 ◐ en parte · Centro · Política y elecciones por país · Sonnet M · ~3 % · `research/prompts/C30-politica-elecciones.md`
- C320 ◐ en parte · Correcciones auditoría Opus 2 (datos y scripts) · Sonnet M · ~ · ``
- C321 ◐ en parte · Cadenas: mapa especulativo de escenarios (leyes MiCA/SEC/CFTC, mensajería SWIFT/ · Opus L · ~~6 % · `Sigue CLAUDE.md. Repo PÚBLICO: solo hechos con fuente en cada nodo y todo lo demás marcado [ESPECULACIÓN]; sin recomendaciones ni comparar con la tesis. Diseña (como el mapa de interconexión) un mapa de escenarios: por red, dónde encaja mejor (cantidad tokenizada, cómo se pagan los rewards y las comisiones), qué leyes le aplicarían (MiCA, SEC, CFTC), qué estándar de mensajería usaría (SWIFT, DTCC, BIS, ISO 20022), qué capa de seguridad, y cómo sería un pago transfronterizo (p. ej. USDC → XLM → euro por el DEX nativo) y una tokenización (banco → congelar o emitir contrato → permisos → sacar tokens). Cada flecha: hecho con fuente (P/S) o hipótesis [ESPECULACIÓN] con la razón. Incluye quién saldría beneficiado en el mercado financiero según lo que aporta cada red. Empieza por el diseño visual y deja la investigación de enlaces para sesiones aparte.`
- C322 ◐ en parte · Cadenas: ampliar el mapa de interconexión con enlaces con fuente de XRPL, Hedera · Sonnet M · ~~4 % · `Sigue CLAUDE.md. Repo PÚBLICO. Hoy el mapa (explorador/interconexion.json) no dibuja esas redes porque no hay enlace con fuente. Busca fuente PRIMARIA (docs, comunicados, SEC/EDGAR, BIS) de integraciones con CCIP, CCTP, DTCC, Swift, Canton, Partior, Fnality, Agorá o Nexus, y añade nodos y enlaces con estado (producción/piloto/anunciado/concepto), fecha y nivel. Revisa también por qué Canton se llama «red» y no «cadena». Cierre: revisar_explorador.py (0 avisos), construir_orbita/movil/seguimiento. Sin API de Anthropic; commit y push solo con «sube».`
- C331 ◐ en parte · Cadenas: escenario del activo puente neutral entre redes (país con Ethereum ↔ pa · Opus M · ~~4 % · `Sigue CLAUDE.md. Repo PÚBLICO: solo hechos con fuente y fecha; nada de privado/ ni comparar con la tesis de Joel; sin recomendaciones ni «ganador». Lo especulativo, marcado [ESPECULACIÓN] con su razón y más crítico que optimista (Joel pide más casos estrictos). Edita explorador/cadenas.json (celdas {t,f,u,d,n}; sin dato = null). Cierre: revisar_explorador.py (0 avisos), construir_orbita/movil/seguimiento, informe en informes/research/. Sin API de Anthropic; commit y push solo con «sube». En escenarios-redes.json añade un flujo «puente neutral» con pasos: emisión en la cadena A, conversión a un activo puente (stablecoin, depósito tokenizado, XRP/XLM u otro), paso por CCIP/CCTP/Wormhole/LayerZero o mercado nativo, y salida en la cadena B en la divisa que se quiera. Cada paso con fuente o [ESPECULACIÓN]. Incluye la frase de DTCC «multi-chain» con su fuente y el estado legal en EE. UU. (CLARITY paralizada, Senado/Cámara): qué es hecho y qué es incertidumbre [VERIFICAR].`
- C333 ◐ en parte · Cadenas: escenarios ampliados sin stablecoin por defecto (CBDC, depósitos tokeni · Opus L · ~~8 % · `Sigue CLAUDE.md. Repo PÚBLICO: solo hechos con fuente y fecha; nada de privado/ ni comparar con la tesis de Joel; sin recomendaciones ni «ganador». Lo especulativo, [ESPECULACIÓN] con su razón y más crítico que optimista. Amplía Cadenas › Escenarios (el de «un país en Ethereum y otro en Stellar» era solo un ejemplo): (1) sin la stablecoin por defecto: muchos países no tienen stablecoin propia o no la aceptan (China lo ha dicho), así que modela rutas con CBDC (mBridge, Agorá, Nexus, e-CNY, e-rupia…), dinero de banco comercial tokenizado, depósitos tokenizados, fiat con corresponsal (nostro/vostro) y token/activo puente; (2) corredores concretos con monedas poco líquidas (p. ej. Kenia, Somalia, un país pequeño) y el problema de liquidez duplicada en cuentas nostro/vostro, con fuente de BIS/FMI/Banco Mundial sobre costes de remesas; (3) lo que ya preparan Ethereum y terceros (CCIP, CCTP, LayerZero, Canton, Partior, Fnality, Agorá) frente a lo que sería propio de un activo puente neutral; (4) riesgos de las stablecoins con fuente: GENIUS (reservas en deuda del Tesoro), BIS (informe anual sobre stablecoins y riesgo de salida de liquidez al tener más deuda que efectivo), concentración en USD; el argumento de Joel de que el comercio quiere dejar de depender del dólar es [J]/[ESPECULACIÓN] hasta contrastarlo con cifras (cuota del USD en pagos SWIFT y reservas del FMI COFER); (5) matriz país × tipo de dinero (CBDC / stablecoin / fiat / token) con cuántos países en cada estado y fuente (Atlantic Council CBDC tracker, BIS). Cierre: revisar_explorador.py (0 avisos), construir_orbita/movil/seguimiento, informe en informes/research/. Sin API de Anthropic; commit y push solo con «sube». Usa subagentes de lectura y cotejo en Chrome. AÑADIDO 15-nov (noche): (6) coste de la liquidez en cuentas nostro/vostro: el banco debe tener prefinanciada la moneda de destino además de la de origen (capital inmovilizado, casi doble) y la liquidación transfronteriza tarda hoy de horas a varios días; cuantifica con fuente (BIS/CPMI, FSB, Banco Mundial: coste, tiempo, % de pagos que superan 1 hora o 1 día, capital inmovilizado) y explica qué liberaría un activo puente entre bancos (XRP, XLM u otro: ODL de Ripple con cifras públicas y sus límites) y qué no (riesgo de precio, regulación, bancos que no lo usan); (7) bloques de países, no solo países: BRICS (India, Rusia, China, Brasil, Sudáfrica y nuevos miembros; no atribuir a Singapur lo que no sea suyo), Proyecto Agorá, mBridge, Nexus y los proyectos del BIS con calendario hacia 2027: qué mínimos técnicos y legales piden y en qué estado están, con fuente; (8) Stellar y XRPL comparados con hechos: origen (Stellar nace en 2014 del bifurcación de ideas de Jed McCaleb, cofundador de Ripple; cotejar), tiempo de cierre de ledger (≈3-5 s), DEX nativo, emisión de CBDC y stablecoins, y activos reales tokenizados (acciones, bonos, ETF, fondos del Tesoro) usables como colateral o medio de pago transfronterizo, con ejemplos reales y su nivel de producción; (9) opinión de analistas e instituciones (BIS, FMI, bancos centrales, Ripple, SDF, críticos) sobre la evolución, citando a cada uno, y una sección [ESPECULACIÓN] mía con escenarios y sus razones, más crítica que optimista y sin recomendar comprar ni vender. Presupuesto: no cabe en una ventana de 5 horas; reparte en subagentes y sesiones aparte.`
- C36 · Centro · Rutina de noticias manuales (Claude y Gemini) · Sonnet M · ~3 % · `research/prompts/C36-rutina-noticias-manual.md`
- C39 ◐ en parte · Centro · Volcar al panel lo ya investigado sin movimiento (países T07-T16 y W03E · Sonnet S · ~2 % · `research/prompts/C39-volcado-orbita.md`
- C42 ◐ en parte · Centro · Rendimientos y colateral: staking, lending CeFi/DeFi, AMM XRPL/Stellar, · Sonnet M · ~3 % · `research/prompts/C42-rendimientos-colateral.md`
- C58 ◐ en parte · Centro · Fichas políticas de 12 países (UE: España, Alemania, Francia, Italia, P · Sonnet M · ~3 % · `research/prompts/C58-fichas-politicas-paises.md`
- C59 ◐ en parte · Centro · Indicadores económicos por país (IPC, paro total y juvenil, PIB, deuda, · Sonnet M · ~3 % · `research/prompts/C59-indicadores-sociales-economicos.md`
- C61 ◐ en parte · Centro · Servicios públicos y estabilidad social por país: sanidad (gasto, hitos · Sonnet M · ~3 % · `research/prompts/C61-servicios-publicos-estabilidad.md`
- C68 ◐ en parte · Centro · España · Sueldos de cada cargo político (presidente, ministros, secreta · Sonnet L · ~~6 % · `research/prompts/C68-sueldos-por-persona-politicos.md`
- C68B ◐ en parte · Centro · España · Cuadrar sueldos de secretarios de Estado, subsecretarios y dir · Sonnet M · ~~3 % · `research/prompts/C68B-cuadrar-sueldos-segundo-nivel.md`
- C69 ◐ en parte · Centro · España · España: cada partida con 2024 y 2025 y su variación (IGAE 2024 · Sonnet L · ~~6 % · `research/prompts/C69-espana-2024-vs-2025.md`
- C77 ◐ en parte · Centro · España: gasto público y deuda por ministerio, comunidad, municipio y co · Opus L · ~ · ``
- C79 · Centro · España: PDF del Tesoro, AIReF, IGAE y AEAT (requieren OK de descarga),  · Sonnet M · ~ · ``
- C80B ◐ en parte · Centro · Fuentes Fase 2: catálogo con estado (API/Chrome/bloqueada/manual) y cad · Sonnet M · ~ · ``
- C87 · Centro · Separar público/privado: auditoría del repo público y plan de repo priv · Opus M · ~~3 % · ``
- C88 · Centro · Endurecer el Worker de Cloudflare y los bots de pago: token fine-graine · Sonnet S · ~~1 % · ``
- C89 · Centro · Endurecer candado() de app.py: cerrado por defecto, cookie/sesión en ve · Sonnet S · ~~2 % · ``
- C92 ◐ en parte · Centro · Medición: normalizar predicciones (fecha límite, fuente_id), script de  · Sonnet M · ~~3 % · ``
- C95 · Centro · Plan de salida a producción para la familia: auth, hosting, copias, avi · Opus M · ~~3 % · ``
- C96 · Centro · Consulta regulatoria de monetización [VERIFICAR con asesor/CNMV]: pregu · Sonnet S · ~~1 % · ``
**Países y temas (T)** · detalle en `research/COLA-TEMAS-GEMINI.md`
- T25 · Tema libre
**Deuda y bonos (D)** · detalle en `research/COLA-DEUDA-BONOS.md`
- D06 · (parcial) Bancos y deuda: exposición soberana de 116 bancos europeos (
**Otros research (R)** · detalle en `research/COLA.md`
- R17 · Resumen semanal de 1 página (para imprimir)
- R36 · PROFUNDO: Segunda pasada con los PDFs que haya en research/fuentes/ (R
- R39 · Auditoría final corta (18-19 oct): solo lo escrito después de R31/R38 

## Auditorías abiertas
- A1 (Media): Abierto: voces.json lo está editando otra sesión (W06); propuesta: v002→cumplido con la nota del 28-oct; v062→
- A2 (Media): Abierto: propuesta, mostrar «P + novedades S» o añadir url a HK ETF
- A3 (Media): Parcial: antes faltaban 23. Abierto: 9 celdas
- A4 (Baja): Abierto
- A5 (Media): Abierto: propuesta, 2-3 canales o analistas críticos o neutrales en el próximo lote de vídeos
- A7 (Media): Abierto
- A8 (Baja): Abierto solo v062
- A9 (Baja): Cerrado (W07)
- Auditoría mensual W08: última semana del mes (miércoles)

## Verificaciones abiertas ([VERIFICAR]; las cierra W05 o W08)
- ninguna anotada

## Verificaciones pendientes con antigüedad (noticias de prensa sin contrastar y [VERIFICAR]; se anotan en eventos/verificados.json)
- [media] 2026-10-25 (25 d) · Texto definitivo de los modelos 172/175/721 y de DAC8 en el BOE
- [media] 2026-10-25 (25 d) · [VERIFICAR] Precio y cierre de cada adquisición de Ripple sin precio publicado (Standard Custody, Palisade, So
- [media] 2026-10-25 (25 d) · [VERIFICAR] Integración de Chainlink CCIP en producción en SWIFT.
- [media] 2026-10-25 (25 d) · [VERIFICAR] Vigencia 2026 de la escala del ahorro (art. 66 LIRPF)
- [media] 2026-10-25 (25 d) · [VERIFICAR] Consulta DGT V0648-24 leída en petete
- [media] 2026-10-25 (25 d) · [VERIFICAR] Cloture CLARITY 49-50 en fuente oficial (senate.gov)
- [media] 2026-10-25 (25 d) · [VERIFICAR] Texto literal de la **sección 404** de CLARITY en congress.gov
- [media] 2026-10-25 (25 d) · [VERIFICAR] Vigencia 2026 de la escala del ahorro (art. 66 LIRPF)
- … y 35 más en el Seguimiento

## Qué se está quedando viejo (frescura)
- 🔴 Voces: Voces sin confirmar (30) → W06 · 17 llevan más de 14 días
- 🔴 Predicciones: Vencidas sin resultado (1) → W06 · #20
- 🔴 Datos a mano: Liquidez de Japón y China (1) → W01 · CN (2026-09)
- 🔴 Explorador: JSON con dato viejo o sin fecha (más de 7 días) (33) → rutina de cada tema (ver explorador/frescura.json) · verdes 47, amarillos 20, rojos 6, grises 7. Rojos: bancos-eba, espana-contrataci
- 🟡 Radar regulatorio: Celdas sin dato (8) → W03 · Más huecos: IR 2, AE 1, BRICS 1, ID 1, EG 1

## Bots con problema
- Votos de noticias, Paneles de datos

## Calendario: ya pasaron (10 días) y qué falta decidir
- 2026-11-10 · Inflación EE. UU. (IPC de octubre) (alto) → ◐ rutina ejecutada (W01 del 2026-11-16); dato sin marcar como leído
- 2026-11-10 · EIA: perspectivas de energía a corto plazo (STEO) (medio) → ◐ rutina ejecutada (W10 del 2026-11-14); dato sin marcar como leído
- 2026-11-11 · SEC: plazo sobre opciones de ETFs cripto (SR-ISE-2026-42) (medio) → ✓ revisado (hecho)
- 2026-11-11 · OPEP: informe mensual del mercado petrolero (noviembre) (medio) → ✓ revisado (hecho)
- 2026-11-13 · AIE: informe mensual del mercado petrolero (noviembre) (medio) → ✓ revisado (hecho)
- 2026-11-13 · España: IPC definitivo de octubre (INE) (medio) → ✓ revisado (hecho)
- 2026-11-16 · Plazo del 13F del 3T (quién tiene ETF de XRP/XLM) (medio) → ⏳ SIN research: decidir (EV)
- 2026-11-18 · Reino Unido: IPC de octubre (ONS) (medio) → ⏳ SIN research: decidir (EV)
- 2026-11-18 · Zona euro: IPCA definitivo de octubre (Eurostat) (medio) → ⏳ SIN research: decidir (EV)
«✓ cubierto» exige que el informe de la rutina tenga una línea `Eventos leídos: <fecha o título>`; sin ella solo consta que la rutina se ejecutó (C256).
Para los «SIN research»: pide `/research EV <fecha> <título>`; usa `research/prompts/EV-post-evento.md`. Descartar o marcar hecho: `eventos/revisados.json`.

## Calendario: próximos 14 días de impacto y qué los cubre
- 2026-11-18→11-19 · APEC en Shenzhen: cumbre de líderes (medio) · EN CURSO → cubre W03 (Regulación por países)
- 2026-11-23 · Stellar: voto de mainnet de Protocol 30 (Bell) (medio) → sin rutina: valorar research EV
- 2026-11-25 · PCE de octubre y PIB de EE. UU. (2.ª estimación) (medio) → cubre W01 (Datos macro y tipos)
- 2026-11-26 · Corea: próxima reunión del Banco de Corea sobre el tipo base (medio) → cubre W01 (Tipos de interés)
- 2026-11-27 · Francia: revisión programada de la calificación de S&P (hoy  (medio) → cubre W02 (Deuda y subastas)
- 2026-11-27 · España: IPC adelantado de noviembre (INE) (medio) → cubre W01 (Datos macro y tipos)
- 2026-11-29 · España: elecciones generales anticipadas (alto) → cubre W11 (Política y elecciones)
- 2026-11-29 · OPEP+: reunión mensual (fecha según prensa) (medio) → cubre W10 (Energía y geopolítica)
- 2026-11-30 · EE. UU.: fin de comentarios a las propuestas de la Fed sobre (medio) → sin rutina: valorar research EV
- 2026-12-01 · Zona euro: IPCA adelantado de noviembre (Eurostat) (medio) → cubre W01 (Datos macro y tipos)
- 2026-12-01 · Estonia: cierre de los pasos fronterizos con Rusia (medio) → sin rutina: valorar research EV
- 2026-12-02→12-04 · Reunión del RBI (India) (medio) → cubre W01 (Tipos de interés)

## Predicciones que vencen en 14 días
- #20 · 2026-10-23 · ledger
- #24 · 2026-11-30 · Abbas Araqchi (ministro de Exteriores de Irán), vía Catar, según prensa
- #68 · 2026-11-30 · Richard Blumenthal (cartas del 5-nov), según Cointelegraph y Unchained
- #24 · 2026-11-30 · IMF PortWatch
- #68 · 2026-11-30 · PSI

## Próximas fechas clave
- 2026-11-23 · Stellar: voto de mainnet de Protocol 30 (Bell)
- 2026-11-25 · PCE de octubre y PIB de EE. UU. (2.ª estimación)
- 2026-11-26 · Corea: próxima reunión del Banco de Corea sobre el tipo base (hoy 3,00 %)
- 2026-11-27 · Francia: revisión programada de la calificación de S&P (hoy A+, estable)
- 2026-11-27 · España: IPC adelantado de noviembre (INE)
- 2026-11-29 · España: elecciones generales anticipadas
- 2026-11-30 · EE. UU.: fin de comentarios a las propuestas de la Fed sobre stablecoins
