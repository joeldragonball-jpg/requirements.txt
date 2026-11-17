# C229 · Pack macro de España (17-nov-2026)

Salida: `explorador/espana-macro.json` (nuevo). Lectura directa en la API del INE (Tempus), la nota de la Seguridad Social del 4-nov y el BOE; sin IA ni workflows. No se regeneró `espana.json` (lo hace la sesión principal).

## Cerrado [P]
- **IPC oct-2026 (INE, 13-nov, NSA):** general 4,9 % anual (sep 4,9 %; mensual 0,6 %). A impuestos constantes: 5,6 %; subyacente 3,1 %; energía 29,0 %; servicios 4,1 %. Grupos: vivienda/electricidad/gas 7,6 %, transporte 10,3 %, alimentos y bebidas no alcohólicas 2,4 %.
- **EPA 3T-2026 (INE, 27-oct, NSA):** paro 10,18 % (2T 9,87 %; 3T-2025 10,45 %); menores de 25 años 23,33 %; ocupados 22.852,6 miles; parados 2.591,2 miles; tasa por las 19 CCAA/ciudades (Andalucía 14,91 %, Illes Balears 4,63 %, Melilla 18,87 %).
- **Afiliación oct-2026 (Seg. Social, 4-nov):** 22.624.165 personas (+186.612 mes; +784.573 año, 3,6 %); desestacionalizado 22.571.105.
- **SMI 2026 (BOE-A-2026-3815 leído):** 40,70 €/día, 1.221 €/mes; cuantía anual no inferior a 17.094 €; subida 3,1 %.
- **Coste laboral ETCL 2T-2026:** 3.388,15 €/mes total y 2.512,68 €/mes salarial.
- **PIB 3T-2026 (CNTR):** +0,63 % trimestral y +2,66 % anual (corregido); original +2,62 %.

## Abierto [VERIFICAR] / null
- Balanza de pagos BdE; Euríbor diario (la media de octubre 3,239 % viene de la lectura en Chrome del 12-nov, no releída); tipo medio de hipotecas; salario medio AEAT / mediano EAES; subyacente a impuestos corrientes.
- «14 pagas» del SMI: no aparece en el texto del RD leído; sigue sin confirmar.
- La atribución del salto de afiliación a la regularización es de analistas, no de la nota oficial.
- `scripts/indicadores.py` aún no lee estos bloques (patrón C201).

## Notas de lectura
- IPC: la diferencia entre 4,9 % (publicado) y 5,6 % (impuestos constantes) son 0,7 pp de efecto de medidas fiscales.
- SMI +3,1 % frente a IPC 4,9 % = 1,8 pp por debajo (cálculo propio; coste salarial +4,0 % según nota INE previa, sin releer).
- EPA y afiliación no son comparables entre sí. Sin recomendaciones.
