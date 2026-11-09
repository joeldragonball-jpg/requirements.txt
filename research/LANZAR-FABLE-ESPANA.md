# Plan «España desnuda» para el tablero de inteligencia (Fable · 2 ventanas de 5 horas)

Objetivo de Joel (9-nov-2026): que España quede **abierta de arriba abajo** en la Órbita: quién gasta, en qué, con qué contratos y subvenciones, qué leyes cambian, qué investigaciones hay abiertas, cuánto se debe y a quién, sueldos, vivienda, pensiones, energía y cripto. Más detalle que la prensa, con fuente primaria y cifras sin ambigüedad. **Hechos y fuentes; sin recomendaciones de compra/venta; presunción de inocencia en todo lo judicial.**

## Cómo usarlo
1. Abre cada sesión tú, con **Fable 5.2 y esfuerzo alto** (selector de modelo). Una sesión por bloque (S1, S2…), para que el contexto no se llene.
2. Pega SOLO esta línea (cambia el bloque): `Continuamos cartera-github (fecha de hoy). Responde en español y sigue CLAUDE.md. git pull y git status. Lee research/LANZAR-FABLE-ESPANA.md (reglas comunes + bloque S1) y ejecútalo.`
3. **Ventana 1** (tras el reinicio del martes 10-nov a las 02:00): S1 → S5. **Ventana 2** (cuando se agote la primera o tras pulsar «Restablecer gratis», antes del 16-nov): S6 → S11.
4. Pulsa «Restablecer gratis» después de haber gastado mucho con Fable, no antes (devuelve lo que Fable gastó del semanal).
5. Al acabar cada bloque, la sesión actualiza `research/tareas.csv`, ejecuta `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py` y te pregunta «¿Actualizo el Seguimiento y el planning?». Commit/push solo con tu «sube» (las rutinas programadas suben solas y pueden arrastrar lo que haya sin subir; revisa `git status`).

## Reglas comunes (valen para todos los bloques)
- **Fuente primaria primero** (BOE, IGAE, INE, Banco de España, AEAT, Congreso, Tribunal de Cuentas, PLACSP, BDNS, Fiscalía Europea, OLAF, Audiencia Nacional/CGPJ). Prensa solo como [S] con medio y fecha. Lo no leído: [VERIFICAR]. Predicciones y opiniones: [ESPECULACIÓN]. Cada dato con fuente, fecha y nivel P/S/V.
- **Si un sitio bloquea scripts, usa Chrome** (`research/ACCESOS-CHROME.md`) antes de darlo por bloqueado.
- **Cifras con unidad y escala explícitas** (M€ = millones de euros, mil M€ = miles de millones). En JSON: número puro + `unidad` + `escala`; en pantalla, punto de miles y coma decimal. (Regla de C240.)
- **Una sola página, sin capas nuevas**: cuelga todo bajo España y vincula a la política/tema existente. Extiende `explorador/espana*.json` sin romper su formato; no toques `cerebro/` existente (solo añade).
- Contrasta caso alcista y bajista donde haya inversión de por medio; señala sesgos de la fuente.
- No llames a la API de Anthropic ni lances workflows; nunca escribas claves; repo público: nada privado.
- Cada bloque: informe `informes/research/AAAA-MM-DD-<id>-<tema>.md` (máx. 5 líneas de lecciones), fila en `research/tareas.csv`, regenerar móvil y seguimiento. Aviso de contexto: al 50-75 % no empieces nada grande; al 75 % da el relevo con `python scripts/generar_relevo.py --resumen "..."`.

## VENTANA 1

### S1 · C239 — Investigaciones y fondos públicos (Adif, Transportes, UE, accidente ferroviario)
Prompt completo: `research/prompts/C239-espana-investigaciones-fondos.md`. Añade: enlaza cada investigación con los contratos reales de S2 (ID de expediente en PLACSP) cuando exista; si no consta, déjalo sin vincular.

### S2 · C241 — «A dónde va el dinero»: contratación pública y subvenciones
Fuentes ya probadas en `research/fuentes-nuevas/F-gasto-contratos-deuda.md` (PLACSP: feed ATOM y ZIP mensual de licitaciones y menores; BDNS: API `infosubvenciones.es/bdnstrans/api/` con convocatorias, concesiones, sanciones, partidos y grandes beneficiarios).
1. Script local `scripts/leer_contratacion.py` (sin IA, sin claves): descarga el ZIP del último mes de PLACSP y de contratos menores y agrega por órgano (Adif, Ministerio de Transportes, Defensa, Sanidad, Interior…), por tipo de procedimiento (abierto, negociado, **emergencia**, menor) y por adjudicatario; marca concentración (mismo adjudicatario repetido, % de contratos por emergencia o menores). Datos agregados, no listas de personas físicas.
2. Script `scripts/leer_bdns.py`: concesiones del último año por órgano concedente y mayores beneficiarios; partidos políticos y sanciones desde sus endpoints.
3. Salida: `explorador/espana-contratacion.json` y `explorador/espana-subvenciones.json` + vista en España › «Dónde va el dinero». Importes con unidad y escala. Límites honestos: qué no cubre PLACSP (CCAA que usan su propia plataforma, menores no publicados) y por qué un adjudicatario repetido NO implica irregularidad.
4. Cierra con 10 hechos verificables que sorprendan por cifra (con enlace al expediente o concesión).

