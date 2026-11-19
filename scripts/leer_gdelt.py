"""C286: intensidad de prensa sobre conflicto por país y tema con GDELT DOC 2.0 (sin clave, sin IA).
Guarda explorador/conflictos-gdelt.json. Nivel S: volumen de cobertura (% de artículos monitorizados), NO hechos.
Sesgo: GDELT indexa sobre todo medios en inglés (y traducción automática); no mide víctimas ni eventos.
Espera entre peticiones (límite ~1 cada 5 s); certificados verificados. ACLED: no incluido (falta cuenta).
Uso: python scripts/leer_gdelt.py [--seco] [--completar]"""
import json
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "conflictos-gdelt.json"
API = "https://api.gdeltproject.org/api/v2/doc/doc?query={q}&mode=timelinevol&timespan=90d&format=json"
TERM = "(war OR conflict OR attack OR military OR sanctions)"
EN = {"ES": "Spain", "DE": "Germany", "FR": "France", "IT": "Italy", "NL": "Netherlands", "PL": "Poland", "US": "\"United States\"",
      "CN": "China", "JP": "Japan", "IN": "India", "GB": "\"United Kingdom\"", "RU": "Russia", "BR": "Brazil", "ZA": "\"South Africa\"",
      "ID": "Indonesia", "EG": "Egypt", "ET": "Ethiopia", "IR": "Iran", "AE": "\"United Arab Emirates\"", "SV": "\"El Salvador\"",
      "AR": "Argentina", "VE": "Venezuela", "CU": "Cuba"}
TEMAS = {"ucrania": "Ukraine war", "ormuz": "\"Strait of Hormuz\"", "taiwan": "Taiwan (military OR blockade OR invasion)",
         "sanciones": "sanctions (Russia OR Iran OR China)", "conflicto_global": "(war OR armed conflict)"}


def pedir(consulta):
    url = API.format(q=urllib.parse.quote(consulta))
    for n in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.4.0"}), timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            if n == 4:
                raise
            time.sleep(20 * (n + 1) if "429" in str(e) else 6)


def resumir(datos):
    dias = defaultdict(list)
    for s in datos.get("timeline", []):
        for p in s.get("data", []):
            dias[p["date"][:8]].append(float(p["value"]))
    serie = sorted((d, sum(v) / len(v)) for d, v in dias.items())
    if len(serie) < 40:
        raise ValueError("serie corta")
    v = [x for _, x in serie]
    ult = datetime.strptime(serie[-1][0], "%Y%m%d")
    # media de la ventana = media de los dias realmente disponibles (n); media 30 d = dias con fecha dentro de los 30 dias naturales finales
    v30 = [x for d, x in serie if (ult - datetime.strptime(d, "%Y%m%d")).days < 30]
    m90, m30 = sum(v) / len(v), sum(v30) / len(v30)
    top = sorted(serie, key=lambda t: -t[1])[:3]
    return {"media_30d": round(m30, 4), "media_90d": round(m90, 4), "ratio_30_90": round(m30 / m90, 2) if m90 else None,
            "dias": len(serie), "dias_en_media_30d": len(v30),
            "nota_media": f"media_90d = media de los {len(serie)} dias con dato (GDELT no devuelve 90 completos); media_30d = {len(v30)} dias con dato en los 30 naturales finales", "picos": [{"fecha": f"{d[:4]}-{d[4:6]}-{d[6:]}", "valor": round(x, 4)} for d, x in top]}


def main():
    paises = {p["id"]: p["pais"] for p in json.loads((RAIZ / "explorador" / "paises.json").read_text(encoding="utf-8"))["paises"]}
    consultas = [("tema", k, q) for k, q in TEMAS.items()] + [("pais", i, f"{EN[i]} {TERM}") for i in paises if i in EN]
    if "--seco" in sys.argv:
        print(len(consultas), "peticiones"); return
    out, fallos = {"temas": {}, "paises": {}}, []
    if "--completar" in sys.argv and SALIDA.exists():      # reintenta solo lo que falló (GDELT limita por IP y a veces devuelve 429)
        previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        out = {"temas": previo.get("temas", {}), "paises": previo.get("paises", {})}
    previo = json.loads(SALIDA.read_text(encoding="utf-8")) if SALIDA.exists() else {}
    for tipo, k, q in consultas:
        if k in out["temas" if tipo == "tema" else "paises"]:
            continue
        try:
            r = resumir(pedir(q))
            r["consulta"] = q
            if tipo == "pais":
                r["pais"] = paises[k]
            out["temas" if tipo == "tema" else "paises"][k] = r
        except Exception as e:
            fallos.append(f"{k}: {str(e)[:80]}")
            ant = (previo.get("temas" if tipo == "tema" else "paises") or {}).get(k)
            if ant:                      # conserva el dato bueno anterior y lo marca
                ant["conservado_sin_actualizar"] = previo.get("leido")
                out["temas" if tipo == "tema" else "paises"][k] = ant
        print(k, flush=True); time.sleep(10)
    if not out["paises"] and not out["temas"]:
        print("ERROR: GDELT sin datos (429?); no se sobrescribe", SALIDA, "fallos:", fallos); return
    doc = {"titulo": "Intensidad de cobertura de conflictos en prensa (GDELT DOC 2.0)", "nivel": "S",
           "leido": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
           "fuente": "GDELT Project, DOC 2.0 API, modo timelinevol, ventana 90 días (https://api.gdeltproject.org/api/v2/doc/doc)",
           "aviso": "Nivel S: mide volumen de cobertura (% de artículos monitorizados que casan con la consulta), no hechos, víctimas ni gravedad. "
                    "GDELT está sesgado hacia medios en inglés (y traducción automática), por lo que infrarrepresenta prensa local; "
                    "un pico puede ser una noticia mediática y no una escalada. Consultas con palabras clave en inglés: país + (war OR conflict OR attack OR military OR sanctions); "
                    "'United States', 'China' o 'Russia' salen altos por aparecer como actores en muchas noticias. Interpretar solo el cambio 30d frente a 90d, no comparar niveles entre países.",
           "unidad": 'media_30d, media_90d y valores de «picos»: % de los artículos monitorizados por GDELT que casan con la consulta (escala 1, sin multiplicador); ratio_30_90: cociente sin unidad (>1 = más cobertura reciente); dias: número de días', "acled": "falta: sin cuenta/clave de ACLED", "metodo": "ratio_30_90 = media de los 30 días naturales finales / media de la ventana (días con dato, ver dias y nota_media; <90 si GDELT devuelve menos) (>1 = más cobertura reciente)",
           **out, "fallos": fallos}
    SALIDA.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print("ok", len(out["paises"]), "países", len(out["temas"]), "temas", "fallos:", fallos)


if __name__ == "__main__":
    main()
