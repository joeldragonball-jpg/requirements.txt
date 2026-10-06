"""Resumen SIN IA de lo que el bot de noticias ya ha filtrado, para empezar una sesión de research sin repetir trabajo.

Uso (desde la carpeta del repo):
    python scripts/ultimas.py            # últimas 12 horas
    python scripts/ultimas.py 24         # últimas 24 horas
    python scripts/ultimas.py 12 7       # últimas 12 horas, solo nota >= 7

Lee noticias/noticias.json de la rama 'datos' (la misma que usa la app). No usa claves ni consume tokens de la API.
Pegar la salida (unas pocas líneas) al empezar la sesión cuesta mucho menos que volver a buscar lo mismo en la web.
"""
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

URL = "https://raw.githubusercontent.com/joeldragonball-jpg/requirements.txt/datos/noticias/noticias.json"
VOTO = {1: "👍", -1: "👎"}


def main():
    horas = float(sys.argv[1]) if len(sys.argv) > 1 else 12
    nota_min = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    try:
        db = json.loads(urllib.request.urlopen(URL + f"?t={int(datetime.now().timestamp())}", timeout=30).read())
    except Exception as e:
        sys.exit(f"No pude leer las noticias del bot ({e}). Si el repo es privado, esto necesita un token.")

    desde = datetime.now(timezone.utc) - timedelta(hours=horas)
    recientes = [n for n in db.get("noticias", []) if datetime.fromisoformat(n["fecha_envio"]) >= desde
                 and n.get("puntuacion", 0) >= nota_min]
    recientes.sort(key=lambda n: n["fecha_envio"], reverse=True)

    print(f"# Lo que el bot ya te envió en las últimas {horas:g} h ({len(recientes)} noticias"
          + (f", nota >= {nota_min}" if nota_min else "") + ")")
    print("# Ya cubierto: no hace falta buscarlo otra vez. Usa la web solo para lo que falte o para verificar.\n")
    for n in recientes:
        hora = datetime.fromisoformat(n["fecha_envio"]).astimezone().strftime("%d/%m %H:%M")
        marca = ("🚨 " if n.get("urgente") else "") + VOTO.get(n.get("valoracion"), "")
        url = n.get("url", "")
        if "news.google.com" in url:   # redirecciones larguísimas y opacas: gastan tokens y no se pueden abrir con fiabilidad
            url = ""
        print(f"- {hora} ⭐{n.get('puntuacion', '?')} [{n.get('tema', '')}] {marca} {n['titulo']} ({n.get('fuente', '')}) {url}".rstrip())
        if n.get("actualiza_apuntes"):
            print(f"    🧠 {n['actualiza_apuntes']}")

    temas = {}
    for n in recientes:
        temas[n.get("tema", "")] = temas.get(n.get("tema", ""), 0) + 1
    if temas:
        print("\n# Por tema: " + " · ".join(f"{t} {c}" for t, c in sorted(temas.items(), key=lambda x: -x[1])))
    no_interesa = [n["titulo"] for n in recientes if n.get("valoracion") == -1]
    if no_interesa:
        print(f"# Marcaste 👎 en {len(no_interesa)}: evita insistir en ese tipo de noticia.")
    pendientes = len(db.get("urg_vistos", []))
    print(f"# (El bot vigila alertas urgentes cada hora; ha evaluado {pendientes} titulares con palabras de alarma en total.)")


if __name__ == "__main__":
    main()
