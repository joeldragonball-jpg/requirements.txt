# España · claridad en los bloques de política (10-nov-2026)

**Qué se hizo** (pestaña España › «Política y leyes», `explorador/vistas.html`; textos en `scripts/leyendas_politica.py` → `explorador/espana-politica.json`, campos `explicacion`, `leyenda_*`):
- Cada bloque (Congreso, iniciativas, intereses, financiación de partidos, altos cargos, «lo que no se ha leído») lleva arriba 3-4 frases visibles: qué es, unidades, de dónde sale y **qué NO dice**.
- Unidades dentro de cada celda («172 votos», «54 personas», «1.224 declaraciones», «88 iniciativas», «64 normas») y en el título de columna; añadido % sobre el total donde aclara.
- Códigos traducidos: ACTIVIDAD → «Actividad: empleo, cargo o negocio»; DONACION → «Donaciones o regalos recibidos»; FUNDACIONES → «Aportaciones a fundaciones u otras entidades»; OBSERVACIONES → texto libre. Cada resultado de iniciativa (Aprobado, Caducado, Decaído, Retirado, Subsumido, Inadmitido…) y cada tipo de norma tiene columna «Qué significa». «Aprobado» ≠ ley en vigor; «Caducado/Decaído» ≠ rechazo.
- Intereses: aclarado que «recuento» = número de declaraciones, no euros; añadidas tablas por momento de la declaración y por año de registro.
- Financiación: columna Fecha rellenada (ejercicio 2020 / 2021-22) y enlace a cada informe en «Fuente» (antes vacío).
- Quitada la jerga interna «C68/C68B» de la nota de altos cargos.

**Quedó sin aclarar**
- Definición formal de los tipos del fichero `docacteco`: la página de datos abiertos del Congreso no la publica; los significados se han deducido de los campos y ejemplos reales del fichero. Marcado [VERIFICAR] en FUNDACIONES y en «Inadmitido… con requerimiento».
- Por qué 403 diputados con registro > 137 en alta: se supone que incluye bajas [VERIFICAR].
- Efecto jurídico de los dos Reales Decretos-leyes votados el 2-oct (172-178 y 166-184): no se concluye, remite al BOE [VERIFICAR].

**Bloques que no son política:** ninguno en mis bloques. «Justicia» (`espana_judicial`) ya tiene su propia introducción y no se tocó.
No se movió ningún bloque de subpestaña.
