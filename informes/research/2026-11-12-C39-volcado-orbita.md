# C39 · Volcado a la Órbita de lo ya investigado (12-nov-2026)

14 movimientos nuevos en `explorador/datos.json` (de 190 a 204), todos con fecha concreta y enlace a su informe: India 2 (RBI 7-oct, SEBI 10-sep), Singapur 3 (MAS dólar mayorista, letras tokenizadas, PS-G03), Emiratos 2 (Ley 54/2023, vencimiento DL 6/2025), Corea 1 (FSC/Bithumb), Hong Kong 2 (HKMA, SFC), Brasil 1 (Res. BCB 589), China 1 (Notice 42), Rusia 1 (ley 282-ФЗ), DTCC 1 (pruebas 15-jul). 4 son [S] (SEBI detalle, CBUAE plazo, SFC) y así se marcan.
Comprobadas 5 cifras contra su informe (repo 5,50 %, TD26101Z, Notice 42, 282-, 4,25 %): coinciden. `revisar_explorador.py`: 1 aviso previo (XRPL 25-sep, mayúscula), no de este volcado.
Quedan sin volcar: T15 BRICS, W03E (Irán/Egipto/Etiopía), D08/D09 y Gemini D01-D05; sobrantes [P] listos: China LPR 20-oct, Corea 29-ene (KoFIU), Brasil Res. 584, Collateral AppChain DTCC, Rusia 7489-У.
Lecciones: 1) un subagente puede preparar el JSON y el coordinador lo aplica sin choques; 2) al reescribir JSON conservar indent=2 y CRLF, o el diff arrastra todo el archivo.
