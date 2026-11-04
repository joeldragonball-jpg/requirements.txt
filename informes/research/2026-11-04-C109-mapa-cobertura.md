# C109 · Mapa de cobertura temática y plan de automatización (4-nov-2026)

Sin API de Anthropic, sin workflows lanzados, sin descargas de PDF/binarios. Pruebas con `curl` y User-Agent `cartera-joel/1.0 (uso personal)` el 4-nov-2026. Nivel de fuente: [P] primaria/oficial, [S] secundaria. No es asesoramiento de inversión: son datos de contexto.

## Resumen
1. Nivel A (países) está bien cubierto: 12 países × 9 indicadores en `paneles.json › indicadores` (ipc, paro, paro juvenil, pib, deuda, déficit, pobreza, gini, salario mínimo), más defensa, tipos, inflación, vivienda UE y deuda FMI.
2. Nivel B (España) tiene mucho texto y datos manuales (presupuesto, DANA, inmigración, opacidad, hipotecas), pero **pagos/contratos, tráfico, delitos, siniestralidad laboral e incendios no están en ningún panel**.
3. Nivel C está casi vacío: solo oro, plata, cobre, gas Henry Hub, trigo, maíz, café y Brent en `materias`. Sin electricidad, TTF, agua, soja, arroz, azúcar, fertilizantes, FAO, RAM ni centros de datos.
4. **Casi todo el nivel C se puede automatizar sin IA ni clave**: probados 200 en OMIE, REE (apidatos), FRED (precios FMI de materias), FAO (CSV), Eurostat y Yahoo (futuros). Bloqueados o con clave: ENTSO-E (token gratis), urea/potasa/DAP (Banco Mundial en xlsx), RAM/DRAM (pago).

## 1. Matriz de cobertura (comprobada)
Estado: **Panel** = dato vivo en `explorador/*.json`; **Manual** = en `explorador/*-manual.json` o `espana-manual.json`; **Informe** = solo texto en `informes/` o `research/`; **Nada** = no aparece (búsqueda con grep en informes, research y explorador).

| Tema | Nivel | Estado hoy | Dónde |
|---|---|---|---|
| IPC, paro, PIB, deuda, déficit, pobreza, Gini, salario mínimo (12 países) | A | Panel | `paneles.json › indicadores` |
| Tipos de interés / bonos | A | Panel | `tipos_vivos`, `tipos_bis`, `bonos` |
| Gasto en defensa (% PIB) | A | Panel | `defensa` |
| Vivienda UE (precios) | A | Panel | `vivienda_eurostat` |
| Deuda y calificaciones | A | Panel + Manual | `deuda-fmi.json`, `calificaciones.json` |
| Población, demografía, energía por país | A | **Nada** (parcial en `paises.json` texto) | [VERIFICAR] |
| Balanza comercial/corriente | A | **Nada** como panel | |
| Presupuesto, ingresos/gasto AAPP, personal público | B | Panel + Manual | `espana-presupuesto.json`, `espana.json` |
| Hipotecas, vivienda, paro, IPC España | B | Panel | `espana_ine`, `espana_hipotecas` |
| DANA / catástrofes | B | Manual + Informe | `espana-manual.json › dana`, `research/fuentes-nuevas/H-catastrofes-dana.md` |
| Inmigración | B | Manual + Informe | `espana-manual.json › inmigracion`, fuentes-nuevas/G |
| Opacidad, recaudación vs infraestructuras | B | Manual | `espana-manual.json` |
| Contratos (PLACSP) y subvenciones (BDNS) | B | Informe (pocas menciones) | fuentes-nuevas/F; C77 |
| Defunciones / exceso de mortalidad (MoMo) | B | Informe | C77, fuentes-nuevas/H |
| Accidentes de tráfico (DGT) | B | **Nada** | |
| Delitos (Balance de Criminalidad) | B | Informe mínimo | fuentes-nuevas/G |
| Siniestralidad laboral | B | **Nada** | |
| Incendios forestales | B | Informe mínimo | C77, H |
| Sanidad | B | Manual (gasto COFOG) | `espana.json › f_sanidad` |
| Petróleo Brent/WTI | C | Panel + histórico | `materias`, `precios_historico` |
| Gas Henry Hub | C | Panel | `materias` |
| Gas Europa (TTF) | C | **Nada** | |
| Trigo, maíz | C | Panel | `materias` |
| Soja, arroz, azúcar | C | Informe (dossier G9) | sin serie |
| Oro, plata, cobre, café | C | Panel | `materias` |
| Electricidad (mayorista y hogar) | C | **Nada** (OMIE solo citado en fuentes-nuevas/C) | |
| Agua por zonas | C | **Nada** | |
| Fertilizantes | C | Informe (R46, de pasada) | |
| Índice FAO | C | **Nada** | |
| Semiconductores (valores) | C | Panel parcial: NVDA, AVGO, AMD, TXN, QCOM en `valoracion.json` (TSMC y ASML no) | |
| RAM/DRAM, NAND | C | **Nada** | |
| Centros de datos | C | **Nada** | |

