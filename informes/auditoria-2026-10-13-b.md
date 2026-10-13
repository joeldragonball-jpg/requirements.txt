# Auditoría de las guías G6, G7, G10 y G11 y de su coherencia con G12, G13, G15, G5, G9 y MAPA (13-oct-2026)

> Revisión informativa. **No es una recomendación** de inversión ni asesoramiento fiscal. Se han leído completas `2026-10-13-G6-pensiones-pias-seguros-ahorro.md`, `2026-10-13-G7-derivados-y-apalancamiento.md`, `2026-10-13-G10-pymes-y-autonomos.md` y `2026-10-13-G11-startups-y-capital-riesgo.md`. De G12 (§0, §1.3-1.6, §2.1, §4, §6), G13, G15, G5, G9, G8 y `MAPA.md` se han revisado las partes que tocan a estas cuatro guías. **No se ha modificado ningún documento**: aquí solo se proponen correcciones. Los números de línea son los del archivo tal como está hoy.
> **Método.** Todos los ejemplos numéricos se han recalculado a mano y con Python (`C:\Python313\python`). Las fuentes primarias se consultaron el 13-oct-2026 en la API de datos abiertos del BOE (texto consolidado, la última versión de cada bloque): LIRPF (BOE-A-2006-20764), RIRPF (BOE-A-2007-6820), LIS (BOE-A-2014-12328), RDLeg 1/2002 (BOE-A-2002-24252), RD 304/2004 o Reglamento de planes (**BOE-A-2004-3453**, ID localizado vía ELI), Ley 19/1991, Ley 29/1987, Ley 22/2014, Ley 28/2022, Ley 5/2015, LGSS (BOE-A-2015-11724), LSC (BOE-A-2010-10544), Ley 3/2004 (BOE-A-2004-21830), LETA (BOE-A-2007-13409), RD 1007/2023 (BOE-A-2023-24840) y TRLC (BOE-A-2020-4859). También se leyeron en el BOE diario: RDL 3/2026 (BOE-A-2026-2548), Orden PJC/297/2026 (BOE-A-2026-7296), RD 238/2026 (BOE-A-2026-7295), Orden HAC/1028/2026 (BOE-A-2026-20587), RD 126/2026 (BOE-A-2026-3815), las resoluciones de la CNMV de 27-jun-2019 (**BOE-A-2019-9737**) y de 11-jul-2023 (BOE-A-2023-16394), el texto original del RDLeg 3/2004 (BOE-A-2004-4347), los metadatos de las Circulares 1/2018 y 1/2022 de la CNMV y los sumarios del BOE del 6 al 13-oct-2026.
> **Fuentes bloqueadas o no leídas:** EUR-Lex (respuesta vacía); el PDF del DOUE no se pudo extraer a texto. Por eso el Reglamento 2020/1503, ELTIF 2 y MiCA **no** se han verificado en fuente primaria. FRED (VIX) agotó el tiempo de espera, y BIS y FOGAIN no se consultaron.

## 0. Resumen

- **Hallazgos:** 28 en total. **ALTA: 2**, **MEDIA: 4**, **BAJA: 22**. En conjunto, las cuatro guías tienen mucha más calidad que las auditadas por la mañana:
  - **todos los ejemplos numéricos cuadran** (hay una única diferencia de 1 céntimo por redondeo);
  - no hay frases que recomienden algo de forma explícita;
  - casi todos los datos legales clave coinciden con el BOE.
- **Los 5 más graves:**
  1. **G12 l.206**: dice que la deducción del art. 68.1 LIRPF es para «empresas emergentes certificadas» y lo marca **[VERIFICADO 13-oct]**. El BOE no exige esa certificación: vale cualquier SA, SL, SAL o SLL no cotizada que cumpla los requisitos. Para las emergentes de la Ley 28/2022 solo cambian dos cosas: el plazo de suscripción pasa de 5 a 7 años y sus socios fundadores quedan libres del límite del 40 %. G12 contradice así a G10 §6.5 y a G11 §6.1, que son correctas.
  2. **G7 l.90**: dice que el margen inicial es «**no superior** al menor entre el de 2019 y el del mercado». La Resolución CNMV de 11-jul-2023 dice lo contrario: la garantía inicial **exigida** es el menor de esos dos importes, es decir, un mínimo y no un tope. Además, en criptoactivos que no son instrumento financiero MiFID nunca puede ser inferior a la de 2019. La guía invierte el sentido de una protección al minorista.
  3. **G6 l.240**: dice que una modificación del **art. 7.ñ)** (exención del SIALP) entrará en vigor el 23-oct-2026 por BOE-A-2026-20528. Esa norma es la **Ley 4/2026, DF 8.ª**, y modifica la **letra x)**. El texto de la ñ) no cambia.
  4. **G6 l.148 y l.360**: el régimen transitorio de la DT 12.ª atribuye el 40 % al «texto refundido de 2006» y lo marca [VERIFICAR]. Se puede verificar: es el **art. 17.2.b) del RDLeg 3/2004** (texto refundido de 2004, en su redacción a 31-dic-2006). La guía además **omite sus condiciones**: solo vale para prestaciones **en forma de capital** y si han pasado **más de 2 años desde la primera aportación**.
  5. **G12 l.53, l.64 y l.75**: los tramos del art. 63, el art. 66 y el mínimo del art. 57 siguen marcados como «no leídos» o [VERIFICAR]. G6, G7, G10 y G11 los dan por confirmados remitiendo precisamente a G12. Este hallazgo va unido a las **remisiones obsoletas** a guías «pendientes» (G6, G7, G9 y G10), que aparecen en 7 archivos.
- **Marcas [VERIFICADO] comprobadas:** 24, contra el BOE. **23 son correctas** y **1 es incorrecta** (G12 l.206). Una de las correctas (G11 l.194) simplifica de más, y la de G11 l.196 (Reglamento 2020/1503) no se ha podido contrastar en fuente primaria (ver §5). Además, **8 marcas [VERIFICAR] se pueden resolver ya** con el BOE (ver §4, BAJA).

## 1. Contradicciones entre documentos

