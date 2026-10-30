# C66 · España: a dónde va cada euro (por ministerio y programa) y quién lo recibe (pedido de Joel, 30-oct-2026)

Objetivo: desglosar el gasto del Estado por ministerio y política, y, donde se publique, el perfil de los beneficiarios (incluida la nacionalidad). Solo datos oficiales publicados; si no existe el desglose, decirlo con claridad en vez de estimarlo. Hechos con fuente y año; [VERIFICAR] lo no leído; opiniones aparte. Presentar cada dato con su denominador (p. ej. % de beneficiarios extranjeros frente al % de población extranjera) para no inducir a error. Sin recomendaciones.

## Parte A · Presupuesto por ministerio y programa
1. Presupuestos Generales del Estado vigentes (comprobar si hay PGE 2026 aprobados o siguen prorrogados los de 2023): gasto por sección (ministerio) y por política de gasto/programa. Fuentes: Hacienda (SEPG, «Presupuestos Generales del Estado», libro amarillo y Estado de gastos), IGAE (ejecución mensual y cuentas), Intervención General.
2. Para cada ministerio: crédito inicial, crédito definitivo y obligaciones reconocidas del último año cerrado. Distinguir Estado, Seguridad Social, organismos y CCAA (sanidad y educación son autonómicas).
3. Programas que Joel pide, con su partida exacta: Igualdad (Ministerio de Igualdad y Pacto de Estado contra la Violencia de Género: transferencias a CCAA y ayuntamientos; Delegación del Gobierno contra la Violencia de Género), enfermedades raras (no tiene partida propia: ver Sanidad, ISCIII, CIBERER, Dependencia; decir qué se puede y qué no se puede aislar), Ingreso Mínimo Vital, becas y ayudas al estudio, inmigración y asilo (Inclusión, Interior: CATE, CETI, protección internacional, acogida), pensiones no contributivas, dependencia, cooperación al desarrollo, defensa, cultura, vivienda.
4. Violencia de género: cifras de órdenes de protección, víctimas mortales, denuncias y juzgados especializados (CGPJ, Delegación del Gobierno, INE «Estadística de violencia doméstica y violencia de género»); gasto frente a casos.

## Parte B · Quién recibe las prestaciones
1. Ingreso Mínimo Vital: hogares y personas beneficiarias, importe medio y total, por nacionalidad, comunidad y composición del hogar (Seguridad Social/INSS, estadística del IMV).
2. Becas y ayudas al estudio (Ministerio de Educación, estadística de becas): nº de becarios, importe, por nivel, por nacionalidad si se publica; criterios de acceso (renta, patrimonio, residencia).
3. Prestaciones por desempleo, pensiones no contributivas y otras: beneficiarios por nacionalidad cuando los publique SEPE, IMSERSO, INSS; afiliación y cotización de extranjeros (Seguridad Social) como contrapartida.
4. Nacionalidad y origen: las estadísticas oficiales hablan de nacionalidad y país de nacimiento; **no publican «hijos de inmigrantes» (ascendencia) con detalle** salvo la Encuesta de Condiciones de Vida y el Censo de Población (INE): decir qué cruza se puede hacer y cuál no. No inferir por apellido ni por origen supuesto.
5. Siempre al lado: población total y por nacionalidad (INE), y los requisitos legales de acceso (residencia legal y años exigidos).

## Entregables
- `explorador/espana-presupuesto.json` (ministerios y programas, con crédito inicial/obligaciones, año y fuente) y ampliar `explorador/espana-manual.json` (beneficiarios).
- Informe `informes/research/AAAA-MM-DD-C66-presupuesto-y-beneficiarios.md` con tablas, lo que no existe y [VERIFICAR].
- Después, la capa «España» del Panel informativo (escritorio) y la viñeta «España» del móvil (fase 3 de C65, ver `research/prompts/C65-espana-ingresos-gasto-resultados.md`).

## Cómo ejecutarlo
Sesión nueva con el relevo (`privado/relevo.md`). Es lectura larga de PDF/Excel de Hacienda: modelo potente (Opus) y esfuerzo alto si Joel lo autoriza; navegador integrado para webs que dan 403. Parar al 70 % de contexto y dejar relevo. Regenerar con `construir_movil.py` y `construir_seguimiento.py`.
