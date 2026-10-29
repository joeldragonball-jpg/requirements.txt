# D01–D03, D05: tipo a 10 años mensual por país, fuente oficial del BCE (29-oct-2026)

Fuente [P]: BCE, Data Portal, serie IRS «Long-term interest rate for convergence purposes» (10 años, mensual, media del mes; retraso ~1 mes). URL: `https://data-api.ecb.europa.eu/service/data/IRS/M.<PAÍS>.L.L40.CI.0000.EUR.N.Z?lastNObservations=3&format=csvdata` (funciona con curl desde este equipo).

| País | 2026-07 | 2026-08 | 2026-09 |
|---|---|---|---|
| Alemania | 3,070 % | 3,185 % | 3,473 % |
| Francia | 3,850 % | 4,000 % | 4,440 % |
| España | 3,534 % | 3,635 % | 3,927 % |
| Italia | 3,881 % | 3,986 % | 4,362 % |
| Países Bajos | 3,195 % | 3,285 % | 3,564 % |

Curva diaria de la zona euro (no por país): serie `YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y`, última observación 28-oct-2026.

Límites (HECHOS): es media mensual, solo 10 años y sin 2/5/30 años; no sustituye a una serie diaria por país. Bundesbank (clave `BBSIS…`), AFT (Cloudflare) y Banca d'Italia (sin serie diaria abierta) siguen sin dar la serie diaria gratuita. Los 30 años de subasta de ES, IT y FR ya están en `explorador/bonos-manual.json` [P].
