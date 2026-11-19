# Auditoría de cableado: explorador/*.json → Órbita (docs/orbita) y móvil (docs/movil) — 18-nov-2026

Método (solo lectura, sin IA): se contrastó cada `explorador/*.json` con (a) las claves `D.*` que `explorador.py::_html` incrusta en `docs/orbita/index.html`, (b) las referencias de clave en `explorador/vistas.html`, (c) `docs/movil/data.json` e `index.html`, (d) `explorador/frescura.json`. `python scripts/revisar_explorador.py` => «0 avisos en 13 capas y 322 movimientos» (radar: 10 celdas sin dato; pendientes C327: 6 [VERIFICAR fecha], 775 fuentes sin URL, 17 nivel R). Nivel de este informe: [P] para los recuentos (script), [S] para las valoraciones de esfuerzo.

Nota de método: la Órbita incrusta los datos en una sola página, así que «sin vista» se mide por clave interna (p. ej. `D.etf_flujos`), no por nombre de fichero. Las claves marcadas «sin referencia» son nombres que no aparecen en vistas.html; algunas son claves dinámicas (siglas de grupo, categorías) y no son un fallo.

## 1. Estado general

- Órbita: `docs/orbita/index.html` (21:41) lleva la misma vistas.html que `explorador/vistas.html`, pero hay JSON más nuevos que la página: cadenas, escenarios-redes, espana-empleados, fichas-activos, frescura, precios_r00, precios_vivos. Hay que regenerar (`python scripts/construir_orbita.py`).
- Móvil: `docs/movil/data.json` (22:10) también es anterior a cadenas, escenarios-redes, espana-empleados, fichas-activos, frescura. Regenerar con `python scripts/construir_movil.py`.
- No hay ningún JSON «principal» completamente huérfano en la Órbita; los huérfanos son entradas manuales/auxiliares (sección 2). El hueco real está en el móvil.

## 2. JSON sin vista directa

| JSON | Órbita | Móvil | Comentario |
|---|---|---|---|
| chips-manual.json | No (ningún script ni vista lo lee) | No | Huérfano. Posiblemente ya volcado a `paneles.chips` a mano; confirmar o retirar. 18 días (amarillo). |
| edgar.json | No como D.* | No | Lo consume `leer_etf_flujos.py`/vigilante; solo llega a la vista como `etf_flujos`. Indirecto. |
| noticias-archivo.json | No | No | Va a la línea de tiempo vía `noticias_a_orbita.py`. Indirecto. |
| espana-manual.json | No como D.* | No | Alimenta `espana.json` (manual) y `espana_fiscal.py`. Indirecto. |
| bonos-manual, tipos-manual, estabilidad-manual, indicadores-historia-manual/-fmi | No | No | Entradas de scripts que escriben paneles.json / estabilidad.json / indicadores-historia.json. Correcto, pero indicadores-historia-manual lleva 322 días «rojo». |
| cadenas-token.json, rendimientos-defillama.json | No como D.* | No | Alimentan cadenas.json (captura, rendimientos). Comprobar que los campos nuevos llegan: vistas cita «captura» (8) y «rendimientos» (2). |
| cadenas-validadores-historial.jsonl, profundidad-historial.jsonl | No | No | Históricos de apoyo (jsonl). Sin gráfica de evolución. |
| calendario-oficial-bls.ics | No | No | El calendario oficial se pinta; el .ics no se ofrece para descargar (Órbita sí tiene .ics propio). |
| precios_vivos.json | Vivo (fetch) | Parcial | Correcto. |
| centro.json, enlaces.json | enlaces sí; centro no | centro sí | Centro solo móvil. |

## 3. Campos nuevos sin pintar (en la Órbita)

