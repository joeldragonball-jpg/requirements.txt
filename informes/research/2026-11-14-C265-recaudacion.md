# C265 · España › Recaudación (14-nov-2026)

**Resultado:** nuevo `explorador/espana-recaudacion.json` (lo genera `scripts/espana_recaudacion.py`; las cifras de la AEAT van escritas en el script con la comprobación de que las figuras suman el total) y pestaña «Recaudación» en la vista España de la Órbita (7 bloques: gráfico de barras apiladas, año a año, 2026 frente a 2025, directos/indirectos y Estado/AA.TT., Impuestos Especiales, medidas y devoluciones, PIB y Eurostat, lecturas).

## Fuente y método
- Tablas (no prensa) de los «Informes mensuales de recaudación tributaria» de la AEAT, descargados el 14-nov-2026 a una carpeta temporal fuera del repo y leídos con `pdftotext -raw`: diciembre de 2020, 2021, 2022, 2023, 2024 y 2025, y septiembre de 2026 (cuadros 0, 1.1, 1.2, 2.1 y 3.1). Nivel P. URL de cada PDF en el JSON.
- Criterio: caja, neto de devoluciones, M€ corrientes. Eurostat (devengo) solo para % del PIB y cotizaciones (copiado de `espana.json`).

## Cifras clave (M€, AEAT, nivel P)
| Año | Total neto | Variación |
|---|---|---|
| 2019 | 212.808 | — |
| 2020 | 194.051 | −8,8 % |
| 2021 | 223.385 | +15,1 % |
| 2022 | 255.463 | +14,4 % |
| 2023 | 271.935 | +6,4 % |
| 2024 | 294.734 | +8,4 % |
| 2025 | 325.356 | +10,4 % |
| ene-sep 2026 | 248.326 | +10,0 % (+8,0 % homogéneo) frente a 225.747 |

- 2025: IRPF 142.466 · IVA 99.532 · Sociedades 42.266 · Especiales 23.083 · Resto 18.009. Devoluciones 76.856 (brutos 402.212, cálculo propio).
- Ene-sep 2026: IRPF 118.068 (+12,5 %) · Sociedades 18.877 (+25,8 %; +7,0 % homogéneo) · IVA 81.181 (+8,1 %) · Especiales 15.718 (−8,5 %). Medidas de 2026 (ene-sep): −3.983 M€; en 2025: +7.820 M€ (AEAT, cuadro 0).
- % del PIB (AEAT ÷ PIB corriente de Eurostat, cálculo propio): 17,0 % (2019) → 19,3 % (2025). Presión fiscal Eurostat (impuestos + cotizaciones): 37,6 % en 2025.
- Las tasas que salen en el JSON coinciden con las publicadas por la AEAT (6,4 / 8,4 / 10,4 / 10,0 / 8,0). En Especiales por producto, las variaciones salen con importes redondeados y pueden diferir 0,1-0,2 puntos.

## Pendiente [VERIFICAR]
- Grandes empresas: el informe mensual no las desglosa.
- Comunidades autónomas y entes locales por separado (el cuadro 1.3 sí lo separa por mes; no volcado). Hoy solo «AA.TT.».
- Cotizaciones sociales: solo el dato anual de Eurostat; la serie mensual de la Seguridad Social/IGAE queda sin leer.
- Diferencia exacta AEAT frente a Eurostat por partida (tributos propios de CCAA y ayuntamientos, criterio de devengo): descrita, no cuantificada.

## Lecciones (máx. 5 líneas)
1. `pdftotext -raw` da las tablas de la AEAT limpias; con `-layout` salen desordenadas (columnas mezcladas).
2. El cuadro 1.2 de cada informe de diciembre trae el año y el anterior por figura: 2019-2025 salen de 6 PDF (2019 solo en el de diciembre de 2020).
3. `python -I` falla en este PC («No module named encodings»): usar `python` normal en los scripts propios.
4. Las filas de `espana-manual.json` ya tenían el total de 2025 y ene-sep 2026: `revisar_explorador.py` las cruza con el JSON nuevo.
5. `espana.json` no se ha regenerado: no se tocó `espana-manual.json`; el JSON nuevo se lee aparte (`D.espana_recaudacion`).