| # | Tema | Documento A (cita literal) | Documento B (cita literal) | Versión más fiable y por qué |
|---|---|---|---|---|
| C1 | Alcance de la deducción del art. 68.1 | `G12` l.206: «deducción del **50 %** de hasta **100.000 €** invertidos al año en empresas emergentes certificadas» [VERIFICADO 13-oct] | `G11` l.233-236 y `G10` l.214: SA, SL, SAL o SLL no cotizada, con fondos propios ≤ 400.000 €; «5 años (7 años para empresas emergentes)» | **G10 y G11**. Art. 68.1.2.º y 3.º LIRPF (BOE): «empresas de nueva o reciente creación»; las emergentes solo aparecen para ampliar el plazo a 7 años (3.º.a) y para eximir a los fundadores del 40 % (3.º.b). |
| C2 | Margen en futuros y opciones para minoristas | `G7` l.90: «un margen inicial **no superior al menor** entre el de 2019 y el del mercado» | BOE-A-2023-16394 (parte segunda): «se entiende por garantía inicial el importe **menor** entre…»; en cripto no MiFID, «no podrá ser inferior» al de 2019 | **BOE**. Es una garantía mínima exigida, no un máximo. |
| C3 | Modificación del art. 7.ñ) | `G6` l.240: «Una modificación posterior del art. 7.ñ) figura con vigencia **23-oct-2026** (BOE-A-2026-20528)» | BOE consolidado, art. 7: «Se modifica la **letra x)** por la disposición final 8 de la Ley 4/2026, de 1 de octubre. Ref. BOE-A-2026-20528» | **BOE**. La letra ñ) de esa versión es idéntica a la vigente. |
| C4 | Edad para el 8 % de las rentas vitalicias | `G12` l.99: «**70 o más: 8 %**» | `G6` l.213: «8 % (**más de 70**)… deja sin cubrir exactamente 70 años»; BOE art. 25.3.a) 2.º: «cuando el perceptor tenga **más de 70 años**» | **G6 y BOE** (literal). G12 completa el hueco de los 70 años exactos sin fuente. |
| C5 | Tramos de la tarifa general y del ahorro | `G12` l.64: «Los tramos intermedios… **salen de mi conocimiento previo**… [VERIFICAR en el BOE]»; l.75: «**no he vuelto a abrir esos artículos**» | `G6` l.151: «leída hoy, **confirma la tabla de G12 §1.4**»; `G10` l.131; `G11` l.290; `G7` l.284 | **BOE** (arts. 63 y 66, leídos hoy: coinciden). G12 no se ha actualizado y sigue siendo la referencia que citan las demás. |
| C6 | Mínimo personal de 5.550 € | `G11` l.263: «art. 57, **no releído hoy**; supuesto»; `G12` l.53: «[VERIFICAR] en el texto de los arts. 57-60» | BOE, art. 57.1: «será, con carácter general, de 5.550 euros anuales» | **BOE**. Los dos [VERIFICAR] sobran para el art. 57. |
| C7 | Reglamento (UE) 2020/1503 | `G10` l.184: «(resumen de búsqueda, **no abierto**) [VERIFICAR]» | `G11` l.196: «**[VERIFICADO 13-oct**, texto del DOUE de 20-oct-2020]» | Las cifras coinciden (5 M€ y 4 días), pero el estado de la verificación no. Esta auditoría tampoco ha podido abrir el texto (§5). |
| C8 | Régimen español del crowdfunding | `G11` l.194: «la ley española **se limita a remitir** al Reglamento… y a designar a la CNMV… (arts. 46-49)» | `G10` l.183: arts. 46-56, «plataformas no armonizadas (art. 55) y agrupación de inversores (art. 56)»; BOE, Ley 5/2015: arts. 46-56 vigentes desde el 10-nov-2022 | **G10 y BOE**. El Título V incluye también fichas (arts. 51-52), sanciones (arts. 53-54), plataformas no armonizadas (art. 55) y agrupación de inversores (art. 56). |
| C9 | Límite de 8.500 € | `G12` l.13: «(**8.500 €** adicionales si los aporta la empresa…)» | `G12` l.189 y `G6` l.65-77: incremento «**no automático**», ligado a una tabla y que también puede venir de aportaciones del trabajador al mismo instrumento | **G6 y el BOE (art. 52.1.1.º)**. El resumen de G12 se quedó con la versión simplificada. |
| C10 | SIALP: plazo de 5 años | `G13` l.185: «art. 7.ñ) [VERIFICAR el plazo de 5 años y requisitos]» | `G6` l.235 y BOE art. 7.ñ): «antes de finalizar el plazo de cinco años desde su apertura» | **BOE**. El [VERIFICAR] de G13 ya se puede quitar. |
| C11 | Estado de las guías | `G7` l.394: «**G6**… pendiente»; `G13` l.17: «(G6, **pendiente**)»; `G8` l.221: «Ver G7 (pendiente)»; `G5` l.285: «Pendientes de la serie: G6, G7, G10, G11 y G13-G15»; `G11` l.356: «G10 (guía paralela, **no consultada**)»; `G12` l.152: «en la **futura** G9»; `MAPA` l.24: «(…; **pendientes**)» | `MAPA` l.30-44: las 15 guías aparecen «✅ hecha» | **MAPA** (tabla). Son remisiones obsoletas, y el encabezado del propio MAPA (l.24) también lo está. |
| C12 | Fecha de la derogación del RDL 16/2025 | `G6` l.314: «se derogó el **28-ene-2026**» | `G10` l.93: «acuerdos del Congreso (**27-ene** y 26-feb-2026)» | **No es una contradicción**. La resolución es del 27-ene y se publicó el 28-ene (BOE-A-2026-2024). Conviene precisar cuál de las dos fechas se usa. |
| C13 | Pérdida total en una startup | `G11` l.272: «sin otras ganancias, **0 € de ahorro fiscal ese año**» | `G11` l.248 y art. 49 LIRPF: el saldo negativo se compensa con hasta el 25 % de los rendimientos del capital mobiliario del año | **Art. 49**. La tabla solo es cierta si además no hay intereses ni dividendos. Es una contradicción dentro de G11. |

## 2. Verificación de datos clave (BOE, consulta del 13-oct-2026)

