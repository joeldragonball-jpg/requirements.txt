# C241 · Volcados masivos de BDNS y PLACSP — 12-nov-2026

> Comprobado solo existencia (cabeceras HTTP) y fichas oficiales; **nada descargado**. [P] ficha oficial leída / [VERIFICAR].

## PLACSP (contrataciondelestado.es/sindicacion) — SÍ hay volcado
| Conjunto | URL (patrón) | Formato | Periodicidad | Tamaño |
|---|---|---|---|---|
| Licitaciones agregadas, sin menores | `/sindicacion/sindicacion_1044/PlataformasAgregadasSinMenores_AAAAMM.zip` y `_AAAA.zip` (2016-actual); feed diario `.atom` | ATOM XML, 500 entradas/fichero | Diario; mensual (mes anterior); anual | oct-2026 ≈ 194 MB (informe C241 del 10-nov); anual no medido |
| Encargos a medios propios (Tragsa, Tragsatec…) | `/sindicacion/sindicacion_1383/EMP_SectorPublico_AAAA.zip` y `EMP_SectorPublico.atom` | ATOM | Diario; ZIP anual 2022-2026 (2022 desde 1-jul-2021) | no indicado |
| Contratos menores | existe (ZIP oct ≈ 25 MB, leído el 10-nov); URL no reconfirmada | ATOM | mensual | ≈ 25 MB |
Comprobado hoy (GET con cabeceras, 12-nov): `…1044…_202610.zip` 200 OK, modificado 1-nov; `…_2025.zip` 200 OK, 1-ene-2026; `EMP_SectorPublico_2026.zip` 200 OK, actualizado 12-nov 05:01; feeds `.atom` 200 OK 12-nov. Tamaños sin Content-Length [no medido].
**Modificaciones**: no hay conjunto aparte; cada cambio se republica como nueva entrada del mismo expediente (hay que quedarse con la última versión, como ya hace `leer_contratacion.py`) [P, ficha Hacienda].
Avisos: comentarios en datos.gob.es hablan de incidencias en 2026 (actuaciones en la plataforma el 16-oct; enlaces rotos en la ficha de perfiles de contratante) [S].

## BDNS (infosubvenciones.es) — NO localizado volcado completo
- La ficha de datos.gob.es lista CSV/XLSX/PDF, pero los enlaces apuntan al portal (export por búsqueda, tope 10.000 filas según terceros [S]) y a la API JSON (swagger). Periodicidad diaria; tamaño no indicado; licencia: aviso legal de Hacienda [P].
- Volumen citado por la IGAE: 520.000 convocatorias y 27,7 M de concesiones (nota antigua) [S].
- La página «descargas»/utilidades externas no devolvió contenido legible [VERIFICAR]; manual de «cargas masivas» de la BDNS es para entidades que suben datos, no para reutilizadores.

## Huecos
- Tamaños exactos de ZIP anual/mensual y URL vigente de menores; confirmar si BDNS ofrece volcado en `/bdnstrans/GE/es/descargas` (probar en Chrome).
- Encargos: ZIP no abierto, campos no leídos.

## Lecciones
1. PLACSP resuelve el «semana a semana»: bajar ZIP mensual/anual ATOM, no la API.
2. BDNS: seguir con ventanas por fecha; probar Chrome antes de darlo por inexistente.
3. HEAD falla en estos servidores; usar GET con `-r 0-0` y leer `Last-Modified`.
4. Modificaciones = versiones repetidas: dedupe por expediente.
