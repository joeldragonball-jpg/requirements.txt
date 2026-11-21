"""C355: valor tokenizado (RWA) por red, siempre con fecha de lectura. Sin IA ni claves; solo biblioteca estandar.
Fuentes publicas (todas nivel S salvo la comprobacion on-chain de Stellar, [P]):
  1) RWA.xyz: las paginas publicas /networks y /networks/<red> son SSG de Next.js y traen sus datos en __NEXT_DATA__ (sin login).
     La API api.rwa.xyz exige clave (401), por eso se lee la pagina, igual que un navegador. Es fragil: si RWA.xyz cambia la
     estructura, el bloque falla y se conserva la lectura anterior.
  2) DefiLlama api.llama.fi/protocols (categoria RWA): mide valor bloqueado en DeFi, NO lo tokenizado total.
  3) Stellar Horizon (horizon.stellar.org): oferta on-chain de BENJI con el emisor verificado por su home_domain.
Si una fuente falla se conserva el bloque anterior del archivo (con su fecha de lectura vieja) y el script sale con codigo 1.
Salida: explorador/tokenizado.json"""
import gzip, json, re, sys, time, urllib.request, datetime, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "tokenizado.json"
CADUCA_DIAS = 14
UA = {"User-Agent": "Mozilla/5.0 (cartera-lector/1.0; lectura publica semanal)", "Accept-Encoding": "gzip"}
HOY = datetime.date.today().isoformat()
CADUCA = (datetime.date.today() + datetime.timedelta(days=CADUCA_DIAS)).isoformat()

# id de cadenas.json -> (nombre en RWA.xyz, nombre en DefiLlama /protocols chainTvls)
REDES = {
    "ethereum": ("Ethereum", "Ethereum"), "solana": ("Solana", "Solana"), "stellar": ("Stellar", "Stellar"),
    "xrpl": ("XRP Ledger", "XRPL"), "avalanche": ("Avalanche", "Avalanche"), "polygon": ("Polygon", "Polygon"),
    "bnb": ("BNB Chain", "BSC"), "hedera": ("Hedera", "Hedera"), "canton": ("Canton", "Canton"),
    "plume": ("Plume", "Plume Mainnet"), "algorand": ("Algorand", "Algorand"),
}
TRAMPA_RWAXYZ = ("«Distribuido» = emitido y transferible en la red; «representado» = solo registrado en ella (no transferible ni liquidado). "
                 "RWA.xyz reclasifica entre lecturas (XRPL 14-nov a 19-nov: no fue flujo de dinero). Es un tercero comercial sin auditoria. "
                 "Las tablas por plataforma/gestora de cada red INCLUYEN stablecoins (Circle, Tether, Paxos...); las cifras de red las excluyen. "
                 "El campo «value_7d_ago» de la pagina coincide con el valor de hace 30 dias (comprobado con el cambio a 30 d de Stellar), no de 7.")
TRAMPA_DEFI = ("Solo el valor bloqueado en protocolos DeFi de categoria RWA de DefiLlama; no incluye BENJI, Ondo, Spiko ni la mayor parte "
               "de lo tokenizado. Stellar ~7 M$ frente a ~4.900 M$ distribuidos en RWA.xyz no es contradiccion: miden cosas distintas.")


def esperar():
    time.sleep(1.0)


def get(url, binario=False):
    rq = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(rq, timeout=60) as r:
        datos = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            datos = gzip.decompress(datos)
    return datos if binario else datos.decode("utf-8", "replace")


def next_data(url):
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', get(url), re.S)
    if not m:
        raise ValueError("sin __NEXT_DATA__ en " + url)
    return json.loads(m.group(1))["props"]["pageProps"]


def m_(x):
    return None if x is None else round(float(x) / 1e6, 1)


def tabla(pp, clave, tipo):
    """filas de una tabla de ligas: pp['leagueTableTabs'][tipo] con key == clave."""
    for t in pp["leagueTableTabs"].get(tipo, []):
        if t.get("key") == clave:
            return t["data"]["rows"]
    return []


def filas(rows, n=6):
    out = []
    for r in rows[:n]:
        v = r.get("value")
        if v is None:
            continue
        out.append({"nombre": r["group"]["name"].strip(), "musd": m_(v), "hace_30d_musd": m_(r.get("value_7d_ago"))})
    return out


