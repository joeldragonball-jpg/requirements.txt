"""Índice de los datos del Explorador (sin IA, sin red, solo lectura de los JSON).

Genera explorador/indice/: por-pais.json, por-tema.json, cambios.json (7 y 30 días), informes.json
(TODOS los informes por tema y país) e INDICE.md («dato → archivo → campo»).
Uso: python scripts/indice_datos.py
"""
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
EXP = RAIZ / "explorador"
SAL = EXP / "indice"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import indice_investigacion as ii  # noqa: E402


def cargar(nombre):
    p = EXP / nombre
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def escribir(nombre, obj):
    (SAL / nombre).write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def fecha_dia(f):
    """AAAA-MM-DD completa o None (las fechas con solo año o mes no cuentan como cambio reciente)."""
    return f if isinstance(f, str) and re.match(r"^\d{4}-\d{2}-\d{2}$", f) else None


def main():
    SAL.mkdir(exist_ok=True)
    hoy = date.today()
    reg, dat = cargar("regulacion.json"), cargar("datos.json")
    nombre_jur = {j["id"]: j["nombre"] for j in reg.get("jurisdicciones", [])}
    nombre_tema = {t["id"]: t["nombre"] for t in reg.get("temas", [])}
    pais_de_jur = {j["id"]: j.get("pais_id") for j in reg.get("jurisdicciones", [])}

    # Cada elemento lleva la huella común: tipo, archivo, campo, pais_id, tema, fecha, nivel, revisar, texto
    elems = []
    for c in reg.get("celdas", []):
        elems.append({
            "tipo": "celda_regulacion", "archivo": "regulacion.json", "campo": f"celdas[{c['jur']}.{c['tema']}]",
            "pais_id": [c.get("pais_id") or pais_de_jur.get(c["jur"])], "tema": c["tema"],
            "fecha": c.get("fecha"), "revisado": c.get("revisado"), "caduca": c.get("caduca"),
            "nivel": c.get("nivel"), "revisar": c.get("revisar", False), "etapa": c.get("etapa"),
            "texto": (c.get("estado") or "")[:160]})
    for m in dat.get("movimientos", []):
        elems.append({
            "tipo": "movimiento", "archivo": "datos.json", "campo": f"movimientos[{m['fecha']} {m['actor']}]",
            "pais_id": m.get("pais_id", []), "tema": m.get("capa"), "fecha": m["fecha"],
            "nivel": m.get("nivel"), "revisar": m.get("revisar", False), "texto": m["texto"][:160]})
    for cp in dat.get("capas", []):
        for k, v in cp.items():
            if isinstance(v, list):
                for i, e in enumerate(v):
                    if isinstance(e, dict) and "pais" in e:
                        elems.append({
                            "tipo": "hecho_capa" if "t" in e else "cifra_capa", "archivo": "datos.json",
                            "campo": f"capas[{cp['id']}].{k}[{i}]", "pais_id": e.get("pais_id", []),
                            "tema": cp["id"], "fecha": None, "nivel": e.get("nivel"),
                            "revisar": e.get("revisar", False), "texto": (e.get("t") or e.get("e") or "")[:160]})

    por_pais, por_tema = {}, {}
    for e in elems:
        for p in e["pais_id"] or ["(sin país)"]:
            por_pais.setdefault(p, []).append(e)
        por_tema.setdefault(e["tema"] or "(sin tema)", []).append(e)

    informes = ii.fichas_todas()
    inf_pais, inf_tema = {}, {}
    for i in informes:
        for p in i["pais_id"] or ["(sin país)"]:
            inf_pais.setdefault(p, []).append(i["ruta"])
        inf_tema.setdefault(i["tema"], []).append(i["ruta"])

    def cambios(dias):
        lim = (hoy - timedelta(days=dias)).isoformat()

        def f(e):
            return fecha_dia(e.get("revisado")) or fecha_dia(e.get("fecha")) or ""
        sel = sorted((e for e in elems if f(e) >= lim), key=f, reverse=True)
        return {"desde": lim, "elementos": sel, "informes": [i["ruta"] for i in informes if i["fecha"] >= lim]}

    cab = {"generado": hoy.isoformat(),
           "aviso": "Autogenerado por scripts/indice_datos.py; no editar a mano. Informativo, sin recomendaciones."}
    escribir("por-pais.json", {**cab, "nombres_jurisdiccion": nombre_jur,
                               "paises": {p: {"datos": v, "informes": inf_pais.get(p, [])} for p, v in sorted(por_pais.items())},
                               "informes_sin_pais": inf_pais.get("(sin país)", [])})
    escribir("por-tema.json", {**cab, "nombres_tema": nombre_tema,
                               "temas": {t: {"datos": v} for t, v in sorted(por_tema.items())},
                               "informes_por_tema": inf_tema})
    c7, c30 = cambios(7), cambios(30)
    escribir("cambios.json", {**cab, "ultimos_7_dias": c7, "ultimos_30_dias": c30})
    escribir("informes.json", {**cab, "total": len(informes), "informes": informes})

    md = [
        "# Índice de datos del Explorador (autogenerado)", "",
        f"Generado el {hoy.isoformat()} por `python scripts/indice_datos.py` (sin IA, solo lectura de los JSON). No editar a mano.", "",
        "## Cómo se usa",
        "Buscar un dato aquí → abrir el archivo → ir al campo. `por-pais.json`, `por-tema.json`, `cambios.json` e `informes.json` "
        "enumeran cada elemento con su huella común.", "",
        "## Dato → archivo → campo", "| Dato | Archivo | Campo |", "|---|---|---|",
        "| Etapa regulatoria (0-5) por país y tema | `regulacion.json` | `celdas[].etapa` (`jur`, `tema`) |",
        "| Estado, próxima fecha, hitos y lo que falta | `regulacion.json` | `celdas[].estado`, `proxima`, `hitos`, `falta` |",
        "| Política monetaria (dirección y valor) | `regulacion.json` | `celdas[tema=politica].dir`, `valor` |",
        "| Países y jurisdicciones | `regulacion.json` | `jurisdicciones[]` (`id`, `nombre`, `pais_id`) |",
        "| Hechos por capa (producción, piloto, plan, XRP/XLM) | `datos.json` | `capas[].produccion/piloto/plan/xrp[]` |",
        "| Cifras clave de cada capa | `datos.json` | `capas[].cifras[]` |",
        "| Línea de tiempo de eventos | `datos.json` | `movimientos[]` |",
        "| Informes de origen | `datos.json` / `regulacion.json` | `informe` / `celdas[].informes` / `base_informes` |",
        "| Voces y predicciones | `voces.json` | `voces[]`, `canales[]` |",
        "| Paneles de mercado (stablecoins, RWA, tipos, defensa…) | `paneles.json` | claves de primer nivel |",
        "| Calificaciones soberanas | `calificaciones.json` | `paises` |",
        "| Deuda (FMI) | `deuda-fmi.json` | `paises`, `anios` |",
        "| Reservas y oro | `reservas.json` | `reservas`, `oro`, `bancos_centrales` |",
        "| Valoración sectorial | `valoracion.json` | `filas[]` |",
        "| Bancos europeos (EBA) | `bancos-eba.json` | `bancos[]` |",
        "| Módulos del Centro | `centro.json` | `modulos[]` |",
        "| Todos los informes por tema y país | `indice/informes.json` | `informes[]` (`tema`, `pais_id`) |",
        "| Qué cambió en 7 y 30 días | `indice/cambios.json` | `ultimos_7_dias`, `ultimos_30_dias` |", "",
        "## Esquema común (campos opcionales y aditivos: no sustituyen a los antiguos)",
        "| Campo | Tipo | Significado |", "|---|---|---|",
        "| `pais_id` | texto o lista | Código de país en mayúsculas (ISO 3166-1 alfa-2). Pseudocódigos: `EU` Unión Europea, `EA` zona euro, `INT` internacional o supranacional |",
        "| `nivel` | `P` / `S` / `V` | Certeza de la fuente: P = primaria leída, S = secundaria, V = por verificar. Mismo criterio que `fuente` y `k` |",
        "| `fecha` | AAAA[-MM[-DD]] | Fecha del hecho o del último cambio (ya existía en celdas y movimientos) |",
        "| `url` | http(s):// | Fuente enlazable (ya existía en 76 celdas) |",
        "| `revisar` | verdadero/falso | Hay que volver a comprobarlo (nivel S/V o celda sin dato) |",
        "| `caduca` | AAAA-MM-DD | Desde cuándo el dato debe darse por viejo. En celdas: `revisado` + 90 días (convención de C43, ajustable) |",
        "| `sesgo` | texto o lista | Sesgo de la fuente (promoción, conflicto de interés…). Reservado; sin rellenar aún |",
        "| `perspectivas` | texto o lista | Caso alcista, bajista u otras lecturas. Reservado; sin rellenar aún |", "",
        "Rellenado hoy: `regulacion.json` (jurisdicciones: `pais_id`; celdas: `pais_id`, `nivel`, `revisar` y `caduca` si hay `revisado`) y "
        "`datos.json` (movimientos y hechos o cifras de las capas con país: `pais_id`, `nivel`, `revisar` cuando procede). "
        "El resto de JSON, sin tocar. `python scripts/revisar_explorador.py` comprueba la forma de estos campos.", "",
        "## Recuento",
        f"- Elementos con huella común: {len(elems)} ({len(por_pais)} países, {len(por_tema)} temas).",
        f"- Informes indexados: {len(informes)}.",
        f"- Cambios en 7 días: {len(c7['elementos'])} datos y {len(c7['informes'])} informes; en 30 días: "
        f"{len(c30['elementos'])} y {len(c30['informes'])}.", "",
        "## Informes por tema", "| Tema | Informes |", "|---|---|"]
    for t, v in sorted(inf_tema.items()):
        md.append(f"| {t} | {len(v)} |")
    (SAL / "INDICE.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"explorador/indice/: {len(elems)} elementos, {len(informes)} informes, "
          f"cambios 7d={len(c7['elementos'])}, 30d={len(c30['elementos'])}")


if __name__ == "__main__":
    main()
