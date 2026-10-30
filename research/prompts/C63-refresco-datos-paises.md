# C63 · Refresco a fondo de los datos de países (política, economía y estabilidad)

Contexto: el Panel informativo (pestañas Países y capa Política) y el móvil (Agenda → Comparar países) usan `explorador/paises.json`, `explorador/paneles.json["indicadores"]` (lector `scripts/indicadores.py`) y `explorador/estabilidad.json` (lector `scripts/estabilidad.py`). Muchas cifras son de 2022-2024 (Banco Mundial/OMS) y el IPC de la zona euro y España sigue en dic-2025.

## Qué hacer (en este orden)
1. **Auditoría de frescura** (sin IA, 5 min): script o consulta que liste, por indicador y país, la fecha del dato y los meses de retraso; marcar lo que tenga más de 12 meses (anual) o 3 meses (mensual).
2. **Buscar el dato más nuevo en la fuente oficial** de cada cifra atrasada, en este orden:
   - IPC zona euro y España: probar Eurostat `prc_hicp_manr` / `prc_hicp_mmor` (¿por qué devuelve dic-2025?), INE (IPC base 2025), BCE Data Portal; si la API falla, leer la nota de prensa de Eurostat/INE con el navegador integrado.
   - Gasto sanitario, educación, vivienda, médicos, camas: Eurostat (`hlth_sha11_hf`, `gov_10a_exp`, `ilc_lvho07a`, `hlth_rs_prs2`), OCDE Health Statistics, estadísticas nacionales (INE, Destatis, INSEE, ISTAT, CBS, GUS), WHO GHED. Anotar el año más reciente publicado.
   - Obras de vivienda e infraestructuras: Eurostat (`sts_cobp_a`), ministerios de vivienda; EE. UU.: Census (housing starts), BEA; China/India/Rusia: oficinas estadísticas (NBS, MoSPI, Rosstat) o FMI/Banco Mundial.
   - Paro, PIB, pobreza: confirmar el último mes/trimestre publicado.
3. **Noticias y anuncios recientes** (últimos 30-60 días) que cambien una cifra o un hito: presupuestos de sanidad/educación, planes de vivienda, reformas de pensiones, huelgas o crisis de servicios públicos. Una línea por hecho con fuente y fecha; los que cambien una cifra, actualizarla en el JSON con nivel [P]/[S].
4. **Escribir lo encontrado** donde corresponda: cifras nuevas en `explorador/estabilidad-manual.json` o `explorador/indicadores-manual.json` si no hay API; hitos en `explorador/estabilidad.json` (por script o a mano en el manual); NO inventar. Si una fuente no responde: [VERIFICAR].
5. Regenerar: `python scripts/actualizar_paneles.py` no (llama a APIs de bots); usar `python scripts/estabilidad.py --refrescar` y la función `leer_indicadores` como ya se hizo; luego `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`.
6. Informe en `informes/research/AAAA-MM-DD-C63-refresco-paises.md` con tabla «antes → ahora» por cifra cambiada, fuentes y lo que sigue sin dato.

## Reglas
- Solo cifras publicadas; sin índices propios ni rankings. Caso alcista/bajista solo si cambia la lectura de un país.
- Hechos con fuente y fecha; [VERIFICAR] lo no contrastado; sin recomendaciones de compra/venta.
- Comprobar la pantalla del Panel informativo (Países) y del móvil antes de dar la tarea por hecha.
- Parar al 70 % de contexto y dar relevo.
