# C275 · Huecos de la matriz país × tema (19-nov-2026)

Origen: `explorador/regulacion.json` (matriz, 22 jurisdicciones × 8 temas = 176 celdas) y `explorador/paises.json` (fichas). Sesión corta; sin commit, sin API, sin construir_*.

## Diagnóstico
- 29 celdas con etapa vacía («—»). 17 son **Política monetaria** (Fed, BCE, MAS, Banco de Corea, BoJ, RBI, Copom, Rusia, CBUAE, PBoC, BRICS, SARB, BI, Egipto, Etiopía, Irán, BoE, SNB, BoC, RBA, ES): llevan texto, nivel y fecha de fuente primaria; no tienen etapa 0-5 por diseño, no son hueco de contenido (BRICS, ES y ZA/ID quedan en V/S).
- Huecos de contenido real (sin dato, nivel V o S): ETF en BRICS (no aplica), ID, IR, ES; Fiscal en EG, ET, IR; ETF en AE (nivel S).
- Prioridad pedida (G20, UE, Singapur, Corea, Emiratos): UE, SG, KR, EEUU, JP, CN, BR, RU, UK, CA, AU ya tienen política con nivel P. Emiratos: solo ETF abierto (S).
- Países: no queda ningún texto con «…» en el JSON; 12 fichas tienen `sistemas_publicos` en null (BR, ZA, ID, EG, ET, IR, AE, SV, AR, VE, CU, MX, CA; pendiente C61) y se muestran como sin dato.

## Cerrado
- Aviso de `paises.json`: «un campo es null» pasa a «un campo está vacío». No había más «null» en textos de ambos JSON.

## Abierto (sin relleno inventado)
- AE ETF (S): intento con sca.gov.ae en Chrome; el sitio redirige a otro dominio y el lector bloquea la lectura. Sin fuente primaria leída; queda en S.
- ID ETF (OJK), IR ETF y fiscal, EG fiscal, ET fiscal, ES ETF: no se encontró fuente primaria leída en esta sesión (3 intentos previos documentados en el JSON); quedan vacíos/VERIFICAR.
- `sistemas_publicos` de 12 países: no tocado (C61).

## Validación
`python scripts/revisar_explorador.py`: 0 avisos; Radar regulatorio con 9 sin dato (no cuentan como aviso).
