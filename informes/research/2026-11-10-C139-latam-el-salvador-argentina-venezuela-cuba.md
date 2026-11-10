# C139 · El Salvador, Argentina y (con cautela) Venezuela y Cuba (10-nov-2026)

Estado: **PARCIAL** (sesión cortada por cuota). Enfoque de datos, no de ideología. NO se han tocado `scripts/indicadores.py` ni `indicadores_historia.py` (pendiente). Fuentes: prensa que cita organismos; no se leyeron los documentos primarios → [VERIFICAR] en origen.

## El Salvador (Bukele, desde jun-2019)
- **FMI:** acuerdo EFF de 40 meses. Acuerdo a nivel técnico de las revisiones 2.ª y 3.ª combinadas publicado el **3-sep-2026**; desembolso aprobado por el Directorio el **1-oct-2026** de ~138-140 M USD (Cointelegraph/Crypto Briefing; [VERIFICAR] en imf.org). Previsión de PIB real 2026: **4,5 %** (FMI, vía prensa). Última Artículo IV localizada: [jun-2025, 1.ª revisión EFF](https://www.imf.org/en/news/articles/2025/06/27/imf-concludes-2025-article-iv-consultation-and-first-review-under-the-eff-for-el-salvador). [P]
- **Bitcoin:** el FMI afirma que desde la 1.ª revisión no se han usado fondos públicos para acumular BTC; la acumulación documentada refleja donaciones privadas (The Block / Cointelegraph, 4-sep-2026). Se concedió una exención (waiver) por incumplir un criterio de desempeño ligado a Bitcoin. La Oficina Nacional del Bitcoin dice haber "comprado" BTC y su rastreador marca ~**7.764 BTC** → **versiones contradictorias [S]**. Chivo: el FMI pide desvincular al sector público. Curso legal de BTC: 2021 (ley), alcance limitado después en el marco del programa [VERIFICAR fecha y alcance].
- Sesgos: prensa cripto con interés en el titular; PIB y seguridad oficiales con poca verificación independiente [S].
- Pendiente: BM (PIB per cápita, inflación, desempleo), deuda y déficit FMI, hito Bitcoin 2021, mandatos previos (Saca, Funes, Sánchez Cerén).

## Argentina (Milei, desde 10-dic-2023)
- **Inflación INDEC:** sep-2026 **1,9 %** mensual (ago 1,7 %); acumulado 2026 **23,6 %**; interanual **33,4 %**; mayorista sep +3,2 % mensual, +29,2 % interanual. Impulso: servicios regulados, salud 2,4 %, alimentos 2 % ([Chequeado, 13-oct-2026](https://chequeado.com/nota/la-inflacion-de-septiembre-fue-del-19-y-acumula-236-en-lo-que-va-del-ano/), [Finanzas Digital](https://finanzasdigital.com/inflacion-argentina-septiembre-2026-indec-ipc-acumulada/)). [P]. Una nota con "6,2 % / 83 %" es incoherente con el resto → descartada.
- **FMI y reservas:** el FMI (29-oct-2026) insiste en acumular reservas; se discute un waiver por incumplir la meta de reservas netas (~5.000 M USD según JP Morgan citado por Perfil) [VERIFICAR]. El BCRA habría comprado ~7.500 M USD en 2026 [VERIFICAR].
- **Riesgo país:** cifras sin fecha fiable (441 pb en jul-2026; pico de 641 pb citado sin fecha) → [VERIFICAR]. Brecha oficial–blue ~3 % y CCL–mayorista ~7 % (informe de jul-2026) [VERIFICAR].
- Caso alcista: inflación interanual muy por debajo de los 3 dígitos previos, brecha cambiaria baja. Bajista: repunte mensual, reservas insuficientes según el FMI, pobreza e indigencia [VERIFICAR con INDEC].
- Pendiente: BM, deuda/déficit (FMI), mandatos previos (Macri, Fernández, Kirchner), hitos 2023-26 (devaluación dic-2023, cepo, programa FMI 2025).

## Venezuela (todo [S]/[VERIFICAR])
- Restableció relaciones con el FMI en **abr-2026** tras 7 años (Bloomberg Línea).
- FMI (act. oct-2026, vía Bloomberg Línea): inflación media 2026 **467,9 %** (abr: 387,4 %); crecimiento 2026 **5 %** (abr: 4 %). BCV: PIB 2T-2026 **+7,14 %** interanual; inflación mensual 19,9 % jul, 13,8 % jun, 8,4 % sep. Otros: PNUD +7,4 %, UCAB +6,5 %. Inflación 2025 reportada **475 %** (prensa). Rango de estimaciones muy amplio; BCV con historial de retrasos.
- CEPAL: no se localizó cifra.

## Cuba (todo [S]/[VERIFICAR])
- PIB 2025: CEPAL (abr-2026) −3,8 %; CEEC ~−5 %; Pedro Monreal estima −9,1 % a −12,5 %. 2026: CEPAL −6,5 %; el Gobierno proyectaba +1 %. Inflación: ONEI indica precios x4 entre 2021 y 2025; Pavel Vidal estima ~70 % en 2025 con mercado informal. PIB per cápita corriente, último de la región (CEPAL, Anuario 2025). Fuentes: Cubanet y Diario de Cuba (medios críticos con el Gobierno → posible sesgo), La Nación/EFE. Falta ONEI primaria.

## Lectura de «qué resultados dan esos modelos» (solo datos)
No se puede concluir causalidad: los cuatro casos tienen datos oficiales de calidad desigual y condiciones iniciales muy distintas. Solo comparable la inflación: Argentina ~33 % interanual, Venezuela >400 % (estimación FMI), Cuba sin dato oficial fiable. Cualquier extrapolación = [ESPECULACIÓN].

## Pendiente
Descargar series BM (FP.CPI.TOTL.ZG, NY.GDP.MKTP.KD.ZG) para SLV/ARG; deuda y déficit FMI WEO oct-2026; añadir SLV/ARG a indicadores*.py y tarjetas por mandato; abrir CEPAL/ONEI/BCV directamente.