| # | Dato | Guía y línea | Valor del documento | Valor en la fuente primaria (artículo y URL) | ¿Correcto? |
|---|---|---|---|---|---|
| V1 | Límite de aportación a planes de pensiones | G6 l.7, l.64-68; G12 l.188-191 | Menor entre el 30 % y 1.500 €; +8.500 €; +4.250 €; máximo de ambos incrementos 8.500 € | Art. 52.1 LIRPF (versión desde 1-ene-2023, Ley 31/2022): exactamente así; los dos incrementos juntos no pasan de 8.500 € ([BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764)) | **Sí** |
| V2 | Tabla de la aportación del trabajador | G6 l.72-75 | ×2,5 hasta 500 €; 1.250 € + 0,25 × (C − 500) entre 500,01 y 1.500 €; ×1 por encima; ×1 con más de 60.000 € | Art. 52.1.1.º: idéntico | **Sí** |
| V3 | Límite de 1.500 € individual por partícipe (RDL 1/2002) | G6 l.79 | Art. 5.3.b): por partícipe de la unidad familiar | Art. 5.3.a) y b) RDLeg 1/2002 ([BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2002-24252)) | **Sí** |
| V4 | Cónyuge: 1.000 € si gana menos de 8.000 €; sin ISD | G6 l.8, l.91, l.183; G12 l.192 | 1.000 €; < 8.000 €; no sujeto a Sucesiones | Art. 51.7 LIRPF: literal, con «no estarán sujetas al Impuesto sobre Sucesiones y Donaciones» | **Sí** |
| V5 | Discapacidad: 10.000 € y 24.250 € | G6 l.92-95 | 10.000 / 24.250 / 5 ejercicios | Art. 53.1 a), b) y c) LIRPF | **Sí** |
| V6 | Multa por exceso | G6 l.9, l.100 | 50 % si no se retira antes del 30-jun del año siguiente | Art. 36.5 RDLeg 1/2002: «multa equivalente al 50 por ciento de dicho exceso» | **Sí** |
| V7 | Liquidez a 10 años y DT 7.ª | G6 l.10, l.121-125 [VERIFICADO] | Aportaciones hasta 31-dic-2015 disponibles desde 1-ene-2025 | Art. 8.8 y DT 7.ª RDLeg 1/2002: literal | **Sí** |
| V8 | Jubilación anticipable desde los 60 | G6 l.111 | «anticipable desde 60 años» | Art. 8.6 RDLeg 1/2002: «a partir de los sesenta años de edad, en los términos que se establezcan reglamentariamente» | **Sí** |
| V9 | Comisiones máximas de los planes | G6 l.15, l.250-256 | 0,85 / 1,30 / 1,50 %; depósito 0,20 %; alternativa 1 % + 9 %; garantía externa 1,50 % | Art. 84.1.b), d) y 84.2 del RD 304/2004 (versión de 21-jul-2023) ([BOE-A-2004-3453](https://www.boe.es/buscar/act.php?id=BOE-A-2004-3453)) | **Sí** |
| V10 | Promoción pública (PPES): < 0,30 % y < 0,10 % | G6 l.244, l.258 | < 0,30 % de gestión; < 0,10 % de depósito | Art. 107 del RD 304/2004: «inferiores al 0,30 por ciento»; «inferiores al 0,10 por ciento» | **Sí** |
| V11 | Exención del PIAS | G6 l.12, l.207 | Art. 7.v): al constituir la renta vitalicia | Art. 7.v) LIRPF: «rentas que se pongan de manifiesto en el momento de la constitución de rentas vitalicias aseguradas» de los PIAS | **Sí** |
| V12 | Requisitos del PIAS | G6 l.200-206 | 8.000 €/año, 240.000 € en total, primera prima con más de 5 años | DA 3.ª, letras c), d), g) y h) LIRPF | **Sí** |
| V13 | Régimen transitorio de la DT 12.ª | G6 l.148 | Reducción del «texto refundido de 2006»; 40 % [VERIFICAR]; contingencia del año + 2 | DT 12.ª.2 y 4 LIRPF: el «texto refundido… vigente a 31 de diciembre de 2006» (RDLeg 3/2004); el plazo es correcto. El art. 17.2.b) del RDLeg 3/2004 (texto original, [BOE-A-2004-4347](https://www.boe.es/buscar/doc.php?id=BOE-A-2004-4347)) da «el 40 por ciento… que se perciban en forma de capital, siempre que hayan transcurrido más de dos años desde la primera aportación» | **Plazo correcto**; el 40 % **se puede verificar** y **faltan las condiciones** |
| V14 | Porcentajes de las rentas vitalicias | G6 l.213; G12 l.99 | 40 / 35 / 28 / 24 / 20 / 8 % | Art. 25.3.a) 2.º: «8 por ciento, cuando el perceptor tenga **más de 70 años**» | G6 **sí**; G12 «70 o más» **no es literal** |
| V15 | Reducción del 30 % del art. 18.3 | G6 l.146 | Solo para el art. 17.2.a) 1.ª y 2.ª | Art. 18.3 LIRPF: literal | **Sí** |
| V16 | Edad de jubilación y cuantía en 2026 | G6 l.17, l.304-306, l.317 | 65 con 38 años y 3 meses o 66 años y 10 meses; 50 % + 0,19 % / 0,18 %; tope en el mes 248 | DT 7.ª LGSS (fila de 2026) y art. 210.1 ([BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724)) | **Sí** |
| V17 | Pensión máxima, revalorización y base máxima de 2026 | G6 l.309-311 | 3.359,60 €/mes (47.034,40 €); 2,7 %; 5.101,20 € | RDL 3/2026 ([BOE-A-2026-2548](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-2548)): literal | **Sí** |
| V18 | Cuotas del RETA en 2026 | G10 l.11, l.68-78 [VERIFICADO] | 28,30 + 1,30 + 0,90 + 0,90 + 0,10 = 31,50 %; 15 tramos de 653,59 € a 5.101,20 € | Orden PJC/297/2026, art. 18 (tabla y tipos) y tipos de cese (0,90 %) y FP (0,10 %) ([BOE-A-2026-7296](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7296)); la tabla coincide fila por fila | **Sí** |
| V19 | Tarifa plana | G10 l.83-84, l.242 | 80 € en 2023-2025; 2026 sin confirmar | Art. 38 ter LETA: la cuantía «se establecerá en la respectiva Ley de Presupuestos»; nota del BOE: 80 € en 2023-2025 (DT 5.ª RDL 13/2022). La Orden de 2026 no la fija | **Sí** (falta añadir que depende de los Presupuestos) |
| V20 | Verifactu | G10 l.14, l.100 [VERIFICADO] | Antes del 1-ene-2027 (IS) y del 1-jul-2027 (resto) | DF 4.ª RD 1007/2023, modificada por el RDL 15/2025 ([BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840)). En los sumarios del 6 al 13-oct no hay ninguna norma nueva | **Sí** (el aplazamiento a 2028 sigue sin estar en el BOE) |
| V21 | Factura electrónica B2B | G10 l.14, l.101 [VERIFICADO] | 6-oct-2027 (más de 8 M€) y 6-oct-2028 | RD 238/2026, DF 4.ª: 12 y 24 meses desde la entrada en vigor de la orden; Orden HAC/1028/2026 (BOE 5-oct) «entrará en vigor el día siguiente» | **Sí** |
| V22 | IS 2026 | G10 l.15, l.116-121 [VERIFICADO] | 25 %; micro 19/21 %; ERD 23 / 22 / 21 %; nueva creación 15 % | Art. 29.1 y DT 44.ª LIS (Ley 7/2024) ([BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328)) | **Sí** |
| V23 | Plazo de pago a proveedores | G10 l.17, l.189 [VERIFICADO] | 30 días, hasta 60 por pacto; factura en 15 días; BCE + 8 puntos; 40 € | Arts. 4.1, 7.2 y 8.1 de la Ley 3/2004 (versión de la **Ley 11/2013**, BOE-A-2013-8187) | **Sí** (el «presumiblemente Ley 11/2013» queda confirmado) |
| V24 | SL, SA, cuentas abreviadas y auditoría | G10 l.10, l.39-40, l.50-53 [VERIFICADO] | SL 1 €, regla de los 3.000 €; SA 60.000 €; 4 / 8 M€ y 50 trabajadores; 2,85 / 5,7 M€; SLNE derogada | Arts. 4, 257 y 263 LSC; título XII y art. 434 «derogado por el art. 2.6 de la Ley 18/2022» | **Sí** |
| V25 | Autónomo societario y deducción del 7 % / 3 % | G10 l.67, l.80 [VERIFICADO] | 1/3, 1/4 con dirección, 50 % entre familiares; 7 % y 3 % | Arts. 305.2.b) y 308.1.c) LGSS | **Sí** |
| V26 | Exoneración del pasivo y avalistas | G10 l.19, l.231-232 [VERIFICADO] | Crédito público hasta 10.000 € (5.000 € íntegros); el aval sobrevive; plan de 3 o 5 años | Arts. 489.1.5.º, 492.1 y 497 TRLC | **Sí** |
| V27 | IRPF del autónomo | G10 l.85, l.92, l.94-95 [VERIFICADO] | 20 % de inicio; simplificada hasta 600.000 €; 5 % con tope de 2.000 €; retención del 15 % / 7 %; pago fraccionado del 20 % / 4-3-2 % | Arts. 30.1, 30.2.4.ª y 32.3 LIRPF; arts. 30.2.ª, 95.1 y 110 RIRPF | **Sí** |
| V28 | Módulos | G10 l.13, l.93 | 250.000 € solo en 2016-2024; RDL 16/2025 y RDL 2/2026 sin efecto | DT 32.ª LIRPF y sus notas (Resoluciones de 27-ene-2026 y 26-feb-2026) | **Sí** |
| V29 | SMI 2026 | G10 l.241 [VERIFICADO] | 1.221 €/mes; 40,70 €/día | RD 126/2026, art. 1 | **Sí** |
| V30 | Art. 68.1 LIRPF | G11 l.11, l.226-241; G10 l.214 [VERIFICADO] | 50 %, 100.000 €; antes 30 % y 60.000 €; 5 o 7 años; más de 3 y menos de 12 años; 40 %; ≤ 400.000 €; sin mercado regulado ni SMN | Art. 68.1 (versión de 8-oct-2026; el apartado 1 no cambia desde el 1-ene-2023). Historial: 20 % / 50.000 € (2015), 30 % / 60.000 € (5-jul-2018), 50 % / 100.000 € (2023) | **Sí** (G12 l.206, **no**) |
| V31 | Ley 28/2022 | G11 l.12, l.163-181 [VERIFICADO] | 5 o 7 años; 60 % de la plantilla; ENISA en 3 meses con silencio positivo; IS del 15 % durante 4 periodos; 10 M€; 3 años sin disolución por pérdidas | Arts. 3.1, 4.2, 4.3.i), 6, 7, 8 y 13 ([BOE-A-2022-21739](https://www.boe.es/buscar/act.php?id=BOE-A-2022-21739)) | **Sí** |
| V32 | Stock options en empresas emergentes | G11 l.180-181 | 50.000 € frente a 12.000 €; imputación del exceso; 10 años | Arts. 42.3.f) y 14.2.m) LIRPF | **Sí** |
| V33 | Capital riesgo para no profesionales | G11 l.13, l.185-189 [VERIFICADO] | a) 100.000 € con declaración escrita, o b) asesoramiento, 10.000 € y 10 % si el patrimonio es ≤ 500.000 € | Art. 75.2 Ley 22/2014 (versión de 7-abr-2023) ([BOE-A-2014-11714](https://www.boe.es/buscar/act.php?id=BOE-A-2014-11714)) | **Sí** |
| V34 | Objeto de las ECR y exención en el IS | G11 l.46, l.154, l.254 [VERIFICADO] | Art. 9.1; exención del 99 % entre el año 2 y el 15 (ampliable al 20) | Art. 9.1 Ley 22/2014; art. 50.1 LIS | **Sí** |
| V35 | Regla de recompra | G11 l.250; G10 l.217; G7 l.291 | Letra f): 2 meses para cotizados; letra g): 1 año para no cotizados; letra e): 1 año | Art. 33.5 e), f) y g) LIRPF | **Sí** |
| V36 | Derivados como ganancia patrimonial y retenciones | G7 l.282, l.285 | Art. 37.1.m); art. 75.1.d) RIRPF sin derivados | Art. 37.1.m) LIRPF: literal. Art. 75.1.d) RIRPF: IIC, aprovechamientos forestales y derechos de suscripción | **Sí** |
| V37 | Límites a los CFD (CNMV 2019) | G7 l.11, l.157-168 | 30:1 a 2:1; 3,33 / 5 / 10 / 20 / 50 %; BOE n.º 155 del 29-jun-2019; en vigor el 2-jul y el 1-ago-2019 | Resolución CNMV de 27-jun-2019, anexo I y fechas de entrada en vigor ([BOE-A-2019-9737](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2019-9737)); aviso «cada tres meses» sobre 12 meses | **Sí** |
| V38 | Resolución de la CNMV de 2023 | G7 l.13, l.90, l.173-177 | 11-jul-2023, BOE del 14-jul, aplicable desde el 3-ago; parte segunda con margen y cierre al 50 % | BOE-A-2023-16394: publicada el 14-jul; «aplicable a los veinte días»; garantía inicial = el **menor** de dos importes (mínimo exigido) | Fechas **sí**; **margen mal descrito** (C2) |
| V39 | Circulares 1/2018 y 1/2022 | G7 l.13, l.202, l.208-209 | 1/2018 vigente desde el 27-jun-2018; 1/2022 derogada el 28-dic-2024 | Metadatos del BOE: Circular 1/2018 con vigencia desde 20180627 y sin derogar; Circular 1/2022 con «fecha_derogacion 20241228» | **Sí** |
| V40 | Escalas de los arts. 63 y 66 | G6 l.151; G10 l.131; G11 l.265, l.290; G7 l.284 | 9,5 / 12 / 15 / 18,5 / 22,5 / 24,5 %; ahorro 9,5 / 10,5 / 11,5 / 13,5 / 15 % | Arts. 63 (vigente desde 1-ene-2021) y 66 (vigente desde 22-dic-2024): cuotas 1.182,75 / 2.112,75 / 4.362,75 / 8.950,75 / 62.950,75 € | **Sí** |
| V41 | Patrimonio y Sucesiones | G6 l.189-193; G10 l.212-213; G11 l.286-287 | Planes exentos (art. 4.Cinco); seguros por su valor de rescate (art. 17.Uno); 9.195,49 €; 95 % y 10 años | Ley 19/1991, arts. 4.Cinco y 17.Uno; Ley 29/1987, art. 20.2.b), c) y 20.6 | **Sí** |