## 2. Fuente, formato, cadencia y clave por tema nuevo
Pruebas del 4-nov-2026. «Automatizable» = sin IA en `actualizar_paneles.py` (solo stdlib, como el resto).

| Tema | Fuente exacta | Formato / prueba | Cadencia | Clave / OK de Joel | Automatizable |
|---|---|---|---|---|---|
| Electricidad mayorista España | OMIE `marginalpdbc_AAAAMMDD.1` vía `omie.es/es/file-download?parents[0]=marginalpdbc&filename=...` [P] | 200 tras redirección; texto `;`, 24 precios horarios (3-nov: 221,16 €/MWh en la hora 1) [HECHO de la prueba]. La ruta antigua `/sites/default/files/dados/...` da 404 | diaria (día siguiente, ~13:00 CET) | Sin clave | **Sí** (seguir redirección) |
| Electricidad/demanda/PVPC España | REE `apidatos.ree.es` (precios tiempo real, demanda) [P] | 200 JSON | diaria/horaria | Sin clave | **Sí** |
| Electricidad Europa por zonas | ENTSO-E Transparency (`web-api.tp.entsoe.eu`) [P] | 401 sin token | horaria | **Token gratuito: registro de Joel** | Sí, tras token |
| Precio electricidad hogar/industria por país | Eurostat `nrg_pc_204` (hogares) y `nrg_pc_205` (no hogares), gas `nrg_pc_202` [P] | 200 JSON; actualizado 19-oct-2026 | semestral | Sin clave | **Sí** |
| Gas Europa (TTF) | Yahoo `TTF=F` [S] | 200; futuro, retraso | diaria | Sin clave | **Sí** (como `leer_materias`) |
| Gas EE. UU. spot/mensual | FRED `PNGASEUUSDM` (precio gas UE, FMI) [P vía FRED] | 200; sep-2026: 25,49 (ago 20,92) [unidad: USD/MMBtu, VERIFICAR] | mensual | Sin clave | **Sí** |
| Petróleo | ya en paneles; FRED `POILBREUSDM` (sep-2026: 102,02 $/barril) | 200 | mensual | | Ya corre |
| Soja, trigo, maíz, arroz, azúcar (mensual) | FRED `PSOYBUSDM` 481,7; `PWHEAMTUSDM` 246,9; `PMAIZMTUSDM` 236,9; `PRICENPQUSDM` 466,5; `PSUGAISAUSDM` 17,94 (sep-2026) [P, FMI] | 200 CSV | mensual (desfase ~1 mes) | Sin clave | **Sí** |
| Soja, arroz, azúcar (diario) | Yahoo `ZS=F`, `ZR=F`, `SB=F` [S] | 200 | diaria | Sin clave | **Sí** |
| Índice FAO de precios de alimentos | FAO `food_price_indices_data.csv` (enlace en `fao.org/worldfoodsituation/foodpricesindex/en/`, 48 KB) [P] | 200; sep-2026: general 136,0; cereales 122,8; aceites 198,6; azúcar 114,0 (base 2014-16=100). El enlace lleva un hash `sfvrsn` que cambia | mensual (primer viernes) | Sin clave | **Sí**, leyendo la página para extraer el enlace |
| Fertilizantes (urea, amoníaco, potasa, DAP) | Banco Mundial «Pink Sheet» (xlsx mensual) [P]. En FRED las series de urea/potasa/DAP dan 404 | xlsx = binario | mensual | **OK de Joel para descargar xlsx** | No sin descarga; alternativa: Yahoo de empresas (Nutrien, CF) [S] |
| Agua por zonas | Sin API estatal de precios; INE «Encuesta sobre suministro y saneamiento del agua» (precio €/m³ por CCAA) y AEAS/EMASESA [VERIFICAR]. Banco Mundial `SH.H2O.BASW.ZS` (acceso, 200) no mide precio | Tabla INE (probable API Tempus) / PDF AEAS | anual (con 2 años de retraso) | Sin clave; PDF = OK de Joel | Parcial (INE); precios por ciudad: manual [S] |
| Semiconductores (producción) | FRED `IPG3344S` (producción industrial de semiconductores EE. UU., ago→sep-2026: 194,5→198,6) y `PCU334413334413` (precios al productor: 28,5→28,8) [P] | 200 | mensual | Sin clave | **Sí** |
| Semiconductores (valores/ETF) | Yahoo `SOXX`, `TSM`, `ASML`, `MU` [S] | 200 | diaria | Sin clave | **Sí**; TSMC/ASML no están en la valoración (SEC no los cubre igual: 20-F) |
| Ventas globales de chips | SIA/WSTS (`semiconductors.org`) [P] | URL probada 404; nota de prensa mensual | mensual | Chrome | No: manual [VERIFICAR] |
| RAM/DRAM, NAND (spot/contrato) | TrendForce/DRAMeXchange (pago) [S]; Micron en Yahoo como indicador indirecto | de pago | semanal/mensual | **Manual/[S]** | Solo `MU` como proxy |
| Centros de datos: consumo eléctrico | EIA (`api.eia.gov`) exige clave (403 «API_KEY_MISSING») [P]; Eurostat y REE no lo desglosan | 403 | mensual | **Clave gratuita EIA: registro de Joel** | Parcial; capacidad e inversión = informes de empresas [S], manual |
| Contratos públicos | PLACSP `sindicacion_643/...Completo3.atom` | 200, **13 MB** de un solo feed | diaria | Sin clave | Sí, pero pesado: solo contar/agregar con filtro; no guardar |
| Subvenciones | BDNS `infosubvenciones.es/bdnstrans/api/convocatorias/busqueda` | 200 JSON | diaria | Sin clave | **Sí** (contar por día/nivel) |
| Defunciones / exceso de mortalidad | MoMo CSV `momo.isciii.es/public/momo/data` | 200, **~724 MB** (un descarga accidental en la prueba, borrada) | diaria | — | **No tal cual**; usar INE Tempus (tabla de defunciones 6552, 200) o EuroMOMO. Tabla INE sí funciona |
| Accidentes de tráfico | Eurostat `tran_sf_roadus` (200; muertos por categoría); DGT: página HTML 230 KB sin API | 200 | anual | Sin clave | Sí (Eurostat); DGT = microdatos zip, OK de Joel |
| Delitos | Eurostat `crim_off_cat` (200; ES, última actualización 29-abr-2026); Interior: portal estadístico responde 206, la ficha de balances da 403 Cloudflare | 200 / bloqueada | trimestral (Interior) / anual | Sin clave | Eurostat sí; Interior: **Chrome, no saltar** |
| Siniestralidad laboral | Ministerio de Trabajo «Estadística de accidentes de trabajo» | no probada | mensual | | [VERIFICAR] |
| Incendios | EFFIS (JRC) | no probada | diaria | | [VERIFICAR] |
| Nivel A faltante (población, energía, balanza) | Banco Mundial v2 (`EG.USE.ELEC.KH.PC`, 200), Eurostat | 200 | anual | Sin clave | **Sí** |

