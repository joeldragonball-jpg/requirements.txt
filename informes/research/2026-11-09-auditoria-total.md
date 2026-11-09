# Auditoría total: todo el research y la Órbita como un solo conjunto · 9-nov-2026

Hecha el 9-nov-2026 por Claude (Opus), sin IA de pago adicional ni workflows. **No hay recomendaciones de compra ni de venta.**
Niveles: **[P]** fuente primaria leída · **[S]** secundaria o agregador · **[VERIFICAR]** sin comprobar (se dice el motivo) · **[ESPECULACIÓN]** opinión o predicción · **[RAZONADO]** deducción mía a partir de hechos [P].
Separación: las secciones (a), (b) y (e) son **HECHOS** salvo que se marque lo contrario; (c) mezcla hechos y lectura; (d) y (f) son **OPINIONES/propuestas**.

**Cómo se hizo (reproducible, sin IA):**
- Se cruzaron los 40 JSON de `explorador/`, `explorador/vistas.html`, `eventos/calendario.toml`, `informes/predicciones.md` y 391 archivos Markdown (`informes/**`, `research/verificaciones`, `research/fuentes-nuevas`, `cerebro/`).
- Para cada archivo se contaron las etiquetas [P], [S] y [VERIFICAR] y se miró si su nombre aparece en algún dato de la Órbita.
- Después se buscaron hechos [P] de sep-nov 2026 por ámbito y se comprobó si están en la Línea de tiempo (`datos.json`), en la Matriz (`regulacion.json`) o en otro JSON.
- Datos históricos: FRED (`fredgraph.csv`) con curl el 9-nov-2026; Reglamento del Congreso en el BOE, leído el 9-nov-2026.
- No se usó Chrome: FRED rechazó Python pero respondió a curl, y el BOE respondió directamente.

---

## Resumen en 8 líneas
1. **El problema principal no es que falte research, sino que no llega a la Órbita.** Hay 735 etiquetas [P] en informes cuyo nombre no cita ningún dato de la Órbita.
2. **Las «capas paradas» son, en parte, un efecto de cómo se miden.** La Línea de tiempo (103 movimientos) y la Matriz (168 celdas) son dos almacenes que no se sincronizan.
   - La Matriz sí recoge la norma final de la OCC sobre GENIUS (21-oct), el reglamento de Canadá (24-oct), Corea, Brasil y Singapur.
   - La Línea de tiempo no los tiene, y COBERTURA.md solo cuenta la Línea de tiempo.
3. Hay **21 hechos verificados** guardados en informes que la Órbita no enseña, o enseña desfasados. Los más importantes:
   - el lanzamiento de DTCC (28-oct);
   - la propuesta de custodia de la SEC (1-oct);
   - el FBI sobre Binance (31-oct);
   - las subidas del RBA (3-nov) y del Banco de Inglaterra (5-nov);
   - el e₹ de la India;
   - el resultado provisional de las legislativas de EE. UU.
4. **6 contradicciones concretas.** Entre ellas:
   - La Matriz da el Banco de Inglaterra en 3,75 % y el panel en 4,00 %.
   - Una celda dice «la Fed, el BCE y el BoJ suben a la vez» cuando los tres mantuvieron los tipos en octubre.
   - DTCC sigue «pendiente» en Voces una semana después de que la auditoría W08 lo señalara.
5. **Patrón global [P]:** hay una ola sincronizada de subidas de tipos (8 de 21 jurisdicciones suben, 1 baja) con el Brent por encima de 100 $. Lo más parecido en la historia son 2022 y, por el origen en Oriente Medio, 1979-80 [ESPECULACIÓN sobre el parecido].
6. **Comparaciones históricas [P, FRED]:**
   - El bono de EE. UU. a 10 años ha estado en el 5 % o más por primera vez desde el 19-jul-2007.
   - El Brent solo había superado los 120 $ en 2008, 2011-12 y 2022.
   - La caída del Nasdaq del 5-nov (−5,52 %) es una de las 22 sesiones de −5 % o peor desde 2008.
7. **Sesgo estructural:** las 73 voces son casi solo cripto (17 de 23 menciones de red son XRPL) y no hay ninguna voz de energía, política ni liquidez. Además, cada capa tiene un cajón «xrp». Las dos cosas chocan con el criterio de tablero general.
8. **Propuestas:**
   - Primero, un script sin IA que detecte desincronías (Línea ↔ Matriz ↔ Voces ↔ Calendario) y volcar los 21 hechos.
   - Después, un registro único de hechos con identificador.
   - Se añaden 8 rutinas recurrentes (W12-W19) al Seguimiento.

---

## (a) Lo que ya está bien (HECHOS)

