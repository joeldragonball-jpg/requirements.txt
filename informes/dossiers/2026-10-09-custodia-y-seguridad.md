# Dossier: Custodia y seguridad al tener XRP y XLM (9-oct-2026)

> Informativo. No es recomendación de compra, venta ni de ningún exchange o wallet concreto. **Aviso de método:** en esta sesión he leído como fuente "casi primaria" solo el texto del art. 75 de MiCA (reproducido por springlex.eu a partir del DOUE), la documentación de Stellar (memos) y resultados de búsqueda que citan a xrpl.org, CNMV y ESMA. Las cifras de hackeos y quiebras vienen de **prensa y webs de seguridad (secundarias)** y las marco así. No he leído sentencias, el texto íntegro de los informes forenses ni el registro de ESMA en sí. Lo no confirmado va como [VERIFICAR]; las predicciones, como [ESPECULACIÓN].

## 1. Resumen ejecutivo
1. **Quien tiene las claves, tiene los fondos.** Con un exchange confías en su seguridad y en su solvencia; con wallet propia asumes tú el riesgo de perder la clave, de que te la roben o de fallecer sin dejar acceso. No hay una opción sin riesgo: son riesgos distintos.
2. **Los grandes fallos recientes no fueron "criptografía rota", sino proveedores, personas y procesos:** Bybit (feb-2025, ~1.500 M$) por una interfaz de un proveedor de multifirma comprometida; Bitget (24-sep-2026, 387,5 M$ según los forenses citados; 351,6 M$ en la primera cifra) por un día cero en productos de seguridad de terceros; Coinbase (may-2025) por empleados de soporte sobornados. Las claves de multifirma o el almacenamiento en frío no bastan si falla lo que rodea a la firma.
3. **Quiebras: lo que se recupera depende del caso y de la valoración.** En FTX los acreedores han recibido, en dólares valorados a la fecha de la quiebra (nov-2022), más del 100 % (prensa, [VERIFICAR] en documentos del fideicomiso); no es lo mismo que recuperar las monedas ni su valor actual. Lo cobrado llegó años después.
4. **MiCA (UE):** los CASP autorizados deben **segregar** los criptoactivos de clientes, tener política de custodia, dar **extractos al menos trimestrales** y **responder por pérdidas atribuibles a ellos** hasta el valor de mercado del activo perdido (art. 75 del Reglamento (UE) 2023/1114, leído). El periodo transitorio terminó el **1-jul-2026** (secundaria [VERIFICAR]). Se comprueba en el registro de ESMA y en la CNMV.
5. **Ninguna garantía pública cubre cripto** (ni el Fondo de Garantía de Depósitos ni el de Inversiones): lo dicen la CNMV y el Banco de España (secundaria, comunicados citados por prensa [VERIFICAR texto vigente]).
6. **XRP/XLM:** el error más común que pierde fondos es **olvidar la destination tag (XRP) o el memo (XLM)** en depósitos a exchanges, o enviar por una red que el destinatario no soporta. Los ecosistemas tienen además estafas propias (sorteos "envía X y recibe el doble", suplantación de Ripple/Stellar, falsos soportes).

## 2. Exchange frente a custodia propia: riesgos de cada una
| Opción | Qué es | Riesgos principales | Qué dice la regulación (UE) |
|---|---|---|---|
| **Exchange / custodio (CASP)** | El proveedor guarda las claves; tú tienes un saldo en su sistema | Hackeo (Bybit, Bitget); quiebra o fraude (FTX); congelación de retiradas; insider/soporte (Coinbase); mezcla de fondos si no hay segregación; sin garantía pública | MiCA art. 75: contrato escrito, registro de posiciones por cliente, segregación legal (aislada de acreedores del proveedor, también en insolvencia) y operativa, extractos trimestrales, procedimiento de devolución, responsabilidad por pérdidas atribuibles |
| **Wallet propia, software ("hot")** | Tú guardas la frase semilla/clave en app o ordenador | Malware, phishing, frase semilla fotografiada o en la nube (caso Larsen, abajo), errores al firmar | MiCA **no** regula la custodia propia: no hay proveedor ni reclamación; solo aplican las normas generales (fiscalidad, DAC8 no la recoge salvo que uses un CASP) |
| **Hardware wallet** | Dispositivo que firma sin exponer la clave | Copia de seguridad mal guardada, compra por canal no oficial o manipulado, firmar a ciegas lo que muestra una pantalla comprometida (análogo a Bybit), pérdida del dispositivo sin copia | Igual: sin proveedor regulado de custodia |
| **Multifirma** | Varias claves, X de N para mover fondos | Complejidad; todas las claves en el mismo lugar o la misma interfaz web (Bybit usó multifirma); pérdida de quórum | Sin norma específica para particulares |
| **Custodio cualificado / banco** | Entidad regulada guarda por ti | Concentración y dependencia de un tercero; la responsabilidad existe pero tiene tope (valor de mercado del activo perdido) | MiCA art. 75; subcustodios deben estar autorizados (art. 59) y se te debe informar |

