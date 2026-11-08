# Ideas para ampliar la Órbita (C228, 9-nov-2026)

Origen: Joel (9-nov): «me estás dando poco», falta información, sobre todo de España. Sin recomendaciones de compra/venta: solo información. Nivel de cada dato: P (fuente primaria/oficial), S (secundaria), [VERIFICAR] hasta que se lea la fuente. Las URLs y cadencias son [propuesta] y deben comprobarse al implementar [VERIFICAR].

## 1. Qué hay hoy (resumen, sin repetir)
- **España** (`espana.json`, `espana-manual.json`, `espana-pagos.json`, `espana-judicial.json`, `espana-mortalidad.json`, `espana-presupuesto.json`): ingresos/gasto AAPP (Eurostat), recaudación AEAT, paro SEPE, sector exterior, rescate bancario, vivienda/hipotecas (parcial), inmigración, DANA, incendios EFFIS, siniestralidad DGT y laboral, criminalidad, previsión AIReF, deuda del Tesoro, subvenciones BDNS y contratos PLACSP, casos judiciales, mortalidad semanal, Presupuesto/IGAE.
- **Países/riesgo:** 23 fichas (`paises.json`), calificaciones, deuda FMI, reservas, estabilidad, elecciones, mandatos de bancos centrales, regulación cripto por jurisdicción (8 temas), voces.
- **Mercado/macro:** precios vivos y paneles, indicadores y liquidez (manuales), historia de indicadores, tipos, valoración sectorial.
- **Ya en cola (no se repite aquí):** C201 (automatizar tipos/indicadores), C203 (fichas por activo), C205–C210 (tesis privada, alertas, cartera, modo familia, capas ETF XRP/XLM, stablecoins, vivienda y combustibles UE), C213, C217–C223 (comparadores, calendario, glosario, mercado, rendimiento), C224/C225 (línea de tiempo y noticias).

## 2. Criterios
Valor (1-5, para decidir a largo plazo) · Esfuerzo (S ≤1 %, M 1-3 %, L >3 % de cuota semanal) · Fuente oficial · Periodicidad · Dónde encaja (pestaña/archivo existente; **no se crean capas nuevas**: todo cuelga de España, Países, Macro, Calendario, Matriz o Línea de tiempo).

## 3. Ideas (36)

### A. España (la carencia que señala Joel)
| # | Idea | Valor | Esf. | Fuente oficial | Periodicidad | Encaja en |
|---|---|---|---|---|---|---|
| 1 | IPC desglosado (vivienda, energía, alimentos, subyacente) y diferencial con la zona euro | 5 | S | INE (IPC) + Eurostat HICP | mensual | España › indicadores (`espana-manual.json`) |
| 2 | EPA: paro, tasa de actividad, paro juvenil y por CCAA | 5 | S | INE (EPA) | trimestral | España, junto a paro SEPE |
| 3 | Afiliación a la Seguridad Social y relación afiliados/pensionistas | 5 | S | Seg. Social (estadísticas) | mensual | España › pensiones |
| 4 | Pensiones: gasto, pensión media, déficit contributivo y fondo de reserva | 5 | M | Seg. Social, AIReF, Ministerio de Inclusión | mensual/anual | España › gasto |
| 5 | Precio de vivienda (compraventa y alquiler) y esfuerzo de acceso por CCAA | 5 | M | INE (IPV), Registradores, Banco de España, Mitma (Observatorio) | trimestral | España › vivienda (ya hay hipotecas) |
| 6 | Hipotecas: Euribor 12 m, firmadas, tipo medio y variable/fija | 4 | S | BdE, INE (hipotecas), Banco de España (Euribor) | mensual | España › vivienda; enlaza con `tipos-manual.json` |
| 7 | Electricidad: precio mayorista diario, mix renovable y apagones | 4 | M | OMIE, Red Eléctrica (REData) | diaria/semanal | España › energía; Calendario no |
| 8 | Combustibles: gasolina/diésel vs media UE y fiscalidad | 3 | S | Boletín Petrolero UE, MITECO | semanal | España › energía (cubre C210) |
| 9 | Gas: almacenamiento y dependencia por origen | 4 | M | ENAGAS, Eurostat, AGSI+ | semanal | España › energía; Países (Rusia/Argelia) |
| 10 | Embalses y sequía (reserva hídrica) | 3 | S | MITECO (boletín hidrológico) | semanal | España › clima/riesgos (junto a DANA, incendios) |
| 11 | Deuda por CCAA y fondos de liquidez autonómica | 4 | M | BdE (deuda PDE), Hacienda (FLA) | trimestral | España › deuda |
| 12 | Morosidad bancaria y crédito a hogares/empresas | 4 | S | Banco de España | mensual | España › banca (ya hay rescate bancario) |
| 13 | Balanza de pagos y posición de inversión internacional | 3 | M | BdE | trimestral | España › exterior |
| 14 | Turismo: llegadas, gasto, ocupación | 3 | S | INE (Frontur/Egatur) | mensual | España › exterior |
| 15 | Productividad, salarios y SMI (real vs inflación) | 4 | S | INE (ETCL), BOE (SMI), Eurostat | trimestral/anual | España › empleo |
| 16 | Demografía: natalidad, saldo vegetativo y envejecimiento (dependencia) | 4 | S | INE (MNP), Eurostat | anual/mensual | España (junto a inmigración) |
| 17 | Fiscalidad cripto: modelos 172/173/721, plazos y cambios normativos | 5 | M | AEAT, BOE, Hacienda | por evento | España + Regulación (tema fiscal) + Calendario |
| 18 | MiCA en España: CASP autorizados y supervisión CNMV | 4 | S | CNMV, ESMA (registro CASP) | mensual | Regulación › ley marco/custodia |
| 19 | BOE vigilante: normas que afectan a ahorro, vivienda, impuestos | 4 | M | BOE (sumario, API abierta) | diaria (resumen semanal) | Línea de tiempo + España judicial (ya hay `_vigilante`) |
| 20 | Sanidad y dependencia: listas de espera, gasto por CCAA | 2 | M | Ministerio de Sanidad, IMSERSO | trimestral | España › servicios (resultados_servicios) |
| 21 | Concursos de acreedores y creación/disolución de sociedades | 3 | S | INE (EMPRESAS), Registradores | mensual | España › empresas |
| 22 | Ciberincidentes y apagones de infraestructuras críticas | 2 | M | INCIBE-CERT, CCN-CERT | trimestral | España › riesgos [VERIFICAR] |