## 3. Plan de automatización
- **Ya corre solo** (`paneles.yml`, lunes a viernes 21:30 UTC, sin IA ni clave): tic, stablecoins, rwa, mercado, bonos, índices, tipos, BIS, defensa, liquidez, inflación, INE, BdE, Eurostat vivienda, Brasil, Ormuz, crédito, materias, precios histórico, valoración.
- **Podría correr solo con coste cero** (mismo patrón que `leer_materias`: función nueva, conserva el dato anterior si falla): `leer_electricidad` (OMIE + REE + Eurostat), `leer_alimentos` (FRED mensual + FAO CSV + Yahoo `ZS=F/ZR=F/SB=F/TTF=F`), `leer_chips` (FRED `IPG3344S` + Yahoo `SOXX/TSM/ASML/MU`), `leer_bdns` (conteos), `leer_trafico_delitos` (Eurostat). Salida a nuevas claves de `paneles.json` (`energia_precios`, `alimentos`, `chips`), **sin workflow nuevo y sin capa nueva**.
- **Seguirá manual**: fertilizantes (xlsx), RAM/DRAM, centros de datos, precios del agua por ciudad, Interior (criminalidad), DGT, SIA/WSTS. Van a `*-manual.json` con campo `nivel: "S"` y fecha.
- **Punto de entrada único**: `scripts/actualizar_paneles.py` + `paneles.yml` + Worker existentes. Cada serie con campo `desde` (punto de referencia) para comparar trayectorias, como ya hace `materias`.