| # | Qué | Prueba |
|---|---|---|
| 1 | **Las cifras de pantalla son fiables.** 21 de 21 coinciden con su fuente y los niveles S/P son coherentes. | `informes/research/2026-11-09-auditoria-datos-y-research.md` (8-nov) |
| 2 | **La Matriz es la parte más rigurosa del tablero.** Tiene 168 celdas con fecha, «revisado», «caduca», «falta» y nivel. Hay mayoría de [P] en CBDC (15/21), Stablecoins (16/21) y Política monetaria (18/21). | `explorador/regulacion.json` |
| 3 | **El panel de tipos ya se autocontrola**: el campo `coincide_radar` detectó solo el desfase del Banco de Inglaterra. Es el patrón a copiar en el resto. | `paneles.json › tipos_vivos` |
| 4 | **España: presupuesto con vigencia clara.** PGE de 2023 prorrogados, techo de gasto de 2027 aprobado el 7-jul-2026 y disolución de las Cortes el 6-oct [P]. | `espana-presupuesto.json › vigencia` |
| 5 | **Elecciones de España con fuente primaria**: Real Decreto 806/2026, BOE-A-2026-20742 [P]. | `elecciones.json`, `datos.json` |
| 6 | **Disciplina de verificación**: registro de 60 predicciones (8 aciertos y 2 fallos resueltos), `verificaciones-consolidado.md` y [VERIFICAR] con su motivo. | `informes/predicciones.md` |
| 7 | **Matriz de riesgos con desmentidores**: 7 escenarios, cada uno con lo que lo desmentiría. Es buena práctica contra el sesgo de confirmación. | `datos.json`, capa «riesgos» |

---

## (b) Hechos guardados que la Órbita no enseña (o enseña desfasados) y dónde deberían ir

Columna «Dónde está hoy»: el informe que lo prueba. «Debería ir» se refiere a la capa de la Línea de tiempo (`datos.json`), salvo que se indique otra cosa.

