# C233 — España: energía (17-nov-2026)

Datos en `explorador/espana-energia.json` (nivel P = fuente oficial leída). Sin recomendaciones.

## HECHOS (fuente oficial leída)
**Precio mayorista (OMIE, ficheros `marginalpdbc`, zona España; cálculo propio: media simple de medias diarias)**
- Octubre 2026: 168,93 €/MWh (máx. diario 249,27). Octubre 2025: 76,02 €/MWh → ≈ 2,2 veces (+122 %).
- Septiembre 2026: 143,9 €/MWh. 1-16 nov-2026 (mes incompleto): 186,08 €/MWh.
- Sustituye el ≈156 provisional del borrador del 10-nov (23 días, prensa).

**Mix (REE REData, oct-2026, total 22,69 TWh)**: ciclo combinado 21,4 %, fotovoltaica 21,0 %, nuclear 21,7 %, eólica 17,5 %, hidráulica 7,1 %. En septiembre el ciclo combinado fue 20,9 % y la fotovoltaica 26,2 %.

**Combustibles (Boletín Petrolero UE, 9-nov-2026, con impuestos)**
| | España | UE-27 | España hace un año |
|---|---|---|---|
| Gasolina 95 (€/l) | 1,730 | 1,877 | 1,477 (+17 %) |
| Gasóleo (€/l) | 1,898 | 2,097 | 1,425 (+33 %) |
España queda por debajo de la media UE (≈ −0,147 y −0,199 €/l); Francia, Alemania, Italia y Portugal están por encima.

**Dependencia energética (Eurostat nrg_ind_id, act. 16-jul-2026)**: España 74,2 % (2022), 68,3 % (2023), 68,9 % (2024); UE-27 62,5 %, 58,3 %, 57,3 %. Brecha 2024 ≈ 11,6 puntos.

**Embalses (MITECO, 27-oct-2026)**: 56,8 % de la capacidad, 31.809 hm³ (20-oct: 57,2 %; 22-sep: 61,8 %).

## Alcista vs. bajista
- Alcista: España paga menos que la media UE por carburantes; la dependencia bajó 5,3 puntos desde 2022; fotovoltaica y nuclear cubren ≈ 43 % del mix en octubre.
- Bajista: el mayorista se multiplicó por ≈ 2,2 interanual y sube en noviembre; el ciclo combinado sigue ≈ 21 % del mix (el gas fija el precio marginal [ESPECULACIÓN] sin cifras de gas leídas); carburantes +17 % y +33 % interanual; reserva hídrica en descenso y por debajo del 60 %.
- Sesgos: la media mensual es cálculo propio, no la publicada por OMIE; la dependencia de Eurostat (68,9 %) difiere de la de MITECO/Endesa (68,4 %, nivel S).

## Abierto ([VERIFICAR] / null)
- Gas: reservas (AGSI+ pide clave de API) y precio MIBGAS/TTF; no se escribe ninguna cifra.
- Rebaja temporal de 20 cént./l en el impuesto de carburantes: solo prensa (Selectra); falta BOE/Hacienda.
- Embalses del 3 y 10-nov: no aparecen en el feed de MITECO.
- Media mensual oficial de OMIE y PVPC mensual; importaciones de gas 2025 (CORES) solo nivel S, no releídas.
- La capa nueva `espana-energia` no está en la lista de `scripts/revisar_explorador.py` (línea ~481) ni en el constructor de `espana.json`: lo añade la sesión principal.

## Fuentes
- OMIE: https://www.omie.es/es/file-download?parents%5B0%5D=marginalpdbc (marginalpdbc_AAAAMMDD)
- Boletín Petrolero UE: https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en
- Eurostat: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_ind_id
- REE REData: https://apidatos.ree.es/es/datos/generacion/estructura-generacion
- MITECO: https://www.miteco.gob.es/es/prensa/ultimas-noticias/2026/octubre/la-reserva-hidrica-espanola-se-encuentra-al-56-8---de-su-capacid.html

> **Corrección 19-nov-2026:** las cifras OMIE de este informe (168,93; 186,08; 143,9; 76,02 €/MWh) usaban la columna de Portugal. Cifras de España: octubre 2026 166,66 y octubre 2025 75,33 €/MWh (ver 2026-11-19-C233-C229-espana-energia-macro.md). La proporción (≈2,2 veces) no cambia.