**Hechos clave de la regulación (art. 75 MiCA, texto leído):**
- Contrato escrito con identidad de las partes, política de custodia, sistemas de seguridad, comisiones y ley aplicable.
- Registro por cliente; movimientos anotados "lo antes posible".
- Resumen de la política de custodia disponible a petición en formato electrónico.
- Extractos **al menos cada tres meses**.
- Procedimientos para devolver los criptoactivos o los medios de acceso "lo antes posible".
- Segregación: activos del cliente separados de los propios; **segregación legal** (sin recurso de los acreedores del proveedor, en particular en insolvencia) y **operativa**.
- Responsabilidad por pérdidas **atribuibles al proveedor**, con tope en el valor de mercado del activo en el momento de la pérdida; no responde de incidentes ajenos a la prestación del servicio.
- Subcustodios autorizados conforme al art. 59 y con información al cliente.

Matiz [OPINIÓN mía, sin verificar jurídicamente]: "atribuible" deja margen de discusión en un hackeo (¿fallo del proveedor o ataque inevitable?). Cómo lo interpretarán tribunales y supervisores está por ver.

## 3. Hackeos y quiebras 2022-2026
> Cifras de prensa/seguridad (secundarias). "Qué recuperaron los clientes" se indica solo si la fuente lo dice.

