# C21 · R00 retroactivo (recuperar sesiones perdidas en una sola ventana)

Objetivo: que Joel no tenga que lanzar R00 de madrugada (apertura de Asia). El siguiente `/research R00` recupera lo que falte.

1. Mira en `informes/` qué `AAAA-MM-DD-apertura.md` / `-cierre.md` faltan de los últimos 3 días (hora de Madrid; fines de semana sin sesión de mercado). La apertura de Asia cuenta dentro de la apertura del día.
2. Haz UNA sola sesión (máx. 20 min): sección corta por hueco (Asia / Europa / EE. UU.), sin repetir lo ya escrito. Lo no reconstruible con fuente y fecha: «no reconstruible» o [VERIFICAR].
3. Guarda como el informe de hoy y pon en la cabecera: `cubre: AAAA-MM-DD-apertura, AAAA-MM-DD-cierre`.
4. `python scripts/construir_seguimiento.py` y `python scripts/construir_movil.py`: `r00()` cuenta lo declarado en `cubre:` como hecho.

Regla viva en `.claude/commands/research.md` (paso 3c). Coste: el de un R00 normal (~1 %), no uno por hueco.
