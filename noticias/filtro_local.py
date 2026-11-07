#!/usr/bin/env python3
"""Filtro local de noticias SIN IA (C170, 7-nov-2026). Solo biblioteca estándar.

Puntúa titulares con reglas (fuente, palabras clave, verbo, fecha, token, dedup) y
BM25 contra los temas e intereses de noticias/config.toml. El resumen es el titular
+ la primera frase de la descripción de la fuente: NO inventa «por qué importa».

Offline y de solo lectura sobre la entrada. Escribe SIEMPRE a un archivo nuevo.
Nunca llama a ninguna API ni toca noticias.json / noticias.py.

Uso:
  python noticias/filtro_local.py --entrada noticias/noticias.json \
      --salida noticias/salida_filtro_local.json [--dias 7] [--por-dia 6] [--nota-min 7]
La entrada es el JSON del bot (clave «noticias») o una lista de objetos con
titulo_original/titulo, descripcion, fuente, fecha.
"""
import argparse, json, math, re, sys, unicodedata
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import tomllib
except ImportError:  # Python < 3.11
    tomllib = None

AQUI = Path(__file__).resolve().parent

# --- Reglas (derivadas de G17 y del borrador g17; ajustables) ---------------
FUENTES_A = ["federal reserve", "ecb", "bce", "sec.gov", "cftc", "treasury", "eia", "esma", "bis.org",
             "reuters", "bloomberg", "cnbc", "ap news", "financial times", "wsj", "stellar blog"]
PARTE_INTERESADA = ["ripple", "stellar development", "sdf", "21shares", "bitwise", "grayscale", "binance",
                    "coinbase", "kraken", "remittix", "mexc", "changelly"]
PROMO = ["price prediction", "price forecast", "xrp news today", "prediccion de precio", "prediccion del precio",
         "could hit", "to the moon", "will explode", "next 100x", "sponsored", "presale"]
VERBOS_DEBILES = ["propone", "proposes", "proposed", "considera", "considering", "consultation", "consulta",
                  "preliminary", "preliminar", "plans to", "planea", "could", "may ", "might", "seeks"]
VERBOS_FUERTES = ["aprueba", "approves", "approved", "bans", "prohibe", "enacts", "entra en vigor", "sanctions",
                  "sues", "charges", "hacked", "hackeo", "exploit", "ceasefire", "alto el fuego"]
CLAVES_ALTAS = {  # palabra -> peso (hechos concretos de los temas de Joel)
    "xrp": 2, "xlm": 2, "stellar": 2, "ripple": 2, "rlusd": 2, "xrpl": 2, "sec": 2, "cftc": 2, "mica": 2, "esma": 2,
    "ofac": 2, "fatf": 2, "bis": 1, "fsb": 1, "iosco": 1, "stablecoin": 2, "cbdc": 2, "etf": 2,
    "fed": 2, "bce": 2, "ecb": 2, "inflation": 1, "inflacion": 1, "tipos": 1, "rates": 1, "brent": 2, "wti": 2,
    "opec": 2, "opep": 2, "hormuz": 3, "ormuz": 3, "iran": 2, "eia": 2, "brics": 2, "yuan": 1, "ibex": 1,
    "treasury": 1, "oil": 1, "petroleo": 1, "crude": 1, "gold": 1, "oro": 1, "dollar": 1, "dolar": 1,
}
BULO_TOKEN = re.compile(r"\b(xrpl|rlusd|custody|custodia|license|licencia)\b", re.I)

STOP = set("""el la los las un una unos unas de del al y o en con por para que se su sus es son a lo como mas pero sin
the of and to in on for with is are a an at by from as it its be this that after over new says say""".split())


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return s


def tokens(s):
    return [t for t in re.findall(r"[a-z0-9]+", norm(s)) if t not in STOP and len(t) > 1]


def primera_frase(desc, titulo):
    d = (desc or "").strip()
    if not d:
        return ""
    # Google News repite el titular + fuente en la descripción: si no aporta nada, vacío.
    if norm(d)[:60] == norm(titulo)[:60] or set(tokens(d)) <= set(tokens(titulo)) | {"cnbc", "reuters"}:
        return ""
    m = re.split(r"(?<=[.!?])\s+", d, maxsplit=1)
    return m[0][:300]


class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.docs = docs
        self.N = len(docs)
        self.avg = sum(len(d) for d in docs) / max(self.N, 1)
        df = Counter(t for d in docs for t in set(d))
        self.idf = {t: math.log(1 + (self.N - n + 0.5) / (n + 0.5)) for t, n in df.items()}
        self.k1, self.b = k1, b

    def score(self, query, doc):
        tf = Counter(doc)
        s = 0.0
        for q in set(query):
            if q in tf:
                f = tf[q]
                s += self.idf.get(q, 0.0) * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * len(doc) / max(self.avg, 1)))
        return s


def cargar_config():
    cfg = {"temas": [], "intereses": "", "umbral_duplicado": 0.55, "nota_minima": 7,
           "titulos_descartar": [], "dominios_descartar": []}
    p = AQUI / "config.toml"
    if tomllib and p.exists():
        with open(p, "rb") as f:
            cfg.update({k: v for k, v in tomllib.load(f).items() if k in cfg})
    return cfg


def jaccard(a, b):
    a, b = set(a), set(b)
    return len(a & b) / max(len(a | b), 1)