| # | Hecho | Fecha | Nivel | Dónde está hoy | Debería ir |
|---|---|---|---|---|---|
| 1 | La OCC publica la **norma final** que desarrolla la GENIUS Act (NR 2026-92); la ley entra en vigor el 18-ene-2027 | 21-oct-2026 | P | Matriz y cajón «xrp» de la capa; `2026-10-27-C13-urls-radar.md` | Stablecoins (movimiento «norma») |
| 2 | **DTCC «Goes Live»**: DTC lanza su servicio de tokenización en Canton y Besu, con 20 participantes firmados y más redes en 2027 | 28-oct-2026 | P | `2026-10-28-W05-predicciones-octubre.md`, `2026-10-30-W09` | Tokenización + Custodia; Voces v002 → cumplido |
| 3 | La SEC propone una norma de **custodia** (S7-2026-35; comentarios hasta el 7-dic) | 1-oct-2026 | P | `2026-10-07-clarity-lame-duck-y-custodia.md`; está en el Calendario pero no en la Línea | Custodia |
| 4 | Canadá: **Stablecoin Act** sancionada (S.C. 2026, c. 3); a 30-sep casi todo sin entrar en vigor. **Reglamento propuesto** en la Canada Gazette: sin intereses y reservas ≥100 % | 26-mar y 24-oct-2026 | P | `2026-10-31-W03-B-canada-australia`, `2026-10-26-apertura.md`; Matriz | Stablecoins; ficha de Canadá (no existe) |
| 5 | Banco de Rusia, Указание 7441-У: solo BTC, ETH y USDT admitidos; tope de ₽300.000 al año para inversores no cualificados | 11-sep-2026 | P | `2026-10-27-T12-rusia.md`; Matriz | Regulación |
| 6 | El **FSB** cifra las stablecoins en ≈ $300 mil M, sin cambio en un año, y pide más vigilancia transfronteriza. El BIS (Informe Económico Anual) daba ≈ $320 mil M a fin de mayo | 12-oct y 23-jun-2026 | P | `2026-10-27-T16-organismos.md` | Stablecoins (cifra de capa) |
| 7 | Singapur (MAS): consulta P015-2026 sobre stablecoins de un solo activo ligadas al SGD o al G10, con prohibición de intereses | del 1-sep al 16-oct-2026 | P | `2026-10-21-radar-v5-research.md`; Matriz | Stablecoins |
| 8 | Japón (FSA): la tokenización pasa a etapa 5 en la Matriz | 20-oct-2026 | P | `2026-10-26-W03-japon-singapur.md` | Tokenización |
| 9 | Standard Chartered custodia RLUSD en el XRPL desde su sucursal del DIFC (Dubái) | 12-oct-2026 | P | `2026-10-25-T23-ripple-y-stellar-por-region.md` | Custodia (sin cajón «xrp»: es custodia bancaria) |
| 10 | **FBI**: Corea del Norte (TraderTraitor) robó «más de 6.000 M$» a Binance | 31-oct-2026 | P | `2026-11-08-verificacion-prensa.md`; la Línea solo tiene la consulta de la Fed y la OCC del 5-nov [S] | Riesgos + Custodia |
| 11 | India: el **e₹ sigue en piloto** (preguntas frecuentes del RBI) | 1-oct-2026 | P | `2026-10-20-radar-v4-research.md`, `2026-10-27-T10-india.md` | `cbdc-blockchains.json`, que hoy dice «Sin datos [VERIFICAR]» |
| 12 | Hong Kong: el **e-HKD es solo mayorista por ahora**; EnsembleTX en piloto real durante 2026 | 13-nov-2025 y 29-may-2026 | P | `2026-10-19-radar-v2-research.md` | `cbdc-blockchains.json` (lo lista como «pendiente») |
| 13 | Corea (KoFIU/FSS): en el 1S-2026 el mercado cripto coreano pierde un 33 % de capitalización y un 44 % de volumen diario; 26 VASP | 1-oct-2026 | P | `2026-10-17-R30-segunda-pasada-jurisdicciones.md` | Regulación; ficha de Corea (no existe) |
| 14 | Brasil: Res. 561 prohíbe liquidar ciertas operaciones de cambio con activos virtuales. Desde el 1-oct hay aviso al Coaf de transferencias de 10.000 US$ o más a monederos autocustodiados | 30-abr y 1-oct-2026 | P | `2026-10-21-verificacion-chrome.md`, `radar-v4`; Matriz | Regulación |
| 15 | **Ola de subidas de septiembre**: BCE (16-sep), Fed (17-sep, de 3,75 a 4,00 %) y BoJ (18-sep, a 1,25 %) | sep-2026 | P (FRED DFEDTARU, BCE, BoJ) | Solo como resumen del 25-oct en la Línea; detalle en la Matriz | Liquidez: tres movimientos con fecha |
| 16 | **RBA** sube 25 pb, hasta el 4,85 % (votación 6-3) | 3-nov-2026 | P | `2026-11-04-EV-rba-3-nov.md`; Matriz | Liquidez |
| 17 | **Banco de Inglaterra** sube al 4,00 % | 5-nov-2026 | P (IUDBEDR) | Panel de tipos y Calendario; la Línea solo tiene el titular de CNBC [S] | Liquidez (subir a P) y Matriz (hoy dice 3,75 %) |
| 18 | Banco de Canadá sube al 2,50 % | 28-oct-2026 | P | Matriz | Liquidez |
| 19 | **Legislativas de EE. UU.**: proyección de mayoría demócrata en la Cámara; el Senado sigue abierto; aprobación de Trump del 38 % en las encuestas a pie de urna | 3-4 nov-2026 | S (cadenas; aún no hay recuento oficial) | `2026-11-04-EV-elecciones-eeuu.md` | `elecciones.json`, que sigue «en_recuento» con la composición previa. Anotar ya como S y subir a P con la certificación |
| 20 | **Art. 207 del Reglamento del Congreso**: «Disuelto el Congreso… quedarán caducados todos los asuntos pendientes». Aplicación: si el proyecto de ley de transposición de DAC8 seguía en trámite el 6-oct, ha decaído y el nuevo Gobierno tendría que volver a presentarlo [RAZONADO; que siguiera en trámite es VERIFICAR: la API del BOE no devolvió ninguna ley con «2023/2226»] | 9-nov-2026 (lectura) | P (regla) | Nuevo hoy | España + Calendario (23-dic, nuevas Cortes) + predicción #38 |
| 21 | Franklin Templeton FOBXX/BENJI: activos netos de $667,96 M a 30-sep-2026 (todas las cadenas) | 30-sep-2026 | P | `2026-10-29-C50-rwa-por-cadena.md` | Panel de RWA (hoy solo trae el agregador [S]) |

**Bloques enteros sin uso (HECHO):**
- `research/fuentes-nuevas` (11 archivos, 16 [P]) y `research/verificaciones` (5) no se citan en ningún dato.
- `informes/videos`: 82 [P] en 13 archivos, con solo 1 citado.
- `informes/gemini`: 47 [P] en archivos no citados.
- Los informes diarios (apertura y cierre, 63 archivos) llevan 89 [P] que no pasan a la Línea de tiempo: tipos, subastas y cierres de mercado con fuente oficial.