| Origen | Campos en el JSON sin referencia en vistas.html |
|---|---|
| etf-flujos.json | `13f_3T` (declarantes 3T, top10, valor declarado, nuevos vs 2T), `trackers_contraste`, `lecturas_edgar`, `completitud`, `serie_btc`/`ibit_fbtc_13nov`; `bloques_no_hechos.*` solo salen como texto en `metodo`. Es el hueco más claro: la 13F del 3T no se ve. |
| espana-contratacion.json | `encargos_medios_propios`/`mayores_encargos`, `historico_meses`, `c241_segunda_2026-11-17`, acuerdos marco múltiples, `n_anuladas`, `limites`. |
| espana-subvenciones.json | `mayores_concesiones`, `grandes_beneficiarios`, `partidos_politicos`, `recuento_semanal_concesiones…`, `concesiones_importe_negativo`, `c241_segunda_2026-11-17`, `limites`. |
| espana-presupuesto.json | `cierre_definitivo`, `cierre_2024/2025(_detalle)`, `cierre_18nov`, `comparativa_2024_2025`, `cuenta_age_2023/24/25`, `por_administracion_2024`, `credito_inicial/definitivo`, `agosto_2026`. Solo `deflactor_ipc…` y `capitulos_por_ministerio` constan. Hay mucha carga nueva del 18-nov sin pintar. |
| espana-recaudacion.json | `acumulado_2025`, `aeat_2025`, `eurostat_devengo`, `impuestos_con_cotizaciones`, variaciones `*_var_pct`, `*_devol`, `homogeneos`. |
| espana-empleados.json | `adscritos`, `eventuales`, `funcionarios_*`, `laborales_*`, `personal_senado…`, `limites`, `intento_C245`, `total_ministerios_rotulo`. |
| espana-empresas.json | `deuda_miles_eur`, `ebitda`, `corto_plazo_entidades_credito`, `largo_plazo`, `fecha_fuente`. |
| espana-judicial.json | `audiencia_nacional`, `supremo`, `pieza_separada`, `por_abrir`, `palabras_clave`. |
| espana-mortalidad.json | `media_2015_2019`, `media_5_anios_previos`, `referencias`. |
| espana-leyes.json | `nota_publicacion`, `vinculo_tema`. |
| espana-investigaciones.json (vía espana_cifras) | `caso_id`, `estado_17_nov`, `pct_bde`, `remite_a`. |
| interconexion.json | `tarea`, `nota_tipo` (menores). El resto sí se pinta. |
| estabilidad.json, fertilizantes-agua.json | Todas las claves tienen referencia: bien pintados. |
| mica-registro, mandatos, pruebas-bancos, cadenas-onchain, eeuu-fiscal | Solo claves dinámicas (países, siglas) o menores (`hora_servidor`, `reserva_base_xrp`, `P_realizada`, `sin_cadena_publica`). Bajo riesgo. |

## 4. Móvil: lo que no llega

`docs/movil/data.json` solo tiene tarjeta de España (`datos.espana`: macro, pensiones, vivienda, energía, presupuesto, pagos, mortalidad, leyes, seguridad). No hay nada de:

- cadenas.json y los 8 JSON de Cadenas (cadenas-*, escenarios-redes, aporta-redes, empresas-redes, pruebas-bancos, comparativa-liquidacion, swift-liquidacion, corredores-liquidez, pais-corredores, profundidad-multidivisa, interconexion).
- etf-flujos.json (el «etf» del móvil es regulación y la lista de ETF indexados, no flujos).
- fertilizantes-agua.json.
- espana-contratacion, subvenciones, votaciones, politica, empresas, empleados, judicial, investigaciones, recaudacion (solo si `datos.espana` lo recoge: no hay claves de recaudación en el índice móvil), mandatos, mica-registro, eeuu-fiscal, ocde-bis, conflictos-gdelt, ley-eeuu, bancos-eba.
- Decisión recogida en memoria: la Órbita es para PC y el móvil es seguimiento, así que no todo debe ir al móvil; pero fertilizantes/agua, ETF flujos y un resumen de Cadenas sí encajan en una tarjeta.

## 5. Cifras sin unidad/escala explícita (C240)

- `espana_cifras`: 0 filas numéricas con unidad vacía (bien). Hay una unidad en blanco y escalas mezcladas entre filas del mismo bloque: «personas», «miles de personas» y «millones de personas»; «M€», «€/mes», «€/año». Lo ve el usuario con la unidad, pero no es comparable de un vistazo.
- `ocde_bis.paises.ES.indicadores.*` (tipo_oficial, brecha_credito, vivienda_real): 47 valores numéricos sin `unidad` propia; `conflictos_gdelt.temas.*.picos` (84) sin unidad (son z-score/picos); `profundidad_multidivisa…pagos_por_dia_estimados` sin unidad.
- `espana-contratacion` y `subvenciones`: importes en euros crudos (escala 1); la vista debe pasar a M€/mil M€. Hay 7 usos de `1e6/1000000` en vistas.html, pero campos como `importe_muestra`, `importe_total`, `credito_inicial/definitivo` no tienen referencia pintada, así que su unidad no se ha comprobado en pantalla.
- `espana-empleados`, `etf-flujos`, `interconexion`, `estabilidad`, `mandatos`, `reservas`, `deuda-fmi` no declaran `unidad` a nivel de fichero. En etf-flujos conviven `valor_usd`, `valor_usd_miles` y `valor_declarado_usd_miles`: mezcla de USD y miles de USD en el mismo fichero.
- `espana-presupuesto` y `espana-recaudacion` declaran «M€ corrientes» solo a nivel de fichero; secciones con euros crudos (`credito_inicial`) deben rotularse.

## 6. «null» visible al usuario