## 4. Lista priorizada de tareas (valor / coste / riesgo)
Ver sección final «Filas para tareas.csv» (C110-C119). Orden recomendado: C110 > C111 > C112 > C113 > C114 > C115 > resto.

## 5. Qué tiene que hacer Joel a mano
1. **Registrar un token gratuito de ENTSO-E** (Transparency Platform) y guardarlo como secreto de GitHub (no pegarlo en chat).
2. **Clave gratuita de EIA** (opcional, solo centros de datos EE. UU.).
3. **OK explícito** para descargar el xlsx del Pink Sheet del Banco Mundial (fertilizantes) y, si se quiere, microdatos DGT (zip).
4. Abrir en Chrome (con la extensión) las fichas de Interior (Balance de Criminalidad) y SIA/WSTS, que dan 403/404 a curl; no se saltan.
5. Decidir si se quiere pagar o no TrendForce (RAM/DRAM). Mientras, solo proxy `MU`.
6. `appId` de e-Stat (Japón) sigue pendiente de C-anteriores; no cambia aquí.

## 6. Sesgos y límites
- **Definiciones distintas por país**: delitos (Eurostat registra delitos policiales; criterios penales y de registro varían, así que no son comparables sin nota), muertes en carretera (a 30 días vs 24 horas según país), exceso de mortalidad (modelos distintos MoMo vs EuroMOMO). Retrasos: Eurostat delitos actualiza abril, balances trimestrales de Interior van con 1-2 trimestres de retraso.
- **Precios de materias**: los FRED/FMI son medias mensuales (retraso ~1 mes); Yahoo son futuros (rollover, contratos distintos), nivel [S]. Unidades distintas (USX céntimos vs USD): verificar antes de comparar.
- **Electricidad**: OMIE es precio mayorista marginal; el recibo del hogar (Eurostat, PVPC) incluye peajes e impuestos y no es comparable directamente. Precios altos o bajos entre zonas reflejan mezcla energética, interconexión y regulación [OPINIÓN].
- **«Dónde empezó a cambiar todo»**: elegir el punto de referencia introduce sesgo de selección. Mostrar siempre varias fechas de partida y no inferir causa [ESPECULACIÓN].
- **Chips/RAM/IA**: cifras de capacidad e inversión de centros de datos vienen de comunicados de empresas (promoción, hype, conflicto de interés) [S]. Cualquier lectura de ciclo de memoria es [ESPECULACIÓN].
- **No probado**: siniestralidad laboral, EFFIS, series INE de agua y mortalidad concreta, ESIOS (200 pero requiere token para uso real), SPARQL de otros temas. Marcados [VERIFICAR].
- Sin recomendaciones de compra/venta; los tickers son indicadores de contexto.

## Filas para tareas.csv
Columnas: `id,origen,tema,estado,tipo,modelo,tam,est,real,prompt,cuando,falta,bloqueo,detalle`

