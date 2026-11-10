# C243 · Empresas públicas y comparador de CCAA (10-nov-2026)

Estado: **en parte**. Salida: `explorador/espana-empresas.json` (generado por `scripts/leer_espana_empresas.py`, sin IA) y 2 bloques nuevos en España (Explorador › vistas).

## Hechos (con fuente)
- **Grupo SEPI 2025**: cifra de negocio 7.384 M€, resultado neto 130 M€, inversiones 529 M€, ≈87.000 profesionales; Grupo Correos = 28 % de la cifra de negocio. Fuente: nota de SEPI de 30-jun-2026 sobre las cuentas anuales aprobadas (nivel P por ser la propia entidad; no auditado aquí). Deuda y aportaciones del Estado: no leídas.
- **Aena 2025**: «ingresos totales» 6.379,2 M€ y EBITDA 3.785 M€ (web de inversores, sin fecha del documento). Resultado, deuda y plantilla: no leídos.
- **Ineco**: su web dice que no ha requerido deuda financiera; las cuentas 2025 y el detalle de subvenciones están en PDF de abril 2026 que no pude leer (sin librería PDF local).
- **Comparador de CCAA** (17 comunidades; Ceuta y Melilla excluidas): paro EPA 2T 2026 (INE, tabla 65334; de 4,63 % Baleares a 14,91 % Andalucía), población 1-ene-2025 (INE, tabla 56941) y deuda PDE 2T 2026 (Banco de España, ya cargada en paneles). Deuda por habitante calculada aquí: mezcla periodos distintos (deuda 2T 2026 / población enero 2025), orden de magnitud correcto, no cifra oficial.

## Sin leer [VERIFICAR]
Adif y Adif AV (adif.es da 403 a scripts), Renfe, Correos (cifra propia), Enaire (web vacía), deuda y aportaciones del Estado de todas, subvenciones en BDNS y contratos (dependen de C241), renta y precio de vivienda por CCAA, vínculo con las investigaciones de S1. No probé Chrome para Adif/Renfe (siguiente paso).

## Opiniones / sesgos
- Las cifras vienen de notas y webs de las propias empresas (autopromoción; «récord» es adjetivo de la fuente). Un resultado bajo o negativo no implica mala gestión: Renfe/Adif tienen función de servicio público.
- [ESPECULACIÓN] ninguna incluida. No se vincula ninguna empresa con investigaciones: no hay base para conclusiones de culpabilidad.

## Lecciones
1. Los sitios de Adif/Enaire bloquean o sirven páginas vacías a scripts: ir directo a Chrome o al Registro Mercantil.
2. Faltan herramientas para leer PDF local: valorar instalar `pypdf` (con OK de Joel).
3. La API Tempus del INE da CCAA fácilmente (tablas 65334 y 56941).
4. Los nombres de CCAA difieren entre INE y Banco de España: hay mapa en el script.

## Segunda pasada (10-nov, tarde)
- **Navantia 2025 (nivel P, nota en sepi.es, 3-jul-2026)**: cifra de negocio consolidada 1.978 M€, resultado consolidado -149 M€ (individual -119 M€), 6.761 personas, cartera 12.826 M€. Motivo de la pérdida no leído [VERIFICAR].
- **Correos 2025 (nivel S, prensa 3-mar-2026)**: 1.658 M€ de cifra de negocio sin ingresos electorales, beneficio 14,4 M€, EBITDA 76 M€. Que lo sostenga la compensación del servicio postal universal (>400 M€/año) es opinión de CCOO, no hecho leído.
- **Renfe 2025 (nivel S, prensa)**: beneficio 60,2 M€, EBITDA 528,6 M€, billetes ≈2.000 M€. Las fuentes discrepan en Renfe Viajeros.
- **Adif/Adif AV (S)**: deuda de Adif AV >21.300 M€ y pérdidas 193,4 M€ por prensa con ejercicio dudoso; CNMC: inversión 5.230 M€ en 2025 (extracto). Cuentas no leídas: adif.es da 403 a scripts y 404 en las rutas probadas con Chrome.
- **Enaire**: PDF oficiales 2025 localizados (cuentas, informe de gestión, deuda) pero ilegibles para las herramientas; solo coste medio de deuda 2,21 % y vida media 6,09 años (extracto). **Paradores** (error de certificado) e **Indra** (conexión rechazada): sin cifras.
- Deuda y aportaciones del Estado: siguen sin leerse en ninguna empresa (necesitan los PDF de cuentas con capa de texto o el OK de Joel para descargarlos e instalar `pypdf`, o IGAE/SEPI).
- Lección añadida: las cuentas de Enaire/Ineco están en PDF; sin lector de PDF local la vía oficial queda cerrada.
