"""Genera el prompt de relevo para abrir una sesión nueva cuando la conversación llega al 75 % de contexto (sin IA).

Uso:  python scripts/generar_relevo.py --resumen "3-5 líneas de lo hecho y lo pendiente"
Escribe privado/relevo.md (esa carpeta no se sube) y lo imprime para copiarlo y pegarlo en una sesión nueva."""
import argparse
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def git(*args):
    r = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=RAIZ)
    return r.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--resumen", default="(sin resumen: léelo en research/PLANNING.md y en la memoria)")
    args = ap.parse_args()
    sin_commit = [l for l in git("status", "--short").splitlines() if "maqueta-movil" not in l]
    texto = f"""Continuamos el repo cartera-github ({date.today():%d-%m-%Y}). Responde en español, con pasos cortos, y sigue CLAUDE.md.
Primero `git pull` (no descartes cambios), `git status` y los últimos 5 commits. Para saber qué hay por hacer lee SOLO `research/PLANNING.md`; lee también la memoria `ideas-pendientes-mejoras` y `actualizar-seguimiento-al-lanzar`.

Estado al hacer el relevo:
- Últimos commits:
{chr(10).join('  ' + l for l in git('log', '--oneline', '-5').splitlines())}
- Sin commitear: {('; '.join(sin_commit)) if sin_commit else 'nada'}

Resumen de la sesión anterior: {args.resumen}

Reglas que siguen: commit y push solo cuando yo diga «sube» (commit por nombre de archivo; `git pull` y `git push` en comandos separados); al terminar o añadir una tarea, actualiza `research/COLA.md` y regenera con `python scripts/construir_movil.py` y `python scripts/construir_seguimiento.py`; trabaja en sesiones cortas y avísame cuando el contexto llegue al 75 % (nunca pasar del 85 %) con un prompt de relevo (`python scripts/generar_relevo.py`); no lances workflows ni llames a la API de Anthropic sin pedírmelo; la suscripción de Claude termina hacia el 4-5 de noviembre: prioriza lo que quede funcionando solo."""
    destino = RAIZ / "privado" / "relevo.md"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text(texto + "\n", encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
