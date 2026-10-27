# MANTENIMIENTO (qué corre solo, qué cuesta y qué hacer si falla)

Última revisión: 2026-10-26. Sin claves ni secretos: los valores viven en GitHub (Settings → Secrets), en Cloudflare y en `.env` (que no se sube). El repositorio es PÚBLICO.

## 1. Qué corre solo

Todo vive en `.github/workflows/` (GitHub Actions). «IA» = llama a la API de Anthropic (facturación aparte de la suscripción de Claude).

| Workflow | Qué hace | Cuándo (UTC) | IA |
|---|---|---|---|
| `alertas.yml` | Alertas de precio y de movimientos de la watchlist → Telegram | cada 30 min (`7,37`) | No |
| `onchain.yml` | Vigilancia on-chain (XRP/XLM) → Telegram | cada 30 min (`19,49`) | No |
| `paneles.yml` | Refresca los paneles de datos del móvil y reconstruye `docs/movil/` y el Seguimiento | L-V 21:30 | No |
| `despertador.yml` | Despierta la app (evita que se duerma) | 04:41, 10:41, 16:41, 22:41 | No |
| `eventos.yml` | Aviso diario si hay un evento del calendario hoy o mañana | 05:47 | No |
| `escrow.yml` | Vigila el escrow de Ripple; avisa si cambia y el día 1 de cada mes | 06:12 | No |
| `federal-register.yml` | Vigilante del Federal Register (normas de cripto) | L-V 13:17 y 21:17 | No |
| `votos.yml` | Recoge tus 👍/👎 de las noticias | cada 15 min | No (`noticias.py` con `SOLO_VOTOS=true`) |
| `noticias.yml` | Bot de noticias: RSS + clasificación con IA + Telegram | cada hora (`:23`) | **Sí** (Sonnet 5.5; triaje y modo ahorro con Haiku 4.5; ver `noticias/config.toml`) |
| `cerebro.yml` | Convierte PDFs/capturas/notas de Telegram en apuntes (`cerebro_bot/procesar.py`) | solo bajo demanda (lo lanza el Worker) | **Sí** (Sonnet 5.5) |
| `revision.yml` | Revisión semanal del cerebro | domingos 19:17 | **Sí** (Sonnet 5.5) |
| `verificar.yml` | Verifica con búsquedas los [VERIFICAR] de los apuntes | día 1 de cada mes | **Sí** (Sonnet 5.5) |

**Worker de Cloudflare `lanzador-bots`** (código en `scripts/cloudflare-lanzador-bots.js`): cada 30 min lanza `alertas.yml` y `onchain.yml` por `workflow_dispatch` (el cron de GitHub es de «mejor esfuerzo» y llega a retrasarse horas) y, de L-V a las 07:00, 13:00 y 21:30 UTC, también `paneles.yml`. No llama a la API de Anthropic. Usa el secreto `GITHUB_TOKEN` guardado en Cloudflare.

**Otro Worker (cerebro):** https://cerebro-joel.joeldragonball.workers.dev (el cerebro separado). Su código no está en este repo [VERIFICAR dónde se guarda].

**Las dos apps**
- App del PC (Streamlit): `app.py`; se abre con `Abrir-Cerebro.bat` (pestañas, incluida «🧠 Cerebro» y Seguimiento).
- App del móvil (PWA): carpeta `docs/` (`docs/movil/index.html`, `data.json`, `seguimiento.json`). Se regenera con `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`; `paneles.yml` lo hace solo.

## 2. Qué cuesta

- **Sin coste de API:** alertas, on-chain, paneles, despertador, eventos, escrow, federal-register, votos y el Worker. GitHub Actions es gratis en repos públicos; el Worker usa el plan gratuito de Cloudflare [VERIFICAR límite de ejecuciones/día en la consola].
- **Con coste de API (los 4 con IA):** `noticias` (el más caro: corre cada hora), `cerebro`, `revision`, `verificar`. Para cifras reales mira la consola de Anthropic (Usage) y el informe de la tarea C16 (`informes/research/*-C16-costes-api.md`) cuando exista.
- **Mantén un límite de gasto mensual** en la consola de Anthropic (Settings → Limits). Si se agota el saldo, esos 4 bots fallan sin romper el resto.
- La suscripción de Claude (research con `/research`) NO paga la API. Cuando termine (~4-5 nov), los bots con IA siguen mientras haya saldo en la API.

## 3. Qué caduca y cuándo

| Qué | Caduca | Qué hacer |
|---|---|---|
| Token de GitHub del Worker (`GITHUB_TOKEN` en Cloudflare) | 1 año desde su creación (~oct-2027) [VERIFICAR fecha exacta en GitHub → Settings → Developer settings] | Crear uno nuevo con permiso solo de Actions (lectura/escritura) sobre este repo y pegarlo en Cloudflare → Worker → Settings → Variables (como secreto). |
| Saldo/límite de la API de Anthropic | Cuando se agote | Recargar o subir el límite; mientras tanto pausar `noticias.yml` (ver §5). |
| Secretos `TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID`, `ANTHROPIC_API_KEY` | No caducan solos; rota si sospechas filtración | GitHub → Settings → Secrets and variables → Actions. |
| Crons de GitHub | GitHub desactiva los workflows programados tras 60 días sin actividad en el repo | Mientras los bots escriban en el repo no pasa; si ocurre, Actions → workflow → «Enable». |
| Plan de Claude | ~4-5 nov | Ver `research/gemini/` y §6. |

