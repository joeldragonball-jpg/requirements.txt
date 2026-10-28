"""Exporta a explorador/prueba-datos.json lo que la Órbita calcula en Python y no está en los JSON:
calendario de eventos, documentos por capa y totales de la biblioteca. Solo lo usa el prototipo
explorador/prueba-diseno.html (C41C). Sin IA. No incluye nada de privado/.

Uso: python scripts/exportar_prueba_orbita.py
"""
import json
import re
import sys
import types
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

# explorador.py importa streamlit solo para mostrarse en la app; aquí basta un sustituto vacío
st = types.ModuleType("streamlit")
st.cache_data = lambda *a, **k: (lambda f: f)
sys.modules["streamlit"] = st
sys.modules["streamlit.components"] = types.ModuleType("streamlit.components")
sys.modules["streamlit.components.v1"] = types.ModuleType("streamlit.components.v1")
import explorador  # noqa: E402

html = explorador._html(None)
m = re.search(r'<script id="datos" type="application/json">(.*?)</script>', html, re.S)
if not m:
    raise SystemExit("No encuentro el bloque de datos en la página de la Órbita")
datos = json.loads(m.group(1).replace("<\\/", "</").replace("<\\!--", "<!--"))

salida = {
    "calendario": datos.get("calendario"),
    "biblioteca": datos.get("biblioteca"),
    "docs": {c["id"]: c.get("docs") for c in datos.get("capas", [])},
}
destino = RAIZ / "explorador" / "prueba-datos.json"
destino.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ok:", destino, destino.stat().st_size, "bytes;", len((salida["calendario"] or {}).get("eventos", [])), "eventos")
