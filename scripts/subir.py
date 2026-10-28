"""Subida segura en un solo comando (sin IA, sin red salvo git). Se usa SOLO cuando Joel dice «sube».

Uso:  python scripts/subir.py "mensaje del commit" [--simular]
Hace, en este orden y por separado:
  1. git pull --rebase --autostash (por si el bot de paneles o el de noticias escribió antes)
  2. enseña git status y busca claves o archivos sensibles en lo que se va a subir (si encuentra algo, PARA y no sube nada)
  3. git add por nombre de archivo (nunca `git add -A`), git commit con la atribución de Claude
  4. git push
`--simular` solo enseña qué subiría.
"""
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ATRIBUCION = "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
PATRON_SECRETO = re.compile(r"(sk-ant-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[0-9A-Z]{16}"
                            r"|xox[abp]-[A-Za-z0-9-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|\b\d{8,10}:[A-Za-z0-9_-]{35}\b)")
RUTA_SENSIBLE = re.compile(r"(^|/)(privado/|\.env($|\.)|\.streamlit/secrets\.toml|secrets?\.(json|toml|ya?ml)$|.*\.(pem|key|p12)$)")


def git(*a, ok=False):
    r = subprocess.run(["git", *a], capture_output=True, text=True, encoding="utf-8", cwd=RAIZ)
    if r.returncode and not ok:
        print(f"git {' '.join(a)} falló:\n{r.stdout}{r.stderr}")
        sys.exit(1)
    return r.stdout


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    simular = "--simular" in sys.argv
    if not args and not simular:
        sys.exit('Falta el mensaje: python scripts/subir.py "mensaje" [--simular]')
    mensaje = args[0] if args else "(simulación)"

    if not simular:
        print(git("pull", "--rebase", "--autostash").strip())
    estado = git("status", "--porcelain", "-uall")
    archivos = []
    for linea in estado.splitlines():
        ruta = linea[3:].split(" -> ")[-1].strip('"')
        archivos.append(ruta)
    if not archivos:
        sys.exit("No hay nada que subir.")
    print(git("status", "--short"))

    problemas = [f"ruta sensible: {f}" for f in archivos if RUTA_SENSIBLE.search(f)]
    for f in archivos:
        p = RAIZ / f
        if p.is_file() and p.stat().st_size < 3_000_000 and p.suffix.lower() not in (".png", ".jpg", ".pdf", ".ico"):
            try:
                if PATRON_SECRETO.search(p.read_text(encoding="utf-8", errors="ignore")):
                    problemas.append(f"posible clave o token dentro de: {f}")
            except OSError:
                pass
    if problemas:
        print("PARO: no subo nada hasta que lo mires.\n  " + "\n  ".join(problemas))
        sys.exit(2)
    print(f"Revisión de claves y rutas sensibles: sin hallazgos ({len(archivos)} archivos).")
    if simular:
        print("(simulación: no se hace commit ni push)")
        return

    git("add", "--", *archivos)
    git("commit", "-m", f"{mensaje}\n\n{ATRIBUCION}")
    print(git("log", "--oneline", "-1").strip())
    print(git("push", ok=True).strip() or "push hecho")


if __name__ == "__main__":
    main()