def puntuar(items, cfg, ahora=None):
    consulta = tokens(" ".join(cfg["temas"]) + " " + cfg["intereses"])
    docs = [tokens((i.get("titulo_original") or i.get("titulo", "")) + " " + (i.get("descripcion") or "")) for i in items]
    bm = BM25(docs)
    # normalización de BM25: contra el máximo de la tanda
    bms = [bm.score(consulta, d) for d in docs]
    mx = max(bms) or 1.0
    out = []
    for it, d, b in zip(items, docs, bms):
        tit = it.get("titulo_original") or it.get("titulo", "")
        desc = it.get("descripcion") or ""
        t = norm(tit + " " + desc)
        fuente = norm(it.get("fuente", ""))
        p, razones = 3.0, []
        bmn = b / mx
        p += 3.0 * bmn
        razones.append(f"bm25={bmn:.2f}")
        kw = sum(w for k, w in CLAVES_ALTAS.items() if re.search(r"\b" + k + r"\b", t))
        p += min(kw, 6) * 0.5
        if kw:
            razones.append(f"claves+{min(kw, 6) * 0.5:.1f}")
        if any(a in fuente or a in t[-60:] for a in FUENTES_A):
            p += 1; razones.append("fuente_A")
        if any(x in t for x in PROMO) or any(x in t for x in cfg.get("titulos_descartar", [])):
            p -= 4; razones.append("promo-4")
        if any(x in t for x in PARTE_INTERESADA) and not re.search(r"\b(sec|cftc|reuters|bloomberg|cnbc)\b", t):
            p -= 1; razones.append("parte_interesada-1")
        if any(v in t for v in VERBOS_DEBILES) and any(v in t for v in VERBOS_FUERTES):
            p -= 1; razones.append("verbo_ambiguo-1")
        if BULO_TOKEN.search(t) and not re.search(r"\b(xrp|xlm)\b", t):
            p -= 1; razones.append("no_nombra_token-1")
        if not desc.strip():
            p -= 0.5; razones.append("sin_descripcion")
        f = it.get("fecha")
        if f and ahora:
            try:
                dt = datetime.fromisoformat(f.replace("Z", "+00:00"))
                if ahora - dt > timedelta(days=3):
                    p -= 2; razones.append("vieja-2")
            except ValueError:
                pass
        out.append({"nota": round(max(1.0, min(10.0, p)), 1), "razones": razones, "tokens": d})
    return out


def desduplicar(items, notas, umbral):
    orden = sorted(range(len(items)), key=lambda i: -notas[i]["nota"])
    mantenidos, dup = [], {}
    for i in orden:
        for j in mantenidos:
            if jaccard(notas[i]["tokens"][:12], notas[j]["tokens"][:12]) >= umbral:
                dup[i] = j
                break
        else:
            mantenidos.append(i)
    return dup


def seleccionar(items, cfg, nota_min, por_dia, ahora=None):
    notas = puntuar(items, cfg, ahora)
    dup = desduplicar(items, notas, cfg["umbral_duplicado"])
    por = {}
    res = []
    for i in sorted(range(len(items)), key=lambda i: -notas[i]["nota"]):
        it, n = items[i], notas[i]
        dia = (it.get("fecha") or it.get("fecha_envio") or "")[:10]
        tit = it.get("titulo_original") or it.get("titulo", "")
        ok = n["nota"] >= nota_min and i not in dup and por.get(dia, 0) < por_dia
        if ok:
            por[dia] = por.get(dia, 0) + 1
        res.append({
            "id": it.get("id"), "fuente": it.get("fuente"), "fecha": it.get("fecha"), "tema_bot": it.get("tema"),
            "titulo": tit, "resumen": (tit + " — " + primera_frase(it.get("descripcion"), tit)).strip(" —"),
            "nota_local": n["nota"], "razones": n["razones"], "duplicado_de": items[dup[i]].get("id") if i in dup else None,
            "seleccionada": ok, "url": it.get("url"),
        })
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", default=str(AQUI / "noticias.json"))
    ap.add_argument("--salida", default=str(AQUI / "salida_filtro_local.json"))
    ap.add_argument("--dias", type=int, default=7)
    ap.add_argument("--por-dia", type=int, default=6)
    ap.add_argument("--nota-min", type=float, default=5.0)  # escala propia (no la del bot): sus notas rara vez pasan de 8
    a = ap.parse_args()
    ent, sal = Path(a.entrada).resolve(), Path(a.salida).resolve()
    if ent == sal or sal.name == "noticias.json":
        sys.exit("La salida no puede ser noticias.json")
    data = json.loads(ent.read_text(encoding="utf-8"))
    items = data["noticias"] if isinstance(data, dict) else data
    cfg = cargar_config()
    if a.dias:
        fechas = [(i.get("fecha_envio") or i.get("fecha") or "") for i in items]
        ult = max(f for f in fechas if f)
        lim = (datetime.fromisoformat(ult.replace("Z", "+00:00")) - timedelta(days=a.dias)).isoformat()
        items = [i for i, f in zip(items, fechas) if f >= lim]
    ahora = datetime.now(timezone.utc)
    res = seleccionar(items, cfg, a.nota_min, a.por_dia, None)
    sal.write_text(json.dumps({"generado": ahora.isoformat(), "n_entrada": len(items),
                               "n_seleccionadas": sum(r["seleccionada"] for r in res), "noticias": res},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(items)} entradas -> {sum(r['seleccionada'] for r in res)} seleccionadas. Salida: {sal}")


if __name__ == "__main__":
    main()
