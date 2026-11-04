"""Valida que los ids de país de los ficheros de explorador/ resuelven en explorador/ids/paises.json (C99).
Sin IA. Sale con código 1 si algún id no resuelve. Uso: python scripts/validar_ids.py"""
import json, sys, pathlib, re, tomllib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
EXP = RAIZ / "explorador"


def cargar(nombre):
    return json.loads((EXP / nombre).read_text(encoding="utf-8"))


def main():
    tabla = cargar("ids/paises.json")["paises"]
    iso3 = {v["iso3"]: k for k, v in tabla.items()}
    alias = {v["alias_regulacion"]: k for k, v in tabla.items()}
    fallos, vistos = [], 0

    def comprobar(fichero, ids, valido):
        nonlocal vistos
        for i in ids:
            vistos += 1
            if not valido(i):
                fallos.append(f"{fichero}: id «{i}» no resuelve")

    for f in ("paises.json", "elecciones.json", "estabilidad.json"):
        comprobar(f, [p["id"] for p in cargar(f)["paises"]], lambda i: i in tabla)
    comprobar("calificaciones.json", [p["id"] for p in cargar("calificaciones.json")["paises"]], lambda i: i in iso3)
    reg = cargar("regulacion.json")["jurisdicciones"]
    comprobar("regulacion.json (id)", [j["id"] for j in reg], lambda i: i in alias)
    comprobar("regulacion.json (pais_id)", [j["pais_id"] for j in reg], lambda i: i in tabla)
    for j in reg:  # coherencia id <-> pais_id
        if alias.get(j["id"]) != j["pais_id"]:
            fallos.append(f"regulacion.json: {j['id']} ↔ {j['pais_id']} no coincide con la tabla")
    ind = cargar("indicadores-manual.json")
    comprobar("indicadores-manual.json", [k for k in ind if not k.startswith("_")], lambda i: i in tabla)

    # C100: cada evento de calendario.toml lleva id ev-AAAA-MM[-DD]-slug, único (hay fechas solo con mes)
    evs = tomllib.loads((RAIZ / "eventos" / "calendario.toml").read_text(encoding="utf-8"))["eventos"]
    repetidos = set()
    for e in evs:
        vistos += 1
        i = e.get("id")
        if not i or not re.fullmatch(r"ev-\d{4}-\d{2}(-\d{2})?-[a-z0-9-]+", i):
            fallos.append(f"calendario.toml: «{e.get('titulo','?')[:40]}» sin id válido")
        elif i in repetidos:
            fallos.append(f"calendario.toml: id repetido {i}")
        repetidos.add(i)
    rev = json.loads((RAIZ / "eventos" / "revisados.json").read_text(encoding="utf-8"))["revisados"]
    for clave, v in rev.items():
        if v.get("id") and v["id"] not in repetidos:
            fallos.append(f"revisados.json: {clave} apunta a un id inexistente")

    # C91: cada hilo de enlaces.json apunta solo a cosas que existen
    enl = cargar("enlaces.json")
    voces = {v["id"] for v in cargar("voces.json")["voces"]}
    texto_pred = (RAIZ / "informes" / "predicciones.md").read_text(encoding="utf-8")
    preds = {f"p{int(m):03d}" for m in re.findall(r"^\|\s*(\d+)\s*\|", texto_pred, re.M)}
    for h in enl["enlaces"]:
        h_id = h["id"]
        for campo, validos in (("pais", set(tabla)), ("evento", repetidos), ("voz", voces), ("pred", preds), ("activo", set(enl["activos_validos"]))):
            for x in h.get(campo, []):
                vistos += 1
                if x not in validos:
                    fallos.append(f"enlaces.json {h_id}: {campo} «{x}» no existe")
        for ruta in h.get("informe", []):
            vistos += 1
            if not (RAIZ / ruta).exists():
                fallos.append(f"enlaces.json {h_id}: informe «{ruta}» no existe")
        if "tesis" in json.dumps(h, ensure_ascii=False).lower():
            fallos.append(f"enlaces.json {h_id}: menciona la tesis (debe vivir en privado/)")

    print(f"ids comprobados: {vistos} · fallos: {len(fallos)}")
    for x in fallos:
        print(" -", x)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