**Marcas [VERIFICADO] comprobadas una a una (24):**
- **G10:** l.10, l.11, l.15, l.19, l.39, l.40, l.42, l.67, l.83, l.85, l.94, l.95, l.100, l.101, l.189, l.231 y l.241.
- **G11:** l.46, l.154, l.163, l.183 y l.221.
- **G6:** l.121.
- **G12:** l.206.

Resultado: **23 correctas** y **1 incorrecta** (G12 l.206).

## 3. Calidad

### 3.1 Frases que pueden leerse como recomendación
No hay recomendaciones explícitas. Todas las guías llevan el aviso y cierran comparaciones con «No se concluye cuál es mejor» (G10 l.166) o «La tabla describe condiciones» (G6 l.298). Quedan tres matices menores:

| Archivo y línea | Texto literal | Problema |
|---|---|---|
| G7 l.184 | «por eso el CFD está diseñado para posiciones **cortas en el tiempo**» | Atribuye una finalidad al producto que se lee como pauta de uso. Basta con describir el coste. |
| G7 l.238 | «abrir una posición corta en derivados es una forma de cobertura que **tiene los mismos riesgos de margen**… No es una sugerencia, es descripción.» | Presenta una estrategia concreta para la cartera de Joel. El aviso la neutraliza en parte; es aceptable. |
| G6 l.336 | «Los regalos de bienvenida **suelen compensar** costes o permanencia» | Generaliza sin dato ni fuente, con tono de advertencia. |

