# W03 · Huecos del radar regulatorio (10-nov-2026)

Etiquetas: [P] = documento oficial leído · [S] = prensa o despacho · [VERIFICAR] = sin confirmar · [ESPECULACIÓN]. Informativo; no es recomendación de compra ni venta. Los datos salen de `explorador/regulacion.json` (campo `revisado` = 2026-11-10).

## 1. Fechas previstas ya pasadas

**Brasil (ley marco, custodia, política).** El Voto 108/2026-BCB (22-sep-2026, PDF de normativos.bcb.gov.br, leído [P]) propone aplazar al **6-nov-2026** el inicio de la vedación del art. 91 de la Res. BCB 520. El texto original decía 30-oct-2026. Desde esa fecha, bancos, entidades de pago y demás instituciones autorizadas no pueden operar con proveedores cripto que no estén autorizados ni en trámite. La vedación alcanza negociación, intermediación y custodia, operaciones de cambio, cuentas de pago y transacciones de pago hechas para viabilizar esas operaciones. El motivo del aplazamiento es publicar antes la lista oficial de instituciones en transición. Los cambios del art. 88 III (informes) entran el **1-ene-2027**. Es un voto, no la resolución publicada: la Res. 589 se leyó en otra pasada (2-nov), pero esta vez no la he vuelto a abrir. La lista oficial y los efectos tras el 6-nov quedan [VERIFICAR]. Copom del 3-4 nov: la celda de política ya cita la fecha, y esta pasada no verificó el resultado [VERIFICAR].

**Rusia (stablecoins).** La propuesta de FinCEN sobre los sub-agentes de A7 (publicada el 5-oct) daba 30 días de comentarios, es decir, hasta ~4-nov [S: búsqueda, resúmenes de TRM y Decrypt; el PDF de FinCEN no se abrió]. No he visto regla final [VERIFICAR]. La ley 282-ФЗ no cambia: 1-mar-2027 y 1-jul-2027 siguen siendo los hitos de la celda.

## 2. Celdas rellenadas

| Celda | Etapa | Dato clave | Nivel |
|---|---|---|---|
| UK · stablecoins | 3 | PS26/10 (jun-2026): respaldo en depósitos y deuda corta, statutory trust, reembolso tras KYC, exceso del 5 %. Sistémicas bajo el Banco de Inglaterra: máx. 70 % deuda británica <6 meses, mín. 30 % depósitos en el banco central, tope £40 mil M por moneda, T+0. En vigor el **25-oct-2027** | P |
| UK · custodia | 3 | PS26/11: salvaguarda con **CASS 17** adaptado a cripto (corrige a Gemini, que decía CASS 16); prudencial en PS26/12. En vigor 25-oct-2027 | P |
| UK · tokenización | 1 | Visión conjunta FCA-BoE (sept-2026) solo vía despacho; la PS26/10 admite activos de respaldo tokenizados | S |
| UK · CBDC | 1 | Libra digital en fase de diseño; decisión prometida para 2026; sin decisión vista | S |
| ZA · stablecoins | 1 | Comunicación conjunta SARB (28-may-2026) [P]: cripto y stablecoins fuera de la ley de pagos; improbable aceptar como pago las no respaldadas y las de divisa extranjera (riesgo de dolarización); prueba de stablecoins en rand en el sandbox del IFWG | P |
| ZA · custodia | 4 | La declaración FAIS (2022) incluye la custodia segura como actividad con licencia FSCA [P]; borrador transfronterizo (3-ago, comentarios hasta 30-sep): enviar a monedero propio = exportación de capital | P / S |
| ZA · ETF, tokenización | — | Sin fuente primaria | VERIFICAR |
| ID · stablecoins | 1 | POJK «listo en ene-2027» (investortrust, 8-oct); IDRP en sandbox desde jun-2026 | S |
| ID · tokenización | 1 | Objetivo OJK: tercer trimestre de 2026 (Kontan, 8-jun); plazo vencido sin publicación vista | S |
| ID · ETF, custodia | — | ojk.go.id no cargó; sin dato | VERIFICAR |
| EG, ET | — | cbe.org.eg bloquea el acceso automático; la FRA y nbe.gov.et no publican nada cripto; el aviso etíope de jul-2026 sigue sin localizar | VERIFICAR |

## 3. Caso a favor / en contra

- **A favor de más claridad:** Reino Unido (régimen completo con fecha fija), Brasil (licencias y vedación) y Sudáfrica (licencias FSCA) dan reglas conocidas. Eso permite operar con proveedores autorizados y con custodia segregada.
- **En contra:** Reino Unido tarda hasta oct-2027. Brasil y Sudáfrica cierran el acceso desde proveedores no autorizados, y Sudáfrica trata el envío a monedero propio como salida de capital. Indonesia, Egipto y Etiopía siguen sin marco publicado o sin acceso a la fuente.
- **Qué cambia para XRP/XLM y otros activos digitales:** no hay norma nueva que los nombre. Los regímenes británico y brasileño regulan al proveedor (custodia, plataforma), no al token. Sobre stablecoins, la distinción es que las emitidas en el país bajo licencia (UK, ZA con rand) tienen camino y las de divisa extranjera encuentran freno (ZA). Si eso beneficia a stablecoins sobre XRPL o Stellar depende de quién las emita: [ESPECULACIÓN].

## 4. Límites de esta pasada

- Texto de las PS26/10 y PS26/11 y del Voto 108: extraído de los PDF descargados con `pdftotext`; el modelo de lectura web no pudo decodificarlos, y yo solo leí los capítulos citados, no los documentos enteros.
- La Res. 589 no se ha reabierto; el 6-nov sale del voto.
- Egipto, Etiopía e Indonesia (fuente oficial) siguen pendientes: probar el navegador Chrome.

## 5. Vigilar

1. Lista oficial del BCB de instituciones en transición y primeros cierres tras el 6-nov.
2. Decisión del Banco de Inglaterra sobre la libra digital (prometida para 2026) y POJK de stablecoins de Indonesia (ene-2027).
