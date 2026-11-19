# C245 - Plantilla de órganos constitucionales (19-nov-2026)

Alcance: Cortes, Tribunal de Cuentas, CGPJ, TC, Consejo de Estado, Casa de S.M. el Rey. Solo se completó explorador/espana-empleados.json.

| Órgano | Dato | Tipo | Fuente | Fecha | Nivel |
|---|---|---|---|---|---|
| Cortes Generales | 853 (sin cambios) | personas | Congreso/Senado | 17-nov-2026 | P |
| CGPJ | 465 puestos (sin cambios) | puestos | RPT oficial ene-2025 | | S |
| Tribunal Constitucional | 221 (sin cambios) | personas | Memoria 2025 | 31-dic-2024 | P |
| Consejo de Estado (NUEVO) | RPT funcionario: dotación 122, ocupadas 100 (82 filas); RPT laboral: dotación 15, cubiertas 8 (11 filas); total 137 dotados / 108 ocupados | puestos, no personas | consejo-estado.es/wp-content/uploads/2026/10/rpt-personal-funcionario-... y rpt-personal-laboral-...-octubre-2026.pdf | oct-2026 | P (puestos); empleados null |
| Tribunal de Cuentas | «más de 750 personas» (cota textual); sin RPT numérica; empleados null | personas, cota | tcu.es, Personal al servicio de la institución | consulta 19-nov-2026 | P (texto) |
| Casa de S.M. el Rey | null; Secretaría General 156 funcionarios (solo una unidad) | parcial | casareal.es | 18-nov-2026 | P parcial |

## Método Consejo de Estado
Los PDF se descargaron con fetch desde la propia página en Chrome (curl da 403), se descomprimieron los flujos y se extrajo el texto (funcionario: cadenas literales; laboral: fuentes CID con ToUnicode). Suma funcionario automática por regex (82 filas, incl. 6 filas «ROCE» de letrados); laboral comprobada a mano (15/8). [VERIFICAR] la suma funcionaria contra el PDF.

## Notas
- Puestos presupuestados/RPT no son personas [VERIFICAR].
- Anexo de personal de los PGE por órgano: no localizado comparable (igual que 18-nov).
- Pendiente: Tribunal de Cuentas (RPT numérica), Casa Real (total), TC dic-2025.