**Lo que «citado» no mide (matiz pedido):**
- Un informe puede no estar citado y que su hecho sí esté en la Matriz con otra fuente; es el caso de 4, 5, 7 y 14.
- Lo que de verdad se desaprovecha son tres cosas:
  1. los hechos **con fecha** que no entran en la Línea de tiempo (que es la vista con reacción de precios);
  2. los **resultados** (qué pasó) de eventos que solo estaban como previsión;
  3. el research de España y de fuentes nuevas que alimenta cifras pero no la cronología.

---

## (c) Contradicciones, desfases y repeticiones

### Contradicciones (HECHO + fuente)

| # | Qué no cuadra | Lado A | Lado B | Qué hacer |
|---|---|---|---|---|
| C1 | Banco de Inglaterra | Matriz: «mantuvo el 3,75 % el 17-sep» | Panel `tipos_vivos`: 4,00 % desde el 5-nov [P, IUDBEDR]; el Calendario también dice 3,75 → 4,00 | Actualizar la celda; `coincide_radar=false` ya lo marcaba |
| C2 | Celda supranacional (BRICS/BIS) de política monetaria, del 14-oct | «La Fed, el BCE y el BoJ suben tipos a la vez; Brent ≈ $126,6» | Los tres **mantuvieron** del 28 al 30-oct [P]. Brent al contado 107,03 $ el 3-nov (FRED DCOILBRENTEU) [P] | Reescribir en pasado («subieron en septiembre; pausa en octubre»). Su «caduca» del 18-ene-2027 no protege ante cambios rápidos |
| C3 | India e₹ | `cbdc-blockchains.json`: «Sin datos [VERIFICAR]» | RBI, preguntas frecuentes del 1-oct-2026: sigue en piloto [P] | Volcar el dato |
| C4 | DTCC en Voces | v002 «pendiente: a 23-oct sin confirmación» | Nota de DTCC del 28-oct «Goes Live» [P]. W08 lo señaló el 2-nov (A1) y sigue sin corregir el 9-nov | Pasar a «cumplido» y revisar v062 (Binance, plazo del 1-nov vencido) |
| C5 | Fecha de la caída del Nasdaq | Línea de tiempo: «El Nasdaq se desploma un 5,5 %», fechado el 6-nov | FRED NASDAQCOM: −5,52 % en la sesión del **5-nov** y +1,09 % el 6-nov [P] | Separar «fecha de la sesión» de «fecha del titular» |
| C6 | IPC de EE. UU. de septiembre | Móvil: 3,7 % (sin desestacionalizar, la convención del BLS) [P] | FRED CPIAUCSL (desestacionalizado): 4,02 % [P] | **No es un error**, son dos definiciones. Etiquetar «SA/NSA» para que no aparezcan contradicciones falsas |

### Tensiones a vigilar (no son contradicción todavía)
- **Ormuz.**
  - La Matriz de riesgos (25-oct) da «Ormuz sigue casi cerrado» con probabilidad alta [ESPECULACIÓN propia].
  - Después llegan dos titulares del 5-6 nov: «Irán exime a China e India» y «el Brent cierra su mayor caída semanal desde 2020» [S]. El mismo día hay otro de «ataque a barcos en Ormuz» [S].
  - El último dato de tráfico con fuente primaria (PortWatch) es del **18-oct**: 3 semanas sin medir lo que decide el escenario.
- **Prima de riesgo de España**: los dossiers G1 y G4 dan 34 pb frente a 45-49 pb según el agregador; ya está marcado [VERIFICAR]. Con elecciones el 29-N conviene una serie primaria (BdE/Tesoro frente a Bundesbank).
- **Escenario 5 (CLARITY en el lame-duck).**
  - Hay un titular del 4-nov: «probabilidades caen al 31 %» [S, mercado de predicción].
  - Hay una proyección de Cámara demócrata desde enero [S].
  - Afecta a los desmentidores del escenario.

### Patrones y repeticiones entre fuentes, ámbitos y fechas
1. **Ola sincronizada de subidas [P, Matriz + panel]:**
   - Suben: Fed, BCE y BoJ (septiembre); Canadá, Australia, Reino Unido, India, Sudáfrica, EAU y Etiopía (sep-nov).
   - Mantienen: 11. Baja: solo Brasil.
   - El hilo común que citan los comunicados es la inflación por energía tras el cierre de Ormuz (PortWatch: 0 barcos el 4-mar-2026 [P]).
