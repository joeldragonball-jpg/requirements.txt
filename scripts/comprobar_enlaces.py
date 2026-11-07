"""C148 · Comprobador de enlaces (voces, calendario, regulación). Sin IA y sin dependencias (urllib).

HEAD y, si falla, GET con User-Agent de navegador, 8 en paralelo. No se esquivan anti-bots: un 403/429 se anota como tal
(no como roto). Escribe docs/movil/enlaces.json y lista los 404 NUEVOS respecto a la ejecución anterior.
No edita research/tareas.csv. Verificación de certificados activa.
Uso: python scripts/comprobar_enlaces.py"""
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = ["explorador/voces.json", "eventos/calendario.toml", "explorador/regulacion.json"]
SALIDA = RAIZ / "docs" / "movil" / "enlaces.json"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")
RE_URL = re.compile(r"https?://[^\s\"'<>\\\]\[{}|^`]+")


def limpiar(u):
    """Quita puntuación final, pero conserva los paréntesis que cierran uno abierto dentro de la URL."""
    while u and u[-1] in ".,;:!?*":
        u = u[:-1]
    while u.endswith(")") and u.count(")") > u.count("("):
        u = u[:-1]
    return u


def extraer():
    urls = {}
    for f in FUENTES:
        p = RAIZ / f
        if not p.exists():
            continue
        for m in RE_URL.findall(p.read_text(encoding="utf-8")):
            urls.setdefault(limpiar(m), f)
    return urls


def probar(url):
    for metodo in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=metodo, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if metodo == "HEAD" and e.code in (400, 403, 404, 405, 406, 501, 503):
                continue  # algunos servidores no admiten HEAD: se reintenta con GET
            return e.code
        except Exception as e:
            ultimo = type(e).__name__
            if metodo == "GET":
                return ultimo
    return "error"


def etiqueta(c):
    if isinstance(c, int):
        if 200 <= c < 400:
            return "OK"
        return str(c)  # 403, 404, 503...: el código tal cual
    return "sin_respuesta"


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    urls = extraer()
    previo = {}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8")).get("enlaces", {})
        except Exception:
            previo = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        codigos = list(ex.map(probar, urls))
    hoy = date.today().isoformat()
    enlaces = {u: {"estado": etiqueta(c), "codigo": c if isinstance(c, int) else None, "fuente": urls[u], "fecha": hoy}
               for u, c in zip(urls, codigos)}
    cuenta = {}
    for v in enlaces.values():
        cuenta[v["estado"]] = cuenta.get(v["estado"], 0) + 1
    nuevos = [u for u, v in enlaces.items() if v["estado"] == "404" and previo.get(u, {}).get("estado") != "404"]
    SALIDA.write_text(json.dumps({"_nota": "Comprobador de enlaces (C148, sin IA). 403/429 = anti-bot, no roto.",
                                  "fecha": hoy, "total": len(enlaces), "recuento": cuenta, "enlaces": enlaces},
                                 ensure_ascii=False, indent=1), encoding="utf-8")
    for u in nuevos:
        print(f"404 NUEVO: {u}  ({urls[u]})")
    print(f"RESUMEN {hoy}: {len(enlaces)} enlaces · " + " · ".join(f"{k} {v}" for k, v in sorted(cuenta.items()))
          + f" · 404 nuevos: {len(nuevos)}")


if __name__ == "__main__":
    main()
