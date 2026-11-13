---
tema: Coherencia entre informes y datos: los «dudosos» de XRP, XLM y España revisados uno a uno (C237, cuarta pasada)
etiquetas: [coherencia, xrp, xlm, españa, evernorth, fichas, cobertura, fiscalidad]
actualizado: 2026-11-13
---
# C237 · Cuarta pasada: los 50 dudosos, uno a uno

Local, sin IA. Medido con `python scripts/cobertura_hechos.py` (13-nov-2026) y revisado buscando el identificador de cada hecho (cifra exacta, número de ledger, nombre propio) en `explorador/*.json`. Lo que se volcó se releyó antes en su fuente primaria cuando era posible.

## Medición y resultado
| Ámbito | Dudosos | Ya estaban | Superados (estado intermedio) | Faltaban de verdad |
|---|---|---|---|---|
| XRP | 21 | 13 | 4 | 4 |
| XLM | 7 | 5 | 0 | 2 (uno era solo un detalle) |
| España | 22 | 16 | 0 | 6 |

De los «faltan» que quedaban (XRP 15, XLM 3, España 5): todos estaban ya o eran lecturas pasajeras del estado del nodo, salvo Verifactu y el criterio FIFO, volcados ahora.

## HECHOS volcados (nivel P, con relectura de hoy)

### XRP → `explorador/fichas-activos.json` (de 21 a 27 hechos)
- **Evernorth, discrepancia CERRADA** [SEC, 424B3 del 9-nov-2026, leído en EDGAR]: «approximately 388,910,554 XRP in kind». Desglose: 211.319.096 (patrocinador) + 126.791.458 (Ripple) + 50.000.000 (entidad vinculada) + 800.000 (inversores privados). Los ≈ 388,1 M del S-4/A de agosto son las tres primeras partidas: **388,1 y 388,9 eran la misma cuenta con y sin esos 800.000**.
- Total tras el cierre: 388.910.554 + 84.365.876 comprados = **≈ 473,28 M XRP** (suma nuestra); cuadra con los «más de 473 millones» del Form 425. Las tres cifras del repo (388,1 / 388,9 / 473) quedan conciliadas.
- Efectivo bruto del cierre: 272,6 M USD (224,6 de colocación privada + 48,0 de la cuenta fiduciaria). Notas convertibles: 30 M USD al 4 %, vencimiento 2031.
- Línea de capital con Cantor (23-oct-2026): hasta 5.218.935 acciones nuevas al 97 % del precio medio, unos 14 meses. Es dilución potencial de XRPN, no compra de XRP.
- Suministro total de XRP [ledger 108302027, 13-nov-2026 11:00 UTC]: 99.985.553.928; quemados desde el origen 14.446.072 (≈ 1.340 al día desde el 17-oct, cálculo nuestro).
- Escrow de Ripple leído en el ledger (7-nov-2026, no releído hoy): 31.100 M en 99 escrows; 1.000 M al mes de dic-2026 a jun-2029.
- Compras de Ripple en custodia: Standard Custody (cerrada 11-jun-2024) y Palisade (anunciada 3-nov-2025), sin precio.
- **Corrección de coherencia:** la ficha decía que la aprobación final de la OCC «sigue pendiente» y la Línea de tiempo la daba por concedida el 26-oct-2026. Estado real: aprobación condicional n.º 1359 confirmada en occ.gov [P]; la final solo consta por el comunicado de Ripple; el buscador de occ.gov no la lista a 13-nov-2026 [VERIFICAR].

### XLM → misma ficha (de 12 a 14 hechos)
- USDC en Stellar [Horizon, 13-nov-2026 11:02 UTC]: **351,2 M USD** (235,8 en cuentas + 112,0 en contratos + 2,4 en fondos de liquidez); 2.545.008 cuentas con línea de confianza. El 29-oct eran 342,6 M.
- Protocolo en vigor: 29 (ledger 65456342); voto del Protocolo 30 anunciado para el 23-nov-2026.
- Añadido el valor liquidativo del fideicomiso de Grayscale (15,38 USD) a su entrada.

### España
- `espana-manual.json` › `cotizaciones_y_tributos` (de 6 a 9): pensión máxima 2026 de **3.359,60 €/mes** (47.034,40 €/año; RDL 3/2026, art. 1); retención del **19 %** al reembolsar fondos con ganancia; planes de pensiones, **1.500 €/año** (+8.500 de empresa o +4.250 en planes sectoriales y de autónomos; art. 52 LIRPF).
- `espana-leyes.json` (de 23 a 24): Verifactu, antes del 1-ene-2027 (impuesto de sociedades) y del 1-jul-2027 (resto) [RD 1007/2023, disposición final cuarta en su redacción del RDL 15/2025]. El aplazamiento a 2028 sigue sin constar en el BOE [VERIFICAR].
- `regulacion.json` (celda España · fiscal): criterio FIFO y valoración de permutas, del Manual práctico de Renta 2025 de la AEAT.

## Correcciones a informes anteriores
1. El hecho «art. 97 del Reglamento del IRPF: retención del 19 %» citaba mal el artículo: el 97 define la **base**; el tipo del 19 % está en el **art. 101.6 de la Ley**. La cifra era correcta.
2. El informe de la tercera pasada decía que el FIFO «ya está en la Matriz de regulación»: no estaba en ningún JSON de la Órbita. Ya está.

## No volcado (y por qué)
- Encuesta de préstamos bancarios del Banco de España (27-oct-2026): cualitativa, sin cifra; próxima el 2-feb-2027.
- Campaña de la renta 2025 (8-abr a 30-jun-2026): ya pasada; la de 2026 no está publicada.
- Estados intermedios de fixCleanup3_4_0 y lecturas del estado del nodo: superados por la activación del 4-nov.
- Cifra exacta de RWA en Stellar: sigue abierta [VERIFICAR] (3.550 a 3.996 M USD según la métrica).

## OPINIÓN (mía)
- Evernorth: a favor, las cifras de la SEC cuadran al XRP exacto y dan transparencia. En contra, el 82 % del XRP llegó en especie de partes vinculadas (no fue demanda nueva de mercado) y la línea con Cantor permite emitir acciones con descuento. Son hechos de la estructura; qué pese más es interpretación.

## Lecciones (máx. 5)
1. Dos cifras casi iguales de un mismo documento suelen ser la misma suma con y sin una partida pequeña: pedir el desglose antes de marcar contradicción.
2. `www.sec.gov/Archives` rechaza scripts sin identificar, pero el navegador integrado lo lee; el buscador de texto completo (`efts.sec.gov`) sí responde a scripts.
3. Al volcar un artículo de ley, releer la última versión del bloque en la API del BOE: la primera que devuelve es la redacción original.
4. `espana-leyes.json` tiene formato propio (una ley por línea): añadir la línea, no reescribir el archivo.

## Fuentes
- SEC, 424B3 de Evernorth (9-nov-2026): https://www.sec.gov/Archives/edgar/data/2092592/000162828026072223/evernorth-424b3.htm
- XRPL: https://xrplcluster.com/ (método `ledger`) · Stellar: https://horizon.stellar.org/assets?asset_code=USDC
- OCC, buscador: https://www.occ.gov/search.html
- BOE: RDL 3/2026 https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-2548 · LIRPF https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 · RD 1007/2023 https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840
- AEAT, Manual de Renta 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c11-ganancias-perdidas-patrimoniales/monedas-virtuales/compra-venta-monedas-virtuales-tributacion-inversor.html
