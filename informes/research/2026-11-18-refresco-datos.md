# Refresco de datos atrasados del explorador (18-nov-2026)

Nivel de lo leído: P (fuente oficial leída por script o por curl hoy). Sin IA, sin claves, sin tocar privado/.

## Actualizado
| Fichero | Cómo | Resultado |
|---|---|---|
| seguridad-eurostat.json | `scripts/leer_seguridad_eurostat.py` (Eurostat tran_sf_roadus y crim_off_cat) | Releído 18-nov. Último año disponible sigue siendo 2024 (p. ej. homicidios 2024: ES 349, FR 882, DE 694, IT 336, PT 72); Eurostat marca actualización 5-nov-2026. El semáforo seguirá en rojo porque el dato más reciente es de 2024: no hay 2025 publicado [VERIFICAR cuando Eurostat lo suba]. |
| espana-mortalidad.json | `scripts/leer_mortalidad_ine.py` (INE EDeS, serie EDES52) | Última semana 2026-S44: 8.069 defunciones estimadas; exceso 499 vs 2015-2019 y 238 vs 5 años. Es estimación del INE, provisional, no el exceso oficial MoMo (ISCIII; su CSV de 724 MB no se descargó). |
| espana-votaciones.json | `scripts/leer_votaciones_congreso.py` (Congreso, datos abiertos) | 147 días con votación, 2.058 votaciones, 0 fallos, 0 sesiones nuevas: el último día sigue siendo 2-oct-2026 (no hay votaciones del Pleno posteriores publicadas). Solo cambia `generado`. |
| mandatos.json | Lectura por curl de portales oficiales | AE: u.ae confirma a Mohamed bin Zayed como presidente. IR: president.ir/en muestra a Pezeshkian en funciones (COP31, cumbre GECF). Solo se confirma el cargo actual; las fechas «desde» siguen en S. `leido` = 2026-11-18. El resto de países ya estaba leído el 5-17 nov; el «rojo» de frescura viene de la fecha «desde» más reciente (20-jul-2026, GB), no de falta de lectura. |

## No actualizado y motivo
- **bancos-eba.json**: la EBA declara el ejercicio de transparencia DISCONTINUADO desde junio de 2025 (página oficial leída hoy); el último corte es 30-jun-2025 y no habrá más. Datos nuevos solo en el Pillar 3 Data Hub (`edap-public.eba.europa.eu`), sin probar ni leído; requiere otro pipeline [VERIFICAR]. Semáforo rojo estructural.
- **espana-contratacion.json**: ya contiene el mes 202610 (generado 10-nov, ampliado 17-nov), el último mes completo. El ZIP 202611 existe (curl lo ve) pero el mes está a medias, así que no se cargó para no mezclar un mes parcial con el histórico. Rehacer con `python scripts/leer_contratacion.py --mes 202611` a comienzos de diciembre.
- **Sin fuente leída**: Venezuela (cargo vigente, presidencia.gob.ve no respondió), Etiopía (pmo.gov.et sin texto útil), Sudáfrica y resto de fechas «desde» marcadas S: siguen [S]/[VERIFICAR].
