"""Órbita para la tablet (C141): genera docs/orbita/index.html, el Explorador completo (Resumen, Capas, Línea de tiempo,
Calendario, Matriz, Noticias, Voces, Países, España y Paneles) como página suelta, sin Streamlit, sin IA y sin claves.
Usa el mismo código que la pestaña «Cerebro» del PC (explorador.py) pero en modo público: NO incluye nada de privado/
(ni el contraste ni el cruce con la tesis). Uso: python scripts/construir_orbita.py"""
import sys
import types
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

# explorador.py importa Streamlit solo para la pestaña del PC; aquí se sustituye por un módulo vacío (cache_data = no hace nada)
st = types.ModuleType("streamlit")
st.cache_data = lambda *a, **k: (a[0] if a and callable(a[0]) else (lambda f: f))
comp = types.ModuleType("streamlit.components")
comp_v1 = types.ModuleType("streamlit.components.v1")
sys.modules.update({"streamlit": st, "streamlit.components": comp, "streamlit.components.v1": comp_v1})
st.components = comp
comp.v1 = comp_v1

import explorador  # noqa: E402

SALIDA = RAIZ / "docs" / "orbita"
CABECERA = ('<meta name="theme-color" content="#050816"><meta name="mobile-web-app-capable" content="yes">'
            '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Órbita">'
            '<title>Órbita · Tablero de inteligencia</title><link rel="manifest" href="manifest.webmanifest">'
            '<link rel="icon" type="image/png" href="../assets/icono-192.png"><link rel="apple-touch-icon" href="../assets/icono-180.png">'
            '<style>html,body{background:#050816;margin:0;min-height:100%}</style>')


def main():
    html = explorador._html(None, publico=True)
    if "privado" in html.lower() and "contraste-tesis" in html.lower():
        sys.exit("La página pública menciona archivos de privado/: no se escribe.")
    html = html.replace("<head>", "<head>" + CABECERA, 1)
    SALIDA.mkdir(parents=True, exist_ok=True)
    (SALIDA / "index.html").write_text(html, encoding="utf-8")
    (SALIDA / "manifest.webmanifest").write_text(
        '{"name":"Órbita · Tablero de inteligencia","short_name":"Órbita","start_url":"./","scope":"./","display":"standalone",'
        '"background_color":"#050816","theme_color":"#050816","icons":[{"src":"../assets/icono-192.png","sizes":"192x192","type":"image/png"}]}',
        encoding="utf-8")
    print(f"docs/orbita/index.html: {len(html) // 1024} KB (versión pública, sin privado/)")


if __name__ == "__main__":
    main()
