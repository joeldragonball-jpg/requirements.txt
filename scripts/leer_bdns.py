#!/usr/bin/env python3
"""Lee la BDNS (infosubvenciones.es, API pública sin clave) y agrega las
concesiones por órgano concedente y beneficiario. Sin IA, sin claves.

Uso:  python scripts/leer_bdns.py [--desde dd/mm/aaaa] [--hasta dd/mm/aaaa] [--dias 365]
Salida: explorador/espana-subvenciones.json

LÍMITES HONESTOS (también van dentro del JSON):
- BDNS recoge la CONCESIÓN, no el pago. Importe concedido != dinero cobrado.
- Los filtros de la API por nivel1 e importe NO funcionan (se ignoran); solo
  fechaDesde/fechaHasta. Por eso se pagina por semanas y se agrega en local.
- Personas físicas: la BDNS las enmascara (****1234* NOMBRE). Se agregan
  en un cajón «personas físicas (enmascaradas)» y NO se listan nunca.
- Retraso de publicación por entidad no medido [VERIFICAR]; subvenciones
  nominativas/directas pueden estar incompletas [VERIFICAR].
- Un beneficiario repetido NO implica irregularidad (p. ej. universidades,
  ONG, Cruz Roja reciben muchas convocatorias legítimas).
"""
import argparse, collections, datetime as dt, json, re, sys, time, urllib.request, urllib.parse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from leyendas_contratacion import LEYENDA_SUBVENCIONES

BASE = "https://www.infosubvenciones.es/bdnstrans/api/"
RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "espana-subvenciones.json"
UA = {"User-Agent": "cartera-github/leer_bdns (investigacion personal; sin IA)"}


def get(endpoint, **p):
    p.setdefault("vpd", "GE")
    url = BASE + endpoint + "?" + urllib.parse.urlencode(p, safe="/")
    for intento in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)
        except Exception as e:
            if intento == 3:
                raise
            time.sleep(3 * (intento + 1))


def es_persona_fisica(b):
    # enmascaradas: empiezan por asteriscos; personas jurídicas: letra + 8 dígitos/alfanum.
    return b.startswith("*") or not re.match(r"^[A-Z]\d{7}[0-9A-Z]\b", b)


def semanas(d0, d1):
    a = d0
    while a <= d1:
        b = min(a + dt.timedelta(days=6), d1)
        yield a, b
        a = b + dt.timedelta(days=1)


