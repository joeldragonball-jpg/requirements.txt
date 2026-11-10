"""C240 · Auditoría local (sin IA) de unidades y separadores en los JSON de España y afines.
Uso: python scripts/auditar_unidades.py [--todo] [-n 40]
Detecta: (1) cifras de miles con punto («1.234») en texto sin unidad cerca (M€, mil M€, €, %, M$…);
(2) separadores ambiguos («1,234.5» formato inglés); (3) archivos con campos numéricos y sin 'unidad'/'escala';
(4) escalas mezcladas (M€ y «mil M€» en el mismo texto)."""
import json, re, sys, glob, os
sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNI = r"(?:mil\s+M€|M€|M\$|mil\s+M\$|€|\$|%|euros|millones|miles|hab|años|mm|km|MW|GWh|t\b|barcos|puntos|pb)"
MILES = re.compile(r"(?<![\d.,/-])(\d{1,3}(?:\.\d{3})+)(?!\d|\.\d|,\d)(?!\s*" + UNI + ")")
INGLES = re.compile(r"(?<![\d.,])\d{1,3}(?:,\d{3})+\.\d+")
FECHA_ISO = re.compile(r"\d{4}\.\d{3}")  # p. ej. 2026.123 (ids), no es cifra

def textos(o, ruta=""):
    if isinstance(o, dict):
        for k, v in o.items(): yield from textos(v, f"{ruta}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from textos(v, f"{ruta}[{i}]")
    elif isinstance(o, str): yield ruta, o

def tiene_num(o):
    if isinstance(o, dict): return any(tiene_num(v) for v in o.values())
    if isinstance(o, list): return any(tiene_num(v) for v in o[:50])
    return isinstance(o, (int, float)) and not isinstance(o, bool)

def main():
    n = int(sys.argv[sys.argv.index("-n") + 1]) if "-n" in sys.argv else 40
    pat = "explorador/*.json" if "--todo" in sys.argv else "explorador/espana*.json"
    tot = {"sin_unidad": 0, "ingles": 0, "mezcla": 0, "sin_campo_unidad": 0}
    for f in sorted(glob.glob(os.path.join(RAIZ, pat))):
        try: d = json.load(open(f, encoding="utf-8"))
        except Exception as e: print(f"[ERROR] {f}: {e}"); continue
        nom = os.path.relpath(f, RAIZ).replace("\\", "/")
        if isinstance(d, dict) and tiene_num(d) and not any(k in d for k in ("unidad", "unidades", "escala")):
            tot["sin_campo_unidad"] += 1; print(f"[SIN-CAMPO-UNIDAD] {nom}: tiene números y no declara 'unidad'/'escala' en la raíz")
        mostrados = 0
        for r, t in textos(d):
            if re.search(r"mil\s+M€", t) and re.search(r"(?<!mil )M€", t) and re.search(r"\d\s+mil\s+M€", t) and re.search(r"\d\s+M€", t):
                tot["mezcla"] += 1
            for m in INGLES.finditer(t):
                tot["ingles"] += 1
                if mostrados < n: print(f"[INGLÉS] {nom}{r}: …{t[max(0,m.start()-30):m.end()+20]}…"); mostrados += 1
            for m in MILES.finditer(t):
                if FECHA_ISO.match(m.group(1)) or t.startswith("http"): continue
                tot["sin_unidad"] += 1
                if mostrados < n: print(f"[SIN-UNIDAD] {nom}{r}: …{t[max(0,m.start()-30):m.end()+25]}…"); mostrados += 1
    print("\nResumen:", tot)
main()
