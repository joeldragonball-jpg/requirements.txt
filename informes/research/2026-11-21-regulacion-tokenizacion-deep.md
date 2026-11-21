# Regulación cripto y tokenización: pasada de verificación (21-nov-2026)

Alcance real: pasada corta (no el barrido completo de 25 jurisdicciones y actores). Se releyeron en fuente oficial los puntos de EE. UU., Hong Kong y UE que podían haber cambiado. Las 9 celdas vacías siguen vacías (ver abajo).

## HECHOS leídos en fuente oficial [P]
- **CLARITY (H.R. 3633)**: senate.gov, votaciones 2.ª sesión 119.º: hay 279 votaciones a 20-nov (nombramientos judiciales); la única sobre H.R. 3633 es la n.º 234 del 15-sep (49-50, rechazada). Sin segundo intento en el Senado.
- **GENIUS**: Federal Register (búsqueda «payment stablecoin», 21-nov): la OCC es la única con norma final (23-oct). Tesoro: propuesta 18-ago y norma provisional firme del 30-sep solo sobre el procedimiento del Comité de Certificación de Estados. Fed: dos propuestas del 29-sep. FDIC: solo formularios (20-jul). FinCEN propuso el 19-nov reforzar la diligencia debida (regla general).
- **SEC custodia**: nota 2026-100 (1-oct) leída en sec.gov: propuesta de custodia cripto para asesores y fondos regulados; permite autocustodia en ciertos casos y fideicomisos estatales como custodios; comentarios 60 días tras su publicación en el Federal Register (6-oct, por tanto cierre estimado ~5-dic [razonado]).
- **CFTC**: ANPRM sobre Regulation Crypto Asset Transactions/Markets publicado en el Federal Register el 13-oct.
- **SEC tokenización**: exención temporal para sedes DLT con acciones NMS tokenizadas (orden del 22-sep en el Federal Register), ya recogida.
- **Hong Kong**: Registro de la HKMA leído hoy: solo Anchorpoint (FRS01) y HSBC (FRS02), 10-abr-2026; última revisión 23-abr-2026.
- **SEC-FSA** (nota 2026-107, 20-oct): diálogo en Tokio el 19-oct; no cita cripto ni ETF. Sin novedad para la celda de ETF de Japón.

## [S] prensa, sin comunicado oficial leído
- Euro digital: el trílogo del 18-nov terminó sin acuerdo tras más de 14 h (prensa italiana/alemana); el BCE pide cerrar antes de fin de año. Se escribió en la celda como [S].
- Nasdaq: orden aprobada por la SEC (Federal Register 23-mar-2026, SR-NASDAQ-2025-072) para negociar valores tokenizados, con aviso de 30 días antes de empezar; no se ha confirmado fecha de inicio [S/VERIFICAR].

## Lectura / opinión [ESPECULACIÓN]
- Caso alcista: con CLARITY parada, las agencias (SEC con exenciones y propuesta de custodia, CFTC, OCC) avanzan por reglamento; la tokenización ya tiene marco temporal (DTC, exención de la SEC, Nasdaq).
- Caso bajista: las vías administrativas son revocables por una futura Administración y no sustituyen a una ley; el Congreso 119.º termina el 3-ene-2027 y el proyecto caduca si no se aprueba; GENIUS sin normas finales de Tesoro, Fed y FDIC pese a entrar en vigor el 18-ene-2027.
- Sesgos: las notas del regulador son autodescriptivas (calificar de «claridad» su propia propuesta); la prensa sobre el euro digital mezcla fechas; las gestoras y los emisores (21Shares, etc.) tienen interés comercial.

## No cubierto o sin verificar [VERIFICAR]
- Las 9 celdas vacías (ES ETF, ID ETF, AE ETF, EG/ET/IR ETF y fiscal, BRICS ETF): no se reintentó; el informe del 20-nov ya documenta bloqueos de red/WAF (CNMV, OJK, SCA, DFSA) y no se sortean.
- Sin leer en esta pasada: Reino Unido (BoE), Suiza, Singapur (MAS), Emiratos, Corea, Brasil, India, BIS/FSB/IOSCO/FMI; JPMorgan (Kinexys/JPMD), BNY, Citi, Deutsche Bank, SG-Forge, Euroclear, Swift, Visa/Mastercard, BUIDL/BENJI/WTGXX; ESMA (el registro no se reabrió, vale el de 22-oct).
- Texto del acuerdo o fecha del próximo trílogo del euro digital; confirmación de DTC/Nasdaq del inicio de la negociación tokenizada.

## Candidatos a movimiento de la línea de tiempo
```json
[
  {"fecha":"2026-10-01","capa":"regulacion","actor":"SEC (EE. UU.)","texto":"La SEC propone reglas de custodia de cripto para asesores registrados y fondos regulados (autocustodia en ciertos casos y fideicomisos estatales como custodios); comentarios 60 días tras su publicación en el Federal Register.","fuente":"SEC, nota 2026-100","nivel":"P","url":"https://www.sec.gov/newsroom/press-releases/2026-100-sec-proposal-would-address-how-investment-advisers-funds-can-custody-crypto-assets-under-federal"},
  {"fecha":"2026-10-13","capa":"regulacion","actor":"CFTC (EE. UU.)","texto":"La CFTC publica en el Federal Register un aviso previo de norma (ANPRM) sobre Regulation Crypto Asset Transactions y Regulation Crypto Asset Markets.","fuente":"Federal Register","nivel":"P","url":"https://www.federalregister.gov/documents/search?conditions%5Bterm%5D=%22payment+stablecoin%22&order=newest"},
  {"fecha":"2026-11-18","capa":"regulacion","actor":"UE (Consejo y Parlamento)","texto":"El trílogo del euro digital termina sin acuerdo tras más de 14 horas; el BCE pide cerrar la ley antes de fin de año.","fuente":"Prensa italiana y alemana (sin comunicado oficial leído)","nivel":"S","url":""}
]
```

## Validación
`python scripts/revisar_explorador.py`: 0 avisos. Archivos tocados: `explorador/regulacion.json` (5 celdas: eeuu ley_marco, stablecoins, custodia; hk stablecoins; ue cbdc; campo `revisado` global) y este informe. Las celdas con `caduca` anterior al 18-ene-2027 no vencen antes de hoy.
