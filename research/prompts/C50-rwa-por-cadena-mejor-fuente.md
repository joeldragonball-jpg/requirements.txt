# C50 · Tokenización por blockchain: acercarse a la fuente primaria

Coste estimado: ~3 % de la cuota semanal · Sin día fijo, en sesión nueva · Segunda pasada tras el panel por cadena de 29-oct

## Pega esto en una sesión nueva

```
Sesión corta (máx. 20 min). Sigue CLAUDE.md: español claro, sin recomendaciones de compra/venta, cada dato con fuente y fecha, etiquetas [P]/[S]/[VERIFICAR], nunca claves ni secretos, no lances workflows ni llames a la API de Anthropic, no hagas commit ni push sin mi «sube». No leas enteros app.py ni apuntes.

Contexto: el panel «Mercado y RWA» ya muestra el valor RWA por blockchain (top 10 + XRPL + Stellar) con DefiLlama [S] (solo TVL en protocolos DeFi: Ethereum ~$1.900 M, Solana ~$600 M, Stellar ~$7 M el 29-oct). NO es todo lo tokenizado.
Tarea C50: completar con el valor tokenizado total por cadena con la mejor fuente posible.
1. Compara DefiLlama con RWA.xyz (métrica «distributed asset value» por red) y con los emisores principales (BlackRock BUIDL, Franklin Templeton BENJI, Ondo, Circle USYC, etc.): su propia página o atestación [P], y su dato en cadena si el emisor publica la dirección en su web oficial.
2. Para XRPL y Stellar, lista los emisores de activos tokenizados (fondos, bonos, oro, inmuebles) con su cifra y fecha; Stellar: Franklin Templeton y otros; XRPL: los que publiquen en su web oficial.
3. Propón una tabla «por blockchain» con: valor DefiLlama [S], valor RWA.xyz [S] con fecha, y emisores con cifra [P]. Explica por qué difieren y qué se cuenta en cada una.
4. Frecuencia: mensual a mano con Claude/Gemini (RWA.xyz no tiene API gratuita) y semanal automática solo la parte DefiLlama (ya existe). Anótalo en el informe.
Informe en informes/research/AAAA-MM-DD-C50-rwa-por-cadena.md (máx. 1 página). Al terminar: fila en research/COLA.md con coste, `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`, y cierra con «¿Actualizo el Seguimiento y el planning?».
```
