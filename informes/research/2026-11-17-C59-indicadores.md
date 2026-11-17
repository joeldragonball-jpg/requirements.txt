# C59 · Indicadores por país: huecos cerrados (17-nov-2026)

Alcance: solo los huecos que quedaban (salario mínimo JP/CN/IN/IT y pobreza JP). Archivo tocado: `explorador/indicadores-manual.json` (sin borrar nada). No se ha tocado `actualizar_paneles.py` (`leer_indicadores()` ya existía). Sin `construir_*`.

| País | Indicador | Dato | Nivel | Fuente y fecha |
|---|---|---|---|---|
| Japón | Salario mínimo | media nacional ponderada 1.177 ¥/h (+56 ¥; antes 1.121); máx. Tokio 1.280, mín. 1.085 | **P** | MHLW, nota de respuesta de los consejos regionales (año fiscal 2026), leída 17-nov-2026; vigor 1-oct a 2-dic-2026 |
| Japón | Pobreza relativa | 15,0 % (línea 1,38 M¥, renta 2024) frente a 15,4 %; infantil 11,0 %; monoparentales 44,7 % | **S** | Encuesta de Condiciones de Vida 2025 (MHLW, julio 2026). El PDF oficial no se pudo leer en texto; cifras de lecturas secundarias |
| China | Salario mínimo | sin mínimo nacional; Shanghái 2.740 ¥/mes desde 1-jul-2025 (el más alto) | **S** | prensa que cita 沪人社规〔2025〕10号 y el recuento del Ministerio de RR. HH.; el PDF oficial dio 404 |
| India | Salario mínimo | suelo nacional no vinculante 178 ₹/día (2019); sin suelo nuevo notificado | **S** | guías jurídicas 2026; Reglas Centrales de 2026 notificadas el 8-may-2026 [VERIFICAR gaceta] |
| Italia | Salario mínimo | no existe (convenios colectivos); n/a por diseño | V | marco, sin cifra |

## Contraste y sesgos
- 1.177 ¥ (MHLW) coincide con la cifra de la prensa laboral y el objetivo del consejo central (1.176 ¥): 3 fuentes cuadran.
- Pobreza JP (relativa, 50 % mediana) no es comparable con AROPE (60 %) ni con la tasa absoluta de EE. UU.; el hogar monoparental (44,7 %) tira de la media.
- China e India: las cifras de «salario mínimo» no son nacionales; no se ordenan países.

## Sigue abierto
- Series 2025 de IN/RU/JP/GB (Banco Mundial dio 502 el 16-nov), pobreza JP en [P], aviso oficial de Shanghái, gaceta india.
- Próxima actualización del salario mínimo japonés: julio-septiembre de 2027 (ciclo anual).

[VERIFICAR] pobreza JP y China/India hasta leer la fuente primaria.
