# W03 · Huecos del radar regulatorio (2-nov-2026)

Informativo: no es recomendación de compra ni venta. [P] = documento oficial leído; [S] = prensa, despacho o buscador; [VERIFICAR] = sin leer en la fuente. Chrome (extensión) no estaba conectado: se leyó con curl y la API del Banco Central de Brasil. rba.gov.au da 403.

## HECHOS leídos en fuente primaria [P]

**Brasil (Res. BCB 520, texto consolidado en la API del BCB; modificada por la 589)**
- Art. 88: quien ya operaba como proveedor cripto (PSAV) debía pedir autorización en 270 días desde el 2-feb-2026, es decir, hasta el 30-oct-2026. Los que lo pidieron a tiempo pueden seguir hasta la decisión (§6). Los que no lo pidieron deben cesar en 30 días tras el plazo (§7: hacia el 29-nov-2026). Al acabar la adaptación rige la ley 14.478 plena aunque no haya decisión (§3).
- Art. 91 (redacción de la 589, 23-sep-2026): desde el **6-nov-2026** bancos, entidades de pago y demás instituciones del BCB no pueden operar con proveedores que **no estén autorizados**. La redacción anterior (veto desde el 30-oct) decía «autorizados o en proceso»: la 589 quita «en proceso». Alcanza negociación, intermediación, custodia, cambio y cuentas de pago.
- Tensión sin resolver: el §6 del art. 88 deja operar a quien pidió a tiempo, pero el art. 91 solo admite «autorizados» como contraparte bancaria [VERIFICAR cómo lo aplica el BCB].
- Custodia: art. 88 III obliga a informar a diario saldos y activos custodiados, y cada mes pruebas de reservas y cifras de staking; la 589 reescribe las letras b-e desde el 1-ene-2027 y añade los arts. 90-A y 90-B (sin leer).

**Suiza**
- FINMA Guidance 06/2024 (26-jul-2024): el stablecoin suele ser depósito bancario o fondo colectivo; el emisor es intermediario financiero (antiblanqueo). Con garantía de impago de un banco no necesita licencia bancaria, pero FINMA avisa de que no equivale a la protección de una licencia.
- FINMA Guidance 01/2026 (12-ene-2026): custodia de activos cripto con protección en quiebra (ley marco DLT, art. 37d Ley bancaria); un custodio extranjero solo recibe el trato equivalente si tiene supervisión prudencial y su derecho garantiza la protección en quiebra. Los ETP cripto minoristas pasan por la LSFin (art. 70: garantía exigible o real).
- CARF suizo (SIF): no puede aplicarse antes del **1-ene-2027**; el Consejo Federal aprobaría los Estados socios hacia **finales de nov-2026** y notificaría a la OCDE.

**Canadá**
- Proyecto C-31 (Presupuesto 2025, n.º 2): incluye el CARF (Parte XXI de la Ley del Impuesto sobre la Renta); informe del Comité de Finanzas el 30-oct-2026, en fase de informe en la Cámara. Aplicación al reglamento: años 2027 y siguientes.
- Banco de Canadá: reduce su trabajo en una CBDC minorista y lo reorienta a pagos en general. Sin piloto.

**Australia**
- ASIC INFO 225: exención (Instrumento 2025/867) para distribuidores de stablecoins elegibles; plataformas de activos digitales y custodia tokenizada serán productos financieros según el borrador del Tesoro (la ficha ya recoge la DAF Act en vigor el 9-abr-2027).

**Hong Kong y UE**
- HKMA 29-oct-2026: la Fed mantiene 3,75-4 %; la HKMA avisa del diferencial HKD-USD y del *carry trade*. El tipo base queda en 4,25 % por fórmula (cifra confirmada solo por prensa [S]).
- Euro digital: el pleno del Parlamento aprobó su mandato el 9-jul-2026 (416-169-22; Banca d'Italia). Sigue el trílogo; sin acuerdo [P]. Objetivo de cerrar a fin de 2026 solo según prensa [S].

## Solo [S] (queda para subir a [P])
- Australia: INFO 230 retirada el 7-nov-2025 y absorbida por RG 282; Proyecto Acacia (18-may-2026) y papel de CBDC minorista del RBA (sep-2026).
- Canadá: compromisos previos al registro de la CSA (aviso 21-332, 2023) para custodia.
- Egipto: la subida de 100 pb del 29-oct de Egypt Today choca con otra fuente; no se escribió como hecho.

## Caso a favor / en contra (sin recomendar nada)
- **A favor** (de más claridad para activos digitales como XRP/XLM): Brasil exige licencia y datos de custodia y prueba de reservas; Suiza da protección en quiebra a la custodia; Australia ya exime a distribuidores de stablecoins y prepara licencia de plataformas; el CARF avanza en Suiza y Canadá.
- **En contra**: veto bancario brasileño a no autorizados desde el 6-nov (riesgo de salida o corte para plataformas sin licencia); Suiza limita sub-custodios extranjeros; el CARF aumenta la información a las autoridades fiscales desde 2027; el euro digital aún sin acuerdo.
- Qué cambia para XRP/XLM: nada directo en las fichas leídas; el efecto es sobre plataformas y custodios con los que se opera, no sobre los tokens. [ESPECULACIÓN] fuera de eso.

## Huecos que siguen abiertos
Egipto y Etiopía (ETF, stablecoins, tokenización, custodia, fiscal), Suiza tokenización, Canadá ley marco/tokenización/stablecoin en vigor, Australia fiscal (fecha del CARF) y decisión del RBA del 3-nov, texto de la DAF Act y RG 282, lista de PSAV autorizados en Brasil (¿Ripple?), decisión del Banco Central de Egipto del 29-oct.

## Seguridad (3 líneas)
Sin claves ni secretos; solo lectura de webs oficiales (sin saltar anti-bots; rba.gov.au 403 respetado); sin workflows ni API de Anthropic.