| Caso | Fecha | Qué pasó | Pérdida | Fallo concreto | Clientes |
|---|---|---|---|---|---|
| **FTX** | nov-2022 | Quiebra por fraude y uso indebido de fondos de clientes (hechos judiciales ya probados; detalle [VERIFICAR] en sentencias) | Miles de M$ (agujero) | Mezcla de fondos de clientes con una empresa de trading; sin segregación real | Reparto escalonado: sep-2025 ~1.600 M$; mar-2026 ~2.200 M$; jul-2026 ~900 M$; total ~10.000 M$; clases principales ~105 % acumulado **en dólares a nov-2022** (prensa). 6.º reparto previsto ~ene-2027 [VERIFICAR] |
| **Celsius / Genesis / Gemini Earn** | 2022-2023 | Plataformas de préstamo ("earn") congelan retiradas; Genesis cae | Miles de M$ | Prestar fondos de clientes con riesgo de contraparte; clientes eran acreedores, no propietarios | Gemini Earn: ~97 % en especie (prensa) tras negociar en la quiebra de Genesis. Celsius: [VERIFICAR] |
| **Larsen (cofundador de Ripple)** | 30-ene-2024 | 213.078.759 XRP salieron de cuentas personales suyas (no de Ripple) en 8 transacciones en 12 h | ~112 M$ | Compromiso de clave/semilla (causa exacta no publicada en lo que he leído) | Mayoría convertida y "casi todo congelado" según Larsen, con exchanges (prensa). Es el ejemplo de que en XRP hay congelaciones **solo si el destino es un exchange colaborador** |
| **DMM Bitcoin (Japón)** | may-2024 | Robo de ~4.500 BTC; cierre y traspaso de cuentas a SBI VC Trade (mar-2025) | ~320 M$ | Compromiso de la cadena de firma [VERIFICAR] | Promesa de reembolso íntegro y traspaso de cuentas (prensa) |
| **WazirX (India)** | 18-jul-2024 | Robo de ~234,9 M$ (~45 % de las reservas); atribuido a Lazarus (prensa) | 234,9 M$ | Wallet multifirma con interfaz manipulada [VERIFICAR] | Reestructuración; detalle [VERIFICAR] |
| **Bybit** | 21-feb-2025 | Lazarus (Corea del Norte) inyectó JavaScript malicioso en la interfaz de Safe{Wallet}, tras comprometer el portátil de un desarrollador de Safe; los firmantes de Bybit aprobaron sin ver la transacción real | ~1.500 M$ (ETH) | **Cadena de suministro**: la interfaz de firma, no las claves | Bybit repuso las reservas de ETH y se declaró solvente; recompensa de hasta 140 M$; recuperación posterior pequeña [VERIFICAR] |
| **Coinbase (datos)** | 15-may-2025 | Soportistas subcontratados sobornados copiaron datos de ~70.000 clientes; extorsión de 20 M$ rechazada | Coste estimado 180-400 M$; ~45 M$ robados a usuarios en una semana (secundaria) | **Insider/ingeniería social** | Coinbase dijo que reembolsaría a las víctimas de ingeniería social (prensa) |
| **Bitget** | 24-sep-2026 | 387,5 M$ salieron de wallets calientes y templadas en 11 redes, **incluidas XRP Ledger y Algorand** (no consta Stellar en lo que he leído); retiradas pausadas | 387,5 M$ (primera cifra: 351,6 M$) | Día cero en dos productos de seguridad de terceros; actividad maliciosa desde el 31-ago; herramienta de retirada automatizada el 25-sep (SlowMist y Mandiant, citados por prensa) | Bitget dice que cubre la pérdida con su fondo de protección (>464 M$, cifra suya); cada pérdida de un usuario [VERIFICAR] |
| **Otros 2026** | 2026 | Liquid Network (~320 M$ en BTC, sept-2026) y 333 incidentes con 1.730 M$ robados en lo que va de año según TRM Labs (prensa) | — | — | — |

**Patrones (hecho + lectura):**
- **Hecho:** de los casos anteriores, ninguno rompió la criptografía de XRP, XLM, ETH ni BTC. Los fallos fueron en (a) interfaces/proveedores, (b) personas, (c) gestión de claves, (d) fondos de clientes usados de forma indebida.
- **Hecho:** "frío" y "multifirma" no protegen si quien firma ve una pantalla manipulada (Bybit) o si el atacante entra en la red desde un proveedor (Bitget).
- **Opinión:** un fondo propio del exchange (como el de Bitget) es una promesa de la empresa, no una garantía pública; su valor depende de la solvencia futura de esa empresa.
- **Relevancia XRP/XLM:** Bitget confirma que el XRP en exchanges ha estado expuesto a hackeos (XRP figura entre los activos afectados, prensa).

## 4. MiCA y cómo comprobar que un exchange es un CASP
**Obligaciones de un CASP con custodia** (resumen del art. 75, ver §2): segregación, política de custodia, extractos trimestrales, devolución, responsabilidad por pérdidas atribuibles, subcustodios autorizados. **Informar:** mantener informado al cliente de operaciones que requieran su respuesta, y los demás deberes de información de MiCA (no he leído el resto del título V) [VERIFICAR].

**Qué MiCA no hace:** no crea un seguro público; no impide hackeos; no regula la custodia propia.

**Cómo comprobarlo (pasos):**
1. **ESMA – registro provisional MiCA (art. 109):** en la web de ESMA, sección "MiCA / markets in crypto-assets", hay una lista descargable de CASP (archivo CASPS.csv). Según un tercero (tangem.com) había **312 CASP autorizados**, actualizado semanalmente [VERIFICAR fecha]. Busca el nombre jurídico exacto (no la marca) y el país de la autoridad que autorizó.
2. **Servicios autorizados:** que figure "custodia y administración" y "intercambio" según lo que uses; no todos los CASP tienen todos los servicios.
3. **CNMV:** publica las entidades autorizadas en España, incluidas las que prestan servicios por pasaporte desde otro Estado miembro. Según prensa había **más de 130** entidades habilitadas y entre ellas bancos y proveedores españoles (secundaria) [VERIFICAR el listado actual].
4. **Coincidencia:** nombre jurídico, domicilio, web, correo y regulador deben coincidir con lo que muestra la plataforma; los falsos exchanges copian logos y nombres.
5. **Registros de avisos:** la CNMV mantiene listados de entidades no autorizadas/"chiringuitos" [VERIFICAR enlace y vigencia].
6. **Fecha:** desde el 1-jul-2026 ya no hay periodo transitorio en la UE (secundaria): una plataforma sin autorización operando para residentes en España es una señal de alarma.

