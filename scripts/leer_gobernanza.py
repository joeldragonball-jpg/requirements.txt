"""C297 · Gobernanza y releases por red: enmiendas XRPL (método feature, nodo s1.ripple.com) y releases oficiales de los repos
núcleo (solo feeds releases.atom: sin API REST de GitHub, por su límite de 60 peticiones/h). Sin IA, sin claves, stdlib.
Nivel P: enmiendas (nodo directo). Nivel S: releases (el feed es de GitHub, tercero; la etiqueta la pone el equipo del repo).
Filtra etiquetas no oficiales (custom, rc, beta, alpha, nightly...) y las lista aparte como «preliminares».
No sobrescribe el JSON si todo falla. Uso: python scripts/leer_gobernanza.py"""
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "cadenas-gobernanza.json"
NODO = "https://s1.ripple.com:51234/"
REPOS = {"xrpl": ["XRPLF/rippled"], "stellar": ["stellar/stellar-core"], "ethereum": ["ethereum/go-ethereum", "prysmaticlabs/prysm"],
         "solana": ["anza-xyz/agave"], "hedera": ["hashgraph/hedera-services"], "avalanche": ["ava-labs/avalanchego"],
         "algorand": ["algorand/go-algorand"], "iota": ["iotaledger/iota"], "xdc": ["XinFinOrg/XDPoSChain"],
         "bnb": ["bnb-chain/bsc"], "polygon": ["0xPolygon/bor"]}
NO_OFICIAL = re.compile(r"custom|candidate|testnet|devnet|xts|[-_.]?(rc|beta|alpha|nightly|dev|pre|test|snapshot|canary)[-_.0-9]|[-_](rc|b|beta|alpha)\d*$", re.I)
NS = {"a": "http://www.w3.org/2005/Atom"}


def reintentar(f, n=3):
    ult = None
    for i in range(n):
        try:
            return f()
        except Exception as e:
            ult = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{type(ult).__name__}: {ult}")


def enmiendas():
    def go():
        cuerpo = json.dumps({"method": "feature"}).encode()
        req = urllib.request.Request(NODO, data=cuerpo, headers={"Content-Type": "application/json", "User-Agent": "cartera-bot"})
        r = json.load(urllib.request.urlopen(req, timeout=40))["result"]
        if r.get("status") != "success":
            raise RuntimeError(r.get("error_message") or r.get("error"))
        return r["features"]
    f = reintentar(go)
    act, vot, vet, obs = [], [], [], 0
    for h, v in f.items():
        nom = v.get("name") or h[:8]
        if v.get("enabled"):
            act.append(nom)
        elif v.get("vetoed") == "Obsolete":
            obs += 1
        elif v.get("vetoed"):
            vet.append(nom)
        else:
            e = {"nombre": nom, "soportada_por_nodo": v.get("supported")}
            if "count" in v:
                e["votos"] = v.get("count")
                e["umbral"] = v.get("threshold")
            vot.append(e)
    return {"nivel": "P", "fuente": NODO + " (método feature)", "conocidas": len(f), "activadas": len(act),
            "pendientes_votando": sorted(vot, key=lambda x: x["nombre"]), "vetadas_por_este_nodo": sorted(vet), "obsoletas": obs,
            "nota": "«Pendientes» = no activadas ni vetadas; la lista puede incluir enmiendas aún no soportadas. El veto es de este nodo (Ripple), no de la red. [VERIFICAR] estado en xrpl.org/resources/known-amendments."}


def release_feed(repo):
    def go():
        req = urllib.request.Request(f"https://github.com/{repo}/releases.atom", headers={"User-Agent": "cartera-bot"})
        return urllib.request.urlopen(req, timeout=40).read()
    raiz = ET.fromstring(reintentar(go))
    oficiales, prelim = [], []
    for e in raiz.findall("a:entry", NS):
        titulo = (e.findtext("a:title", "", NS) or "").strip()
        link = e.find("a:link", NS)
        tag = (link.get("href") if link is not None else "").rsplit("/", 1)[-1]
        item = {"version": titulo or tag, "etiqueta": tag, "fecha": (e.findtext("a:updated", "", NS) or "")[:10],
                "enlace": link.get("href") if link is not None else None}
        (prelim if NO_OFICIAL.search(tag) or NO_OFICIAL.search(titulo) else oficiales).append(item)
    return {"repo": repo, "ultima_oficial": oficiales[0] if oficiales else None, "oficiales_recientes": oficiales[:5],
            "preliminares_no_contados": [p["etiqueta"] for p in prelim[:5]]}


def main():
    ahora = datetime.now(timezone.utc)
    fallos, redes = [], {}
    try:
        redes["xrpl"] = {"enmiendas": enmiendas()}
    except Exception as e:
        fallos.append({"que": "enmiendas XRPL", "error": str(e)[:200]})
    for red, repos in REPOS.items():
        for repo in repos:
            try:
                redes.setdefault(red, {}).setdefault("releases", []).append(release_feed(repo))
            except Exception as e:
                fallos.append({"que": repo, "error": str(e)[:200]})
    if not redes:
        print("Todo falló: no se sobrescribe el JSON.", file=sys.stderr)
        return 1
    if SALIDA.exists():  # conservar lo bueno anterior de lo que falle hoy
        try:
            ant = json.loads(SALIDA.read_text(encoding="utf-8")).get("redes", {})
            for red, v in ant.items():
                if red not in redes:
                    redes[red] = dict(v, obsoleto=True)
                else:
                    for k, val in v.items():
                        if k not in redes[red]:
                            redes[red][k] = val
                            redes[red]["obsoleto"] = True
        except Exception:
            pass
    out = {"generado_utc": ahora.strftime("%Y-%m-%d %H:%M UTC"),
           "metodo": "Enmiendas: POST JSON-RPC «feature» a un nodo público (P). Releases: releases.atom de GitHub (S), sin API REST; se separan etiquetas no oficiales por patrón (custom, rc, beta, alpha, nightly...). Reintentos x3.",
           "avisos": ["Un feed de releases dice qué publica el equipo, no cuántos validadores han actualizado.",
                      "El filtro de etiquetas es heurístico: [VERIFICAR] si una versión oficial aparece como preliminar o al revés.",
                      "La fecha es la de actualización del feed, que puede diferir de la de publicación."],
           "fallos": fallos, "redes": redes}
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {len(redes)} redes, {len(fallos)} fallos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
