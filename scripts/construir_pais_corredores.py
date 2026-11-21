"""C306: cruza regulacion.json (CBDC/stablecoins/ETF) + cbdc-blockchains.json + corredores-liquidez.json
-> explorador/pais-corredores.json. Sin IA, sin red. Uso: python scripts/construir_pais_corredores.py"""
import json
from pathlib import Path

E = Path(__file__).resolve().parent.parent / "explorador"


def cargar(n):
    return json.loads((E / n).read_text(encoding="utf-8"))


reg, cbdc, cor = cargar("regulacion.json"), cargar("cbdc-blockchains.json"), cargar("corredores-liquidez.json")

# Clasificación manual de stablecoins privadas (revisar al cambiar regulacion.json). Resto: según etapa.
SC_MANUAL = {
    "cn": "vetadas", "eg": "vetadas", "et": "vetadas", "ir": "limitadas", "ru": "limitadas", "br": "limitadas",
    "in": "sin_marco", "eeuu": "permitidas_marco_aprobado_sin_vigor", "ca": "permitidas_marco_aprobado_sin_vigor",
    "uk": "permitidas_marco_aprobado_sin_vigor",
}
# Redes cripto con proyecto oficial (de cbdc-blockchains.json); ninguna es CBDC real en cadena pública.
REDES = {
    "PW": ["XRPL (Palau; stablecoin, piloto 2023)"],
    "UA": ["Stellar (e-hryvnia; piloto 2021-23, lo operaban TASCOMBANK y Bitt)"],
    "KZ": ["BNB Chain (tenge digital; sin evidencia en producción)"],
    "BT": ["XRPL (Bután; exploratorio) [VERIFICAR]"],
    "ME": ["XRPL (Montenegro; exploratorio) [VERIFICAR]"],
    "GE": ["XRPL (Georgia; exploratorio) [VERIFICAR]"],
    "CO": ["XRPL (Colombia; exploratorio) [VERIFICAR]"],
}
NOMBRE = {"TH": "Tailandia", "SA": "Arabia Saudí", "MX": "México", "MY": "Malasia", "PH": "Filipinas",
          "PW": "Palau", "UA": "Ucrania", "KZ": "Kazajistán", "BT": "Bután", "ME": "Montenegro",
          "GE": "Georgia", "CO": "Colombia"}
MAPA = {"FR": "EU"}  # Banco de Francia representa al Eurosistema


def sc_estado(j, etapa):
    if j in SC_MANUAL:
        return SC_MANUAL[j]
    if etapa is None:
        return "sin_dato"   # C363: jurisdicción añadida sin lectura de este tema; no se da por «sin marco»
    if etapa >= 4:
        return "permitidas_reguladas"
    return "en_tramite_o_consulta" if etapa >= 1 else "sin_marco"


def vacio(pid):
    return {"pais_id": pid, "nombre": NOMBRE.get(pid, pid), "jur": None, "cbdc": None, "stablecoins_privadas": None,
            "etf": None, "corredores": [], "redes_cripto_oficiales": [], "fuera_de_regulacion_json": True}


cel = {(c["jur"], c["tema"]): c for c in reg["celdas"]}
paises = {}
for j in reg["jurisdicciones"]:
    cb, sc, et = (cel.get((j["id"], t)) for t in ("cbdc", "stablecoins", "etf"))
    paises[j["pais_id"]] = {
        "pais_id": j["pais_id"], "nombre": j["nombre"], "jur": j["id"],
        "cbdc": {"etapa": cb["etapa"], "resumen": cb["estado"][:200]} if cb else None,
        "stablecoins_privadas": ({"clase": sc_estado(j["id"], sc["etapa"]), "etapa": sc["etapa"],
                                  "resumen": sc["estado"][:200]} if sc else None),
        "etf": {"etapa": et["etapa"]} if et else None,
        "corredores": [], "redes_cripto_oficiales": [], "fuera_de_regulacion_json": False,
    }
for c in cor["corredores"]:
    for pid in c["pais_id"]:
        pid = MAPA.get(pid, pid)
        paises.setdefault(pid, vacio(pid))["corredores"].append(
            {"id": c["id"], "nombre": c["nombre"], "estado": c["estado"][:90]})
for pid, r in REDES.items():
    paises.setdefault(pid, vacio(pid))["redes_cripto_oficiales"] += r

sal = {
    "paises": sorted(paises.values(), key=lambda p: p["pais_id"]),
    "metodo": ("Script reproducible scripts/construir_pais_corredores.py, sin IA. Parte automática: etapas y resúmenes "
               "de regulacion.json y pertenencia a corredores de corredores-liquidez.json. Parte manual (dentro del script): "
               "clasificación de stablecoins vetadas/limitadas (SC_MANUAL) y redes cripto con proyecto oficial (REDES, de "
               "cbdc-blockchains.json, leído el " + str(cbdc.get("leido")) + "). No hay lectura automática de web."),
    "aviso": "Análisis neutral, sin recomendación. Países sin celda en regulacion.json aparecen con valores null.",
    "fuente_corredores_revisado": cor["revisado"], "revisado": "2026-11-15", "caduca": "2027-02-15",
}
(E / "pais-corredores.json").write_text(json.dumps(sal, ensure_ascii=False, indent=1), encoding="utf-8")
print("paises:", len(sal["paises"]))
