# C205 y C206 · Vista privada de la tesis y alertas de datos por Telegram (14-nov-2026)

Tareas de mejora (propuestas 17 y 18 de research/VALORACION-CAPAS-Y-CALENDARIO.md). Sin IA, sin red, sin claves en el repo y sin lanzar workflows. Este informe es público: no contiene nada de la tesis.

## C205 · Vista de tesis privada
- **Qué hace:** `scripts/construir_tesis_privada.py` genera `privado/tesis-vista.html`, que solo existe en el PC.
  - Reparte cada premisa del contraste privado en tres columnas: a favor, en contra y sin dato. Usa el veredicto que ya tenía y no reclasifica nada.
  - Debajo de cada capa pone la evidencia pública del Explorador con su enlace: movimientos (con su informe), voces confirmadas (con su URL) y celdas del radar regulatorio (con su URL).
- **La tesis es una lente:** lo publicado después de la fecha del contraste sale como «Nuevo, sin clasificar», sin juzgarlo frente a la tesis. El Explorador sigue sin medirse contra ella.
- **Garantías de privacidad (el repo es público):**
  1. `privado/` está en `.gitignore` y no hay ningún archivo suyo en git (`git ls-files privado` vacío, 14-nov-2026).
  2. El generador se niega a escribir si su salida no está dentro de `privado/` o si `privado/` deja de estar ignorado.
  3. `scripts/huellas_privado.py` saca huellas de 60 caracteres de las conclusiones privadas y una marca propia de la vista. No las imprime ni las guarda; en GitHub Actions no hay huellas porque `privado/` no existe allí.
  4. `construir_orbita.py` no escribe la Órbita si la página lleva alguna huella. Esto se suma a la comprobación que ya tenía.
  5. `revisar_explorador.py` avisa si algún archivo de `privado/` entra en git, si `.gitignore` deja de excluirlo o si alguna huella aparece en `docs/`.
- **Prueba en negativo:** un razonamiento privado y la marca de la vista se detectan; un texto público del Explorador no da falso positivo.
  - La primera versión de las huellas, de 40 caracteres e incluyendo las preguntas abiertas, dio un falso positivo: una pregunta genérica también aparece en un dossier público.
  - Se corrigió quitando las preguntas abiertas y alargando las huellas a 60 caracteres.
  - Los nombres de archivo de `privado/` no cuentan como huella: salen en las tareas públicas y no revelan nada. Con eso, `docs/` sale limpio.

## C206 · Alertas por umbral y por evento
- **Qué hace:** `alertas/datos.py` avisa por Telegram solo de lo nuevo desde la última ejecución:
  - Datos en rojo: elementos de frescura que pasan a «alerta» (`docs/movil/seguimiento.json`).
  - Tipos oficiales: decisión nueva de un banco central (cambia `ultimo_cambio` en `paneles.json → tipos_vivos` y en `tipos-manual.json`) y cruces de los umbrales de `[datos.umbrales_tipos]`, con un margen de 5 pb.
  - Noticias de nivel P: movimientos nuevos con fuente primaria [P] de los últimos 7 días (`explorador/datos.json`), con enlace a la fuente o al informe.
- **Configuración:** sección `[datos]` de `alertas/config.toml`. Cada parte se puede apagar; tope de 8 líneas por mensaje. Los umbrales de la Fed (3,50 y 4,50 %) y del BCE (2,00 y 3,00 %) son ejemplos que Joel debe ajustar.
- **Memoria:** `alertas/estado-datos.json`, guardado en la caché de GitHub (sin commits) e incluido en `.gitignore`. La primera ejecución solo memoriza el estado y no envía nada.
- **Dónde se ejecuta:** paso nuevo en `.github/workflows/eventos.yml` (diario, 05:47 UTC), con los mismos secrets `TELEGRAM_TOKEN` y `TELEGRAM_CHAT_ID`, `continue-on-error` y permisos de solo lectura. No se ha lanzado.
- **Prueba local en modo prueba (sin token):**
  1. La primera ejecución memoriza y no envía nada.
  2. La segunda no tiene nada nuevo que avisar.
  3. Al simular cambios salen 1 dato en rojo, 1 decisión del Banco de Inglaterra (5-nov, +25 pb), 1 cruce de umbral y 3 movimientos [P], todos con enlace.
- **Nota técnica:** no importa `alertas.py`, porque al cargarse necesita `requests` y `tzdata`, que el Python del PC no tiene. Reutiliza el mismo `config.toml`, los mismos secrets y la misma forma de enviar que `eventos/avisos.py`.

## Pendiente
- Joel: ajustar los umbrales de tipos en `alertas/config.toml`.
- Tras el primer aviso real, comprobar que el mensaje llega bien a Telegram.
- Si se quiere probar ya, lanzar a mano el workflow «Aviso de eventos». La primera vez solo memoriza.
