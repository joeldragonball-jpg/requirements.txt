# C11 · Comprobar el Worker de Cloudflare que lanza los bots (lo hace Joel)

Coste: 0 % de cuota · Cuándo: cuando Joel pueda; sin día fijo

Estado a 26-oct-2026 22:25 (hora España): el Worker `lanzador-bots` está creado, pero GitHub aún no muestra ejecuciones con evento `workflow_dispatch` de «Alertas de precio» ni «Vigilancia on-chain» (solo `schedule`).

Pasos: Cloudflare → Worker `lanzador-bots` → Edit code → pestaña Scheduled → «Trigger scheduled event». Debe salir `alertas.yml 204` y `onchain.yml 204` (204 = lanzado). 401 = token mal o caducado; 403/404 = falta el permiso «Actions: Read and write» o el repo en el token; 422 = parámetro no aceptado. Después, en Settings → Triggers, comprobar que existe el cron `*/30 * * * *`, y a los 30 minutos ver en GitHub → Actions una ejecución con `workflow_dispatch`. El token solo va en Cloudflare, nunca en el chat ni en el repo.

Código del Worker: `scripts/cloudflare-lanzador-bots.js`. Si sale un error, pasarle a Claude el código y el texto (sin el token).
