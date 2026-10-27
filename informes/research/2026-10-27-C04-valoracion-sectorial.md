# C04 · Cuadro de valoración por sector (PER, EV/EBITDA, FCF yield) — 27-oct-2026

Información para decidir tú; no es una recomendación de compra ni de venta. Los múltiplos son una foto con fecha, no un veredicto.

## 1. Qué fuente gratis sirve (prueba del 27-oct-2026)
| Fuente | Resultado | Etiqueta |
|---|---|---|
| SEC EDGAR `companyfacts` (data.sec.gov) | Con `urllib`/curl y un User-Agent genérico da **403**. Con el navegador integrado y `fetch` dentro de la página **funciona** (JSON completo, 3,4 MB por empresa). Da beneficio neto, resultado operativo, D&A, flujo operativo, capex, deuda, caja y acciones en circulación. | [P] |
| Yahoo `v8/finance/chart` (precio) | **200 sin clave**: último cierre y fecha. | [S] |
| Yahoo `v10/quoteSummary` (PER, EV/EBITDA ya hechos) | **401 sin clave/crumb**: no sirve gratis y sin pasos extra. | — |
| Múltiplos de ETF (PER ponderado) | No salen gratis por API; hay que ir a la web del emisor (VanEck, iShares, First Trust). | [VERIFICAR] |

Conclusión: la combinación viable es **fundamentales de la SEC [P] + precio de Yahoo [S]**, calculando nosotros los múltiplos.

## 2. Cuadro (precios: último cierre de Yahoo, 26-oct-2026; fundamentales: SEC EDGAR, 10-K/10-Q más recientes)
Capitalización y valor de empresa (EV) en `mil M` de dólares. TTM = últimos 12 meses (año fiscal + acumulado del trimestre actual − acumulado del año anterior). PER = capitalización / beneficio neto TTM. FCF yield = (flujo operativo − capex) / capitalización. «n/s» = no significativo (beneficio o EBITDA casi nulo o negativo); «n/d» = dato no localizado.

| Sector | Valor | Precio | Cap. | EV | PER | EV/EBITDA | FCF yield | Notas de cálculo |
|---|---|---|---|---|---|---|---|---|
| Defensa | LMT | $635,20 | $147 mil M | $161 mil M | 22,5 | 14,7 | 5,7 % | TTM a 30-sep-26 |
| Defensa | RTX | $197,48 | $266 mil M | $288 mil M | 31,7 | 18,4 | 3,6 % | TTM a 30-sep-26 |
| Defensa | NOC | $565,41 | $80 mil M | $91 mil M | 17,8 | 14,9 | 4,8 % | TTM a 30-sep-26 |
| Defensa | GD | $357,04 | $96 mil M | $101 mil M | 22,9 | 16,0 | 4,1 % | Año fiscal 2025 (sin TTM) |
| Defensa | LHX | $260,23 | $48 mil M | $58 mil M | 30,1 | 17,4 | 5,5 % | Año fiscal a 2-ene-26 (sin TTM) |
| Energía | XOM | $184,54 | $765 mil M | $802 mil M | 30,2 | 12,5 | 2,5 % | TTM a 31-mar-26 (desfasado); EBITDA aprox. |
| Energía | CVX | $232,01 | $458 mil M | $489 mil M | 22,3 | 8,8 | 5,9 % | TTM a 30-jun-26; EBITDA aprox. |
| Energía | COP | $151,37 | $182 mil M | $197 mil M | 19,6 | 7,2 | n/d | Capex no localizado; EBITDA aprox. |
| Energía | EOG | $163,68 | $86 mil M | $89 mil M | 12,5 | 6,5 | 8,4 % | TTM a 30-jun-26 |
| Ciberseguridad | PANW | $390,46 | $319 mil M | $316 mil M | n/s (1.040) | n/s (204) | 1,3 % | TTM a 31-jul-26; deuda 0 [VERIFICAR] |
| Ciberseguridad | CRWD | $261,83 | $268 mil M | $264 mil M | n/s (4.623) | n/d | 0,6 % | EBITDA no calculable |
| Ciberseguridad | FTNT | $183,33 | $135 mil M | $132 mil M | 63,4 | 50,8 | 2,4 % | TTM a 30-jun-26 |
| Ciberseguridad | ZS | $260,45 | $42 mil M | $42 mil M | n/s (pérdidas) | n/s | 2,0 % | Deuda 0 [VERIFICAR] |
| Semiconductores | NVDA | $216,00 | $5.206 mil M | $5.168 mil M | 27,0 | 25,7 | 2,4 % | TTM a 26-jul-26 |
| Semiconductores | AVGO | $329,17 | $1.571 mil M | $1.609 mil M | 41,1 | 37,0 | 2,5 % | D&A parcial → EV/EBITDA [VERIFICAR] |
| Semiconductores | AMD | $531,28 | $867 mil M | $857 mil M | n/s (134,8) | n/s (122) | 1,0 % | D&A de 2025 (parcial) |
| Semiconductores | TXN | $298,12 | $272 mil M | $279 mil M | 38,3 | 26,2 | 2,7 % | TTM a 30-sep-26 |
| Semiconductores | QCOM | $179,60 | $189 mil M | $195 mil M | 20,4 | 16,5 | 5,5 % | TTM a 30-jun-26 |

