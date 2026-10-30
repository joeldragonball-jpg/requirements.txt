# C59 · Indicadores económicos y sociales de 12 países (30-oct-2026)

Código: `scripts/indicadores.py` (`leer_indicadores()`, enganchado en `actualizar_paneles.py`). Resultado en `explorador/paneles.json` clave «indicadores»; datos sin API en `explorador/indicadores-manual.json`. Sin claves ni IA.

**Fuentes [P]:** Eurostat (IPCA, paro total y juvenil, PIB trimestral, deuda y déficit Maastricht, AROPE, Gini, salario mínimo) para ES, DE, FR, IT, NL, PL; Banco Mundial (IPC, paro, paro juvenil, PIB, Gini, pobreza nacional) y FMI WEO oct-2026 (deuda y saldo, leídos del navegador porque el FMI da 403 a los scripts) para US, CN, JP, IN, GB, RU.

**Cubierto.** 12 países × 9-10 indicadores, cada uno con fecha, fuente, nivel, definición y periodicidad.

**No cubierto / avisos**
- Salario mínimo de US, GB, RU: cifra recordada, nivel V [VERIFICAR]; JP, CN, IN no tienen mínimo nacional único (null); Italia no tiene mínimo legal.
- Pobreza de US (Census) y JP: sin cifra (null, [VERIFICAR]).
- Fechas de la próxima publicación: solo periodicidad; fechas exactas a `eventos/calendario.toml` quedan pendientes.
- IPC último mes de JP y CN: sin fuente abierta (FRED da timeout); aquí va el IPC anual del Banco Mundial.

**Definiciones distintas (no comparar a la ligera).** IPCA (UE) ≠ IPC nacional ≠ media anual del Banco Mundial; pobreza AROPE (relativa y de exclusión) ≠ línea nacional (BM, p. ej. China 0 %, Rusia 7,2 %) ≠ umbral absoluto del Census; paro mensual desestacionalizado (UE) ≠ estimación anual OIT (BM); el Gini de BM mezcla encuestas de años distintos. No se ordenan países.
