# Auditoría Opus (2.ª) del commit 10c089f — Cadenas 15-nov, 2.ª parte

Fecha: 15-nov-2026. Solo lectura: no se ha editado ningún archivo salvo este informe.
Alcance: `explorador/aporta-redes.json`, `interconexion.json`, `corredores-liquidez.json`, `pruebas-bancos.json`, `empresas-redes.json`, `comparativa-liquidacion.json`, `cadenas-validadores/incidentes/gobernanza.json`, celdas e hitos nuevos de `cadenas.json` y `vistas.html`.
Método: fuentes originales abiertas con WebFetch, Chrome (swift.com da 403 a WebFetch) y consultas directas a nodos públicos y APIs (curl a s1.ripple.com, api.mainnet-beta.solana.com y api.llama.fi/hacks). Leyenda: ✅ confirmado · ⚠️ confirmado con matiz o fuente mal citada · ❓ no confirmado en la fuente citada · ❌ contradicho.

## 1. Cotejo de 26 hechos con la fuente original

| # | Hecho (archivo) | Fuente abierta | Resultado |
|---|---|---|---|
| 1 | Multa civil de 125.035.150 $ a Ripple (`empresas-redes.json:22`) | SEC LR-26369 | ✅ |
| 2 | Desistimiento de los dos recursos el 7-ago-2025, recursos 24-2648 y 24-2705 (`:23`, `:25`) | SEC LR-26369 (7-ago-2025) | ✅ |
| 3 | Sentencia final del 7-ago-2024 (`:22`) | SEC LR-26369 | ❓ La release habla de la sentencia final pero no le pone fecha. La fecha es correcta según el expediente judicial, pero la URL citada no la muestra. |
| 4 | Aprobación final de la OCC a Ripple National Trust Bank, 26-oct-2026; sin depósitos ni préstamos; RLUSD lo emite SC&T (NYDFS) (`:30`, `:45`) | The Block, 26-oct-2026 | ✅ como S. El artículo no da el día exacto de la aprobación: 26-oct es la fecha de publicación. La aprobación condicional del 12-dic-2025 ✅. |
| 5 | «Primer ETF al contado de XRP en EE. UU.» (Canary XRPC, 13-nov-2025, ~58 M$ el primer día) (`:27`) | The Block | ⚠️ Fecha y volumen ✅. La fuente no dice «primero»: recuerda que REX-Osprey XRPR salió en sep-2025 (37,7 M$ el primer día), aunque con estructura distinta. Conviene matizar: «primer ETF de XRP 100 % al contado (estructura de la Ley de 1933)». |
| 6 | Hidden Road por 1.250 M$, anunciada en abr-2025 (`:53`) | privsource (8-abr-2025) | ✅ |
| 7 | Rail por 200 M$, ago-2025 (`:54`) | ripple.com/insights (4-dic-2025) | ⚠️ El importe ✅. La fecha no aparece en esa página y el nivel P es de parte interesada sin etiquetar. |
| 8 | GTreasury por 1.000 M$, 16-oct-2025 (`:55`) | ripple.com/insights | ⚠️ El importe ✅ («now-closed»). La fecha no aparece en la página citada. Mismo problema de nivel que el #7. |
| 9 | DTS de DTCC en marcha el 28-oct-2026 con Canton y Besu privada; 20 participantes (`interconexion.json:58`, `:75`) | dtcc.com, 28-oct-2026 | ✅ |
| 10 | Carta de no acción de la SEC a DTC en dic-2025 (Russell 1000, ETF de índices, Tesoro) (`interconexion.json:74`; 11-dic en `empresas-redes.json:212`) | DTCC 28-oct-2026 y sec.gov/files/tm/no-action/dtc-nal-121125.pdf | ✅ Mes y alcance confirmados. El PDF de la SEC existe con nombre fechado 12-11-25, pero no se pudo extraer su texto: el día 11 queda confirmado solo indirectamente. |
| 11 | Operaciones de «producción limitada» en Canton en jul-2026 (`interconexion.json:59`; `pruebas-bancos.json:791`) | DTCC 28-oct-2026 | ⚠️ DTCC dice «unos siete meses después» de la carta de dic-2025 y no nombra julio. Julio sale del blog de Canton (parte interesada). |
| 12 | Stellar conectado a DTS en el 1S-2027 (`interconexion.json`; `pruebas-bancos`) | dtcc.com, 27-may-2026 | ✅ |
| 13 | Solana conectado a DTS en el 2S-2027 (`interconexion.json:274`) | dtcc.com, 12-nov-2026 | ✅ |
| 14 | Agorá: informe del 27-may-2026, 7 bancos centrales y más de 40 entidades (`interconexion.json:104`) | bis.org | ✅ |
| 15 | Agorá con valor real (RVT): ~800.000 CHF, 28 participantes, 17 escenarios, 30 transacciones, 6 monedas, SIX como facilitador, jul-2026 (`:105`) | bis.org/about/bisih/topics/fmis/agora/rvt.htm | ✅ Es página del propio BIS: puede subir de S a P. Matiz: la página lista 22 entidades y 5 bancos centrales (27), no 28. |
| 16 | mBridge: ~55.500 M$ acumulados, más de 4.000 operaciones, ~95 % en e-CNY (`corredores-liquidez.json:48`, `:57`) | The Block, 17-ene-2026 (Reuters, que cita al Atlantic Council) | ✅ como S |
| 17 | Arabia Saudí «SALIÓ… el 13-may-2025 (hecho público el 20-sep-2026 por el FT)» (`corredores-liquidez.json:140`) | Cointelegraph, 21-sep-2026 (cita al FT y a SAMA) | ❌ El 13-may-2025 es la fecha en que **terminó la prueba de concepto**. La fuente no da la fecha de salida. |
| 18 | CIPS: 214 participantes directos y 1.651 indirectos (sep-2026) (`corredores-liquidez.json:601`) | cips.com.cn | ✅ |
| 19 | CCIP en el T2-2026: 4.900 M$ (+353 % interanual), más de 7.000 M$ migrados, TVS de 110.000 M$ (`interconexion.json:27`) | chain.link, 24-jul-2026 | ✅ Es parte interesada; la cifra la publica Chainlink. |
| 20 | Swift, 9-jul-2026: libro listo para uso inicial, 17 bancos «preparan» pilotos, liquidación final en los sistemas existentes (`cadenas.json:110`; `pruebas-bancos.json:1132`) | swift.com (Chrome) | ✅ La lista de 17 bancos coincide. |
| 21 | Swift, Sibos 22-oct-2026: los 17 bancos «pilotan transacciones transfronterizas en vivo» (`interconexion.json:91`) | swift.com/insights/news/four-reflections-swift-sibos-2026 | ⚠️ El hecho ✅, pero en `interconexion.json:91` la URL es la nota del 9-jul, que dice «preparan». Hay que poner la URL de Sibos. |
| 22 | MiCA, art. 143.2: plazo del 31-dic-2027 para los libros blancos de criptoactivos admitidos antes del 30-dic-2024; XDC (`cadenas.json:4800`, `:4883`) | ESMA, rulebook | ✅ |
| 23 | ETF de HBAR de Canary: CERT y 8-A12B el 27-oct-2025, 424B3 el 28-oct-2025 (`cadenas.json:1500`) | SEC EDGAR, CIK 0002039458 | ✅ |
| 24 | Comisión de XRPL: «0,005 XRP (mediana, 5.000 gotas)» ≈ 0,0048 $ (`comparativa-liquidacion.json:23-25`) | curl a s1.ripple.com, método `fee` | ❌ como comisión típica. `median_fee`=5000 es el nivel por defecto (`median_level` 128000 = 500 × referencia), no lo que se paga: `open_ledger_fee` y `base_fee` dan 10 gotas. La cifra real ronda 0,00001 $, unas 500 veces menos. |
| 25 | Solana: slot de ~0,215 s; TPS sin votos igual al TPS total (`comparativa-liquidacion.json:63-69`) | curl a getRecentPerformanceSamples | ✅ 276 slots en 60 s ≈ 0,217 s. El nodo devuelve numNonVoteTransactions = numTransactions, así que con esta fuente no se pueden separar los votos (ya marcado [VERIFICAR]). |
| 26 | Incidentes: Bitget 387 M$ (XRPL), Binance CEX 6.360 M$ (Ethereum y Avalanche), Mercado Bitcoin 40 M$ (9 redes) (`cadenas-incidentes.json`) | api.llama.fi/hacks | ✅ Las cifras coinciden con DefiLlama. ❌ en su uso: los tres tienen `targetType: "CEX"`, es decir, robos de carteras calientes de exchanges, no fallos de la red (ver §2). |