def leer_rwaxyz():
    """Devuelve {id: bloque}. Lanza excepcion si falla la pagina general."""
    gen = next_data("https://app.rwa.xyz/networks")
    ag = {a["label"]: a for a in gen["aggregates"]}
    filas_gen = gen["leagueTableTabsWithoutStablecoins"]["distributed"][0]["data"]["rows"]
    rep_gen = {r["group"]["name"]: r for r in gen["leagueTableTabsWithoutStablecoins"]["represented"][0]["data"]["rows"]}
    dist_gen = {r["group"]["name"]: r for r in filas_gen}
    total = {
        "distribuido_musd": m_(ag["Distributed Asset Value"]["value"]),
        "distribuido_cambio_30d_pct": round(float(ag["Distributed Asset Value"]["percentChange"]["value"]) * 100, 1),
        "representado_musd": m_(ag["Represented Asset Value"]["value"]),
        "representado_cambio_30d_pct": round(float(ag["Represented Asset Value"]["percentChange"]["value"]) * 100, 1),
        "stablecoins_musd": m_(ag["Stablecoin Value"]["value"]), "redes": ag["Total Networks"]["value"],
    }
    res = {}
    for rid, (nom, _dl) in REDES.items():
        fila = dist_gen.get(nom) or rep_gen.get(nom)
        if not fila:
            continue
        href = fila["group"]["linkTo"]["href"]
        d = dist_gen.get(nom)
        r = rep_gen.get(nom)
        b = {
            "distribuido_musd": m_(d["value"]) if d else 0.0,
            "distribuido_hace_30d_musd": m_(d.get("value_7d_ago")) if d else None,
            "representado_musd": m_(r["value"]) if r else 0.0,
            "activos_distribuidos": d.get("asset_count") if d else None,
            "pagina": "https://app.rwa.xyz" + href,
        }
        if d and b["distribuido_hace_30d_musd"]:
            b["distribuido_cambio_30d_pct"] = round((b["distribuido_musd"] / b["distribuido_hace_30d_musd"] - 1) * 100, 1)
        esperar()
        try:  # detalle por red: plataformas (emisores), clases de activo; si falla solo se omite el detalle
            pp = next_data("https://app.rwa.xyz" + href)
            det = {a["label"]: a for a in pp.get("aggregates", [])}
            if "RWA Holders" in det:
                b["titulares"] = det["RWA Holders"]["value"]
            if "RWA Count" in det:
                b["activos_rwa"] = det["RWA Count"]["value"]
            b["top_plataformas"] = filas(tabla(pp, "platforms", "distributed"))
            b["top_gestoras"] = filas(tabla(pp, "managers", "distributed"))
            b["clases_activo"] = filas(tabla(pp, "asset_classes", "distributed"), 8)
        except Exception as e:
            print("aviso: detalle", rid, type(e).__name__, str(e)[:80], file=sys.stderr)
            b["detalle_error"] = True
        res[rid] = b
    return total, res


def leer_defillama():
    prot = json.loads(get("https://api.llama.fi/protocols"))
    rwa = [p for p in prot if p.get("category") == "RWA"]
    out = {}
    for rid, (_n, dl) in REDES.items():
        lst = sorted(((p["chainTvls"].get(dl, 0), p["name"]) for p in rwa if p.get("chainTvls", {}).get(dl)), reverse=True)
        out[rid] = {"rwa_defi_musd": round(sum(v for v, _ in lst) / 1e6, 1), "protocolos": len(lst),
                    "top": [{"nombre": n, "musd": round(v / 1e6, 1)} for v, n in lst[:3]]}
    return len(rwa), out


