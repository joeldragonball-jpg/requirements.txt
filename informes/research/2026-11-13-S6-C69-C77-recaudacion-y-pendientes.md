---
tema: España 2024 frente a 2025: recaudación por impuesto y estado de lo pendiente (S6 = C69 + C77)
etiquetas: [españa, aeat, recaudacion, eurostat, cofog, igae, presupuesto]
actualizado: 2026-11-13
---
# S6 · C69 + C77: se cierra la recaudación por impuesto; el resto necesita descargas

Lecturas del 12-nov-2026. M€ = millones de euros. Datos en `explorador/espana-manual.json` (bloque `recaudacion_aeat`) y, regenerado, `explorador/espana.json`.

## HECHOS

### Recaudación de la Agencia Tributaria por impuesto [P, capítulos 2 a 5 de los informes anuales 2024 y 2025]
| Impuesto | 2024 | 2025 | Variación |
|---|---|---|---|
| IRPF | 129.408 M€ | 142.466 M€ | +10,1 % |
| IVA | 90.541 M€ | 99.532 M€ | +9,9 % |
| Sociedades | 39.096 M€ | 42.266 M€ | +8,1 % |
| Impuestos Especiales | 22.128 M€ | 23.083 M€ | +4,3 % |
| **Total ingresos tributarios** | 294.734 M€ | 325.356 M€ | +10,4 % |

- Cierra el [VERIFICAR] de C65/C69: el IRPF de 142.466 M€ era cifra de prensa y ahora está leído en la AEAT. Criterio de caja; no coincide con Eurostat (devengo, con cotizaciones y entes locales).
- En 2024 las variaciones fueron: IRPF +7,6 %, IVA +7,9 %, Sociedades +11,5 %, Especiales +6,6 %. Hidrocarburos: 12.366 M€ en 2025 (+0,5 %).

### Gasto por funciones (COFOG) de 2025
- [P, API de Eurostat, tabla gov_10a_exp actualizada el 21-oct-2026] Para España el último año con dato es **2024**; 2025 está vacío. Último dato: protección social 297.532 M€ (18,7 % del PIB), sanidad 102.942 M€ (6,5 %), servicios públicos generales 92.551 M€ (5,8 %), asuntos económicos 80.908 M€ (5,1 %), educación 65.862 M€ (4,1 %), defensa 14.233 M€ (0,9 %).

### Hallazgo de mantenimiento
- `explorador/espana.json` no se regeneraba desde el 4-nov, así que los bloques manuales añadidos después (pensiones, demografía, energía, vivienda, recaudación) **no salían en la Órbita**. Regenerado el 13-nov con `python scripts/espana_fiscal.py`: ya se ven. Hay que ejecutarlo siempre que cambie `espana-manual.json`.

## NO HECHO (y por qué)
- **Cierre definitivo de la IGAE de 2024**, capítulos y programas de 2024 con IPC, y las 4 notas [VERIFICAR] de programas (igualdad, cooperación, defensa industrial, vivienda-ICO): requieren descargar los PDF/XLSX de la IGAE (regla de S6: descargas con OK de Joel).
- **SEPE 2024 mensual:** solo en XLSX mensuales; mismo motivo.
- **C77:** nivel contrato ya cubierto por C241 (PLACSP y BDNS); saldo fiscal de la inmigración y fallecidos de la DANA por municipio siguen sin fuente primaria nueva.

## OPINIÓN (mía)
- La recaudación crece más de un 10 % con una economía que crece mucho menos: parte es inflación y parte medidas normativas (7.820 M€ en 2025 según la propia AEAT). Leerlo como «más presión fiscal» o como «más actividad» depende de qué parte se mire; los datos dan las dos.

## Lecciones (máx. 5)
1. Los importes por impuesto están en la primera frase de cada capítulo HTML del informe anual: no hacía falta el Excel.
2. Tras tocar `espana-manual.json`, ejecutar `espana_fiscal.py` antes de `construir_orbita.py`.
3. Comprobar la API de Eurostat antes de dar por «pendiente de publicar» un año.

## Fuentes
- AEAT, informe anual 2025: https://sede.agenciatributaria.gob.es/Sede/eu_es/estadisticas/recaudacion-tributaria/informe-anual/ejercicio-2025.html
- AEAT, informe anual 2024: https://sede.agenciatributaria.gob.es/Sede/eu_es/estadisticas/recaudacion-tributaria/informe-anual/ejercicio-2024.html
- Eurostat gov_10a_exp: https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table
