"""Comprobación rápida de seguridad SIN IA (no gasta tokens ni llama a la API de Anthropic).

Uso (desde la carpeta del repo):
    python scripts/seguridad_rapida.py            # resumen y veredicto
    python scripts/seguridad_rapida.py --json     # lo mismo en JSON

Qué hace (solo fuentes oficiales/abiertas y comprobaciones locales):
  1. pip-audit (base de PyPA/OSV) sobre las dependencias que usa el proyecto (necesita `uv`).
  2. OSV (osv.dev) para las GitHub Actions que usan los workflows.
  3. CISA KEV: entradas de los últimos 3 días que nombren tecnologías de este proyecto.
  4. Secretos: patrones de claves en los archivos rastreados y en TODO el historial de git (el repo es público).
  5. TLS: busca verificación de certificados desactivada.
  6. Observaciones de endurecimiento (workflows sin permisos, pip sin versión, devcontainer): NO cambian el veredicto.
Veredicto: 🔴 si hay secreto, TLS desactivado, vulnerabilidad en dependencias o KEV que nos nombre;
           🟡 si algo no se pudo comprobar; 🟢 si no hay nada.
Los avisos de runtimes (Node, Python, Go, Rust, Java) y de certificados se buscan aparte, en las fuentes oficiales
listadas en CLAUDE.md; este script no los sustituye.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
EXTRAS = ["tzdata", "feedparser", "markdown", "openpyxl", "pypdf", "playwright"]   # los que usan scripts y workflows
TECNOLOGIAS = r"python|cpython|node\.?js|golang|\bgo\b|rust|openjdk|oracle|java|openssl|brotli|certifi|urllib3|requests|streamlit|pandas|numpy|jinja|tornado|pillow|playwright|chromium|github|anthropic"
PATRON_SECRETO = (r"(sk-ant-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[0-9A-Z]{16}"
                  r"|xox[baprs]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_-]{30,}|BEGIN (RSA |EC |OPENSSH |PGP )?PRIVATE KEY|[0-9]{8,10}:AA[A-Za-z0-9_-]{33})")
PATRON_TLS = r"verify\s*=\s*False|rejectUnauthorized|NODE_TLS_REJECT_UNAUTHORIZED|CERT_NONE|_create_unverified_context|check_hostname\s*=\s*False|disable_warnings|curl [^\n]* -k "


def git(*a):
    return subprocess.run(["git", *a], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout


def pedir(url, datos=None, timeout=40):
    req = urllib.request.Request(url, data=json.dumps(datos).encode() if datos else None,
                                 headers={"Content-Type": "application/json", "User-Agent": "seguridad-rapida"})
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def pip_audit():
    cmd = ["uv", "run", "--with-requirements", "requirements.txt"]
    for e in EXTRAS:
        cmd += ["--with", e]
    cmd += ["--with", "pip-audit", "pip-audit", "--progress-spinner", "off", "-f", "json"]
    try:
        r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        datos = json.loads(r.stdout[r.stdout.index("{"):])
    except Exception as e:                                   # sin uv, sin red, etc.
        return None, f"no se pudo ejecutar pip-audit ({type(e).__name__})"
    paquetes = datos.get("dependencies", [])
    vulns = [(d["name"], d["version"], v["id"], v.get("fix_versions")) for d in paquetes for v in d.get("vulns", [])]
    return vulns, f"{len(paquetes)} paquetes auditados"


def acciones():
    usadas = set()
    for f in (RAIZ / ".github" / "workflows").glob("*.yml"):
        usadas.update(re.findall(r"uses:\s*([\w.-]+/[\w.-]+)@", f.read_text(encoding="utf-8", errors="replace")))
    if not usadas:
        return [], "sin acciones"
    qs = [{"package": {"name": n, "ecosystem": "GitHub Actions"}} for n in sorted(usadas)]
    try:
        res = pedir("https://api.osv.dev/v1/querybatch", {"queries": qs})["results"]
    except Exception as e:
        return None, f"OSV no respondió ({type(e).__name__})"
    return [(q["package"]["name"], v["id"]) for q, r in zip(qs, res) for v in r.get("vulns", [])], f"{len(usadas)} acciones consultadas"


def kev():
    try:
        d = pedir("https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json", timeout=60)
    except Exception as e:
        return None, f"CISA KEV no respondió ({type(e).__name__})"
    desde = (dt.date.today() - dt.timedelta(days=3)).isoformat()
    nuevas = [v for v in d["vulnerabilities"] if v["dateAdded"] >= desde]
    marcadas = [f"{v['cveID']} {v['vendorProject']} {v['product']}" for v in nuevas if re.search(TECNOLOGIAS, f"{v['vendorProject']} {v['product']}", re.I)]
    return marcadas, f"{len(nuevas)} entradas nuevas en 3 días"


def secretos():
    rastreados = [f for f in git("ls-files").splitlines() if not f.lower().endswith((".pdf", ".png", ".ico"))]
    hallazgos = []
    for f in rastreados:
        p = RAIZ / f
        try:
            for i, linea in enumerate(p.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                if re.search(PATRON_SECRETO, linea):
                    hallazgos.append(f"{f}:{i}")
        except OSError:
            pass
    hist = git("log", "--all", "-p", "--pretty=format:@@%h", "-G", PATRON_SECRETO, "--", ".", ":(exclude)*.pdf", ":(exclude)*.png")
    en_historial = sorted({l.split("@@")[1] for l in hist.splitlines() if l.startswith("@@")}) if re.search(r"^\+.*" + PATRON_SECRETO, hist, re.M) else []
    return hallazgos, en_historial, len(git("rev-list", "--all").split())


def tls():
    out = []
    for f in git("ls-files").splitlines():
        if f.endswith((".py", ".js", ".yml", ".yaml", ".html", ".toml", ".sh", ".bat")) and not f.startswith("privado/") and f != "scripts/seguridad_rapida.py":
            for i, l in enumerate((RAIZ / f).read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                if re.search(PATRON_TLS, l):
                    out.append(f"{f}:{i}")
    return out


def observaciones():
    o = []
    for f in sorted((RAIZ / ".github" / "workflows").glob("*.yml")):
        t = f.read_text(encoding="utf-8", errors="replace")
        if "permissions:" not in t:
            o.append(f"{f.name}: sin bloque `permissions` (usa los permisos por defecto del token)")
        for m in re.findall(r"pip install ([^\n]+)", t):
            if not re.search(r"==", m):
                o.append(f"{f.name}: pip install sin versión fijada ({m.strip()[:50]})")
    dc = RAIZ / ".devcontainer" / "devcontainer.json"
    if dc.exists() and "enableXsrfProtection false" in dc.read_text(encoding="utf-8", errors="ignore"):
        o.append("devcontainer: Streamlit con CORS y XSRF desactivados (solo Codespaces)")
    return o


def main():
    # La consola de Windows (cp1252) no imprime los emojis del veredicto
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    hoy = dt.date.today().isoformat()
    graves, avisos = [], []
    pa, nota_pa = pip_audit()
    if pa is None:
        avisos.append(nota_pa)
    else:
        graves += [f"dependencia {n} {v}: {i} (corregida en {fx})" for n, v, i, fx in pa]
    ac, nota_ac = acciones()
    if ac is None:
        avisos.append(nota_ac)
    else:
        graves += [f"GitHub Action {n}: {i}" for n, i in ac]
    kv, nota_kv = kev()
    if kv is None:
        avisos.append(nota_kv)
    else:
        graves += [f"CISA KEV: {x}" for x in kv]
    sec, hist, ncom = secretos()
    graves += [f"posible secreto en {x}" for x in sec] + [f"posible secreto en el historial (commit {x})" for x in hist]
    graves += [f"TLS: verificación desactivada en {x}" for x in tls()]
    obs = observaciones()
    veredicto = "🔴 ACCIÓN INMEDIATA" if graves else ("🟡 REVISAR" if avisos else "🟢 SIN NOVEDADES")
    res = {"fecha": hoy, "veredicto": veredicto, "graves": graves, "no_verificado": avisos, "observaciones_fijas": obs,
           "detalle": {"pip_audit": nota_pa, "actions": nota_ac, "kev": nota_kv, "commits_revisados": ncom}}
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"{veredicto} · {hoy}")
        for g in graves:
            print("  - " + g)
        for v in avisos:
            print("  ? no verificado: " + v)
        print(f"  (pip-audit: {nota_pa}; acciones: {nota_ac}; KEV: {nota_kv}; historial: {ncom} commits)")
        if obs:
            print("  Observaciones de endurecimiento (no cambian el veredicto):")
            for o in obs:
                print("   · " + o)
    sys.exit(1 if graves else 0)


if __name__ == "__main__":
    main()