2. **El mismo hecho en 4-5 sitios con estados distintos.** OCC NR 2026-92 aparece en `datos.json` (cajón «xrp»), `regulacion.json`, `voces.json` y `prueba-datos.json`. Causa: no hay un identificador de hecho; cada vista copia texto.
3. **Titulares del bot mezclados con hechos.** En la capa «Energía y Ormuz», 9 de 16 movimientos son [S] de titulares (Google News, OilPrice, CNBC). Uno es «V» (salto sin causa). Se ven igual que los [P] de la EIA.
4. **Voces concentradas.**
   - 73 voces: reg 27, token 21, custodia 15, stable 11; energía, política y liquidez, **0**.
   - Redes citadas: XRPL 17, Stellar 6 y el resto 1-3.
   - Las voces más repetidas son el CEO de Ripple (3) y un canal de YouTube (3): **sesgo promocional y conflicto de interés** que hay que señalar al leerlas.
5. **Predicciones abiertas.**
   - 50 de 60 sin resolver; 2 con plazo vencido sin cerrar: #20 (PaymentBurn, 23-oct) y #38 (DAC8, 31-dic-2025; ahora condicionada por el art. 207).
   - En Voces: v002 y v062 vencidas.
6. **El Calendario no guarda resultados.** Hay 45 eventos pasados sin campo de resultado. Solo algunos lo llevan dentro del título (Banco de Inglaterra: «3,75 % → 4,00 % [P]»).
7. **Concentración en EE. UU.:** 32 % de las menciones por país. Hay 9 países con ficha y 0 hechos, y 9 sitios con hechos y sin ficha (COBERTURA.md).

---

## (d) Huecos por ámbito (OPINIÓN, con fuente oficial gratuita propuesta)

| Ámbito | Qué hay | Qué falta (lo de más valor primero) | Fuente oficial gratuita | Frecuencia |
|---|---|---|---|---|
| **Bancos centrales y CBDC** | 16 proyectos en `cbdc-blockchains.json`; Matriz CBDC 15/21 P | Volcar e₹ y e-HKD (b-11, b-12). Pagos transfronterizos mayoristas: Nexus, Mandala, Partior, Fnality [VERIFICAR estado 2026, no están en el repo]. Libra digital del Banco de Inglaterra [VERIFICAR]. Volúmenes de Pontes. **Voces de banqueros centrales: 0** | BIS Innovation Hub, BCE, BoE, MAS, HKMA, RBI | Trimestral, o por hito |
| **Stablecoins** | Panel de DefiLlama (S), Matriz 16/21 P | Serie de capitalización con un ancla P semestral (FSB, BIS). Normas GENIUS de la Fed (comentarios hasta el 30-nov) y de la OCC en la Línea. Multiemisión en la UE (EBA, sin guía). Peso del euro frente al dólar en stablecoins | FSB, BIS, Federal Register, EBA | Mensual (cifra) y por hito (norma) |
| **Tokenización** | RWA por cadena (manual, S), Matriz | DTCC en producción (b-2). Corea, fase 1 el 4-feb-2027. AUM de fondos tokenizados con la web del emisor [P] (FOBXX ya leído). Volumen de Pontes | DTCC, FSC, webs de emisores | Mensual |
| **Depósitos tokenizados** (305 días sin movimiento) | 1 hecho (JPMD, enero) | O se alimenta (BLOOM de la MAS, EnsembleTX de la HKMA, Agorá, bancos) o se **fusiona con Tokenización**. Las fuentes del repo son pocas: [VERIFICAR] qué bancos tienen servicio en producción | HKMA, MAS, BIS | Trimestral |
| **Liquidación y custodia** | 5 hechos | Propuesta de custodia de la SEC (b-3). Libro mayor de Swift con 19 bancos a fin de 2026 (calendario) [S]. Collateral AppChain de DTCC (4T). T+1 en la UE [VERIFICAR fecha oficial de ESMA]. Robo a Binance y su respuesta supervisora | SEC, ESMA, DTCC, FBI | Por hito |
| **Regulación** | Matriz (8 temas × 21) | CLARITY tras las legislativas. Resultados del pleno del GAFI del 30-oct (en el calendario, sin resultado). DAC8 en España (art. 207). Lote de MiCA (CASP por país de la UE) | Congress.gov (⛔ en Chrome, ver ACCESOS), FATF, ESMA, BOE | Semanal (W03) |
| **Energía y geopolítica** | 16 hechos; EIA y PortWatch [P] | **Tráfico de Ormuz desde el 18-oct** (lo que decide el escenario 1). Almacenamiento de gas en la UE (AGSI+). Reservas estratégicas. Informes de la AIE (13-nov) y de la OPEP (11-nov) | IMF PortWatch, GIE AGSI+, EIA, AIE, OPEP | Semanal |
| **Grandes potencias** | Fichas y mandatos | China: política económica tras el 15.º Plan [VERIFICAR qué aprobó la APN en 2026]; APEC Shenzhen (18-nov); G20 Miami (14-dic). **Guerra de Ucrania: no aparece en la Línea de tiempo** [VERIFICAR estado]. Aranceles entre EE. UU., China y la UE | Gobiernos, USTR, MOFCOM, Consejo UE | Semanal y por cumbre |
| **Política y elecciones** | `elecciones.json` (15) | Resultado certificado de EE. UU. España 29-N: **programas** fiscales, de vivienda, de ahorro y cripto de PSOE, PP, Vox y Sumar, descritos sin juzgar. Varias encuestas con ficha técnica, no solo el CIS | Junta Electoral Central, webs de los partidos, CIS | Diaria durante la campaña (13 al 27-nov) |
| **España** | El mejor cubierto (presupuesto, IGAE, INE, judicial) | Ya en cola: C229-C233. Nuevo: caducidad de leyes por la disolución (art. 207), prima de riesgo primaria, IPC del 13-nov | BOE, Congreso, BdE, INE | Ver C229-C233 |
| **Tipos, liquidez y deuda** | Panel automático de tipos, M2, curvas | M2 de EE. UU., la zona euro y Japón solo hasta **agosto** (se publica en mes+1). Resultados de subastas. Bono japonés a 30 años. Percentil histórico de cada cifra (ver e) | FRED, BCE, BoJ, TreasuryDirect | Mensual |
| **Otros vistos** | — | **Ciberseguridad financiera** (robo a Binance de más de 6.000 M$). **IA y chips** (caídas del 4 y 5-nov atribuidas a la IA: [S], causa sin probar). Clima y seguros (DANA) | FBI IC3, CISA, SEC 8-K | Por hito |