**Reparto de papeles en España (secundaria):** la CNMV supervisa los CASP y los abusos de mercado; el Banco de España supervisa el aspecto prudencial en lo que le reserva la ley y la emisión de ciertos tokens (ART/EMT). [VERIFICAR la distribución exacta en la ley española vigente.]

## 5. Pruebas de reservas (proof of reserves)
- **Qué demuestran (hecho):** que, en un momento (una "foto"), el exchange controla en la cadena activos al menos iguales a la suma de saldos de clientes comprometidos en un árbol de Merkle; tú puedes comprobar que tu saldo está en el árbol.
- **Qué no demuestran (hecho):** otras deudas (préstamos, obligaciones fuera de la cadena); que los activos no estén pignorados o prestados; que no se hayan movido fondos antes/después de la foto; que la lista de wallets sea completa; ni que se cumpla la segregación legal. Un exchange puede pasar un PoR y ser insolvente.
- **Quién lo hace:** si lo audita un tercero independiente, vale más que si lo publica el propio exchange (idea citada en la fuente consultada).
- **Mejor señal:** PoR **de activos y de pasivos**, por un auditor independiente, repetido con frecuencia, más estados financieros auditados. MiCA no sustituye esto, pero impone segregación y extractos.
- **XRP/XLM:** como los exchanges usan **una dirección con muchas tags/memos**, el PoR debe incluir el total de saldos por tag y todas las direcciones; revisa si el exchange las publica [VERIFICAR por plataforma].

## 6. Seguridad específica de XRP y XLM
### XRP (XRPL)
- **Destination tag (etiqueta de destino):** número que el exchange usa para saber a qué cliente acreditar. Los exchanges usan **una dirección para muchos clientes** (xrpl.org). Si la dirección tiene el ajuste "Require Destination Tag", el ledger **rechaza** pagos sin tag; si no lo tiene, el pago **se ejecuta** y los fondos quedan en la dirección del exchange sin identificar: recuperarlos depende del soporte y puede tardar o no ser posible.
- **Reserva:** el XRPL exige una reserva base de **1 XRP** y **0,2 XRP por objeto** (xrpl.org, dato leído en resultados que lo citan; la reserva se cambia por votación: [VERIFICAR hoy]). Por eso **enviar menos de la reserva a una cuenta nueva falla**, y por eso no puedes vaciar la cuenta.
- **Trustlines:** para tener tokens emitidos (RLUSD, otros IOU) debes crear una línea de confianza (reserva 0,2 XRP). **Crear una trustline con un emisor desconocido te expone a tokens falsos**: cualquiera puede emitir un token con nombre parecido ("XRP", "RLUSD") y hacerlo aparecer. Comprueba la **dirección del emisor**, no el nombre.
- **Direcciones de depósito:** copia siempre desde la app oficial; verifica primero 4 y últimos 4 caracteres; los portapapeles y extensiones pueden cambiarla (malware "clipper").
- **Irreversibilidad:** no hay "deshacer" en XRPL; solo pueden congelar emisores de tokens (no XRP nativo).

