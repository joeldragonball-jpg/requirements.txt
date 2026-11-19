# Órbita, pasada 4 (prioridades 2, 3 y 4 de la auditoría) — 18-nov-2026

Nivel: [P] para los recuentos de scripts y la comprobación en navegador; sin IA ni API de pago.

## 2. «null» y «ValueError (NaN)» ya no salen al usuario
- `explorador/vistas.html`, función `cargar()`: bloque `sinJerga`, que recorre los datos incrustados y, solo en textos (no claves ni URLs), cambia «null» por «sin dato» y quita «ValueError: sin dato (NaN)» y similares. Cubre los ~25 grupos de la auditoría (61 textos) sin tocar los JSON ni `explorador.py`.
- Comprobado en el navegador (configuración «orbita»): 0 apariciones de «null», «ValueError» o «(NaN)» en Resumen, España, Paneles, Fichas por activo, Cadenas, Países, Voces y Noticias (antes 2, 3 y 6 en tres pestañas).
- Los JSON de origen no se han tocado (otro agente trabaja en ellos); el origen sigue diciendo «null» y la vista lo traduce.

## 3. Frescura de España
- `scripts/frescura_explorador.py`: regla «periodo cerrado + lectura reciente». Si el dato más reciente es un fin de año (hasta 400 d) o de trimestre (hasta 130 d) y el archivo se leyó hace 30 d o menos, el semáforo se juzga por la fecha de lectura; el origen sale como «periodo cerrado + lectura».
- Resultado: de 13 rojos pasan a 6; verde 50, amarillo 17, gris 7. Salen del rojo espana, espana-energia, espana-presupuesto, espana-recaudacion, espana-vivienda e indicadores-historia-manual (cierre 2025, leídos 13-18 nov), y espana-mortalidad.
- Siguen en rojo, y es correcto: seguridad-eurostat (dato 2024, 687 d), bancos-eba (2025-06-30, 506 d), espana-contratacion (2026-06-05, 166 d), mandatos (2026-07-20, 121 d), espana-votaciones (2026-10-02, 47 d, no es fin de periodo) y espana-manual (cierre 2025 sin fecha de lectura, así que no hay prueba de que se haya revisado).
- El script reescribe también `informes/research/2026-11-14-C287-frescura.md` (comportamiento habitual del script).

## 4. etf-flujos en la Órbita (Fichas por activo > fondos cripto)
- `vistas.html`: nuevas funciones `etf13f` y `etfContraste`, enganchadas al final de `nEtf()`.
  - 13F del 3T: tabla por fondo (declarantes 3T/2T, valor 3T y 2T, cambio, acciones), recuento de la unión de los 7 ETF de XRP (190 frente a 163; 47 nuevos, 20 que ya no aparecen), top 10 de declarantes por fondo (plegable), nivel y completitud PARCIAL [VERIFICAR].
  - Lecturas directas en EDGAR (nivel P): tabla gestora x fondo.
  - Contraste (Farside, S): flujo neto diario de ETF de BTC, 9-13 nov, y IBIT/FBTC del 13-nov; nota de XRP/XLM sin tracker.
- Unidades: 13f.info trae miles de USD y EDGAR trae USD; la vista convierte todo a millones de USD (M$) y lo declara en cada cabecera y nota. Se añadió la clave `unidades` en `explorador/etf-flujos.json` para dejarlo documentado en origen (el resto del fichero no cambia).
- Comprobado: la pestaña carga, las tres secciones y sus tablas se pintan, 0 errores de consola.

## Verificaciones
- `python scripts/revisar_explorador.py`: 0 avisos en 13 capas y 322 movimientos.
- `python scripts/construir_orbita.py`: docs/orbita/index.html regenerado (4542 KB, versión pública).
- No se hizo commit ni push.

## Pendiente
- Prioridad 1 del móvil (`construir_movil.py`) y prioridades 5-14 de la auditoría.
- Decidir si el origen de los «null» de las notas se limpia en los scripts (espana_cifras y otros) para que también salgan limpios en el móvil.
