# Plan de actualización de datos (3-nov-2026)

Consolida los cinco informes de fuentes de `research/fuentes-nuevas/` (A tipos, B hipotecas y crédito, C España, D zona euro y EE. UU., E Sudamérica). Las pruebas de acceso las hicieron agentes el 3-nov con curl (User-Agent identificado) y, si había 403, una vez con Chrome. Lo que verifiqué yo a mano el 3-nov: Banco de Canadá 2,50 % (API Valet, 29-30 oct) y Selic 13,75 % (BCB SGS 432). Nada de esto es recomendación de compra ni venta.

## 1. ¿Está terminada la tabla de tipos de interés? No
- Cubre 15 bancos (Fed, BCE, BoE, Brasil y Canadá con fuente primaria; otros 10 vía BIS). Faltan RBA, RBNZ, Riksbank, Norges, Colombia, Chile, Perú y Argentina (Argentina no tiene tipo de política desde jul-2025: mostrar TAMAR/BADLAR como «no comparable»).
- El BIS va días por detrás (Canadá: BIS 2,25 %, oficial 2,50 % desde el 29-oct). Regla: Fed, BCE, BoE, Canadá y Brasil siempre por su fuente primaria; el BIS solo como respaldo.
- Cierre propuesto: ampliar `URL_BIS_TIPOS` en `scripts/actualizar_paneles.py` con AU, NZ, SE, NO, CO, CL, PE; y APIs abiertas sin clave para Riksbank, Norges, SNB y BCRP (probadas OK). RBA se lee con Chrome (4,60 % desde 30-sep); RBNZ queda manual.
- Corregir la ficha de Canadá (aún 2,25 %).

## 2. Cadencias (el disparador es el calendario oficial, no el reloj)
| Cadencia | Datos | Disparador |
|---|---|---|
| Diaria | Curvas de bonos, €STR/RRP, luz (OMIE), mercado cripto, subastas en su día | Cada día; las subastas del Tesoro (3, 5, 10, 19-nov) el día de resultados |
| Semanal | Freddie Mac (jueves), balances Fed/Eurosistema, CFTC (viernes), EIA | Día de publicación |
| Día de decisión de un banco central y el siguiente | Tabla de tipos | Fechas del apartado 3 |
| Mensual | España: paro y afiliación (2.º-3.er día hábil), IPC (~13-15), hipotecas INE (~25), deuda PDE (~17), balanza (fin de mes). EE. UU.: empleo, IPC, PCE. Zona euro: IPCA, paro. BCE MIR/BSI. Brasil (SGS, Focus) | Día de publicación del calendario oficial |
| Trimestral | PIB, EPA, salarios (ETCL), precios de vivienda (IPV), BLS del BCE, SLOOS | Tras cada publicación |
| Anual | Estructura salarial, Padrón, calificaciones, escala del ahorro (art. 66 LIRPF) | Fecha oficial |

## 3. Próximas citas (fuente oficial salvo [VERIFICAR])
- **Tipos:** 3-nov RBA · 3-4 nov Copom [VERIFICAR, prensa] · 4-nov Riksbank · 5-nov BoE y Norges [VERIFICAR] · 9-dic Fed, BoC, RBNZ, Copom [VERIFICAR] · 10-dic SNB [VERIFICAR] · 15-dic BCCh [VERIFICAR] · 17-dic BCE (la decisión es el 17; el calendario del repo anota el día 1).
- **España:** IPC 13-nov, 27-nov, 15-dic, 30-dic · deuda PDE 17-nov y 15-dic · hipotecas INE 25-nov · balanza 30-nov · IPV 3T 4-dic · ETCL 3T 17-dic · PIB 3T 23-dic. El calendario del INE de 2027 aún no existe.
- **EE. UU.:** empleo 6-nov · IPC 10-nov · PCE 25-nov (calendarios BLS hasta dic-2027, BEA hasta el 23-dic-2026).
- **Argentina (INDEC, contrastar columnas del PDF):** IPC oct 12-nov, IPC nov 15-dic, EMAE 24-nov, PIB y empleo 3T 17-18 dic.
- **Petróleo:** informe OPEP 11-nov, AIE 13-nov (ya en `eventos/calendario.toml`); próxima reunión de OPEP+ sin confirmar.

## 4. Qué automatizar primero (orden)
1. Tipos faltantes (apartado 1) · 2. España: IPC y PIB del INE como serie viva (códigos nuevos: `IPC290750`; la `IPC251856` quedó congelada en dic-2025), paro y afiliación, deuda PDE, subastas del Tesoro · 3. Hipotecas: INE (IPV e hipotecas), morosidad oficial, Eurostat precios de vivienda · 4. EE. UU. vía FRED: SLOOS (DRTSCILM, DRTSCLCC), Case-Shiller, PCE core, nóminas/JOLTS, RRP · 5. Brasil: SGS (Selic, tipos de financiación inmobiliaria 20774/25499), Focus, IBGE · 6. Argentina (BCRA v4, datos.gob.ar), Perú (BCRP), Colombia (TRM) · 7. Zona euro: Bundesbank, INSEE, subastas de Italia.
- Ojo con trampas conocidas: `prc_hicp_manr` y las series `ICP…ANR` del BCE están congeladas en dic-2025 (usar `prc_hicp_minr`); el agregado de la zona euro ya es `EA21`.
- SLOOS: la Fed retira la semana del 9-nov solo el paquete «Build Your Package» del DDP, no el SLOOS; leer desde FRED.

## 5. Bloqueos y permisos pendientes
- **Bloqueados (no se saltan):** congress.gov, senate.gov, CNMV (403; Chrome sin texto), Notarios, Idealista, MBA, SBS Perú, Superfinanciera, bcentral.cl, RBNZ, FMI DataMapper con User-Agent identificado, AFT (solo con Chrome).
- **Piden registro gratuito (no creado):** Banxico, BCCh, BEA, EIA v2, Census, ESIOS. FRED cubre parte de BEA/EIA/Census.
- **Requieren tu OK de descarga:** PDF de Registradores (9,3 MB), calendarios PDF de INE y Tesoro, descargas de CMF y BIS.
- Matiz al `MAPA-DE-FUENTES.md`: bls.gov bloquea las páginas, pero `api.bls.gov` y su calendario responden 200 con User-Agent identificado.

## 6. Discrepancias abiertas ([VERIFICAR])
- Selic: SGS 432 (oficial) 13,75 %; prensa citada por el agente E: 14,25 % desde junio. No contrastado con el comunicado del Copom.
- Qué miden los códigos SGS de deuda (4503, 4513), morosidad y saldo de crédito.
- Clave del BCE para morosidad (SUP) y TARGET2 (`TGB`); `emp_es` definida pero ausente de `paneles.json`.
- Códigos vivos del INE para tasa de paro EPA, IPCA, IPV y salarios.
- Paro registrado de octubre (sale hoy), pensiones, Registradores y AIReF: solo prensa [S].
- Tipos de Colombia (12 %) y calendario de BanRep, BCRP y BCCh 2027.

## 7. Correcciones al repo propuestas (sin hacer)
- `eventos/calendario.toml`: reuniones de dos días con el día de la decisión (BCE 17-dic, Fed 9-dic, BoJ 30-oct y 18-dic) para que el aviso diario no salte el día equivocado.
- Ficha de Canadá a 2,50 %; ampliar `URL_BIS_TIPOS`; actualizar `MAPA-DE-FUENTES.md` con las fuentes nuevas de cada informe.
