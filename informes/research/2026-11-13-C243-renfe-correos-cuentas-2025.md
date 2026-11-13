---
tema: Empresas públicas: cuentas 2025 de Renfe y Correos leídas (C243, quinta pasada)
etiquetas: [españa, empresas-publicas, renfe, correos, adif, subvenciones, deuda]
actualizado: 2026-11-13
---
# C243 · Renfe y Correos 2025 en sus cuentas oficiales; Adif sigue sin leer

Lecturas del 12-nov-2026 con `pdftotext`. M€ = millones de euros. Datos en `explorador/espana-empresas.json` (Renfe y Correos pasan de nivel S a P).

## HECHOS

### Renfe-Operadora, cuentas consolidadas 2025 [P, PDF de grupo.renfe.com con informe de auditoría de la Intervención General del Estado, 441 páginas]
| Magnitud | 2025 | 2024 |
|---|---|---|
| Cifra de negocios | 2.207,0 M€ | 1.923,6 M€ |
| Subvenciones de explotación | 1.850,7 M€ | 1.999,8 M€ |
| Resultado de explotación | 114,2 M€ | 68,6 M€ |
| Resultado atribuido a la entidad dominante | 60,2 M€ | −2,9 M€ |
| Deudas con entidades de crédito (largo + corto) | 5.570,3 M€ | 4.989,9 M€ |
| Patrimonio neto | 2.350,2 M€ | 2.235,4 M€ |

- Detalle de las subvenciones (nota de la memoria): servicios competencia del Estado 1.372,7 M€ (Cercanías 493,4; Media Distancia 443,4; Ancho Métrico 148,7; abonos gratuitos del RD-ley 14/2022 271,7, frente a 452,9 en 2024; Abono Joven 15,6); servicios competencia de otra administración 411,2 M€; otras subvenciones 66,8 M€.
- Cálculo nuestro: las subvenciones equivalen al 84 % de la cifra de negocios y la deuda bancaria sube 580 M€ en el año.

### Grupo Correos, cuentas consolidadas 2025 [P, Informe Anual Integrado 2025, PDF enlazado desde correos.com, 370 páginas]
| Magnitud | 2025 | 2024 |
|---|---|---|
| Cifra de negocios | 2.076,5 M€ | 2.107,1 M€ |
| Compensación por el servicio postal universal | 334,5 M€ | 200,6 M€ |
| Compensación por servicios de interés económico general | 55,9 M€ | 0 |
| Resultado de explotación | 31,4 M€ | −581,0 M€ |
| Resultado consolidado | 11,2 M€ | −458,5 M€ |

- Gastos de personal 1.588,0 M€; 46.094 empleados (equivalentes a tiempo completo); inversiones 122,6 M€; «otras aportaciones de socios» en el balance: 200,0 M€ a 31-dic-2025 (0 un año antes); el grupo dice haber reducido su endeudamiento neto en 175,6 M€.
- Corrección: la cifra de prensa de marzo (14,4 M€ de beneficio, 1.658 M€ de negocio sin elecciones) era provisional y mide otra cosa; la consolidada es 11,2 M€.
- Cálculo nuestro: sin la compensación del servicio universal, el resultado de explotación de 2025 habría sido negativo.

### Adif y BOE
- [P] Las «Cuentas Anuales 2025 con informe de auditoría» de Adif (3,8 MB) y el informe del art. 129 de la Ley General Presupuestaria están publicados en adif.es/sobre-adif/transparencia/economica. **No leídos**: la web rechaza lecturas automáticas y el navegador solo ofrece guardar el archivo.
- [P, búsqueda por título] En el BOE del 1-ene al 12-nov-2026 no consta la publicación de las cuentas anuales de Adif ni de Renfe.

## OPINIÓN (mía) y sesgos
- A favor: Renfe vuelve a beneficio y Correos sale de pérdidas. En contra: en los dos casos el resultado depende de dinero público (subvenciones del 84 % de las ventas en Renfe; compensación que sube un 67 % en Correos). Una empresa pública que presta un servicio obligatorio no se juzga como una privada: la compensación paga un servicio que el mercado no daría.
- Sesgo: las notas de prensa de las propias empresas destacan el beneficio y no la subvención; las cuentas dan las dos cosas.
- El origen de la pérdida de Correos en 2024 no se ha leído [VERIFICAR].

## Pendiente
Cuentas 2025 de Adif y Adif AV (si Joel guarda el PDF en el repo se leen en minutos); saldo de deuda de Correos (tabla desalineada en el PDF); Navantia (motivo de la pérdida); Paradores e Indra.

## Lecciones (máx. 5)
1. La página de Renfe guarda los enlaces a los PDF dentro de un JSON incrustado: buscarlos en el HTML crudo.
2. `pdftotext -layout` desalinea las columnas de 2025 y 2024: validar cada cifra con una suma de control antes de anotarla.
3. Si una web rechaza al script, no se disfrazan las cabeceras: se anota como no leído.

## Fuentes
- Renfe: https://grupo.renfe.com/content/dam/grupo-renfe/gobierno-y-transparencia/documentos/informacion-economica/cuentas-anuales/grupo-renfe/2025_InfAudit+CCAA+InfGestion+EINF_CONSO_FIRMADAS.pdf
- Correos: https://cswetwebcorsta01.blob.core.windows.net/uploads/2026/07/Informe_Anual_Integrado_2025_GRUPO-CORREOS.pdf
- Adif: https://www.adif.es/sobre-adif/transparencia/economica
