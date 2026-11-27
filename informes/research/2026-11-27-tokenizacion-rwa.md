# Tokenización de activos reales (RWA) — situación a 27-nov-2026

Fecha de trabajo: 27-nov-2026. Sin recomendaciones. Etiquetas: [P] primaria/oficial, [D] dato de agregador o medio, [S] secundaria sin contrastar, [VERIFICAR], [ESPECULACIÓN].
Limitación: los datos de RWA.xyz vienen de la lectura de su web mediante la herramienta de lectura de páginas (resume; no es captura). Los detalles por cadena exigen login y no se vieron.

## 1. Valor total on-chain (RWA.xyz, sin stablecoins)
HECHOS (agregador):
- [D] RWA.xyz, 27-nov-2026 (https://app.rwa.xyz/): valor distribuido 41,25 B USD (-4,08 % en 30 días); valor representado 451,86 B USD (+22,49 % en 30 días); 5.942.761 titulares (+7,24 %).
- Diferencia clave: «distribuido» = tokens que circulan libremente entre carteras; «representado» = el activo solo se registra en la cadena (poca liquidez, otra naturaleza). No sumar ni comparar ambas. Los stablecoins quedan fuera de estas cifras según RWA.xyz [VERIFICAR la metodología en su página].
- [S] Cifras anteriores citadas por medios secundarios: ~39,4 B distribuido el 6-nov y ~39,9 B el 22-nov-2026. Un medio da 46,2 B «en 36 cadenas» sin fecha: descartar [VERIFICAR].
- Lectura: el distribuido cae un 4 % en un mes mientras el representado sube; la subida del representado no equivale a más liquidez on-chain.
SESGO: RWA.xyz es un agregador comercial, no un dato oficial; incluye ciertos activos por criterio propio.

## 2. Fondos tokenizados y tesoros (RWA.xyz, 27-nov-2026; https://app.rwa.xyz/treasuries)
- [D] Tesoros tokenizados: 14,11 B USD distribuido (-3,09 % en 30 días); 123 productos; 87.397 titulares; APY 7 días 3,66 %.
- [D] Principales productos (AUM distribuido): USYC (Circle) 2,12 B; USDY (Ondo) 2,38 B; iBENJI 1,66 B; BUIDL (Securitize/BlackRock) 1,55 B; BENJI (Franklin Templeton) 1,41 B; OUSG (Ondo) 0,32 B. Nota: la lectura de la página no ordenó con claridad USDY e iBENJI frente a USYC [VERIFICAR el ranking].
- BUIDL: en jul-2026 medios hablaban de 2,9 B [S] y alguno de >5 B [S] (contradictorio). La cifra de RWA.xyz de hoy (1,55 B) sugiere descenso notable desde esos valores [VERIFICAR con la web del emisor y de BlackRock; no hay dato oficial de BlackRock leído].
- BENJI: un medio dio 1,98 B en abr-2026 [S]; hoy 1,41 B en RWA.xyz.
- Ojo: otras fuentes dan «>26 B en tesoros y fondos monetarios tokenizados» a mitad de 2026 [S]; es otro perímetro (incluye fondos monetarios y probablemente valor representado). No comparable con 14,11 B.

## 3. Por cadena
- [D] Productos presentes por cadena (RWA.xyz): Ethereum (USDY, USYC, iBENJI, BUIDL, BENJI, OUSG); Solana (USDY, USYC, BUIDL, BENJI, OUSG); Stellar (BENJI, USDY); XRPL (OUSG). Los valores por cadena de tesoros no estaban accesibles (login) [VERIFICAR].
- [S] Total RWA distribuido por cadena el 22-nov-2026 (medio de análisis, atribuido a RWA.xyz; no son solo tesoros): Ethereum 14,29 B; BNB Chain 6,06 B; Solana 5,14 B; Stellar 4,87 B; XRPL 3,00 B. Ethereum ≈ 36 % del total (cálculo propio con ~39,86 B).
- [S] Stellar: otras cifras entre 4,1 B y casi 6 B (principios de nov); fondos tokenizados +80,4 M en 24 h el 26-nov frente a +36,3 M en XRPL. XRPL: 642,6 M distribuido el 7-nov frente a 5,14 B «representado» el 17-nov: métricas distintas, no mezclar. Contradicción con la cifra de 3,00 B de XRPL [VERIFICAR].
- Para XRP/XLM: el dato más sólido es cualitativo (BENJI/USDY en Stellar; OUSG en XRPL); las magnitudes por cadena varían mucho según la métrica.

## 4. DTCC, Nasdaq, NYSE y la SEC
- [P/S] Carta de no acción de la SEC (División de Trading y Mercados) a DTC, 11-dic-2025: alivio de 3 años para un «Preliminary Base Version» del servicio de tokenización (Reg SCI, regla 19b-4, estándares de agencia de compensación). Fuente: despachos (Cleary Gottlieb, Morgan Lewis); carta original en fif.com. No es una aprobación normativa general ni se extiende a otros participantes; revocable en cualquier momento.
- Activos elegibles: componentes del Russell 1000, bonos del Tesoro de EE. UU. y ETF de índices principales (S&P 500, Nasdaq-100).
- [S] The Industry Spread, 20-sep-2026 (https://theindustryspread.com/dtcc-tokenisation-october-launch-three-year-no-action-clock/): producción completa en oct-2026; el reloj de 3 años empieza al lanzar (expiraría ~oct-2029, interpretación del autor). Prueba de producción del 15-jul-2026 con >30 firmas (BlackRock, Goldman, J.P. Morgan, Circle, Ondo) en LFDT Besu y Canton; grupo de trabajo de >100 firmas. Sin solicitud de renovación. [VERIFICAR que el lanzamiento de oct se produjo; no lo confirmé con nota de DTCC.]
- [P/S] Nasdaq: la SEC aprobó el 18-mar-2026 (Release 34-105047; https://www.sec.gov/files/rules/sro/nasdaq/2026/34-105047.pdf, no abierto, confirmado por despachos) el cambio de reglas para negociar valores tokenizados elegibles en el piloto de DTC. Nasdaq avisará con ≥30 días antes de empezar a negociar. Si ya negocia: [VERIFICAR].
- [S] NYSE: presentó un cambio similar en abr-2026 que entró en vigor por vía rápida (una sola fuente secundaria) [VERIFICAR en sec.gov, Release 34-105260].
- Matiz: «aprobado» = reglas de mercado y relief a DTC, no un régimen general de acciones tokenizadas; no equivale a las «acciones tokenizadas» de plataformas cripto (derechos distintos).

## 5. Euroclear / Clearstream y BCE (Pontes / Appia)
- [P] BCE, nota de 1-jul-2025 (https://www.ecb.europa.eu/press/pr/date/2025/html/ecb.pr250701~f4a98dd9dc.en.html): estrategia de dos vías. Pontes (corto plazo): puente entre plataformas DLT y TARGET para liquidar en dinero de banco central, piloto/lanzamiento inicial Q3-2026. Appia (largo plazo): plano de mercado mayorista DLT, hacia 2028.
- [S] Pontes entró en funcionamiento el 21-sep-2026 según varios medios (Cryptonomist, Datafloq, The Industry Spread); uno habla de 13 instituciones y 4 operadores DLT; Clearstream, Deutsche Bank y Santander citados. Otros lo llaman «piloto». La fecha exacta procede de Ledger Insights vía medios [VERIFICAR en ecb.europa.eu].
- [P/S] BCE: desde el 30-mar-2026, activos emitidos en CSD con servicios DLT son admisibles como garantía si cumplen el marco (resumen de RegXplora) [VERIFICAR con nota del BCE].
- [S] Clearstream anunció el 17-ago-2026 pruebas de extremo a extremo antes del lanzamiento. Grupo de contacto: 61 miembros (RegReportingDesk) [VERIFICAR].
- Euroclear: no encontré nada concreto sobre su papel en Pontes [VERIFICAR; no concluir ausencia].

## 6. Contraste alcista / bajista
- Alcista: instituciones y reguladores crean carriles (DTC, Nasdaq, Pontes); 5,9 M de titulares; representado +22 % mensual.
- Bajista: el valor distribuido baja un 4 % en 30 días; BUIDL y tesoros tokenizados parecen por debajo de cifras de jul; mucha cifra de «marketing» contradictoria; la carta de DTC es provisional y revocable; ámbito ligado al piloto, no un mercado abierto.
- [ESPECULACIÓN] La relevancia para XRPL/XLM depende de qué emisores elijan esas cadenas; los datos no permiten concluirlo.

## 7. Pendientes
[VERIFICAR]: (a) metodología y exclusión de stablecoins en RWA.xyz; (b) valor por cadena de tesoros (login); (c) cifras oficiales de BUIDL/BENJI de los emisores; (d) lanzamiento real de DTC en oct-2026 y negociación efectiva en Nasdaq/NYSE; (e) Pontes 21-sep en ecb.europa.eu y participación de Euroclear; (f) cifras de Stellar/XRPL contradictorias.