**ETF sectoriales de tu `watchlist.toml`** (CIBR ciberseguridad, SMH y SOXX semiconductores, TSM): sus múltiplos agregados **no se calcularon**: la SEC no los da y Yahoo pide crumb. [VERIFICAR] en la ficha del emisor. TSM presenta 20-F en TWD/IFRS (no comparable con este método sin más trabajo).

**Ojo con la cobertura:** tu watchlist solo contiene ETFs/valores de ciberseguridad y chips (CIBR, SMH, SOXX, TSM); **no tiene valores individuales de Defensa ni Energía**. Los valores de esos dos sectores y los individuales de ciber/chips (salvo TSM) los elegí yo como grandes representativos; no son posiciones tuyas ni sugerencias.

## 3. Sesgos de cada múltiplo
**HECHOS**
- **PER**: depende de la contabilidad (provisiones, partidas únicas, recompras que reducen acciones). En ciclos (energía) se ve «barato» en el techo de beneficios y «caro» en el suelo. Con beneficio casi nulo explota (PANW, CRWD, AMD): no es significativo.
- **EV/EBITDA**: ignora capex y por tanto castiga poco a sectores intensivos en capital (energía, semis con fábrica propia) y favorece a quien capitaliza gastos. Mi EBITDA de energía es aproximado (resultado antes de impuestos + intereses + D&A) y en software excluye la compensación en acciones, que es un coste real.
- **FCF yield**: es el más difícil de maquillar, pero oscila con el capex del ciclo y con el capital circulante (anticipos en defensa, cobros por adelantado en software). En energía bruta refleja el precio del crudo del momento.

**Específico por sector**
- Defensa: contratos plurianuales; el flujo de caja se mueve por hitos de pago del Gobierno. Pensiones y partidas únicas distorsionan el PER.
- Energía: ligada al precio del crudo y el gas; EV/EBITDA bajo (6-12) es normal en el sector, no es «descuento».
- Ciberseguridad: beneficio GAAP deprimido por remuneración en acciones; el FCF yield suele verse mejor que el PER, pero también lo infla esa remuneración.
- Semiconductores: muy cíclico; un PER bajo puede ser el pico del ciclo.

**OPINIONES / [ESPECULACIÓN]**: leer que «Defensa vale lo mismo que Energía» o que «los chips están caros/baratos» a partir de este cuadro sería sobreinterpretar; son fotos distintas de ciclos distintos.

## 4. Límites y [VERIFICAR]
- Periodos mezclados: XOM llega solo a mar-26, GD y LHX a año fiscal (sin TTM), el resto a jun-sep-26. Comparar con cuidado.
- Acciones en circulación = portada del último 10-K/10-Q (clases sumadas); no incluye diluidas ni opciones. Puede variar ±1-3 %.
- Deuda y caja: etiquetas XBRL de cada empresa, a veces de fechas distintas. Deudas «0» en PANW y ZS, caja parcial en NVDA y D&A parcial en AVGO/AMD: [VERIFICAR] antes de apoyarte en EV.
- Precio: último cierre de Yahoo [S] (26-oct-2026); no es dato oficial.
- Nada de esto contrastado contra una segunda fuente (macrotrends, informes de resultados de las empresas): [VERIFICAR] 3-5 cifras antes de citar.

## 5. Propuesta de panel
| Campo | Fuente | Frecuencia |
|---|---|---|
| Precio, fecha | Yahoo `v8 chart` (sin clave) | diaria o con cada ejecución del panel |
| Beneficio neto, EBIT, D&A, OCF, capex, deuda, caja, acciones | SEC companyfacts (script con navegador/fetch o descarga trimestral a JSON) | trimestral (tras 10-Q/10-K) |
| PER, EV/EBITDA, FCF yield, banderas de calidad (periodo, dato parcial) | calculados | al refrescar precio |
| Múltiplos de ETF | web del emisor (manual) | mensual |

**Esfuerzo**: M. Lo difícil es la etiquetas XBRL (cada empresa usa conceptos distintos, como se vio) y que la SEC bloquea scripts sin User-Agent identificado con contacto real. Opciones: (a) lista pequeña (≈20 valores) con mapeo de etiquetas fijado a mano, refresco trimestral guardado en `explorador/valoracion.json` — recomendable por coste cero de API; (b) automatizar con un User-Agent propio con tu correo (decisión tuya: tu correo iría a la SEC). Sin IA en el bucle.

## 6. Cifras y fechas
Todas las cifras: SEC EDGAR companyfacts 10-K/10-Q hasta jun-sep-2026 [P]; precios Yahoo cierre 26-oct-2026 [S]; cálculos propios.