Recuento: 17 ✅ · 6 ⚠️ · 1 ❓ · 2 ❌ (los ❌ son #17 y #24; el #26 ✅ en cifras, con uso incorrecto).

## 2. Niveles, incoherencias, unidades y sesgos

**Niveles P/S/V**
- `empresas-redes.json:54-56`: Rail, GTreasury y Palisade figuran como P con fuente ripple.com, que es parte interesada. Además, las fechas no salen de esa página. Proponer «P (parte interesada)» con la fecha de una nota fechada, o pasarlos a S.
- `empresas-redes.json:46`: la licencia EMI de la FCA (ene-2026) cita un artículo de Yahoo sobre **Luxemburgo**. Fuente desajustada: usar ripple.com/ripple-press/ripple-receives-fca-permissions-… (ya citada en `corredores-liquidez.json:500`).
- `pruebas-bancos.json:575` (Banco de Inglaterra, Hedera): es P, pero la única fuente es el blog de hedera.com (parte interesada). Además entra en `conteo.hedera.entidades_P` como banco central P. Debería ser S o «P parte interesada», y salir del recuento de bancos centrales P.
- `interconexion.json:105`: el RVT de Agorá es S, pero la página es del BIS: puede subir a P (anotar 27 frente a 28).
- `interconexion.json:275`: el hecho «pruebas con valor real jul-2026» cita «BIS, 27-may-2026». Esa publicación no habla del RVT: citar rvt.htm.
- `interconexion.json:29`: el comunicado de DTCC del 12-may-2026 aparece como S y dice «La nota de Chainlink…». Es comunicado de DTCC (P) y el texto se contradice con la fuente.
- `cadenas.json:4682` (Algorand, inmuebles): es P, pero se trata de un panel de la Fundación en vercel.app con datos de terceros (DefiLlama, Yahoo). Mejor S o «P parte interesada, agregado».

**Incoherencias entre archivos o con la vista**
- `comparativa-liquidacion.json:372`: dice «pruebas-bancos.json no existía al ejecutar». Ahora existe en el mismo commit: la sección de hechos de liquidación no usa los 53 hechos de `pruebas-bancos.json` y la nota ha quedado obsoleta.
- `interconexion.json:91`: fecha del 22-oct con la URL del 9-jul (ver #21). En `swift-liquidacion.json:22` está bien.
- `vistas.html:2216-2218`: pinta la comisión con `num(x,4)`. Stellar (1,39e-6 $) sale «≈ 0,0000 USD» y XRPL «≈ 0,0048 USD», con lo que XRPL parece la más cara después de Ethereum. Tampoco muestra `comision_minima_usd`, que ya está en el JSON.
- `vistas.html:2216`: muestra el «mediano 1 s» de XRPL. Es un artefacto del redondeo de `close_time` (rippled empuja +1 s cuando colisiona), no un dato. El comentario de `scripts/leer_comparativa.py:69` («resolución de 1 s») tampoco es exacto: la resolución es de 10 s o más.

**Unidades**
- No hay errores de unidades en las cifras revisadas: Canton 374.118 M$ ≈ 374.000 millones $ según RWA.xyz [S]; Binance 6.360 M$ coincide con DefiLlama; HHI de mBridge entre 9.025 y 9.050, bien calculado.
- La comisión de XRPL sí está inflada unas 500 veces por usar el campo equivocado (#24). Hedera aparece con «finalidad medida» = intervalo entre bloques del mirror node: no es una medida de finalidad. Etiquetarlo como «intervalo de registros».

**Sesgos**
- **Incidentes (`cadenas-incidentes.json`)**: el script no filtra `targetType: CEX`. El único incidente «base» de XRPL (387 M$) es el robo a Bitget. El de XDC (40 M$) es Mercado Bitcoin. Avalanche suma 6.400 M$ por el de Binance. Los avisos (`:13`) hablan de DeFi, no de exchanges. Hay que separar «CEX con activos en la red» de «fallo de la red o de una app».
- **Error en `otras_redes`** (`scripts/leer_incidentes.py:60`): añade `ids[1:]` sin excluir la red actual. En el caso Bitget, dentro de xrpl, aparece «xrpl» en `otras_redes` y falta «ethereum».
- **Recuento de pruebas de bancos**: DBS y Franklin Templeton (`pruebas-bancos.json:19`, `:35`) son **un mismo memorando** que cuenta 2 hechos P en XRPL. Stellar y Hedera cuentan entidades P a partir de blogs de la propia red. XRPL tiene más S (4 frente a 3 P) porque varias páginas no se abrieron. La advertencia de `contraste` lo reconoce, pero la vista debería mostrarla junto al número.
- **Comparativa**: Hedera y Algorand tienen 1 punto fuerte y 1 flaco cada una, frente a 3 y 3 en el resto. Es asimetría de datos, no de mérito: avisarlo en la vista.

## 3. «Joel» o tesis personal en archivos públicos

- **Archivos nuevos o modificados por 10c089f**: no aparece ninguna mención **nueva** de «Joel», de tesis personal ni de [J]. Los recuentos son iguales antes y después del commit: `explorador/vistas.html` 3 y `docs/orbita/index.html` 8.
- Esas menciones ya existían: comentarios de código, la URL del repo con el usuario de GitHub, y textos visibles en `docs/orbita/index.html` como «Relevante para Joel (España)», «Captura leída por Joel» o «Joel puede abrirla». Conviene limpiarlas en otra tarea porque se publican.
- `interconexion.json` formula la pregunta como «hipótesis de un lector, NO se da por cierta». Es neutral y no expone la tesis.

## 4. Correcciones priorizadas (máx. 12)

1. `explorador/comparativa-liquidacion.json:23-25` y `scripts/leer_comparativa.py:86`: usar `open_ledger_fee` o `base_fee` (10 gotas) como comisión de XRPL y dejar `median_fee` como dato aparte. Hoy la comisión sale unas 500 veces más alta.
2. `scripts/leer_incidentes.py` y `explorador/cadenas-incidentes.json`: separar o excluir `targetType=CEX` (Bitget→XRPL, Binance→Ethereum/Avalanche, Mercado Bitcoin→9 redes) y añadir un aviso. Corregir `otras_redes` en la línea 60.
3. `explorador/corredores-liquidez.json:140`: cambiar a «terminó una prueba de concepto el 13-may-2025 y después dejó el proyecto (fecha de salida no publicada; FT/Cointelegraph, 20-21-sep-2026)».
4. `explorador/vistas.html:2218`: mostrar la comisión con notación significativa (p. ej. 1,4e-6 $) y la mínima. Línea 2216: ocultar o anotar el mediano de XRPL.
5. `explorador/interconexion.json:91`: cambiar la URL por la de Sibos 2026 (22-oct-2026).
6. `explorador/empresas-redes.json:27`: matizar «primer ETF» y citar el XRPR (sep-2025).
7. `explorador/empresas-redes.json:54-56`: Rail, GTreasury y Palisade como «P parte interesada», con fecha de una nota fechada. Línea 46: corregir la fuente de la FCA.
8. `explorador/pruebas-bancos.json:575`: el Banco de Inglaterra pasa a S y sale de `entidades_P` de Hedera. Líneas 19 y 35: marcar «mismo memorando» y contar 1.
9. `explorador/comparativa-liquidacion.json:372`: regenerar la sección con `pruebas-bancos.json` o quitar la nota obsoleta.
10. `explorador/interconexion.json:105` y `:275`: el RVT de Agorá pasa a P con la URL rvt.htm y la nota «27 entidades listadas frente a 28 en el texto».
11. `explorador/interconexion.json:29`: nivel P (comunicado de DTCC) y corregir «La nota de Chainlink».
12. `explorador/empresas-redes.json:22`: citar una fuente que muestre la fecha 7-ago-2024 (p. ej. LR-26080 de la SEC o el auto del SDNY); LR-26369 no la da. Aparte, en otra tarea, quitar las menciones visibles de «Joel» en `docs/orbita/index.html` (preexistentes).