### 3.2 Causalidad no demostrada y etiquetas
- **G7 l.357:** «Un VIX que sube bruscamente → Mayor probabilidad de saltos y llamadas de margen». Afirma una relación sin medirla.
- **G7 l.229:** «las liquidaciones empujan el precio». Es la mecánica habitual, pero la cifra de prensa que la acompaña está sin verificar (ya va marcada).
- **G10 l.235:** «[ESPECULACIÓN: su peso depende de cada caso]» está **mal puesta**: la frase describe un riesgo (concentración en el negocio propio), no hace una previsión.
- **G11 l.212:** el título de la sección dice «[VERIFICADO 13-oct…]», pero dentro (l.213 y l.218) hay datos [VERIFICAR]. La marca del título promete más de lo que hay.

### 3.3 Cifras sin fuente o con remisión dudosa
- **G6 l.15, l.102 y l.259** («No son 1,25 %/0,85 %», «las cifras… que figuraban **en otro documento**», «Cifra del 6 %»): remiten a un documento que no está en el repositorio (no aparece en ningún `.md`). Para quien lea, son correcciones a un encargo invisible.
- **G6 l.3:** usa «RDL» tanto para Reales Decretos **Legislativos** (1/2002, 8/2015) como para Reales Decretos-ley (3/2026, 29/2026). Se presta a confundir el rango de las normas, por ejemplo al hablar de convalidación.
- **G11 l.340:** «tributación distinta, ver G12 **y G13**». G13 no trata la fiscalidad de los tokens; el tema está en G12 §3 y en el dossier 13.
- **G10 l.17:** «(§5.7)». Esa sección no existe; la morosidad está en §5.6.
- **G11 l.74:** la numeración salta de §3.3 a §3.5 (no hay §3.4).
- **G7 l.157:** fecha las medidas de ESMA en el 23 y el 27-mar-2018. Según la propia Resolución de 2019, las decisiones formales se adoptaron el **22-may-2018** y se aplicaron desde el **2-jul-2018** (opciones binarias) y el **1-ago-2018** (CFD).

### 3.4 Recálculo de los ejemplos numéricos

| Guía | Ejemplo | Resultado del documento | Mi recálculo | ¿Cuadra? |
|---|---|---|---|---|
| G6 §2.1 | Tope del trabajador con contribución de 400 / 1.000 / 2.000 € | 1.000 / 1.375 / 2.000 € | Igual | Sí |
| G6 §4.3 ej. 1 | Ahorro por aportar 1.500 € (del 19 % al 45 %); comprobación con G12 | 285 a 675 €; 5.661 €; diferencia de 450 € | Igual (T(28.500) = 6.715,50 − 1.054,50) | Sí |
| G6 §4.3 ej. 1 | Cruce de tramos de 21.000 a 19.500 € | 408 € (27,2 %) | 240 + 168 = 408 | Sí |
| G6 §4.3 ej. 2 | Plan frente a fondo al 4 % durante 20 años; netos según el tipo; punto de igualdad; con costes | 3.286,68 / 2.300,68 / 2.063,05; 2.662,21 … 1.807,68; 37,2 %; 2.816,34 / 1.992,67; 29,2 % | 3.286,68 / 2.300,68 / 2.063,05; igual; 37,23 %; 2.816,34 / 1.992,67; 29,25 % | Sí |
| G6 §4.3 ej. 3 | Rescatar 30.000 € en un año o en tres | 10.736 € (35,8 %) frente a 10.008 € (33,4 %); 728 € | 10.736 / 10.008 | Sí |
| G6 §5.1 | PIAS de 6.000 € al año durante 10 años al 3 %; impuesto si se rescata a capital | 68.783,28 €; 8.783,28 €; 1.724,49 € | Igual | Sí |
| G6 §5.1 | Renta de 4.000 € constituida a los 66 años | 800 € → 152 € | Igual | Sí |
| G6 §5.3 | Seguro de ahorro | 3.000 → 570 € | Igual | Sí |
| G6 §7.3 | 10.000 € al 5 % durante 20 años con costes del 1,50 / 0,85 / 0,20 % | 19.897,89 / 22.552,02 / 25.540,28; 5.642,39 (28,4 %) | Igual; 28,36 % | Sí |
| G6 §9.2 | Pensión con 30 años cotizados; 100 % con 37 años | 84,2 % → 2.105 €; 100 % | 50 + 34,2 = 84,2 %; 50 + 47,12 + 2,88 = 100 % | Sí |
| G7 §3.3 | Futuro 10:1: −2 / −10 / −15 %; llamada de margen; secuencia de dos días | ±1.000; −5.000; −7.500; −3 %; 4.250 → 3.265; 1.735 € | Igual | Sí |
| G7 §4.4-4.5 | Valor intrínseco y temporal; call con prima de 5 €; vendedor a 400 €; put con prima de 4 € | 3 / 3; −500 … +9.500 (+1.900 %); 29.500; +600 / +9.600 / −400 | Igual | Sí |
| G7 §5.4 | Financiación de un CFD de 20.000 € al 5,5 % (base 360) | 3,06 €/día; 1.100 € (110 % del margen) | 3,0556 × 360 = 1.100 | Sí |
| G7 §5.5 | Cierre forzoso con −2,5 %; salto de −7 % | −500 €; −1.400 € (pérdida de 1.000 € con protección) | Igual | Sí |
| G7 §6.2 / §6.4 | Funding del 0,01 % cada 8 h; liquidación al 0,5 %; CFD cripto 2:1 | 1.095 USD (109,5 %); −9,5 %; −25 % | Igual | Sí |
| G7 §7.3 | ETF apalancados, casos A-E; arrastre L(L−1)/2·σ² | 98,18 / 96 / 144 / 94,55 / 98,18; 4 / 25 / 12 % | Igual | Sí |
| G7 §8.2 | Compensación: −5.000 € con 2.000 € de rendimientos del capital mobiliario; +5.000 € | 500; 1.500 → 285 €; arrastre de 4.500; 950 € | Igual | Sí |
| G10 §2.3 | DIRCE | 54,4 / 40,7 / 4,9 %; suma de 3.310.824 | Igual | Sí |
| G10 tabla del RETA | Cuotas con la base mínima (× 31,5 %) | 205,88 … 607,35; 1.606,88 € | Igual en los 15 tramos | Sí |
| G10 §3.6 ej. A | Autónomo con 60.000 € de ingresos y 18.000 € de gastos | 5.435,28 + 7.531,94 = 12.967,22 € | 5.435,28 + 7.531,95 = 12.967,23 € (sin redondeo intermedio) | Sí (1 céntimo) |
| G10 §4.5 B1 / B2 | SL con 30.000 € de salario; con y sin dividendos | 11.379,56 / 20.900,44; 13.390,90 / 28.009,10; +423,68 € | Igual (base del tramo 7 / tramo 8; 3.162,20 €/mes) | Sí |
| G10 §5.4 | Factoring | 105,21 + 100 = 205,21 €; 1,28 %; 7,8 % | Igual | Sí |
| G10 §5.6 | Demora con tipo hipotético del 10 % | 149,59 € | Igual | Sí |
| G10 §6.4 | Crowdlending | −13,6 %; 7,4 %; 13,8 % | Igual | Sí |
| G10 §6.6 | Pérdida de 20.000 € | 750; 13.250; 427,50 frente a 570 € (142,50 €) | Igual | Sí |
| G11 §3.2 | SAFE con cap y descuento; préstamo convertible | 1,00 % / 1,5625 %; 3.750 €; 6.718,75 acciones | Igual | Sí |
| G11 §3.5 | Rondas, dilución y down round; anti-dilución | 4 / 12 / 24 €; 0,75 / 0,60 %; 4,80 €; 10,56 € (1,1364); full ratchet 2,5 | Igual | Sí |
| G11 §3.6 | Preferencia no participativa y participativa | 0 / 50.000 / 150.000 / 300.000 €; 37.500 / 112.500 / 262.500 € | Igual | Sí |
| G11 §3.7 | Comisiones de un fondo | 1,48x | Igual | Sí |
| G11 §4.2 | Cartera de 20 startups; TIR; probabilidad | 145.000 € (1,45x); 69 %; 4,75 % / 17,0 % / 7,2 %; 15 % | 4,754 % / 16,99 % / 7,18 %; 15 % | Sí |
| G11 §6.5 | Cuota estatal con base de 60.000 y de 40.000 €; escenarios | 8.423,50 / 4.723,50 € (276,50 € sin aplicar); −5.000 / −3.020 / +5.000 / +20.920 € | Igual | Sí (con el matiz de C13) |

