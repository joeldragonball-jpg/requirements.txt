# C135 · Fechas de mandato [S] → [P] · 12-nov-2026

Objetivo: subir a [P] las fechas de `explorador/mandatos.json` marcadas S leyendo webs oficiales. Chrome no usado (sin extensión conectada en esta sesión); se usó WebFetch. JSON no modificado.

| País / cargo | Fecha en JSON | Resultado hoy (fuente, 12-nov-2026) | Nivel |
|---|---|---|---|
| EAU, presidente M. bin Zayed | 14-may-2022 | u.ae: «the third President of the UAE, since 14 May 2022» | **[P]** (sube de S) |
| Francia, Sarkozy | 16-may-2007 → 15-may-2012 | elysee.fr/nicolas-sarkozy: «6 mai 2007» = elección, no traspaso; fin solo «2007-2012» | S (el 6-may NO es el inicio) |
| Francia, Hollande | 15-may-2012 → 14-may-2017 | elysee.fr: solo años 2012-2017 | S |
| Alemania, Schröder/Merkel/Scholz | 27-oct-1998, 22-nov-2005, 8-dic-2021, 6-may-2025 | bundeskanzler.de: solo años (1998-2005, 2005-2021, 2021-2025) | S (días) |
| Países Bajos, Rutte | fin 2-jul-2024 | rijksoverheid.nl (Rutte IV): el 7-jul-2023 Rutte ofreció al Rey la dimisión del gabinete (pasó a en funciones); no sale el 2-jul-2024 | S (matiz: en funciones desde 7-jul-2023) |
| Sudáfrica, Ramaphosa | 15-feb-2018 | thepresidency.gov.za: solo toma de posesión 19-jun-2024 (ya anotada) | S (2018) |
| India, Singh | 22-may-2004 → 26-may-2014 | pmindia.gov.in: 403 | sin cambio |
| Polonia (4 tramos 2001-2017) | varias | gov.pl: la página no trae la lista | S |
| Irán, Pezeshkian | 28-jul-2024 | president.ir: 404 / certificado no verificable | S |
| Egipto, Indonesia, Etiopía | — | sis.gov.eg: certificado inválido; presidenri.go.id: 403; pmo.gov.et: sin datos | S |
| Rusia (Medvedev), Kremlin | — | en.kremlin.ru: error | S |

## Huecos
Webs que piden Chrome/VPN (presidenri.go.id, sis.gov.eg, pmindia.gov.in, kremlin.ru) y Élysée/Bundeskanzler: solo publican años; el día exacto hace falta en BOE-equivalentes (Bundesgesetzblatt, Journal officiel) [VERIFICAR]. Cuba, Venezuela, Rusia pre-2012, China (gov.cn) no intentados.

## Lecciones
1. Las listas oficiales de «presidentes/cancilleres» suelen dar solo años; el día está en boletines (JORF, BGBl), no en la ficha.
2. Cuidado: en Élysée la fecha de la ficha es la de elección, no la del traspaso.
3. WebFetch falla con certificados/403; Chrome es la vía para esas webs (ACCESOS-CHROME.md).
4. Resultado neto: 1 fecha sube a [P] (EAU); 1 matiz nuevo (Rutte, 7-jul-2023).
