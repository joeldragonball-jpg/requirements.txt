# C229b · España: tres archivos en rojo de frescura (22-nov-2026)

Nivel: P donde se leyó la fuente oficial; [VERIFICAR] donde no. Sin IA ni API. Sin commit.

## Resultado

| Archivo | Antes (frescura 21-nov) | Después | Qué cambió |
|---|---|---|---|
| espana-contratacion.json | rojo, 169 d (dato 5-jun-2026) | amarillo, 22 d (31-oct-2026) | Releído el ZIP de octubre de 2026 y añadida `fecha_dato`. |
| espana-manual.json | rojo, 325 d (31-dic-2025) | amarillo, 22 d (31-oct-2026) | 13 celdas actualizadas y `ultimo_dato`. |
| espana-votaciones.json | rojo, 50 d | rojo, 51 d (2-oct-2026) | Sin días nuevos en la fuente; se deja rojo y se explica. |

Aviso sobre el semáforo: el script `frescura_explorador.py` no entiende fechas escritas como «oct-2026» ni «2T 2026», solo años enteros. Por eso `espana-manual` figuraba en 31-dic-2025 aunque ya tenía muchas cifras de oct-2026. Se añadió `ultimo_dato` (dato real más reciente del archivo); no se tocó el script.

## espana-contratacion (PLACSP, Hacienda)
- Fuente: `contrataciondelestado.es/sindicacion/sindicacion_643/...3_202610.zip` y `sindicacion_1143/contratosMenoresPerfilesContratantes_202610.zip` (publicados el 1-nov-2026; nivel P).
- Releídos con `scripts/leer_contratacion.py --mes 202610` (5 min). Cifras idénticas a la lectura del 10-nov: licitaciones 40.000 expedientes únicos, adjudicado 17.636.833.848,14 € (17,64 mil M€; n=32.962); menores 43.614 expedientes, 217.686.776,50 € (217,7 M€).
- El script borra las notas `nota_adjudicado` y `nota_posible_tope`; se restauraron a mano. Se añadió que el 40.000 exacto se reproduce al releer el ZIP: sigue sin poder usarse como total del mes [VERIFICAR].
- Existe un ZIP parcial de noviembre-2026 (modificado el 22-nov). NO se cargó: un mes incompleto no es comparable. Es el siguiente paso cuando cierre noviembre.
- Copia previa en el directorio temporal de la sesión; no hay datos personales nuevos (personas físicas siguen agregadas).

## espana-votaciones (Congreso, datos abiertos)
- Ejecutado `leer_votaciones_congreso.py` (incremental): 147 días, 2.058 votaciones, 0 sin leer. Totales sin cambios.
- Comprobado también en el navegador (`congreso.es/es/opendata/votaciones`, variable `diasVotaciones`): el último día es el 2-oct-2026 (Sesión Plenaria 203, convalidación de reales decretos-ley); el calendario termina en octubre.
- No se sabe si no hubo votaciones del Pleno entre el 3-oct y el 22-nov o si el Congreso aún no las ha cargado [VERIFICAR]. Se dejó nota en `nota_lectura_22nov`. El Senado devolvió 403 en esta lectura.

## espana-manual: antes -> después
| Celda | Antes | Después (fuente, fecha, nivel) |
|---|---|---|
| Nacimientos 2025 | 321.164 provisional (S) | 321.684 (+1,2 %), INE MNP 2025, nota 18-nov-2026, P |
| Defunciones 2025 | 446.982 provisional (S) | 444.945 (+2,0 %), mismo INE, P |
| Saldo vegetativo 2025 | −122.167 prov. | −121.237 (2024: −116.056), P |
| Esperanza de vida 2025 | 84,01 (2024) | 84,05 (hombres 81,47; mujeres 86,53), P |
| Fecundidad | 1,1 (2024) | 1,11 en 2025 (españolas 1,08; extranjeras 1,26), P |
| Saldo migratorio exterior 2025 | VERIFICAR | sigue [VERIFICAR]: no está en esa nota; falta leer la Estadística de Migraciones |
| Afiliados extranjeros | 3.038.158 (ene-2026) | 3.699.878 media oct-2026 (+19,3 %; 16,4 % de cotizantes), Inclusión 13-nov-2026, P |
| Inmigración: afiliados extranjeros | 3.635.979 sep (S) | 3.699.878 oct, P |
| IMV hogares | 862.859 (may-2026) | 911.274 oct-2026, Inclusión 10-nov-2026, P |
| IMV personas | 2.631.545 | 2.781.679, P |
| IMV cuantía media por hogar | 538,7 €/mes | 524,6 €/mes (nómina del mes > 748,2 M€), P |
| Compraventas de vivienda | 49.319 (ago-2026) | 54.548 (sep-2026; sep-2025: 63.018; −13,4 %), serie INE ETDP1826, P |

## Lo no leído o sin actualizar (con razón)
- Fondo de Reserva de la Seguridad Social (15.267 M€ a 31-mar-2026, S): no se encontró nota posterior en la web de Inclusión; el buscador DuckDuckGo pidió un captcha y no se intentó saltarlo. [VERIFICAR]
- Hipotecas sobre viviendas (INE HPT) de septiembre: aún no publicadas al consultar (la última serie es ago-2026); no se tocó.
- Préstamo a Grecia, FONPRODE, saldo UE 2024, MEDE, Adif, PNC (dic-2025), becas curso 2025-26, AOD definitiva (OCDE, dic-2026): sin fuente nueva leída; ya llevan sus [VERIFICAR] y razones. El resto de cifras anuales de 2025 (AEAT, IGAE, DGT, Interior, Poder Judicial) son el último cierre anual publicado.
- BdE deuda de las CCAA: la 3.ª entrega es el 15-dic-2026 (según la propia celda); 2T 2026 sigue vigente. La página directa de deuda de CCAA del BdE devolvió 404 (URL adivinada).

## Regeneración (orden de la memoria)
`espana_fiscal.py` (24 indicadores, 0 fallos) -> `construir_movil.py` -> `construir_seguimiento.py` -> `construir_orbita.py` -> `indice_investigacion.py`; luego `frescura_explorador.py` y `revisar_explorador.py` (0 avisos). Archivos tocados por esta tarea: espana-manual, espana-contratacion, espana-votaciones, espana.json, frescura.json y las salidas regeneradas (docs/movil, docs/orbita, índice, PLANNING). Otros cambios del árbol (cadenas, interconexion, regulacion, informes C322b y C363d) son de otras tareas simultáneas.
