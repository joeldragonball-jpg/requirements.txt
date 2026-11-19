# C260 · Indicadores recientes de países · 19-nov-2026

## Cambios en explorador/indicadores-manual.json (único archivo editado)
- GB.ipc: 3,6 % interanual, oct-2026 (ONS D7G7, publicado 18-nov; antes 3,5 % sep). Nivel P. Próxima: 16-dic.
- GB.paro: 4,6 % (jul-sep 2026, tres meses móviles; ONS MGSX, publicado 17-nov; Q2 4,9 %). Nivel P. La serie etiqueta ese periodo «AUG» (mes central); fecha guardada 2026-09. Próxima: 15-dic.
- GB.paro_juvenil: 15,1 % (16-24, MGWY, jul-sep; antes 15,6 %). Nivel P.
- EG.tipo_oficial (nuevo): depósito a 1 día 20 % tras subida de 100 pb el 29-oct-2026 (prensa: Reuters vía agregadores, Daily News Egypt). Nivel S: web del CBE da 404/bloqueo (probado en Chrome) [VERIFICAR].

## Contrastado sin cambio
- RU: tabla del Banco de Rusia (19-nov) aún termina en sep-2026 (IPC 6,35 %, clave 14,00 %); octubre solo por semanales/prensa (~7 %), no oficial.
- JP PIB 3T: -0,1 % anualizado / -0,0 % trimestral (Gabinete, 16-nov), ya reflejado.
- Ya vigentes de pasadas anteriores: US, CN, IN, BR, ZA, ID, AR, SV, AE, CU, VE. Países UE y tipos oficiales (ocde-bis.json, BIS) los leen scripts, no tocados.

## Sin dato / pendiente
- RU IPC octubre oficial; EG paro y PIB; IR, ET, VE (paro, PIB); IT salario mínimo; tipo oficial de EG, ET, IR, AE, SV, VE, CU, AR (2025-06 en BIS) fuera de BIS.
- Fuentes bloqueadas: CBE Egipto (404/rechazo), BPS, BCR (pasadas anteriores).

Validación: `python scripts/revisar_explorador.py` → 0 avisos. Sin commit, sin construir_*.
