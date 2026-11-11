---
tema: C107 · Qué NO construir: lo que ya hacen gratis OpenBB, Koyfin, TradingView y Portfolio Performance
etiquetas: [herramientas, openbb, koyfin, tradingview, portfolio-performance, ghostfolio, no-reinventar]
actualizado: 2026-11-11
---
# C107 · Qué NO construir

> Informativo, no es recomendación. Búsqueda web corta (11-nov-2026), todo nivel [S]: páginas de comparativas con sesgo comercial (cobran comisiones o venden su propia herramienta). Precios y límites: comprobar en la web oficial de cada herramienta [VERIFICAR].

## Hechos [S]
- **OpenBB**: plan «Community» gratuito para particulares en su página de precios (apps y paneles ilimitados, Copilot con 20 consultas al día, soporte por Discord); Workspace Pro de pago por puesto; se menciona una edición «Lite» autoalojada para equipos pequeños (lanzada 20-jul-2026) con precios que las fuentes no coinciden (2.400 $/año vs. desde 500 $/año). Licencia: la plataforma de datos abierta (ODP) es AGPL; un anuncio del 25-ago-2026 habla de liberar todo con licencia permisiva y no pude confirmarlo ([OpenBB precios](https://openbb.co/pricing/)).
- **Koyfin**: plan gratis sin límite de tiempo con paneles de mercado y macro, calendarios económico y de resultados; límites: 2 años de financieros, 1 año de estimaciones, 2 alertas, y pocas listas/filtros guardados. Pago desde 39 $/mes ([Koyfin, resumen de costes](https://costbench.com/software/financial-data-terminals/koyfin/free-plan/)).
- **TradingView**: gratis con anuncios; sobre todo gráficos técnicos: 2-3 indicadores por gráfico y 3 alertas activas. No he encontrado que su plan gratis cubra calendario macro ni filtros fundamentales [S].
- **Portfolio Performance** (de código abierto, escritorio, datos en tu equipo): la opción libre más citada para inversores europeos, con importación CSV y, según las fuentes, PDF de varios brókeres europeos; Ghostfolio es la alternativa web autoalojada; Sharesight (~18 €/mes) y otros son de pago con importación de brókeres europeos [S].

## Razonamiento [RAZONADO]
- **No construir**: gráficos técnicos y alertas de precio (TradingView), pantallas genéricas de acciones y calendarios de resultados (Koyfin), contabilidad de carteras con rendimiento TWR/XIRR e importación de brókeres sueltos si Joel solo quiere ver rentabilidad (Portfolio Performance). Reinventarlos cuesta cuota y mantenimiento y nunca igualarán a equipos dedicados.
- **Sí conviene mantener** (lo que no cubren, por lo que he visto): cruce de **noticia verificada vs. precio**, el registro de **voces con tipo y nivel de evidencia**, los paneles de **España** (BOE, IGAE, SEPI, BDNS) y la **tesis privada** de Joel. Esto es una inferencia mía de que ninguna de las cuatro lo ofrece; no he probado cada herramienta por dentro [ESPECULACIÓN suave].
- Contraargumento: depender de herramientas externas implica cuentas, límites gratis que cambian (Koyfin retiró su plan antiguo en 2026 según una fuente) y datos que no controlas. Mantener lo propio solo donde aporta algo único limita ese riesgo.
- Para la cartera-universal (importador CSV multi-bróker): comprobar antes si el CSV de Portfolio Performance resuelve el caso de Joel; si sí, no seguir ampliando el importador propio [VERIFICAR con un ejemplo real].

## Qué vigilar
- Que los límites del plan gratis de Koyfin/OpenBB sigan como están (revisar 2027-02-11).
- Probar 30 minutos Portfolio Performance con un CSV real de Joel antes de ampliar el importador.