---

## (e) Comparaciones con el pasado (HECHOS de FRED leídos el 9-nov-2026, salvo indicación)

| Dato actual | Precedente | Lectura |
|---|---|---|
| **Bono de EE. UU. a 10 años ≥ 5 %** en sep-oct 2026; máximo de 5,31 % el 5-oct; 4,84 % el 5-nov [P, DGS10] | El último día ≥ 5 % antes de 2026 fue el **19-jul-2007** [P] | Coste del dinero a largo plazo en niveles de antes de la crisis de 2008. La curva 10-2 está en +0,35 (6-nov) [P], **sin inversión**: distinto de 2007 y de 2022-23, cuando estaba invertida |
| **Bono a 30 años: 5,67 %** el 7-oct-2026 [P, DGS30] | No se veía ≥ 5,4 % desde el **28-jul-2004** [P] | Máximo de al menos 22 años |
| **Brent ≥ 120 $** en mar-abr y sep-oct de 2026; máximo de 138,21 $ el 7-abr-2026; 107,03 $ el 3-nov [P, DCOILBRENTEU] | Meses con Brent ≥ 120 $ desde 1987: **solo 2008, 2011-12 y 2022** [P] | Cuarto episodio en casi 40 años. 2008 acabó en recesión, 2022 en subidas fuertes; 2011-12 convivió con la crisis del euro [RAZONADO] |
| **La Fed vuelve a subir** el 17-sep-2026 (3,75 → 4,00 % techo) tras recortar hasta el 11-dic-2025 [P, DFEDTARU] | Primera subida desde jul-2023. En la historia, «recortar y volver a subir en menos de un año» se dio en 1980 y 1998-99 [VERIFICAR con DFEDTAR, de memoria] | **Se parece a 2022** (subidas sincronizadas por energía) y, por el shock de oferta en Oriente Medio, a **1979-80** [ESPECULACIÓN]. Diferencia: hoy se parte del 3,75-4 %, no de cero |
| **IPC de EE. UU.** desestacionalizado: 4,27 % en mayo, 3,71 % en agosto y 4,02 % en septiembre de 2026 [P, CPIAUCSL] | — | Rebrote tras el pico de mayo; la serie sin desestacionalizar (3,7 %) es la que usa el BLS |
| **Nasdaq −5,52 % el 5-nov-2026** y +1,09 % el día siguiente; VIX de 16,6 a 28,2 [P, NASDAQCOM, VIXCLS]. Kospi −11 % en dos sesiones [S, Yahoo] | 22 sesiones de −5 % o peor desde 2008. Las anteriores: **3 y 4-abr-2025** (aranceles), 13-sep-2022 (dato de IPC), mar-2020, ago-2011 y 2008 [P] | Las caídas aisladas de −5 % (2022, 2025) no anticiparon por sí solas un crac; los racimos (2008, 2020) sí acompañaron a crisis [RAZONADO]. Causa del 5-nov atribuida a la IA y a la regulación tecnológica: [S], sin probar |
| **Diferencial high yield 3,48 %** (5-nov) [P, BAMLH0A0HYM2] | En los ~3 años que da FRED, el 89 % de los días estuvo más bajo; mínimo de 2,59 % el 22-ene-2025 [P] | Se amplía, pero sigue lejos de los episodios de crisis [VERIFICAR la serie larga: FRED solo publica 3 años por licencia de ICE] |
| **Robo a Binance de más de 6.000 M$** por TraderTraitor (FBI, 31-oct-2026) [P] | El mismo grupo robó ≈ 1.500 M$ a Bybit (FBI, feb-2025) [VERIFICAR enlace, de memoria] | Unas 4 veces el mayor robo previo conocido [RAZONADO, depende del dato de 2025] |
| **España: Cortes disueltas y PGE prorrogados desde 2023** [P] | Elecciones de noviembre ya hubo el 10-nov-2019 (repetición). PGE prorrogados varios años seguidos: 2019-2020 [VERIFICAR, de memoria] | Con elecciones el 29-N y Cortes el 23-dic, un PGE de 2027 a tiempo es improbable [ESPECULACIÓN] |
| **Ormuz: 0 barcos al día el 4-mar-2026** [P, PortWatch] | La «guerra de los petroleros» de 1984-88 fue un hostigamiento parcial, no un cierre [RAZONADO, sin fuente en el repo] | No hay precedente moderno de cierre total con datos diarios: las comparaciones son débiles |