### XLM (Stellar)
- **Memo:** la documentación oficial de Stellar lista cuatro tipos (TEXT hasta 28 bytes, ID de 64 bits, HASH y RETURN) y dice que los memos se usaban para distinguir cuentas en una cuenta agrupada, pero que esa función está **sustituida por las cuentas multiplexadas (muxed accounts)**. Muchos exchanges **siguen** pidiendo memo [VERIFICAR por exchange]. Sin el memo correcto, el exchange puede no poder identificar tu depósito.
- **Reserva mínima y trustlines:** Stellar exige un saldo mínimo por cuenta y por entrada (trustline, oferta) [VERIFICAR cifras actuales]; los activos distintos de XLM requieren trustline y pueden ser falsos, igual que en el XRPL.
- **Direcciones:** las públicas empiezan por "G"; las multiplexadas, por "M". Verifica el tipo que pide tu plataforma.
- **Clave secreta:** empieza por "S"; **nunca** la introduzcas en una web que te la pida para "reclamar" o "validar".

### Errores comunes que pierden fondos (ambos)
1. Olvidar tag/memo o ponerlo mal.
2. Enviar a una red equivocada (por ejemplo, XRP en una red distinta de la XRPL hacia una dirección que solo existe en esa otra red): el exchange destinatario puede no recuperarlo. Comprueba la red antes de enviar; haz un envío de prueba pequeño.
3. Enviar a una dirección distinta por copia manual.
4. Usar un exchange que no lista el activo o la red (p. ej. envolver/"wrapped" XRP en otra cadena).
5. Firmar mensajes o transacciones de sitios desconocidos.
6. Guardar la frase semilla en fotos, notas o la nube.

## 7. Estafas y bulos habituales en XRP/XLM
- **"Sorteos" y "doble o nada":** enviar XRP/XLM a una dirección para recibir el doble. **Ripple y su CTO (David Schwartz) han dicho públicamente que no hay airdrops ni sorteos de este tipo**; Ripple demandó a YouTube por permitir estos vídeos (Decrypt, 2020; secundaria) y ha vuelto a advertir de deepfakes de Brad Garlinghouse y otras figuras (prensa).
- **Suplantación de Ripple/Stellar/Garlinghouse/Larsen:** cuentas con nombre parecido en X, YouTube, Telegram o Discord; "verificado" **no** garantiza veracidad (se han pagado y se han comprado marcas azules).
- **Falsos airdrops:** piden conectar la wallet o firmar un permiso para "reclamar"; en XRPL/Stellar, también crear trustlines con tokens fraudulentos para que "aparezcan" cantidades falsas.
- **"Recupera tus fondos":** falsos recuperadores que cobran por adelantado a víctimas de estafas previas. Ni un abogado, ni la policía, ni un exchange te pide pagar por adelantado en cripto para "desbloquear" fondos.
- **Falso soporte:** mensajes directos con enlaces o "agentes" de soporte que piden la frase semilla. **Nadie legítimo la pide.**
- **Phishing tras filtraciones de datos:** el caso Coinbase (may-2025) mostró que los atacantes usan datos reales de clientes para suplantar al exchange. Desconfía de llamadas y mensajes "urgentes".
- **Plataformas falsas ("chiringuitos")** con rentabilidades fijas o "staking de XRP garantizado": revisa autorización (§4).
- **Pig-butchering / romance:** relación larga por mensajería hasta que te llevan a una plataforma falsa.
- **Señal de alarma general:** prisa, rentabilidad garantizada, pedir enviar primero, canal privado, presión para no consultar a nadie.

## 8. Herencia y acceso
> Información general, no consejo personal ni jurídico.

- **Hecho técnico:** si el titular fallece sin dejar acceso a la clave/semilla de una wallet propia, **nadie puede recuperar los fondos**; no existe "soporte" que los libere. En un exchange, los herederos acreditan su condición (certificado de últimas voluntades, testamento o declaración de herederos) y el proveedor decide según sus procedimientos y ley aplicable.
- **Fiscalidad (secundaria, prensa):** el heredero tributa por **Impuesto de Sucesiones y Donaciones** (cedido a las comunidades autónomas; normalmente la de residencia del fallecido), valorando las criptomonedas a valor de mercado en la fecha del fallecimiento; no tributa por IRPF por las plusvalías hasta que venda, con valor de adquisición a efectos de futuras ventas [VERIFICAR criterio concreto de la AEAT/DGT; ver dossier 13].
- **Opciones legales en España (generales):** testamento notarial que mencione activos digitales; **testamento digital** o instrucciones (arts. 96 de la Ley Orgánica 3/2018, sobre testamento digital, [VERIFICAR el artículo]); albacea; depósito de instrucciones con notario; y reparto de acceso (multifirma 2 de 3, copias de semilla en lugares distintos). Cada una tiene riesgos (quien conoce la semilla puede mover los fondos ya) y debe valorarse con un notario o abogado.
- **Opinión mía:** la mayor pérdida "silenciosa" de cripto es la clave perdida, no el hackeo. Un procedimiento documentado de acceso (sin escribir claves en el testamento, que es un documento no privado) es una decisión del titular.

