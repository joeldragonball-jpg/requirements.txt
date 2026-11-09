"""C201 (9-nov-2026): rellena sin IA y sin claves lo que antes se escribía a mano en explorador/.

- indicadores-manual.json · EE. UU.: IPC interanual (FRED CPIAUCNS, sin desestacionalizar = el titular oficial), paro (UNRATE) y PIB
  trimestral anualizado (A191RL1Q225SBEA). Solo se sobrescribe si FRED trae un periodo MÁS NUEVO que el guardado; el dato pasa a nivel S
  (FRED reproduce BLS/BEA, pero no se leyó la nota oficial) y la fuente apunta a la serie de FRED.
- tipos-manual.json · Suecia: tipo de la Riksbank (API abierta, diario). Se añade o refresca la fila «se».
- Lo que NO se automatiza (se queda a mano con Chrome): RBA (Australia: bloquea scripts), RBNZ, salarios mínimos, pobreza, Gini y
  los datos de Rusia, Japón, China e India (sin serie abierta mensual fiable).

Uso: python scripts/automatizar_manuales.py [--seco]   (--seco = solo muestra lo que cambiaría)
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import actualizar_paneles as ap  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
IND = RAIZ / "explorador" / "indicadores-manual.json"
TIP = RAIZ / "explorador" / "tipos-manual.json"
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={i}&cosd={d}"
RIKSBANK = "https://api.riksbank.se/swea/v1/Observations/SECBREPOEFF/{d}"


def descargar_fred(url):
    """FRED corta la conexión a los User-Agent de navegador y acepta el de curl; hasta 3 intentos."""
    import time
    import urllib.request
    for n in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.4.0"}), timeout=40).read().decode("utf-8")
        except Exception:
            if n == 2:
                raise
            time.sleep(3)


def serie_fred(i, desde):
    filas = [f.split(",") for f in descargar_fred(FRED.format(i=i, d=desde)).strip().splitlines()[1:]]
    return [(f[0], float(f[1])) for f in filas if len(f) == 2 and f[1] not in ("", ".")]


def us_indicadores():
    """{clave: (valor, periodo, fuente_url, definición)} con lo último de FRED."""
    r = {}
    s = serie_fred("CPIAUCNS", "2024-12-01")
    d = dict(s)
    f, v = s[-1]
    ant = f"{int(f[:4]) - 1}{f[4:]}"
    if ant in d:
        r["ipc"] = (round((v / d[ant] - 1) * 100, 1), f[:7], "https://fred.stlouisfed.org/series/CPIAUCNS",
                    "IPC-U de EE. UU., variación interanual del índice SIN desestacionalizar (el del titular de la BLS), calculada con FRED.")
    f, v = serie_fred("UNRATE", "2025-01-01")[-1]
    r["paro"] = (v, f[:7], "https://fred.stlouisfed.org/series/UNRATE", "Tasa de paro de EE. UU. (BLS), desestacionalizada, vía FRED.")
    f, v = serie_fred("A191RL1Q225SBEA", "2025-01-01")[-1]
    r["pib"] = (v, f"{f[:4]}-Q{(int(f[5:7]) - 1) // 3 + 1}", "https://fred.stlouisfed.org/series/A191RL1Q225SBEA",
                "PIB real de EE. UU., variación trimestral anualizada (BEA), vía FRED; es la estimación más reciente de FRED.")
    return r


def actualizar_indicadores(seco):
    datos = json.loads(IND.read_text(encoding="utf-8"))
    cambios = []
    for clave, (valor, periodo, url, definicion) in us_indicadores().items():
        actual = datos.get("US", {}).get(clave)
        if actual is None or str(actual.get("fecha") or "") >= periodo:
            continue
        cambios.append(f"US {clave}: {actual.get('valor')} ({actual.get('fecha')}) → {valor} ({periodo})")
        actual.update({"valor": valor, "fecha": periodo, "fuente": url, "nivel": "S", "definicion": definicion})
    if cambios and not seco:
        datos["_actualizado"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        IND.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return cambios


def actualizar_riksbank(seco):
    obs = json.loads(ap.descargar(RIKSBANK.format(d="2025-01-01")))
    obs = [o for o in obs if o.get("value") is not None]
    ult = obs[-1]
    cambio = next((o for o in reversed(obs) if o["value"] != ult["value"]), None)
    desde = next((o for o in obs if o["date"] > cambio["date"] and o["value"] == ult["value"]), ult) if cambio else obs[0]
    pb = round((ult["value"] - cambio["value"]) * 100) if cambio else None
    fila = {"jur": "se", "id": "SE", "pais": "Suecia", "banco": "Riksbank (tipo de referencia)",
            "valor": f"{ult['value']:.2f} %".replace(".", ","), "num": ult["value"], "ultimo_cambio": desde["date"], "cambio_pb": pb,
            "dato_de": ult["date"], "fuente": "Riksbank, API SWEA (serie SECBREPOEFF), leída por script", "url": "https://www.riksbank.se/en-gb/statistics/interest-rates-and-exchange-rates/",
            "nivel": "P"}
    datos = json.loads(TIP.read_text(encoding="utf-8"))
    tipos = datos.setdefault("tipos", [])
    previa = next((t for t in tipos if t.get("jur") == "se"), None)
    if previa and previa.get("dato_de") == fila["dato_de"] and previa.get("num") == fila["num"]:
        return []
    if previa:
        tipos[tipos.index(previa)] = fila
    else:
        tipos.append(fila)
    if not seco:
        TIP.write_text(json.dumps(datos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return [f"SE Riksbank: {fila['valor']} (dato de {fila['dato_de']}, último cambio {fila['ultimo_cambio']})"]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    seco = "--seco" in sys.argv
    for nombre, f in (("indicadores", actualizar_indicadores), ("tipos", actualizar_riksbank)):
        try:
            c = f(seco)
            print(f"{nombre}: {'sin cambios' if not c else ''}")
            for x in c:
                print("  ·", x, "(simulado)" if seco else "")
        except Exception as e:
            print(f"{nombre}: AVISO {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