**Qué ya se parece a otro momento [ESPECULACIÓN, con los dos lados]:**
- **Lectura «2022 bis»:** shock de energía, subidas sincronizadas y bonos largos en máximos de 15-20 años.
- **Lectura «2007»:** el 10 años en el 5 % y diferenciales que empiezan a abrirse desde mínimos.
- **Lo que desmiente ambas:** curva sin inversión, diferenciales todavía estrechos y un rebote al día siguiente de la caída.
- Para el Seguimiento: vigilar si el high yield pasa de 4-5 % y si la curva se invierte. Son disparadores observables, no predicciones.

---

## (f) Propuestas ordenadas por valor y esfuerzo (OPINIÓN)

Esfuerzo: S ≤ 1 % de la cuota semanal; M de 1 a 3 %; L > 3 %. Script = 0 % (sin IA). Ninguna toca la Órbita en esta sesión: son **propuestas**.

| Orden | Propuesta | Valor | Esf. | Por qué |
|---|---|---|---|---|
| 1 | **Script de desincronía sin IA** (`scripts/auditar_sincronia.py`). Detecta: celdas de la Matriz revisadas después del último movimiento de su capa; voces y predicciones con plazo vencido; eventos pasados sin resultado; `coincide_radar=false`; [P] de informes de los últimos 7 días que no están en ningún JSON | 5 | S (script) | Convierte los hallazgos (b) y (c) en una lista diaria automática. Joel deja de tener que señalar los huecos |
| 2 | **Volcar a la Línea de tiempo los 21 hechos de (b)** y corregir C1-C5 | 5 | S (~1 %) | La Línea de tiempo es la vista con reacción de precios y hoy le faltan los hitos de octubre |
| 3 | **Calendario con campo `resultado`** y vista «esperado frente a ocurrido» | 5 | M | 45 eventos pasados sin cierre. Es la base para medir fuentes y predicciones |
| 4 | **Bloque «Parecido a…» en Resumen**: 6-8 indicadores (10 años, 30 años, Brent, IPC, high yield, VIX, Nasdaq diario, tipo de la Fed) con percentil histórico y «último precedente» | 5 | M (script FRED, 0 % al automatizar) | Da contexto histórico sin opinar. Datos [P] gratuitos |
| 5 | **Matriz, columna Política monetaria**: rellenar dirección, valor y fecha desde `tipos_vivos` automáticamente; «caduca» = próxima reunión, no +3 meses | 4 | S-M | Evita C1 y C2 para siempre |
| 6 | **Separar titulares del bot de hechos** en la Línea de tiempo: filtro «solo P/S verificados» por defecto y campos `fecha_sesion` / `fecha_publicacion` | 4 | S | Evita C5 y el ruido de la capa de energía |
| 7 | **Registro único de hechos con identificador** (`hechos.json`), del que leen la Línea, la Matriz, Voces y el Calendario | 5 | L | Corta de raíz el «mismo hecho en 5 sitios». **A favor:** consistencia, buscador global real, menos mantenimiento. **En contra:** migración costosa, riesgo de romper vistas que funcionan, y el script de la propuesta 1 ya da el 70 % del beneficio [ESPECULACIÓN]. Hacerlo solo si el script sigue encontrando más de 10 desincronías a la semana |
| 8 | **Voces más allá de cripto**: bancos centrales (actas y discursos), AIE/OPEP, ministros y candidatos del 29-N, con la etiqueta de sesgo de cada voz (promocional, institucional, partidista) | 4 | M | Hoy 0 voces en energía, política y liquidez |
| 9 | **Cajón «xrp» de cada capa → «Lente personal»**, plegado y fuera de la vista por defecto | 4 | S | Criterio de Joel: el tablero es general y la tesis es una lente |
| 10 | **España 29-N**: seguimiento neutral de los programas (fiscal, vivienda, ahorro, cripto), leyes caducadas por el art. 207 y calendario poselectoral (Cortes el 23-dic, investidura) | 4 | M | Es el evento de España de más peso del trimestre |
| 11 | **Fichas o alias de país** para Canadá, Corea, Hong Kong, Arabia Saudí, Taiwán y la UE (ya tienen hechos) | 3 | M | Cierra «hechos sin ficha» |
| 12 | **«Depósitos tokenizados»: fusionar con Tokenización** o alimentarla trimestralmente | 3 | S | Lleva 305 días con 1 hecho |
| 13 | **Indexar `research/fuentes-nuevas` y `research/verificaciones`** en el buscador local y en la «Biblioteca» de la Órbita | 3 | S | 16 [P] sin uso |
| 14 | **Archivar informes superados** (C81, C98, la parte previa de C30), como ya proponía la auditoría del 8-nov | 2 | S | Menos ruido en la búsqueda |