## 9. Protección del inversor y reclamaciones
- **Fondos de garantía:** la CNMV y el Banco de España indican que las criptomonedas **no están cubiertas** por el Fondo de Garantía de Depósitos ni el Fondo de Garantía de Inversiones (comunicados, citados por prensa). Un exchange autorizado no equivale a un depósito garantizado.
- **Advertencias de publicidad:** normativa de la CNMV exige advertir de alto riesgo y pérdida total, y de que no hay protección de fondos de garantía (prensa; circular de publicidad de 2022) [VERIFICAR vigencia tras MiCA].
- **Reclamaciones:** primero, al **servicio de atención al cliente / defensor del cliente** de la entidad; si no responde o no estás de acuerdo, a la **CNMV** (si es un CASP o servicio de inversión) o al **Banco de España** (si el prestador es una entidad de crédito o de pago respecto a servicios bancarios) [VERIFICAR el cauce exacto y plazos]. El resultado de estas reclamaciones **no es vinculante** en general; la vía vinculante es judicial o arbitral [VERIFICAR].
- **Denuncias penales:** estafas o robos: Policía Nacional/Guardia Civil y, si procede, denuncia con cadena de transacciones (hashes, direcciones, capturas).
- **Ley aplicable:** si el proveedor está en otro Estado miembro (pasaporte), la autoridad competente es la de allí, pero puedes avisar a la CNMV [VERIFICAR].

## 10. Checklist práctica (sin datos personales)
**Antes de elegir dónde guardar**
- [ ] ¿Está el proveedor en el registro de ESMA/CNMV con ese nombre jurídico y los servicios que usas?
- [ ] ¿Ofrece contrato, política de custodia resumida, extractos trimestrales y procedimiento de devolución (art. 75)?
- [ ] ¿Publica prueba de reservas de activos **y** pasivos, auditada por terceros? ¿Y cuentas auditadas?
- [ ] ¿Qué proporción de fondos está en frío? ¿Quién custodia (subcustodio autorizado)?
- [ ] ¿Qué dice sobre su fondo de compensación y sus límites? ¿Es una promesa propia o un seguro externo?
- [ ] ¿Historial de incidentes y cómo respondió (¿reembolsó, tardó, culpó al cliente?)?

**Señales de alarma:** rentabilidad garantizada; retirada bloqueada "por mantenimiento" sin plazo; piden más dinero para liberar fondos; soporte que pide semilla; mezcla de productos "earn" con tus fondos sin explicación; empresa sin dirección verificable; promoción con famosos o deepfakes.

**Cuenta en exchange**
- [ ] 2FA con app o llave física (no SMS); contraseña única en gestor.
- [ ] Lista blanca de direcciones de retirada y retraso de retirada.
- [ ] Alertas por correo; correo con 2FA propio.
- [ ] No dejar más en el exchange que lo que necesitas operar (criterio general, no consejo).

**Wallet propia**
- [ ] Hardware comprado en canal oficial; comprobar sellos y firmware.
- [ ] Semilla escrita en papel/metal, **nunca** en foto, nube ni chat; copias en lugares separados.
- [ ] Probar la restauración con una cantidad pequeña antes de confiar.
- [ ] Verificar en la pantalla del dispositivo la dirección y el importe que vas a firmar (lección de Bybit).
- [ ] Un equipo limpio para firmar; extensiones de navegador mínimas.