## 4. Correcciones propuestas, por prioridad (texto exacto: antes → después)

### ALTA
| # | Archivo y línea | Texto actual (literal) | Texto propuesto | Fuente |
|---|---|---|---|---|
| A1 | `2026-10-10-G12-fiscalidad-completa.md` l.206 | «- **Ley 28/2022 de startups:** deducción del **50 %** de hasta **100.000 €** invertidos al año en empresas emergentes certificadas; mantener las participaciones **más de 3 años y menos de 12**» | «- **Art. 68.1 LIRPF (redacción de la Ley 28/2022, desde el 1-ene-2023):** deducción del **50 %** de hasta **100.000 €** suscritos al año en **empresas de nueva o reciente creación** (SA, SL, SAL o SLL no cotizadas ni en mercado regulado ni en SMN, con actividad económica y fondos propios ≤ 400.000 €). **No hace falta que sea una empresa emergente certificada**: a las emergentes de la Ley 28/2022 solo se les amplía el plazo de suscripción de 5 a 7 años desde la constitución y sus socios fundadores no tienen el límite del 40 %. Hay que mantener las participaciones **más de 3 años y menos de 12**» (el resto de la línea, entre corchetes, se mantiene) | [BOE, art. 68.1.2.º y 3.º](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) |
| A2 | `2026-10-13-G7-derivados-y-apalancamiento.md` l.90 | «y un margen inicial **no superior al menor entre el de 2019 y el del mercado** [VERIFICAR texto]» | «y una **garantía inicial mínima** igual al **menor** de dos importes: el porcentaje de la Resolución de 2019 para ese subyacente o el que exija el centro de negociación. Si el subyacente es un criptoactivo que no es instrumento financiero MiFID, no puede ser inferior al de 2019 (Resolución CNMV de 11-jul-2023, parte segunda, BOE-A-2023-16394) [VERIFICADO 13-oct]» | [BOE-A-2023-16394](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-16394) |