```csv
C110,C,Nivel C · Panel de electricidad (OMIE + REE + Eurostat) sin IA,pendiente,build,Sonnet,M,~3 %,,"Añade leer_electricidad() a scripts/actualizar_paneles.py: OMIE marginalpdbc (seguir redirección), REE apidatos y Eurostat nrg_pc_204/205; guarda en paneles.json › energia_precios con campo desde; si falla conserva lo anterior; no toques workflows",,,,"Informe C109 §2: OMIE y REE probados 200 el 4-nov; ENTSO-E exige token (C111)"
C111,C,Nivel C · Electricidad Europa por zonas con ENTSO-E,pendiente,build,Sonnet,S,~2 %,,"Tras recibir el token de ENTSO-E como secreto, añade las zonas ES/FR/DE/IT/PT a leer_electricidad() sin mostrar el token",,Token gratuito ENTSO-E (Joel),manual,"Joel debe registrarse y crear el secreto en GitHub; no pegarlo en chat"
C112,C,Nivel C · Alimentos: FAO + soja/trigo/maíz/arroz/azúcar (FRED y Yahoo),pendiente,build,Sonnet,M,~3 %,,"Añade leer_alimentos() a actualizar_paneles.py: FAO food_price_indices_data.csv (extrae el enlace de la página), FRED PSOYBUSDM PWHEAMTUSDM PMAIZMTUSDM PRICENPQUSDM PSUGAISAUSDM y Yahoo ZS=F ZR=F SB=F; añade TTF=F a materias; campo desde",,,,"Todo probado 200 el 4-nov; la URL FAO lleva hash sfvrsn variable"
C113,C,Nivel C · Chips: producción FRED + SOXX/TSM/ASML/MU,pendiente,build,Sonnet,S,~2 %,,"Añade leer_chips() con FRED IPG3344S y PCU334413334413 y Yahoo SOXX TSM ASML MU en paneles.json › chips; marca nivel S en Yahoo; sin recomendaciones",,,,"RAM/DRAM real = manual (C117)"
C114,C,Nivel B · Subvenciones BDNS y contratos PLACSP: conteos diarios,pendiente,build,Sonnet,M,~3 %,,"Lee la API BDNS (convocatorias) y agrega por nivel y día; para PLACSP solo cuenta entradas del feed sin guardarlo (13 MB); salida a espana-pagos.json",,,,"BDNS 200 JSON; PLACSP 200 pero pesado; no ampliar a datos personales"
C115,C,Nivel B · Muertes y delitos comparables (Eurostat tran_sf_roadus y crim_off_cat) con notas de definición,pendiente,build,Sonnet,M,~3 %,,"Descarga tran_sf_roadus y crim_off_cat para ES/FR/DE/IT/PT y guarda serie anual con nota de definición por país",,,,"Probados 200 el 4-nov; no comparar sin nota"
C116,C,Nivel B · Mortalidad (INE tabla 6552) y exceso de mortalidad,pendiente,build,Sonnet,M,~3 %,,"Lee defunciones INE vía Tempus (tabla 6552, sin MoMo completo de 724 MB) y propón cómo mostrar exceso de mortalidad sin descargar ese CSV",,,,"MoMo CSV pesa ~724 MB; usar INE o EuroMOMO"
C117,C,Nivel C · RAM/DRAM y centros de datos: ficha manual con fuentes [S] y proxy MU,pendiente,research,Sonnet,M,~4 %,,"Busca solo fuentes públicas sobre precios DRAM/NAND y consumo eléctrico de centros de datos (IEA, EIA, comunicados); guarda en explorador/chips-manual.json con nivel S y fecha; marca [ESPECULACIÓN] en ciclos",,Decidir si se paga TrendForce (Joel),manual,"EIA exige clave; capacidad e inversión = empresas [S]"
C118,C,Nivel C · Fertilizantes y agua por zonas: Pink Sheet BM e INE,pendiente,research,Sonnet,M,~4 %,,"Con OK de Joel para descargar el xlsx del Pink Sheet del Banco Mundial, extrae urea/amoníaco/potasa/DAP; busca precio del agua por CCAA en INE/AEAS y marca [VERIFICAR] lo no oficial",,OK de descarga xlsx (Joel),manual,"En FRED las series de urea/potasa/DAP dan 404"
C119,C,Nivel A · Rellenar población, energía y balanza (Banco Mundial/Eurostat) para los 12 países,pendiente,build,Sonnet,M,~3 %,,"Amplía indicadores de paneles.json con población, consumo eléctrico per cápita (EG.USE.ELEC.KH.PC), balanza corriente y gasto defensa con Banco Mundial v2; mismos 12 países",,,,"Banco Mundial 200 el 4-nov"
C120,C,Nivel B · Fichas manuales: Interior (criminalidad), DGT, siniestralidad laboral e incendios EFFIS,pendiente,research,Sonnet,M,~4 %,,"Con Chrome, comprueba y documenta en research/ACCESOS-CHROME.md las fuentes de Interior, DGT, Trabajo y EFFIS; no saltes anti-bots; guarda lo verificado en espana-manual.json",,Chrome (Joel),manual,"Interior ficha da 403 a curl; EFFIS y Trabajo no probados"
```