def leer_horizon_benji():
    """Oferta on-chain de BENJI (Franklin Templeton) en Stellar. El emisor se acepta solo si su home_domain es franklintempleton.com:
    en Horizon hay decenas de activos BENJI falsos con emisores que imitan a marcas (comprobado 21-nov-2026)."""
    emisor = "GBHNGLLIE3KWGKCHIKMHJ5HVZHYIK7WTBE4QF5PLAKL4CJGSEU7HZIW5"
    cuenta = json.loads(get("https://horizon.stellar.org/accounts/" + emisor))
    if cuenta.get("home_domain") != "www.franklintempleton.com":
        raise ValueError("home_domain inesperado: %s" % cuenta.get("home_domain"))
    a = json.loads(get("https://horizon.stellar.org/assets?asset_code=BENJI&asset_issuer=" + emisor))["_embedded"]["records"][0]
    return {"unidades": round(float(a["balances"]["authorized"]), 1), "cuentas": a["accounts"]["authorized"], "emisor": emisor}


def previo():
    try:
        return json.loads(SALIDA.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main():
    ant = previo()
    ant_r = {r["id"]: r for r in ant.get("redes", [])}
    estado, fallos = {}, 0
    tot = ant.get("totales_rwaxyz")
    rx, dl, bj, n_dl = {}, {}, None, None
    for nombre, f in (("rwaxyz", leer_rwaxyz), ("defillama", leer_defillama), ("horizon_benji", leer_horizon_benji)):
        try:
            r = f()
            estado[nombre] = {"estado": "ok", "leido": HOY}
            if nombre == "rwaxyz":
                tot, rx = r
            elif nombre == "defillama":
                n_dl, dl = r
            else:
                bj = r
        except Exception as e:
            fallos += 1
            estado[nombre] = {"estado": "fallo: %s %s" % (type(e).__name__, str(e)[:80]),
                              "leido": (ant.get("fuentes", {}).get(nombre) or {}).get("leido")}
            print("aviso:", nombre, estado[nombre]["estado"], file=sys.stderr)
        esperar()
    redes = []
    for rid, (nom, dln) in REDES.items():
        viejo = ant_r.get(rid, {})
        fila = {"id": rid, "red": nom}
        for clave, datos, trampa, fuente, url in (
                ("rwaxyz", rx.get(rid), TRAMPA_RWAXYZ, "RWA.xyz, Networks (pagina publica, sin login)", "https://app.rwa.xyz/networks"),
                ("defillama", dl.get(rid), TRAMPA_DEFI, "DefiLlama api.llama.fi/protocols, categoria RWA", "https://defillama.com/categories/RWA")):
            if datos is not None:
                fila[clave] = dict(datos, unidad="M$", fuente=fuente, u=url, nivel="S", leido=HOY, caduca=CADUCA, trampa=trampa)
            elif viejo.get(clave):
                fila[clave] = viejo[clave]  # se conserva la lectura anterior con su fecha vieja
        if rid == "stellar":
            if bj:
                fila["primaria"] = {"activo": "BENJI (Franklin Templeton)", "unidades_en_cadena": bj["unidades"], "cuentas": bj["cuentas"],
                                    "unidad": "unidades de BENJI (NAV ~1 $ por unidad [VERIFICAR])", "emisor": bj["emisor"],
                                    "fuente": "Horizon horizon.stellar.org, emisor con home_domain franklintempleton.com",
                                    "u": "https://horizon.stellar.org/assets?asset_code=BENJI&asset_issuer=" + bj["emisor"],
                                    "nivel": "P", "leido": HOY, "caduca": CADUCA,
                                    "trampa": "Hay decenas de activos «BENJI» falsos con otros emisores en Horizon; solo vale el emisor verificado."}
            elif viejo.get("primaria"):
                fila["primaria"] = viejo["primaria"]
        if len(fila) > 2:
            redes.append(fila)
    salida = {
        "_leido": HOY, "version": 1, "caduca_dias": CADUCA_DIAS,
        "nota": "Valor tokenizado por red (M$ = millones de dolares), con fecha de lectura (`leido`) y `caduca`. RWA.xyz es tercero comercial sin "
                "auditoria [S]. No sumar «distribuido» con «representado». Lo regenera scripts/leer_tokenizado.py (paneles.yml, semanal).",
        "fuentes": estado, "totales_rwaxyz": tot, "defillama_protocolos_rwa": n_dl or ant.get("defillama_protocolos_rwa"), "redes": redes,
    }
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("tokenizado.json: %d redes; fallos de fuente: %d %s" % (len(redes), fallos, {k: v["estado"][:2] for k, v in estado.items()}))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
