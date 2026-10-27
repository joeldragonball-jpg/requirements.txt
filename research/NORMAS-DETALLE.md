# Normas de detalle (sacadas de CLAUDE.md para ahorrar contexto al arrancar)

Se leen SOLO cuando la tarea las necesita. CLAUDE.md apunta aquí.

## Formato de los apuntes del cerebro (mismo que usa procesar.py)
Archivos nuevos en `cerebro/documentos/<tema-en-minusculas-con-guiones>.md`:
```
---
tema: (nombre corto)
etiquetas: [palabra1, palabra2]
actualizado: (fecha)
---
# (Tema)
## Resumen
## Explicación
## Puntos clave
## Conceptos
## Cifras y datos importantes
## Opiniones y predicciones
## Relación con mi cartera (XRP / XLM)
## Fiscalidad en España
## Dudas y datos a verificar
```
Antes de crear un apunte, comprueba que el tema no existe ya (busca en `cerebro/` por etiquetas) y amplía en vez de duplicar.

## Informes de las sesiones de research
- Los informes diarios van en `informes/AAAA-MM-DD-apertura.md` y `informes/AAAA-MM-DD-cierre.md`.
- NO los guardes dentro de `cerebro/`: procesar.py lee todos los .md de esa carpeta y el coste de la app subiría.
- Al cerebro solo pasan las LECCIONES (patrones de bulos, fuentes fiables/dudosas, catalizadores), no las noticias en bruto.
- Mantén estos tres archivos cortos y acumulativos, máx. 5 líneas nuevas por sesión y sin repetir:
  - `cerebro/documentos/patrones-de-bulos.md` (cómo se detectó cada bulo)
  - `cerebro/documentos/fuentes-fiables-y-dudosas.md`
  - `cerebro/documentos/catalizadores-xrp-xlm.md` (qué evento movió el precio y cuánto)

## Plantilla de sesión (la pego yo)
Sesión de [APERTURA / CIERRE]. Máximo 20 minutos.
1. Busca las noticias y rumores más relevantes de las últimas 12 h sobre XRP, XLM, cripto y macro (Fed, datos EE. UU.).
2. Marca qué es verificable y qué puede ser bulo, y por qué.
3. Guarda el informe en `informes/` con fecha y sesión.
4. Actualiza los tres archivos de lecciones con lo nuevo y útil (máx. 5 líneas cada uno).
5. Dame un resumen de 5 líneas y las 2 cosas que debería vigilar.

## Comprobación de seguridad diaria
Se aplica en cada lanzamiento matutino y en cada sesión de research, ANTES de empezar. El repo es PÚBLICO.
1. **Antes de empezar** ejecuta la comprobación rápida. Si `SECURITY_REPORT.md` ya dice «Última comprobación» con la fecha de hoy, NO repitas búsquedas ni auditorías: usa lo anotado.
2. **Qué incluye la comprobación rápida:**
   - `python scripts/seguridad_rapida.py` (sin IA, ~15 s): pip-audit de las dependencias, OSV de las GitHub Actions, CISA KEV de los últimos 3 días, secretos en archivos e historial de git y TLS desactivado. Devuelve 🟢, 🟡 o 🔴.
   - Búsqueda de avisos de las últimas 24-48 h SOLO en estas fuentes oficiales, mirando el aviso y no la página entera: nodejs.org/en/blog/vulnerability · python.org/downloads (y blog.python.org) · go.dev/doc/devel/release · rustsec.org y blog.rust-lang.org · oracle.com/security-alerts · osv.dev, nvd.nist.gov y GitHub Advisory Database · blog.mozilla.org/security (certificados y CA) · cisa.gov KEV. Para cada tecnología de este proyecto (Python y sus paquetes de `requirements.txt` y workflows; JavaScript solo `docs/sw.js`); el resto de runtimes solo si aparece algo crítico.
   - Actualiza `SECURITY_REPORT.md` (estado, fecha de «Última comprobación» y tabla) solo si cambió algo.
3. **Sin novedades:** informa en UNA sola línea («🟢 Seguridad: sin novedades, AAAA-MM-DD») y continúa con la tarea.
4. **Si hay 🟡 o 🔴:** avísame antes de seguir y NO avances con el research hasta que lo vea. Si es 🔴, dímelo al principio de la respuesta con los pasos concretos (rotar claves, etc.).
5. **Ligera (plan Pro):** solo las fuentes de arriba; no leas páginas enteras si basta con el aviso; no repitas búsquedas ya hechas el mismo día.
6. **Primarias primero:** avisos oficiales, NVD, OSV y GitHub Advisories antes que noticias o redes; cita el enlace de cada afirmación.
7. **Si no se puede verificar:** escribe «no verificado». No lo des por cierto ni lo descartes.
Reglas de código: nunca desactivar la verificación de certificados; ni claves ni tokens en el repo (solo `secrets.*` y `.env`, que no se sube); no hacer push ni merge de ramas `security/*` sin mi OK; solo aplicar parches y subidas menores que corrijan una vulnerabilidad confirmada, y los saltos de versión mayor se consultan antes.

## Flujo Gemini (manual, desde el 27-oct-2026)
- Gemini CLI no sirve con su cuenta (Google la retiró para particulares). Se trabaja con la app de Gemini (plan Plus) copiando y pegando.
- Cuando diga «C.. de Gemini» o «pásame el prompt de Gemini»: dame el prompt autocontenido de `research/gemini/` con el evento, país o lista ya rellenados (en un bloque de código) y ESPERA. No sigas sin la respuesta.
- La respuesta llegará pegada o subida a Drive (puedes leerla con el conector de Drive si te doy el nombre). Guárdala cruda en `informes/gemini/AAAA-MM-DD-<id>-<slug>.md`.
- Compruébala: contrasta 3-5 datos de mayor impacto con fuente primaria; todo lo no contrastado queda [S] o [VERIFICAR] (Gemini inventa enlaces y cifras). Vuelca al repo solo lo verificado (informe, `noticias/manuales/` cuando exista C18, lecciones de bulos y fuentes con el tope de 5 líneas).
- Cierra con la pregunta del Seguimiento y el planning, y con el «sube» para commit y push (en comandos separados).
- Rutina diaria gratis: 1 consulta ligera al día (~15 fuentes, sin repetirla). Rotación: lun/mié/vie/dom `NOTICIAS-24h`, mar `W02-deuda`, jue `W05-verificacion`, sáb `W10-energia`; si hay un evento de impacto alto hoy o mañana, `EV-post-evento`. La tarea del día sale en el Seguimiento («Tarea para Gemini») y en `research/PLANNING.md`.
- Cada sesión de Gemini se anota en `research/gemini-uso.json` (campo `sesiones`: fecha, prompt, fuentes aprox., nota) y, si Joel avisa de que Gemini le ha dado límite, en `avisos`; con aviso, se para por ese día. La cuota se comparte con NotebookLM.
