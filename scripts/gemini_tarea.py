"""Puente Claude -> Gemini CLI (sin API de Anthropic): lanza un prompt de research/gemini/ y guarda la respuesta cruda.

Uso:
  python scripts/gemini_tarea.py EV-post-evento --param "evento=2026-10-28 Reunión de la Fed (FOMC)"
  python scripts/gemini_tarea.py W01-tipos --dry-run          # solo muestra el prompt, no llama a Gemini
La respuesta va a informes/gemini/AAAA-MM-DD-<id>-<slug>.md (NO en cerebro/). Todo lo que sale de Gemini es [S] o [VERIFICAR]
hasta que se contraste con la fuente primaria. Requiere haber iniciado sesión una vez con `gemini` (cuenta de Google).
"""
import argparse
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PROMPTS = RAIZ / "research" / "gemini"
SALIDA = RAIZ / "informes" / "gemini"
AVISO = ("\n\nAVISO PARA QUIEN LEA: salida cruda de Gemini. Todo dato es [S] o [VERIFICAR] hasta contrastarlo con la fuente primaria; "
         "puede haber enlaces o cifras inventados.\n")


def cargar_prompt(id_):
    f = PROMPTS / f"{id_}.md"
    if not f.is_file():
        sys.exit(f"No existe {f.relative_to(RAIZ)}. Disponibles: " + ", ".join(sorted(p.stem for p in PROMPTS.glob('*.md') if p.stem != 'LEEME')))
    m = re.search(r"```\n(.*?)\n```", f.read_text(encoding="utf-8"), re.S)
    if not m:
        sys.exit(f"{f.name}: no encuentro el bloque de código con el prompt.")
    return m.group(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id", help="nombre del prompt en research/gemini/ (ej. EV-post-evento, W01-tipos)")
    ap.add_argument("--param", action="append", default=[], help="clave=valor que se añade al prompt (evento, país, lista...)")
    ap.add_argument("--timeout", type=int, default=900, help="segundos máximos de espera (por defecto 900)")
    ap.add_argument("--dry-run", action="store_true", help="solo muestra el prompt final")
    args = ap.parse_args()

    prompt = cargar_prompt(args.id)
    hoy = datetime.now().strftime("%Y-%m-%d")
    if args.param:
        prompt += "\n\nDATOS DE ESTA TAREA (hoy es " + hoy + "):\n" + "\n".join(f"- {p}" for p in args.param)
    else:
        prompt += f"\n\nDATOS DE ESTA TAREA: hoy es {hoy}."
    if args.dry_run:
        print(prompt)
        print(f"\n[dry-run] {len(prompt)} caracteres; no se ha llamado a Gemini.")
        return

    exe = shutil.which("gemini")
    if not exe:
        sys.exit("Gemini CLI no está instalado: npm install -g @google/gemini-cli")
    try:
        r = subprocess.run([exe, "-p", prompt], capture_output=True, text=True, encoding="utf-8", timeout=args.timeout)
    except subprocess.TimeoutExpired:
        sys.exit(f"Gemini no respondió en {args.timeout} s.")
    if r.returncode != 0 or not r.stdout.strip():
        err = (r.stderr or r.stdout or "").strip()[:600]
        if "Auth method" in err or "GEMINI_API_KEY" in err:
            sys.exit("Falta iniciar sesión: abre una terminal, escribe `gemini` y elige «Login with Google».")
        sys.exit(f"Gemini falló (código {r.returncode}): {err}")

    SALIDA.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", (args.param[0] if args.param else args.id).lower()).strip("-")[:40]
    destino = SALIDA / f"{hoy}-{args.id}-{slug}.md"
    destino.write_text(f"# Gemini · {args.id} · {hoy}\n\nParámetros: {'; '.join(args.param) or 'ninguno'}{AVISO}\n---\n\n{r.stdout.strip()}\n", encoding="utf-8")
    print(f"Guardado en {destino.relative_to(RAIZ)} ({len(r.stdout)} caracteres).")
    if r.stderr.strip():
        print("Mensajes de Gemini CLI:", r.stderr.strip()[:300])


if __name__ == "__main__":
    main()
