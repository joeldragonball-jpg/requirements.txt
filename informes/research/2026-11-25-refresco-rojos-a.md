# Refresco de archivos en rojo (A) - 2026-11-25

| Archivo | Qué cambió | Fuente |
|---|---|---|
| explorador/calificaciones.json | `leido` a 2026-11-25. España: tabla del Tesoro sin cambios (Moody's/S&P/Fitch sep-2025); añadida KBRA A, perspectiva positiva (6-nov-2026). Francia: AFT en mantenimiento, no releída; cifras sin tocar (próxima S&P 27-nov). Otros soberanos (IT, JP, US, CN, DE) siguen en tabla MoF 3-abr-2026 [S/VERIFICAR]; no se reconfirmaron con fuente primaria. | tesoro.es/en/deuda-publica/calificacion-crediticia; kbra.com/publications/mPbJcqWF; aft.gouv.fr (caída) |
| explorador/reservas.json | `leido` a 2026-11-25 y campo `comprobado` en COFER: sin edición nueva (la última sigue siendo la del 30-sep-2026, 2T). El resto de bloques (oro, SAFE, MoF, Fed, BCE, BoJ) NO se refrescaron. | data.imf.org/en/datasets/IMF.STA:COFER |
| explorador/swift-liquidacion.json | `leido` a 2026-11-25; nota: última edición sigue siendo oct-2026 (22-oct); aviso de Swift de corrección del SGD de sep-2026. Cifras sin tocar (los PDF no son legibles). | swift.com/products/global-currency-tracker/document-centre |
| explorador/deuda-fmi.json | `leido` a 2026-11-25 y nota de edición: WEO oct-2026 sigue vigente, sin edición posterior. | imf.org/en/publications/weo/issues/2026/10/13/world-economic-outlook-october-2026 |

Notas: la web imf.org/en/Publications/WEO dio Access Denied y WebFetch devolvió una caché antigua (jul-2026); se leyó la página de la edición en Chrome. Búsquedas web (secundarias) apuntan a acciones de nov-2026 en otros soberanos (Chipre/Fitch 6-nov, Italia/S&P afirmada, Polonia/S&P perspectiva negativa) [S, VERIFICAR]: no se volcaron.