- La vista pinta los valores nulos como «—» (`num()` y las tablas): no se ve «null» en celdas.
- Sí se ve la palabra «null» dentro de textos de nota, en lenguaje de desarrollador: espana_cifras (macro, energía, vivienda x23 filas, pensiones, investigaciones), espana_presupuesto `sepe_2024_mensual.no_incluido`, espana_empleados (limites + 5 secciones), paises_fichas.nota, estabilidad.nota, paneles.indicadores (paro_juvenil), escenarios_redes.huecos, cadenas_onchain.aviso, etf_flujos.metodo y `bloques_no_hechos` (3), calendario_oficial.aviso, pais_corredores.aviso, empresas_redes.metodo, corredores_liquidez (5 notas «null: no hay volumen ni cuotas»), novedades (5). Total 25 grupos de texto. Solución: sustituir «null» por «sin dato» al incrustar (un reemplazo en `explorador.py` o en `espana_cifras`).
- Texto técnico filtrado: `paneles.tipos_bis.fallos[]` muestra «ValueError: sin dato (NaN)».
- Filas con `valor` nulo (se pintan «—» pero ocupan sitio): espana.manual (27), espana_cifras (8), paneles.indicadores (6), estabilidad (6), espana_presupuesto (11), corredores_liquidez.cuota_moneda (5), profundidad_multidivisa (1). Radar regulatorio: 10 celdas sin dato.

## 7. Frescura (frescura.json, generado 18-nov): 44 verde, 16 amarillo, 13 rojo, 7 gris

Más de 30 días (rojo):

| Archivo | Fecha del dato | Días |
|---|---|---|
| seguridad-eurostat.json | 2024-12-31 | 687 |
| bancos-eba.json | 2025-06-30 | 506 |
| espana.json, espana-manual, espana-presupuesto, espana-recaudacion, espana-vivienda, espana-energia, indicadores-historia-manual | 2025-12-31 | 322 |
| espana-contratacion.json | 2026-06-05 | 166 |
| mandatos.json | 2026-07-20 | 121 |
| espana-mortalidad.json | 2026-09-30 | 49 |
| espana-votaciones.json | 2026-10-02 | 47 |

Aviso: los rojos de 322 días (presupuesto, recaudación, vivienda, energía, espana.json) son muy probablemente falsos: la «fecha del dato» se toma de la última fecha de periodo y cae en el cierre de 2025 aunque el fichero se actualizó el 17/18-nov. Hay que revisar cómo `frescura_explorador.py` elige la fecha (debería usar `leido`/`generado`). Sin esa corrección el semáforo de España engaña. Los 16 amarillos son de 10 a 28 días y los 7 grises no tienen fecha (cadenas-validadores, centro, enlaces, espana-empleados, indicadores-historia-fmi, pais-corredores, prueba-datos).

## 8. Tabla priorizada

| # | Qué falta | Dónde | Esfuerzo |
|---|---|---|---|
| 1 | Regenerar Órbita y móvil (JSON más nuevos que ambos) | `construir_orbita.py`, `construir_movil.py` | S |
| 2 | Reemplazar «null» por «sin dato» en notas/avisos (25 grupos) y limpiar «ValueError (NaN)» | `explorador.py` al incrustar, `espana_cifras.py` | S |
| 3 | Corregir fecha de dato en frescura (rojos falsos de España a 322 días) | `scripts/frescura_explorador.py` | S |
| 4 | Pintar 13F 3T, trackers de contraste y lecturas EDGAR de etf-flujos; unificar USD/miles | vistas.html (`pEtf`), etf-flujos.json | M |
| 5 | Pintar lo nuevo de espana-presupuesto (cierre definitivo, comparativa 2024-2025, cuenta AGE, crédito inicial/definitivo) con unidad M€ | vistas.html (España) | M |
| 6 | Contratación: encargos a medios propios, histórico mensual, acuerdos marco; Subvenciones: mayores concesiones, grandes beneficiarios, partidos | vistas.html (España) | M |
| 7 | Declarar `unidad`/`escala` en etf-flujos, espana-empleados, ocde_bis, conflictos-gdelt, interconexion, estabilidad, mandatos | JSON + vistas | M |
| 8 | Unificar escala de «personas / miles / millones» dentro de cada bloque de espana_cifras | `espana_cifras.py` | S |
| 9 | Pintar recaudación (variaciones, devoluciones, comparación homogénea), empresas (deuda, EBITDA), empleados (adscritos, eventuales, funcionarios) y judicial (AN/Supremo) | vistas.html | M |
| 10 | Móvil: tarjetas para fertilizantes y agua, flujos ETF y resumen de Cadenas | `construir_movil.py`, index.html | M |
| 11 | Móvil: España ampliada (contratación, subvenciones, votaciones, política) | `construir_movil.py` | L |
| 12 | Decidir qué hacer con chips-manual.json (huérfano) y con bancos-eba.json (506 días) | JSON / scripts | S |
| 13 | Ocultar o rotular las filas con valor nulo (espana.manual 27, presupuesto 11, cuota_moneda 5) para ahorrar espacio | vistas.html | S |
| 14 | Mortalidad: pintar medias de referencia; leyes: `vinculo_tema`; investigaciones: `estado_17_nov`, `pct_bde` | vistas.html | S |
