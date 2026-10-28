# C49 · Stablecoins en el XRPL y Stellar con fuente primaria

Coste estimado: ~3 % de la cuota semanal · Sin día fijo, en sesión nueva · Después se actualiza solo (sin IA)

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P]/[S]/[VERIFICAR], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube» (enséñame `git status` antes). No leas enteros app.py ni apuntes.

Tarea C49: sustituir en el panel «Stablecoins» (explorador/paneles.html, datos en scripts/actualizar_paneles.py: leer_stablecoins) las cifras de DefiLlama [S] del XRPL y Stellar por cifras de fuente primaria.
1. Emisores: lista las stablecoins emitidas en el XRPL y en Stellar (RLUSD, USDC, EURC, USDGLO, etc.). Para cada una, la dirección oficial del emisor SACADA DE LA PÁGINA OFICIAL del emisor (Ripple, Circle, etc.), nunca de un agregador ni de memoria; marca [VERIFICAR] si solo la encuentras en una fuente secundaria.
2. Lectura en cadena [P]: XRPL con la API pública (método `gateway_balances` sobre el emisor: obligaciones en circulación) y Stellar con Horizon (`/assets?asset_code=…&asset_issuer=…`: total emitido). Solo lectura, sin claves, endpoints públicos.
3. Contraste: la atestación o página de transparencia del emisor (Circle, Ripple/RLUSD) con fecha, frente a la cifra en cadena y frente a DefiLlama. Explica las diferencias (cadena de la emisión, reservas, fecha).
4. Script sin IA (scripts/stablecoins_primarias.py) que lea el ledger y guarde en explorador/paneles.json (clave `stablecoins_primarias`) con nivel [P], fecha y fuente; si falla, conserva el dato anterior. Engancharlo a paneles.yml (ya corre de lunes a viernes) solo si yo lo digo.
5. Panel: mostrar al lado la cifra primaria, la de DefiLlama y la diferencia, con el nivel [P]/[S] visible. Probar a 1920×1080.
Informe en informes/research/AAAA-MM-DD-C49-stablecoins-primarias.md (máx. 1 página). Al terminar: fila en research/COLA.md con coste, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».
```
