# C18 · Noticias manuales (27-oct-2026)

**Qué hay:** una tubería sin API de Anthropic. Tú o yo hacemos el research con la cuota de Claude o Gemini, el resultado se guarda como JSON en `noticias/manuales/` y el bot lo envía a Telegram y lo guarda como el resto. Probado solo en local con un JSON de ejemplo (sin red, sin bot real, sin API).

## Formato
`noticias/manuales/AAAA-MM-DD-<slug>.json` (los que empiezan por `_` se ignoran; ejemplo en `_ejemplo.json`). Cabecera: `evento`, `fecha`, `nivel` (`evento` o `ligera`), `generado_con`. Cada noticia: `titulo, fuente, url, fecha, resumen (1-2 frases), etiqueta P|S|VERIFICAR, tema (uno de config.toml), nota 1-10, fiabilidad, bulo true|false, motivo_bulo` y opcionales `leccion_bulo`, `fuente_nueva`. `noticias: []` es válido (tanda de tarde sin nada con nota >= 7: no se envía nada).
- Límites: `evento` hasta 25 piezas; `ligera` hasta 8 y solo nota >= 7.
- Validación compartida: `noticias/manuales.py`; `python scripts/validar_manuales.py` (añade `--lecciones` para escribir las líneas en el cerebro, máx. 5 por archivo, idempotente).

## Bot (`noticias/noticias.py`, `importar_manuales`)
- Se ejecuta en cada pasada horaria (entre las 8:00 y las 23:00 de Madrid), sin esperar a una franja. Un JSON roto se salta con aviso en el log, no tumba el bot.
- Evita duplicados: por enlace/título frente a `noticias` guardadas y a la lista `manuales_enviados` (rama `datos`), y por título parecido a lo ya enviado (`es_repeticion`).
- Marca `origen: manual`, `nivel`, `evento`, `etiqueta`, `bulo`. Telegram: mismo formato + línea «🔎 Research manual de evento/ligero» y, si es bulo, «⚠️ Posible bulo». Se guarda con 👍/👎 y `valoracion` como las demás, así salen en el móvil y cuentan en los votos.
- No gasta el cupo diario de 10 (se excluyen del recuento) y respeta `nota_minima` (7). Tope por pasada: `max_manuales_por_ejecucion = 25`.
- Lecciones de bulos y fuentes: NO las escribe el bot (evita commits a `main` desde CI que choquen con los tuyos); se añaden al subir el JSON con `--lecciones`.

## Modo evento (opcional, apagado: `modo_evento = false`)
En días con un evento de impacto «alto» del calendario sube `max_noticias_dia` y `max_tras_triaje` un `modo_evento_aumento_pct` (30 %). Sigue mandando `tope_diario_usd` (C17): al superarlo pasa a `modelo_ahorro`. **Coste extra [ESPECULACIÓN]**: el gasto normal ronda 4-6 $/mes (comentario de `config.toml`), ≈0,15-0,20 $/día; +30 % en ~8 días «alto» al mes ≈ +0,4 $/mes (≈0,35 €). Para activarlo: `modo_evento = true`.

## Prompts
- Claude: `research/prompts/EV-noticias-manual.md` (nivel evento y nivel ligera, con los pasos).
- Gemini (flujo manual): `research/gemini/EV-noticias-evento.md` y `EV-noticias-ligera.md`.
- Tanda de tarde: 20:00 España = 14:00 Nueva York. No es un R00 nuevo; el R00 de cierre sigue cubriendo el final del día. Coste: evento ~1-2 % de cuota (gratis con Gemini); ligera ~0,5 %.

## Prueba local (resultado)
Validador OK con el ejemplo; 2 piezas enviadas la 1.ª vez y 0 la 2.ª (sin duplicar); JSON roto ignorado con aviso; bulo con aviso en el mensaje; lecciones idempotentes (1 línea de bulo, 1 de fuente, sin repetir); detección de evento «alto» correcta (28-oct sí). [Aviso] Probado con módulos simulados en Windows; no se ha ejecutado el workflow real.

## Vigilar
1. Primer envío real: confirmar en Telegram que el formato HTML sale bien y que el JSON subido no se reenvía.
2. Un archivo con URLs inventadas pasaría la validación: el control es de contenido (verificar 3-5 enlaces antes de subir).

## Seguridad
Sin claves ni red nuevas; el bot solo lee archivos del repo. Los JSON son públicos (repo público): nada privado ni de tu tesis en ellos.