### B. Grandes potencias, conflictos y energía (Países, Línea de tiempo)
| # | Idea | Valor | Esf. | Fuente oficial | Periodicidad | Encaja en |
|---|---|---|---|---|---|---|
| 23 | Conflictos activos: tipo, país, fechas y última actualización, con ≥2 fuentes | 5 | L | UCDP (Uppsala), ACLED, ONU/OCHA | semanal | Línea de tiempo (cubre C224/C225) |
| 24 | Sanciones vigentes (UE/EE. UU.) por país y sector con fecha | 4 | M | EUR-Lex, OFAC, Consejo UE | por evento | Países › ficha; Línea de tiempo |
| 25 | Gasto militar y comercio de armas por país | 3 | S | SIPRI (anual) | anual | Países › ficha |
| 26 | Aranceles y comercio bilateral (EE. UU.–China–UE) | 5 | M | USTR, OMC, Eurostat Comext | mensual/por evento | Países + Calendario |
| 27 | Energía por país: mix, importaciones, reservas estratégicas | 4 | M | IEA, Eurostat, EIA | trimestral/anual | Países (comparador C217) |
| 28 | Cadena de chips/IA: controles de exportación y fábricas | 3 | M | BIS (EE. UU.), TSMC/ASML informes | por evento | Países › ficha (EE. UU., China, Taiwán) |
| 29 | Reservas de oro y composición (COFER) de bancos centrales | 3 | S | FMI (IFS/COFER), WGC | trimestral | Riesgo país › reservas (ya existe) |
| 30 | Calendario de cumbres y reuniones (G20, BRICS, OPEP+, BCE, Fed) | 4 | S | web oficial de cada organismo | calendario | Calendario (con filtro por país, C220) |

### C. Utilidad transversal (Resumen, Matriz, Noticias)
| # | Idea | Valor | Esf. | Fuente | Periodicidad | Encaja en |
|---|---|---|---|---|---|---|
| 31 | «Qué ha cambiado esta semana en España» (5 líneas con enlace) | 5 | M | derivado de 1-19 | semanal | Resumen (modo foco C219) |
| 32 | Semáforo de España vs UE-27 en 8 indicadores | 4 | M | Eurostat | mensual/trim. | España; Matriz (fila España) |
| 33 | Cada cifra con «para qué sirve» y qué la movería (sin predicción) | 4 | M | glosario propio | — | Glosario flotante (C221) |
| 34 | Mapa de dependencias: qué dato de España/países mueve qué activo de Joel (XRP, XLM, ETF) | 3 | M | derivado | — | Matriz [ESPECULACIÓN] etiquetada |
| 35 | Registro de «datos que fallaron» (fuente caída/cambio de formato) | 3 | S | `fallos` ya existe en los JSON | diaria | Resumen › frescura (C215) |
| 36 | Referentes de escritorio: revisar 3-4 terminales públicos (Eurostat Dashboard, FRED, Our World in Data, Bloomberg-like) y listar sus pestañas | 3 | S | web pública | una vez | decisión de diseño, sin código |

## 4. Priorización (valor/esfuerzo y cuota)
1. **Pack macro España** (ideas 1, 2, 3, 6, 15): todo INE/Seg. Social/BdE, gratis, mensual-trimestral, esfuerzo S cada una; llena el hueco más grande.
2. **Vivienda y alquiler** (5, 11, 12): es el problema más citado de España y entra por el tema vivienda ya existente.
3. **Pensiones y demografía** (3, 4, 16): determina presión fiscal futura.
4. **Fiscalidad y regulación cripto en España** (17, 18, 19): directo a la situación de Joel como inversor en España; fuentes BOE/AEAT/CNMV.
5. **Energía España** (7, 8, 9, 10): precios y dependencia; reutiliza C210.
6. **Conflictos y sanciones** (23, 24, 26): ya cubierto por C224/C225; añadir fuentes UCDP/ACLED y datos de aranceles.

## 5. Notas y riesgos
- Cada dato debe llevar fuente oficial, fecha, nivel y nota «qué mide / qué no mide»; si no se lee la fuente, queda [VERIFICAR].
- Hay límite de datos manuales: priorizar los que tienen API/CSV (INE, Eurostat, BdE, REE, BOE) para no crear mantenimiento (C201).
- Las ideas 31-34 usan lo ya recogido; no cuestan cuota de research.
- No se propone ninguna capa nueva: todo cuelga de España, Países, Macro, Regulación, Calendario o Línea de tiempo.

## 6. Cinco elegidas → tareas C229-C233
C229 pack macro España · C230 vivienda/alquiler/crédito · C231 pensiones y demografía · C232 fiscalidad cripto y MiCA en España · C233 energía España.