### MEDIA
| # | Archivo y línea | Texto actual (literal) | Texto propuesto | Fuente |
|---|---|---|---|---|
| M1 | G6 l.240 | «- Una modificación posterior del art. 7.ñ) figura con vigencia **23-oct-2026** (BOE-A-2026-20528); su contenido literal aún no sustituye al vigente.» | «- La versión del art. 7 con vigencia **23-oct-2026** (BOE-A-2026-20528, Ley 4/2026, DF 8.ª) modifica la **letra x)**, no la ñ): el texto de la ñ) (exención si no se dispone antes de 5 años) no cambia.» | BOE consolidado, art. 7 (nota de modificación) |
| M2 | G6 l.148 | «el beneficiario puede aplicar la **reducción del art. 17 del texto refundido de 2006** (la cifra de **40 %** viene de esa norma antigua, **no leída hoy [VERIFICAR]**)» | «el beneficiario puede aplicar la **reducción del art. 17 del texto refundido de la Ley del IRPF (RDLeg 3/2004) vigente a 31-dic-2006**: un **40 %** para las prestaciones **en forma de capital**, siempre que hayan pasado **más de dos años desde la primera aportación** (sin ese plazo en invalidez) (art. 17.2.b) del texto original, BOE-A-2004-4347; redacción exacta a 31-dic-2006 [VERIFICAR])» | DT 12.ª LIRPF; [RDLeg 3/2004](https://www.boe.es/buscar/doc.php?id=BOE-A-2004-4347) |
| M2b | G6 l.360 | «- **40 % de reducción** de la DT 12.ª: viene del texto de 2006, no leído **[VERIFICAR]**.» | «- **40 % de reducción** de la DT 12.ª: confirmado en el art. 17.2.b) del RDLeg 3/2004 (texto original: solo en forma de capital y con más de 2 años desde la primera aportación); falta comprobar la redacción exacta a 31-dic-2006 [VERIFICAR].» | Ídem |
| M3 | G12 l.64 | «- **BOE leído hoy:** el art. 63 empieza en el 9,5 % hasta 12.450 € y llega al 24,5 % por encima de 300.000 €. Los tramos intermedios (20.200, 35.200 y 60.000 €) y los tipos del 12, 15, 18,5 y 22,5 % **salen de mi conocimiento previo**, no de la lectura de hoy [VERIFICAR en el BOE].» | «- **Verificado en el BOE (13-oct-2026, art. 63, vigente desde el 1-ene-2021):** tramos de 12.450 / 20.200 / 35.200 / 60.000 / 300.000 €, tipos estatales del 9,5 / 12 / 15 / 18,5 / 22,5 / 24,5 % y cuotas íntegras de 1.182,75 / 2.112,75 / 4.362,75 / 8.950,75 / 62.950,75 €.» | BOE, art. 63 |
| M3b | G12 l.75 | «Aquí **no he vuelto a abrir esos artículos** (la herramienta de hoy dio un resumen erróneo de «19 % fijo»; **lo descarto** porque contradice la lectura directa del día 9).» | «Verificado de nuevo en el BOE el 13-oct-2026 (art. 66, versión vigente desde el 22-dic-2024): escala estatal del 9,5 / 10,5 / 11,5 / 13,5 / 15 % con tramos de 6.000 / 50.000 / 200.000 / 300.000 €.» | BOE, art. 66 |
| M3c | G12 l.53 | «- **Aviso:** el extracto de la web del BOE se obtuvo con un resumen automático; los importes coinciden con los que yo conocía, pero [VERIFICAR] en el texto de los arts. 57-60.» | «- **Art. 57 verificado en el BOE (13-oct-2026)**: 5.550 €; +1.150 € con más de 65 años; +1.400 € adicionales con más de 75. Los arts. 58-60 [VERIFICAR].» | BOE, art. 57 |
| M4 | G7 l.394 | «- **G6** (planes de pensiones, PIAS y seguros de ahorro): pendiente.» | «- [G6](2026-10-13-G6-pensiones-pias-seguros-ahorro.md) (planes de pensiones, PIAS y seguros de ahorro).» | MAPA l.35 |
| M4b | G13 l.17 | «los planes de pensiones tendrán su guía (G6, **pendiente**) (§7).» | «los planes de pensiones tienen su guía ([G6](2026-10-13-G6-pensiones-pias-seguros-ahorro.md)) (§7).» | MAPA l.35 |
| M4c | G8 l.221 | «Ver G7 (pendiente).» | «Ver [G7](2026-10-13-G7-derivados-y-apalancamiento.md).» | MAPA l.36 |
| M4d | G5 l.285 | «- Pendientes de la serie: G6, G7, G10, G11 y G13-G15 (ver [MAPA](MAPA.md)).» | «- Serie G1-G15 completa (ver [MAPA](MAPA.md)).» | MAPA l.30-44 |
| M4e | G11 l.356 | «**G10** (guía paralela, no consultada)» | «**[G10](2026-10-13-G10-pymes-y-autonomos.md)** (pymes y autónomos; su §6.5 resume la misma deducción)» | MAPA l.39 |
| M4f | G12 l.152 | «- Detalle de productos y riesgos, en la futura G9.» | «- Detalle de productos y riesgos, en la [G9](2026-10-13-G9-commodities.md).» | MAPA l.38 |
| M4g | MAPA l.24 | «## Serie «Guías» (educativas, para tener contexto antes de una gestión patrimonial; pendientes)» | «## Serie «Guías» (educativas, para tener contexto antes de una gestión patrimonial; serie completa a 13-oct-2026)» | MAPA l.30-44 |