**Al enviar XRP/XLM**
- [ ] Comprobar red, dirección y **tag (XRP) / memo (XLM)** que pide el destino.
- [ ] Enviar primero una prueba pequeña y esperar la acreditación.
- [ ] Recordar la reserva (XRPL: 1 XRP base + 0,2 por objeto; Stellar: mínimo por entrada) [VERIFICAR valores].
- [ ] Revisar el emisor del token antes de aceptar una trustline.

**Contra estafas**
- [ ] Nadie regala cripto; nadie "devuelve el doble".
- [ ] No pulses enlaces de mensajes directos; entra tecleando la URL o desde favoritos.
- [ ] No conectes wallet ni firmes en webs desconocidas.
- [ ] Desconfía de "recuperadores de fondos" que cobran por adelantado.

**Herencia y acceso**
- [ ] Existe un procedimiento documentado que permita a alguien de confianza acceder en caso de fallecimiento, sin exponer claves hoy.
- [ ] Revisarlo con notario/abogado; actualizarlo cuando cambie algo.

## 11. Calendario y eventos propuestos (no añadidos)
| Fecha | Qué | Fuente / estado |
|---|---|---|
| ~**ene-2027** | 6.º reparto de FTX a acreedores | Prensa; fecha aproximada [VERIFICAR] |
| **1-ene-2027** | DAC8: obligaciones de los CASP respecto a identificar a usuarios y reportar | Ya propuesto/añadido (ver dossier 13) |
| **30-jun-2027** | Informe final de la Comisión sobre MiCA (art. 140) | Texto del Reglamento; fecha por mi memoria [VERIFICAR] |

**Propuesta para `eventos/calendario.toml` (no añadida):**
```toml
[[eventos]]
fecha = "2027-01-15"
titulo = "FTX: 6.º reparto previsto a acreedores"
detalle = "Prensa lo sitúa hacia enero de 2027. Fecha aproximada; ver notas del fideicomiso (dossier 14)."
impacto = "bajo"
aproximado = true
fuente = "https://restructuring.ra.kroll.com/FTX/"

[[eventos]]
fecha = "2027-06-30"
titulo = "MiCA: informe final de la Comisión sobre su aplicación (art. 140)"
detalle = "Fecha prevista en el propio Reglamento; no confirmada en esta sesión (dossier 14)."
impacto = "bajo"
aproximado = true
fuente = "https://eur-lex.europa.eu/eli/reg/2023/1114/oj"
```
(La URL de Kroll es la que usa el fideicomiso en mi memoria; no la he abierto: [VERIFICAR].)

## 12. Escenarios [ESPECULACIÓN]
| Escenario | Qué pasaría | Señales |
|---|---|---|
| **A. Más hackeos a exchanges grandes** | Se repite el patrón de proveedores y firmantes | Nuevos incidentes tras Bitget; informes de TRM/Chainalysis a fin de año |
| **B. MiCA madura** | Concentración en CASP autorizados; menos plataformas offshore para residentes en UE | Registro de ESMA creciendo; sanciones |
| **C. Primer caso de reclamación de responsabilidad bajo art. 75** | Se aclara qué es "atribuible" | Sentencias o decisiones de supervisores |

## 13. Qué vigilar
Reembolso real de Bitget y dato oficial de clientes afectados; informe forense final de Bybit/Safe; registro de ESMA y de la CNMV; reparto de FTX; avisos de Ripple/Stellar sobre estafas; criterio de la AEAT/CNMV sobre custodia y DAC8.

## 14. Lo que no sé
- No he leído el registro de ESMA ni el de la CNMV en sí, ni los informes forenses de Bybit/Bitget, ni documentos judiciales de FTX/Celsius.
- Las cifras de reparto de FTX y de pérdidas por hackeos son de prensa; no he verificado si Bitget ya ha devuelto fondos a todos los usuarios.
- No sé si Bitget, Bybit u otros están autorizados bajo MiCA; no lo he mirado (y no recomiendo ninguno).
- Reservas actuales del XRPL y de Stellar (valores hoy), y si los exchanges usan memo o cuentas multiplexadas en Stellar.
- El alcance exacto de la responsabilidad del art. 75 en hackeos.
- La vía reclamatoria exacta (CNMV frente a Banco de España) para cada tipo de proveedor.
- Si el art. del testamento digital citado es el correcto.
