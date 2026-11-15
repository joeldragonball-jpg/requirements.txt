"""C282: indicadores recientes por país sin IA ni claves. OCDE (SDMX: CLI, paro mensual, IPC interanual) y BIS (WS_CBPOL tipo oficial,
WS_CREDIT_GAP brecha crédito/PIB, WS_SPP precios de vivienda reales) para los países de explorador/paises.json [P].
Vuelca explorador/ocde-bis.json con último dato, fecha, fuente y nivel, y compara con indicadores-historia.json (antes/después).
Si una serie falla se conserva el bloque anterior y se anota en «fallos». Certificados verificados. No edita otros archivos.
Uso: python scripts/leer_ocde_bis.py [--seco]"""
import csv
import io
import json
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent / "explorador"
SALIDA = RAIZ / "ocde-bis.json"
OCDE = "https://sdmx.oecd.org/public/rest/data/"
BIS = "https://stats.bis.org/api/v2/data/dataflow/BIS/"
ISO3 = {"ES": "ESP", "DE": "DEU", "FR": "FRA", "IT": "ITA", "NL": "NLD", "PL": "POL", "US": "USA", "CN": "CHN", "JP": "JPN", "IN": "IND",
        "GB": "GBR", "RU": "RUS", "BR": "BRA", "ZA": "ZAF", "ID": "IDN", "EG": "EGY", "ET": "ETH", "IR": "IRN", "AE": "ARE", "SV": "SLV",
        "AR": "ARG", "VE": "VEN", "CU": "CUB"}
EURO = {"ES", "DE", "FR", "IT", "NL"}   # el BIS publica el tipo de la zona euro como XM
OCDE_IND = {
    "cli": ("OECD.SDD.STES,DSD_STES@DF_CLI,4.1", "{p}.M.LI...AA...H", "Indicador adelantado compuesto (CLI, 100 = tendencia)", None),
    "paro_m": ("OECD.SDD.TPS,DSD_LFS@DF_IALFS_UNE_M,1.0", "{p}.UNE_LF_M.PT_LF_SUB._Z.Y._T.Y_GE15._Z.M", "Paro mensual desestacionalizado, 15+ (% pob. activa)", "paro"),
    "ipc_yy": ("OECD.SDD.TPS,DSD_PRICES@DF_PRICES_ALL,1.0", "{p}.M.N.CPI.PA._T.N.GY", "IPC, variación interanual (%)", "ipc"),
}
BIS_IND = {
    "tipo_oficial": ("WS_CBPOL", "M.{p}", "Tipo oficial del banco central (%, fin de mes)", None),
    "brecha_credito": ("WS_CREDIT_GAP", "Q.{p}.P.A.C", "Brecha crédito/PIB (puntos de PIB; sector privado no financiero)", None),
    "vivienda_real": ("WS_SPP", "Q.{p}.R.628", "Precio real de la vivienda (índice, base según país)", None),
}


def bajar(url):
    for n in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.4.0", "Accept": "text/csv"}), timeout=40) as r:
                return r.read().decode("utf-8")
        except Exception as e:
            if n == 2:
                raise
            time.sleep(4)


def ultimos(texto, campo_pais):
    """Último periodo por país (el mayor TIME_PERIOD)."""
    out = {}
    for f in csv.DictReader(io.StringIO(texto)):
        try:
            v = float(f["OBS_VALUE"])
        except (KeyError, ValueError, TypeError):
            continue
        k, t = f[campo_pais], f["TIME_PERIOD"]
        if k not in out or t > out[k][0]:
            out[k] = (t, v)
    return out


def main(seco=False):
    previo = json.loads(SALIDA.read_text(encoding="utf-8")) if SALIDA.exists() else {}
    ant = (previo.get("paises") or {})
    hist = json.loads((RAIZ / "indicadores-historia.json").read_text(encoding="utf-8"))["paises"]
    paises = {p["id"]: p["pais"] for p in json.loads((RAIZ / "paises.json").read_text(encoding="utf-8"))["paises"]}
    res = {i: {} for i in paises}
    fallos = []
    lote3 = "+".join(ISO3[i] for i in paises if i in ISO3)
    for k, (flujo, clave, desc, _) in OCDE_IND.items():
        url = f"{OCDE}{flujo}/{clave.format(p=lote3)}?lastNObservations=1&format=csvfilewithlabels"
        try:
            datos = ultimos(bajar(url), "REF_AREA")
        except Exception as e:
            fallos.append(f"OCDE {k}: {type(e).__name__}")
            datos = {}
        for i in paises:
            if ISO3.get(i) in datos:
                t, v = datos[ISO3[i]]
                res[i][k] = {"serie": desc, "valor": round(v, 2), "fecha": t, "unidad": desc.split("(")[-1].rstrip(")"),
                             "fuente": f"OCDE SDMX {flujo.split(',')[1].split('@')[-1]}: sdmx.oecd.org/public/rest/data/{flujo}", "nivel": "P"}
        time.sleep(1)
    for k, (flujo, clave, desc, _) in BIS_IND.items():
        cods = sorted({("XM" if i in EURO else i) for i in paises}) if k == "tipo_oficial" else sorted(paises)
        url = f"{BIS}{flujo}/1.0/{clave.format(p='+'.join(cods))}?lastNObservations=1&format=csv"
        campo = "BORROWERS_CTY" if k == "brecha_credito" else "REF_AREA"
        try:
            datos = ultimos(bajar(url), campo)
        except Exception as e:
            fallos.append(f"BIS {k}: {type(e).__name__}")
            datos = {}
        for i in paises:
            c = "XM" if (k == "tipo_oficial" and i in EURO) else i
            if c in datos:
                t, v = datos[c]
                d = {"serie": desc, "valor": round(v, 2), "fecha": t, "fuente": f"BIS stats.bis.org/api/v2 {flujo}", "nivel": "P"}
                if c == "XM" and i != "XM":
                    d["nota"] = "tipo del BCE (depósito), común a la zona euro; BIS publica la serie nacional solo hasta 1998"
                res[i][k] = d
        time.sleep(1)
    for i in paises:                                  # conservar lo anterior si ahora falló
        for k, v in (ant.get(i, {}).get("indicadores") or {}).items():
            if k not in res[i] and any(k in f for f in fallos):
                res[i][k] = {**v, "conservado": True}
    comp = []
    for i, nombre in paises.items():
        for k, mapa in (("paro_m", "paro"), ("ipc_yy", "ipc")):
            n = res[i].get(k)
            a = (hist.get(i) or {}).get(mapa, {}).get("hasta")
            if n:
                comp.append({"pais": i, "indicador": mapa, "antes_hasta": a, "ahora_hasta": n["fecha"], "mas_fresco": (a is None) or (n["fecha"] > (a + "-12" if len(a) == 4 else a))})
    out = {"titulo": "OCDE y BIS por país (C282)", "generado": date.today().isoformat(),
           "nota": "Último dato publicado por SDMX de la OCDE y del BIS. Nivel P = leído en la fuente oficial. País sin serie = no la publica ese flujo.",
           "paises": {i: {"pais": paises[i], "indicadores": res[i]} for i in paises}, "comparacion_frescura": comp, "fallos": fallos}
    if not seco:
        SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    n = sum(len(v) for v in res.values())
    print(f"{n} datos en {sum(1 for v in res.values() if v)} países; fallos: {fallos or 'ninguno'}; más frescos que indicadores-historia: {sum(c['mas_fresco'] for c in comp)}/{len(comp)}")


if __name__ == "__main__":
    main("--seco" in sys.argv)