### BAJA
| # | Archivo y línea | Texto actual (literal) | Texto propuesto | Fuente |
|---|---|---|---|---|
| B1 | G12 l.99 | «**70 o más: 8 %**» | «**más de 70: 8 %** (literal del BOE; la ley no menciona los 70 años exactos)» | Art. 25.3.a) 2.º |
| B2 | G12 l.13 | «(**8.500 €** adicionales si los aporta la empresa; tope conjunto 10.000 €)» | «(hasta **8.500 €** adicionales por contribuciones de la empresa o aportaciones del trabajador al mismo plan de empleo, según la tabla del art. 52; tope conjunto de 10.000 €)» | Art. 52.1.1.º |
| B3 | G10 l.184 | «**Reglamento (UE) 2020/1503 (resumen de búsqueda, no abierto) [VERIFICAR]**:» | «**Reglamento (UE) 2020/1503 (detalle en G11 §5.3; texto del DOUE leído en G11, no en esta guía)**:» | G11 l.196-206 |
| B4 | G11 l.194 | «ahora la ley española se limita a remitir al **Reglamento (UE) 2020/1503** y a designar a la **CNMV** como autoridad competente y de registro (arts. 46-49 Ley 5/2015)» | «ahora la ley española remite al **Reglamento (UE) 2020/1503** para las plataformas armonizadas y designa a la **CNMV** como autoridad competente y de registro (arts. 46-49). También regula fichas de datos, infracciones y sanciones (arts. 50-54), las plataformas **no armonizadas** (art. 55) y la **agrupación de inversores** (art. 56)» | [BOE, Ley 5/2015, Título V](https://www.boe.es/buscar/act.php?id=BOE-A-2015-4607) |
| B5 | G10 l.17 | «**40 €** fijos (arts. 4, 7, 8 Ley 3/2004) (§5.7).» | «**40 €** fijos (arts. 4, 7, 8 Ley 3/2004) (§5.6).» | Estructura de G10 |
| B6 | G10 l.189 | «el régimen actual de 30 + 60 viene de reformas posteriores, presumiblemente la Ley 11/2013 **[VERIFICAR]**» | «la redacción vigente de los arts. 4 y 7 (30 días y hasta 60 por pacto) procede de la **Ley 11/2013** (BOE-A-2013-8187) [VERIFICADO 13-oct, BOE]» | BOE, Ley 3/2004 consolidada |
| B7 | G10 l.84 | «Para **2026 no figura en la Orden PJC/297/2026**; webs dan 80 € y otra 88,64 € **[VERIFICAR]**.» | «Para **2026**, el art. 38 ter remite la cuantía a la Ley de Presupuestos, y la Orden PJC/297/2026 no la fija; webs dan 80 € y otra 88,64 € **[VERIFICAR]**.» | Art. 38 ter LETA |
| B8 | G10 l.235 | «**[ESPECULACIÓN: su peso depende de cada caso]**» | «(su peso depende de cada caso; es una descripción del riesgo, no una previsión)» | Regla de etiquetas del CLAUDE.md |
| B9 | G11 l.251 | «**[VERIFICAR el tipo, 19 % según G12]**» | «al **19 %** (art. 90.1 RIRPF) [VERIFICADO 13-oct, BOE]» | RIRPF, art. 90.1 |
| B10 | G11 l.263 y l.351 | «(art. 57, **no releído hoy**; supuesto)» / «- Art. 57 LIRPF (mínimo personal): **asumido** en 5.550 €.» | «(art. 57.1 LIRPF, verificado en el BOE el 13-oct)» / «- Art. 57 LIRPF: 5.550 €, verificado en el BOE (13-oct).» | BOE, art. 57 |
| B11 | G11 l.272 | «**sin otras ganancias, 0 € de ahorro fiscal ese año** (se compensa en los 4 años siguientes: art. 49)» | «**sin otras ganancias ni rendimientos del capital mobiliario, 0 € de ahorro fiscal ese año**; si hay intereses o dividendos, se compensa hasta el 25 % de ellos (art. 49) y el resto en los 4 años siguientes» | Art. 49 LIRPF |
| B12 | G11 l.74 | «### 3.5 Ejemplo numérico de una ronda y de las diluciones» | Opcional: no renumerar, porque romperías las remisiones a §3.5 y §3.6. Basta con añadir bajo §3.3 la línea «(No hay §3.4.)» | — |
| B13 | G11 l.340 | «(MiCA, tributación distinta, ver G12 y G13)» | «(MiCA, tributación distinta, ver G12 §3 y el dossier 13)» | G12 §3; dossier 13 |
| B14 | G11 l.212 | «**[VERIFICADO 13-oct, texto del DOUE L 80 de 20-mar-2023]**» | «**[VERIFICADO 13-oct salvo los datos marcados [VERIFICAR] en esta sección; texto del DOUE L 80 de 20-mar-2023]**» | Coherencia interna |
| B15 | G13 l.185 | «[VERIFICAR el plazo de 5 años y requisitos]» | «(plazo de **5 años** desde la apertura, art. 7.ñ) LIRPF, verificado en el BOE el 13-oct; requisitos en G6 §5.4)» | BOE, art. 7.ñ) |
| B16 | G6 l.86 | «**No** se aplica al exceso sobre el máximo absoluto del art. 51.6 (RDL 1/2002 art. 5.3).» | «**No** se aplica a las aportaciones que excedan de los límites máximos del art. 51.6 (art. 52.2, último inciso; el art. 51.6 remite a los límites del art. 5.3 RDLeg 1/2002).» | Art. 52.2 LIRPF |
| B17 | G6 l.15 y l.259 | «depósito máx. **0,20 %**. No son 1,25 %/0,85 % (§7).» / «Las cifras de 1,25 % y 0,85 % que figuraban en otro documento **no coinciden** con el BOE leído, que dice **1,50 %** para el resto de fondos.» | «depósito máx. **0,20 %** (§7).» / «Algunas fuentes antiguas citan otros máximos; el art. 84 vigente (jul-2023) dice **1,50 %** para el resto de fondos.» | Art. 84 RD 304/2004 |
| B18 | G6 l.3 | «**RDL 1/2002** (texto refundido de la Ley de Planes y Fondos de Pensiones» y «**RDL 8/2015** (Ley General de la Seguridad Social» | «**RDLeg 1/2002** (texto refundido de la Ley de Planes y Fondos de Pensiones» y «**RDLeg 8/2015** (texto refundido de la Ley General de la Seguridad Social» | Rango de la norma |
| B19 | G6 l.213 | «(art. 25.3.a) 2.º; el texto literal deja sin cubrir exactamente 70 años **[VERIFICAR]**)» | «(art. 25.3.a) 2.º; el BOE dice «más de 70 años» y no menciona los 70 exactos [VERIFICADO 13-oct]; su aplicación a los 70 años [VERIFICAR con la AEAT])» | Art. 25.3.a) 2.º |
| B20 | G7 l.157 y l.168 | «(BOE nº 155, 29-jun-2019)» / «(actualizada trimestralmente, según el resumen de la Resolución de 2019 [VERIFICAR texto])» | «(BOE-A-2019-9737, BOE n.º 155, 29-jun-2019; las decisiones formales de ESMA son del 22-may-2018, aplicables desde el 2-jul-2018 a las opciones binarias y el 1-ago-2018 a los CFD)» / «(estimación cada tres meses sobre los 12 meses anteriores; Resolución CNMV de 27-jun-2019 [VERIFICADO 13-oct])» | [BOE-A-2019-9737](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2019-9737) |
| B21 | G7 l.184 | «Un CFD mantenido largo tiempo **paga un coste** equivalente a un préstamo caro; por eso el CFD está diseñado para posiciones **cortas en el tiempo**.» | «Un CFD mantenido largo tiempo **paga un coste** equivalente a un préstamo caro: el coste crece con cada día de tenencia.» | Regla de no recomendar |
| B22 | G7 l.357 y G6 l.336 | «\| Un VIX que **sube bruscamente** \| Mayor probabilidad de **saltos** y **llamadas de margen** \|» / «Los regalos de bienvenida suelen compensar costes o permanencia;» | «\| Un VIX que **sube bruscamente** \| Volatilidad implícita mayor; suele coincidir con más **saltos** y **llamadas de margen** (relación no medida en esta guía) \|» / «Los regalos de bienvenida pueden ir ligados a permanencia o a costes (condiciones de cada oferta; no medido en esta guía);» | Regla de causalidad |

## 5. Lo que no se ha podido verificar
- **Reglamento (UE) 2020/1503, ELTIF 2 (2023/606), MiCA (art. 2.4 y art. 4) y el Reglamento Delegado 2024/2759:** EUR-Lex dio una respuesta vacía y el PDF del DOUE en boe.es no se pudo convertir a texto. Las cifras de G11 (5 M€, 1.000 € o 5 %, 10 % del patrimonio neto, 4 días, 55 %, dos semanas, 150 personas y 1 M€) coinciden con lo que yo sabía, pero **no las he contrastado hoy**.
- **ESMA (27-mar-2018), FOGAIN (100.000 €), BIS (846 billones de $ y 21,8 billones de $) y FRED (VIX 14,84; mediana 17,09):** no consultados, o la consulta agotó el tiempo de espera.
- **Convalidación del RDL 29/2026:** en los sumarios del BOE del 7 al 13-oct no aparece. Las Cortes están disueltas desde el RD 806/2026 (BOE del 6-oct), y el mismo día 7-oct se publicó también el **RDL 28/2026**, que ninguna guía menciona. Sigue [VERIFICAR].
- **Aplazamiento de Verifactu a 2028:** no está en el BOE hasta el 13-oct.
- **Criterio fiscal de los derivados** (G7 §8.1): queda sin resolver si los CFD, el forex y los perpetuos van a la base del ahorro y qué pasa con la prima perdida de una opción comprada que vence sin ejercerse. Hay criterios administrativos que pueden llevarla a la **base general**. No se ha leído ninguna consulta de la DGT ni del TEAC y sigue [VERIFICAR]. Es el punto fiscal de G7 con más riesgo de error.
- **Datos de mercado y de sector:** INVERCO, SpainCap, Invest Europe, ENISA, DIRCE y demografía del INE, Correlation Ventures, BLS, ICO, el registro de plataformas de la CNMV y los datos del BCE sobre tipos a pymes. Solo se ha comprobado que la aritmética de las tablas cuadra (por ejemplo, la suma del DIRCE).
- **Cuantía de la tarifa plana en 2026, límites de módulos y del IVA simplificado en 2026, tipo de retención de los rescates de planes de pensiones y plazos de traspaso:** no constan en las normas leídas.
- **Redacción a 31-dic-2006 del art. 17.2.b) del RDLeg 3/2004:** solo se ha leído el texto original de 2004.