---

## Rutinas añadidas a `research/tareas.csv` (sin duplicar R00, W02-W11 ni G61-G66)

| Id | Frecuencia | Qué | Coste |
|---|---|---|---|
| W12 | Diaria | Volcado: [P] nuevos de los informes del día → Línea de tiempo y Matriz (con el script de la propuesta 1 cuando exista) | ~0,5 % |
| W13 | Semanal (lunes) | Sincronía y cobertura: `auditar_cobertura.py`, `contradicciones_paneles.py` y el futuro `auditar_sincronia.py`; corregir lo que salga | 0 % script + ~0,5 % |
| W14 | Semanal (domingo) | Cierre del Calendario: resultado de los eventos pasados de la semana y plazos vencidos de predicciones y voces | ~0,5 % |
| W15 | Mensual (primera semana) | «Parecido a…»: comparaciones históricas con FRED y BCE y percentiles; anotar precedentes nuevos | 0 % script + ~0,5 % |
| W16 | Mensual (segunda semana) | Capas lentas: CBDC, stablecoins, tokenización, depósitos tokenizados y custodia, con fuentes oficiales (BIS, FSB, BCE, HKMA, MAS, OCC, Fed, DTCC) | ~2 % |
| W17 | Trimestral | Matriz de riesgos: revisar los 7 escenarios con sus desmentidores y el sesgo de las voces | ~2 % |
| W18 | Trimestral | Países y voces: rotar los 9 países con ficha y 0 hechos; añadir voces no cripto (bancos centrales, energía, política) | ~2 % |
| W19 | Anual (diciembre) | Estructura y calendario del año siguiente: reuniones de bancos centrales, subastas, elecciones y cumbres; revisar capas, temas de la Matriz y cadencias; archivar informes superados | ~4 % |

**Dónde se ven las rutinas y qué falta para el planning:**
- Las 8 rutinas están en `research/tareas.csv` y en el Seguimiento del móvil (`docs/movil/seguimiento.json`), ya regenerados.
- No salen todavía en la línea «Periódicas (próxima)» de `research/PLANNING.md`, porque esa lista está escrita a mano en `scripts/construir_seguimiento.py` (diccionarios de las líneas 250-260: nombre, coste, día y cadencia de W01-W10).
- **Propuesta:** añadir ahí W12-W19 con su día y su cadencia. No se ha tocado porque es un archivo existente.

## [VERIFICAR] abiertos en este informe
- Si el proyecto de ley de DAC8 seguía en trámite el 6-oct. La API del BOE no devolvió ninguna ley; falta mirar el expediente en congreso.es.
- Precedentes «de memoria»: Bybit en 2025, la Fed en 1980 y 1998-99, los PGE de 2019-2020. Se pueden cerrar con FRED (DFEDTAR) y el aviso del FBI.
- Estado en 2026 de Nexus, Mandala, Partior, Fnality y de la libra digital; fecha oficial del T+1 en la UE.
- Causa de las caídas del 4 y 5-nov (IA y regulación): hoy solo atribución de prensa.
- Resultado certificado de las legislativas de EE. UU.
