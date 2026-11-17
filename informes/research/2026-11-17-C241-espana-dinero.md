# C241 · «A dónde va el dinero» — cierre parcial 17-nov-2026

> Repo público. Hechos con fuente oficial y nivel; lo no leído, [VERIFICAR]. Sin recomendaciones. Importes: M€ = millones de euros, mil M€ = miles de millones.

## Qué se cerró hoy
- **Encargos a medios propios** (el hueco que dejó el 12-nov): `scripts/leer_encargos.py` (sin IA, sin claves) lee `EMP_SectorPublico_2026.zip` de PLACSP (sindicacion_1383, Hacienda; Last-Modified 17-nov-2026 05:00 GMT, ≈1,9 MB, 8 ficheros ATOM) [P, feed oficial leído por script].
  Resultado volcado en `explorador/espana-contratacion.json` → `encargos_medios_propios` (EUR, escala 1): 3.093 entradas únicas, 15 anuladas, **3.078 encargos, 5.420,6 M€ (≈5,4 mil M€)**, todos en estado PUB.
  - Por medio propio: Tragsa 678 encargos / 2.086,8 M€; Tragsatec 763 / 641,9 M€; FNMT-RCM 47 / 567,9 M€; Ineco 188 / 375,4 M€; Gerencia de Servicios para la Salud y Seguridad en Canarias 12 / 314,3 M€; LogiRail 65 / 235,2 M€; Isdefe 67 / 147,1 M€.
  - Por nivel: AGE 839 / 2.549,6 M€; otras entidades del sector público 703 / 1.313,0 M€; CCAA 756 / 1.148,7 M€; entidades locales 780 / 409,4 M€.
  - Mayor encargo: Policía Nacional (División Económica y Técnica) → FNMT-RCM, 481,7 M€, adjudicado 26-sep-2025 (id PLACSP 18866811).
- Vista: el bloque cuelga de la capa «Dónde va el dinero» existente; la sesión principal debe regenerar `construir_*` (no lo he hecho).

## Límites honestos
1. El ZIP anual contiene entradas cuya **última actualización** cae en 2026; la fecha de adjudicación va de 2018 a 2026 (2.264 encargos de 2026 = 3.181,5 M€; 602 de 2025 = 1.476,7 M€). **No es el gasto de un año.** Hay 2 fechas absurdas en origen (años «0024» y «0026») sin corregir.
2. Pares con mismo importe y fecha (2 × 215,8 M€ Tragsa, 5-jun-2026; 2 × 98,05 M€ Canarias, 29-dic-2025): ¿duplicado de publicación o encargos distintos? [VERIFICAR] contra la ficha del expediente.
3. Un encargo a medio propio no se licita (art. 32 LCSP); que Tragsa concentre encargos **no implica irregularidad**. Importe = presupuesto del encargo, no pago.
4. Cotejo con la página oficial de cada expediente no hecho (solo feed); las cifras de los 10 mayores quedan [VERIFICAR] hasta abrir la ficha en Chrome.

## Sigue pendiente de C241
- Tamaños exactos de los ZIP mensual/anual: el servidor no envía Content-Length y HEAD/Range fallan; el mensual oct-2026 ≈194 MB (leído el 10-nov); anual 2025 no medido (descarga de >2 min, abortada).
- BDNS: sigue sin volcado masivo localizado; no probé `/bdnstrans/GE/es/descargas` en Chrome. `espana-subvenciones.json` queda en la ventana 11-sep→9-nov (no refrescado hoy).
- PLACSP de noviembre: mes sin cerrar; reejecutar `leer_contratacion.py` tras el 1-dic.
- Menores: URL vigente no reconfirmada.

## Lecciones
1. El ZIP anual de encargos pesa poco (≈1,9 MB) y se lee en segundos; el agregado mensual de licitaciones es lo caro.
2. Año del ZIP ≠ año del gasto: agrupar siempre por fecha de adjudicación.
3. Pares idénticos en un feed ATOM: sospechar duplicado antes de sumar como hecho.
