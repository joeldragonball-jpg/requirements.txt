# C322b (22-nov-2026): interconexión, OUSG y no-action de DTC

Sin API de Anthropic; sin commit. Hechos con fuente y fecha; no es recomendación.

## Interconexión (explorador/interconexion.json)
- Sin enlaces nuevos para XRPL/Hedera: recomprobado (22-nov-2026, P) que XRPL no está en el directorio CCIP (docs.chain.link API mainnet), ni en la página de dominios CCTP (developers.circle.com) ni en los metadatos de LayerZero. Hedera sí está en CCIP y LayerZero (enlaces ya presentes), no en CCTP. Búsquedas en dtcc.com y Swift no muestran enlaces con Hedera/XRPL. Ausencia no prueba inexistencia: [VERIFICAR] para Partior, Fnality, Agorá, Nexus y Canton con ambas cadenas.
- Swift (10-jul-2026, P parte interesada, swift.com/insights/news/collaborative-innovation-...): libro «listo para uso inicial», 17 instituciones piloto con depósitos tokenizados; sin cadenas públicas nombradas. Añadido como nota_estado del nodo swift-ledger y en fuentes.
- Canton «red» vs «cadena»: ya reclasificada el 18-nov-2026 como cadena_publica con nota_tipo (docs.canton.network la define como «public layer 1 blockchain»; matiz: sin estado global único, no EVM, partes identificadas). Razón y fuentes ya constan en el nodo; no se cambió.

## cadenas.json
- ondo/rendimiento: ondo.finance/ousg, tabla Portfolio Overview a 20-nov-2026: 7 días 3,78 %, 30 días 3,73 % (valor subyacente 313,52 M$; APY anunciado 3,73 %). Cifras del emisor, nivel P parte interesada. Sustituyen las [VERIFICAR] de 3,44 %/3,7 %.
- No-action de DTC (11-dic-2025): documento leído en sec.gov (https://www.sec.gov/files/tm/no-action/dtc-nal-121125.pdf, pdftotext, 22-nov-2026), nivel P. La celda de regulación del nodo Canton ahora enlaza a esa URL; la hoja dtcc_ruta ya la tenía.