## 4. Cómo lanzar cada rutina a mano

**Bots (sin usar Claude):** GitHub → pestaña Actions → elige el workflow → «Run workflow». Desde la terminal con `gh`:

```bash
gh workflow run alertas.yml
```

Cambia `alertas.yml` por `onchain.yml`, `paneles.yml`, `eventos.yml`, `escrow.yml`, `federal-register.yml`, etc. Los de IA (`noticias`, `cerebro`, `revision`, `verificar`) cuestan dinero: lánzalos solo si lo necesitas.

**Regenerar paneles/Seguimiento en local:**

```bash
python scripts/construir_movil.py
python scripts/construir_seguimiento.py
```

**Research semanal:** con Claude, `/research` (sin argumento lee `research/PLANNING.md`) o `/research W01`. Prompts en `research/prompts/`. Sin Claude: los equivalentes para Gemini están en `research/gemini/` (ver §6).

## 5. Cómo comprobar que todo va

1. **Seguimiento** (app del móvil/PC): bots con problema, frescura, predicciones por vencer.
2. **`research/PLANNING.md`**: qué toca hoy, auditorías, verificaciones abiertas, «Bots con problema».
3. **Pestaña Sistema** de la app del PC.
4. **GitHub → Actions:** busca ejecuciones en rojo. Una alerta de Telegram que deja de llegar suele ser lo primero que notas.
5. **Seguridad:** `python scripts/seguridad_rapida.py` (sin IA, ~15 s) y `SECURITY_REPORT.md`.

## 6. Si un bot falla

1. Abre Actions → ejecución en rojo → lee las últimas líneas del log (nunca pegues claves en ningún chat).
2. Causas habituales: 
   - *Token o secreto caducado/ausente* → rehacerlo (§3).
   - *Saldo de la API agotado* (solo bots con IA) → recargar, o pausar el workflow: en el archivo `.yml` comenta el bloque `schedule:` y deja `workflow_dispatch:`.
   - *Fuente externa cambió o dio 403/429* → el bot suele seguir en la siguiente pasada; si no, revisa el script correspondiente (`alertas/`, `eventos/`, `noticias/`).
   - *Conflicto de `git push` entre bots* → vuelve a lanzarlo; si persiste, haz `git pull` en el PC.
3. Si el Worker no lanza nada: Cloudflare → Workers → `lanzador-bots` → Logs; un 401/403 = token caducado; un 404 = nombre de repo o de workflow mal escrito.
4. Si nada se arregla, los bots sin IA siguen funcionando con el cron propio de GitHub, solo que más lentos.

## 7. Si ya no hay Claude

**Sigue actualizándose solo:** alertas de precio, on-chain, paneles de datos (bolsas, tipos, divisas, etc.), calendario con avisos, escrow, Federal Register, despertador y el móvil/PC (con los datos ya cargados). Con saldo en la API: noticias con IA, entrada de PDFs/notas al cerebro, revisión semanal y verificación mensual.

**Queda manual (o con otra IA):**
- Las rutinas de research W01-W10, C-xx y EV: se hacen pegando los prompts de `research/gemini/` en Gemini Deep Research (u otro) y volcando el resultado al repo a mano (instrucciones en esa carpeta).
- Editar `explorador/*.json`, `eventos/calendario.toml`, `research/COLA.md` y el cerebro (`cerebro/`): son archivos de texto y JSON editables a mano; luego `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`.
- Renovar el token de GitHub del Worker (§3) y vigilar el gasto de la API.
- Revisar el aviso de seguridad (`seguridad_rapida.py`) de vez en cuando; los parches y saltos de versión mayor se deciden a mano.
- Commit y push con `git` de siempre (`git pull` primero; los bots también escriben en el repo).

## 8. Gemini CLI (primera pasada de research)
- Instalado en el PC con `npm install -g @google/gemini-cli` (versión 0.65.0). **27-oct-2026: «Login with Google» ya no sirve:** Google respondió `IneligibleTierError: This client is no longer supported for Gemini Code Assist for individuals` (migrar a Antigravity). La vía que queda para la CLI es una clave de API de Google AI Studio en la variable `GEMINI_API_KEY` (nunca en el repo) [VERIFICAR gratuidad y límites].
- Puente: `python scripts/gemini_tarea.py <prompt> --param "clave=valor"` (prompts en `research/gemini/`; `--dry-run` solo muestra el prompt). La respuesta cruda va a `informes/gemini/` y es [S] o [VERIFICAR] hasta contrastarla con la fuente primaria. Ejemplo: `python scripts/gemini_tarea.py EV-post-evento --param "evento=2026-10-28 Reunión de la Fed (FOMC)"`.
- No usa la API de Anthropic. El límite de uso gratis depende de tu cuenta de Google [VERIFICAR].