def f(d):
    return d.strftime("%d/%m/%Y")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=365)
    ap.add_argument("--desde")
    ap.add_argument("--hasta")
    a = ap.parse_args()
    hoy = dt.date.today()
    hasta = dt.datetime.strptime(a.hasta, "%d/%m/%Y").date() if a.hasta else hoy - dt.timedelta(days=1)
    desde = dt.datetime.strptime(a.desde, "%d/%m/%Y").date() if a.desde else hasta - dt.timedelta(days=a.dias - 1)

    por_n1 = collections.defaultdict(lambda: [0, 0.0])
    por_org = collections.defaultdict(lambda: [0, 0.0])
    por_ben = collections.defaultdict(lambda: [0, 0.0])
    por_instr = collections.defaultdict(lambda: [0, 0.0])
    fisicas = [0, 0.0]
    top = []  # mayores concesiones a personas jurídicas
    total = [0, 0.0]
    neg = 0
    for d0, d1 in semanas(desde, hasta):
        pag = 0
        while True:
            d = get("concesiones/busqueda", pageSize=5000, page=pag, order="fechaConcesion",
                    direccion="desc", fechaDesde=f(d0), fechaHasta=f(d1))
            for c in d["content"]:
                imp = c.get("importe") or 0.0
                if imp < 0:
                    neg += 1
                total[0] += 1
                total[1] += imp
                n1 = c.get("nivel1") or "?"
                por_n1[n1][0] += 1
                por_n1[n1][1] += imp
                org = f"{n1} | {c.get('nivel2') or ''} | {c.get('nivel3') or ''}"
                por_org[org][0] += 1
                por_org[org][1] += imp
                ins = (c.get("instrumento") or "?").strip()
                por_instr[ins][0] += 1
                por_instr[ins][1] += imp
                b = (c.get("beneficiario") or "").strip()
                if es_persona_fisica(b):
                    fisicas[0] += 1
                    fisicas[1] += imp
                else:
                    por_ben[b][0] += 1
                    por_ben[b][1] += imp
                    if imp >= 1_000_000:
                        top.append({"codConcesion": c.get("codConcesion"), "fecha": c.get("fechaConcesion"),
                                    "beneficiario": b, "importe": imp, "organo": org,
                                    "convocatoria": (c.get("convocatoria") or "")[:160],
                                    "numeroConvocatoria": c.get("numeroConvocatoria")})
                        top.sort(key=lambda x: -x["importe"])
                        del top[40:]
            pag += 1
            if d.get("last") or not d["content"]:
                break
        print(f"  {d0}..{d1}: acumulado {total[0]:,} concesiones", file=sys.stderr)

    def tops(dic, n, clave="clave"):
        return [{clave: k, "n": v[0], "importe": round(v[1], 2)}
                for k, v in sorted(dic.items(), key=lambda kv: -kv[1][1])[:n]]

    tb = tops(por_ben, 25, "beneficiario")
    suma_juridicas = sum(v[1] for v in por_ben.values())
    sh10 = sum(x["importe"] for x in tb[:10]) / suma_juridicas if suma_juridicas else 0

    # extras: sanciones y partidos (últimas entradas, no agregado histórico)
    sanc = get("sanciones/busqueda", pageSize=2000, page=0)
    sanc_c = sanc["content"]
    sanc_res = {"total_registros_bdns": sanc.get("totalElements"),
                "muestra_leida": len(sanc_c),
                "por_nivel1": dict(collections.Counter(s.get("nivel1") for s in sanc_c)),
                "importe_multa_muestra": round(sum(s.get("importeMulta") or 0 for s in sanc_c), 2),
                "nota": "Muestra de la primera página de la API (orden por defecto), NO el histórico completo ni 'las últimas'. Sancionados no se listan (pueden ser personas físicas)."}
    part = get("partidospoliticos/busqueda", pageSize=2000, page=0)
    pc = part["content"]
    part_res = {"total_registros_bdns": part.get("totalElements"), "muestra_leida": len(pc),
                "importe_muestra": round(sum(p.get("importe") or 0 for p in pc), 2),
                "ejemplos_organo": sorted({(p.get("nivel3") or "")[:80] for p in pc})[:5],
                "nota": "Endpoint partidospoliticos = concesiones a grupos/partidos (incl. grupos municipales). Solo muestra de una página; agregado completo [VERIFICAR]."}
    gb = get("grandesbeneficiarios/busqueda", pageSize=2000, page=0)
    gbc = gb["content"]
    gb_res = {"total_registros_bdns": gb.get("totalElements"), "muestra_leida": len(gbc),
              "nota": "Endpoint de grandes beneficiarios por ejercicio; solo primera página, sin ordenar por importe (la ordenación por importe da timeout). No se usa para rankings."}

    out = {
        "id": "espana-subvenciones",
        "generado": hoy.isoformat(),
        "fuente": {"nombre": "BDNS - Base de Datos Nacional de Subvenciones (IGAE/Hacienda)",
                   "url": "https://www.infosubvenciones.es/bdnstrans/",
                   "api": BASE, "nivel": "P (API oficial leída)",
                   "ventana": {"desde": desde.isoformat(), "hasta": hasta.isoformat(),
                               "criterio": "fechaConcesion"}},
        "unidad": "EUR", "escala": 1,
        "nota_unidad": "importe = euros (escala 1, sin dividir). Para mostrar: M€ = importe/1e6; mil M€ = importe/1e9.",
        "totales": {"concesiones": total[0], "importe": round(total[1], 2),
                    "concesiones_importe_negativo": neg,
                    "personas_fisicas_enmascaradas": {"n": fisicas[0], "importe": round(fisicas[1], 2)},
                    "personas_juridicas": {"beneficiarios_distintos": len(por_ben), "importe": round(suma_juridicas, 2)}},
        "por_nivel": tops(por_n1, 10, "nivel"),
        "por_organo": tops(por_org, 25, "organo"),
        "por_instrumento": tops(por_instr, 8, "instrumento"),
        "mayores_beneficiarios": tb,
        "concentracion": {"top10_beneficiarios_pct_importe_juridicas": round(sh10 * 100, 1),
                          "nota": "Concentración != irregularidad: muchos son entes públicos, universidades, entidades de gestión de ayudas europeas."},
        "mayores_concesiones": top[:25],
        "sanciones": sanc_res,
        "leyenda": LEYENDA_SUBVENCIONES,
        "partidos_politicos": part_res,
        "grandes_beneficiarios": gb_res,
        "limites": [
            "BDNS publica concesiones, no pagos ni ejecución.",
            "Filtros de la API por nivel e importe no funcionan; todo se agrega en local por fechaConcesion.",
            "Personas físicas enmascaradas por la propia BDNS; no se listan.",
            "Retraso de publicación por entidad y completitud de subvenciones nominativas/directas: [VERIFICAR].",
            "La API avisa de que los datos pueden corregirse después de su extracción (dinámicos).",
            "Beneficiario repetido o concentración de importe NO implica irregularidad.",
        ],
    }
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK {SALIDA} · {total[0]:,} concesiones · {total[1]/1e6:,.0f} M€", file=sys.stderr)


if __name__ == "__main__":
    main()
