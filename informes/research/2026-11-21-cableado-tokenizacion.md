# Cableado de tokenizado, pistas, instituciones y 13F (21-nov-2026)

Solo programación: no hay datos nuevos; se pintan los cuatro JSON del día con su fecha, nivel y límites.

## Qué se ha cableado
- `explorador.py`: carga `tokenizado`, `cadenas-pistas`, `tokenizacion-instituciones` y `etf-13f` (claves `D.tokenizado`, `D.cadenas_pistas`, `D.tokenizacion_instituciones`, `D.etf_13f`).
- Órbita > Cadenas (`explorador/vistas.html`):
  - «Representado o distribuido»: ahora muestra primero la lectura del 21-nov (`brecha_rwa.lectura_actual`) con cambio a 30 d, fecha de lectura y chip «caduca en N d / caducada», la nota de trampa (representado frente a distribuido), la comprobación on-chain de BENJI y los «por qué» (Stellar +33,9 %, Franklin BENJI). La tabla del 19-nov queda debajo como histórico.
  - Nueva caja «Valor tokenizado por red» (11 redes, `leido`, `caduca`, nivel y trampa).
  - Nueva caja «Lo que dicen las voces (pistas): NO son hechos»: filtros por estado y por red, chip de estado, nivel y «sin concretar» resaltado; nota y [VERIFICAR] al abrir cada pista.
  - Nueva caja «Instituciones financieras que tokenizan»: buscador por actor o red, tarjeta por actor con iniciativas (qué, red/tecnología, fecha, estado, importe, nivel, enlace, «sin concretar»).
- Órbita > Capas (tokenización y fondos) y Paneles de datos: «Quién tiene los ETF (13F, 3T-2026)» con pestañas por activo (XRP, XLM, SOL, BTC, ETH), tabla de tenedores principales (valor, acciones 3T/2T, variación), bloque de fondos soberanos y públicos y advertencias (foto a 30-sep, sin cortos ni no-EE. UU., tipo = clasificación del analista).
- Glosario («?»): 13F ampliado, «Tokenizado» y «Sin concretar».
- Móvil (`scripts/construir_movil.py` + `docs/movil/index.html`, pestaña Datos): 4 tarjetas plegables (Tokenizado con Stellar y caducidad, Pistas con recuento por estado, Instituciones, 13F con 3 titulares y soberanos).
- `scripts/revisar_explorador.py`: JSON válido, niveles, fechas AAAA-MM-DD, `caduca` (aviso si caducada), estados de pistas, `concreta{token,red,producto}`, ids únicos, advertencias del 13F.

## Comprobaciones
- `revisar_explorador.py`: 0 avisos. `validar_ids.py`: 0 fallos.
- Navegador a 1280x800, 1000x620 y 500x800: sin errores de consola, sin desbordamiento horizontal. El móvil (500 px) sin desbordamiento; los 403 de consola son de recursos externos ya existentes.

## Notas
- El 13F de `etf-13f.json` trae 18 ETF (no 17).
- 10 pistas están como `confirmada_concreta` con algún campo «sin concretar» (p. ej. Deutsche Bank custodia, Goldman 13F): es un dato de la fuente, no se ha tocado; conviene revisarlo en el research.
- Las cifras del 21-nov son [S] (RWA.xyz, tercero comercial sin auditoría); la comprobación de BENJI en Horizon es [P], con NAV [VERIFICAR].