### S3 · C238 — Leyes nuevas y modificaciones (BOE, Congreso)
Prompt completo: `research/prompts/C238-espana-leyes-boe.md`. Haz primero el barrido de 90 días y luego `scripts/vigilante_boe.py` (sumario diario por palabras clave, sin IA, sin activar el workflow hasta tu OK). Cada ley: qué cambia, quién se ve afectado, entrada en vigor, enlace al BOE.

### S4 · C229 — Pack macro de España
IPC desglosado (general, subyacente, alimentos, vivienda, energía; **etiquetar si el dato es SA o NSA**, como C236), EPA (paro total y juvenil, por CCAA), afiliación a la Seguridad Social, salarios y SMI, Euríbor y tipo medio de hipotecas, PIB trimestral, balanza de pagos. Fuentes: INE (API JSON), Banco de España, Seguridad Social, Eurostat, BCE. Hacer que `scripts/indicadores.py` los lea solo (patrón de C201) para que no envejezcan. Un panel España › macro con serie corta y semáforo de frescura.

### S5 · C230 — Vivienda y deuda autonómica (FLA frente a PDE)
Precio y alquiler (INE, Registradores, Ministerio de Vivienda), esfuerzo de acceso por CCAA, hipotecas firmadas. **Deuda de las CCAA en dos conceptos separados**: deuda con el Estado (FLA y otros mecanismos) y deuda total PDE (Banco de España, Boletín Estadístico: [VERIFICAR] el capítulo y la tabla exactos). Qué significaría una condonación en cifras (M€, % del PIB regional). Comparador de CCAA lado a lado.

## VENTANA 2

### S6 · C77 + C69 — «Dónde va cada euro»: gasto por ministerio, comunidad, municipio y comparativa 2024-2025
Prompts: `research/prompts/C69-espana-2024-vs-2025.md` y filas C65-C67/C77 en `research/tareas.csv`. Clasificación orgánica, funcional y económica (capítulos 1, 2, 4, 6, 7) con la **ejecución real de la IGAE**, no solo lo presupuestado. Presupuestado frente a ejecutado y variación. Descargas con OK de Joel. Datos en `explorador/espana-presupuesto.json` (368 KB: no leerlo entero, buscar con Grep).

### S7 · C231 + C233 — Pensiones, demografía y energía
Pensiones: gasto, déficit contributivo, fondo de reserva, relación afiliados/pensionistas (Seguridad Social, AIReF). Demografía: natalidad, saldo migratorio, envejecimiento (INE). Energía: precio eléctrico (OMIE/REE), combustibles frente a la UE, gas y dependencia exterior, vinculado a Ormuz y al Brent ya en la Órbita.

### S8 · C232 — Fiscalidad cripto en España, MiCA y CASP
Modelos 172/173/721, FIFO, permutas, DAC8, Ley de Mercados de Valores y CNMV, CASP autorizados en España, tratamiento de stablecoins y staking. Cada punto con BOE/DGT/CNMV y fecha. **Informativo, no asesoramiento fiscal**; lo no leído en BOE/DGT = [VERIFICAR] (hay verificaciones abiertas sobre la escala del ahorro 2026 y los modelos).

### S9 · C242 — Congreso, partidos y altos cargos
Votaciones y asistencia, iniciativas y su estado (Congreso, Senado), financiación y cuentas de partidos (Tribunal de Cuentas, BDNS), declaraciones de bienes e intereses de altos cargos (Portal de Transparencia), sueldos con `C68/C68B`. Solo datos oficiales y neutrales (sin ranking de «los peores»); señalar sesgos de la fuente.

### S10 · C243 — Empresas públicas y comparador de CCAA
SEPI y sus empresas (Adif, Renfe, Correos, Enaire, Ineco…): resultados, deuda, subvenciones recibidas (BDNS) y contratos (S2). Comparador de comunidades: gasto per cápita, deuda, paro, vivienda, renta. Vincular con las investigaciones de S1 por organismo, sin sacar conclusiones de culpabilidad.

### S11 · Cierre (Sonnet basta)
C237 tercera pasada (xrp, xlm y España con `python scripts/cobertura_hechos.py`), C240 (unidades y escala en todas las tablas con `scripts/auditar_unidades.py`), `python scripts/auditar_cobertura.py`, y un informe «España: qué cubre ya la Órbita y qué sigue faltando» con huecos honestos (qué fuente no responde, qué no se pudo verificar).

## Qué NO hacer
No gastar Fable en tareas mecánicas (C240, rutinas W/R00): van con Sonnet. No volcar nada sin fuente. No inventar causas ni culpables.
