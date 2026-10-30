# C65 · España: cuánto se ingresa, en qué se gasta y qué resultados da (pedido de Joel, 30-oct-2026)

Objetivo: contrastar con datos oficiales la idea «máximos históricos de recaudación y servicios públicos que empeoran». No se parte de la conclusión: se muestran ingresos, gasto y resultados y se dice qué confirman y qué no. Caso alcista/bajista de cada lectura, sesgo de la fuente, [P]/[S]/[VERIFICAR]/[ESPECULACIÓN].

## Ya hecho (fase 1, 30-oct)
`python scripts/espana_fiscal.py` → `explorador/espana.json` (Eurostat, 24 series 2014-2025: ingresos, impuestos por tipo, gasto por funciones COFOG, inversión pública, intereses, ayuda exterior COFOG 01.2; % PIB y euros reales por habitante). Lo no abierto va a `explorador/espana-manual.json`.

## Fase 2 · datos que faltan (leer de la fuente oficial, sin memoria)
1. **Recaudación de Hacienda (AEAT):** Informe anual de recaudación tributaria y mensual (sede.agenciatributaria.gob.es): IRPF, IVA, sociedades, IIEE, por año 2019-2025 y lo que va de 2026; devoluciones; fraude descubierto. Comparar con Eurostat (criterio distinto: caja vs devengo).
2. **Paro:** gasto en prestaciones y subsidios (SEPE, estadísticas de prestaciones; Seguridad Social), nº de beneficiarios, tasa de cobertura, cuantía media; Eurostat GF1005 ya está.
3. **Dinero que sale al exterior y cuánto vuelve:** ayuda oficial al desarrollo (OCDE-CAD y Seguimiento del PACI, Ministerio de Asuntos Exteriores): AOD neta, % de la renta nacional; créditos reembolsables (FONPRODE, antiguo FAD) y devoluciones; **préstamo bilateral a Grecia** (importe, intereses cobrados, devoluciones; Banco de España / Ministerio de Economía); **MEDE/ESM** (capital aportado y desembolsado); aportación al presupuesto de la UE y saldo neto (Comisión Europea, «EU spending and revenue»); contribuciones a organismos (FMI, Banco Mundial). Distinguir donación, préstamo y garantía.
4. **Rescate bancario:** ayudas del FROB, importe recuperado y pérdida estimada (Banco de España, informe del FROB); coste fiscal.
5. **Resultados de los servicios (la mitad del contraste):** listas de espera del SNS (Ministerio de Sanidad), médicos y camas (ya en estabilidad.json), abandono escolar temprano y PISA (Eurostat edat_lfse_14; OCDE), vivienda: esfuerzo de acceso y obra nueva (INE, Ministerio de Vivienda), puntualidad y estado de infraestructuras (Renfe/ADIF, Tribunal de Cuentas), justicia (CGPJ: pendientes). Cada indicador con serie 2019-último año.
6. **Ajustes para no engañar:** envejecimiento (gasto por habitante no corrige por edad), inflación sectorial (sanidad y educación suben más que el deflactor del PIB), fondos europeos NextGen (inflan «asuntos económicos» e inversión 2021-2025), reparto estado/comunidades (la sanidad y educación las gestionan las CCAA).

## Fase 3 · mostrarlo
Capa «España» en el Panel informativo (vistas.html) y tarjeta en la pestaña Datos del móvil: serie 2014-último, % PIB, euros reales por habitante, colores frente al dato anterior; una lectura de 3 líneas por bloque ([OPINIÓN]).

## Reglas
Cifras publicadas con fuente y fecha; sin recomendaciones; no inventar; si una fuente no responde, [VERIFICAR]. Informe en `informes/research/AAAA-MM-DD-C65-espana-ingresos-gasto.md`. Regenerar con `python scripts/espana_fiscal.py`, `construir_movil.py` y `construir_seguimiento.py`. Parar al 70 % de contexto.
